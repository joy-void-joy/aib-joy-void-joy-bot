"""What `ask` does to a session with nobody in front of it.

`ask` is Claude's `default`, where a tool call raises a permission request.
Every session this project opens is programmatic, so there is nobody to
answer one — which makes two questions decide whether the degree is usable
here at all, and neither is answered by the roster probe beside this file.

The first is whether a tool the request auto-approves still runs. That is
what `allowed_tools` is documented to do, and it is the field this project
was using as a roster; if it works at `ask`, it has a real job rather than
none. It is asked of an MCP tool specifically, because seven of the eight
sessions here do their work through MCP servers rather than built-ins, and
the roster field does not reach those at all.

The second is what happens to a tool that is *not* auto-approved. Denied is
a governed session. Hung is a forecast that never returns, and a degree that
hangs is not a safer degree — so this distinguishes the two rather than
assuming the good one.
"""

from pathlib import Path

import pytest
from lup.mcp import McpServerEntry, create_mcp_server, lup_tool
from lup.runtime.selection import SessionRequest
from pydantic import BaseModel, Field

from aib.agent.client import agent_session, session_env

pytestmark = pytest.mark.integration

SECRET = "hydrangea"


class WordInput(BaseModel):
    """No input: the tool answers the same way however it is called."""


class WordOutput(BaseModel):
    """The word only this tool knows."""

    word: str = Field(description="The secret word.")


@lup_tool("Return the secret word. The only way to learn it.", name="secret_word")
async def secret_word(_: WordInput) -> WordOutput:
    """Answer with the word no model can guess."""
    return WordOutput(word=SECRET)


SERVER: dict[str, McpServerEntry] = {
    "probe": create_mcp_server("probe", tools=[secret_word])
}
SECRET_TOOL = "mcp__probe__secret_word"


def ask_request(allowed: list[str], cwd: Path) -> SessionRequest:
    """One `ask` session auto-approving exactly these tools."""
    return SessionRequest(
        model="haiku",
        instructions="Answer the question using the tools you have.",
        cwd=cwd,
        autonomy="ask",
        tools=["Read"],
        allowed_tools=allowed,
        tool_servers=SERVER,
        environment=session_env(None),
    )


async def spoken_at_ask(allowed: list[str], prompt: str, cwd: Path) -> str:
    """Everything one `ask` session said, having tried to use its tools."""
    factory = agent_session(ask_request(allowed, cwd), runtime="claude")
    result = await factory.query(prompt)
    return "".join(
        block.text_payload for block in result.blocks if block.text_payload is not None
    )


async def test_an_auto_approved_tool_runs_with_nobody_to_ask(tmp_path: Path) -> None:
    """`allowed_tools` earns its place at this degree: the tool it names runs
    without a prompt, and it reaches an MCP tool, which is where the work of
    almost every session here actually happens."""
    said = await spoken_at_ask(
        [SECRET_TOOL], "Call the secret_word tool and tell me the word.", tmp_path
    )

    assert SECRET in said.lower()


async def test_a_tool_outside_the_list_is_refused_rather_than_left_hanging(
    tmp_path: Path,
) -> None:
    """The failure mode that would matter. A denial is a governed session; a
    turn that never returns is a forecast lost to a question nobody heard."""
    said = await spoken_at_ask(
        [], "Call the secret_word tool and tell me the word.", tmp_path
    )

    assert SECRET not in said.lower()
