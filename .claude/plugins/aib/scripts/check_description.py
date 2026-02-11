"""Check whether AsyncMetaculusClient returns description for a question."""

import asyncio

import typer

from aib.config import settings
from metaculus.client import AsyncMetaculusClient


app = typer.Typer()


@app.command()
def check(post_id: int = typer.Argument(help="Post ID to check")) -> None:
    """Fetch a question and inspect description-related fields."""
    asyncio.run(_check(post_id))


async def _check(post_id: int) -> None:
    async with AsyncMetaculusClient(token=settings.metaculus_token) as client:
        q = await client.get_question_by_post_id(post_id)

        if isinstance(q, list):
            print(f"Got {len(q)} questions (group question)")
            for i, sub_q in enumerate(q):
                print(f"\n--- Sub-question {i} ---")
                _print_info(sub_q)
        else:
            _print_info(q)


def _print_info(q) -> None:  # noqa: ANN001
    from metaculus.models import MetaculusQuestion

    assert isinstance(q, MetaculusQuestion)

    print(f"Post ID: {q.id_of_post}")
    print(f"Question ID: {q.id_of_question}")
    print(f"Type: {q.get_question_type()}")
    print(f"Title: {q.question_text}")
    print()

    # Check the parsed field
    print(f"background_info (from model): {_truncate(q.background_info)}")
    print(f"resolution_criteria (from model): {_truncate(q.resolution_criteria)}")
    print(f"fine_print (from model): {_truncate(q.fine_print)}")
    print()

    # Check raw API JSON
    api = q.api_json
    question_json = api.get("question", {})

    # Post-level fields
    print("=== Post-level fields ===")
    for key in ("description", "title", "html_description"):
        val = api.get(key)
        if val is not None:
            print(f"  post['{key}']: {_truncate(val)}")
        else:
            print(f"  post['{key}']: NOT PRESENT")

    # Question-level fields
    print("\n=== Question-level fields ===")
    for key in ("description", "title", "resolution_criteria", "fine_print"):
        val = question_json.get(key)
        if val is not None:
            print(f"  question['{key}']: {_truncate(val)}")
        else:
            print(f"  question['{key}']: NOT PRESENT")

    # Show all top-level keys for reference
    print("\n=== All post-level keys ===")
    print(f"  {sorted(api.keys())}")
    print("\n=== All question-level keys ===")
    print(f"  {sorted(question_json.keys())}")


def _truncate(text: str | None, max_len: int = 200) -> str:
    if text is None:
        return "None"
    if len(text) <= max_len:
        return repr(text)
    return repr(text[:max_len]) + "..."


if __name__ == "__main__":
    app()
