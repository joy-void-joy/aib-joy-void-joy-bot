"""Worldview entry schemas for research and sub-forecast persistence.

These models define the structure of entries in the worldview store
(notes/worldview/). Research entries capture factual findings; forecast
entries capture predictions with CDF, resolution tracking, and scoring.
"""

import hashlib
import re
from datetime import datetime, timezone
from enum import StrEnum
from typing import TYPE_CHECKING
from unicodedata import normalize

from pydantic import BaseModel, Field, model_validator

from aib.agent.models import Factor
from aib.version import AGENT_VERSION

if TYPE_CHECKING:
    from aib.agent.models import ForecastOutput


class EntryState(StrEnum):
    fresh = "fresh"
    stale = "stale"
    superseded = "superseded"
    resolved = "resolved"


# ── Shared sub-models ──────────────────────────────────────────────


class Source(BaseModel):
    url: str
    title: str
    domain: str
    accessed_at: str = Field(
        description="ISO 8601 datetime when the source was accessed."
    )
    snippet: str | None = None


class DataPoint(BaseModel):
    metric: str
    value: float
    unit: str
    as_of: str = Field(description="ISO 8601 date for the data point.")
    source_url: str


class Revision(BaseModel):
    timestamp: datetime
    fields_changed: list[str]
    reason: str


class NumericBounds(BaseModel):
    range_min: float | None = None
    range_max: float | None = None
    open_lower_bound: bool = False
    open_upper_bound: bool = False
    zero_point: float | None = None

    @model_validator(mode="after")
    def check_bounds_order(self) -> "NumericBounds":
        if self.range_min is not None and self.range_max is not None:
            if self.range_max < self.range_min:
                raise ValueError(
                    f"range_max ({self.range_max}) must be >= range_min ({self.range_min})"
                )
        return self


# ── Slug generation ────────────────────────────────────────────────

SLUG_MAX_LENGTH = 50
SLUG_HASH_CHARS = 8

NON_ALNUM_RE = re.compile(r"[^a-z0-9]+")


def slugify_topic(text: str, max_length: int = SLUG_MAX_LENGTH) -> str:
    """Convert text to kebab-case slug: lowercase, strip accents, collapse non-alnum to hyphens."""
    text = normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = NON_ALNUM_RE.sub("-", text.lower()).strip("-")
    if len(text) > max_length:
        text = text[:max_length].rstrip("-")
    return text


def make_slug(topic: str, existing_slugs: set[str] | None = None) -> str:
    """Generate a worldview slug from a topic description.

    Format: {kebab-case-topic}-{8-char-hash}
    Uses 8 hex chars for disambiguation (~4 billion possibilities).
    If existing_slugs is provided, detects and resolves collisions
    by rehashing with an attempt counter.
    """
    kebab = slugify_topic(topic)
    hash_suffix = hashlib.sha256(topic.encode()).hexdigest()[:SLUG_HASH_CHARS]
    slug = f"{kebab}-{hash_suffix}"
    if existing_slugs is not None:
        attempt = 1
        while slug in existing_slugs:
            hash_suffix = hashlib.sha256(f"{topic}:{attempt}".encode()).hexdigest()[
                :SLUG_HASH_CHARS
            ]
            slug = f"{kebab}-{hash_suffix}"
            attempt += 1
    return slug


# ── Research entry ─────────────────────────────────────────────────


class WorldviewResearchEntry(BaseModel):
    slug: str
    query: str
    answer: str
    sources: list[Source] = Field(default_factory=list)
    key_facts: list[str] = Field(default_factory=list)
    data_points: list[DataPoint] = Field(default_factory=list)

    created_at: datetime
    updated_at: datetime
    stale_after: datetime
    resolvable_after: datetime | None = None
    state: EntryState = EntryState.fresh
    superseded_by: str | None = None
    revision_history: list[Revision] = Field(default_factory=list)
    session_id: str | None = None
    follow_up_count: int = 0


# ── Forecast entry ─────────────────────────────────────────────────


class WorldviewForecastEntry(BaseModel):
    slug: str
    question: str
    question_type: str

    # Core forecast (mirrors ForecastOutput fields)
    probability: float | None = None
    probabilities: dict[str, float] | None = None
    median: float | None = None
    confidence_interval: tuple[float, float] | None = None
    percentiles: dict[int, float] | None = None
    cdf: list[float] | None = None
    numeric_bounds: NumericBounds | None = None
    factors: list[Factor] = Field(default_factory=list)
    summary: str = ""
    reasoning: str = ""

    # Metadata
    created_at: datetime
    updated_at: datetime
    stale_after: datetime
    resolvable_after: datetime | None = None
    state: EntryState = EntryState.fresh
    superseded_by: str | None = None
    revision_history: list[Revision] = Field(default_factory=list)
    agent_version: str = AGENT_VERSION
    parent_post_id: int | None = None
    parent_slug: str | None = None
    depth: int = 0
    tags: list[str] = Field(default_factory=list)
    cost_usd: float | None = None
    duration_seconds: float | None = None

    # Resolution tracking
    resolved: bool = False
    resolution: float | str | None = None
    resolved_at: datetime | None = None
    resolution_source: str | None = None
    score: float | None = None


# ── Conversion helpers ─────────────────────────────────────────────


def from_forecast_output(
    output: "ForecastOutput",
    slug: str,
    stale_after: datetime,
    resolvable_after: datetime | None,
    parent_post_id: int | None,
    parent_slug: str | None = None,
    depth: int = 0,
    tags: list[str] | None = None,
) -> WorldviewForecastEntry:
    """Convert a ForecastOutput from a subforecast run into a worldview entry."""
    now = datetime.now(timezone.utc)
    return WorldviewForecastEntry(
        slug=slug,
        question=output.question_title,
        question_type=output.question_type,
        probability=output.probability,
        probabilities=output.probabilities,
        median=output.median,
        confidence_interval=output.confidence_interval,
        percentiles=output.percentiles,
        cdf=output.cdf,
        factors=output.factors,
        summary=output.summary,
        reasoning=output.reasoning,
        created_at=now,
        updated_at=now,
        stale_after=stale_after,
        resolvable_after=resolvable_after,
        agent_version=AGENT_VERSION,
        parent_post_id=parent_post_id,
        parent_slug=parent_slug,
        depth=depth,
        tags=tags or [],
        cost_usd=output.cost_usd,
        duration_seconds=output.duration_seconds,
    )


def to_forecast_output(
    entry: WorldviewForecastEntry,
    question_id: int = 0,
    post_id: int = 0,
) -> "ForecastOutput":
    """Convert a worldview entry back to ForecastOutput for CDF extraction."""
    from aib.agent.models import ForecastOutput

    return ForecastOutput(
        question_id=question_id,
        post_id=post_id,
        question_title=entry.question,
        question_type=entry.question_type,
        probability=entry.probability,
        probabilities=entry.probabilities,
        median=entry.median,
        confidence_interval=entry.confidence_interval,
        percentiles=entry.percentiles,
        cdf=entry.cdf,
        factors=entry.factors,
        summary=entry.summary,
        reasoning=entry.reasoning,
    )
