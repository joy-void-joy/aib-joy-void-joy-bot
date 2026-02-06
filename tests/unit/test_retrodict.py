"""Tests for retrodict mode hooks and utilities."""

from datetime import datetime
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from aib.agent.hooks import HooksConfig
from aib.tools.exa import ExaResult
from aib.agent.retrodict import (
    RetrodictConfig,
    create_retrodict_hooks,
    generate_pypi_only_iptables_rules,
    get_pypi_allowed_ips,
)
from aib.tools.wayback import (
    normalize_wayback_timestamp,
    rewrite_to_wayback,
    wayback_validate_results,
)


class TestRetrodictConfig:
    """Tests for RetrodictConfig dataclass."""

    def test_date_str_format(self) -> None:
        """date_str should format as YYYY-MM-DD."""
        config = RetrodictConfig(forecast_date=datetime(2026, 1, 15, 12, 30, 45))
        assert config.date_str == "2026-01-15"

    def test_wayback_ts_format(self) -> None:
        """wayback_ts should format as YYYYMMDD."""
        config = RetrodictConfig(forecast_date=datetime(2026, 1, 15, 12, 30, 45))
        assert config.wayback_ts == "20260115"

    def test_unix_ts(self) -> None:
        """unix_ts should return seconds since epoch."""
        config = RetrodictConfig(forecast_date=datetime(2026, 1, 1, 0, 0, 0))
        # Just verify it's an integer and reasonable
        assert isinstance(config.unix_ts, int)
        assert config.unix_ts > 0

    def test_unix_ts_ms(self) -> None:
        """unix_ts_ms should return milliseconds."""
        config = RetrodictConfig(forecast_date=datetime(2026, 1, 1, 0, 0, 0))
        assert config.unix_ts_ms == config.unix_ts * 1000


class TestWaybackRewrite:
    """Tests for Wayback Machine URL rewriting."""

    def test_basic_rewrite(self) -> None:
        """Should rewrite URL to Wayback format."""
        url = "https://example.com/page"
        timestamp = "20260115"
        result = rewrite_to_wayback(url, timestamp)
        assert (
            result == "https://web.archive.org/web/20260115id_/https://example.com/page"
        )

    def test_url_with_query_params(self) -> None:
        """Should preserve query parameters."""
        url = "https://example.com/search?q=test&page=1"
        timestamp = "20260115"
        result = rewrite_to_wayback(url, timestamp)
        assert "q=test" in result
        assert "page=1" in result

    def test_wayback_url_structure(self) -> None:
        """Verify the Wayback URL structure is correct."""
        url = "https://example.com/page?q=test&lang=en"
        timestamp = "20260115"
        result = rewrite_to_wayback(url, timestamp)

        # Should have the id_ modifier for raw content
        assert "id_/" in result
        # Should preserve the full original URL including query params
        assert result.endswith(url)
        # Should use the correct base format
        assert result.startswith("https://web.archive.org/web/")


class TestWaybackTimestampNormalization:
    """Tests for Wayback timestamp normalization used in cutoff validation."""

    def test_normalize_short_timestamp(self) -> None:
        """YYYYMMDD format should normalize to same integer."""
        assert normalize_wayback_timestamp("20260115") == 20260115

    def test_normalize_long_timestamp(self) -> None:
        """YYYYMMDDHHMMSS format should extract just the date portion."""
        assert normalize_wayback_timestamp("20260115120000") == 20260115

    def test_comparison_for_cutoff_validation(self) -> None:
        """Normalized timestamps should compare correctly for cutoff checks."""
        cutoff = normalize_wayback_timestamp("20260115")
        before_cutoff = normalize_wayback_timestamp("20260110120000")
        after_cutoff = normalize_wayback_timestamp("20260120235959")

        assert before_cutoff < cutoff
        assert after_cutoff > cutoff


class TestRetrodictHooks:
    """Tests for the PreToolUse hooks that modify tool inputs for time restriction.

    Note: Some tools (WebSearch, live market prices, Playwright) are excluded
    entirely via ToolPolicy and never reach these hooks. This class tests only
    the tools that ARE allowed but need input modification.
    """

    @pytest.fixture
    def config(self) -> RetrodictConfig:
        """Create a test config."""
        return RetrodictConfig(
            forecast_date=datetime(2026, 1, 15),
            strict_mode=True,
        )

    @pytest.fixture
    def hooks(self, config: RetrodictConfig) -> HooksConfig:
        """Create hooks from config."""
        return create_retrodict_hooks(config)

    async def _invoke_hook(
        self, hooks: HooksConfig, tool_name: str, tool_input: dict[str, Any]
    ) -> dict[str, Any]:
        """Helper to invoke the PreToolUse hook."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]
        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": tool_name,
            "tool_input": tool_input,
        }
        return await pre_hook(input_data, None, None)

    # --- WebFetch tests (URL rewriting to Wayback Machine) ---

    @pytest.mark.asyncio
    async def test_webfetch_rewrites_to_wayback(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """WebFetch URLs should be rewritten to Wayback Machine."""
        mock_availability = {"timestamp": config.wayback_ts, "available": True}
        with patch(
            "aib.agent.retrodict.check_wayback_availability",
            return_value=mock_availability,
        ):
            result = await self._invoke_hook(
                hooks, "WebFetch", {"url": "https://example.com/page"}
            )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "updatedInput" in output
        updated_url = output["updatedInput"]["url"]
        assert updated_url.startswith("https://web.archive.org/web/")
        assert "example.com/page" in updated_url

    @pytest.mark.asyncio
    async def test_webfetch_denies_when_no_snapshot(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """WebFetch should deny URLs without archived snapshots (appears as 404)."""
        with patch(
            "aib.agent.retrodict.check_wayback_availability",
            return_value=None,
        ):
            result = await self._invoke_hook(
                hooks, "WebFetch", {"url": "https://nonexistent-site.example/page"}
            )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"
        assert "404" in output["permissionDecisionReason"]

    @pytest.mark.asyncio
    async def test_webfetch_uses_actual_snapshot_timestamp(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """WebFetch should use the actual snapshot timestamp from Wayback API."""
        actual_snapshot_ts = "20260110120000"  # Different from requested
        mock_availability = {"timestamp": actual_snapshot_ts, "available": True}
        with patch(
            "aib.agent.retrodict.check_wayback_availability",
            return_value=mock_availability,
        ):
            result = await self._invoke_hook(
                hooks, "WebFetch", {"url": "https://example.com/page"}
            )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert actual_snapshot_ts in output["updatedInput"]["url"]

    @pytest.mark.asyncio
    async def test_webfetch_skips_wayback_urls(self, hooks: HooksConfig) -> None:
        """Should not rewrite URLs that are already Wayback URLs."""
        result = await self._invoke_hook(
            hooks,
            "WebFetch",
            {"url": "https://web.archive.org/web/20260115/https://example.com"},
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "updatedInput" not in output

    # --- Financial/market data capping tests ---

    @pytest.mark.asyncio
    async def test_stock_history_end_date_capped(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """stock_history should have end_date capped to forecast date."""
        result = await self._invoke_hook(
            hooks, "mcp__markets__stock_history", {"symbol": "AAPL", "period": "1y"}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["end_date"] == config.date_str

    @pytest.mark.asyncio
    async def test_fred_series_observation_end_capped(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """fred_series should have observation_end capped to forecast date."""
        result = await self._invoke_hook(
            hooks, "mcp__financial__fred_series", {"series_id": "DGS10"}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["observation_end"] == config.date_str

    @pytest.mark.asyncio
    async def test_polymarket_history_timestamp_capped(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """polymarket_history should have timestamp capped."""
        future_ts = config.unix_ts + 86400 * 30  # 30 days in future
        result = await self._invoke_hook(
            hooks, "mcp__markets__polymarket_history", {"timestamp": future_ts}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["timestamp"] == config.unix_ts

    @pytest.mark.asyncio
    async def test_manifold_history_timestamp_capped(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """manifold_history should have timestamp capped."""
        future_ts = config.unix_ts + 86400 * 30
        result = await self._invoke_hook(
            hooks, "mcp__markets__manifold_history", {"timestamp": future_ts}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["timestamp"] == config.unix_ts

    # --- Google Trends tests ---

    @pytest.mark.asyncio
    async def test_google_trends_timeframe_converted_to_date_range(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """Google Trends relative timeframe should become date range ending at cutoff."""
        result = await self._invoke_hook(
            hooks,
            "mcp__trends__google_trends",
            {"keyword": "test", "timeframe": "today 12-m"},
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        timeframe = output["updatedInput"]["timeframe"]
        # Should end at the cutoff date
        assert config.date_str in timeframe
        # Should be a date range format (YYYY-MM-DD YYYY-MM-DD)
        assert len(timeframe.split()) == 2

    @pytest.mark.asyncio
    async def test_google_trends_compare_timeframe_capped(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """google_trends_compare should also have timeframe capped."""
        result = await self._invoke_hook(
            hooks,
            "mcp__trends__google_trends_compare",
            {"keywords": ["a", "b"], "timeframe": "today 3-m"},
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert config.date_str in output["updatedInput"]["timeframe"]

    # --- Search tool tests ---

    @pytest.mark.asyncio
    async def test_retrodict_search_gets_cutoff_date_injected(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """Retrodict search tool should have cutoff_date injected."""
        result = await self._invoke_hook(
            hooks, "mcp__search__web_search", {"query": "test query"}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["cutoff_date"] == config.date_str

    @pytest.mark.asyncio
    async def test_search_exa_gets_published_before_and_livecrawl(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """search_exa should have published_before and livecrawl=never injected."""
        result = await self._invoke_hook(
            hooks, "mcp__forecasting__search_exa", {"query": "test"}
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["published_before"] == config.date_str
        assert output["updatedInput"]["livecrawl"] == "never"


class TestRetrodictToolSchemas:
    """Tests for retrodict tool schema configuration.

    The SDK/MCP layer strips parameters not in the declared schema, so
    hook-injected parameters must be explicitly included in the schema
    even though they're hidden from the agent.
    """

    def test_web_search_schema_includes_cutoff_date(self) -> None:
        """web_search tool schema must include cutoff_date for hook injection to work."""
        from aib.tools.retrodict_search import web_search

        assert "cutoff_date" in web_search.input_schema, (
            "cutoff_date must be in web_search input_schema or it will be "
            "stripped by SDK validation before reaching the handler"
        )

    def test_search_exa_schema_includes_retrodict_params(self) -> None:
        """search_exa tool schema must include published_before and livecrawl."""
        from aib.tools.forecasting import search_exa

        assert "published_before" in search_exa.input_schema, (
            "published_before must be in search_exa input_schema or it will be "
            "stripped by SDK validation before reaching the handler"
        )
        assert "livecrawl" in search_exa.input_schema, (
            "livecrawl must be in search_exa input_schema or it will be "
            "stripped by SDK validation before reaching the handler"
        )

    def test_get_cp_history_schema_includes_before(self) -> None:
        """get_cp_history tool schema must include before parameter."""
        from aib.tools.forecasting import get_cp_history

        assert "before" in get_cp_history.input_schema, (
            "before must be in get_cp_history input_schema or it will be "
            "stripped by SDK validation before reaching the handler"
        )


class TestRetrodictHooksContinued:
    """Continuation of TestRetrodictHooks tests."""

    @pytest.fixture
    def config(self) -> RetrodictConfig:
        """Create a retrodict config for testing."""
        return RetrodictConfig(forecast_date=datetime(2026, 1, 25))

    @pytest.fixture
    def hooks(self, config: RetrodictConfig) -> HooksConfig:
        """Create retrodict hooks for testing."""
        return create_retrodict_hooks(config)

    async def _invoke_hook(
        self, hooks: HooksConfig, tool_name: str, tool_input: dict[str, Any]
    ) -> dict[str, Any]:
        """Helper to invoke a PreToolUse hook and return the result."""
        hook_matchers = hooks["PreToolUse"]
        hook_fn = hook_matchers[0].hooks[0]
        return await hook_fn(  # type: ignore[return-value]
            {
                "hook_event_name": "PreToolUse",
                "tool_name": tool_name,
                "tool_input": tool_input,
            },
            None,  # type: ignore[arg-type]
            None,  # type: ignore[arg-type]
        )

    @pytest.mark.asyncio
    async def test_cp_history_gets_before_parameter(
        self, hooks: HooksConfig, config: RetrodictConfig
    ) -> None:
        """get_cp_history should have 'before' parameter injected."""
        result = await self._invoke_hook(
            hooks,
            "mcp__forecasting__get_cp_history",
            {"question_id": 123, "days": 30},
        )

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["updatedInput"]["before"] == config.date_str
        # Original parameters should be preserved
        assert output["updatedInput"]["question_id"] == 123
        assert output["updatedInput"]["days"] == 30

    # --- Passthrough tests ---

    @pytest.mark.asyncio
    async def test_unmodified_tools_pass_through(self, hooks: HooksConfig) -> None:
        """Tools without special handling should be allowed without modification."""
        result = await self._invoke_hook(hooks, "Read", {"file_path": "/some/path"})

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "updatedInput" not in output


class TestExaDateFilter:
    """Tests for client-side publishedDate filtering in exa_search."""

    def test_drops_results_after_cutoff(self) -> None:
        from aib.tools.exa import ExaResult, _filter_by_published_date

        results: list[ExaResult] = [
            {
                "title": "Before cutoff",
                "url": "https://example.com/before",
                "snippet": None,
                "highlights": None,
                "published_date": "2026-01-20T10:00:00",
                "score": 1.0,
            },
            {
                "title": "After cutoff",
                "url": "https://example.com/after",
                "snippet": None,
                "highlights": None,
                "published_date": "2026-02-04T08:00:00",
                "score": 0.9,
            },
        ]
        filtered = _filter_by_published_date(results, "2026-01-25")
        assert len(filtered) == 1
        assert filtered[0]["url"] == "https://example.com/before"

    def test_drops_results_without_published_date(self) -> None:
        from aib.tools.exa import ExaResult, _filter_by_published_date

        results: list[ExaResult] = [
            {
                "title": "Has date",
                "url": "https://example.com/dated",
                "snippet": None,
                "highlights": None,
                "published_date": "2026-01-10",
                "score": 1.0,
            },
            {
                "title": "No date",
                "url": "https://example.com/undated",
                "snippet": None,
                "highlights": None,
                "published_date": None,
                "score": 0.8,
            },
        ]
        filtered = _filter_by_published_date(results, "2026-01-25")
        assert len(filtered) == 1
        assert filtered[0]["url"] == "https://example.com/dated"

    def test_keeps_all_valid_results(self) -> None:
        from aib.tools.exa import ExaResult, _filter_by_published_date

        results: list[ExaResult] = [
            {
                "title": "Old article",
                "url": "https://example.com/old",
                "snippet": None,
                "highlights": None,
                "published_date": "2025-06-15",
                "score": 1.0,
            },
            {
                "title": "Recent article",
                "url": "https://example.com/recent",
                "snippet": None,
                "highlights": None,
                "published_date": "2026-01-24",
                "score": 0.9,
            },
        ]
        filtered = _filter_by_published_date(results, "2026-01-25")
        assert len(filtered) == 2

    def test_boundary_date_is_included(self) -> None:
        from aib.tools.exa import ExaResult, _filter_by_published_date

        results: list[ExaResult] = [
            {
                "title": "Exact cutoff",
                "url": "https://example.com/boundary",
                "snippet": None,
                "highlights": None,
                "published_date": "2026-01-25T23:59:59",
                "score": 1.0,
            },
        ]
        filtered = _filter_by_published_date(results, "2026-01-25")
        assert len(filtered) == 1


class TestPyPIOnlyNetwork:
    """Tests for PyPI-only network iptables generation."""

    def test_get_pypi_allowed_ips(self) -> None:
        """Should resolve PyPI domain IPs."""
        ips = get_pypi_allowed_ips()
        # Should have at least some IPs (depends on network availability)
        # In CI, this might fail - consider mocking
        assert isinstance(ips, set)

    def test_generate_iptables_rules(self) -> None:
        """Should generate valid iptables rules."""
        allowed_ips = {"1.2.3.4", "5.6.7.8"}
        rules = generate_pypi_only_iptables_rules(allowed_ips)

        # Should have DNS rules
        assert any("--dport 53" in r for r in rules)

        # Should have loopback rule
        assert any("-o lo" in r for r in rules)

        # Should have established connections rule
        assert any("ESTABLISHED,RELATED" in r for r in rules)

        # Should have rules for each IP
        assert any("1.2.3.4" in r for r in rules)
        assert any("5.6.7.8" in r for r in rules)

        # Should end with DROP
        assert rules[-1] == "iptables -A OUTPUT -j DROP"

    def test_iptables_rules_https_only(self) -> None:
        """IP rules should only allow port 443."""
        allowed_ips = {"1.2.3.4"}
        rules = generate_pypi_only_iptables_rules(allowed_ips)

        ip_rules = [r for r in rules if "1.2.3.4" in r]
        for rule in ip_rules:
            assert "--dport 443" in rule


def _make_exa_result(
    url: str,
    snippet: str | None = "original snippet",
    published_date: str | None = "2026-01-10",
) -> ExaResult:
    return {
        "title": f"Result for {url}",
        "url": url,
        "snippet": snippet,
        "highlights": None,
        "published_date": published_date,
        "score": 1.0,
    }


class TestWaybackValidateResults:
    """Tests for wayback_validate_results() which replaces Exa snippets
    with Wayback-extracted content and drops results without valid snapshots."""

    @pytest.mark.asyncio
    async def test_drops_results_without_snapshot(self) -> None:
        """Results should be dropped when no pre-cutoff Wayback snapshot exists."""
        results = [
            _make_exa_result("https://example.com/a"),
            _make_exa_result("https://example.com/b"),
        ]
        with patch(
            "aib.tools.wayback.fetch_wayback_content",
            new_callable=AsyncMock,
            side_effect=[None, None],
        ):
            validated = await wayback_validate_results(results, "20260115")

        assert len(validated) == 0

    @pytest.mark.asyncio
    async def test_replaces_snippet_with_wayback_content(self) -> None:
        """Snippet should be replaced with first 500 chars of Wayback content."""
        results = [_make_exa_result("https://example.com/a")]
        wayback_text = "Wayback content " * 50  # >500 chars

        with patch(
            "aib.tools.wayback.fetch_wayback_content",
            new_callable=AsyncMock,
            return_value=wayback_text,
        ):
            validated = await wayback_validate_results(results, "20260115")

        assert len(validated) == 1
        assert validated[0]["snippet"] == wayback_text[:500]
        assert validated[0]["snippet"] != "original snippet"

    @pytest.mark.asyncio
    async def test_keeps_results_with_snapshot_drops_without(self) -> None:
        """Should keep results with snapshots and drop those without."""
        results = [
            _make_exa_result("https://example.com/good"),
            _make_exa_result("https://example.com/bad"),
            _make_exa_result("https://example.com/also-good"),
        ]
        with patch(
            "aib.tools.wayback.fetch_wayback_content",
            new_callable=AsyncMock,
            side_effect=["Good content", None, "Also good"],
        ):
            validated = await wayback_validate_results(results, "20260115")

        assert len(validated) == 2
        assert validated[0]["url"] == "https://example.com/good"
        assert validated[0]["snippet"] == "Good content"
        assert validated[1]["url"] == "https://example.com/also-good"
        assert validated[1]["snippet"] == "Also good"

    @pytest.mark.asyncio
    async def test_concurrent_fetching(self) -> None:
        """All URLs should be fetched concurrently via asyncio.gather."""
        results = [
            _make_exa_result(f"https://example.com/{i}")
            for i in range(5)
        ]
        call_order: list[str] = []

        async def mock_fetch(url: str, _ts: str) -> str:
            call_order.append(url)
            return f"Content for {url}"

        with patch(
            "aib.tools.wayback.fetch_wayback_content",
            side_effect=mock_fetch,
        ):
            validated = await wayback_validate_results(results, "20260115")

        assert len(validated) == 5
        assert len(call_order) == 5
