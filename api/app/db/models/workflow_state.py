"""Workflow state model."""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base


class WorkflowState(Base):
    """Workflow state table - tracks progress through phases."""

    __tablename__ = "workflow_states"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    project_id = Column(UUID(as_uuid=True), ForeignKey("projects.id", ondelete="CASCADE"), nullable=False)
    phase = Column(String(50), nullable=False)  # SMART_DETECTION, EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN
    status = Column(String(50), nullable=False)  # PENDING, IN_PROGRESS, COMPLETED, FAILED
    input_data = Column(JSONB)
    output_data = Column(JSONB)
    error_message = Column(Text)
    started_at = Column(DateTime)
    completed_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    project = relationship("Project", back_populates="workflow_states")
    llm_logs = relationship("LLMLog", back_populates="workflow_state", cascade="all, delete-orphan")
