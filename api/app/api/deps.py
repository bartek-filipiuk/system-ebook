"""API dependencies."""
from typing import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.auth import verify_admin_token
from app.db.session import get_db

# Re-export for convenience
__all__ = ["get_db", "verify_admin_token"]


async def get_db_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session dependency."""
    async for session in get_db():
        yield session
