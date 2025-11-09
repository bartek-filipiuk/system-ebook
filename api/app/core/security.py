"""Security utilities including rate limiting."""
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.config import settings

# Initialize rate limiter
limiter = Limiter(
    key_func=get_remote_address,
    default_limits=[f"{settings.RATE_LIMIT_PER_SECOND}/second"],
    storage_uri="memory://",  # Use in-memory storage for now, can switch to Redis later
)
