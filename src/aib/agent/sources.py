"""Source URL extraction from agent tool calls and results."""

import json
from collections.abc import Sequence
from typing import Literal
from urllib.parse import urlparse

from pydantic import BaseModel

from claude_agent_sdk import (
    AssistantMessage,
    ToolResultBlock,
    ToolUseBlock,
    UserMessage,
)


# ---------------------------------------------------------------------------
# Source tool models
# ---------------------------------------------------------------------------


class ApiSourceTool(BaseModel):
    """Source tool that constructs a reference URL from tool input."""

    kind: Literal["api"] = "api"
    label: str
    input_key: str
    url_template: str


class ResultSourceTool(BaseModel):
    """Source tool that extracts URLs from the result JSON."""

    kind: Literal["result"] = "result"
    label: str


SourceTool = ApiSourceTool | ResultSourceTool


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------

_SOURCE_TOOLS: dict[str, SourceTool] = {
    # Search
    "mcp__search__fetch_arxiv": ApiSourceTool(
        label="arXiv",
        input_key="paper_id",
        url_template="https://arxiv.org/abs/{}",
    ),
    "mcp__search__wikipedia": ResultSourceTool(label="Wikipedia"),
    # Prediction markets
    "mcp__markets__kalshi_price": ResultSourceTool(label="Kalshi"),
    "mcp__markets__kalshi_event": ResultSourceTool(label="Kalshi"),
    "mcp__markets__polymarket_price": ResultSourceTool(label="Polymarket"),
    "mcp__markets__manifold_price": ResultSourceTool(label="Manifold"),
    # Metaculus
    "mcp__markets__get_metaculus_questions": ResultSourceTool(label="Metaculus"),
    "mcp__markets__search_metaculus": ResultSourceTool(label="Metaculus"),
    "mcp__markets__list_tournament_questions": ResultSourceTool(label="Metaculus"),
    "mcp__markets__get_coherence_links": ResultSourceTool(label="Metaculus"),
    # Financial
    "mcp__financial__stock_price": ApiSourceTool(
        label="yfinance",
        input_key="symbol",
        url_template="https://finance.yahoo.com/quote/{}",
    ),
    "mcp__financial__stock_history": ApiSourceTool(
        label="yfinance",
        input_key="symbol",
        url_template="https://finance.yahoo.com/quote/{}",
    ),
    "mcp__financial__fred_series": ApiSourceTool(
        label="FRED",
        input_key="series_id",
        url_template="https://fred.stlouisfed.org/series/{}",
    ),
    "mcp__financial__company_financials": ApiSourceTool(
        label="yfinance",
        input_key="ticker",
        url_template="https://finance.yahoo.com/quote/{}",
    ),
    # Trends
    "mcp__trends__google_trends": ApiSourceTool(
        label="Google Trends",
        input_key="keyword",
        url_template="https://trends.google.com/trends/explore?q={}",
    ),
    "mcp__trends__google_trends_related": ApiSourceTool(
        label="Google Trends",
        input_key="keyword",
        url_template="https://trends.google.com/trends/explore?q={}",
    ),
}

_AUGMENTED_RESULT_TOOLS: frozenset[str] = frozenset({"mcp__search__web_search"})


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _domain_label(url: str) -> str:
    """Generate a readable label from a URL's domain, used as fallback when no title."""
    try:
        return urlparse(url).netloc.removeprefix("www.")
    except Exception:
        return url


def _walk_urls(data: object) -> list[tuple[str, str]]:
    """Extract (url, title) pairs from url/pdf_url/id keys in nested JSON data.

    Looks for sibling 'title' keys at the same dict level as URL keys.
    """
    results: list[tuple[str, str]] = []
    if isinstance(data, dict):
        title = str(
            data.get("title")
            or data.get("market_title")
            or data.get("event_title")
            or ""
        )
        url_found = False
        for k, v in data.items():
            if k in ("url", "pdf_url") and isinstance(v, str) and v.startswith("http"):
                results.append((v, title))
                url_found = True
            elif k == "id" and isinstance(v, str) and v.startswith("http"):
                results.append((v, ""))
                url_found = True
        if not url_found:
            for v in data.values():
                results.extend(_walk_urls(v))
    elif isinstance(data, list):
        for item in data:
            results.extend(_walk_urls(item))
    return results


def _format_source(url: str, title: str = "", label: str = "") -> str:
    """Format a source URL as a markdown link."""
    if label:
        display = f"({label}) {title.strip('[]()') or _domain_label(url)}"
    elif title:
        display = title.strip("[]()")
    else:
        display = _domain_label(url)
    return f"[{display}]({url})"


def _extract_result_texts(block: ToolResultBlock) -> list[str]:
    """Extract text strings from a ToolResultBlock's content."""
    texts: list[str] = []
    if isinstance(block.content, str):
        texts.append(block.content)
    elif isinstance(block.content, list):
        for item in block.content:
            if isinstance(item, dict) and item.get("type") == "text":
                texts.append(item["text"])
    return texts


def _extract_augmented_urls(data: object) -> list[tuple[str, str]]:
    """Extract (url, title) pairs from results that have api_data set."""
    results: list[tuple[str, str]] = []
    if not isinstance(data, dict):
        return results
    for item in data.get("results", []):
        if not isinstance(item, dict):
            continue
        if item.get("api_data") is None:
            continue
        url = item.get("url", "")
        if isinstance(url, str) and url.startswith("http"):
            results.append((url, str(item.get("title") or "")))
    return results


# ---------------------------------------------------------------------------
# Main extraction
# ---------------------------------------------------------------------------


def extract_sources(messages: Sequence[AssistantMessage | UserMessage]) -> list[str]:
    """Extract deduplicated source URLs as markdown links from tool calls and results."""
    seen: set[str] = set()
    sources: list[str] = []
    pending_augmented: set[str] = set()
    pending_result: dict[str, str] = {}  # tool_use_id → label

    def _add(url: str, title: str = "", label: str = "") -> None:
        if url not in seen:
            seen.add(url)
            sources.append(_format_source(url, title, label))

    for msg in messages:
        content = msg.content
        if isinstance(content, str):
            continue
        for block in content:
            if isinstance(block, ToolUseBlock) and isinstance(block.input, dict):
                if block.name in ("WebFetch", "mcp__search__fetch_url") and (
                    url := block.input.get("url")
                ):
                    _add(str(url))
                elif block.name in _AUGMENTED_RESULT_TOOLS:
                    pending_augmented.add(block.id)
                elif (entry := _SOURCE_TOOLS.get(block.name)) is not None:
                    if isinstance(entry, ApiSourceTool):
                        if val := block.input.get(entry.input_key):
                            _add(entry.url_template.format(val), str(val), entry.label)
                    else:
                        pending_result[block.id] = entry.label
            elif isinstance(block, ToolResultBlock):
                if block.tool_use_id in pending_augmented:
                    pending_augmented.discard(block.tool_use_id)
                    for text in _extract_result_texts(block):
                        try:
                            for url, title in _extract_augmented_urls(json.loads(text)):
                                _add(url, title)
                        except (json.JSONDecodeError, TypeError):
                            pass
                elif block.tool_use_id in pending_result:
                    label = pending_result.pop(block.tool_use_id)
                    for text in _extract_result_texts(block):
                        try:
                            for url, title in _walk_urls(json.loads(text)):
                                _add(url, title, label)
                        except (json.JSONDecodeError, TypeError):
                            pass

    return sources
