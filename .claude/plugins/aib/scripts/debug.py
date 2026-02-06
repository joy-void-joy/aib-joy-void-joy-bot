#!/usr/bin/env python
"""Debug tools for Metaculus API, MCP error propagation, and more."""

import asyncio
import traceback

import httpx
import typer

from aib.clients.metaculus import get_client
from aib.config import settings
from metaculus.models import MetaculusQuestion

app = typer.Typer(help="Debug tools for the forecasting agent.")


# --- Metaculus API Debugging ---


async def test_raw_parse(tournament: str, limit: int) -> None:
    """Test raw API fetch and parsing."""
    print("=== Raw API Parse Test ===")
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            "https://www.metaculus.com/api/posts/",
            headers={
                "Authorization": f"Token {settings.metaculus_token}",
                "Accept-Language": "en",
            },
            params={
                "tournaments": tournament,
                "status": "open",
                "limit": limit,
            },
        )
        data = response.json()
        results = data["results"]
        print(f"Fetched {len(results)} posts")

        for i, result in enumerate(results):
            print(f"\n--- Post {i + 1} ---")
            print(f"ID: {result.get('id')}")
            print(f"Title: {result.get('title', '')[:60]}...")

            try:
                q = MetaculusQuestion.from_api_json(result)
                print(f"Parsed OK: {type(q).__name__}")
            except Exception as e:
                print(f"Parse ERROR: {type(e).__name__}: {e}")
                traceback.print_exc()


async def test_client(tournament: str) -> None:
    """Test the full client flow."""
    print("\n=== Client Test ===", flush=True)
    client = get_client()
    print(f"Token length: {len(client.token) if client.token else 0}", flush=True)

    # First, fetch raw to see the structure
    async with httpx.AsyncClient(timeout=30.0) as http_client:
        response = await http_client.get(
            "https://www.metaculus.com/api/posts/",
            headers=client._get_headers(),
            params={
                "tournaments": tournament,
                "status": "open",
                "limit": 10,
            },
        )
        data = response.json()
        results = data["results"]
        print(f"Raw fetch: {len(results)} posts")
        for r in results:
            has_question = "question" in r and r["question"] is not None
            has_group = "group_of_questions" in r
            has_conditional = "conditional" in r
            print(
                f"  - {r.get('id')}: question={has_question}, "
                f"group={has_group}, conditional={has_conditional}"
            )

    try:
        questions = await client.get_all_open_questions_from_tournament(tournament)
        print(f"Parsed {len(questions)} questions")
        for q in questions[:3]:
            print(f"  - [{q.id_of_post}] {type(q).__name__}: {q.question_text[:40]}...")
    except Exception as e:
        print(f"Error: {type(e).__name__}: {e}")
        traceback.print_exc()


async def check_raw_status(tournament: str, limit: int) -> None:
    """Check raw API status vs close_time for questions."""
    from datetime import datetime, timezone

    print(f"=== Raw API Status Check for {tournament} ===")
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            "https://www.metaculus.com/api/posts/",
            headers={
                "Authorization": f"Token {settings.metaculus_token}",
                "Accept-Language": "en",
            },
            params={
                "tournaments": tournament,
                "status": "open",
                "limit": limit,
            },
        )
        data = response.json()
        results = data["results"]

    now = datetime.now(timezone.utc)
    print(f"Current time: {now.isoformat()}")
    print(f"Returned {len(results)} posts with status=open filter\n")

    for r in results[:limit]:
        post_status = r.get("status")
        q = r.get("question") or {}
        q_status = q.get("status")
        close_time_str = q.get("scheduled_close_time") or q.get("actual_close_time")
        close_time = None
        if close_time_str:
            close_time = datetime.fromisoformat(close_time_str.replace("Z", "+00:00"))
            is_past = close_time < now
        else:
            is_past = "?"

        print(
            f"  [{r.get('id')}] post.status={post_status!r}, "
            f"question.status={q_status!r}, close_time_past={is_past}"
        )


async def check_question_times(tournament: str, limit: int) -> None:
    """Check open/close times of questions in a tournament."""
    from datetime import datetime, timezone

    print(f"\n=== Question Times for {tournament} ===")
    client = get_client()
    questions = await client.get_all_open_questions_from_tournament(tournament)

    now = datetime.now(timezone.utc)
    print(f"Current time: {now.isoformat()}")
    print(f"Total open questions: {len(questions)}\n")

    # Sort by close_time
    questions_with_close = [q for q in questions if q.close_time]
    questions_with_close.sort(key=lambda q: q.close_time)  # type: ignore

    for q in questions_with_close[:limit]:
        close_time = q.close_time
        open_time = q.open_time

        if close_time:
            time_left = close_time - now
            hours_left = time_left.total_seconds() / 3600
            status = f"{hours_left:+.1f}h" if hours_left > 0 else "CLOSED"
        else:
            status = "no close_time"

        open_str = open_time.strftime("%m/%d %H:%M") if open_time else "?"
        close_str = close_time.strftime("%m/%d %H:%M") if close_time else "?"

        print(f"  [{q.id_of_post}] {status:>8} | open={open_str} close={close_str}")
        print(f"           {q.question_text[:55]}...")

    if len(questions_with_close) > limit:
        print(f"\n  ... and {len(questions_with_close) - limit} more")


@app.command()
def metaculus(
    tournament: str = typer.Option("spring-aib-2026", help="Tournament slug"),
    limit: int = typer.Option(5, help="Number of posts to fetch"),
    raw_only: bool = typer.Option(False, "--raw-only", help="Only test raw parsing"),
    client_only: bool = typer.Option(False, "--client-only", help="Only test client"),
) -> None:
    """Debug Metaculus API parsing and client."""

    async def run() -> None:
        if not client_only:
            await test_raw_parse(tournament, limit)
        if not raw_only:
            await test_client(tournament)

    asyncio.run(run())


@app.command()
def times(
    tournament: str = typer.Option("spring-aib-2026", help="Tournament slug"),
    limit: int = typer.Option(20, help="Number of questions to show"),
) -> None:
    """Check open/close times of questions in a tournament."""
    asyncio.run(check_question_times(tournament, limit))


@app.command()
def raw_status(
    tournament: str = typer.Option("spring-aib-2026", help="Tournament slug"),
    limit: int = typer.Option(20, help="Number of questions to show"),
) -> None:
    """Check raw API status vs actual close times."""
    asyncio.run(check_raw_status(tournament, limit))


# --- MCP Error Propagation Debugging ---


@app.command("mcp-error")
def mcp_error_test() -> None:
    """Test if is_error property works on our CallToolResult subclass."""
    from aib.tools.mcp_server import _CallToolResultWithAlias
    from mcp.types import TextContent

    print("=== MCP Error Propagation Test ===\n")

    # Test with isError=True
    result = _CallToolResultWithAlias(
        content=[TextContent(type="text", text="Test error message")],
        isError=True,
    )

    print("Created _CallToolResultWithAlias with isError=True")
    print(f"  type(result): {type(result).__name__}")
    print(f"  result.isError: {result.isError}")
    print(f"  hasattr(result, 'is_error'): {hasattr(result, 'is_error')}")

    try:
        is_error_val = result.is_error
        print(f"  result.is_error: {is_error_val}")
    except Exception as e:
        print(f"  result.is_error FAILED: {type(e).__name__}: {e}")
        is_error_val = None

    # Test with isError=False
    print("\nCreated _CallToolResultWithAlias with isError=False")
    result2 = _CallToolResultWithAlias(
        content=[TextContent(type="text", text="Success")],
        isError=False,
    )
    print(f"  result2.isError: {result2.isError}")
    print(f"  result2.is_error: {result2.is_error}")

    # Summary
    print("\n=== Summary ===")
    if hasattr(result, "is_error") and is_error_val is True:
        print("✅ is_error property works correctly")
    else:
        print("❌ is_error property NOT working - SDK bug workaround failed")


if __name__ == "__main__":
    app()
