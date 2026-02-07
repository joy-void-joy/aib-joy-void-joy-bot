"""Tests for CP history processing with the new posts API format."""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import TYPE_CHECKING, Any

import pytest

if TYPE_CHECKING:
    from types import ModuleType


@pytest.fixture(scope="session")
def fc() -> ModuleType:
    """Import forecasting module (resolving circular import chain first)."""
    import aib.agent.core  # noqa: F401 — resolves circular import
    from aib.tools import forecasting

    return forecasting


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


UNIX_HISTORY: dict[str, Any] = {
    "history": [
        {
            "start_time": 1738800000.0,  # 2025-02-06 ~00:00 UTC
            "end_time": None,
            "forecaster_count": 50,
            "centers": [0.35, 0.65],
        },
        {
            "start_time": 1738886400.0,  # 2025-02-07 00:00 UTC
            "end_time": None,
            "forecaster_count": 55,
            "centers": [0.40, 0.60],
        },
        {
            "start_time": 1738972800.0,  # 2025-02-08 00:00 UTC
            "end_time": None,
            "forecaster_count": 60,
            "centers": [0.45, 0.55],
        },
    ]
}


class TestProcessCPHistory:
    """Tests for _process_cp_history with new API data format."""

    @pytest.mark.asyncio
    async def test_processes_unix_timestamps(self, fc: ModuleType) -> None:
        result = await fc._process_cp_history(UNIX_HISTORY, 12345, 30, None)
        data = json.loads(result["content"][0]["text"])
        assert data["data_points"] == 3
        assert data["history"][0]["community_prediction"] == 0.35
        assert data["history"][1]["community_prediction"] == 0.40
        assert data["history"][2]["community_prediction"] == 0.45

    @pytest.mark.asyncio
    async def test_retrodict_cutoff_filters_unix(self, fc: ModuleType) -> None:
        cutoff = datetime(2025, 2, 7, 0, 0, tzinfo=timezone.utc)
        result = await fc._process_cp_history(UNIX_HISTORY, 12345, 30, cutoff)
        data = json.loads(result["content"][0]["text"])
        # Feb 6 00:00 and Feb 7 00:00 both pass (cutoff filters strictly >)
        assert data["data_points"] == 2
        assert data["history"][0]["community_prediction"] == 0.35
        assert data["history"][1]["community_prediction"] == 0.40

    @pytest.mark.asyncio
    async def test_empty_history(self, fc: ModuleType) -> None:
        result = await fc._process_cp_history({"history": []}, 12345, 30, None)
        data = json.loads(result["content"][0]["text"])
        assert data["data_points"] == 0

    @pytest.mark.asyncio
    async def test_all_filtered_shows_note(self, fc: ModuleType) -> None:
        cutoff = datetime(2025, 2, 5, 0, 0, tzinfo=timezone.utc)
        result = await fc._process_cp_history(UNIX_HISTORY, 12345, 30, cutoff)
        data = json.loads(result["content"][0]["text"])
        assert data["data_points"] == 0
        assert "note" in data
