# Reasoning Log: Will U.S. spot Bitcoin ETFs take in at least $1 billion of net inflows during April 2026?

*Generated: 2026-04-12T15:13:59.410139+00:00*


## 💭 Thinking

Let me analyze this forecasting question about U.S. spot Bitcoin ETFs taking in at least $1 billion of net inflows during April 2026.

Key details:
- Resolution: Sum of Farside "Total" values from 2026-04-01 through 2026-04-30 ≥ $1,000.0M
- Resolution source: https://farside.co.uk/bitcoin-etf-flow-all-data/
- Scheduled close: 2026-04-12T16:30:00Z (today!)
- Published: 2026-04-12T15:00:00Z (today)


- Resolves: 2026-05-01T00:00:00Z

I can see April started with a -$173.7M outflow on the 1st, then recovered with +$9.0M on the 2nd. I need to check the cumulative flows so far this month and assess whether the remaining days can reach the $1B threshold. I'll look at current Bitcoin ETF flow data for April, historical monthly patterns, and the broader market context around tariffs and price movements.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43135
  ]
}
```

### 📋 Result

```
{"post_id": 43135, "title": "Will U.S. spot Bitcoin ETFs take in at least $1 billion of net inflows during April 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43135",
"background_info": "This question measures short-horizon institutional-demand. April 2026 started badly, with -$173.7M on Apr. 1, then +$9.0M on Apr. The question also directly answers whether the
March rebound in ETF demand is continuing or fading.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"c3ee713b10c01c80\",\"sheet_id\":536.0}}`", "resolution_criteria": "This
question resolves as Yes if the sum of the Farside \u201cTotal\u201d values dated 2026-04-01 through 2026-04-30 is at least $1,000.0M. Otherwise it resolves as No. Resolution source:
https://farside.co.uk/bitcoin-etf-flow-all-data/", "fine_print": "", "num_forecasters": 8, "community_prediction": null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://farside.co.uk/bitcoin-etf-flow-all-data/",
  "prompt": "What are all the daily Bitcoin ETF total net flow values for April 2026? List each date and total value."
}
```

### 📋 Result

```
{"url": "https://farside.co.uk/bitcoin-etf-flow-all-data/", "content": "Based on the data provided, here are all the daily Bitcoin ETF total net flow values for April 2026:\n\n| Date | Total Net Flow
(millions USD) |\n|---|---|\n| 01 Apr 2026 | -173.7 |\n| 02 Apr 2026 | 9.0 |\n| 06 Apr 2026 | 471.4 |\n| 07 Apr 2026 | -159.1 |\n| 08 Apr 2026 | -93.9 |\n| 09 Apr 2026 | 358.1 |\n| 10 Apr 2026 | 240.4
|\n\nNote: April 3-5, 2026 are not shown in the data (likely weekends/holidays with no trading).\n\nRelevant links:\n- [Bitcoin ETF Flow All Data - Farside Investors](https://farside.co.uk/bitcoin-
etf-flow-all-data/)", "title": "Farside Investors"}
```

```json
{
  "query": "US spot Bitcoin ETF net inflows April 2026"
}
```

### 📋 Result

```
{"query": "US spot Bitcoin ETF net inflows April 2026", "results": [{"title": "Bitcoin ETF Fund Flows | Spot BTC Net Inflow & Holdings | CoinGlass", "url": "https://www.coinglass.com/etf/bitcoin",
"snippet": "Bitcoin ETF data is better suited for identifying medium- to long-term capital trends, rather than serving as short-term trading signals.\nA common analytical approach includes:\nUsing ETF
fund flows to observe institutional allocation preferences toward Bitcoin\nCombining ETF data with Bitcoin spot price movements to assess whether capital inflows are driving trend formation\nComparing
ETF data with crypto derivatives market indicators, such as\n[BTC Funding Rate](/FundingRate/BTC) and\n[BTC Open Int", "api_data": null, "hint": null}, {"title": "Bitcoin US Spot ETF Net Flows Chart",
"url": "https://studio.glassnode.com/charts/institutions.UsSpotEtfFlowsNet?a=BTC", "snippet": "This metric shows the total net flow of funds of the leading Bitcoin and Ethereum ETFs traded in the
U.S., reflecting the day-to-day changes in the ETF's holdings. It is calculated as the difference between today's balance data point and the previously available balance data point in native units.
Each day's native net flow is then converted into USD, leveraging the closing USD exchange rate at 16:00 New York time. It updates hourly from 00:00 to 18:00 UTC to ensure timely information on the
dai", "api_data": null, "hint": null}, {"title": "US Bitcoin ETF Adds 4,614 BTC as Ethereum ETF Sees 23,039 ETH Inflow", "url": "https://bitcoinethereumnews.com/bitcoin/us-bitcoin-etf-adds-4614-btc-
as-ethereum-etf-sees-23039-eth-inflow/", "snippet": "U.S. spot Bitcoin ETFs recorded a net inflow of 4,614 BTC on April 10, 2026, while Ethereum ETFs absorbed 23,039 ETH in the same session, marking a
day of synchronized institutional demand across both major crypto assets.\nThe figures come from blockchain analytics tracker Lookonchain, which posted its daily ETF flow update showing the Bitcoin
inflow was worth approximately $334.63 million at the time of reporting.\nU.S. Bitcoin ETF 1D Net Flow\n+4,614 BTC\nThe positive flow adds to a strong weekly ", "api_data": null, "hint": null},
{"title": "Bitcoin ETF inflows hit highest level since February", "url": "https://www.coindesk.com/markets/2026/04/07/bitcoin-etf-inflows-hit-highest-level-since-february", "snippet": "U.S. spot
bitcoin ETFs saw about $471 million in net inflows on April 6, their strongest daily intake in more than a month, even as bitcoin hovered around $68,780.\nRobust ETF demand is helping to offset weak
spot buying and selling by large holders, effectively anchoring bitcoin\u2019s price below the $70,000 level.\nNew research suggests bitcoin has shifted from lagging to leading global monetary policy,
with ETF-driven institutional flows now front-running expected central bank moves rather than rea", "api_data": null, "hint": null}, {"title": "Bitcoin ETF Inflows Hit $53B: Why Institutions ...",
"url": "https://intellectia.ai/blog/bitcoin-etf-inflows-53b-institutional-investors-2026", "snippet": null, "api_data": null, "hint": null}, {"title": "US Spot Bitcoin and Ethereum ETFs Added Solid
Net Inflows - Tekedia", "url": "https://www.tekedia.com/us-spot-bitcoin-and-ethereum-etfs-added-solid-net-inflows/", "snippet": "![US Spot Bitcoin and Ethereum ETFs Added Solid Net Inflows US Spot
Bitcoin and Ethereum ETFs Added Solid Net Inflows](https://www.tekedia.com/wp-content/uploads/2025/10/ETF.jpg)\nU.S. spot Bitcoin (BTC) and Ethereum (ETH) ETFs have been seeing solid net inflows
recently. BTC ETFs recorded ~$358M net inflows led heavily by BlackRock\u2019s IBIT at +$269M, with Fidelity\u2019s FBTC adding +$53M and smaller contributions from others.\nETH ETFs added ~$85M net;
BlackRock\u2019s ETHA was the standout at +$91M, offse", "api_data": null, "hint": null}, {"title": "Bitcoin ETF Flows [Table & Chart]", "url": "https://bitbo.io/treasuries/etf-flows/", "snippet":
"The chart above shows daily total net flow for spot bitcoin ETFs in the USA.\nBitcoin ETF Flow (US$m)\n| Date | IBIT | FBTC | GBTC | BTC | BITB | ARKB | HODL | BRRR | EZBC | BTCO | BTCW | MSBT | DEFI
| Totals |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| Apr 10, 2026 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |\n| Apr 09, 2026 | 264.8
| 52.4 | -11.5 | 0.0 | 11.6 | 4.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 14.6 | 0.0 | 336.7 |\n| Apr 08, 2026 | 4", "api_data": null, "hint": null}, {"title": "Largest bitcoin ETF inflow in three months
signals institutional bid is back", "url": "https://www.coindesk.com/markets/2026/01/06/largest-bitcoin-etf-inflow-in-three-months-signals-institutional-bid-is-back", "snippet": "U.S. spot bitcoin
ETFs recorded $697.2 million in inflows on Monday, the largest since Oct. 7.\nU.S. ETFs have recorded approximately $1.2 billion in net inflows across the first two trading days of 2026.\nExtended ETF
outflow periods have historically aligned with local market bottoms, with recent flows flipping back into positive territory alongside a recovering Coinbase premium, suggesting capitulation conditions
are fading.\nBitcoin exchange-traded funds (ETFs) in the U.S. registered their larg", "api_data": null, "hint": null}, {"title": "Bitcoin ETFs Draw Record $471 Million Amid US-Iran Tensions
Reinforcing Digital Gold Status - Reelfinancial.com", "url": "https://www.reelfinancial.com/archives/94242", "snippet": "On April 6, 2026, U.S. spot
[Bitcoin](https://reelfinancial.com/archives/tag/bitcoin) exchange-traded funds (ETFs) experienced a remarkable surge, attracting $471.4 million in net inflows. This marked the strongest single-day
inflow in over six weeks and signaled a renewed interest from institutional investors. The influx occurred as global tensions escalated around the U.S.-Iran standoff concerning the Strait of Hormuz,
with a critical deadline set for April 7 at 8:00 P.M. ET. This geopolitical", "api_data": null, "hint": null}, {"title": "Bitcoin ETFs Gain as Institutional Demand Continues to Support Flows |
Investing.com", "url": "https://www.investing.com/analysis/bitcoin-etfs-gain-as-institutional-demand-continues-to-support-flows-200677973", "snippet": "Trump says U.S. Navy to enact Strait of Hormuz
blockade after Iran talks collapse\niShares Bitcoin Trust ETF (NASDAQ:[IBIT](https://www.investing.com/etfs/ibit-nasdaq)) is trading at $39.51 on Monday, April 6, 2026 \u2014 up 4.06%, or $1.54, from
Friday\u2019s close of $37.97. The intraday range spans $39.21 to $39.90, with average daily volume of 58.66 million shares and a market capitalization of $149.72 billion. The 52-week range from
$35.30 at the absolute floor to $71.82 at the peak captures the full ", "api_data": null, "hint": null}]}
```

## 💬 Response

Good, I have the Farside data for April 2026 so far. Let me calculate the cumulative total and research recent Bitcoin market conditions and historical monthly flow patterns.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# April 2026 daily flows from Farside data\ndaily_flows = {\n    '2026-04-01': -173.7,\n    '2026-04-02': 9.0,\n    '2026-04-06': 471.4,\n    '2026-04-07': -159.1,\n    '2026-04-08': -93.9,\n    '2026-04-09': 358.1,\n    '2026-04-10': 240.4,\n}\n\ncumulative = sum(daily_flows.values())\nprint(f\"Cumulative April flows through Apr 10: ${cumulative:.1f}M\")\nprint(f\"Remaining to reach $1B: ${1000 - cumulative:.1f}M\")\n\n# Trading days remaining in April (Apr 13-30, excluding weekends)\n# April 2026: 13(Mon), 14(Tue), 15(Wed), 16(Thu), 17(Fri), \n#              20(Mon), 21(Tue), 22(Wed), 23(Thu), 24(Fri),\n#              27(Mon), 28(Tue), 29(Wed), 30(Thu)\nremaining_trading_days = 14\nprint(f\"Trading days remaining (Apr 13-30): {remaining_trading_days}\")\nprint(f\"Average daily flow needed: ${(1000 - cumulative)/remaining_trading_days:.1f}M per day\")\nprint(f\"\\nAverage daily flow so far in April: ${cumulative/7:.1f}M per day\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Cumulative April flows through Apr 10: $652.2M\nRemaining to reach $1B: $347.8M\nTrading days remaining (Apr 13-30): 14\nAverage daily flow needed: $24.8M per
day\n\nAverage daily flow so far in April: $93.2M per day\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__financial__stock_price


```json
{
  "query": "Bitcoin ETF monthly net inflows 2025 2026 total by month"
}
```

### 📋 Result

```
{"query": "Bitcoin ETF monthly net inflows 2025 2026 total by month", "results": [{"title": "Bitcoin ETF Fund Flows | Spot BTC Net Inflow & Holdings | CoinGlass", "url":
"https://www.coinglass.com/etf/bitcoin", "snippet": "Bitcoin ETF data is better suited for identifying medium- to long-term capital trends, rather than serving as short-term trading signals.\nA common
analytical approach includes:\nUsing ETF fund flows to observe institutional allocation preferences toward Bitcoin\nCombining ETF data with Bitcoin spot price movements to assess whether capital
inflows are driving trend formation\nComparing ETF data with crypto derivatives market indicators, such as\n[BTC Funding Rate](/FundingRate/BTC) and\n[BTC Open Int", "api_data": null, "hint": null},
{"title": "Bitcoin ETF Flows [Table & Chart]", "url": "https://bitbo.io/treasuries/etf-flows/", "snippet": "The chart above shows daily total net flow for spot bitcoin ETFs in the USA.\nBitcoin ETF
Flow (US$m)\n| Date | IBIT | FBTC | GBTC | BTC | BITB | ARKB | HODL | BRRR | EZBC | BTCO | BTCW | MSBT | DEFI | Totals |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n| Apr 10, 2026
| 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |\n| Apr 09, 2026 | 264.8 | 52.4 | -11.5 | 0.0 | 11.6 | 4.7 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 14.6 | 0.0 | 336.7 |\n|
Apr 08, 2026 | 4", "api_data": null, "hint": null}, {"title": "Bitcoin and Ether ETFs pull in $646M on first trading day of 2026 \u2014 TradingView News", "url":
"https://www.tradingview.com/news/cointelegraph:5fdc329bd094b:0-bitcoin-and-ether-etfs-pull-in-646m-on-first-trading-day-of-2026/", "snippet": "Bitcoin and Ether ETFs pull in $646M on first trading
day of 2026\nUS-based spot Bitcoin and Ether ETFs began 2026 on a strong note, posting a combined net inflow of around $646 million on the first trading day, despite mixed sentiment across the broader
crypto market.\nOn Friday, spot Bitcoin (BTC) ETFs saw net inflows of $471.3 million, while spot Ether (ETH) ETFs added $174.5 million, bringing total inflows across the two ETF types to $645.8
million, according to Farside data.\nUS spot Bitcoin E", "api_data": null, "hint": null}, {"title": "Bitcoin's 2026 Flow: ETF Inflows vs. Cycle Reality", "url":
"https://www.ainvest.com/news/bitcoin-2026-flow-etf-inflows-cycle-reality-2604/", "snippet": "Bitcoin's 2026 Flow: ETF Inflows vs. Cycle Reality\n[Evan
Hultman](https://www.ainvest.com/news/author/evan-hultman/)Reviewed by\n[AInvest News Editorial Team](https://www.ainvest.com/news/author/ainvest-news-editorial-
team/)\n[BTC--](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE)\n![Speaker
1](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/en_Amelia_e5b296241755764828756.png)\n![Speaker
2](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/en_chris_2", "api_data": null, "hint": null}, {"title": "From Bitcoin to Bonds: Examining the 2025 ETF Heavyweights", "url":
"https://www.etftrends.com/bitcoin-bonds-examining-2025-etf-heavyweights/", "snippet": "2025 proved to be a historic period for the ETF industry, characterized by massive flows and a significant
broadening of investor appetite across asset classes. The data reveals a market that remains heavily tilted toward core equity exposures while simultaneously embracing alternative stores of value and
fixed-income safety.\n\u201cIt was a tremendous year for the ETF industry in 2025 as many categories hit new milestones,\u201d Todd Rosenbluth, head of research at VettaFi, said. \u201cThe $1 trillion
mark for", "api_data": null, "hint": null}, {"title": "Bitcoin ETF Flows 2025\u20132026: $782M Outflows, BTC at $87K, $220B AUM in Sight", "url": "https://www.tradingnews.com/news/bitcoin-etf-
rotation-btc-usd-near-87k-usd-782m-usd-outflows", "snippet": "![Bitcoin ETF Rotation: BTC-USD Near $87K, $782M Outflows Now, $220B AUM Target for
2026](/Warehouse/content/pics/pic_39946_a_f2d87fbf-660f-406e-b336-122c9d75fcce.jpg?1=1)\nBitcoin ETF Rotation: BTC-USD Near $87K, $782M Outflows Now, $220B AUM Target for 2026\nSpot Bitcoin ETFs hold
about 7% of BTC supply, endured 2025 extremes with $782M weekly redemptions and AUM near $115\u2013$165B, while capital rotates into XRP and Solana ETFs as Wall Street eyes $180K BTC and
$180\u2013$220B in Bitcoin ETF assets by ", "api_data": null, "hint": null}, {"title": "Bitcoin ETF Flow (US$m) \u2013 Farside Investors", "url": "https://farside.co.uk/btc/", "snippet": "Total
|\n|||||||||||||\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\nIBIT |\nFBTC |\nBITB |\nARKB |\nBTCO |\nEZBC |\nBRRR |\nHODL |\nBTCW |\nMSBT |\nGBTC |\nBTC |\n||\n| Fee | 0.25% |\n0.25%
|\n0.20% |\n0.21% |\n0.25% |\n0.19% |\n0.25% |\n0.20% |\n0.25% |\n0.14% |\n1.50% |\n0.15% |\n|\n| 24 Mar 2026 | (4.7) |\n(45.3) |\n(16.6) |\n0.0 |\n0.0 |\n0.0 |\n0.0 |\n(7.9) |\n0.0 |\n- |\n0.0 |\n0.0
|\n(74.5) |\n| 25 Mar 2026 | (70.7) |\n83.3 |\n0.0 |\n(4.8) |\n0.0 |\n0.0 |\n0.0 |\n0.0 |\n0.0 |\n- |\n0.0 |\n0.0 |\n7.8 |\n| 26 Mar 2026 | (41.9) |\n", "api_data": null, "hint": null}, {"title":
"Bitcoin ETF Performance Q1 2026: Inflows, Outflows, and What It Means", "url": "https://blocklr.com/news/bitcoin-etf-performance-q1-2026/", "snippet": "Key Takeaways\n- Spot Bitcoin ETFs attracted
$18.7 billion in net inflows during Q1 2026, pushing total AUM past $128 billion\n- BlackRock's IBIT dominated with $8.4 billion in net inflows, followed by Fidelity's FBTC at $4.1 billion\n-
Grayscale GBTC outflows slowed to $1.2 billion for the quarter, down sharply from peak outflow periods in 2024\n- Fee competition intensified as several providers maintained or cut expense ratios
below 0.25%\n- Institutional allocators now account for an estimated 38%", "api_data": null, "hint": null}, {"title": "Bitcoin ETF List Data", "url": "https://coinmarketcap.com/etf/bitcoin/",
"snippet": "Listed below are ETFs (exchange-traded funds) invested in Bitcoin. These are single asset Bitcoin ETFs holding Bitcoin spot or futures. Also shown are inflows and outflows, total assets
under management (AUM) and net asset value (NAV).\nCrypto Dashboard\nBitcoin ETF Net Flow\n(Invalid Date)\n---.--\nHistorical Values\nLast Week $---.--\nLast Month$---.--\nLast 3 Months$---.--\nYearly
Performance\nStrongest Month (Invalid Date)-\nWeakest Month (Invalid Date)-\nBitcoin ETF Net Flow Chart\nTotal Net Flow\nTotal ", "api_data": null, "hint": null}, {"title": "Spot bitcoin ETFs snap
outflow streak with $562 million in daily inflows | The Block", "url": "https://www.theblock.co/post/388134/spot-bitcoin-etfs-562-million-inflow", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "symbol": "IBIT"
}
```

### 📋 Result

```
{"symbol": "IBIT", "name": "iShares Bitcoin Trust ETF", "current_price": 41.56, "previous_close": 40.91, "change_percent": 1.5888574, "currency": "USD", "market_cap": null, "fifty_two_week_high":
71.82, "fifty_two_week_low": 35.3, "recent_history": [{"date": "2026-03-11", "close": 40.07}, {"date": "2026-03-12", "close": 39.95}, {"date": "2026-03-13", "close": 40.37}, {"date": "2026-03-16",
"close": 41.94}, {"date": "2026-03-17", "close": 42.27}, {"date": "2026-03-18", "close": 40.26}, {"date": "2026-03-19", "close": 39.82}, {"date": "2026-03-20", "close": 39.77}, {"date": "2026-03-23",
"close": 40.05}, {"date": "2026-03-24", "close": 39.28}, {"date": "2026-03-25", "close": 40.17}, {"date": "2026-03-26", "close": 38.82}, {"date": "2026-03-27", "close": 37.4}, {"date": "2026-03-30",
"close": 37.68}, {"date": "2026-03-31", "close": 38.42}, {"date": "2026-04-01", "close": 38.64}, {"date": "2026-04-02", "close": 37.97}, {"date": "2026-04-06", "close": 39.52}, {"date": "2026-04-07",
"close": 39.1}, {"date": "2026-04-08", "close": 40.42}, {"date": "2026-04-09", "close": 40.91}, {"date": "2026-04-10", "close": 41.56}], "summary_stats": {"drawdown_from_52w_high_pct":
-42.13311055416318, "distance_from_52w_low_pct": 17.733711048158657, "trailing_returns": {"five_day": 9.45483276270741, "ten_day": 7.058217413704282, "twenty_day": 4.030037546933666},
"trailing_volatility_20d": 2.399289860637252, "trailing_mean_return_20d": 0.19754747009371695, "recent_low": {"date": "2026-03-27", "close": 37.4, "days_ago": 9}, "recent_high": {"date": "2026-03-17",
"close": 42.27, "days_ago": 17}, "max_bounce_from_recent_low_pct": 11.122994652406428}, "shock_alert": {"event": "2026-04-06 spike: +4.1%", "daily_return_pct": 4.08, "comparable_events": 29,
"median_forward_return_pct": 3.43, "pct_positive": 62.1, "horizon_days": 10}}
```

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Bitcoin ETF monthly flows history 2024 2025 2026 billion monthly totals"
}
```

### 📋 Result

```
[{"title": "Bitcoin ETFs Return to Monthly Inflows for the First Time Since October", "url": "https://unchainedcrypto.com/bitcoin-etfs-post-first-monthly-inflows-since-october-2025-as-btc-price-
stabilizes/", "snippet": "One moment, please...\n\nPlease wait while your request is being verified...\n\nOne moment, please...\nLoader\nPlease wait while your request is being verified...",
"highlights": ["One moment, please...\n\nPlease wait while your request is being verified... One moment, please...\nLoader\nPlease wait while your request is being verified..."], "published_date":
"2026-04-01T00:00:00.000", "score": null}, {"title": "Bitcoin Achieves First ETF Monthly Inflow in 2026 - TradingView", "url": "https://www.tradingview.com/news/u_today:f653d3cb1094b:0-bitcoin-
achieves-first-etf-monthly-inflow-in-2026/", "snippet": "Bitcoin Achieves First ETF Monthly Inflow in 2026 \u2014 TradingView News\n\nSearch\n\nEN\n\n# Bitcoin Achieves First ETF Monthly Inflow in
2026\n\n1 min read\n\nAs March 2026 comes to a close, spot Bitcoin ETFs have recorded overall positive performance for the month, making it the best month for the Bitcoin funds so far in
2026.\n\nAccording to data showcased by SosoValue, Bitcoin ETFs have recorded their first monthly inflow of 2026 in March. This suggests that momentum has returned to the Bitcoin ETF market ",
"highlights": ["Bitcoin Achieves First ETF Monthly Inflow in 2026 \u2014 TradingView News\n\nSearch\n\nEN # Bitcoin Achieves First ETF Monthly Inflow in 2026\n\n1 min read As March 2026 comes to a
close, spot Bitcoin ETFs have recorded overall positive performance for the month, making it the best month for the Bitcoin funds so far in 2026. According to data showcased by SosoValue, Bitcoin ETFs
have recorded their first monthly inflow of 2026 in March. This suggests that momentum has returned to the Bitcoin ETF market after several months of consistent capital withdrawals. Bitcoin ETFs hit
$1.32 billion in March inflow The data revealed that Bitcoin ETFs collectively recorded a positive net ETF flow in March, closing the month with a massive $1.32 billion in inflows. While the prolonged
market volatility has seen institutional investors increasingly withdraw their funds while moving with caution, the inflow seen in March has reversed the negative trend that had seen Bitcoin funds
lose capital for four consecutive months. The fresh capital collectively achieved in March has come after January recorded $1.61 billion in outflows and February saw another $206.52 million exit. The
long monthly outflow streak started in November 2025, and it persisted until last month, February 2026. The rebound signals rising institutional demand as investors appear to be preparing
Bitcoin\u2019s potential for the long term as its market movements suggest it may be near its bottom. BlackRock retains dominance Following a decent monthly performance, Bitcoin ETFs recorded $117.63
million in net inflows on March 31, marking a strong monthly close. As usual, BlackRock has continued to lead the Bitcoin ETF market event in times of both weak and strong performances. Notably,
BlackRock led daily inflows, with about 1,450 BTC worth $98.42 million in just one day. Read original article on U.Today\n\nRead more from U.Today\n\n---\n\n## More news from U.Today"],
"published_date": "2026-04-01T15:43:00.000", "score": null}, {"title": "Monthly ETF Flows", "url": "https://jan3.com/monthly-etf-flows/", "snippet": "Monthly ETF Flows\n\nHome> Charts> Bitcoin ETF
Data> Monthly ETF Flows\n\n### Monthly ETF Flow in USD\n\nX\n\nFacebook\n\nLinkedIn\n\nMonthly net inflows and outflows for major Bitcoin ETFs.\n\nData for this chart is currently unavailable",
"highlights": ["Monthly ETF Flows\n\nHome> Charts> Bitcoin ETF Data> Monthly ETF Flows\n\n### Monthly ETF Flow in USD\n\nX\n\nFacebook\n\nLinkedIn Monthly net inflows and outflows for major Bitcoin
ETFs.\n\nData for this chart is currently unavailable"], "published_date": "2025-04-08T20:17:29.000", "score": null}, {"title": "Bitcoin ETF Tracker 2026 - Live Flows, Holdings & Performance for All
11 Spot ETFs | Bitcoin News Office", "url": "https://bitcoinnewsoffice.com/etf.html", "snippet": "Bitcoin ETF Tracker 2026 - Live Flows, Holdings & Performance for All 11 Spot ETFs | Bitcoin News
Office\n\n# Bitcoin ETF Tracker\n\nLive daily flows, holdings, and performance for all 11 US spot Bitcoin ETFs\n\nNet Flows Today\n\nLoading latest data...\n\nCumulative Net Inflows\n\nSince Jan
2024\n\nLive BTC Price\n\nFetching...\n\nBitcoin spot ETFs have attracted over $54 billion in cumulative net inflows since their historic SEC approval in January 2024. Track every ETF's daily flows,
holdings, and performance ", "highlights": ["Bitcoin ETF Tracker 2026 - Live Flows, Holdings & Performance for All 11 Spot ETFs | Bitcoin News Office # Bitcoin ETF Tracker\n\nLive daily flows,
holdings, and performance for all 11 US spot Bitcoin ETFs\n\nNet Flows Today Loading latest data...\n\nCumulative Net Inflows\n\nSince Jan 2024\n\nLive BTC Price\n\nFetching... Bitcoin spot ETFs have
attracted over $54 billion in cumulative net inflows since their historic SEC approval in January 2024. Track every ETF's daily flows, holdings, and performance below.   ...    Total AUM?Assets Under
Management \u2014 the total market value of all investments held across all ETFs.\n\n$123.1B Combined Assets\n\nTotal BTC Held\n\n1,221,000\n\nAcross 11 ETFs\n\nNumber of ETFs\n\n11   ...    Market
Dominance\n\n6.4%\n\nOf total BTC supply\n\nTrading Days Tracked\n\n541\n\nDaily flow records\n\nLast Updated\n\n--   ...    \ud83d\udd2c Is the market overheating? Check the Bitcoin Stress &
Fragility Index \u2192\n\n## Daily ETF Flows (Last 30 Days) 30 Days 90 Days\n\n## ETF Comparison Table\n\nClick column headers to sort. All flow data in US$ millions. | #\u25bc | Ticker\u25bc |
Issuer\u25bc | Daily Flow?Net money flowing into (+) or out of (-) the ETF today, in millions of US dollars.\u25bc | Cumulative?Total net flows since the ETF launched in January 2024.\u25bc |
Expense?Annual fee as a percentage of   ...    ## Cumulative Net Inflows Over Time\n\n## Recent Daily Flow History\n\nLast 30 Days Last 90 Days | Date | IBIT | FBTC | GBTC | ARKB | BITB | Other |
Total |\n| --- | --- | --- | --- | --- | --- | --- | --- | View All 541+ Daily Flow Records \u2192\n\n## ETF Investment Calculator\n\n### Compare Bitcoin ETF Costs   ...    Spot Bitcoin ETFs hold
actual Bitcoin in custody, allowing investors to gain exposure through traditional brokerage accounts. The SEC approved the first 11 spot Bitcoin ETFs in January 2024, attracting over $54 billion in
cumulative net inflows \u2014 making this the most successful ETF launch in history.   ...    Daily ETF flows are one of the best real-time indicators of institutional Bitcoin demand. Large inflows
signal institutions are buying Bitcoin through ETFs, while outflows suggest selling. IBIT alone has attracted $61+ billion,   ...    Bitcoin ETFs hold approximately 6.4% of all circulating Bitcoin.
This institutional demand, combined with Bitcoin's fixed 21M supply cap and the 2024 halving, creates significant supply pressure. ETFs are now one of the largest sources   ...    How much Bitcoin do
ETFs hold? As of early 2026, the 11 US spot Bitcoin ETFs collectively hold approximately 1.35 million BTC, worth over $130 billion. This represents roughly 6.4% of the total Bitcoin supply.
BlackRock's IBIT alone holds about 620,000 BTC,   ...    What are Bitcoin ETF flows? ETF flows measure the net amount of money entering (inflows) or leaving (outflows) a Bitcoin ETF each trading day.
Positive flows mean more money came in than went out \u2014 indicating investors are net buying. Negative flows indicate net selling. Daily flow data is published after US market close and is a key
indicator of institutional Bitcoin demand. Which Bitcoin ETF has the most inflows? BlackRock's IBIT has dominated with over $61 billion in cumulative net inflows since January 2024 \u2014 the fastest
an ETF has ever reached this milestone. Fidelity's FBTC is second with approximately $11 billion. Together, IBIT and FBTC   ...    What is the cheapest Bitcoin ETF? The cheapest by expense ratio is
Grayscale Bitcoin Mini Trust (BTC) at 0.15%, followed by Franklin Bitcoin ETF (EZBC)   ...    ## Explore More\n\n\ud83c\udfe2Saylor Tracker714K BTC & counting\n\n\ud83d\udc0bWhale TrackerLargest BTC
wallets \ud83d\udcb0DCA CalculatorPlan your strategy\n\n\ud83d\udcdcBitcoin HistoryThe full timeline \u26a0\ufe0f Disclaimer: ETF flow"], "published_date": null, "score": null}, {"title": "Real-Time
Bitcoin ETF Fund Flows - Monitor BTC Market Sentiment", "url": "https://btcetffundflow.com/", "snippet": "Real-Time Bitcoin ETF Fund Flows - Monitor BTC Market Sentiment\n\nGet insights on daily
Bitcoin ETF flows to guide your investment decisions.\n\n1W\n\n0.19%\n\n1M\n\n0.91%\n\n3M\n\n-7.13%\n\nUSA\n\nHong Kong\n\nNet Flow\n\nAUM\n\n\u20bf0\n\nBTC Holdings\n\nTake a snapshot\n\nData are
derived from the daily-reported BTC holdings, as publicly disclosed on each ETF\u2019s official website.\n\nUpdated date\n\n2026-04-08\n\nUS Bitcoin ETF - AUM (2026-04-08)\n\n\u20bf 1,291,013\n\nBTC
Holdings\n\nManaged by SmashFi\n\nSelect All Issuers\n\nBTC Price\n\n$71,924\n\n", "highlights": ["ETF Fund Flows - Monitor BTC Market Sentiment Get insights on daily Bitcoin ETF flows to guide your
investment decisions.\n\n1W\n\n0.19%\n\n1M\n\n0.91%\n\n3M\n\n-7.13%\n\nUSA Hong Kong\n\nNet Flow\n\nAUM\n\n\u20bf0\n\nBTC Holdings\n\nTake a snapshot Data are derived from the daily-reported BTC
holdings, as publicly disclosed on each ETF\u2019s official website. Updated date\n\n2026-04-08\n\nUS Bitcoin ETF - AUM (2026-04-08)\n\n\u20bf 1,291,013\n\nBTC Holdings\n\nManaged by SmashFi Select
All Issuers\n\nBTC Price\n\n$71,924\n\nTOTAL\n\n\u20bf1,291,013\n\nGBTC (Grayscale)\n\n\u20bf153,851\n\nBITB (Bitwise)\n\n\u20bf37,567 IBIT (BlackRock)\n\n\u20bf785,187\n\nHODL
(VanEck)\n\n\u20bf16,807\n\nEZBC (Franklin Templeton)\n\n\u20bf6,303\n\nBTCO (Invesco Galaxy)\n\n\u20bf6,711 BRRR (Valkyrie)\n\n\u20bf6,335\n\nFBTC (Fidelity)\n\n\u20bf188,475\n\nDEFI
(Hashdex)\n\n\u20bf135\n\nARKB (Ark 21Shares)\n\n\u20bf35,403 BTCW (WisdomTree)\n\n\u20bf2,165\n\nBTC (Grayscale Mini)\n\n\u20bf52,074\n\nDaily ETF Net Flow\n\nUpdated date\n\n2026-04-08 Top Daily Net
Flow\n\n\ud83e\udd47\n\nIBIT\n\n(BlackRock)\n\n\ud83e\udd48\n\nBITB\n\n(Bitwise)\n\n\ud83e\udd49\n\nEZBC\n\n(Franklin Templeton)\n\n4\n\nBTCO\n\n(Invesco Galaxy) 5\n\nBRRR\n\n(Valkyrie)\n\n| Rank |
Ticker/Issuer | Net Flows(\u20bf) |\n| --- | --- | --- |\n| + 567 |\n| 0 |\n| 0 |\n| 0 |\n| 0 | - The data used in this chart is information published on the official website of each ETF management
company. Please note that we take no responsibility for the integrity of this data. - The latest daily data is updated at D+1 09:00 (GMT).   ...    Dive into the Bitcoin ETF market with our exclusive
weekly newsletter, offering expert analysis on fund flows, AUM trends,"], "published_date": null, "score": null}, {"title": "Bitcoin ETF Tracker | CoinFlows", "url": "https://coinflows.org/",
"snippet": "Bitcoin ETF Tracker | CoinFlows\n\n# CoinFlows\n\nLoading your dashboard...\n\nLive Data Updates\n\n# Bitcoin and Ethereum ETF Tracker\n\nIntroducing CoinFlows, track institutional
adoption and market movements for Bitcoin & Ethereum ETF Flows as Wall Street embraces crypto.\n\nBitcoin ETF Flow\n\nTotal Net Flows to Date\n\n$56.5B\n\n+0.6% today\n\n1-Day Net
Flow\n\n$343.2M\n\n7-Day Net Flow\n\n$531.0M\n\nEthereum ETF Flow\n\nTotal Net Flows to Date\n\n$10.3B\n\n-0.1% today\n\n1-Day Net Flow\n\n-$5.7M\n\n7-Day Net Flow\n\n$7.5M\n\nBitcoin", "highlights":
["Bitcoin ETF Tracker | CoinFlows\n\n# CoinFlows\n\nLoading your dashboard...\n\nLive Data Updates   ...    Introducing CoinFlows, track institutional adoption and market movements for Bitcoin &
Ethereum ETF Flows as Wall Street embraces crypto. Bitcoin ETF Flow\n\nTotal Net Flows to Date\n\n$56.5B\n\n+0.6% today\n\n1-Day Net Flow\n\n$343.2M\n\n7-Day Net Flow\n\n$531.0M Ethereum ETF
Flow\n\nTotal Net Flows to Date\n\n$10.3B\n\n-0.1% today\n\n1-Day Net Flow\n\n-$5.7M\n\n7-Day Net Flow\n\n$7.5M Bitcoin ETF Flow Trends\n\nCopy to Clipboard\n\nShare to
Twitter\n\nDailyWeeklyMonthly\n\nFlowsProviders\n\nTotal Inflow $857.3M\n\nTotal Outflow\n\n-$326.3M\n\nNet Flow\n\n$531.0M\n\nCoinFlows.org\n\nEthereum ETF Flow Trends\n\nCopy to Clipboard Share to
Twitter\n\nDailyWeeklyMonthly\n\nFlowsProviders\n\nTotal Inflow\n\n$129M\n\nTotal Outflow\n\n-$121.5M\n\nNet Flow\n\n$7.5M CoinFlows.org\n\n## Historical ETF Impact Timeline Key milestones in the
evolution of Bitcoin and Ethereum ETFs and their impact on cryptocurrency markets.\n\nOctober 2021 First\n\n### First Bitcoin Futures ETF Launch ProShares Bitcoin Strategy ETF (BITO) became the first
Bitcoin-linked ETF in the US, attracting over $1 billion in   ...    January 2024\n\nMilestone\n\n### Spot Bitcoin ETFs Approved The SEC approved the first spot Bitcoin ETFs in the US after years of
rejections, allowing investors direct exposure to   ...    Bitcoin price increased by 15% in the week following approval\n\nJanuary 2024\n\nMilestone\n\n### Spot Bitcoin ETFs Approved   ...    Bitcoin
price increased by 15% in the week following approval\n\nFebruary 2024\n\n### Record-Breaking ETF Inflows Bitcoin ETFs collectively accumulated over $10 billion in assets within their first month of
trading, demonstrating unprecedented demand from institutional investors and financial advisors. This rapid adoption exceeded most analysts'   ...    February 2024\n\n### Record-Breaking ETF Inflows
Bitcoin ETFs collectively accumulated over $10 billion in assets within their first month of trading, demonstrating unprecedented demand from institutional investors and financial advisors. This rapid
adoption exceeded most analysts'   ...    long-term tax-advantaged cryptocurrency exposure for millions of Americans. This development represented a significant step toward mainstream adoption of
digital assets as a legitimate asset class. Q1 2025\n\n### Combined ETF Assets Surpass $50B Bitcoin and Ethereum ETFs collectively reached $50 billion in assets under management, demonstrating
sustained institutional demand and growing mainstream acceptance of cryptocurrencies as a legitimate asset class within traditional investment portfolios. Q1 2025\n\n### Combined ETF Assets Surpass
$50B Bitcoin and Ethereum ETFs collectively reached $50 billion in assets under management, demonstrating sustained institutional demand and growing mainstream acceptance of cryptocurrencies as a
legitimate asset class within   ...    Key Impacts\n\n## ETF Impact on Cryptocurrency Markets\n\n### Price Discovery ETFs have contributed to"], "published_date": null, "score": null}, {"title": "What
are the inflows and outflows for bitcoin into etfs | AIME by AInvest", "url": "https://www.ainvest.com/aime/share/inflows-outflows-bitcoin-etfs-676dcf/", "snippet": "What are the inflows and outflows
for bitcoin into etfs | AIME by AInvest\n\nSymbols\n\nSymbols\n\nAime\n\nProducts\n\nNews\n\nMarkets\n\nWatchlist\n\nBrokers\n\n \n\n \n\n# What are the inflows and outflows for bitcoin into
etfs?\n\n3/6/2026 03:00pm\n\nMoney is still **net flowing into Bitcoin via spot ETFs**, not out of them. Cumulative net inflows are in the **tens of billions of dollars**, and the most recent days
show **strong positive daily flows** with a few outflow days mixed in. \ud83d\udcca --- ### 1\ufe0f\u20e3 Big picture \u2013 cumul", "highlights": ["Money is still **net flowing into Bitcoin via spot
ETFs**, not out of them. Cumulative net inflows are in the **tens of billions of dollars**, and the most recent days show **strong positive daily flows** with a few outflow days mixed in. \ud83d\udcca
--- ### 1\ufe0f\u20e3 Big picture \u2013 cumulative flows since launch - U.S. **spot Bitcoin ETFs** (IBIT, FBTC, ARKB, etc.) have attracted very large net inflows since they launched in early 2024. -
Based on SoSoValue data reported in early March 2026, cumulative **net inflows are around \\$55.3 billion** as of Mar 3, 2026. - Earlier reporting noted that cumulative net flows **peaked above \\$62
billion in Oct 2025** and, after some outflows, remained **above \\$54 billion** into early 2026. **Takeaway:** Despite periods of heavy redemptions, ETFs remain a massive net channel of capital
*into* Bitcoin, not a net drain. --- ### 2\ufe0f\u20e3 Recent flows \u2013 late Feb to early Mar 2026 Using Bitbo\u2019s ETF-flow table for the main U.S. spot Bitcoin ETFs (IBIT, FBTC, GBTC, BTC,
BITB, ARKB, HODL, BRRR, EZBC, BTCO, BTCW, DEFI): **Period:** 9 recent trading days from **Feb 19 \u2013 Mar 4, 2026** **Aggregate across all these ETFs:** - **Net flow (all days combined):**
+**1,838.3** (Bitbo \u201cflow units,\u201d representing changes in BTC held by the ETFs) - **Gross inflows (positive days only):** +**2,170.5** - **Gross outflows (negative days only):**
\u2013**332.2** **Daily pattern (all ETFs combined):** - **Strong inflow days:** - Mar 4: **+631.7** - Mar 2: **+361.5** - Feb 25\u201326: **+398.7** and **+397.7** - **Outflow days:** - Feb 19:
**\u2013172.7** - Feb 23: **\u2013159.5** So over this recent window you\u2019ve had **7 inflow days vs. 2   ...    ```reference [{\"id\":12,\"type\":\"plotly-json\"}] ``` Over these days,
Bitbo\u2019s totals show the **biggest net inflows** going into: IBIT, BITB, and ARKB, with IBIT taking the largest share of net new BTC holdings across ETFs in that period. --- ### 3\ufe0f\u20e3 How
to read these inflows/outflows Conceptually, **ETF flows** work like this: - **Inflow (net   ...    offloads BTC \u2192 **ETF BTC holdings go down.** What they **signal**: - **Sustained net inflows**
usually indicate that   ...    Macro/market news (rate expectations, risk sentiment) --- ### 4\ufe0f\u20e3 Where you can track Bitcoin ETF flows in real time If you want to follow this data yourself,
some commonly used dashboards: - **Bitbo \u2013 \u201cBitcoin ETF Flows\u201d** (table and chart of daily flows by ETF and totals). - **SoSoValue \u2013 US spot BTC ETF flows** (daily per-issuer flows
+ cumulative net flows, widely cited in media). - **CoinGlass \u2013 Bitcoin ETF fund flows page** (ETF list, AUM, net flows, plus   ...    consistency. --- If you"], "published_date": null, "score":
null}, {"title": "Bitcoin ETF flow graphic 2025| Statista", "url": "https://cdn2.statista.com/statistics/1462194/bitcoin-etf-flows-per-day/", "snippet": "Bitcoin ETF flow graphic 2025|
Statista\n\nBlackRock's Bitcoin ETF received around 15 billion dollars' worth of investment inflow since January 2024, whereas Grayscale lost 16 billion. This is according to a day-to-day investment
flow timeline involving 10 of the 11 Bitcoin ETFs that got approved by the U.S. Securities and Exchange Commission in early 2024. The highest inflow towards these ETFs occurred in March, coinciding
with the Bitcoin price's all-time high and a general increase in Bitcoin t", "highlights": ["BlackRock's Bitcoin ETF received around 15 billion dollars' worth of investment inflow since January 2024,
whereas Grayscale lost 16 billion. This is according to a day-to-day investment flow timeline involving 10 of the 11 Bitcoin ETFs that got approved by the U.S. Securities and Exchange Commission in
early 2024. The highest inflow towards these   ...    ## Cryptocurrency investment flow per day in the Bitcoin ETFs listed on the NYSE and NASDAQ from January 2024 to December 2025 (in million U.S.
dollars) | Characteristic | ARK 21Shares Bitcoin ETF (ARKB) | Bitwise Bitcoin ETF (BITB) | Valkyrie Bitcoin Fund (BRRR) | Grayscale Bitcoin Mini Trust ETF (BTC) | Invesco Galaxy Bitcoin ETF (BTCO) |
WisdomTree Physical Bitcoin (BTCW) | Franklin Bitcoin ETF (EZBC) | Fidelity Wise Origin Bitcoin Fund (FBTC) | Grayscale Bitcoin Trust (GBTC) | VanEck Bitcoin Trust (HODL) | iShares Bitcoin Trust
(IBIT) | Sum | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Jan 11, 2024 | 65.3 | 237.9 | 29.4 | 655.3 | 17.4 | 1 | 50.1 | 227 | -95.1 | 10.6 | 111.7 | 655.3 | |
Jan 12, 2024 | 39.8 | 17.4 | 20.2 | 203 | 28.4 | 0 | 0 | 195.3 | -484.1 | 0 | 386 | 203 | | Jan 15, 2024 | - | - | - | 0 | - | - | - | - | - | - | - | 0 | | Jan 16, 2024 | 122.3 | 50.2 | 15.3 | -52.7
| 31.9 | 0 | 0 | 102 | -594.4 | 7.3 | 212.7 | -52.7 |   ...    | Jul 02, 2024 | 2.5 | -6.8 | 0 | -13.7 | 0 | 0 | 0 | 5.4 | -32.4 | 3.5 | 14.1 | -13.7 |  | Dec 26, 2024 | 186.9 | -8.3   ...    | Dec
27, 2024 | -112.6 | -36 | 0 | -287.9 | -14.2 | 0 | 0 | -208.2 | 3.7 | 0 | 79.4 | -287.9 | | Dec 30, 2024 | -26.4 | -31.4 | 0 | -415.1 | 0 | 0 | 0 | -154.6 | -134.5 | 0 | -36.5 | -415.1 | | Dec 31,
2024 | -11.2 | 8.7 | 0 | 5.3 | 0 | 0 | 0 | 36.8 | -9.6 | 0 | -23.5 | 5.3 | | Jan 01, 2025 | - | - | - | 0 | - | - | - | - | - | - | - | 0 |  Additional Information \u00a9 Statista 2026\n\nShow
source\n\nDownload for free\n\nDownload\n\nPDF+\n\nXLS+\n\nPNG+\n\nPPT+\n\nSource   ...    Show sources information Show publisher information Use Ask Statista Research Service\n\nRelease
date\n\nDecember 2025   ...    +Weekly crypto asset flow and AUM from Fidelity's Wise Origin Bitcoin Fund 2024  +Weekly crypto asset flow and AUM from   ...    +Weekly crypto asset flow and AUM from
Grayscale Bitcoin Trust (GBTC) 2023-2024 +Weekly investment flow into cryptocurrency, such as from Bitcoin ETFs, 2023-2024   ...    - Monthly number of Bitcoin ATMs worldwide 2015-2025 The most
important statistics  - Weekly crypto asset flow and AUM from Grayscale Bitcoin Trust (GBTC) 2023-2024 - Weekly crypto asset flow and AUM from Fidelity's Wise Origin Bitcoin Fund 2024 - Weekly crypto
asset flow and AUM from BlackRock's iShares Bitcoin Trust 2024 - Daily crypto asset flow of the Bitcoin ETFs listed at NYSE and NASDAQ 2024-2025 - Weekly investment flow into cryptocurrency, such as
from Bitcoin ETFs, 2023-2024   ...    - Monthly number of Bitcoin ATMs worldwide 2015-2025 Bitcoin ETFs 5  - Weekly crypto asset flow and AUM from Grayscale Bitcoin Trust (GBTC) 2023-2024 - Weekly
crypto asset flow and AUM from Fidelity's Wise Origin Bitcoin Fund 2024 - Weekly crypto asset flow and AUM from BlackRock's iShares Bitcoin Trust 2024 - Daily crypto asset flow of the Bitcoin ETFs
listed at NYSE and NASDAQ 2024-2025 - Weekly investment"], "published_date": "2025-12-02T12:00:00.000", "score": null}, {"title": "Bitcoin ETF Performance Q1 2026: Inflows & Outflows \u00b7 Blocklr",
"url": "https://blocklr.com/news/bitcoin-etf-performance-q1-2026/", "snippet": "Bitcoin ETF Performance Q1 2026: Inflows & Outflows \u00b7 Blocklr\n\n# Bitcoin ETF Performance Q1 2026: Inflows,
Outflows, and What It Means\n\n### In This Article\n\n1. Bitcoin ETF Q1 2026 Overview\n2. Flow Data by ETF Provider\n3. Cumulative Flow Trends\n4. Fee Comparison and Cost Analysis\n5. What the Flow
Patterns Signal\n6. Institutional Adoption Accelerates\n7. Outlook for Q2 2026 and Beyond\n8. Frequently Asked Questions\n\n### Key Takeaways\n\n- Spot Bitcoin ETFs attracted $18.7 billion in net
inflows during", "highlights": ["Bitcoin ETF Performance Q1 2026: Inflows & Outflows \u00b7 Blocklr   ...    ### Key Takeaways - Spot Bitcoin ETFs attracted $18.7 billion in net inflows during Q1
2026, pushing total AUM past $128 billion - BlackRock's IBIT dominated with $8.4 billion in net inflows, followed by Fidelity's FBTC at $4.1 billion - Grayscale GBTC outflows slowed to $1.2 billion
for the quarter, down sharply from peak outflow periods in 2024   ...    The first quarter of 2026 marked another record-setting period for spot Bitcoin ETFs in the United States. After   ...    for a
growing number of institutional and retail investors. Combined net inflows for the quarter totaled $18.7 billion, bringing cumulative net inflows since inception past the $65 billion mark. Bitcoin's
price traded between $94,000 and $112,000 during the quarter, with the appreciation driving total assets under management across all U.S. spot Bitcoin ETFs to approximately $128 billion by March 15,
2026. That figure represents a 22% increase from the $105 billion recorded at the end of 2025, fueled by both price gains and fresh   ...    Bitcoin thesis, while BITB has positioned itself as a cost-
effective option with its 0.20% expense ratio and strong crypto-native branding. ## Cumulative Flow Trends\n\nChart: Cumulative Net Flows into Spot Bitcoin ETFs (Jan 2024 - Mar 2026) Type: Area chart.
X-axis: Monthly intervals from January 2024 through March 2026. Y-axis: Cumulative net flows in billions of USD. Data shows a steep initial ramp from $0 to ~$12B in Q1 2024, a plateau and slight dip
mid-2024 at ~$15B, renewed acceleration to ~$35B by end of 2024, steady climbing through 2025 reaching ~$47B, and a sharp Q1 2026 spike pushing the total past $65B. The cumulative flow chart reveals
three distinct phases in spot Bitcoin ETF adoption. The first phase, spanning January through April 2024, was characterized by euphoric launch-period demand that pushed cumulative inflows past $12
billion within the first three months. The second phase, covering mid-2024 through early 2025, saw slower but steady accumulation as the initial excitement faded and periodic outflow episodes tempered
net figures. The third and current phase, beginning in Q4 2025, shows renewed momentum driven by institutional adoption and Bitcoin's sustained move above $90,000. January 2026 was the weakest month
of the quarter with $3.8 billion in net inflows, dragged down by the late-month selloff. February rebounded to $6.9 billion as Bitcoin reclaimed $105,000. March, through the 15th, was on pace for
approximately $8.0 billion, which would make it the strongest single month since the initial launch period.   ...    Several patterns from Q1 2026 offer insight into the evolving Bitcoin ETF market.
First, the correlation between Bitcoin price and daily ETF flows has weakened compared to 2024. In the early months after launch, inflows and outflows   ...    trading days in late January, compared
to eight consecutive days during the mid-2024 pullback. The average daily outflow on negative days was $340 million in Q1 2026 versus $520 million in Q1 2025, indicating that fewer investors   ...
Third, GBTC's outflow rate has stabilized at a level that is manageable for the broader market. At $1.2 billion for the   ...    BlackRock's iShares Bitcoin Trust (IBIT) led all spot Bitcoin ETFs with
approximately $8.4 billion in net inflows   ...    What was the total AUM for spot Bitcoin ETFs at the end of Q1 2026? Combined assets under management for all U.S. spot Bitcoin ETFs reached
approximately $128 billion by mid-March 2026,   ...    Did Grayscale GBTC continue to see outflows in Q1 2026? GBTC outflows slowed significantly in Q1 2026 compared to 2024. The fund saw
approximately $1.2 billion in net outflows for the quarter, a sharp reduction from the multi-billion-dollar monthly outflows seen in its first year after   ...    What drove Bitcoin ETF inflows in Q1
2026? Several factors"], "published_date": "2026-03-18T13:17:50.000", "score": null}, {"title": "Bitcoin ETF Flows Today \u2013 Daily Net Inflows, AUM & Holdings", "url":
"https://heyapollo.com/bitcoin-tracker", "snippet": "Bitcoin ETF Flows Today \u2013 Daily Net Inflows, AUM & Holdings \n\n \n\n \n\n \n\n \n\n \n\n \n\n### Assets Under Management\n\n \n\n1.288M
BTC\n\n \n\n$85.9B\n\nUS Listed Spot Bitcoin ETF assets\n\n \n\n \n\n### 1-Day Net Flows\n\n \n\n+135 BTC\n\n \n\n+$9M\n\nFlows into ETFs\n\n \n\n \n\n### 7-Day Net Flows\n\n \n\n-3,048 BTC\n\n
\n\n-$203M\n\nFlows out of ETFs\n\n \n\n \n\n### 30-Day Net Flows\n\n \n\n+6,509 BTC\n\n \n\n+$435M\n\nFlows into ETFs\n\n \n\nHoldings as of market close: 2 April 2026\n\n \n\n### IBIT\n\niShares
Bitcoin Trust\n\n \n\n$37.97\n\n-1.73%\n\n \n\nAUM\n\n$52.17B\n\nBTC", "highlights": ["Bitcoin ETF Flows Today \u2013 Daily Net Inflows, AUM & Holdings \n\n \n\n \n\n \n\n \n\n \n\n \n\n### Assets
Under Management 1.288M BTC\n\n \n\n$85.9B\n\nUS Listed Spot Bitcoin ETF assets\n\n \n\n \n\n### 1-Day Net Flows\n\n \n\n+135 BTC\n\n \n\n+$9M Flows into ETFs\n\n \n\n \n\n### 7-Day Net Flows\n\n
\n\n-3,048 BTC\n\n \n\n-$203M\n\nFlows out of ETFs\n\n \n\n \n\n### 30-Day Net Flows +6,509 BTC\n\n \n\n+$435M\n\nFlows into ETFs\n\n \n\nHoldings as of market close: 2 April 2026\n\n \n\n### IBIT
iShares Bitcoin Trust\n\n \n\n$37.97\n\n-1.73%\n\n \n\nAUM\n\n$52.17B\n\nBTC Held\n\n782.43K\n\n1D Flow\n\n-$3.01M\n\n7D Flow\n\n-$185.47M 30D Flow\n\n+$678.39M\n\nFee\n\n0.25%\n\n### FBTC\n\nWise
Origin Bitcoin Trust\n\n \n\n$58.36\n\n-1.68%\n\n \n\nAUM\n\n$12.48B\n\nBTC Held   ...    Grayscale Bitcoin Trust (Conversion)\n\n \n\n$52.15\n\n-1.70%\n\n \n\nAUM\n\n$10.33B\n\nBTC
Held\n\n154.85K\n\n1D Flow\n\n$0.00M\n\n7D Flow -$13.26M\n\n30D Flow\n\n-$121.15M\n\nFee\n\n1.50%\n\n### BTC\n\nGrasycale Mini Trust\n\n \n\n$29.65\n\n-1.69%\n\n \n\nAUM\n\n$3.46B\n\nBTC Held   ...
AUM\n\n$0.14B\n\nBTC Held\n\n2.15K\n\n1D Flow\n\n$0.00M\n\n7D Flow\n\n$0.00M\n\n30D Flow\n\n+$7.77M\n\nFee\n\n0.25%\n\n \n\nPrice\n\n24h change BTC Held \n\n AUM \n\n 1D Flows \n\n 7D Flows \n\n 30D
Flows \n\n Fee \n\niShares Bitcoin Trust \n\n \n\n$37.97\n\n-1.73% Wise Origin Bitcoin Trust \n\n \n\n$58.36\n\n-1.68%\n\nGrayscale Bitcoin Trust (Conversion) \n\n \n\n$52.15\n\n-1.70% Grasycale Mini
Trust \n\n \n\n$29.65\n\n-1.69%\n\nBitwise Bitcoin ETF \n\n \n\n$36.39\n\n-1.68%\n\nArk/21 Shares Bitcoin Trust $22.24\n\n-1.68%\n\nVanEck Bitcoin Trust \n\n \n\n$18.95\n\n-1.71%\n\nInvesco Galaxy
Bitcoin ETF \n\n \n\n$66.71\n\n-1.68%   ...    | Issuer | ETF | Ticker | | | | | | | Custodian |\n| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | | BlackRock | IBIT | | 782.43K |
$52.17B | -$3.01M | -$185.47M | +$678.39M | 0.25% | Coinbase | | Fidelity | FBTC | | 187.10K | $12.48B | +$7.29M | -$26.22M | -$40.39M | 0.25% | Self-custody | | Grayscale | GBTC | | 154.85K | $10.33B
| $0.00M | -$13.26M | -$121.15M | 1.50% | Coinbase | | Grayscale | BTC | | 51.90K | $3.46B | $0.00M | +$10.25M | +$52.27M | 0.15% | Coinbase |   ...    | WisdomTree | BTCW | | 2.15K | $0.14B | $0.00M
| $0.00M | +$7.77M | 0.25% | Coinbase | | | Total | 1.288M | $85.9B | +$9.0M | -$203.5M | +$434.5M |\n| |   ...    ## ETF Flows (BTC)\n\nNet BTC flows since inception\n\n \n\n### Daily Flows & Total
Since Inception\n\nDaily Weekly Monthly Loading chart data\u2026\n\n \n\n \n\n## ETFs - BTC Holdings Over Time\n\nBitcoin holdings accumulation over time for Spot ETFS   ...    This tracker monitors
daily net flows for all US spot Bitcoin ETFs including BlackRock's IBIT, Fidelity's FBTC, ARK 21Shares' ARKB, Bitwise's BITB, and others. Data is updated each trading day after market close. What you
can track: - Net flows over 1, 7 and 30 days for each ETF\n- Total BTC holdings by fund and Assets under management (AUM) - Historical flow trends and holdings charts ## Frequently Asked Questions\n\n
How much did Bitcoin ETFs flow today? US spot Bitcoin ETFs saw net inflows of $9M in the most recent trading day. This tracker updates daily after market   ...    What is the total AUM of Bitcoin
ETFs? The combined assets under management (AUM) of all US spot Bitcoin ETFs is currently $85.9B, representing 1,287,602 BTC   ...    BlackRock's iShares Bitcoin Trust (IBIT) holds the most Bitcoin
among US spot ETFs, followed by Fidelity's FBTC. You   ...    How do I track Bitcoin ETF inflows? This tracker monitors daily net flows, 7-day cumulative flows, and 30-day cumulative flows for all US
spot Bitcoin ETFs. Detailed charts showing BTC flows"], "published_date": null, "score": null}]
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "Bitcoin ETF inflows April 2026 week",
  "hours_back": 72,
  "categories": [
    "Finance",
    "Business"
  ]
}
```

### 📋 Result

```
Error calling tool 'search_news': APIError: 403015 - You've reached your maximum billable overage limit for 'requests'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

```json
{
  "url": "https://farside.co.uk/btc/",
  "prompt": "What are the daily total net flow values for March 2026 and the complete April 2026 data? List each date and the Total column value."
}
```

### 📋 Result

```
{"url": "https://farside.co.uk/btc/", "content": "Based on the table, here are the daily total net flow values:\n\n**March 2026:**\n- March 24: -74.5\n- March 25: 7.8\n- March 26: -171.3\n- March 27:
-225.5\n- March 30: 69.4\n- March 31: 117.5\n\n**April 2026:**\n- April 1: -173.7\n- April 2: 9.0\n- April 6: 471.4\n- April 7: -159.1\n- April 8: -93.9\n- April 9: 358.1\n- April 10: 240.4\n\nAll
values are in millions of dollars.\n\n**Relevant links:**\n- [Alternative table with all daily flow data](https://farside.co.uk/bitcoin-etf-flow-all-data/)", "title": "Farside Investors"}
```

## 💭 Thinking

Let me now analyze the data I have and compute the probability. Let me note some discrepancies in the data sources:

From Farside (the resolution source):
- Apr 1: -173.7
- Apr 2: 9.0
- Apr 6: 471.4
- Apr 7: -159.1
- Apr 8: -93.9
- Apr 9: 358.1
- Apr 10: 240.4

Total so far: 652.2M

But I noticed bitbo.io shows Apr 10 as 0.0 total, and Apr 9 as 336.7. And there's a news article saying Apr 10 had ~$334.63M inflow worth of BTC. 

The Farside data shows 240.4 for Apr 10, though other sources like CoinFlows and news reports suggest around $335M for that day. Since Farside is my resolution source, I'll use their 240.4 figure despite the discrepancy with the external reports.

Looking at the cumulative picture, I've got $652.2M through Apr 10, leaving $347.8M needed across the remaining ~14 trading days in April. This context matters because March 2026 was the first positive month with $1.32B in inflows, and Q1 overall saw $18.7B. inflows (though this seems very high - the article from blocklr might be unreliable, as Jan had -$1.61B and Feb had -$206.52M according to the other source. Let me note that there are contradictions)

Actually, looking at TradingView/U.Today article: "January recorded $1.61 billion in outflows and February saw another $206.52 million exit" and March had $1.32B inflows. So Q1 was roughly: -1.61 + (-0.207) + 1.32 = -0.497B. The blocklr $18.7B figure seems very wrong or maybe it's a different time period.

Key factors:
- Already at $652.2M through 7 trading days (average $93.2M/day)
- Need only $347.8M more over 14 trading days ($24.8M/day average needed)
- Recent trend is positive: last 3 days were 471.4, -159.1, -93.9, 358.1, 240.4
- Bitcoin price is recovering (IBIT at $41.56, up from recent low of $37.40 on Mar 27)
- March had $1.32B total inflows
- The 52-week high for IBIT was $71.82, current is $41.56 (42% drawdown)

But there are headwinds too: the month started with a -$173.7M outflow, there were some significant outflow days, geopolitical tensions around the US-Iran Strait of Hormuz are adding volatility, and the market remains choppy overall. The question closes today at 16:30 UTC.

I should run a Monte Carlo simulation based on the historical daily flow distribution to get a better sense of the probability.

I'm running a Monte Carlo simulation based on the historical daily flow distribution to estimate the probability of reaching $1B by end of April.

## 💬 Response

Now let me run a Monte Carlo simulation to model the remaining April flows.

## 🔧 Tool: mcp__sandbox__execute_code


## 🔧 Tool: mcp__search__web_search


```json
{
  "code": "\nimport numpy as np\n\n# April 2026 daily flows from Farside (resolution source)\napril_flows_so_far = [-173.7, 9.0, 471.4, -159.1, -93.9, 358.1, 240.4]\ncumulative_so_far = sum(april_flows_so_far)\nremaining_needed = 1000 - cumulative_so_far\nremaining_days = 14  # Apr 13-30 trading days\n\nprint(f\"Cumulative April flows through Apr 10: ${cumulative_so_far:.1f}M\")\nprint(f\"Remaining to reach $1B: ${remaining_needed:.1f}M\")\nprint(f\"Remaining trading days: {remaining_days}\")\nprint()\n\n# Use April daily flows as our empirical distribution\n# But also incorporate broader recent history for better distribution estimation\n# Let's use the late March + April data we have\nrecent_daily_flows = [\n    # Late March 2026 (from Farside)\n    -74.5, 7.8, -171.3, -225.5, 69.4, 117.5,\n    # April 2026\n    -173.7, 9.0, 471.4, -159.1, -93.9, 358.1, 240.4\n]\n\nmean_flow = np.mean(recent_daily_flows)\nstd_flow = np.std(recent_daily_flows, ddof=1)\nmedian_flow = np.median(recent_daily_flows)\n\nprint(f\"Recent daily flows (late Mar + Apr):\")\nprint(f\"  Mean: ${mean_flow:.1f}M\")\nprint(f\"  Std dev: ${std_flow:.1f}M\")\nprint(f\"  Median: ${median_flow:.1f}M\")\nprint(f\"  Min: ${min(recent_daily_flows):.1f}M, Max: ${max(recent_daily_flows):.1f}M\")\nprint()\n\n# April-only stats\napril_mean = np.mean(april_flows_so_far)\napril_std = np.std(april_flows_so_far, ddof=1)\nprint(f\"April-only daily flows:\")\nprint(f\"  Mean: ${april_mean:.1f}M\")\nprint(f\"  Std dev: ${april_std:.1f}M\")\nprint()\n\n# Monte Carlo simulation using April daily flow distribution\nnp.random.seed(42)\nn_sims = 100000\n\n# Model 1: Normal distribution based on recent flows\nremaining_flows_normal = np.random.normal(mean_flow, std_flow, (n_sims, remaining_days))\ntotal_normal = cumulative_so_far + remaining_flows_normal.sum(axis=1)\nprob_normal = (total_normal >= 1000).mean()\n\n# Model 2: Bootstrap from observed April flows\nremaining_flows_boot = np.random.choice(april_flows_so_far, size=(n_sims, remaining_days), replace=True)\ntotal_boot = cumulative_so_far + remaining_flows_boot.sum(axis=1)\nprob_boot = (total_boot >= 1000).mean()\n\n# Model 3: Bootstrap from all recent flows (broader sample)\nremaining_flows_boot2 = np.random.choice(recent_daily_flows, size=(n_sims, remaining_days), replace=True)\ntotal_boot2 = cumulative_so_far + remaining_flows_boot2.sum(axis=1)\nprob_boot2 = (total_boot2 >= 1000).mean()\n\n# Model 4: Student-t for heavier tails\nfrom scipy import stats as sp_stats\ndf_t = 4  # heavy tails\nremaining_flows_t = sp_stats.t.rvs(df_t, loc=mean_flow, scale=std_flow*0.8, size=(n_sims, remaining_days))\ntotal_t = cumulative_so_far + remaining_flows_t.sum(axis=1)\nprob_t = (total_t >= 1000).mean()\n\nprint(\"P(April total >= $1B):\")\nprint(f\"  Normal model (recent):     {prob_normal:.3f}\")\nprint(f\"  Bootstrap (April only):    {prob_boot:.3f}\")\nprint(f\"  Bootstrap (recent flows):  {prob_boot2:.3f}\")\nprint(f\"  Student-t (heavy tails):   {prob_t:.3f}\")\nprint()\n\n# Summary statistics for the remaining flows\nfor name, totals in [(\"Normal\", total_normal), (\"Bootstrap-April\", total_boot), \n                       (\"Bootstrap-Recent\", total_boot2), (\"Student-t\", total_t)]:\n    pcts = np.percentile(totals, [10, 25, 50, 75, 90])\n    print(f\"{name}: P10={pcts[0]:.0f}, P25={pcts[1]:.0f}, P50={pcts[2]:.0f}, P75={pcts[3]:.0f}, P90={pcts[4]:.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Cumulative April flows through Apr 10: $652.2M\nRemaining to reach $1B: $347.8M\nRemaining trading days: 14\n\nRecent daily flows (late Mar + Apr):\n  Mean: $28.9M\n  Std
dev: $217.2M\n  Median: $7.8M\n  Min: $-225.5M, Max: $471.4M\n\nApril-only daily flows:\n  Mean: $93.2M\n  Std dev: $262.0M\n\nP(April total >= $1B):\n  Normal model (recent):     0.525\n  Bootstrap
(April only):    0.851\n  Bootstrap (recent flows):  0.516\n  Student-t (heavy tails):   0.525\n\nNormal: P10=12, P25=504, P50=1051, P75=1602, P90=2090\nBootstrap-April: P10=794, P25=1326, P50=1942,
P75=2568, P90=3134\nBootstrap-Recent: P10=68, P25=512, P50=1031, P75=1575, P90=2078\nStudent-t: P10=-85, P25=464, P50=1055, P75=1651, P90=2202\n", "stderr": "", "duration_ms": 1342}
```

```json
{
  "query": "Bitcoin price April 11 12 2026 market sentiment tariffs geopolitical"
}
```

### 📋 Result

```
{"query": "Bitcoin price April 11 12 2026 market sentiment tariffs geopolitical", "results": [{"title": "Latest Bitcoin News - (BTC) Future Outlook, Trends & Market Insights", "url":
"https://coinmarketcap.com/cmc-ai/bitcoin/latest-updates/", "snippet": "Deep Dive\n1. Bitcoin Core v31.0 Final Release (Q2 2026)\nOverview: Developers released Bitcoin Core v31.0rc4 for testing on 11
April 2026 ([U.Today](https://u.today/bitcoin-developers-release-major-update-on-testnet-what-changed)). The final version is expected soon. Key upgrades include a redesigned \"cluster mempool\" to
improve transaction selection and fee efficiency, and a new privacy rule requiring transactions to be broadcast only over Tor or I2P networks to hide users' IP addresses. It also", "api_data": null,
"hint": null}, {"title": "How War, Tariffs, And Oil Are Shaping The Bitcoin Price - And How To Predict What\u2019s Next", "url": "https://bitcoinmagazine.com/sponsored/how-war-tariffs-and-oil-are-
shaping-the-bitcoin-price-and-how-to-predict-whats-next", "snippet": "Bitcoin is trading around $70,000 today \u2013 down roughly 44% from the $126,000 all-time high it hit in October 2025. The
pullback hasn\u2019t been driven by any single catalyst. Instead, it\u2019s been a cascade: a U.S.-Israeli military operation in Iran, surging oil prices, an escalating global tariff war, and a
Federal Reserve stuck on pause. The question on every trader\u2019s mind isn\u2019t just \u201cwhy\u201d \u2013 it\u2019s \u201cwhat comes next?\u201d\nWar, Oil, and the Macro Storm\nOn February 28,
the U.S. and Israel launched joint strik", "api_data": null, "hint": null}, {"title": "Bitcoin Price Outlook 2026: Analysts Target $240K Amid Halving Cycle Signals", "url":
"https://www.ainvest.com/news/bitcoin-price-outlook-2026-analysts-target-240k-halving-cycle-signals-2604/", "snippet": "Bitcoin Price Outlook 2026: Analysts Target $240K Amid Halving Cycle
Signals\n[Ainvest Coin Buzz](https://www.ainvest.com/news/author/ainvest-coin-buzz/)Reviewed by\n[The Newsroom](https://www.ainvest.com/news/author/newsroom/)\n[BTC--
](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE)\n[STRK--](https://chart.ainvest.com/STRKUSDT/?exchange=BINANCE)\n[SOL--](https://chart.ainvest.com/SOLUSDT/?exchange=BINANCE)\n![Aime
Robot](https://cdn.ainvest.com/frontResources/s/nova-ainews/news/_next/static/medi", "api_data": null, "hint": null}, {"title": "BTC, ETH Prices: Impact of 2022-2026 Geopolitical Conflicts -
Crypto.com US", "url": "https://crypto.com/us/market-updates/btc-eth-prices-geopolitical-conflicts-history", "snippet": null, "api_data": null, "hint": null}, {"title": "Bitcoin Price Outlook 2026:
Expert Forecasts Amid Geopolitical Risks and Quantum Threats", "url": "https://www.devere-group.com/analysts-downgrade-bitcoin-price-target-amid-iran-war-turmoil/", "snippet": null, "api_data": null,
"hint": null}, {"title": "Bitcoin Price Today April 9, 2026: BTC Price Near USD 71,000 Level Amid Shifting Geopolitical Landscape | LatestLY", "url": "https://www.latestly.com/business/bitcoin-price-
today-april-9-2026-btc-price-near-usd-71000-level-amid-shifting-geopolitical-landscape-7385789.html", "snippet": "Bitcoin traded at USD 70,879 on Thursday morning, maintaining a key psychological
support level as the broader cryptocurrency market reacts to a shifting geopolitical landscape. The digital asset has seen renewed volatility following news of a ceasefire in the Middle East, which
has prompted a rotation back into risk-on assets and reignited discussions regarding year-end price targets.\nThe current price action represents a steady recovery from recent lows in early February,
though the asset rema", "api_data": null, "hint": null}, {"title": "It\u2019s been a weird few days on Wall Street | CNN Business", "url": "https://www.cnn.com/2026/02/02/investing/gold-silver-
bitcoin-us-stock-market", "snippet": "Wall Street traders are grappling with sharp swings in precious metals, bitcoin is hovering at its lowest level since April and there are lingering nerves about
technology stocks.\nIt\u2019s been a weird few days on Wall Street. Gold and silver, considered havens amid uncertainty, have experienced enormous volatility. A [ferocious
rally](https://www.cnn.com/2026/01/25/business/gold-record-trump-global-concerns-intl-hnk) in precious metals this year halted with a [painful drop](https://www.cnn.com/busi", "api_data": null,
"hint": null}, {"title": "Bitcoin Price Outlook Still 'Constructive' Despite Geopolitical 'Noise'", "url": "https://www.ainvest.com/news/bitcoin-price-outlook-constructive-geopolitical-noise-2601/",
"snippet": "Bitcoin Price Outlook Still 'Constructive' Despite Geopolitical 'Noise'\n[Nyra Feldon](https://www.ainvest.com/news/author/nyra-feldon/)Reviewed by\n[The
Newsroom](https://www.ainvest.com/news/author/newsroom/)\n[BTC--](https://chart.ainvest.com/BTCUSDT/?exchange=BINANCE)\n[ETH--](https://chart.ainvest.com/ETHUSDT/?exchange=BINANCE)\n![Aime
Robot](https://cdn.ainvest.com/frontResources/s/nova-ainews/news/_next/static/media/aimeRobot.ddb9bcda.png)\n\u0435\u0441\u044c\nBitcoin (BTC) experienced a pullback to around $92", "api_data": null,
"hint": null}, {"title": "Bitcoin Price Prediction 2026-2031: Is $73K Next After 4% Gain?", "url": "https://coindcx.com/blog/price-predictions/bitcoin-price-weekly/", "snippet": null, "api_data":
null, "hint": null}, {"title": "CoinDesk: Bitcoin, Ethereum, XRP, Crypto News and Price Data", "url": "https://www.coindesk.com", "snippet": "More Featured Stories\nAdvertisement\nMost Read\nBhutan
has sold 70% of its bitcoin in 18 months. It may have stopped BTC mining too.\nThe kingdom's holdings have dropped from 13,000 BTC to 3,954 since October 2024, with $215.7 million moved out this year
alone. Its last mining inflow over $100,000 was recorded more than a year ago.\nAdvertisement", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me also look at this from a different angle - using broader historical data\n# Monthly flows context:\n# Jan 2026: -$1,610M\n# Feb 2026: -$206.5M  \n# Mar 2026: +$1,320M\n# April so far (7 trading days): +$652.2M\n\n# The key question: with $652.2M already in, needing only $347.8M more over 14 days,\n# what's the probability of a total reversal?\n\n# For the remaining 14 days to cause a miss, the average daily flow would need to be\n# LESS than $24.8M/day. Given recent momentum, how likely is that?\n\n# Let's think about it in terms of: what fraction of the distribution of 14-day sums\n# falls below $347.8M?\n\n# Using the broader recent sample (late Mar + Apr), mean = $28.9M/day, std = $217.2M/day\n# 14-day sum: mean = 14 * 28.9 = 404.6M, std = sqrt(14) * 217.2 = 812.6M\nexpected_14day = 14 * 28.9\nstd_14day = np.sqrt(14) * 217.2\n\nfrom scipy import stats as sp_stats\n\n# P(14-day sum >= 347.8)\nz = (347.8 - expected_14day) / std_14day\np_exceed = 1 - sp_stats.norm.cdf(z)\nprint(f\"Analytical (normal, recent distribution): P(remaining >= $347.8M) = {p_exceed:.3f}\")\n\n# Using April-only distribution (more optimistic)\nexpected_14day_apr = 14 * 93.2\nstd_14day_apr = np.sqrt(14) * 262.0\nz_apr = (347.8 - expected_14day_apr) / std_14day_apr\np_exceed_apr = 1 - sp_stats.norm.cdf(z_apr)\nprint(f\"Analytical (normal, April-only): P(remaining >= $347.8M) = {p_exceed_apr:.3f}\")\n\nprint()\n# Key consideration: the distribution of daily flows is NOT normal - it has fat tails\n# and is bimodal (some big inflow days, some big outflow days)\n\n# Let's also consider: if we just need 1-2 good days like Apr 6 ($471.4M) or Apr 9 ($358.1M),\n# we'd already be past $1B even if most other days are flat/slightly negative\nprint(\"Scenario analysis:\")\nprint(f\"If remaining days average $0/day: Total = ${652.2:.0f}M -> {'NO' if 652.2 < 1000 else 'YES'}\")\nprint(f\"If remaining days average $25/day: Total = ${652.2 + 25*14:.0f}M -> {'NO' if 652.2 + 25*14 < 1000 else 'YES'}\")\nprint(f\"If remaining days average $50/day: Total = ${652.2 + 50*14:.0f}M -> {'NO' if 652.2 + 50*14 < 1000 else 'YES'}\")\nprint(f\"If remaining days average -$25/day: Total = ${652.2 - 25*14:.0f}M -> {'NO' if 652.2 - 25*14 < 1000 else 'YES'}\")\nprint(f\"If remaining days average -$50/day: Total = ${652.2 - 50*14:.0f}M -> {'NO' if 652.2 - 50*14 < 1000 else 'YES'}\")\n\nprint()\n# How many \"big inflow days\" ($200M+) would we need?\nprint(f\"With 2 days of $200M+ inflows and rest at $0: ${652.2 + 400:.0f}M -> YES\")\nprint(f\"With 1 day of $350M+ and rest at $0: ${652.2 + 350:.0f}M -> YES\")\nprint(f\"Need cumulative of $347.8M more over 14 days\")\n\nprint()\n# What if flows revert to late-March negative pattern?\n# Late March: -74.5, 7.8, -171.3, -225.5, 69.4, 117.5 -> avg = -46.1M/day\nlate_march = [-74.5, 7.8, -171.3, -225.5, 69.4, 117.5]\nlate_march_avg = np.mean(late_march)\nprint(f\"Late March average daily flow: ${late_march_avg:.1f}M\")\nprint(f\"If rest of April matches late March: Total = ${652.2 + late_march_avg * 14:.0f}M -> {'NO' if 652.2 + late_march_avg * 14 < 1000 else 'YES'}\")\n\n# What about April average so far?\napril_avg = np.mean([-173.7, 9.0, 471.4, -159.1, -93.9, 358.1, 240.4])\nprint(f\"April average daily flow: ${april_avg:.1f}M\")\nprint(f\"If rest of April matches April avg: Total = ${652.2 + april_avg * 14:.0f}M -> {'YES' if 652.2 + april_avg * 14 >= 1000 else 'NO'}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Analytical (normal, recent distribution): P(remaining >= $347.8M) = 0.528\nAnalytical (normal, April-only): P(remaining >= $347.8M) = 0.836\n\nScenario analysis:\nIf
remaining days average $0/day: Total = $652M -> NO\nIf remaining days average $25/day: Total = $1002M -> YES\nIf remaining days average $50/day: Total = $1352M -> YES\nIf remaining days average
-$25/day: Total = $302M -> NO\nIf remaining days average -$50/day: Total = $-48M -> NO\n\nWith 2 days of $200M+ inflows and rest at $0: $1052M -> YES\nWith 1 day of $350M+ and rest at $0: $1002M ->
YES\nNeed cumulative of $347.8M more over 14 days\n\nLate March average daily flow: $-46.1M\nIf rest of April matches late March: Total = $7M -> NO\nApril average daily flow: $93.2M\nIf rest of April
matches April avg: Total = $1957M -> YES\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me also look at the broader context of monthly Bitcoin ETF flows\n# to get a base rate for months exceeding $1B\n\n# Key monthly data points (from articles):\n# Positive months (2024-2026):\n# Jan 2024: ~$1.5B (launch excitement but GBTC outflows)\n# Feb 2024: ~$6B+\n# Mar 2024: ~$4.6B (ATH period) \n# Oct 2024: strong\n# Nov 2024: very strong\n# Dec 2024: mixed (late month selloff)\n# Jan 2025: (various)\n# Mar 2026: $1.32B (first positive month of 2026)\n\n# Negative months:\n# Nov 2025: outflows started\n# Dec 2025: outflows\n# Jan 2026: -$1.61B\n# Feb 2026: -$206.5M\n\n# From the data, months can swing dramatically.\n# The question is whether April 2026 is more like a continuation of March's recovery\n# or a reversal back to the Nov-Feb outflow trend.\n\n# Current sentiment indicators:\n# - Bitcoin at ~$70K, recovering from lows\n# - IBIT up 9.5% in 5 days, 7% in 10 days  \n# - March saw $1.32B inflows (strong positive momentum)\n# - April started negative but had big inflow days\n# - Geopolitical tensions (Iran/Hormuz) initially drove safe-haven flows INTO BTC\n\n# The threshold is $1B for the full month. We're at $652.2M with 14 days left.\n# The key insight: we just need $347.8M more, which is less than a SINGLE good day\n# (Apr 6 was $471.4M, Apr 9 was $358.1M)\n\n# Even one strong day would essentially clear the threshold.\n# The question is really: will we get at least one more strong inflow day\n# in the next 14 trading days?\n\n# Out of 7 April trading days so far:\n# - 2 days had inflows > $240M (471.4, 358.1, 240.4 - actually 3 days)\n# - 3 days had outflows (-173.7, -159.1, -93.9)\n# - 1 day was tiny positive (9.0)\n\n# So the probability of getting a $350M+ day is roughly 2/7 \u2248 29% per day\n# P(at least one $350M+ day in 14 days) = 1 - (1-2/7)^14\np_no_big_day = (1 - 2/7)**14\np_at_least_one = 1 - p_no_big_day\nprint(f\"P(at least one $350M+ day in next 14 days): {p_at_least_one:.4f}\")\n\n# But even without a single huge day, moderate inflows of $25M/day average would suffice\n# P(daily flow > $25M) from recent data\nfrom_recent = np.array([-74.5, 7.8, -171.3, -225.5, 69.4, 117.5, -173.7, 9.0, 471.4, -159.1, -93.9, 358.1, 240.4])\np_above_25 = np.mean(from_recent > 25)\nprint(f\"P(daily flow > $25M) from recent data: {p_above_25:.3f}\")\n\n# More robust: weighted average of models\n# Normal (broad): 0.528\n# Normal (April): 0.836\n# Bootstrap (April): 0.851\n# Bootstrap (recent): 0.516\n# Student-t: 0.525\n\n# The April-only models are more optimistic because April has had a positive mean\n# The broader models include the late-March negative period\n\n# I think the truth is somewhere in between, but leaning toward the more optimistic side because:\n# 1. Bitcoin is in a recovery trend (IBIT up 9.5% in 5 days)\n# 2. March showed institutional buying returning\n# 3. The $347.8M remaining is achievable in just 1-2 good days\n# 4. Recent momentum favors continued inflows\n\n# However, risks include:\n# 1. Geopolitical escalation could cause risk-off\n# 2. The late-March pattern showed significant outflows\n# 3. Daily flows are highly variable\n\n# My estimate: weight the models\n# Broad models average: ~0.52\n# April models: ~0.84\n# I'll weight 60% toward broad (conservative) and 40% toward April-specific\nweighted_prob = 0.6 * 0.525 + 0.4 * 0.843\nprint(f\"\\nWeighted probability estimate: {weighted_prob:.3f}\")\n\n# But I also need to adjust for the fact that:\n# 1. Current Bitcoin price trend is positive (tailwind for inflows)\n# 2. The question only needs $24.8M/day average, which is modest\n# 3. We already have 65% of the target banked\n\n# I think a probability around 0.60-0.65 is appropriate\nprint(\"\\nFinal assessment range: 0.55-0.70\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "P(at least one $350M+ day in next 14 days): 0.9910\nP(daily flow > $25M) from recent data: 0.385\n\nWeighted probability estimate: 0.652\n\nFinal assessment range:
0.55-0.70\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__markets__polymarket_price


## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "Bitcoin ETF inflows April 2026"
}
```

### 📋 Result

```
{"markets": [], "query": "Bitcoin ETF inflows April 2026"}
```

```json
{
  "query": "Bitcoin ETF inflows April billion"
}
```

### 📋 Result

```
{"markets": [], "query": "Bitcoin ETF inflows April billion"}
```

## 💬 Response

No prediction market coverage on this specific question. Let me now run the reflection.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Already $652.2M banked through 7 trading days (65% of target), needing only $347.8M more over 14 remaining days ($24.8M/day avg)",
      "logit": 1.5,
      "confidence": 0.95
    },
    {
      "description": "March 2026 saw $1.32B inflows - first positive month since Oct 2025, signaling institutional demand recovery",
      "logit": 0.8,
      "confidence": 0.8
    },
    {
      "description": "Bitcoin price recovering: IBIT up 9.5% in 5 days, BTC near $71K, positive momentum favors continued inflows",
      "logit": 0.7,
      "confidence": 0.7
    },
    {
      "description": "High daily flow variance (std ~$217-262M) means even one good day ($350M+) would clear threshold; P(at least one in 14 days) \u2248 99%",
      "logit": 1,
      "confidence": 0.6
    },
    {
      "description": "Geopolitical risks (US-Iran tensions, tariff war) create macro uncertainty that could trigger risk-off outflows",
      "logit": -0.8,
      "confidence": 0.6
    },
    {
      "description": "Late March showed consecutive outflow days (-74.5, -171.3, -225.5), demonstrating flows can turn sharply negative",
      "logit": -0.7,
      "confidence": 0.7
    },
    {
      "description": "Monte Carlo simulations across multiple models center probability at 52-85%, with broad models at ~53% and April-only at ~84%",
      "logit": 0.3,
      "confidence": 0.8
    },
    {
      "description": "Jan and Feb 2026 were negative months (-$1.61B and -$207M), showing full months of outflows are possible despite recovery",
      "logit": -0.5,
      "confidence": 0.5
    }
  ],
  "tentative_estimate": {
    "logit": 0.5,
    "probability": 0.62
  },
  "assessment": "The question asks whether April 2026 Bitcoin ETF flows will total at least $1B. Through 7 of ~21 trading days, $652.2M has already flowed in (65% of target). The remaining $347.8M needed over 14 days requires only $24.8M/day average - well below the April average of $93.2M/day.\n\nKey tension: The broad recent distribution (including late March) has a mean of only $28.9M/day, making this close to a coin flip analytically. But the April-specific mean ($93.2M/day) strongly favors YES. The correct weighting depends on whether April represents a new regime (recovery continuing from March's $1.32B) or will revert to the late-March negative pattern.\n\nArguments for YES: (1) 65% already banked; (2) just 1-2 strong inflow days would suffice; (3) Bitcoin is in an uptrend; (4) March institutional demand recovery appears sustained.\n\nArguments for NO: (1) Daily flows are extremely volatile; (2) 14 consecutive days of modest outflows (-$25M/day) would cause a miss; (3) geopolitical shocks could trigger risk-off; (4) Jan-Feb were heavily negative months showing prolonged outflows are possible.\n\nThe probability is NOT as high as 85% because the flow distribution has fat downside tails and regime shifts happen quickly. But it's above 50% because a significant buffer already exists and the required daily average is modest.",
  "calibration_notes": "Base rate: Of 2+ years of Bitcoin ETF history, roughly 60-65% of months have had net positive inflows exceeding $1B when the ETF market was established. But the recent period (Nov 2025 - Feb 2026) had 4 consecutive months of outflows, suggesting a different regime. March's rebound to $1.32B suggests recovery. The starting position of $652.2M already banked is the strongest factor - this shifts the question from 'will April be a strong month?' to 'will the remaining 14 days average slightly positive?'",
  "key_uncertainties": "1. Whether the March/early-April recovery in institutional demand is sustainable or a temporary bounce. 2. Impact of geopolitical events (Iran tensions, tariff escalation) on crypto sentiment. 3. Bitcoin price trajectory - if BTC drops significantly, outflows would likely accelerate. 4. Whether April 11 (today, a Friday) had significant flows not yet reported.",
  "update_triggers": "- A single day of $350M+ outflows would significantly reduce probability. - Bitcoin dropping below $65K would suggest risk-off and lower probability. - Continued positive daily flows of $100M+ for 2-3 more days would push probability above 75%.",
  "tool_audit": "Farside resolution source: Successfully fetched, provided exact daily flow data. Stock price (IBIT): Good context on price trend and volatility. Web search: Found key contextual articles on monthly flow patterns and market conditions. Exa search: Good historical flow context from blocklr article. Prediction markets: No matching markets found (Polymarket, Manifold). AskNews: Hit rate limit, couldn't get breaking news (minor gap). Monte Carlo simulation: Successfully run with multiple models.",
  "process_reflection": "The tools worked well overall. Fetching the Farside resolution source directly was the most valuable step - it gave exact data. The AskNews rate limit was a minor frustration but web search compensated. The Monte Carlo simulation was crucial for framing this as a threshold-crossing problem rather than a narrative YES/NO debate. The main challenge was choosing the right sample period for the flow distribution - the answer is quite sensitive to whether you use April-only data (optimistic) or broader recent data (neutral)."
}
```

### 📋 Result

```
{"factor_count": 8, "factor_sum": 2.175, "tentative_logit": 0.5, "logit_gap": -1.6749999999999998, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Already $652.2M banked through 7
trading days (65% of target), needing only $347.8M more over 14 remaining days ($24.8M/day avg)", "logit": 1.5, "confidence": 0.95, "effective_logit": 1.4249999999999998}, {"description": "March 2026
saw $1.32B inflows - first positive month since Oct 2025, signaling institutional demand recovery", "logit": 0.8, "confidence": 0.8, "effective_logit": 0.6400000000000001}, {"description": "Bitcoin
price recovering: IBIT up 9.5% in 5 days, BTC near $71K, positive momentum favors continued inflows", "logit": 0.7, "confidence": 0.7, "effective_logit": 0.48999999999999994}, {"description": "High
daily flow variance (std ~$217-262M) means even one good day ($350M+) would clear threshold; P(at least one in 14 days) \u2248 99%", "logit": 1.0, "confidence": 0.6, "effective_logit": 0.6},
{"description": "Geopolitical risks (US-Iran tensions, tariff war) create macro uncertainty that could trigger risk-off outflows", "logit": -0.8, "confidence": 0.6, "effective_logit": -0.48},
{"description": "Late March showed consecutive outflow days (-74.5, -171.3, -225.5), demonstrating flows can turn sharply negative", "logit": -0.7, "confidence": 0.7, "effective_logit":
-0.48999999999999994}, {"description": "Monte Carlo simulations across multiple models center probability at 52-85%, with broad models at ~53% and April-only at ~84%", "logit": 0.3, "confidence": 0.8,
"effective_logit": 0.24}, {"description": "Jan and Feb 2026 were negative months (-$1.61B and -$207M), showing full months of outflows are possible despite recovery", "logit": -0.5, "confidence": 0.5,
"effective_logit": -0.25}], "dominant_factor": "Already $652.2M banked through 7 trading days (65% of target), needing only $347.8M more over 14 remaining days ($24.8M/day avg)",
"dominant_effective_logit": 1.4249999999999998, "factor_implied_probability": 0.8979819308108695, "tentative_probability": 0.62, "gap_pp": -27.798193081086954, "sources": ["[(Metaculus) Will U.S. spot
Bitcoin ETFs take in at least $1 billion of net inflows during April 2026?](https://www.metaculus.com/questions/43135)", "[Farside Investors](https://farside.co.uk/bitcoin-etf-flow-all-data/)",
"[(yfinance) IBIT](https://finance.yahoo.com/quote/IBIT)", "[Farside Investors](https://farside.co.uk/btc/)"], "reviewer_critique": "## Evidence Verification\n\n**Factor 1: $652.2M banked through 7
trading days (65% of target), needing $347.8M more over 14 days ($24.8M/day avg)**\n- VERIFIED: Trace shows Farside data fetched (Apr 1-10: -173.7, 9.0, 471.4, -159.1, -93.9, 358.1, 240.4 = $652.2M).
Code output confirms: \"Cumulative April flows through Apr 10: $652.2M, Remaining to reach $1B: $347.8M, Remaining trading days: 14, Average daily flow needed: $24.8M per day\"\n\n**Factor 2: March
2026 saw $1.32B inflows - first positive month since Oct 2025**\n- VERIFIED: TradingView article in trace: \"Bitcoin ETFs hit $1.32 billion in March inflow... The fresh capital collectively achieved
in March has come after January recorded $1.61 billion in outflows and February saw another $206.52 million exit. The long monthly outflow streak started in November 2025\"\n\n**Factor 3: Bitcoin
price recovering: IBIT up 9.5% in 5 days, BTC near $71K**\n- VERIFIED: Trace shows stock data with \"trailing_returns\": {\"five_day\": 9.45483276270741}. BTC at $70,879 confirmed by LatestLY article:
\"Bitcoin traded at USD 70,879 on Thursday morning\"\n\n**Factor 4: High daily flow variance (std ~$217-262M), P(at least one $350M+ day in 14 days) \u2248 99%**\n- VERIFIED: Monte Carlo output in
trace: \"Std dev: $217.2M\" for recent flows, \"$262.0M\" for April-only. Code output shows \"P(at least one $350M+ day in next 14 days): 0.9910\"\n\n**Factor 5: Geopolitical risks (US-Iran tensions,
tariff war)**\n- VERIFIED: Multiple trace references to \"U.S.-Iran standoff concerning the Strait of Hormuz\", \"escalating global tariff war\", and Bitcoin Magazine article discussing
war/tariffs/oil\n\n**Factor 6: Late March showed consecutive outflow days (-74.5, -171.3, -225.5)**\n- VERIFIED: Farside data in trace shows March 24: -74.5, March 26: -171.3, March 27: -225.5. Note:
These weren't fully consecutive (Mar 25 was +7.8), but the pattern of sharp negative days is accurate.\n\n**Factor 7: Monte Carlo simulations center probability at 52-85%**\n- VERIFIED: Trace output
shows \"Normal model (recent): 0.525, Bootstrap (April only): 0.851, Bootstrap (recent flows): 0.516, Student-t (heavy tails): 0.525\"\n\n**Factor 8: Jan and Feb 2026 were negative months (-$1.61B and
-$207M)**\n- VERIFIED: TradingView/U.Today article: \"January recorded $1.61 billion in outflows and February saw another $206.52 million exit\"\n\n## Resolution Criteria Check\n- Resolution criteria
clearly stated: sum of Farside \"Total\" values from 2026-04-01 through 2026-04-30 \u2265 $1,000.0M\n- Agent correctly used Farside as resolution source and explicitly noted discrepancies with other
sources (e.g., \"Since Farside is my resolution source, I'll use their 240.4 figure despite the discrepancy\")\n\n## Double-Counting Check\n- No significant double-counting detected. Factors cover
distinct aspects: current progress (F1), historical context (F2, F8), price momentum (F3), statistical properties (F4, F7), risks (F5, F6).\n\n## Wrong-Direction Check\n- All factor signs are
consistent with their descriptions.\n\n## Adversarial Reasoning Check\n- Assessment explicitly addresses both sides: Arguments for YES (65% banked, 1-2 strong days would suffice, uptrend, March
recovery) and Arguments for NO (high volatility, 14 consecutive outflow days could cause miss, geopolitical shocks, Jan-Feb negative months). This is adequate.\n\n## Probability Assessment\n- Agent's
62% sits reasonably within the Monte Carlo range (52-85%) and matches the \"weighted probability estimate: 0.652\" from code output\n- The agent correctly weights the tension between broad recent
distribution (~53%) and April-only distribution (~84%)\n- 62% represents a reasonable blend given: (1) strong April start, (2) high variance means one good day clears threshold, (3) but regime shifts
happen quickly and late March was very negative\n- My independent estimate would be in the 58-68% range, so 62% is well within bounds\n\n## No Issues Found\nAll factual claims are grounded in the
research trace. The probability estimate is well-supported by the Monte Carlo analysis and appropriately positioned between the pessimistic (broad distribution) and optimistic (April-only)
scenarios."}
```

## 💬 Response

The reflection passed with all factors verified. Let me finalize my forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "Through April 10, U.S. spot Bitcoin ETFs have accumulated $652.2M in net inflows (65% of the $1B target), per Farside data. Only $347.8M more is needed over 14 remaining trading days ($24.8M/day average). Monte Carlo simulations across multiple distributional assumptions yield 52-85% probability of crossing $1B. The broad recent distribution (including negative late-March days) gives ~53%, while April-only data gives ~84%. Key positive factors: 65% already banked, just 1-2 strong days would suffice, Bitcoin recovering (+9.5% in 5 days), March saw $1.32B inflows. Key risks: extreme daily variance (std $217-262M), geopolitical uncertainty (Iran/tariffs), and the Nov 2025-Feb 2026 outflow streak showing sustained negative periods are possible. I weight the evidence at 62% probability, reflecting genuine uncertainty about whether the recovery regime persists or a shock causes reversal.",
  "logit": 0.5,
  "probability": 0.62,
  "factors": [
    {
      "description": "Already $652.2M banked through 7 trading days (65% of target), needing only $347.8M more over 14 remaining days ($24.8M/day avg)",
      "logit": 1.5,
      "confidence": 0.95
    },
    {
      "description": "March 2026 saw $1.32B inflows - first positive month since Oct 2025, signaling institutional demand recovery",
      "logit": 0.8,
      "confidence": 0.8
    },
    {
      "description": "Bitcoin price recovering: IBIT up 9.5% in 5 days, BTC near $71K, positive momentum favors continued inflows",
      "logit": 0.7,
      "confidence": 0.7
    },
    {
      "description": "High daily flow variance (std ~$217-262M) means even one good day ($350M+) would clear threshold; P(at least one in 14 days) \u2248 99%",
      "logit": 1,
      "confidence": 0.6
    },
    {
      "description": "Geopolitical risks (US-Iran tensions, tariff war) create macro uncertainty that could trigger risk-off outflows",
      "logit": -0.8,
      "confidence": 0.6
    },
    {
      "description": "Late March showed consecutive outflow days (-74.5, -171.3, -225.5), demonstrating flows can turn sharply negative",
      "logit": -0.7,
      "confidence": 0.7
    },
    {
      "description": "Monte Carlo simulations across multiple models center probability at 52-85%, with broad models at ~53% and April-only at ~84%",
      "logit": 0.3,
      "confidence": 0.8
    },
    {
      "description": "Jan and Feb 2026 were negative months (-$1.61B and -$207M), showing full months of outflows are possible despite recovery",
      "logit": -0.5,
      "confidence": 0.5
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**Forecast: 0.62 (62% probability YES)**

**Key findings:**

- **Current status:** $652.2M already accumulated through April 10 (7 trading days), per Farside resolution source. That's 65% of the $1B target.
- **Remaining gap:** Only $347.8M needed over 14 remaining trading days — an average of just $24.8M/day, well below April's current average of $93.2M/day.
- **One big day suffices:** April already had three days above $240M (471.4, 358.1, 240.4). A single $350M+ day would essentially clear the threshold.
- **Recovery momentum:** March 2026 was the first positive month ($1.32B) after four consecutive outflow months (Nov 2025–Feb 2026). Bitcoin is near $71K with IBIT up 9.5% in 5 days.

**Why not higher than 62%:**
- Daily flows are extremely volatile (std $217-262M) and can flip negative quickly
- Late March had three severe outflow days showing rapid reversals happen
- The broader recent distribution (including late March) puts the Monte Carlo probability at only ~53%
- Geopolitical tail risks (Iran tensions, tariff escalation) could trigger sustained risk-off flows
- Jan 2026 (-$1.61B) showed an entire month of outflows is feasible even in a broadly positive market
