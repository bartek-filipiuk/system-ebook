"""Application configuration using Pydantic Settings."""
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # Application
    PROJECT_NAME: str = "AI-Driven Development Framework API"
    VERSION: str = "1.0.0"
    API_V1_PREFIX: str = "/api/v1"
    DEBUG: bool = False

    # Server
    HOST: str = "0.0.0.0"
    PORT: int = 8000

    # Database
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DB: str = "ai_dev_framework"
    DATABASE_URL: str = Field(
        default="postgresql+asyncpg://postgres:postgres@localhost:5432/ai_dev_framework"
    )

    # Authentication
    ADMIN_TOKEN: str = Field(default="change-me-in-production")

    # OpenRouter
    OPENROUTER_API_KEY: str = Field(default="")
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    # LangFuse
    LANGFUSE_PUBLIC_KEY: str = Field(default="")
    LANGFUSE_SECRET_KEY: str = Field(default="")
    LANGFUSE_HOST: str = "https://cloud.langfuse.com"

    # Rate Limiting
    RATE_LIMIT_PER_SECOND: int = 1
    REDIS_URL: str = Field(
        default="",
        description="Redis URL for rate limiting (empty = in-memory). Example: redis://localhost:6379",
    )

    # CORS
    BACKEND_CORS_ORIGINS: List[str] = Field(
        default_factory=lambda: ["http://localhost:3000", "http://localhost:8080"]
    )

    # Logging
    LOG_LEVEL: str = "INFO"

    @property
    def database_url_sync(self) -> str:
        """Get synchronous database URL for Alembic."""
        return self.DATABASE_URL.replace("+asyncpg", "")

    def model_post_init(self, __context) -> None:
        """Validate settings after initialization."""
        # Validate admin token strength in production
        if not self.DEBUG:
            if not self.ADMIN_TOKEN or len(self.ADMIN_TOKEN) < 32:
                raise ValueError(
                    "ADMIN_TOKEN must be set and at least 32 characters long in production mode (DEBUG=False). "
                    "Generate a secure token with: python -c 'import secrets; print(secrets.token_urlsafe(32))'"
                )
            if self.ADMIN_TOKEN in ["change-me-in-production", "your-super-secret-admin-token-here-change-in-production"]:
                raise ValueError(
                    "ADMIN_TOKEN must be changed from default value in production. "
                    "Generate a secure token with: python -c 'import secrets; print(secrets.token_urlsafe(32))'"
                )


settings = Settings()
