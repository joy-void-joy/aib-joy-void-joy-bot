#!/usr/bin/env python3
"""Find retrodiction candidates from scores.csv."""

import csv
from collections import defaultdict
from pathlib import Path
import typer

app = typer.Typer()


@app.command()
def main(
    scores_file: Path = Path("notes/scores.csv"),
):
    """Find candidates for re-retrodiction with v0.6.0."""

    # Read CSV
    with open(scores_file) as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    # Build index: post_id -> list of rows
    post_data = defaultdict(list)
    for row in rows:
        post_data[row["post_id"]].append(row)

    # Find candidates
    candidates = []

    for post_id, versions in post_data.items():
        # Check if there's any retrodict row with resolution
        retrodict_resolved = [
            r
            for r in versions
            if r["source"] == "retrodict"
            and r["resolution"]
            and r["resolved"] == "True"
        ]

        if not retrodict_resolved:
            continue

        # Check if v0.6.0 already has a resolved retrodict
        v060_resolved = [
            r
            for r in versions
            if r["source"] == "retrodict"
            and r["agent_version"] == "0.6.0"
            and r["resolution"]
            and r["resolved"] == "True"
        ]

        if v060_resolved:
            continue  # Already retrodicted with v0.6.0 and resolved

        # Get v0.3.1 retrodict data
        v031 = [r for r in retrodict_resolved if r["agent_version"] == "0.3.1"]

        if not v031:
            continue

        # Use the first v0.3.1 row (they should be similar)
        row = v031[0]

        candidates.append(
            {
                "post_id": post_id,
                "question_type": row["question_type"],
                "title": row["question_title"],
                "resolution": row["resolution"],
                "probability": row["probability"],
                "median": row["median"],
                "ci_lower": row["ci_lower"],
                "ci_upper": row["ci_upper"],
                "brier": row["brier"],
                "abs_error": row["abs_error"],
                "within_ci": row["within_ci"],
            }
        )

    # Classify domains
    def classify_domain(title: str) -> str:
        title_lower = title.lower()
        if "community prediction" in title_lower or "metaculus" in title_lower:
            return "meta"
        if any(
            x in title_lower
            for x in [
                "stock",
                "market close",
                "earnings",
                "revenue",
                "futures",
                "bitcoin",
                "gold",
                "nvidia",
                "apple",
            ]
        ):
            return "markets"
        if any(
            x in title_lower
            for x in [
                "sofr",
                "treasury",
                "yield",
                "interest",
                "fed funds",
                "high yield",
            ]
        ):
            return "economics"
        if any(x in title_lower for x in ["vix", "volatility"]):
            return "volatility"
        if any(
            x in title_lower
            for x in ["un general assembly", "venezuela", "government", "congress"]
        ):
            return "geopolitics"
        return "other"

    for c in candidates:
        c["domain"] = classify_domain(c["title"])

    # Print candidates table
    print(f"Found {len(candidates)} candidates for re-retrodiction:\n")
    print(
        f"{'post_id':<8} {'type':<8} {'domain':<12} {'res':<8} {'pred':<12} {'score':<12} {'CI?':<5} {'title':<50}"
    )
    print("-" * 120)

    for c in sorted(candidates, key=lambda x: (c["domain"], x["post_id"])):
        qtype = c["question_type"]
        res = c["resolution"][:6] if c["resolution"] else "N/A"
        domain = c["domain"]

        if qtype == "binary":
            pred = c["probability"] if c["probability"] else "N/A"
            score = f"Br={c['brier'][:5]}" if c["brier"] else "N/A"
            ci = "N/A"
        else:
            pred = c["median"] if c["median"] else "N/A"
            abs_err = c["abs_error"]
            if abs_err and len(abs_err) > 10:
                # Shorten long numbers
                try:
                    abs_err = f"{float(abs_err):.1e}"
                except (ValueError, TypeError):
                    pass
            score = f"AE={abs_err}" if abs_err else "N/A"
            ci = c["within_ci"] if c["within_ci"] else "N/A"

        title = c["title"][:50] if len(c["title"]) > 50 else c["title"]

        print(
            f"{c['post_id']:<8} {qtype:<8} {domain:<12} {res:<8} {pred:<12} {score:<12} {ci:<5} {title:<50}"
        )

    print(f"\n\nTotal candidates: {len(candidates)}")

    # Count by type
    by_type = defaultdict(int)
    by_domain = defaultdict(int)
    for c in candidates:
        by_type[c["question_type"]] += 1
        by_domain[c["domain"]] += 1

    print("\nBy type:")
    for qtype, count in sorted(by_type.items()):
        print(f"  {qtype}: {count}")

    print("\nBy domain:")
    for domain, count in sorted(by_domain.items(), key=lambda x: -x[1]):
        print(f"  {domain}: {count}")


if __name__ == "__main__":
    app()
