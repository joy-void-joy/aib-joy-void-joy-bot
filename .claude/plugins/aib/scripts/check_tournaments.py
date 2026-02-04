#!/usr/bin/env python
"""Check tournament status on Metaculus."""

import asyncio

from aib.clients.metaculus import get_client


async def main() -> None:
    client = get_client()

    for slug in ["spring-aib-2026", "minibench"]:
        print(f"\n=== {slug} ===")
        try:
            questions = await client.get_all_open_questions_from_tournament(slug)
            print(f"Open questions: {len(questions)}")
            for q in questions[:5]:
                print(f"  - [{q.id_of_post}] {q.question_text[:50]}...")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    asyncio.run(main())
