"""Tests for aib.scoring — scoring functions and CSV row building."""

import math

import pytest

from aib.scoring import (
    build_score_row,
    compute_baseline_score,
    compute_brier,
    compute_log_score,
    resolve_binary,
    resolve_mc,
    resolve_numeric,
)


class TestComputeBrier:
    def test_perfect_prediction_yes(self) -> None:
        assert compute_brier(1.0, outcome=True) == 0.0

    def test_perfect_prediction_no(self) -> None:
        assert compute_brier(0.0, outcome=False) == 0.0

    def test_worst_prediction_yes(self) -> None:
        assert compute_brier(0.0, outcome=True) == 1.0

    def test_worst_prediction_no(self) -> None:
        assert compute_brier(1.0, outcome=False) == 1.0

    def test_random_baseline(self) -> None:
        assert compute_brier(0.5, outcome=True) == pytest.approx(0.25)
        assert compute_brier(0.5, outcome=False) == pytest.approx(0.25)

    def test_moderate_confidence(self) -> None:
        assert compute_brier(0.7, outcome=True) == pytest.approx(0.09)

    def test_symmetric(self) -> None:
        assert compute_brier(0.7, True) == pytest.approx(compute_brier(0.3, False))


class TestComputeLogScore:
    def test_near_perfect(self) -> None:
        assert compute_log_score(0.999, outcome=True) == pytest.approx(-math.log(0.999))

    def test_random_baseline(self) -> None:
        assert compute_log_score(0.5, outcome=True) == pytest.approx(math.log(2))

    def test_positive_lower_is_better(self) -> None:
        score = compute_log_score(0.8, outcome=True)
        assert score > 0

    def test_better_prediction_lower_score(self) -> None:
        good = compute_log_score(0.9, outcome=True)
        bad = compute_log_score(0.3, outcome=True)
        assert good < bad

    def test_clamping_prevents_infinity(self) -> None:
        result = compute_log_score(0.0, outcome=True)
        assert math.isfinite(result)
        assert result == pytest.approx(-math.log(0.001))

    def test_clamping_upper_bound(self) -> None:
        result = compute_log_score(1.0, outcome=True)
        assert math.isfinite(result)
        assert result == pytest.approx(-math.log(0.999))

    def test_outcome_false(self) -> None:
        assert compute_log_score(0.2, outcome=False) == pytest.approx(-math.log(0.8))


class TestResolveBinary:
    def test_direct_yes(self) -> None:
        assert resolve_binary({"resolution": "yes"}) == "yes"

    def test_direct_no(self) -> None:
        assert resolve_binary({"resolution": "no"}) == "no"

    def test_from_comparison_true(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": True}}) == "yes"

    def test_from_comparison_false(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": False}}) == "no"

    def test_from_comparison_string_yes(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": "yes"}}) == "yes"

    def test_from_comparison_numeric_1(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": 1}}) == "yes"

    def test_from_comparison_numeric_0(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": 0}}) == "no"

    def test_no_resolution(self) -> None:
        assert resolve_binary({}) is None

    def test_ambiguous_resolution(self) -> None:
        assert resolve_binary({"resolution": "ambiguous"}) is None

    def test_comparison_none_actual(self) -> None:
        assert resolve_binary({"comparison": {"actual_value": None}}) is None

    def test_comparison_not_dict(self) -> None:
        assert resolve_binary({"comparison": "invalid"}) is None


class TestResolveNumeric:
    def test_direct_float(self) -> None:
        assert resolve_numeric({"resolution": 42.5}) == 42.5

    def test_direct_int(self) -> None:
        assert resolve_numeric({"resolution": 100}) == 100.0

    def test_string_with_commas(self) -> None:
        assert resolve_numeric({"resolution": "1,234.5"}) == 1234.5

    def test_from_comparison(self) -> None:
        assert resolve_numeric({"comparison": {"actual_value": 100.0}}) == 100.0

    def test_no_resolution(self) -> None:
        assert resolve_numeric({}) is None

    def test_non_numeric_string(self) -> None:
        assert resolve_numeric({"resolution": "not-a-number"}) is None

    def test_comparison_not_dict(self) -> None:
        assert resolve_numeric({"comparison": "invalid"}) is None

    def test_resolution_takes_precedence(self) -> None:
        data: dict[str, object] = {
            "resolution": 42.0,
            "comparison": {"actual_value": 99.0},
        }
        assert resolve_numeric(data) == 42.0


class TestResolveMC:
    def test_direct(self) -> None:
        assert resolve_mc({"resolution": "Option A"}) == "Option A"

    def test_from_comparison(self) -> None:
        assert resolve_mc({"comparison": {"actual_value": "Option B"}}) == "Option B"

    def test_no_resolution(self) -> None:
        assert resolve_mc({}) is None

    def test_numeric_not_string(self) -> None:
        assert resolve_mc({"resolution": 42}) is None

    def test_empty_string(self) -> None:
        assert resolve_mc({"resolution": ""}) is None

    def test_comparison_not_dict(self) -> None:
        assert resolve_mc({"comparison": "invalid"}) is None


class TestComputeBaselineScore:
    def _uniform_cdf(self, n: int = 201) -> list[float]:
        """A uniform CDF: linearly from 0 to 1."""
        return [i / (n - 1) for i in range(n)]

    def _peaked_cdf(self, center: float, n: int = 201) -> list[float]:
        """A CDF peaked near center (sigmoid-shaped)."""
        import math
        return [1.0 / (1.0 + math.exp(-20 * (i / (n - 1) - center))) for i in range(n)]

    def test_binary_positive(self) -> None:
        data: dict[str, object] = {
            "question_type": "binary",
            "probability": 0.9,
            "resolution": "yes",
        }
        score = compute_baseline_score(data)
        assert score is not None
        assert score > 0

    def test_numeric_uniform_scores_zero(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "resolution": 50.0,
            "cdf": self._uniform_cdf(),
            "numeric_bounds": {"range_min": 0.0, "range_max": 100.0},
        }
        score = compute_baseline_score(data)
        assert score is not None
        assert score == pytest.approx(0.0, abs=1.0)

    def test_numeric_peaked_scores_positive(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "resolution": 50.0,
            "cdf": self._peaked_cdf(0.5),
            "numeric_bounds": {"range_min": 0.0, "range_max": 100.0},
        }
        score = compute_baseline_score(data)
        assert score is not None
        assert score > 0

    def test_numeric_peaked_wrong_scores_negative(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "resolution": 10.0,
            "cdf": self._peaked_cdf(0.9),
            "numeric_bounds": {"range_min": 0.0, "range_max": 100.0},
        }
        score = compute_baseline_score(data)
        assert score is not None
        assert score < 0

    def test_numeric_missing_cdf_returns_none(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "resolution": 50.0,
            "numeric_bounds": {"range_min": 0.0, "range_max": 100.0},
        }
        assert compute_baseline_score(data) is None

    def test_numeric_missing_bounds_returns_none(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "resolution": 50.0,
            "cdf": self._uniform_cdf(),
        }
        assert compute_baseline_score(data) is None

    def test_numeric_unresolved_returns_none(self) -> None:
        data: dict[str, object] = {
            "question_type": "numeric",
            "cdf": self._uniform_cdf(),
            "numeric_bounds": {"range_min": 0.0, "range_max": 100.0},
        }
        assert compute_baseline_score(data) is None


class TestBuildScoreRow:
    def test_binary_resolved_yes(self) -> None:
        data: dict[str, object] = {
            "post_id": 123,
            "question_id": 456,
            "question_type": "binary",
            "question_title": "Test question",
            "timestamp": "20260101_120000",
            "probability": 0.8,
            "resolution": "yes",
        }
        row = build_score_row(data, "live")
        assert row["post_id"] == "123"
        assert row["source"] == "live"
        assert row["resolved"] == "True"
        assert float(row["brier"]) == pytest.approx(0.04)
        assert float(row["log_score"]) == pytest.approx(-math.log(0.8), abs=1e-5)

    def test_binary_resolved_no(self) -> None:
        data: dict[str, object] = {
            "post_id": 123,
            "question_type": "binary",
            "question_title": "Test",
            "timestamp": "20260101_120000",
            "probability": 0.8,
            "resolution": "no",
        }
        row = build_score_row(data, "live")
        assert row["resolved"] == "True"
        assert float(row["brier"]) == pytest.approx(0.64)

    def test_binary_unresolved(self) -> None:
        data: dict[str, object] = {
            "post_id": 123,
            "question_type": "binary",
            "question_title": "Test",
            "timestamp": "20260101_120000",
            "probability": 0.5,
        }
        row = build_score_row(data, "live")
        assert row["resolved"] == "False"
        assert row["brier"] == ""
        assert row["log_score"] == ""

    def test_numeric_resolved_within_ci(self) -> None:
        data: dict[str, object] = {
            "post_id": 789,
            "question_type": "numeric",
            "question_title": "Numeric Q",
            "timestamp": "20260101_120000",
            "median": 100.0,
            "confidence_interval": [80.0, 120.0],
            "resolution": "105",
        }
        row = build_score_row(data, "retrodict")
        assert row["resolved"] == "True"
        assert row["source"] == "retrodict"
        assert float(row["abs_error"]) == pytest.approx(5.0)
        assert row["within_ci"] == "True"

    def test_numeric_resolved_outside_ci(self) -> None:
        data: dict[str, object] = {
            "post_id": 789,
            "question_type": "numeric",
            "question_title": "Numeric Q",
            "timestamp": "20260101_120000",
            "median": 100.0,
            "confidence_interval": [80.0, 120.0],
            "resolution": "200",
        }
        row = build_score_row(data, "live")
        assert row["within_ci"] == "False"

    def test_mc_resolved(self) -> None:
        data: dict[str, object] = {
            "post_id": 999,
            "question_type": "multiple_choice",
            "question_title": "MC Q",
            "timestamp": "20260101_120000",
            "probabilities": {"A": 0.5, "B": 0.3, "C": 0.2},
            "resolution": "A",
        }
        row = build_score_row(data, "live")
        assert row["resolved"] == "True"
        assert float(row["log_score"]) == pytest.approx(-math.log(0.5))

    def test_mc_unresolved(self) -> None:
        data: dict[str, object] = {
            "post_id": 999,
            "question_type": "multiple_choice",
            "question_title": "MC Q",
            "timestamp": "20260101_120000",
            "probabilities": {"A": 0.5, "B": 0.3, "C": 0.2},
        }
        row = build_score_row(data, "live")
        assert row["resolved"] == "False"

    def test_title_truncated(self) -> None:
        data: dict[str, object] = {
            "post_id": 1,
            "question_type": "binary",
            "question_title": "x" * 200,
            "timestamp": "20260101_120000",
            "probability": 0.5,
        }
        row = build_score_row(data, "live")
        assert len(row["question_title"]) == 80

    def test_agent_version_preserved(self) -> None:
        data: dict[str, object] = {
            "post_id": 1,
            "question_type": "binary",
            "question_title": "Test",
            "timestamp": "20260101_120000",
            "probability": 0.5,
            "agent_version": "0.3.0",
        }
        row = build_score_row(data, "live")
        assert row["agent_version"] == "0.3.0"
