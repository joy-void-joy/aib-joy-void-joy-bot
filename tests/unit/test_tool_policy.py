"""Tests for ToolPolicy class."""

from datetime import date
from unittest.mock import MagicMock

import pytest
from lup.mcp import McpServerEntry, server_tool_names

from aib.retrodict_context import retrodict_cutoff
from aib.agent.tool_policy import (
    ASKNEWS_TOOLS,
    BUILTIN_TOOLS,
    CORE_DATA_TOOLS,
    DATA_TOOLS,
    METACULUS_TOOLS,
    NOTES_TOOLS,
    RESEARCH_TOOLS,
    SANDBOX_TOOLS,
    WEATHER_TOOLS,
    ToolPolicy,
)


class TestToolPolicyToolSets:
    """Tests for tool set constants."""

    def test_builtin_tools_present(self) -> None:
        """Built-in tools should be defined, with the shell excluded."""
        assert "Bash" not in BUILTIN_TOOLS
        assert "Task" in BUILTIN_TOOLS
        assert "ToolSearch" in BUILTIN_TOOLS

    def test_builtins_exclude_the_pair_that_ignores_the_cutoff(self) -> None:
        """`search` and `fetch` supersede WebSearch and WebFetch entirely.

        What was left of the pair once the condensed tools covered their
        work is that they do not honour `retrodict_cutoff` — so granting
        them leaves a way to leak and buys nothing.
        """
        assert "WebSearch" not in BUILTIN_TOOLS
        assert "WebFetch" not in BUILTIN_TOOLS

    def test_metaculus_tool_is_served_by_the_markets_server(self) -> None:
        for tool in METACULUS_TOOLS:
            assert tool.startswith("mcp__markets__")

    def test_core_data_tools_are_part_of_the_data_surface(self) -> None:
        """What `delegated` keeps is a subset of what `condensed` mounts."""
        assert CORE_DATA_TOOLS < DATA_TOOLS


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
        settings.research = "condensed"

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
    """Tests for the forecaster's tool surface."""

    def test_orchestrator_has_builtin_tools(self) -> None:
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in BUILTIN_TOOLS:
            assert tool in allowed

    def test_orchestrator_has_metaculus_tool_with_token(self) -> None:
        policy = ToolPolicy(metaculus_token="test-token")
        allowed = policy.orchestrator_allowlist()
        for tool in METACULUS_TOOLS:
            assert tool in allowed

    def test_orchestrator_excludes_metaculus_without_token(self) -> None:
        policy = ToolPolicy(metaculus_token=None)
        allowed = policy.orchestrator_allowlist()
        for tool in METACULUS_TOOLS:
            assert tool not in allowed

    def test_orchestrator_has_sandbox(self) -> None:
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in SANDBOX_TOOLS:
            assert tool in allowed

    def test_orchestrator_has_notes(self) -> None:
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist()
        for tool in NOTES_TOOLS:
            assert tool in allowed

    def test_orchestrator_holds_the_data_tools(self) -> None:
        """Ten condensed tools fit in the context forty narrow ones did not.

        This is the whole point of condensing them: the reasoning that uses
        an observation is in the same context that made it.
        """
        policy = ToolPolicy(metaculus_token="t", census_api_key="c")
        allowed = set(policy.orchestrator_allowlist())
        assert DATA_TOOLS <= allowed

    def test_orchestrator_does_not_hold_the_narrow_tools(self) -> None:
        """The narrow tools are still called — as lanes, not as the surface."""
        allowed = set(ToolPolicy(metaculus_token="t").orchestrator_allowlist())
        for withdrawn in (
            "mcp__search__web_search",
            "mcp__markets__search_markets",
            "mcp__markets__polymarket_price",
            "mcp__financial__fred_series",
            "mcp__financial__stock_price",
            "mcp__trends__google_trends",
        ):
            assert withdrawn not in allowed


class TestToolPolicyDelegated:
    """The other topology: the same tools, one context down."""

    def test_delegated_gives_the_forecaster_research(self) -> None:
        policy = ToolPolicy(research="delegated", metaculus_token="t")
        allowed = set(policy.orchestrator_allowlist())
        assert RESEARCH_TOOLS <= allowed

    def test_delegated_keeps_retrieval_on_the_forecaster(self) -> None:
        """Enough to check one fact without opening a sub-agent for it."""
        policy = ToolPolicy(research="delegated", metaculus_token="t")
        allowed = set(policy.orchestrator_allowlist())
        assert CORE_DATA_TOOLS <= allowed

    def test_delegated_moves_the_rest_behind_research(self) -> None:
        policy = ToolPolicy(research="delegated", metaculus_token="t")
        allowed = set(policy.orchestrator_allowlist())
        assert not (DATA_TOOLS - CORE_DATA_TOOLS) & allowed

    def test_condensed_withdraws_the_tool_that_would_delegate(self) -> None:
        """An arm that may or may not have delegated measures neither shape."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.orchestrator_servers(sandbox)

        assert "research" not in servers
        assert not RESEARCH_TOOLS & set(policy.orchestrator_allowlist())

    def test_the_shipped_topology_is_the_condensed_one(self) -> None:
        """Sixteen tools fit, so the forecaster holds them."""
        assert ToolPolicy().research == "condensed"


class TestToolPolicyDirect:
    """The surface this project ran before the condensed tools.

    Kept runnable because the narrow tools were unregistered rather than
    deleted: the value costs a branch, and dropping it would cost the
    ability to run that surface at all.
    """

    def test_direct_mounts_the_narrow_tools(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy(research="direct").orchestrator_servers(sandbox)
        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }

        assert "mcp__search__web_search" in served
        assert "mcp__markets__search_markets" in served
        assert "mcp__markets__polymarket_history" in served
        assert "mcp__wayback__wayback_snapshot" in served

    def test_direct_mounts_none_of_the_merged_tools(self) -> None:
        """One surface at a time, or a session carries both descriptions.

        Only the seven that actually merged. `census`, `weather` and
        `stock_conditional_returns` are in `DATA_TOOLS` and here both,
        because nothing was merged into any of them — each has an address
        space of its own that no other tool shared.
        """
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy(research="direct").orchestrator_servers(sandbox)
        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }

        merged = {
            "mcp__search__search",
            "mcp__search__fetch",
            "mcp__financial__series",
            "mcp__financial__stock",
            "mcp__markets__market",
            "mcp__markets__metaculus",
            "mcp__trends__trends",
        }
        assert merged < DATA_TOOLS
        assert not merged & served
        assert "research" not in servers

    def test_direct_grants_every_tool_it_mounts(self) -> None:
        """A tool registered and left out of the roster reads as broken.

        The roster is read off the servers the session actually carries, so
        the two cannot disagree — which is why forty tools are derived where
        sixteen are declared.
        """
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy(research="direct", fred_api_key="f", exa_api_key="e")
        servers = policy.orchestrator_servers(sandbox)
        granted = set(policy.orchestrator_allowlist(mounted=servers))

        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }
        assert served
        assert served - policy.excluded_tools.keys() <= granted

    def test_a_missing_key_ungrants_the_narrow_tool_it_governs(self) -> None:
        """Where a condensed lane would be dropped, a narrow tool is ungranted.

        The exclusion is what obeys the policy's own key argument. The
        module-level tool lists read the process settings, so a policy built
        with `exa_api_key=None` in an environment that has one would
        otherwise still serve and grant `search_exa`.
        """
        without = ToolPolicy(research="direct", exa_api_key=None)
        granted = set(without.orchestrator_allowlist())

        assert "mcp__search__search_exa" not in granted
        assert "mcp__search__web_search" in granted

    def test_asknews_is_named_rather_than_derived_so_it_is_gated(self) -> None:
        """The one server introspection cannot enumerate.

        `server_tool_names` answers `[]` for an HTTP server, so its four
        tools are named — and nothing else would stop a key-less session
        granting four tools no server can serve.
        """
        without = ToolPolicy(research="direct", asknews_api_key=None)
        assert not ASKNEWS_TOOLS & set(without.narrow_allowlist())

        withkey = ToolPolicy(research="direct", asknews_api_key="k")
        assert ASKNEWS_TOOLS <= set(withkey.narrow_allowlist())


class TestToolPolicySpawn:
    """Tests for subforecast availability."""

    def test_subforecast_allowed_by_default(self) -> None:
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist(allow_spawn=True)
        assert "mcp__subforecast__subforecast" in allowed

    def test_subforecast_excluded_when_disabled(self) -> None:
        policy = ToolPolicy()
        allowed = policy.orchestrator_allowlist(allow_spawn=False)
        assert "mcp__subforecast__subforecast" not in allowed


class TestToolPolicyIsToolAvailable:
    """Tests for is_tool_available method (API key gating)."""

    def test_builtin_always_available(self) -> None:
        policy = ToolPolicy()
        for tool in BUILTIN_TOOLS:
            assert policy.is_tool_available(tool)

    def test_excluded_tool_not_available(self) -> None:
        policy = ToolPolicy(metaculus_token=None)
        for tool in METACULUS_TOOLS:
            assert not policy.is_tool_available(tool)

    def test_trends_always_available(self) -> None:
        """Trends needs no API key."""
        assert ToolPolicy().is_tool_available("mcp__trends__trends")

    def test_a_lane_credential_does_not_withhold_its_tool(self) -> None:
        """Exa, AskNews and Reddit each govern one lane of nine.

        Withholding `search` for a missing EXA_API_KEY would withhold the
        eight lanes that key has nothing to do with, so the lane drops and
        the tool stays.
        """
        policy = ToolPolicy(exa_api_key=None, asknews_api_key=None)
        assert policy.is_tool_available("mcp__search__search")

    def test_fred_key_does_not_withhold_the_series_tool(self) -> None:
        """`series` still answers for the World Bank and BLS without it."""
        assert ToolPolicy(fred_api_key=None).is_tool_available("mcp__financial__series")


class TestToolPolicyMcpServers:
    """Tests for the servers the forecaster mounts."""

    def test_includes_orchestrator_servers(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy().orchestrator_servers(sandbox)

        assert "sandbox" in servers
        assert "subforecast" in servers
        assert "notes" in servers
        assert "premortem" in servers

    def test_condensed_mounts_the_data_servers(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy().orchestrator_servers(sandbox)

        assert "search" in servers
        assert "financial" in servers
        assert "government" in servers
        assert "markets" in servers
        assert "trends" in servers

    def test_delegated_mounts_only_retrieval_and_research(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy(research="delegated").orchestrator_servers(sandbox)

        assert "research" in servers
        assert "search" in servers
        assert "financial" not in servers
        assert "government" not in servers
        assert "trends" not in servers

    def test_weather_is_withheld_from_a_backtest(self) -> None:
        """A forecast for a past date cannot ask what the weather will be."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy()
            assert "weather" not in policy.orchestrator_servers(sandbox)
            allowed = set(policy.orchestrator_allowlist())
            assert not WEATHER_TOOLS & allowed
        finally:
            retrodict_cutoff.reset(token)


class TestToolPolicyDataServers:
    """The data surface, which both topologies build from."""

    def test_includes_every_data_server(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        servers = ToolPolicy().data_servers(sandbox)

        assert "financial" in servers
        assert "government" in servers
        assert "sandbox" in servers
        assert "markets" in servers
        assert "trends" in servers
        assert "search" in servers

    def test_serves_exactly_the_declared_data_surface(self) -> None:
        """The declaration and the servers cannot drift apart unnoticed."""
        policy = ToolPolicy()
        servers = policy.data_servers()

        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }
        assert served == set(DATA_TOOLS)

    def test_the_sub_agent_gets_the_same_surface_as_the_forecaster(self) -> None:
        """Re-plugging research() must not resurrect an older tool surface."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        forecaster = ToolPolicy().orchestrator_servers(sandbox)
        delegate = ToolPolicy(research="delegated").data_servers()

        for name in delegate:
            assert name in forecaster


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
        docs = policy._format_tool_docs({"mcp__search__search": "Search everything."})
        assert "exact name" in docs


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
    ) -> set[str]:
        """What the tools on `servers` come to, minus the sandbox's."""
        names = set(policy.get_allowed_tools(servers, builtin_tools=BUILTIN_TOOLS))
        return names - SANDBOX_TOOLS

    def test_the_orchestrator_allowlist_is_what_its_servers_serve(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()
        policy = ToolPolicy(metaculus_token="t", census_api_key="c")

        servers = policy.orchestrator_servers(sandbox)
        declared = set(policy.orchestrator_allowlist()) - SANDBOX_TOOLS

        assert self.derived(servers, policy) == declared

    def test_the_delegated_allowlist_is_what_its_servers_serve(self) -> None:
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()
        policy = ToolPolicy(research="delegated", metaculus_token="t")

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
        """
        from aib.tools.research import get_research_allowed_tools

        policy = ToolPolicy(fred_api_key="f", exa_api_key="e", census_api_key="c")
        servers = policy.data_servers()
        granted = set(get_research_allowed_tools(servers))

        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }
        assert served
        assert served - policy.excluded_tools.keys() <= granted

    @pytest.mark.parametrize("topology", ["condensed", "delegated", "direct"])
    def test_the_resolver_is_granted_what_it_is_served(
        self, topology: str, monkeypatch: pytest.MonkeyPatch
    ) -> None:
        """Under every topology, not only the one it happens to default to.

        The resolver's servers are `data_tool_groups()` whatever `research`
        is set to, so a roster read off a topology-dependent allowlist
        agreed with them only on the default. Under `direct` the two had
        three names in common out of forty.
        """
        from aib.agent.resolver import build_resolver_servers, build_resolver_tools
        from aib.config import settings as live_settings

        monkeypatch.setattr(live_settings, "research", topology)
        servers = build_resolver_servers()
        granted = {t for t in build_resolver_tools(servers) if t.startswith("mcp__")}

        served = {
            f"mcp__{name}__{tool}"
            for name, server in servers.items()
            for tool in server_tool_names(server)
        }
        assert served
        assert served == granted
