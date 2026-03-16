"""Session-scoped state for a single forecast run.

Replaces scattered module-level globals with a single ContextVar that
propagates automatically through asyncio.gather() to sub-forecasts.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any

from aib.tools.metrics import MetricsCollector

if TYPE_CHECKING:
    from aib.agent.models import ForecastOutput

RunForecastFn = Callable[..., Awaitable["ForecastOutput"]]


class ForecastSession:
    """Per-forecast mutable state."""

    __slots__ = ("metrics", "modified_inputs", "run_forecast_fn")

    def __init__(
        self,
        *,
        run_forecast_fn: RunForecastFn | None = None,
    ) -> None:
        self.metrics = MetricsCollector()
        self.modified_inputs: dict[str, dict[str, Any]] = {}
        self.run_forecast_fn = run_forecast_fn


_current_session: ContextVar[ForecastSession | None] = ContextVar(
    "forecast_session", default=None
)


def get_session() -> ForecastSession:
    """Get the current forecast session. Raises if not in a session."""
    session = _current_session.get()
    if session is None:
        raise RuntimeError("No active forecast session")
    return session


def set_session(session: ForecastSession) -> None:
    """Set the current forecast session (returns no token — use reset_session)."""
    _current_session.set(session)


def reset_session() -> None:
    """Clear the current forecast session."""
    _current_session.set(None)
