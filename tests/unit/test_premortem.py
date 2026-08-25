"""Tests for the premortem tool and reviewer gate state."""

from pathlib import Path

import pytest
from lup.adapters.claude.runtime import SUBMISSION_TOOL as CLAUDE_SUBMISSION_TOOL
from lup.adapters.codex.runtime import SUBMISSION_TOOL as CODEX_SUBMISSION_TOOL
from lup.hooks import LupHookInput, LupHookOutput, LupHooksConfig
from lup.mcp import LupMcpTool
from lup.types import JsonObject

from aib.agent.models import BinaryEstimate, Factor
from aib.agent.nested import NestedAgentReport
from aib.agent.session import ReviewResult, ReviewState, ReviewVerdict
from aib.tools.premortem import (
    PremortemInput,
    PremortemVerdict,
    build_reviewer_hooks,
    build_reviewer_prompt,
    create_premortem_tool,
)
from aib.tools.reflection import ReflectionInput


def _make_binary_input(
    factors: list[Factor] | None = None,
    tentative_probability: float = 0.6,
) -> ReflectionInput:
    return ReflectionInput(
        factors=factors or [],
        tentative_estimate=BinaryEstimate(logit=0.5, probability=tentative_probability),
        assessment="Test assessment.",
        tool_audit="Test tool audit.",
        process_reflection="Test process reflection.",
    )


def _make_premortem_input(
    counterargument: str = "A reasonable disagreer would point out that the data is noisy.",
    what_would_change_my_mind: str = "A definitive announcement in the next 24 hours.",
    confidence_in_estimate: float = 0.7,
) -> PremortemInput:
    return PremortemInput(
        counterargument=counterargument,
        what_would_change_my_mind=what_would_change_my_mind,
        confidence_in_estimate=confidence_in_estimate,
    )


class TestReviewState:
    """ReviewState verdict tracking and gate logic."""

    def test_initial_state_not_passed(self) -> None:
        state = ReviewState()
        assert state.passed is False
        assert state.reflection_done is False
        assert state.last_verdict is None
        assert state.consecutive_fails == 0

    def test_reflection_done_after_store(self) -> None:
        state = ReviewState()
        state.store_reflection(_make_binary_input())
        assert state.reflection_done is True
        assert state.passed is False

    def test_approve_passes(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.passed is True
        assert state.last_verdict == ReviewVerdict.approve

    def test_warn_passes(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.warn, assessment="Minor"))
        assert state.passed is True
        assert state.last_verdict == ReviewVerdict.warn

    def test_single_fail_does_not_pass(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.passed is False
        assert state.consecutive_fails == 1

    def test_three_consecutive_fails_auto_approves(self) -> None:
        state = ReviewState()
        for _ in range(3):
            state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.consecutive_fails == 3
        assert state.passed is True

    def test_approve_resets_consecutive_fails(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.consecutive_fails == 2
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.consecutive_fails == 0
        assert state.passed is True

    def test_fail_after_approve_resets_pass(self) -> None:
        state = ReviewState()
        state.record(ReviewResult(verdict=ReviewVerdict.approve, assessment="OK"))
        assert state.passed is True
        state.record(ReviewResult(verdict=ReviewVerdict.fail, assessment="Bad"))
        assert state.passed is False
        assert state.consecutive_fails == 1

    def test_history_records_verdicts(self) -> None:
        state = ReviewState()
        reflection = _make_binary_input()
        state.record(
            ReviewResult(verdict=ReviewVerdict.warn, assessment="Some concern"),
            reflection_input=reflection,
        )
        assert len(state.history) == 1
        entry = state.history[0]
        assert entry["verdict"] == "warn"
        assert entry["reviewer_assessment"] == "Some concern"
        assert "input" in entry


class TestPremortemInput:
    """Adversarial input validation."""

    def test_confidence_bounds(self) -> None:
        _make_premortem_input(confidence_in_estimate=0.0)
        _make_premortem_input(confidence_in_estimate=1.0)
        with pytest.raises(Exception):
            _make_premortem_input(confidence_in_estimate=-0.1)
        with pytest.raises(Exception):
            _make_premortem_input(confidence_in_estimate=1.1)

    def test_required_fields(self) -> None:
        with pytest.raises(Exception):
            PremortemInput.model_validate({})  # type: ignore[arg-type]


class TestBuildReviewerPrompt:
    """Reviewer prompt construction — takes reflection + premortem input."""

    def test_includes_question_context(self) -> None:
        reflection = _make_binary_input(
            factors=[Factor(description="Evidence", logit=1.0, confidence=0.8)],
        )
        premortem = _make_premortem_input()
        context = {"title": "Will X happen?", "type": "binary"}

        prompt = build_reviewer_prompt(reflection, premortem, context, None)

        assert "Will X happen?" in prompt
        assert "binary" in prompt

    def test_includes_factors(self) -> None:
        reflection = _make_binary_input(
            factors=[
                Factor(description="Strong signal", logit=2.0, confidence=0.9),
                Factor(description="Weak counter", logit=-0.5, confidence=0.7),
            ],
        )
        premortem = _make_premortem_input()

        prompt = build_reviewer_prompt(reflection, premortem, None, None)

        assert "Strong signal" in prompt
        assert "Weak counter" in prompt

    def test_includes_adversarial_section(self) -> None:
        reflection = _make_binary_input()
        premortem = _make_premortem_input(
            counterargument="The trend could reverse due to Fed action.",
            what_would_change_my_mind="A rate cut announcement.",
            confidence_in_estimate=0.75,
        )

        prompt = build_reviewer_prompt(reflection, premortem, None, None)

        assert "adversarial self-examination" in prompt
        assert "The trend could reverse due to Fed action." in prompt
        assert "A rate cut announcement." in prompt
        assert "0.75" in prompt

    def test_includes_trace_file(self) -> None:
        reflection = _make_binary_input()
        premortem = _make_premortem_input()
        trace_path = Path("/tmp/session/trace_at_premortem.md")

        prompt = build_reviewer_prompt(reflection, premortem, None, trace_path)

        assert "trace_at_premortem.md" in prompt
        assert "/tmp/session/trace_at_premortem.md" in prompt


class TestReviewerHooks:
    """What the reviewer's hooks may and may not stop.

    The reviewer submits its verdict through whichever tool the selected
    runtime binds the turn to, and the adapter injects that tool under a
    spelling no caller states. A hook that judges the reviewer by a list of
    tool names it was written with cannot know that name, so it denies the
    one call the reviewer exists to make — silently, because the gate
    answers an unreachable reviewer by opening.
    """

    async def invoke(
        self,
        hooks: LupHooksConfig,
        tool_name: str,
        tool_input: JsonObject,
        tool_path: str = "",
    ) -> LupHookOutput:
        """Drive every PreToolUse hook, returning the first that decides.

        `tool_path` is resolved by the adapter in production, so a path-bearing
        tool is stated here the way the hook receives it rather than the way
        the tool spells it.
        """
        decided = LupHookOutput()
        for matcher in hooks.pre_tool_use:
            result = await matcher.hook(
                LupHookInput(
                    event="PreToolUse",
                    tool_name=tool_name,
                    tool_input=tool_input,
                    tool_path=tool_path,
                )
            )
            if result.decision is not None:
                decided = result
                break
        return decided

    @pytest.mark.asyncio
    @pytest.mark.parametrize(
        "submission_tool", [CLAUDE_SUBMISSION_TOOL, CODEX_SUBMISSION_TOOL]
    )
    async def test_submission_tool_is_never_denied(self, submission_tool: str) -> None:
        hooks = build_reviewer_hooks([Path("/tmp/traces")])
        result = await self.invoke(hooks, submission_tool, {"verdict": "approve"})
        assert result.decision != "deny"

    @pytest.mark.asyncio
    async def test_reads_outside_the_allowed_directories_are_denied(self) -> None:
        """Dropping the tool allowlist leaves the directory rules intact."""
        hooks = build_reviewer_hooks([Path("/tmp/traces")])
        result = await self.invoke(
            hooks, "Read", {"file_path": "/etc/passwd"}, tool_path="/etc"
        )
        assert result.decision == "deny"

    @pytest.mark.asyncio
    async def test_reads_inside_the_allowed_directories_are_permitted(self) -> None:
        hooks = build_reviewer_hooks([Path("/tmp/traces")])
        result = await self.invoke(
            hooks,
            "Read",
            {"file_path": "/tmp/traces/t.md"},
            tool_path="/tmp/traces",
        )
        assert result.decision != "deny"


class TestUnreachableReviewer:
    """What the gate records when the review does not happen.

    The gate opens either way — a forecast is not abandoned because its
    reviewer died. What must not happen is the outage being written down as
    a pass: that is how a broken reviewer stays broken, since every trace it
    leaves behind reads exactly like a clean approval.
    """

    def build_gate(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> tuple[LupMcpTool[PremortemInput, PremortemVerdict], ReviewState]:
        async def reviewer_that_never_returns_a_verdict(
            *_args: object, **_kwargs: object
        ) -> NestedAgentReport[ReviewResult]:
            return NestedAgentReport[ReviewResult](
                error="turn completed without a valid submit_output call",
            )

        monkeypatch.setattr(
            "aib.tools.premortem.run_reviewer",
            reviewer_that_never_returns_a_verdict,
        )
        state = ReviewState()
        state.store_reflection(_make_binary_input())
        tool = create_premortem_tool(session_dir=tmp_path, review_state=state)
        return tool, state

    @pytest.mark.asyncio
    async def test_outage_is_recorded_as_warn_not_approve(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        tool, state = self.build_gate(monkeypatch, tmp_path)
        verdict = await tool(_make_premortem_input())

        assert verdict.verdict == "warn"
        assert state.last_verdict == ReviewVerdict.warn

    @pytest.mark.asyncio
    async def test_outage_still_opens_the_gate(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        tool, state = self.build_gate(monkeypatch, tmp_path)
        await tool(_make_premortem_input())

        assert state.passed is True

    @pytest.mark.asyncio
    async def test_outage_names_itself_in_the_record(
        self, monkeypatch: pytest.MonkeyPatch, tmp_path: Path
    ) -> None:
        """The reviewer's own failure reaches the forecast's revision history."""
        tool, state = self.build_gate(monkeypatch, tmp_path)
        verdict = await tool(_make_premortem_input())

        assert "GATE DID NOT RUN" in verdict.assessment
        assert "submit_output" in verdict.assessment
        assert verdict.note is not None
        assert "GATE DID NOT RUN" in str(state.history[-1]["reviewer_assessment"])
