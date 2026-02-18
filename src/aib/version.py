"""Agent version tracking.

AGENT_VERSION tracks the forecasting agent's behavior — prompts, tools,
tools, scoring logic. Bump this when agent behavior changes, NOT
for data commits, dependency updates, or infrastructure changes.

Bump rules:
- Patch (0.3.x): bug fixes, config tweaks, tool fixes
- Minor (0.x.0): prompt changes, new tools, tool modifications
- Major (x.0.0): architecture changes (new LLM, new framework)
"""

AGENT_VERSION = "1.3.0"
