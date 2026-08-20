"""Source URL extraction from agent tool calls and results.

A source is a place the agent went, and there are three ways to learn that
it went there: the call names it outright, the answer carries it, or the
answer is the document. Each tool falls into one of the three, and which
one it falls into is the whole of what this module knows about it.
"""

import json
import logging
from collections.abc import Iterator, Sequence
from typing import Literal
from urllib.parse import quote, urlparse

from pydantic import BaseModel

from lup.runtime.models import (
    TurnMessage,
    TurnToolCallBlock,
    TurnToolResultBlock,
)
from lup.types import JsonObject, JsonValue

logger = logging.getLogger(__name__)


class Source(BaseModel):
    """One consulted source, before it is written as a link."""

    url: str
    title: str = ""
    label: str = ""


# ---------------------------------------------------------------------------
# Source tool models
# ---------------------------------------------------------------------------


class ApiSourceTool(BaseModel):
    """Source tool whose reference URL follows from what it was asked for."""

    kind: Literal["api"] = "api"
    label: str
    input_key: str
    url_template: str

    def sources(self, arguments: JsonObject) -> list[Source]:
        """Everything one call named, whether it named one thing or several."""
        return [
            Source(url=self.url_template.format(quote(v)), title=v, label=self.label)
            for v in input_values(arguments, self.input_key)
        ]


class Publisher(BaseModel):
    """Where one body puts what it publishes."""

    label: str
    url_template: str


class PublishedSourceTool(BaseModel):
    """Source tool that names its publisher in the call, not in its name.

    `series(source="fred", series_ids=["UNRATE"])` addresses one body's own
    namespace, and the three bodies address a series differently, so which
    URL stands for the answer follows from the call rather than from the
    tool. A publisher this does not know yields no source rather than a
    guessed one: a template applied to the wrong namespace produces a link
    that resolves to nothing and reads as though it had been consulted.
    """

    kind: Literal["published"] = "published"
    source_key: str
    input_key: str
    publishers: dict[str, Publisher]

    def sources(self, arguments: JsonObject) -> list[Source]:
        """Everything one call named, in the namespace it named them in."""
        # lup: ignore[dict-get] — the agent's raw tool arguments
        publisher = self.publishers.get(str(arguments.get(self.source_key, "")))
        if publisher is None:
            return []
        return [
            Source(
                url=publisher.url_template.format(quote(v)),
                title=v,
                label=publisher.label,
            )
            for v in input_values(arguments, self.input_key)
        ]


class ResultSourceTool(BaseModel):
    """Source tool whose URLs are in its answer rather than in its call."""

    kind: Literal["result"] = "result"
    label: str


SourceTool = ApiSourceTool | PublishedSourceTool | ResultSourceTool


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

SOURCE_TOOLS: dict[str, SourceTool] = {
    # Prediction markets. `market` answers with a URL only where an event
    # ladder was opened; a bare price trace re-reads a market the search
    # already listed, and names no source that hit did not.
    "mcp__markets__market": ResultSourceTool(label="Prediction market"),
    "mcp__markets__metaculus": ResultSourceTool(label="Metaculus"),
    # Financial
    "mcp__financial__stock": ApiSourceTool(
        label="yfinance",
        input_key="symbol",
        url_template="https://finance.yahoo.com/quote/{}",
    ),
    "mcp__financial__stock_conditional_returns": ApiSourceTool(
        label="yfinance",
        input_key="reference_index",
        url_template="https://finance.yahoo.com/quote/{}",
    ),
    "mcp__financial__series": PublishedSourceTool(
        source_key="source",
        input_key="series_ids",
        publishers={
            "fred": Publisher(
                label="FRED",
                url_template="https://fred.stlouisfed.org/series/{}",
            ),
            "worldbank": Publisher(
                label="World Bank",
                url_template="https://data.worldbank.org/indicator/{}",
            ),
            "bls": Publisher(
                label="BLS",
                url_template="https://data.bls.gov/timeseries/{}",
            ),
        },
    ),
    # Trends
    "mcp__trends__trends": ApiSourceTool(
        label="Google Trends",
        input_key="terms",
        url_template="https://trends.google.com/trends/explore?q={}",
    ),
}
"""Every tool whose call or answer names a source, under the name it is called by.

Keyed by the *mounted* name, which is what a call carries: the server is
`markets`, so a Metaculus entry filed under `mcp__metaculus__` matches
nothing however right it reads. `search` and `fetch` are absent because
neither is a template — each is read from the shape of its own answer.
"""

AUGMENTED_SEARCH_TOOL = "mcp__search__search"
"""The one tool whose answer carries hits it read rather than links it found."""

FETCH_TOOL = "mcp__search__fetch"
"""The one tool that goes and reads a named document."""


class PendingRead(BaseModel):
    """How to read a call's result, recorded when the call goes by.

    A call and its result arrive on different messages, so what the result
    will mean has to be remembered between them. One record per call rather
    than one collection per reading: the three readings are alternatives,
    and holding them in three separate bags meant three membership tests,
    three ways to forget an id, and nowhere that a reading which had
    stopped matching any tool would show up as unused.
    """

    kind: Literal["augmented", "document", "walk"]
    label: str = ""


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def fetch_title(url: str) -> str:
    """Fetch page title via trafilatura metadata extraction."""
    import trafilatura

    try:
        html = trafilatura.fetch_url(url)
        if html:
            meta = trafilatura.extract_metadata(html, default_url=url)
            if meta and meta.title:
                return meta.title
    except Exception:
        logger.debug("Title fetch failed for %s", url, exc_info=True)
    return ""


def domain_label(url: str) -> str:
    """Generate a readable label from a URL's domain, used as fallback when no title."""
    try:
        return urlparse(url).netloc.removeprefix("www.")
    except ValueError:
        return url


def input_values(arguments: JsonObject, key: str) -> list[str]:
    """The values one argument names, whether it holds one or many.

    `series_ids` and `terms` take a list where `symbol` takes a scalar, and
    every element of the list is something the agent asked about.
    """
    value = arguments.get(key)  # lup: ignore[dict-get] — raw tool arguments
    if isinstance(value, list):
        return [str(v) for v in value if v]
    return [str(value)] if value else []


def record_title(record: dict[str, JsonValue]) -> str:
    """What a vendor record calls its subject, however it names that field."""
    for key in ("title", "market_title", "event_title"):
        named = record.get(key)  # lup: ignore[dict-get] — a vendor record
        if isinstance(named, str) and named:
            return named
    return ""


def walk_urls(data: JsonValue, label: str = "") -> Iterator[Source]:
    """Every url/pdf_url/id key in nested JSON data, with its sibling title.

    Recursion stops at the level that had a URL, so a record's own address
    stands rather than every address nested beneath it.
    """
    if isinstance(data, list):
        for item in data:
            yield from walk_urls(item, label)
        return
    if not isinstance(data, dict):
        return

    title = record_title(data)
    addressed = False
    for key, value in data.items():
        if not isinstance(value, str) or not value.startswith("http"):
            continue
        if key in ("url", "pdf_url"):
            yield Source(url=value, title=title, label=label)
            addressed = True
        elif key == "id":
            yield Source(url=value, label=label)
            addressed = True

    if not addressed:
        for value in data.values():
            yield from walk_urls(value, label)


def augmented_sources(data: JsonValue) -> Iterator[Source]:
    """The web hits a search actually read.

    A hit carrying `api_data` was answered from a recognized domain's API,
    and one carrying `text` had its page fetched and opened in the answer.
    Both were read. A hit that is only a title and a snippet was listed
    among candidates, which is a different thing — and counting those would
    make every nine-lane search a page of sources nobody consulted.

    The other eight lanes list rather than read, so a source reached
    through one of them is recorded when the agent drills into it: with
    `fetch`, or with the tool that owns it.
    """
    if not isinstance(data, dict):
        return
    web = data.get("web")  # lup: ignore[dict-get] — the tool's own payload
    if not isinstance(web, list):
        return
    for item in web:
        if not isinstance(item, dict):
            continue
        if item.get("api_data") is None and item.get("text") is None:
            continue
        url = item.get("url", "")
        if isinstance(url, str) and url.startswith("http"):
            yield Source(url=url, title=str(item.get("title") or ""))


def fetched_document(content: str) -> Source | None:
    """What a fetch read, which is not always what it was asked for.

    `fetch` takes a bare arXiv id as readily as a URL, and `at=` answers
    with the Internet Archive's copy rather than the live page. The answer
    carries the URL that was actually read; the request does not.
    """
    try:
        data = json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return None
    if not isinstance(data, dict):
        return None
    url = data.get("url", "")  # lup: ignore[dict-get] — the tool's own payload
    if not isinstance(url, str) or not url.startswith("http"):
        return None
    title = data.get("title", "")  # lup: ignore[dict-get] — same
    named = title if isinstance(title, str) and title else fetch_title(url)
    return Source(url=url, title=named)


def format_source(source: Source) -> str:
    """One source as a markdown link."""
    named = source.title.strip("[]()") or domain_label(source.url)
    shown = f"({source.label}) {named}" if source.label else named
    return f"[{shown}]({source.url})"


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------


def pending_read(block: TurnToolCallBlock) -> PendingRead | None:
    """How this call's result will have to be read, if it has to be at all."""
    if block.name == FETCH_TOOL:
        return PendingRead(kind="document")
    if block.name == AUGMENTED_SEARCH_TOOL:
        return PendingRead(kind="augmented")
    entry = SOURCE_TOOLS.get(block.name)
    if isinstance(entry, ResultSourceTool):
        return PendingRead(kind="walk", label=entry.label)
    return None


def call_sources(block: TurnToolCallBlock) -> list[Source]:
    """The sources a call names outright, needing no answer to know."""
    match SOURCE_TOOLS.get(block.name):
        case ApiSourceTool() | PublishedSourceTool() as entry:
            return entry.sources(block.arguments)
        case _:
            return []


def result_sources(waiting: PendingRead, content: str) -> Iterator[Source]:
    """The sources in one answer, read the way its own call said it would be."""
    if waiting.kind == "document":
        document = fetched_document(content)
        if document is not None:
            yield document
        return
    try:
        data = json.loads(content)
    except (json.JSONDecodeError, TypeError):
        return
    if waiting.kind == "augmented":
        yield from augmented_sources(data)
    else:
        yield from walk_urls(data, waiting.label)


def found_sources(messages: Sequence[TurnMessage]) -> Iterator[Source]:
    """Every source a call named or an answer carried, as they arrived."""
    # lup: ignore[empty-collection] — calls awaiting the results that read them
    pending: dict[str, PendingRead] = {}
    for msg in messages:
        for block in msg.blocks:
            if isinstance(block, TurnToolCallBlock):
                if (waiting := pending_read(block)) is not None:
                    pending[block.id] = waiting
                else:
                    yield from call_sources(block)
            elif isinstance(block, TurnToolResultBlock):
                if (waiting := pending.pop(block.tool_call_id, None)) is not None:
                    yield from result_sources(waiting, block.content)


def extract_sources(messages: Sequence[TurnMessage]) -> list[str]:
    """Deduplicated source URLs, as markdown links, from tool calls and results.

    First mention wins, so a source keeps the title it was found under
    rather than one a later and shallower mention carried.
    """
    # lup: ignore[empty-collection] — a first-wins fold, which a dict
    # comprehension inverts: a later duplicate would overwrite the first
    first: dict[str, Source] = {}
    for source in found_sources(messages):
        first.setdefault(source.url, source)
    return [format_source(source) for source in first.values()]
