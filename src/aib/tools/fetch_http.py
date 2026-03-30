"""HTTP fetch with retry, content extraction, and Playwright JS fallback.

Pipeline: httpx GET (with_retry on 429/5xx) → trafilatura → Playwright
"""

import hashlib
import logging
from contextvars import ContextVar
from pathlib import Path
from typing import Any

import httpx
import trafilatura
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
from mcp.types import TextContent

from pydantic import BaseModel, ConfigDict, field_validator

from aib.tools.responses import mcp_error, mcp_success
from aib.tools.retry import with_retry

logger = logging.getLogger(__name__)


class FetchResult(BaseModel):
    model_config = ConfigDict(extra="ignore")
    text: str
    title: str = ""
    data: list[str] = []

    @field_validator("title", mode="before")
    @classmethod
    def coerce_title(cls, v: object) -> str:
        return v if isinstance(v, str) else ""


_USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

_ERROR_HINTS: dict[int, str] = {
    401: "Try search_exa for cached content, or search_news for news articles.",
    403: "Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series, company_financials, world_bank_indicator).",
    404: "The URL may have changed. Try WebSearch to find the current URL.",
    405: "Try search_exa for indexed content.",
}


async def _http_get(client: httpx.AsyncClient, url: str) -> httpx.Response:
    """GET a URL, raising on 429/5xx so the caller's retry loop catches it."""
    resp = await client.get(url)
    if resp.status_code == 429 or resp.status_code >= 500:
        resp.raise_for_status()
    return resp


async def _playwright_render(url: str) -> FetchResult | None:
    """Render a JS page via Playwright, extracting text and structured data.

    Pipeline:
    1. Navigate and render the page
    2. Extract embedded data (Next.js __NEXT_DATA__, JSON script tags, global state)
    3. Extract text via trafilatura on rendered HTML, fallback to innerText
    """
    params = StdioServerParameters(
        command="bun",
        args=["x", "@playwright/mcp@latest", "--headless"],
        env={"PLAYWRIGHT_MCP_HEADLESS": "true"},
    )

    try:
        async with stdio_client(params) as (read, write):
            async with ClientSession(read, write) as session:
                await session.initialize()
                nav = await session.call_tool("browser_navigate", {"url": url})

                if nav.isError:
                    logger.warning("Playwright navigate error for %s", url)
                    return None

                # --- Extract structured data from the page ---
                data_snippets: list[str] = []
                data_result = await session.call_tool(
                    "browser_evaluate",
                    {"function": _EXTRACT_PAGE_DATA_JS},
                )
                if not data_result.isError:
                    for block in data_result.content:
                        if isinstance(block, TextContent) and block.text.strip():
                            data_snippets.append(block.text)

                # --- Extract text content ---
                text = ""
                html_result = await session.call_tool(
                    "browser_evaluate",
                    {"function": "() => document.documentElement.outerHTML"},
                )
                if not html_result.isError:
                    html_parts = [
                        block.text
                        for block in html_result.content
                        if isinstance(block, TextContent)
                    ]
                    rendered_html = "\n".join(html_parts)
                    extracted = trafilatura.extract(rendered_html)
                    if extracted and len(extracted) > 100:
                        text = extracted

                if not text:
                    text_result = await session.call_tool(
                        "browser_evaluate",
                        {"function": "() => document.body.innerText"},
                    )
                    if not text_result.isError:
                        parts = [
                            block.text
                            for block in text_result.content
                            if isinstance(block, TextContent)
                        ]
                        text = "\n".join(parts).strip()

                if text or data_snippets:
                    return FetchResult(
                        text=text or "(no text content)",
                        data=data_snippets,
                    )
                return None

    except BaseException as e:
        if isinstance(e, ExceptionGroup):
            for exc in e.exceptions:
                logger.warning("Playwright sub-exception for %s: %s", url, exc)
        else:
            logger.warning("Playwright fallback failed for %s: %s", url, e)
        return None


_EXTRACT_PAGE_DATA_JS = """() => {
    const results = [];

    // Next.js embedded data
    if (window.__NEXT_DATA__) {
        try {
            const s = JSON.stringify(window.__NEXT_DATA__);
            if (s.length < 500000) results.push(s);
        } catch {}
    }

    // JSON script tags (common in SSR frameworks)
    for (const el of document.querySelectorAll('script[type="application/json"]')) {
        const t = el.textContent;
        if (t && t.length > 10 && t.length < 500000) results.push(t);
    }

    // Common global state patterns
    for (const key of [
        '__INITIAL_STATE__', '__PRELOADED_STATE__', '__APP_DATA__',
        '__NUXT__', '__APOLLO_STATE__',
    ]) {
        if (window[key]) {
            try {
                const s = JSON.stringify(window[key]);
                if (s.length < 500000) results.push(s);
            } catch {}
        }
    }

    return JSON.stringify(results);
}"""


downloads_dir: ContextVar[Path] = ContextVar("downloads_dir", default=Path("tmp"))


MAX_PDF_BYTES = 100 * 1024 * 1024


def _save_pdf(url: str, content: bytes) -> dict[str, Any]:
    """Save PDF content to disk and return a path hint for the agent."""
    if len(content) > MAX_PDF_BYTES:
        return mcp_error(
            f"PDF too large to process ({len(content) / 1024 / 1024:.0f} MB). "
            f"Try finding the information from a different source."
        )
    target = downloads_dir.get() / "pdf"
    target.mkdir(parents=True, exist_ok=True)
    slug = hashlib.sha256(url.encode()).hexdigest()[:12]
    pdf_path = target / f"{slug}.pdf"
    pdf_path.write_bytes(content)
    return mcp_success(
        {
            "format": "pdf",
            "url": url,
            "pdf_path": str(pdf_path.resolve()),
            "hint": (
                f"PDF downloaded to {pdf_path.resolve()}. "
                "Use the Read tool to read the PDF content."
            ),
        }
    )


async def fetch_live(url: str) -> dict[str, Any] | FetchResult:
    """Fetch URL in live mode: httpx → trafilatura → Playwright fallback.

    Creates a single httpx client so retries reuse the same TCP connection.
    Returns extracted text on success, or an MCP error dict on failure.
    """
    try:
        async with httpx.AsyncClient(
            timeout=20.0,
            follow_redirects=True,
            headers={"User-Agent": _USER_AGENT},
        ) as client:

            @with_retry(max_attempts=3)
            async def _get() -> httpx.Response:
                return await _http_get(client, url)

            resp = await _get()
    except httpx.TimeoutException:
        return mcp_error(f"Timeout fetching {url}. Try Playwright or search_exa.")
    except httpx.ConnectError:
        return mcp_error(f"Could not connect to {url}. Check the URL.")
    except httpx.HTTPStatusError as e:
        status = e.response.status_code
        if status == 429:
            return mcp_error(
                f"Rate limited by {url} after retries. "
                "Try search_exa for cached content."
            )
        return mcp_error(
            f"HTTP {status} for {url}. "
            "Server error. Try again later, or use search_exa."
        )
    except httpx.HTTPError as e:
        return mcp_error(f"HTTP error fetching {url}: {e}")

    # Non-retryable client errors (4xx except 429, which was retried above)
    if 400 <= resp.status_code < 500:
        hint = _ERROR_HINTS.get(resp.status_code, "")
        return mcp_error(f"HTTP {resp.status_code} for {url}. {hint}")

    # Extract text
    ct = resp.headers.get("content-type", "")
    raw = resp.text

    if "application/pdf" in ct:
        return _save_pdf(url, resp.content)

    if "text/plain" in ct or "application/json" in ct:
        return FetchResult(text=raw, title="")

    json_str = trafilatura.extract(
        raw,
        include_comments=False,
        include_tables=True,
        no_fallback=False,
        with_metadata=True,
        output_format="json",
        include_images=True,
        include_links=True,
    )
    if json_str:
        result = FetchResult.model_validate_json(json_str)
        if result.text:
            return result

    # JS detection: trafilatura failed but substantial HTML present
    if len(raw) > 500:
        logger.info("JS detected for %s, trying Playwright", url[:80])
        pw_result = await _playwright_render(url)
        if pw_result:
            return pw_result
        return mcp_error(
            f"Could not extract text from {url} (JavaScript-rendered page). "
            "Playwright also failed. Try search_exa for indexed content."
        )

    return mcp_error(f"No content could be extracted from {url}.")
