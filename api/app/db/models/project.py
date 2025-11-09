"""Project model."""
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import JSONB, UUID
from sqlalchemy.orm import relationship

from app.db.base import Base


class Project(Base):
    """Project table."""

    __tablename__ = "projects"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    idea = Column(Text, nullable=False)
    status = Column(String(50), nullable=False)  # CREATED, PROCESSING, COMPLETED, FAILED
    current_phase = Column(String(50))  # SMART_DETECTION, EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN
    metadata = Column(JSONB, default=dict, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    completed_at = Column(DateTime)

    # Relationships
    user = relationship("User", back_populates="projects")
    workflow_states = relationship("WorkflowState", back_populates="project", cascade="all, delete-orphan")
    documents = relationship("Document", back_populates="project", cascade="all, delete-orphan")
    llm_logs = relationship("LLMLog", back_populates="project", cascade="all, delete-orphan")
