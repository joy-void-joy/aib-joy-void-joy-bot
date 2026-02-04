"""Type-safe hook configuration for the Claude Agent SDK.

Provides typed alternatives to dict[str, Any] for hook configuration,
enabling better type checking and IDE support.
"""

from typing import Literal, TypedDict

from claude_agent_sdk import HookMatcher

# All hook event types supported by the Claude Agent SDK
HookEventType = Literal[
    "PreToolUse",
    "PostToolUse",
    "PostToolUseFailure",
    "UserPromptSubmit",
    "Stop",
    "SubagentStop",
    "PreCompact",
]


class HooksConfig(TypedDict, total=False):
    """Typed hook configuration for ClaudeAgentOptions.

    Each key is a hook event type, and the value is a list of HookMatcher
    instances that will be invoked for that event.

    Example:
        hooks: HooksConfig = {
            "PreToolUse": [HookMatcher(hooks=[my_pre_hook])],
            "PostToolUse": [HookMatcher(hooks=[my_post_hook])],
        }
    """

    PreToolUse: list[HookMatcher]
    PostToolUse: list[HookMatcher]
    PostToolUseFailure: list[HookMatcher]
    UserPromptSubmit: list[HookMatcher]
    Stop: list[HookMatcher]
    SubagentStop: list[HookMatcher]
    PreCompact: list[HookMatcher]


def merge_hooks(base: HooksConfig, additional: HooksConfig) -> HooksConfig:
    """Merge two hook configurations.

    For each hook event type, combines the matchers from both configs.
    Base hooks run first, then additional hooks.

    Args:
        base: The base hook configuration.
        additional: Hook configuration to merge into base.

    Returns:
        New HooksConfig with combined matchers.

    Example:
        permission_hooks = create_permission_hooks(...)
        retrodict_hooks = create_retrodict_hooks(...)
        combined = merge_hooks(permission_hooks, retrodict_hooks)
    """
    # Start with a copy of base
    merged: HooksConfig = dict(base)  # type: ignore[assignment]

    # Merge in additional hooks
    for event in additional:
        if event in merged:
            # Combine matchers for the same event (base runs first)
            merged[event] = merged[event] + additional[event]  # type: ignore[literal-required]
        else:
            merged[event] = additional[event]  # type: ignore[literal-required]

    return merged
