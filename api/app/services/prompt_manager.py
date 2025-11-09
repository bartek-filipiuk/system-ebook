"""Prompt template manager for loading and rendering prompts."""
import os
from pathlib import Path
from typing import Dict, Optional


class PromptManager:
    """Manager for loading and rendering prompt templates."""

    def __init__(self):
        """Initialize prompt manager."""
        self.prompts_dir = Path(__file__).parent.parent / "prompts"
        self._cache: Dict[str, str] = {}

    def load_prompt(self, prompt_name: str) -> str:
        """Load a prompt template from file.

        Args:
            prompt_name: Name of the prompt file (without .txt extension)

        Returns:
            Prompt template string

        Raises:
            FileNotFoundError: If prompt file doesn't exist

        """
        # Check cache first
        if prompt_name in self._cache:
            return self._cache[prompt_name]

        # Load from file
        prompt_path = self.prompts_dir / f"{prompt_name}.txt"
        if not prompt_path.exists():
            raise FileNotFoundError(f"Prompt template '{prompt_name}' not found at {prompt_path}")

        with open(prompt_path, "r", encoding="utf-8") as f:
            template = f.read()

        # Cache it
        self._cache[prompt_name] = template
        return template

    def render_prompt(self, prompt_name: str, **kwargs) -> str:
        """Load and render a prompt template with variables.

        Args:
            prompt_name: Name of the prompt file (without .txt extension)
            **kwargs: Variables to substitute in the template

        Returns:
            Rendered prompt string

        Example:
            prompt = manager.render_prompt("smart_detection", idea="Build a blog")

        """
        template = self.load_prompt(prompt_name)
        return template.format(**kwargs)

    def get_smart_detection_prompt(self, idea: str) -> str:
        """Get smart detection prompt.

        Args:
            idea: Project idea

        Returns:
            Rendered prompt

        """
        return self.render_prompt("smart_detection", idea=idea)

    def get_event_storming_prompt(self, idea: str) -> str:
        """Get event storming prompt.

        Args:
            idea: Project idea

        Returns:
            Rendered prompt

        """
        return self.render_prompt("event_storming", idea=idea)

    def get_init_prompt(self, idea: str, event_storming_summary: Optional[str] = None) -> str:
        """Get INIT prompt for PRD generation.

        Args:
            idea: Project idea
            event_storming_summary: Optional event storming summary

        Returns:
            Rendered prompt

        """
        # Add event storming context if available
        event_storming_context = ""
        if event_storming_summary:
            event_storming_context = f"""
Additionally, here is the Event Storming Summary from our business domain analysis:

---
{event_storming_summary}
---

Use this summary to inform your questions and the final PRD.
"""

        return self.render_prompt(
            "init_prompt", idea=idea, event_storming_context=event_storming_context
        )

    def get_tech_stack_prompt(self, prd_content: str) -> str:
        """Get tech stack generation prompt.

        Args:
            prd_content: Complete PRD markdown

        Returns:
            Rendered prompt

        """
        return self.render_prompt("tech_stack_prompt", prd_content=prd_content)

    def get_stages_prompt(
        self, prd_content: str, tech_stack_content: str, approach: str = "HORIZONTAL"
    ) -> str:
        """Get execution plan generation prompt.

        Args:
            prd_content: Complete PRD markdown
            tech_stack_content: Complete tech stack markdown
            approach: Development approach ("HORIZONTAL" or "VERTICAL")

        Returns:
            Rendered prompt

        """
        # Add approach-specific instructions
        if approach == "VERTICAL":
            approach_instruction = """
**IMPORTANT:** Use a VERTICAL (feature-by-feature) development approach.
This means each stage should implement a complete feature from backend to frontend, not layers.

Structure stages as:
- Stage 1: Minimal Working Installation (basic end-to-end system)
- Stage 2-N: Complete feature slices (backend + frontend + integration per feature)
- Final Stage: Polish & finalization
"""
        else:
            approach_instruction = """
**IMPORTANT:** Use a HORIZONTAL (layer-by-layer) development approach.
This means stages should build each layer completely before moving to the next.

Structure stages as:
- Stage 1: Project Setup & Environment
- Stage 2: Backend Development (all APIs)
- Stage 3: Frontend Development (all UI)
- Stage 4: Integration
- Stage 5: Testing & Documentation
"""

        return self.render_prompt(
            "stages_prompt",
            prd_content=prd_content,
            tech_stack_content=tech_stack_content,
            approach_instruction=approach_instruction,
        )

    def get_approach_detection_prompt(self, prd_content: str) -> str:
        """Get approach detection prompt.

        Args:
            prd_content: Complete PRD markdown

        Returns:
            Rendered prompt

        """
        return self.render_prompt("approach_detection", prd_content=prd_content)


# Global instance
prompt_manager = PromptManager()
