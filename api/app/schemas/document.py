"""Pydantic schemas for documents."""
from datetime import datetime
from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel, Field


class DocumentResponse(BaseModel):
    """Schema for a single document response."""

    type: str = Field(..., description="Document type (EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN)")
    content_md: str = Field(..., description="Markdown content of the document")
    metadata: Dict[str, Any] = Field(default_factory=dict)
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class DocumentsResponse(BaseModel):
    """Schema for all documents response."""

    project_id: UUID
    documents: list[DocumentResponse]
