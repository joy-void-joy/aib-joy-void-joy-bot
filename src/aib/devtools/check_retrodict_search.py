#!/usr/bin/env python
"""Diagnose empty results from the retrodict search pipeline.

Tests each layer independently:
1. Wayback availability API (can we reach archive.org?)
2. Wayback content fetch (does trafilatura extract anything?)
3. Raw web search sub-agent (does Haiku return results?)
4. Full pipeline (raw search → Wayback filter)
"""

import asyncio
import json
import logging

import typer

from aib.tools.search import SearchResult

app = typer.Typer()

logging.basicConfig(
    level=logging.DEBUG,
    format="%(name)s %(levelname)s %(message)s",
)
log = logging.getLogger("check_retrodict_search")


async def check_wayback_availability_layer(
    url: str, timestamp: str
) -> dict[str, str] | None:
    """Layer 1: Can we reach the Wayback availability API?"""
    from aib.tools.wayback import check_wayback_availability

    log.info("--- Layer 1: Wayback availability for %s @ %s ---", url, timestamp)
    result = await check_wayback_availability(
        url, timestamp, validate_before_cutoff=True
    )
    if result is None:
        log.warning("No snapshot found (or snapshot is after cutoff)")
    else:
        log.info("Snapshot found: %s", json.dumps(result, indent=2))

    # Also check without cutoff validation
    result_any = await check_wayback_availability(
        url, timestamp, validate_before_cutoff=False
    )
    if result_any and result is None:
        log.warning(
            "Snapshot exists but AFTER cutoff! ts=%s",
            result_any.get("timestamp"),
        )
    return result


async def check_wayback_content_layer(url: str, timestamp: str) -> str | None:
    """Layer 2: Does fetch_wayback_content return text?"""
    from aib.tools.wayback import fetch_wayback_content

    log.info("--- Layer 2: Wayback content fetch for %s @ %s ---", url, timestamp)
    content = await fetch_wayback_content(url, timestamp)
    if content is None:
        log.warning("fetch_wayback_content returned None")
    else:
        log.info("Got %d chars of content", len(content))
        log.info("Preview: %s", content[:200])
    return content


async def check_raw_search_layer(query: str, cutoff_date: str) -> list[SearchResult]:
    """Layer 3: Does the Haiku sub-agent return any results?

    Runs the sub-agent inline (instead of calling _raw_web_search) so we can
    print every content block and see what Haiku is doing with its turns.
    """
    import json as _json

    from claude_agent_sdk import (
        AssistantMessage,
        ClaudeAgentOptions,
        ClaudeSDKClient,
        ResultMessage,
    )

    from aib.agent.display import print_block
    from aib.tools.search import (
        _SearchResultsOutput,
        _make_tool_filter_hook,
    )
    from claude_agent_sdk import HookMatcher

    log.info("--- Layer 3: Raw web search for %r cutoff=%s ---", query, cutoff_date)

    prompt = (
        f"Search the web for: {query}\n\n"
        f"Constraints:\n"
        f"- Focus on information published before {cutoff_date}. "
        "Include date context in your search query.\n\n"
        "Return the search results."
    )

    options = ClaudeAgentOptions(
        model="haiku",
        max_turns=3,
        permission_mode="bypassPermissions",
        allowed_tools=["WebSearch"],
        hooks={
            "PreToolUse": [
                HookMatcher(
                    hooks=[
                        _make_tool_filter_hook(
                            frozenset({"WebSearch", "StructuredOutput"})
                        )
                    ]
                )
            ],
        },
        system_prompt=(
            "You are a web search assistant. Use WebSearch to find information, "
            "then return the results with title, url, and snippet for each."
        ),
        output_format={
            "type": "json_schema",
            "schema": _SearchResultsOutput.model_json_schema(),
        },
        extra_args={"no-session-persistence": None},
    )

    data = None
    async with ClaudeSDKClient(options=options) as client:
        await client.query(prompt)
        async for message in client.receive_response():
            if isinstance(message, AssistantMessage):
                log.info("--- AssistantMessage (turn) ---")
                for block in message.content:
                    print_block(block, prefix="  [search] ")
            elif isinstance(message, ResultMessage):
                log.info(
                    "ResultMessage: subtype=%s turns=%d is_error=%s",
                    message.subtype,
                    message.num_turns,
                    message.is_error,
                )
                log.info("  result=%s", (message.result or "")[:500])
                log.info("  structured_output=%s", message.structured_output)
                if data is None:
                    if message.structured_output:
                        data = message.structured_output
                    elif message.result:
                        data = _json.loads(message.result)

    if not data or not isinstance(data.get("results"), list):
        log.warning("Sub-agent returned no structured results")
        return []

    results: list[SearchResult] = [
        SearchResult(
            title=item.get("title", ""),
            url=item["url"],
            snippet=item.get("snippet"),
        )
        for item in data["results"]
        if isinstance(item, dict) and item.get("url")
    ]
    log.info("Raw search returned %d results", len(results))
    for i, r in enumerate(results):
        log.info("  [%d] %s  %s", i, r.get("url", "?"), r.get("title", "?"))
    return results


async def check_wayback_filter_layer(
    results: list[SearchResult], cutoff_date: str
) -> list[SearchResult]:
    """Layer 4: How many results survive Wayback filtering?"""
    from aib.tools.search import _wayback_filter_results

    log.info("--- Layer 4: Wayback filter on %d results ---", len(results))
    filtered = await _wayback_filter_results(results, cutoff_date)
    log.info("Filtered: %d/%d survived", len(filtered), len(results))
    for i, r in enumerate(filtered):
        log.info("  [%d] %s", i, r.get("url", "?"))
    return filtered


async def run_all(query: str, cutoff_date: str, test_url: str | None) -> None:
    wayback_ts = cutoff_date.replace("-", "")

    # Layer 1 & 2: test with a known URL
    if test_url:
        await check_wayback_availability_layer(test_url, wayback_ts)
        await check_wayback_content_layer(test_url, wayback_ts)
    else:
        log.info("Skipping layers 1-2 (no --test-url provided)")

    # Layer 3: raw search
    results = await check_raw_search_layer(query, cutoff_date)
    if not results:
        log.error("DIAGNOSIS: _raw_web_search returned 0 results.")
        log.error("  → The Haiku sub-agent isn't returning structured output.")
        log.error("  → Check: is the SDK available? model=haiku reachable?")
        return

    # Layer 4: Wayback filter
    filtered = await check_wayback_filter_layer(results, cutoff_date)
    if not filtered:
        log.error("DIAGNOSIS: All %d results dropped by Wayback filter.", len(results))
        log.error("  → None of the URLs had pre-cutoff Wayback snapshots.")
        log.error("  → Try a broader cutoff or check if archive.org is reachable.")
    else:
        log.info("SUCCESS: %d results survived the full pipeline.", len(filtered))


@app.command()
def main(
    query: str = typer.Argument(
        "US inflation rate 2025",
        help="Search query to test",
    ),
    cutoff_date: str = typer.Option(
        "2026-01-15",
        "--cutoff",
        "-c",
        help="Cutoff date (YYYY-MM-DD)",
    ),
    test_url: str = typer.Option(
        None,
        "--test-url",
        "-u",
        help="A known URL to test Wayback layers 1-2 with",
    ),
    layer: int = typer.Option(
        0,
        "--layer",
        "-l",
        help="Run only this layer (1-4), or 0 for all",
    ),
) -> None:
    """Diagnose empty results from retrodict search pipeline."""

    async def _run() -> None:
        wayback_ts = cutoff_date.replace("-", "")

        if layer == 1:
            url = test_url or "https://en.wikipedia.org/wiki/Main_Page"
            await check_wayback_availability_layer(url, wayback_ts)
        elif layer == 2:
            url = test_url or "https://en.wikipedia.org/wiki/Main_Page"
            await check_wayback_content_layer(url, wayback_ts)
        elif layer == 3:
            await check_raw_search_layer(query, cutoff_date)
        elif layer == 4:
            results = await check_raw_search_layer(query, cutoff_date)
            if results:
                await check_wayback_filter_layer(results, cutoff_date)
        else:
            await run_all(query, cutoff_date, test_url)

    asyncio.run(_run())


if __name__ == "__main__":
    app()
