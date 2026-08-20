"""Running several sources for one question, and surviving the ones that fail.

A condensed tool asks every source that could answer and returns what came
back. That only works if one source's outage costs its own line rather than
the whole answer, which is what :func:`run_lane` buys: the failure is
recorded as something the agent can read and the other lanes still land.

The record is deliberately part of the answer rather than a log line. An
empty lane and a broken lane look identical in the payload otherwise, and
the difference is exactly what decides whether to ask again.
"""

import asyncio
import logging
from collections.abc import Awaitable
from typing import TypedDict

logger = logging.getLogger(__name__)


class LaneFailure(TypedDict):
    """A source that was asked and could not answer."""

    lane: str
    reason: str


async def run_lane[T](
    lane: str,
    work: Awaitable[T],
    empty: T,
    failures: list[LaneFailure],
    deadline: float | None = None,
) -> T:
    """Run one lane, recording rather than raising when it cannot answer.

    `deadline` is for a source whose own backoff outlasts the patience of
    the tool asking it — a lane that waits longer than the answer is worth
    reports itself cold instead of holding the others open.
    """
    reason = ""
    try:
        if deadline is not None:
            return await asyncio.wait_for(work, timeout=deadline)
        return await work
    except TimeoutError:
        reason = f"no answer within {deadline:.0f}s"
    except Exception as exc:
        logger.warning("lane %s failed: %s", lane, exc)
        reason = str(exc) or type(exc).__name__
    failures.append(LaneFailure(lane=lane, reason=reason))
    return empty
