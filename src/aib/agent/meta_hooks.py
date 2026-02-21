"""PreToolUse hook for StructuredOutput.

Combines two concerns into a single hook to work around CLI bug #15897
(updatedInput is discarded when multiple PreToolUse hooks execute):

- Meta-gate: Denies StructuredOutput until meta.md exists on disk.
- Unwrap: Fixes model hallucination where output is wrapped in {"parameter": {...}}.
"""

import logging
from pathlib import Path
from typing import Any

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.agent.hooks import HooksConfig

logger = logging.getLogger(__name__)


def create_structured_output_hooks(reflection_path: Path | None = None) -> HooksConfig:
    """Combined StructuredOutput hook: unwrap + optional reflection gate.

    Must be the LAST PreToolUse hook registered to ensure updatedInput
    is not overwritten by subsequent hooks (CLI bug #15897).

    Args:
        reflection_path: Path to reflection.yaml. If set, StructuredOutput
            is denied until this file exists. If None, gate is skipped.

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

        # --- Reflection gate: deny until reflection has been called ---
        if reflection_path is not None and not reflection_path.exists():
            logger.warning(
                "Denying StructuredOutput — reflection not yet written at %s",
                reflection_path,
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        "You must call reflection(...) with your factors "
                        "and tentative estimate BEFORE providing your final "
                        "forecast. Run your reflection first, then call "
                        "StructuredOutput again."
                    ),
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
