"""Tests for the unified web_search tool."""

import json
from datetime import date
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from lup.mcp import response_text
from lup.tool_routes import routes

from aib.retrodict_context import retrodict_cutoff
from aib.tools.search import (
    AugmentedSearchResult,
    SearchResult,
    _augment_with_api_data,
    web_search as _web_search_tool,
)

_handler = _web_search_tool.handler


def _make_result(
    url: str, title: str = "Test", snippet: str = "snippet"
) -> SearchResult:
    return SearchResult(title=title, url=url, snippet=snippet)


class TestWebSearchLiveMode:
    """Tests for web_search in live mode (no retrodict cutoff)."""

    @pytest.mark.asyncio
    async def test_returns_augmented_results(self) -> None:
        raw = [_make_result("https://example.com")]
        augmented = [
            AugmentedSearchResult(
                title="Test",
                url="https://example.com",
                snippet="snippet",
                api_data=None,
                hint=None,
            )
        ]
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=raw,
            ),
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=augmented,
            ),
            patch(
                "aib.tools.search._fetch_live_snippets",
                new_callable=AsyncMock,
                return_value=augmented,
            ),
        ):
            result = await _handler({"query": "test"})

        assert "is_error" not in result
        data = json.loads(response_text(result))
        assert len(data["results"]) == 1
        assert data["results"][0]["url"] == "https://example.com"

    @pytest.mark.asyncio
    async def test_live_snippets_called_not_wayback(self) -> None:
        augmented: list[AugmentedSearchResult] = []
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=[],
            ),
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=augmented,
            ),
            patch(
                "aib.tools.search._fetch_live_snippets",
                new_callable=AsyncMock,
                return_value=augmented,
            ) as mock_live,
            patch(
                "aib.tools.search._wayback_filter_non_api_results",
                new_callable=AsyncMock,
            ) as mock_wb,
        ):
            await _handler({"query": "test"})

        mock_live.assert_called_once_with(augmented)
        mock_wb.assert_not_called()

    @pytest.mark.asyncio
    async def test_augmentation_called(self) -> None:
        raw = [_make_result("https://example.com")]
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=raw,
            ),
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=[],
            ) as mock_aug,
            patch(
                "aib.tools.search._fetch_live_snippets",
                new_callable=AsyncMock,
                return_value=[],
            ),
        ):
            await _handler({"query": "test"})

        mock_aug.assert_called_once_with(raw)


class TestWebSearchRetrodictMode:
    """Tests for web_search in retrodict mode."""

    @pytest.fixture(autouse=True)
    def set_cutoff(self) -> Any:
        token = retrodict_cutoff.set(date(2026, 1, 15))
        yield
        retrodict_cutoff.reset(token)

    @pytest.mark.asyncio
    async def test_wayback_called_after_augmentation(self) -> None:
        """Wayback filter runs after augmentation, not before."""
        raw = [_make_result("https://example.com")]
        augmented = [
            AugmentedSearchResult(
                title="Test",
                url="https://example.com",
                snippet="snippet",
                api_data=None,
                hint=None,
            )
        ]
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=raw,
            ),
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=augmented,
            ),
            patch(
                "aib.tools.search._wayback_filter_non_api_results",
                new_callable=AsyncMock,
                return_value=augmented,
            ) as mock_wb,
        ):
            await _handler({"query": "test"})

        mock_wb.assert_called_once_with(augmented, "2026-01-15")

    @pytest.mark.asyncio
    async def test_augmentation_runs_on_raw_results(self) -> None:
        """Augmentation runs on raw results (before Wayback filter)."""
        raw = [_make_result("https://a.com"), _make_result("https://b.com")]
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=raw,
            ),
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=[],
            ) as mock_aug,
            patch(
                "aib.tools.search._wayback_filter_non_api_results",
                new_callable=AsyncMock,
                return_value=[],
            ),
        ):
            await _handler({"query": "test"})

        mock_aug.assert_called_once_with(raw)

    @pytest.mark.asyncio
    async def test_cutoff_passed_to_raw_search(self) -> None:
        with (
            patch(
                "aib.tools.search._raw_web_search",
                new_callable=AsyncMock,
                return_value=[],
            ) as mock_raw,
            patch(
                "aib.tools.search._augment_with_api_data",
                new_callable=AsyncMock,
                return_value=[],
            ),
        ):
            await _handler({"query": "test"})

        mock_raw.assert_called_once_with("test", "2026-01-15", None, None)


def _make_fake_route(
    domain: str,
    pattern: str,
    handler: AsyncMock,
) -> Any:
    """Create a fake ToolRoute for testing.

    A route holds a whole `LupMcpTool`; dispatch reaches only its `name` and
    `handler`, so the rest is filled with the least that constructs. Going
    through the real class rather than a stub is what keeps the route
    model's own validation in play.
    """
    import re

    from lup.mcp import LupMcpTool
    from lup.tool_routes import ToolRoute
    from pydantic import BaseModel

    class FakeInput(BaseModel):
        symbol: str = ""

    return ToolRoute(
        pattern=re.compile(pattern),
        tool=LupMcpTool(
            name=domain,
            description="fake",
            input_schema={},
            handler=handler,
            call_handler=handler,
            input_model=FakeInput,
        ),
        build_params=lambda m: {"symbol": m.group(1)},
    )


class TestAugmentWithApiData:
    """Tests for the API augmentation logic."""

    @pytest.mark.asyncio
    async def test_non_matching_url_passes_through(self) -> None:
        results = [_make_result("https://blog.example.com/post")]
        mock_handler = AsyncMock()
        fake_routes = [
            _make_fake_route(
                "finance.yahoo.com", r"finance\.yahoo\.com/quote/(\w+)", mock_handler
            )
        ]

        with patch.object(routes, "routes", fake_routes):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 1
        assert augmented[0]["api_data"] is None
        assert augmented[0]["hint"] is None
        assert augmented[0]["url"] == "https://blog.example.com/post"
        mock_handler.assert_not_called()

    @pytest.mark.asyncio
    async def test_suggest_only_gets_hint(self) -> None:
        results = [_make_result("https://tradingeconomics.com/us/gdp")]

        with patch.object(routes, "routes", []):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 1
        assert augmented[0]["hint"] is not None
        assert "fred" in augmented[0]["hint"].lower()
        assert augmented[0]["api_data"] is None

    @pytest.mark.asyncio
    async def test_matching_route_gets_api_data(self) -> None:
        results = [_make_result("https://finance.yahoo.com/quote/AAPL")]
        mock_response = {"content": [{"type": "text", "text": "price data"}]}
        mock_handler = AsyncMock(return_value=mock_response)
        fake_routes = [
            _make_fake_route(
                "finance.yahoo.com", r"finance\.yahoo\.com/quote/(\w+)", mock_handler
            )
        ]

        with patch.object(routes, "routes", fake_routes):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 1
        assert augmented[0]["api_data"] == mock_response
        mock_handler.assert_called_once_with({"symbol": "AAPL"})

    @pytest.mark.asyncio
    async def test_handler_failure_returns_no_api_data(self) -> None:
        results = [_make_result("https://finance.yahoo.com/quote/AAPL")]
        mock_handler = AsyncMock(side_effect=Exception("API timeout"))
        fake_routes = [
            _make_fake_route(
                "finance.yahoo.com", r"finance\.yahoo\.com/quote/(\w+)", mock_handler
            )
        ]

        with patch.object(routes, "routes", fake_routes):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 1
        assert augmented[0]["api_data"] is None

    @pytest.mark.asyncio
    async def test_error_response_not_included(self) -> None:
        results = [_make_result("https://finance.yahoo.com/quote/INVALID")]
        error_response = {
            "content": [{"type": "text", "text": "not found"}],
            "is_error": True,
        }
        mock_handler = AsyncMock(return_value=error_response)
        fake_routes = [
            _make_fake_route(
                "finance.yahoo.com", r"finance\.yahoo\.com/quote/(\w+)", mock_handler
            )
        ]

        with patch.object(routes, "routes", fake_routes):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 1
        assert augmented[0]["api_data"] is None

    @pytest.mark.asyncio
    async def test_mixed_results(self) -> None:
        results = [
            _make_result("https://finance.yahoo.com/quote/AAPL"),
            _make_result("https://tradingeconomics.com/us/gdp"),
            _make_result("https://blog.example.com/post"),
        ]
        mock_stock = {"content": [{"type": "text", "text": "AAPL data"}]}
        mock_handler = AsyncMock(return_value=mock_stock)
        fake_routes = [
            _make_fake_route(
                "finance.yahoo.com", r"finance\.yahoo\.com/quote/(\w+)", mock_handler
            )
        ]

        with patch.object(routes, "routes", fake_routes):
            augmented = await _augment_with_api_data(results)

        assert len(augmented) == 3
        assert augmented[0]["api_data"] == mock_stock
        assert augmented[1]["hint"] is not None
        assert augmented[1]["api_data"] is None
        assert augmented[2]["api_data"] is None
        assert augmented[2]["hint"] is None


class TestWebSearchInputValidation:
    """Tests for input validation."""

    @pytest.mark.asyncio
    async def test_rejects_both_domain_filters(self) -> None:
        result = await _handler(
            {
                "query": "test",
                "allowed_domains": ["a.com"],
                "blocked_domains": ["b.com"],
            }
        )
        assert result.get("is_error") is True

    @pytest.mark.asyncio
    async def test_rejects_empty_query(self) -> None:
        result = await _handler({"query": ""})
        assert result.get("is_error") is True
