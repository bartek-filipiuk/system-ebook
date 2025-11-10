"""Document storage utilities."""
from datetime import datetime
from typing import Dict, List, Optional
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.models import Document
from app.workflow.state_machine import DocumentType


async def save_document(
    db: AsyncSession,
    project_id: UUID,
    document_type: DocumentType,
    content_md: str,
    metadata: Optional[Dict] = None,
) -> Document:
    """Save a document to the database.

    Args:
        db: Database session
        project_id: Project UUID
        document_type: Type of document
        content_md: Markdown content
        metadata: Optional metadata

    Returns:
        Created Document

    """
    # Check if document already exists (overwrite if yes)
    result = await db.execute(
        select(Document).where(
            Document.project_id == project_id,
            Document.type == document_type.value,
        )
    )
    existing_doc = result.scalar_one_or_none()

    if existing_doc:
        # Update existing document
        existing_doc.content_md = content_md
        existing_doc.metadata = metadata or {}
        existing_doc.updated_at = datetime.utcnow()
        await db.commit()
        await db.refresh(existing_doc)
        return existing_doc
    else:
        # Create new document
        document = Document(
            project_id=project_id,
            type=document_type.value,
            content_md=content_md,
            metadata=metadata or {},
        )
        db.add(document)
        await db.commit()
        await db.refresh(document)
        return document


async def get_document(
    db: AsyncSession,
    project_id: UUID,
    document_type: DocumentType,
) -> Optional[Document]:
    """Get a document from the database.

    Args:
        db: Database session
        project_id: Project UUID
        document_type: Type of document

    Returns:
        Document or None if not found

    """
    result = await db.execute(
        select(Document).where(
            Document.project_id == project_id,
            Document.type == document_type.value,
        )
    )
    return result.scalar_one_or_none()


async def get_all_documents(
    db: AsyncSession,
    project_id: UUID,
) -> List[Document]:
    """Get all documents for a project.

    Args:
        db: Database session
        project_id: Project UUID

    Returns:
        List of Documents

    """
    result = await db.execute(
        select(Document)
        .where(Document.project_id == project_id)
        .order_by(Document.created_at)
    )
    return list(result.scalars().all())


async def delete_document(
    db: AsyncSession,
    project_id: UUID,
    document_type: DocumentType,
) -> bool:
    """Delete a document from the database.

    Args:
        db: Database session
        project_id: Project UUID
        document_type: Type of document

    Returns:
        True if document was deleted, False if not found

    """
    document = await get_document(db, project_id, document_type)
    if document:
        await db.delete(document)
        await db.commit()
        return True
    return False
