"""Retrodict mode hooks for time-restricted forecasting.

Retrodict mode restricts all tools to data available before a given date,
enabling calibration testing on resolved questions without "future leak"
(the agent finding out the answer by searching for news about the resolution).

The cutoff date is stored in a ContextVar (retrodict_cutoff) so that it
propagates automatically through asyncio.gather() to sub-forecasts.

Most tools read the ContextVar directly in their implementations. The hook
handles two responsibilities:
- Rewriting WebFetch URLs to Wayback Machine (built-in SDK tool, can't modify)
- Denying tools that have no retrodict support (WebSearch, live market prices,
  Playwright, search_news) — needed because bypassPermissions ignores allowed_tools
"""

import logging
import re
import socket
from datetime import date, datetime, timedelta
from typing import Any

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.agent.hooks import HooksConfig
from aib.retrodict_context import retrodict_cutoff
from aib.tools.wayback import (
    check_wayback_availability,
    rewrite_to_wayback,
)

logger = logging.getLogger(__name__)

# Track hook modifications so display code can show actual tool params
_modified_inputs: dict[str, dict[str, Any]] = {}


def get_modified_input(tool_use_id: str) -> dict[str, Any] | None:
    """Look up the post-hook input for a tool call, if modified by retrodict."""
    return _modified_inputs.get(tool_use_id)


# Tools explicitly denied in retrodict mode (no date filtering support).
# WebSearch is denied separately with a hint to use web_search instead.
_DENIED_TOOLS = frozenset(
    {
        "mcp__forecasting__search_news",
        "mcp__playwright__browser_navigate",
        "mcp__playwright__browser_snapshot",
        "mcp__playwright__browser_click",
        "mcp__playwright__browser_type",
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


def _cap_trends_timeframe(timeframe: str, cutoff_date: date) -> str:
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


def create_retrodict_hooks() -> HooksConfig:
    """Create hooks that restrict tool access to data before the retrodict cutoff.

    Reads the cutoff date from the retrodict_cutoff ContextVar at invocation time.
    If no cutoff is set, all tools pass through unmodified.

    Returns:
        HooksConfig for ClaudeAgentOptions with PreToolUse hook.
    """

    async def pre_tool_use_hook(
        input_data: Any,
        tool_use_id: str | None,
        _context: HookContext,
    ) -> dict[str, Any]:
        """Filter and modify tool inputs for time restriction."""
        if input_data.get("hook_event_name") != "PreToolUse":
            return {}

        cutoff = retrodict_cutoff.get()
        if cutoff is None:
            return {}

        wayback_ts = cutoff.strftime("%Y%m%d")

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
            """Return modified tool input and record for display."""
            if tool_use_id:
                _modified_inputs[tool_use_id] = new_input
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                    "updatedInput": new_input,
                }
            }

        def allow() -> dict[str, Any]:
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                }
            }

        # --- Deny tools with no retrodict support ---
        # bypassPermissions ignores allowed_tools, so we must deny explicitly

        if tool_name == "WebSearch":
            return deny("WebSearch is not available.")

        if tool_name in _DENIED_TOOLS:
            return deny(f"{tool_name} is not available.")

        # --- WebFetch: rewrite URL to Wayback Machine ---

        if tool_name == "WebFetch":
            url = tool_input.get("url", "")
            if url and "web.archive.org" not in url:
                availability = await check_wayback_availability(
                    url, wayback_ts, validate_before_cutoff=True
                )

                if availability is None:
                    logger.warning(
                        "[Retrodict] No valid Wayback snapshot for %s at %s",
                        url,
                        wayback_ts,
                    )
                    return deny("HTTP 404: URL not found or unavailable.")

                actual_ts = availability.get("timestamp", wayback_ts)
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

        # All other tools read retrodict_cutoff ContextVar internally
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
