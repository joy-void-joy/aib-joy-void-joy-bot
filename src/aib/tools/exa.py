"""Exa AI-powered web search.

This module provides the core Exa search functionality used by both
the forecasting tools and retrodict search.
"""

import logging
from typing import Any, TypedDict

import httpx

from aib.config import settings
from aib.retrodict_context import retrodict_cutoff
from aib.tools.cache import cached
from aib.tools.retry import with_retry
from aib.tools.wayback import wayback_validate_results

logger = logging.getLogger(__name__)


class ExaResult(TypedDict):
    title: str | None
    url: str | None
    snippet: str | None
    highlights: list[str] | None
    published_date: str | None
    score: float | None


@cached(ttl=300)
@with_retry(max_attempts=3)
async def exa_search(
    query: str,
    num_results: int,
    published_before: str | None = None,
    published_after: str | None = None,
    livecrawl: str = "always",
    include_domains: list[str] | None = None,
    exclude_domains: list[str] | None = None,
) -> list[ExaResult]:
    """Execute an Exa search (cached for 5 minutes).

    When published_before is set, applies client-side date filtering as a
    defense against Exa's unreliable server-side endPublishedDate filter
    (which fails for static files like PDFs and investor relations pages).

    Args:
        query: Search query string.
        num_results: Number of results to return.
        published_before: Optional ISO date (YYYY-MM-DD) upper bound for results.
        published_after: Optional ISO date (YYYY-MM-DD) lower bound for results.
        livecrawl: Livecrawl mode ('always', 'fallback', 'never').
        include_domains: Only include results from these domains.
        exclude_domains: Exclude results from these domains.

    Returns:
        List of ExaResult dicts with title, url, snippet, etc.

    Raises:
        ValueError: If EXA_API_KEY is not configured.
        httpx.HTTPStatusError: If the Exa API request fails.
    """
    api_key = settings.exa_api_key
    if not api_key:
        raise ValueError("EXA_API_KEY not configured")

    url = "https://api.exa.ai/search"
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "x-api-key": api_key,
    }
    payload: dict[str, Any] = {
        "query": query,
        "type": "auto",
        "useAutoprompt": True,
        "numResults": num_results,
        "livecrawl": livecrawl,
        "contents": {
            "text": {"includeHtmlTags": False},
            "highlights": {
                "query": query,
                "numSentences": 4,
                "highlightsPerUrl": 3,
            },
        },
    }

    if published_before:
        payload["endPublishedDate"] = f"{published_before}T23:59:59.999Z"
    if published_after:
        payload["startPublishedDate"] = f"{published_after}T00:00:00.000Z"
    if include_domains:
        payload["includeDomains"] = include_domains
    if exclude_domains:
        payload["excludeDomains"] = exclude_domains

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        if response.status_code != 200:
            logger.error("Exa API error %d: %s", response.status_code, response.text)
        if 400 <= response.status_code < 500:
            raise ValueError(f"Exa API client error {response.status_code}: {response.text[:200]}")
        response.raise_for_status()
        data = response.json()

    results: list[ExaResult] = []
    for r in data.get("results", []):
        published_date = r.get("publishedDate")
        if published_date and isinstance(published_date, str):
            published_date = published_date.rstrip("Z")

        results.append(
            {
                "title": r.get("title"),
                "url": r.get("url"),
                "snippet": (r.get("text") or "")[:500] or None,
                "highlights": r.get("highlights", [])[:3] or None,
                "published_date": published_date,
                "score": r.get("score"),
            }
        )

    if published_before and retrodict_cutoff.get() is not None:
        results = _filter_by_published_date(results, published_before)
        wayback_ts = published_before.replace("-", "")
        results = await wayback_validate_results(results, wayback_ts)

    return results


def _filter_by_published_date(
    results: list[ExaResult],
    cutoff_date: str,
) -> list[ExaResult]:
    """Drop results published after cutoff or with unknown publication date.

    Exa's server-side publishedBefore filter is unreliable for static files
    (PDFs, investor relations pages). This provides client-side validation.

    Args:
        results: Exa search results to filter.
        cutoff_date: YYYY-MM-DD cutoff date.

    Returns:
        Results with verified publishedDate before cutoff.
    """
    validated: list[ExaResult] = []

    for r in results:
        pd = r.get("published_date")
        if pd and pd[:10] <= cutoff_date:
            validated.append(r)
        elif pd:
            logger.warning(
                "Date filter: dropping %s (published %s > cutoff %s)",
                r.get("url", "?"),
                pd[:10],
                cutoff_date,
            )
        else:
            logger.warning(
                "Date filter: dropping %s (no published_date)",
                r.get("url", "?"),
            )

    if len(validated) < len(results):
        logger.info(
            "Retrodict date filter: %d/%d results passed (cutoff %s)",
            len(validated),
            len(results),
            cutoff_date,
        )

    return validated
