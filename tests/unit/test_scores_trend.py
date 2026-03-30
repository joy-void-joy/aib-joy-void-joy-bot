"""Tests for the `scores trend` command and its helpers."""

from pathlib import Path
from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from aib.devtools.version import load_version_dates
from aib.paths import parse_semver


runner = CliRunner()


class TestParseSemver:
    def test_valid(self) -> None:
        assert parse_semver("3.2.0") == (3, 2, 0)

    def test_ordering(self) -> None:
        versions = ["1.0.0", "0.11.0", "3.2.0", "0.9.2", "2.1.0"]
        result = sorted(versions, key=lambda v: parse_semver(v) or (0, 0, 0))
        assert result == ["0.9.2", "0.11.0", "1.0.0", "2.1.0", "3.2.0"]

    def test_invalid_returns_none(self) -> None:
        assert parse_semver("not-a-version") is None
        assert parse_semver("") is None

    def test_two_part_invalid(self) -> None:
        assert parse_semver("3.2") is None


class TestLoadVersionDates:
    def test_parse_changelog(self, tmp_path: Path) -> None:
        changelog = tmp_path / "CHANGELOG.md"
        changelog.write_text(
            "# Changelog\n\n"
            "## v3.5.0 (2026-03-02)\n\nSome changes\n\n"
            "## v3.4.0 (2026-02-27)\n\nOther changes\n\n"
            "## v1.0.0 (2026-02-14)\n\nInitial\n"
        )
        result = load_version_dates(path=changelog)
        assert result == {
            "3.5.0": "2026-03-02",
            "3.4.0": "2026-02-27",
            "1.0.0": "2026-02-14",
        }

    def test_missing_file(self, tmp_path: Path) -> None:
        result = load_version_dates(path=tmp_path / "nonexistent.md")
        assert result == {}

    def test_no_version_lines(self, tmp_path: Path) -> None:
        changelog = tmp_path / "CHANGELOG.md"
        changelog.write_text("# Changelog\n\nNo versions here.\n")
        result = load_version_dates(path=changelog)
        assert result == {}


def _make_forecast(
    post_id: int,
    version: str,
    peer_score: float,
    timestamp: str = "20260215_120000",
    baseline_score: float = 5.0,
    score_timestamp: float = 1771053678.0,
) -> dict[str, object]:
    return {
        "post_id": post_id,
        "agent_version": version,
        "question_type": "binary",
        "timestamp": timestamp,
        "question_close_time": f"2026-02-{15 + post_id}T12:00:00Z",
        "baseline_score": baseline_score,
        "peer_score": peer_score,
        "score_timestamp": score_timestamp,
    }


@pytest.fixture
def mock_forecasts() -> list[dict[str, object]]:
    return [
        _make_forecast(1, "0.3.1", 10.0),
        _make_forecast(2, "0.3.1", 20.0),
        _make_forecast(3, "0.3.1", 15.0),
        _make_forecast(4, "1.0.0", -5.0),
        _make_forecast(5, "1.0.0", 30.0),
        _make_forecast(6, "1.0.0", 25.0),
        _make_forecast(7, "3.2.0", 50.0),
        _make_forecast(8, "3.2.0", 40.0),
        _make_forecast(9, "3.2.0", 45.0),
    ]


class TestStripCommand:
    def test_basic_invocation(self, mock_forecasts: list[dict[str, object]]) -> None:
        from aib.devtools.scores import app

        with patch(
            "aib.devtools.scores.load_all_forecast_jsons",
            return_value=mock_forecasts,
        ), patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(app, ["strip", "--no-watch", "--min-n", "1"])
        assert result.exit_code == 0
        assert "v0.3.1" in result.output
        assert "v1.0.0" in result.output
        assert "v3.2.0" in result.output

    def test_min_n_filters(self) -> None:
        from aib.devtools.scores import app

        forecasts = [
            _make_forecast(1, "0.3.1", 10.0),
            _make_forecast(4, "1.0.0", -5.0),
            _make_forecast(5, "1.0.0", 30.0),
            _make_forecast(6, "1.0.0", 25.0),
        ]
        with patch(
            "aib.devtools.scores.load_all_forecast_jsons",
            return_value=forecasts,
        ), patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(app, ["strip", "--no-watch", "--min-n", "3"])
        assert result.exit_code == 0
        assert "v1.0.0" in result.output

    def test_no_data(self) -> None:
        from aib.devtools.scores import app

        with patch("aib.devtools.scores.load_all_forecast_jsons", return_value=[]), patch(
            "aib.devtools.scores.refresh_scrape"
        ):
            result = runner.invoke(app, ["strip", "--no-watch"])
        assert result.exit_code == 0


class TestTrendCommand:
    def test_basic_invocation(self, mock_forecasts: list[dict[str, object]]) -> None:
        from aib.devtools.scores import app

        with patch(
            "aib.devtools.scores.load_all_forecast_jsons",
            return_value=mock_forecasts,
        ), patch("aib.devtools.scores.refresh_scrape"):
            result = runner.invoke(app, ["trend", "--no-watch"])
        assert result.exit_code == 0
        assert "Baseline score by forecast date" in result.output
        assert "v0.3.1" in result.output
        assert "v3.2.0" in result.output

    def test_legend_uses_forecast_dates(
        self, mock_forecasts: list[dict[str, object]]
    ) -> None:
        """Legend date ranges should come from forecast timestamps, not resolution dates."""
        from aib.devtools.scores import _load_trend_data

        with patch(
            "aib.devtools.scores.load_all_forecast_jsons",
            return_value=mock_forecasts,
        ):
            result = _load_trend_data()
        assert result is not None
        _, version_forecast_dates = result
        assert "0.3.1" in version_forecast_dates
        assert "3.2.0" in version_forecast_dates
        assert len(version_forecast_dates["0.3.1"]) == 3

    def test_no_data(self) -> None:
        from aib.devtools.scores import app

        with patch("aib.devtools.scores.load_all_forecast_jsons", return_value=[]), patch(
            "aib.devtools.scores.refresh_scrape"
        ):
            result = runner.invoke(app, ["trend", "--no-watch"])
        assert result.exit_code == 0
        assert "No scored forecasts found" in result.output
