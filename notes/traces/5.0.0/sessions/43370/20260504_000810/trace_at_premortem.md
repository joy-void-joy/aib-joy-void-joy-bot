# Reasoning Log: What will the US April 2026 nonfarm payrolls figure be in the initial release?

*Generated: 2026-05-04T00:28:47.117624+00:00*


## 💭 Thinking

Let me analyze this forecasting question about US April 2026 nonfarm payrolls.

Key details:
- Question asks for the initially reported change in total nonfarm payroll employment for April 2026
- Release date: May 8, 2026
- Resolution: headline number from BLS Employment Situation Summary
- Units: thousands (e.g., 73,000 jobs = 73)
- Numeric bounds: -200 to 350, both open

Recent data points:
- January 2026: +160k (revised from +126k)
- February 2026: -133k (revised from -92k)


- March 2026: +178k (initial release)

Looking at the consensus forecasts, most estimates cluster around 70-73k for April, with the range spanning 60-75k. The March surge appears to be a temporary bump from healthcare workers returning after a strike, so underlying momentum seems to have cooled. I should dig deeper into what's driving these expectations.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


## 🔧 Tool: mcp__research__research


```json
{
  "post_id_list": [
    43370
  ]
}
```

### 📋 Result

```
{"post_id": 43370, "title": "What will the US April 2026 nonfarm payrolls figure be in the initial release?", "type": "numeric", "url": "https://www.metaculus.com/questions/43370", "background_info":
"The U.S. Bureau of Labor Statistics (BLS) publishes the monthly Employment Situation report, whose headline number is the change in total nonfarm payroll employment (seasonally adjusted) from the
prior month. The April 2026 report is scheduled for release on **Friday, May 8, 2026 at 8:30 a.m. ET** ([BLS release schedule](https://www.bls.gov/schedule/news_release/empsit.htm)).\n\nRecent monthly
prints have been unusually volatile:\n- January 2026: +160,000 (revised from +126,000)\n- February 2026: \u2212133,000 (revised from \u221292,000)\n- March 2026: +178,000 (initial release,
USDL-26-0580)\n\nThe unemployment rate stood at 4.3% in March 2026. Consensus forecasts for April 2026 ahead of the release cluster in the +60,000 to +75,000 range (Trading Economics ~70k;
Investing.com ~73k), reflecting expectations that March's surge \u2014 partly driven by health-care strike returns \u2014 was a one-off and underlying job growth has slowed.\n\nThis question asks
about the **initially reported** April 2026 figure for total nonfarm payroll employment change, not any later revision.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 4,
\"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves to the change in total nonfarm payroll employment (seasonally adjusted) for April 2026, in
thousands of jobs, as first reported by the Bureau of Labor Statistics in the Employment Situation news release scheduled for May 8, 2026.\n\nThe figure will be taken from the lead summary of the BLS
Employment Situation Summary published at https://www.bls.gov/news.release/empsit.nr0.htm (the headline sentence of the form \"Total nonfarm payroll employment [rose/fell] by X in April\"). Report the
value in thousands \u2014 for example, a reported gain of 73,000 jobs resolves as **73**; a reported loss of 50,000 jobs resolves as **\u221250**.\n\nOnly the initial release counts; subsequent
revisions in later monthly reports are ignored. If the May 8, 2026 release is delayed, the value from the first BLS Employment Situation release covering April 2026 reference-month data published
before May 17, 2026 will be used. If no such release occurs before May 17, 2026, the question resolves N/A.", "fine_print": "If the BLS website is temporarily unavailable, the same figure as reported
by [credible sources](https://www.metaculus.com/faq/#definitions) citing the BLS Employment Situation release will be used.", "num_forecasters": 8, "community_prediction": null, "lower_bound": -200.0,
"upper_bound": 350.0}
```

```json
{
  "questions": [
    {
      "query": "US April 2026 nonfarm payrolls forecast consensus estimates May 2026",
      "ttl": "6h"
    },
    {
      "query": "US labor market conditions April 2026 tariffs impact employment layoffs",
      "ttl": "6h"
    },
    {
      "query": "Historical nonfarm payrolls surprise distribution - how much do initial releases deviate from consensus forecasts",
      "ttl": "3d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "US April 2026 nonfarm payrolls forecast consensus estimates May 2026", "entry": {"slug": "us-april-2026-nonfarm-payrolls-forecast-consensus-e811bccd", "query": "US April 2026
nonfarm payrolls forecast consensus estimates May 2026", "answer": "I apologize, but I'm unable to access web search, web fetch, or tool search capabilities in this session. All of my external data-
gathering tools are currently unavailable, which means I cannot retrieve current consensus estimates for the US April 2026 nonfarm payrolls report.\n\nLet me provide what I can based on my training
knowledge and the typical structure of this data release:\n\n## US April 2026 Nonfarm Payrolls \u2014 Research Limitations\n\n### What I Know Structurally:\n- The **Bureau of Labor Statistics (BLS)**
releases the Employment Situation report (which includes nonfarm payrolls) on the **first Friday of the following month**. For April 2026 data, this would be released on **Friday, May 1, 2026** (or
the first Friday in May).\n- Consensus estimates are typically compiled by organizations like **Bloomberg, Reuters, MarketWatch, and the Wall Street Journal** via economist surveys in the days leading
up to the release.\n- Key metrics reported include: total nonfarm payrolls change (in thousands), unemployment rate (%), average hourly earnings (month-over-month and year-over-year), and labor force
participation rate.\n\n### What I Cannot Provide:\n- The actual consensus estimate number for April 2026 NFP\n- The range of economist forecasts\n- Recent trend data from early 2026 payroll reports\n-
Any revisions to prior months\n\n### Typical Context for Forecasting:\n- In recent years (2023-2025), monthly NFP gains have generally ranged from ~100K to ~300K depending on economic conditions\n-
Consensus estimates are influenced by leading indicators such as ADP private payrolls, initial jobless claims trends, ISM employment indices, and the JOLTS report\n\n---\n\n**I strongly recommend
consulting the following sources for current data:**\n- Bloomberg Terminal economic calendar\n- Reuters economic polls\n- Trading Economics (tradingeconomics.com)\n- Investing.com economic calendar\n-
The Wall Street Journal economic forecasting survey\n\nI cannot fulfill this research request with the required rigor given my tool limitations. The caller should retry when web access is restored or
use an alternative data source.", "sources": [], "key_facts": ["The BLS Employment Situation report for April 2026 is scheduled for release on the first Friday of May 2026 (likely May 1, 2026)",
"Consensus estimates are compiled by Bloomberg, Reuters, and WSJ via economist surveys typically in the week before release", "Key metrics include total nonfarm payrolls change (thousands),
unemployment rate, average hourly earnings, and labor force participation rate", "RESEARCH INCOMPLETE: All web search and fetch tools were unavailable; no current consensus estimate could be
retrieved", "In 2023-2025, monthly NFP gains generally ranged from approximately 100K to 300K depending on economic conditions"], "data_points": [], "created_at": "2026-05-04T00:09:12.111507Z",
"updated_at": "2026-05-04T00:09:12.111507Z", "stale_after": "2026-05-04T06:09:12.111507Z", "state": "fresh", "revision_history": [], "session_id": "adadb8e8-985c-4b20-aa6a-cefe573aa2a3",
"follow_up_count": 0}, "is_follow_up": false}, {"query": "US labor market conditions April 2026 tariffs impact employment layoffs", "entry": {"slug": "us-labor-market-conditions-april-2026-tariffs-
impa-d00eec2b", "query": "US labor market conditions April 2026 tariffs impact employment layoffs", "answer": "Now I have extensive data. Let me compile the final research report.\n\n---\n\n# US Labor
Market Conditions \u2014 April/May 2026: Tariff Impact on Employment & Layoffs\n\n## Executive Summary\n\nThe US labor market in early 2026 exhibits a paradoxical \"low-hire, low-fire\" equilibrium.
While initial jobless claims hit a 56-year low (189,000 in the week ending April 25) and the unemployment rate moderated to 4.3% in March, hiring has slowed to pandemic-era lows and tariff-exposed
industries\u2014particularly manufacturing and transportation\u2014have hemorrhaged jobs. The economy lost 189,600 blue-collar jobs in the 10 months following \"Liberation Day\" (April 2, 2025). The
labor market remains under pressure from overlapping shocks: tariffs, the Iran war (begun February 28, 2026), federal workforce reductions (DOGE), and AI-driven restructuring.\n\n---\n\n## 1. Latest
Employment Situation Data\n\n### March 2026 (released April 3, 2026)\n- **Nonfarm payrolls: +178,000** \u2014 the largest gain in 15 months, far above consensus of ~60,000\n- **Unemployment rate:
4.3%**, down from 4.4% in February\n- **Average hourly earnings: +0.4% m/m to $37.32**\n\n### February 2026 (released March 6, 2026)\n- **Nonfarm payrolls: -92,000** \u2014 an unexpected loss;
consensus was +60,000\n- **Unemployment rate: 4.4%**\n- January payrolls revised down from +130,000 to +126,000\n\n### January 2026 (released February 11, 2026)\n- **Nonfarm payrolls: +130,000**
(later revised to +126,000)\n- **Unemployment rate: 4.3%**\n- 2025 benchmark revisions revealed employers added **fewer than 200,000 jobs in all of 2025** (vs. ~1.5 million in 2024)\n\n### April 2026
Report\n- Scheduled for release **May 2, 2026** \u2014 data not yet confirmed in my sources.\n\n---\n\n## 2. Initial Jobless Claims\n\n### Week Ending April 25, 2026\n- **Initial claims: 189,000**
\u2014 a plunge of 26,000, the **lowest since September 1969**\n- **4-week moving average: 207,500**\n- **Continuing claims: 1.79 million** (week ending April 18)\n\n### Recent Weekly Trajectory\n|
Week Ending | Initial Claims |\n|-------------|---------------|\n| Apr 25, 2026 | 189,000 |\n| Apr 11, 2026 | 207,000 |\n| Mar 22, 2026 | 210,000 |\n| Mar 15, 2026 | 205,000 |\n\nHFE Chief Economist
Carl Weinberg cautioned: *\"There is nothing to worry about in this report. YET! At some point, elevated energy costs and prices for materials will cause firms to lay off marginal workers to protect
profit margins.\"*\n\n---\n\n## 3. JOLTS Data \u2014 Job Openings & Hiring\n\n### February 2026 (released March 31, 2026)\n- **Job openings: 6.9 million** \u2014 a larger-than-expected decline\n-
**Hiring fell to the lowest level since the pandemic**\n- Layoffs edged down\n\n### December 2025 (released February 5, 2026)\n- **Job openings dropped to the lowest level since 2020**\n- Layoffs
edged up\n\n**Key dynamic:** The \"low-hire, low-fire\" paradox \u2014 employers aren't laying off workers, but they're barely hiring either. Those who lose their jobs face historically long search
times.\n\n---\n\n## 4. Tariff Impact on Employment by Sector\n\n### Manufacturing\n- **89,000 manufacturing jobs lost** in the 10 months following \"Liberation Day\" (April 2, 2025 \u2013 February
2026)\n- Equivalent to approximately **2,800 average-size factory closures** (Center for American Progress)\n- Manufacturing activity contracted for **8 consecutive months** post-Liberation Day\n\n###
Transportation & Warehousing\n- **123,700 jobs lost** in the same 10-month period\n- Challenger data: **703% year-over-year increase** in Q1 2026 transportation job cuts \u2014 highest Q1 on
record\n\n### Total Blue-Collar Jobs\n- **189,600 blue-collar jobs lost since Liberation Day**\n- In **45 of 50 states**, blue-collar job creation under tariffs fell short of Biden-era annual
averages\n- Average state lost 2,500+ blue-collar jobs vs. average annual gain of 7,400 previously\n\n---\n\n## 5. Announced Layoffs (Challenger Data)\n\n### Q1 2026 Totals: 217,362 job cuts
announced\n- Down 56% from Q1 2025 (497,052, which included massive federal workforce cuts)\n- Down 16% from Q4 2025 (259,948)\n\n### Q1 2026 by Industry\n| Industry | Q1 2026 Cuts | YoY Change
|\n|----------|-------------|------------|\n| Technology | 52,050 | +40% |\n| Transportation | 32,241 | +703% (record) |\n| Healthcare | 23,520 | Record Q1 |\n| Education | 11,467 | +170% |\n|
Financial | 9,397 | -41% |\n\n### March 2026 specifically\n- **60,620 job cuts** \u2014 up 25% from February's 48,307\n- **AI was the leading cited reason** for job cuts in March\n\n### Notable
Company Actions (2026)\n- **Whirlpool:** 341 layoffs at Amana, Iowa facility (Feb 2026), despite being a vocal tariff supporter \u2014 moved production to China\n- **Harley-Davidson:** Worldwide
layoffs began March 2026; profits fell 26% as \"tariffs erase profits\"\n- **Amazon:** ~16,000 corporate job cuts (Jan 2026)\n- **Nike:** 775 employees cut, accelerated automation (Jan 2026)\n-
**Morgan Stanley, Block, UPS, Dell, Oracle, Meta:** All announced cuts in early 2026\n\n---\n\n## 6. Federal Reserve Assessment\n\n### April 28-29, 2026 FOMC Decision (most recent)\n- **Rate held at
3.50%-3.75%**\n- **4 dissents** \u2014 highest since October 1992 (33+ years)\n- Statement cited \"solid economic activity, low job gains, and elevated uncertainty including from the Middle East
conflict and energy prices\"\n- Likely **Powell's final meeting as Chair** (term ends May 2026)\n\n### Key Fed Forecasts (March 2026 SEP)\n- Unemployment: **4.4% by year-end 2026**\n- Core PCE
inflation: **2.7%** (raised from 2.5%)\n- GDP growth: **2.4%**\n\n### Market Expectations\n- Fed funds futures: **No cuts priced through at least July 2026**\n- J.P. Morgan: Predicts **zero cuts in
all of 2026**\n\n---\n\n## 7. Consumer Confidence & Broader Context\n\n### University of Michigan Consumer Sentiment\n| Month | Index | Notes |\n|-------|-------|-------|\n| Jan 2026 | 56.4 | Well
below neutral (80) |\n| Feb 2026 | 56.6 | |\n| Mar 2026 | 55.5 | Lowest of 2026 |\n\n### Broader Macro Context\n- **Q1 2026 GDP: 2.0%** (advance estimate, April 30)\n- **CPI inflation: 3.3% y/y**
(March 2026)\n- **PCE inflation: 3.5% y/y** (March 2026)\n- **Core PCE: 3.2%** (March 2026)\n- **Gas prices: ~$4.30/gallon** (national average, late April)\n- **Oil: ~$104/barrel**\n- **US tariff
rates ended 2025 above 15%** (up from ~2.5% at start of 2025), with limited deescalation expected\n- **Goldman Sachs recession probability: 30%** over next 12 months\n- **Small-business bankruptcies
up 10%** over past year; large corporate bankruptcies at highest since 2010\n\n---", "sources": [{"url": "https://www.bls.gov/news.release/empsit.nr0.htm", "title": "Bureau of Labor Statistics
Employment Situation Summary", "domain": "bls.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "March 2026: Nonfarm payrolls +178,000; unemployment rate 4.3%; average hourly earnings +0.4% to
$37.32"}, {"url": "https://fred.stlouisfed.org/series/PAYEMS", "title": "FRED Total Nonfarm Payrolls (PAYEMS)", "domain": "fred.stlouisfed.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet":
"Total nonfarm payrolls at 158,637K as of March 2026, last updated 2026-04-03"}, {"url": "https://fred.stlouisfed.org/series/UNRATE", "title": "FRED Unemployment Rate (UNRATE)", "domain":
"fred.stlouisfed.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Unemployment rate 4.3% in March 2026"}, {"url": "https://www.dol.gov/ui/data.pdf", "title": "Department of Labor Unemployment
Insurance Weekly Claims", "domain": "dol.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Initial claims 189,000 for week ending April 25, 2026 \u2014 lowest since September 1969"}, {"url":
"https://www.bls.gov/news.release/jolts.nr0.htm", "title": "BLS Job Openings and Labor Turnover Survey (JOLTS)", "domain": "bls.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Job openings
fell to 6.9 million in February 2026; hiring at lowest level since pandemic"}, {"url": "https://www.challengergray.com/", "title": "Challenger, Gray & Christmas Job Cuts Report", "domain":
"challengergray.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Q1 2026: 217,362 job cuts announced; March 60,620 cuts (+25% from Feb); AI leading cited reason; transportation +703% YoY"},
{"url": "https://www.americanprogress.org/", "title": "Center for American Progress: One Year After Liberation Day", "domain": "americanprogress.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet":
"189,600 blue-collar jobs lost since Liberation Day: 89,000 manufacturing + 123,700 transportation/warehousing"}, {"url": "https://www.cnbc.com/", "title": "CNBC: Fed holds rates with highest dissent
since 1992", "domain": "cnbc.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Fed held rates at 3.50-3.75% at April 28-29 meeting with 4 dissents, highest since October 1992"}, {"url":
"https://www.reuters.com/", "title": "Reuters: US labor market posts largest jobs gain in 15 months", "domain": "reuters.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "March 2026 +178K
payrolls described as largest gain in 15 months; weekly claims at 50+ year low"}, {"url": "https://www.sca.isr.umich.edu/", "title": "University of Michigan Surveys of Consumers", "domain":
"sca.isr.umich.edu", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Consumer sentiment fell to 55.5 in March 2026, lowest reading of the year"}, {"url": "https://www.bea.gov/data/gdp/gross-
domestic-product", "title": "BEA Gross Domestic Product", "domain": "bea.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Q1 2026 real GDP grew 2.0% annualized (advance estimate released April
30)"}, {"url": "https://www.bea.gov/data/personal-consumption-expenditures-price-index", "title": "BEA Personal Consumption Expenditures Price Index", "domain": "bea.gov", "accessed_at":
"2026-05-04T00:00:00Z", "snippet": "PCE inflation 3.5% y/y in March 2026; core PCE 3.2% \u2014 biggest increase in nearly 3 years"}, {"url": "https://finance.yahoo.com/news/stock-market-flashes-
warning-investors-084500526.html", "title": "Yahoo Finance: Stock Market Warning \u2014 Tariff Impact", "domain": "finance.yahoo.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Since tariffs
took effect, unemployment reached 4-year high, jobs growth slowed dramatically, consumer sentiment at record low"}, {"url": "https://www.cnbc.com/2026/01/12/trumps-tariffs-trigger-rising-rate-of-job-
layoffs-inside-supply-chain.html", "title": "CNBC: Tariffs trigger rising rate of job layoffs inside supply chain", "domain": "cnbc.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "ASCM/CNBC
survey found tariffs causing rising layoff rates across supply chain and logistics sector"}, {"url": "https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm", "title": "Federal Reserve FOMC
Calendar and Statements", "domain": "federalreserve.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "April 28-29, 2026: Rate held at 3.50-3.75%; cited 'solid economic activity, low job gains,
elevated uncertainty'"}, {"url": "https://gasprices.aaa.com/", "title": "AAA Gas Prices", "domain": "gasprices.aaa.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "National average gas price
~$4.30/gallon as of late April 2026"}, {"url": "https://equitablegrowth.org/tariffs-pose-real-risks-to-the-u-s-labor-market/", "title": "Equitable Growth: Tariffs pose real risks to the US labor
market", "domain": "equitablegrowth.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Trade policy uncertainty making it difficult to assess labor conditions; tariffs creating structural labor
market risks"}, {"url": "https://www.opb.org/article/2026/03/06/us-lost-surprising-92000-jobs-unemployment-rate-ticks-higher/", "title": "OPB: US lost surprising 92,000 jobs, unemployment rate ticks
higher", "domain": "opb.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "February 2026 payrolls fell by 92,000, far worse than expected +60,000; unemployment rose to 4.4%"}], "key_facts": ["US
nonfarm payrolls rose by +178,000 in March 2026 (released April 3), the largest gain in 15 months, far above consensus of ~60,000", "US unemployment rate was 4.3% in March 2026, down from 4.4% in
February", "February 2026 nonfarm payrolls fell by -92,000, a shocking miss against consensus of +60,000", "Initial jobless claims fell to 189,000 for week ending April 25, 2026 \u2014 the lowest
level since September 1969", "Continuing claims stood at 1.79 million for week ending April 18, 2026", "JOLTS job openings fell to 6.9 million in February 2026; hiring reached the lowest level since
the pandemic", "189,600 blue-collar jobs lost in the 10 months following Liberation Day (April 2, 2025), including 89,000 manufacturing and 123,700 transportation/warehousing jobs", "Challenger
reported 217,362 job cuts in Q1 2026; transportation cuts surged 703% YoY to record levels", "AI was the leading cited reason for job cuts in March 2026 (60,620 cuts announced, up 25% from February)",
"The Federal Reserve held rates at 3.50%-3.75% at the April 28-29 FOMC meeting with 4 dissents \u2014 the highest dissent level since 1992", "The Fed's March 2026 SEP projected year-end unemployment
at 4.4% and core PCE inflation at 2.7%", "US employers added fewer than 200,000 jobs in all of 2025 per benchmark revisions, down from ~1.5 million in 2024", "University of Michigan consumer sentiment
fell to 55.5 in March 2026, the lowest reading of the year", "Q1 2026 GDP grew at 2.0% (advance estimate), below expectations", "PCE inflation reached 3.5% year-over-year in March 2026, the biggest
increase in nearly 3 years", "Gas prices averaged ~$4.30/gallon nationally by late April 2026; oil at ~$104/barrel", "Goldman Sachs raised US recession probability to 30% over the next 12 months",
"Whirlpool laid off 341 workers while moving production to China; Harley-Davidson began worldwide layoffs as tariffs erased profits", "In 45 of 50 states, blue-collar job creation under tariffs fell
short of Biden-era annual averages", "J.P. Morgan predicts zero Fed rate cuts through all of 2026; fed funds futures price no change through at least July"], "data_points": [{"metric": "Nonfarm
Payrolls Change (March 2026)", "value": 178000.0, "unit": "jobs", "as_of": "2026-03-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Nonfarm Payrolls Change (February
2026)", "value": -92000.0, "unit": "jobs", "as_of": "2026-02-28", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Nonfarm Payrolls Change (January 2026)", "value":
126000.0, "unit": "jobs (revised)", "as_of": "2026-01-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Unemployment Rate (March 2026)", "value": 4.3, "unit":
"percent", "as_of": "2026-03-31", "source_url": "https://fred.stlouisfed.org/series/UNRATE"}, {"metric": "Unemployment Rate (February 2026)", "value": 4.4, "unit": "percent", "as_of": "2026-02-28",
"source_url": "https://fred.stlouisfed.org/series/UNRATE"}, {"metric": "Initial Jobless Claims (week ending Apr 25)", "value": 189000.0, "unit": "claims", "as_of": "2026-04-25", "source_url":
"https://www.dol.gov/ui/data.pdf"}, {"metric": "Continuing Claims (week ending Apr 18)", "value": 1790000.0, "unit": "claims", "as_of": "2026-04-18", "source_url": "https://www.dol.gov/ui/data.pdf"},
{"metric": "4-Week Moving Average Initial Claims", "value": 207500.0, "unit": "claims", "as_of": "2026-04-25", "source_url": "https://www.dol.gov/ui/data.pdf"}, {"metric": "JOLTS Job Openings
(February 2026)", "value": 6900000.0, "unit": "openings", "as_of": "2026-02-28", "source_url": "https://www.bls.gov/news.release/jolts.nr0.htm"}, {"metric": "Challenger Job Cuts Q1 2026", "value":
217362.0, "unit": "announced cuts", "as_of": "2026-03-31", "source_url": "https://www.challengergray.com/"}, {"metric": "Challenger Job Cuts March 2026", "value": 60620.0, "unit": "announced cuts",
"as_of": "2026-03-31", "source_url": "https://www.challengergray.com/"}, {"metric": "Manufacturing Jobs Lost Since Liberation Day", "value": -89000.0, "unit": "jobs", "as_of": "2026-02-28",
"source_url": "https://www.americanprogress.org/"}, {"metric": "Transportation/Warehousing Jobs Lost Since Liberation Day", "value": -123700.0, "unit": "jobs", "as_of": "2026-02-28", "source_url":
"https://www.americanprogress.org/"}, {"metric": "Total Blue-Collar Jobs Lost Since Liberation Day", "value": -189600.0, "unit": "jobs", "as_of": "2026-02-28", "source_url":
"https://www.americanprogress.org/"}, {"metric": "Federal Funds Rate", "value": 3.625, "unit": "percent (midpoint of 3.50-3.75%)", "as_of": "2026-04-29", "source_url":
"https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm"}, {"metric": "Q1 2026 Real GDP Growth (advance)", "value": 2.0, "unit": "percent annualized", "as_of": "2026-03-31", "source_url":
"https://www.bea.gov/data/gdp/gross-domestic-product"}, {"metric": "PCE Inflation Year-over-Year (March 2026)", "value": 3.5, "unit": "percent", "as_of": "2026-03-31", "source_url":
"https://www.bea.gov/data/personal-consumption-expenditures-price-index"}, {"metric": "Core PCE Inflation Year-over-Year (March 2026)", "value": 3.2, "unit": "percent", "as_of": "2026-03-31",
"source_url": "https://www.bea.gov/data/personal-consumption-expenditures-price-index"}, {"metric": "CPI Inflation Year-over-Year (March 2026)", "value": 3.3, "unit": "percent", "as_of": "2026-03-31",
"source_url": "https://www.bls.gov/cpi/"}, {"metric": "Average Hourly Earnings (March 2026)", "value": 37.32, "unit": "USD", "as_of": "2026-03-31", "source_url":
"https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "University of Michigan Consumer Sentiment (March 2026)", "value": 55.5, "unit": "index", "as_of": "2026-03-31", "source_url":
"https://www.sca.isr.umich.edu/"}, {"metric": "National Average Gas Price (late April 2026)", "value": 4.3, "unit": "USD per gallon", "as_of": "2026-04-30", "source_url":
"https://gasprices.aaa.com/"}, {"metric": "US Crude Oil Price (late April 2026)", "value": 104.0, "unit": "USD per barrel", "as_of": "2026-04-30", "source_url":
"https://www.reuters.com/markets/commodities/"}, {"metric": "Total Jobs Added in All of 2025 (revised)", "value": 200000.0, "unit": "jobs (fewer than)", "as_of": "2025-12-31", "source_url":
"https://fred.stlouisfed.org/series/PAYEMS"}, {"metric": "Goldman Sachs Recession Probability (12-month)", "value": 30.0, "unit": "percent", "as_of": "2026-03-31", "source_url":
"https://www.goldmansachs.com/"}], "created_at": "2026-05-04T00:21:30.657920Z", "updated_at": "2026-05-04T00:21:30.657920Z", "stale_after": "2026-05-04T06:21:30.657920Z", "state": "fresh",
"revision_history": [], "session_id": "1e862ff3-c6c9-452c-bbda-4cc328d8b4d4", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Historical nonfarm payrolls surprise distribution - how much do
initial releases deviate from consensus forecasts", "entry": {"slug": "historical-nonfarm-payrolls-surprise-distribution-b42c217c", "query": "Historical nonfarm payrolls surprise distribution - how
much do initial releases deviate from consensus forecasts", "answer": "Now let me compile and cross-validate the findings from all three research agents. One agent was able to pull actual FRED data
showing the most recent payrolls levels and revisions, which is extremely valuable. Let me synthesize everything into a comprehensive report.\n\n---\n\n# Historical Nonfarm Payrolls Surprise
Distribution: How Initial Releases Deviate from Consensus Forecasts\n\n## 1. Overview\n\nThe \"NFP surprise\" \u2014 the difference between the Bureau of Labor Statistics' initial nonfarm payrolls
release and the median economist consensus forecast (typically compiled by Bloomberg/Reuters from 60\u201380 economists) \u2014 is one of the most closely watched economic data points in financial
markets. This report synthesizes historical statistics, recent data, and revision patterns.\n\n## 2. Surprise Distribution Statistics\n\n### Pre-COVID Era (2010\u20132019, ~120 months)\n\n| Metric |
Value |\n|--------|-------|\n| Mean surprise (Actual \u2212 Consensus) | +5K to +10K |\n| Median surprise | ~+5K |\n| Standard deviation | ~60K\u201375K |\n| Interquartile range | \u221230K to +50K
|\n| 90th percentile range | \u221290K to +120K |\n| Largest positive surprise | ~+200K |\n| Largest negative surprise | ~\u2212150K |\n\n### Post-COVID Era (2021\u20132024)\n\n| Metric | Value
|\n|--------|-------|\n| Mean surprise | +40K to +60K |\n| Standard deviation | ~90K\u2013120K |\n| Systematic pattern | Persistent under-prediction by consensus |\n\n### Full Sample (2000\u20132024,
excluding COVID months Mar\u2013Jun 2020)\n\n| Metric | Value |\n|--------|-------|\n| Mean surprise | +10K to +15K |\n| Median surprise | ~+8K |\n| Standard deviation | ~70K\u201385K |\n| Mean
absolute forecast error | ~65K\u201375K |\n| Median absolute forecast error | ~47K |\n| Distribution shape | Roughly normal, positive skew, fat tails (leptokurtic) |\n| Months with surprise > 100K |
~15\u201320% |\n| Surprises > 2\u03c3 frequency | ~8\u201310% (vs. 5% for normal distribution) |\n\n## 3. Recent Monthly Surprise Data\n\n### 2024 (Initial Releases vs. Consensus)\n\n| Month | Actual
(K) | Consensus (K) | Surprise (K) |\n|-------|-----------|---------------|-------------|\n| Jan 2024 | +353 | +185 | **+168** |\n| Feb 2024 | +275 | +198 | +77 |\n| Mar 2024 | +303 | +200 | +103 |\n|
Apr 2024 | +175 | +243 | \u221268 |\n| May 2024 | +272 | +185 | +87 |\n| Jun 2024 | +206 | +191 | +15 |\n| Jul 2024 | +114 | +176 | \u221262 |\n| Aug 2024 | +142 | +164 | \u221222 |\n| Sep 2024 | +254
| +150 | **+104** |\n| Oct 2024 | +12 | +113 | **\u2212101** |\n| Nov 2024 | +227 | +200 | +27 |\n| Dec 2024 | +256 | +160 | +96 |\n\n**2024 Summary:** Mean surprise = +35K; Median = +51K; Std dev =
~85K; 8 of 12 months were positive surprises.\n\n### 2025\u20132026 (From FRED Vintage Data)\n\n| Month | Initial Release (K) | Consensus (K) | Notes
|\n|-------|-------------------|---------------|-------|\n| Jan 2025 | +143 | ~+170 | \u221227K miss |\n| Feb 2025 | +151 | \u2014 | Revised dramatically to +42K |\n| Mar 2025 | +228 | \u2014 |
Revised to +67K |\n| Jan 2026 | +130 | +70 | +60K beat |\n| Feb 2026 | \u221292 | \u2014 | Large negative surprise |\n| Mar 2026 | +178 | \u2014 | Released Apr 3, 2026 |\n\n## 4. Systematic Bias:
Surprises Skew Positive in Expansions\n\nThere is strong evidence that NFP surprises are **regime-dependent**:\n\n| Economic Regime | Mean Surprise | Notes
|\n|----------------|--------------|-------|\n| Steady expansion | +5K to +15K | Mild positive bias |\n| Early recovery | +30K to +80K | Strong positive bias |\n| Late cycle/slowdown | \u221210K to
+5K | Roughly unbiased |\n| Recession | \u221250K to \u2212100K | Negative bias |\n\nOver multi-year samples, NFP beats consensus roughly **55\u201360%** of the time.\n\n## 5. Consensus Forecast
Dispersion\n\nThe spread among individual economist forecasts provides context on uncertainty:\n\n| Period | IQR of Forecasts | Full Range | Std Dev of Forecasts
|\n|--------|-----------------|------------|---------------------|\n| 2015\u20132019 | 40K\u201360K | 120K\u2013180K | 25K\u201340K |\n| 2021\u20132024 | 60K\u2013100K | 200K\u2013350K | 40K\u201370K
|\n\nWider forecast dispersion correlates with larger absolute surprises.\n\n## 6. Revision Patterns: Initial Releases Are Noisy\n\n### Standard Monthly Revisions\n\n| Metric | Value
|\n|--------|-------|\n| Mean first revision (1 month later) | +10K to +15K |\n| Mean cumulative revision (2 months later) | +20K to +30K |\n| Std dev of first revision | ~30K\u201340K |\n| Std dev of
cumulative revision | ~45K\u201355K |\n| Share of first revisions that are positive | ~55\u201360% |\n\n### Annual Benchmark Revisions (Applied Each February)\n\nThe BLS incorporates comprehensive
QCEW data, producing often-massive benchmark revisions:\n\n| Year | Benchmark Revision (K) |\n|------|----------------------|\n| 2024 (ref Mar 2024) | **\u2212818K** |\n| 2023 (ref Mar 2023) |
\u2212187K |\n| 2022 (ref Mar 2022) | \u2212306K |\n| 2021 (ref Mar 2021) | +462K |\n| 2019 (ref Mar 2019) | \u2212514K |\n| 2009 (ref Mar 2009) | \u2212617K |\n| **Mean absolute benchmark revision
(2004\u20132024)** | **266K** |\n\n### The 2025\u20132026 Benchmark Revision Was Historically Extreme\n\nFRED vintage data reveals that the February 2026 benchmark revision revised 2025 employment
levels **downward by approximately 1 million jobs** on average across all 2025 months:\n\n- Initial reports for 2025 showed average monthly gains of ~+103K\n- Revised data shows average monthly gains
of only ~+10K\n- Individual monthly revisions ranged from \u22129K to **\u2212167K** (June 2025)\n- 12 of 13 months examined were revised downward\n\n## 7. Academic Literature\n\nKey studies on NFP
data quality and forecast accuracy:\n\n- **Aruoba (2008)** \u2013 \"Data Revisions Are Not Well Behaved\" (Philadelphia Fed): Initial BLS releases are noisy and systematically revised upward during
expansions.\n- **Gilbert et al. (2017)** \u2013 Nonfarm payrolls initial releases revised ~+30K on average over two subsequent revisions, with std dev of ~45K\u201355K.\n- **Swanson & van Dijk
(2006)** \u2013 Found slight downward bias in initial releases (revisions tend to be positive), questioning rationality of initial estimates.\n- **NY Fed/Philadelphia Fed research** \u2013 NFP
surprise is the single most important driver of intraday Treasury, equity, and FX price moves on release day.\n\n## 8. Key Takeaways for Modeling\n\n1. **Standard deviation of ~70\u201385K** is the
appropriate baseline for the surprise distribution in normal times; use ~90\u2013120K in high-uncertainty periods.\n2. **Positive bias of ~+10\u201315K** exists on average (actual tends to beat
consensus in expansions).\n3. **Fat tails**: Extreme surprises (>2\u03c3) occur ~8\u201310% of the time vs. 5% expected under normality.\n4. **Revisions are large**: Cumulative revisions average +25K
with std dev ~48K, and annual benchmark revisions can reach hundreds of thousands.\n5. **The initial release is a poor measure of \"truth\"**: The 2025 experience (initially reported ~+103K/month,
revised to ~+10K/month) shows initial data can be dramatically misleading.\n6. **Regime matters**: The surprise distribution shifts substantially across economic regimes.\n\n---", "sources": [{"url":
"https://www.bls.gov/news.release/empsit.nr0.htm", "title": "Bureau of Labor Statistics - Employment Situation Summary", "domain": "bls.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Primary
source for monthly nonfarm payrolls initial releases. Historical releases used to compute surprise distributions."}, {"url": "https://fred.stlouisfed.org/series/PAYEMS", "title": "FRED - All
Employees, Total Nonfarm (PAYEMS)", "domain": "fred.stlouisfed.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "FRED vintage data showing PAYEMS levels through March 2026 (last updated
2026-04-03). Used to compute monthly change revisions and benchmark impacts."}, {"url": "https://alfred.stlouisfed.org/series?seid=PAYEMS", "title": "ALFRED - Archival FRED Real-Time Data for PAYEMS",
"domain": "alfred.stlouisfed.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Historical vintage data for all past releases of PAYEMS, enabling computation of revision statistics across
initial and subsequent releases."}, {"url": "https://www.bls.gov/ces/publications/benchmark/ces-benchmark-revision.htm", "title": "BLS Current Employment Statistics - Benchmark Revisions", "domain":
"bls.gov", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Annual benchmark revision data showing cumulative adjustments to nonfarm payrolls. 2024 revision was -818K; 2025/2026 revision revised
2025 levels down ~1 million."}, {"url": "https://www.philadelphiafed.org/surveys-and-data/real-time-data-research/", "title": "Philadelphia Fed Real-Time Data Research Center", "domain":
"philadelphiafed.org", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Research on data revisions including Aruoba (2008) finding that initial BLS employment releases are noisy and systematically
revised."}, {"url": "https://tradingeconomics.com/united-states/non-farm-payrolls", "title": "Trading Economics - United States Non Farm Payrolls", "domain": "tradingeconomics.com", "accessed_at":
"2026-05-04T00:00:00Z", "snippet": "Historical NFP actual vs forecast data. Cross-validated 2024 monthly surprise figures."}, {"url": "https://www.bloomberg.com", "title": "Bloomberg Economist Survey
- NFP Consensus Forecasts", "domain": "bloomberg.com", "accessed_at": "2026-05-04T00:00:00Z", "snippet": "Bloomberg compiles 60-80 economist forecasts for monthly NFP consensus. Dispersion data (IQR,
range) derived from survey distributions."}], "key_facts": ["The standard deviation of NFP surprises (actual minus consensus) is approximately 70K-85K in normal times, widening to 90K-120K in high-
uncertainty periods like 2021-2024.", "NFP surprises exhibit a positive bias in expansions: the mean surprise is +10K to +15K over full samples (2000-2024 ex-COVID), rising to +40K-60K during
2021-2023.", "NFP beats consensus roughly 55-60% of the time across multi-year samples.", "The median absolute forecast error is approximately 47K, while the mean absolute error is 65K-75K.",
"Surprises exceeding 100K occur in roughly 15-20% of months.", "The distribution has fat tails (leptokurtic): extreme surprises (>2 standard deviations) occur 8-10% of the time vs 5% expected under
normality.", "In 2024, the mean surprise was +35K with 8 of 12 months beating consensus; the largest positive surprise was January (+168K) and largest negative was October (-101K, hurricane/strike-
distorted).", "Monthly revisions are substantial: the mean first revision is +10K-15K, and cumulative two-month revision averages +20K-30K with std dev of 45K-55K.", "Annual benchmark revisions
(applied each February using QCEW data) averaged 266K in absolute terms from 2004-2024.", "The 2026 benchmark revision revised 2025 employment levels down by ~1 million jobs, changing average monthly
gains from ~+103K initially reported to ~+10K.", "The 2024 benchmark revision was -818K (preliminary), the largest downward revision since 2009's -617K (later exceeded by the 2025 revision).",
"Consensus forecast dispersion (IQR of individual forecasts) ranges from 40K-60K in calm periods to 60K-100K in uncertain periods.", "NFP surprise bias is regime-dependent: +5K to +15K in steady
expansions, +30K to +80K in early recovery, roughly zero in late cycle, and -50K to -100K in recessions.", "The Bloomberg/Reuters consensus typically includes 60-80 individual economist forecasts.",
"FRED vintage data shows 2025 monthly changes were revised downward in 12 of 13 months examined, with individual revisions ranging from -9K to -167K."], "data_points": [{"metric": "NFP surprise
standard deviation (pre-COVID 2010-2019)", "value": 67.5, "unit": "thousands of jobs", "as_of": "2019-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "NFP surprise
standard deviation (post-COVID 2021-2024)", "value": 105.0, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "NFP
surprise standard deviation (full sample ex-COVID)", "value": 77.5, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric":
"NFP mean surprise (full sample 2000-2024 ex-COVID)", "value": 12.5, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric":
"NFP mean surprise (2021-2023 post-COVID recovery)", "value": 50.0, "unit": "thousands of jobs", "as_of": "2023-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric":
"NFP mean surprise (2024)", "value": 35.0, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "NFP median absolute
forecast error", "value": 47.0, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "NFP mean absolute forecast error",
"value": 70.0, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Share of months NFP beats consensus", "value": 57.5,
"unit": "percent", "as_of": "2024-12-31", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Mean first monthly revision", "value": 12.5, "unit": "thousands of jobs",
"as_of": "2024-12-31", "source_url": "https://alfred.stlouisfed.org/series?seid=PAYEMS"}, {"metric": "Mean cumulative two-month revision", "value": 25.0, "unit": "thousands of jobs", "as_of":
"2024-12-31", "source_url": "https://alfred.stlouisfed.org/series?seid=PAYEMS"}, {"metric": "Std dev of cumulative revision", "value": 48.0, "unit": "thousands of jobs", "as_of": "2024-12-31",
"source_url": "https://alfred.stlouisfed.org/series?seid=PAYEMS"}, {"metric": "Mean absolute annual benchmark revision (2004-2024)", "value": 266.0, "unit": "thousands of jobs", "as_of": "2024-12-31",
"source_url": "https://www.bls.gov/ces/publications/benchmark/ces-benchmark-revision.htm"}, {"metric": "2024 annual benchmark revision", "value": -818.0, "unit": "thousands of jobs", "as_of":
"2025-02-01", "source_url": "https://www.bls.gov/ces/publications/benchmark/ces-benchmark-revision.htm"}, {"metric": "2025 benchmark revision (avg level change across 2025 months)", "value": -1041.0,
"unit": "thousands of jobs", "as_of": "2026-02-01", "source_url": "https://fred.stlouisfed.org/series/PAYEMS"}, {"metric": "2025 avg monthly NFP gain (revised)", "value": 10.0, "unit": "thousands of
jobs", "as_of": "2026-04-03", "source_url": "https://fred.stlouisfed.org/series/PAYEMS"}, {"metric": "2025 avg monthly NFP gain (initially reported)", "value": 103.0, "unit": "thousands of jobs",
"as_of": "2025-12-31", "source_url": "https://fred.stlouisfed.org/series/PAYEMS"}, {"metric": "Jan 2024 NFP surprise (largest positive in 2024)", "value": 168.0, "unit": "thousands of jobs", "as_of":
"2024-02-02", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Oct 2024 NFP surprise (largest negative in 2024)", "value": -101.0, "unit": "thousands of jobs", "as_of":
"2024-11-01", "source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Frequency of surprises exceeding 100K", "value": 17.5, "unit": "percent of months", "as_of": "2024-12-31",
"source_url": "https://www.bls.gov/news.release/empsit.nr0.htm"}, {"metric": "Consensus forecast IQR (pre-COVID)", "value": 50.0, "unit": "thousands of jobs", "as_of": "2019-12-31", "source_url":
"https://www.bloomberg.com"}, {"metric": "Consensus forecast IQR (post-COVID)", "value": 80.0, "unit": "thousands of jobs", "as_of": "2024-12-31", "source_url": "https://www.bloomberg.com"},
{"metric": "PAYEMS level March 2026", "value": 158637.0, "unit": "thousands of persons", "as_of": "2026-04-03", "source_url": "https://fred.stlouisfed.org/series/PAYEMS"}, {"metric": "Unemployment
rate March 2026", "value": 4.3, "unit": "percent", "as_of": "2026-03-31", "source_url": "https://fred.stlouisfed.org/series/UNRATE"}], "created_at": "2026-05-04T00:15:50.796149Z", "updated_at":
"2026-05-04T00:15:50.796149Z", "stale_after": "2026-05-07T00:15:50.796149Z", "state": "fresh", "revision_history": [], "session_id": "a0ca3f4b-1286-4bf4-a2b5-e4e53749d017", "follow_up_count": 0},
"is_follow_up": false}], "successful_count": 3, "failed_count": 0}
```

## 💬 Response

Now let me search for the most recent consensus estimates and any additional leading indicators for April 2026:

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "April 2026 nonfarm payrolls forecast consensus estimate May 8"
}
```

### 📋 Result

```
{"query": "April 2026 nonfarm payrolls forecast consensus estimate May 8", "results": [{"title": "US nonfarm payrolls for April 2026 Odds and Forecast | Octagon AI", "url":
"https://octagonai.co/markets/economics/jobs-economy/us-nonfarm-payrolls-for-april-2026/", "snippet": "![US nonfarm payrolls for April 2026 prediction market](https://kalshi-public-
docs.s3.amazonaws.com/series-images-webp/KXUSNFP.webp)\nUS nonfarm payrolls for April 2026\n[1. Executive Verdict](https://octagonai.co#verdict)\n[2. Market Behavior & Price
Dynamics](https://octagonai.co#chart)\n[3. Significant Price Movements](https://octagonai.co#movements)\n[4. Market Data](https://octagonai.co#market-data)\n[5. How Do Regional Fed Surveys Predict
Future Employment and Spending?](https://octagonai.co#q1)", "api_data": null, "hint": null}, {"title": "United States Non Farm Payrolls", "url": "https://tradingeconomics.com/united-states/non-farm-
payrolls", "snippet": "The US economy added 178K jobs in March 2026, the most since December 2024, following a revised decline of 133K in February, when a strike in the healthcare sector weighed on
employment. The figure came in well above market expectations of 60K. Job gains were concentrated in healthcare (76K), mostly ambulatory health care services (54K), reflecting an increase of 35K in
offices of physicians as workers returned from a strike. Construction added 26K jobs following weather-related declines during ", "api_data": null, "hint": "Use fred_series/fred_search for US data, or
world_bank_indicator for international data."}, {"title": "Non Farm Payrolls Forecast 2026/2027", "url": "https://tradingeconomics.com/forecast/non-farm-payrolls", "snippet": "This feature is
exclusively available to subscribers. Trading Economics has more than 20 million economic indicators for nearly 200 countries, plus exchange rates, government bond yields, stock indexes, shares and
commodity prices. Consider subscribing to unlock all benefits!", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "Non-
Farm Payrolls Forecast", "url": "https://www.forecasts.org/jobs-growth-forecast.htm", "snippet": "The Financial Forecast Center\u2122\nIndependent. Objective.
Accurate.\n[Home](https://www.forecasts.org/)\n[About Us](https://www.forecasts.org/service/about.htm)\n[Contact
Us](https://www.forecasts.org/service/contact.htm)\n[Subscribe](https://www.forecasts.org/subscribe/index.htm)\n[Subscriber Log In](https://www.forecasts.org/extended/index.htm)\n[Stock Market
Forecasts](https://www.forecasts.org/stock-index/index.htm)\n[Interest Rate Forecasts](https://www.forecasts.org/interest-rate/index.htm)\n[Exchang", "api_data": null, "hint": null}, {"title":
"Nonfarm Payrolls - United States - 2026 Calendar Forecast", "url": "https://www.fxstreet.com/economic-calendar/event/9cdf56fd-99e4-4026-aa99-2b6c0ca92811", "snippet": "INSTITUTIONS AND OTHER
BACKGROUND INFORMATION\nAbout the US Bureau of Labor Statistics\nThe US Bureau of Labour Statistics is an agency of the country\u2019s Department of Labor, responsible for measuring labor market
activity, working conditions, and price changes in the economy. Its main mission is to create and organize timely, needed government information and services and make them accessible anytime,
anywhere, via different channels. The Bureau of Labor Statistics is responsible for releasing the", "api_data": null, "hint": null}, {"title": "April Jobs Report Forecasts Show Stable Growth, but
Impact From Federal Layoffs and Tariffs Looms | Morningstar", "url": "https://www.morningstar.com/markets/april-jobs-report-forecasts-show-stable-growth-impact-federal-layoffs-tariffs-looms",
"snippet": "April Jobs Report Forecasts Show Stable Growth, but Impact From Federal Layoffs and Tariffs Looms\nFed looks likely to cut rates in June.\n![Illustration of capital building with bubbles
of currency inflating](https://cloudfront-us-east-1.images.arcpublishing.com/morningstar/LNMUHDRH3JAXRGAR6CXLBPTQL4.png)\nKey Takeaways\n- Job growth is forecast to remain steady in April, though
slower than in March.\n- Early signs of impact from federal workforce cuts, trade policy shifts, and immigration changes m", "api_data": null, "hint": null}, {"title": "Nonfarm Payrolls Forecast",
"url": "https://www.fxstreet.com/macroeconomics/economic-indicator/nfp", "snippet": "Nonfarm Payrolls (NFP) in the United States (US) increased by 178K in March, according to data released by the US
Bureau of Labor Statistics (BLS) on Friday. The figure marks a marked reversal from February\u2019s 133K drop (revised from -92K) and came in well above market expectations for a 60K gain.\nUS Nonfarm
Payrolls rose by 178,000 in March, following the 133,000 decrease recorded in February. This print came in above the market expectation for an increase of 60,000.\n\"The change in total nonfarm",
"api_data": null, "hint": null}, {"title": "ADP\u00ae National Employment Report", "url": "https://adpemploymentreport.com/", "snippet": "11,000\nMarch 2026Change in U.S. private
employment\n62,000\nSubscribe to the National employment report\nNatural resources and mining\n11,000\nConstruction\n30,000\nManufacturing\n11,000\nTrade, transportation, and
utilities\n58,000\nInformation\n16,000\nFinancial activities\n4,000\nProfessional and business services\n1,000\nEducation and health services\n58,000\nLeisure and hospitality\n7,000\nOther
services\n4,000\nThe ADP National Employment Report is an independent and high-frequency view of the private-sector lab", "api_data": null, "hint": null}, {"title": "Employment Situation Summary -
2026 M03 Results", "url": "https://www.bls.gov/news.release/empsit.nr0.htm", "snippet": null, "api_data": null, "hint": "Use fred_series (FRED mirrors BLS data). Try UNRATE, CPIAUCSL, PAYEMS."},
{"title": "Employment Situation News Release - 2025 M13 Results", "url": "https://www.bls.gov/news.release/archives/empsit_01092026.htm", "snippet": null, "api_data": null, "hint": "Use fred_series
(FRED mirrors BLS data). Try UNRATE, CPIAUCSL, PAYEMS."}]}
```

```json
{
  "query": "ADP private payrolls April 2026"
}
```

### 📋 Result

```
{"query": "ADP private payrolls April 2026", "results": [{"title": "ADP National Employment Report: Private Sector Employment Increased by 62,000 Jobs in March; Annual Pay was Up 4.5% - Apr 1, 2026",
"url": "https://mediacenter.adp.com/2026-04-01-ADP-National-Employment-Report-Private-Sector-Employment-Increased-by-62,000-Jobs-in-March-Annual-Pay-was-Up-4-5", "snippet": "ROSELAND, N.J., April 1,
2026 /[PRNewswire](http://www.prnewswire.com/)/ -- Private sector employment increased by 62,000 jobs in March and pay was up 4.5 percent year-over-year according to the March [ADP National Employment
Report\u00ae](http://www.adpemploymentreport.com/?utm_source=PRnewsroom&utm_medium=pressrelease&utm_campaign=adpnerrelease&utm_content=prrelease020426link1) produced by ADP Research in collaboration
with the Stanford Digital Economy Lab (\"Stanford Lab\").\nThe ADP National Employm", "api_data": null, "hint": null}, {"title": "ADP\u00ae National Employment Report", "url":
"https://adpemploymentreport.com/", "snippet": "11,000\nMarch 2026Change in U.S. private employment\n62,000\nSubscribe to the National employment report\nNatural resources and
mining\n11,000\nConstruction\n30,000\nManufacturing\n11,000\nTrade, transportation, and utilities\n58,000\nInformation\n16,000\nFinancial activities\n4,000\nProfessional and business
services\n1,000\nEducation and health services\n58,000\nLeisure and hospitality\n7,000\nOther services\n4,000\nThe ADP National Employment Report is an independent and high-frequency view of the
private-sector lab", "api_data": null, "hint": null}, {"title": "Private sector added 62,000 jobs in March, driven by small employers - UPI.com", "url":
"https://www.upi.com/Top_News/US/2026/04/01/adp-march-2026-jobs-report/8341775050760/", "snippet": "April 1 (UPI) -- Private sector hiring in the United States remained steady in March, bolstered by
small businesses, the ADP National Employment Report said Wednesday.\nSmall businesses with less than 20 employees [added 112,000 jobs](https://adpemploymentreport.com/) in March. Mid-sized businesses
with 250 to 499 employees added 6,000 jobs.\nAll other categories reduced payrolls with small businesses of 20 to 49 employees losing 27,000 jobs and businesses of 50 to 249 employees losing 26,000
jobs", "api_data": null, "hint": null}, {"title": "United States ADP Employment Change Weekly", "url": "https://tradingeconomics.com/united-states/adp-employment-change-weekly", "snippet": "US private
employers added an average of 39,250 jobs per week in the four weeks ending April 11, 2026, according to the ADP Research Institute, slightly below the downwardly revised 40,250 weekly gain in the
prior period. The data suggests a stabilization in hiring momentum following an acceleration in job creation during the second half of March. source: [Automatic Data Processing,
Inc.](https://adpemploymentreport.com/)\nADP Employment Change Weekly in the United States decreased to 39.25 Thous", "api_data": null, "hint": "Use fred_series/fred_search for US data, or
world_bank_indicator for international data."}, {"title": "ADP National Employment Report: 62K Private Jobs Added in March - dshort - Advisor Perspectives", "url":
"https://www.advisorperspectives.com/dshort/updates/2026/04/01/adp-private-employment-report-march-2026", "snippet": null, "api_data": null, "hint": null}, {"title": "United States ADP Employment
Change", "url": "https://tradingeconomics.com/united-states/adp-employment-change", "snippet": "Private businesses in the US added a net 62,000 jobs in March of 2026, extending the upwardly revised
66,000 in February and above market expectations of a 40,000 increase. The result held signs of resilience in the labor market per the latest leading indicators, despite economic uncertainty and the
pullback in the labor force growth amid lower immigration. Education and health services jobs rose by 58,000 to remain the main source of job growth. Other gains were seen in construction (30,000),
n", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "ADP Employment Change - United States - 2026 Calendar Forecast",
"url": "https://www.fxstreet.com/economic-calendar/event/4f50e4f8-cd33-428b-b721-5fb620b7f097", "snippet": "INSTITUTIONS AND OTHER BACKGROUND INFORMATION\nAbout the ADP Research Institue\nThe ADP
Research Institute is the global thought leader in labor market and employee performance research. It generates data-driven discoveries about the world of work and derives reliable economic indicators
from these insights. The ADP releases monthly surveys on private job creation, not only for the US, although the US survey is the one market participants pay more attention to, as it is released
monthly, a couple ", "api_data": null, "hint": null}, {"title": "ADP National Employment Report: Private Sector Employment Increased by 62,000 Jobs in April; Annual Pay was Up 4.5%", "url":
"https://www.prnewswire.com/news-releases/adp-national-employment-report-private-sector-employment-increased-by-62-000-jobs-in-april-annual-pay-was-up-4-5-302442587.html", "snippet":
"![](/content/dam/amplify-logo.png)\nROSELAND, N.J., April 30, 2025 /PRNewswire/ -- Private sector employment increased by 62,000 jobs in April and annual pay was up 4.5 percent year-over-year,
according to the April [ADP\u00ae National Employment Report\u2122](http://www.adpemploymentreport.com/) produced by ADP Research in collaboration with the Stanford Digital Economy Lab (\"Stanford
Lab\"). The ADP National Employment Report is an independent measure and high-frequency view of the private-sector labor ma", "api_data": null, "hint": null}, {"title": "US private hiring improved for
a third straight week, ADP says", "url": "https://www.stocktitan.net/news/ADP/adp-national-employment-report-preliminary-estimate-for-march-21-s95m55sv9oq5.html", "snippet": "ADP National Employment
Report Preliminary Estimate for March 21, 2026\nRhea-AI Summary\nADP (ADP) reports that for the four weeks ending March 21, 2026, U.S. private employers added an average of 26,000 jobs per week per
the NER Pulse. It was the third straight week of improvement in hiring. These are preliminary, seasonally adjusted estimates with a two-week data lag.\nThe NER Pulse uses a four-week moving average
and publishes weekly on Tuesdays at 8:15 a.m. ET; the next release is April 14, 202", "api_data": null, "hint": null}, {"title": "ADP: Private payrolls dropped 32,000 positions last month in slowing
job market", "url": "https://finance.yahoo.com/news/adp-private-payrolls-dropped-32000-positions-last-month-in-slowing-job-market-133210474.html", "snippet": "US private employers lost 32,000
positions in November, with job creation seemingly locked in a standstill, according to the [private payroll processor ADP.](https://adpemploymentreport.com/)\nThe firm\u2019s revised data showed a
gain of [47,000 jobs in October](https://finance.yahoo.com/news/adp-private-payrolls-show-modest-rebound-in-october-134112187.html), coming off losses in September and August. Job creation has
essentially been flat in the second half of this year, ADP said, and small busines", "api_data": null, "hint": null}]}
```

```json
{
  "query": "ISM employment index April 2026"
}
```

### 📋 Result

```
{"query": "ISM employment index April 2026", "results": [{"title": "United States ISM Manufacturing PMI", "url": "https://tradingeconomics.com/united-states/business-confidence", "snippet": "The ISM
Manufacturing PMI for the US remained unchanged at 52.7 in April 2026, matching its highest level since August 2022 but falling short of market expectations for a rise to 53.0. New orders grew at a
faster pace (54.1 vs. 53.5 in March), and supplier deliveries lengthened further (60.6 vs. 58.9), while production expanded at a slower rate (53.4 vs. 55.1), and employment levels declined at the
sharpest pace in four months (46.4 vs. 48.7). Prices surged at the fastest rate since late 2021, d", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for
international data."}, {"title": "Manufacturing PMI\u00ae at 52.7%; April 2026 ISM\u00ae Manufacturing PMI\u00ae Report", "url": "https://www.prnewswire.com/news-releases/manufacturing-pmi-
at-52-7-april-2026-ism-manufacturing-pmi-report-302759226.html", "snippet": "![](/content/dam/amplify-logo.png)\nNew Orders Growing; Production Growing; Employment Contracting; Supplier Deliveries
Slowing; Raw Materials Inventories Contracting; Customers' Inventories Too Low; Prices Increasing; Imports Growing; Exports Contracting\nTEMPE, Ariz., May 1, 2026 /PRNewswire/ -- Economic activity in
the manufacturing sector expanded in April for the fourth consecutive month, say the nation's supply executives in the latest ISM\u00ae Manufacturing PMI\u00ae Report.\nThe report was issued to",
"api_data": null, "hint": null}, {"title": "TD Economics - U.S. ISM Manufacturing Index (April 2026)", "url": "https://economics.td.com/us-ism-manufacturing-index", "snippet": "U.S. ISM Manufacturing
Index (April 2026)\nVikram Rai, Senior Economist | 416-923-1692\nDate Published: May 1, 2026\n- Category:\n[U.S.](http://economics.td.com/US)[Data
Commentary](https://economics.td.com/USCommentaries)[Commodities & Industry](https://economics.td.com/USCommoditiesIndustry)\nISM Manufacturing Index Shows Prices Surged Again in April\n- The ISM
Manufacturing Index was unchanged at 52.7 in April, remaining in expansionary territory for a fourth consecutive month (the longest such str", "api_data": null, "hint": null}, {"title": "FX.co - U.S.
ISM Manufacturing Employment Index Slips Further in April, Signaling Softer Factory Hiring", "url": "https://www.fx.co/en/forex-news/2988810", "snippet": "The employment component of the U.S. ISM
Manufacturing Index weakened in April 2026, pointing to a further cooling in factory hiring. The indicator declined to 46.4 in April from 48.7 in March, remaining below the 50-point threshold that
separates expansion from contraction.\nThe continued drop suggests that manufacturing employers are becoming more cautious about adding to payrolls, reflecting a softer labor environment in the
industrial sector. With the index now deeper in contractionary territ", "api_data": null, "hint": null}, {"title": "ISM Manufacturing Employment 2026 - economic data from the United States", "url":
"https://www.mql5.com/en/economic-calendar/united-states/ism-manufacturing-employment", "snippet": "ISM United States Manufacturing Employment\n| Medium | 46.4 | 47.8 |\n48.7\n|\n|\n| Last release |
Importance | Actual | Forecast |\nPrevious\n|\n| 46.7 |\n46.4\n|\n|||\n| Next release | Actual | Forecast |\nPrevious\n|\nISM Manufacturing Employment is one of the diffuse indicators, based on which
the Supply Management Institute calculates [the Manufacturing PMI](https://www.mql5.com/en/economic-calendar/united-states/ism-manufacturing-pmi). It reflects a change in employment in industrial
companies.\nThe index", "api_data": null, "hint": null}, {"title": "ISM Manufacturing PMI: Expansion Continues in April - dshort - Advisor Perspectives", "url":
"https://www.advisorperspectives.com/dshort/updates/2026/05/01/ism-manufacturing-pmi-expansion-continues-april-2026", "snippet": null, "api_data": null, "hint": null}, {"title": "ISM Manufacturing
index for April 52,7 vs 53.0 estimate | investingLive", "url": "https://investinglive.com/news/ism-manufacturing-index-for-april-527-vs-530-estimate-20260501/", "snippet": "- Prior month 52.7\n-
manufacturing index 52.7 versus 53.0 estimate.\n- Prices paid 84.6 versus 80.0 estimate and 78.3 last month.\n- Employment index up 46.4 versus 49.0 estimate. Last month 48.7.\n- New orders 54.1
versus 53.5 last month.\n- Production 53.4 versus 55.1 last month.\n- Supplier deliveries 60.6 versus 58.9 last month.\n- Inventories 49.0 versus 47.1 last month.\n- Backlog of orders 51.4 versus 54.4
last month\n- New export orders 47.9 versus 49.9 last month\n- Imports 50.3 versus 52.6 last", "api_data": null, "hint": null}, {"title": "Manufacturing ISM Misses As Prices Surge Most Since April
2022, Employment Slides To Worst Print Of 2026<!-- --> | ZeroHedge", "url": "https://www.zerohedge.com/markets/manufacturing-ism-misses-prices-surge-most-april-2022-employment-slides-worst-
print-2026", "snippet": "Manufacturing ISM Misses As Prices Surge Most Since April 2022, Employment Slides To Worst Print Of 2026\nAmid the fog of war and fading 'hard' data, the final April S&P
Global Manufacturing PMI printed 54.5, a small gain from the flash 54.0 print, and higher than the 52.3 February final print, although it came with a [warning ](chrome-
extension://efaidnbmnnnibpcajpcglclefindmkaj/https://www.pmi.spglobal.com/Public/Home/PressRelease/b8123dcab4204a3f979075403c433cd0)from Chris Williamson, Chief Bu", "api_data": null, "hint": null},
{"title": "ISM US Manufacturing PMI - April 2026 - Neil's Newsletter", "url": "https://neilsethi.substack.com/p/ism-us-manufacturing-pmi-april-2026", "snippet": "ISM US Manufacturing PMI - April
2026\nISM manufacturing PMI remains at the strongest since Aug 2022 but in part on longest delivery times since then with prices at 4-yr high. Like S&P PMI employment fell.\nUS ISM Manufacturing Apr:
52.7 (est 53.2; prev 52.7)\n- Price Paid: 84.6 (est 80.0; prev 78.3)\n- New Orders: 54.1 (prev 53.5)\n- Employment: 46.4 (prev 48.7)\nLike its S&P counterpart (which is generally smaller companies
than the ISM survey and more domestic focused) [which jumped +2.2pts to 54.5", "api_data": null, "hint": null}, {"title": "United States ISM Manufacturing Employment", "url":
"https://tradingeconomics.com/united-states/ism-manufacturing-employment", "snippet": "The index measuring employment levels in the ISM PMI fell to 46.4 in April of 2026 from 48.7 in the previous
month, well below market expectations of 49. It was the a 15th consecutive contraction, the lowest this year, despite other data pointing to a robust labor market in the US. source: [Institute for
Supply Management](https://www.ismworld.org)\nISM Manufacturing Employment in the United States averaged 50.06 points from 1950 until 2026, reaching an all time high of 73.70 points in February o",
"api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Kalshi nonfarm payrolls April 2026 prediction market"
}
```

### 📋 Result

```
{"query": "Kalshi nonfarm payrolls April 2026 prediction market", "results": [{"title": "Nonfarm Payrolls Odds & Predictions 2026", "url": "https://kalshi.com/tag/nonfarm-payrolls", "snippet": "###
Result\n\"MARKETS\\nLIVE\\n28\\nSOCIAL\\nFAIRNESS\\n$0\\nLog in\\nSign
up\\nTrending\\nElections\\nPolitics\\nSports\\nCulture\\nCrypto\\nCommodities\\nClimate\\nEconomics\\nMentions\\nCompanies\\nFinancials\\nTech & Science\\nNonfarm Payrolls Odds &
Predictions\\nTrending\\nFrequency\\nAll categories\\nNo results found\\n\u2022 Make sure all words are spelled correctly\\n\u2022 Try a broader search\\nCompany\\nBlog\\nCareers\\nPrivacy
Policy\\nData Terms of Service\\nCompany\\nBrand Kit\\nSocial\\nX (Twitter)\\nLinkedIn\\nDiscord\\nInstagra", "api_data": null, "hint": null}, {"title": "US nonfarm payrolls for April 2026 Odds and
Forecast | Octagon AI", "url": "https://octagonai.co/markets/economics/jobs-economy/us-nonfarm-payrolls-for-april-2026/", "snippet": "![US nonfarm payrolls for April 2026 prediction
market](https://kalshi-public-docs.s3.amazonaws.com/series-images-webp/KXUSNFP.webp)\nUS nonfarm payrolls for April 2026\n[1. Executive Verdict](https://octagonai.co#verdict)\n[2. Market Behavior &
Price Dynamics](https://octagonai.co#chart)\n[3. Significant Price Movements](https://octagonai.co#movements)\n[4. Market Data](https://octagonai.co#market-data)\n[5. How Do Regional Fed Surveys
Predict Future Employment and Spending?](https://octagonai.co#q1)", "api_data": null, "hint": null}, {"title": "Jobs numbers this month? Odds & Predictions 2026", "url":
"https://kalshi.com/markets/kxpayrolls/jobs-numbers", "snippet": "{\"markets\": [{\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.92, \"volume\": 1395.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-5\", \"source\": \"kalshi\", \"description\": \"If the U-3 unemployment rate from June 2025 to January 2030 is above 5%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-5\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-5\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If the U-3 unemployment rate from June 2025 to
January 2030 is ", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.92, \"volume\": 1395.0,
\"url\": \"https://kalshi.com/markets/KXU3MAX-30-5\", \"source\": \"kalshi\", \"description\": \"If the U-3 unemployment rate from June 2025 to January 2030 is above 5%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-5\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-5\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If the U-3 unemployment rate from June 2025 to
January 2030 is above 5%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.85, \"volume\": 647.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-6\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 6%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-6\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-6\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 6%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.79, \"volume\": 804.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-7\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 7%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-7\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-7\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 7%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.6, \"volume\": 757.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-8\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 8%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-8\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-8\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 8%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.44, \"volume\": 3171.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-9\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 9%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-9\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-9\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 9%, the market resolves to Yes.\"}], \"query\": \"jobs numbers\"}"}]}, "hint": null}, {"title": "Non Farm Payrolls Forecast 2026/2027", "url":
"https://tradingeconomics.com/forecast/non-farm-payrolls", "snippet": "This feature is exclusively available to subscribers. Trading Economics has more than 20 million economic indicators for nearly
200 countries, plus exchange rates, government bond yields, stock indexes, shares and commodity prices. Consider subscribing to unlock all benefits!", "api_data": null, "hint": "Use
fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "Market | Trade on Kalshi", "url": "https://kalshi.com/markets/kxpayrolls", "snippet": "{\"markets\":
[], \"query\": \"kxpayrolls\"}", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [], \"query\": \"kxpayrolls\"}"}]}, "hint": null}, {"title": "Jobs numbers in February 2026? Odds &
Predictions", "url": "https://kalshi.com/markets/payrolls/jobs-numbers", "snippet": "{\"markets\": [{\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.92,
\"volume\": 1395.0, \"url\": \"https://kalshi.com/markets/KXU3MAX-30-5\", \"source\": \"kalshi\", \"description\": \"If the U-3 unemployment rate from June 2025 to January 2030 is above 5%, the market
resolves to Yes.\", \"market_id\": \"KXU3MAX-30-5\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-5\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If the U-3 unemployment rate
from June 2025 to January 2030 is ", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.92,
\"volume\": 1395.0, \"url\": \"https://kalshi.com/markets/KXU3MAX-30-5\", \"source\": \"kalshi\", \"description\": \"If the U-3 unemployment rate from June 2025 to January 2030 is above 5%, the market
resolves to Yes.\", \"market_id\": \"KXU3MAX-30-5\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-5\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If the U-3 unemployment rate
from June 2025 to January 2030 is above 5%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.85, \"volume\": 647.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-6\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 6%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-6\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-6\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 6%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.79, \"volume\": 804.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-7\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 7%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-7\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-7\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 7%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.6, \"volume\": 757.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-8\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 8%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-8\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-8\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 8%, the market resolves to Yes.\"}, {\"market_title\": \"How high will unemployment get before 2030?\", \"probability\": 0.44, \"volume\": 3171.0, \"url\":
\"https://kalshi.com/markets/KXU3MAX-30-9\", \"source\": \"kalshi\", \"description\": \"If, from June 2025 to January 2030 the U-3 unemployment rate is above 9%, the market resolves to Yes.\",
\"market_id\": \"KXU3MAX-30-9\", \"recent_history\": [], \"market_ticker\": \"KXU3MAX-30-9\", \"event_ticker\": \"KXU3MAX-30\", \"rules_primary\": \"If, from June 2025 to January 2030 the U-3
unemployment rate is above 9%, the market resolves to Yes.\"}], \"query\": \"jobs numbers\"}"}]}, "hint": null}, {"title": "April Jobs Report Forecasts Show Stable Growth, but Impact From Federal
Layoffs and Tariffs Looms | Morningstar", "url": "https://www.morningstar.com/markets/april-jobs-report-forecasts-show-stable-growth-impact-federal-layoffs-tariffs-looms", "snippet": "April Jobs
Report Forecasts Show Stable Growth, but Impact From Federal Layoffs and Tariffs Looms\nFed looks likely to cut rates in June.\n![Illustration of capital building with bubbles of currency
inflating](https://cloudfront-us-east-1.images.arcpublishing.com/morningstar/LNMUHDRH3JAXRGAR6CXLBPTQL4.png)\nKey Takeaways\n- Job growth is forecast to remain steady in April, though slower than in
March.\n- Early signs of impact from federal workforce cuts, trade policy shifts, and immigration changes m", "api_data": null, "hint": null}, {"title": "Kalshi Fees Explained (2026): Trading Costs,
Fee Schedule & Calculator | Market Math", "url": "https://marketmath.io/platforms/kalshi", "snippet": "![Kalshi
logo](/_next/image?url=%2Fimages%2Fplatforms%2Fkalshi.png&w=96&q=75&dpl=dpl_6riP8iYPuz6bHZTpU1c6KU7aAKXD)\nKalshi Review 2026: Fees, Markets & Features\nThe first CFTC-regulated prediction market
exchange\nLast updated: May 4, 2026\nFee model\n7% \u00d7 p \u00d7\nCategories\n7 markets\nFounded\n2018\nMin age\n18+\nKalshi is a CFTC-regulated designated contract market (DCM) offering binary
event contracts on politics, economics, weather, and more. Funds sit in segregated accounts with standardized 1099 tax re", "api_data": null, "hint": null}, {"title": "United States Non Farm
Payrolls", "url": "https://tradingeconomics.com/united-states/non-farm-payrolls", "snippet": "The US economy added 178K jobs in March 2026, the most since December 2024, following a revised decline of
133K in February, when a strike in the healthcare sector weighed on employment. The figure came in well above market expectations of 60K. Job gains were concentrated in healthcare (76K), mostly
ambulatory health care services (54K), reflecting an increase of 35K in offices of physicians as workers returned from a strike. Construction added 26K jobs following weather-related declines during
", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "Schedule of Selected Releases 2026", "url":
"https://www.bls.gov/schedule/2026/home.htm", "snippet": null, "api_data": null, "hint": "Use fred_series (FRED mirrors BLS data). Try UNRATE, CPIAUCSL, PAYEMS."}]}
```

```json
{
  "query": "\"April 2026\" nonfarm payrolls forecast economists estimate consensus Wall Street"
}
```

### 📋 Result

```
{"query": "\"April 2026\" nonfarm payrolls forecast economists estimate consensus Wall Street", "results": [{"title": "US nonfarm payrolls for April 2026 Odds and Forecast | Octagon AI", "url":
"https://octagonai.co/markets/economics/jobs-economy/us-nonfarm-payrolls-for-april-2026/", "snippet": "![US nonfarm payrolls for April 2026 prediction market](https://kalshi-public-
docs.s3.amazonaws.com/series-images-webp/KXUSNFP.webp)\nUS nonfarm payrolls for April 2026\n[1. Executive Verdict](https://octagonai.co#verdict)\n[2. Market Behavior & Price
Dynamics](https://octagonai.co#chart)\n[3. Significant Price Movements](https://octagonai.co#movements)\n[4. Market Data](https://octagonai.co#market-data)\n[5. How Do Regional Fed Surveys Predict
Future Employment and Spending?](https://octagonai.co#q1)", "api_data": null, "hint": null}, {"title": "United States Non Farm Payrolls", "url": "https://tradingeconomics.com/united-states/non-farm-
payrolls", "snippet": "The US economy added 178K jobs in March 2026, the most since December 2024, following a revised decline of 133K in February, when a strike in the healthcare sector weighed on
employment. The figure came in well above market expectations of 60K. Job gains were concentrated in healthcare (76K), mostly ambulatory health care services (54K), reflecting an increase of 35K in
offices of physicians as workers returned from a strike. Construction added 26K jobs following weather-related declines during ", "api_data": null, "hint": "Use fred_series/fred_search for US data, or
world_bank_indicator for international data."}, {"title": "Non Farm Payrolls Forecast 2026/2027", "url": "https://tradingeconomics.com/forecast/non-farm-payrolls", "snippet": "This feature is
exclusively available to subscribers. Trading Economics has more than 20 million economic indicators for nearly 200 countries, plus exchange rates, government bond yields, stock indexes, shares and
commodity prices. Consider subscribing to unlock all benefits!", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "Non-
Farm Payrolls Forecast", "url": "https://www.forecasts.org/jobs-growth-forecast.htm", "snippet": "The Financial Forecast Center\u2122\nIndependent. Objective.
Accurate.\n[Home](https://www.forecasts.org/)\n[About Us](https://www.forecasts.org/service/about.htm)\n[Contact
Us](https://www.forecasts.org/service/contact.htm)\n[Subscribe](https://www.forecasts.org/subscribe/index.htm)\n[Subscriber Log In](https://www.forecasts.org/extended/index.htm)\n[Stock Market
Forecasts](https://www.forecasts.org/stock-index/index.htm)\n[Interest Rate Forecasts](https://www.forecasts.org/interest-rate/index.htm)\n[Exchang", "api_data": null, "hint": null}, {"title":
"Employment Situation Summary - 2026 M03 Results", "url": "https://www.bls.gov/news.release/empsit.nr0.htm", "snippet": null, "api_data": null, "hint": "Use fred_series (FRED mirrors BLS data). Try
UNRATE, CPIAUCSL, PAYEMS."}, {"title": "Nonfarm Payrolls - United States - 2026 Calendar Forecast", "url": "https://www.fxstreet.com/economic-calendar/event/9cdf56fd-99e4-4026-aa99-2b6c0ca92811",
"snippet": "INSTITUTIONS AND OTHER BACKGROUND INFORMATION\nAbout the US Bureau of Labor Statistics\nThe US Bureau of Labour Statistics is an agency of the country\u2019s Department of Labor,
responsible for measuring labor market activity, working conditions, and price changes in the economy. Its main mission is to create and organize timely, needed government information and services and
make them accessible anytime, anywhere, via different channels. The Bureau of Labor Statistics is responsible for releasing the", "api_data": null, "hint": null}, {"title": "April 2026 US Jobs Report
| Staffing Industry Analysts", "url": "https://www.staffingindustry.com/research/research-reports/americas/april-2026-us-jobs-report", "snippet": null, "api_data": null, "hint": null}, {"title": "U.S.
added 178,000 jobs in March, beat expectations - UPI.com", "url": "https://www.upi.com/Top_News/US/2026/04/03/bls-march-2026-jobs-report-beats-expectations/1091775224119/", "snippet": "April 3 (UPI)
-- New jobs grew while unemployment held firm in the United States in March, with 178,000 nonfarm payrolls added, the Bureau of Labor Statistics reported Friday.\nMarch was a rebound from a poor
February report that showed [133,000 jobs lost](https://www.bls.gov/news.release/empsit.nr0.htm). The unemployment rate remained at 4.3%.\nThe February jobs report numbers were revised down by
41,000.\nFriday's report beat the Dow Jones consensus estimate of 59,000 added payrolls. It is more t", "api_data": null, "hint": null}, {"title": "Financial Consultant (@financialconsultantnearme)",
"url": "https://www.facebook.com/financialconsultantnearme/?locale=zh_CN", "snippet": null, "api_data": null, "hint": null}, {"title": "\"100% of new jobs in private sector...\" US President Trump
...", "url": "https://www.facebook.com/ANINEWS.IN/posts/100-of-new-jobs-in-private-sector-us-president-trump-defends-increase-in-unemplo/1322316083429038/?locale=zh_CN", "snippet": null, "api_data":
null, "hint": null}]}
```

```json
{
  "query": "ISM services employment April 2026"
}
```

### 📋 Result

```
{"query": "ISM services employment April 2026", "results": [{"title": "ISM\u00ae PMI\u00ae Reports Roundup: March Services", "url": "https://www.ismworld.org/supply-management-news-and-reports/news-
publications/inside-supply-management-magazine/blog/2026/2026-04/ism-pmi-reports-roundup-march-2026-services/", "snippet": "Oops!\nWe can't seem to find the page you're looking for.\nLet's get you to
where you need to go.\nPlease call 480-752-6276 and select option 8 to reach Customer Service.\nWe can't seem to find the page you're looking for.\nPlease call 480-752-6276 and select option 8 to
reach Customer Service.", "api_data": null, "hint": null}, {"title": "ISM Services Employment Index - United States - 2026 Calendar Forecast", "url": "https://www.fxstreet.com/economic-
calendar/event/6ea5ed9b-d9f0-4e87-8f81-7ec89b5e2f12", "snippet": "Skip to main content\nTRENDING:\nOil price\n|\nXAU/USD\n|\nEUR/USD\n|\nTrade War\n|\nSilver\n|\nGBP/USD\n|\nAUD/USD\nTRENDING:\nOil
price\n|\nXAU/USD\n|\nEUR/USD\n|\nTrade War\n|\nSilver\n|\nGBP/USD\n|\nAUD/USD\n|\nGET THE APP\n|\nNewsletter\nMENU\nShow navigation\nFXStreet\nFXStreet - The forex market\nRATES & CHARTS\nLive
Chart\nForecast Poll\nRates Table\nTechnical Levels\nTechnical Confluences Detector\nFed Sentiment Index\nEUR/USD\nGBP/USD\nUSD/JPY\nAUD/USD\nNZD/USD\nUSD/CAD\nGBP/JPY\nEUR/JPY\nDollar
Index\nGold\nOil\nSP500\nNews\nForex News\nInst", "api_data": null, "hint": null}, {"title": "United States ISM Services Employment", "url": "https://tradingeconomics.com/united-states/ism-non-
manufacturing-employment", "snippet": "The ISM Employment Index for US service providers tumbled 6.6 points to 45.2 in March 2026, one of the steepest drops since the pandemic, reversing three months
of job growth and signaling a return to contraction. source: [Institute for Supply Management](https://www.ismworld.org)\nISM Non Manufacturing Employment in the United States averaged 51.54 points
from 1997 until 2026, reaching an all time high of 60.30 points in January of 2018 and a record low of 29.30 points in April of 2020. This pag", "api_data": null, "hint": "Use fred_series/fred_search
for US data, or world_bank_indicator for international data."}, {"title": "Manufacturing PMI\u00ae at 52.7%; April 2026 ISM\u00ae Manufacturing PMI\u00ae Report", "url":
"https://www.prnewswire.com/news-releases/manufacturing-pmi-at-52-7-april-2026-ism-manufacturing-pmi-report-302759226.html", "snippet": "![](/content/dam/amplify-logo.png)\nNew Orders Growing;
Production Growing; Employment Contracting; Supplier Deliveries Slowing; Raw Materials Inventories Contracting; Customers' Inventories Too Low; Prices Increasing; Imports Growing; Exports
Contracting\nTEMPE, Ariz., May 1, 2026 /PRNewswire/ -- Economic activity in the manufacturing sector expanded in April for the fourth consecutive month, say the nation's supply executives in the
latest ISM\u00ae Manufacturing PMI\u00ae Report.\nThe report was issued to", "api_data": null, "hint": null}, {"title": "United States ISM Services PMI", "url": "https://tradingeconomics.com/united-
states/non-manufacturing-pmi", "snippet": "The ISM Services PMI fell to 54 in March 2026 from 56.1 in February which was the highest since August 2022 and compared to forecasts of 55. The reading
pointed to a slowdown in services activity, led by an ease in business activity (53.9 vs 59.9) and the first drop in employment in four months (45.2 vs 51.8). Also, the prices index rose to 70.7, the
highest since October 2022 from 63 in February, amid higher oil and fuel costs and the supplier deliveries index indicated slower performance compa", "api_data": null, "hint": "Use
fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "ISM Services PMI - United States - 2026 Calendar Forecast", "url":
"https://www.fxstreet.com/economic-calendar/event/6c5853c1-a409-4722-bdea-17ad5d8a193f", "snippet": "Skip to main content\nTRENDING:\nOil price\n|\nXAU/USD\n|\nEUR/USD\n|\nTrade
War\n|\nSilver\n|\nGBP/USD\n|\nAUD/USD\nTRENDING:\nOil price\n|\nXAU/USD\n|\nEUR/USD\n|\nTrade War\n|\nSilver\n|\nGBP/USD\n|\nAUD/USD\n|\nGET THE APP\n|\nNewsletter\nMENU\nShow
navigation\nFXStreet\nFXStreet - The forex market\nRATES & CHARTS\nLive Chart\nForecast Poll\nRates Table\nTechnical Levels\nTechnical Confluences Detector\nFed Sentiment
Index\nEUR/USD\nGBP/USD\nUSD/JPY\nAUD/USD\nNZD/USD\nUSD/CAD\nGBP/JPY\nEUR/JPY\nDollar Index\nGold\nOil\nSP500\nNews\nForex News\nInst", "api_data": null, "hint": null}, {"title": "Fall 2025 Semi
Annual", "url": "https://www.ismworld.org/supply-management-news-and-reports/reports/semi-annual-economic-forecast/2025/fall", "snippet": null, "api_data": null, "hint": null}, {"title": "06 April 202
6 ISM Services Survey | 1 PNC Economics Research", "url": "https://www.pnc.com/content/dam/pnc-
com/pdf/aboutpnc/EconomicReports/EconomicUpdates/2026/PNC_Economics_Research_ISM_Services_6_April_2026.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Services PMI\u00ae at 54%;
March 2026 ISM\u00ae Services PMI\u00ae Report", "url": "https://www.prnewswire.com/news-releases/services-pmi-at-54-march-2026-ism-services-pmi-report-302734026.html", "snippet":
"![](/content/dam/amplify-logo.png)\nBusiness Activity Index at 53.9%; New Orders Index at 60.6%; Employment Index at 45.2%; Supplier Deliveries Index at 56.2%\nTEMPE, Ariz., April 6, 2026
/PRNewswire/ -- Economic activity in the services sector continued to expand in March, say the nation's purchasing and supply executives in the latest ISM\u00ae Services PMI\u00ae Report. The Services
PMI\u00ae registered 54 percent, the 21st consecutive month in expansion territory.\nThe report was issued today by Steve Miller,", "api_data": null, "hint": null}, {"title": "United States ISM Non-
Manufacturing PMI", "url": "https://www.investing.com/economic-calendar/ism-non-manufacturing-pmi-176", "snippet": "Risk Disclosure: Trading in financial instruments and/or cryptocurrencies involves
high risks including the risk of losing some, or all, of your investment amount, and may not be suitable for all investors. Prices of cryptocurrencies are extremely volatile and may be affected by
external factors such as financial, regulatory or political events. Trading on margin increases the financial risks.\nBefore deciding to trade in financial instrument or cryptocurrencies you should be
fully informed of th", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.morningstar.com/markets/april-jobs-report-forecasts-show-stable-growth-impact-federal-layoffs-tariffs-looms",
  "prompt": "What are the specific consensus forecasts for April 2026 nonfarm payrolls? What do economists predict? What are the key factors mentioned?"
}
```

### 📋 Result

```
{"url": "https://www.morningstar.com/markets/april-jobs-report-forecasts-show-stable-growth-impact-federal-layoffs-tariffs-looms", "content": "Based on the content provided, there appears to be a date
discrepancy in your question. The article discusses **April 2025** forecasts, not April 2026. Here are the specific details:\n\n## Consensus Forecasts for April 2025 Nonfarm Payrolls:\n\n- **Consensus
estimate (FactSet)**: 135,000 jobs added\n- **March 2025 actual**: 228,000 jobs added (for comparison)\n- **Unemployment rate forecast**: 4.2% (unchanged from March)\n- **Hourly earnings forecast**:
0.3% monthly increase\n\n## Individual Economist Predictions:\n\n- **Jeffrey Roach (LPL Financial)**: 150,000 jobs\n- **Gus Faucher (PNC Financial Services)**: 150,000 jobs\n- **Lydia Boussour (EY)**:
65,000 jobs (significantly below consensus)\n\n## Key Factors Mentioned:\n\n1. **Federal workforce cuts** - Expected to begin showing impact, though buyouts delay some effects\n2. **Trade policy and
tariffs** - Steep tariff increases causing uncertainty; limited April impact expected but more significant effects anticipated in coming months\n3. **Immigration policy shifts** - Restrictions
expected to weaken long-term job growth, particularly toward end of 2025 and into 2026\n4. **Seasonal factors** - Particularly negative in April for services industries\n5. **Economic uncertainty** -
Survey conducted after April 2nd reciprocal tariff announcement during period of high volatility\n\nRelevant links:\n- [Morningstar's editorial policies](https://www.morningstar.com/editorial-
policy)", "title": "April Jobs Report Forecasts Show Stable Growth, but Impact From Federal Layoffs and Tariffs Looms"}
```

```json
{
  "url": "https://octagonai.co/markets/economics/jobs-economy/us-nonfarm-payrolls-for-april-2026/",
  "prompt": "What are the prediction market odds for the April 2026 nonfarm payrolls report? What ranges and probabilities are shown?"
}
```

### 📋 Result

```
{"url": "https://octagonai.co/markets/economics/jobs-economy/us-nonfarm-payrolls-for-april-2026/", "content": "Based on the content, here are the prediction market odds for April 2026 nonfarm
payrolls:\n\n**Available Contract Probabilities:**\n- Above -40K: 91%\n- Above -20K: 95%\n- Above 0K: 93%\n- Above 20K: 86%\n- Above 40K: 77%\n- Above 60K: 62%\n- Above 80K: 56%\n- Above 100K: 47%\n-
Above 120K: 40%\n- Above 140K: 33%\n- Above 160K: 26%\n- Above 180K: 18%\n- Above 200K: 9%\n- Above 220K: 8%\n- Above 240K: 7%\n\n**Model vs. Market Comparison:**\nThe analytical model is slightly
more bullish than market prices:\n- Above 20K: Market 86% vs Model 88.3%\n- Above 60K: Market 62% vs Model 65.9%\n- Above 80K: Market 56% vs Model 60.0%\n- Above 100K: Market 47% vs Model 50.7%\n-
Above 240K: Market 7% vs Model 7.5%\n\nThe market suggests roughly 56% probability of payrolls exceeding 80K, with declining probabilities for higher thresholds.\n\n**Relevant links:**\n- [Regional
Fed Survey Data - Philadelphia Fed](https://www.philadelphiafed.org/surveys-and-data/regional-economic-analysis/mbos-2025-12)\n- [BLS Birth/Death Model Historical
Data](https://www.bls.gov/web/empsit/cesbdhst.htm)\n- [BLS Foreign-Born Labor Force Statistics](https://www.bls.gov/news.release/empsit.t07.htm)\n- [NFIB Small Business Employment
Report](https://www.nfib.com/wp-content/uploads/2026/01/NFIB-SBET-Report-Dec.-2025.pdf)", "title": "US nonfarm payrolls for April 2026 Odds and Forecast | Octagon AI"}
```

## 💭 Thinking

Excellent! Now I have very rich data. Let me compile the key information and run a Monte Carlo simulation.

Key data points:
1. **Consensus forecasts**: Trading Economics ~70k, Investing.com ~73k, range 60-75k
2. **Kalshi prediction market**: Median around 80k (P(>80k) = 56%, P(>60k) = 62%, P(>100k) = 47%)
3. **Recent NFP prints**: Jan +160k (revised from +126k), Feb -133k (revised from -92k), Mar +178k


4. **Labor market cross-checks**: ADP came in much weaker at +62k for March, weekly averages around 39k, while ISM employment indices are contracting sharply (manufacturing at 46.4, services at 45.2). Initial jobless claims hit a 56-year low at 189k, but JOLTS shows job openings declining to pandemic lows at 6.9M in February.
5. **Unemployment rate**: Holding at 4.3% in March.

Now I'm working through what the Kalshi prediction market odds tell me about the distribution. The probabilities suggest a median somewhere around 90k—notably higher than the economist consensus of 60-75k—which means the market is pricing in a stronger print than most forecasters expect.

But there's a real tension in the data I need to reconcile. On one hand, initial claims are at 56-year lows and March came in solid at 178k, with construction and healthcare still firing on all cylinders and manufacturing PMI in expansion. On the other hand, the employment subcomponents are screaming weakness: ISM manufacturing employment is contracting at its worst level this year, services employment just posted one of its steepest drops since the pandemic, ADP is only tracking around 39k per week, and JOLTS hiring has cratered to pandemic lows. Blue-collar jobs are getting hit by tariffs, there are Fed layoffs happening, and 2025 got massively revised down to just 200k total versus the initial 1.2M report. Consumer sentiment is in the basement and job cuts remain elevated.

The March number itself is probably inflated—healthcare strike returns alone added 35k in physicians' offices, which won't repeat in April, and there's no other strike or weather effects to lean on this month. So I'm working with consensus estimates around 60-75k, though the Kalshi market is pricing in something closer to 85-90k. The ADP data is confusing me a bit since the weekly average of 39.25k doesn't quite line up with how the monthly figures are tracking, but the March ADP monthly came in at just 62k, well below the BLS's 178k.

The real puzzle is reconciling two opposing signals: initial claims are extremely low, suggesting minimal layoffs, but the ISM employment indices are contracting sharply in both manufacturing and services, which points to weak hiring. This fits the "low-hire, low-fire" pattern I'm seeing in the research. Weighing all this—the weak ISM readings, the historically low claims, the one-off boost from March, and ADP's softer March print—I'm settling on a center estimate around 70-80k with pretty wide uncertainty bands. Now I'm going to model this out with a Monte Carlo simulation to get a sense of the surprise distribution.

For the surprise component, I'm assuming a bias of roughly -10k to +5k in this late-cycle slowdown environment, with a standard deviation around 80-100k to account for the elevated uncertainty we're seeing, and I need to account for fat tails in the distribution.

## 💬 Response

Now let me run a Monte Carlo simulation to build my distribution, incorporating the consensus, leading indicators, and historical surprise distribution:

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom scipy import stats\n\nnp.random.seed(42)\nn_sims = 100000\n\n# === APPROACH 1: Consensus + Historical Surprise Distribution ===\n# Consensus estimate center\nconsensus = 70  # ~70k, midpoint of 60-75k range\n\n# In current regime (late cycle, high uncertainty), surprise std dev is ~85-100k\n# Using elevated std dev due to: tariff uncertainty, volatile recent data, \n# benchmark revision regime, ADP-BLS divergence\nsurprise_std = 90  # thousands\n\n# Regime-specific bias: in late-cycle/slowdown, bias is roughly -10k to +5k\n# With tariff headwinds and DOGE layoffs, lean slightly negative\nsurprise_bias = -5  \n\n# Fat tails: use t-distribution with ~5 degrees of freedom\ndf_t = 5\nsurprises_1 = stats.t.rvs(df=df_t, loc=surprise_bias, scale=surprise_std / np.sqrt(df_t / (df_t - 2)), size=n_sims)\nsim_1 = consensus + surprises_1\n\n# === APPROACH 2: Leading Indicator Model ===\n# ISM Manufacturing Employment: 46.4 (contracting)\n# ISM Services Employment: 45.2 (contracting sharply)\n# Initial Claims: 189k (very low = bullish)\n# ADP Monthly (March): 62k\n# JOLTS hiring: lowest since pandemic\n\n# ADP has been systematically below BLS recently, but the March divergence (62k vs 178k)\n# was extreme. ADP for April not yet released (releases May 6).\n# Typically ADP and BLS loosely track each other, but recent divergence is large.\n\n# ISM employment indices suggest weakness:\n# Manufacturing employment at 46.4 \u2192 implies manufacturing job losses\n# Services employment at 45.2 \u2192 implies services job losses\n# But initial claims at historic lows suggest no mass layoffs\n\n# Leading indicator model estimate:\n# - Healthcare: +30-40k (still strong, but no more strike returns)\n# - Government: -10 to +10k (DOGE cuts continue but may plateau)  \n# - Construction: +10-20k (seasonal boost)\n# - Manufacturing: -10 to 0k (ISM employment deeply contracting)\n# - Other private: +20-40k\n# Total: roughly +40 to +110k, center ~75k\n\nli_center = 75\nli_std = 45  # uncertainty from leading indicators\nsim_2 = np.random.normal(li_center, li_std, n_sims)\n\n# === APPROACH 3: Recent Trajectory Model ===\n# Recent 3-month average (using initial releases): \n# Jan +126k (revised), Feb -133k (revised), Mar +178k\n# 3-month avg of initial releases: Jan +130, Feb -92, Mar +178 \u2192 avg = 72k\n# But huge volatility. Use the revised 3-month avg as center with high dispersion\n\ntraj_center = 70\ntraj_std = 70\nsim_3 = np.random.normal(traj_center, traj_std, n_sims)\n\n# === APPROACH 4: Kalshi Market-Implied Distribution ===\n# Back out the implied distribution from Kalshi contract prices\n# P(>0) = 93%, P(>40) = 77%, P(>60) = 62%, P(>80) = 56%, \n# P(>100) = 47%, P(>120) = 40%, P(>140) = 33%, P(>160) = 26%, \n# P(>180) = 18%, P(>200) = 9%\n\n# The Kalshi data implies median ~85-90k with heavy right tail\n# This is more bullish than economist consensus\nkalshi_center = 87\nkalshi_std = 75\nsim_4 = np.random.normal(kalshi_center, kalshi_std, n_sims)\n\n# === COMBINE ALL APPROACHES ===\n# Weight: Kalshi market 30%, Leading indicators 25%, Consensus+surprise 30%, Trajectory 15%\nweights = [0.30, 0.25, 0.30, 0.15]\napproaches = [sim_1, sim_2, sim_4, sim_3]\n\n# Sample from mixture\nmixture_choice = np.random.choice(4, size=n_sims, p=weights)\ncombined = np.array([approaches[c][i] for i, c in enumerate(mixture_choice)])\n\n# Calculate percentiles\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\npct_values = np.percentile(combined, percentiles)\n\nprint(\"=== Combined Distribution ===\")\nfor p, v in zip(percentiles, pct_values):\n    print(f\"  P{p:2d}: {v:8.1f}k\")\n\nprint(f\"\\n  Mean: {np.mean(combined):.1f}k\")\nprint(f\"  Std:  {np.std(combined):.1f}k\")\nprint(f\"  P(negative): {np.mean(combined < 0)*100:.1f}%\")\nprint(f\"  P(>100): {np.mean(combined > 100)*100:.1f}%\")\nprint(f\"  P(>150): {np.mean(combined > 150)*100:.1f}%\")\nprint(f\"  P(>200): {np.mean(combined > 200)*100:.1f}%\")\n\nprint(\"\\n=== Individual Approach Medians ===\")\nfor i, (name, sim) in enumerate(zip(\n    [\"Consensus+surprise\", \"Leading indicators\", \"Kalshi market\", \"Recent trajectory\"],\n    [sim_1, sim_2, sim_4, sim_3])):\n    print(f\"  {name}: median={np.median(sim):.1f}, P10={np.percentile(sim,10):.1f}, P90={np.percentile(sim,90):.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Combined Distribution ===\n  P 1:   -111.3k\n  P 5:    -42.2k\n  P10:    -12.2k\n  P20:     19.7k\n  P25:     31.1k\n  P30:     41.0k\n  P40:     58.6k\n  P50:
74.5k\n  P60:     90.8k\n  P70:    108.6k\n  P75:    118.8k\n  P80:    130.3k\n  P90:    162.7k\n  P95:    192.1k\n  P99:    256.0k\n\n  Mean: 74.7k\n  Std:  73.9k\n  P(negative): 13.1%\n  P(>100):
34.6%\n  P(>150): 13.3%\n  P(>200): 4.1%\n\n=== Individual Approach Medians ===\n  Consensus+surprise: median=64.3, P10=-38.6, P90=167.9\n  Leading indicators: median=75.1, P10=17.6, P90=132.8\n
Kalshi market: median=86.8, P10=-9.3, P90=183.6\n  Recent trajectory: median=69.5, P10=-20.0, P90=159.6\n", "stderr": "", "duration_ms": 1627}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also validate against the Kalshi market-implied distribution\n# by comparing my CDF to their contract prices\n\nkalshi_thresholds = [0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240]\nkalshi_probs = [0.93, 0.86, 0.77, 0.62, 0.56, 0.47, 0.40, 0.33, 0.26, 0.18, 0.09, 0.08, 0.07]\n\nprint(\"=== Comparison: My Distribution vs Kalshi Market ===\")\nprint(f\"{'Threshold':>12s} {'My P(>X)':>10s} {'Kalshi P(>X)':>12s} {'Diff':>8s}\")\nfor t, kp in zip(kalshi_thresholds, kalshi_probs):\n    my_p = np.mean(combined > t)\n    print(f\"{t:>10d}k {my_p:>10.1%} {kp:>12.1%} {(my_p-kp)*100:>+7.1f}pp\")\n\nprint(\"\\n=== Sensitivity Analysis ===\")\n\n# Test with shifted center (more bearish)\nsim_bearish = combined - 15  # shift down 15k\npct_bearish = np.percentile(sim_bearish, [10, 25, 50, 75, 90])\nprint(f\"Bearish scenario (center -15k): P10={pct_bearish[0]:.0f}, P25={pct_bearish[1]:.0f}, P50={pct_bearish[2]:.0f}, P75={pct_bearish[3]:.0f}, P90={pct_bearish[4]:.0f}\")\n\n# Test with shifted center (more bullish)\nsim_bullish = combined + 15  # shift up 15k\npct_bullish = np.percentile(sim_bullish, [10, 25, 50, 75, 90])\nprint(f\"Bullish scenario (center +15k): P10={pct_bullish[0]:.0f}, P25={pct_bullish[1]:.0f}, P50={pct_bullish[2]:.0f}, P75={pct_bullish[3]:.0f}, P90={pct_bullish[4]:.0f}\")\n\n# Test with wider uncertainty (\u03c3 scaled up 20%)\nsim_wider = combined * 1.15 + 74.7 * (1 - 1.15)  # scale around mean\npct_wider = np.percentile(sim_wider, [10, 25, 50, 75, 90])\nprint(f\"Wider uncertainty (+15% \u03c3): P10={pct_wider[0]:.0f}, P25={pct_wider[1]:.0f}, P50={pct_wider[2]:.0f}, P75={pct_wider[3]:.0f}, P90={pct_wider[4]:.0f}\")\n\n# Check: width vs recent volatility\nrecent_data = np.array([130, -92, 178])  # initial releases Jan-Mar 2026\nprint(f\"\\nRecent monthly NFP std dev: {np.std(recent_data):.0f}k\")\nprint(f\"My distribution std dev: {np.std(combined):.0f}k\")\nprint(f\"My 80% CI width: {np.percentile(combined,90) - np.percentile(combined,10):.0f}k\")\nprint(f\"Random walk width (1 std dev): \u00b1{np.std(recent_data):.0f}k\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Comparison: My Distribution vs Kalshi Market ===\n   Threshold   My P(>X) Kalshi P(>X)     Diff\n         0k      87.0%        93.0%    -6.0pp\n        20k      79.9%
86.0%    -6.1pp\n        40k      70.5%        77.0%    -6.5pp\n        60k      59.1%        62.0%    -2.9pp\n        80k      46.6%        56.0%    -9.4pp\n       100k      34.6%        47.0%
-12.4pp\n       120k      24.5%        40.0%   -15.5pp\n       140k      16.5%        33.0%   -16.5pp\n       160k      10.6%        26.0%   -15.4pp\n       180k       6.7%        18.0%   -11.3pp\n
200k       4.1%         9.0%    -4.9pp\n       220k       2.5%         8.0%    -5.5pp\n       240k       1.5%         7.0%    -5.5pp\n\n=== Sensitivity Analysis ===\nBearish scenario (center -15k):
P10=-27, P25=16, P50=60, P75=104, P90=148\nBullish scenario (center +15k): P10=3, P25=46, P50=90, P75=134, P90=178\nWider uncertainty (+15% \u03c3): P10=-25, P25=25, P50=75, P75=125, P90=176\n\nRecent
monthly NFP std dev: 118k\nMy distribution std dev: 74k\nMy 80% CI width: 175k\nRandom walk width (1 std dev): \u00b1118k\n", "stderr": "", "duration_ms": 9}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# My distribution is notably more bearish than Kalshi, especially at the upper end.\n# The Kalshi market implies a much heavier right tail. Let me think about why...\n# \n# The initial claims at 189k (lowest since 1969) is a very strong bullish signal\n# that I may be underweighting. Also, March was +178k and while healthcare strikes\n# returning was a one-off, the underlying economy may be stronger than ISM surveys suggest.\n#\n# Let me recalibrate with more weight to the Kalshi market signal,\n# while keeping my bearish adjustments for ISM weakness.\n\n# Revised mixture: give more weight to Kalshi\n# Also adjust the consensus+surprise to have a slightly less negative bias\n# given the extraordinary claims data\n\nn_sims = 200000\nnp.random.seed(42)\n\n# Approach 1: Consensus + surprise (adjusted)\nconsensus = 72  # slightly higher given claims data\nsurprise_bias = 0  # remove negative bias, claims are very strong\nsurprise_std = 85\ndf_t = 5\nsurprises_1 = stats.t.rvs(df=df_t, loc=surprise_bias, scale=surprise_std / np.sqrt(df_t / (df_t - 2)), size=n_sims)\nsim_1 = consensus + surprises_1\n\n# Approach 2: Leading indicators (adjusted slightly higher)\nli_center = 80\nli_std = 45\nsim_2 = np.random.normal(li_center, li_std, n_sims)\n\n# Approach 3: Kalshi market-implied\n# The Kalshi median is ~90k. The right tail is heavier.\n# Use a slightly right-skewed distribution\nkalshi_center = 90\nkalshi_std = 72\n# Add slight right skew using log-normal component\nkalshi_base = np.random.normal(kalshi_center, kalshi_std, n_sims)\nsim_3 = kalshi_base\n\n# Approach 4: Claims-based model\n# Initial claims at 189k with 4-week avg at 207k\n# Historically, claims this low are associated with NFP of 100-200k\n# But hiring is also at pandemic lows, so net effect is more moderate\nclaims_center = 95\nclaims_std = 50\nsim_4 = np.random.normal(claims_center, claims_std, n_sims)\n\n# === COMBINE ===\n# Kalshi 30%, Claims 15%, Leading indicators 20%, Consensus+surprise 25%, Trajectory 10%\nweights = [0.25, 0.20, 0.30, 0.15, 0.10]\napproaches = [sim_1, sim_2, sim_3, sim_4, np.random.normal(70, 70, n_sims)]\n\nmixture_choice = np.random.choice(5, size=n_sims, p=weights)\ncombined_v2 = np.array([approaches[c][i] for i, c in enumerate(mixture_choice)])\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\npct_values = np.percentile(combined_v2, percentiles)\n\nprint(\"=== Revised Combined Distribution ===\")\nfor p, v in zip(percentiles, pct_values):\n    print(f\"  P{p:2d}: {v:8.1f}k\")\n\nprint(f\"\\n  Mean: {np.mean(combined_v2):.1f}k\")\nprint(f\"  Std:  {np.std(combined_v2):.1f}k\")\nprint(f\"  P(negative): {np.mean(combined_v2 < 0)*100:.1f}%\")\n\nprint(\"\\n=== Comparison: Revised vs Kalshi Market ===\")\nprint(f\"{'Threshold':>12s} {'My P(>X)':>10s} {'Kalshi P(>X)':>12s} {'Diff':>8s}\")\nfor t, kp in zip(kalshi_thresholds, kalshi_probs):\n    my_p = np.mean(combined_v2 > t)\n    print(f\"{t:>10d}k {my_p:>10.1%} {kp:>12.1%} {(my_p-kp)*100:>+7.1f}pp\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Revised Combined Distribution ===\n  P 1:    -92.6k\n  P 5:    -28.2k\n  P10:     -0.3k\n  P20:     30.4k\n  P25:     41.1k\n  P30:     50.5k\n  P40:     67.2k\n  P50:
82.6k\n  P60:     97.9k\n  P70:    114.6k\n  P75:    123.9k\n  P80:    134.7k\n  P90:    164.3k\n  P95:    191.1k\n  P99:    249.6k\n\n  Mean: 82.1k\n  Std:  68.9k\n  P(negative): 10.1%\n\n===
Comparison: Revised vs Kalshi Market ===\n   Threshold   My P(>X) Kalshi P(>X)     Diff\n         0k      89.9%        93.0%    -3.1pp\n        20k      84.1%        86.0%    -1.9pp\n        40k
75.5%        77.0%    -1.5pp\n        60k      64.4%        62.0%    +2.4pp\n        80k      51.7%        56.0%    -4.3pp\n       100k      38.7%        47.0%    -8.3pp\n       120k      27.0%
40.0%   -13.0pp\n       140k      17.8%        33.0%   -15.2pp\n       160k      11.1%        26.0%   -14.9pp\n       180k       6.6%        18.0%   -11.4pp\n       200k       3.9%         9.0%
-5.1pp\n       220k       2.3%         8.0%    -5.7pp\n       240k       1.3%         7.0%    -5.7pp\n", "stderr": "", "duration_ms": 51}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# My distribution still has less probability in the right tail than Kalshi.\n# The Kalshi market seems to have substantial probability mass at 120-180k.\n# This could be because:\n# 1. Market participants expect a repeat of March's upside surprise\n# 2. Very low claims data suggests strong labor market\n# 3. Possible positive seasonal adjustments for April\n#\n# However, I think the Kalshi right tail is somewhat overpriced because:\n# 1. March's healthcare strike return (+35k one-off) won't repeat\n# 2. ISM employment indices both deeply contractionary\n# 3. DOGE federal layoffs continuing\n# 4. ADP monthly running well below BLS\n#\n# I'll stick with my revised distribution but note the discrepancy.\n# My distribution is slightly more bearish than the market, \n# particularly in the 100-180k range, which I believe is justified\n# by the ISM employment weakness.\n\n# Let me also check: what if we just fit directly to the Kalshi data?\nfrom scipy.optimize import minimize\n\ndef kalshi_loss(params):\n    mu, sigma = params\n    total_loss = 0\n    for t, kp in zip(kalshi_thresholds, kalshi_probs):\n        my_p = 1 - stats.norm.cdf(t, mu, sigma)\n        total_loss += (my_p - kp)**2\n    return total_loss\n\nresult = minimize(kalshi_loss, [90, 80], method='Nelder-Mead')\nkalshi_mu, kalshi_sigma = result.x\nprint(f\"Kalshi-implied normal: mean={kalshi_mu:.1f}k, std={kalshi_sigma:.1f}k\")\nprint(f\"Kalshi-implied median: {kalshi_mu:.1f}k\")\nprint(f\"Kalshi-implied P10: {kalshi_mu - 1.28*kalshi_sigma:.1f}k\")\nprint(f\"Kalshi-implied P90: {kalshi_mu + 1.28*kalshi_sigma:.1f}k\")\n\n# The Kalshi contracts have some unusual behavior at the top (220k=8%, 240k=7%)\n# which may indicate thin liquidity and stale prices at the extremes.\n# Let me exclude the top 2 contracts and refit\ndef kalshi_loss_trimmed(params):\n    mu, sigma = params\n    total_loss = 0\n    for t, kp in zip(kalshi_thresholds[:11], kalshi_probs[:11]):\n        my_p = 1 - stats.norm.cdf(t, mu, sigma)\n        total_loss += (my_p - kp)**2\n    return total_loss\n\nresult2 = minimize(kalshi_loss_trimmed, [90, 80], method='Nelder-Mead')\nkalshi_mu2, kalshi_sigma2 = result2.x\nprint(f\"\\nKalshi-implied (trimmed): mean={kalshi_mu2:.1f}k, std={kalshi_sigma2:.1f}k\")\nprint(f\"Kalshi-implied (trimmed) P10: {kalshi_mu2 - 1.28*kalshi_sigma2:.1f}k\")\nprint(f\"Kalshi-implied (trimmed) P90: {kalshi_mu2 + 1.28*kalshi_sigma2:.1f}k\")\n\n# Final summary of my chosen distribution\nprint(\"\\n\" + \"=\"*60)\nprint(\"=== FINAL DISTRIBUTION (Revised V2) ===\")\nprint(\"=\"*60)\npct_list = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nfinal_pcts = np.percentile(combined_v2, pct_list)\nfor p, v in zip(pct_list, final_pcts):\n    print(f\"  P{p:2d}: {v:7.1f}\")\n\nprint(f\"\\n  Mean:   {np.mean(combined_v2):.1f}\")\nprint(f\"  Median: {np.median(combined_v2):.1f}\")\nprint(f\"  Std:    {np.std(combined_v2):.1f}\")\nprint(f\"  80% CI: [{np.percentile(combined_v2,10):.1f}, {np.percentile(combined_v2,90):.1f}]\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Kalshi-implied normal: mean=98.6k, std=84.2k\nKalshi-implied median: 98.6k\nKalshi-implied P10: -9.2k\nKalshi-implied P90: 206.3k\n\nKalshi-implied (trimmed): mean=98.3k,
std=83.2k\nKalshi-implied (trimmed) P10: -8.2k\nKalshi-implied (trimmed) P90: 204.8k\n\n============================================================\n=== FINAL DISTRIBUTION (Revised V2)
===\n============================================================\n  P 1:   -92.6\n  P 5:   -28.2\n  P10:    -0.3\n  P20:    30.4\n  P25:    41.1\n  P30:    50.5\n  P40:    67.2\n  P50:    82.6\n
P60:    97.9\n  P70:   114.6\n  P75:   123.9\n  P80:   134.7\n  P90:   164.3\n  P95:   191.1\n  P99:   249.6\n\n  Mean:   82.1\n  Median: 82.6\n  Std:    68.9\n  80% CI: [-0.3, 164.3]\n", "stderr":
"", "duration_ms": 47}
```

## 💭 Thinking

Let me now assess my distribution. The Kalshi market-implied normal has mean ~98.6k and std ~84.2k, while my distribution has mean ~82.1k and std ~68.9k. 

My distribution is about 16k lower in center and about 15k narrower than Kalshi. Let me think about whether this is justified.

Reasons my center might be lower than Kalshi:
1. ISM Manufacturing Employment fell to 46.4 (deeply contracting) - this is bearish
2. ISM Services Employment was 45.2 in March (one of steepest drops since pandemic) - very bearish


3. March's +178k was partly a one-off from healthcare strikes returning
4. ADP monthly at only 62k for March vs 178k BLS
5. JOLTS hiring at pandemic lows

But there's a strong counterargument: initial claims just hit a 56-year low at 189k, which is extraordinarily bullish and directly relevant to April. The Kalshi market also aggregates substantial information, and recent months have tended to beat consensus.

On volatility, the recent NFP prints have been all over the place—ranging from -92k to +178k—so my distribution might actually be too tight given that kind of swings.

Looking at the confidence intervals, my 80% CI spans about 165k wide while Kalshi implies a 216k width, suggesting the market is pricing in more tail risk than I am. The ISM employment data does support a narrower distribution—manufacturing at 46.4 and services at 45.2 both point against a strong right tail—but I'm realizing I don't have April's ISM Services reading yet, which could shift things.

More importantly, I need to reconsider the timing of the claims data relative to the survey reference period. The April employment survey was conducted mid-April around the April 12 pay period, but the 189k claims figure from April 25 falls outside that window, so it's not directly informative about the April jobs report. I should trace back which claims weeks actually overlap with the survey reference period to properly assess the employment picture. The ADP report for April won't be released until May 6, so I can't use that yet. The weekly pulse data through mid-April showed about 39,250 jobs per week over four weeks, which would translate to roughly 157k in monthly terms, but this uses a different methodology than the official monthly ADP report and tends to diverge significantly from it.

## 💬 Response

Now let me run the reflection checkpoint:

## 💭 Thinking

The reflection shows:
- Factor-implied median: 74.1k
- My tentative center: 83k (gap of ~9k, about 10%)
- Spread ratio: 1.78 (my range is wider than factor-implied range)

The 10% gap is reasonable - I'm slightly above the factor-implied median because I'm giving extra weight to the very strong initial claims data and the Kalshi market signal, which pulls the center up somewhat.

The spread ratio of 1.78 means my uncertainty is wider than what the factors alone would suggest, which is appropriate given the mixture approach and the extreme recent volatility (3-month std of 118k for initial releases).


Now I'm going to work through a premortem to identify what could go wrong with this estimate.

## 💬 Response

Now let me run the premortem:
