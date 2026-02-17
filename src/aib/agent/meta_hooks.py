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


def create_structured_output_hooks(meta_path: Path | None = None) -> HooksConfig:
    """Combined StructuredOutput hook: unwrap + optional meta-gate.

    Must be the LAST PreToolUse hook registered to ensure updatedInput
    is not overwritten by subsequent hooks (CLI bug #15897).

    Args:
        meta_path: Path to meta.md. If set, StructuredOutput is denied
            until this file exists. If None, meta-gate is skipped.

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

        # --- Meta-gate: deny until meta-reflection exists ---
        if meta_path is not None and not meta_path.exists():
            logger.warning(
                "Denying StructuredOutput — meta-reflection not yet written at %s",
                meta_path,
            )
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "deny",
                    "permissionDecisionReason": (
                        "You must write a meta-reflection using "
                        "write_meta(content='...') BEFORE providing "
                        "your final forecast. Write your meta-reflection first, "
                        "then call StructuredOutput again."
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
