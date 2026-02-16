"""Dump the full API JSON for a question to inspect all fields."""

import asyncio
import json
import os
from pathlib import Path

import httpx
import typer
from dotenv import load_dotenv

app = typer.Typer()


async def _dump(post_id: int) -> None:
    token = os.getenv("METACULUS_TOKEN")
    base = "https://www.metaculus.com/api"
    headers = {"Authorization": f"Token {token}", "Accept-Language": "en"}

    async with httpx.AsyncClient(timeout=30) as client:
        r = await client.get(f"{base}/posts/{post_id}/", headers=headers)
        r.raise_for_status()
        data = r.json()

        # Print the full question JSON
        question = data.get("question") or {}
        print(json.dumps(question, indent=2, default=str))


@app.command()
def dump(
    post_id: int = typer.Argument(help="Post ID to dump"),
) -> None:
    """Dump the full question JSON from the API."""
    project_root = Path(__file__).resolve().parents[4]
    load_dotenv(project_root / ".env")
    load_dotenv(project_root / ".env.local", override=True)
    asyncio.run(_dump(post_id))


if __name__ == "__main__":
    app()
