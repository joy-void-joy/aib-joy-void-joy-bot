"""Test whether the Claude API model knows the real date despite system prompt.

Instantiates ClaudeSDKClient with the same system prompt template used in
retrodict mode (with a fake date substituted). Asks the model what today's
date is and prints the response.

This tests the API's inference-time date injection, which is independent of
the system prompt. If the model reports the real date instead of the fake
date, it confirms that the API leaks temporal information.

Usage:
    uv run python .claude/plugins/aib/scripts/test_date_awareness.py
    uv run python .claude/plugins/aib/scripts/test_date_awareness.py --date 2025-06-15
"""

import asyncio
from datetime import date
from pathlib import Path

import typer
from claude_agent_sdk import ClaudeAgentOptions, ClaudeSDKClient
from claude_agent_sdk.types import AssistantMessage, ResultMessage, TextBlock

from aib.config import settings

PRESET_TEMPLATE = (
    Path(__file__).parents[4] / "src" / "aib" / "agent" / "claude_code_preset.txt"
).read_text()


def build_system_prompt(fake_date: date) -> str:
    return PRESET_TEMPLATE.replace("{{DATE}}", fake_date.isoformat()).replace(
        "{{WORKING_DIRECTORY}}", str(Path.cwd())
    )


async def run_test(fake_date: date) -> None:
    system_prompt = build_system_prompt(fake_date)
    print(f"Model:        {settings.model}")
    print(f"System date:  {fake_date.isoformat()}")
    print(f"Real date:    {date.today().isoformat()}")
    print("─" * 40)

    options = ClaudeAgentOptions(
        model=settings.model,
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
                            response = block.text.strip()
                            print(f"Model says:   {response}")

                            if fake_date.isoformat() in response:
                                print("✅ Model reported the FAKE date (system prompt)")
                            elif date.today().isoformat() in response:
                                print(
                                    "⚠️  Model reported the REAL date "
                                    "(API leaks date despite system prompt)"
                                )
                            else:
                                print("❓ Model reported an unexpected date")
                case ResultMessage():
                    break


app = typer.Typer()


@app.command()
def main(
    fake_date: str = typer.Option(
        "1999-12-31",
        "--date",
        "-d",
        help="Fake date to inject into system prompt (YYYY-MM-DD)",
    ),
) -> None:
    """Test whether the model knows the real date despite system prompt."""
    parsed = date.fromisoformat(fake_date)
    asyncio.run(run_test(parsed))


if __name__ == "__main__":
    app()
