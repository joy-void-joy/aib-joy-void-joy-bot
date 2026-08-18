"""What a session this project opens asks for, whichever runtime opens it.

A portable request says what a caller wants in words both runtimes share, and
each runtime renders it. Two things are worth pinning about that arrangement.

The first is that a tool-free inference is the one session shape this project
opens that either runtime accepts unchanged — Codex refuses `tools`,
`allowed_tools` and `hooks`, and this request sets none of them. The second is
containment: sessions are opened concurrently, a provider CLI rewrites its
startup document non-atomically, and the failure when two collide is a
truncated parse before any work begins. The home is derived per workspace so
that cannot happen, and so what one session writes stays inside its own
folder.
"""

from pathlib import Path

import pytest
from lup.adapters.claude.login import CLAUDE_CONFIG_DIR
from lup.adapters.claude.runtime import SUBMISSION_TOOL, ClaudeSandboxConfig
from lup.adapters.claude.selection import claude_config
from lup.adapters.codex.selection import codex_config

from aib.agent.client import (
    SESSION_BUFFER_BYTES,
    ClaudeExtras,
    agent_request,
    one_shot_request,
    session_env,
)
from aib.paths import AGENT_CWD
from aib.runtime import select_runtime


def test_a_tool_free_request_is_one_either_runtime_accepts() -> None:
    """The three fields Codex refuses are the three this request never sets."""
    request = one_shot_request("sonnet", "be brief", None)

    assert request.tools is None
    assert request.allowed_tools == []
    assert request.hooks is None


def test_a_tool_free_request_carries_the_model_prompt_and_cwd() -> None:
    request = one_shot_request("sonnet", "be brief", None)

    assert request.model == "sonnet"
    assert request.instructions == "be brief"
    assert request.cwd == AGENT_CWD


def test_a_session_runs_in_a_configuration_home_of_its_own() -> None:
    """Shared, two concurrent startups read each other's half-written document."""
    home = session_env(None)[CLAUDE_CONFIG_DIR]

    assert AGENT_CWD.name in home


def test_the_derived_home_sits_under_the_one_the_profile_names() -> None:
    """Containment narrows what a session writes, never which login it runs as."""
    home = session_env(None)[CLAUDE_CONFIG_DIR]

    assert ".lup-sessions" in home


def test_every_session_loads_its_tool_schemas_eagerly() -> None:
    """Deferred schemas left the research agent guessing search terms."""
    assert session_env(None)["ENABLE_TOOL_SEARCH"] == "false"


def test_a_tool_free_request_runs_in_that_same_contained_home() -> None:
    """The portable path and the streaming path have to agree on containment."""
    request = one_shot_request("sonnet", "", None)

    assert (
        request.environment[CLAUDE_CONFIG_DIR] == session_env(None)[CLAUDE_CONFIG_DIR]
    )


def test_effort_is_asked_for_portably_rather_than_through_the_environment() -> None:
    """`CLAUDE_CODE_EFFORT_LEVEL` is one runtime's variable and means nothing
    to the other, so a request that only set it would run the Codex arm at
    whatever its own configuration file happened to say."""
    request = one_shot_request("sonnet", "", None)

    assert request.effort == "max"
    assert "CLAUDE_CODE_EFFORT_LEVEL" not in request.environment


def test_the_effort_asked_for_reaches_both_runtimes() -> None:
    """A degree that rendered to None would be the silent fall-through itself."""
    request = one_shot_request("sonnet", "", None)

    assert claude_config(request).effort is not None
    assert codex_config(request).effort is not None


def test_the_runtime_a_session_opens_through_is_the_selected_one() -> None:
    assert select_runtime("claude").name == "Claude Code"
    assert select_runtime("codex").name == "Codex"


def test_a_tool_using_session_asks_for_unattended_autonomy() -> None:
    """`bypassPermissions` is Claude's spelling of a degree both runtimes have."""
    request = agent_request(model="sonnet", system_prompt="", allowed_tools=["Read"])

    assert request.autonomy == "unattended"
    assert claude_config(request).permission_mode == "bypassPermissions"


def test_the_allowlist_and_the_hook_enforcing_it_both_reach_claude() -> None:
    """Under bypassPermissions the SDK field alone is ignored, so the hook is
    what actually holds the line — and it has to render alongside it."""
    rendered = claude_config(
        agent_request(model="sonnet", system_prompt="", allowed_tools=["Read"])
    )

    assert "Read" in rendered.allowed_tools
    assert rendered.hooks is not None


def test_the_allowlist_admits_the_tool_a_structured_turn_finishes_through() -> None:
    """A structured turn is served by a submission tool the runtime installs.
    The allowlist hook is enforced by name, so one written without it denies
    the single tool the turn cannot end without — and the failure would be an
    agent that researched correctly and could not answer."""
    request = agent_request(model="sonnet", system_prompt="", allowed_tools=["Read"])

    assert SUBMISSION_TOOL in request.allowed_tools


def test_codex_refuses_a_tool_using_session_by_design() -> None:
    """Not a gap to close here: on Codex the dispatcher generated into its
    harness tree governs, so a session-level allowlist would be a second
    answer to a question that already has one."""
    request = agent_request(model="sonnet", system_prompt="", allowed_tools=["Read"])

    with pytest.raises(ValueError, match="no session-level"):
        codex_config(request)


def test_claude_only_settings_ride_a_transform_rather_than_the_request() -> None:
    """A request carrying these would be asking Codex for what it cannot answer."""
    extras = ClaudeExtras(
        add_dirs=[Path("/tmp/notes")],
        sandbox=ClaudeSandboxConfig(enabled=True),
    )
    rendered = extras.apply(
        claude_config(agent_request(model="sonnet", system_prompt=""))
    )

    assert rendered.add_dirs == [Path("/tmp/notes")]
    assert rendered.sandbox is not None and rendered.sandbox.enabled


def test_a_session_holds_one_whole_frame_of_a_fetched_page() -> None:
    """A Wayback snapshot arrives as a single frame well past the SDK ceiling."""
    rendered = ClaudeExtras().apply(
        claude_config(agent_request(model="sonnet", system_prompt=""))
    )

    assert rendered.max_buffer_size == SESSION_BUFFER_BYTES
