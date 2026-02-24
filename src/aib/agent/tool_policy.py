"""Unified tool availability policy for the forecasting agent.

Centralizes all tool availability decisions based on API keys, retrodict mode,
and other context. This replaces scattered conditional logic throughout core.py.
"""

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any, cast

from claude_agent_sdk.types import (
    McpHttpServerConfig,
    McpSdkServerConfig,
    McpServerConfig,
)

from aib.retrodict_context import retrodict_cutoff
from aib.tools.financial import create_financial_server
from aib.tools.government import create_government_server
from aib.tools.markets import create_markets_server
from aib.tools.reddit import create_reddit_server
from aib.tools.search import create_search_server
from aib.tools.trends import create_trends_server
from aib.tools.reflection import create_reflection_server

if TYPE_CHECKING:
    from aib.config import Settings
    from aib.tools.reflection import ReviewState
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
        "mcp__markets__get_metaculus_questions",
        "mcp__markets__list_tournament_questions",
        "mcp__markets__search_metaculus",
        "mcp__markets__get_coherence_links",
        "mcp__markets__get_cp_history",
    }
)

# Wikipedia tool (no API key required)
WIKIPEDIA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__wikipedia",
    }
)

# Exa search tools (require EXA_API_KEY)
EXA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__search_exa",
    }
)

# AskNews tools (require ASKNEWS_API_KEY, served by remote MCP server)
ASKNEWS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__asknews__search_news",
        "mcp__asknews__search_google",
        "mcp__asknews__search_x_twitter",
        "mcp__asknews__do_news_research",
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
        "mcp__markets__kalshi_price",
        "mcp__markets__kalshi_event",
    }
)

# Market tools - historical data
HISTORICAL_MARKET_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__markets__polymarket_history",
        "mcp__markets__manifold_history",
        "mcp__markets__kalshi_history",
    }
)

# Stock tools (now in financial server)
STOCK_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__financial__stock_price",
        "mcp__financial__stock_history",
    }
)

# Google Trends tools (no API key required)
TRENDS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__trends__google_trends",
        "mcp__trends__google_trends_compare",
    }
)

# Notes tools
NOTES_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__notes__reflection",
    }
)

# Fetch tool (now in search server)
FETCH_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__fetch_url",
    }
)

# Web search tools (Haiku sub-agent with WebSearch + API augmentation)
SEARCH_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__web_search",
    }
)

# arXiv tools (no API key required, supports date filtering)
ARXIV_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__search_arxiv",
        "mcp__search__fetch_arxiv",
    }
)

# World Bank tools (now in financial server)
WORLD_BANK_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__financial__world_bank_indicator",
        "mcp__financial__world_bank_search",
    }
)

# Reddit tools (require REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET)
REDDIT_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__reddit__reddit_search",
        "mcp__reddit__reddit_hot",
    }
)

# BLS tools (optional BLS_API_KEY, always registered)
BLS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__government__bls_series",
    }
)

# Census tools (require CENSUS_API_KEY)
CENSUS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__government__census_data",
    }
)


_STATIC_TOOL_DOCS: dict[str, str] = {
    "mcp__asknews__search_news": (
        "Search 50k+ global news sources for breaking and recent news. "
        "Covers the last 48-72 hours. Use when recency matters."
    ),
    "mcp__asknews__search_google": (
        "Google search via AskNews. Complement to web_search for different result coverage."
    ),
    "mcp__asknews__search_x_twitter": (
        "Search X/Twitter for real-time public sentiment, expert opinions, "
        "and breaking developments."
    ),
    "mcp__asknews__do_news_research": (
        "Deep, multi-step news research on a topic. Synthesizes across many "
        "sources for complex questions requiring extensive news coverage."
    ),
}


@dataclass
class ToolPolicy:
    """Centralized policy for tool availability.

    Determines which tools are available based on:
    - API key availability (from settings)
    - Retrodict mode via retrodict_cutoff ContextVar
    - Forecast context (e.g., allow_spawn for subquestions)

    Example:
        policy = ToolPolicy.from_settings(settings)
        mcp_servers = policy.get_mcp_servers(sandbox, composition_server, session_dir=Path("notes/traces/1.2.1/sessions/41906/20260202"))
        allowed_tools = policy.get_allowed_tools(allow_spawn=True)
    """

    # API keys (None means not available)
    metaculus_token: str | None = None
    exa_api_key: str | None = None
    asknews_api_key: str | None = None
    fred_api_key: str | None = None
    reddit_client_id: str | None = None
    reddit_client_secret: str | None = None
    census_api_key: str | None = None

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
        if not self.asknews_api_key:
            excluded.update(ASKNEWS_TOOLS)
        if not self.fred_api_key:
            excluded.update(FRED_TOOLS)
        if not self.reddit_client_id or not self.reddit_client_secret:
            excluded.update(REDDIT_TOOLS)
        if not self.census_api_key:
            excluded.update(CENSUS_TOOLS)

        # Retrodict exclusions (tools with no date filtering)
        if self.is_retrodict:
            excluded.update(ASKNEWS_TOOLS)
            excluded.update(REDDIT_TOOLS)

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
            asknews_api_key=settings.asknews_api_key,
            fred_api_key=settings.fred_api_key,
            reddit_client_id=settings.reddit_client_id,
            reddit_client_secret=settings.reddit_client_secret,
            census_api_key=settings.census_api_key,
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
        session_dir: Path | None = None,
        question_type: str = "binary",
        get_sources: Callable[[], list[str]] | None = None,
        get_trace: Callable[[], str] | None = None,
        question_context: dict[str, Any] | None = None,
        traces_dir: Path | None = None,
        review_state: ReviewState | None = None,
    ) -> dict[str, McpServerConfig]:
        """Get MCP server configuration based on policy.

        Args:
            sandbox: The sandbox instance for code execution.
            composition_server: The composition MCP server for spawn_subquestions.
            session_dir: Session directory path for the reflection tool.
                If None, reflection is disabled.
            question_type: Question type for the reflection tool.
            get_sources: Callback returning sources consulted so far.
                Passed to the reflection tool for mid-session source output.
            get_trace: Callback returning the full reasoning trace as markdown.
                Passed to the reviewer sub-agent for context.
            question_context: Question details (title, type, resolution criteria).
                Passed to the reviewer for informed critique.
            traces_dir: Directory with past forecast data for the reviewer.
                The reviewer gets read access to browse historical performance.
            review_state: Shared reviewer state for gate coordination
                between the reflection tool and the StructuredOutput hook.

        Returns:
            Dict mapping server name to server config.
        """
        servers: dict[str, McpServerConfig] = {
            "financial": create_financial_server(),
            "government": create_government_server(),
            "sandbox": sandbox.create_mcp_server(),
            "composition": composition_server,
            "markets": create_markets_server(),
            "notes": create_reflection_server(
                session_dir,
                question_type,
                get_sources,
                get_trace=get_trace,
                question_context=question_context,
                traces_dir=traces_dir,
                review_state=review_state,
            ),
            "trends": create_trends_server(),
            "search": create_search_server(),
        }

        # Reddit MCP server (excluded in retrodict — no exact date cutoff)
        if (
            self.reddit_client_id
            and self.reddit_client_secret
            and not self.is_retrodict
        ):
            servers["reddit"] = create_reddit_server()

        # AskNews remote MCP server (excluded in retrodict — no date filtering)
        if self.asknews_api_key and not self.is_retrodict:
            servers["asknews"] = McpHttpServerConfig(
                type="http",
                url="https://mcp.asknews.app",
                headers={"Authorization": f"Bearer {self.asknews_api_key}"},
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

        # Stock tools (in financial server)
        tools.update(STOCK_TOOLS)

        # Trends tools
        tools.update(TRENDS_TOOLS)

        # Notes tools
        tools.update(NOTES_TOOLS)

        # arXiv tools (supports date filtering)
        tools.update(ARXIV_TOOLS)

        # World Bank tools (no API key required)
        tools.update(WORLD_BANK_TOOLS)

        # Reddit tools (conditional on API keys)
        tools.update(REDDIT_TOOLS)

        # Government data tools
        tools.update(BLS_TOOLS)
        tools.update(CENSUS_TOOLS)

        # Fetch tool (unified URL fetching)
        tools.update(FETCH_TOOLS)

        # Web search tools
        tools.update(SEARCH_TOOLS)

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

        server_names = set(mcp_servers.keys())
        for full_name, desc in _STATIC_TOOL_DOCS.items():
            if full_name in allowed:
                parts = full_name.split("__")
                if len(parts) >= 3 and parts[1] in server_names:
                    descriptions[full_name] = desc

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
