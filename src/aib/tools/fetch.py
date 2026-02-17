"""Unified URL fetch with content extraction, domain routing, and JS rendering.

Replaces WebFetch for the forecasting agent. Pipeline:

    URL → domain dispatch → httpx + trafilatura → (JS?) → Playwright → prompt extract

Live mode: httpx direct fetch with trafilatura extraction.
Retrodict mode: Wayback Machine fetch with trafilatura extraction.
JS fallback: Playwright MCP server via direct MCP client call.
"""

import logging
from typing import Any

from claude_agent_sdk import tool
from pydantic import BaseModel, Field

from aib.retrodict_context import retrodict_cutoff
from aib.tools.extract import extract_with_prompt
from aib.tools.fetch_http import fetch_live
from aib.tools.fetch_routes import SUGGEST_ONLY, domain_dispatch
from aib.tools.mcp_server import create_mcp_server
from aib.tools.metrics import tracked
from aib.tools.responses import mcp_error, mcp_success
from aib.tools.wayback import (
    WaybackRateLimitError,
    check_wayback_availability,
    fetch_wayback_content,
)

logger = logging.getLogger(__name__)

_MAX_CONTENT = 10_000


class FetchUrlInput(BaseModel):
    url: str = Field(min_length=1, description="The URL to fetch content from")
    prompt: str | None = Field(
        default=None,
        description="What information to extract from the page",
    )


@tool(
    "fetch_url",
    (
        "Fetch and extract content from a URL. "
        "Automatically extracts readable text, renders JavaScript pages via Playwright, "
        "and routes known domains to specialized tools "
        "(Yahoo Finance, arXiv, Wikipedia, FRED, Polymarket). "
        "If a prompt is provided, uses an LLM to extract specific information. "
        "Prefer this over WebFetch for URL fetching."
    ),
    FetchUrlInput.model_json_schema(),
)
@tracked("fetch_url")
async def fetch_url(args: dict[str, Any]) -> dict[str, Any]:
    """Unified fetch: domain dispatch → http/wayback → trafilatura → playwright → prompt."""
    try:
        inp = FetchUrlInput.model_validate(args)
    except Exception as e:
        return mcp_error(f"Invalid input: {e}")

    url, prompt = inp.url, inp.prompt

    # 1. Suggest-only domains (can't auto-dispatch, different interface)
    for domain, hint in SUGGEST_ONLY.items():
        if domain in url.lower():
            return mcp_error(f"fetch_url is not optimal for this domain. {hint}")

    # 2. Domain auto-dispatch
    dispatched = await domain_dispatch(url)
    if dispatched is not None:
        return dispatched

    # 3. Fetch content (live or retrodict)
    if retrodict_cutoff.get() is not None:
        content = await _fetch_retrodict(url)
    else:
        content = await fetch_live(url)

    if isinstance(content, dict):
        return content

    # 4. Optional prompt extraction (Sonnet)
    if prompt:
        try:
            content = await extract_with_prompt(content, prompt, url)
        except Exception as e:
            logger.warning("Prompt extraction failed for %s: %s", url, e)
            content = f"[Prompt extraction failed, returning raw content]\n\n{content}"

    return mcp_success({"url": url, "content": content[:_MAX_CONTENT]})


async def _fetch_retrodict(url: str) -> dict[str, Any] | str:
    """Fetch in retrodict mode via Wayback Machine."""
    cutoff = retrodict_cutoff.get()
    assert cutoff is not None
    ts = cutoff.strftime("%Y%m%d")

    try:
        snapshot = await check_wayback_availability(
            url, ts, validate_before_cutoff=True, raise_on_rate_limit=True,
        )
    except WaybackRateLimitError:
        return mcp_error(
            f"Wayback rate limited for {url}. Try again shortly, "
            "or use web_search to find alternative sources."
        )

    if snapshot is None:
        return mcp_error(
            f"No archived snapshot for {url}. "
            "Try web_search to find alternative sources."
        )

    content = await fetch_wayback_content(url, ts)
    if content is None:
        return mcp_error(
            f"Content extraction failed for {url}. "
            "May be a PDF, image, or JS-rendered page. "
            "Try web_search for alternative sources."
        )

    return content


def create_fetch_server() -> Any:
    """Create MCP server with the fetch_url tool."""
    return create_mcp_server("fetch", tools=[fetch_url])
