"""Test specific enrichment approaches for getting question text fields."""

import asyncio
import os
from pathlib import Path

import httpx
import typer
from dotenv import load_dotenv

app = typer.Typer()


def _trunc(val: object, max_len: int = 200) -> str:
    if val is None:
        return "None"
    s = str(val)
    return s[:max_len] + "..." if len(s) > max_len else s


async def _test_enrichment(post_id: int) -> None:
    token = os.getenv("METACULUS_TOKEN")
    base = "https://www.metaculus.com/api"
    headers = {"Authorization": f"Token {token}", "Accept-Language": "en"}

    async with httpx.AsyncClient(timeout=30) as client:
        # Approach 1: ?format=api
        print("1. ?format=api ...")
        r1 = await client.get(
            f"{base}/posts/{post_id}/",
            headers=headers,
            params={"format": "api"},
        )
        print(
            f"   Status: {r1.status_code}, Content-Type: {r1.headers.get('content-type', 'unknown')}"
        )
        if r1.status_code == 200:
            ct = r1.headers.get("content-type", "")
            if "html" in ct:
                from metaculus.client import _parse_html_api_response

                html_data = _parse_html_api_response(r1.text)
                if html_data:
                    hq = html_data.get("question") or {}
                    print(f"   description: {_trunc(hq.get('description'))}")
                    print(
                        f"   resolution_criteria: {_trunc(hq.get('resolution_criteria'))}"
                    )
                    print(f"   fine_print: {_trunc(hq.get('fine_print'))}")
                else:
                    print("   HTML parse failed")
            else:
                fq = r1.json().get("question") or {}
                print(f"   description: {_trunc(fq.get('description'))}")
                print(
                    f"   resolution_criteria: {_trunc(fq.get('resolution_criteria'))}"
                )

        await asyncio.sleep(5)

        # Approach 2: ?format=json (explicit)
        print("\n2. ?format=json ...")
        r2 = await client.get(
            f"{base}/posts/{post_id}/",
            headers=headers,
            params={"format": "json"},
        )
        print(f"   Status: {r2.status_code}")
        if r2.status_code == 200:
            fq2 = r2.json().get("question") or {}
            desc = fq2.get("description")
            rc = fq2.get("resolution_criteria")
            print(f"   description: {_trunc(desc)}")
            print(f"   resolution_criteria: {_trunc(rc)}")
            # Print ALL question keys to see what's available
            print(f"   Question keys: {sorted(fq2.keys())}")

        await asyncio.sleep(5)

        # Approach 3: Question ID endpoint
        print("\n3. Fetching question keys from post to find question_id...")
        if r2.status_code == 200:
            qid = r2.json().get("question", {}).get("id")
            if qid:
                print(f"   Question ID: {qid}")
                await asyncio.sleep(3)
                r3 = await client.get(
                    f"{base}/questions/{qid}/",
                    headers=headers,
                )
                print(f"   /api/questions/{qid}/ status: {r3.status_code}")
                if r3.status_code == 200:
                    q3 = r3.json()
                    print(f"   Keys: {sorted(q3.keys())[:20]}")
                    print(f"   description: {_trunc(q3.get('description'))}")
                    print(
                        f"   resolution_criteria: {_trunc(q3.get('resolution_criteria'))}"
                    )
                    print(f"   fine_print: {_trunc(q3.get('fine_print'))}")

        await asyncio.sleep(5)

        # Approach 4: HTML without auth token
        print("\n4. HTML API without auth...")
        r4 = await client.get(
            f"{base}/posts/{post_id}/",
            headers={"Accept": "text/html", "Accept-Language": "en"},
        )
        print(f"   Status: {r4.status_code}")

        await asyncio.sleep(5)

        # Approach 5: ?format=api without auth
        print("\n5. ?format=api without auth...")
        r5 = await client.get(
            f"{base}/posts/{post_id}/",
            headers={"Accept-Language": "en"},
            params={"format": "api"},
        )
        print(
            f"   Status: {r5.status_code}, Content-Type: {r5.headers.get('content-type', 'unknown')}"
        )
        if r5.status_code == 200:
            ct5 = r5.headers.get("content-type", "")
            if "html" in ct5:
                from metaculus.client import _parse_html_api_response

                html_data5 = _parse_html_api_response(r5.text)
                if html_data5:
                    hq5 = html_data5.get("question") or {}
                    print(f"   description: {_trunc(hq5.get('description'))}")
                    print(
                        f"   resolution_criteria: {_trunc(hq5.get('resolution_criteria'))}"
                    )
                    print(f"   fine_print: {_trunc(hq5.get('fine_print'))}")
                else:
                    print("   HTML parse failed")


@app.command()
def test(
    post_id: int = typer.Argument(help="Post ID to test enrichment for"),
) -> None:
    """Test enrichment approaches for a question."""
    project_root = Path(__file__).resolve().parents[4]
    load_dotenv(project_root / ".env")
    load_dotenv(project_root / ".env.local", override=True)
    asyncio.run(_test_enrichment(post_id))


if __name__ == "__main__":
    app()
