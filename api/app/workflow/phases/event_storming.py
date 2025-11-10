"""Event Storming phase - business domain discovery."""
from typing import Any, Dict

from app.services.prompt_manager import prompt_manager
from app.workflow.phases.base import BasePhaseHandler, PhaseResult
from app.workflow.state_machine import WorkflowPhase


class EventStormingPhase(BasePhaseHandler):
    """Event Storming phase handler."""

    def get_phase_name(self) -> WorkflowPhase:
        """Get phase name."""
        return WorkflowPhase.EVENT_STORMING

    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute Event Storming.

        Args:
            input_data: {"idea": str}

        Returns:
            PhaseResult with Event Storming summary

        """
        idea = input_data.get("idea", "")

        # Get Event Storming prompt
        base_prompt = prompt_manager.get_event_storming_prompt(idea)

        # Create autonomous version of the prompt for API
        # In the interactive version, the LLM asks questions and waits
        # For API, we make it autonomous - the LLM imagines typical answers
        autonomous_prompt = base_prompt + """

---

**IMPORTANT FOR API MODE:**
Since this is an autonomous API mode (not interactive), you should:

1. Imagine you are interviewing a typical stakeholder for this type of project
2. Ask yourself the questions from each phase
3. Provide reasonable, typical answers based on the project idea
4. Then generate the final Event Storming Summary Document

Skip the back-and-forth questioning. Go directly to creating a comprehensive
Event Storming Summary Document based on your expert understanding of this
type of project.

Generate the complete Event Storming Summary Document now with all 10 sections.
"""

        # Call LLM (using Claude for structured thinking)
        llm_response = await self.call_llm(
            model="anthropic/claude-3.5-sonnet",
            prompt=autonomous_prompt,
            temperature=0.7,
            max_tokens=4000,
            system_message="You are an expert business analyst conducting Event Storming sessions.",
        )

        # The response should be a markdown document
        event_storming_md = llm_response.content

        # Validate that it looks like a proper document
        if len(event_storming_md) < 500:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="Event Storming summary too short - likely generation failed",
                llm_response=llm_response,
            )

        return PhaseResult(
            phase=self.get_phase_name(),
            success=True,
            output_data={"event_storming_md": event_storming_md},
            llm_response=llm_response,
        )
