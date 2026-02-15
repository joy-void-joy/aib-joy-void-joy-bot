"""Integration tests for date leak detection in retrodict mode.

Tests whether the Claude Agent SDK / API injects the real date into the
system prompt, overriding the fake retrodict date. This matters because
retrodiction forecasts must believe they are in the past.

Requires API keys. Each test creates a fresh agent with a fake date and
asks it what date it thinks today is.
"""

import asyncio
from datetime import date
from pathlib import Path

import pytest
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from claude_agent_sdk.types import AssistantMessage, ResultMessage, TextBlock

pytestmark = pytest.mark.integration

PRESET_TEMPLATE = (Path(__file__).parents[2] / "src" / "aib" / "agent" / "claude_code_preset.txt").read_text()
FAKE_DATE = date(1999, 12, 31)


def _build_system_prompt(fake_date: date) -> str:
    return PRESET_TEMPLATE.replace("{{DATE}}", fake_date.isoformat()).replace(
        "{{WORKING_DIRECTORY}}", str(Path.cwd())
    )


async def _ask_agent(prompt: str, tools: list[str] | None = None, max_turns: int = 1) -> str:
    """Run a single query against an agent with a fake date and return text response."""
    options = ClaudeAgentOptions(
        model="claude-sonnet-4-5-20250929",
        system_prompt=_build_system_prompt(FAKE_DATE),
        max_thinking_tokens=1024,
        permission_mode="bypassPermissions",
        tools=tools or [],
        max_turns=max_turns,
        extra_args={"no-session-persistence": None},
    )

    texts: list[str] = []
    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            match message:
                case AssistantMessage():
                    for block in message.content:
                        if isinstance(block, TextBlock):
                            texts.append(block.text.strip())
                case ResultMessage():
                    break

    return " ".join(texts)


def test_direct_date_question() -> None:
    """Model should report the fake date, not the real one."""
    response = asyncio.run(
        _ask_agent("What is today's date? Reply with ONLY the date in YYYY-MM-DD format.")
    )

    real_date = date.today().isoformat()
    fake_date = FAKE_DATE.isoformat()

    assert real_date not in response, (
        f"Model reported real date {real_date} instead of fake date {fake_date}"
    )


def test_published_before_reasoning() -> None:
    """Model should reason about dates using the fake date."""
    response = asyncio.run(
        _ask_agent(
            "If you were searching for the latest news and needed to set a "
            "'published_before' date filter to include everything up to today, "
            "what date would you use? Reply with ONLY the YYYY-MM-DD date."
        )
    )

    real_date = date.today().isoformat()
    assert real_date not in response, (
        f"Model used real date {real_date} for reasoning"
    )


def test_bash_date_with_tools() -> None:
    """With Bash tool, system clock may leak the real date."""
    response = asyncio.run(
        _ask_agent(
            "Run `date +%Y-%m-%d` using the Bash tool, then tell me: "
            "does the system date match what you believe today's date is? "
            "Reply with the system date and your believed date.",
            tools=["Bash"],
            max_turns=3,
        )
    )

    assert len(response) > 0, "Agent returned empty response"
