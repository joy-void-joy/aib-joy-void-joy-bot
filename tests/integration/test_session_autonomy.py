"""What each degree of autonomy does to a session that must answer.

Every session this project opens programmatically ends in a structured
answer, and most of them are opened with no human in front of them. So the
question a degree of autonomy has to survive here is not "what may it reach"
but "does it still answer" — and the two are not the same question, because
Claude spells two of the four degrees as modes that change what the model is
asked to do rather than only what it is allowed to do.

`plan` is the one to doubt. It is not a read-only permission: it puts the
session in plan mode, where the model is instructed to research and then
present a plan for approval instead of acting. A sub-agent whose whole job is
to return a model would be derailed by that, and the failure would arrive as
a forecast missing its review rather than as an error.

`ask` is the second. It is Claude's `default`, where a tool outside the
auto-approval list raises a permission request — and an unattended session
has nothing to answer one with.

Pinned as tests because the cost of guessing is a session that reads
correctly and returns nothing, which no static gate reports.
"""

from pathlib import Path

import pytest
from lup.runtime.selection import SessionAutonomy, SessionRequest
from pydantic import BaseModel, Field

from aib.agent.client import agent_session, session_env

pytestmark = pytest.mark.integration

SECRET = "hydrangea"
"""A word the model cannot answer with unless it actually read the file."""


class Answer(BaseModel):
    """The smallest structured answer a session can be asked for."""

    word: str = Field(description="The word found in the file.")


def autonomy_probe_request(autonomy: SessionAutonomy, cwd: Path) -> SessionRequest:
    """One read-only session at this degree, asked for a structured answer.

    The roster is stated rather than left open so the degree under test is the
    only thing varying — a session that could reach the shell would differ in
    two ways at once.
    """
    return SessionRequest(
        model="haiku",
        instructions="Answer the question directly, using the tools you have.",
        cwd=cwd,
        autonomy=autonomy,
        tools=["Read"],
        environment=session_env(None),
    )


async def answers_at(autonomy: SessionAutonomy, cwd: Path) -> Answer | None:
    """What a session at this degree submitted, or None if it never answered.

    The question is one no model can answer from its own knowledge, so an
    answer is evidence the session both reached its tool and got a result
    back — which is the half a question like "what is 2 + 2" cannot test,
    because it never needs the tool whose approval is under test.
    """
    secret_file = cwd / "secret.txt"
    secret_file.write_text(f"The word is {SECRET}.\n", encoding="utf-8")
    factory = agent_session(autonomy_probe_request(autonomy, cwd), runtime="claude")
    return (
        await factory.query(f"Read {secret_file} and tell me the word in it.", Answer)
    ).output


async def test_an_unattended_session_answers(tmp_path: Path) -> None:
    """The control, and the degree every session here opens at today."""
    answer = await answers_at("unattended", tmp_path)

    assert answer is not None and SECRET in answer.word.lower()


@pytest.mark.parametrize("autonomy", ["ask", "plan", "accept_edits"])
async def test_every_degree_still_returns_the_answer_it_was_opened_for(
    autonomy: SessionAutonomy, tmp_path: Path
) -> None:
    """Whether a narrowed degree is a governance choice or a broken session.

    A degree that cannot answer is not a safer version of this session; it is
    a session that does not work, and narrowing to it would trade a permission
    nothing was using for a result something needs.
    """
    answer = await answers_at(autonomy, tmp_path)

    assert answer is not None and SECRET in answer.word.lower()
