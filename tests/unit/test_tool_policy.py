"""Tests for ToolPolicy class."""

from datetime import date
from unittest.mock import MagicMock

from aib.retrodict_context import retrodict_cutoff
from aib.agent.tool_policy import (
    ASKNEWS_TOOLS,
    BUILTIN_TOOLS,
    EXA_TOOLS,
    FETCH_TOOLS,
    FRED_TOOLS,
    HISTORICAL_MARKET_TOOLS,
    LIVE_MARKET_TOOLS,
    METACULUS_TOOLS,
    TRENDS_TOOLS,
    WORLD_BANK_TOOLS,
    ToolPolicy,
)


class TestToolPolicyToolSets:
    """Tests for tool set constants."""

    def test_builtin_tools_present(self) -> None:
        """Built-in tools should be defined."""
        assert "WebSearch" in BUILTIN_TOOLS
        assert "WebFetch" in BUILTIN_TOOLS
        assert "Bash" in BUILTIN_TOOLS
        assert "Task" in BUILTIN_TOOLS

    def test_metaculus_tools_require_token(self) -> None:
        """Metaculus tools should all have markets prefix."""
        for tool in METACULUS_TOOLS:
            assert tool.startswith("mcp__markets__")

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


class TestToolPolicyExclusions:
    """Tests for tool exclusion logic."""

    def test_excludes_metaculus_without_token(self) -> None:
        """Should exclude Metaculus tools without token."""
        policy = ToolPolicy(metaculus_token=None)

        allowed = policy.get_allowed_tools()
        for tool in METACULUS_TOOLS:
            assert tool not in allowed

    def test_includes_metaculus_with_token(self) -> None:
        """Should include Metaculus tools with token."""
        policy = ToolPolicy(metaculus_token="test-token")

        allowed = policy.get_allowed_tools()
        for tool in METACULUS_TOOLS:
            assert tool in allowed

    def test_excludes_exa_without_key(self) -> None:
        """Should exclude Exa tools without API key."""
        policy = ToolPolicy(exa_api_key=None)

        allowed = policy.get_allowed_tools()
        for tool in EXA_TOOLS:
            assert tool not in allowed

    def test_excludes_asknews_without_any_credentials(self) -> None:
        """Should exclude AskNews tools without any credentials."""
        policy = ToolPolicy()

        allowed = policy.get_allowed_tools()
        for tool in ASKNEWS_TOOLS:
            assert tool not in allowed

    def test_includes_asknews_with_api_key(self) -> None:
        """Should include AskNews tools with api_key."""
        policy = ToolPolicy(asknews_api_key="key")

        allowed = policy.get_allowed_tools()
        for tool in ASKNEWS_TOOLS:
            assert tool in allowed

    def test_excludes_fred_without_key(self) -> None:
        """Should exclude FRED tools without API key."""
        policy = ToolPolicy(fred_api_key=None)

        allowed = policy.get_allowed_tools()
        for tool in FRED_TOOLS:
            assert tool not in allowed

    def test_includes_live_markets_in_retrodict(self) -> None:
        """Live market tools should be in allowed_tools in retrodict mode.

        They handle retrodict internally by returning historical prices.
        """
        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy()
            allowed = policy.get_allowed_tools()
            for tool in LIVE_MARKET_TOOLS:
                assert tool in allowed
        finally:
            retrodict_cutoff.reset(token)

    def test_includes_historical_markets_in_retrodict(self) -> None:
        """Should include historical market tools in retrodict mode."""
        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy()
            allowed = policy.get_allowed_tools()
            for tool in HISTORICAL_MARKET_TOOLS:
                assert tool in allowed
        finally:
            retrodict_cutoff.reset(token)


class TestToolPolicySpawn:
    """Tests for spawn_subquestions availability."""

    def test_spawn_allowed_by_default(self) -> None:
        """spawn_subquestions should be allowed by default."""
        policy = ToolPolicy()
        allowed = policy.get_allowed_tools(allow_spawn=True)
        assert "mcp__composition__spawn_subquestions" in allowed

    def test_spawn_excluded_when_disabled(self) -> None:
        """spawn_subquestions should be excluded when allow_spawn=False."""
        policy = ToolPolicy()
        allowed = policy.get_allowed_tools(allow_spawn=False)
        assert "mcp__composition__spawn_subquestions" not in allowed


class TestToolPolicyIsToolAvailable:
    """Tests for is_tool_available method."""

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

    def test_fetch_always_available(self) -> None:
        """Fetch tools should always be available (no API key required)."""
        policy = ToolPolicy()

        for tool in FETCH_TOOLS:
            assert policy.is_tool_available(tool)

    def test_world_bank_always_available(self) -> None:
        """World Bank tools should always be available (no API key required)."""
        policy = ToolPolicy()

        for tool in WORLD_BANK_TOOLS:
            assert policy.is_tool_available(tool)

    def test_world_bank_in_allowed_tools(self) -> None:
        """World Bank tools should appear in get_allowed_tools."""
        policy = ToolPolicy()
        allowed = policy.get_allowed_tools()
        for tool in WORLD_BANK_TOOLS:
            assert tool in allowed


class TestToolPolicyMcpServers:
    """Tests for get_mcp_servers method."""

    def test_includes_core_servers(self) -> None:
        """Should include core MCP servers."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.get_mcp_servers(sandbox)

        assert "financial" in servers
        assert "sandbox" in servers
        assert "composition" in servers
        assert "markets" in servers
        assert "notes" in servers
        assert "trends" in servers
        assert "search" in servers
        assert "arxiv" not in servers

    def test_adds_search_server_in_retrodict(self) -> None:
        """Should add date-filtered search server in retrodict mode."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy()
            servers = policy.get_mcp_servers(sandbox)
            assert "search" in servers
        finally:
            retrodict_cutoff.reset(token)

    def test_search_server_in_normal_mode(self) -> None:
        """Search server should be present in normal mode too."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.get_mcp_servers(sandbox)
        assert "search" in servers

    def test_includes_asknews_server_with_api_key(self) -> None:
        """Should register throttled AskNews proxy server when api_key is set."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy(asknews_api_key="test-key")
        servers = policy.get_mcp_servers(sandbox)

        assert "asknews" in servers
        asknews = servers["asknews"]
        assert isinstance(asknews, dict)
        assert asknews.get("type") == "sdk"
        assert asknews.get("name") == "asknews"

    def test_excludes_asknews_server_without_api_key(self) -> None:
        """Should not register AskNews server without api_key."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        policy = ToolPolicy()
        servers = policy.get_mcp_servers(sandbox)

        assert "asknews" not in servers

    def test_excludes_asknews_server_in_retrodict(self) -> None:
        """Should not register AskNews server in retrodict mode."""
        sandbox = MagicMock()
        sandbox.create_mcp_server.return_value = MagicMock()

        token = retrodict_cutoff.set(date(2026, 1, 15))
        try:
            policy = ToolPolicy(asknews_api_key="test-key")
            servers = policy.get_mcp_servers(sandbox)
            assert "asknews" not in servers
        finally:
            retrodict_cutoff.reset(token)
