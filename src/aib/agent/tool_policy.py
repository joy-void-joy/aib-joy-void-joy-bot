"""Unified tool availability policy for the forecasting agent.

Centralizes all tool availability decisions based on API keys, retrodict mode,
and other context. This replaces scattered conditional logic throughout core.py.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, cast

from claude_agent_sdk.types import (
    McpSdkServerConfig,
    McpServerConfig,
    McpStdioServerConfig,
)

from aib.retrodict_context import retrodict_cutoff
from aib.tools.arxiv_search import arxiv_server
from aib.tools.financial import financial_server
from aib.tools.forecasting import create_forecasting_server
from aib.tools.markets import create_markets_server
from aib.tools.notes import create_notes_server
from aib.tools.retrodict_search import create_retrodict_search_server
from aib.tools.trends import trends_server

if TYPE_CHECKING:
    from aib.config import Settings
    from aib.tools.sandbox import Sandbox

# --- Tool Sets ---

# Built-in SDK tools (always available)
BUILTIN_TOOLS: frozenset[str] = frozenset(
    {
        "WebSearch",
        "WebFetch",
        "Read",
        "Write",
        "Glob",
        "Grep",
        "Bash",
        "Task",
    }
)

# Metaculus tools (require METACULUS_TOKEN)
METACULUS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__forecasting__get_metaculus_questions",
        "mcp__forecasting__list_tournament_questions",
        "mcp__forecasting__search_metaculus",
        "mcp__forecasting__get_coherence_links",
        "mcp__forecasting__get_prediction_history",
        "mcp__forecasting__get_cp_history",
    }
)

# Wikipedia tool (no API key required)
WIKIPEDIA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__forecasting__wikipedia",
    }
)

# Exa search tools (require EXA_API_KEY)
EXA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__forecasting__search_exa",
    }
)

# AskNews tools (require ASKNEWS_CLIENT_ID and ASKNEWS_SECRET)
ASKNEWS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__forecasting__search_news",
    }
)

# FRED tools (require FRED_API_KEY)
FRED_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__financial__fred_series",
        "mcp__financial__fred_search",
    }
)

# Company financials tools (no API key required, uses yfinance)
COMPANY_FINANCIALS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__financial__company_financials",
    }
)

# Sandbox tools (always available when sandbox is running)
SANDBOX_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__sandbox__execute_code",
        "mcp__sandbox__install_package",
    }
)

# Composition tools
COMPOSITION_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__composition__spawn_subquestions",
    }
)

# Market tools - live prices
LIVE_MARKET_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__markets__polymarket_price",
        "mcp__markets__manifold_price",
        "mcp__markets__stock_price",
    }
)

# Market tools - historical data
HISTORICAL_MARKET_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__markets__polymarket_history",
        "mcp__markets__manifold_history",
        "mcp__markets__stock_history",
    }
)

# Google Trends tools (no API key required)
TRENDS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__trends__google_trends",
        "mcp__trends__google_trends_compare",
        "mcp__trends__google_trends_related",
    }
)

# Notes tools
NOTES_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__notes__notes",
    }
)

# Playwright browser tools (excluded in retrodict mode)
PLAYWRIGHT_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__playwright__browser_navigate",
        "mcp__playwright__browser_snapshot",
        "mcp__playwright__browser_click",
        "mcp__playwright__browser_type",
    }
)

# Search tools for retrodict mode (date-filtered via Exa)
RETRODICT_SEARCH_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__web_search",
    }
)

# arXiv tools (no API key required, supports date filtering)
ARXIV_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__arxiv__search_arxiv",
    }
)


@dataclass
class ToolPolicy:
    """Centralized policy for tool availability.

    Determines which tools are available based on:
    - API key availability (from settings)
    - Retrodict mode via retrodict_cutoff ContextVar
    - Forecast context (e.g., allow_spawn for subquestions)

    Example:
        policy = ToolPolicy.from_settings(settings)
        mcp_servers = policy.get_mcp_servers(sandbox, composition_server, session_id="41906_20260202")
        allowed_tools = policy.get_allowed_tools(allow_spawn=True)
    """

    # API keys (None means not available)
    metaculus_token: str | None = None
    exa_api_key: str | None = None
    asknews_client_id: str | None = None
    asknews_client_secret: str | None = None
    fred_api_key: str | None = None

    # Computed sets (populated by __post_init__)
    _excluded_tools: frozenset[str] = field(default_factory=frozenset, init=False)

    def __post_init__(self) -> None:
        """Compute excluded tools based on configuration."""
        excluded: set[str] = set()

        # API key-based exclusions
        if not self.metaculus_token:
            excluded.update(METACULUS_TOOLS)
        if not self.exa_api_key:
            excluded.update(EXA_TOOLS)
        if not self.asknews_client_id or not self.asknews_client_secret:
            excluded.update(ASKNEWS_TOOLS)
        if not self.fred_api_key:
            excluded.update(FRED_TOOLS)

        self._excluded_tools = frozenset(excluded)

    @classmethod
    def from_settings(cls, settings: Settings) -> ToolPolicy:
        """Create a ToolPolicy from application settings.

        Args:
            settings: Application settings with API keys.

        Returns:
            ToolPolicy configured based on settings.
        """
        return cls(
            metaculus_token=settings.metaculus_token,
            exa_api_key=settings.exa_api_key,
            asknews_client_id=settings.asknews_client_id,
            asknews_client_secret=settings.asknews_client_secret,
            fred_api_key=settings.fred_api_key,
        )

    @property
    def is_retrodict(self) -> bool:
        """Whether retrodict mode is active (reads ContextVar)."""
        return retrodict_cutoff.get() is not None

    def get_mcp_servers(
        self,
        sandbox: Sandbox,
        composition_server: McpSdkServerConfig,
        *,
        session_id: str | None = None,
    ) -> dict[str, McpServerConfig]:
        """Get MCP server configuration based on policy.

        Args:
            sandbox: The sandbox instance for code execution.
            composition_server: The composition MCP server for spawn_subquestions.
            session_id: Session ID for the notes tool. Format: "<post_id>_<timestamp>".
                Enables write_meta mode. If None, write_meta is disabled.

        Returns:
            Dict mapping server name to server config.
        """
        servers: dict[str, McpServerConfig] = {
            "forecasting": create_forecasting_server(),
            "financial": financial_server,
            "sandbox": sandbox.create_mcp_server(),
            "composition": composition_server,
            "markets": create_markets_server(),
            "notes": create_notes_server(
                session_id,
                notes_base=(
                    Path(f"./tmp/notes/{session_id}")
                    if self.is_retrodict and session_id
                    else None
                ),
            ),
            "trends": trends_server,
            "arxiv": arxiv_server,
        }

        # Add search server in retrodict mode (date-filtered web search)
        if self.is_retrodict:
            servers["search"] = create_retrodict_search_server()

        # Only add Playwright in non-retrodict mode
        if not self.is_retrodict:
            servers["playwright"] = McpStdioServerConfig(
                type="stdio",
                command="bun",
                args=["x", "@anthropic-ai/mcp-server-playwright"],
            )

        return cast(dict[str, McpServerConfig], servers)

    def get_allowed_tools(self, *, allow_spawn: bool = True) -> list[str]:
        """Get list of allowed tools based on policy.

        Args:
            allow_spawn: Whether to allow spawn_subquestions (False for sub-forecasts).

        Returns:
            List of tool names that are allowed for this forecast.
        """
        # Start with all potential tools
        tools: set[str] = set()

        # Built-in tools
        tools.update(BUILTIN_TOOLS)

        # Metaculus tools (conditional on token)
        tools.update(METACULUS_TOOLS)

        # Wikipedia (no API key needed)
        tools.update(WIKIPEDIA_TOOLS)

        # Search tools (conditional on API keys)
        tools.update(EXA_TOOLS)
        tools.update(ASKNEWS_TOOLS)

        # Financial tools (conditional on API key)
        tools.update(FRED_TOOLS)
        tools.update(COMPANY_FINANCIALS_TOOLS)

        # Sandbox tools
        tools.update(SANDBOX_TOOLS)

        # Composition tools (conditional on allow_spawn)
        if allow_spawn:
            tools.update(COMPOSITION_TOOLS)

        # Market tools
        tools.update(LIVE_MARKET_TOOLS)
        tools.update(HISTORICAL_MARKET_TOOLS)

        # Trends tools
        tools.update(TRENDS_TOOLS)

        # Notes tools
        tools.update(NOTES_TOOLS)

        # arXiv tools (supports date filtering)
        tools.update(ARXIV_TOOLS)

        # Playwright tools
        tools.update(PLAYWRIGHT_TOOLS)

        # Retrodict search tools (date-filtered web search)
        if self.is_retrodict:
            tools.update(RETRODICT_SEARCH_TOOLS)

        # Remove excluded tools
        tools -= self._excluded_tools

        # Also remove spawn if not allowed (in case it was in _excluded_tools)
        if not allow_spawn:
            tools -= COMPOSITION_TOOLS

        return sorted(tools)

    def is_tool_available(self, tool_name: str) -> bool:
        """Check if a specific tool is available under this policy.

        Args:
            tool_name: Name of the tool to check.

        Returns:
            True if the tool is available, False otherwise.
        """
        return tool_name not in self._excluded_tools

    def get_tool_docs(
        self,
        mcp_servers: dict[str, McpServerConfig],
        *,
        allow_spawn: bool = True,
    ) -> str:
        """Generate tool documentation for allowed tools.

        Extracts tool descriptions from MCP server instances.

        Args:
            mcp_servers: Dict of MCP servers from get_mcp_servers().
            allow_spawn: Whether to include spawn_subquestions.

        Returns:
            Markdown-formatted tool documentation.
        """
        allowed = set(self.get_allowed_tools(allow_spawn=allow_spawn))
        descriptions: dict[str, str] = {}

        # Extract descriptions from SDK servers (which have _tools attribute)
        for server_name, server_config in mcp_servers.items():
            # Check if this is an SDK server with an instance
            server_type = (
                server_config.get("type")
                if isinstance(server_config, dict)
                else getattr(server_config, "type", None)
            )
            if server_type != "sdk":
                continue

            instance = (
                server_config.get("instance")
                if isinstance(server_config, dict)
                else getattr(server_config, "instance", None)
            )
            if instance is None:
                continue

            # Access stored tools from the server instance
            tools = getattr(instance, "_tools", [])
            for tool in tools:
                full_name = f"mcp__{server_name}__{tool.name}"
                if full_name in allowed:
                    descriptions[full_name] = tool.description

        return self._format_tool_docs(descriptions)

    def _format_tool_docs(self, descriptions: dict[str, str]) -> str:
        """Format tool descriptions as markdown documentation."""
        # Group by server
        by_server: dict[str, list[tuple[str, str]]] = {}
        for full_name, desc in descriptions.items():
            parts = full_name.split("__")
            if len(parts) >= 3:
                server = parts[1]
                tool_name = parts[2]
            else:
                server = "other"
                tool_name = full_name
            by_server.setdefault(server, []).append((tool_name, desc))

        # Format as markdown
        lines = ["## Available Tools\n"]
        for server, tools in sorted(by_server.items()):
            lines.append(f"### {server.title()}\n")
            for tool_name, desc in sorted(tools):
                lines.append(f"- **{tool_name}**: {desc}")
            lines.append("")

        return "\n".join(lines)
