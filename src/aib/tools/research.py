"""Research tool — Opus sub-agent for factual data gathering.

Delegates data-gathering questions to an Opus sub-agent that has access
to ~35 data tools (web search, financial, government, markets, trends,
news, arXiv). Results are persisted to the worldview store for reuse
across forecasts.

Supports:
- List input → parallel execution via asyncio.gather
- Pre-write Grep dedup (search store before spawning Opus)
- Resumable sessions via SDK session IDs + cwd isolation
- Follow-up queries on existing research
- Amend mode (patch fields without re-running Opus)
"""

import asyncio
import json
import logging
from collections.abc import Mapping
from datetime import date, datetime, timedelta, timezone

from lup.runtime.models import (
    MessageCompletedEvent,
    SessionId,
    TurnMessage,
    TurnTextBlock,
    TurnToolCallBlock,
    turn_request,
)
from pydantic import BaseModel, Field, ValidationError, model_validator

from aib.agent.client import ClaudeExtras, agent_request, agent_session
from aib.agent.display import make_agent_prefix, print_block

from aib.agent.nested import NestedAgentReport
from aib.agent.retrodict import create_retrodict_hooks
from aib.retrodict_context import retrodict_cutoff
from aib.agent.session import get_session, register_nested_trace
from aib.paths import WORLDVIEW_PATH
from lup.mcp import McpServerEntry, ToolError, lup_tool
from aib.tools.metrics import costs
from aib.worldview.lookup import (
    all_slugs,
    amend_research_entry,
    commit_worldview,
    load_research_entry,
    save_research_entry,
)
from aib.worldview.models import (
    DataPoint,
    Source,
    WorldviewResearchEntry,
    make_slug,
)

logger = logging.getLogger(__name__)

# TTL presets: agent picks one based on topic volatility
TTL_PRESETS: dict[str, timedelta] = {
    "6h": timedelta(hours=6),
    "12h": timedelta(hours=12),
    "1d": timedelta(days=1),
    "3d": timedelta(days=3),
    "7d": timedelta(days=7),
    "14d": timedelta(days=14),
}

DEFAULT_TTL = "3d"


# ── Input/Output schemas ─────────────────────────────────────────


class ResearchQuestion(BaseModel):
    """A single research question for the Opus sub-agent."""

    query: str = Field(description="The factual question to research.")
    context: str = Field(
        default="",
        description="Additional context to help the sub-agent understand what data is needed.",
    )
    ttl: str = Field(
        default=DEFAULT_TTL,
        description=(
            "Cache lifetime. How long before this research goes stale. "
            "Options: 6h, 12h, 1d, 3d, 7d, 14d. "
            "Use shorter TTLs for fast-moving topics (outbreaks, earnings week), "
            "longer for slow-moving (historical trends, structural facts)."
        ),
    )


class ResearchInput(BaseModel):
    """Input for the research tool."""

    questions: list[ResearchQuestion] = Field(
        min_length=1,
        description="List of factual questions to research in parallel.",
    )
    follow_up: str | None = Field(
        default=None,
        description=(
            "Slug of an existing research entry to continue. "
            "Resumes the prior SDK session so the sub-agent has full context. "
            "Only one question allowed when using follow_up."
        ),
    )
    amend: str | None = Field(
        default=None,
        description=(
            "Slug of an existing research entry to patch. "
            "Updates specific fields without re-running the Opus sub-agent. "
            "Provide the updates in the first question's context field as JSON."
        ),
    )

    @model_validator(mode="before")
    @classmethod
    def lift_bare_question(cls, data: object) -> object:
        """Wrap a single top-level question into the questions list.

        `questions` holds `ResearchQuestion` objects whose own field is
        `query`, so a single-question call reads naturally as
        `research(query=...)` and callers write it that way. Accepting that
        shape costs nothing and removes a guaranteed round-trip.
        """
        if not isinstance(data, dict) or "questions" in data:
            return data
        bare = {k: data[k] for k in ("query", "context", "ttl") if k in data}
        if "query" not in bare:
            return data
        rest = {k: v for k, v in data.items() if k not in bare}
        return {**rest, "questions": [bare]}


class ResearchResult(BaseModel):
    """Result from a single research question."""

    query: str
    entry: WorldviewResearchEntry | None = None
    error: str | None = None
    is_follow_up: bool = False


class ResearchOutput(BaseModel):
    """Output from the research tool."""

    results: list[dict[str, object]]
    successful_count: int
    failed_count: int


class NestedAgentNoStructuredOutputError(BaseException):
    """Nested agent turn ended without a structured payload.

    Raised when a nested session asked for structured findings but its turn
    finished without a valid submission. Intentionally inherits
    from BaseException (not Exception) so it bypasses every `except Exception`
    in the call chain — the broad catches in run_single_research, the
    @mcp_tool decorator, and core.py's partial-save handler — and crashes
    the whole forecast process. We want a hard, immediately visible failure
    we can debug, not a buried log line.
    """


# ── Research sub-agent system prompt ──────────────────────────────

RESEARCH_SYSTEM_PROMPT = """\
You are a research sub-agent for a forecasting system. Your job is to gather
factual, current data on the topic(s) you're given.

## Guidelines

- **Be thorough**: Use multiple sources and cross-validate key facts.
- **Be structured**: Organize findings with clear sections and bullet points.
- **Be quantitative**: Extract specific numbers, dates, and metrics whenever possible.
- **Be sourced**: Cite every claim. Note the domain and access date.
- **Recency matters**: Prioritize the most recent data. Note data vintage.
- **No forecasting**: You gather facts. You do NOT predict the future or assign
  probabilities. If asked "what will X be?", reframe as "what is the current
  trajectory of X?" and report the data.

Write your full synthesis as a thorough markdown report in your final
text response, then call the `StructuredOutput` tool with a
`ResearchFindings` payload containing `key_facts`, `sources`, and
`data_points` (the structured fields the caller needs). The caller
uses your text response as the `answer`, so put your complete prose
there — don't repeat it inside the tool call.\
"""


def build_research_system_prompt(cutoff_date: date | None) -> str:
    effective_date = (cutoff_date or date.today()).isoformat()
    return f"Today's date: {effective_date}\n\n{RESEARCH_SYSTEM_PROMPT}"


# ── Structured findings schema ────────────────────────────────────


class ResearchFindings(BaseModel):
    """Structured findings produced by the Opus research sub-agent."""

    answer: str = Field(
        description="Thorough synthesis of the research findings as structured prose."
    )
    key_facts: list[str] = Field(
        default_factory=list,
        description="Most important factual findings as concise bullet points.",
    )
    sources: list[Source] = Field(
        default_factory=list,
        description="Every source consulted with URL, title, domain, accessed_at, and optional snippet.",
    )
    data_points: list[DataPoint] = Field(
        default_factory=list,
        description="Every quantitative finding with metric, value, unit, as_of date, source_url.",
    )


# ── Sub-agent runner ──────────────────────────────────────────────


def get_research_allowed_tools(
    servers: Mapping[str, McpServerEntry] | None = None,
) -> list[str]:
    """Every tool the research sub-agent may call, from the servers it has.

    Derived rather than listed. The union this replaced named seventeen tool
    groups, which is a second statement of what the servers already carry —
    and a second statement drifts: a tool added to a server and not to the
    union is registered and then refused by the allowlist hook, which reads
    to the agent as the tool being broken rather than as it being ungranted.

    Two things still have to be named, each because it is not on an
    in-process server. The built-ins belong to the engine. AskNews is served
    over HTTP, and an external MCP server cannot be enumerated without
    connecting to it — ``server_tool_names`` answers ``[]`` for one — so its
    four tools are named here. Naming them costs nothing when its server is
    absent: the missing key that leaves the server unregistered also puts
    those tools in the policy's exclusions, which the derivation subtracts.

    Passing no servers answers with the built-ins alone, which is what a
    sub-agent given no data tools should see.
    """
    from aib.agent.tool_policy import ASKNEWS_TOOLS, BUILTIN_TOOLS, ToolPolicy
    from aib.config import settings

    policy = ToolPolicy.from_settings(settings)
    return policy.get_allowed_tools(
        dict(servers or {}), builtin_tools=BUILTIN_TOOLS | ASKNEWS_TOOLS
    )


async def run_research_agent(
    query: str,
    context: str,
    *,
    resume_session_id: str | None = None,
    mcp_servers: Mapping[str, McpServerEntry] | None = None,
) -> NestedAgentReport[ResearchFindings]:
    """Run the Opus research sub-agent.

    Args:
        query: The research question.
        context: Additional context for the sub-agent.
        resume_session_id: SDK session ID to resume a prior conversation.
        mcp_servers: Optional MCP servers to provide data tools to the
            sub-agent (financial, markets, etc.). When None, the sub-agent
            uses only built-in SDK tools.

    Returns:
        NestedAgentReport wrapping the structured findings, the agent's
        final free-form text block, the SDK session_id, and any collated
        error.
    """
    WORLDVIEW_PATH.mkdir(parents=True, exist_ok=True)

    prompt_parts = [f"Research question: {query}"]
    if context:
        prompt_parts.append(f"\nAdditional context: {context}")
    prompt = "\n".join(prompt_parts)

    allowed_tools = get_research_allowed_tools(mcp_servers)

    from aib.config import settings

    # One pass over the stream feeds four accumulators and prints as it goes,
    # so the fold carries control flow no comprehension expresses.
    so_tool_blocks: list[TurnToolCallBlock] = []  # lup: ignore[empty-collection]
    text_blocks: list[str] = []  # lup: ignore[empty-collection]
    nested_messages: list[TurnMessage] = []  # lup: ignore[empty-collection]
    assistant_msg_count = 0
    tool_use_count = 0
    prefix = make_agent_prefix("research", query)
    cutoff = retrodict_cutoff.get()  # lup: ignore[dict-get] — a ContextVar
    retrodict_hooks = None if cutoff is None else create_retrodict_hooks()

    factory = agent_session(
        agent_request(
            model=settings.model,
            system_prompt=build_research_system_prompt(cutoff),
            cwd=WORLDVIEW_PATH,
            allowed_tools=allowed_tools,
            extra_hooks=retrodict_hooks,
            tool_servers=mcp_servers or {},
        ),
        extras=ClaudeExtras(),
    )
    resume = None if resume_session_id is None else SessionId(value=resume_session_id)
    async with factory.open(resume) as handle:
        turn = await handle.session.start(turn_request(prompt, ResearchFindings))
        if turn.events is not None:
            async for event in turn.events.events():
                if not isinstance(event, MessageCompletedEvent):
                    continue
                nested_messages.append(event.message)
                if event.message.role != "assistant":
                    continue
                assistant_msg_count += 1
                for block in event.message.blocks:
                    print_block(block, prefix=prefix)
                    if isinstance(block, TurnToolCallBlock):
                        tool_use_count += 1
                        if block.name == "StructuredOutput":
                            so_tool_blocks.append(block)
                    elif isinstance(block, TurnTextBlock):
                        text_blocks.append(block.text)
        result = await turn.turn.result()

    session_id = result.identifiers.session.value
    logger.info(
        "Research sub-agent turn: session=%s duration=%s cost_usd=%s "
        "assistant_msgs=%d tool_uses=%d text_blocks=%d so_blocks=%d",
        session_id,
        result.duration,
        result.usage.cost_usd,
        assistant_msg_count,
        tool_use_count,
        len(text_blocks),
        len(so_tool_blocks),
    )
    if result.usage.cost_usd is not None:
        costs.record("research", result.usage.cost_usd)

    findings = result.output
    if findings is None and so_tool_blocks:
        try:
            findings = ResearchFindings.model_validate(so_tool_blocks[-1].arguments)
            logger.warning(
                "Recovered research findings from the tool call the runtime did "
                "not fold into an output: %s",
                query[:80],
            )
        except ValidationError:
            raise NestedAgentNoStructuredOutputError(
                f"Research nested agent called StructuredOutput but "
                f"payload failed validation. "
                f"session_id={session_id} "
                f"blocks={len(so_tool_blocks)}"
            ) from None
    if findings is None:
        raise NestedAgentNoStructuredOutputError(
            f"Research nested agent ended without structured output. "
            f"session_id={session_id} "
            f"assistant_msgs={assistant_msg_count} tool_uses={tool_use_count} "
            f"last_text={(text_blocks[-1] if text_blocks else '')[:300]!r}"
        )

    from aib.agent.core import build_trace

    return NestedAgentReport[ResearchFindings](
        payload=findings,
        final_text=text_blocks[-1] if text_blocks else "",
        session_id=session_id,
        trace=build_trace(nested_messages, query),
    )


# ── Entry construction ──────────────────────────────────────────


def build_research_entry(
    query: str,
    findings: ResearchFindings,
    session_id: str | None,
    final_text: str,
    ttl: timedelta,
    slug: str,
) -> WorldviewResearchEntry:
    """Assemble a WorldviewResearchEntry from the sub-agent's structured findings."""
    now = datetime.now(timezone.utc)
    return WorldviewResearchEntry(
        slug=slug,
        query=query,
        answer=final_text or findings.answer,
        key_facts=findings.key_facts[:20],
        sources=findings.sources[:20],
        data_points=findings.data_points[:30],
        created_at=now,
        updated_at=now,
        stale_after=now + ttl,
        session_id=session_id,
    )


# ── Single question runner ────────────────────────────────────────


async def run_single_research(
    question: ResearchQuestion,
    existing_slugs: set[str],
) -> ResearchResult:
    """Run research for a single question and persist the result."""
    slug = make_slug(question.query, existing_slugs)
    ttl = TTL_PRESETS.get(question.ttl, TTL_PRESETS[DEFAULT_TTL])

    try:
        forecast_session = get_session()
        research_servers = forecast_session.research_mcp_servers
    except RuntimeError:
        research_servers = None

    try:
        report = await run_research_agent(
            question.query,
            question.context,
            mcp_servers=research_servers,
        )
    except (RuntimeError, OSError, ValidationError) as e:
        logger.exception("Research failed for: %s", question.query)
        return ResearchResult(
            query=question.query,
            error=f"{type(e).__name__}: {e}",
        )

    register_nested_trace(f"research:{question.query}", report.trace)

    if report.payload is None:
        return ResearchResult(
            query=question.query,
            error="Research sub-agent did not return structured findings",
        )

    try:
        entry = build_research_entry(
            question.query,
            report.payload,
            report.session_id,
            report.final_text,
            ttl,
            slug,
        )
    except (ValidationError, ValueError) as e:
        logger.exception("Failed to build research entry: %s", question.query)
        return ResearchResult(
            query=question.query,
            error=f"{type(e).__name__}: {e}",
        )

    save_research_entry(entry)
    commit_worldview(f"research: {question.query[:60]}")

    return ResearchResult(query=entry.query, entry=entry)


# ── Staleness refresh ─────────────────────────────────────────────


async def refresh_research_entry(entry: WorldviewResearchEntry) -> ResearchResult:
    """Re-research a stale entry in place, keeping its slug and per-entry TTL."""
    ttl = entry.stale_after - entry.updated_at
    if ttl <= timedelta(0):
        ttl = TTL_PRESETS[DEFAULT_TTL]

    try:
        research_servers = get_session().research_mcp_servers
    except RuntimeError:
        research_servers = None

    try:
        report = await run_research_agent(
            entry.query,
            "",
            mcp_servers=research_servers,
        )
    except (RuntimeError, OSError, ValidationError) as e:
        logger.exception("Refresh failed for: %s", entry.slug)
        return ResearchResult(query=entry.query, error=f"{type(e).__name__}: {e}")

    register_nested_trace(f"research:{entry.query}", report.trace)

    if report.payload is None:
        return ResearchResult(
            query=entry.query,
            error="Research sub-agent did not return structured findings",
        )

    refreshed = build_research_entry(
        entry.query,
        report.payload,
        report.session_id,
        report.final_text,
        ttl,
        entry.slug,
    ).model_copy(update={"created_at": entry.created_at})
    save_research_entry(refreshed)
    return ResearchResult(query=refreshed.query, entry=refreshed)


# ── Follow-up handler ─────────────────────────────────────────────


async def run_follow_up(
    slug: str,
    question: ResearchQuestion,
) -> ResearchResult:
    """Resume a prior research session with a follow-up question."""
    entry = load_research_entry(slug)
    if entry is None:
        return ResearchResult(
            query=question.query,
            error=f"Research entry '{slug}' not found",
        )

    ttl = TTL_PRESETS.get(question.ttl, TTL_PRESETS[DEFAULT_TTL])

    try:
        forecast_session = get_session()
        research_servers = forecast_session.research_mcp_servers
    except RuntimeError:
        research_servers = None

    try:
        report = await run_research_agent(
            question.query,
            question.context,
            resume_session_id=entry.session_id,
            mcp_servers=research_servers,
        )
    except (RuntimeError, OSError, ValidationError) as e:
        logger.exception("Follow-up failed for: %s", slug)
        return ResearchResult(
            query=question.query,
            error=f"{type(e).__name__}: {e}",
        )

    register_nested_trace(f"research:{question.query}", report.trace)

    findings = report.payload
    if findings is None:
        return ResearchResult(
            query=question.query,
            error="Research sub-agent did not return structured findings",
        )

    new_prose = report.final_text or findings.answer
    now = datetime.now(timezone.utc)
    new_facts = [f for f in findings.key_facts if f not in entry.key_facts]
    try:
        updated = entry.model_copy(
            update={
                "answer": f"{entry.answer}\n\n---\n\n## Follow-up: {question.query}\n\n{new_prose}",
                "key_facts": [*entry.key_facts, *new_facts],
                "sources": [*entry.sources, *findings.sources],
                "data_points": [*entry.data_points, *findings.data_points],
                "updated_at": now,
                "stale_after": now + ttl,
                "follow_up_count": entry.follow_up_count + 1,
                "session_id": report.session_id or entry.session_id,
            }
        )
    except (ValidationError, ValueError) as e:
        logger.exception("Failed to build follow-up entry: %s", slug)
        return ResearchResult(
            query=question.query,
            error=f"{type(e).__name__}: {e}",
        )

    save_research_entry(updated)
    commit_worldview(f"research follow-up: {slug}")

    return ResearchResult(query=question.query, entry=updated, is_follow_up=True)


# ── Amend handler ─────────────────────────────────────────────────


def handle_amend(slug: str, updates_json: str) -> ResearchResult:
    """Patch fields on an existing research entry."""
    try:
        updates = json.loads(updates_json)
    except json.JSONDecodeError as e:
        return ResearchResult(
            query="",
            error=f"Invalid JSON in amend updates: {e}",
        )

    allowed_fields = {"answer", "key_facts", "data_points", "sources"}
    filtered = {k: v for k, v in updates.items() if k in allowed_fields}
    if not filtered:
        return ResearchResult(
            query="",
            error=f"No amendable fields in updates. Allowed: {allowed_fields}",
        )

    result = amend_research_entry(
        slug, filtered, reason="manual amend via research tool"
    )
    if result is None:
        return ResearchResult(
            query="",
            error=f"Research entry '{slug}' not found",
        )

    commit_worldview(f"research amend: {slug}")

    return ResearchResult(query=result.query, entry=result)


# ── MCP Tool ──────────────────────────────────────────────────────


@lup_tool(
    "Delegate factual research questions to an Opus sub-agent with full data-gathering "
    "tools (web search, financial APIs, government data, prediction markets, arXiv, "
    "news, trends). The sub-agent researches thoroughly and persists findings to the "
    "worldview store for reuse across forecasts.\n\n"
    "**Use research() for backward-looking questions**: 'What IS the current state of X?' "
    "'What data exists on Y?' 'What happened with Z?'\n\n"
    "**Do NOT use for predictions**: If it needs a probability distribution, use "
    "subforecast() instead.\n\n"
    "Pass multiple questions to research them in parallel.\n\n"
    "Example:\n"
    '  research(questions=[{query: "Current US measles case count and trajectory", ttl: "6h"},\n'
    '                      {query: "CDC vaccination rate trends 2024-2026", ttl: "7d"}])\n\n'
    "Follow-up on prior research (resumes the sub-agent conversation):\n"
    '  research(follow_up="us-measles-trajectory-2026-a7f2b3c1",\n'
    '           questions=[{query: "What about state-level breakdown?"}])\n\n'
    "Amend an existing entry without re-running Opus:\n"
    '  research(amend="us-measles-trajectory-2026-a7f2b3c1",\n'
    '           questions=[{context: \'{"key_facts": ["Updated fact"]}\'}])\n',
    name="research",
)
async def research(args: ResearchInput) -> ResearchOutput:
    """Run parallel research via Opus sub-agents with worldview persistence."""

    # Handle amend mode (no sub-agent needed)
    if args.amend:
        updates_json = args.questions[0].context if args.questions else "{}"
        result = handle_amend(args.amend, updates_json)
        return ResearchOutput(
            results=[result.model_dump(exclude_none=True)],
            successful_count=0 if result.error else 1,
            failed_count=1 if result.error else 0,
        )

    # Handle follow-up mode (single question, resumes session)
    if args.follow_up:
        if len(args.questions) != 1:
            raise ToolError("follow_up mode requires exactly one question")
        result = await run_follow_up(args.follow_up, args.questions[0])
        return ResearchOutput(
            results=[result.model_dump(exclude_none=True)],
            successful_count=0 if result.error else 1,
            failed_count=1 if result.error else 0,
        )

    # Standard mode: parallel execution
    existing = all_slugs()
    tasks = [run_single_research(q, existing) for q in args.questions]
    results = await asyncio.gather(*tasks)

    errors = [r for r in results if r.error is not None]
    successful = [r for r in results if r.error is None]

    if not successful:
        error_msgs = [r.error for r in errors]
        raise ToolError(f"All research questions failed: {error_msgs}")

    return ResearchOutput(
        results=[r.model_dump(exclude_none=True) for r in results],
        successful_count=len(successful),
        failed_count=len(errors),
    )
