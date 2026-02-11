"""PreToolUse hook that gates StructuredOutput behind meta-reflection.

Denies StructuredOutput until meta.md exists on disk, forcing the agent
to call notes(write_meta) before providing its final forecast.
"""

import logging
from pathlib import Path
from typing import Any

from claude_agent_sdk import HookMatcher
from claude_agent_sdk.types import HookContext

from aib.agent.hooks import HooksConfig

logger = logging.getLogger(__name__)


def create_meta_gate_hooks(meta_path: Path) -> HooksConfig:
    """Create PreToolUse hook that denies StructuredOutput until meta-reflection exists.

    Args:
        meta_path: Expected path to meta.md (varies by retrodict mode).

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

        if meta_path.exists():
            return {
                "hookSpecificOutput": {
                    "hookEventName": hook_event,
                    "permissionDecision": "allow",
                }
            }

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
                    "notes(mode='write_meta', content='...') BEFORE providing "
                    "your final forecast. Write your meta-reflection first, "
                    "then call StructuredOutput again."
                ),
            }
        }

    return {
        "PreToolUse": [HookMatcher(hooks=[pre_tool_use_hook])],  # type: ignore[list-item]
    }
