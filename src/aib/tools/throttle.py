"""Rate limiting combining concurrency control and temporal spacing.

Provides a generic Throttle class that enforces both a maximum number of
concurrent requests (semaphore) and a minimum time interval between request
starts. This prevents API rate limit violations during concurrent forecast
sessions in tournament mode.

Per-API throttle instances are module-level singletons, configured from
settings, and shared across all concurrent forecast sessions in the process.
"""

import asyncio
import time
from types import TracebackType

from aib.config import settings


class _LoopState:
    """Per-event-loop state for a Throttle instance."""

    __slots__ = ("semaphore", "last_request_time", "lock")

    def __init__(self, semaphore: asyncio.Semaphore) -> None:
        self.semaphore = semaphore
        self.last_request_time: float = 0.0
        self.lock = asyncio.Lock()


class Throttle:
    """Async context manager enforcing concurrency limits and temporal spacing.

    Combines an asyncio.Semaphore (max concurrent) with a minimum time interval
    between request starts. Creates internal state lazily per-event-loop to
    avoid "bound to a different event loop" errors.

    Args:
        max_concurrent: Maximum simultaneous requests allowed.
        min_interval: Minimum seconds between consecutive request starts.
            0.0 disables temporal spacing (pure concurrency limiting).
    """

    def __init__(self, max_concurrent: int, min_interval: float = 0.0) -> None:
        self._max_concurrent = max_concurrent
        self._min_interval = min_interval
        self._state: dict[int, _LoopState] = {}

    def _get_state(self) -> _LoopState:
        loop = asyncio.get_running_loop()
        loop_id = id(loop)
        if loop_id not in self._state:
            self._state[loop_id] = _LoopState(
                asyncio.Semaphore(self._max_concurrent),
            )
        return self._state[loop_id]

    async def __aenter__(self) -> None:
        state = self._get_state()
        await state.semaphore.acquire()
        if self._min_interval > 0:
            async with state.lock:
                if state.last_request_time > 0:
                    elapsed = time.monotonic() - state.last_request_time
                    remaining = self._min_interval - elapsed
                    if remaining > 0:
                        await asyncio.sleep(remaining)
                state.last_request_time = time.monotonic()

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self._get_state().semaphore.release()


# Per-API throttle singletons
exa_throttle = Throttle(max_concurrent=settings.exa_max_concurrent)
wayback_throttle = Throttle(max_concurrent=settings.wayback_max_concurrent)
wikipedia_throttle = Throttle(max_concurrent=settings.wikipedia_max_concurrent)
