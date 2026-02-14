"""ContextVar for retrodict mode cutoff date.

Tools read this to apply time restrictions without hook-based parameter injection.
"""

from contextvars import ContextVar
from datetime import date, datetime, time, timezone

retrodict_cutoff: ContextVar[date | None] = ContextVar("retrodict_cutoff", default=None)
forecasted_post_id: ContextVar[int | None] = ContextVar(
    "forecasted_post_id", default=None
)


def effective_now() -> datetime:
    """Return retrodict cutoff as datetime, or real current time."""
    cutoff = retrodict_cutoff.get()
    if cutoff is not None:
        return datetime.combine(cutoff, time.min, tzinfo=timezone.utc)
    return datetime.now(timezone.utc)
