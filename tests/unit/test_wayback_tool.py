"""The agent-facing wayback_snapshot tool."""

import json
from datetime import date
from typing import Any
from unittest.mock import AsyncMock, patch

from lup.mcp import ToolResponse, response_text

from aib.retrodict_context import retrodict_cutoff
from aib.tools.wayback import wayback_snapshot, wayback_url_variants

SNAPSHOT = {
    "available": True,
    "url": "http://web.archive.org/web/20260101235955/https://example.com/",
    "timestamp": "20260101235955",
    "status": "200",
}


def payload(result: ToolResponse) -> dict[str, Any]:
    """Decode the JSON body a lup_tool success wraps in its text block."""
    parsed = json.loads(response_text(result))
    assert isinstance(parsed, dict)
    return parsed


class TestUrlVariants:
    def test_bare_form_is_appended(self) -> None:
        assert wayback_url_variants("https://www.bbc.com/news") == [
            "https://www.bbc.com/news",
            "bbc.com/news",
        ]

    def test_already_bare_url_yields_one_form(self) -> None:
        assert wayback_url_variants("example.com") == ["example.com"]

    def test_query_string_is_preserved(self) -> None:
        assert wayback_url_variants("https://www.a.com/p?q=1")[1] == "a.com/p?q=1"


class TestWaybackSnapshot:
    async def test_returns_snapshot_metadata(self) -> None:
        with patch(
            "aib.tools.wayback.check_wayback_availability",
            new=AsyncMock(return_value=SNAPSHOT),
        ):
            result = await wayback_snapshot.handler(
                {
                    "url": "https://example.com",
                    "date": "2026-01-01",
                    "include_content": False,
                }
            )
        body = payload(result)
        assert body["snapshot_date"] == "20260101235955"
        assert body["requested_date"] == "20260101"
        assert body["content"] is None

    async def test_rejects_malformed_date(self) -> None:
        result = await wayback_snapshot.handler(
            {"url": "https://example.com", "date": "01-2026"}
        )
        # lup: ignore[dict-get] — is_error is an optional key on ToolResponse
        assert result.get("is_error") is True

    async def test_missing_snapshot_is_an_error(self) -> None:
        with patch(
            "aib.tools.wayback.check_wayback_availability",
            new=AsyncMock(return_value=None),
        ):
            result = await wayback_snapshot.handler(
                {"url": "https://example.com", "date": "20260101"}
            )
        # lup: ignore[dict-get] — is_error is an optional key on ToolResponse
        assert result.get("is_error") is True

    async def test_falls_back_to_the_bare_url_form(self) -> None:
        availability = AsyncMock(side_effect=[None, SNAPSHOT])
        with patch("aib.tools.wayback.check_wayback_availability", new=availability):
            result = await wayback_snapshot.handler(
                {
                    "url": "https://www.bbc.com/news",
                    "date": "20260101",
                    "include_content": False,
                }
            )
        assert payload(result)["snapshot_date"] == "20260101235955"
        assert availability.await_count == 2

    async def test_retrodict_clamps_a_future_request_to_the_cutoff(self) -> None:
        availability = AsyncMock(return_value=SNAPSHOT)
        token = retrodict_cutoff.set(date(2026, 1, 1))
        try:
            with patch(
                "aib.tools.wayback.check_wayback_availability", new=availability
            ):
                await wayback_snapshot.handler(
                    {
                        "url": "https://example.com",
                        "date": "20260601",
                        "include_content": False,
                    }
                )
        finally:
            retrodict_cutoff.reset(token)
        assert availability.await_args is not None
        assert availability.await_args.args[1] == "20260101"

    async def test_request_before_the_cutoff_is_left_alone(self) -> None:
        availability = AsyncMock(return_value=SNAPSHOT)
        token = retrodict_cutoff.set(date(2026, 6, 1))
        try:
            with patch(
                "aib.tools.wayback.check_wayback_availability", new=availability
            ):
                await wayback_snapshot.handler(
                    {
                        "url": "https://example.com",
                        "date": "20260101",
                        "include_content": False,
                    }
                )
        finally:
            retrodict_cutoff.reset(token)
        assert availability.await_args is not None
        assert availability.await_args.args[1] == "20260101"
