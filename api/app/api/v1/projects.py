"""Projects API endpoints."""
import logging
from typing import List
from uuid import UUID

from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException, Request, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db_session, verify_admin_token
from app.core.security import limiter
from app.db.models import LLMLog, Project
from app.schemas.document import DocumentResponse, DocumentsResponse
from app.schemas.project import (
    CostBreakdownItem,
    ProjectCostResponse,
    ProjectCreate,
    ProjectCreateResponse,
    ProjectResponse,
    ProjectStartWorkflowResponse,
)
from app.workflow.document_storage import get_all_documents, get_document
from app.workflow.engine import WorkflowEngine
from app.workflow.state_machine import DocumentType, WorkflowStatus

logger = logging.getLogger(__name__)

router = APIRouter()


async def execute_workflow_background(project_id: UUID, db: AsyncSession) -> None:
    """Execute workflow in background.

    Args:
        project_id: Project UUID
        db: Database session

    """
    try:
        logger.info(f"Starting background workflow for project {project_id}")
        engine = WorkflowEngine(db, project_id)
        success = await engine.execute_workflow()

        if success:
            logger.info(f"Workflow completed successfully for project {project_id}")
        else:
            logger.error(f"Workflow failed for project {project_id}")

    except Exception as e:
        logger.error(f"Background workflow error for project {project_id}: {e}", exc_info=True)


@router.post(
    "",
    response_model=ProjectCreateResponse,
    status_code=status.HTTP_201_CREATED,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("10/minute")
async def create_project(
    request: Request,
    project_data: ProjectCreate,
    db: AsyncSession = Depends(get_db_session),
) -> ProjectCreateResponse:
    """Create a new project.

    Args:
        project_data: Project creation data
        db: Database session

    Returns:
        Created project info

    """
    # Create project
    project = Project(
        user_id=project_data.user_id,
        idea=project_data.idea,
        status=WorkflowStatus.CREATED.value,
        metadata={},
    )

    db.add(project)
    await db.commit()
    await db.refresh(project)

    logger.info(f"Created project {project.id} for user {project.user_id}")

    return ProjectCreateResponse(
        project_id=project.id,
        status=project.status,
        created_at=project.created_at,
    )


@router.post(
    "/{project_id}/start-workflow",
    response_model=ProjectStartWorkflowResponse,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("5/minute")
async def start_workflow(
    request: Request,
    project_id: UUID,
    background_tasks: BackgroundTasks,
    db: AsyncSession = Depends(get_db_session),
) -> ProjectStartWorkflowResponse:
    """Start workflow for a project.

    Args:
        project_id: Project UUID
        background_tasks: FastAPI background tasks
        db: Database session

    Returns:
        Workflow start confirmation with WebSocket URL

    Raises:
        HTTPException: If project not found or already processing

    """
    # Get project
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    # Check if already processing or completed
    if project.status in [WorkflowStatus.PROCESSING.value, WorkflowStatus.COMPLETED.value]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Project is already {project.status.lower()}",
        )

    # Update status to processing
    project.status = WorkflowStatus.PROCESSING.value
    await db.commit()

    # Start workflow in background
    background_tasks.add_task(execute_workflow_background, project_id, db)

    logger.info(f"Started workflow for project {project_id}")

    return ProjectStartWorkflowResponse(
        project_id=project.id,
        status=WorkflowStatus.PROCESSING.value,
        current_phase="SMART_DETECTION",
        websocket_url=f"/api/v1/projects/{project_id}/progress",
    )


@router.get(
    "/{project_id}",
    response_model=ProjectResponse,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("30/minute")
async def get_project(
    request: Request,
    project_id: UUID,
    db: AsyncSession = Depends(get_db_session),
) -> ProjectResponse:
    """Get project by ID.

    Args:
        project_id: Project UUID
        db: Database session

    Returns:
        Project details

    Raises:
        HTTPException: If project not found

    """
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    return ProjectResponse.model_validate(project)


@router.get(
    "/{project_id}/documents",
    response_model=DocumentsResponse,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("30/minute")
async def get_project_documents(
    request: Request,
    project_id: UUID,
    db: AsyncSession = Depends(get_db_session),
) -> DocumentsResponse:
    """Get all documents for a project.

    Args:
        project_id: Project UUID
        db: Database session

    Returns:
        All project documents

    Raises:
        HTTPException: If project not found

    """
    # Check if project exists
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    # Get all documents
    documents = await get_all_documents(db, project_id)

    return DocumentsResponse(
        project_id=project_id,
        documents=[DocumentResponse.model_validate(doc) for doc in documents],
    )


@router.get(
    "/{project_id}/documents/{document_type}",
    response_model=DocumentResponse,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("30/minute")
async def get_project_document(
    request: Request,
    project_id: UUID,
    document_type: str,
    db: AsyncSession = Depends(get_db_session),
) -> DocumentResponse:
    """Get a specific document for a project.

    Args:
        project_id: Project UUID
        document_type: Document type (EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN)
        db: Database session

    Returns:
        Document details

    Raises:
        HTTPException: If project or document not found

    """
    # Validate document type
    try:
        doc_type = DocumentType[document_type.upper()]
    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid document type: {document_type}. Valid types: EVENT_STORMING, PRD, TECH_STACK, EXECUTION_PLAN",
        )

    # Check if project exists
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    # Get document
    document = await get_document(db, project_id, doc_type)

    if not document:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Document {document_type} not found for project {project_id}",
        )

    return DocumentResponse.model_validate(document)


@router.get(
    "/{project_id}/costs",
    response_model=ProjectCostResponse,
    dependencies=[Depends(verify_admin_token)],
)
@limiter.limit("30/minute")
async def get_project_costs(
    request: Request,
    project_id: UUID,
    db: AsyncSession = Depends(get_db_session),
) -> ProjectCostResponse:
    """Get cost breakdown for a project.

    Args:
        project_id: Project UUID
        db: Database session

    Returns:
        Cost breakdown by phase

    Raises:
        HTTPException: If project not found

    """
    # Check if project exists
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Project {project_id} not found",
        )

    # Get all LLM logs
    result = await db.execute(
        select(LLMLog)
        .where(LLMLog.project_id == project_id)
        .order_by(LLMLog.created_at)
    )
    llm_logs = result.scalars().all()

    # Build breakdown
    breakdown: List[CostBreakdownItem] = []
    total_cost = 0.0

    for log in llm_logs:
        breakdown.append(
            CostBreakdownItem(
                phase=log.phase,
                model=log.model,
                tokens=log.total_tokens,
                cost_usd=float(log.cost_usd),
            )
        )
        total_cost += float(log.cost_usd)

    return ProjectCostResponse(
        project_id=project_id,
        total_cost_usd=round(total_cost, 6),
        breakdown=breakdown,
    )
