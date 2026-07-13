"""Agent tool serving for interactive Claude Code sessions."""

from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)

RESEARCH_SERVER_NAME = "research"


@app.callback()
def main() -> None:
    """Agent tool serving for interactive Claude Code sessions."""


@app.command("serve-tools")
def serve_tools_cmd(
    list_only: Annotated[
        bool,
        typer.Option("--list", help="List tool names instead of serving"),
    ] = False,
    server: Annotated[
        str | None,
        typer.Option(
            "--server", help="Serve a single tool group (e.g. search, markets)"
        ),
    ] = None,
) -> None:
    """Serve the session-free research tools over MCP stdio.

    `lup-devtools claude` writes an MCP config whose research server runs this
    command, so interactive Claude Code sessions get the same research tools
    the forecasting agents use (search, financial, government, markets,
    trends, and reddit when configured).
    """
    from aib.agent.resolver import build_research_tool_groups
    from aib.tools.mcp_server import create_mcp_server, serve_stdio

    groups = build_research_tool_groups()
    if server is None:
        selected = groups
    elif server in groups:
        selected = {server: groups[server]}
    else:
        typer.echo(
            f"Error: unknown tool group '{server}'."
            f" Available: {', '.join(sorted(groups))}",
            err=True,
        )
        raise typer.Exit(1)

    tools = [tool for group in selected.values() for tool in group]

    if list_only:
        for tool in tools:
            typer.echo(tool.name)
        return

    serve_stdio(create_mcp_server(server or RESEARCH_SERVER_NAME, tools=tools))
