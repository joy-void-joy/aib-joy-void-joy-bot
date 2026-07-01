"""Inline expansion of nested sub-agent traces in build_trace."""

from claude_agent_sdk.types import (
    AssistantMessage,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)

from aib.agent.core import build_trace
from aib.agent.session import (
    ForecastSession,
    register_nested_trace,
    register_premortem_trace,
    reset_session,
    set_session,
)


def tool_call(
    tool_use_id: str, name: str, tool_input: dict
) -> list[AssistantMessage | UserMessage]:
    """A main-agent tool call plus its result, as (assistant, user) messages."""
    return [
        AssistantMessage(
            content=[ToolUseBlock(id=tool_use_id, name=name, input=tool_input)],
            model="opus",
        ),
        UserMessage(content=[ToolResultBlock(tool_use_id=tool_use_id, content="ok")]),
    ]


def test_research_trace_expands_after_its_result() -> None:
    messages = tool_call(
        "t1",
        "mcp__research__research",
        {"questions": [{"query": "How many measles cases?"}]},
    )
    nested = {"research:How many measles cases?": "DEEP RESEARCH REASONING"}
    trace = build_trace(messages, "Q", nested_traces=nested)

    assert "DEEP RESEARCH REASONING" in trace
    assert "↳ Nested research agent trace" in trace
    assert trace.index("Nested research agent trace") > trace.index("Result")


def test_no_expansion_without_matching_key() -> None:
    messages = tool_call(
        "t1", "mcp__research__research", {"questions": [{"query": "unmatched"}]}
    )
    trace = build_trace(messages, "Q", nested_traces={"research:other": "X"})
    assert "Nested research agent trace" not in trace


def test_no_expansion_when_nested_traces_absent() -> None:
    messages = tool_call(
        "t1", "mcp__research__research", {"questions": [{"query": "q"}]}
    )
    assert "Nested" not in build_trace(messages, "Q")


def test_subforecast_trace_expands() -> None:
    messages = tool_call(
        "s1", "mcp__subforecast__subforecast", {"specs": [{"question": "Will X?"}]}
    )
    trace = build_trace(
        messages, "Q", nested_traces={"subforecast:Will X?": "PIPELINE TRACE"}
    )
    assert "PIPELINE TRACE" in trace
    assert "↳ Nested subforecast agent trace" in trace


def test_premortem_traces_match_by_render_ordinal() -> None:
    messages = [
        *tool_call("p1", "mcp__premortem__premortem", {}),
        *tool_call("p2", "mcp__premortem__premortem", {}),
    ]
    nested = {"premortem:0": "FIRST REVIEW", "premortem:1": "SECOND REVIEW"}
    trace = build_trace(messages, "Q", nested_traces=nested)
    assert trace.index("FIRST REVIEW") < trace.index("SECOND REVIEW")


def test_register_helpers_write_to_session() -> None:
    session = ForecastSession()
    set_session(session)
    try:
        register_nested_trace("research:q", "R")
        register_premortem_trace("first")
        register_premortem_trace("second")
    finally:
        reset_session()

    assert session.nested_traces["research:q"] == "R"
    assert session.nested_traces["premortem:0"] == "first"
    assert session.nested_traces["premortem:1"] == "second"


def test_register_helpers_noop_without_session() -> None:
    reset_session()
    register_nested_trace("research:q", "R")
    register_premortem_trace("x")
