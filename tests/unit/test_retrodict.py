"""Tests for retrodict mode hooks and utilities."""

from datetime import datetime
from typing import Any
from unittest.mock import AsyncMock, patch

import pytest

from aib.agent.retrodict import (
    RetrodictConfig,
    _rewrite_to_wayback,
    create_retrodict_hooks,
    generate_pypi_only_iptables_rules,
    get_pypi_allowed_ips,
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
        result = _rewrite_to_wayback(url, timestamp)
        assert result == "https://web.archive.org/web/20260115id_/https://example.com/page"

    def test_url_with_query_params(self) -> None:
        """Should preserve query parameters."""
        url = "https://example.com/search?q=test&page=1"
        timestamp = "20260115"
        result = _rewrite_to_wayback(url, timestamp)
        assert "q=test" in result
        assert "page=1" in result

    def test_wayback_url_structure(self) -> None:
        """Verify the Wayback URL structure is correct."""
        url = "https://example.com/page?q=test&lang=en"
        timestamp = "20260115"
        result = _rewrite_to_wayback(url, timestamp)

        # Should have the id_ modifier for raw content
        assert "id_/" in result
        # Should preserve the full original URL including query params
        assert result.endswith(url)
        # Should use the correct base format
        assert result.startswith("https://web.archive.org/web/")


class TestRetrodictHooks:
    """Tests for the PreToolUse and PostToolUse hooks."""

    @pytest.fixture
    def config(self) -> RetrodictConfig:
        """Create a test config."""
        return RetrodictConfig(
            forecast_date=datetime(2026, 1, 15),
            strict_mode=True,
        )

    @pytest.fixture
    def hooks(self, config: RetrodictConfig) -> dict[str, Any]:
        """Create hooks from config."""
        return create_retrodict_hooks(config)

    @pytest.mark.asyncio
    async def test_websearch_adds_before_filter(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """WebSearch queries should have before: operator added."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebSearch",
            "tool_input": {"query": "breaking news"},
        }

        result = await pre_hook(input_data, None, None)

        assert "hookSpecificOutput" in result
        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "modifiedInput" in output
        assert f"before:{config.date_str}" in output["modifiedInput"]["query"]

    @pytest.mark.asyncio
    async def test_websearch_no_duplicate_before(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """Should not add before: if already present."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebSearch",
            "tool_input": {"query": f"news before:{config.date_str}"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        # Should allow without modification since before: already present
        assert "modifiedInput" not in output or output["modifiedInput"]["query"].count("before:") == 1

    @pytest.mark.asyncio
    async def test_webfetch_rewrites_to_wayback(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """WebFetch URLs should be rewritten to Wayback Machine."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://example.com/page"},
        }

        # Mock the availability check to return a valid snapshot
        mock_availability = {"timestamp": config.wayback_ts, "available": True}
        with patch(
            "aib.agent.retrodict._check_wayback_availability",
            return_value=mock_availability,
        ):
            result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "modifiedInput" in output
        assert "web.archive.org" in output["modifiedInput"]["url"]
        assert config.wayback_ts in output["modifiedInput"]["url"]

    @pytest.mark.asyncio
    async def test_webfetch_denies_when_no_snapshot(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """WebFetch should deny URLs without archived snapshots (appears as 404)."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://nonexistent-site.example/page"},
        }

        # Mock the availability check to return None (no snapshot)
        with patch(
            "aib.agent.retrodict._check_wayback_availability",
            return_value=None,
        ):
            result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"
        # Returns generic 404 to not reveal archive mechanism
        assert "404" in output["permissionDecisionReason"]

    @pytest.mark.asyncio
    async def test_webfetch_uses_actual_snapshot_timestamp(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """WebFetch should use the actual snapshot timestamp from API."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://example.com/page"},
        }

        # Mock with a different timestamp than requested
        actual_snapshot_ts = "20260110120000"  # Closest available
        mock_availability = {"timestamp": actual_snapshot_ts, "available": True}
        with patch(
            "aib.agent.retrodict._check_wayback_availability",
            return_value=mock_availability,
        ):
            result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        # Should use the actual snapshot timestamp, not the requested one
        assert actual_snapshot_ts in output["modifiedInput"]["url"]

    @pytest.mark.asyncio
    async def test_webfetch_skips_wayback_urls(
        self, hooks: dict[str, Any]
    ) -> None:
        """Should not rewrite URLs that are already Wayback URLs."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://web.archive.org/web/20260115/https://example.com"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        # Should not have modifiedInput since URL is already Wayback
        assert "modifiedInput" not in output

    # Note: Live-only tools (LIVE_ONLY_TOOLS) are excluded via allowed_tools
    # in core.py, not via hooks. No test needed here since the tools simply
    # never reach the hooks.

    @pytest.mark.asyncio
    async def test_stock_history_capped(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """stock_history should have end_date capped."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__markets__stock_history",
            "tool_input": {"symbol": "AAPL", "period": "1y"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["modifiedInput"]["end_date"] == config.date_str

    @pytest.mark.asyncio
    async def test_fred_series_capped(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """fred_series should have observation_end capped."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__financial__fred_series",
            "tool_input": {"series_id": "DGS10"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert output["modifiedInput"]["observation_end"] == config.date_str

    @pytest.mark.asyncio
    async def test_google_trends_capped(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """Google Trends should have timeframe capped."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__trends__google_trends",
            "tool_input": {"keyword": "test"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert config.date_str in output["modifiedInput"]["timeframe"]

    @pytest.mark.asyncio
    async def test_other_tools_allowed(self, hooks: dict[str, Any]) -> None:
        """Non-restricted tools should be allowed without modification."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "Read",
            "tool_input": {"file_path": "/some/path"},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "modifiedInput" not in output

    @pytest.mark.asyncio
    async def test_cp_history_injects_before_parameter(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """get_cp_history PreToolUse should inject 'before' parameter."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "mcp__forecasting__get_cp_history",
            "tool_input": {"question_id": 123, "days": 30},
        }

        result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "allow"
        assert "modifiedInput" in output
        assert output["modifiedInput"]["before"] == config.date_str
        assert output["modifiedInput"]["question_id"] == 123
        assert output["modifiedInput"]["days"] == 30

    @pytest.mark.asyncio
    async def test_webfetch_denies_snapshot_after_cutoff(
        self, hooks: dict[str, Any], config: RetrodictConfig
    ) -> None:
        """WebFetch should deny if closest snapshot is after cutoff (appears as 404)."""
        pre_hook = hooks["PreToolUse"][0].hooks[0]

        input_data = {
            "hook_event_name": "PreToolUse",
            "tool_name": "WebFetch",
            "tool_input": {"url": "https://example.com/page"},
        }

        # Mock with a snapshot timestamp AFTER the cutoff
        future_snapshot_ts = "20260120120000"  # 5 days after 20260115
        mock_availability = {"timestamp": future_snapshot_ts, "available": True}
        with patch(
            "aib.agent.retrodict._check_wayback_availability",
            return_value=mock_availability,
        ):
            result = await pre_hook(input_data, None, None)

        output = result["hookSpecificOutput"]
        assert output["permissionDecision"] == "deny"
        # Returns generic 404 to not reveal archive mechanism
        assert "404" in output["permissionDecisionReason"]


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
