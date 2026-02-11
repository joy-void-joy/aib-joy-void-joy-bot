"""Check what yfinance earnings_dates provides for a ticker."""

from datetime import date, datetime, timedelta

import typer

app = typer.Typer()


@app.command()
def main(ticker: str = typer.Argument("GOOG"), limit: int = 12) -> None:
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

    # Build and display the release map
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
                        f"  Q ending {quarter_end} → reported {edt} "
                        f"(lag: {lag}d, 45d-fallback would be {'OK' if not fallback_ok else 'TOO EARLY'})"
                    )
                    matched = True
                    break
            if not matched:
                print(f"  Q ending {quarter_end} → NO MATCH in earnings_dates")


if __name__ == "__main__":
    app()
