"""What an A/B arm reports back beyond its exit code.

An experiment exists to compare arms, and the summary answered only whether
each one's process finished. Two arms could disagree by thirty points, cost
four times as much, or skip their adversarial review entirely, and the run
that was launched to notice exactly that printed `1/1 ok` for both.

The arm is a separate process, so nothing it computed returns through the
exit code. These pin the forecast it wrote as the place that is read back.
"""

from datetime import datetime, timezone
from pathlib import Path

import pytest

from aib.agent.history import SavedForecast
from aib.cli import (
    ArmResult,
    Experiment,
    arm_detail,
    format_prediction,
    read_arm_forecast,
    render_summary,
)


def saved(**overrides: object) -> SavedForecast:
    fields: dict[str, object] = {
        "question_id": 41521,
        "post_id": 41521,
        "question_title": "Will it happen?",
        "question_type": "binary",
        "timestamp": "20260825_120000",
        "summary": "Status quo holds.",
        "factors": [],
        "probability": 0.05,
    }
    return SavedForecast.model_validate(fields | overrides)


def write(root: Path, version: str, post_id: int, forecast: SavedForecast) -> Path:
    question_dir = root / "notes" / "traces" / version / "forecasts" / str(post_id)
    question_dir.mkdir(parents=True, exist_ok=True)
    path = question_dir / f"{forecast.timestamp}.json"
    path.write_text(forecast.model_dump_json(indent=2), encoding="utf-8")
    return path


class TestFormatPrediction:
    """Every question type collapses to one comparable field."""

    def test_binary_reads_as_a_percentage(self) -> None:
        assert format_prediction(saved(probability=0.05)) == "5.0%"

    def test_multiple_choice_names_the_winning_option(self) -> None:
        forecast = saved(
            question_type="multiple_choice",
            probability=None,
            probabilities={"Yes": 0.7, "No": 0.2, "Maybe": 0.1},
        )
        assert format_prediction(forecast) == "Yes 70%"

    def test_numeric_reads_as_its_median(self) -> None:
        forecast = saved(question_type="numeric", probability=None, median=9100.0)
        assert format_prediction(forecast) == "median 9,100"

    def test_a_forecast_with_no_answer_is_not_a_crash(self) -> None:
        assert format_prediction(saved(probability=None)) == "—"


class TestRecordOutcome:
    """What the arm took from the forecast it left behind."""

    def test_cost_sums_the_orchestrator_and_its_subagents(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed")
        arm.record_outcome(
            saved(cost_usd=4.5, tool_metrics={"subagent_cost_usd": 16.1275})
        )
        assert arm.cost_usd is not None
        assert round(arm.cost_usd, 4) == 20.6275

    def test_tool_counts_come_across(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed")
        arm.record_outcome(
            saved(tool_metrics={"total_tool_calls": 99, "total_errors": 6})
        )
        assert arm.tool_calls == 99
        assert arm.tool_errors == 6

    def test_the_last_premortem_verdict_is_carried(self) -> None:
        """A gate that did not run must be visible from the summary."""
        arm = ArmResult(post_id=41521, variant="condensed")
        arm.record_outcome(
            saved(revision_history=[{"verdict": "fail"}, {"verdict": "warn"}])
        )
        assert arm.premortem_verdict == "warn"

    def test_a_forecast_without_metrics_records_no_counts(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed")
        arm.record_outcome(saved())
        assert arm.prediction == "5.0%"
        assert arm.tool_calls is None
        assert arm.premortem_verdict is None


class TestReadArmForecast:
    """Which file on disk is this arm's."""

    def test_reads_from_the_variant_directory(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        import aib.paths

        write(tmp_path, "1.4.0+condensed", 41521, saved(probability=0.05))
        write(tmp_path, "1.4.0+direct-research", 41521, saved(probability=0.42))
        monkeypatch.setattr(
            aib.paths, "traces_path", lambda: tmp_path / "notes" / "traces"
        )

        found = read_arm_forecast(41521, "1.4.0", "condensed")
        assert found is not None
        assert found.probability == 0.05

    def test_takes_the_newest_by_the_timestamp_it_carries(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """A partial run prefixes its filename, so the record's field decides."""
        import aib.paths

        write(tmp_path, "1.4.0+condensed", 41521, saved(timestamp="20260825_090000"))
        newer = saved(timestamp="20260825_140000", probability=0.31)
        path = write(tmp_path, "1.4.0+condensed", 41521, newer)
        path.rename(path.with_name(f"PARTIAL_{path.name}"))
        monkeypatch.setattr(
            aib.paths, "traces_path", lambda: tmp_path / "notes" / "traces"
        )

        found = read_arm_forecast(41521, "1.4.0", "condensed")
        assert found is not None
        assert found.probability == 0.31

    def test_a_missing_directory_is_not_an_error(self, tmp_path: Path) -> None:
        assert read_arm_forecast(999, "1.4.0", "nonexistent") is None


class TestArmDetail:
    """The line one arm gets under its question."""

    def test_a_finished_arm_leads_with_its_prediction(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed", status="ok")
        arm.record_outcome(
            saved(
                cost_usd=4.5, tool_metrics={"total_tool_calls": 99, "total_errors": 6}
            )
        )
        line = arm_detail(arm)
        assert line.startswith("5.0%")
        assert "99 calls" in line
        assert "6 err" in line
        assert "$4.50" in line

    def test_a_cut_off_arm_says_so_instead(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed")
        assert "cut off" in arm_detail(arm)

    def test_a_failed_arm_reports_its_exit_code(self) -> None:
        arm = ArmResult(
            post_id=41521, variant="condensed", status="failed", returncode=1
        )
        assert "exited 1" in arm_detail(arm)

    def test_an_arm_that_wrote_nothing_is_distinguished_from_one_that_did(self) -> None:
        arm = ArmResult(post_id=41521, variant="condensed", status="ok")
        assert "wrote no forecast" in arm_detail(arm)


class TestRenderSummary:
    """The block the run prints when it is over."""

    def experiment(self, tmp_path: Path) -> Experiment:
        run = Experiment.model_validate(
            {
                "path": tmp_path / "20260825_120000.json",
                "version": "8.1.2",
                "baseline": "condensed",
                "variants": ["condensed", "direct-research"],
                "question_ids": [45181, 45203],
                "retrodict": False,
                "concurrency": 2,
                "started_at": datetime(2026, 8, 25, 12, 0, tzinfo=timezone.utc),
            }
        )
        settled = [
            (
                "condensed",
                45181,
                saved(
                    probability=0.05,
                    cost_usd=4.5,
                    tool_metrics={
                        "subagent_cost_usd": 13.92,
                        "total_tool_calls": 99,
                        "total_errors": 6,
                    },
                    revision_history=[{"verdict": "approve"}],
                ),
                1380.0,
            ),
            (
                "direct-research",
                45181,
                saved(
                    probability=0.07,
                    cost_usd=6.1,
                    tool_metrics={
                        "subagent_cost_usd": 15.0,
                        "total_tool_calls": 132,
                        "total_errors": 9,
                    },
                    revision_history=[{"verdict": "warn"}],
                ),
                1500.0,
            ),
            (
                "condensed",
                45203,
                saved(
                    question_type="numeric",
                    probability=None,
                    median=9100.0,
                    cost_usd=3.2,
                    tool_metrics={
                        "subagent_cost_usd": 8.0,
                        "total_tool_calls": 61,
                        "total_errors": 0,
                    },
                    revision_history=[{"verdict": "approve"}],
                ),
                900.0,
            ),
        ]
        for variant, post_id, forecast, secs in settled:
            arm = run.open_arm(post_id, variant)
            arm.close(0, secs, ["done"])
            arm.record_outcome(forecast)
        broken = run.open_arm(45203, "direct-research")
        broken.close(1, 42.0, ["Traceback...", "RuntimeError: no key"])
        return run

    def test_prints_each_arm_prediction_under_its_question(
        self, tmp_path: Path
    ) -> None:
        rendered = render_summary(self.experiment(tmp_path))
        print("\n" + rendered)

        assert "5.0%" in rendered
        assert "7.0%" in rendered
        assert "median 9,100" in rendered

    def test_rolls_up_spend_and_tool_use_per_variant(self, tmp_path: Path) -> None:
        rendered = render_summary(self.experiment(tmp_path))

        assert "$29.62" in rendered  # 4.5 + 13.92 + 3.2 + 8.0
        assert "160 tool calls (6 errors)" in rendered

    def test_names_the_question_whose_gate_did_not_approve(
        self, tmp_path: Path
    ) -> None:
        """A premortem that warned is the reason to open the trace."""
        rendered = render_summary(self.experiment(tmp_path))

        assert "45181 premortem: warn" in rendered

    def test_a_failed_arm_keeps_its_last_line_of_output(self, tmp_path: Path) -> None:
        rendered = render_summary(self.experiment(tmp_path))

        assert "45203 exited 1" in rendered
        assert "RuntimeError: no key" in rendered
