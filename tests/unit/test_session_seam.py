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
from lup.adapters.codex.login import CODEX_HOME
from lup.adapters.codex.selection import CODEX_AUTONOMY, codex_config
from lup.runtime.selection import Runtime, SessionAutonomy, SessionRequest

from aib.agent.client import (
    SESSION_BUFFER_BYTES,
    ClaudeExtras,
    agent_request,
    one_shot_request,
    session_env,
)
from aib.paths import AGENT_CWD
from aib.runtime import select_runtime


def contained_home(runtime: Runtime, account: Path, request: SessionRequest) -> str:
    """The home that runtime derives for one of this project's sessions.

    Read off a contained request rather than off the environment a request is
    built with: the home appears when a session is opened, which is the only
    moment both the workspace and the runtime opening it are known.

    The account is named rather than inherited so the derivation lands under
    a directory the test owns. Containment derives under whichever home the
    environment already selects, and a suite that let it select the operator's
    own would write there to assert that it does not.
    """
    variable = runtime.login.config_home_env
    rooted = request.model_copy(
        update={"environment": {**request.environment, variable: str(account)}}
    )
    return runtime.contained(rooted).environment[variable]


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


def test_a_session_runs_in_a_configuration_home_of_its_own(tmp_path: Path) -> None:
    """Shared, two concurrent startups read each other's half-written document."""
    home = contained_home(
        select_runtime("claude"), tmp_path, one_shot_request("sonnet", "", None)
    )

    assert AGENT_CWD.name in home


def test_the_derived_home_sits_under_the_one_the_profile_names(tmp_path: Path) -> None:
    """Containment narrows what a session writes, never which login it runs as."""
    home = contained_home(
        select_runtime("claude"), tmp_path, one_shot_request("sonnet", "", None)
    )

    assert home.startswith(str(tmp_path))


def test_every_session_loads_its_tool_schemas_eagerly() -> None:
    """Deferred schemas left the research agent guessing search terms."""
    assert session_env(None)["ENABLE_TOOL_SEARCH"] == "false"


def test_stating_a_request_asks_for_no_home_and_touches_no_disk() -> None:
    """A request is a declaration. Deriving the home here did a real `mkdir`
    seeded from the selected account, so building a session nobody opened cost
    a directory — and picked a runtime before one had been named."""
    request = one_shot_request("sonnet", "", None)

    assert CLAUDE_CONFIG_DIR not in request.environment
    assert CODEX_HOME not in request.environment


def test_both_session_shapes_are_contained_in_the_same_home(tmp_path: Path) -> None:
    """The portable path and the streaming path have to agree on containment."""
    runtime = select_runtime("claude")
    tool_free = one_shot_request("sonnet", "", None)
    tool_using = agent_request(
        model="sonnet", system_prompt="", autonomy="unattended", allowed_tools=["Read"]
    )

    assert contained_home(runtime, tmp_path, tool_free) == contained_home(
        runtime, tmp_path, tool_using
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


@pytest.mark.parametrize(
    ("autonomy", "permission_mode", "sandbox"),
    [
        ("ask", "default", "read-only"),
        ("accept_edits", "acceptEdits", "workspace-write"),
        ("unattended", "bypassPermissions", "danger-full-access"),
    ],
)
def test_the_degree_a_session_states_is_the_one_both_runtimes_render(
    autonomy: SessionAutonomy, permission_mode: str, sandbox: str
) -> None:
    """Autonomy is what each session says about its own reach, so the degree a
    caller states has to survive rendering — as a permission mode on Claude and
    as a sandbox on Codex, which is the whole of what bounds a session there.

    `plan` is absent because no session here opens at it: Claude renders it as
    plan mode, where the model presents a plan instead of acting, and every
    session this project opens has to act and then answer.
    """
    request = agent_request(
        model="sonnet", system_prompt="", autonomy=autonomy, allowed_tools=["Read"]
    )

    assert claude_config(request).permission_mode == permission_mode
    assert CODEX_AUTONOMY[autonomy] == sandbox


def test_the_allowlist_and_the_hook_enforcing_it_both_reach_claude() -> None:
    """Under bypassPermissions the SDK field alone is ignored, so the hook is
    what actually holds the line — and it has to render alongside it."""
    rendered = claude_config(
        agent_request(
            model="sonnet",
            system_prompt="",
            autonomy="unattended",
            allowed_tools=["Read"],
        )
    )

    assert "Read" in rendered.allowed_tools
    assert rendered.hooks is not None


def test_the_allowlist_admits_the_tool_a_structured_turn_finishes_through() -> None:
    """A structured turn is served by a submission tool the runtime installs.
    The allowlist hook is enforced by name, so one written without it denies
    the single tool the turn cannot end without — and the failure would be an
    agent that researched correctly and could not answer."""
    request = agent_request(
        model="sonnet", system_prompt="", autonomy="unattended", allowed_tools=["Read"]
    )

    assert SUBMISSION_TOOL in request.allowed_tools


def test_codex_refuses_a_tool_using_session_by_design() -> None:
    """Not a gap to close here: on Codex the dispatcher generated into its
    harness tree governs, so a session-level allowlist would be a second
    answer to a question that already has one."""
    request = agent_request(
        model="sonnet", system_prompt="", autonomy="unattended", allowed_tools=["Read"]
    )

    with pytest.raises(ValueError, match="no session-level"):
        codex_config(request)


def test_claude_only_settings_ride_a_transform_rather_than_the_request() -> None:
    """A request carrying these would be asking Codex for what it cannot answer."""
    extras = ClaudeExtras(
        add_dirs=[Path("/tmp/notes")],
        sandbox=ClaudeSandboxConfig(enabled=True),
    )
    rendered = extras.apply(
        claude_config(
            agent_request(model="sonnet", system_prompt="", autonomy="unattended")
        )
    )

    assert rendered.add_dirs == [Path("/tmp/notes")]
    assert rendered.sandbox is not None and rendered.sandbox.enabled


def test_a_session_holds_one_whole_frame_of_a_fetched_page() -> None:
    """A Wayback snapshot arrives as a single frame well past the SDK ceiling."""
    rendered = ClaudeExtras().apply(
        claude_config(
            agent_request(model="sonnet", system_prompt="", autonomy="unattended")
        )
    )

    assert rendered.max_buffer_size == SESSION_BUFFER_BYTES


def test_a_session_is_pointed_at_the_home_of_the_runtime_opening_it(
    tmp_path: Path,
) -> None:
    """Containment is a per-runtime fact, so the variable naming it has to be
    the selected runtime's own. Naming Claude's unconditionally pointed a
    Codex session at a home its CLI never reads, and dropped the `CODEX_HOME`
    the profile selected — so the arm ran under whichever account happened to
    be logged in rather than the one asked for."""
    request = one_shot_request("sonnet", "", None)
    codex = select_runtime("codex")

    opened = codex.contained(
        request.model_copy(update={"environment": {CODEX_HOME: str(tmp_path)}})
    ).environment

    assert CODEX_HOME in opened
    assert CLAUDE_CONFIG_DIR not in opened
