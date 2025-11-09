"""Base class for workflow phase handlers."""
import json
from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import LLMLog, WorkflowState
from app.services.langfuse_service import LangFuseTracker, is_langfuse_enabled
from app.services.llm_service import LLMResponse, llm_service
from app.workflow.state_machine import PhaseStatus, WorkflowPhase


class PhaseResult:
    """Result from a phase execution."""

    def __init__(
        self,
        phase: WorkflowPhase,
        success: bool,
        output_data: Dict[str, Any],
        error_message: Optional[str] = None,
        llm_response: Optional[LLMResponse] = None,
    ):
        self.phase = phase
        self.success = success
        self.output_data = output_data
        self.error_message = error_message
        self.llm_response = llm_response


class BasePhaseHandler(ABC):
    """Base class for all phase handlers."""

    def __init__(
        self,
        db: AsyncSession,
        project_id: UUID,
        tracker: Optional[LangFuseTracker] = None,
    ):
        """Initialize phase handler.

        Args:
            db: Database session
            project_id: Project UUID
            tracker: Optional LangFuse tracker

        """
        self.db = db
        self.project_id = project_id
        self.tracker = tracker

    @abstractmethod
    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute the phase.

        Args:
            input_data: Input data for this phase

        Returns:
            PhaseResult with output data

        """
        pass

    @abstractmethod
    def get_phase_name(self) -> WorkflowPhase:
        """Get the phase name.

        Returns:
            WorkflowPhase enum value

        """
        pass

    async def create_workflow_state(
        self, input_data: Dict[str, Any]
    ) -> WorkflowState:
        """Create a workflow state record for this phase.

        Args:
            input_data: Input data for this phase

        Returns:
            Created WorkflowState

        """
        workflow_state = WorkflowState(
            project_id=self.project_id,
            phase=self.get_phase_name().value,
            status=PhaseStatus.IN_PROGRESS.value,
            input_data=input_data,
            started_at=datetime.utcnow(),
        )
        self.db.add(workflow_state)
        await self.db.commit()
        await self.db.refresh(workflow_state)
        return workflow_state

    async def update_workflow_state(
        self,
        workflow_state: WorkflowState,
        status: PhaseStatus,
        output_data: Optional[Dict[str, Any]] = None,
        error_message: Optional[str] = None,
    ) -> None:
        """Update workflow state.

        Args:
            workflow_state: WorkflowState to update
            status: New status
            output_data: Optional output data
            error_message: Optional error message

        """
        workflow_state.status = status.value
        workflow_state.output_data = output_data
        workflow_state.error_message = error_message
        workflow_state.completed_at = datetime.utcnow()

        await self.db.commit()

    async def save_llm_log(
        self,
        workflow_state_id: UUID,
        phase: str,
        llm_response: LLMResponse,
        langfuse_trace_id: Optional[str] = None,
    ) -> None:
        """Save LLM log to database.

        Args:
            workflow_state_id: WorkflowState UUID
            phase: Phase name
            llm_response: LLM response with usage data
            langfuse_trace_id: Optional LangFuse trace ID

        """
        llm_log = LLMLog(
            project_id=self.project_id,
            workflow_state_id=workflow_state_id,
            phase=phase,
            model=llm_response.model,
            langfuse_trace_id=langfuse_trace_id,
            prompt_tokens=llm_response.usage["prompt_tokens"],
            completion_tokens=llm_response.usage["completion_tokens"],
            total_tokens=llm_response.usage["total_tokens"],
            cost_usd=llm_response.cost_usd,
            latency_ms=llm_response.latency_ms,
        )
        self.db.add(llm_log)
        await self.db.commit()

    async def call_llm(
        self,
        model: str,
        prompt: str,
        temperature: float = 0.7,
        max_tokens: int = 4000,
        response_format: Optional[Dict[str, str]] = None,
        system_message: Optional[str] = None,
    ) -> LLMResponse:
        """Call LLM and handle errors.

        Args:
            model: Model identifier
            prompt: User prompt
            temperature: Sampling temperature
            max_tokens: Maximum tokens
            response_format: Optional response format
            system_message: Optional system message

        Returns:
            LLMResponse

        Raises:
            Exception: If LLM call fails

        """
        return await llm_service.call(
            model=model,
            prompt=prompt,
            temperature=temperature,
            max_tokens=max_tokens,
            response_format=response_format,
            system_message=system_message,
        )

    def track_phase_in_langfuse(
        self,
        phase_name: str,
        model: str,
        input_data: Dict[str, Any],
        output_data: Dict[str, Any],
        llm_response: LLMResponse,
        status: str = "completed",
        error: Optional[str] = None,
    ) -> Optional[str]:
        """Track phase execution in LangFuse.

        Args:
            phase_name: Name of the phase
            model: Model used
            input_data: Input to LLM
            output_data: Output from LLM
            llm_response: LLM response with usage
            status: Status ("completed" or "failed")
            error: Optional error message

        Returns:
            LangFuse trace ID or None

        """
        if not self.tracker or not is_langfuse_enabled():
            return None

        return self.tracker.track_phase(
            phase_name=phase_name,
            model=model,
            input_data=input_data,
            output_data=output_data,
            tokens=llm_response.usage,
            cost=llm_response.cost_usd,
            duration_ms=llm_response.latency_ms,
            status=status,
            error=error,
        )

    async def run_with_state_tracking(
        self, input_data: Dict[str, Any]
    ) -> PhaseResult:
        """Run the phase with automatic state tracking.

        Args:
            input_data: Input data for this phase

        Returns:
            PhaseResult

        """
        # Create workflow state
        workflow_state = await self.create_workflow_state(input_data)

        try:
            # Execute phase
            result = await self.execute(input_data)

            # Update workflow state
            await self.update_workflow_state(
                workflow_state,
                PhaseStatus.COMPLETED if result.success else PhaseStatus.FAILED,
                output_data=result.output_data,
                error_message=result.error_message,
            )

            # Save LLM log if available
            if result.llm_response:
                langfuse_trace_id = None
                if result.success and self.tracker:
                    langfuse_trace_id = self.track_phase_in_langfuse(
                        phase_name=self.get_phase_name().value,
                        model=result.llm_response.model,
                        input_data=input_data,
                        output_data=result.output_data,
                        llm_response=result.llm_response,
                    )

                await self.save_llm_log(
                    workflow_state.id,
                    self.get_phase_name().value,
                    result.llm_response,
                    langfuse_trace_id,
                )

            return result

        except Exception as e:
            # Update workflow state with error
            await self.update_workflow_state(
                workflow_state,
                PhaseStatus.FAILED,
                error_message=str(e),
            )

            # Track error in LangFuse if available
            if self.tracker:
                self.tracker.track_event(
                    event_name=f"{self.get_phase_name().value}_failed",
                    metadata={"error": str(e)},
                )

            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message=str(e),
            )
