"""Workflow engine for orchestrating the AI-driven development workflow."""
import logging
from datetime import datetime
from typing import Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Project
from app.services.langfuse_service import LangFuseTracker, is_langfuse_enabled
from app.workflow.document_storage import save_document
from app.workflow.phases.base import PhaseResult
from app.workflow.phases.event_storming import EventStormingPhase
from app.workflow.phases.execution_plan import ExecutionPlanPhase
from app.workflow.phases.prd_generation import PRDGenerationPhase
from app.workflow.phases.smart_detection import SmartDetectionPhase
from app.workflow.phases.tech_stack import TechStackPhase
from app.workflow.state_machine import (
    DocumentType,
    WorkflowPhase,
    WorkflowStateMachine,
    WorkflowStatus,
)

logger = logging.getLogger(__name__)


class WorkflowEngine:
    """Main workflow engine for orchestrating all phases."""

    def __init__(self, db: AsyncSession, project_id: UUID):
        """Initialize workflow engine.

        Args:
            db: Database session
            project_id: Project UUID

        """
        self.db = db
        self.project_id = project_id
        self.tracker: Optional[LangFuseTracker] = None

    async def _get_project(self) -> Project:
        """Get project from database.

        Returns:
            Project

        Raises:
            ValueError: If project not found

        """
        result = await self.db.execute(
            select(Project).where(Project.id == self.project_id)
        )
        project = result.scalar_one_or_none()
        if not project:
            raise ValueError(f"Project {self.project_id} not found")
        return project

    async def _update_project_status(
        self,
        status: WorkflowStatus,
        current_phase: Optional[WorkflowPhase] = None,
        metadata: Optional[dict] = None,
    ) -> None:
        """Update project status.

        Args:
            status: New workflow status
            current_phase: Optional current phase
            metadata: Optional metadata to merge

        """
        project = await self._get_project()
        project.status = status.value
        project.current_phase = current_phase.value if current_phase else None
        project.updated_at = datetime.utcnow()

        if status == WorkflowStatus.COMPLETED:
            project.completed_at = datetime.utcnow()

        if metadata:
            project.metadata = {**project.metadata, **metadata}

        await self.db.commit()

    async def execute_workflow(self) -> bool:
        """Execute the complete workflow.

        Returns:
            True if workflow completed successfully, False otherwise

        """
        try:
            # Get project
            project = await self._get_project()

            # Initialize LangFuse tracker if enabled
            if is_langfuse_enabled():
                self.tracker = LangFuseTracker(self.project_id, project.idea)
                self.tracker.track_event("workflow_started")

            # Update status to processing
            await self._update_project_status(
                WorkflowStatus.PROCESSING,
                WorkflowPhase.SMART_DETECTION,
            )

            logger.info(f"Starting workflow for project {self.project_id}")

            # Phase 0: Smart Detection
            smart_detection_result = await self._run_smart_detection(project.idea)
            if not smart_detection_result.success:
                await self._handle_workflow_failure(smart_detection_result.error_message)
                return False

            use_event_storming = smart_detection_result.output_data.get("use_event_storming", False)

            # Store smart detection results in project metadata
            await self._update_project_status(
                WorkflowStatus.PROCESSING,
                WorkflowPhase.SMART_DETECTION,
                metadata={"smart_detection": smart_detection_result.output_data},
            )

            # Phase 0.5: Event Storming (conditional)
            event_storming_summary = None
            if use_event_storming:
                await self._update_project_status(
                    WorkflowStatus.PROCESSING,
                    WorkflowPhase.EVENT_STORMING,
                )

                event_storming_result = await self._run_event_storming(project.idea)
                if not event_storming_result.success:
                    await self._handle_workflow_failure(event_storming_result.error_message)
                    return False

                event_storming_summary = event_storming_result.output_data.get("event_storming_md")

                # Save Event Storming document
                await save_document(
                    self.db,
                    self.project_id,
                    DocumentType.EVENT_STORMING,
                    event_storming_summary,
                    metadata={"model": event_storming_result.llm_response.model if event_storming_result.llm_response else None},
                )

            # Phase 1-2: PRD Generation
            await self._update_project_status(
                WorkflowStatus.PROCESSING,
                WorkflowPhase.PRD,
            )

            prd_result = await self._run_prd_generation(project.idea, event_storming_summary)
            if not prd_result.success:
                await self._handle_workflow_failure(prd_result.error_message)
                return False

            prd_md = prd_result.output_data.get("prd_md")

            # Save PRD document
            await save_document(
                self.db,
                self.project_id,
                DocumentType.PRD,
                prd_md,
                metadata={"model": prd_result.llm_response.model if prd_result.llm_response else None},
            )

            # Phase 3: Tech Stack
            await self._update_project_status(
                WorkflowStatus.PROCESSING,
                WorkflowPhase.TECH_STACK,
            )

            tech_stack_result = await self._run_tech_stack(prd_md)
            if not tech_stack_result.success:
                await self._handle_workflow_failure(tech_stack_result.error_message)
                return False

            tech_stack_md = tech_stack_result.output_data.get("tech_stack_md")

            # Save Tech Stack document
            await save_document(
                self.db,
                self.project_id,
                DocumentType.TECH_STACK,
                tech_stack_md,
                metadata={"model": tech_stack_result.llm_response.model if tech_stack_result.llm_response else None},
            )

            # Phase 4: Execution Plan
            await self._update_project_status(
                WorkflowStatus.PROCESSING,
                WorkflowPhase.EXECUTION_PLAN,
            )

            execution_plan_result = await self._run_execution_plan(prd_md, tech_stack_md)
            if not execution_plan_result.success:
                await self._handle_workflow_failure(execution_plan_result.error_message)
                return False

            execution_plan_md = execution_plan_result.output_data.get("execution_plan_md")
            approach = execution_plan_result.output_data.get("approach", "HORIZONTAL")

            # Save Execution Plan document
            await save_document(
                self.db,
                self.project_id,
                DocumentType.EXECUTION_PLAN,
                execution_plan_md,
                metadata={
                    "model": execution_plan_result.llm_response.model if execution_plan_result.llm_response else None,
                    "approach": approach,
                },
            )

            # Calculate total cost and duration
            total_cost, total_duration = await self._calculate_totals()

            # Update project with final metadata
            await self._update_project_status(
                WorkflowStatus.COMPLETED,
                WorkflowPhase.EXECUTION_PLAN,
                metadata={
                    "use_event_storming": use_event_storming,
                    "use_vertical_approach": approach == "VERTICAL",
                    "total_cost_usd": total_cost,
                    "total_duration_seconds": total_duration,
                },
            )

            # Finalize LangFuse trace
            if self.tracker:
                documents_generated = 4 if use_event_storming else 3
                self.tracker.finalize(
                    total_cost=total_cost,
                    total_duration_seconds=total_duration,
                    status="completed",
                    documents_generated=documents_generated,
                )

            logger.info(f"Workflow completed successfully for project {self.project_id}")
            return True

        except Exception as e:
            logger.error(f"Workflow failed for project {self.project_id}: {e}", exc_info=True)
            await self._handle_workflow_failure(str(e))
            return False

    async def _run_smart_detection(self, idea: str) -> PhaseResult:
        """Run smart detection phase."""
        handler = SmartDetectionPhase(self.db, self.project_id, self.tracker)
        return await handler.run_with_state_tracking({"idea": idea})

    async def _run_event_storming(self, idea: str) -> PhaseResult:
        """Run Event Storming phase."""
        handler = EventStormingPhase(self.db, self.project_id, self.tracker)
        return await handler.run_with_state_tracking({"idea": idea})

    async def _run_prd_generation(
        self, idea: str, event_storming_summary: Optional[str]
    ) -> PhaseResult:
        """Run PRD generation phase."""
        handler = PRDGenerationPhase(self.db, self.project_id, self.tracker)
        input_data = {"idea": idea}
        if event_storming_summary:
            input_data["event_storming_summary"] = event_storming_summary
        return await handler.run_with_state_tracking(input_data)

    async def _run_tech_stack(self, prd_md: str) -> PhaseResult:
        """Run Tech Stack phase."""
        handler = TechStackPhase(self.db, self.project_id, self.tracker)
        return await handler.run_with_state_tracking({"prd_md": prd_md})

    async def _run_execution_plan(self, prd_md: str, tech_stack_md: str) -> PhaseResult:
        """Run Execution Plan phase."""
        handler = ExecutionPlanPhase(self.db, self.project_id, self.tracker)
        return await handler.run_with_state_tracking({
            "prd_md": prd_md,
            "tech_stack_md": tech_stack_md,
        })

    async def _calculate_totals(self) -> tuple[float, int]:
        """Calculate total cost and duration from LLM logs.

        Returns:
            Tuple of (total_cost_usd, total_duration_seconds)

        """
        from app.db.models import LLMLog
        from sqlalchemy import func

        result = await self.db.execute(
            select(
                func.sum(LLMLog.cost_usd),
                func.sum(LLMLog.latency_ms),
            ).where(LLMLog.project_id == self.project_id)
        )

        row = result.one()
        total_cost = float(row[0] or 0.0)
        total_latency_ms = int(row[1] or 0)
        total_duration_seconds = total_latency_ms // 1000

        return total_cost, total_duration_seconds

    async def _handle_workflow_failure(self, error_message: Optional[str]) -> None:
        """Handle workflow failure.

        Args:
            error_message: Error message

        """
        await self._update_project_status(
            WorkflowStatus.FAILED,
            metadata={"error": error_message},
        )

        if self.tracker:
            self.tracker.track_event(
                "workflow_failed",
                metadata={"error": error_message},
            )

        logger.error(f"Workflow failed for project {self.project_id}: {error_message}")
