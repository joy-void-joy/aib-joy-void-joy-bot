#!/usr/bin/env python3
"""Check what aggregation/CP data the Metaculus API returns for resolved AIB questions."""

import asyncio
import httpx
import typer

app = typer.Typer()


@app.command()
def main(
    tournament_id: int = typer.Option(32916, help="Tournament ID"),
    limit: int = typer.Option(5, help="Number of questions to check"),
) -> None:
    """Inspect aggregation data in resolved question API responses."""
    asyncio.run(_check(tournament_id, limit))


async def _check(tournament_id: int, limit: int) -> None:
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            "https://www.metaculus.com/api/posts/",
            params={
                "order_by": "-resolve_time",
                "status": "resolved",
                "tournaments": tournament_id,
                "limit": limit,
            },
        )
        response.raise_for_status()
        results = response.json().get("results", [])

        for r in results:
            post_id = r.get("id")
            title = r.get("title", "")[:60]
            q = r.get("question", {})
            resolution = q.get("resolution")
            aggs = q.get("aggregations", {})
            qtype = q.get("type")

            print(f"\n=== {post_id}: {title} ===")
            print(f"  type: {qtype}")
            print(f"  resolution: {resolution}")
            print(f"  aggregation keys: {list(aggs.keys())}")
            for key, val in aggs.items():
                if isinstance(val, dict):
                    latest = val.get("latest")
                    history_len = len(val.get("history", []))
                    print(
                        f"  {key}: latest={'yes' if latest else 'no'}, "
                        f"history_len={history_len}"
                    )
                    if latest:
                        centers = latest.get("centers", [])
                        print(f"    centers: {centers[:3]}")
                else:
                    print(f"  {key}: {type(val).__name__}")


@app.command("single")
def single(
    post_id: int = typer.Argument(help="Post ID to check"),
) -> None:
    """Inspect a single question's aggregation data via direct fetch."""
    asyncio.run(_check_single(post_id))


async def _check_single(post_id: int) -> None:
    from aib.config import settings  # noqa: F401 — loads env
    from metaculus.client import AsyncMetaculusClient

    async with AsyncMetaculusClient() as mc:
        r = await mc.fetch_post_json(post_id)

        title = r.get("title", "")[:60]
        q = r.get("question", {})
        resolution = q.get("resolution")
        aggs = q.get("aggregations", {})
        qtype = q.get("type")

        print(f"\n=== {post_id}: {title} ===")
        print(f"  type: {qtype}")
        print(f"  resolution: {resolution}")
        print(f"  aggregation keys: {list(aggs.keys())}")
        for key, val in aggs.items():
            if isinstance(val, dict):
                latest = val.get("latest")
                history_len = len(val.get("history", []))
                print(
                    f"  {key}: latest={'yes' if latest else 'no'}, "
                    f"history_len={history_len}"
                )
                if latest:
                    centers = latest.get("centers", [])
                    print(f"    centers: {centers[:3]}")
            else:
                print(f"  {key}: {type(val).__name__}")


if __name__ == "__main__":
    app()
