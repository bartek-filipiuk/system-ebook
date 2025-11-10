"""WebSocket endpoints for real-time progress updates."""
import logging
from typing import Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query, WebSocket, WebSocketDisconnect, status
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.api.deps import get_db_session
from app.config import settings
from app.core.websocket_manager import manager
from app.db.models import Project

logger = logging.getLogger(__name__)

router = APIRouter()


@router.websocket("/projects/{project_id}/progress")
async def project_progress(
    websocket: WebSocket,
    project_id: UUID,
    token: str = Query(..., description="Admin authentication token"),
    db: AsyncSession = Depends(get_db_session),
) -> None:
    """WebSocket endpoint for real-time project progress updates.

    Requires authentication via query parameter: ?token=<ADMIN_TOKEN>

    Args:
        websocket: WebSocket connection
        project_id: Project UUID
        token: Admin authentication token (query parameter)
        db: Database session

    """
    # Verify authentication token before accepting connection
    if token != settings.ADMIN_TOKEN:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="Unauthorized - Invalid token")
        logger.warning(f"WebSocket authentication failed for project {project_id}")
        return

    # Verify project exists before accepting connection
    result = await db.execute(select(Project).where(Project.id == project_id))
    project = result.scalar_one_or_none()

    if not project:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION, reason="Project not found")
        return

    # Accept and register connection
    await manager.connect(project_id, websocket)
    logger.info(f"WebSocket authenticated and connected for project {project_id}")

    try:
        # Send initial connection confirmation
        await websocket.send_json({
            "type": "connected",
            "project_id": str(project_id),
            "current_status": project.status,
            "current_phase": project.current_phase,
            "message": "Connected to project progress updates",
        })

        # Keep connection alive and listen for client messages (if any)
        while True:
            # Wait for any message from client (mostly just to detect disconnects)
            # Client doesn't need to send messages, but this keeps the connection alive
            data = await websocket.receive_text()

            # Echo back if client sends anything (optional)
            if data == "ping":
                await websocket.send_json({"type": "pong"})

    except WebSocketDisconnect:
        logger.info(f"WebSocket disconnected for project {project_id}")
    except Exception as e:
        logger.error(f"WebSocket error for project {project_id}: {e}", exc_info=True)
    finally:
        manager.disconnect(project_id, websocket)
