"""Unified tool availability policy for the forecasting agent.

Centralizes all tool availability decisions based on API keys, retrodict mode,
and other context. This replaces scattered conditional logic throughout core.py.
"""

from __future__ import annotations

from collections.abc import Callable
from pathlib import Path
from typing import TYPE_CHECKING, Any

from lup.mcp import LupMcpTool, McpServerEntry, create_mcp_server
from lup.tool_policy import BaseToolPolicy
from pydantic import BaseModel

from aib.config import ResearchTopology
from aib.retrodict_context import retrodict_cutoff
from aib.tools.premortem import create_premortem_server
from aib.tools.reflection import create_reflection_server

if TYPE_CHECKING:
    from aib.agent.session import ReviewState
    from aib.config import Settings
    from aib.tools.sandbox import Sandbox

# --- Tool Sets ---

# Built-in SDK tools the agent is allowed to use, and the set every session
# opened here has its built-in half derived against. Bash is excluded — code
# runs only in the Docker-isolated mcp__sandbox__execute_code, never the host
# shell. WebSearch and WebFetch are excluded too: `search` and `fetch`
# supersede them with API augmentation, and the pair's one remaining
# distinction is that they do not honour `retrodict_cutoff` — which makes a
# granted-but-unused tool a standing way to leak. No lane reaches past this
# set either, so the exclusion is the whole answer rather than half of one.
# ToolSearch loads deferred MCP tool schemas.
BUILTIN_TOOLS: frozenset[str] = frozenset(
    {
        "Read",
        "Write",
        "Glob",
        "Grep",
        "Task",
        "ToolSearch",
        "StructuredOutput",
    }
)

# The condensed data surface. Each of these fans out over the narrow tools
# that used to be registered one by one: `search` over sixteen sources,
# `series` over three statistical publishers, `stock` over four ticker
# facets, `market` and `metaculus` over their drill-downs. The narrow tools
# are still there and still called — they are simply no longer the surface.
DATA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__search",
        "mcp__search__fetch",
        "mcp__financial__series",
        "mcp__financial__stock",
        "mcp__financial__stock_conditional_returns",
        "mcp__government__census",
        "mcp__markets__market",
        "mcp__markets__metaculus",
        "mcp__trends__trends",
        "mcp__weather__weather",
    }
)

# What the forecaster keeps in either topology: retrieval it can reach for
# without opening a sub-agent, and the question record it is forecasting.
CORE_DATA_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__search__search",
        "mcp__search__fetch",
        "mcp__markets__metaculus",
    }
)

# Metaculus question drill-down (requires METACULUS_TOKEN)
METACULUS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__markets__metaculus",
    }
)

# Census data (requires CENSUS_API_KEY)
CENSUS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__government__census",
    }
)

# Weather (no API key required, uses Open-Meteo)
WEATHER_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__weather__weather",
    }
)

# Sandbox tools (always available when sandbox is running)
SANDBOX_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__sandbox__execute_code",
        "mcp__sandbox__install_package",
    }
)

# Subforecast tools
SUBFORECAST_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__subforecast__subforecast",
        "mcp__subforecast__extract_cdf_threshold",
    }
)

# Research tool (sub-agent for delegated data gathering)
RESEARCH_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__research__research",
    }
)

# AskNews, served over HTTP and so unenumerable. A lane inside `search` for
# the two condensed topologies; four tools of its own under `direct`, which
# is the only place this has to be named.
# lup: ignore[frozenset-shape] — a fixed tool group, like the others here
ASKNEWS_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__asknews__search_news",
        "mcp__asknews__search_google",
        "mcp__asknews__search_x_twitter",
        "mcp__asknews__do_news_research",
    }
)

# The narrow sources a credential governs where `direct` mounts them one at
# a time. Under the condensed topologies each of these is a lane rather than
# a tool, so none of these names is in `DATA_TOOLS` and excluding them there
# subtracts nothing.
# lup: ignore[frozenset-shape] — a fixed tool group, like the others here
EXA_TOOLS: frozenset[str] = frozenset({"mcp__search__search_exa"})

# lup: ignore[frozenset-shape] — a fixed tool group, like the others here
FRED_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__financial__fred_series",
        "mcp__financial__fred_search",
    }
)

# lup: ignore[frozenset-shape] — a fixed tool group, like the others here
REDDIT_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__reddit__reddit_search",
        "mcp__reddit__reddit_hot",
    }
)

# Notes tools
NOTES_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__notes__reflection",
    }
)

# Premortem tool (Opus reviewer with adversarial input)
PREMORTEM_TOOLS: frozenset[str] = frozenset(
    {
        "mcp__premortem__premortem",
    }
)


def data_tool_groups() -> dict[str, list[LupMcpTool]]:
    """The condensed data surface, grouped by the server that serves it.

    One declaration, because everything that reaches these tools reads it:
    the forecaster mounts it, `research()` is handed it, the resolver builds
    its servers from it, and `lup-devtools agent serve-tools` offers it to an
    interactive session. A second list would let one of those drift onto a
    surface the allowlist no longer grants, and a tool served but not granted
    is refused at the moment it is called — which reads to the agent as the
    tool being broken rather than as it being ungranted.
    """
    from aib.tools.financial import series, stock, stock_conditional_returns
    from aib.tools.government import census
    from aib.tools.markets import market, metaculus
    from aib.tools.search import fetch, search
    from aib.tools.trends import trends
    from aib.tools.weather import weather

    return {
        "search": [search, fetch],
        "financial": [series, stock, stock_conditional_returns],
        "government": [census],
        "markets": [market, metaculus],
        "trends": [trends],
        "weather": [weather],
    }


class Credentialed(BaseModel):
    """One tool group and the credential it cannot run without."""

    tools: frozenset[str]  # lup: ignore[frozenset-shape] — a fixed tool group
    configured: bool
    credential: str


class ToolPolicy(BaseToolPolicy):
    """Centralized policy for tool availability.

    Determines which tools are available based on:
    - API key availability (from settings)
    - Retrodict mode via retrodict_cutoff ContextVar
    - Forecast context (e.g., allow_spawn for subquestions)

    The exclusion machinery is lup's (:class:`BaseToolPolicy`): this decides
    *what* is excluded and why, and the base owns *how* an exclusion applies.
    Each entry carries its reason, so `exclusion_reason` can answer why a
    tool is unavailable rather than only that it is.

    The server builders and the orchestrator allowlist stay this project's
    own: `orchestrator_servers` needs a session's directory, callbacks and
    review state, and the allowlist is a deliberate split — the orchestrator
    sees ~10 tools and delegates the other ~35 to the research sub-agent.
    Neither is the shape the base's `get_mcp_servers` / `get_allowed_tools`
    describe, so they are named for what they build rather than shadowing
    those with an incompatible signature.

    Example:
        policy = ToolPolicy.from_settings(settings)
        servers = policy.orchestrator_servers(sandbox, session_dir=session)
        allowed = policy.orchestrator_allowlist(allow_spawn=True)
    """

    def __init__(
        self,
        metaculus_token: str | None = None,
        exa_api_key: str | None = None,
        asknews_api_key: str | None = None,
        fred_api_key: str | None = None,
        reddit_client_id: str | None = None,
        reddit_client_secret: str | None = None,
        census_api_key: str | None = None,
        research: ResearchTopology = "condensed",
    ) -> None:
        self.research: ResearchTopology = research
        self.metaculus_token = metaculus_token
        self.exa_api_key = exa_api_key
        self.asknews_api_key = asknews_api_key
        self.fred_api_key = fred_api_key
        self.reddit_client_id = reddit_client_id
        self.reddit_client_secret = reddit_client_secret
        self.census_api_key = census_api_key

        # A credential governs a whole tool only where that tool is one
        # source. Exa, AskNews, Reddit and FRED are each one lane of nine
        # inside `search` or one publisher of three inside `series`, so
        # nothing here withholds those: `available_lanes` drops the lane, and
        # `series` says which publisher it could not reach.
        #
        # The narrow names are still listed, because `direct` mounts those
        # sources as tools of their own. Under the condensed topologies each
        # entry is a no-op — no narrow name is in `DATA_TOOLS` to subtract —
        # and under `direct` it is the only thing that can gate them: the
        # module-level tool lists read the process settings, so a policy
        # built with a key argument of its own would not otherwise be obeyed.
        requirements = [
            Credentialed(
                tools=ASKNEWS_TOOLS,
                configured=bool(asknews_api_key),
                credential="ASKNEWS_API_KEY",
            ),
            Credentialed(
                tools=EXA_TOOLS,
                configured=bool(exa_api_key),
                credential="EXA_API_KEY",
            ),
            Credentialed(
                tools=FRED_TOOLS,
                configured=bool(fred_api_key),
                credential="FRED_API_KEY",
            ),
            Credentialed(
                tools=REDDIT_TOOLS,
                configured=bool(reddit_client_id and reddit_client_secret),
                credential="REDDIT_CLIENT_ID + REDDIT_CLIENT_SECRET",
            ),
            Credentialed(
                tools=METACULUS_TOOLS,
                configured=bool(metaculus_token),
                credential="METACULUS_TOKEN",
            ),
            Credentialed(
                tools=CENSUS_TOOLS,
                configured=bool(census_api_key),
                credential="CENSUS_API_KEY",
            ),
        ]

        reasons = {
            tool: f"{requirement.credential} is not configured"
            for requirement in requirements
            if not requirement.configured
            for tool in requirement.tools
        }

        # Retrodict exclusions, which win where they overlap a missing
        # credential: a forecast for a past date cannot ask for a forecast of
        # the weather now, and AskNews carries no publication date this could
        # filter on.
        if self.is_retrodict:
            reasons |= {
                tool: "retrodict mode: this source ignores the cutoff"
                for tools in (WEATHER_TOOLS, ASKNEWS_TOOLS)
                for tool in tools
            }

        super().__init__(excluded_tools=reasons)

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
            research=settings.research,
        )

    @property
    def is_retrodict(self) -> bool:
        """Whether retrodict mode is active (reads ContextVar)."""
        return retrodict_cutoff.get() is not None

    def orchestrator_servers(
        self,
        sandbox: Sandbox,
        *,
        session_dir: Path | None = None,
        question_type: str = "binary",
        get_sources: Callable[[], list[str]] | None = None,
        get_trace: Callable[[], str] | None = None,
        question_context: dict[str, Any] | None = None,
        traces_dir: Path | None = None,
        review_state: ReviewState | None = None,
    ) -> dict[str, McpServerEntry]:
        """Get MCP server configuration based on policy.

        Args:
            sandbox: The sandbox instance for code execution.
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
        from aib.tools.markets import metaculus
        from aib.tools.research import research
        from aib.tools.search import fetch, search
        from aib.tools.subforecast import extract_cdf_threshold_tool, subforecast

        # What the forecaster holds whatever the topology: the sandbox it
        # computes in, the instruments it forecasts with, and the notes it
        # keeps.
        servers: dict[str, McpServerEntry] = {
            "sandbox": sandbox.create_mcp_server(),
            "subforecast": create_mcp_server(
                "subforecast", tools=[subforecast, extract_cdf_threshold_tool]
            ),
            "notes": create_reflection_server(
                session_dir,
                question_type,
                get_sources,
                review_state=review_state,
            ),
            "premortem": create_premortem_server(
                session_dir=session_dir,
                get_trace=get_trace,
                question_context=question_context,
                traces_dir=traces_dir,
                review_state=review_state,
            ),
        }

        if self.research == "delegated":
            # research() opens a sub-agent holding the whole data surface and
            # answers with a digest, so the forecaster keeps only what it
            # needs to check one fact for itself and to read its own question.
            servers["research"] = create_mcp_server("research", tools=[research])
            servers["search"] = create_mcp_server("search", tools=[search, fetch])
            servers["markets"] = create_mcp_server("markets", tools=[metaculus])
            return servers

        if self.research == "direct":
            servers.update(self.narrow_servers())
            return servers

        servers.update(self.data_servers())
        return servers

    def narrow_servers(self) -> dict[str, McpServerEntry]:
        """The forty tools the condensed sixteen were drawn out of.

        Reached only by `direct`, which is the surface this project ran
        before them. They are the same functions every condensed tool calls,
        so this mounts nothing that was resurrected — it hands the agent one
        at a time what `search` and the rest now ask for it.

        Each group carries its own credential conditional, so a session
        without a key is served what it can answer rather than granted what
        it cannot: the reason those lists live beside their tools.
        """
        from aib.tools.financial import FINANCIAL_TOOLS
        from aib.tools.government import bls_series, census
        from aib.tools.markets import (
            METACULUS_QUESTION_TOOLS,
            PREDICTION_MARKET_TOOLS,
        )
        from aib.tools.reddit import reddit_hot, reddit_search
        from aib.tools.search import BASE_SEARCH_TOOLS, OPTIONAL_SEARCH_TOOLS
        from aib.tools.trends import google_trends, google_trends_compare
        from aib.tools.wayback import wayback_snapshot
        from aib.tools.weather import weather

        groups: dict[str, list[LupMcpTool]] = {
            "search": [*BASE_SEARCH_TOOLS, *OPTIONAL_SEARCH_TOOLS],
            "financial": FINANCIAL_TOOLS,
            "government": [bls_series, census],
            "markets": [*PREDICTION_MARKET_TOOLS, *METACULUS_QUESTION_TOOLS],
            "trends": [google_trends, google_trends_compare],
            "wayback": [wayback_snapshot],
        }

        if not self.is_retrodict:
            groups["weather"] = [weather]
            if self.reddit_client_id and self.reddit_client_secret:
                groups["reddit"] = [reddit_search, reddit_hot]

        servers: dict[str, McpServerEntry] = {
            name: create_mcp_server(name, tools=tools) for name, tools in groups.items()
        }

        if self.asknews_api_key and not self.is_retrodict:
            from aib.tools.asknews import create_asknews_server

            servers["asknews"] = create_asknews_server(self.asknews_api_key)

        return servers

    def data_servers(
        self,
        sandbox: Sandbox | None = None,
    ) -> dict[str, McpServerEntry]:
        """The condensed data surface: ten tools over forty-odd sources.

        Mounted on the forecaster under `condensed`, and handed to the
        research sub-agent under `delegated`. The same surface either way,
        so re-plugging research() cannot resurrect an older one — which is
        what a second list of what the servers hold would eventually do.

        A sandbox server for data analysis is included only when a sandbox
        is passed, since the sub-agent is given one and the forecaster
        already mounts its own. Weather is withheld from a backtest, which
        cannot ask what the weather will be.
        """
        servers: dict[str, McpServerEntry] = {
            name: create_mcp_server(name, tools=tools)
            for name, tools in data_tool_groups().items()
            if not (name == "weather" and self.is_retrodict)
        }

        if sandbox is not None:
            servers["sandbox"] = sandbox.create_mcp_server()

        return servers

    def narrow_allowlist(
        self,
        mounted: dict[str, McpServerEntry] | None = None,
    ) -> list[str]:
        """Every narrow tool a `direct` session is served, from its servers.

        Derived rather than listed. A tool registered and left out of the
        roster is refused by the allowlist hook at the moment it is called,
        which reads to the agent as the tool being broken rather than as it
        being ungranted — so it retries, works around it, and reports a
        capability gap that is really a bookkeeping one.

        AskNews is the exception the derivation cannot cover: an external
        MCP server cannot be enumerated without connecting to it, so
        `server_tool_names` answers `[]` for one and its four tools are
        named. Naming them costs nothing when its server is absent, since
        the same condition that leaves it unregistered leaves the tools
        uncalled.
        """
        servers = dict(mounted) if mounted is not None else self.narrow_servers()
        return self.get_allowed_tools(servers, builtin_tools=ASKNEWS_TOOLS)

    def orchestrator_allowlist(
        self,
        *,
        allow_spawn: bool = True,
        mounted: dict[str, McpServerEntry] | None = None,
    ) -> list[str]:
        """Get list of allowed tools based on policy.

        Args:
            allow_spawn: Whether to allow subforecast (False for leaf sub-forecasts).
            mounted: The servers this session actually carries, which under
                `direct` is what the roster is read off. The condensed
                surface is small enough to declare, so both other topologies
                name it; forty tools are not, and a second statement of what
                forty servers hold is a thing that drifts.

        Returns:
            List of tool names that are allowed for this forecast.
        """
        # The whole surface, because the whole surface now fits. `delegated`
        # is the narrower case rather than the wider one: the data tools move
        # behind research(), and the forecaster keeps the retrieval pair and
        # its own question record.
        # lup: ignore[set-shape] — an accumulating roster of tool names
        tools: set[str] = set()

        tools.update(BUILTIN_TOOLS)
        tools.update(SANDBOX_TOOLS)
        tools.update(NOTES_TOOLS)
        tools.update(PREMORTEM_TOOLS)

        if self.research == "delegated":
            tools.update(RESEARCH_TOOLS)
            tools.update(CORE_DATA_TOOLS)
        elif self.research == "direct":
            tools.update(self.narrow_allowlist(mounted))
        else:
            tools.update(DATA_TOOLS)

        if allow_spawn:
            tools.update(SUBFORECAST_TOOLS)

        # Remove excluded tools (API key gating), which the base holds
        tools -= self.excluded_tools.keys()

        return sorted(tools)

    def get_tool_docs(
        self,
        mcp_servers: dict[str, McpServerEntry],
        *,
        allow_spawn: bool = True,
    ) -> str:
        """Generate tool documentation for allowed tools.

        Extracts tool descriptions from MCP server instances.

        Args:
            mcp_servers: Dict of MCP servers from get_mcp_servers().
            allow_spawn: Whether to include subforecast.

        Returns:
            Markdown-formatted tool documentation.
        """
        # lup: ignore[set-shape] — membership test over the allowlist
        allowed = set(self.orchestrator_allowlist(allow_spawn=allow_spawn))
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
            server = parts[1] if len(parts) >= 3 else "other"
            by_server.setdefault(server, []).append((full_name, desc))

        # Format as markdown
        lines = [
            "## Available Tools\n",
            "Call each tool by the exact name shown in bold (e.g. "
            "`mcp__research__research`) — not a shortened form like `research`.\n",
        ]
        for server, tools in sorted(by_server.items()):
            lines.append(f"### {server.title()}\n")
            for full_name, desc in sorted(tools):
                lines.append(f"- **{full_name}**: {desc}")
            lines.append("")

        return "\n".join(lines)
