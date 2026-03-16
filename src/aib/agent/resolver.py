"""Resolution checker agent.

Spawns Agent SDK agents to check whether unresolved forecasting questions
have resolved by examining resolution criteria and fetching real-world data.
"""

import asyncio
import logging
from collections.abc import Callable
from dataclasses import dataclass

from claude_agent_sdk import ResultMessage
from claude_agent_sdk.types import McpHttpServerConfig, McpServerConfig
from pydantic import BaseModel

from aib.agent.client import build_client
from aib.agent.tool_policy import (
    COMPOSITION_TOOLS,
    NOTES_TOOLS,
    SANDBOX_TOOLS,
    ToolPolicy,
)
from aib.config import settings as default_settings
from aib.tools.financial import create_financial_server
from aib.tools.government import create_government_server
from aib.tools.markets import create_markets_server
from aib.tools.reddit import create_reddit_server
from aib.tools.search import create_search_server
from aib.tools.trends import create_trends_server

logger = logging.getLogger(__name__)

MAX_CONCURRENT = 5
MAX_TURNS = 30


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

EXCLUDED_TOOL_SETS = SANDBOX_TOOLS | COMPOSITION_TOOLS | NOTES_TOOLS


def build_resolver_servers() -> dict[str, McpServerConfig]:
    """Build MCP servers for the resolver agent."""
    s = default_settings
    servers: dict[str, McpServerConfig] = {
        "search": create_search_server(),
        "financial": create_financial_server(),
        "government": create_government_server(),
        "markets": create_markets_server(),
        "trends": create_trends_server(),
    }
    if s.reddit_client_id and s.reddit_client_secret:
        servers["reddit"] = create_reddit_server()
    if s.asknews_api_key:
        servers["asknews"] = McpHttpServerConfig(
            type="http",
            url="https://mcp.asknews.app",
            headers={"x-api-key": s.asknews_api_key},
        )
    return servers


def build_resolver_tools() -> list[str]:
    """Build allowed tool list using ToolPolicy (all tools except sandbox/composition/notes)."""
    policy = ToolPolicy.from_settings(default_settings)
    all_tools = policy.get_allowed_tools(allow_spawn=False)
    return [t for t in all_tools if t not in EXCLUDED_TOOL_SETS]


async def resolve_question(
    question: QuestionForResolution,
    *,
    mcp_servers: dict[str, McpServerConfig] | None = None,
    allowed_tools: list[str] | None = None,
) -> ResolutionVerdict:
    """Run a resolver agent to check if a question has resolved."""
    servers = mcp_servers or build_resolver_servers()
    tools = allowed_tools or build_resolver_tools()

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

    result_output: dict[str, object] | None = None
    async with build_client(
        model="opus",
        system_prompt=RESOLVER_SYSTEM_PROMPT,
        mcp_servers=servers,
        allowed_tools=tools,
        permission_mode="bypassPermissions",
        max_turns=MAX_TURNS,
        output_format={
            "type": "json_schema",
            "schema": ResolutionVerdict.model_json_schema(),
        },
    ) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, ResultMessage):
                result_output = message.structured_output

    if result_output:
        return ResolutionVerdict.model_validate(result_output)

    return ResolutionVerdict(
        resolved=False,
        resolution=None,
        confidence=0.0,
        reason="Agent produced no structured output",
        sources=[],
    )


async def resolve_batch(
    questions: list[QuestionForResolution],
    on_complete: Callable[[int, ResolutionVerdict], None] | None = None,
) -> list[tuple[int, ResolutionVerdict]]:
    """Resolve multiple questions concurrently with a semaphore limit."""
    servers = build_resolver_servers()
    tools = build_resolver_tools()
    semaphore = asyncio.Semaphore(MAX_CONCURRENT)

    async def resolve_one(
        q: QuestionForResolution,
    ) -> tuple[int, ResolutionVerdict]:
        try:
            async with semaphore:
                logger.info("Resolving post %d: %s", q.post_id, q.question_title[:60])
                verdict = await asyncio.shield(resolve_question(
                    q, mcp_servers=servers, allowed_tools=tools
                ))
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
