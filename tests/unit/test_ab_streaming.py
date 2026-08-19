"""What an A/B arm shows while it is running, rather than once it has finished.

An arm is a whole forecast — tens of minutes — and the command collected its
output and printed at exit, so it showed nothing for the entire run. That is
not a cosmetic difference: a command printing nothing for half an hour cannot
be told apart from one that has hung, and it was reported as a hang.
"""

import asyncio

import pytest

from aib.cli import ARM_LINE_LIMIT, stream_arm


async def test_a_line_is_printed_before_the_stream_ends(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """The property the whole change is for, and the one a buffer breaks.

    Asserted against output read *while the arm is still open*, because
    collecting at exit passes every other test one could write about this —
    the lines are all there in the end either way.
    """
    reader = asyncio.StreamReader()
    reader.feed_data(b"first line\n")
    streaming = asyncio.create_task(stream_arm(reader, "[45181 baseline] "))
    await asyncio.sleep(0)

    while_still_running = capsys.readouterr().out

    reader.feed_eof()
    await streaming
    assert "first line" in while_still_running


async def test_every_line_says_which_arm_it_came_from(
    capsys: pytest.CaptureFixture[str],
) -> None:
    """Arms run concurrently into one terminal, so an unlabelled line is orphaned."""
    reader = asyncio.StreamReader()
    reader.feed_data(b"one\ntwo\n")
    reader.feed_eof()

    await stream_arm(reader, "[45181 baseline] ")

    printed = capsys.readouterr().out.splitlines()
    assert printed == ["[45181 baseline] one", "[45181 baseline] two"]


async def test_the_lines_are_kept_as_well_as_printed() -> None:
    """The summary reports how a failed arm ended, and a stream reads once."""
    reader = asyncio.StreamReader()
    reader.feed_data(b"one\ntwo\n")
    reader.feed_eof()

    assert await stream_arm(reader, "") == ["one", "two"]


async def test_a_line_without_a_final_newline_is_not_dropped() -> None:
    """A process killed mid-line still said what it managed to say."""
    reader = asyncio.StreamReader()
    reader.feed_data(b"cut off here")
    reader.feed_eof()

    assert await stream_arm(reader, "") == ["cut off here"]


async def test_a_tool_result_longer_than_the_default_buffer_is_read() -> None:
    """A forecast prints tool results that exceed a StreamReader's 64 KiB default.

    The default does not truncate, it raises — so an arm would die on its own
    output partway through a run, and the failure would look like the forecast
    rather than the reading of it. Both halves are asserted: that the hazard
    is real, and that the declared limit answers it.
    """
    long_line = b"x" * (128 * 1024) + b"\n"

    default_limit = asyncio.StreamReader()
    default_limit.feed_data(long_line)
    default_limit.feed_eof()
    with pytest.raises(ValueError):
        await stream_arm(default_limit, "")

    declared = asyncio.StreamReader(limit=ARM_LINE_LIMIT)
    declared.feed_data(long_line)
    declared.feed_eof()

    assert await stream_arm(declared, "") == [long_line.decode().splitlines()[0]]
