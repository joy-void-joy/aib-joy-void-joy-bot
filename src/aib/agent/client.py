"""Centralized Agent SDK client creation.

All Agent SDK client construction goes through this module to ensure
consistent defaults (session persistence, OpenRouter routing).

Two exports:
- build_client(**kwargs) — AsyncContextManager[ClaudeSDKClient] with defaults
- one_shot(prompt, ...) — prompt→result convenience for tool-free LLM calls
"""

import logging
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any, overload

from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient, ResultMessage
from pydantic import BaseModel

from aib.config import settings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def build_client(**kwargs: Any) -> AsyncIterator[ClaudeSDKClient]:
    """Return a configured ClaudeSDKClient with project-wide defaults.

    Always injects (merged with caller values, caller wins on conflict):
    - extra_args={"no-session-persistence": None}
    - env=settings.openrouter_env
    """
    caller_extra = kwargs.pop("extra_args", None) or {}
    merged_extra = {"no-session-persistence": None, **caller_extra}

    caller_env = kwargs.pop("env", None) or {}
    merged_env = {**settings.openrouter_env, **caller_env}

    options = ClaudeAgentOptions(
        extra_args=merged_extra,
        env=merged_env,
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
) -> str | None: ...


@overload
async def one_shot[T: BaseModel](
    prompt: str,
    *,
    model: str = ...,
    system_prompt: str = ...,
    output_type: type[T],
) -> T | None: ...


async def one_shot(
    prompt: str,
    *,
    model: str = "sonnet",
    system_prompt: str = "",
    output_type: type[BaseModel] | None = None,
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

    if output_type is not None:
        if structured_output:
            return output_type.model_validate(structured_output)
        return None
    return result_text
