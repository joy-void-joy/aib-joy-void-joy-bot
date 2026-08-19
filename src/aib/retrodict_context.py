"""ContextVar for retrodict mode cutoff date.

Tools read this to apply time restrictions without hook-based parameter injection.

It is process state, and that is the whole of what bounds where it reaches.
A forecast's tool groups are hosted in the process that sets it, so a tool
called from that session reads the cutoff it was opened under. The same tool
modules are also served over stdio by `lup-devtools agent serve-tools`, for a
session a native harness tree launches — a different process, where nothing
sets this and every tool answers with today's data. That is right for an
interactive session and would be silently wrong for a retrodict one, because
a tool reading an unset cutoff does not fail: it returns confident
post-cutoff data, and nothing downstream can tell.

Nothing crosses that boundary today. A retrodict runs in process, and lup
refuses to relaunch a hosted tool group as a subprocess rather than spawning
one that would answer from defaults. Both halves are load-bearing: serving
these groups to an out-of-process session is not a transport change, it is a
change to what they say.
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
