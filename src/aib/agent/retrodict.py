"""Retrodict mode hooks for time-restricted forecasting.

Retrodict mode restricts all tools to data available before a given date,
enabling calibration testing on resolved questions without "future leak"
(the agent finding out the answer by searching for news about the resolution).

The hooks work by:
- Appending `before:YYYY-MM-DD` to WebSearch queries
- Rewriting WebFetch URLs to Wayback Machine snapshots
- Capping date parameters on financial tools (FRED, stock_history, trends)
- Blocking live-only tools (stock_price, manifold_price, polymarket_price)
- Filtering PostToolUse responses to remove data after the cutoff
"""

import logging
import socket
from dataclasses import dataclass
from datetime import datetime
from typing import Any
from urllib.parse import quote

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

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


# Tools that return live data and cannot be reliably restricted
LIVE_ONLY_TOOLS = frozenset(
    {
        "mcp__markets__stock_price",
        "mcp__markets__polymarket_price",
        "mcp__markets__manifold_price",
    }
)

# Tools that need date parameter modification
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

    Args:
        url: Original URL to fetch
        timestamp: Wayback timestamp format (YYYYMMDD or YYYYMMDDHHMMSS)

    Returns:
        Wayback Machine URL for the closest snapshot before the timestamp.
    """
    # Wayback URL format: web.archive.org/web/{timestamp}id_/{url}
    # The "id_" modifier returns the original content without Wayback toolbar
    # Preserve URL structure including query parameters (safe chars: :/?&=)
    encoded_url = quote(url, safe=":/?&=")
    return f"https://web.archive.org/web/{timestamp}id_/{encoded_url}"


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
            msg = f"[Retrodict mode] {reason}"
            if hint:
                msg += f" Hint: {hint}"
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

        # Block live-only tools
        if tool_name in LIVE_ONLY_TOOLS:
            hints = {
                "mcp__markets__stock_price": "Use mcp__markets__stock_history with end_date instead.",
                "mcp__markets__polymarket_price": "Use mcp__markets__polymarket_history instead.",
                "mcp__markets__manifold_price": "Use mcp__markets__manifold_history instead.",
            }
            return deny(
                f"Tool '{tool_name}' returns live data only.",
                hints.get(tool_name, ""),
            )

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

        # WebFetch: Rewrite to Wayback Machine
        if tool_name == "WebFetch":
            url = tool_input.get("url", "")
            if url and "web.archive.org" not in url:
                wayback_url = _rewrite_to_wayback(url, config.wayback_ts)
                logger.info(
                    "[Retrodict] WebFetch URL rewritten to Wayback: %s -> %s",
                    url,
                    wayback_url,
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

        # Allow all other tools
        return allow()

    async def post_tool_use_hook(
        input_data: Any,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> dict[str, Any]:
        """Filter tool outputs to remove data after the cutoff."""
        if input_data.get("hook_event_name") != "PostToolUse":
            return {}

        tool_name = input_data.get("tool_name", "")
        # tool_response = input_data.get("tool_response")

        # get_cp_history: Filter points after cutoff
        if tool_name == "mcp__forecasting__get_cp_history":
            # The response contains history points with timestamps
            # We would filter them here, but for now just log
            logger.info(
                "[Retrodict] get_cp_history response should be filtered to %s",
                config.date_str,
            )
            # TODO: Implement actual filtering of response data
            pass

        return {}

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_use_hook])],  # type: ignore[list-item]
        "PostToolUse": [HookMatcher(hooks=[post_tool_use_hook])],  # type: ignore[list-item]
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
