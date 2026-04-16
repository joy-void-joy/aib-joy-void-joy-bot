"""Centralized Agent SDK client creation.

All Agent SDK client construction goes through this module to ensure
consistent defaults (session persistence, OpenRouter routing).

Exports:
- REMOVE — sentinel to drop a single default from extra_args or env
- build_client(**kwargs) — AsyncContextManager[ClaudeSDKClient] with defaults
- one_shot(prompt, ...) — prompt→result convenience for tool-free LLM calls
"""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, cast, overload

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, ResultMessage
from pydantic import BaseModel

from aib.config import settings
from aib.paths import AGENT_CWD

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


DEFAULT_EXTRA_ARGS: dict[str, str | None] = {"no-session-persistence": None}
DEFAULT_ENV: dict[str, str] = {
    "CLAUDE_CODE_EFFORT_LEVEL": "max",
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
    *, defaults: bool = True, **kwargs: Any
) -> AsyncIterator[ClaudeSDKClient]:
    """Return a configured ClaudeSDKClient with project-wide defaults.

    Defaults (caller values win on conflict):
    - extra_args: no-session-persistence
    - env: openrouter routing, disable adaptive thinking, max effort

    Pass defaults=False to skip all defaults. Use REMOVE as a value
    to selectively drop a single default key.
    """
    from aib.agent.hooks import HooksConfig, merge_hooks
    from aib.agent.meta_hooks import create_structured_output_enforcement

    caller_extra = kwargs.pop("extra_args", None) or {}
    caller_env = kwargs.pop("env", None) or {}
    caller_hooks: HooksConfig = kwargs.pop("hooks", None) or cast(HooksConfig, {})

    if defaults:
        merged_extra = _merge(DEFAULT_EXTRA_ARGS, caller_extra)
        merged_env = _merge({**settings.openrouter_env, **DEFAULT_ENV}, caller_env)
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

    options = ClaudeAgentOptions(
        extra_args=merged_extra,
        env=merged_env,
        hooks=cast(Any, caller_hooks) if caller_hooks else None,
        max_buffer_size=500 * 1024 * 1024,
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
) -> str | None: ...


@overload
async def one_shot[T: BaseModel](
    prompt: str,
    *,
    model: str = ...,
    system_prompt: str = ...,
    output_type: type[T],
    cost_tool_name: str | None = ...,
) -> T | None: ...


async def one_shot(
    prompt: str,
    *,
    model: str = "sonnet",
    system_prompt: str = "",
    output_type: type[BaseModel] | None = None,
    cost_tool_name: str | None = None,
) -> BaseModel | str | None:
    """One-shot prompt→result convenience wrapper.

    Without output_type: returns ResultMessage.result (str).
    With output_type: sets output_format to JSON schema, returns validated model.
    """
    extra_kwargs: dict[str, Any] = {}
    if output_type is not None:
        extra_kwargs["output_format"] = {
            "type": "json_schema",
            "schema": output_type.model_json_schema(),
        }

    structured_output: dict[str, Any] | None = None
    result_text: str | None = None

    async with build_client(
        model=model,
        system_prompt=system_prompt,
        allowed_tools=[],
        **extra_kwargs,
    ) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, ResultMessage):
                structured_output = message.structured_output
                result_text = message.result
                if cost_tool_name and message.total_cost_usd is not None:
                    from aib.tools.metrics import get_collector

                    get_collector().record_cost(cost_tool_name, message.total_cost_usd)

    if result_text and result_text.startswith(AUP_REFUSAL_PREFIX):
        raise AupRefusalError(result_text)

    if output_type is not None:
        if structured_output:
            return output_type.model_validate(structured_output)
        return None
    return result_text
