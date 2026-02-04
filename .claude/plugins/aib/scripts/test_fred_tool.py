#!/usr/bin/env python3
"""Test the FRED API tools."""

import os


def main() -> None:
    """Test fredapi directly."""
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("FRED_API_KEY not set. Get a free key at:")
        print("https://fred.stlouisfed.org/docs/api/api_key.html")
        return

    from fredapi import Fred

    fred = Fred(api_key=api_key)

    # Test series lookup
    print("Testing DGS10 (10-Year Treasury)...")
    data = fred.get_series("DGS10")
    print(f"Latest 5 values:\n{data.tail()}")

    # Test series info
    info = fred.get_series_info("DGS10")
    print("\nSeries info:")
    print(f"  Title: {info.get('title')}")
    print(f"  Frequency: {info.get('frequency')}")
    print(f"  Units: {info.get('units')}")

    # Test search
    print("\nSearching for 'unemployment rate'...")
    results = fred.search("unemployment rate")
    print(f"Found {len(results)} series. Top 3:")
    for idx, row in results.head(3).iterrows():
        print(f"  {idx}: {row.get('title')}")


if __name__ == "__main__":
    main()
