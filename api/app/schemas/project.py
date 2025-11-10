"""Pydantic schemas for projects."""
from datetime import datetime
from typing import Any, Dict, Optional
from uuid import UUID

from pydantic import BaseModel, Field


# Request schemas
class ProjectCreate(BaseModel):
    """Schema for creating a new project."""

    idea: str = Field(..., min_length=10, max_length=5000, description="Project idea description")
    user_id: UUID = Field(..., description="User ID from frontend system")


class ProjectStartWorkflow(BaseModel):
    """Schema for starting workflow (empty, uses project ID from path)."""

    pass


class ProjectRetry(BaseModel):
    """Schema for retrying a failed workflow."""

    from_phase: Optional[str] = Field(
        None,
        description="Phase to retry from (defaults to failed phase if not specified)",
    )


# Response schemas
class ProjectResponse(BaseModel):
    """Schema for project response."""

    project_id: UUID
    idea: str
    status: str
    current_phase: Optional[str] = None
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime
    completed_at: Optional[datetime] = None

    class Config:
        from_attributes = True


class ProjectCreateResponse(BaseModel):
    """Schema for project creation response."""

    project_id: UUID
    status: str
    created_at: datetime


class ProjectStartWorkflowResponse(BaseModel):
    """Schema for workflow start response."""

    project_id: UUID
    status: str
    current_phase: str
    websocket_url: str


class CostBreakdownItem(BaseModel):
    """Schema for a single cost breakdown item."""

    phase: str
    model: str
    tokens: int
    cost_usd: float


class ProjectCostResponse(BaseModel):
    """Schema for project cost breakdown response."""

    project_id: UUID
    total_cost_usd: float
    breakdown: list[CostBreakdownItem]
