"""Exa AI-powered web search.

This module provides the core Exa search functionality used by both
the forecasting tools and retrodict search.
"""

from typing import Any

import httpx

from aib.config import settings
from aib.tools.cache import cached
from aib.tools.retry import with_retry


@cached(ttl=300)
@with_retry(max_attempts=3)
async def exa_search(
    query: str,
    num_results: int,
    published_before: str | None = None,
    livecrawl: str = "always",
) -> list[dict[str, Any]]:
    """Execute an Exa search (cached for 5 minutes).

    Args:
        query: Search query string.
        num_results: Number of results to return.
        published_before: Optional ISO date (YYYY-MM-DD) to filter results.
        livecrawl: Livecrawl mode ('always', 'fallback', 'never').

    Returns:
        List of search result dicts with title, url, snippet, etc.

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
        payload["publishedBefore"] = f"{published_before}T23:59:59.999Z"

    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.post(url, json=payload, headers=headers)
        response.raise_for_status()
        data = response.json()

    results = []
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
    return results
