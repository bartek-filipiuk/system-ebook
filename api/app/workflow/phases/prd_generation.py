"""PRD generation phase - create Product Requirements Document."""
from typing import Any, Dict, Optional

from app.services.prompt_manager import prompt_manager
from app.workflow.phases.base import BasePhaseHandler, PhaseResult
from app.workflow.state_machine import WorkflowPhase


class PRDGenerationPhase(BasePhaseHandler):
    """PRD generation phase handler."""

    def get_phase_name(self) -> WorkflowPhase:
        """Get phase name."""
        return WorkflowPhase.PRD

    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute PRD generation.

        Args:
            input_data: {
                "idea": str,
                "event_storming_summary": Optional[str]
            }

        Returns:
            PhaseResult with PRD markdown

        """
        idea = input_data.get("idea", "")
        event_storming_summary = input_data.get("event_storming_summary")

        # Get INIT prompt
        base_prompt = prompt_manager.get_init_prompt(idea, event_storming_summary)

        # Make it autonomous for API mode
        autonomous_prompt = base_prompt + """

---

**IMPORTANT FOR API MODE:**
Since this is an autonomous API mode (not interactive):

1. First, ask yourself the 15 questions listed above
2. Then, provide reasonable, well-thought-out answers based on the project idea
   (and Event Storming summary if provided)
3. Finally, generate the complete PRD document with all 9 sections

Skip the interactive back-and-forth. Generate a complete, professional PRD
document directly.

The PRD must include these 9 sections:
1. Project Overview & Vision
2. Strategic Alignment & Success Metrics
3. Target Users & Personas
4. User Stories & Acceptance Criteria
5. Functional Requirements by Feature
6. Scope & In-Scope Features (MVP)
7. Explicitly Out-of-Scope (Post-MVP)
8. Non-Functional Requirements
9. Assumptions, Dependencies, Risks

Generate the complete PRD markdown document now.
"""

        # Call LLM (using Claude for complex document generation)
        llm_response = await self.call_llm(
            model="anthropic/claude-3.5-sonnet",
            prompt=autonomous_prompt,
            temperature=0.7,
            max_tokens=4000,
            system_message="You are an expert AI software architect and project manager.",
        )

        prd_md = llm_response.content

        # Validate PRD
        if len(prd_md) < 1000:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="PRD too short - likely generation failed",
                llm_response=llm_response,
            )

        # Check for required sections (at least some of them)
        required_keywords = ["Overview", "Requirements", "Scope", "Features"]
        if not any(keyword in prd_md for keyword in required_keywords):
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message="PRD missing required sections",
                llm_response=llm_response,
            )

        return PhaseResult(
            phase=self.get_phase_name(),
            success=True,
            output_data={"prd_md": prd_md},
            llm_response=llm_response,
        )
