"""Retrodict mode hooks for time-restricted forecasting.

Retrodict mode restricts all tools to data available before a given date,
enabling calibration testing on resolved questions without "future leak"
(the agent finding out the answer by searching for news about the resolution).

The hooks work by:
- Appending `before:YYYY-MM-DD` to WebSearch queries
- Rewriting WebFetch URLs to Wayback Machine snapshots (with availability check)
- Capping date parameters on financial tools (FRED, stock_history, trends)
- Injecting `before` parameter to filter CP history data
- Blocking live-only tools (stock_price, manifold_price, polymarket_price)
"""

import logging
import re
import socket
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Any

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.agent.hooks import HooksConfig
from aib.tools.wayback import (
    check_wayback_availability,
    rewrite_to_wayback,
)

logger = logging.getLogger(__name__)


@dataclass
class RetrodictConfig:
    """Configuration for retrodict (blind forecasting) mode.

    Args:
        forecast_date: The date to restrict data access to. All tools
            will behave as if this is "today".
        strict_mode: If True, block tools that can't be reliably restricted.
            If False, allow them with a warning.
    """

    forecast_date: datetime
    strict_mode: bool = True

    @property
    def date_str(self) -> str:
        """Date formatted as YYYY-MM-DD for search filters."""
        return self.forecast_date.strftime("%Y-%m-%d")

    @property
    def wayback_ts(self) -> str:
        """Date formatted as YYYYMMDD for Wayback Machine URLs."""
        return self.forecast_date.strftime("%Y%m%d")

    @property
    def unix_ts(self) -> int:
        """Unix timestamp (seconds since epoch)."""
        return int(self.forecast_date.timestamp())

    @property
    def unix_ts_ms(self) -> int:
        """Unix timestamp in milliseconds (for Manifold API)."""
        return int(self.forecast_date.timestamp() * 1000)


# Tools that need date parameter modification
# Note: Live-only market tools are excluded at MCP server level (see markets.py)
DATE_CAPPABLE_TOOLS = frozenset(
    {
        "mcp__markets__stock_history",
        "mcp__financial__fred_series",
        "mcp__trends__google_trends",
        "mcp__trends__google_trends_compare",
    }
)


def _parse_trends_duration(timeframe: str) -> int:
    """Parse Google Trends timeframe to get duration in days.

    Supported formats:
    - 'now 1-H' -> 1 hour (rounds to 1 day)
    - 'now 4-H' -> 4 hours (rounds to 1 day)
    - 'now 1-d' -> 1 day
    - 'now 7-d' -> 7 days
    - 'today 1-m' -> 30 days (1 month)
    - 'today 3-m' -> 90 days (3 months)
    - 'today 12-m' -> 365 days (12 months)
    - 'today 5-y' -> 1825 days (5 years)
    - 'all' -> 10 years (approximate)
    - '2020-01-01 2020-12-31' -> exact date range

    Args:
        timeframe: Google Trends timeframe string.

    Returns:
        Duration in days.
    """
    timeframe = timeframe.lower().strip()

    # Handle 'all' - use 10 years as approximation
    if timeframe == "all":
        return 3650

    # Handle date range format: 'YYYY-MM-DD YYYY-MM-DD'
    date_range_match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\d{4}-\d{2}-\d{2})", timeframe)
    if date_range_match:
        start_date = datetime.strptime(date_range_match.group(1), "%Y-%m-%d")
        end_date = datetime.strptime(date_range_match.group(2), "%Y-%m-%d")
        return (end_date - start_date).days

    # Handle relative formats: 'now X-Y' or 'today X-Y'
    relative_match = re.match(r"(now|today)\s+(\d+)-([hdmy])", timeframe)
    if relative_match:
        value = int(relative_match.group(2))
        unit = relative_match.group(3)

        if unit == "h":
            return max(1, value // 24)  # Hours -> days, minimum 1
        elif unit == "d":
            return value
        elif unit == "m":
            return value * 30  # Months -> days
        elif unit == "y":
            return value * 365  # Years -> days

    # Default to 1 year if unrecognized
    return 365


def _cap_trends_timeframe(timeframe: str, cutoff_date: datetime) -> str:
    """Convert trends timeframe to date range ending at cutoff.

    Preserves the requested duration while ensuring end date doesn't exceed
    the retrodict cutoff.

    Args:
        timeframe: Original Google Trends timeframe.
        cutoff_date: Maximum end date (retrodict cutoff).

    Returns:
        Date range string in 'YYYY-MM-DD YYYY-MM-DD' format.
    """
    duration_days = _parse_trends_duration(timeframe)
    start_date = cutoff_date - timedelta(days=duration_days)
    return f"{start_date.strftime('%Y-%m-%d')} {cutoff_date.strftime('%Y-%m-%d')}"


def create_retrodict_hooks(config: RetrodictConfig) -> HooksConfig:
    """Create hooks that restrict tool access to data before forecast_date.

    Args:
        config: Retrodict configuration with forecast date and mode settings.

    Returns:
        HooksConfig for ClaudeAgentOptions with PreToolUse hook.
    """

    async def pre_tool_use_hook(
        input_data: Any,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> dict[str, Any]:
        """Filter and modify tool inputs for time restriction."""
        if input_data.get("hook_event_name") != "PreToolUse":
            return {}

        tool_name = input_data.get("tool_name", "")
        tool_input = input_data.get("tool_input", {})
        hook_event = input_data["hook_event_name"]

        def deny(reason: str, hint: str = "") -> dict[str, Any]:
            msg = reason
            if hint:
                msg += f" {hint}"
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "deny",
                    "permissionDecisionReason": msg,
                }
            }

        def modify_input(new_input: dict[str, Any]) -> dict[str, Any]:
            """Return modified tool input."""
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                    "modifiedInput": new_input,
                }
            }

        def allow() -> dict[str, Any]:
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                }
            }

        # Note: Tools excluded via policy in retrodict mode:
        # - WebSearch (unreliable before: operator)
        # - search_news (no date filtering)
        # - Live market tools (stock_price, polymarket_price, manifold_price)
        # - Playwright tools

        # web_search (search server): Inject cutoff_date for Wayback validation
        if tool_name == "mcp__search__web_search":
            new_input = {**tool_input, "cutoff_date": config.date_str}
            logger.info(
                "[Retrodict] web_search cutoff_date injected: %s",
                config.date_str,
            )
            return modify_input(new_input)

        # WebFetch: Check Wayback availability and rewrite URL
        if tool_name == "WebFetch":
            url = tool_input.get("url", "")
            if url and "web.archive.org" not in url:
                # Check if snapshot exists before rewriting (rate-limited, validates cutoff)
                availability = await check_wayback_availability(
                    url, config.wayback_ts, validate_before_cutoff=True
                )

                if availability is None:
                    logger.warning(
                        "[Retrodict] No valid Wayback snapshot for %s at %s",
                        url,
                        config.wayback_ts,
                    )
                    return deny("HTTP 404: URL not found or unavailable.")

                actual_ts = availability.get("timestamp", config.wayback_ts)
                wayback_url = rewrite_to_wayback(url, actual_ts)
                logger.info(
                    "[Retrodict] WebFetch URL rewritten to Wayback: %s -> %s (snapshot: %s)",
                    url,
                    wayback_url,
                    actual_ts,
                )
                new_input = {**tool_input, "url": wayback_url}
                return modify_input(new_input)
            return allow()

        # stock_history: Cap end parameter
        if tool_name == "mcp__markets__stock_history":
            # yfinance uses period by default, but we can also accept start/end
            # For retrodict, we'll add end_date to cap the data
            new_input = {**tool_input, "end_date": config.date_str}
            logger.info("[Retrodict] stock_history capped to %s", config.date_str)
            return modify_input(new_input)

        # FRED: Cap observation_end
        if tool_name == "mcp__financial__fred_series":
            new_input = {**tool_input, "observation_end": config.date_str}
            logger.info("[Retrodict] fred_series capped to %s", config.date_str)
            return modify_input(new_input)

        # Google Trends: Cap timeframe while preserving requested duration
        if tool_name in (
            "mcp__trends__google_trends",
            "mcp__trends__google_trends_compare",
        ):
            current_timeframe = tool_input.get("timeframe", "today 12-m")
            new_timeframe = _cap_trends_timeframe(
                current_timeframe, config.forecast_date
            )
            new_input = {**tool_input, "timeframe": new_timeframe}
            logger.info(
                "[Retrodict] trends timeframe capped: %s -> %s",
                current_timeframe,
                new_timeframe,
            )
            return modify_input(new_input)

        # get_cp_history: Inject 'before' parameter to filter out future data
        if tool_name == "mcp__forecasting__get_cp_history":
            new_input = {**tool_input, "before": config.date_str}
            logger.info("[Retrodict] get_cp_history capped to %s", config.date_str)
            return modify_input(new_input)

        # search_exa: Add publishedBefore and disable livecrawl
        if tool_name == "mcp__forecasting__search_exa":
            new_input = {
                **tool_input,
                "published_before": config.date_str,
                "livecrawl": "never",
            }
            logger.info(
                "[Retrodict] search_exa capped to %s with livecrawl=never",
                config.date_str,
            )
            return modify_input(new_input)

        # wikipedia: Inject cutoff_date for historical revision lookup
        if tool_name == "mcp__forecasting__wikipedia":
            new_input = {**tool_input, "cutoff_date": config.date_str}
            logger.info("[Retrodict] wikipedia cutoff_date injected: %s", config.date_str)
            return modify_input(new_input)

        # get_metaculus_questions: Inject cutoff_date to hide current CP
        if tool_name == "mcp__forecasting__get_metaculus_questions":
            new_input = {**tool_input, "cutoff_date": config.date_str}
            logger.info(
                "[Retrodict] get_metaculus_questions cutoff_date injected: %s",
                config.date_str,
            )
            return modify_input(new_input)

        # search_arxiv: Inject cutoff_date to filter papers by publication date
        if tool_name == "mcp__arxiv__search_arxiv":
            new_input = {**tool_input, "cutoff_date": config.date_str}
            logger.info("[Retrodict] search_arxiv cutoff_date injected: %s", config.date_str)
            return modify_input(new_input)

        # google_trends_related: Cap timeframe (same as google_trends)
        if tool_name == "mcp__trends__google_trends_related":
            current_timeframe = tool_input.get("timeframe", "today 12-m")
            new_timeframe = _cap_trends_timeframe(
                current_timeframe, config.forecast_date
            )
            new_input = {**tool_input, "timeframe": new_timeframe}
            logger.info(
                "[Retrodict] google_trends_related timeframe capped: %s -> %s",
                current_timeframe,
                new_timeframe,
            )
            return modify_input(new_input)

        # polymarket_history: Cap timestamp to retrodict cutoff
        if tool_name == "mcp__markets__polymarket_history":
            timestamp = tool_input.get("timestamp", 0)
            capped_ts = min(timestamp, config.unix_ts)
            if timestamp != capped_ts:
                logger.info(
                    "[Retrodict] polymarket_history timestamp capped: %d -> %d",
                    timestamp,
                    capped_ts,
                )
            new_input = {**tool_input, "timestamp": capped_ts}
            return modify_input(new_input)

        # manifold_history: Cap timestamp to retrodict cutoff
        if tool_name == "mcp__markets__manifold_history":
            timestamp = tool_input.get("timestamp", 0)
            capped_ts = min(timestamp, config.unix_ts)
            if timestamp != capped_ts:
                logger.info(
                    "[Retrodict] manifold_history timestamp capped: %d -> %d",
                    timestamp,
                    capped_ts,
                )
            new_input = {**tool_input, "timestamp": capped_ts}
            return modify_input(new_input)

        # Allow all other tools
        return allow()

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_use_hook])],  # type: ignore[list-item]
    }


def get_pypi_allowed_ips() -> set[str]:
    """Resolve current IP addresses for PyPI domains.

    PyPI uses Fastly CDN, so IPs may change. We resolve at sandbox start
    to get current addresses for iptables rules.

    Returns:
        Set of IP addresses that should be allowed for pip installs.
    """
    pypi_domains = [
        "pypi.org",
        "files.pythonhosted.org",
        "pypi.python.org",
    ]

    allowed_ips: set[str] = set()
    for domain in pypi_domains:
        try:
            for info in socket.getaddrinfo(domain, 443):
                # info[4] is sockaddr tuple: (address, port) for IPv4
                # or (address, port, flowinfo, scope_id) for IPv6
                addr = info[4][0]
                if isinstance(addr, str):
                    allowed_ips.add(addr)
        except socket.gaierror as e:
            logger.warning("Failed to resolve %s: %s", domain, e)

    logger.info("Resolved %d PyPI IP addresses", len(allowed_ips))
    return allowed_ips


def generate_pypi_only_iptables_rules(allowed_ips: set[str]) -> list[str]:
    """Generate iptables rules to allow only PyPI traffic.

    Args:
        allowed_ips: Set of IP addresses to allow (from get_pypi_allowed_ips)

    Returns:
        List of iptables commands to execute in the container.
    """
    rules = [
        # Allow DNS (needed to resolve pypi.org)
        "iptables -A OUTPUT -p udp --dport 53 -j ACCEPT",
        "iptables -A OUTPUT -p tcp --dport 53 -j ACCEPT",
        # Allow loopback
        "iptables -A OUTPUT -o lo -j ACCEPT",
        # Allow established connections (responses to our requests)
        "iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT",
    ]

    # Allow PyPI IPs on HTTPS
    for ip in sorted(allowed_ips):
        rules.append(f"iptables -A OUTPUT -d {ip} -p tcp --dport 443 -j ACCEPT")

    # Drop everything else
    rules.append("iptables -A OUTPUT -j DROP")

    return rules
