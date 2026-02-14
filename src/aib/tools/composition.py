"""Composition tools for agent spawning and sub-forecasting.

These tools enable the main forecasting agent to:
- Spawn specialized subagents (researcher, analyst, premortem) for parallel work
- Decompose questions and forecast sub-questions recursively

Subagents use ClaudeSDKClient with fully controlled system_prompt to prevent
runtime context injection (date, working directory) that would break retrodict.
"""

import asyncio
import logging
import uuid
from collections.abc import Awaitable, Callable
from datetime import date
from pathlib import Path
from typing import TYPE_CHECKING, Literal

if TYPE_CHECKING:
    from aib.tools.sandbox import Sandbox

from claude_agent_sdk import (
    AssistantMessage,
    ClaudeAgentOptions,
    ClaudeSDKClient,
    ResultMessage,
    TextBlock,
    tool,
)
from claude_agent_sdk.types import McpServerConfig
from pydantic import BaseModel, Field

from aib.agent.display import print_block
from aib.agent.models import ForecastOutput
from aib.agent.subagents import (
    ANALYST_PROMPT,
    PREMORTEM_PROMPT,
    RESEARCHER_PROMPT,
    SUBAGENT_MAX_TURNS,
    SUBAGENT_MODEL,
    analyst_tools,
    researcher_tools,
)
from aib.agent.hooks import create_allowed_tools_hook, merge_hooks
from aib.agent.retrodict import create_retrodict_hooks
from aib.retrodict_context import retrodict_cutoff
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success

logger = logging.getLogger(__name__)


# --- Dependencies (set by core.py) ---

_RunForecastFn = Callable[..., Awaitable["ForecastOutput"]]

_run_forecast_fn: _RunForecastFn | None = None


def set_run_forecast_fn(fn: _RunForecastFn) -> None:
    """Set the run_forecast function reference.

    Called by core.py after run_forecast is defined to enable
    subquestion agents to recursively call the forecasting pipeline.
    """
    global _run_forecast_fn
    _run_forecast_fn = fn


NetworkMode = Literal["bridge", "pypi_only", "none"]


class SandboxConfig(BaseModel):
    """Configuration for creating fresh analyst sandboxes."""

    network_mode: NetworkMode
    fake_date: date | None = None
    shared_dir: Path


_sandbox_config: SandboxConfig | None = None
_session_id: str | None = None


def set_sandbox_config(config: SandboxConfig) -> None:
    """Set sandbox configuration for analyst subagents."""
    global _sandbox_config
    _sandbox_config = config


def set_session_id(session_id: str) -> None:
    """Set the session ID for subagent notes servers."""
    global _session_id
    _session_id = session_id


# --- Input Schemas ---

SubagentType = Literal["researcher", "analyst", "premortem", "subquestion"]


class NumericBounds(BaseModel):
    """Bounds for numeric/discrete sub-questions."""

    range_min: float | None = None
    range_max: float | None = None
    open_lower_bound: bool = False
    open_upper_bound: bool = False
    zero_point: float | None = None


class SubagentSpec(BaseModel):
    """Specification for a single subagent to spawn.

    For researcher/analyst/premortem: provide type and prompt.
    For subquestion: provide type, question, context, and question_type.
    """

    type: SubagentType
    prompt: str = ""

    # subquestion-specific fields
    question: str = ""
    context: str = ""
    weight: float = 1.0
    question_type: str = "binary"
    options: list[str] = Field(default_factory=list)
    numeric_bounds: NumericBounds = Field(default_factory=NumericBounds)


class SpawnSubagentsInput(BaseModel):
    """Input for spawn_subagents tool."""

    agents: list[SubagentSpec] = Field(min_length=1)


# --- Subagent System Prompt ---


def _build_subagent_prompt(role_prompt: str) -> str:
    """Build system prompt for a subagent with effective date."""
    cutoff = retrodict_cutoff.get()
    effective_date = (cutoff or date.today()).isoformat()
    return f"Today's date is {effective_date}.\n\n{role_prompt}"


# --- MCP Server Factories ---


def _notes_base_for_session(session_id: str | None) -> Path | None:
    """Compute notes base path for retrodict mode."""
    if retrodict_cutoff.get() is not None and session_id:
        return Path(f"./tmp/notes/{session_id}")
    return None


def _researcher_mcp_servers(session_id: str | None) -> dict[str, McpServerConfig]:
    """Create MCP servers for researcher/premortem subagents."""
    from aib.tools.arxiv_search import arxiv_server
    from aib.tools.forecasting import create_forecasting_server
    from aib.tools.markets import create_markets_server
    from aib.tools.notes import create_notes_server
    from aib.tools.retrodict_search import create_retrodict_search_server

    servers: dict[str, McpServerConfig] = {
        "forecasting": create_forecasting_server(),
        "markets": create_markets_server(),
        "arxiv": arxiv_server,
        "notes": create_notes_server(
            session_id, notes_base=_notes_base_for_session(session_id)
        ),
    }
    if retrodict_cutoff.get() is not None:
        servers["search"] = create_retrodict_search_server()
    return servers


def _analyst_mcp_servers(
    session_id: str | None,
    sandbox_config: SandboxConfig,
) -> tuple[dict[str, McpServerConfig], "Sandbox"]:
    """Create MCP servers for analyst subagent with fresh sandbox.

    Args:
        session_id: Parent session ID for notes server.
        sandbox_config: Sandbox configuration for creating fresh containers.

    Returns:
        Tuple of (mcp_servers, sandbox). Caller must call sandbox.stop()
        after the subagent finishes.
    """
    from aib.tools.financial import financial_server
    from aib.tools.forecasting import create_forecasting_server
    from aib.tools.markets import create_markets_server
    from aib.tools.notes import create_notes_server
    from aib.tools.sandbox import Sandbox
    from aib.tools.trends import trends_server

    sandbox = Sandbox(
        session_id=f"analyst-{uuid.uuid4().hex[:8]}",
        shared_dir=sandbox_config.shared_dir,
        network_mode=sandbox_config.network_mode,
        fake_date=sandbox_config.fake_date,
    )
    sandbox.start()

    servers: dict[str, McpServerConfig] = {
        "sandbox": sandbox.create_mcp_server(),
        "forecasting": create_forecasting_server(),
        "markets": create_markets_server(),
        "financial": financial_server,
        "trends": trends_server,
        "notes": create_notes_server(
            session_id, notes_base=_notes_base_for_session(session_id)
        ),
    }
    return servers, sandbox


# --- Role Prompts ---

_ROLE_PROMPTS: dict[SubagentType, str] = {
    "researcher": RESEARCHER_PROMPT,
    "analyst": ANALYST_PROMPT,
    "premortem": PREMORTEM_PROMPT,
}


# --- Subagent Runners ---


class SubagentOutput(BaseModel):
    """Result from a single subagent execution."""

    type: str
    output: str = ""
    error: str | None = None

    # subquestion-specific fields
    question: str = ""
    weight: float = 1.0
    forecast: ForecastOutput | None = None


async def _run_claude_subagent(
    spec: SubagentSpec,
    *,
    session_id: str | None,
    sandbox_config: SandboxConfig | None,
) -> SubagentOutput:
    """Run a researcher, analyst, or premortem subagent via ClaudeSDKClient."""
    sandbox: Sandbox | None = None
    try:
        system_prompt = _build_subagent_prompt(_ROLE_PROMPTS[spec.type])

        if spec.type == "analyst":
            if sandbox_config is None:
                return SubagentOutput(
                    type=spec.type,
                    error="Sandbox config not set - call set_sandbox_config first",
                )
            servers, sandbox = _analyst_mcp_servers(session_id, sandbox_config)
            allowed = analyst_tools()
        else:
            servers = _researcher_mcp_servers(session_id)
            allowed = researcher_tools()

        options = ClaudeAgentOptions(
            system_prompt=system_prompt,
            model=SUBAGENT_MODEL[spec.type],
            max_turns=SUBAGENT_MAX_TURNS.get(spec.type, 5),
            allowed_tools=allowed,
            mcp_servers=servers,
            permission_mode="bypassPermissions",
            hooks=merge_hooks(  # type: ignore[arg-type]
                create_allowed_tools_hook(allowed),
                create_retrodict_hooks(),
            ),
            extra_args={"no-session-persistence": None},
        )

        prefix = f"  ↳ [{spec.type}] "
        logger.info("SUBAGENT [%s] START prompt=%s", spec.type, spec.prompt[:200])

        text_blocks: list[str] = []
        result: ResultMessage | None = None
        async with ClaudeSDKClient(options=options) as client:
            await client.query(spec.prompt)
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        print_block(block, prefix=prefix)
                        if isinstance(block, TextBlock):
                            text_blocks.append(block.text)
                elif isinstance(message, ResultMessage):
                    result = message

        collected_text = "\n\n".join(text_blocks)

        if result is None:
            if collected_text:
                logger.warning(
                    "SUBAGENT [%s] stream terminated without result, returning collected text",
                    spec.type,
                )
                return SubagentOutput(type=spec.type, output=collected_text)
            logger.warning(
                "SUBAGENT [%s] stream terminated without result or text", spec.type
            )
            return SubagentOutput(
                type=spec.type,
                error="Agent terminated prematurely — no result received",
            )

        if result.is_error:
            logger.warning("SUBAGENT [%s] ERROR: %s", spec.type, result.result)
            return SubagentOutput(
                type=spec.type,
                error=f"Agent error: {result.result}",
            )

        output = result.result or collected_text
        logger.info("SUBAGENT [%s] DONE output_len=%d", spec.type, len(output))
        return SubagentOutput(type=spec.type, output=output)

    except Exception as e:
        logger.exception("Subagent %s failed", spec.type)
        return SubagentOutput(type=spec.type, error=str(e))
    finally:
        if sandbox is not None:
            sandbox.stop()


async def _run_subforecast(spec: SubagentSpec) -> SubagentOutput:
    """Run a recursive sub-forecast via run_forecast()."""
    if _run_forecast_fn is None:
        return SubagentOutput(
            type="subquestion",
            question=spec.question,
            error="run_forecast not configured - call set_run_forecast_fn first",
        )

    question_type = spec.question_type
    context: dict[str, object] = {
        "title": spec.question,
        "type": question_type,
        "description": spec.context,
        "resolution_criteria": "",
        "fine_print": "",
    }

    if question_type == "multiple_choice" and spec.options:
        context["options"] = spec.options
    elif question_type in ("numeric", "discrete"):
        bounds = spec.numeric_bounds
        if bounds.range_min is not None or bounds.range_max is not None:
            context["numeric_bounds"] = bounds.model_dump(exclude_none=True)

    try:
        result = await _run_forecast_fn(
            question_context=context,
            allow_spawn=False,
        )

        return SubagentOutput(
            type="subquestion",
            question=spec.question,
            weight=spec.weight,
            forecast=result,
        )

    except Exception as e:
        logger.exception("Sub-forecast failed: %s", spec.question)
        return SubagentOutput(
            type="subquestion",
            question=spec.question,
            weight=spec.weight,
            error=str(e),
        )


# --- Tools ---


@tool(
    "spawn_subagents",
    (
        "Spawn specialized subagents for parallel work. Types:\n"
        "- researcher: Web search, news, Wikipedia, arXiv, prediction markets\n"
        "- analyst: Code execution, financial data, Google Trends, CP history\n"
        "- premortem: Devil's advocate that argues against your position\n"
        "- subquestion: Recursive sub-forecast with full pipeline\n\n"
        "Pass multiple agents to run them concurrently. Each gets its own "
        "isolated environment. Return format varies by type.\n\n"
        "USAGE EXAMPLES:\n\n"
        "Two researchers with different search angles:\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "researcher", "prompt": "Search for polling data and '
        "electoral projections for the 2026 German federal election. Focus on "
        'coalition scenarios and recent shifts in party support."},\n'
        '    {"type": "researcher", "prompt": "Search for economic conditions '
        "in Germany — unemployment rate, GDP growth, inflation — and how "
        'economic sentiment historically affects German election outcomes."}\n'
        "  ])\n\n"
        "Researcher + analyst in parallel:\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "researcher", "prompt": "Find recent news about FDA '
        "approval timeline for pembrolizumab combo therapy. Focus on advisory "
        'committee dates, CRLs, and comparable drug timelines."},\n'
        '    {"type": "analyst", "prompt": "Fetch AAPL stock history for 6mo '
        "using stock_history. Compute 30-day rolling volatility, then run "
        "Monte Carlo simulation of 10000 paths forward 14 days. Return "
        'percentile estimates at p10, p25, p50, p75, p90."}\n'
        "  ])\n\n"
        "Multi-subquestion decomposition (revenue segments):\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "subquestion", "question": "What will Google Search '
        'revenue be in Q1 2026?", "context": "Alphabet segment. Q1 2025 was '
        "$50.7B. Consider AI Overview impact on ad revenue and seasonal "
        'patterns.", "question_type": "numeric", "weight": 1.0},\n'
        '    {"type": "subquestion", "question": "What will YouTube revenue '
        'be in Q1 2026?", "context": "Alphabet segment. Q1 2025 was $8.9B. '
        "Consider Shorts monetization and connected TV "
        'growth.", "question_type": "numeric", "weight": 1.0},\n'
        '    {"type": "subquestion", "question": "What will Google Cloud '
        'revenue be in Q1 2026?", "context": "Alphabet segment. Q1 2025 was '
        "$12.3B growing ~28% YoY. Consider enterprise AI "
        'adoption.", "question_type": "numeric", "weight": 1.0}\n'
        "  ])\n"
        "  Then sum the sub-forecast medians and propagate uncertainty.\n\n"
        "Multi-subquestion decomposition (conditional chain):\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "subquestion", "question": "Will Country X formally '
        'apply to join Organization Y by mid-2026?", "context": "Application '
        "requires parliamentary vote. Current government interested but no "
        'formal motion.", "question_type": "binary", "weight": 1.0},\n'
        '    {"type": "subquestion", "question": "If applied, will all '
        'existing members approve by end of 2027?", "context": "Requires '
        "unanimous approval. Member Z has historically vetoed similar "
        'applications.", "question_type": "binary", "weight": 1.0},\n'
        '    {"type": "subquestion", "question": "If approved, will '
        'ratification complete before the deadline?", "context": "Ratification '
        "typically takes 6-18 months. Some members require parliamentary "
        'ratification.", "question_type": "binary", "weight": 1.0}\n'
        "  ])\n"
        "  Then multiply: P(join) = P(apply) × P(approve|apply) × P(ratify|approve).\n\n"
        "Premortem after forming initial estimate:\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "premortem", "prompt": "Question: \'Will the EU AI Act '
        "enforcement begin by July 2026?' My preliminary forecast: 72% YES. "
        "I'm anchoring on the official timeline and published roadmap. Argue "
        "against — what concrete risks of delay am I "
        'underweighting?"}\n'
        "  ])\n\n"
        "Mixed types (research + analysis + sub-forecast):\n"
        "  spawn_subagents(agents=[\n"
        '    {"type": "researcher", "prompt": "Find recent news about Company '
        "X's drug pipeline. Focus on Phase 3 trial readouts expected in the "
        'next 6 months."},\n'
        '    {"type": "analyst", "prompt": "Get Company X quarterly financials '
        "via company_financials('TICKER'). Compute revenue growth trajectory "
        'and R&D spending trend."},\n'
        '    {"type": "subquestion", "question": "Will the FDA advisory '
        'committee vote favorably for Drug Y?", "context": "Phase 3 OS '
        "benefit HR=0.74, p=0.003. Safety: 12% grade 3+ "
        'hepatotoxicity.", "question_type": "binary", "weight": 0.8}\n'
        "  ])\n"
    ),
    SpawnSubagentsInput.model_json_schema(),
)
@tracked("spawn_subagents")
async def spawn_subagents(
    args: dict[str, object],
) -> dict[str, object]:
    """Spawn parallel subagents for research, analysis, and sub-forecasting."""
    try:
        validated = SpawnSubagentsInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    # Snapshot module-level config before asyncio.gather to avoid races:
    # concurrent subquestions call run_forecast() which overwrites these globals.
    session_id = _session_id
    sandbox_config = _sandbox_config

    async def run_one(spec: SubagentSpec) -> SubagentOutput:
        if spec.type == "subquestion":
            return await _run_subforecast(spec)
        return await _run_claude_subagent(
            spec, session_id=session_id, sandbox_config=sandbox_config
        )

    results = await asyncio.gather(*[run_one(s) for s in validated.agents])

    errors = [r for r in results if r.error is not None]
    successful = [r for r in results if r.error is None]

    if not successful:
        error_msgs = [r.error for r in errors]
        return mcp_error(f"All subagents failed: {error_msgs}")

    return mcp_success(
        {
            "results": [r.model_dump(exclude_none=True) for r in results],
            "successful_count": len(successful),
            "failed_count": len(errors),
        }
    )


# --- MCP Server ---

composition_server = create_mcp_server(
    name="composition",
    version="3.0.0",
    tools=[spawn_subagents],
)
