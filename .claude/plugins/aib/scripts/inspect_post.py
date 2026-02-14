#!/usr/bin/env python
"""Inspect raw API response for a Metaculus post."""

import asyncio

import typer

from aib.clients.metaculus import AsyncMetaculusClient

app = typer.Typer()


@app.command()
def main(
    post_id: int = typer.Argument(help="Post ID to inspect"),
    keys_only: bool = typer.Option(False, "--keys", help="Show only top-level keys"),
    field: str = typer.Option(
        "", "--field", "-f", help="Show specific field path (dot-separated)"
    ),
) -> None:
    """Inspect raw Metaculus API response for a post."""

    async def fetch() -> dict:
        async with AsyncMetaculusClient() as mc:
            return await mc.fetch_post_json(post_id)

    data = asyncio.run(fetch())

    if keys_only:
        print("Top-level keys:", sorted(data.keys()))
        if "question" in data:
            print("Question keys:", sorted(data["question"].keys()))
        return

    if field:
        obj = data
        for part in field.split("."):
            if isinstance(obj, dict):
                obj = obj.get(part)
            else:
                obj = None
                break
        if isinstance(obj, str):
            print(f"{field} ({len(obj)} chars):")
            print(obj[:500])
        elif obj is None:
            print(f"{field}: null/missing")
        else:
            import json

            print(f"{field}:")
            print(json.dumps(obj, indent=2, default=str)[:1000])
        return

    # Default: show description-related fields
    print(f"Post {post_id}")
    print(f"  title: {data.get('title', '')[:80]}")
    for key in ("description", "body", "markdown", "content", "url_title"):
        val = data.get(key)
        if val:
            print(f"  post.{key}: ({len(val)} chars) {str(val)[:100]}")
        else:
            print(f"  post.{key}: {val!r}")

    q = data.get("question") or {}
    print(f"\n  question.title: {q.get('title', '')[:80]}")
    for key in ("description", "resolution_criteria", "fine_print", "body", "markdown"):
        val = q.get(key)
        if val:
            print(f"  question.{key}: ({len(val)} chars) {str(val)[:100]}")
        else:
            print(f"  question.{key}: {val!r}")


if __name__ == "__main__":
    app()
