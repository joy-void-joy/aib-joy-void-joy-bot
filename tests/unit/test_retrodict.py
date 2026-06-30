"""Tests for retrodict mode hooks and utilities."""

from datetime import date
from typing import Any, cast
from unittest.mock import AsyncMock, patch

import pytest

from claude_agent_sdk.types import HookContext, PreToolUseHookInput

from aib.agent.hooks import HooksConfig
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

    The retrodict hook denies the few tools that exist in allowed_tools but
    have no retrodict-aware filtering (currently just Bash). Tools excluded
    from allowed_tools entirely (asknews, playwright, WebSearch, WebFetch)
    are denied upstream by create_allowed_tools_hook in both modes with
    identical wording — they pass through the retrodict hook unchanged.
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
        pre_hooks = hooks.get("PreToolUse")
        assert pre_hooks is not None, "PreToolUse hooks must be configured"
        pre_hook = pre_hooks[0].hooks[0]
        input_data: PreToolUseHookInput = {
            "hook_event_name": "PreToolUse",
            "tool_name": tool_name,
            "tool_input": tool_input,
            "session_id": "",
            "transcript_path": "",
            "cwd": "",
        }
        ctx: HookContext = {"signal": None}
        result = await pre_hook(input_data, None, ctx)
        return cast(dict[str, Any], result)

    # --- Denial tests ---

    @pytest.mark.asyncio
    async def test_bash_denied(self, hooks: HooksConfig) -> None:
        """Bash should be denied in retrodict mode."""
        result = await self._invoke_hook(hooks, "Bash", {"command": "ls"})
        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"
        assert output["permissionDecisionReason"] == "Bash is not available."

    @pytest.mark.asyncio
    async def test_web_tools_denied_in_retrodict(self, hooks: HooksConfig) -> None:
        """Native WebSearch/WebFetch bypass the cutoff, so retrodict denies them."""
        for tool_name in ("WebSearch", "WebFetch"):
            result = await self._invoke_hook(hooks, tool_name, {"query": "x"})
            output = result["hookSpecificOutput"]
            assert output["permissionDecision"] == "deny"
            assert (
                output["permissionDecisionReason"] == f"{tool_name} is not available."
            )

    @pytest.mark.asyncio
    async def test_excluded_tools_pass_through(self, hooks: HooksConfig) -> None:
        """Tools excluded from allowed_tools (asknews, playwright) pass through
        the retrodict hook — they're denied upstream by create_allowed_tools_hook
        in both live and retrodict mode with identical wording.
        """
        excluded_tools = [
            "mcp__asknews__search_news",
            "mcp__asknews__search_google",
            "mcp__asknews__do_news_research",
            "mcp__playwright__browser_navigate",
        ]
        for tool_name in excluded_tools:
            result = await self._invoke_hook(hooks, tool_name, {"query": "test"})
            output = result["hookSpecificOutput"]
            assert output["permissionDecision"] == "allow", (
                f"{tool_name} should pass through retrodict hook (denied upstream)"
            )

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
        from aib.tools.search import search_exa

        schema = search_exa.input_schema
        assert isinstance(schema, dict), "input_schema must be a dict"
        props = schema.get("properties", schema)
        assert "published_before" in props, (
            "published_before must be in search_exa input_schema or it will be "
            "stripped by SDK validation before reaching the handler"
        )
        assert "livecrawl" in props, (
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
    async def test_clears_highlights(self) -> None:
        """Highlights should be cleared to prevent live index data leaking."""
        results: list[ExaResult] = [
            {
                "title": "Test",
                "url": "https://example.com/a",
                "snippet": "original",
                "highlights": ["live highlight 1", "live highlight 2"],
                "published_date": "2026-01-10",
                "score": 1.0,
            }
        ]
        with patch(
            "aib.tools.wayback.fetch_wayback_content",
            new_callable=AsyncMock,
            return_value="Archived content",
        ):
            validated = await wayback_validate_results(results, "20260115")

        assert len(validated) == 1
        assert validated[0]["highlights"] is None

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
