"""What every agent session this project opens asks for.

Sessions are stated portably and opened through the selected runtime, so this
module is the only place either provider's own configuration is named.

Exports:
- agent_request(...) — a tool-using session, in words both runtimes share
- agent_session(request, extras=...) — the factory the selection answers with
- ClaudeExtras — the settings only Claude has a word for
- one_shot(prompt, ...) — prompt→result convenience for tool-free LLM calls
"""

import logging
from collections.abc import Mapping, Sequence
from pathlib import Path
from typing import overload

from lup.adapters.claude.runtime import (
    SUBMISSION_TOOL,
    ClaudeSandboxConfig,
    ClaudeSessionConfig,
    create_claude_session_factory,
)
from lup.adapters.claude.selection import CLAUDE_RUNTIME, claude_config
from lup.hooks import LupHooksConfig, create_tool_allowlist_hook, merge_hooks
from lup.mcp import McpServerEntry
from lup.runtime.config import ConfigTransform
from lup.runtime.factory import SessionFactory
from lup.runtime.models import TurnResult
from lup.runtime.selection import SessionAutonomy, SessionRequest
from lup.types import EnvVars, Usage
from pydantic import BaseModel

from aib.config import settings
from aib.paths import AGENT_CWD
from aib.profiles import profile_env
from aib.runtime import select_runtime

logger = logging.getLogger(__name__)

AUP_REFUSAL_PREFIX = "API Error: Claude Code is unable to respond to this request"


class AupRefusalError(Exception):
    """Anthropic content moderation refused the one_shot inference.

    Raised by one_shot when the result text matches the AUP refusal prefix.
    Callers should treat the failure as a hard stop rather than passing the
    refusal string back into agent context — doing so poisons later turns
    with the same content and triggers a refusal cascade.
    """


# ENABLE_TOOL_SEARCH: unset means the harness defers tool schemas once they
# exceed 10% of the context window, leaving the agent only tool *names* and a
# ToolSearch tool to load them. A search with the wrong terms returns nothing,
# so the agent concludes the capability does not exist and gives up without
# ever calling the tool. The research sub-agent carries ~35 data tools and sits
# well past that threshold, so every session must load schemas eagerly.
DEFAULT_ENV: dict[str, str] = {
    "ENABLE_TOOL_SEARCH": "false",
}

SESSION_EFFORT = "max"
"""How hard every session this project opens is asked to think.

Asked as a field rather than as `CLAUDE_CODE_EFFORT_LEVEL`, which only one
runtime reads: a portable request now carries effort, and an environment
variable naming one provider would have gone on quietly meaning nothing to
the other."""


SESSION_BUFFER_BYTES = 500 * 1024 * 1024
"""How much of one CLI message the transport will hold.

A tool result carrying a fetched page or a Wayback snapshot arrives as a
single frame, and the SDK's default ceiling is well under what one weighs."""


def session_env(profile: str | None) -> EnvVars:
    """The environment every session this project opens runs under.

    States which account to run as and leaves the rest to the runtime that
    opens the session. That runtime derives a configuration home private to
    this workspace under the one named here, so concurrent sessions do not
    read each other's half-written startup document — but which variable
    carries that home is its own to say, and deriving it here would have to
    pick a runtime before one was selected.
    """
    return {
        **settings.openrouter_env,
        **profile_env(profile),
        **DEFAULT_ENV,
    }


class ClaudeExtras(ConfigTransform[ClaudeSessionConfig]):
    """Session settings only Claude has a word for, stacked after rendering.

    A portable request states what both runtimes share. A bash sandbox, the
    roots a session may read outside its cwd, and the transport ceiling are
    not among them, and a request carrying them would be asking Codex for
    something it has no way to answer. Rendering first and transforming after
    is the seam lup leaves for exactly this, so the Claude-only half is
    additive rather than a second way to open a session.
    """

    def __init__(
        self,
        *,
        add_dirs: Sequence[Path] = (),
        sandbox: ClaudeSandboxConfig | None = None,
        max_buffer_size: int | None = SESSION_BUFFER_BYTES,
    ) -> None:
        self.add_dirs = list(add_dirs)
        self.sandbox = sandbox
        self.max_buffer_size = max_buffer_size

    def apply(self, config: ClaudeSessionConfig) -> ClaudeSessionConfig:
        """Return the rendered configuration with this project's extras on it."""
        return config.model_copy(
            update={
                "add_dirs": self.add_dirs,
                "sandbox": self.sandbox,
                "max_buffer_size": self.max_buffer_size,
            }
        )


def agent_request(
    *,
    model: str,
    system_prompt: str,
    autonomy: SessionAutonomy,
    allowed_tools: Sequence[str] = (),
    extra_hooks: LupHooksConfig | None = None,
    tool_servers: Mapping[str, McpServerEntry] | None = None,
    cwd: Path | None = None,
    max_thinking_tokens: int | None = None,
    profile: str | None = None,
) -> SessionRequest:
    """What a tool-using session this project opens asks for, portably.

    Autonomy is stated by the caller rather than defaulted, because it is the
    portable word for what a session may do to the world and no two of these
    sessions mean the same thing by it. Claude reads it as a permission mode
    and Codex as a sandbox, so a degree left to a default would be a sandbox
    nobody chose.

    `plan` is not among the degrees to reach for here. It is not a read-only
    permission but a mode that asks the model to present a plan instead of
    acting, and a session that must return a model never returns one.

    The allowlist and the hook enforcing it both travel as fields: Claude
    renders them, and Codex refuses them by design because the dispatcher
    generated into its harness tree is what governs a session there.

    The hook is built here rather than by the caller because bypassPermissions
    ignores the SDK's allowlist field, which leaves the hook as the only thing
    holding the line — and a structured turn is served by a submission tool the
    runtime installs, so an allowlist written without it denies the one tool
    the turn cannot finish without. Callers state the tools they want and pass
    anything further as `extra_hooks`.
    """
    resolved = AGENT_CWD if cwd is None else cwd
    resolved.mkdir(parents=True, exist_ok=True)
    tools = [*allowed_tools, SUBMISSION_TOOL]
    hooks = create_tool_allowlist_hook(tools)
    return SessionRequest(
        model=model,
        instructions=system_prompt,
        cwd=resolved,
        autonomy=autonomy,
        effort=SESSION_EFFORT,
        allowed_tools=tools,
        hooks=hooks if extra_hooks is None else merge_hooks(hooks, extra_hooks),
        tool_servers=dict(tool_servers or {}),
        max_thinking_tokens=max_thinking_tokens,
        environment=session_env(profile if profile is not None else settings.profile),
    )


def agent_session(
    request: SessionRequest,
    *,
    extras: ClaudeExtras | None = None,
    runtime: str | None = None,
) -> SessionFactory:
    """The configured factory the selected runtime answers this request with.

    Extras are shown to Claude and to nothing else: they are that runtime's
    own configuration, so offering them to another would be handing it a
    vocabulary it never agreed to.

    Containment is applied before either path, because the second renders the
    request itself rather than going through the selection — and a session
    opened with extras is as concurrent as one opened without.
    """
    selected = select_runtime(runtime)
    contained = selected.contained(request)
    if extras is None or selected is not CLAUDE_RUNTIME:
        return selected.session_factory(contained)
    return create_claude_session_factory(extras.apply(claude_config(contained)))


@overload
async def one_shot(
    prompt: str,
    *,
    model: str = ...,
    system_prompt: str = ...,
    cost_tool_name: str | None = ...,
    profile: str | None = ...,
    runtime: str | None = ...,
) -> str | None: ...


@overload
async def one_shot[T: BaseModel](
    prompt: str,
    *,
    model: str = ...,
    system_prompt: str = ...,
    output_type: type[T],
    cost_tool_name: str | None = ...,
    profile: str | None = ...,
    runtime: str | None = ...,
) -> T | None: ...


def one_shot_request(
    model: str, system_prompt: str, profile: str | None
) -> SessionRequest:
    """The session a tool-free inference asks for, in portable words.

    Tool-free is what makes this one portable at all: an empty allowlist is
    not an allowlist and no hooks are declared, so it is the one session shape
    this project opens that either runtime accepts unchanged.
    """
    AGENT_CWD.mkdir(parents=True, exist_ok=True)
    selected = profile if profile is not None else settings.profile
    return SessionRequest(
        model=model,
        instructions=system_prompt,
        cwd=AGENT_CWD,
        effort=SESSION_EFFORT,
        environment=session_env(selected),
    )


def spoken_text(result: TurnResult[BaseModel] | TurnResult[None]) -> str | None:
    """Everything a turn said, or None when it said nothing.

    Asked of `text_payload` rather than of the block kinds that hold text, so
    a runtime spelling its prose differently still reads here.
    """
    said = [
        block.text_payload for block in result.blocks if block.text_payload is not None
    ]
    return "".join(said) if said else None


def refuse_aup(text: str | None) -> str | None:
    """Raise when the text is a content-moderation refusal, else pass it on."""
    if text is not None and text.startswith(AUP_REFUSAL_PREFIX):
        raise AupRefusalError(text)
    return text


def record_cost(cost_tool_name: str | None, usage: Usage) -> None:
    """Attribute this turn's reported cost to the tool that spent it."""
    if cost_tool_name is None or usage.cost_usd is None:
        return
    from aib.tools.metrics import costs

    costs.record(cost_tool_name, usage.cost_usd)


async def one_shot(
    prompt: str,
    *,
    model: str = "sonnet",
    system_prompt: str = "",
    output_type: type[BaseModel] | None = None,
    cost_tool_name: str | None = None,
    profile: str | None = None,
    runtime: str | None = None,
) -> BaseModel | str | None:
    """One-shot prompt→result convenience wrapper.

    Without output_type: returns what the turn said.
    With output_type: returns the model the runtime submitted, which each
    serves its own way — Claude through a rendered output schema, Codex
    through a submission tool — and neither of which this has to know.
    """
    factory = select_runtime(runtime).session_factory(
        one_shot_request(model, system_prompt, profile)
    )
    if output_type is None:
        untyped = await factory.query(prompt)
        record_cost(cost_tool_name, untyped.usage)
        return refuse_aup(spoken_text(untyped))
    typed = await factory.query(prompt, output_type)
    record_cost(cost_tool_name, typed.usage)
    refuse_aup(spoken_text(typed))
    return typed.output
