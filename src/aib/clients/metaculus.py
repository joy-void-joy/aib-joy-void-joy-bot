"""Async Metaculus API client - re-exports from metaculus package.

This module re-exports the AsyncMetaculusClient and related types from
the metaculus package for backward compatibility with existing aib code.
"""

from metaculus import (
    ApiFilter,
    AsyncMetaculusClient,
    BinaryQuestion,
    DetailedCoherenceLink,
    MetaculusQuestion,
)

from aib.config import settings

__all__ = [
    "ApiFilter",
    "AsyncMetaculusClient",
    "BinaryQuestion",
    "DetailedCoherenceLink",
    "MetaculusQuestion",
    "get_client",
]

# Module-level singleton for convenience
_client: AsyncMetaculusClient | None = None


def get_client() -> AsyncMetaculusClient:
    """Get the async Metaculus client singleton."""
    global _client
    if _client is None:
        _client = AsyncMetaculusClient(
            timeout=settings.http_timeout_seconds,
            token=settings.metaculus_token,
        )
    return _client
