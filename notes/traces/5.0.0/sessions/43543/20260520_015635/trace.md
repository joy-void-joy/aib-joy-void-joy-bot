# Reasoning Log: How many companies will be listed as May 2026 IPOs on Stock Analysis's IPO Statistics page?

*Generated: 2026-05-20T02:10:51.951507+00:00*


## 💭 Thinking

Let me analyze this question about the number of companies listed as May 2026 IPOs on Stock Analysis's IPO Statistics page.

Key information from the question:
- Resolution source: Stock Analysis IPO Statistics page (https://stockanalysis.com/ipos/statistics/)
- Deadline: May 31, 2026 (or next day page is updated)
- Includes SPACs, direct listings, smaller exchange listings
- 2025 monthly range: 18-37, with May 2025 = 33
- 2024 monthly range: 12-34, with May 2024 = 14


- Renaissance Capital is reporting 13 IPOs priced in May 2026 as of mid-May, and Stock Analysis typically shows 2-3x higher counts than Renaissance Capital, so I'd expect somewhere in the 26-39 range based on that multiplier.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43543
  ]
}
```

### 📋 Result

```
{"post_id": 43543, "title": "How many companies will be listed as May 2026 IPOs on Stock Analysis's IPO Statistics page?", "type": "numeric", "url": "https://www.metaculus.com/questions/43543",
"background_info": "After a sluggish 2025 in some segments, the U.S. IPO market has shown mixed activity in 2026. According to [Stock Analysis's IPO Statistics
page](https://stockanalysis.com/ipos/statistics/), which counts all U.S. IPO listings (including traditional IPOs, SPACs, and smaller listings on Nasdaq, NYSE, and NYSE American), monthly IPO counts
for 2025 ranged from 18 to 37, with May 2025 recording 33 IPOs. For 2024, monthly counts ranged from 12 to 34, with May 2024 recording 14 IPOs.\n\n2026 monthly figures on Stock Analysis so far (as of
mid-May 2026) have been broadly in line with 2024-2025 ranges. Notable recent debuts referenced in market commentary include Cerberus (CBRS), Blackstone Digital Infrastructure Trust (BXDC), and Fervo
Energy (FRVO).\n\nSeparately, [Renaissance Capital](https://www.renaissancecapital.com/IPO-Center/Stats), which counts only traditional operating-company IPOs above a size threshold and excludes most
SPACs and micro-listings, reports 13 IPOs priced in May 2026 as of May 17, 2026. Stock Analysis's broader methodology typically yields counts roughly 2-3x higher than Renaissance
Capital's.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves as
the number reported for \"May\" 2026 in the \"2026 IPOs by Month\" section of the Stock Analysis IPO Statistics page at https://stockanalysis.com/ipos/statistics/, as observed on May 31, 2026 (or the
next day the page is updated if not yet refreshed on May 31). For example, if the page shows \"May: 27\", the question resolves as 27. If Stock Analysis's IPO Statistics page is unavailable or has not
been updated with a May 2026 figure by June 5, 2026, the resolution will use the count of IPOs with an IPO date in May 2026 appearing on https://stockanalysis.com/ipos/ filtered to that month, or, if
that is also unavailable, the count reported by [credible sources](https://www.metaculus.com/faq/#definitions) citing Stock Analysis data for May 2026.", "fine_print": "Stock Analysis's methodology
includes SPACs, direct listings, and smaller exchange listings (Nasdaq, NYSE, NYSE American). The figure used is whatever Stock Analysis publishes for May 2026 in its monthly breakdown; this question
does not adjust for inclusion/exclusion of any particular listing type. Any later upward or downward revisions made by Stock Analysis after June 5, 2026 will not change the resolution.",
"num_forecasters": 5, "community_prediction": null, "lower_bound": 0.0, "upper_bound": 80.0}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://stockanalysis.com/ipos/statistics/",
  "prompt": "What are the monthly IPO counts for 2026 and 2025? Look for the \"2026 IPOs by Month\" and \"2025 IPOs by Month\" sections. What is the May 2026 count if available?"
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/statistics/", "content": "Based on the provided content, **no monthly IPO data for 2026 is available**. The text mentions annual data from 2000-2026 and monthly
data since 2019, but does not include a \"2026 IPOs by Month\" section or any May 2026 count.\n\n**2025 Monthly IPO Counts:**\n- July: 37 (most)\n- November: 18 (least)\n- Total for 2025: 347
IPOs\n\nThe content does not provide a complete month-by-month breakdown for 2025, only highlighting the highest and lowest months.\n\n**Relevant links:**\n- [View all 2025
IPOs](https://stockanalysis.com/ipos/2025/)\n- [View all 2024 IPOs](https://stockanalysis.com/ipos/2024/)\n- [View all 2023 IPOs](https://stockanalysis.com/ipos/2023/)\n- [View all 2022
IPOs](https://stockanalysis.com/ipos/2022/)\n- [View all 2021 IPOs](https://stockanalysis.com/ipos/2021/)\n- [View all 2020 IPOs](https://stockanalysis.com/ipos/2020/)\n- [View all 2019
IPOs](https://stockanalysis.com/ipos/2019/)", "title": "IPO Statistics and Charts"}
```

```json
{
  "url": "https://stockanalysis.com/ipos/",
  "prompt": "How many IPOs are listed for May 2026? Look for all IPOs with dates in May 2026. Count them and list the dates."
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/", "content": "Based on the content, there are **26 IPOs listed for May 2026**.\n\nHere are the dates and counts:\n- May 19, 2026: 1 IPO\n- May 15, 2026: 5
IPOs\n- May 14, 2026: 5 IPOs\n- May 13, 2026: 3 IPOs\n- May 8, 2026: 3 IPOs\n- May 7, 2026: 3 IPOs\n- May 6, 2026: 2 IPOs\n- May 1, 2026: 4 IPOs\n\n**Relevant links:**\n- [AMAN - Amanat Acquisition
Corp](/stocks/aman/)\n- [EXYN - Exyn Technologies, Inc.](/stocks/exyn/)\n- [GUAC - Berto Acquisition Corp. II](/stocks/guac/)\n- [IDAC - Iron Dome Acquisition I Corp.](/stocks/idac/)\n- [PTAC -
Patriot Acquisition Corp.](/stocks/ptac/)\n- [VIDA - VIDA Global Inc.](/stocks/vida/)\n- [BXDC - Blackstone Digital Infrastructure Trust Inc.](/stocks/bxdc/)\n- [CBRS - Cerebras Systems
Inc.](/stocks/cbrs/)\n- [EROK - EagleRock Land, LLC](/stocks/erok/)\n- [GSRV - GSR V Acquisition Corp.](/stocks/gsrv/)\n- [MWC - Micware Co., Ltd.](/stocks/mwc/)\n- [BREZ - Breeze Acquisition Corp.
II](/stocks/brez/)\n- [FRVO - Fervo Energy Company](/stocks/frvo/)\n- [GMRS - GMR Solutions Inc.](/stocks/gmrs/)\n- [MOBI - Mobia Medical, Inc.](/stocks/mobi/)\n- [ODTX - Odyssey Therapeutics,
Inc.](/stocks/odtx/)\n- [OTAI - Starlink AI Acquisition Corporation](/stocks/otai/)\n- [HAWK - HawkEye 360, Inc.](/stocks/hawk/)\n- [SAGU - Shreya Acquisition Group](/stocks/sagu/)\n- [SUJA - Suja
Life, Inc.](/stocks/suja/)\n- [REA - Rare Earths Americas, Inc.](/stocks/rea/)\n- [VECA - Vernal Capital Acquisition Corp.](/stocks/veca/)\n- [COAG - Hemab Therapeutics Holdings,
Inc.](/stocks/coag/)\n- [MTNE - CH4 Natural Solutions Corporation](/stocks/mtne/)\n- [QLEP - Quantum Leap Acquisition Corp](/stocks/qlep/)\n- [SPTX - Seaport Therapeutics, Inc.](/stocks/sptx/)",
"title": "200 Most Recent IPOs"}
```

## 💬 Response

Excellent - I have solid data. Let me now get the 2025 and 2024 monthly data for comparison, and check the 2026 monthly data so far.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://stockanalysis.com/ipos/2025/",
  "prompt": "How many IPOs were there in each month of 2025? Count the IPOs by month (January through December). Also what was the total?"
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/2025/", "content": "Based on the provided data, here are the IPO counts by month for 2025:\n\n- **January**: 21 IPOs\n- **February**: 19 IPOs\n- **March**: 12
IPOs\n- **April**: 15 IPOs\n- **May**: 22 IPOs\n- **June**: 17 IPOs\n- **July**: 20 IPOs\n- **August**: 18 IPOs\n- **September**: 15 IPOs\n- **October**: 12 IPOs\n- **November**: 9 IPOs\n-
**December**: 30 IPOs\n\n**Total: 210 IPOs in 2025**\n\nRelevant links:\n- [SCPQ](/stocks/scpq/)\n- [SVAQ](/stocks/svaq/)\n- [BEBE](/stocks/bebe/)\n- [ANDG](/stocks/andg/)\n- [MDLN](/stocks/mdln/)\n-
[WLTH](/stocks/wlth/)\n- [CDNL](/stocks/cdnl/)\n- [All other individual stock links are available in the original content]", "title": "All 2025 IPOs - A Complete List"}
```

```json
{
  "url": "https://stockanalysis.com/ipos/2026/",
  "prompt": "How many IPOs are listed for each month of 2026? Count by month. What is the current count for May 2026?"
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/2026/", "content": "Based on the content, here are the IPO counts by month for 2026:\n\n- **January 2026**: 29 IPOs\n- **February 2026**: 29 IPOs\n- **March
2026**: 13 IPOs\n- **April 2026**: 20 IPOs\n- **May 2026**: 25 IPOs (current count as of May 19, 2026)\n\n**Current count for May 2026: 25 IPOs**\n\nRelevant links:\n- [AMAN - Amanat Acquisition
Corp](/stocks/aman/)\n- [EXYN - Exyn Technologies, Inc.](/stocks/exyn/)\n- [GUAC - Berto Acquisition Corp. II](/stocks/guac/)\n- [IDAC - Iron Dome Acquisition I Corp.](/stocks/idac/)\n- [PTAC -
Patriot Acquisition Corp.](/stocks/ptac/)\n- [VIDA - VIDA Global Inc.](/stocks/vida/)\n- [BXDC - Blackstone Digital Infrastructure Trust Inc.](/stocks/bxdc/)\n- [CBRS - Cerebras Systems
Inc.](/stocks/cbrs/)\n- [EROK - EagleRock Land, LLC](/stocks/erok/)\n- [GSRV - GSR V Acquisition Corp.](/stocks/gsrv/)\n- [MWC - Micware Co., Ltd.](/stocks/mwc/)\n- [BREZ - Breeze Acquisition Corp.
II](/stocks/brez/)\n- [FRVO - Fervo Energy Company](/stocks/frvo/)\n- [GMRS - GMR Solutions Inc.](/stocks/gmrs/)\n- [MOBI - Mobia Medical, Inc.](/stocks/mobi/)\n- [ODTX - Odyssey Therapeutics,
Inc.](/stocks/odtx/)\n- [OTAI - Starlink AI Acquisition Corporation](/stocks/otai/)\n- [HAWK - HawkEye 360, Inc.](/stocks/hawk/)\n- [SAGU - Shreya Acquisition Group](/stocks/sagu/)\n- [SUJA - Suja
Life, Inc.](/stocks/suja/)\n- [REA - Rare Earths Americas, Inc.](/stocks/rea/)\n- [VECA - Vernal Capital Acquisition Corp.](/stocks/veca/)\n- [COAG - Hemab Therapeutics Holdings,
Inc.](/stocks/coag/)\n- [MTNE - CH4 Natural Solutions Corporation](/stocks/mtne/)\n- [QLEP - Quantum Leap Acquisition Corp](/stocks/qlep/)\n- [SPTX - Seaport Therapeutics, Inc.](/stocks/sptx/)",
"title": "All 2026 IPOs (so far)"}
```

```json
{
  "url": "https://stockanalysis.com/ipos/2024/",
  "prompt": "How many IPOs were there in each month of 2024? Count the IPOs by month. What was May 2024's count?"
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/2024/", "content": "Based on the data provided, here are the monthly IPO counts for 2024:\n\n- **January**: 15 IPOs\n- **February**: 13 IPOs\n- **March**: 10
IPOs\n- **April**: 15 IPOs\n- **May**: 11 IPOs\n- **June**: 13 IPOs\n- **July**: 13 IPOs\n- **August**: 11 IPOs\n- **September**: 13 IPOs\n- **October**: 24 IPOs\n- **November**: 13 IPOs\n-
**December**: 15 IPOs\n\n**May 2024's count: 11 IPOs**\n\nRelevant links:\n- Individual stock pages are referenced throughout (e.g., [LOAR](/stocks/loar/), [VIK](/stocks/vik/), [ZK](/stocks/zk/),
etc.) but these appear to be relative paths on stockanalysis.com", "title": "All 2024 IPOs - A Complete List"}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "upcoming IPOs May 2026 week of May 19 20 21 22 23"
}
```

### 📋 Result

```
{"query": "upcoming IPOs May 2026 week of May 19 20 21 22 23", "results": [{"title": "Upcoming & Recent IPO's - IPOs Calendar - Yahoo Finance", "url": "https://finance.yahoo.com/calendar/ipo/",
"snippet": null, "api_data": null, "hint": null}, {"title": "Upcoming IPOs and Recent IPOs | IPO Calendar - Investing.com", "url": "https://www.investing.com/ipo-calendar/", "snippet":
"www.investing.com\nPerforming security verification\nThis website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.\nThis
website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.", "api_data": null, "hint": null}, {"title": "All 2026 IPOs (so
far)", "url": "https://stockanalysis.com/ipos/2026/", "snippet": "| May 19, 2026 | [AMAN](/stocks/aman/) | Amanat Acquisition Corp | $10.00 | $10.01 | - |\n| May 15, 2026 | [EXYN](/stocks/exyn/) |
Exyn Technologies, Inc. | - | $4.76 | - |\n| May 15, 2026 | [GUAC](/stocks/guac/) | Berto Acquisition Corp. II | $10.00 | $10.00 | 0.05% |\n| May 15, 2026 | [IDAC](/stocks/idac/) | Iron Dome
Acquisition I Corp. | $10.00 | $10.01 | 0.05% |\n| May 15, 2026 | [PTAC](/stocks/ptac/) | Patriot Acquisition Corp. | $10.00 | $9.96 | -0.45% |\n| May 15, 2026 | [VIDA](/stocks/vida/)", "api_data":
null, "hint": null}, {"title": "Upcoming IPOs in 2026: SpaceX, OpenAI, Anthropic + 9 More", "url": "https://dealroom.net/blog/upcoming-recent-ipos", "snippet": "The 12 most-watched upcoming IPOs of
2026 represent $3.12 trillion in combined estimated value, led by SpaceX ($1.5T), OpenAI ($1.0T), Anthropic ($300B), Databricks ($134B), and Revolut ($75B). AI and AI-adjacent companies account for 8
of the 12 deals in the pipeline, roughly 92% of the combined valuation, making 2026 the most AI-concentrated IPO year on record.\nThis page tracks every upcoming IPO with its targeted listing window,
expected valuation, lead underwriters, and sector, alongside a r", "api_data": null, "hint": null}, {"title": "IPO Listings | Nasdaq", "url": "https://www.nasdaq.com/market-activity/ipos", "snippet":
null, "api_data": null, "hint": null}, {"title": "8 Best Upcoming IPOs in 2026 | Investing - U.S. News Money", "url": "https://money.usnews.com/investing/articles/new-and-upcoming-ipos-in-2026",
"snippet": null, "api_data": null, "hint": null}, {"title": "IPO Calendar - Upcoming IPOs", "url": "https://stockanalysis.com/ipos/calendar/", "snippet": "Sources: Most data is sourced from the S-1
filings that companies submit to the U.S.\nSecurities and Exchange Commission (SEC). IPO dates are sourced from SEC filings, press releases, roadshow presentations,\nNASDAQ, NYSE and others. IPO dates
are estimated and may change, and in some cases companies postpone or withdraw their\nplans.", "api_data": null, "hint": null}, {"title": "2026 IPO Calendar | Upcoming Initial Public Offerings",
"url": "https://www.marketbeat.com/ipos/", "snippet": "IPOs can be quite complicated. There is a lot of important information to keep track of for each IPO. It can also be difficult trying to stay
informed of all the upcoming hot IPOs. This calendar makes tracking upcoming IPOs and understanding the relevant information incredibly simple. If you\u2019re new to the stock market and wondering,
\u201c[What is a dividend yield?](https://www.marketbeat.com/financial-terms/what-is-dividend-yield/)\u201d, you may not understand all the information provided, but once you ", "api_data": null,
"hint": null}, {"title": "Forge - Tech IPO Calendar for 2026", "url": "https://forgeglobal.com/tech-ipo-calendar-2026/", "snippet": null, "api_data": null, "hint": null}, {"title": "IPO Calendar:
Upcoming IPOs & IPO Offerings Calendar", "url": "https://www.renaissancecapital.com/IPO-Center/Calendar", "snippet": "The IPO ETF has almost NO Overlap with the S&P 500\nThe IPO ETF only contains New
Stocks\n| Ticker | Company | Ticker | Shares (M) | Price Range | Deal Size ($M) | Underwriters | |\n|---|---|---|---|---|---|---|---|\n|\n|\n| Company | Ticker | Deal Size ($M)
|\n|---|---|---|\n|\n|\n| Company | Ticker | Deal Size ($M) |\n|---|---|---|\n|\n|\nNavigating the IPO market is complex. IPO Pro makes it simple.\nWith calendars, dashboards, custom alerts, deal
lists, screening tools, filing data, and analyst insights, I", "api_data": null, "hint": null}]}
```

```json
{
  "query": "IPO calendar May 2026 last two weeks"
}
```

### 📋 Result

```
{"query": "IPO calendar May 2026 last two weeks", "results": [{"title": "Upcoming IPOs and Recent IPOs | IPO Calendar - Investing.com", "url": "https://www.investing.com/ipo-calendar/", "snippet":
"www.investing.com\nPerforming security verification\nThis website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.\nThis
website uses a security service to protect against malicious bots. This page is displayed while the website verifies you are not a bot.", "api_data": null, "hint": null}, {"title": "Upcoming & Recent
IPO's - IPOs Calendar - Yahoo Finance", "url": "https://finance.yahoo.com/calendar/ipo/", "snippet": null, "api_data": null, "hint": null}, {"title": "IPO Calendar | IPOScoop", "url":
"https://www.iposcoop.com/ipo-calendar/", "snippet": "[Amanat Acquisition (Stock-Only)](https://www.iposcoop.com/ipo/amanat-acquisition-stock-only/) |\n[AMAN](http://finance.yahoo.com/q?s=AMAN)
|\nLeerink Partners |\n7.5 |\n10.00 |\n10.00 |\n$ 75.0 mil |\n5/19/2026 Priced |\n[S/O](https://www.iposcoop.com/how-to-subscribe) |\n[S/O](https://www.iposcoop.com/how-to-subscribe) |\n[Lincoln
International](https://www.iposcoop.com/ipo/lincoln-international/) |\n[LCLN](http://finance.yahoo.com/q?s=LCLN) |\nGoldman Sachs/Morgan Stanley/BMO Capital Markets/Citizens Cap", "api_data": null,
"hint": null}, {"title": "IPO Calendar", "url": "https://www.nasdaq.com/market-activity/ipos", "snippet": null, "api_data": null, "hint": null}, {"title": "IPO Calendar - Upcoming IPOs", "url":
"https://stockanalysis.com/ipos/calendar/", "snippet": "Sources: Most data is sourced from the S-1 filings that companies submit to the U.S.\nSecurities and Exchange Commission (SEC). IPO dates are
sourced from SEC filings, press releases, roadshow presentations,\nNASDAQ, NYSE and others. IPO dates are estimated and may change, and in some cases companies postpone or withdraw their\nplans.",
"api_data": null, "hint": null}, {"title": "Upcoming IPO Calendar 2026 - Renaissance Capital", "url": "https://www.renaissancecapital.com/IPO-Center/Calendar", "snippet": "The IPO ETF has almost NO
Overlap with the S&P 500\nThe IPO ETF only contains New Stocks\n| Ticker | Company | Ticker | Shares (M) | Price Range | Deal Size ($M) | Underwriters | |\n|---|---|---|---|---|---|---|---|\n|\n|\n|
Company | Ticker | Deal Size ($M) |\n|---|---|---|\n|\n|\n| Company | Ticker | Deal Size ($M) |\n|---|---|---|\n|\n|\nNavigating the IPO market is complex. IPO Pro makes it simple.\nWith calendars,
dashboards, custom alerts, deal lists, screening tools, filing data, and analyst insights, I", "api_data": null, "hint": null}, {"title": "Forge - Tech IPO Calendar for 2026", "url":
"https://forgeglobal.com/tech-ipo-calendar-2026/", "snippet": null, "api_data": null, "hint": null}, {"title": "Upcoming IPO in May 2026 Calendar \u2013 Key Listings Details - IPO Watch", "url":
"https://ipowatch.in/ipo-calendar-may-2026/", "snippet": "Below is a list of [upcoming IPOs](https://ipowatch.in/upcoming-ipo-list/), along with their tentative dates and other key details to help you
stay informed.\n| Company IPO | Opening date | Closing Date | Type of IPO | IPO size | Price Band |\n|\n[Value 360 Communications](https://ipowatch.in/value-360-communications-ipo/)[Bagmane
REIT](https://ipowatch.in/bagmane-reit-ipo/)[Recode Studios](https://ipowatch.in/recode-studios-ipo-date-review-price-allotment-details/)[Simca Advertising](https://ipowa", "api_data": null, "hint":
null}, {"title": "2026 IPO Calendar | Upcoming Initial Public Offerings", "url": "https://www.marketbeat.com/ipos/", "snippet": "IPOs can be quite complicated. There is a lot of important information
to keep track of for each IPO. It can also be difficult trying to stay informed of all the upcoming hot IPOs. This calendar makes tracking upcoming IPOs and understanding the relevant information
incredibly simple. If you\u2019re new to the stock market and wondering, \u201c[What is a dividend yield?](https://www.marketbeat.com/financial-terms/what-is-dividend-yield/)\u201d, you may not
understand all the information provided, but once you ", "api_data": null, "hint": null}, {"title": "The IPOX\u00ae IPO Calendar \u2014 IPOX", "url": "https://www.ipox.com/upcoming-ipos", "snippet":
"Upcoming IPOs\nRobotphoenix Intelligent Technology Co., Ltd. (Ticker: 6871 HK) is a Chinese industrial robotics and factory automation company headquartered in Taizhou, Zhejiang. The company designs,
develops, manufactures and commercializes industrial robots, controllers, vision systems and integrated robotics solutions for light-industry applications. Its product portfolio includes parallel
robots, AGV/AMR mobile robots, SCARA robots, wafer-handling robots and six-axis industrial robots, suppor", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://stockanalysis.com/ipos/calendar/",
  "prompt": "What IPOs are upcoming or scheduled for the rest of May 2026 (May 20-31)? List all IPOs scheduled for the remainder of May 2026."
}
```

### 📋 Result

```
{"url": "https://stockanalysis.com/ipos/calendar/", "content": "Based on the provided content, **there is no information about specific IPOs scheduled for the remainder of May 2026 (May 20-31)**.
\n\nThe content only describes the sources used for the IPO calendar (S-1 filings, SEC data, press releases, etc.) and notes that IPO dates are estimated and subject to change. It does not contain any
actual IPO listings or dates.\n\nTo find the specific IPOs scheduled for late May 2026, you would need to access the actual calendar page at the source URL, which would contain the up-to-date IPO
schedule.\n\n**Relevant links:**\n- [Stock Analysis IPO Calendar](https://stockanalysis.com/ipos/calendar/) - The source page that should contain the current IPO schedule", "title": "IPO Calendar -
Upcoming IPOs"}
```

```json
{
  "url": "https://www.iposcoop.com/ipo-calendar/",
  "prompt": "What IPOs are expected or scheduled for the rest of May 2026 (May 20-31)? List all upcoming IPOs with expected pricing dates in May 2026."
}
```

### 📋 Result

```
{"url": "https://www.iposcoop.com/ipo-calendar/", "content": "Based on the content, the following IPOs are scheduled for the rest of May 2026 (May 20-31):\n\n**May 20, 2026 (Priced):**\n- **Lincoln
International (LCLN)** - 21.1 million shares at $20.00, raising $421.0 million. Underwriters: Goldman Sachs/Morgan Stanley/BMO Capital Markets/Citizens Capital Markets/Evercore ISI\n\n**Week of May
21, 2026:**\n- **BW Industrial Holdings (BWGC)** - 2.6 million shares at $6.00-$7.00 range, raising $17.1 million. Underwriter: Eddid Securities USA\n\n- **Encore Medical Inc. (EMI)** - 3.0 million
shares at $5.00, raising $15.0 million. Underwriter: The Oak Ridge Financial Services Group\n\n- **Optimi Health (OPTH)** - Uplisting, 2.5 million shares at $6.00-$8.00 range, raising $17.5 million.
Underwriter: Joseph Gunnar & Co.\n\n- **Riku Dining Group (RIKU)** - 5.0 million shares at $4.00-$6.00 range, raising $25.0 million. Underwriter: Eddid Securities USA\n\n**Thursday, May 21, 2026:**\n-
**Conexeu Sciences (CNXU)** - Direct Listing, 9.5 million shares at $4.00, $38.0 million. Financial Advisor: H.C. Wainwright\n\n- **Lannister Mining Corp. (DRIL)** - 2.0 million shares at $5.00,
raising $10.0 million. Underwriter: Joseph Gunnar & Co.\n\n**Relevant links:**\n- [Amanat Acquisition (Stock-Only)](https://www.iposcoop.com/ipo/amanat-acquisition-stock-only/)\n- [Lincoln
International](https://www.iposcoop.com/ipo/lincoln-international/)\n- [BW Industrial Holdings](https://www.iposcoop.com/ipo/bw-industrial-holdings-2/)\n- [Conexeu Sciences (Direct
Listing)](https://www.iposcoop.com/ipo/conexeu-sciences-direct-listing/)\n- [Encore Medical Inc.](https://www.iposcoop.com/ipo/encore-medical-inc/)\n- [Lannister Mining
Corp.](https://www.iposcoop.com/ipo/lannister-mining-corp/)\n- [Optimi Health (Uplisting)](https://www.iposcoop.com/ipo/optimi-health-ltd/)\n- [Riku Dining Group](https://www.iposcoop.com/ipo/riku-
dining-group/)", "title": "IPO Calendar"}
```

## 💭 Thinking

Now I have good data. Let me analyze what we know:

**Current state (as of May 19-20, 2026):**
- Stock Analysis lists 25-26 IPOs for May 2026 so far (through May 19)
- One source said 26 (from the main IPOs page), another said 25 (from the 2026 page). Let me reconcile - the difference might be due to timing of the fetch or counting methodology. Let me use 25-26 as the current count through May 19.

**Upcoming IPOs for rest of May (May 20-31):**
From IPOScoop, scheduled for the week of May 20-21:


Looking at the scheduled filings, I see seven more IPOs coming in just the May 20-21 window alone—Lincoln International pricing on May 20, followed by several others like BW Industrial Holdings, Encore Medical, Optimi Health, Riku Dining Group, Conexeu Sciences with a direct listing, and Lannister Mining Corp. That's already pushing the total higher, and there's still more of May left to account for.

Now I'm noticing a discrepancy between what the question stated about May 2025 having 33 IPOs and the actual monthly data I'm looking at, which shows different numbers across the year. Let me figure out where this gap is coming from. with May 2025 recording 33 IPOs"
My fetched data shows: 2025 range 9-30, May 2025 = 22

And for 2024: the question says "ranged from 12 to 34, with May 2024 recording 14 IPOs"
My fetched data shows: 2024 range 10-24, May 2024 = 11

There's a discrepancy. The question description might have been based on data from a different point in time, or the website may have revised its numbers. The actual current data from the site is what matters for resolution.

For the 2026 data I fetched:
- Jan: 29, Feb: 29, Mar: 13, Apr: 20, May: 25-26 (through May 19)

Now I need to figure out how many trading days are left in May. Today is May 20, which is a Tuesday, so I have this week (May 20-23) and next week (May 26-29, since May 25 is Memorial Day) — that's 8 more trading days. IPOScoop shows at least 7 IPOs scheduled for May 20-21 alone.

I'm calculating the IPO rate: roughly 2 IPOs per trading day through May 19. If that pace continues, I'd expect around 16 more IPOs by month-end, bringing the total to 41-42. But this is a rough estimate since IPO schedules can shift. Now I'm calculating the average IPOs per trading day based on 13 days through May 19, which comes to about 1.9-2.0 per day. For the remaining days in May after the 19th, I need to account for Memorial Day on May 25 (the last Monday of May 2026), so I'm looking at May 20-22 and then May 26-29 as available trading days. So if today is May 20, that leaves 7 trading days remaining through the end of the month. At roughly 2 IPOs per trading day, I'd expect around 14 more, bringing the total to approximately 39-40. Though that does seem high, so let me verify by looking at the actual IPO data more carefully. Through May 19 I'm counting 26 IPOs across the various dates, and now I'm checking the 2026 page to see what additional information it contains. Looking at the weekly breakdown, the IPO rate accelerates significantly from week to week—starting at 1.6 per day in early May, jumping to 2.6 per day by mid-May, then dropping to 0.5 per day in the most recent partial week. Given that IPOScoop shows at least 7 scheduled for May 20-22 and there's a full week ahead without Memorial Day disruptions, I need to reconcile this with Renaissance Capital's count of 13 priced IPOs as of May 17, keeping in mind that Stock Analysis typically reports 2-3x higher numbers than Renaissance Capital.

Projecting forward using the year-to-date pattern—with January through April averaging 22.75 per month and May already at 25-26 through the 19th—suggests May could finish around 38-40 total if the current pace continues linearly. However, IPO activity clusters unevenly throughout months, so I should weight the scheduled IPOs and recent acceleration more heavily than a simple linear projection. I'm noticing that Stock Analysis tracks more IPOs than Renaissance Capital—roughly 1.9x as many—likely because it includes SPACs and smaller listings that Renaissance doesn't capture. If Renaissance ends May with around 18-20 IPOs, that would suggest Stock Analysis could reach 34-38 by month's end.

Looking at it another way, with 65% of trading days completed and 25-26 IPOs already recorded, a linear projection points to roughly 38-40 total. Though Memorial Day on May 25 will compress the available trading window and might push some companies to delay their offerings, so I should account for that dampening effect.

Now I'm reviewing the specific IPOScoop listings for May 20-21 to verify the count and see which ones might actually appear on Stock Analysis. I need to verify whether Lincoln International is already in that count of 26, and if not, it would push the total to 27 through May 19. Now I'm setting up a simulation to model the remaining IPOs as a Poisson process and estimate how many will price by the end of May.

## 💬 Response

Now let me run a Monte Carlo simulation to project the final count.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Data gathered:\n# Current count through May 19: 25-26 IPOs (use 26 from the main listing page)\n# There's a small discrepancy between pages (25 vs 26), likely timing of updates\n\n# 2026 monthly data so far: Jan=29, Feb=29, Mar=13, Apr=20, May=25-26 (through May 19)\n# 2025 monthly data: Jan=21, Feb=19, Mar=12, Apr=15, May=22, Jun=17, Jul=20, Aug=18, Sep=15, Oct=12, Nov=9, Dec=30\n# 2024 monthly data: Jan=15, Feb=13, Mar=10, Apr=15, May=11, Jun=13, Jul=13, Aug=11, Sep=13, Oct=24, Nov=13, Dec=15\n\n# Trading days analysis for May 2026:\n# May 1 (Fri), May 4-8 (Mon-Fri), May 11-15 (Mon-Fri), May 18-22 (Mon-Fri), May 25=Memorial Day, May 26-29 (Tue-Fri)\n# Total trading days: 1 + 5 + 5 + 5 + 4 = 20 trading days\n# Through May 19: 1 + 5 + 5 + 2 = 13 trading days\n# Remaining: May 20-22 (3 days) + May 26-29 (4 days) = 7 trading days\n\n# IPO distribution by date through May 19:\n# May 1: 4, May 6: 2, May 7: 3, May 8: 3, May 13: 3, May 14: 5, May 15: 5, May 19: 1\n# Plus Lincoln International (LCLN) priced May 20\n\ncurrent_count = 26  # through May 19\ntrading_days_elapsed = 13\ntrading_days_remaining = 7\ntotal_trading_days = 20\n\n# Daily IPO rate so far\ndaily_rate = current_count / trading_days_elapsed\nprint(f\"Current count through May 19: {current_count}\")\nprint(f\"Trading days elapsed: {trading_days_elapsed}\")\nprint(f\"Trading days remaining: {trading_days_remaining}\")\nprint(f\"Daily IPO rate: {daily_rate:.2f}\")\nprint(f\"Simple linear projection: {current_count + daily_rate * trading_days_remaining:.1f}\")\n\n# From IPOScoop, we know of at least 7 specific IPOs scheduled for May 20-21\n# These are concrete scheduled deals, not projections\nknown_upcoming = 7  # LCLN, BWGC, EMI, OPTH, RIKU, CNXU, DRIL\nprint(f\"\\nKnown upcoming IPOs from IPOScoop (May 20-21): {known_upcoming}\")\n\n# But not all IPOScoop listings may appear on Stock Analysis, and SA may have others\n# Let's estimate the overlap - SA includes more (SPACs, small listings) but IPOScoop\n# tracks traditional IPOs well. Probably ~80% of these will appear on SA, plus SA\n# will have additional ones\n\n# Monte Carlo simulation\nnp.random.seed(42)\nn_sims = 100000\n\n# Model: current_count is known (either 25 or 26)\n# Remaining IPOs come from:\n# 1. Known scheduled IPOs (May 20-21): ~5-7 will actually price and appear on SA\n# 2. Unknown additional IPOs for May 22-29: modeled as Poisson\n\n# For known upcoming (May 20-21 week):\n# 7 scheduled, but some may slip or not be on SA, and SA may have additional ones\n# Model as a distribution: center ~6, range 4-9\nknown_upcoming_actual = np.random.poisson(6, n_sims)  # could be a bit more or less\n\n# For remaining period (May 22-29, ~5 trading days after the known ones):\n# Daily rate has been ~2.0 but with high variance\n# Use the observed rate with some uncertainty\n# The daily rate might slow down near Memorial Day weekend\n# Use a slightly lower rate for the remaining period: ~1.5-2.0/day for 5 days\n\n# Actually, let's be more precise. After May 21, there are:\n# May 22 (Fri): 1 day\n# May 26-29 (Tue-Fri): 4 days\n# Total: 5 more trading days\n\n# Model the remaining days' IPOs\nremaining_after_known = 5  # trading days May 22-29\n# Use observed daily rate with uncertainty\nrate_mean = daily_rate  # ~2.0\nrate_std = 0.5  # uncertainty in the daily rate\n\nrates = np.maximum(0.5, np.random.normal(rate_mean, rate_std, n_sims))\nadditional_ipos = np.random.poisson(rates * remaining_after_known)\n\n# Also, there might be IPOs that haven't been posted yet for May 20-21 that SA catches\n# This is captured in the known_upcoming_actual Poisson\n\n# Total\ntotal_may = current_count + known_upcoming_actual + additional_ipos\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total_may, percentiles)\n\nprint(\"\\n--- Monte Carlo Results (Model 1: Poisson) ---\")\nprint(f\"Mean: {np.mean(total_may):.1f}\")\nprint(f\"Median: {np.median(total_may):.1f}\")\nprint(f\"Std: {np.std(total_may):.1f}\")\nfor p, v in zip(percentiles, values):\n    print(f\"  P{p}: {v:.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Current count through May 19: 26\nTrading days elapsed: 13\nTrading days remaining: 7\nDaily IPO rate: 2.00\nSimple linear projection: 40.0\n\nKnown upcoming IPOs from
IPOScoop (May 20-21): 7\n\n--- Monte Carlo Results (Model 1: Poisson) ---\nMean: 42.0\nMedian: 42.0\nStd: 4.7\n  P1: 32.0\n  P5: 35.0\n  P10: 36.0\n  P20: 38.0\n  P25: 39.0\n  P30: 39.0\n  P40: 41.0\n
P50: 42.0\n  P60: 43.0\n  P70: 44.0\n  P75: 45.0\n  P80: 46.0\n  P90: 48.0\n  P95: 50.0\n  P99: 54.0\n", "stderr": "", "duration_ms": 274}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also run alternative models to triangulate\n\n# Model 2: Use the historical monthly totals and current progress\n# Approach: what fraction of monthly total comes in first 65% of trading days?\n\n# Historical monthly data\nmonths_2025 = [21, 19, 12, 15, 22, 17, 20, 18, 15, 12, 9, 30]\nmonths_2024 = [15, 13, 10, 15, 11, 13, 13, 11, 13, 24, 13, 15]\nmonths_2026 = [29, 29, 13, 20]  # Jan-Apr\n\nall_months = months_2024 + months_2025 + months_2026\nprint(\"Historical monthly statistics (2024-2026 Q1):\")\nprint(f\"  Mean: {np.mean(all_months):.1f}\")\nprint(f\"  Median: {np.median(all_months):.1f}\")\nprint(f\"  Std: {np.std(all_months):.1f}\")\nprint(f\"  Min: {np.min(all_months)}, Max: {np.max(all_months)}\")\n\n# 2026 average (Jan-Apr): \navg_2026 = np.mean(months_2026)\nprint(f\"\\n2026 monthly average (Jan-Apr): {avg_2026:.1f}\")\n\n# Model 3: Ratio-based approach using Renaissance Capital\n# Renaissance reports 13 IPOs through May 17\n# Stock Analysis has ~25-26 through May 19 (close dates)\n# Ratio: 25-26 / 13 \u2248 1.9-2.0x\n\n# If Renaissance ends May with ~18-22 IPOs (they had 13 through May 17 with ~8 trading days left)\n# RC daily rate: 13/12 \u2248 1.08/day, so 8 more days \u2192 ~8-9 more \u2192 total ~21-22\n# But RC rate might slow or speed up\n\nrc_current = 13\nrc_rate = rc_current / 12  # trading days through May 17\nrc_remaining_days = 8  # May 19-29 (approx)\nrc_projected = rc_current + rc_rate * rc_remaining_days\nratio = 26 / 13  # SA/RC ratio\nsa_from_rc = rc_projected * ratio\nprint(f\"\\nRenaissance Capital approach:\")\nprint(f\"  RC current: {rc_current}, daily rate: {rc_rate:.2f}\")\nprint(f\"  RC projected full month: {rc_projected:.1f}\")\nprint(f\"  SA/RC ratio: {ratio:.1f}x\")\nprint(f\"  SA projected from RC: {sa_from_rc:.1f}\")\n\n# Model 4: Consider that end-of-month might have fewer IPOs (Memorial Day effect)\n# Memorial Day weekend typically sees reduced activity\n# Last week of May might have ~60-80% of normal rate\n\nprint(\"\\n--- Scenario Analysis ---\")\n\n# Scenario 1: Normal rate continues (base case)\nremaining_normal = current_count + daily_rate * trading_days_remaining\nprint(f\"Scenario 1 (normal rate): {remaining_normal:.1f}\")\n\n# Scenario 2: Slower rate due to Memorial Day effect\nslow_rate = daily_rate * 0.7\nremaining_slow = current_count + slow_rate * trading_days_remaining\nprint(f\"Scenario 2 (Memorial Day slowdown, 70% rate): {remaining_slow:.1f}\")\n\n# Scenario 3: Rate picks up (more deals rush before month-end)\nfast_rate = daily_rate * 1.3\nremaining_fast = current_count + fast_rate * trading_days_remaining\nprint(f\"Scenario 3 (month-end rush, 130% rate): {remaining_fast:.1f}\")\n\n# But we also need to account for IPOs being added retroactively\n# Stock Analysis might add IPOs that priced earlier in the month but weren't yet listed\n# This is a small effect, maybe 1-3 additional\n\nprint(f\"\\nAdjusted for potential retroactive additions (+0 to +3):\")\nprint(f\"  Low: {remaining_slow:.1f} to {remaining_slow + 3:.1f}\")\nprint(f\"  Mid: {remaining_normal:.1f} to {remaining_normal + 3:.1f}\")\nprint(f\"  High: {remaining_fast:.1f} to {remaining_fast + 3:.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Historical monthly statistics (2024-2026 Q1):\n  Mean: 16.7\n  Median: 15.0\n  Std: 5.7\n  Min: 9, Max: 30\n\n2026 monthly average (Jan-Apr): 22.8\n\nRenaissance Capital
approach:\n  RC current: 13, daily rate: 1.08\n  RC projected full month: 21.7\n  SA/RC ratio: 2.0x\n  SA projected from RC: 43.3\n\n--- Scenario Analysis ---\nScenario 1 (normal rate): 40.0\nScenario
2 (Memorial Day slowdown, 70% rate): 35.8\nScenario 3 (month-end rush, 130% rate): 44.2\n\nAdjusted for potential retroactive additions (+0 to +3):\n  Low: 35.8 to 38.8\n  Mid: 40.0 to 43.0\n  High:
44.2 to 47.2\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Refined Monte Carlo with scenario mixture\nnp.random.seed(123)\nn_sims = 200000\n\n# Current count: 26 (through May 19) - could be 25 or 26, use uncertainty\ncurrent_base = np.random.choice([25, 26], size=n_sims, p=[0.3, 0.7])\n\n# 7 remaining trading days\n# Key uncertainty sources:\n# 1. How many of the 7 known IPOs from IPOScoop actually price and appear on SA\n# 2. How many additional IPOs are there that we don't know about yet\n# 3. Memorial Day effect\n# 4. Retroactive additions (IPOs that priced but aren't yet on the page)\n\n# Scenario weights\n# Base case: normal rate continues (50%)\n# Slowdown: Memorial Day, reduced activity (25%)\n# Acceleration: month-end rush, more deals (15%)\n# Very slow: market conditions deteriorate (10%)\n\nscenarios = np.random.choice(\n    ['base', 'slow', 'fast', 'very_slow'], \n    size=n_sims, \n    p=[0.50, 0.25, 0.15, 0.10]\n)\n\n# Daily rates by scenario\nrate_map = {\n    'base': (2.0, 0.4),      # mean, std of daily rate\n    'slow': (1.3, 0.3),       # Memorial Day slowdown\n    'fast': (2.6, 0.5),       # month-end rush\n    'very_slow': (0.8, 0.3),  # market stress\n}\n\nadditional = np.zeros(n_sims, dtype=int)\nfor scenario, (rate_mean, rate_std) in rate_map.items():\n    mask = scenarios == scenario\n    n = mask.sum()\n    rates = np.maximum(0.2, np.random.normal(rate_mean, rate_std, n))\n    additional[mask] = np.random.poisson(rates * 7)\n\n# Retroactive additions (IPOs that may be added later for earlier May dates)\nretroactive = np.random.choice([0, 1, 2, 3], size=n_sims, p=[0.4, 0.35, 0.2, 0.05])\n\ntotal = current_base + additional + retroactive\n\n# Clip at 0 (can't have negative)\ntotal = np.maximum(total, 0)\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total, percentiles)\n\nprint(\"--- Refined Monte Carlo (Scenario Mixture) ---\")\nprint(f\"Mean: {np.mean(total):.1f}\")\nprint(f\"Median: {np.median(total):.1f}\")\nprint(f\"Std: {np.std(total):.1f}\")\nprint(f\"Min: {np.min(total)}, Max: {np.max(total)}\")\nprint()\nfor p, v in zip(percentiles, values):\n    print(f\"  P{p}: {v:.1f}\")\n\n# Sanity check: compare with historical range\nprint(f\"\\nHistorical monthly range (2024-2026 Q1): 9-30\")\nprint(f\"2026 monthly range so far (Jan-Apr): 13-29\")\nprint(f\"Our forecast range (P10-P90): {values[2]:.0f}-{values[12]:.0f}\")\nprint(f\"Note: May 2026 already has 26 with 35% of month remaining, so higher than most months is expected\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "--- Refined Monte Carlo (Scenario Mixture) ---\nMean: 39.2\nMedian: 39.0\nStd: 5.9\nMin: 25, Max: 71\n\n  P1: 28.0\n  P5: 30.0\n  P10: 32.0\n  P20: 34.0\n  P25: 35.0\n
P30: 36.0\n  P40: 37.0\n  P50: 39.0\n  P60: 40.0\n  P70: 42.0\n  P75: 43.0\n  P80: 44.0\n  P90: 47.0\n  P95: 49.0\n  P99: 55.0\n\nHistorical monthly range (2024-2026 Q1): 9-30\n2026 monthly range so
far (Jan-Apr): 13-29\nOur forecast range (P10-P90): 32-47\nNote: May 2026 already has 26 with 35% of month remaining, so higher than most months is expected\n", "stderr": "", "duration_ms": 40}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Wait - I need to reconsider. The question description mentions numbers that are different\n# from what I'm seeing on the site. Let me re-read:\n# \n# Question says: \"2025 ranged from 18 to 37, with May 2025 recording 33 IPOs\"\n# My fetch says: 2025 ranged from 9 to 30, May 2025 = 22\n#\n# Question says: \"2024 ranged from 12 to 34, with May 2024 recording 14 IPOs\"\n# My fetch says: 2024 ranged from 10 to 24, May 2024 = 11\n#\n# This is a significant discrepancy. The question was likely written using data from the\n# IPO statistics page (which may show different numbers than the individual year pages).\n# OR the website has revised its numbers since the question was written.\n# OR my web fetch is not capturing all entries (pagination issues).\n#\n# The resolution uses the statistics page number. Let me check: the statistics page\n# didn't show 2026 monthly breakdown in my earlier fetch. But the question description\n# references that page's methodology.\n#\n# Important: The question says the statistics page shows monthly counts that are higher\n# than what I'm seeing on the yearly listing pages. This suggests the statistics page\n# may use a broader methodology or include more listings.\n#\n# If the statistics page typically shows higher numbers:\n# - My count of 26 from the listing page might correspond to a higher number on the stats page\n# - The ratio could be: stats_page / listing_page \u2248 33/22 = 1.5x (for May 2025)\n# Or: 14/11 = 1.27x (for May 2024)\n#\n# Let me check if there's a systematic difference\n\n# Numbers from question description (statistics page):\nstats_may_2025 = 33\nstats_may_2024 = 14\n\n# Numbers from my fetch (listing pages):\nlisting_may_2025 = 22\nlisting_may_2024 = 11\n\nratio_2025 = stats_may_2025 / listing_may_2025\nratio_2024 = stats_may_2024 / listing_may_2024\n\nprint(f\"Ratio (stats page / listing page):\")\nprint(f\"  May 2025: {stats_may_2025}/{listing_may_2025} = {ratio_2025:.2f}\")\nprint(f\"  May 2024: {stats_may_2024}/{listing_may_2024} = {ratio_2024:.2f}\")\n\n# Hmm, the ratios aren't consistent. Let me consider alternative explanations:\n# 1. My web fetch might be paginated and not showing all results\n# 2. The listing page might have been updated/revised since the question was written\n# 3. The statistics page uses a different counting methodology\n\n# Actually, looking more carefully at the 2025 totals:\n# Question says: \"2025 ranged from 18 to 37\" with July=37, November=18\n# My fetch says: Total 2025 = 210, with July=20, November=9\n# The statistics page says total 2025 = 347\n\n# So the statistics page number (347) is much higher than the listing page (210)\n# Ratio: 347/210 \u2248 1.65x\n\n# This strongly suggests the listing pages are paginated or filtered differently\n# The statistics page likely includes MORE listings\n\n# Let me recalculate with this correction factor\nlisting_2025_total = 210\nstats_2025_total = 347\noverall_ratio = stats_2025_total / listing_2025_total\nprint(f\"\\nOverall 2025 ratio: {stats_2025_total}/{listing_2025_total} = {overall_ratio:.2f}\")\n\n# For May 2026, the listing page shows 25-26\n# Adjusted for the stats page methodology:\nstats_equivalent_low = 25 * overall_ratio\nstats_equivalent_high = 26 * overall_ratio\nprint(f\"\\nMay 2026 current (listing page): 25-26\")\nprint(f\"May 2026 current (stats page equivalent): {stats_equivalent_low:.0f}-{stats_equivalent_high:.0f}\")\n\n# But wait - this is problematic. The ratio might not be consistent.\n# Let me check the May-specific ratio:\nmay_ratio = stats_may_2025 / listing_may_2025\nprint(f\"\\nMay 2025 specific ratio: {may_ratio:.2f}\")\nprint(f\"May 2026 adjusted (using May ratio): {25 * may_ratio:.0f}-{26 * may_ratio:.0f}\")\n\n# This is really uncertain. The stats page might count differently.\n# Let me also check if the question description numbers match the stats page data\n# that might have different inclusion criteria.\n\n# Actually, I think there might be a simpler explanation:\n# The listing pages might be paginated (showing only first N results)\n# while the stats page shows the actual total count.\n\n# Either way, I need to figure out whether my current count of 26 from the listing\n# page captures ALL May 2026 IPOs or just a subset.\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Ratio (stats page / listing page):\n  May 2025: 33/22 = 1.50\n  May 2024: 14/11 = 1.27\n\nOverall 2025 ratio: 347/210 = 1.65\n\nMay 2026 current (listing page): 25-26\nMay
2026 current (stats page equivalent): 41-43\n\nMay 2025 specific ratio: 1.50\nMay 2026 adjusted (using May ratio): 38-39\n", "stderr": "", "duration_ms": 0}
```

## 💭 Thinking

This is a critical finding. The listing page and the statistics page show different numbers. The statistics page appears to include more listings than the listing page. Let me investigate further - the listing page might be paginated or the stats page might use a different methodology.

The listing page (stockanalysis.com/ipos/2025/) showed 210 total for 2025, while the statistics page mentioned 347 for 2025. That's a significant difference.

But wait - I need to re-read what the statistics page actually said. My fetch returned:
"Total for 2025: 347 IPOs"
"July: 37 (most)"


"November: 18 (least)"

And from the listing page I got monthly totals summing to about 210. So the statistics page captures about 1.65x more IPOs than the listing page. This is a crucial correction.

But then my current count of 26 from the listing page for May 2026 might only represent about 60-70% of what the statistics page will eventually show. Actually, the 2026 page showed 25 IPOs. Let me check: could the main IPOs page (stockanalysis.com/ipos/) be showing the most recent 200 IPOs across all years? If it showed 26 for May 2026, that might be a subset of the full data.

The title says "200 Most Recent IPOs" - so if there are 26 IPOs in May 2026 among the most recent, they should all be captured. But the 2026 page showed 25, the 2025 page showed 210, while the statistics page showed 347 for 2025. The discrepancy likely comes down to pagination on the listing pages - my scraper probably only captured the first page of results rather than the complete dataset.

For 2025, getting 210 entries when the page displays 200 per page suggests the extraction wasn't perfectly accurate, but the key issue is that May 2026 has far fewer entries than any pagination limit, so the 25-26 count is probably the actual current number on the listing page. The real question is whether the statistics page uses a different counting methodology than the listing pages, since it shows significantly higher numbers.

Looking at the data more carefully: the 2025 statistics page showed 347 total while the listing page had 210, a 1.65x difference. For 2024, I'm seeing a similar pattern where the listing page undercounts compared to what the statistics page likely shows. This suggests the listing pages might be paginated for older years and I only captured the first batch, though for the current year the listing page might be showing everything.

The real issue is that the statistics page and listing page are measuring different things—the statistics page appears to include more types of listings that get filtered out on the listing page. Looking at May 2025 specifically, the listing page showed 22 but the statistics page showed 33, a 1.5x ratio. So for May 2026, I should estimate based on the statistics page ratio rather than trusting the listing page count of 25. The statistics page hasn't been updated with 2026 monthly data yet, so the final resolution number will depend on what appears there at month's end. Given the consistent pattern of the statistics page showing higher counts than the listing page across historical data, I'm leaning toward the statistics page genuinely capturing more IPOs rather than my listing count being accurate.

If I apply a moderate adjustment factor of around 1.4 to my current count of 25-26 through May 19, that would suggest the true count is closer to 35-36, but projecting that linearly across the full month yields numbers that seem too high. I'm reconsidering whether the adjustment ratio works the same way for partial months versus complete months, since the statistics page might be adding listings retroactively or in batches. Let me shift my perspective and look at what the 2025 statistics page actually shows—the monthly range was 18-37 with an average around 29.

For 2024, the statistics page shows a range of 12-34 with an estimated total of 200-250, giving a mean of roughly 17-21. The question states that 2026 figures have tracked in line with the 2024-2025 ranges, but when I apply my estimated 1.5-1.65x adjustment to my fetched data for 2026 (January through April showing 29, 29, 13, and 20 respectively), I get adjusted values of around 43-44, 43-44, 19-20, and 30—which would exceed the stated 18-37 range for most months.

Re-reading more carefully, the 2026 figures I'm seeing (29, 29, 13, 20) actually fall within the 2024-2025 ranges without any adjustment needed. This suggests the listing page numbers I fetched are already the statistics page figures for 2026, not raw counts that need conversion. The consistency across all four months with the prior year ranges supports this interpretation, so the discrepancy I was concerned about may not actually exist.

The real issue is likely that my web scraping for 2025 only captured a partial dataset due to pagination—the listing page shows all 347 IPOs, but my extraction probably only processed the first page of results. For 2026, with only ~116 IPOs so far, everything fits on a single page, which is why my May count of 25 should be reliable. The scraper's reliability is probably limited for historical data, but May 2026 should be more accurate since it's current and has fewer entries. Let me anchor on what I can verify: the listing page shows 25-26 IPOs for May 2026 through the 19th, the "200 Most Recent IPOs" page is capped at that limit, and the 2026 yearly page should capture all entries for the year. The real question is whether the statistics page and the IPO listing pages are pulling from the same dataset, and given that the 2026 figures align with the 2024-2025 ranges mentioned in the question, I'm fairly confident in the current month's count. I'm counting through all the May 2026 IPO entries from the main page and getting 26 total, which contradicts the 25 shown on the 2026 stats page—there might be a discrepancy in how one entry was counted or categorized.

For the remaining trading days in late May, IPOScoop lists 7 upcoming IPOs, though Stock Analysis might exclude certain ones like uplisting companies or include additional smaller listings that IPOScoop doesn't track.

Looking at the ratio between the two sources across the first three weeks of May, Stock Analysis typically shows about 1.4-1.7x more listings than IPOScoop, so I should account for that gap when projecting the final week. For May 22-29 (accounting for Memorial Day on May 25), I need to estimate how many additional IPOs beyond the known ones will be announced and included on Stock Analysis.

My refined projection puts the total additional IPOs for the rest of May at around 11-19, bringing the full month to approximately 37-45 with a center estimate of 39-41, which aligns closely with my Monte Carlo simulation results. However, I'm now second-guessing whether my current count of 26 might be an undercount if the question's source data uses a different methodology than what I'm seeing on IPOScoop.

The question hints that Renaissance Capital reported 13 IPOs through May 17, and Stock Analysis's methodology typically captures 2-3x more than RC's count. If RC continues at roughly 1.08 IPOs per day for the remaining 8 trading days in May, that projects to about 21-22 total for RC, which would translate to 43-65 IPOs on Stock Analysis at the 2-3x multiplier—or around 54 using 2.5x as a midpoint estimate.

But wait, that projection seems high compared to what I'm seeing on the listing page. Let me recalibrate: if Stock Analysis counted 33 IPOs for May 2025 and Renaissance Capital had roughly 10-15 for that same month, the 2-3x ratio checks out. For May 2026, RC's trajectory through May 17 suggests a full-month count around 20-22, which at 2.5x multiplier would put Stock Analysis at 50-55 IPOs. Yet my listing page only shows 26 through May 19, so there's a significant gap between what the statistics page might report and what I'm actually seeing in the data.

The ratio might not be consistent throughout the month—Stock Analysis could be adding listings retroactively or on a different schedule than Renaissance Capital. Or the 2-3x figure from the question is just an approximation rather than a precise multiplier. Looking at the raw numbers for May 2025, if RC had around 13 IPOs and SA had 33, that's exactly 2.5x. For the current month, RC has 13 through May 17 while SA's listing page shows 26 through May 19, which is already a 2x ratio with SA having a couple extra days of data. This suggests the multiplier might be settling closer to 2x right now, though it could shift higher as SA adds more small-cap or SPAC listings later in the month.

I think the most reliable approach is to treat my listing page count of 26 as a lower bound for what the statistics page currently shows, use the RC-based projection of around 32-33 as an upper indicator, and then extrapolate from there. But actually, I'm probably overcomplicating this—the 2026 listing page likely reflects the correct count for the statistics page. The question mentions that 2026 figures have been in line with the 2024-2025 range of 18-37, and the year page shows January through April at 29, 29, 13, and 20 respectively, all within that range. If there were a significant undercount, those months would fall outside the historical bounds.

So I'm confident the 2026 listing numbers match the statistics page. The 2025 discrepancy is probably just a web scraping artifact from pagination limits. I'll use 26 as my current count through May 19, and with 7 trading days left and at least 7 known IPOs coming, I'm projecting somewhere between 37-42, though there's real uncertainty here. Now I need to reconsider the Renaissance Capital multiplier more carefully—they had 13 through May 17 while Stock Analysis shows 26 through May 19, so I should account for those two extra days when comparing the rates.

Between May 17 and May 19, Stock Analysis picked up one IPO (AMAN) and May 18 was a weekend, so they added just one in that window. If Renaissance Capital added maybe zero or one more by May 19, the ratio would be around 1.86 to 2.0x. This ratio could hold steady or widen as Stock Analysis captures more smaller listings that lag behind the major deals. If the final ratio lands at 2.0 to 2.5x and Renaissance Capital finishes May around 20-22, then Stock Analysis would end up somewhere between 40-55 depending on which multiplier holds, with 40 being the result if I apply a 2.0x ratio to Renaissance Capital's projection.

Now I'm setting up a Monte Carlo simulation with better-calibrated parameters: Stock Analysis currently has 26 through May 19, there are 7 trading days left in the month, IPOScoop shows 7 scheduled for May 20-21, the historical daily rate is around 2.0 per day, Memorial Day will suppress activity, and the Renaissance Capital ratio points toward a full-month range of 40-55. My central estimate is 38-42, with P10 around 30-33 and P90 around 48-52.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me investigate whether the listing page count matches the statistics page\n# by checking whether the question's description numbers are consistent\n\n# The question says 2026 figures are \"broadly in line with 2024-2025 ranges\"\n# 2025 stats page range: 18-37\n# 2026 listing page: Jan=29, Feb=29, Mar=13, Apr=20\n# These ARE within 18-37 range, suggesting listing page = stats page for 2026\n\n# For 2025, my listing page extraction likely missed entries due to pagination\n# (page shows 200 most recent, 2025 had 347 total)\n\n# So for May 2026 through May 19: 26 IPOs is the correct current count\n# Now project the remaining 7 trading days\n\n# Key data points:\n# 1. Current count: 26 through May 19 (13 trading days)\n# 2. Daily rate: 2.0/day\n# 3. IPOScoop shows 7 scheduled for May 20-21  \n# 4. Renaissance Capital at 13 through May 17, ratio ~2x with SA\n# 5. RC projected full month: ~20-22, SA at 2-2.5x \u2192 40-55\n# 6. Historical May on stats page: May 2025=33, May 2024=14\n\n# The biggest uncertainty is whether the remaining rate holds at ~2/day\n# or whether the statistics page will add additional listings retroactively\n\nnp.random.seed(456)\nn_sims = 200000\n\n# Current count: 26 (tight, well-established from listing page)\ncurrent = 26\n\n# Additional from stats page methodology: might add 0-5 extra that listing page misses\n# Based on the RC multiplier analysis, the stats page could show a bit more\nstats_page_bonus = np.random.choice([0, 1, 2, 3, 4, 5], size=n_sims, \n                                     p=[0.30, 0.25, 0.20, 0.15, 0.07, 0.03])\n\n# Known upcoming IPOs (May 20-21): 7 scheduled on IPOScoop\n# Probability each makes it to SA: ~75-85%\n# Plus SA may have 1-3 additional that IPOScoop doesn't track\nknown_upcoming = np.random.binomial(7, 0.80, n_sims) + np.random.poisson(1.5, n_sims)\n\n# Remaining period (May 22-29): 5 trading days\n# Scenario mixture for daily rate\nscenarios = np.random.choice(['normal', 'slow', 'fast'], size=n_sims, p=[0.5, 0.3, 0.2])\n\nadditional_rest = np.zeros(n_sims, dtype=int)\nfor s, (rmean, rstd) in [('normal', (1.8, 0.4)), ('slow', (1.0, 0.3)), ('fast', (2.5, 0.5))]:\n    mask = scenarios == s\n    n = mask.sum()\n    rates = np.maximum(0.2, np.random.normal(rmean, rstd, n))\n    additional_rest[mask] = np.random.poisson(rates * 5)\n\ntotal = current + stats_page_bonus + known_upcoming + additional_rest\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total, percentiles)\n\nprint(\"--- Final Refined Monte Carlo ---\")\nprint(f\"Mean: {np.mean(total):.1f}\")\nprint(f\"Median: {np.median(total):.1f}\")\nprint(f\"Std: {np.std(total):.1f}\")\nprint(f\"Min: {np.min(total)}, Max: {np.max(total)}\")\nprint()\npct_dict = {}\nfor p, v in zip(percentiles, values):\n    pct_dict[str(p)] = round(float(v), 1)\n    print(f\"  P{p}: {v:.1f}\")\n\nprint(f\"\\n--- Sanity Checks ---\")\nprint(f\"Historical May on stats page: May 2025=33, May 2024=14\")\nprint(f\"Our median ({np.median(total):.0f}) vs 2025 ({33}): Our is higher, consistent with 2026 being active\")\nprint(f\"P(below May 2024 level of 14): {100*np.mean(total < 14):.2f}% (essentially 0 since we already have 26)\")\nprint(f\"P(above May 2025 level of 33): {100*np.mean(total > 33):.1f}%\")\nprint(f\"P(between 30 and 50): {100*np.mean((total >= 30) & (total <= 50)):.1f}%\")\nprint(f\"P(above 50): {100*np.mean(total > 50):.1f}%\")\nprint(f\"P(below 30): {100*np.mean(total < 30):.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "--- Final Refined Monte Carlo ---\nMean: 43.1\nMedian: 43.0\nStd: 4.9\nMin: 29, Max: 72\n\n  P1: 34.0\n  P5: 36.0\n  P10: 37.0\n  P20: 39.0\n  P25: 40.0\n  P30: 40.0\n
P40: 41.0\n  P50: 43.0\n  P60: 44.0\n  P70: 45.0\n  P75: 46.0\n  P80: 47.0\n  P90: 50.0\n  P95: 52.0\n  P99: 56.0\n\n--- Sanity Checks ---\nHistorical May on stats page: May 2025=33, May 2024=14\nOur
median (43) vs 2025 (33): Our is higher, consistent with 2026 being active\nP(below May 2024 level of 14): 0.00% (essentially 0 since we already have 26)\nP(above May 2025 level of 33):
99.2%\nP(between 30 and 50): 92.2%\nP(above 50): 7.8%\nP(below 30): 0.0%\n", "stderr": "", "duration_ms": 41}
```

## 💭 Thinking

Hmm, the median of 43 seems a bit high. Let me reconsider the stats_page_bonus. Am I double-counting? 

My base count is 26 from the listing page. I'm adding:
1. stats_page_bonus: 0-5 extra listings the stats page might count
2. known_upcoming: ~5-6 + ~1.5 Poisson = ~7-8
3. additional_rest: ~5-9 for the remaining 5 trading days

Total additional: ~12-17, so total ~38-43.


Actually, I might be overcounting here. The stats_page_bonus could be redundant if the listing page already captures the full picture, and there's likely some overlap between the known upcoming IPOs and what materializes during the rest of the month. If I drop the bonus and tighten my assumptions—assuming about 7 from the IPOScoop list actually show up on SA, plus 5-10 more across the final five trading days—I'm looking at roughly 36-43 total, centering around 39.

But keeping the stats_page_bonus modest at 0-2 pushes the range to 36-45, with a midpoint around 40-41. The real question is whether I'm double-counting somewhere. Let me recalibrate by anchoring to what I actually know: the question closed May 20, RC had 13 through May 17, and SA typically runs 2-3x RC's count. That gives me a much clearer baseline to work from than trying to estimate uncertain future additions.

Looking at the current data, SA is at 26 through May 19 while RC is at 13 through May 17—that's roughly a 2x ratio, which sits at the lower end of the stated range. If RC finishes around 20 and that ratio holds steady, SA should land near 40, though there's room for it to climb slightly higher if the ratio tightens toward 2.5x by month-end.

My models are clustering around a median of 39-43, with the 10th percentile near 32-37 and the 90th percentile around 47-50. I think 35-50 is a solid range with 40-42 as the center, though I should probably dial back the stats_page_bonus adjustment since it might be inflating the estimate.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me run a more conservative version without the stats_page_bonus\n# since 2026 listing page numbers appear consistent with stats page ranges\n\nnp.random.seed(789)\nn_sims = 200000\n\ncurrent = 26  # confirmed through May 19\n\n# May 20-21 additions: 7 on IPOScoop, ~80% make it to SA, plus SA extras\nweek4_additions = np.random.binomial(7, 0.80, n_sims) + np.random.poisson(1.0, n_sims)\n\n# May 22-29 (5 trading days), with Memorial Day reducing activity\n# Use a moderate rate, slightly below the month-to-date average\nscenarios = np.random.choice(['normal', 'slow', 'fast'], size=n_sims, p=[0.5, 0.3, 0.2])\n\nweek5_additions = np.zeros(n_sims, dtype=int)\nfor s, (rmean, rstd) in [('normal', (1.6, 0.4)), ('slow', (0.8, 0.3)), ('fast', (2.3, 0.5))]:\n    mask = scenarios == s\n    n = mask.sum()\n    rates = np.maximum(0.1, np.random.normal(rmean, rstd, n))\n    week5_additions[mask] = np.random.poisson(rates * 5)\n\n# Small chance of retroactive additions (1-2 IPOs added to earlier May dates)\nretro = np.random.choice([0, 1, 2], size=n_sims, p=[0.6, 0.3, 0.1])\n\ntotal = current + week4_additions + week5_additions + retro\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total, percentiles)\n\nprint(\"--- Conservative Monte Carlo (No Stats Page Bonus) ---\")\nprint(f\"Mean: {np.mean(total):.1f}\")\nprint(f\"Median: {np.median(total):.1f}\")\nprint(f\"Std: {np.std(total):.1f}\")\nprint()\n\npct_dict = {}\nfor p, v in zip(percentiles, values):\n    pct_dict[str(p)] = round(float(v), 1)\n    print(f\"  P{p}: {v:.1f}\")\n\n# Compare all models\nprint(\"\\n--- Model Comparison ---\")\nprint(f\"Model 1 (basic Poisson): median ~42\")\nprint(f\"Model 2 (scenario mixture): median ~39\")\nprint(f\"Model 3 (refined with stats bonus): median ~43\")\nprint(f\"Model 4 (conservative, no stats bonus): median ~{np.median(total):.0f}\")\nprint(f\"\\nLinear projection: 40.0\")\nprint(f\"RC-based (2x): ~40-44\")\nprint(f\"RC-based (2.5x): ~50-55\")\n\n# The truth is probably between Models 2 and 4\n# Given all evidence, I'll center around 39-40 with moderate uncertainty\nprint(\"\\n--- Recommended Distribution ---\")\n# Average of models 2 and 4 roughly\nrecommended_center = 39\nprint(f\"Center: ~{recommended_center}\")\nprint(f\"P10-P90 range: ~32-48\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "--- Conservative Monte Carlo (No Stats Page Bonus) ---\nMean: 40.6\nMedian: 40.0\nStd: 4.6\n\n  P1: 32.0\n  P5: 34.0\n  P10: 35.0\n  P20: 37.0\n  P25: 37.0\n  P30: 38.0\n
P40: 39.0\n  P50: 40.0\n  P60: 41.0\n  P70: 43.0\n  P75: 43.0\n  P80: 44.0\n  P90: 47.0\n  P95: 49.0\n  P99: 53.0\n\n--- Model Comparison ---\nModel 1 (basic Poisson): median ~42\nModel 2 (scenario
mixture): median ~39\nModel 3 (refined with stats bonus): median ~43\nModel 4 (conservative, no stats bonus): median ~40\n\nLinear projection: 40.0\nRC-based (2x): ~40-44\nRC-based (2.5x):
~50-55\n\n--- Recommended Distribution ---\nCenter: ~39\nP10-P90 range: ~32-48\n", "stderr": "", "duration_ms": 37}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Final blended model averaging across approaches\nnp.random.seed(999)\nn_sims = 300000\n\ncurrent = 26\n\n# Model A: Conservative (50% weight) - listing page count is accurate\n# Model B: With stats page upward adjustment (30% weight) \n# Model C: RC-based higher estimate (20% weight)\n\nmodel_choice = np.random.choice(['A', 'B', 'C'], size=n_sims, p=[0.50, 0.30, 0.20])\n\ntotal = np.zeros(n_sims, dtype=int)\n\nfor i in range(n_sims):\n    base = current\n    \n    if model_choice[i] == 'A':\n        # Conservative: listing page = stats page, normal rate\n        upcoming = np.random.binomial(7, 0.78) + np.random.poisson(1.0)\n        rate = max(0.2, np.random.normal(1.5, 0.4))\n        rest = np.random.poisson(rate * 5)\n        retro = np.random.choice([0, 1, 2], p=[0.6, 0.3, 0.1])\n        total[i] = base + upcoming + rest + retro\n        \n    elif model_choice[i] == 'B':\n        # Stats page shows more: add 2-4 extra from broader methodology\n        stats_bonus = np.random.choice([1, 2, 3, 4], p=[0.25, 0.35, 0.25, 0.15])\n        upcoming = np.random.binomial(7, 0.80) + np.random.poisson(1.5)\n        rate = max(0.2, np.random.normal(1.8, 0.4))\n        rest = np.random.poisson(rate * 5)\n        retro = np.random.choice([0, 1, 2], p=[0.5, 0.35, 0.15])\n        total[i] = base + stats_bonus + upcoming + rest + retro\n        \n    elif model_choice[i] == 'C':\n        # RC-based: higher multiplier implies more listings\n        stats_bonus = np.random.choice([3, 4, 5, 6, 7], p=[0.2, 0.3, 0.25, 0.15, 0.1])\n        upcoming = np.random.binomial(7, 0.85) + np.random.poisson(2.0)\n        rate = max(0.3, np.random.normal(2.2, 0.5))\n        rest = np.random.poisson(rate * 5)\n        retro = np.random.choice([0, 1, 2, 3], p=[0.4, 0.3, 0.2, 0.1])\n        total[i] = base + stats_bonus + upcoming + rest + retro\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total, percentiles)\n\nprint(\"--- Final Blended Monte Carlo ---\")\nprint(f\"Mean: {np.mean(total):.1f}\")\nprint(f\"Median: {np.median(total):.1f}\")\nprint(f\"Std: {np.std(total):.1f}\")\nprint(f\"Min: {np.min(total)}, Max: {np.max(total)}\")\nprint()\n\nfinal_pct = {}\nfor p, v in zip(percentiles, values):\n    final_pct[str(p)] = round(float(v), 1)\n    print(f\"  P{p}: {v:.1f}\")\n\nprint(f\"\\nP(30-50): {100*np.mean((total >= 30) & (total <= 50)):.1f}%\")\nprint(f\"P(35-45): {100*np.mean((total >= 35) & (total <= 45)):.1f}%\")\nprint(f\"P(<30): {100*np.mean(total < 30):.2f}%\")\nprint(f\"P(>55): {100*np.mean(total > 55):.2f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "--- Final Blended Monte Carlo ---\nMean: 43.9\nMedian: 43.0\nStd: 5.7\nMin: 28, Max: 72\n\n  P1: 34.0\n  P5: 36.0\n  P10: 37.0\n  P20: 39.0\n  P25: 40.0\n  P30: 40.0\n
P40: 42.0\n  P50: 43.0\n  P60: 45.0\n  P70: 46.0\n  P75: 47.0\n  P80: 49.0\n  P90: 52.0\n  P95: 54.0\n  P99: 59.0\n\nP(30-50): 86.8%\nP(35-45): 62.7%\nP(<30): 0.00%\nP(>55): 3.38%\n", "stderr": "",
"duration_ms": 2941}
```

## 💭 Thinking

Let me look at this more carefully. The blended model gives a median of 43, which is influenced by the RC-based model (Model C) pulling it up. Let me reconsider whether Model C's assumptions are right.

The key question is: does the SA statistics page count match what I see on the listing page, or is it systematically higher?

Evidence for listing = stats (Model A):
- 2026 figures described as "broadly in line with 2024-2025 ranges" (18-37)
- My 2026 listing page shows Jan=29, Feb=29, which are within 18-37


- A 1.5x factor would push Jan and Feb to around 44, exceeding the stated maximum

Evidence for stats > listing (Model B/C):
- Clear discrepancy for 2025: listing showed ~210 total vs stats showing 347
- The ratio for May-specific numbers also differs (22 vs 33 for May 2025)
- RC multiplier of 2-3x is mentioned in the question

I'm wondering if the simpler explanation is that the web scraper for 2025 only captured a partial view due to pagination or rendering issues, while the 2026 page with far fewer entries was fully captured.

For 2026, the listing page count should be accurate and align with the stats page. Given that, Model A seems most appropriate with a median around 40. Though I should still hedge against the possibility that the stats page uses a different counting methodology. I'm settling on weighting Model A at 60%, Model B at 25%, and Model C at 15%. My blended model gives a median of 43, but the more conservative approaches cluster around 40-42, so I'll use the conservative model as my primary estimate with slightly wider confidence intervals to account for the methodological uncertainty. Looking at the percentile distributions across my models, they're clustering pretty consistently around similar values. The blended model output seems reasonable, and while I had some hesitation about the stats_page_bonus estimate, the uncertainty in the SA methodology balances that concern out. I'll settle on values that split the difference between my conservative and blended approaches.

## 💬 Response

Now let me check coherence with related questions and run my reflection.

## 🔧 Tool: mcp__metaculus__get_coherence_links


```json
{
  "post_id": 43543
}
```

### 📋 Result

```
[]
```

## 💭 Thinking

No coherence links. Let me proceed to reflection and then premortem.

Let me synthesize my findings and decide on final percentiles. The key data:

1. Current count on SA listing page: 26 through May 19 (13 trading days)
2. 7 remaining trading days (May 20-22, May 26-29, Memorial Day May 25)
3. 7 known upcoming IPOs from IPOScoop for May 20-21
4. Historical daily rate: ~2.0/day
5. RC multiplier suggests ~2x, pointing to ~40-44 full month


6. Linear projection: 40
7. Monte Carlo models give median 39-43 depending on assumptions

The main question is whether the statistics page will report higher numbers than the listing page. Since 2026 figures are described as broadly aligned with 2024-2025 ranges and the listing page already falls within those ranges, I'm inclined to trust the listing page as the more accurate source. I'll set my distribution centered around 40-41, with P10 at 34-35 for a slowdown scenario, P50 at 40-41, and P90 at 49-50 to account for potential acceleration or methodological differences in how the statistics page counts.

Now I'm settling on final values that split the difference between my conservative and blended approaches.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Current confirmed count of 26 IPOs through May 19 on SA listing page establishes a hard floor",
      "supports": {
        "center": 40,
        "low": 34,
        "high": 50
      },
      "logit": 2,
      "confidence": 0.95
    },
    {
      "description": "7 known upcoming IPOs from IPOScoop for May 20-21 (LCLN, BWGC, EMI, OPTH, RIKU, CNXU, DRIL), ~80% likely to appear on SA",
      "supports": {
        "center": 32,
        "low": 30,
        "high": 34
      },
      "logit": 1.5,
      "confidence": 0.8
    },
    {
      "description": "Historical daily rate of ~2.0 IPOs/trading day extrapolated over 7 remaining trading days suggests ~14 more",
      "supports": {
        "center": 40,
        "low": 35,
        "high": 47
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Memorial Day (May 25) reduces activity in last week - some slowdown expected",
      "supports": {
        "center": 38,
        "low": 33,
        "high": 42
      },
      "logit": -0.5,
      "confidence": 0.6
    },
    {
      "description": "RC multiplier of 2-3x applied to RC's projected ~20-22 full-month count suggests SA could reach 40-55",
      "supports": {
        "center": 45,
        "low": 40,
        "high": 55
      },
      "logit": 0.5,
      "confidence": 0.5
    },
    {
      "description": "Possible stats page methodology captures additional listings not on listing page (SPACs, micro-listings)",
      "supports": {
        "center": 44,
        "low": 40,
        "high": 55
      },
      "logit": 0.5,
      "confidence": 0.4
    }
  ],
  "tentative_estimate": {
    "center": 40,
    "low": 34,
    "high": 49
  },
  "anchor": "Historical May IPO counts on SA statistics page: May 2025 = 33, May 2024 = 14. 2026 has been more active than 2024 but variable. Current count of 26 through 65% of trading days points to ~40.",
  "assessment": "May 2026 already has 26 confirmed IPOs through May 19 on the Stock Analysis listing page, with 7 remaining trading days. At the observed daily rate of ~2.0 IPOs/day, linear projection gives ~40. IPOScoop shows 7 specific IPOs scheduled for May 20-21, suggesting the near-term pipeline is active. The Memorial Day holiday (May 25) will reduce activity in the final week.\n\nKey uncertainty: whether the SA statistics page will show a higher count than the listing page due to broader methodology. Evidence suggests the listing page is accurate for 2026 (2026 monthly figures described as \"in line\" with historical stats page ranges). The RC multiplier (2-3x) at current observed ratio of ~2.0x supports a full-month total of 40-44.\n\nMultiple estimation methods converge:\n- Linear projection: 40\n- MC Model (conservative): median 40\n- MC Model (with stats bonus): median 43\n- RC-based (2.0x): 40-44\n- RC-based (2.5x): 50-55\n\nCentral estimate: ~40-41, with right skew from the possibility of higher stats page counts.",
  "calibration_notes": "The floor is effectively 26 (current confirmed count), though practically it will be 30+ given known upcoming IPOs. The ceiling is plausibly 55-60 if the stats page methodology captures substantially more listings. The P10-P90 range of 34-49 spans ~15 units, which is reasonable given we're 65% through the month with 7 trading days of uncertainty.",
  "key_uncertainties": "1. Whether SA statistics page count matches listing page count for 2026 (biggest source of upside uncertainty). 2. IPO rate in the Memorial Day week (May 26-29). 3. Whether additional IPOs get retroactively added for earlier May dates.",
  "tool_audit": "fetch_url: Successfully retrieved data from stockanalysis.com/ipos/ (26 May entries), /ipos/2026/ (monthly breakdown), /ipos/2025/ and /ipos/2024/ (historical data, but likely undercount due to pagination). Statistics page fetch didn't show 2026 monthly breakdown. IPOScoop provided useful upcoming IPO calendar data. web_search returned relevant results. Code execution for Monte Carlo worked well.",
  "process_reflection": "The web scraping approach had a key limitation: the LLM-based extraction from paginated listing pages likely undercounted historical years (2025 showed 210 vs 347 actual). This created a confusing discrepancy that required significant analytical effort to resolve. For numeric IPO counting questions, having a direct API or structured data source would be much more efficient. The Monte Carlo simulation approach worked well once parameters were established. The multiple-model comparison was helpful for triangulating."
}
```

### 📋 Result

```
{"factor_count": 6, "factor_sum": 3.95, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Current confirmed count of 26 IPOs through May 19 on SA listing page establishes a hard floor",
"supports": {"center": 40.0, "low": 34.0, "high": 50.0}, "logit": 2.0, "confidence": 0.95, "effective_logit": 1.9}, {"description": "7 known upcoming IPOs from IPOScoop for May 20-21 (LCLN, BWGC, EMI,
OPTH, RIKU, CNXU, DRIL), ~80% likely to appear on SA", "supports": {"center": 32.0, "low": 30.0, "high": 34.0}, "logit": 1.5, "confidence": 0.8, "effective_logit": 1.2000000000000002}, {"description":
"Historical daily rate of ~2.0 IPOs/trading day extrapolated over 7 remaining trading days suggests ~14 more", "supports": {"center": 40.0, "low": 35.0, "high": 47.0}, "logit": 1.0, "confidence": 0.7,
"effective_logit": 0.7}, {"description": "Memorial Day (May 25) reduces activity in last week - some slowdown expected", "supports": {"center": 38.0, "low": 33.0, "high": 42.0}, "logit": -0.5,
"confidence": 0.6, "effective_logit": -0.3}, {"description": "RC multiplier of 2-3x applied to RC's projected ~20-22 full-month count suggests SA could reach 40-55", "supports": {"center": 45.0,
"low": 40.0, "high": 55.0}, "logit": 0.5, "confidence": 0.5, "effective_logit": 0.25}, {"description": "Possible stats page methodology captures additional listings not on listing page (SPACs, micro-
listings)", "supports": {"center": 44.0, "low": 40.0, "high": 55.0}, "logit": 0.5, "confidence": 0.4, "effective_logit": 0.2}], "dominant_factor": "Current confirmed count of 26 IPOs through May 19 on
SA listing page establishes a hard floor", "dominant_effective_logit": 1.9, "distribution_metrics": {"implied_median": 38.20879120879121, "implied_p10": 33.62637362637363, "implied_p90":
45.28571428571429, "median_gap": 1.7912087912087884, "median_gap_pct": 15.36286522148913, "spread_ratio": 1.2865221489161163, "precision": 0.375}, "sources": ["[(Metaculus) How many companies will be
listed as May 2026 IPOs on Stock Analysis's IPO Statistics page?](https://www.metaculus.com/questions/43543)", "[IPO Statistics and Charts](https://stockanalysis.com/ipos/statistics/)", "[200 Most
Recent IPOs](https://stockanalysis.com/ipos/)", "[All 2025 IPOs - A Complete List](https://stockanalysis.com/ipos/2025/)", "[All 2026 IPOs (so far](https://stockanalysis.com/ipos/2026/)", "[All 2024
IPOs - A Complete List](https://stockanalysis.com/ipos/2024/)", "[IPO Calendar - Upcoming IPOs](https://stockanalysis.com/ipos/calendar/)", "[IPO Calendar](https://www.iposcoop.com/ipo-calendar/)"]}
```

## 💬 Response

The reflection shows my tentative center (40) is ~5% above the factor-implied median (38.2), and my range is slightly wider than implied (spread_ratio 1.29). This seems reasonable given methodology uncertainty. Let me proceed to premortem.

## 🔧 Tool: mcp__premortem__premortem


```json
{
  "counterargument": "The strongest case against my median of ~40 has two variants:\n\n**Low side (actual ~30-33):** The current daily rate of 2.0/day is inflated by a cluster of SPACs and small listings in weeks 2-3 (13 IPOs in week of May 11-15 alone). This clustering is common - SPAC sponsors coordinate timing. The remaining days could see a sharp dropoff, especially around Memorial Day. Many of the IPOScoop-listed IPOs for May 20-21 could slip to June. The stats page might not update until early June and could use a slightly different cutoff that excludes some borderline cases. Historical precedent: months like March 2026 (13 IPOs) and March 2024 (10) show the rate CAN be very low.\n\n**High side (actual ~50-55):** The SA statistics page demonstrably counts MORE than the listing page (347 vs 210 for 2025 total). My assumption that this discrepancy is just a web-scraping artifact could be wrong - the stats page might genuinely include additional listing types. If the stats page captures ~1.5x what the listing shows, then 26 through May 19 implies ~39 already, projecting to ~55-60 full month. The RC ratio of 2-3x, applied to RC's projected ~22, gives SA up to 55-66. My Model C captures this but only at 20% weight.",
  "what_would_change_my_mind": "1. If I could directly verify the SA statistics page's current count for May 2026 (even a partial month figure) and it showed substantially different from 26, that would shift my estimate by 10+ units. 2. If the upcoming IPO calendar showed 10+ additional confirmed deals for May 26-29 (beyond what's on IPOScoop), that would push me up 5-10 points. 3. If IPOScoop-listed deals for May 20-21 started getting delayed/withdrawn, that would push me down 3-5 points. 4. If I could verify the 2025 stats page monthly breakdown independently (confirming whether 347 vs 210 is a methodology difference or web scraping artifact), that would significantly affect my estimate.",
  "confidence_in_estimate": 0.45
}
```

### 📋 Result

```
{"verdict": "approve", "assessment": "## Systematic Review\n\n### Factor verification against trace\n\n**Factor 1 (26 IPOs through May 19, logit=+2.0):** Verified. The fetch of
`stockanalysis.com/ipos/` returned exactly \"26 IPOs listed for May 2026\" with specific dates (May 1: 4, May 6: 2, May 7: 3, May 8: 3, May 13: 3, May 14: 5, May 15: 5, May 19: 1) and named tickers.
The 2026 page showed 25 (minor discrepancy the agent noted and discussed). Core claim is well-grounded.\n\n**Factor 2 (7 IPOScoop IPOs for May 20-21, logit=+1.5):** Verified. IPOScoop fetch returned
LCLN (May 20, priced), BWGC, EMI, OPTH, RIKU (week of May 21), CNXU, DRIL (Thursday May 21). Exactly 7 named IPOs match.\n\n**Factor 3 (2.0 IPOs/trading day rate, logit=+1.0):** Verified. 26/13 =
2.0/day, confirmed in Monte Carlo code output.\n\n**Factor 4 (Memorial Day slowdown, logit=-0.5):** Reasonable calendar-based inference. Not directly researched but well-known. Direction correct
(negative logit = downward pressure).\n\n**Factor 5 (RC 2-3x multiplier, logit=+0.5):** Verified. The question background text explicitly states \"Stock Analysis's broader methodology typically yields
counts roughly 2-3x higher than Renaissance Capital's.\" RC had 13 through May 17 per the question. Agent's projection of RC full-month ~20-22 is mathematically sound (13/12 \u2248 1.08/day \u00d7 8
remaining days \u2248 8.7 more).\n\n**Factor 6 (Stats page methodology bonus, logit=+0.5):** Grounded in real data \u2014 the agent found 2025 listing page showed 210 total vs stats page 347 total.
Appropriately given low confidence (0.4).\n\n### Double-counting check\nFactors 5 and 6 draw on overlapping evidence \u2014 the RC multiplier exists precisely because the stats page captures more
listing types. However, both have low logits (+0.5) and low confidence (0.5, 0.4), so combined impact is modest (~0.45 effective logits total). Minor issue, not forecast-changing.\n\n### Wrong-
direction factors\nNone found. All logit signs match descriptions.\n\n### Resolution criteria engagement\nThe agent fetched the actual statistics page (stockanalysis.com/ipos/statistics/) and found no
2026 monthly breakdown available yet. The agent correctly identified this as a key uncertainty and engaged thoroughly with the question of whether listing page counts will match the eventual stats
page figures. The agent's analysis that 2026 listing page numbers fall within the question's stated 18-37 range (without adjustment) is a sound inference that listing = stats for 2026.\n\n###
Probability assessment\nCenter of 40.0 with range 34.0-49.0. My independent estimate based on the evidence: 26 confirmed + ~5-6 from IPOScoop (80% of 7) + ~8-10 from 5 remaining trading days at
~1.6-2.0/day \u2248 39-42. This aligns well. The P10 of 34 (only +8 from floor) is conservative but defensible given Memorial Day slowdown risk. The P90 of 49 accounts for upside from stats page
methodology. No meaningful divergence from my assessment.\n\n### Counterargument quality\nSubstantive \u2014 identifies specific mechanisms (SPAC clustering, Memorial Day, stats page methodology, IPO
slippage), quantifies impacts, and names concrete evidence that would change the estimate. Passes.\n\n### Confidence assessment\n0.45 is reasonable given the methodology uncertainty about stats page
vs listing page and 7 remaining trading days of activity to estimate.\n\n### Tool audit consistency\nAgent claims successful fetches; metrics show 7 fetch_url calls with 0 errors. Consistent."}
```

## 💬 Response

Approved. Let me finalize my distribution, taking the best elements from my Monte Carlo models.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Final distribution: blend between conservative model and blended model\n# Conservative model median: 40, Blended model median: 43\n# I'll weight 60% conservative, 40% blended to get center ~41\n\nnp.random.seed(1111)\nn_sims = 300000\n\n# Use the conservative model with a slight upward adjustment for stats page uncertainty\ncurrent = 26\n\ntotal = np.zeros(n_sims, dtype=int)\nfor i in range(n_sims):\n    base = current\n    \n    # Small stats page bonus (0-3, modest)\n    stats_bonus = np.random.choice([0, 0, 1, 1, 2, 3])\n    \n    # Known upcoming (May 20-21): ~5-7 from IPOScoop + some SA extras\n    upcoming = np.random.binomial(7, 0.78) + np.random.poisson(1.0)\n    \n    # Remaining 5 trading days (May 22-29)\n    scenario = np.random.choice(['normal', 'slow', 'fast'], p=[0.50, 0.30, 0.20])\n    if scenario == 'normal':\n        rate = max(0.2, np.random.normal(1.6, 0.4))\n    elif scenario == 'slow':\n        rate = max(0.1, np.random.normal(0.9, 0.3))\n    else:\n        rate = max(0.3, np.random.normal(2.4, 0.5))\n    rest = np.random.poisson(rate * 5)\n    \n    # Retroactive additions\n    retro = np.random.choice([0, 1, 2], p=[0.6, 0.3, 0.1])\n    \n    total[i] = base + stats_bonus + upcoming + rest + retro\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(total, percentiles)\n\nprint(\"--- FINAL Distribution ---\")\nprint(f\"Mean: {np.mean(total):.1f}\")\nprint(f\"Median: {np.median(total):.1f}\")\nprint(f\"Std: {np.std(total):.1f}\")\nprint()\n\nfinal_pct = {}\nfor p, v in zip(percentiles, values):\n    final_pct[str(p)] = round(float(v))\n    print(f\"  P{p}: {v:.0f}\")\n\nprint(f\"\\nFinal percentile dict for submission:\")\nprint(final_pct)\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "--- FINAL Distribution ---\nMean: 41.9\nMedian: 41.0\nStd: 4.7\n\n  P1: 33\n  P5: 35\n  P10: 36\n  P20: 38\n  P25: 38\n  P30: 39\n  P40: 40\n  P50: 41\n  P60: 43\n  P70:
44\n  P75: 45\n  P80: 46\n  P90: 48\n  P95: 50\n  P99: 55\n\nFinal percentile dict for submission:\n{'1': 33, '5': 35, '10': 36, '20': 38, '25': 38, '30': 39, '40': 40, '50': 41, '60': 43, '70': 44,
'75': 45, '80': 46, '90': 48, '95': 50, '99': 55}\n", "stderr": "", "duration_ms": 4815}
```

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "May 2026 IPO count on Stock Analysis's statistics page. As of May 19, the SA listing page shows 26 confirmed IPOs for May 2026, with 7 remaining trading days (including Memorial Day on May 25). IPOScoop shows 7 additional IPOs scheduled for May 20-21. At the observed daily rate of ~2.0 IPOs/trading day, linear projection gives ~40. Multiple Monte Carlo models with different assumptions about the SA statistics page methodology, Memorial Day slowdown, and pipeline activity converge on a median of 40-43. The RC multiplier (2-3x on RC's ~20 projected) provides upside risk to ~50+. Center estimate: ~41, with P10-P90 of 36-48.",
  "anchor": "Historical May IPO counts on SA statistics page: May 2025 = 33, May 2024 = 14. 2026 has been more active (Jan-Apr avg 22.8 on listing page). Current partial-month count of 26 through 65% of trading days points to linear projection of ~40.",
  "factors": [
    {
      "description": "Current confirmed count of 26 IPOs through May 19 on SA listing page establishes a hard floor, with linear projection to ~40",
      "supports": {
        "center": 40,
        "low": 34,
        "high": 50
      },
      "logit": 2,
      "confidence": 0.95
    },
    {
      "description": "7 known upcoming IPOs from IPOScoop for May 20-21 (LCLN, BWGC, EMI, OPTH, RIKU, CNXU, DRIL), ~80% likely to appear on SA",
      "supports": {
        "center": 32,
        "low": 30,
        "high": 34
      },
      "logit": 1.5,
      "confidence": 0.8
    },
    {
      "description": "Historical daily rate of ~2.0 IPOs/trading day extrapolated over 7 remaining trading days suggests ~14 more additions",
      "supports": {
        "center": 40,
        "low": 35,
        "high": 47
      },
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Memorial Day (May 25) reduces activity in final week \u2014 some slowdown expected in May 26-29 window",
      "supports": {
        "center": 38,
        "low": 33,
        "high": 42
      },
      "logit": -0.5,
      "confidence": 0.6
    },
    {
      "description": "RC multiplier of 2-3x applied to RC's projected ~20-22 full-month count suggests SA could reach 40-55",
      "supports": {
        "center": 45,
        "low": 40,
        "high": 55
      },
      "logit": 0.5,
      "confidence": 0.5
    },
    {
      "description": "Possible stats page methodology captures additional listings not on listing page (SPACs, micro-listings added retroactively)",
      "supports": {
        "center": 44,
        "low": 40,
        "high": 55
      },
      "logit": 0.5,
      "confidence": 0.4
    }
  ],
  "percentile_values": {
    "1": 33,
    "5": 35,
    "10": 36,
    "20": 38,
    "25": 38,
    "30": 39,
    "40": 40,
    "50": 41,
    "60": 43,
    "70": 44,
    "75": 45,
    "80": 46,
    "90": 48,
    "95": 50,
    "99": 55
  }
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

## Forecast Summary

**Question:** How many companies will be listed as May 2026 IPOs on Stock Analysis's IPO Statistics page?

**Median estimate: 41 IPOs** (P10: 36, P90: 48)

### Key Evidence
- **26 confirmed IPOs** through May 19 on the SA listing page (hard floor)
- **7 additional IPOs** scheduled for May 20-21 per IPOScoop (LCLN, BWGC, EMI, OPTH, RIKU, CNXU, DRIL)
- **7 remaining trading days** (May 20-22, May 26-29; Memorial Day on May 25)
- **Daily rate of ~2.0 IPOs/day** observed so far in May
- **RC multiplier** of ~2x (13 RC IPOs through May 17 vs 26 SA) supports full-month total of 40-44

### Distribution Shape
The distribution is right-skewed, reflecting upside risk from the SA statistics page potentially capturing additional listings beyond what the listing page shows. The floor is effectively ~30 (current 26 + minimum known upcoming), and the plausible ceiling is ~55-60 if the stats page methodology adds significantly more.
