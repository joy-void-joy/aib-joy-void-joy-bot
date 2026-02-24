"""Tests for the reflection tool."""

import math
from pathlib import Path

import pytest

from aib.agent.models import BinaryEstimate, Factor, NumericEstimate, NumericSupport
from aib.tools.reflection import (
    ReflectionInput,
    ReflectionOutput,
    ReviewResult,
    ReviewState,
    ReviewVerdict,
    compute_reflection,
    _append_reflection,
    _build_reviewer_prompt,
)


def _make_binary_input(
    factors: list[Factor] | None = None,
    tentative_logit: float = 0.0,
    tentative_probability: float | None = None,
) -> ReflectionInput:
    """Helper to create a ReflectionInput for binary questions."""
    if tentative_probability is None:
        tentative_probability = 1 / (1 + math.exp(-tentative_logit))
    return ReflectionInput(
        factors=factors or [],
        tentative_estimate=BinaryEstimate(
            logit=tentative_logit,
            probability=tentative_probability,
        ),
        assessment="Test assessment.",
        tool_audit="No tools used.",
        process_reflection="Test reflection.",
    )


def _make_numeric_input(
    factors: list[Factor] | None = None,
    center: float = 100.0,
    low: float = 90.0,
    high: float = 110.0,
) -> ReflectionInput:
    """Helper to create a ReflectionInput for numeric questions."""
    return ReflectionInput(
        factors=factors or [],
        tentative_estimate=NumericEstimate(center=center, low=low, high=high),
        assessment="Test assessment.",
        tool_audit="No tools used.",
        process_reflection="Test reflection.",
    )


class TestComputeReflectionBinary:
    """Tests for binary question reflection computation."""

    def test_aligned_factors_no_gap(self) -> None:
        """When factor_sum ≈ tentative_logit, gap should be near zero."""
        factors = [
            Factor(description="Evidence A", logit=1.0, confidence=0.8),
            Factor(description="Evidence B", logit=-0.5, confidence=0.6),
        ]
        factor_sum = 1.0 * 0.8 + (-0.5) * 0.6  # 0.5
        inp = _make_binary_input(factors=factors, tentative_logit=factor_sum)

        result = compute_reflection(inp, "binary")

        assert isinstance(result, ReflectionOutput)
        assert result.gap_pp is not None
        assert abs(result.gap_pp) < 0.1
        assert result.logit_gap is not None
        assert abs(result.logit_gap) < 0.01

    def test_large_gap(self) -> None:
        """Factor sum of +2.0 with tentative logit of +1.0 should show a gap."""
        factors = [
            Factor(description="Strong evidence", logit=2.0, confidence=1.0),
        ]
        inp = _make_binary_input(factors=factors, tentative_logit=1.0)

        result = compute_reflection(inp, "binary")

        assert result.factor_sum == pytest.approx(2.0)
        assert result.tentative_logit == 1.0
        assert result.logit_gap == pytest.approx(-1.0)
        # sigmoid(2.0) ≈ 0.881, sigmoid(1.0) ≈ 0.731 → gap ≈ -15pp
        assert result.gap_pp is not None
        assert result.gap_pp < -10

    def test_factor_implied_probability(self) -> None:
        """Factor implied probability should be sigmoid(factor_sum)."""
        factors = [
            Factor(description="Moderate positive", logit=1.0, confidence=1.0),
        ]
        inp = _make_binary_input(
            factors=factors, tentative_logit=1.0, tentative_probability=0.73
        )

        result = compute_reflection(inp, "binary")

        expected = 1 / (1 + math.exp(-1.0))
        assert result.factor_implied_probability == pytest.approx(expected)
        assert result.tentative_probability == pytest.approx(0.73)

    def test_contradictory_direction(self) -> None:
        """All positive factors with negative tentative logit."""
        factors = [
            Factor(description="Positive A", logit=1.0, confidence=0.8),
            Factor(description="Positive B", logit=0.5, confidence=1.0),
        ]
        inp = _make_binary_input(factors=factors, tentative_logit=-1.0)

        result = compute_reflection(inp, "binary")

        assert result.factor_sum > 0
        assert result.tentative_logit is not None
        assert result.tentative_logit < 0
        assert result.logit_gap is not None
        assert result.logit_gap < -1.0

    def test_empty_factors(self) -> None:
        """Empty factor list should give factor_sum = 0."""
        inp = _make_binary_input(factors=[], tentative_logit=0.5)

        result = compute_reflection(inp, "binary")

        assert result.factor_count == 0
        assert result.factor_sum == 0.0
        assert result.factor_implied_probability == pytest.approx(0.5)


class TestComputeReflectionNumeric:
    """Tests for numeric question reflection with NumericSupport factors."""

    def test_distribution_metrics_computed(self) -> None:
        """Numeric factors with NumericSupport should produce distribution metrics."""
        factors = [
            Factor(
                description="Historical avg",
                supports=NumericSupport(center=100.0, low=90.0, high=110.0),
                logit=1.0,
                confidence=1.0,
            ),
            Factor(
                description="Recent uptick",
                supports=NumericSupport(center=120.0, low=110.0, high=130.0),
                logit=0.5,
                confidence=1.0,
            ),
        ]
        inp = _make_numeric_input(factors=factors, center=108.0, low=95.0, high=120.0)

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is not None
        assert result.factor_implied_probability is None
        assert result.gap_pp is None
        # Weighted avg: (100*1.0 + 120*0.5) / 1.5 = 106.67
        assert result.distribution_metrics.implied_median == pytest.approx(
            106.67, abs=0.01
        )

    def test_weighted_average_by_effective_logit(self) -> None:
        """Distribution metrics should weight by abs(effective_logit)."""
        factors = [
            Factor(
                description="Strong signal",
                supports=NumericSupport(center=200.0, low=180.0, high=220.0),
                logit=2.0,
                confidence=1.0,
            ),
            Factor(
                description="Weak signal",
                supports=NumericSupport(center=100.0, low=80.0, high=120.0),
                logit=0.5,
                confidence=1.0,
            ),
        ]
        inp = _make_numeric_input(factors=factors, center=180.0, low=160.0, high=200.0)

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is not None
        # Weighted: (200*2.0 + 100*0.5) / 2.5 = 180.0
        assert result.distribution_metrics.implied_median == pytest.approx(180.0)

    def test_spread_ratio(self) -> None:
        """Spread ratio = agent's range / implied range."""
        factors = [
            Factor(
                description="Evidence",
                supports=NumericSupport(center=50.0, low=40.0, high=60.0),
                logit=1.0,
                confidence=1.0,
            ),
        ]
        # Agent range = 30, implied range = 20 → ratio = 1.5
        inp = _make_numeric_input(factors=factors, center=50.0, low=35.0, high=65.0)

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is not None
        assert result.distribution_metrics.spread_ratio == pytest.approx(1.5)

    def test_median_gap_as_pct(self) -> None:
        """Median gap should be expressed as % of implied range."""
        factors = [
            Factor(
                description="Evidence",
                supports=NumericSupport(center=100.0, low=80.0, high=120.0),
                logit=1.0,
                confidence=1.0,
            ),
        ]
        # Agent center=110, implied center=100, implied range=40 → gap=10, pct=25%
        inp = _make_numeric_input(factors=factors, center=110.0, low=90.0, high=130.0)

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is not None
        assert result.distribution_metrics.median_gap == pytest.approx(10.0)
        assert result.distribution_metrics.median_gap_pct == pytest.approx(25.0)

    def test_empty_factors_no_metrics(self) -> None:
        """Empty factor list should give no distribution metrics."""
        inp = _make_numeric_input(factors=[])

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is None

    def test_zero_weight_factors_no_metrics(self) -> None:
        """Factors with zero effective logit should produce no metrics."""
        factors = [
            Factor(
                description="Zero weight",
                supports=NumericSupport(center=100.0, low=90.0, high=110.0),
                logit=0.0,
                confidence=1.0,
            ),
        ]
        inp = _make_numeric_input(factors=factors)

        result = compute_reflection(inp, "numeric")

        assert result.distribution_metrics is None


class TestNeutralAndDominant:
    """Tests for neutral factor detection and dominant factor."""

    def test_neutral_count_threshold(self) -> None:
        """Factors with |logit| < 0.1 should be counted as neutral."""
        factors = [
            Factor(description="Neutral", logit=0.05, confidence=1.0),
            Factor(description="Also neutral", logit=-0.03, confidence=1.0),
            Factor(description="Not neutral", logit=0.5, confidence=1.0),
        ]
        inp = _make_binary_input(factors=factors, tentative_logit=0.5)

        result = compute_reflection(inp, "binary")

        assert result.neutral_factor_count == 2

    def test_dominant_factor(self) -> None:
        """Should identify the factor with the largest effective logit."""
        factors = [
            Factor(description="Weak", logit=0.3, confidence=1.0),
            Factor(description="Strong", logit=2.0, confidence=0.9),
            Factor(description="Medium", logit=-1.0, confidence=0.8),
        ]
        inp = _make_binary_input(factors=factors, tentative_logit=1.0)

        result = compute_reflection(inp, "binary")

        assert result.dominant_factor == "Strong"
        assert result.dominant_effective_logit == pytest.approx(1.8)


class TestFactorBreakdown:
    """Tests for the per-factor breakdown."""

    def test_effective_logit_calculation(self) -> None:
        """Each factor's effective_logit should be logit * confidence."""
        factors = [
            Factor(description="Test", logit=2.0, confidence=0.7),
        ]
        inp = _make_binary_input(factors=factors, tentative_logit=1.0)

        result = compute_reflection(inp, "binary")

        assert len(result.factor_breakdown) == 1
        assert result.factor_breakdown[0].effective_logit == pytest.approx(1.4)


class TestFileWriting:
    """Tests for reflection file I/O."""

    @pytest.mark.asyncio
    async def test_creates_reflection_yaml(self, tmp_path: Path) -> None:
        """reflection() should create reflection.yaml."""
        inp = _make_binary_input(
            factors=[Factor(description="Evidence", logit=1.0, confidence=0.8)],
            tentative_logit=0.8,
        )
        computed = compute_reflection(inp, "binary")

        filepath = await _append_reflection(tmp_path, inp, computed, "binary")

        assert filepath.exists()
        assert filepath.name == "reflection.yaml"
        content = filepath.read_text()
        assert "factor_sum" in content
        assert "Evidence" in content

    @pytest.mark.asyncio
    async def test_appends_multiple_entries(self, tmp_path: Path) -> None:
        """Multiple calls should append to the same file."""
        inp1 = _make_binary_input(
            factors=[Factor(description="First", logit=1.0, confidence=1.0)],
            tentative_logit=1.0,
        )
        inp2 = _make_binary_input(
            factors=[Factor(description="Second", logit=-2.0, confidence=0.5)],
            tentative_logit=1.5,
        )

        await _append_reflection(
            tmp_path, inp1, compute_reflection(inp1, "binary"), "binary"
        )
        await _append_reflection(
            tmp_path, inp2, compute_reflection(inp2, "binary"), "binary"
        )

        content = (tmp_path / "reflection.yaml").read_text()
        assert content.count("---") == 2
        assert "First" in content
        assert "Second" in content

    @pytest.mark.asyncio
    async def test_optional_fields_excluded(self, tmp_path: Path) -> None:
        """Optional fields that are None should not appear in YAML."""
        inp = _make_binary_input(tentative_logit=0.0)
        computed = compute_reflection(inp, "binary")

        await _append_reflection(tmp_path, inp, computed, "binary")

        content = (tmp_path / "reflection.yaml").read_text()
        assert "calibration_notes" not in content
        assert "update_triggers" not in content

    @pytest.mark.asyncio
    async def test_optional_fields_included_when_set(self, tmp_path: Path) -> None:
        """Optional fields should appear when provided."""
        inp = ReflectionInput(
            factors=[],
            tentative_estimate=BinaryEstimate(logit=0.0, probability=0.5),
            assessment="Strong positive evidence outweighs base rate concerns.",
            tool_audit="web_search worked well, fred_series returned empty",
            process_reflection="Missing a tool for satellite imagery analysis",
            calibration_notes="Base rate is 30% for similar events",
            key_uncertainties="Whether the trend persists past Q1",
        )
        computed = compute_reflection(inp, "binary")

        await _append_reflection(tmp_path, inp, computed, "binary")

        content = (tmp_path / "reflection.yaml").read_text()
        assert "tool_audit" in content
        assert "process_reflection" in content
        assert "satellite imagery" in content
        assert "calibration_notes" in content


class TestSourcesInOutput:
    """Tests for sources populated in reflection output."""

    def test_sources_default_empty(self) -> None:
        """Output should have empty sources by default."""
        inp = _make_binary_input(tentative_logit=0.5)
        result = compute_reflection(inp, "binary")
        assert result.sources == []

    def test_sources_populated_externally(self) -> None:
        """Sources can be injected after computation."""
        inp = _make_binary_input(tentative_logit=0.5)
        result = compute_reflection(inp, "binary")
        result.sources = ["https://example.com", "https://other.org"]
        dumped = result.model_dump(exclude_none=True)
        assert dumped["sources"] == ["https://example.com", "https://other.org"]


class TestReviewerCritique:
    """Tests for the reviewer critique field."""

    def test_reviewer_critique_default_none(self) -> None:
        """Output should have None reviewer_critique by default."""
        inp = _make_binary_input(tentative_logit=0.5)
        result = compute_reflection(inp, "binary")
        assert result.reviewer_critique is None

    def test_reviewer_critique_excluded_when_none(self) -> None:
        """reviewer_critique should not appear in dump when None."""
        inp = _make_binary_input(tentative_logit=0.5)
        result = compute_reflection(inp, "binary")
        dumped = result.model_dump(exclude_none=True)
        assert "reviewer_critique" not in dumped

    def test_reviewer_critique_included_when_set(self) -> None:
        """reviewer_critique should appear in dump when populated."""
        inp = _make_binary_input(tentative_logit=0.5)
        result = compute_reflection(inp, "binary")
        result.reviewer_critique = "The factors seem one-sided."
        dumped = result.model_dump(exclude_none=True)
        assert dumped["reviewer_critique"] == "The factors seem one-sided."


class TestBuildReviewerPrompt:
    """Tests for reviewer prompt construction."""

    def test_includes_question_context(self) -> None:
        """Prompt should include question title and type."""
        inp = _make_binary_input(
            factors=[Factor(description="Evidence", logit=1.0, confidence=0.8)],
            tentative_logit=0.8,
        )
        context = {"title": "Will X happen?", "type": "binary"}

        prompt = _build_reviewer_prompt(inp, context, None)

        assert "Will X happen?" in prompt
        assert "binary" in prompt

    def test_includes_factors(self) -> None:
        """Prompt should list all factors."""
        inp = _make_binary_input(
            factors=[
                Factor(description="Strong signal", logit=2.0, confidence=0.9),
                Factor(description="Weak counter", logit=-0.5, confidence=0.7),
            ],
            tentative_logit=1.0,
        )

        prompt = _build_reviewer_prompt(inp, None, None)

        assert "Strong signal" in prompt
        assert "Weak counter" in prompt

    def test_includes_trace(self) -> None:
        """Prompt should reference the trace file."""
        inp = _make_binary_input(tentative_logit=0.5)
        trace_path = Path("/tmp/session/trace.md")

        prompt = _build_reviewer_prompt(inp, None, trace_path)

        assert "trace.md" in prompt

    def test_trace_file_path_included(self) -> None:
        """Prompt should reference the trace file path."""
        inp = _make_binary_input(tentative_logit=0.5)
        trace_path = Path("/tmp/session/trace.md")

        prompt = _build_reviewer_prompt(inp, None, trace_path)

        assert "/tmp/session/trace.md" in prompt


class TestReviewState:
    """Tests for ReviewState verdict tracking and gate logic."""

    def test_initial_state_not_passed(self) -> None:
        state = ReviewState()
        assert state.passed is False
        assert state.last_verdict is None
        assert state.consecutive_fails == 0

    def test_approve_passes(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.passed is True
        assert state.last_verdict == ReviewVerdict.approve

    def test_warn_passes(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.warn, assessment="Minor"))
        assert state.passed is True
        assert state.last_verdict == ReviewVerdict.warn

    def test_single_fail_does_not_pass(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.passed is False
        assert state.consecutive_fails == 1

    def test_three_consecutive_fails_auto_approves(self) -> None:
        state = ReviewState()
        for _ in range(3):
            state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.consecutive_fails == 3
        assert state.passed is True

    def test_approve_resets_consecutive_fails(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.consecutive_fails == 2
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.consecutive_fails == 0
        assert state.passed is True

    def test_fail_after_approve_resets_pass(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.passed is True
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.passed is False
        assert state.consecutive_fails == 1
