"""Whether a roster bounds a session that bypasses permissions.

The question this settles is which field states "this session may call only
these tools". Claude's SDK documents two that read alike and are not: `tools`
is "the base set of available built-in tools", while `allowed_tools` is an
auto-approval list whose own documentation says to use `tools` "to restrict
which tools are available at all".

The doubt is that a session opened at `unattended` — Claude's
`bypassPermissions` — is known to ignore `allowed_tools`, because that mode
skips the permission check `allowed_tools` feeds. Whether it also ignores
`tools` is not documented either way, and the two fields fail differently:
one is a permission, the other is which tools the model is given at all.

So it is asked of a real session rather than reasoned about. Both arms are
needed. The bounded arm alone proves nothing — a model that simply chose not
to reach for the shell looks identical to one that could not — so the control
establishes that this prompt does reach it when the roster admits it.
"""

import pytest
from lup.runtime.selection import SessionRequest

from aib.agent.client import agent_session, session_env
from aib.paths import AGENT_CWD

pytestmark = pytest.mark.integration

PROBE = "Run the shell command `echo probe` with the Bash tool, then tell me what it printed."

PROBE_INSTRUCTIONS = "You are a shell assistant. When asked to run a command, run it."


def roster_probe_request(tools: list[str] | None) -> SessionRequest:
    """One unattended, hookless session carrying exactly this roster.

    Hookless is the whole point: this project's allowlist hook would hold the
    line whatever the roster field does, so a probe carrying it would measure
    the hook. Built here rather than through `agent_request` for that reason.
    """
    AGENT_CWD.mkdir(parents=True, exist_ok=True)
    return SessionRequest(
        model="haiku",
        instructions=PROBE_INSTRUCTIONS,
        cwd=AGENT_CWD,
        autonomy="unattended",
        tools=tools,
        environment=session_env(None),
    )


async def tools_called(tools: list[str] | None) -> set[str]:
    """Every tool one probe session actually invoked."""
    factory = agent_session(roster_probe_request(tools), runtime="claude")
    result = await factory.query(PROBE)
    return {
        block.tool_call_name
        for block in result.blocks
        if block.tool_call_name is not None
    }


async def test_the_probe_prompt_reaches_the_shell_when_the_roster_admits_it() -> None:
    """The control. A session naming no roster gets Claude Code's own default
    set, so this prompt has Bash available and takes it — which is what makes
    the bounded arm's silence mean the roster and not the model's choice."""
    assert "Bash" in await tools_called(None)


async def test_a_name_the_engine_does_not_know_leaves_the_roster_standing() -> None:
    """This project's roster is derived by intersecting what a session asked
    for with the built-ins it declares, and that declaration carries names the
    engine has no built-in for — `StructuredOutput` among them, which is served
    over MCP. A roster that refused such a name would turn a derivation into a
    list every caller had to curate against a set nobody publishes.

    Asked as "does the roster still bind", which separates the three outcomes
    that matter: a raised error fails here, a roster quietly discarded shows up
    as the shell being reachable, and a name harmlessly ignored passes."""
    assert "Bash" not in await tools_called(["Read", "StructuredOutput"])


async def test_a_roster_bounds_a_session_that_bypasses_permissions() -> None:
    """The gate. `tools` naming only Read leaves a session at `unattended`
    unable to reach the shell, which is what makes the field a roster rather
    than a preference — and what leaves this project's allowlist hook with no
    remaining job on the built-ins it was written to hold."""
    assert "Bash" not in await tools_called(["Read"])
