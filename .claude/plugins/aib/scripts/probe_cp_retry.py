#!/usr/bin/env python
"""Focused retry: test aggregation_explorer with minimize=true + aggregation_methods."""

import asyncio
import json
import time

import httpx
import typer

from aib.config import settings

app = typer.Typer()


def _headers() -> dict[str, str]:
    return {
        "Authorization": f"Token {settings.metaculus_token}",
        "Accept-Language": "en",
    }


def _print_agg(data: dict) -> None:
    """Print aggregation data from a response."""
    q = data.get("question") or data
    agg = q.get("aggregations")
    if agg is None:
        print("  aggregations: NULL")
    elif not agg:
        print("  aggregations: empty")
    else:
        print(f"  aggregation keys: {list(agg.keys())}")
        for k, v in agg.items():
            if isinstance(v, dict):
                h = v.get("history", [])
                lat = "present" if v.get("latest") else "NULL"
                print(f"    {k}: {len(h)} history entries, latest={lat}")
                if h:
                    print(f"    first: {json.dumps(h[0])[:200]}")
                    if len(h) > 1:
                        print(f"    last:  {json.dumps(h[-1])[:200]}")
            else:
                print(f"    {k}: {type(v).__name__}")


async def run_probes() -> None:
    print("Waiting 30s for rate limit cooldown...")
    time.sleep(30)

    async with httpx.AsyncClient(timeout=60.0) as client:
        # Test 1: minimize=true with aggregation_methods for resolved
        print("\n=== T1: resolved 41835, minimize=true, aggregation_methods ===")
        resp1 = await client.get(
            "https://www.metaculus.com/api/aggregation_explorer/",
            headers=_headers(),
            params={
                "post_id": 41835,
                "aggregation_methods": "recency_weighted,unweighted",
            },
        )
        print(f"Status: {resp1.status_code}")
        if resp1.status_code == 200:
            _print_agg(resp1.json())
        else:
            print(f"Body: {resp1.text[:400]}")

        time.sleep(5)

        # Test 2: minimize=true with aggregation_methods for open
        print(
            "\n=== T2: open 3479, minimize=true, aggregation_methods=recency_weighted ==="
        )
        resp2 = await client.get(
            "https://www.metaculus.com/api/aggregation_explorer/",
            headers=_headers(),
            params={
                "post_id": 3479,
                "aggregation_methods": "recency_weighted",
            },
        )
        print(f"Status: {resp2.status_code}")
        if resp2.status_code == 200:
            _print_agg(resp2.json())
        else:
            print(f"Body: {resp2.text[:400]}")

        time.sleep(5)

        # Test 3: For the resolved question, check if CP is hidden on the question object
        print("\n=== T3: resolved 41835, no aggregation_methods (default) ===")
        resp3 = await client.get(
            "https://www.metaculus.com/api/aggregation_explorer/",
            headers=_headers(),
            params={"post_id": 41835},
        )
        print(f"Status: {resp3.status_code}")
        if resp3.status_code == 200:
            _print_agg(resp3.json())
            # Also check other top-level keys
            data = resp3.json()
            print(f"  top-level keys: {list(data.keys())[:20]}")
            q = data.get("question") or {}
            for k in (
                "is_cp_hidden",
                "cp_reveal_time",
                "status",
                "default_aggregation_method",
            ):
                if k in q:
                    print(f"  question.{k}: {q[k]}")
        else:
            print(f"Body: {resp3.text[:400]}")


@app.command()
def main() -> None:
    """Run focused aggregation probes."""
    asyncio.run(run_probes())


if __name__ == "__main__":
    app()
