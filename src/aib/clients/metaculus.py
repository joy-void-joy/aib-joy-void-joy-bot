"""Metaculus API clients - re-exports from metaculus package.

This module re-exports the clients and related types from the metaculus
package, and provides singleton accessors configured from aib settings.
"""

from metaculus import (
    ApiFilter,
    AsyncMetaculusClient,
    BinaryQuestion,
    DetailedCoherenceLink,
    MetaculusClient,
    MetaculusQuestion,
)

from aib.config import settings

__all__ = [
    "ApiFilter",
    "AsyncMetaculusClient",
    "BinaryQuestion",
    "DetailedCoherenceLink",
    "MetaculusClient",
    "MetaculusQuestion",
    "get_client",
    "get_sync_client",
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
            min_request_interval=settings.metaculus_request_interval,
        )
    return _client


def get_sync_client() -> MetaculusClient:
    """Create a sync Metaculus client configured from settings."""
    return MetaculusClient(
        timeout=settings.http_timeout_seconds,
        token=settings.metaculus_token,
        min_request_interval=settings.metaculus_request_interval,
    )
