"""Tests for ToolPolicy class."""

from datetime import date
from unittest.mock import MagicMock

from lup.mcp import McpServerEntry, server_tool_names

from aib.retrodict_context import retrodict_cutoff
from aib.agent.tool_policy import (
    ASKNEWS_TOOLS,
    BUILTIN_TOOLS,
    HISTORICAL_MARKET_TOOLS,
    LIVE_MARKET_TOOLS,
    METACULUS_TOOLS,
    NOTES_TOOLS,
    RESEARCH_TOOLS,
    SANDBOX_TOOLS,
    TRENDS_TOOLS,
    ToolPolicy,
)


class TestToolPolicyToolSets:
    """Tests for tool set constants."""

    def test_builtin_tools_present(self) -> None:
        """Built-in tools should be defined (Bash excluded; web tools retrodict-gated)."""
        assert "Bash" not in BUILTIN_TOOLS
        assert "Task" in BUILTIN_TOOLS
        assert "ToolSearch" in BUILTIN_TOOLS
        assert "WebSearch" in BUILTIN_TOOLS
        assert "WebFetch" in BUILTIN_TOOLS

    def test_metaculus_tools_require_token(self) -> None:
        """Metaculus tools should all have metaculus prefix."""
        for tool in METACULUS_TOOLS:
            assert tool.startswith("mcp__metaculus__")

    def test_asknews_tools_use_asknews_prefix(self) -> None:
        """AskNews tools should all have mcp__asknews__ prefix."""
        assert len(ASKNEWS_TOOLS) == 4
        for tool_name in ASKNEWS_TOOLS:
            assert tool_name.startswith("mcp__asknews__")

    def test_live_market_tools_separate_from_historical(self) -> None:
        """Live and historical market tools should be disjoint."""
        assert LIVE_MARKET_TOOLS.isdisjoint(HISTORICAL_MARKET_TOOLS)


class TestToolPolicyConstruction:
    """Tests for ToolPolicy construction."""

    def test_from_settings_with_all_keys(self) -> None:
        """Should populate all fields from settings."""
        settings = MagicMock()
        settings.metaculus_token = "token"
        settings.exa_api_key = "exa"
        settings.asknews_api_key = "asknews_key"
        settings.fred_api_key = "fred"
        settings.reddit_client_id = None
        settings.reddit_client_secret = None
        settings.census_api_key = None

        policy = ToolPolicy.from_settings(settings)

        assert policy.metaculus_token == "token"
        assert policy.exa_api_key == "exa"
        assert policy.asknews_api_key == "asknews_key"
        assert policy.fred_api_key == "fred"
        assert not policy.is_retrodict

    def test_is_retrodict_reads_contextvar(self) -> None:
        """is_retrodict should read from retrodict_cutoff ContextVar."""
        policy = ToolPolicy()
        assert not policy.is_retrodict

        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            assert policy.is_retrodict
        finally:
            retrodict_cutoff.reset(token)


class TestToolPolicyOrchestrator:
    """Tests for the main agent's orchestrator tool surface."""

    def test_orchestrator_has_builtin_tools(self) -> None:
        """Main agent should have built-in SDK tools."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in BUILTIN_TOOLS:
            assert tool in allowed

    def test_orchestrator_has_metaculus_tools(self) -> None:
        """Main agent should have Metaculus tools when token is set."""
        policy = ToolPolicy(metaculus_token="test-token")
        allowed = policy.orchestrator_allowlist()
        for tool in METACULUS_TOOLS:
            assert tool in allowed

    def test_orchestrator_excludes_metaculus_without_token(self) -> None:
        """Main agent should exclude Metaculus tools without token."""
        policy = ToolPolicy(metaculus_token=None)
        allowed = policy.orchestrator_allowlist()
        for tool in METACULUS_TOOLS:
            assert tool not in allowed

    def test_orchestrator_has_research_tool(self) -> None:
        """Main agent should have the research tool."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in RESEARCH_TOOLS:
            assert tool in allowed

    def test_orchestrator_has_sandbox(self) -> None:
        """Main agent should have sandbox tools."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in SANDBOX_TOOLS:
            assert tool in allowed

    def test_orchestrator_has_notes(self) -> None:
        """Main agent should have notes/reflection tools."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in NOTES_TOOLS:
            assert tool in allowed

    def test_orchestrator_no_data_tools(self) -> None:
        """Main agent should NOT have data-gathering tools (those are on research sub-agent)."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        # Data tools should not be on the main agent
        for tool in LIVE_MARKET_TOOLS:
            assert tool not in allowed
        for tool in HISTORICAL_MARKET_TOOLS:
            assert tool not in allowed
        for tool in TRENDS_TOOLS:
            assert tool not in allowed


class TestToolPolicySpawn:
    """Tests for subforecast availability."""

    def test_subforecast_allowed_by_default(self) -> None:
        """subforecast should be allowed by default."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist(allow_spawn=True)
        assert "mcp__subforecast__subforecast" in allowed

    def test_subforecast_excluded_when_disabled(self) -> None:
        """subforecast should be excluded when allow_spawn=False."""
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist(allow_spawn=False)
        assert "mcp__subforecast__subforecast" not in allowed


class TestToolPolicyIsToolAvailable:
    """Tests for is_tool_available method (API key gating)."""

    def test_builtin_always_available(self) -> None:
        """Built-in tools should always be available."""
        policy = ToolPolicy()
        for tool in BUILTIN_TOOLS:
            assert policy.is_tool_available(tool)

    def test_excluded_tool_not_available(self) -> None:
        """Excluded tools should not be available."""
        policy = ToolPolicy(metaculus_token=None)
        for tool in METACULUS_TOOLS:
            assert not policy.is_tool_available(tool)

    def test_trends_always_available(self) -> None:
        """Trends tools should always be available (no API key required)."""
        policy = ToolPolicy()
        for tool in TRENDS_TOOLS:
            assert policy.is_tool_available(tool)


class TestToolPolicyMcpServers:
    """Tests for get_mcp_servers method (main agent)."""

    def test_includes_orchestrator_servers(self) -> None:
        """Should include orchestrator MCP servers."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.orchestrator_servers(sandbox)

        assert "sandbox" in servers
        assert "subforecast" in servers
        assert "research" in servers
        assert "search" in servers
        assert "metaculus" in servers
        assert "notes" in servers

    def test_excludes_data_servers(self) -> None:
        """Main agent should not have data-gathering servers."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.orchestrator_servers(sandbox)

        assert "financial" not in servers
        assert "government" not in servers
        assert "trends" not in servers
        assert "markets" not in servers


class TestToolPolicyResearchServers:
    """Tests for get_research_mcp_servers method."""

    def test_includes_data_servers(self) -> None:
        """Research sub-agent should have data-gathering servers."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.research_servers(sandbox)

        assert "financial" in servers
        assert "government" in servers
        assert "sandbox" in servers
        assert "markets" in servers
        assert "trends" in servers
        assert "search" in servers

    def test_includes_asknews_with_api_key(self) -> None:
        """Research sub-agent should have AskNews server when api_key is set."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy(asknews_api_key="test-key")
        servers = policy.research_servers(sandbox)

        assert "asknews" in servers


class TestToolPolicyToolDocs:
    """Tool docs must present the exact callable name (mcp__server__tool)."""

    def test_shows_full_callable_name_not_bare(self) -> None:
        policy = ToolPolicy()
        docs = policy._format_tool_docs(
            {"mcp__research__research": "Delegate data-gathering."}
        )
        assert "**mcp__research__research**" in docs
        assert "- **research**:" not in docs

    def test_includes_exact_name_instruction(self) -> None:
        policy = ToolPolicy()
        docs = policy._format_tool_docs({"mcp__search__web_search": "Search the web."})
        assert "exact name" in docs
        assert "mcp__research__research" in docs

    def test_excludes_asknews_without_api_key(self) -> None:
        """Research sub-agent should not have AskNews without api_key."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.research_servers(sandbox)

        assert "asknews" not in servers

    def test_excludes_asknews_in_retrodict(self) -> None:
        """Research sub-agent should not have AskNews in retrodict mode."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy(asknews_api_key="test-key")
            servers = policy.research_servers(sandbox)
            assert "asknews" not in servers
        finally:
            retrodict_cutoff.reset(token)


class TestAllowlistsMatchTheServersRegistered:
    """Each allowlist against the tools its own servers actually serve.

    Both lists were hand-kept unions of named constants, which is a second
    statement of what the servers already carry — and a second statement
    drifts. A tool added to a server and not to the union is registered and
    then refused by the allowlist hook, which reads to the agent as the tool
    being broken rather than as it being ungranted.

    The sandbox server is subtracted from both sides: it is built by a
    `Sandbox` instance a unit test has no reason to construct, so its two
    tools are the one part of the surface these compare nothing about.
    """

    def derived(
        self,
        servers: dict[str, McpServerEntry],
        policy: ToolPolicy,
        named: frozenset[str] = frozenset(),  # lup: ignore[frozenset-shape]
    ) -> set[str]:
        """What the tools on `servers` come to, minus the sandbox's.

        `named` is for tools no introspection can reach. An external MCP
        server — AskNews is served over HTTP — cannot be enumerated without
        connecting to it, so `server_tool_names` answers `[]` for one and
        its tools have to be named the way built-ins are.
        """
        names = set(
            policy.get_allowed_tools(servers, builtin_tools=BUILTIN_TOOLS | named)
        )
        return names - SANDBOX_TOOLS

    def test_the_orchestrator_allowlist_is_what_its_servers_serve(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()
        policy = ToolPolicy(metaculus_token="t")

        servers = policy.orchestrator_servers(sandbox)
        declared = set(policy.orchestrator_allowlist()) - SANDBOX_TOOLS

        assert self.derived(servers, policy) == declared

    def test_the_research_allowlist_refuses_nothing_its_servers_serve(self) -> None:
        """Every registered tool is granted, which is the failure that hurts.

        A tool the sub-agent is served but not granted is refused by the
        allowlist hook at the moment it is called, which reads to the agent
        as the tool being broken rather than as it being ungranted — so it
        retries, works around it, and reports a capability gap that is
        really a bookkeeping one.

        The derivation makes this true by construction, so what the test
        actually pins is that the call site hands over the servers it has:
        passing none is a legal call that answers with the built-ins alone,
        and that is exactly what the old drift looked like from here.
        """
        from aib.tools.research import get_research_allowed_tools

        policy = ToolPolicy(fred_api_key="f", exa_api_key="e")
        servers = policy.research_servers()
        granted = set(get_research_allowed_tools(servers))

        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }
        assert served
        assert served - policy.excluded_tools.keys() <= granted
