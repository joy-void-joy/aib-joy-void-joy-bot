"""Test whether the agent uses the real date or the system prompt date.

Three tests:
1. Direct question: "What's today's date?" (no tools)
2. Reasoning question: "What published_before would you use?" (no tools)
3. Bash date: Does the system clock leak the real date? (with tools)

Each test creates a fresh agent with a fake date of 2025-06-15.
"""

import asyncio
from datetime import date
from pathlib import Path

from claude_agent_sdk import ClaudeSDKClient, ClaudeAgentOptions
from claude_agent_sdk.types import (
    AssistantMessage,
    ResultMessage,
    TextBlock,
    ToolUseBlock,
    ToolResultBlock,
)

PRESET_TEMPLATE = (
    Path(__file__).parents[4] / "src" / "aib" / "agent" / "claude_code_preset.txt"
).read_text()
FAKE_DATE = date(2025, 6, 15)
REAL_DATE = date.today()


def build_system_prompt() -> str:
    return PRESET_TEMPLATE.replace("{{DATE}}", FAKE_DATE.isoformat()).replace(
        "{{WORKING_DIRECTORY}}", str(Path.cwd())
    )


async def run_test(name: str, prompt: str, tools: list[str] | None = None) -> None:
    print(f"\n{'=' * 60}")
    print(f"TEST: {name}")
    print(f"System prompt date: {FAKE_DATE.isoformat()}")
    print(f"Real date:          {REAL_DATE.isoformat()}")
    print(f"{'=' * 60}")

    options = ClaudeAgentOptions(
        model="claude-sonnet-4-5-20250929",
        system_prompt=build_system_prompt(),
        max_thinking_tokens=1024,
        permission_mode="bypassPermissions",
        tools=tools or [],
        max_turns=3,
        extra_args={"no-session-persistence": None},
    )

    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            match message:
                case AssistantMessage():
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            print(f"  Agent: {block.text}")
                        elif isinstance(block, ToolUseBlock):
                            print(f"  Tool:  {block.name}({block.input})")
                        elif isinstance(block, ToolResultBlock):
                            content = block.content
                            if isinstance(content, str):
                                print(f"  Result: {content[:200]}")
                            elif isinstance(content, list):
                                for b in content:
                                    if isinstance(b, dict) and "text" in b:
                                        print(f"  Result: {b['text'][:200]}")
                case ResultMessage():
                    break


async def main() -> None:
    # Test 1: Direct date question (no tools)
    await run_test(
        "Direct date (no tools)",
        "What is today's date? Reply with ONLY the date in YYYY-MM-DD format.",
    )

    # Test 2: Reasoning about published_before (no tools)
    await run_test(
        "Published_before reasoning (no tools)",
        "If you were searching for the latest news and needed to set a "
        "'published_before' date filter to include everything up to today, "
        "what date would you use? Reply with ONLY the YYYY-MM-DD date.",
    )

    # Test 3: Bash date command (with Bash tool)
    await run_test(
        "Bash date command (with Bash tool)",
        "Run `date +%Y-%m-%d` using the Bash tool, then tell me: "
        "does the system date match what you believe today's date is? "
        "Reply with the system date and your believed date.",
        tools=["Bash"],
    )

    print(f"\n{'=' * 60}")
    print(f"EXPECTED (fake): {FAKE_DATE.isoformat()}")
    print(f"REAL:            {REAL_DATE.isoformat()}")
    print(f"{'=' * 60}")


if __name__ == "__main__":
    asyncio.run(main())
