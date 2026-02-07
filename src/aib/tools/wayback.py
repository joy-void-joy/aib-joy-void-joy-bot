"""Wayback Machine API utilities with rate limiting.

Provides rate-limited access to the Wayback Machine Availability API,
respecting Internet Archive's usage guidelines:
- Limited concurrent requests (semaphore)
- Retry with exponential backoff on 429/5xx
- Respect Retry-After header
- Cache results (availability rarely changes)
"""

from __future__ import annotations

import asyncio
import logging
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from aib.tools.exa import ExaResult

import httpx
import trafilatura
from tenacity import (
    AsyncRetrying,
    retry_if_exception_type,
    stop_after_attempt,
    wait_exponential_jitter,
)

from aib.tools.cache import cached

logger = logging.getLogger(__name__)

# Lazily create semaphores per-event-loop to avoid binding issues
_wayback_semaphore_store: dict[str, asyncio.Semaphore] = {}


def _wayback_semaphore() -> asyncio.Semaphore:
    loop = asyncio.get_running_loop()
    key = f"wayback_{id(loop)}"
    if key not in _wayback_semaphore_store:
        _wayback_semaphore_store[key] = asyncio.Semaphore(5)
    return _wayback_semaphore_store[key]

# Custom exception for rate limiting
class WaybackRateLimitError(Exception):
    """Raised when Wayback API returns 429 Too Many Requests."""

    def __init__(self, retry_after: int | None = None):
        self.retry_after = retry_after
        super().__init__(f"Rate limited, retry after {retry_after}s")


async def _make_wayback_request(url: str, timestamp: str) -> dict[str, Any] | None:
    """Make a single request to Wayback Availability API.

    Args:
        url: The URL to check.
        timestamp: Wayback timestamp format (YYYYMMDD).

    Returns:
        Dict with snapshot info if available, or None.

    Raises:
        WaybackRateLimitError: If rate limited (429).
        httpx.HTTPStatusError: For other HTTP errors.
    """
    async with httpx.AsyncClient(timeout=15.0) as client:
        response = await client.get(
            "https://archive.org/wayback/available",
            params={"url": url, "timestamp": timestamp},
        )

        if response.status_code == 429:
            retry_after = response.headers.get("Retry-After")
            retry_seconds = int(retry_after) if retry_after else None
            raise WaybackRateLimitError(retry_seconds)

        response.raise_for_status()
        return response.json()


@cached(ttl=86400)  # 24 hours - availability rarely changes
async def check_wayback_availability(
    url: str, timestamp: str, *, validate_before_cutoff: bool = True
) -> dict[str, Any] | None:
    """Check if a URL has a Wayback Machine snapshot near the given timestamp.

    Uses rate limiting (semaphore) and retry with exponential backoff.
    Results are cached for 24 hours.

    Args:
        url: The URL to check.
        timestamp: Wayback timestamp format (YYYYMMDD or YYYYMMDDHHMMSS).
        validate_before_cutoff: If True, only returns snapshots that are
            at or before the requested timestamp. If False, returns the
            closest snapshot regardless of whether it's before or after.

    Returns:
        Dict with snapshot info if available (contains 'url', 'timestamp', 'status'),
        or None if no snapshot exists, snapshot is after cutoff, or on persistent failure.

    API docs: https://archive.org/help/wayback_api.php
    """
    async with _wayback_semaphore():
        try:
            async for attempt in AsyncRetrying(
                stop=stop_after_attempt(3),
                wait=wait_exponential_jitter(initial=1, max=30, jitter=2),
                retry=retry_if_exception_type((WaybackRateLimitError, httpx.HTTPStatusError)),
                reraise=True,
            ):
                with attempt:
                    data = await _make_wayback_request(url, timestamp)
                    if data is None:
                        return None

                    snapshots = data.get("archived_snapshots", {})
                    closest = snapshots.get("closest")
                    if closest and closest.get("available"):
                        # Validate snapshot is not after the cutoff if requested
                        if validate_before_cutoff:
                            actual_ts = closest.get("timestamp", "")
                            if actual_ts and normalize_wayback_timestamp(actual_ts) > normalize_wayback_timestamp(timestamp):
                                logger.debug(
                                    "Wayback snapshot %s is after cutoff %s for %s",
                                    actual_ts, timestamp, url
                                )
                                return None
                        return closest
                    return None

        except WaybackRateLimitError as e:
            logger.warning("Wayback rate limited after retries: %s", e)
            return None
        except httpx.HTTPStatusError as e:
            logger.warning("Wayback API error after retries: %s", e)
            return None
        except Exception as e:
            logger.exception("Unexpected error checking Wayback availability: %s", e)
            return None

    return None


def normalize_wayback_timestamp(timestamp: str) -> int:
    """Normalize Wayback timestamp to YYYYMMDD integer for safe comparison.

    The Wayback API returns timestamps with variable precision (YYYYMMDD to
    YYYYMMDDHHMMSS). This function extracts just the date portion as an integer
    for reliable comparison.

    Args:
        timestamp: Wayback timestamp string (8-14 digits).

    Returns:
        Integer in YYYYMMDD format for comparison.

    Example:
        >>> normalize_wayback_timestamp("20260115")
        20260115
        >>> normalize_wayback_timestamp("20260115120000")
        20260115
    """
    return int(timestamp[:8])


def rewrite_to_wayback(url: str, timestamp: str) -> str:
    """Rewrite a URL to use Wayback Machine snapshot.

    The Wayback Machine URL format appends the original URL directly after the
    timestamp - no encoding needed. The 'id_' modifier returns raw content
    without the Wayback toolbar injection.

    Args:
        url: Original URL to fetch (e.g., "https://example.com/search?q=test")
        timestamp: Wayback timestamp format (YYYYMMDD or YYYYMMDDHHMMSS)

    Returns:
        Wayback Machine URL for the closest snapshot before the timestamp.

    Example:
        >>> rewrite_to_wayback("https://example.com/page?q=1", "20260115")
        'https://web.archive.org/web/20260115id_/https://example.com/page?q=1'
    """
    return f"https://web.archive.org/web/{timestamp}id_/{url}"


@cached(ttl=3600)
async def fetch_wayback_content(url: str, timestamp: str) -> str | None:
    """Fetch a Wayback Machine snapshot and extract text content.

    Validates that a pre-cutoff snapshot exists, fetches the archived HTML,
    and extracts readable text using trafilatura.

    Args:
        url: Original URL to fetch from Wayback.
        timestamp: Wayback timestamp format (YYYYMMDD) used as cutoff.

    Returns:
        Extracted text content, or None if no valid snapshot exists
        or text extraction fails.
    """
    snapshot = await check_wayback_availability(
        url, timestamp, validate_before_cutoff=True
    )
    if not snapshot:
        return None

    actual_ts = snapshot.get("timestamp", timestamp)
    wayback_url = rewrite_to_wayback(url, actual_ts)

    async with _wayback_semaphore():
        try:
            async with httpx.AsyncClient(timeout=20.0) as client:
                response = await client.get(wayback_url, follow_redirects=True)
                response.raise_for_status()
                html = response.text
        except httpx.HTTPError as e:
            logger.warning("Wayback fetch failed for %s: %s", url, e)
            return None

    extracted = trafilatura.extract(
        html,
        include_comments=False,
        include_tables=True,
        no_fallback=False,
    )

    if not extracted:
        logger.debug("Trafilatura extraction returned nothing for %s", url)
        return None

    return extracted


async def wayback_validate_results(
    results: list[ExaResult],
    wayback_ts: str,
) -> list[ExaResult]:
    """Replace Exa snippets with Wayback-validated content.

    For each search result, fetches the page from the Wayback Machine
    (as it existed at the cutoff date) and replaces the snippet with
    extracted text. Results without a valid pre-cutoff snapshot are dropped.

    Args:
        results: Exa search results to validate.
        wayback_ts: Wayback timestamp (YYYYMMDD) cutoff.

    Returns:
        Filtered results with Wayback-derived snippets.
    """
    tasks = [
        fetch_wayback_content(r["url"] or "", wayback_ts)
        for r in results
    ]
    contents = await asyncio.gather(*tasks)

    validated: list[ExaResult] = []
    for result, content in zip(results, contents):
        if content is None:
            logger.warning(
                "Wayback validate: dropping %s (no pre-cutoff snapshot)",
                result.get("url", "?"),
            )
            continue
        result["snippet"] = content[:500]
        validated.append(result)

    logger.info(
        "[Retrodict] Wayback validated %d/%d search results",
        len(validated),
        len(results),
    )

    return validated
