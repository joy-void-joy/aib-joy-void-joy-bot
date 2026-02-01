#!/usr/bin/env python
"""Debug Metaculus API parsing and client."""

import asyncio
import traceback

import httpx
import typer

from aib.clients.metaculus import get_client
from aib.config import settings
from metaculus.models import MetaculusQuestion


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


app = typer.Typer()


@app.command()
def main(
    tournament: str = typer.Option("spring-aib-2026", help="Tournament slug"),
    limit: int = typer.Option(5, help="Number of posts to fetch"),
    raw_only: bool = typer.Option(False, "--raw-only", help="Only test raw parsing"),
    client_only: bool = typer.Option(False, "--client-only", help="Only test client"),
) -> None:
    """Debug Metaculus API parsing and client."""
    async def run():
        if not client_only:
            await test_raw_parse(tournament, limit)
        if not raw_only:
            await test_client(tournament)

    asyncio.run(run())


if __name__ == "__main__":
    app()
