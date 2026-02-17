"""API inspection and debugging tools.

Combines: inspect_api, module_info, inspect_post, check_cp, debug,
debug_websearch, and check_earnings_dates.
"""

import asyncio
import importlib
import inspect as pyinspect
import sys
import traceback
from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)


# ---------------------------------------------------------------------------
# inspect: Explore Python module APIs
# ---------------------------------------------------------------------------


def _resolve_target(target: str) -> tuple[object, None] | tuple[None, str]:
    """Resolve a dotted path to a Python object."""
    parts = target.split(".")

    for i in range(len(parts), 0, -1):
        module_path = ".".join(parts[:i])
        try:
            module = importlib.import_module(module_path)
            obj = module
            for attr in parts[i:]:
                obj = getattr(obj, attr)
            return obj, None
        except (ImportError, AttributeError):
            continue

    return None, f"Could not import or find: {target}"


def _print_summary(target: str, obj: object) -> None:
    """Print a summary of the object."""
    print(f"=== {target} ===\n")

    if hasattr(obj, "__doc__") and obj.__doc__:
        doc = obj.__doc__.strip().split("\n")[0]
        print(f"Doc: {doc}\n")

    public_attrs = [m for m in dir(obj) if not m.startswith("_")]

    if callable(obj) and not isinstance(obj, type):
        try:
            sig = pyinspect.signature(obj)
            print(f"Signature: {getattr(obj, '__name__', '?')}{sig}\n")
        except (ValueError, TypeError):
            pass
    else:
        methods: list[str] = []
        properties: list[str] = []
        constants: list[str] = []

        for attr in public_attrs:
            try:
                val = getattr(obj, attr)
                if callable(val):
                    methods.append(attr)
                elif isinstance(val, property):
                    properties.append(attr)
                else:
                    constants.append(attr)
            except AttributeError:
                constants.append(attr)

        if methods:
            print(f"Methods ({len(methods)}):")
            for m in sorted(methods):
                print(f"  - {m}")
            print()

        if properties:
            print(f"Properties ({len(properties)}):")
            for p in sorted(properties):
                print(f"  - {p}")
            print()

        if constants and len(constants) <= 20:
            print(f"Constants ({len(constants)}):")
            for c in sorted(constants):
                print(f"  - {c}")


@app.command("inspect")
def inspect_cmd(
    target: Annotated[
        str,
        typer.Argument(help="Module path like 'module.Class' or 'module.Class.method'"),
    ],
    help_full: Annotated[
        bool,
        typer.Option("--help-full", help="Show full help() output"),
    ] = False,
) -> None:
    """Inspect a Python module, class, or method."""
    obj, error = _resolve_target(target)

    if error:
        print(error, file=sys.stderr)
        raise typer.Exit(1)

    if help_full:
        help(obj)
    else:
        _print_summary(target, obj)


# ---------------------------------------------------------------------------
# module: Get paths and source code for installed modules
# ---------------------------------------------------------------------------


@app.command("module-path")
def module_path(
    module: Annotated[str, typer.Argument(help="Module name")],
) -> None:
    """Print the file path of a Python module."""
    mod = importlib.import_module(module)
    if hasattr(mod, "__file__") and mod.__file__:
        print(mod.__file__)
    else:
        print(
            f"Module {module} has no __file__ attribute (built-in or namespace package)"
        )
        raise typer.Exit(1)


@app.command("module-source")
def module_source(
    module: Annotated[str, typer.Argument(help="Module name")],
    lines: Annotated[
        int, typer.Option("--lines", "-n", help="Number of lines to show (0 = all)")
    ] = 100,
) -> None:
    """Print the source code of a Python module."""
    mod = importlib.import_module(module)
    try:
        src = pyinspect.getsource(mod)
        if lines > 0:
            source_lines = src.split("\n")
            src = "\n".join(source_lines[:lines])
            if len(source_lines) > lines:
                src += f"\n... ({len(source_lines) - lines} more lines)"
        print(src)
    except (TypeError, OSError) as e:
        print(f"Cannot get source for {module}: {e}")
        raise typer.Exit(1)


# ---------------------------------------------------------------------------
# post: Inspect raw API response for a Metaculus post
# ---------------------------------------------------------------------------


@app.command("post")
def post_cmd(
    post_id: int = typer.Argument(help="Post ID to inspect"),
    keys_only: bool = typer.Option(False, "--keys", help="Show only top-level keys"),
    field: str = typer.Option(
        "", "--field", "-f", help="Show specific field path (dot-separated)"
    ),
) -> None:
    """Inspect raw Metaculus API response for a post."""
    from aib.clients.metaculus import AsyncMetaculusClient

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
        import json

        obj: object = data
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
            print(f"{field}:")
            print(json.dumps(obj, indent=2, default=str)[:1000])
        return

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


# ---------------------------------------------------------------------------
# cp: Check aggregation/CP data
# ---------------------------------------------------------------------------


@app.command("cp")
def cp_cmd(
    tournament_id: int = typer.Option(32916, help="Tournament ID"),
    limit: int = typer.Option(5, help="Number of questions to check"),
) -> None:
    """Inspect aggregation data in resolved question API responses."""

    async def _check() -> None:
        from aib.clients.metaculus import AsyncMetaculusClient

        async with AsyncMetaculusClient() as mc:
            results = await mc.fetch_posts_list(
                {
                    "order_by": "-resolve_time",
                    "status": "resolved",
                    "tournaments": tournament_id,
                    "limit": limit,
                }
            )

            for r in results:
                pid = r.get("id")
                title = r.get("title", "")[:60]
                q = r.get("question", {})
                resolution = q.get("resolution")
                aggs = q.get("aggregations", {})
                qtype = q.get("type")

                print(f"\n=== {pid}: {title} ===")
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

    asyncio.run(_check())


@app.command("cp-single")
def cp_single(
    post_id: int = typer.Argument(help="Post ID to check"),
) -> None:
    """Inspect a single question's aggregation data via direct fetch."""

    async def _check() -> None:
        from aib.clients.metaculus import AsyncMetaculusClient

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

    asyncio.run(_check())


# ---------------------------------------------------------------------------
# debug: Metaculus API parsing and MCP error propagation
# ---------------------------------------------------------------------------


@app.command("debug")
def debug_metaculus(
    tournament: str = typer.Option("spring-aib-2026", help="Tournament slug"),
    limit: int = typer.Option(5, help="Number of posts to fetch"),
    raw_only: bool = typer.Option(False, "--raw-only", help="Only test raw parsing"),
) -> None:
    """Debug Metaculus API parsing and client."""
    from aib.clients.metaculus import AsyncMetaculusClient, get_client
    from metaculus.models import MetaculusQuestion

    async def run() -> None:
        if not raw_only:
            print("=== Raw API Parse Test ===")
            async with AsyncMetaculusClient() as mc:
                results = await mc.fetch_posts_list(
                    {"tournaments": tournament, "status": "open", "limit": limit}
                )
                print(f"Fetched {len(results)} posts")
                for i, result in enumerate(results):
                    print(f"\n--- Post {i + 1} ---")
                    print(f"ID: {result.get('id')}")
                    print(f"Title: {result.get('title', '')[:60]}...")
                    try:
                        q = MetaculusQuestion.from_api_json(result)
                        print(f"Parsed OK: {type(q).__name__}")
                    except (ValueError, TypeError, KeyError) as e:
                        print(f"Parse ERROR: {type(e).__name__}: {e}")
                        traceback.print_exc()

        print("\n=== Client Test ===", flush=True)
        client = get_client()
        print(f"Token length: {len(client.token) if client.token else 0}", flush=True)

        try:
            questions = await client.get_all_open_questions_from_tournament(tournament)
            print(f"Parsed {len(questions)} questions")
            for q in questions[:3]:
                print(
                    f"  - [{q.id_of_post}] {type(q).__name__}: {q.question_text[:40]}..."
                )
        except (OSError, ValueError) as e:
            print(f"Error: {type(e).__name__}: {e}")
            traceback.print_exc()

    asyncio.run(run())


@app.command("mcp-error")
def mcp_error_test() -> None:
    """Test if is_error property works on our CallToolResult subclass."""
    from aib.tools.mcp_server import _CallToolResultWithAlias
    from mcp.types import TextContent

    print("=== MCP Error Propagation Test ===\n")

    result = _CallToolResultWithAlias(
        content=[TextContent(type="text", text="Test error message")],
        isError=True,
    )

    print("Created _CallToolResultWithAlias with isError=True")
    print(f"  type(result): {type(result).__name__}")
    print(f"  result.isError: {result.isError}")
    print(f"  hasattr(result, 'is_error'): {hasattr(result, 'is_error')}")

    try:
        is_error_val = result.is_error
        print(f"  result.is_error: {is_error_val}")
    except AttributeError as e:
        print(f"  result.is_error FAILED: {type(e).__name__}: {e}")
        is_error_val = None

    result2 = _CallToolResultWithAlias(
        content=[TextContent(type="text", text="Success")],
        isError=False,
    )
    print("\nCreated _CallToolResultWithAlias with isError=False")
    print(f"  result2.isError: {result2.isError}")
    print(f"  result2.is_error: {result2.is_error}")

    print("\n=== Summary ===")
    if hasattr(result, "is_error") and is_error_val is True:
        print("is_error property works correctly")
    else:
        print("is_error property NOT working - SDK bug workaround failed")


# ---------------------------------------------------------------------------
# websearch: Debug retrodict web search
# ---------------------------------------------------------------------------


@app.command("websearch")
def websearch_cmd(
    query: str = typer.Argument(..., help="Search query"),
    cutoff: str = typer.Option("2026-01-15", help="Cutoff date YYYY-MM-DD"),
    num_results: int = typer.Option(5, help="Number of results"),
) -> None:
    """Test the retrodict web search (Exa-based)."""
    import json
    import logging

    logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")

    async def _search() -> None:
        from aib.tools.retrodict_search import web_search

        print(f"\nQuery: {query}")
        print(f"Cutoff: {cutoff}")
        print(f"Requested results: {num_results}\n")

        result = await web_search.handler(
            {"query": query, "num_results": num_results, "cutoff_date": cutoff}
        )

        is_error = result.get("isError", False)
        content_text = result.get("content", [{}])[0].get("text", "{}")

        if is_error:
            print(f"Error: {content_text}")
            return

        try:
            data = json.loads(content_text)
        except json.JSONDecodeError:
            print(f"Failed to parse response: {content_text}")
            return

        results = data.get("results", [])
        print(f"Got {len(results)} results from Exa")

        for r in results:
            print(f"  {(r.get('title') or '')[:60]}")
            print(f"    {(r.get('url') or '')[:70]}")

    asyncio.run(_search())


# ---------------------------------------------------------------------------
# earnings: Check yfinance earnings dates
# ---------------------------------------------------------------------------


@app.command("earnings")
def earnings_cmd(
    ticker: str = typer.Argument("GOOG"),
    limit: int = typer.Option(12),
) -> None:
    """Check what yfinance earnings_dates provides for a ticker."""
    from datetime import date, datetime, timedelta

    import pandas as pd
    import yfinance as yf

    t = yf.Ticker(ticker)

    print(f"=== earnings_dates (limit={limit}) ===")
    df = t.get_earnings_dates(limit=limit)
    if df is not None and not df.empty:
        print(df.to_string())
        print(f"\nColumns: {df.columns.tolist()}")
        print(f"Index: {df.index.name} ({df.index.dtype})")
    else:
        print("No data")

    print("\n=== earnings_history ===")
    eh = t.get_earnings_history()
    if eh is not None and isinstance(eh, pd.DataFrame) and not eh.empty:
        print(eh.to_string())
        print(f"\nColumns: {eh.columns.tolist()}")
    else:
        print("No data")

    print("\n=== release map ===")
    if (
        df is not None
        and not df.empty
        and eh is not None
        and isinstance(eh, pd.DataFrame)
        and not eh.empty
    ):
        for idx in eh.index:
            quarter_end: date
            if hasattr(idx, "date"):
                quarter_end = idx.date()
            elif isinstance(idx, str):
                quarter_end = datetime.strptime(idx, "%Y-%m-%d").date()
            else:
                continue

            matched = False
            for earnings_dt in df.index:
                edt = (
                    earnings_dt.date() if hasattr(earnings_dt, "date") else earnings_dt
                )
                if abs((edt - quarter_end).days) <= 60:
                    lag = (edt - quarter_end).days
                    fallback_ok = quarter_end + timedelta(days=45) <= edt
                    print(
                        f"  Q ending {quarter_end} -> reported {edt} "
                        f"(lag: {lag}d, 45d-fallback would be {'OK' if not fallback_ok else 'TOO EARLY'})"
                    )
                    matched = True
                    break
            if not matched:
                print(f"  Q ending {quarter_end} -> NO MATCH in earnings_dates")
