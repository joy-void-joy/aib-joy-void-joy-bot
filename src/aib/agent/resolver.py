"""Resolution checker agent.

Spawns Agent SDK agents to check whether unresolved forecasting questions
have resolved by examining resolution criteria and fetching real-world data.
"""

import asyncio
import logging
from collections.abc import Callable
from dataclasses import dataclass

from lup.runtime.models import (
    TurnMessage,
    TurnTextBlock,
    turn_request,
)
from lup.mcp import (
    LupMcpTool,
    McpServerEntry,
    create_mcp_server,
)
from pydantic import BaseModel

from aib.agent.client import (
    ClaudeExtras,
    agent_request,
    agent_session,
    drive_turn,
)
from aib.agent.display import make_agent_prefix, print_block
from aib.agent.nested import NestedAgentReport
from aib.agent.tool_policy import (
    BUILTIN_TOOLS,
    ToolPolicy,
    data_tool_groups,
)
from aib.config import settings as default_settings

logger = logging.getLogger(__name__)

MAX_CONCURRENT = 5


class ResolutionVerdict(BaseModel):
    """Structured output from a resolver agent."""

    resolved: bool
    resolution: str | float | None = None
    confidence: float
    reason: str
    sources: list[str]


@dataclass
class QuestionForResolution:
    """Minimal question data needed for resolution checking."""

    post_id: int
    question_title: str
    question_type: str
    resolution_criteria: str
    fine_print: str
    description: str = ""
    scheduled_resolve_time: str | None = None
    scheduled_close_time: str | None = None


RESOLVER_SYSTEM_PROMPT = """\
You are a resolution checker for forecasting questions. Your job is to determine
whether a question has already resolved based on its resolution criteria.

You have access to web search, URL fetching, financial data (FRED, stock prices,
World Bank), government data (BLS, Census), prediction market data (Polymarket,
Manifold, Kalshi, Metaculus), Google Trends, Reddit, arXiv, Wikipedia, and news
search. Use whatever tools are needed to check the resolution criteria.

Guidelines:
- Read the resolution criteria carefully. Focus on what EXACTLY triggers resolution.
- Search for the specific data, events, or announcements mentioned in the criteria.
- For binary questions: determine if the outcome is YES or NO.
- For numeric questions: find the specific value that the question resolves to.
- If the criteria reference a specific date and that date hasn't passed, the question
  has NOT resolved yet.
- If you cannot find definitive evidence either way, report resolved=false.
- Be conservative: only report resolved=true when you have strong evidence.
- Include the URLs and sources you consulted in your response.
"""


def build_research_tool_groups() -> dict[str, list[LupMcpTool]]:
    """Session-free research tools, grouped by MCP server name.

    The forecaster's own surface, because `build_resolver_tools` reads its
    roster from `orchestrator_allowlist` — a resolver served one set of tools
    and granted another would have every call refused at the moment it was
    made.
    """
    return data_tool_groups()


def build_resolver_servers() -> dict[str, McpServerEntry]:
    """Build MCP servers for the resolver agent.

    AskNews is no longer mounted beside these. It is a lane inside `search`,
    so the resolver reaches it there — and mounting the remote server would
    serve four tools the roster does not name, each refused at the moment it
    was called.
    """
    return {
        name: create_mcp_server(name, tools=tools)
        for name, tools in build_research_tool_groups().items()
    }


def build_resolver_tools(
    mounted: dict[str, McpServerEntry] | None = None,
) -> list[str]:
    """Every tool the resolver is served, and nothing besides.

    Derived from its own servers rather than read off
    `orchestrator_allowlist`, which branches on the research topology — a
    setting that governs where the *forecaster's* tools sit and says
    nothing about the resolver, whose servers are `data_tool_groups()`
    whatever it is set to.

    Reading it made the two disagree the moment the setting moved off its
    default: under `direct` the resolver was granted the forty narrow names
    while being served the condensed ten, so the only tools that worked
    were the three whose names happen to appear in both. The failure is
    quiet in the direction that hurts — a served tool that is not granted
    is refused when called, which reads to the agent as the tool being
    broken rather than as it being ungranted.
    """
    policy = ToolPolicy.from_settings(default_settings)
    servers = mounted if mounted is not None else build_resolver_servers()
    return policy.get_allowed_tools(servers, builtin_tools=BUILTIN_TOOLS)


async def resolve_question(
    question: QuestionForResolution,
    *,
    mcp_servers: dict[str, McpServerEntry] | None = None,
    allowed_tools: list[str] | None = None,
) -> NestedAgentReport[ResolutionVerdict]:
    """Run a resolver agent to check if a question has resolved."""
    servers = mcp_servers or build_resolver_servers()
    tools = allowed_tools or build_resolver_tools(servers)

    prompt = (
        f"Check whether this forecasting question has resolved.\n\n"
        f"**Title:** {question.question_title}\n"
        f"**Type:** {question.question_type}\n"
        f"**Resolution Criteria:**\n{question.resolution_criteria}\n\n"
        f"**Fine Print:**\n{question.fine_print}\n"
    )
    if question.description:
        prompt += f"\n**Background:**\n{question.description}\n"
    if question.scheduled_resolve_time:
        prompt += f"\n**Scheduled Resolve Time:** {question.scheduled_resolve_time}\n"

    text_blocks: list[str] = []
    prefix = make_agent_prefix("resolver", question.question_title)
    factory = agent_session(
        agent_request(
            model=default_settings.model,
            system_prompt=RESOLVER_SYSTEM_PROMPT,
            autonomy="ask",
            tool_servers=servers,
            allowed_tools=tools,
        ),
        extras=ClaudeExtras(),
    )

    def record(message: TurnMessage) -> None:
        if message.role != "assistant":
            return
        for block in message.blocks:
            print_block(block, prefix=prefix)
            if isinstance(block, TurnTextBlock):
                text_blocks.append(block.text)

    async with factory.open() as handle:
        turn = await handle.session.start(turn_request(prompt, ResolutionVerdict))
        verdict = (await drive_turn(turn, record)).output

    final_text = text_blocks[-1] if text_blocks else ""
    if verdict is not None:
        return NestedAgentReport[ResolutionVerdict](
            payload=verdict,
            final_text=final_text,
        )

    return NestedAgentReport[ResolutionVerdict](
        payload=ResolutionVerdict(
            resolved=False,
            resolution=None,
            confidence=0.0,
            reason="Agent produced no structured output",
            sources=[],
        ),
        final_text=final_text,
    )


async def resolve_batch(
    questions: list[QuestionForResolution],
    on_complete: Callable[[int, ResolutionVerdict], None] | None = None,
) -> list[tuple[int, ResolutionVerdict]]:
    """Resolve multiple questions concurrently with a semaphore limit."""
    servers = build_resolver_servers()
    tools = build_resolver_tools(servers)
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    async def resolve_one(
        q: QuestionForResolution,
    ) -> tuple[int, ResolutionVerdict]:
        try:
            async with semaphore:
                logger.info("Resolving post %d: %s", q.post_id, q.question_title[:60])
                report = await asyncio.shield(
                    resolve_question(q, mcp_servers=servers, allowed_tools=tools)
                )
                verdict = report.payload or ResolutionVerdict(
                    resolved=False,
                    resolution=None,
                    confidence=0.0,
                    reason="Agent produced no structured output",
                    sources=[],
                )
        except (Exception, asyncio.CancelledError) as exc:
            logger.exception("Resolver failed for post %d", q.post_id)
            verdict = ResolutionVerdict(
                resolved=False,
                resolution=None,
                confidence=0.0,
                reason=f"Agent error: {exc}",
                sources=[],
            )
        if on_complete:
            on_complete(q.post_id, verdict)
        return q.post_id, verdict

    coros = [resolve_one(q) for q in questions]
    raw = await asyncio.gather(*coros, return_exceptions=True)
    results: list[tuple[int, ResolutionVerdict]] = []
    for i, item in enumerate(raw):
        if isinstance(item, BaseException):
            pid = questions[i].post_id
            logger.error("Unhandled exception for post %d: %s", pid, item)
            verdict = ResolutionVerdict(
                resolved=False,
                resolution=None,
                confidence=0.0,
                reason=f"Unhandled error: {item}",
                sources=[],
            )
            if on_complete:
                on_complete(pid, verdict)
            results.append((pid, verdict))
        else:
            results.append(item)
    return results
