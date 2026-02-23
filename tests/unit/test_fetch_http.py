"""Tests for HTTP fetch module."""

from unittest.mock import AsyncMock, patch

import httpx
import pytest

from aib.tools.fetch_http import FetchResult, _ERROR_HINTS, fetch_live


def _make_response(
    status_code: int = 200,
    text: str = "<html><body>Hello</body></html>",
    content_type: str = "text/html",
) -> httpx.Response:
    """Create a mock httpx.Response."""
    resp = httpx.Response(
        status_code=status_code,
        text=text,
        headers={"content-type": content_type},
        request=httpx.Request("GET", "https://example.com"),
    )
    return resp


class TestFetchLiveSuccess:
    """Tests for successful fetch_live responses."""

    @pytest.mark.asyncio
    async def test_returns_extracted_text(self) -> None:
        trafilatura_json = '{"text": "Extracted text", "title": "Example"}'
        with (
            patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls,
            patch(
                "aib.tools.fetch_http.trafilatura.extract",
                return_value=trafilatura_json,
            ),
        ):
            mock_client = AsyncMock()
            mock_client.get.return_value = _make_response()
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://example.com")

        assert isinstance(result, FetchResult)
        assert result.text == "Extracted text"
        assert result.title == "Example"

    @pytest.mark.asyncio
    async def test_plaintext_passthrough(self) -> None:
        with patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_client.get.return_value = _make_response(
                text="Plain text content", content_type="text/plain"
            )
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://example.com/data.txt")

        assert isinstance(result, FetchResult)
        assert result.text == "Plain text content"

    @pytest.mark.asyncio
    async def test_json_passthrough(self) -> None:
        with patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_client.get.return_value = _make_response(
                text='{"key": "value"}', content_type="application/json"
            )
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://api.example.com/data")

        assert isinstance(result, FetchResult)
        assert result.text == '{"key": "value"}'


class TestFetchLiveErrors:
    """Tests for fetch_live error handling."""

    @pytest.mark.asyncio
    async def test_timeout_returns_error(self) -> None:
        with patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_client.get.side_effect = httpx.TimeoutException("timeout")
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://slow.example.com")

        assert isinstance(result, dict)
        assert result["is_error"] is True
        assert "Timeout" in result["content"][0]["text"]

    @pytest.mark.asyncio
    async def test_connect_error_returns_error(self) -> None:
        with patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_client.get.side_effect = httpx.ConnectError("connection refused")
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://down.example.com")

        assert isinstance(result, dict)
        assert result["is_error"] is True
        assert "Could not connect" in result["content"][0]["text"]

    @pytest.mark.asyncio
    async def test_4xx_returns_error_with_hint(self) -> None:
        with patch("aib.tools.fetch_http.httpx.AsyncClient") as mock_cls:
            mock_client = AsyncMock()
            mock_client.get.return_value = _make_response(status_code=403)
            mock_cls.return_value.__aenter__ = AsyncMock(return_value=mock_client)
            mock_cls.return_value.__aexit__ = AsyncMock(return_value=None)

            result = await fetch_live("https://blocked.example.com")

        assert isinstance(result, dict)
        assert result["is_error"] is True
        text = result["content"][0]["text"]
        assert "403" in text
        assert "Access denied" in text


class TestErrorHints:
    """Tests for error hint messages."""

    def test_all_hints_nonempty(self) -> None:
        for status, hint in _ERROR_HINTS.items():
            assert hint, f"Empty hint for HTTP {status}"

    def test_403_mentions_primary_sources(self) -> None:
        hint = _ERROR_HINTS[403]
        assert "search_exa" in hint
        assert "fred_series" in hint or "primary data source" in hint
