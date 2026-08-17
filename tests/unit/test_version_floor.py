"""Tests for the minimum version the cross-version views chart from."""

import json
from collections.abc import Iterator
from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from aib.paths import parse_trace_version, versions_at_least


runner = CliRunner()


def write_forecast(traces: Path, version: str, post_id: int, score: float) -> None:
    """Write one scored forecast under a version's forecasts directory."""
    directory = traces / version / "forecasts" / str(post_id)
    directory.mkdir(parents=True)
    (directory / "20260215_120000.json").write_text(
        json.dumps(
            {
                "post_id": post_id,
                "agent_version": version,
                "question_type": "binary",
                "timestamp": "20260215_120000",
                "baseline_score": score,
                "peer_score": score,
                "score_timestamp": 1771053678.0,
            }
        )
    )


@pytest.fixture
def traces(tmp_path: Path) -> Iterator[Path]:
    """A traces tree: one version below the floor, two at or above it."""
    root = tmp_path / "traces"
    write_forecast(root, "6.3.0", 1, 10.0)
    write_forecast(root, "7.0.0", 2, 20.0)
    write_forecast(root, "7.1.0+sonnet-max", 3, 30.0)
    with patch("aib.paths.traces_path", return_value=root):
        yield root


class TestParseTraceVersion:
    def test_plain_release(self) -> None:
        assert parse_trace_version("7.0.0") == (7, 0, 0)

    def test_variant_arm_answers_with_its_release(self) -> None:
        assert parse_trace_version("7.0.0+sonnet-max") == (7, 0, 0)

    def test_directory_that_names_no_release(self) -> None:
        assert parse_trace_version("scratch") is None


class TestVersionsAtLeast:
    def test_the_floor_itself_is_included(self, traces: Path) -> None:
        assert versions_at_least("7.0.0") == ["7.0.0", "7.1.0+sonnet-max"]

    def test_a_lower_floor_widens_the_scope(self, traces: Path) -> None:
        assert versions_at_least("6.0.0") == [
            "6.3.0",
            "7.0.0",
            "7.1.0+sonnet-max",
        ]

    def test_a_floor_above_every_version_is_empty(self, traces: Path) -> None:
        assert versions_at_least("8.0.0") == []

    def test_a_floor_that_is_not_a_version_is_rejected(self, traces: Path) -> None:
        with pytest.raises(ValueError):
            versions_at_least("7.0")


class TestStripHonoursTheFloor:
    def test_earlier_versions_are_left_out_by_default(self, traces: Path) -> None:
        from aib.devtools.scores import app

        with patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(app, ["strip", "--no-watch"])

        assert result.exit_code == 0
        assert "v7.0.0" in result.output
        assert "v6.3.0" not in result.output

    def test_a_zero_floor_charts_every_version(self, traces: Path) -> None:
        from aib.devtools.scores import app

        with patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(
                app, ["strip", "--no-watch", "--min-version", "0.0.0"]
            )

        assert result.exit_code == 0
        assert "v6.3.0" in result.output
        assert "v7.0.0" in result.output

    def test_a_malformed_floor_is_a_usage_error(self, traces: Path) -> None:
        from aib.devtools.scores import app

        with patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(app, ["strip", "--no-watch", "--min-version", "7"])

        assert result.exit_code != 0
