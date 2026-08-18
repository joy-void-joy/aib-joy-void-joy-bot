"""Centralized Agent SDK client creation.

All Agent SDK client construction goes through this module to ensure
consistent defaults (configuration home, OpenRouter routing).

Exports:
- REMOVE — sentinel to drop a single default from env
- build_client(**kwargs) — AsyncContextManager[ClaudeSDKClient] with defaults
- one_shot(prompt, ...) — prompt→result convenience for tool-free LLM calls
"""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, overload

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from claude_agent_sdk.types import McpSdkServerConfig
from lup.adapters.claude.config_home import workspace_config_environment
from lup.mcp import LupMcpServerConfig
from lup.runtime.models import TurnResult
from lup.runtime.selection import SessionRequest
from lup.types import EnvVars, Usage
from pydantic import BaseModel

from aib.config import settings
from aib.paths import AGENT_CWD
from aib.profiles import profile_env
from aib.runtime import select_runtime

logger = logging.getLogger(__name__)

REMOVE = object()

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

    The configuration home is derived per workspace rather than shared, so
    concurrent sessions do not read each other's half-written startup
    document, and what one writes stays inside its own folder. Derived under
    whichever home the selected profile names, so the account is still the
    profile's to decide.
    """
    return {
        **settings.openrouter_env,
        **workspace_config_environment(profile_env(profile), AGENT_CWD),
        **DEFAULT_ENV,
    }


def _merge(defaults: dict[str, Any], overrides: dict[str, Any]) -> dict[str, Any]:
    merged = {**defaults, **overrides}
    return {k: v for k, v in merged.items() if v is not REMOVE}


def _find_format_path(schema: object, path: str = "") -> str | None:
    """Return the JSON path of the first `format` key found, or None."""
    if isinstance(schema, dict):
        if "format" in schema:
            return f"{path}.format" if path else "format"
        for key, value in schema.items():
            sub_path = f"{path}.{key}" if path else key
            found = _find_format_path(value, sub_path)
            if found is not None:
                return found
    elif isinstance(schema, list):
        for i, item in enumerate(schema):
            found = _find_format_path(item, f"{path}[{i}]")
            if found is not None:
                return found
    return None


def reject_ajv_unsafe_schema(schema: object) -> None:
    """Raise ValueError if schema contains a `format` field.

    The bundled Claude Code CLI compiles output_format json_schemas via
    Ajv in strict mode. Strict-mode Ajv rejects any schema containing a
    `format` keyword it does not have a validator registered for, and
    the bundled CLI does not register any format validators. When the
    schema is rejected, StructuredOutput is silently NOT added to the
    agent's tool list — the agent then has no way to finalize its
    response, writes the answer as prose, and hits the Stop hook
    enforcement (or silently produces no structured output).

    Pydantic emits `"format": "date"` / `"format": "date-time"` /
    `"format": "email"` / etc. for typed fields like `date`, `datetime`,
    `EmailStr`, etc. Use `str` with a `Field(description=...)` instead.
    """
    offending = _find_format_path(schema)
    if offending is not None:
        raise ValueError(
            f"output_format json_schema contains `format` at {offending!r}. "
            "The Claude Code CLI's Ajv compiler silently rejects schemas "
            "with format keywords in strict mode, which prevents "
            "StructuredOutput from being registered at all. Replace the "
            "Pydantic `date`/`datetime`/`EmailStr`/etc. field with `str` "
            "and document the expected format via `Field(description=...)`. "
            "See memory/bug_json_schema_date_format.md."
        )


@asynccontextmanager
async def build_client(
    *, defaults: bool = True, profile: str | None = None, **kwargs: Any
) -> AsyncIterator[ClaudeSDKClient]:
    """Return a configured ClaudeSDKClient with project-wide defaults.

    Defaults (caller values win on conflict):
    - env: openrouter routing, a per-workspace configuration home, eager
      tool schemas

    `profile` names a Claude account from the registry, falling back to
    settings.profile. Passing it per call rather than through the process
    environment is what lets concurrent sessions run on different accounts.

    Pass defaults=False to skip all defaults. Use REMOVE as a value
    to selectively drop a single default key.
    """
    from lup.adapters.claude.hooks import lup_hooks_to_claude
    from lup.hooks import LupHooksConfig, merge_hooks

    from aib.agent.meta_hooks import create_structured_output_enforcement

    caller_extra = kwargs.pop("extra_args", None) or {}
    caller_env = kwargs.pop("env", None) or {}
    caller_hooks: LupHooksConfig = kwargs.pop("hooks", None) or LupHooksConfig()

    if defaults:
        merged_extra = _merge({}, caller_extra)
        selected = profile if profile is not None else settings.profile
        merged_env = _merge(session_env(selected), caller_env)
    else:
        merged_extra = {k: v for k, v in caller_extra.items() if v is not REMOVE}
        merged_env = {k: v for k, v in caller_env.items() if v is not REMOVE}

    output_format = kwargs.get("output_format")
    if isinstance(output_format, dict) and output_format.get("type") == "json_schema":
        reject_ajv_unsafe_schema(output_format.get("schema"))
        caller_hooks = merge_hooks(create_structured_output_enforcement(), caller_hooks)

    if "cwd" not in kwargs:
        AGENT_CWD.mkdir(parents=True, exist_ok=True)
        kwargs["cwd"] = str(AGENT_CWD)

    if "setting_sources" not in kwargs:
        kwargs["setting_sources"] = []

    if "effort" not in kwargs:
        kwargs["effort"] = SESSION_EFFORT

    # The one place lup's neutral server configs become the SDK's own shape.
    # It has to be here, at the boundary, and nowhere earlier:
    # `server_tool_names` reads `tool_names` off a `LupMcpServerConfig` and
    # answers `[]` for anything already projected, so projecting sooner
    # would silently empty the hook-enforced tool allowlist.
    if "mcp_servers" in kwargs:
        kwargs["mcp_servers"] = {
            name: (
                McpSdkServerConfig(type="sdk", name=cfg.name, instance=cfg.server)
                if isinstance(cfg, LupMcpServerConfig)
                else cfg
            )
            for name, cfg in kwargs["mcp_servers"].items()
        }

    options = ClaudeAgentOptions(
        extra_args=merged_extra,
        env=merged_env,
        # The hook seam's other projection point, beside mcp_servers above:
        # every factory speaks lup's normalized (LupHookInput) -> LupHookOutput
        # shape, and the adapter renders it into the SDK's native matchers.
        hooks=lup_hooks_to_claude(caller_hooks) if caller_hooks.by_event() else None,
        max_buffer_size=SESSION_BUFFER_BYTES,
        **kwargs,
    )
    async with ClaudeSDKClient(options=options) as client:
        yield client


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
