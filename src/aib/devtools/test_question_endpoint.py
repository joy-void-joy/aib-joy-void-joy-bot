"""Test the /api/questions/{id}/ endpoint for text fields."""

import asyncio
import json
import os
from pathlib import Path

import httpx
import typer
from dotenv import load_dotenv

app = typer.Typer()


def _trunc(val: object, max_len: int = 300) -> str:
    if val is None:
        return "None"
    s = str(val)
    return s[:max_len] + "..." if len(s) > max_len else s


async def _test(question_id: int) -> None:
    token = os.getenv("METACULUS_TOKEN")
    base = "https://www.metaculus.com/api"
    headers = {"Authorization": f"Token {token}", "Accept-Language": "en"}

    async with httpx.AsyncClient(timeout=30) as client:
        print(f"Fetching /api/questions/{question_id}/ ...")
        r = await client.get(
            f"{base}/questions/{question_id}/",
            headers=headers,
        )
        print(f"Status: {r.status_code}")
        if r.status_code == 200:
            data = r.json()
            print(f"Keys: {sorted(data.keys())}")
            print(f"description: {_trunc(data.get('description'))}")
            print(f"resolution_criteria: {_trunc(data.get('resolution_criteria'))}")
            print(f"fine_print: {_trunc(data.get('fine_print'))}")
            print(f"title: {_trunc(data.get('title'))}")
            print(f"type: {data.get('type')}")
            # Full JSON dump for inspection
            print(f"\nFull JSON:\n{json.dumps(data, indent=2, default=str)[:3000]}")
        else:
            print(f"Body: {r.text[:500]}")


@app.command()
def test(
    question_id: int = typer.Argument(help="Question ID (not post ID)"),
) -> None:
    """Test the questions endpoint."""
    project_root = Path(__file__).resolve().parents[4]
    load_dotenv(project_root / ".env")
    load_dotenv(project_root / ".env.local", override=True)
    asyncio.run(_test(question_id))


if __name__ == "__main__":
    app()
