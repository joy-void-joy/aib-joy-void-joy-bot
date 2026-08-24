"""What an A/B run leaves behind when it does not reach its summary.

An experiment is hours of forecasts against a hand-picked question set, and
Ctrl+C is how most of them end. The command kept its record in a `gather`
result and printed it at exit, so the one path that most needs the record —
the interrupted one — was the only path that discarded it entirely.

These pin the record to disk instead, written as each arm settles rather than
once they all have, and asserted by *reading the file while arms are still
running*. Collecting at exit passes every other test one could write about
this: the arms are all in the record in the end either way.
"""

import asyncio
from datetime import datetime, timezone
from pathlib import Path

import pytest

from aib.cli import ArmResult, Experiment, run_arm
from aib.variants import Variant


def experiment(tmp_path: Path, **overrides: object) -> Experiment:
    fields: dict[str, object] = {
        "path": tmp_path / "20260825_120000.json",
        "version": "1.4.0",
        "baseline": "shipped",
        "variants": ["shipped", "condensed"],
        "question_ids": [41521, 41454],
        "retrodict": True,
        "concurrency": 2,
        "started_at": datetime(2026, 8, 25, 12, 0, tzinfo=timezone.utc),
    }
    run = Experiment.model_validate(fields | overrides)
    run.save()
    return run


def on_disk(run: Experiment) -> Experiment:
    """Re-read the trace, as the reader of an interrupted run would."""
    return Experiment.read(run.path)


def test_an_arm_reaches_disk_before_it_finishes(tmp_path: Path) -> None:
    """The property the whole change is for, and the one a write-at-exit breaks."""
    run = experiment(tmp_path)

    run.open_arm(41521, "shipped")

    assert [(a.post_id, a.variant, a.status) for a in on_disk(run).arms] == [
        (41521, "shipped", "running")
    ]


def test_a_cancelled_arm_is_still_named_by_the_trace(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    """Ctrl+C reaches an in-flight arm as cancellation, and it must not erase it.

    The arm is cancelled while its process is still streaming — the state a
    real interrupt catches most arms in — and the assertion reads the file
    rather than the object, because the object dies with the process.
    """

    class NeverFinishing:
        def __init__(self) -> None:
            self.stdout = asyncio.StreamReader()
            self.returncode: int | None = None

        async def wait(self) -> int:
            await asyncio.Event().wait()
            return 0

    async def fake_exec(*args: object, **kwargs: object) -> NeverFinishing:
        return NeverFinishing()

    monkeypatch.setattr(asyncio, "create_subprocess_exec", fake_exec)
    run = experiment(tmp_path)

    async def start_then_cancel() -> None:
        arm = asyncio.create_task(
            run_arm(41521, Variant(name="shipped"), True, asyncio.Semaphore(2), run)
        )
        while not run.arms:
            await asyncio.sleep(0)
        arm.cancel()
        with pytest.raises(asyncio.CancelledError):
            await arm

    asyncio.run(start_then_cancel())

    kept = on_disk(run).arms
    assert [(a.post_id, a.status) for a in kept] == [(41521, "running")]


def test_a_finished_arm_records_how_its_process_exited(tmp_path: Path) -> None:
    """`ok` and `failed` are what the summary counts, so an arm has to carry them."""
    run = experiment(tmp_path)
    passing = run.open_arm(41521, "shipped")
    failing = run.open_arm(41454, "condensed")

    passing.close(0, 61.0, ["done"])
    failing.close(1, 12.0, ["boom"])
    run.save()

    assert [(a.status, a.returncode) for a in on_disk(run).arms] == [
        ("ok", 0),
        ("failed", 1),
    ]


def test_the_tail_keeps_only_the_end_of_a_long_arm() -> None:
    """The summary reprints how a failed arm ended, not the run it printed live."""
    arm = ArmResult(post_id=41521, variant="shipped")

    arm.close(1, 1.0, [str(i) for i in range(100)])

    assert arm.tail.splitlines()[-1] == "99"
    assert len(arm.tail.splitlines()) < 100


def test_the_trace_says_what_the_experiment_was_comparing(tmp_path: Path) -> None:
    """A record of arms that does not name the control is not a comparison."""
    written = on_disk(experiment(tmp_path, interrupted=True))

    assert written.baseline == "shipped"
    assert written.variants == ["shipped", "condensed"]
    assert written.question_ids == [41521, 41454]
    assert written.interrupted is True


def test_the_trace_does_not_write_its_own_path_into_itself(tmp_path: Path) -> None:
    """Where the file is is not part of what the experiment did."""
    run = experiment(tmp_path)

    assert "path" not in run.model_dump()
