"""LangFuse service for observability and cost tracking."""
from typing import Any, Dict, Optional
from uuid import UUID

from langfuse import Langfuse
from langfuse.model import CreateTrace

from app.config import settings


class LangFuseTracker:
    """LangFuse tracker for a single project workflow."""

    def __init__(self, project_id: UUID, idea: str):
        """Initialize tracker for a project.

        Args:
            project_id: Project UUID
            idea: Project idea (truncated for metadata)

        """
        self.project_id = str(project_id)
        self.langfuse = get_langfuse_client()

        # Create trace for this project
        self.trace = self.langfuse.trace(
            name=f"project_{self.project_id}",
            user_id=self.project_id,
            metadata={"idea": idea[:200]},  # Truncate long ideas
            tags=["ai-dev-framework", "workflow"],
        )

    def track_phase(
        self,
        phase_name: str,
        model: str,
        input_data: Dict[str, Any],
        output_data: Dict[str, Any],
        tokens: Dict[str, int],
        cost: float,
        duration_ms: int,
        status: str = "completed",
        error: Optional[str] = None,
    ) -> str:
        """Track a workflow phase execution.

        Args:
            phase_name: Name of the phase (e.g., "SMART_DETECTION", "PRD")
            model: Model used (e.g., "openai/gpt-4o-mini")
            input_data: Input to the LLM
            output_data: Output from the LLM
            tokens: Token usage dict
            cost: Cost in USD
            duration_ms: Duration in milliseconds
            status: Status ("completed" or "failed")
            error: Error message if failed

        Returns:
            LangFuse generation ID (trace ID)

        """
        metadata = {
            "cost_usd": cost,
            "duration_ms": duration_ms,
            "status": status,
        }

        if error:
            metadata["error"] = error

        generation = self.trace.generation(
            name=phase_name,
            model=model,
            input=input_data,
            output=output_data if status == "completed" else None,
            usage={
                "input": tokens.get("prompt_tokens", 0),
                "output": tokens.get("completion_tokens", 0),
                "total": tokens.get("total_tokens", 0),
            },
            metadata=metadata,
            level="ERROR" if error else "DEFAULT",
        )

        return generation.id

    def track_event(
        self,
        event_name: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> None:
        """Track a workflow event (non-LLM).

        Args:
            event_name: Name of the event (e.g., "workflow_started")
            metadata: Optional metadata

        """
        self.trace.event(
            name=event_name,
            metadata=metadata or {},
        )

    def finalize(
        self,
        total_cost: float,
        total_duration_seconds: int,
        status: str,
        documents_generated: int,
    ) -> None:
        """Finalize the trace with summary metadata.

        Args:
            total_cost: Total cost in USD
            total_duration_seconds: Total duration in seconds
            status: Final status ("completed" or "failed")
            documents_generated: Number of documents generated

        """
        self.trace.update(
            metadata={
                "total_cost_usd": total_cost,
                "total_duration_seconds": total_duration_seconds,
                "final_status": status,
                "documents_generated": documents_generated,
            },
            output={
                "status": status,
                "cost": total_cost,
                "duration": total_duration_seconds,
            },
        )


def get_langfuse_client() -> Langfuse:
    """Get LangFuse client singleton.

    Returns:
        LangFuse client instance

    """
    return Langfuse(
        public_key=settings.LANGFUSE_PUBLIC_KEY,
        secret_key=settings.LANGFUSE_SECRET_KEY,
        host=settings.LANGFUSE_HOST,
    )


# Helper function to check if LangFuse is configured
def is_langfuse_enabled() -> bool:
    """Check if LangFuse is properly configured.

    Returns:
        True if both public and secret keys are set

    """
    return bool(settings.LANGFUSE_PUBLIC_KEY and settings.LANGFUSE_SECRET_KEY)
