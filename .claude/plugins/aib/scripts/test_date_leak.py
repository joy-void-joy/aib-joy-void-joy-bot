"""Test whether the Agent SDK injects the real date into the system prompt.

Creates an agent using the same preset template and options as the forecasting
agent, but with a fake retrodict date of 1999-12-31. Then asks it what date
it thinks today is.
"""

import asyncio
from datetime import date
from pathlib import Path

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
from claude_agent_sdk.types import AssistantMessage, ResultMessage, TextBlock

PRESET_TEMPLATE = (
    Path(__file__).parents[4] / "src" / "aib" / "agent" / "claude_code_preset.txt"
).read_text()
FAKE_DATE = date(1999, 12, 31)


def build_system_prompt() -> str:
    return PRESET_TEMPLATE.replace("{{DATE}}", FAKE_DATE.isoformat()).replace(
        "{{WORKING_DIRECTORY}}", str(Path.cwd())
    )


async def main() -> None:
    system_prompt = build_system_prompt()
    print(f"System prompt date: {FAKE_DATE.isoformat()}")
    print(f"Real date: {date.today().isoformat()}")
    print("---")

    options = ClaudeAgentOptions(
        model="claude-sonnet-4-5-20250929",
        system_prompt=system_prompt,
        max_thinking_tokens=1024,
        permission_mode="bypassPermissions",
        tools=[],
        max_turns=1,
        extra_args={"no-session-persistence": None},
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query(
            "What is today's date? Reply with ONLY the date in YYYY-MM-DD format."
        )
        async for message in client.receive_response():
            match message:
                case AssistantMessage():
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"Agent says: {block.text}")
                case ResultMessage():
                    break


if __name__ == "__main__":
    asyncio.run(main())
