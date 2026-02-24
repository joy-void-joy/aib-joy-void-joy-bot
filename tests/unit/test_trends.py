"""Tests for Google Trends tool helpers: change stats and tail stats."""

from aib.tools.trends import (
    TrendDataPoint,
    _calculate_change_stats,
    _compute_tail_stats,
)


def _make_history(
    values: list[int], start_date: str = "2026-01-25"
) -> list[TrendDataPoint]:
    """Build a TrendDataPoint list from raw values."""
    year, month, day = int(start_date[:4]), int(start_date[5:7]), int(start_date[8:10])
    points: list[TrendDataPoint] = []
    for i, v in enumerate(values):
        d = day + i
        m = month
        if d > 28:
            d -= 28
            m += 1
        points.append(TrendDataPoint(date=f"{year}-{m:02d}-{d:02d}", value=v))
    return points


# ── _calculate_change_stats ──────────────────────────────────────────


class TestCalculateChangeStats:
    def test_post_spike_decay_plateau(self) -> None:
        values = [0, 0, 63, 94, 70, 55, 100, 48, 30, 17, 14, 14, 14, 12, 13, 16, 13, 13]
        stats = _calculate_change_stats(values)
        assert stats["total"] == len(values) - 1
        assert stats["threshold"] == 3
        assert stats["no_change"] > 0
        assert (
            stats["increases"] + stats["decreases"] + stats["no_change"]
            == stats["total"]
        )

    def test_pure_decay(self) -> None:
        values = [100, 80, 60, 40, 20, 5, 1, 0, 0, 0]
        stats = _calculate_change_stats(values)
        assert stats["decreases"] > stats["increases"]
        assert stats["decrease_rate"] > 0.5

    def test_flat_series(self) -> None:
        values = [10, 10, 10, 10, 10]
        stats = _calculate_change_stats(values)
        assert stats["no_change"] == 4
        assert stats["increases"] == 0
        assert stats["decreases"] == 0
        assert stats["no_change_rate"] == 1.0

    def test_custom_threshold(self) -> None:
        values = [10, 15, 10, 15]
        stats_t3 = _calculate_change_stats(values, threshold=3)
        stats_t10 = _calculate_change_stats(values, threshold=10)
        assert stats_t3["no_change"] < stats_t10["no_change"]

    def test_two_values(self) -> None:
        stats = _calculate_change_stats([5, 10])
        assert stats["total"] == 1
        assert stats["increases"] == 1


# ── _compute_tail_stats ──────────────────────────────────────────────


class TestComputeTailStats:
    def test_post_spike_decay_plateau(self) -> None:
        """The 42187 pattern: spike then plateau at low values."""
        values = [0, 0, 63, 94, 70, 55, 100, 48, 30, 17, 14, 14, 14, 12, 13, 16, 13, 13]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "stable_tail_days" in stats
        assert stats["stable_tail_days"] >= 5
        assert "stable_tail_range" in stats
        assert stats["stable_tail_range"]["low"] <= 13
        assert stats["stable_tail_range"]["high"] <= 17
        assert "peak" in stats
        assert stats["peak"]["value"] == 100
        assert "drawdown_from_peak_pct" in stats
        assert stats["drawdown_from_peak_pct"] < -80

    def test_pure_decay_to_zero(self) -> None:
        """Exponential decay with no plateau — large day-over-day drops."""
        values = [100, 70, 45, 25, 12, 5, 1, 0, 0, 0]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        # Last three values are 0,0,0 — diffs are 0, within threshold
        assert "stable_tail_days" in stats
        assert stats["stable_tail_days"] >= 2
        assert "peak" in stats
        assert stats["peak"]["value"] == 100
        assert "drawdown_from_peak_pct" in stats
        assert stats["drawdown_from_peak_pct"] == -100.0

    def test_flat_stable_series(self) -> None:
        """Flat series should have stable_tail_days == len - 1."""
        values = [15, 15, 15, 15, 15]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "stable_tail_days" in stats
        assert stats["stable_tail_days"] == 4
        assert "peak" in stats
        assert stats["peak"]["value"] == 15
        assert "drawdown_from_peak_pct" in stats
        assert stats["drawdown_from_peak_pct"] == 0.0

    def test_short_series_returns_none(self) -> None:
        """Series with < 3 points returns None."""
        assert _compute_tail_stats(_make_history([10, 20])) is None
        assert _compute_tail_stats(_make_history([5])) is None
        assert _compute_tail_stats([]) is None

    def test_spike_at_end(self) -> None:
        """Spike at the very end — no stable tail."""
        values = [10, 12, 11, 10, 50, 100]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "stable_tail_days" not in stats
        assert "peak" in stats
        assert stats["peak"]["value"] == 100
        assert stats["peak"]["days_ago"] == 0

    def test_trough_excludes_leading_zeros(self) -> None:
        """Trough should ignore leading zeros."""
        values = [0, 0, 0, 50, 30, 10, 5, 8]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "trough" in stats
        assert stats["trough"]["value"] == 5

    def test_trailing_change_stats_present(self) -> None:
        """Trailing change stats use last 7 points."""
        values = [100, 80, 60, 40, 20, 10, 10, 10, 10, 10]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "trailing_change_stats" in stats
        trailing = stats["trailing_change_stats"]
        assert trailing["total"] == 6
        assert trailing["no_change"] > trailing["decreases"]

    def test_trailing_volatility_present(self) -> None:
        """Trailing volatility is std dev of day-over-day changes."""
        values = [10, 10, 10, 10, 10]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "trailing_volatility" in stats
        assert stats["trailing_volatility"] == 0.0

    def test_trailing_volatility_nonzero(self) -> None:
        values = [10, 15, 10, 15, 10]
        history = _make_history(values)
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "trailing_volatility" in stats
        assert stats["trailing_volatility"] > 0

    def test_exactly_three_points(self) -> None:
        """Boundary: 3 points is the minimum for a result."""
        history = _make_history([10, 12, 11])
        stats = _compute_tail_stats(history)
        assert stats is not None
        assert "peak" in stats
        assert stats["peak"]["value"] == 12
