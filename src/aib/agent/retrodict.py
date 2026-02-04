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
import socket
from dataclasses import dataclass
from datetime import datetime
from typing import Any

import httpx
from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.tools.retry import with_retry

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


def _rewrite_to_wayback(url: str, timestamp: str) -> str:
    """Rewrite a URL to use Wayback Machine snapshot.

    The Wayback Machine URL format appends the original URL directly after the
    timestamp - no encoding needed. The 'id_' modifier returns raw content
    without the Wayback toolbar injection.

    Args:
        url: Original URL to fetch (e.g., "https://example.com/search?q=test")
        timestamp: Wayback timestamp format (YYYYMMDD or YYYYMMDDHHMMSS)

    Returns:
        Wayback Machine URL for the closest snapshot before the timestamp.

    Example:
        >>> _rewrite_to_wayback("https://example.com/page?q=1", "20260115")
        'https://web.archive.org/web/20260115id_/https://example.com/page?q=1'
    """
    return f"https://web.archive.org/web/{timestamp}id_/{url}"


@with_retry(max_attempts=2)
async def _check_wayback_availability(
    url: str, timestamp: str
) -> dict[str, Any] | None:
    """Check if a URL has a Wayback Machine snapshot near the given timestamp.

    Uses the Wayback Availability API to check for archived snapshots before
    attempting to rewrite URLs. This prevents errors when URLs aren't archived.

    Args:
        url: The original URL to check.
        timestamp: Wayback timestamp format (YYYYMMDD or YYYYMMDDHHMMSS).

    Returns:
        Dict with snapshot info if available (contains 'url', 'timestamp', 'status'),
        or None if no snapshot exists near the requested time.

    API docs: https://archive.org/help/wayback_api.php
    """
    async with httpx.AsyncClient(timeout=10.0) as client:
        response = await client.get(
            "https://archive.org/wayback/available",
            params={"url": url, "timestamp": timestamp},
        )
        response.raise_for_status()
        data = response.json()

    snapshots = data.get("archived_snapshots", {})
    closest = snapshots.get("closest")
    if closest and closest.get("available"):
        return closest
    return None


def create_retrodict_hooks(config: RetrodictConfig) -> dict[str, Any]:
    """Create hooks that restrict tool access to data before forecast_date.

    Args:
        config: Retrodict configuration with forecast date and mode settings.

    Returns:
        Hooks dict for ClaudeAgentOptions with PreToolUse and PostToolUse hooks.
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

        # Note: Live-only tools (stock_price, polymarket_price, manifold_price)
        # are excluded from allowed_tools in retrodict mode (see core.py)

        # WebSearch: Append before: operator
        if tool_name == "WebSearch":
            query = tool_input.get("query", "")
            if query and f"before:{config.date_str}" not in query:
                modified_query = f"{query} before:{config.date_str}"
                logger.info(
                    "[Retrodict] WebSearch query modified: %r -> %r",
                    query,
                    modified_query,
                )
                new_input = {**tool_input, "query": modified_query}
                return modify_input(new_input)
            return allow()

        # WebFetch: Check Wayback availability and rewrite URL
        if tool_name == "WebFetch":
            url = tool_input.get("url", "")
            if url and "web.archive.org" not in url:
                # Check if snapshot exists before rewriting
                try:
                    availability = await _check_wayback_availability(
                        url, config.wayback_ts
                    )
                except httpx.HTTPError as e:
                    logger.warning(
                        "[Retrodict] Wayback availability check failed: %s", e
                    )
                    # Proceed anyway with requested timestamp
                    availability = {"timestamp": config.wayback_ts}

                if availability is None:
                    logger.warning(
                        "[Retrodict] No Wayback snapshot for %s at %s",
                        url,
                        config.wayback_ts,
                    )
                    return deny(f"HTTP 404: URL not found or unavailable.")

                # Validate snapshot is not after the cutoff (Wayback returns "closest"
                # which could be after the requested date)
                actual_ts = availability.get("timestamp", config.wayback_ts)
                if actual_ts > config.wayback_ts:
                    logger.warning(
                        "[Retrodict] Wayback closest snapshot (%s) is after cutoff (%s)",
                        actual_ts,
                        config.wayback_ts,
                    )
                    return deny(f"HTTP 404: URL not found or unavailable.")

                wayback_url = _rewrite_to_wayback(url, actual_ts)
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

        # Google Trends: Cap timeframe
        if tool_name in (
            "mcp__trends__google_trends",
            "mcp__trends__google_trends_compare",
        ):
            # Trends uses timeframe like "today 3-m" or "2020-01-01 2020-12-31"
            # We'll override with a specific end date
            current_timeframe = tool_input.get("timeframe", "today 12-m")
            # Convert to date range ending at forecast_date
            start_date = config.forecast_date.replace(
                year=config.forecast_date.year - 1
            )
            new_timeframe = f"{start_date.strftime('%Y-%m-%d')} {config.date_str}"
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
