"""Tests for financial tool helpers: summary stats and conditional returns."""

import math

import pytest

from aib.tools.financial import (
    DailyClose,
    StockPrice,
    _compute_conditional_return_stats,
    _compute_summary_stats,
)


def _make_stock_price(
    closes: list[float],
    *,
    start_date: str = "2026-01-01",
    fifty_two_week_high: float | None = None,
    fifty_two_week_low: float | None = None,
) -> StockPrice:
    """Build a StockPrice with synthetic history."""
    history = [
        DailyClose(date=f"{start_date[:8]}{i + 1:02d}", close=c)
        for i, c in enumerate(closes)
    ]
    return StockPrice(
        symbol="TEST",
        name="Test Stock",
        current_price=closes[-1] if closes else None,
        previous_close=closes[-2] if len(closes) > 1 else None,
        change_percent=None,
        currency="USD",
        market_cap=None,
        fifty_two_week_high=fifty_two_week_high or max(closes),
        fifty_two_week_low=fifty_two_week_low or min(closes),
        recent_history=history,
    )


class TestSummaryStats:
    def test_returns_none_for_empty_history(self) -> None:
        result = StockPrice(
            symbol="X",
            name="X",
            current_price=100,
            previous_close=100,
            change_percent=None,
            currency="USD",
            market_cap=None,
            fifty_two_week_high=100,
            fifty_two_week_low=100,
            recent_history=None,
        )
        assert _compute_summary_stats(result) is None

    def test_returns_none_for_single_entry(self) -> None:
        result = _make_stock_price([100.0])
        assert _compute_summary_stats(result) is None

    def test_trailing_returns(self) -> None:
        closes = list(range(100, 125))  # 25 days: 100, 101, ..., 124
        sp = _make_stock_price([float(c) for c in closes])
        stats = _compute_summary_stats(sp)
        assert stats is not None

        tr = stats.get("trailing_returns")
        assert tr is not None
        assert tr.get("five_day") == pytest.approx((124 - 119) / 119 * 100)
        assert tr.get("ten_day") == pytest.approx((124 - 114) / 114 * 100)
        assert tr.get("twenty_day") == pytest.approx((124 - 104) / 104 * 100)

    def test_volatility(self) -> None:
        closes = [100.0, 105.0, 95.0, 102.0, 98.0, 103.0]
        sp = _make_stock_price(closes)
        stats = _compute_summary_stats(sp)
        assert stats is not None
        assert "trailing_volatility_20d" in stats

        vol = stats.get("trailing_volatility_20d")
        assert vol is not None and vol > 0

        log_returns = [math.log(closes[i] / closes[i - 1]) for i in range(1, 6)]
        mean_ret = sum(log_returns) / len(log_returns)
        variance = sum((r - mean_ret) ** 2 for r in log_returns) / len(log_returns)
        expected_vol = math.sqrt(variance) * 100
        assert vol == pytest.approx(expected_vol)

    def test_recent_low_and_high(self) -> None:
        closes = [100.0, 90.0, 95.0, 110.0, 105.0]
        sp = _make_stock_price(closes)
        stats = _compute_summary_stats(sp)
        assert stats is not None

        low = stats.get("recent_low")
        assert low is not None
        assert low["close"] == 90.0
        assert low["days_ago"] == 3

        high = stats.get("recent_high")
        assert high is not None
        assert high["close"] == 110.0
        assert high["days_ago"] == 1

    def test_bounce_from_low(self) -> None:
        closes = [100.0, 80.0, 90.0, 85.0, 88.0]
        sp = _make_stock_price(closes)
        stats = _compute_summary_stats(sp)
        assert stats is not None

        expected = (90.0 - 80.0) / 80.0 * 100
        assert stats.get("max_bounce_from_recent_low_pct") == pytest.approx(expected)

    def test_drawdown_and_distance(self) -> None:
        sp = _make_stock_price(
            [100.0, 90.0],
            fifty_two_week_high=120.0,
            fifty_two_week_low=80.0,
        )
        stats = _compute_summary_stats(sp)
        assert stats is not None

        assert stats.get("drawdown_from_52w_high_pct") == pytest.approx(
            (90.0 - 120.0) / 120.0 * 100
        )
        assert stats.get("distance_from_52w_low_pct") == pytest.approx(
            (90.0 - 80.0) / 80.0 * 100
        )

    def test_no_bounce_when_low_is_last(self) -> None:
        closes = [100.0, 95.0, 90.0]
        sp = _make_stock_price(closes)
        stats = _compute_summary_stats(sp)
        assert stats is not None
        assert "max_bounce_from_recent_low_pct" not in stats


def _make_index_history(
    n_days: int,
    *,
    base: float = 1000.0,
    daily_returns: list[float] | None = None,
) -> list[DailyClose]:
    """Build synthetic daily close history.

    If daily_returns is provided, use those. Otherwise flat prices.
    """
    if daily_returns is not None:
        closes = [base]
        for r in daily_returns:
            closes.append(closes[-1] * (1 + r))
        n_days = len(closes)
    else:
        closes = [base] * n_days

    return [
        DailyClose(date=f"2020-{(i // 28) + 1:02d}-{(i % 28) + 1:02d}", close=c)
        for i, c in enumerate(closes)
    ]


class TestConditionalReturns:
    def test_insufficient_data(self) -> None:
        closes = _make_index_history(100)
        result = _compute_conditional_return_stats(closes, 10.0, 5)
        assert isinstance(result, str)
        assert "Insufficient" in result

    def test_no_events_found(self) -> None:
        closes = _make_index_history(500)
        result = _compute_conditional_return_stats(closes, 50.0, 5)
        assert isinstance(result, str)
        assert "No events" in result

    def test_basic_drawdown_detection(self) -> None:
        returns: list[float] = []
        returns.extend([0.0] * 300)
        returns.extend([-0.01] * 30)
        returns.extend([0.005] * 60)

        closes = _make_index_history(0, daily_returns=returns)
        result = _compute_conditional_return_stats(closes, 15.0, 5)
        assert not isinstance(result, str), f"Expected stats, got error: {result}"
        assert result["total_events"] >= 1
        assert 0 <= result["pct_positive"] <= 100
        assert result["return_distribution"]["std"] >= 0

    def test_deduplication(self) -> None:
        returns: list[float] = []
        returns.extend([0.0] * 300)
        returns.extend([-0.01] * 30)
        returns.extend([0.005] * 60)

        closes = _make_index_history(0, daily_returns=returns)
        result = _compute_conditional_return_stats(closes, 15.0, 20)
        assert not isinstance(result, str), f"Expected stats, got error: {result}"
        assert result["total_events"] <= 5

    def test_return_distribution_fields(self) -> None:
        returns: list[float] = []
        returns.extend([0.0] * 300)
        returns.extend([-0.01] * 30)
        returns.extend([0.005] * 60)

        closes = _make_index_history(0, daily_returns=returns)
        result = _compute_conditional_return_stats(closes, 15.0, 5)
        assert not isinstance(result, str), f"Expected stats, got error: {result}"

        dist = result["return_distribution"]
        assert (
            dist["p10"] <= dist["p25"] <= dist["median"] <= dist["p75"] <= dist["p90"]
        )
        assert dist["min"] <= dist["p10"]
        assert dist["p90"] <= dist["max"]
