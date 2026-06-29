"""Worldview manager — maintenance sub-agent for the worldview store.

Spawns a sub-agent that has full read/write access to the worldview store
via dedicated MCP tools. The sub-agent decides what to do — cleanup,
deduplicate, link research to forecasts, reconcile contradictions, and
trigger AI resolution for ready subforecasts. All semantic judgments are
made by the agent rather than by keyword heuristics.
"""

import asyncio
import logging
from collections.abc import Iterator
from contextlib import contextmanager
from contextvars import ContextVar
from datetime import datetime, timezone
from typing import Literal

from claude_agent_sdk import AssistantMessage, ResultMessage
from claude_agent_sdk.types import TextBlock
from pydantic import BaseModel, Field

from aib.agent.client import REMOVE, build_client
from aib.tools.metrics import get_collector
from aib.agent.display import make_agent_prefix, print_block
from aib.agent.hooks import create_allowed_tools_hook
from aib.agent.resolver import (
    QuestionForResolution,
    ResolutionVerdict,
    resolve_question,
)
from aib.paths import WORLDVIEW_PATH
from aib.tools.decorator import ToolError, mcp_tool
from aib.tools.mcp_server import create_mcp_server
from aib.worldview.lookup import (
    all_slugs,
    archive_entry,
    commit_worldview,
    iter_forecast_entries,
    iter_research_entries,
    load_forecast_entry,
    load_research_entry,
    resolve_forecast_entry,
    save_forecast_entry,
    supersede_entry,
)
from aib.worldview.models import (
    EntryState,
    WorldviewForecastEntry,
)

logger = logging.getLogger(__name__)


def score_binary_forecast(probability: float, resolution: float) -> float:
    """Brier score for a binary forecast."""
    return (probability - resolution) ** 2


# ── Structural helpers (no semantic judgment) ────────────────────


def find_resolvable_forecasts() -> list[WorldviewForecastEntry]:
    """Return forecast entries with resolvable_after <= now and not yet resolved."""
    now = datetime.now(timezone.utc)
    return [
        e
        for e in iter_forecast_entries()
        if not e.resolved
        and e.resolvable_after is not None
        and e.resolvable_after <= now
        and e.state != EntryState.resolved
    ]


async def resolve_ready_forecasts(
    *,
    dry_run: bool = False,
    min_confidence: float = 0.7,
    max_concurrent: int = 3,
) -> list[dict[str, object]]:
    """Run AI resolution on every forecast whose resolvable_after has passed.

    Structural sweep — no semantic judgment. For dedup/linking/contradiction
    maintenance, use run_worldview_refresh (survey + fix) instead.
    """
    resolvable = find_resolvable_forecasts()
    if not resolvable:
        return []

    semaphore = asyncio.Semaphore(max_concurrent)
    results: list[dict[str, object]] = []

    async def resolve_one(entry: WorldviewForecastEntry) -> dict[str, object]:
        question = QuestionForResolution(
            post_id=entry.parent_post_id or 0,
            question_title=entry.question,
            question_type=entry.question_type,
            resolution_criteria=entry.summary,
            fine_print="",
            description=entry.reasoning or "",
        )
        try:
            async with semaphore:
                report = await resolve_question(question)
                verdict = report.payload or ResolutionVerdict(
                    resolved=False,
                    resolution=None,
                    confidence=0.0,
                    reason="Agent produced no structured output",
                    sources=[],
                )
        except (RuntimeError, ValueError) as exc:
            logger.exception("Resolution failed for %s", entry.slug)
            return {
                "slug": entry.slug,
                "question": entry.question,
                "resolved": False,
                "error": f"{type(exc).__name__}: {exc}",
            }

        record: dict[str, object] = {
            "slug": entry.slug,
            "question": entry.question,
            "resolved": verdict.resolved,
            "confidence": verdict.confidence,
            "reason": verdict.reason,
        }

        if not verdict.resolved or verdict.confidence < min_confidence:
            return record
        if verdict.resolution is None:
            return record
        if not isinstance(verdict.resolution, (int, float)):
            logger.warning(
                "Resolver for %s returned non-numeric resolution %r; skipping",
                entry.slug,
                verdict.resolution,
            )
            return record

        resolution = float(verdict.resolution)
        score: float | None = None
        if entry.question_type == "binary" and entry.probability is not None:
            score = score_binary_forecast(entry.probability, resolution)

        if not dry_run:
            resolve_forecast_entry(
                entry.slug,
                resolution=resolution,
                resolution_source="worldview_auto_resolver",
                score=score,
            )

        record["resolution"] = resolution
        record["score"] = score
        return record

    coros = [resolve_one(e) for e in resolvable]
    results = await asyncio.gather(*coros)
    return results


# ── Maintenance sub-agent MCP tools ──────────────────────────────


class ListEntriesInput(BaseModel):
    """Input for wv_list_entries."""

    kind: Literal["research", "forecast", "all"] = Field(
        default="all",
        description="Which kind of entries to list.",
    )
    include_superseded: bool = Field(
        default=False,
        description="Include entries already marked as superseded.",
    )


@mcp_tool(
    "wv_list_entries",
    (
        "List worldview entries with summary info (slug, kind, query/question, "
        "state, updated_at, tags, resolvable_after). Call this first to see "
        "what exists; then use wv_read_entry to drill into specific entries."
    ),
)
async def wv_list_entries(args: ListEntriesInput) -> dict[str, object]:
    """List worldview entries (summaries only)."""
    entries: list[dict[str, object]] = []

    if args.kind in ("research", "all"):
        for r in iter_research_entries():
            if not args.include_superseded and r.state == EntryState.superseded:
                continue
            entries.append(
                {
                    "slug": r.slug,
                    "kind": "research",
                    "query": r.query,
                    "state": r.state.value,
                    "updated_at": r.updated_at.isoformat(),
                    "stale_after": r.stale_after.isoformat(),
                }
            )

    if args.kind in ("forecast", "all"):
        for f in iter_forecast_entries():
            if not args.include_superseded and f.state == EntryState.superseded:
                continue
            entries.append(
                {
                    "slug": f.slug,
                    "kind": "forecast",
                    "question": f.question,
                    "question_type": f.question_type,
                    "state": f.state.value,
                    "parent_post_id": f.parent_post_id,
                    "resolvable_after": (
                        f.resolvable_after.isoformat() if f.resolvable_after else None
                    ),
                    "resolved": f.resolved,
                    "updated_at": f.updated_at.isoformat(),
                    "stale_after": f.stale_after.isoformat(),
                    "tags": list(f.tags),
                }
            )

    return {"count": len(entries), "entries": entries}


class ReadEntryInput(BaseModel):
    """Input for wv_read_entry."""

    slug: str = Field(description="Slug of the entry to read.")
    kind: Literal["research", "forecasts"]


@mcp_tool(
    "wv_read_entry",
    (
        "Read a worldview entry in full. Use this to inspect details before "
        "deciding to archive, supersede, tag, or resolve it."
    ),
)
async def wv_read_entry(args: ReadEntryInput) -> dict[str, object]:
    """Read a worldview entry in full."""
    if args.kind == "research":
        entry = load_research_entry(args.slug)
    else:
        entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Entry {args.slug!r} ({args.kind}) not found")
    return entry.model_dump(mode="json")


class ArchiveEntryInput(BaseModel):
    """Input for wv_archive_entry."""

    slug: str
    kind: Literal["research", "forecasts"]
    reason: str = Field(
        description="Why this entry is being archived (e.g., 'resolved', 'past 2xTTL').",
    )


@mcp_tool(
    "wv_archive_entry",
    (
        "Move an entry to the worldview archive directory. Use for resolved "
        "entries or ones clearly past their stale window. Include a reason."
    ),
)
async def wv_archive_entry(args: ArchiveEntryInput) -> dict[str, object]:
    """Archive a worldview entry."""
    success = archive_entry(args.slug, args.kind)
    if not success:
        raise ToolError(f"Entry {args.slug!r} ({args.kind}) not found")
    logger.info(
        "Maintenance agent archived %s %s: %s", args.kind, args.slug, args.reason
    )
    return {"archived": args.slug, "kind": args.kind, "reason": args.reason}


class SupersedeEntryInput(BaseModel):
    """Input for wv_supersede_entry."""

    older_slug: str
    newer_slug: str
    kind: Literal["research", "forecasts"]
    reason: str = Field(
        description="Why the older entry is superseded by the newer one.",
    )


@mcp_tool(
    "wv_supersede_entry",
    (
        "Mark an older entry as superseded by a newer one. Use only when two "
        "entries genuinely cover the same question (not just share keywords). "
        "Include a reason explaining why they are redundant."
    ),
)
async def wv_supersede_entry(args: SupersedeEntryInput) -> dict[str, object]:
    """Supersede an older worldview entry with a newer one."""
    if args.older_slug == args.newer_slug:
        raise ToolError("older_slug and newer_slug must differ")

    success = supersede_entry(args.older_slug, args.kind, args.newer_slug)
    if not success:
        raise ToolError(f"Entry {args.older_slug!r} ({args.kind}) not found")
    logger.info(
        "Maintenance agent superseded %s %s by %s: %s",
        args.kind,
        args.older_slug,
        args.newer_slug,
        args.reason,
    )
    return {
        "superseded": args.older_slug,
        "superseded_by": args.newer_slug,
        "kind": args.kind,
        "reason": args.reason,
    }


class ReconcileInput(BaseModel):
    """Input for wv_reconcile."""

    claim: str = Field(
        description=(
            "The disputed factual claim to re-research, phrased as a precise "
            "current-state question (e.g., 'What is the current status of the "
            "Knesset dissolution bill as of today?')."
        ),
    )
    conflicting_slugs: list[str] = Field(
        description=(
            "Slugs of the research entries that disagree and should be "
            "superseded by the fresh, authoritative entry."
        ),
    )
    ttl: str = Field(
        default="1d",
        description="Cache lifetime for the reconciled entry (6h, 12h, 1d, 3d, 7d, 14d).",
    )


@mcp_tool(
    "wv_reconcile",
    (
        "Reconcile a contradiction by re-researching the disputed claim and "
        "superseding the conflicting entries with one fresh, authoritative "
        "note that resolves the disagreement. Use this instead of merely "
        "noting a contradiction — the store should converge on one current "
        "truth per fact."
    ),
)
async def wv_reconcile(args: ReconcileInput) -> dict[str, object]:
    """Re-research a disputed claim and supersede the conflicting entries."""
    from aib.tools.research import ResearchQuestion, run_single_research

    missing = [s for s in args.conflicting_slugs if load_research_entry(s) is None]
    if missing:
        raise ToolError(f"Conflicting slugs not found: {', '.join(missing)}")

    result = await run_single_research(
        ResearchQuestion(query=args.claim, ttl=args.ttl),
        all_slugs(),
    )
    if result.entry is None:
        raise ToolError(f"Re-research failed: {result.error or 'no entry produced'}")

    new_slug = result.entry.slug
    superseded: list[str] = []
    for slug in args.conflicting_slugs:
        if slug == new_slug:
            continue
        if supersede_entry(slug, "research", new_slug):
            superseded.append(slug)
    logger.info("Maintenance agent reconciled %s into %s", superseded, new_slug)
    return {
        "reconciled_into": new_slug,
        "superseded": superseded,
        "claim": args.claim,
    }


class TagForecastInput(BaseModel):
    """Input for wv_tag_forecast."""

    slug: str = Field(description="Slug of the forecast entry to tag.")
    tags: list[str] = Field(
        description=(
            "Tags to add. Tags are merged with existing tags. "
            "Use 'research:<slug>' to link a research entry to this forecast."
        ),
    )


@mcp_tool(
    "wv_tag_forecast",
    (
        "Add tags to a forecast entry. Commonly used to link research to "
        "forecasts with a 'research:<slug>' tag. Tags are merged into the "
        "existing tag set. Only forecast entries are taggable."
    ),
)
async def wv_tag_forecast(args: TagForecastInput) -> dict[str, object]:
    """Add tags to a forecast entry."""
    forecast = load_forecast_entry(args.slug)
    if forecast is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")
    merged = sorted(set(forecast.tags) | set(args.tags))
    save_forecast_entry(forecast.model_copy(update={"tags": merged}))
    return {"slug": args.slug, "tags": merged}


class ResolveForecastInput(BaseModel):
    """Input for wv_resolve_forecast."""

    slug: str
    resolution: float = Field(
        description=(
            "Resolution value. For binary: 1.0 for YES, 0.0 for NO. "
            "For numeric: the actual resolved value."
        ),
    )
    source: str = Field(
        description="Where the resolution came from (e.g., 'ai_resolver', 'manual').",
    )


@mcp_tool(
    "wv_resolve_forecast",
    (
        "Set the resolution for a worldview forecast entry. Use only after "
        "you have verified the resolution from a reliable source. Automatically "
        "computes the Brier score for binary forecasts."
    ),
)
async def wv_resolve_forecast(args: ResolveForecastInput) -> dict[str, object]:
    """Resolve a worldview forecast entry."""
    entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")

    score: float | None = None
    if entry.question_type == "binary" and entry.probability is not None:
        score = score_binary_forecast(entry.probability, args.resolution)

    resolve_forecast_entry(
        args.slug,
        resolution=args.resolution,
        resolution_source=args.source,
        score=score,
    )
    return {
        "resolved": args.slug,
        "resolution": args.resolution,
        "source": args.source,
        "score": score,
    }


class AiResolveForecastInput(BaseModel):
    """Input for wv_ai_resolve_forecast."""

    slug: str = Field(description="Slug of the forecast entry to resolve via AI.")


@mcp_tool(
    "wv_ai_resolve_forecast",
    (
        "Run the AI resolver agent on a forecast entry. Returns the resolver's "
        "verdict with confidence and reasoning. Use this for subforecasts where "
        "resolvable_after has passed. Review the verdict before calling "
        "wv_resolve_forecast to record it."
    ),
)
async def wv_ai_resolve_forecast(
    args: AiResolveForecastInput,
) -> dict[str, object]:
    """Run AI resolution on a worldview forecast entry."""
    entry = load_forecast_entry(args.slug)
    if entry is None:
        raise ToolError(f"Forecast entry {args.slug!r} not found")

    question = QuestionForResolution(
        post_id=entry.parent_post_id or 0,
        question_title=entry.question,
        question_type=entry.question_type,
        resolution_criteria=entry.summary,
        fine_print="",
        description=entry.reasoning or "",
    )
    report = await resolve_question(question)
    verdict = report.payload or ResolutionVerdict(
        resolved=False,
        resolution=None,
        confidence=0.0,
        reason="Agent produced no structured output",
        sources=[],
    )
    return verdict.model_dump(mode="json")


class RefreshEntryInput(BaseModel):
    """Input for wv_refresh."""

    slug: str = Field(description="Slug of the research entry to re-research in place.")


@mcp_tool(
    "wv_refresh",
    (
        "Re-research a research entry in place, keeping its slug and TTL. Use "
        "for an outdated entry to replace it with the current state of the "
        "world; the prior version is archived as a trajectory snapshot."
    ),
)
async def wv_refresh(args: RefreshEntryInput) -> dict[str, object]:
    """Re-research a stale research entry in place."""
    from aib.tools.research import refresh_research_entry

    entry = load_research_entry(args.slug)
    if entry is None:
        raise ToolError(f"Research entry {args.slug!r} not found")
    result = await refresh_research_entry(entry)
    if result.entry is None:
        raise ToolError(f"Refresh failed: {result.error or 'no entry produced'}")
    return {
        "refreshed": args.slug,
        "stale_after": result.entry.stale_after.isoformat(),
    }


# ── Survey + fix agents ───────────────────────────────────────────


class Issue(BaseModel):
    """One issue in the worldview store, registered by the survey agent."""

    kind: Literal[
        "contradiction", "outdated", "duplicate", "missing_link", "resolvable"
    ] = Field(description="The kind of issue.")
    description: str = Field(description="What the issue is, in one sentence.")
    slugs: list[str] = Field(
        default_factory=list,
        description="Slugs of the entries involved.",
    )
    claim: str | None = Field(
        default=None,
        description=(
            "For contradiction/outdated: the precise current-state question to "
            "re-research (e.g., 'What is the current status of X as of today?')."
        ),
    )


survey_issues: ContextVar[list[Issue] | None] = ContextVar(
    "survey_issues", default=None
)


@mcp_tool(
    "add_issue",
    (
        "Register one issue you found in the worldview store. Call once per "
        "distinct issue. Kinds: 'contradiction' (entries disagree on a metric), "
        "'outdated' (an entry is stale or the world moved), 'duplicate' (two "
        "entries cover the same question), 'missing_link' (a forecast's evidence "
        "is an untagged research entry), 'resolvable' (a forecast past its "
        "resolve date). For contradiction/outdated, include the precise claim "
        "to re-research."
    ),
)
async def add_issue(args: Issue) -> dict[str, object]:
    """Register an issue during a survey."""
    issues = survey_issues.get()
    if issues is None:
        raise ToolError("add_issue called outside a survey run")
    issues.append(args)
    return {"registered": args.kind, "total": len(issues)}


SURVEY_TOOLS = [wv_list_entries, wv_read_entry, add_issue]

SURVEY_TOOL_NAMES = [
    "mcp__worldview_maintenance__wv_list_entries",
    "mcp__worldview_maintenance__wv_read_entry",
    "mcp__worldview_maintenance__add_issue",
]

FIX_TOOLS = [
    wv_read_entry,
    wv_reconcile,
    wv_refresh,
    wv_supersede_entry,
    wv_tag_forecast,
    wv_ai_resolve_forecast,
    wv_resolve_forecast,
    wv_archive_entry,
]

FIX_TOOL_NAMES = [
    "mcp__worldview_maintenance__wv_read_entry",
    "mcp__worldview_maintenance__wv_reconcile",
    "mcp__worldview_maintenance__wv_refresh",
    "mcp__worldview_maintenance__wv_supersede_entry",
    "mcp__worldview_maintenance__wv_tag_forecast",
    "mcp__worldview_maintenance__wv_ai_resolve_forecast",
    "mcp__worldview_maintenance__wv_resolve_forecast",
    "mcp__worldview_maintenance__wv_archive_entry",
]


SURVEY_SYSTEM_PROMPT = """\
You are the survey agent for the worldview store — a cache of factual notes
(research entries) and subforecasts that the forecasting pipeline relies on.

Your ONLY job is to read the whole store and register every issue you find by
calling `add_issue` once per distinct issue. You do NOT fix anything.

Issue kinds:
- **contradiction** — two or more research entries report different values for
  the same metric. Include the conflicting slugs and a precise `claim` (a
  current-state question to re-research).
- **outdated** — a research entry that looks out of date even though it is NOT
  marked `stale` (entries already marked `stale` are auto-queued for refresh, so
  do not register those). Include the slug and a `claim`.
- **duplicate** — two entries genuinely cover the same question (not just share
  keywords). Include both slugs.
- **missing_link** — a forecast whose primary evidence is a research entry that
  is not tagged `research:<slug>`. Include the forecast and research slugs.
- **resolvable** — a forecast whose `resolvable_after` has passed and is not
  yet resolved. Include the forecast slug.

## How to work

1. Call `wv_list_entries` to see everything, including each entry's state and
   staleness.
2. Read the entries you need with `wv_read_entry` to judge contradictions and
   duplicates — compare their actual content, not just titles.
3. Register each issue with `add_issue`. Be precise and conservative: register
   an issue only when it is clear. Related-but-distinct entries are not a
   contradiction or a duplicate.
4. Do not register the same issue twice. When you have surveyed the whole
   store, stop.
"""


FIX_SYSTEM_PROMPT = """\
You are a fix agent for the worldview store. You are given ONE issue and must
resolve it, then report what you did in one or two sentences.

Resolve by issue kind:
- **contradiction** — call `wv_reconcile` with the claim and the conflicting
  slugs. It re-researches the claim and supersedes the stale entries with one
  fresh, authoritative note.
- **outdated** — call `wv_refresh` on the slug to replace it with the current
  state of the world.
- **duplicate** — read both; `wv_supersede_entry` the older one by the newer.
- **missing_link** — `wv_tag_forecast` the forecast with `research:<slug>`.
- **resolvable** — `wv_ai_resolve_forecast` the forecast; if the verdict is
  confident and the reasoning holds, `wv_resolve_forecast` to record it.
  Otherwise leave it unresolved — a later sweep will re-attempt it.

Read the entries first if you need to. Act only on this one issue. If on
inspection the issue is not real, do nothing and say so.
"""


async def run_survey() -> list[Issue]:
    """Spawn the read-only survey agent; return the issues it registered."""
    WORLDVIEW_PATH.mkdir(parents=True, exist_ok=True)
    issues: list[Issue] = []
    token = survey_issues.set(issues)

    survey_server = create_mcp_server("worldview_maintenance", tools=SURVEY_TOOLS)
    prefix = make_agent_prefix("worldview-survey", None)

    from aib.config import settings

    try:
        async with build_client(
            model=settings.model,
            system_prompt=SURVEY_SYSTEM_PROMPT,
            permission_mode="bypassPermissions",
            cwd=str(WORLDVIEW_PATH),
            extra_args={"no-session-persistence": REMOVE},
            allowed_tools=SURVEY_TOOL_NAMES,
            hooks=create_allowed_tools_hook(SURVEY_TOOL_NAMES),
            mcp_servers={"worldview_maintenance": survey_server},
        ) as client:
            await client.query(
                "Survey the worldview store and register every issue you find."
            )
            async for message in client.receive_response():
                if isinstance(message, AssistantMessage):
                    for block in message.content:
                        print_block(block, prefix=prefix)
                if isinstance(message, ResultMessage):
                    if message.total_cost_usd is not None:
                        get_collector().record_cost(
                            "worldview_survey", message.total_cost_usd
                        )
    finally:
        survey_issues.reset(token)

    return issues


async def fix_issue(issue: Issue) -> str:
    """Spawn a fix agent to resolve one issue; return its report."""
    fix_server = create_mcp_server("worldview_maintenance", tools=FIX_TOOLS)
    prefix = make_agent_prefix("worldview-fix", issue.kind)

    from aib.config import settings

    text_blocks: list[str] = []
    prompt = (
        f"Issue kind: {issue.kind}\n"
        f"Description: {issue.description}\n"
        f"Entries: {', '.join(issue.slugs) or '(none)'}\n"
        f"Claim to research: {issue.claim or '(none)'}\n\n"
        "Resolve this issue, then report what you did."
    )
    async with build_client(
        model=settings.model,
        system_prompt=FIX_SYSTEM_PROMPT,
        permission_mode="bypassPermissions",
        cwd=str(WORLDVIEW_PATH),
        extra_args={"no-session-persistence": REMOVE},
        allowed_tools=FIX_TOOL_NAMES,
        hooks=create_allowed_tools_hook(FIX_TOOL_NAMES),
        mcp_servers={"worldview_maintenance": fix_server},
    ) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                for block in message.content:
                    print_block(block, prefix=prefix)
                    if isinstance(block, TextBlock):
                        text_blocks.append(block.text)
            if isinstance(message, ResultMessage):
                if message.total_cost_usd is not None:
                    get_collector().record_cost("worldview_fix", message.total_cost_usd)

    return text_blocks[-1] if text_blocks else f"{issue.kind}: no report"


# ── Standalone refresh loop ───────────────────────────────────────


@contextmanager
def worldview_research_session() -> Iterator[None]:
    """Enter a session with research MCP servers for standalone worldview work.

    Refresh and reconcile both run the research sub-agent, which reads its data
    tools from the active session. Outside a forecast there is no session, so we
    build the data-gathering servers (no sandbox — fact lookup needs no code
    execution) and enter a session for the duration of the sweep.
    """
    from aib.agent.session import ForecastSession, reset_session, set_session
    from aib.agent.tool_policy import ToolPolicy
    from aib.config import settings

    policy = ToolPolicy.from_settings(settings)
    session = ForecastSession(research_mcp_servers=policy.get_research_mcp_servers())
    set_session(session)
    try:
        yield
    finally:
        reset_session()


class WorldviewRefreshReport(BaseModel):
    """Result of one worldview survey + fix cycle."""

    issues_found: list[Issue] = Field(default_factory=list)
    fixes: list[str] = Field(default_factory=list)
    dry_run: bool = False
    committed: bool = False


def stale_outdated_issues() -> list[Issue]:
    """Queue every TTL-expired research entry for refresh (deterministic)."""
    return [
        Issue(
            kind="outdated",
            description=f"TTL expired; stale since {entry.stale_after.isoformat()}.",
            slugs=[entry.slug],
            claim=entry.query,
        )
        for entry in iter_research_entries()
        if entry.state == EntryState.stale
    ]


async def run_worldview_refresh(
    *, max_concurrent: int = 3, dry_run: bool = False
) -> WorldviewRefreshReport:
    """Survey the worldview store, then fan out a fix agent per issue.

    Every TTL-expired research entry is queued for refresh deterministically; a
    read-only survey agent then registers the remaining issues (contradiction,
    duplicate, missing_link, resolvable, and any non-stale outdated). A fix agent
    resolves each issue in parallel, inside a research-capable session. When
    dry_run is set, issues are collected but no fix agents are spawned.
    """
    with worldview_research_session():
        seeded = stale_outdated_issues()
        seeded_slugs = {slug for issue in seeded for slug in issue.slugs}
        surveyed = await run_survey()
        deduped = [
            issue
            for issue in surveyed
            if not (
                issue.kind == "outdated"
                and any(slug in seeded_slugs for slug in issue.slugs)
            )
        ]
        issues = seeded + deduped
        if dry_run or not issues:
            return WorldviewRefreshReport(issues_found=issues, dry_run=dry_run)

        semaphore = asyncio.Semaphore(max_concurrent)

        async def fix_one(issue: Issue) -> str:
            async with semaphore:
                return await fix_issue(issue)

        fixes = await asyncio.gather(*[fix_one(i) for i in issues])

    committed = commit_worldview("worldview: survey + fix sweep")
    return WorldviewRefreshReport(
        issues_found=issues,
        fixes=list(fixes),
        committed=committed,
    )
