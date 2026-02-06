#!/usr/bin/env python3
"""Debug script to test web search in retrodict mode."""

import asyncio
import json
import logging

import typer
from rich import print as rprint
from rich.console import Console
from rich.table import Table

# Set up logging before imports
logging.basicConfig(level=logging.INFO, format="%(name)s: %(message)s")

app = typer.Typer()
console = Console()


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    cutoff: str = typer.Option("2026-01-15", help="Cutoff date YYYY-MM-DD"),
    num_results: int = typer.Option(5, help="Number of results"),
):
    """Test the retrodict web search (now using Exa with date filtering)."""
    asyncio.run(_test_search(query, cutoff, num_results))


async def _test_search(query: str, cutoff: str, num_results: int):
    from aib.tools.retrodict_search import web_search

    rprint(f"\n[bold]Testing retrodict web search (Exa-based)[/bold]")
    rprint(f"Query: {query}")
    rprint(f"Cutoff: {cutoff}")
    rprint(f"Requested results: {num_results}")
    rprint()

    # Call the underlying handler (web_search is an SdkMcpTool, not a function)
    rprint("[bold blue]Searching via Exa with publishedBefore filter...[/bold blue]")
    result = await web_search.handler({
        "query": query,
        "num_results": num_results,
        "cutoff_date": cutoff,
    })

    # Parse the MCP response
    is_error = result.get("isError", False)
    content_text = result.get("content", [{}])[0].get("text", "{}")

    if is_error:
        rprint(f"[red]Error: {content_text}[/red]")
        return

    try:
        data = json.loads(content_text)
    except json.JSONDecodeError:
        rprint(f"[red]Failed to parse response: {content_text}[/red]")
        return

    results = data.get("results", [])
    rprint(f"Got {len(results)} results from Exa")

    if results:
        table = Table(title="Search Results")
        table.add_column("Title", max_width=50)
        table.add_column("URL", max_width=50)
        table.add_column("Snippet", max_width=40)

        for r in results:
            table.add_row(
                (r.get("title") or "")[:50],
                (r.get("url") or "")[:50],
                (r.get("snippet") or "")[:40],
            )
        console.print(table)
    else:
        rprint("[yellow]No results found[/yellow]")


@app.command()
def wayback(
    url: str = typer.Argument(..., help="URL to check"),
    cutoff: str = typer.Option("2026-01-15", help="Cutoff date YYYY-MM-DD"),
):
    """Check Wayback availability for a single URL."""
    asyncio.run(_test_wayback(url, cutoff))


async def _test_wayback(url: str, cutoff: str):
    from aib.tools.wayback import check_wayback_availability

    cutoff_ts = cutoff.replace("-", "")
    rprint(f"Checking Wayback for: {url}")
    rprint(f"Cutoff timestamp: {cutoff_ts}")

    result = await check_wayback_availability(url, cutoff_ts)
    if result:
        rprint(f"[green]Found snapshot:[/green]")
        for k, v in result.items():
            rprint(f"  {k}: {v}")
    else:
        rprint("[red]No valid snapshot found[/red]")


if __name__ == "__main__":
    app()
