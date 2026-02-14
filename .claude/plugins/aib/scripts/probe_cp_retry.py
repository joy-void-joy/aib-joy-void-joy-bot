#!/usr/bin/env python
"""Probe aggregation/CP data availability via the Metaculus client."""

import asyncio
import json

import typer

app = typer.Typer()


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
    from aib.clients.metaculus import AsyncMetaculusClient

    async with AsyncMetaculusClient() as mc:
        # Test 1: resolved question with CP
        print("\n=== T1: resolved 41835, with_cp=True ===")
        data1 = await mc.fetch_post_json(41835, with_cp=True)
        print(f"  title: {data1.get('title', '')[:60]}")
        _print_agg(data1)

        # Test 2: open question with CP
        print("\n=== T2: open 3479, with_cp=True ===")
        data2 = await mc.fetch_post_json(3479, with_cp=True)
        print(f"  title: {data2.get('title', '')[:60]}")
        _print_agg(data2)

        # Test 3: resolved question without CP
        print("\n=== T3: resolved 41835, with_cp=False (default) ===")
        data3 = await mc.fetch_post_json(41835)
        print(f"  title: {data3.get('title', '')[:60]}")
        _print_agg(data3)

        q = data3.get("question") or {}
        for k in (
            "is_cp_hidden",
            "cp_reveal_time",
            "status",
            "default_aggregation_method",
        ):
            if k in q:
                print(f"  question.{k}: {q[k]}")


@app.command()
def main() -> None:
    """Run focused aggregation probes."""
    asyncio.run(run_probes())


if __name__ == "__main__":
    app()
