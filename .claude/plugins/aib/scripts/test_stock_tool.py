#!/usr/bin/env python3
"""Test the Yahoo Finance stock tools."""

import yfinance as yf


def main() -> None:
    """Test yfinance directly."""
    # Test current price
    ticker = yf.Ticker("BA")
    info = ticker.info

    print("Symbol: BA")
    print(f"Name: {info.get('shortName')}")
    print(f"Current price: {info.get('regularMarketPrice')}")
    print(f"Previous close: {info.get('previousClose')}")
    print(f"52-week high: {info.get('fiftyTwoWeekHigh')}")
    print(f"52-week low: {info.get('fiftyTwoWeekLow')}")

    # Test history
    hist = ticker.history(period="5d")
    print("\nHistory (last 5 days):")
    print(hist[["Open", "Close", "Volume"]].tail())


if __name__ == "__main__":
    main()
