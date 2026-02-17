"""Parse minibench.html to extract question IDs and resolution values.

Usage:
    uv run python .claude/plugins/aib/scripts/parse_minibench.py parse <html_file>
    uv run python .claude/plugins/aib/scripts/parse_minibench.py apply <html_file> [--dry-run]
"""

import csv
import json
import re
from pathlib import Path

import typer
from bs4 import BeautifulSoup

app = typer.Typer()


def extract_resolutions(html_path: str) -> list[dict[str, str | int | None]]:
    html = Path(html_path).read_text()
    soup = BeautifulSoup(html, "html.parser")

    results: list[dict[str, str | int | None]] = []
    seen: set[int] = set()

    for link in soup.find_all("a", href=re.compile(r"/questions/\d+/")):
        h4 = link.find("h4")
        if not h4:
            continue
        match = re.search(r"/questions/(\d+)/", str(link["href"]))
        if not match:
            continue
        post_id = int(match.group(1))
        if post_id in seen:
            continue
        seen.add(post_id)

        title = h4.get_text(strip=True)
        text = link.get_text(separator="|", strip=True)

        resolution: str | None = None
        res_type: str | None = None

        # Annulled: all MC options show Annulled, or single Annulled marker
        parts = text.split("|")
        if "Annulled" in parts and "Yes" not in parts:
            resolution = "annulled"
            res_type = "annulled"
        # Binary: "Resolved" span with Yes/No
        elif resolved_span := next(
            (
                s
                for s in link.find_all("span")
                if s.string and re.search(r"Resolved", s.string, re.I)
            ),
            None,
        ):
            parent_div = resolved_span.find_parent("div")
            if parent_div:
                for span in parent_div.find_all("span"):
                    t = span.get_text(strip=True)
                    if t.lower() in ("yes", "no"):
                        resolution = t.lower()
                        res_type = "binary"
                        break
        # Numeric: RESOLVED|value
        elif "RESOLVED" in parts:
            for i, p in enumerate(parts):
                if p == "RESOLVED" and i + 1 < len(parts):
                    resolution = parts[i + 1]
                    res_type = "numeric"
                    break
        else:
            # MC: option|Yes/No pairs
            mc_options: dict[str, str] = {}
            for i in range(len(parts) - 1):
                if parts[i + 1] in ("Yes", "No"):
                    mc_options[parts[i]] = parts[i + 1]
            if mc_options:
                winners = [k for k, v in mc_options.items() if v == "Yes"]
                if winners:
                    resolution = winners[0]
                    res_type = "mc"

        results.append(
            {
                "post_id": post_id,
                "title": title[:80],
                "resolution": resolution,
                "type": res_type,
            }
        )

    # Normalize numeric values (expand k suffix)
    for r in results:
        if r["type"] == "numeric" and isinstance(r["resolution"], str):
            val = str(r["resolution"])
            if val.endswith("k"):
                r["resolution"] = str(float(val[:-1]) * 1000)

    return results


@app.command()
def parse(html_file: str = typer.Argument(default="minibench.html")) -> None:
    """Parse minibench HTML and show extracted resolutions."""
    results = extract_resolutions(html_file)

    resolved = [r for r in results if r["type"] not in (None, "annulled")]
    annulled = [r for r in results if r["type"] == "annulled"]
    open_qs = [r for r in results if r["type"] is None]

    print(
        f"Total: {len(results)} | Resolved: {len(resolved)} | Annulled: {len(annulled)} | Open: {len(open_qs)}"
    )
    print()

    for label, group in [
        ("RESOLVED", resolved),
        ("ANNULLED", annulled),
        ("OPEN", open_qs),
    ]:
        if not group:
            continue
        print(f"=== {label} ===")
        for r in group:
            res_str = str(r["resolution"] or "-")
            print(
                f"  {r['post_id']:>6}  {r['type'] or 'open':<10}  {res_str:<25}  {r['title']}"
            )
        print()

    out_path = Path(html_file).with_suffix(".json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"JSON written to {out_path}")


@app.command()
def apply(
    html_file: str = typer.Argument(default="minibench.html"), dry_run: bool = False
) -> None:
    """Apply parsed resolutions to forecast files via resolution_update.py set."""
    results = extract_resolutions(html_file)
    scores_path = Path("notes/scores.csv")

    if not scores_path.exists():
        print("ERROR: notes/scores.csv not found")
        raise typer.Exit(1)

    # Load our forecast post IDs
    our_ids: set[int] = set()
    with open(scores_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            our_ids.add(int(row["post_id"]))

    resolved = [
        r
        for r in results
        if r["type"] not in (None, "annulled") and r["post_id"] in our_ids
    ]
    annulled = [
        r for r in results if r["type"] == "annulled" and r["post_id"] in our_ids
    ]
    missing = [
        r
        for r in results
        if r["type"] not in (None, "annulled") and r["post_id"] not in our_ids
    ]

    print(f"Resolved questions we forecast: {len(resolved)}")
    print(f"Annulled questions we forecast: {len(annulled)}")
    print(f"Resolved questions we didn't forecast: {len(missing)}")
    print()

    if missing:
        print("=== NOT IN OUR DATA ===")
        for r in missing:
            print(f"  {r['post_id']:>6}  {r['title']}")
        print()

    for r in resolved:
        post_id = r["post_id"]
        resolution = r["resolution"]
        action = "DRY RUN" if dry_run else "APPLYING"
        print(f"  {action}: {post_id} -> {resolution}")

        if not dry_run:
            import subprocess

            result = subprocess.run(
                [
                    "uv",
                    "run",
                    "python",
                    ".claude/plugins/aib/scripts/resolution_update.py",
                    "set",
                    str(post_id),
                    str(resolution),
                ],
                capture_output=True,
                text=True,
            )
            if result.returncode != 0:
                print(f"    ERROR: {result.stderr.strip()}")
            else:
                out = result.stdout.strip()
                if out:
                    print(f"    {out}")


if __name__ == "__main__":
    app()
