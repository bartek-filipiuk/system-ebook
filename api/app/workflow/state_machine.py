"""Workflow state machine for managing phase transitions."""
from enum import Enum
from typing import Optional


class WorkflowPhase(str, Enum):
    """Workflow phases."""

    SMART_DETECTION = "SMART_DETECTION"
    EVENT_STORMING = "EVENT_STORMING"
    PRD = "PRD"
    TECH_STACK = "TECH_STACK"
    EXECUTION_PLAN = "EXECUTION_PLAN"


class WorkflowStatus(str, Enum):
    """Workflow status."""

    CREATED = "CREATED"
    PROCESSING = "PROCESSING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class PhaseStatus(str, Enum):
    """Phase status."""

    PENDING = "PENDING"
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"


class DocumentType(str, Enum):
    """Document types."""

    EVENT_STORMING = "EVENT_STORMING"
    PRD = "PRD"
    TECH_STACK = "TECH_STACK"
    EXECUTION_PLAN = "EXECUTION_PLAN"


class WorkflowStateMachine:
    """State machine for workflow phase transitions."""

    # Define phase order (without Event Storming)
    BASE_PHASES = [
        WorkflowPhase.SMART_DETECTION,
        WorkflowPhase.PRD,
        WorkflowPhase.TECH_STACK,
        WorkflowPhase.EXECUTION_PLAN,
    ]

    # Define phase order (with Event Storming)
    PHASES_WITH_EVENT_STORMING = [
        WorkflowPhase.SMART_DETECTION,
        WorkflowPhase.EVENT_STORMING,
        WorkflowPhase.PRD,
        WorkflowPhase.TECH_STACK,
        WorkflowPhase.EXECUTION_PLAN,
    ]

    @classmethod
    def get_next_phase(
        cls, current_phase: WorkflowPhase, use_event_storming: bool = False
    ) -> Optional[WorkflowPhase]:
        """Get the next phase in the workflow.

        Args:
            current_phase: Current workflow phase
            use_event_storming: Whether to include Event Storming phase

        Returns:
            Next phase or None if workflow is complete

        """
        phases = cls.PHASES_WITH_EVENT_STORMING if use_event_storming else cls.BASE_PHASES

        try:
            current_index = phases.index(current_phase)
            if current_index < len(phases) - 1:
                return phases[current_index + 1]
            return None  # Workflow complete
        except ValueError:
            return None

    @classmethod
    def is_workflow_complete(cls, current_phase: WorkflowPhase) -> bool:
        """Check if workflow is complete.

        Args:
            current_phase: Current workflow phase

        Returns:
            True if workflow is complete

        """
        return current_phase == WorkflowPhase.EXECUTION_PLAN

    @classmethod
    def get_phase_order(cls, use_event_storming: bool = False) -> list[WorkflowPhase]:
        """Get the complete phase order.

        Args:
            use_event_storming: Whether to include Event Storming phase

        Returns:
            List of phases in execution order

        """
        return cls.PHASES_WITH_EVENT_STORMING if use_event_storming else cls.BASE_PHASES

    @classmethod
    def validate_phase_transition(
        cls,
        current_phase: WorkflowPhase,
        next_phase: WorkflowPhase,
        use_event_storming: bool = False,
    ) -> bool:
        """Validate if a phase transition is valid.

        Args:
            current_phase: Current workflow phase
            next_phase: Proposed next phase
            use_event_storming: Whether Event Storming is enabled

        Returns:
            True if transition is valid

        """
        expected_next = cls.get_next_phase(current_phase, use_event_storming)
        return expected_next == next_phase
