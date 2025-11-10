"""WebSocket connection manager for real-time progress updates."""
import logging
from datetime import datetime
from typing import Dict, List
from uuid import UUID

from fastapi import WebSocket

logger = logging.getLogger(__name__)


class ConnectionManager:
    """Manage WebSocket connections for projects."""

    def __init__(self):
        """Initialize connection manager."""
        # Maps project_id to list of active WebSocket connections
        self.active_connections: Dict[str, List[WebSocket]] = {}

    async def connect(self, project_id: UUID, websocket: WebSocket) -> None:
        """Accept and register a WebSocket connection.

        Args:
            project_id: Project UUID
            websocket: WebSocket connection

        """
        await websocket.accept()

        project_id_str = str(project_id)
        if project_id_str not in self.active_connections:
            self.active_connections[project_id_str] = []

        self.active_connections[project_id_str].append(websocket)
        logger.info(f"WebSocket connected for project {project_id}")

    def disconnect(self, project_id: UUID, websocket: WebSocket) -> None:
        """Remove a WebSocket connection.

        Args:
            project_id: Project UUID
            websocket: WebSocket connection

        """
        project_id_str = str(project_id)
        if project_id_str in self.active_connections:
            if websocket in self.active_connections[project_id_str]:
                self.active_connections[project_id_str].remove(websocket)
                logger.info(f"WebSocket disconnected for project {project_id}")

            # Clean up empty lists
            if not self.active_connections[project_id_str]:
                del self.active_connections[project_id_str]

    async def broadcast(self, project_id: UUID, message: dict) -> None:
        """Broadcast message to all connections for a project.

        Args:
            project_id: Project UUID
            message: Message to broadcast

        """
        project_id_str = str(project_id)

        if project_id_str not in self.active_connections:
            logger.debug(f"No active connections for project {project_id}")
            return

        # Add timestamp if not present
        if "timestamp" not in message:
            message["timestamp"] = datetime.utcnow().isoformat()

        # Broadcast to all connections
        dead_connections = []
        for connection in self.active_connections[project_id_str]:
            try:
                await connection.send_json(message)
            except Exception as e:
                logger.error(f"Failed to send message to WebSocket: {e}")
                dead_connections.append(connection)

        # Remove dead connections
        for connection in dead_connections:
            self.disconnect(project_id, connection)

    def get_connection_count(self, project_id: UUID) -> int:
        """Get number of active connections for a project.

        Args:
            project_id: Project UUID

        Returns:
            Number of active connections

        """
        project_id_str = str(project_id)
        return len(self.active_connections.get(project_id_str, []))


# Global connection manager instance
manager = ConnectionManager()
