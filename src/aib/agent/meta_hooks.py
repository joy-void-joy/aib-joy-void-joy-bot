"""PreToolUse hook for StructuredOutput.

Combines two concerns into a single hook to work around CLI bug #15897
(updatedInput is discarded when multiple PreToolUse hooks execute):

- Reviewer gate: Denies StructuredOutput until the reviewer passes.
- Unwrap: Fixes model hallucination where output is wrapped in {"parameter": {...}}.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING

from lup.hooks import (
    LupHookInput,
    LupHookMatcher,
    LupHookOutput,
    LupHooksConfig,
    allow_hook,
    block_hook,
    deny_hook,
)

if TYPE_CHECKING:
    from aib.agent.session import ReviewState

logger = logging.getLogger(__name__)


def create_structured_output_hooks(
    review_state: ReviewState | None = None,
) -> LupHooksConfig:
    """Combined StructuredOutput hook: unwrap + optional reviewer gate.

    Must be the LAST PreToolUse hook registered to ensure updated input
    is not overwritten by subsequent hooks (CLI bug #15897).

    Args:
        review_state: Shared reviewer state. If set, StructuredOutput
            is denied until the reviewer passes. If None, gate is skipped.

    Returns:
        LupHooksConfig with a single PreToolUse hook.
    """

    async def pre_tool_use_hook(event: LupHookInput) -> LupHookOutput:
        if event.event != "PreToolUse":
            return LupHookOutput()

        if event.tool_name != "StructuredOutput":
            return LupHookOutput()

        # --- Gate: deny until reflection + premortem have both run ---
        if review_state is not None and not (
            review_state.reflection_done and review_state.passed
        ):
            if not review_state.reflection_done:
                reason = (
                    "You must call reflection(...) with your factors and "
                    "tentative estimate BEFORE providing your final forecast. "
                    "Run reflection first to commit your evidence, then call "
                    "premortem() with your adversarial self-examination, "
                    "then call StructuredOutput."
                )
            elif review_state.last_verdict is None:
                reason = (
                    "You called reflection() but haven't called premortem() "
                    "yet. Call premortem() now with your counterargument, "
                    "what_would_change_my_mind, and confidence_in_estimate. "
                    "The reviewer must approve before you can submit."
                )
            else:
                reason = (
                    "The premortem reviewer found errors in your forecast. "
                    "Address the findings from the last premortem() call, "
                    "update your factors via reflection() if needed, then "
                    "call premortem() again to get reviewer approval."
                )
            logger.warning(
                "Denying StructuredOutput — reflection_done=%s, verdict=%s, passed=%s",
                review_state.reflection_done,
                review_state.last_verdict,
                review_state.passed,
            )
            return deny_hook(reason)

        # --- Unwrap {"parameter": {...}} wrapper ---
        # lup: ignore[dict-get] — the agent's raw tool arguments off the wire
        wrapper = event.tool_input.get("parameter")
        if isinstance(wrapper, dict):
            logger.info(
                "Unwrapping StructuredOutput 'parameter' wrapper (%d fields)",
                len(wrapper),
            )
            return LupHookOutput(decision="allow", updated_input=wrapper)

        return allow_hook()

    return LupHooksConfig(
        pre_tool_use=[
            LupHookMatcher(hook=pre_tool_use_hook, tag="structured_output_gate")
        ],
    )


def create_structured_output_enforcement() -> LupHooksConfig:
    """Block the Stop event until StructuredOutput has been called.

    Pairs with output_format=json_schema on ClaudeAgentOptions. The SDK
    exposes StructuredOutput as a tool but does not enforce that the
    agent calls it before ending the turn. When the agent writes its
    answer as a TextBlock and stops, ResultMessage.structured_output is
    None and the caller has to decide whether to soft-fail or crash.

    This hook pair tracks StructuredOutput invocations via PostToolUse
    and blocks Stop with a feedback reason if the tool was never called.
    stop_hook_active guards against infinite loops: on the second Stop
    we let the agent through so the caller's structured_output=None
    handling remains the final backstop.
    """
    state = {"called": False}

    async def post_tool_use(event: LupHookInput) -> LupHookOutput:
        if event.event == "PostToolUse" and event.tool_name == "StructuredOutput":
            state["called"] = True
        return LupHookOutput()

    async def stop_hook(event: LupHookInput) -> LupHookOutput:
        if event.event != "Stop":
            return LupHookOutput()
        if state["called"] or event.stop_hook_active:
            return LupHookOutput()
        logger.warning(
            "Blocking Stop — agent ended turn without calling StructuredOutput"
        )
        return block_hook(
            "You ended your turn without calling the StructuredOutput "
            "tool. Your response format requires it. Call "
            "StructuredOutput now with your complete findings. Do not "
            "write the answer as prose text — only the StructuredOutput "
            "call is read by the caller."
        )

    return LupHooksConfig(
        post_tool_use=[
            LupHookMatcher(hook=post_tool_use, tag="structured_output_seen")
        ],
        stop=[LupHookMatcher(hook=stop_hook, tag="structured_output_required")],
    )
