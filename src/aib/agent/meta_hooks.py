"""PreToolUse hook for StructuredOutput.

Combines two concerns into a single hook to work around CLI bug #15897
(updatedInput is discarded when multiple PreToolUse hooks execute):

- Reviewer gate: Denies StructuredOutput until the reviewer passes.
- Unwrap: Fixes model hallucination where output is wrapped in {"parameter": {...}}.
"""

from __future__ import annotations

import logging
from typing import TYPE_CHECKING, Any

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.agent.hooks import HooksConfig

if TYPE_CHECKING:
    from aib.tools.reflection import ReviewState

logger = logging.getLogger(__name__)


def create_structured_output_hooks(
    review_state: ReviewState | None = None,
) -> HooksConfig:
    """Combined StructuredOutput hook: unwrap + optional reviewer gate.

    Must be the LAST PreToolUse hook registered to ensure updatedInput
    is not overwritten by subsequent hooks (CLI bug #15897).

    Args:
        review_state: Shared reviewer state. If set, StructuredOutput
            is denied until the reviewer passes. If None, gate is skipped.

    Returns:
        HooksConfig with a single PreToolUse hook.
    """

    async def pre_tool_use_hook(
        input_data: Any,
        _tool_use_id: str | None,
        _context: HookContext,
    ) -> dict[str, Any]:
        if input_data.get("hook_event_name") != "PreToolUse":
            return {}

        if input_data.get("tool_name") != "StructuredOutput":
            return {}

        hook_event = input_data["hook_event_name"]
        tool_input = input_data.get("tool_input", {})

        # --- Reviewer gate: deny until the reviewer has approved ---
        if review_state is not None and not review_state.passed:
            if review_state.last_verdict is None:
                reason = (
                    "You must call reflection(...) with your factors "
                    "and tentative estimate BEFORE providing your final "
                    "forecast. The reviewer must approve before you can "
                    "submit. Run reflection first, then call "
                    "StructuredOutput again."
                )
            else:
                reason = (
                    "The reviewer found errors in your forecast. "
                    "Address the findings from the last reflection() call, "
                    "then call reflection() again to get reviewer approval."
                )
            logger.warning(
                "Denying StructuredOutput — reviewer state: verdict=%s, passed=%s",
                review_state.last_verdict,
                review_state.passed,
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "deny",
                    "permissionDecisionReason": reason,
                }
            }

        # --- Unwrap {"parameter": {...}} wrapper ---
        if "parameter" in tool_input and isinstance(tool_input["parameter"], dict):
            unwrapped = tool_input["parameter"]
            logger.info(
                "Unwrapping StructuredOutput 'parameter' wrapper (%d fields)",
                len(unwrapped),
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                    "updatedInput": unwrapped,
                }
            }

        return {
            "hookSpecificOutput": {
                "hookEventName": hook_event,
                "permissionDecision": "allow",
            }
        }

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_use_hook])],  # type: ignore[list-item]
    }
