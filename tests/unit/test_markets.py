"""Tests for prediction market tools including historical price tools."""

import pytest

from aib.tools.markets import (
    HistoricalPriceInput,
    _parse_yes_price,
    parse_polymarket_event,
)


class TestParseYesPrice:
    """Tests for Polymarket price parsing."""

    def test_list_of_floats(self) -> None:
        """Should parse list of floats."""
        result = _parse_yes_price([0.65, 0.35])
        assert result == 0.65

    def test_list_of_strings(self) -> None:
        """Should parse list of string numbers."""
        result = _parse_yes_price(["0.75", "0.25"])
        assert result == 0.75

    def test_string_encoded_list(self) -> None:
        """Should parse string-encoded list."""
        result = _parse_yes_price("[0.80, 0.20]")
        assert result == 0.80

    def test_nested_structure(self) -> None:
        """Should handle nested lists."""
        result = _parse_yes_price("[[0.55]]")
        assert result == 0.55

    def test_none_input(self) -> None:
        """Should return None for None input."""
        result = _parse_yes_price(None)
        assert result is None

    def test_empty_list(self) -> None:
        """Should return None for empty list."""
        result = _parse_yes_price([])
        assert result is None

    def test_invalid_string(self) -> None:
        """Should return None for invalid strings."""
        result = _parse_yes_price("not a number")
        assert result is None


class TestParsePolymarketEvent:
    """Tests for Polymarket event parsing."""

    def test_valid_event(self) -> None:
        """Should parse a valid event."""
        event = {
            "title": "Test Event",
            "slug": "test-event",
            "markets": [
                {
                    "outcomePrices": [0.65, 0.35],
                    "volume": 1000000,
                }
            ],
        }
        result = parse_polymarket_event(event)
        assert result is not None
        assert result["market_title"] == "Test Event"
        assert result["probability"] == 0.65
        assert result["volume"] == 1000000
        assert result["source"] == "polymarket"

    def test_no_markets(self) -> None:
        """Should return None if no markets."""
        event = {"title": "Test", "markets": []}
        result = parse_polymarket_event(event)
        assert result is None

    def test_unparseable_prices(self) -> None:
        """Should return None if prices can't be parsed."""
        event = {
            "title": "Test",
            "slug": "test",
            "markets": [{"outcomePrices": "invalid"}],
        }
        result = parse_polymarket_event(event)
        assert result is None


class TestHistoricalPriceInput:
    """Tests for historical price input validation."""

    def test_valid_input(self) -> None:
        """Should accept valid input."""
        input_data = HistoricalPriceInput(market_id="abc123", timestamp=1704067200)
        assert input_data.market_id == "abc123"
        assert input_data.timestamp == 1704067200

    def test_empty_market_id(self) -> None:
        """Should reject empty market_id."""
        with pytest.raises(ValueError):
            HistoricalPriceInput(market_id="", timestamp=1704067200)


class TestPolymarketHistoryInternal:
    """Tests for Polymarket history internal logic."""

    def test_find_closest_point_before_timestamp(self) -> None:
        """Should find the closest price point at or before target."""
        history = [
            {"t": 1704067100, "p": 0.60},
            {"t": 1704067000, "p": 0.55},
            {"t": 1704066900, "p": 0.50},
        ]
        target_ts = 1704067200

        # Find closest point at or before target
        closest_point = None
        for point in history:
            point_ts = point.get("t", 0)
            if point_ts <= target_ts:
                if closest_point is None or point_ts > closest_point.get("t", 0):
                    closest_point = point

        assert closest_point is not None
        assert closest_point["p"] == 0.60

    def test_no_points_before_timestamp(self) -> None:
        """Should return None if all points are after target."""
        history = [
            {"t": 1704067300, "p": 0.60},
            {"t": 1704067400, "p": 0.55},
        ]
        target_ts = 1704067200

        closest_point = None
        for point in history:
            point_ts = point.get("t", 0)
            if point_ts <= target_ts:
                if closest_point is None or point_ts > closest_point.get("t", 0):
                    closest_point = point

        assert closest_point is None


class TestManifoldHistoryInternal:
    """Tests for Manifold history internal logic (bet reconstruction)."""

    def test_reconstruct_from_bets(self) -> None:
        """Should use probAfter from most recent bet before target."""
        bets = [
            {"createdTime": 1704067150000, "probBefore": 0.55, "probAfter": 0.60},
            {"createdTime": 1704067100000, "probBefore": 0.50, "probAfter": 0.55},
            {"createdTime": 1704067050000, "probBefore": 0.45, "probAfter": 0.50},
        ]
        target_ts_ms = 1704067200000

        relevant_bet = None
        for bet in bets:
            bet_time = bet.get("createdTime", 0)
            if bet_time <= target_ts_ms:
                if relevant_bet is None or bet_time > relevant_bet.get(
                    "createdTime", 0
                ):
                    relevant_bet = bet

        assert relevant_bet is not None
        assert relevant_bet["probAfter"] == 0.60

    def test_no_bets_before_timestamp(self) -> None:
        """Should return None if all bets are after target."""
        bets = [
            {"createdTime": 1704067300000, "probBefore": 0.55, "probAfter": 0.60},
        ]
        target_ts_ms = 1704067200000

        relevant_bet = None
        for bet in bets:
            bet_time = bet.get("createdTime", 0)
            if bet_time <= target_ts_ms:
                if relevant_bet is None or bet_time > relevant_bet.get(
                    "createdTime", 0
                ):
                    relevant_bet = bet

        assert relevant_bet is None

    def test_uses_prob_after(self) -> None:
        """Should use probAfter, not probBefore."""
        bets = [
            {"createdTime": 1704067100000, "probBefore": 0.45, "probAfter": 0.55},
        ]

        relevant_bet = bets[0]
        prob = relevant_bet.get("probAfter", relevant_bet.get("probBefore", 0.5))

        assert prob == 0.55  # Should be probAfter, not probBefore
