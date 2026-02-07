"""Wikipedia API utilities with historical revision support.

Provides functions for fetching Wikipedia articles, including historical
versions at specific dates via Wikipedia's revision API.
"""

import logging
from typing import Any
from urllib.parse import quote as url_quote

import httpx
import trafilatura

from aib.config import settings
from aib.tools.cache import cached

logger = logging.getLogger(__name__)

# Wikipedia API configuration
WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"
WIKIPEDIA_HEADERS = {
    "User-Agent": "AIBForecastingBot/1.0 (https://github.com/joy-void-joy/aib-forecasting-bot; forecasting research)"
}


@cached(ttl=3600)  # 1 hour - Wikipedia content is stable
async def fetch_wikipedia_historical(
    title: str,
    cutoff_date: str,
) -> dict[str, Any]:
    """Fetch Wikipedia article content as it existed at cutoff_date.

    Uses Wikipedia's revision history API to find the revision that was
    current at the specified date, then fetches that revision's HTML
    via the RESTbase API and extracts text using trafilatura.

    Results are cached to avoid re-fetching when the same article is
    accessed multiple times (e.g., first in search results, then full fetch).

    Args:
        title: Wikipedia article title.
        cutoff_date: Date string (YYYY-MM-DD) to fetch article state from.

    Returns:
        Dict with title, url, extract, revision_id, revision_timestamp.

    Raises:
        ValueError: If article not found or no revision before cutoff.
    """
    # Convert cutoff_date to MediaWiki timestamp format (YYYYMMDDHHMMSS)
    cutoff_ts = cutoff_date.replace("-", "") + "235959"

    async with httpx.AsyncClient(
        timeout=settings.http_timeout_seconds,
        headers=WIKIPEDIA_HEADERS,
    ) as client:
        # Find the revision ID that was current at cutoff_date
        rev_response = await client.get(
            WIKIPEDIA_API_URL,
            params={
                "action": "query",
                "titles": title,
                "prop": "revisions",
                "rvprop": "ids|timestamp",
                "rvlimit": 1,
                "rvstart": cutoff_ts,
                "rvdir": "older",
                "redirects": 1,
                "format": "json",
                "utf8": 1,
            },
        )
        rev_response.raise_for_status()
        rev_data = rev_response.json()

        pages = rev_data.get("query", {}).get("pages", {})
        if not pages:
            raise ValueError(f"Article not found: {title}")

        page_id = next(iter(pages))
        if page_id == "-1":
            raise ValueError(f"Article not found: {title}")

        page = pages[page_id]
        revisions = page.get("revisions", [])
        if not revisions:
            raise ValueError(f"No revision found before {cutoff_date} for: {title}")

        revision = revisions[0]
        rev_id = revision["revid"]
        rev_timestamp = revision["timestamp"]
        resolved_title = page.get("title", title)

        # Fetch HTML content for this specific revision via RESTbase API
        # Wikipedia uses underscores for spaces, and percent-encodes other special chars
        encoded_title = url_quote(resolved_title.replace(" ", "_"), safe="")
        rest_url = (
            f"https://en.wikipedia.org/api/rest_v1/page/html/{encoded_title}/{rev_id}"
        )

        html_response = await client.get(rest_url)
        html_response.raise_for_status()
        html_content = html_response.text

        # Extract plain text using trafilatura
        extracted = trafilatura.extract(
            html_content,
            include_comments=False,
            include_tables=True,
            no_fallback=False,
        )

        if not extracted:
            raise ValueError(
                f"Could not extract text from revision {rev_id} for: {title}"
            )

        return {
            "title": resolved_title,
            "url": f"https://en.wikipedia.org/wiki/{encoded_title}",
            "extract": extracted,
            "revision_id": rev_id,
            "revision_timestamp": rev_timestamp,
            "cutoff_date": cutoff_date,
        }


def extract_intro(text: str) -> str:
    """Extract the intro section from Wikipedia article text.

    The intro is everything before the first section header (== ... ==).
    Uses a heuristic: takes content until hitting a blank line after
    accumulating at least 500 characters.
    """
    lines = text.split("\n")
    intro_lines: list[str] = []
    for line in lines:
        if line.strip() and not intro_lines:
            intro_lines.append(line)
        elif intro_lines:
            if line.strip():
                intro_lines.append(line)
            else:
                # Hit a blank line - check if we have enough content
                current = "\n".join(intro_lines)
                if len(current) > 500:
                    break
                intro_lines.append(line)

    return "\n".join(intro_lines).strip()
