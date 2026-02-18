"""Tests for CP history processing."""

from __future__ import annotations

from datetime import datetime, timezone
from typing import TYPE_CHECKING

import pytest

from metaculus.models import AggregationHistoryPoint, AggregationMethod

if TYPE_CHECKING:
    from types import ModuleType


@pytest.fixture(scope="session")
def fc() -> ModuleType:
    """Import markets module (resolving circular import chain first)."""
    import aib.agent.core  # noqa: F401 — resolves circular import
    from aib.tools import markets

    return markets


SAMPLE_AGGREGATION = AggregationMethod(
    history=[
        AggregationHistoryPoint(
            start_time=1738800000.0,  # 2025-02-06 ~00:00 UTC
            forecaster_count=50,
            centers=[0.35, 0.65],
        ),
        AggregationHistoryPoint(
            start_time=1738886400.0,  # 2025-02-07 00:00 UTC
            forecaster_count=55,
            centers=[0.40, 0.60],
        ),
        AggregationHistoryPoint(
            start_time=1738972800.0,  # 2025-02-08 00:00 UTC
            forecaster_count=60,
            centers=[0.45, 0.55],
        ),
    ]
)


class TestFormatTimestamp:
    """Tests for _format_timestamp handling both formats."""

    def test_unix_float(self, fc: ModuleType) -> None:
        result: str = fc._format_timestamp(1738886400.0)
        assert "2025-02-07" in result

    def test_unix_int(self, fc: ModuleType) -> None:
        result: str = fc._format_timestamp(1738886400)
        assert "2025-02-07" in result

    def test_iso_string_passthrough(self, fc: ModuleType) -> None:
        result: str = fc._format_timestamp("2025-02-07T00:00:00Z")
        assert result == "2025-02-07T00:00:00Z"


class TestBuildCPHistoryResponse:
    """Tests for _build_cp_history_response with AggregationMethod input."""

    def test_processes_unix_timestamps(self, fc: ModuleType) -> None:
        result = fc._build_cp_history_response(SAMPLE_AGGREGATION, 12345, 30, None)
        assert result.data_points == 3
        assert result.history[0].community_prediction == 0.35
        assert result.history[1].community_prediction == 0.40
        assert result.history[2].community_prediction == 0.45

    def test_retrodict_cutoff_filters(self, fc: ModuleType) -> None:
        cutoff = datetime(2025, 2, 7, 0, 0, tzinfo=timezone.utc)
        result = fc._build_cp_history_response(SAMPLE_AGGREGATION, 12345, 30, cutoff)
        assert result.data_points == 2
        assert result.history[0].community_prediction == 0.35
        assert result.history[1].community_prediction == 0.40

    def test_empty_history(self, fc: ModuleType) -> None:
        empty = AggregationMethod(history=[])
        result = fc._build_cp_history_response(empty, 12345, 30, None)
        assert result.data_points == 0

    def test_all_filtered_shows_note(self, fc: ModuleType) -> None:
        cutoff = datetime(2025, 2, 5, 0, 0, tzinfo=timezone.utc)
        result = fc._build_cp_history_response(SAMPLE_AGGREGATION, 12345, 30, cutoff)
        assert result.data_points == 0
        assert result.note is not None
