"""Tests for the unified fetch tool."""

import json
from datetime import date
from unittest.mock import AsyncMock, patch

import pytest

from aib.retrodict_context import retrodict_cutoff
from aib.tools.fetch import fetch_url as _fetch_url_tool

fetch_url = _fetch_url_tool.handler


class TestSuggestOnlyInterception:
    """Tests that SUGGEST_ONLY domains return helpful errors."""

    @pytest.mark.asyncio
    async def test_tradingeconomics_intercepted(self) -> None:
        result = await fetch_url({"url": "https://tradingeconomics.com/germany/gdp"})
        assert result["is_error"] is True
        assert "fred_series" in result["content"][0]["text"] or "world_bank" in result["content"][0]["text"]

    @pytest.mark.asyncio
    async def test_statista_intercepted(self) -> None:
        result = await fetch_url({"url": "https://www.statista.com/statistics/123"})
        assert result["is_error"] is True
        assert "search_exa" in result["content"][0]["text"]


class TestDomainDispatch:
    """Tests that domain dispatch routes to specialized tools."""

    @pytest.mark.asyncio
    async def test_yahoo_finance_dispatched(self) -> None:
        with patch(
            "aib.tools.fetch.domain_dispatch",
            new_callable=AsyncMock,
            return_value={"content": [{"type": "text", "text": "stock data"}]},
        ):
            result = await fetch_url({"url": "https://finance.yahoo.com/quote/AAPL"})
        assert "stock data" in result["content"][0]["text"]

    @pytest.mark.asyncio
    async def test_unknown_domain_falls_through(self) -> None:
        with (
            patch(
                "aib.tools.fetch.domain_dispatch",
                new_callable=AsyncMock,
                return_value=None,
            ),
            patch(
                "aib.tools.fetch.fetch_live",
                new_callable=AsyncMock,
                return_value="Page content here",
            ),
        ):
            result = await fetch_url({"url": "https://example.com/page"})
        data = json.loads(result["content"][0]["text"])
        assert data["content"] == "Page content here"


class TestRetrodictBranching:
    """Tests that retrodict mode uses Wayback Machine."""

    @pytest.mark.asyncio
    async def test_retrodict_uses_wayback(self) -> None:
        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            with (
                patch(
                    "aib.tools.fetch.domain_dispatch",
                    new_callable=AsyncMock,
                    return_value=None,
                ),
                patch(
                    "aib.tools.fetch.check_wayback_availability",
                    new_callable=AsyncMock,
                    return_value={"url": "...", "timestamp": "20260115"},
                ),
                patch(
                    "aib.tools.fetch.fetch_wayback_content",
                    new_callable=AsyncMock,
                    return_value="Wayback content",
                ),
            ):
                result = await fetch_url({"url": "https://example.com/page"})
            data = json.loads(result["content"][0]["text"])
            assert data["content"] == "Wayback content"
        finally:
            retrodict_cutoff.reset(token)


class TestPromptExtractionFailure:
    """Tests that extraction failures surface a note to the agent."""

    @pytest.mark.asyncio
    async def test_extraction_failure_adds_note(self) -> None:
        with (
            patch(
                "aib.tools.fetch.domain_dispatch",
                new_callable=AsyncMock,
                return_value=None,
            ),
            patch(
                "aib.tools.fetch.fetch_live",
                new_callable=AsyncMock,
                return_value="Raw page content",
            ),
            patch(
                "aib.tools.fetch.extract_with_prompt",
                new_callable=AsyncMock,
                side_effect=RuntimeError("Sonnet unavailable"),
            ),
        ):
            result = await fetch_url({
                "url": "https://example.com/page",
                "prompt": "What is the GDP?",
            })

        data = json.loads(result["content"][0]["text"])
        assert "Prompt extraction failed" in data["content"]
        assert "Raw page content" in data["content"]

    @pytest.mark.asyncio
    async def test_extraction_success_returns_extracted(self) -> None:
        with (
            patch(
                "aib.tools.fetch.domain_dispatch",
                new_callable=AsyncMock,
                return_value=None,
            ),
            patch(
                "aib.tools.fetch.fetch_live",
                new_callable=AsyncMock,
                return_value="Raw page content",
            ),
            patch(
                "aib.tools.fetch.extract_with_prompt",
                new_callable=AsyncMock,
                return_value="GDP is 3.2%",
            ),
        ):
            result = await fetch_url({
                "url": "https://example.com/page",
                "prompt": "What is the GDP?",
            })

        data = json.loads(result["content"][0]["text"])
        assert data["content"] == "GDP is 3.2%"
