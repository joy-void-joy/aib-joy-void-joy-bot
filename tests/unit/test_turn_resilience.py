"""What a turn survives, and how a caller may watch it survive.

A turn ends when the model stops, and a model that stops after a preamble has
submitted nothing. That is a fifty-token miss, and without bounded correction
it ends a forecast that had not begun — so every session this project opens
carries retries and corrections rather than each caller remembering to.

Carrying them changes what a turn's event stream is. It becomes one logical
stream spanning every cycle, closing only when the result settles, which makes
the obvious way to watch a turn — drain the events, then ask for the result —
a wait for a close that only the unasked result would cause. `drive_turn` is
what callers use instead, and the deadlock is what these tests pin: each runs
under a timeout, so the regression fails the suite rather than hanging it.
"""

import asyncio
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from datetime import timedelta

import pytest
from lup.runtime.contracts import EventStream, Session, Turn
from lup.runtime.errors import StructuredOutputError, TurnFailure
from lup.runtime.factory import SessionFactory
from lup.runtime.models import (
    MessageCompletedEvent,
    SessionHandle,
    SessionId,
    TurnHandle,
    TurnId,
    TurnIdentifiers,
    TurnMessage,
    TurnRequest,
    TurnResult,
    TurnTextBlock,
    turn_request,
)
from lup.types import Usage
from pydantic import BaseModel

from aib.agent.client import TURN_CORRECTION, drive_turn, resilient

IDENTIFIERS = TurnIdentifiers(
    session=SessionId(value="session"), turn=TurnId(value="turn")
)


class Answer(BaseModel):
    """The typed output a scripted turn either submits or does not."""

    value: int


def said(text: str) -> TurnMessage:
    """One assistant message carrying a single block of text."""
    return TurnMessage(role="assistant", blocks=[TurnTextBlock(text=text)])


class ScriptedStream(EventStream):
    """One native turn's messages, delivered once and then ended."""

    def __init__(self, messages: list[TurnMessage]) -> None:
        self.messages = messages

    async def iterate(self) -> AsyncIterator[MessageCompletedEvent]:
        for message in self.messages:
            yield MessageCompletedEvent(identifiers=IDENTIFIERS, message=message)

    def events(self) -> AsyncIterator[MessageCompletedEvent]:
        return self.iterate()

    def live(self) -> AsyncIterator[MessageCompletedEvent]:
        return self.iterate()


class ScriptedTurn(Turn[Answer | None]):
    """A native turn that submits its scripted output, or admits it did not."""

    def __init__(
        self,
        messages: list[TurnMessage],
        output: Answer | None,
        hold: asyncio.Event | None = None,
    ) -> None:
        self.messages = messages
        self.output = output
        self.hold = hold

    async def result(self) -> TurnResult[Answer | None]:
        if self.hold is not None:
            await self.hold.wait()
        if self.output is None:
            raise StructuredOutputError(
                TurnFailure(
                    message="turn completed without a valid submit_output call",
                    identifiers=IDENTIFIERS,
                    correctable=True,
                )
            )
        return TurnResult[Answer | None](
            output=self.output,
            messages=self.messages,
            blocks=[block for message in self.messages for block in message.blocks],
            usage=Usage(),
            duration=timedelta(0),
            identifiers=IDENTIFIERS,
        )


class ScriptedSession(Session):
    """A session whose successive turns are scripted in advance."""

    def __init__(
        self,
        script: list[tuple[list[TurnMessage], Answer | None]],
        hold: asyncio.Event | None = None,
    ) -> None:
        self.script = script
        self.hold = hold
        self.attempts: list[TurnRequest[Answer | None]] = []

    async def start[T: BaseModel | None](
        self, request: TurnRequest[T]
    ) -> TurnHandle[T]:
        self.attempts.append(request)  # pyright: ignore[reportArgumentType]
        messages, output = self.script[
            min(len(self.attempts) - 1, len(self.script) - 1)
        ]
        handle = TurnHandle[Answer | None](
            turn=ScriptedTurn(messages, output, self.hold),
            events=ScriptedStream(messages),
        )
        return handle  # pyright: ignore[reportReturnType]


def scripted_factory(
    script: list[tuple[list[TurnMessage], Answer | None]],
    hold: asyncio.Event | None = None,
) -> tuple[SessionFactory, ScriptedSession]:
    """A resilient factory over one scripted session, and that session.

    A held session's turns never settle on their own, which is how a test
    about a caller interrupting a turn in flight says so rather than racing
    a fake fast enough to finish first.
    """
    inner = ScriptedSession(script, hold)

    @asynccontextmanager
    async def opener(resume: SessionId | None = None) -> AsyncIterator[SessionHandle]:
        yield SessionHandle(session=inner)

    return resilient(SessionFactory(opener)), inner


@pytest.mark.asyncio
async def test_watching_a_turn_does_not_wait_on_its_own_result() -> None:
    """A caller may consume a resilient turn's messages and still be answered.

    The stream a resilient turn hands out closes when the result settles, so a
    drain that runs before the result is asked for waits forever. Reaching the
    assertion at all is the property under test.
    """
    factory, _ = scripted_factory([([said("done")], Answer(value=7))])
    seen: list[str] = []

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request("go", Answer))
        result = await asyncio.wait_for(
            drive_turn(turn, lambda message: seen.append(str(message.role))), timeout=5
        )

    assert result.output == Answer(value=7)
    assert seen == ["assistant"]


@pytest.mark.asyncio
async def test_a_turn_that_stops_without_submitting_is_asked_again() -> None:
    """A missing submission is corrected rather than raised on the first miss.

    This is the failure that ended a forecast four seconds in: a preamble, no
    tool call, and a completed turn carrying no output. The correction reaches
    the same session, so the second attempt answers with its own messages —
    which the caller sees, because the stream spans both.
    """
    factory, inner = scripted_factory(
        [
            ([said("Step 1: parse the criteria")], None),
            ([said("done")], Answer(value=3)),
        ]
    )
    seen: list[str] = []

    def record(message: TurnMessage) -> None:
        for block in message.blocks:
            if isinstance(block, TurnTextBlock):
                seen.append(block.text)

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request("go", Answer))
        result = await asyncio.wait_for(drive_turn(turn, record), timeout=5)

    assert result.output == Answer(value=3)
    assert seen == ["Step 1: parse the criteria", "done"]
    assert len(inner.attempts) == 2


@pytest.mark.asyncio
async def test_corrections_are_bounded_and_the_last_miss_is_raised() -> None:
    """A model that never submits fails, rather than being asked forever."""
    factory, inner = scripted_factory([([said("still thinking")], None)])

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request("go", Answer))
        with pytest.raises(StructuredOutputError):
            await asyncio.wait_for(drive_turn(turn, lambda _: None), timeout=5)

    assert len(inner.attempts) == TURN_CORRECTION.cycles + 1


@pytest.mark.asyncio
async def test_the_correction_asks_the_agent_to_continue_its_analysis() -> None:
    """The instruction says continue, not submit.

    A correction arrives at an agent that still holds its own context. One told
    to submit a value matching the schema answers with a forecast it has not
    done the work for, so the wording is part of the behaviour rather than
    decoration on it.
    """
    factory, inner = scripted_factory(
        [([said("preamble")], None), ([said("done")], Answer(value=1))]
    )

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request("go", Answer))
        await asyncio.wait_for(drive_turn(turn, lambda _: None), timeout=5)

    corrected = inner.attempts[-1].input.text
    assert "Continue the analysis" in corrected
    assert "call submit_output" in corrected


@pytest.mark.asyncio
async def test_a_callback_that_raises_abandons_the_turn() -> None:
    """A caller rejecting what it just saw is not asking for another attempt.

    The forecaster reads credit exhaustion out of the text it is printing, and
    a turn corrected past that would spend two more attempts on an account that
    cannot answer.
    """

    class Rejected(Exception):
        """What the callback raises when it will not accept the turn."""

    def reject(message: TurnMessage) -> None:
        raise Rejected

    factory, inner = scripted_factory([([said("preamble")], None)], asyncio.Event())

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request("go", Answer))
        with pytest.raises(Rejected):
            await asyncio.wait_for(drive_turn(turn, reject), timeout=5)

    assert len(inner.attempts) == 1
