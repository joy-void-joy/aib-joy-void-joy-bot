"""Session-scoped state for a single forecast run.

Replaces scattered module-level globals with a single ContextVar that
propagates automatically through asyncio.gather() to sub-forecasts.
"""

from __future__ import annotations

from collections.abc import Awaitable, Callable
from contextvars import ContextVar
from dataclasses import dataclass, field
from enum import StrEnum
from typing import TYPE_CHECKING, Any

from pydantic import BaseModel, Field

from aib.tools.metrics import MetricsCollector

if TYPE_CHECKING:
    from aib.agent.models import ForecastOutput

RunForecastFn = Callable[..., Awaitable["ForecastOutput"]]


class ForecastSession:
    """Per-forecast mutable state."""

    __slots__ = (
        "current_depth",
        "metrics",
        "modified_inputs",
        "nested_traces",
        "parent_slug",
        "post_id",
        "research_mcp_servers",
        "run_forecast_fn",
        "subforecast_depth",
    )

    def __init__(
        self,
        *,
        run_forecast_fn: RunForecastFn | None = None,
        research_mcp_servers: dict[str, Any] | None = None,
        subforecast_depth: int | None = None,
        post_id: int | None = None,
        current_depth: int = 0,
        parent_slug: str | None = None,
    ) -> None:
        self.metrics = MetricsCollector()
        self.modified_inputs: dict[str, dict[str, Any]] = {}
        self.nested_traces: dict[str, str] = {}
        self.run_forecast_fn = run_forecast_fn
        self.research_mcp_servers = research_mcp_servers
        self.subforecast_depth: int | None = subforecast_depth
        self.post_id: int | None = post_id
        self.current_depth: int = current_depth
        self.parent_slug: str | None = parent_slug


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


def register_nested_trace(key: str, trace: str) -> None:
    """Store a nested sub-agent's reasoning trace under ``key`` for inline
    expansion in the parent forecast's trace. No-op outside a session."""
    session = _current_session.get()
    if session is not None and trace:
        session.nested_traces[key] = trace


def register_premortem_trace(trace: str) -> None:
    """Store a premortem reviewer's trace under the next ordinal key
    (``premortem:0``, ``premortem:1``, …), matching the render order in which
    build_trace expands premortem result blocks. No-op outside a session."""
    session = _current_session.get()
    if session is None or not trace:
        return
    ordinal = sum(1 for k in session.nested_traces if k.startswith("premortem:"))
    session.nested_traces[f"premortem:{ordinal}"] = trace


class ReviewVerdict(StrEnum):
    approve = "approve"
    warn = "warn"
    fail = "fail"


class ReviewResult(BaseModel):
    """Structured output from the premortem reviewer sub-agent."""

    verdict: ReviewVerdict
    assessment: str = Field(
        description="Your full analysis. Explain what you checked, what you "
        "found, and why you reached your verdict. Be thorough — this is "
        "the agent's primary feedback for improving its forecast.",
    )


@dataclass
class ReviewState:
    """Shared mutable state for the reflection → premortem → StructuredOutput gate.

    Written by:
      - reflection tool: sets last_reflection_input (marks reflection_done).
      - premortem tool: records verdicts via record().

    Read by:
      - premortem tool: reads last_reflection_input to build the reviewer prompt.
      - StructuredOutput hook: checks reflection_done and passed.
    """

    consecutive_fails: int = 0
    last_verdict: ReviewVerdict | None = None
    last_review: ReviewResult | None = None
    history: list[dict[str, object]] = field(default_factory=list)
    last_reflection_input: Any = None

    @property
    def reflection_done(self) -> bool:
        """Whether reflection() has been called at least once."""
        return self.last_reflection_input is not None

    @property
    def passed(self) -> bool:
        """Whether premortem() has approved (or auto-approved after 3 fails)."""
        if self.last_verdict is None:
            return False
        if self.last_verdict in (ReviewVerdict.approve, ReviewVerdict.warn):
            return True
        return self.consecutive_fails >= 3

    def store_reflection(self, reflection_input: Any) -> None:
        """Cache reflection input so premortem can retrieve it."""
        self.last_reflection_input = reflection_input

    def record(
        self,
        result: ReviewResult,
        reflection_input: Any = None,
    ) -> None:
        """Record a premortem reviewer verdict."""
        self.last_verdict = result.verdict
        self.last_review = result
        if result.verdict == ReviewVerdict.fail:
            self.consecutive_fails += 1
        else:
            self.consecutive_fails = 0

        entry: dict[str, object] = {"verdict": result.verdict.value}
        if reflection_input is not None:
            if hasattr(reflection_input, "model_dump"):
                entry["input"] = reflection_input.model_dump(mode="json")
            else:
                entry["input"] = reflection_input
        if result.assessment:
            entry["reviewer_assessment"] = result.assessment
        self.history.append(entry)
