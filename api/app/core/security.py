"""Security utilities including rate limiting."""
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.config import settings

# Determine storage backend for rate limiting
# Use Redis if configured (production), otherwise in-memory (development)
storage_uri = settings.REDIS_URL if settings.REDIS_URL else "memory://"

# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[f"{settings.RATE_LIMIT_PER_SECOND}/second"],
    storage_uri=storage_uri,
)
