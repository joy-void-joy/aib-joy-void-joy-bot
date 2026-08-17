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

from lup.adapters.claude.login import CLAUDE_CONFIG_DIR
from lup.runtime.selection import SessionRequest

from aib.agent.client import one_shot_request, session_env
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


def test_effort_still_travels_as_an_environment_variable() -> None:
    """Portable requests have no word for it yet — joy-void-joy/lup#227.

    Pinned so that when the field lands this fails and says where to move it,
    rather than leaving two ways to ask for the same thing.
    """
    request = one_shot_request("sonnet", "", None)

    assert request.environment["CLAUDE_CODE_EFFORT_LEVEL"] == "max"
    assert "effort" not in SessionRequest.model_fields


def test_the_runtime_a_session_opens_through_is_the_selected_one() -> None:
    assert select_runtime("claude").name == "Claude Code"
    assert select_runtime("codex").name == "Codex"
