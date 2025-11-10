"""Tech Stack phase - generate technology stack document."""
from typing import Any, Dict

from app.services.prompt_manager import prompt_manager
from app.workflow.phases.base import BasePhaseHandler, PhaseResult
from app.workflow.state_machine import WorkflowPhase


class TechStackPhase(BasePhaseHandler):
    """Tech Stack phase handler."""

    def get_phase_name(self) -> WorkflowPhase:
        """Get phase name."""
        return WorkflowPhase.TECH_STACK

    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute Tech Stack generation.

        Args:
            input_data: {"prd_md": str}

        Returns:
            PhaseResult with Tech Stack markdown

        """
        prd_md = input_data.get("prd_md", "")

        if not prd_md:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="PRD markdown is required for Tech Stack generation",
            )

        # Get Tech Stack prompt
        prompt = prompt_manager.get_tech_stack_prompt(prd_md)

        # Call LLM (using GPT-4o for technical decisions)
        llm_response = await self.call_llm(
            model="openai/gpt-4o",
            prompt=prompt,
            temperature=0.5,  # Slightly lower for more consistent technical choices
            max_tokens=3000,
            system_message="You are an expert software architect making technology stack decisions.",
        )

        tech_stack_md = llm_response.content

        # Validate Tech Stack
        if len(tech_stack_md) < 500:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="Tech Stack document too short - likely generation failed",
                llm_response=llm_response,
            )

        # Check for required sections
        required_keywords = ["Frontend", "Backend", "Infrastructure"]
        missing_sections = [kw for kw in required_keywords if kw not in tech_stack_md]
        if missing_sections:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message=f"Tech Stack missing required sections: {', '.join(missing_sections)}",
                llm_response=llm_response,
            )

        return PhaseResult(
            phase=self.get_phase_name(),
            success=True,
            output_data={"tech_stack_md": tech_stack_md},
            llm_response=llm_response,
        )
