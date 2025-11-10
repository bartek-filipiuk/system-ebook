"""Pydantic schemas for workflow and WebSocket messages."""
from datetime import datetime
from typing import Any, Dict, Literal, Optional

from pydantic import BaseModel, Field


# WebSocket message schemas
class PhaseStartedMessage(BaseModel):
    """WebSocket message for phase started."""

    type: Literal["phase_started"] = "phase_started"
    phase: str
    timestamp: datetime
    message: str


class PhaseProgressMessage(BaseModel):
    """WebSocket message for phase progress."""

    type: Literal["phase_progress"] = "phase_progress"
    phase: str
    step: str
    progress_percent: int = Field(..., ge=0, le=100)
    timestamp: datetime


class PhaseCompletedMessage(BaseModel):
    """WebSocket message for phase completed."""

    type: Literal["phase_completed"] = "phase_completed"
    phase: str
    duration_seconds: int
    cost_usd: float
    timestamp: datetime


class PhaseFailedMessage(BaseModel):
    """WebSocket message for phase failed."""

    type: Literal["phase_failed"] = "phase_failed"
    phase: str
    error: str
    retry_available: bool
    timestamp: datetime


class WorkflowCompletedMessage(BaseModel):
    """WebSocket message for workflow completed."""

    type: Literal["workflow_completed"] = "workflow_completed"
    total_duration_seconds: int
    total_cost_usd: float
    documents_generated: int
    timestamp: datetime


# Union type for all WebSocket messages
WebSocketMessage = (
    PhaseStartedMessage
    | PhaseProgressMessage
    | PhaseCompletedMessage
    | PhaseFailedMessage
    | WorkflowCompletedMessage
)


# Workflow state schemas
class WorkflowStateResponse(BaseModel):
    """Schema for workflow state response."""

    phase: str
    status: str
    error_message: Optional[str] = None
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True
