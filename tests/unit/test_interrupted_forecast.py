"""What a forecast leaves behind when it is interrupted rather than failed.

`save_partial` writes the reasoning collected so far, and it hung off an
`except Exception` — which is every way a run can end *except* the two that
actually end long ones. Ctrl+C is `KeyboardInterrupt`; the same interrupt
reaching a task inside a `gather` — how `tournament`, `retrodict` and `ab`
run their questions — is `CancelledError`. Both are `BaseException`, so both
went straight past the handler, and half an hour of research was discarded
precisely when the user had asked to stop and keep it.

This pins the handler's reach rather than driving a whole forecast: what
regressed was which exceptions the clause names, and that is what a reader
changing it would break.
"""

import asyncio

import pytest

from aib.agent.core import FORECAST_ABORTED


@pytest.mark.parametrize(
    "ending",
    [KeyboardInterrupt, asyncio.CancelledError, RuntimeError],
    ids=["ctrl-c", "cancelled-inside-a-gather", "an-ordinary-failure"],
)
def test_every_way_a_run_ends_without_a_forecast_reaches_the_partial_save(
    ending: type[BaseException],
) -> None:
    """A partial trace is worth most on the interrupt path, not least."""
    reached = False
    try:
        raise ending("ended before a forecast")
    except FORECAST_ABORTED:
        reached = True

    assert reached


def test_an_interrupt_is_not_merely_an_exception() -> None:
    """The regression guard: `except Exception` passes every test above but one.

    Without this, narrowing the clause back to `Exception` still satisfies the
    ordinary-failure case and reads as harmless.
    """
    assert not issubclass(KeyboardInterrupt, Exception)
    assert not issubclass(asyncio.CancelledError, Exception)
