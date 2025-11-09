"""Smart detection phase - determine if Event Storming is needed."""
import json
from typing import Any, Dict

from app.services.prompt_manager import prompt_manager
from app.workflow.phases.base import BasePhaseHandler, PhaseResult
from app.workflow.state_machine import WorkflowPhase


class SmartDetectionPhase(BasePhaseHandler):
    """Smart detection phase handler."""

    def get_phase_name(self) -> WorkflowPhase:
        """Get phase name."""
        return WorkflowPhase.SMART_DETECTION

    async def execute(self, input_data: Dict[str, Any]) -> PhaseResult:
        """Execute smart detection.

        Args:
            input_data: {"idea": str}

        Returns:
            PhaseResult with detection results

        """
        idea = input_data.get("idea", "")

        # Get smart detection prompt
        prompt = prompt_manager.get_smart_detection_prompt(idea)

        # Call LLM (using fast, cheap model)
        llm_response = await self.call_llm(
            model="openai/gpt-4o-mini",
            prompt=prompt,
            temperature=0.3,  # Lower temperature for more deterministic results
            max_tokens=500,
            response_format={"type": "json_object"},
        )

        # Parse JSON response
        try:
            detection_result = json.loads(llm_response.content)

            # Validate response structure
            required_keys = [
                "use_event_storming",
                "feature_count_estimate",
                "has_complex_business_logic",
                "reasoning",
            ]
            if not all(key in detection_result for key in required_keys):
                raise ValueError(f"Missing required keys in LLM response: {required_keys}")

            return PhaseResult(
                phase=self.get_phase_name(),
                success=True,
                output_data=detection_result,
                llm_response=llm_response,
            )

        except json.JSONDecodeError as e:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message=f"Failed to parse LLM JSON response: {e}",
                llm_response=llm_response,
            )
        except ValueError as e:
            return PhaseResult(
                phase=self.get_phase_name(),
                success=False,
                output_data={},
                error_message=str(e),
                llm_response=llm_response,
            )
