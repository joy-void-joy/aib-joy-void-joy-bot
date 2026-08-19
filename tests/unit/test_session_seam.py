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
from lup.adapters.claude.runtime import (
    SUBMISSION_TOOL,
    ClaudeSandboxConfig,
    build_claude_options,
)
from lup.runtime.output import SubmissionResponse, TurnSubmission
from lup.types import JsonValue
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


def test_the_derived_home_still_runs_as_the_login_the_profile_names(
    tmp_path: Path,
) -> None:
    """Containment narrows what a session writes, never which login it runs as.

    Asked of the login rather than of where the home sits. A derived home is
    this project's own state and belongs in the tree it serves, while the
    home a profile names belongs to the account — so one sitting inside the
    other was never what made the account carry over. The stored login is
    reached by symlink, which is also why it is not copied: a refresh rotates
    the token, and a copy is what would go stale still holding the old one.
    """
    credentials = tmp_path / ".credentials.json"
    credentials.write_text("{}", encoding="utf-8")

    home = Path(
        contained_home(
            select_runtime("claude"), tmp_path, one_shot_request("sonnet", "", None)
        )
    )

    assert (home / ".credentials.json").is_symlink()
    assert (home / ".credentials.json").resolve() == credentials


def test_every_claude_session_loads_its_tool_schemas_eagerly() -> None:
    """Deferred schemas left the research agent guessing search terms.

    Asked of the rendered configuration rather than of the shared environment:
    the variable is Claude Code's own, so it rides the transform that carries
    what only one runtime reads — and the thing worth pinning is that it
    reaches the session, not where it was written down."""
    rendered = ClaudeExtras().apply(
        claude_config(agent_request(model="sonnet", system_prompt="", autonomy="ask"))
    )

    assert rendered.environment["ENABLE_TOOL_SEARCH"] == "false"


def test_the_shared_environment_names_no_single_runtimes_variable() -> None:
    """The argument that made effort a field: a variable naming one provider
    goes on quietly meaning nothing to the other, and the Codex arm would run
    with deferral on and nothing saying so."""
    assert "ENABLE_TOOL_SEARCH" not in session_env(None)


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


async def accept_submission(_: JsonValue) -> SubmissionResponse:
    """Stand in for the handler a turn binds, which nothing here calls."""
    return SubmissionResponse(accepted=True, message="")


def test_the_roster_reaches_the_field_that_bounds_a_session() -> None:
    """`tools` is the engine's set of built-ins and `allowed_tools` auto-approves
    without restricting, so a roster stated only through the second bounds
    nothing. A session naming one built-in gets exactly it — not the default
    set, which is what an unstated roster would have left standing."""
    rendered = claude_config(
        agent_request(
            model="sonnet",
            system_prompt="",
            autonomy="unattended",
            allowed_tools=["Read"],
        )
    )

    assert rendered.tools == ["Read"]
    assert "Read" in rendered.allowed_tools


def test_a_session_wanting_no_builtin_is_given_none_rather_than_all() -> None:
    """The worldview sessions work entirely through their own MCP servers. An
    empty roster is what says so; the absent one they had before is the whole
    default set, which is the opposite instruction."""
    rendered = claude_config(
        agent_request(
            model="sonnet",
            system_prompt="",
            autonomy="ask",
            allowed_tools=["mcp__worldview_maintenance__wv_read_entry"],
        )
    )

    assert rendered.tools == []


def test_a_session_declares_no_hook_where_the_caller_asked_for_none() -> None:
    """The allowlist hook stood in for a roster field this project was not
    using. With the roster stated, a session carries only the hooks its caller
    actually wanted — and `hooks` being unset is half of what a Codex session
    is no longer refused for."""
    request = agent_request(
        model="sonnet", system_prompt="", autonomy="ask", allowed_tools=["Read"]
    )

    assert request.hooks is None


def test_the_submission_tool_is_auto_approved_by_the_runtime_installing_it() -> None:
    """A structured turn ends through a tool the runtime installs, so at `ask`
    it has to be auto-approved or the turn cannot finish. This project used to
    name it into every allowlist because its own hook was enforced by name;
    the runtime does it, and this pins that rather than restating it."""
    options = build_claude_options(
        claude_config(
            agent_request(
                model="sonnet",
                system_prompt="",
                autonomy="ask",
                allowed_tools=["Read"],
            )
        ),
        binding=lambda: TurnSubmission(schema={}, submit=accept_submission),
        resume=None,
        session_id=None,
    )

    assert SUBMISSION_TOOL in options.allowed_tools


def test_codex_refuses_a_tool_using_session_for_what_it_really_lacks() -> None:
    """Codex refused three fields here, and one of the three was this project's
    own doing: a hook built by hand to enforce a roster stated through a field
    that does not restrict. That hook is gone, and with it the refusal it
    caused.

    Two remain and both are the runtime's own: the app-server has no field for
    a built-in roster, and no concept of an auto-approval list. Neither is
    something this project can stop asking for — the roster is what bounds a
    session, and the approval list is what lets one open below `unattended`
    without stalling on a question nobody hears.
    """
    request = agent_request(
        model="sonnet", system_prompt="", autonomy="ask", allowed_tools=["Read"]
    )

    with pytest.raises(ValueError, match="no session-level tools, allowed_tools;"):
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
