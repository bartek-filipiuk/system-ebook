"""Execution Plan phase - generate staged handoff plan."""
import json
from typing import Any, Dict

from app.services.prompt_manager import prompt_manager
from app.workflow.phases.base import BasePhaseHandler, PhaseResult
from app.workflow.state_machine import WorkflowPhase


class ExecutionPlanPhase(BasePhaseHandler):
    """Execution Plan phase handler."""

    def get_phase_name(self) -> WorkflowPhase:
        """Get phase name."""
        return WorkflowPhase.EXECUTION_PLAN

    async def _detect_approach(self, prd_md: str) -> str:
        """Detect whether to use Horizontal or Vertical approach.

        Args:
            prd_md: PRD markdown content

        Returns:
            "HORIZONTAL" or "VERTICAL"

        """
        # Get approach detection prompt
        prompt = prompt_manager.get_approach_detection_prompt(prd_md)

        # Call LLM (using GPT-4o-mini for fast decision)
        llm_response = await self.call_llm(
            model="openai/gpt-4o-mini",
            prompt=prompt,
            temperature=0.3,
            max_tokens=300,
            response_format={"type": "json_object"},
        )

        # Parse JSON response
        try:
            detection_result = json.loads(llm_response.content)
            approach = detection_result.get("approach", "HORIZONTAL")

            # Validate approach
            if approach not in ["HORIZONTAL", "VERTICAL"]:
                # Default to VERTICAL if invalid
                approach = "VERTICAL"

            return approach

        except (json.JSONDecodeError, ValueError):
            # Default to VERTICAL on error (safer approach)
            return "VERTICAL"

    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute Execution Plan generation.

        Args:
            input_data: {
                "prd_md": str,
                "tech_stack_md": str
            }

        Returns:
            PhaseResult with Execution Plan markdown

        """
        prd_md = input_data.get("prd_md", "")
        tech_stack_md = input_data.get("tech_stack_md", "")

        if not prd_md or not tech_stack_md:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="Both PRD and Tech Stack are required for Execution Plan generation",
            )

        # Detect approach (Horizontal vs Vertical)
        approach = await self._detect_approach(prd_md)

        # Get Execution Plan prompt with detected approach
        prompt = prompt_manager.get_stages_prompt(prd_md, tech_stack_md, approach)

        # Call LLM (using Claude for granular planning)
        llm_response = await self.call_llm(
            model="anthropic/claude-3.5-sonnet",
            prompt=prompt,
            temperature=0.6,
            max_tokens=4000,
            system_message="You are an expert at creating detailed, granular execution plans for AI coding agents.",
        )

        execution_plan_md = llm_response.content

        # Validate Execution Plan
        if len(execution_plan_md) < 1000:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="Execution Plan too short - likely generation failed",
                llm_response=llm_response,
            )

        # Check for required elements
        required_keywords = ["Stage", "Task", "[", "]"]  # Check for stages, tasks, and checkboxes
        missing_elements = [kw for kw in required_keywords if kw not in execution_plan_md]
        if missing_elements:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message=f"Execution Plan missing required elements: {', '.join(missing_elements)}",
                llm_response=llm_response,
            )

        return PhaseResult(
            phase=self.get_phase_name(),
            success=True,
            output_data={
                "execution_plan_md": execution_plan_md,
                "approach": approach,
            },
            llm_response=llm_response,
        )
