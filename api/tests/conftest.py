"""Pytest configuration and fixtures."""
import asyncio
from typing import AsyncGenerator, Generator

import pytest
from httpx import AsyncClient
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from app.config import settings
from app.db.base import Base
from app.main import app

# Test database URL (use separate test database)
TEST_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@localhost:5432/ai_dev_framework_test"


@pytest.fixture(scope="session")
def event_loop() -> Generator:
    """Create an instance of the default event loop for the test session."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
async def test_engine():
    """Create test database engine."""
    engine = create_async_engine(TEST_DATABASE_URL, echo=False)

    # Create all tables
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield engine

    # Drop all tables after tests
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)

    await engine.dispose()


@pytest.fixture
async def db_session(test_engine) -> AsyncGenerator[AsyncSession, None]:
    """Create a test database session."""
    async_session = sessionmaker(
        test_engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session
        await session.rollback()


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """Create test HTTP client."""
    async with AsyncClient(app=app, base_url="http://test") as ac:
        yield ac


@pytest.fixture
def admin_headers() -> dict:
    """Get admin authorization headers."""
    return {"Authorization": f"Bearer {settings.ADMIN_TOKEN}"}
