#!/usr/bin/env python3
"""Check resolutions of specific questions."""

import asyncio
import sys
from pathlib import Path

import typer

# Resolve imports from src/
sys.path.insert(0, str(Path(__file__).parent.parent.parent / "src"))

# Import config first to set up environment variables
from aib.config import settings  # noqa: F401

from metaculus import AsyncMetaculusClient, BinaryQuestion

app = typer.Typer()


@app.command()
def check(question_ids: list[int] = typer.Argument(..., help="Question IDs to check")):
    """Check resolution status of specific questions."""

    async def _check():
        client = AsyncMetaculusClient()
        for qid in question_ids:
            try:
                q = await client.get_question_by_post_id(qid)
                print(f"\n=== Question {qid} ===")
                print(f"Title: {q.question_text[:100]}...")
                print(f"Type: {q.get_question_type()}")
                print(f"Resolution: {q.resolution_string}")
                if isinstance(q, BinaryQuestion) and q.community_prediction_at_access_time is not None:
                    print(f"Final CP: {q.community_prediction_at_access_time:.1%}")
            except Exception as e:
                print(f"\n=== Question {qid} ===")
                print(f"Error: {e}")

    asyncio.run(_check())


if __name__ == "__main__":
    app()
