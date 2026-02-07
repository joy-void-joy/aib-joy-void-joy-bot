"""Tests for retrodict mode hooks and utilities."""

from datetime import date
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from aib.agent.hooks import HooksConfig
from aib.agent.subagents import get_subagents
from aib.tools.exa import ExaResult
from aib.agent.retrodict import (
    create_retrodict_hooks,
    generate_pypi_only_iptables_rules,
    get_pypi_allowed_ips,
)
from aib.retrodict_context import retrodict_cutoff
from aib.tools.wayback import (
    normalize_wayback_timestamp,
    rewrite_to_wayback,
    wayback_validate_results,
)


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
    """Tests for the PreToolUse hooks.

    The hooks handle:
    - Denying tools with no retrodict support (WebSearch, Playwright, search_news)
    - Rewriting WebFetch URLs to Wayback Machine
    - Allowing everything else (tools read ContextVar internally)
    """

    @pytest.fixture(autouse=True)
    def set_cutoff(self) -> Any:
        """Set retrodict_cutoff ContextVar for all tests."""
        token = retrodict_cutoff.set(date(2026, 1, 15))
        yield
        retrodict_cutoff.reset(token)

    @pytest.fixture
    def hooks(self) -> HooksConfig:
        """Create hooks (reads ContextVar internally)."""
        return create_retrodict_hooks()

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

    # --- Denial tests ---

    @pytest.mark.asyncio
    async def test_websearch_denied(self, hooks: HooksConfig) -> None:
        """WebSearch should be denied with hint to use web_search."""
        result = await self._invoke_hook(hooks, "WebSearch", {"query": "test"})
        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"
        assert "web_search" in output["permissionDecisionReason"]

    @pytest.mark.asyncio
    async def test_search_news_denied(self, hooks: HooksConfig) -> None:
        """search_news should be denied in retrodict mode."""
        result = await self._invoke_hook(
            hooks, "mcp__forecasting__search_news", {"query": "test"}
        )
        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"

    @pytest.mark.asyncio
    async def test_playwright_denied(self, hooks: HooksConfig) -> None:
        """Playwright tools should be denied in retrodict mode."""
        result = await self._invoke_hook(
            hooks, "mcp__playwright__browser_navigate", {"url": "https://example.com"}
        )
        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"

    # --- WebFetch tests (URL rewriting to Wayback Machine) ---

    @pytest.mark.asyncio
    async def test_webfetch_rewrites_to_wayback(self, hooks: HooksConfig) -> None:
        """WebFetch URLs should be rewritten to Wayback Machine."""
        mock_availability = {"timestamp": "20260115", "available": True}
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
    async def test_webfetch_denies_when_no_snapshot(self, hooks: HooksConfig) -> None:
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
        self, hooks: HooksConfig
    ) -> None:
        """WebFetch should use the actual snapshot timestamp from Wayback API."""
        actual_snapshot_ts = "20260110120000"
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

    # --- Passthrough tests ---

    @pytest.mark.asyncio
    async def test_unmodified_tools_pass_through(self, hooks: HooksConfig) -> None:
        """Tools without special handling should be allowed without modification."""
        result = await self._invoke_hook(hooks, "Read", {"file_path": "/some/path"})

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "updatedInput" not in output

    @pytest.mark.asyncio
    async def test_no_cutoff_passes_through(self) -> None:
        """When no cutoff is set, all tools should pass through."""
        # Reset the cutoff set by the autouse fixture
        token = retrodict_cutoff.set(None)
        try:
            hooks = create_retrodict_hooks()
            result = await self._invoke_hook(hooks, "WebSearch", {"query": "test"})
            assert result == {}
        finally:
            retrodict_cutoff.reset(token)


class TestRetrodictToolSchemas:
    """Tests for retrodict tool schema configuration.

    Tools that support user-provided date filtering must include
    those params in the schema so the SDK doesn't strip them.
    """

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


class TestExaDateFilter:
    """Tests for client-side publishedDate filtering in exa_search."""

    def test_drops_results_after_cutoff(self) -> None:
        from aib.tools.exa import _filter_by_published_date

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
        from aib.tools.exa import _filter_by_published_date

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
        from aib.tools.exa import _filter_by_published_date

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
        from aib.tools.exa import _filter_by_published_date

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
        results = [_make_exa_result(f"https://example.com/{i}") for i in range(5)]
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


class TestRetrodictSubagentTools:
    """Tests for retrodict-aware subagent tool lists."""

    def test_search_news_excluded_in_retrodict(self) -> None:
        """search_news should be excluded from all subagents in retrodict mode."""
        with retrodict_cutoff.set(date(2026, 1, 15)):
            subagents = get_subagents()
            for name, agent_def in subagents.items():
                tools = agent_def.tools or []
                assert "mcp__forecasting__search_news" not in tools, (
                    f"search_news should be excluded from {name} in retrodict mode"
                )

    def test_search_news_included_normally(self) -> None:
        """search_news should be included when not in retrodict mode."""
        with (
            patch("aib.agent.subagents.settings.asknews_client_id", "test"),
            patch("aib.agent.subagents.settings.asknews_client_secret", "test"),
        ):
            subagents = get_subagents()
            all_tools = []
            for agent_def in subagents.values():
                all_tools.extend(agent_def.tools or [])
            assert "mcp__forecasting__search_news" in all_tools

    def test_search_news_excluded_with_credentials_in_retrodict(self) -> None:
        """search_news should be excluded even with credentials in retrodict mode."""
        with (
            retrodict_cutoff.set(date(2026, 1, 15)),
            patch("aib.agent.subagents.settings.asknews_client_id", "test"),
            patch("aib.agent.subagents.settings.asknews_client_secret", "test"),
        ):
            subagents = get_subagents()
            for name, agent_def in subagents.items():
                tools = agent_def.tools or []
                assert "mcp__forecasting__search_news" not in tools, (
                    f"search_news should be excluded from {name} in retrodict mode"
                )

    def test_search_exa_always_available(self) -> None:
        """search_exa should be available in both modes (has internal date filter)."""
        with retrodict_cutoff.set(date(2026, 1, 15)):
            subagents = get_subagents()
            all_tools = []
            for agent_def in subagents.values():
                all_tools.extend(agent_def.tools or [])
            assert "mcp__forecasting__search_exa" in all_tools
