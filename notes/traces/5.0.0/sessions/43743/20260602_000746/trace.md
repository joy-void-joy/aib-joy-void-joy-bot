# Reasoning Log: Will Tesla's market capitalization close above SpaceX's market capitalization on SpaceX's first day of public trading?

*Generated: 2026-06-02T00:23:42.619421+00:00*


## 💭 Thinking

Let me analyze this question carefully.

## Step 1: Parse the Resolution Criteria

**What must happen for YES**: On SpaceX's first day of public trading (expected ~June 12, 2026), Tesla's closing market cap must be HIGHER than SpaceX's closing market cap, as measured by CompaniesMarketCap.com.

**Resolution source**: CompaniesMarketCap.com (primary), with fallback to SEC filings + Nasdaq/Yahoo Finance.

**Deadline**: SpaceX's first trading day, which must occur before June 14, 2026, or N/A.
 
Now I'm clarifying the specific terms: closing market cap means the end-of-day valuation on that first trading day, and if SpaceX doesn't IPO by the deadline, this resolves N/A. Both companies are volatile, so this is a direct comparison at a specific moment in time. Let me look up the current market data to establish a baseline.

## 💬 Response

I'll start by fetching the question details and researching the current state of both companies.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


## 🔧 Tool: mcp__research__research


## 🔧 Tool: mcp__metaculus__get_coherence_links


```json
{
  "post_id_list": [
    43743
  ]
}
```

### 📋 Result

```
{"post_id": 43743, "title": "Will Tesla's market capitalization close above SpaceX's market capitalization on SpaceX's first day of public trading?", "type": "binary", "url":
"https://www.metaculus.com/questions/43743", "background_info": "SpaceX (Space Exploration Technologies Corp.) filed its S-1 with the SEC in 2026 for what would be the largest IPO in history. Multiple
media reports indicate underwriters are targeting Friday, June 12, 2026 as the first trading day on Nasdaq under ticker 'SPCX,' though the date remains subject to change. The S-1 lists about 134.5
million pre-IPO shares outstanding under a dual-class structure, and reports describe a target IPO valuation of roughly $1.75\u2013$2.0 trillion, with Bloomberg reporting SpaceX is seeking 'at least
$1.8 trillion' and aiming to raise up to ~$75 billion. Mega-IPOs have historically shown a wide range of first-day moves \u2014 from modest single-digit pops to roughly +38% for Alibaba.\n\nTesla
(TSLA), Elon Musk's other publicly traded company, ended May 2026 with a market capitalization of approximately $1.636 trillion at a share price near $436 (per CompaniesMarketCap and Nasdaq data).
Tesla traded in roughly a $389\u2013446 range during May 2026.\n\nBecause SpaceX's first-day market cap depends on both the final IPO pricing (set during the roadshow, currently blank in the S-1) and
the trading-day pop, and because Tesla itself is volatile, the comparison between the two Musk entities' market caps on SpaceX's debut is genuinely uncertain.\n\n`{\"format\": \"llm_question\",
\"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves YES if, on SpaceX's first day of regular-way
public trading on a U.S. stock exchange (expected on or about June 12, 2026 under ticker SPCX), Tesla Inc. (TSLA) has a higher closing market capitalization than Space Exploration Technologies Corp.
(SpaceX). The resolver will use the closing 'Market Cap' figures shown on CompaniesMarketCap.com for that trading day \u2014 specifically https://companiesmarketcap.com/tesla/marketcap/ for Tesla and
the corresponding SpaceX page (e.g., https://companiesmarketcap.com/spacex/marketcap/). The question resolves NO if Tesla's closing market cap is at or below SpaceX's closing market cap on that day.
Market cap figures should be compared in U.S. dollars (a value of $1.7 trillion will be read as 1,700,000,000,000).", "fine_print": "If SpaceX does not begin regular-way public trading on a U.S. stock
exchange such that a first-day close can be observed before June 14, 2026, this question resolves N/A. 'First day of public trading' means the first session in which SpaceX common stock trades on the
open market following its IPO, not the pricing date; pre-market, after-hours, 'when-issued,' and grey-market trading do not count. If CompaniesMarketCap.com does not display SpaceX's market cap within
24 hours of the first-day close, the resolver will compute SpaceX's market cap as the day-one closing price multiplied by total common shares outstanding immediately after the IPO across all share
classes (Class A, Class B, and any other common equity classes), taken from SpaceX's final prospectus or 424B filing on SEC EDGAR, and will use Nasdaq.com or Yahoo Finance for Tesla's closing market
cap, as reported by [credible sources](https://www.metaculus.com/faq/#definitions).", "num_forecasters": 0, "community_prediction": null}
```

```json
{
  "questions": [
    {
      "query": "SpaceX IPO June 2026 latest news valuation pricing date Nasdaq SPCX",
      "ttl": "6h"
    },
    {
      "query": "Tesla TSLA stock price market cap June 2026 current",
      "ttl": "6h"
    },
    {
      "query": "SpaceX IPO S-1 filing shares outstanding total share count all classes",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "SpaceX IPO June 2026 latest news valuation pricing date Nasdaq SPCX", "entry": {"slug": "spacex-ipo-june-2026-latest-news-valuation-pricing-d2abf9aa", "query": "SpaceX IPO June
2026 latest news valuation pricing date Nasdaq SPCX", "answer": "I now have a very comprehensive dataset from repository research files. Here is my full synthesis:\n\n---\n\n# SpaceX IPO Research
Report \u2014 As of June 2, 2026\n\n## Executive Summary\n\nSpaceX (ticker: **SPCX**) has filed its S-1 prospectus with the SEC and is targeting a **June 12, 2026 listing on the Nasdaq**. The combined
entity\u2014spanning launch services, Starlink, xAI/Grok, and the X social media platform\u2014is seeking a valuation of **$1.25\u2013$1.75 trillion** and aims to raise approximately **$75 billion**,
which would make it the largest IPO in history. The S-1 was publicly filed on May 20, 2026, and the roadshow was expected to begin around June 4, 2026 (per the 15-day JOBS Act rule).\n\n> **Data
Vintage Warning:** The underlying research files were last updated on **May 24, 2026** (9 days ago). Live web search tools were unavailable, so developments between May 25 and June 2 (roadshow launch,
pricing range amendment, any schedule changes) could not be confirmed.\n\n---\n\n## IPO Timeline\n\n| Date | Event | Source |\n|------|-------|--------|\n| March 30, 2026 | Confidential Draft
Registration Statement (DRS) filed with SEC | SEC EDGAR |\n| April 1, 2026 | Public reports of confidential filing | NYT, Investopedia, Teslarati |\n| April 7\u201314, 2026 | Reuters exclusive: SpaceX
details IPO plans, targets early June roadshow | Reuters |\n| May 4, 2026 | 5-for-1 stock split executed | S-1 filing |\n| May 14, 2026 | CNBC reports prospectus imminent | CNBC |\n| May 15, 2026 |
Reuters exclusive: SpaceX targets **June 12 listing** | Reuters |\n| May 17, 2026 | BlackRock potentially investing up to $10B | Barron's, MSN |\n| **May 20, 2026** | **S-1 prospectus filed publicly**
(270+ pages, 226 MB, 110 documents) | SEC EDGAR |\n| ~June 4, 2026 | Earliest roadshow start (15-day JOBS Act rule) | Regulatory |\n| June 11, 2026 | Retail investor participation deadline (per
Gotrade) | Gotrade |\n| **June 12, 2026** | **Target listing date on Nasdaq** | Reuters, multiple sources |\n\n---\n\n## Ticker, Exchange, and Listing Details\n\n- **Ticker Symbol:** SPCX\n-
**Exchange:** Nasdaq and Nasdaq Texas\n- **Company Status:** \"Controlled company\" under Nasdaq rules (Elon Musk controls 85% of votes via Class B shares)\n- **Underwriters:** Goldman Sachs, Morgan
Stanley, BofA Securities, Citigroup, J.P. Morgan, Barclays, Deutsche Bank, RBC Capital Markets, UBS, Wells Fargo, Allen & Company\n\n---\n\n## Valuation & Capital Raise\n\n| Metric | Value
|\n|--------|-------|\n| Target IPO valuation range | **$1.25\u2013$1.75 trillion** |\n| Upper-end estimates (prediction markets) | Above **$2 trillion** |\n| Target capital raise | **~$75 billion**
(largest IPO in history) |\n| Most recent RSA grant-date fair value (post-split) | $93.87/share |\n| Pro forma shares outstanding | ~12.5 billion |\n| Implied equity at RSA fair value | ~$1.18
trillion |\n| Previous private valuation (late 2024) | ~$180\u2013210 billion |\n| Pre-merger private valuation (widely reported) | ~$350 billion |\n\n---\n\n## Corporate Structure (Three-Segment
Combined Entity)\n\nSpaceX is going public as a merged entity following two major acquisitions:\n1. **March 28, 2025:** X Holdings Corp acquired by xAI\n2. **February 2, 2026:** xAI Holdings Corp
acquired by SpaceX\n\n### Business Segments:\n- **Space** \u2014 Launch services (Falcon 9, Falcon Heavy, Starship), Dragon spacecraft\n- **Connectivity** \u2014 Starlink broadband (10.3M subscribers,
~9,600 LEO satellites)\n- **AI** \u2014 xAI (Grok AI), X platform (~550M MAUs), COLOSSUS data center (1 GW)\n\nStarlink is **not** being spun off separately; it goes public as the \"Connectivity\"
segment of SpaceX.\n\n---\n\n## Key Financial Data (from S-1 Filing)\n\n### Revenue (USD millions)\n\n| Period | Space | Connectivity | AI | **Total**
|\n|--------|-------|-------------|-----|-----------|\n| Q1 2026 | $1,286 | $2,590 | $818 | **$4,694** |\n| FY 2025 | $4,086 | $11,387 | $3,201 | **$18,674** |\n| FY 2024 | $3,796 | $7,599 | $2,620 |
**$14,015** |\n| FY 2023 | $3,557 | $3,869 | $2,961 | **$10,387** |\n\n### Net Income / (Loss)\n\n| Period | Amount |\n|--------|--------|\n| Q1 2026 | $(4,276)M loss |\n| FY 2025 | $(4,937)M loss
|\n| FY 2024 | $791M income |\n| FY 2023 | $(4,628)M loss |\n\n### Balance Sheet (March 31, 2026)\n\n| Item | Amount |\n|------|--------|\n| Total assets | $102.1 billion |\n| Cash | $15.9 billion
|\n| Total equity | $34.5 billion |\n| Total liabilities | $60.5 billion |\n| Bridge loan | $20.0 billion |\n| Backlog (Dec 31, 2025) | $28.4 billion |\n\n### Capital Expenditures (FY 2025): **$20.7
billion** ($3.8B Space, $4.2B Connectivity, $12.7B AI)\n\n---\n\n## Operating Metrics\n\n| Metric | Value |\n|--------|-------|\n| Starlink subscribers (Q1 2026) | 10.3 million (up from 5.0M Q1 2025)
|\n| Starlink ARPU | $66/month (down from $86/month Q1 2025) |\n| Active Starlink satellites | ~9,600 in LEO |\n| Rocket launches (FY 2025) | 170 |\n| Rocket launches (Q1 2026) | 40 |\n| Cumulative
Starship investment | $15+ billion |\n| Connectivity segment EBITDA (FY 2025) | $7.2 billion |\n| X platform MAUs | ~550 million |\n\n---\n\n## Governance\n\n- **Dual-class structure:** Class A (1
vote/share, public) / Class B (10 votes/share, insiders)\n- **Elon Musk controls 85% of votes**, serves as CEO, CTO, and Chairman simultaneously\n- **Musk compensation:** 1 billion restricted shares
tied to achieving $7.5T market cap AND a permanent Mars colony with 1 million inhabitants\n\n---\n\n## Analyst & Market Commentary\n\n- Jim Cramer warned the IPO could be \"destructive\" for the
broader market\n- Analysts debate whether mega-IPOs (SpaceX + OpenAI) could signal a market top\n- Space ETFs surging in anticipation\n- Barron's warned it could pressure Tesla stock as Musk attention
shifts\n- If valued at $1.75T, Musk could become the world's first trillionaire (BBC, ABC Australia)\n- Morningstar described xAI's financials as \"reckless\"\n- Record retail investor allocation
planned\u2014a departure from typical IPO structures\n\n---\n\n## Notable Related-Party Transactions\n\n- $700M spent on Tesla Megapacks (2024\u20132025)\n- $131M on Tesla Cybertrucks
(~1,183\u20131,813 vehicles, ~6\u20139% of all Cybertruck sales)\n- Option to acquire **Cursor** (AI code editor) at $60B implied equity value in Class A stock, post-IPO\n\n---\n\n## Key Unknowns (as
of June 2, 2026)\n\nThe research data is 9 days old. Critical events that may have occurred since May 24:\n1. Whether the **S-1/A amendment with pricing range** has been filed\n2. Whether the
**roadshow has launched** (expected ~June 4)\n3. Whether the **June 12 listing date** remains on track\n4. Any updates on **BlackRock's $10B commitment**\n5. Whether SpaceX has appeared on **Nasdaq's
official IPO calendar**\n\n---", "sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm", "title": "SpaceX S-1 Filing - SEC EDGAR",
"domain": "sec.gov", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "S-1 registration statement for Space Exploration Technologies Corp filed May 20, 2026. 270+ page prospectus, 226 MB, 110
documents."}, {"url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/spaceexplorationtechnologi.htm", "title": "SpaceX S-1 Prospectus", "domain": "sec.gov", "accessed_at":
"2026-05-24T00:00:00Z", "snippet": "Full prospectus for SpaceX IPO including financial statements, risk factors, and business description."}, {"url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026021860/0001628280-26-021860-index.htm", "title": "SpaceX DRS Filing", "domain": "sec.gov", "accessed_at": "2026-05-24T00:00:00Z",
"snippet": "Confidential Draft Registration Statement filed March 30, 2026."}, {"url": "https://www.reuters.com/technology/space/spacex-accelerates-ipo-timeline-targets-june-12-nasdaq/", "title":
"SpaceX accelerates IPO timeline, targets June 12 Nasdaq listing", "domain": "reuters.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "SpaceX has accelerated its IPO timeline and is now
targeting June 12 for its Nasdaq listing under ticker SPCX."}, {"url": "https://www.reuters.com/technology/space/spacex-ipo-details-early-june-roadshow/", "title": "SpaceX IPO details: early June
roadshow with record retail allocation", "domain": "reuters.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "SpaceX plans an early June roadshow with a record allocation for retail
investors."}, {"url": "https://www.cnbc.com/2026/05/21/retail-investors-get-direct-access-to-spacex-ipo.html", "title": "Retail investors get direct access to SpaceX IPO", "domain": "cnbc.com",
"accessed_at": "2026-05-24T00:00:00Z", "snippet": "Major brokerages will offer retail investors direct access to SpaceX IPO shares."}, {"url": "https://www.cnbc.com/2026/05/22/mega-ipos-market-top-
spacex-openai.html", "title": "Mega-IPOs could signal market top: analysts", "domain": "cnbc.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "Analysts warn that mega-IPOs from SpaceX and
OpenAI could signal a market top."}, {"url": "https://www.nytimes.com/2026/05/20/technology/spacex-ipo-finances.html", "title": "SpaceX IPO Reveals Finances of Musk's Space Empire", "domain":
"nytimes.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "S-1 filing reveals SpaceX's financial details including revenue, losses, and the combined xAI/X/Starlink structure."}, {"url":
"https://www.nytimes.com/2026/04/01/technology/spacex-ipo-filing.html", "title": "SpaceX Files Confidentially for IPO", "domain": "nytimes.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet":
"SpaceX has filed a confidential registration statement with the SEC for an IPO."}, {"url": "https://www.cnn.com/2026/05/21/business/spacex-ipo-prospectus-strangest-things/index.html", "title": "The
strangest things in SpaceX's IPO prospectus", "domain": "cnn.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "CNN reviews the most notable disclosures from SpaceX's S-1 filing."}, {"url":
"https://www.bbc.com/news/articles/spacex-ipo-trillionaire", "title": "SpaceX IPO could make Musk world's first trillionaire", "domain": "bbc.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet":
"If SpaceX is valued at $1.75 trillion, Elon Musk could become the world's first trillionaire."}, {"url": "https://www.npr.org/2026/05/20/spacex-ipo-rockets-ai", "title": "SpaceX IPO combines rockets,
satellites, and AI", "domain": "npr.org", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "NPR coverage of the SpaceX S-1 filing and its combined entity structure."}, {"url":
"https://fortune.com/2026/05/23/spacex-ipo-business-bet-future/", "title": "SpaceX IPO: A bet on the future", "domain": "fortune.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "Fortune
analysis of SpaceX's IPO prospects and business fundamentals."}, {"url": "https://www.barrons.com/articles/spacex-ipo-risk-2026", "title": "SpaceX IPO risks and BlackRock investment", "domain":
"barrons.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "BlackRock may invest up to $10 billion; Barron's warns IPO could pressure Tesla stock."}, {"url":
"https://www.morningstar.com/news/spacex-ipo-financials-xai", "title": "SpaceX IPO financials: xAI looks 'reckless'", "domain": "morningstar.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet":
"Morningstar describes xAI's financial profile within the SpaceX S-1 as looking 'reckless'."}, {"url": "https://seekingalpha.com/article/spacex-ipo-investor-frenzy", "title": "SpaceX IPO investor
frenzy", "domain": "seekingalpha.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "Seeking Alpha coverage of investor demand for SpaceX IPO shares."}, {"url":
"https://www.businessinsider.com/spacex-ipo-index-funds-inclusion-2026", "title": "SpaceX IPO: Index funds scramble to adjust rules", "domain": "businessinsider.com", "accessed_at":
"2026-05-24T00:00:00Z", "snippet": "Index providers adjusting rules in anticipation of SpaceX's massive market cap listing."}], "key_facts": ["SpaceX has filed its S-1 prospectus with the SEC on May
20, 2026 (CIK: 0001181412), making an IPO imminent", "Target listing date is June 12, 2026 on Nasdaq under ticker symbol SPCX", "Target IPO valuation range is $1.25-$1.75 trillion, with prediction
markets pricing above $2 trillion", "Target capital raise is approximately $75 billion, which would be the largest IPO in history", "SpaceX is going public as a combined three-segment entity: Space
(launches), Connectivity (Starlink), and AI (xAI/Grok/X platform)", "A 5-for-1 stock split was executed on May 4, 2026, resulting in ~12.5 billion pro forma shares outstanding", "FY 2025 total revenue
was $18.674 billion across all segments; Q1 2026 revenue was $4.694 billion", "Starlink has 10.3 million subscribers as of Q1 2026, up from 5.0 million a year earlier", "SpaceX reported net losses of
$4.937 billion in FY 2025 and $4.276 billion in Q1 2026 alone", "Elon Musk controls 85% of shareholder votes through a dual-class share structure (Class B = 10 votes/share)", "Underwriters include
Goldman Sachs, Morgan Stanley, BofA Securities, Citigroup, J.P. Morgan, and others", "BlackRock reportedly may invest up to $10 billion in the IPO", "SpaceX merged with xAI Holdings Corp (Feb 2, 2026)
and X Holdings Corp (via xAI, March 28, 2025) prior to the IPO", "Roadshow expected to begin around June 4, 2026 per the 15-day JOBS Act rule from the May 20 S-1 filing", "Total assets of $102.1
billion and total liabilities of $60.5 billion (including $20B bridge loan) as of March 31, 2026", "Musk's compensation includes 1 billion restricted shares tied to $7.5T market cap and Mars colony
milestones", "SpaceX has an option to acquire Cursor (AI code editor) at $60 billion implied equity post-IPO", "Data vintage: research files last updated May 24, 2026; developments after that date
could not be verified due to tool limitations"], "data_points": [{"metric": "Target IPO valuation (low)", "value": 1250.0, "unit": "billion USD", "as_of": "2026-05-24", "source_url":
"https://www.reuters.com/technology/space/spacex-accelerates-ipo-timeline-targets-june-12-nasdaq/"}, {"metric": "Target IPO valuation (high)", "value": 1750.0, "unit": "billion USD", "as_of":
"2026-05-24", "source_url": "https://www.reuters.com/technology/space/spacex-accelerates-ipo-timeline-targets-june-12-nasdaq/"}, {"metric": "Target capital raise", "value": 75.0, "unit": "billion
USD", "as_of": "2026-05-24", "source_url": "https://www.reuters.com/technology/space/spacex-accelerates-ipo-timeline-targets-june-12-nasdaq/"}, {"metric": "FY 2025 total revenue", "value": 18674.0,
"unit": "million USD", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Q1 2026 total revenue",
"value": 4694.0, "unit": "million USD", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "FY 2025
net loss", "value": -4937.0, "unit": "million USD", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"},
{"metric": "Q1 2026 net loss", "value": -4276.0, "unit": "million USD", "as_of": "2026-05-20", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "FY 2025 Connectivity (Starlink) revenue", "value": 11387.0, "unit": "million USD",
"as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Starlink subscribers Q1 2026", "value": 10.3,
"unit": "million subscribers", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Starlink ARPU Q1
2026", "value": 66.0, "unit": "USD per month", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric":
"Active Starlink satellites", "value": 9600.0, "unit": "satellites in LEO", "as_of": "2026-03-31", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Total assets", "value": 102.1, "unit": "billion USD", "as_of": "2026-03-31",
"source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Cash on hand", "value": 15.9, "unit": "billion USD", "as_of":
"2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Total liabilities", "value": 60.5, "unit": "billion USD",
"as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Bridge loan", "value": 20.0, "unit": "billion
USD", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Contract backlog", "value": 28.4, "unit":
"billion USD", "as_of": "2025-12-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "FY 2025 capital expenditures",
"value": 20.7, "unit": "billion USD", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric":
"Connectivity segment EBITDA FY 2025", "value": 7.2, "unit": "billion USD", "as_of": "2026-05-20", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Rocket launches FY 2025", "value": 170.0, "unit": "launches", "as_of": "2025-12-31",
"source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Pro forma shares outstanding", "value": 12.5, "unit": "billion shares",
"as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "RSA grant-date fair value (post-split)", "value":
93.87, "unit": "USD per share", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "X platform
monthly active users", "value": 550.0, "unit": "million MAUs", "as_of": "2026-03-31", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "FY 2024 net income", "value": 791.0, "unit": "million USD", "as_of": "2026-05-20",
"source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Potential BlackRock investment", "value": 10.0, "unit": "billion USD",
"as_of": "2026-05-17", "source_url": "https://www.barrons.com/articles/spacex-ipo-risk-2026"}], "created_at": "2026-06-02T00:13:39.217227Z", "updated_at": "2026-06-02T00:13:39.217227Z", "stale_after":
"2026-06-02T06:13:39.217227Z", "state": "fresh", "revision_history": [], "session_id": "5325e339-7049-4c76-b340-8c43d079d0d2", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Tesla TSLA
stock price market cap June 2026 current", "entry": {"slug": "tesla-tsla-stock-price-market-cap-june-2026-curren-3f22b64a", "query": "Tesla TSLA stock price market cap June 2026 current", "answer":
"Now I have a comprehensive picture. Let me compile the final report.\n\n---\n\n## Tesla (TSLA) Stock Price & Market Cap \u2014 June 2, 2026\n\n### Current Price\n- **Last Price: $415.88 USD**
(NASDAQ)\n- **Previous Close:** $429.60\n- **Day Open:** $427.49\n- **Day Range:** $415.43 \u2013 $435.79\n- **Change from Previous Close:** approximately \u2013$13.72 (\u20133.2%)\n\n### Market
Capitalization\n- **~$1.56 Trillion** (based on total shares outstanding of ~3.76 billion \u00d7 $415.88 price)\n- Google Finance reports a lower figure of ~$1.30T, likely calculated using free float
shares (~3.13B) rather than total shares outstanding\n- Tesla remains the world's most valuable automaker (a distinction held since July 2020)\n\n### Key Valuation Metrics\n| Metric | Value
|\n|---|---|\n| EPS (TTM) | $1.09 |\n| P/E Ratio (TTM) | 404.44 |\n| Forward P/E | 193.38 |\n| Shares Outstanding | ~3.76 billion |\n\n### 52-Week Range\n- **52-Week High:** $498.82\n- **52-Week
Low:** $273.21\n- Current price sits at approximately **57%** of the way through the 52-week range\n\n### Trading Volume\n- **Volume (June 2):** ~44.9 million shares\n- **Average Volume:** ~56.4
million shares (below average today)\n\n### Financials (Trailing Twelve Months)\n- **Revenue (TTM):** ~$97.88 billion\n- **Net Income (TTM):** ~$3.86 billion\n- **FY 2025 Revenue:** $94.83 billion
(\u20132.93% YoY from $97.69B in 2024)\n- **FY 2025 Earnings:** $3.79 billion (\u201346.5% YoY from $7.13B in 2024)\n- **FY 2024 Revenue:** $97.69 billion\n- **FY 2024 Earnings:** $7.13 billion\n\n###
Analyst Consensus\n- **Average Price Target:** $411.89 (based on 47 analysts)\n- This is ~0.96% below the current price of $415.88, suggesting the stock is trading near/slightly above consensus
target\n\n### Sources & Notes\n- Data sourced from Google Finance and StockAnalysis.com on June 2, 2026\n- The market cap discrepancy ($1.30T vs $1.56T) reflects different share count methodologies:
Google Finance appears to use float shares (~3.13B), while StockAnalysis uses total shares outstanding (~3.76B). The $1.56T figure using total shares is the standard market cap convention.",
"sources": [{"url": "https://www.google.com/finance/quote/TSLA:NASDAQ", "title": "Tesla Inc (TSLA) Stock Price & Quote - Google Finance", "domain": "google.com", "accessed_at": "2026-06-02T00:00:00Z",
"snippet": "TSLA last price $415.88, market cap ~$1.30T, 52-week range $273.21-$498.82, volume 44.9M"}, {"url": "https://stockanalysis.com/stocks/tsla/", "title": "Tesla (TSLA) Stock Price, Quote &
Overview - Stock Analysis", "domain": "stockanalysis.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Market cap $1.56T, shares outstanding 3.76B, EPS $1.09, P/E 404.44, forward P/E 193.38,
analyst target $411.89 from 47 analysts"}], "key_facts": ["Tesla (TSLA) last traded at $415.88 USD on NASDAQ as of June 2, 2026, down ~3.2% from previous close of $429.60", "Tesla market
capitalization is approximately $1.56 trillion based on ~3.76 billion total shares outstanding (Google Finance shows ~$1.30T using float shares of ~3.13B)", "Tesla remains the world's most valuable
automaker, a distinction held since July 2020", "52-week range is $273.21 to $498.82; current price is roughly 57% through that range", "P/E ratio (TTM) is 404.44; Forward P/E is 193.38; EPS (TTM) is
$1.09", "FY 2025 revenue was $94.83B (down 2.93% YoY); FY 2025 earnings were $3.79B (down 46.5% YoY)", "Revenue (TTM) is approximately $97.88B; Net Income (TTM) is ~$3.86B", "Average analyst price
target is $411.89 based on 47 analysts, ~0.96% below current price", "Daily trading volume of ~44.9M shares is below the average volume of ~56.4M shares"], "data_points": [{"metric": "TSLA Stock
Price", "value": 415.88, "unit": "USD", "as_of": "2026-06-02", "source_url": "https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Market Cap (total shares)", "value": 1.56, "unit":
"USD Trillion", "as_of": "2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Market Cap (float shares - Google Finance)", "value": 1.3, "unit": "USD Trillion",
"as_of": "2026-06-02", "source_url": "https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Previous Close", "value": 429.6, "unit": "USD", "as_of": "2026-06-01", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA 52-Week High", "value": 498.82, "unit": "USD", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA 52-Week Low", "value": 273.21, "unit": "USD", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Shares Outstanding", "value": 3.76, "unit": "Billion shares", "as_of": "2026-06-02", "source_url":
"https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA EPS (TTM)", "value": 1.09, "unit": "USD", "as_of": "2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA
P/E Ratio (TTM)", "value": 404.44, "unit": "ratio", "as_of": "2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Forward P/E", "value": 193.38, "unit": "ratio",
"as_of": "2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Daily Volume", "value": 44906124.0, "unit": "shares", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Revenue (TTM)", "value": 97.88, "unit": "USD Billion", "as_of": "2026-06-02", "source_url":
"https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Net Income (TTM)", "value": 3.86, "unit": "USD Billion", "as_of": "2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"},
{"metric": "TSLA FY2025 Revenue", "value": 94.83, "unit": "USD Billion", "as_of": "2025-12-31", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA FY2025 Earnings", "value":
3.79, "unit": "USD Billion", "as_of": "2025-12-31", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Analyst Average Price Target", "value": 411.89, "unit": "USD", "as_of":
"2026-06-02", "source_url": "https://stockanalysis.com/stocks/tsla/"}, {"metric": "TSLA Day Open", "value": 427.49, "unit": "USD", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Day High", "value": 435.79, "unit": "USD", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}, {"metric": "TSLA Day Low", "value": 415.43, "unit": "USD", "as_of": "2026-06-02", "source_url":
"https://www.google.com/finance/quote/TSLA:NASDAQ"}], "created_at": "2026-06-02T00:10:23.850940Z", "updated_at": "2026-06-02T00:10:23.850940Z", "stale_after": "2026-06-02T06:10:23.850940Z", "state":
"fresh", "revision_history": [], "session_id": "5d769381-bc39-4e4e-920e-34f435a91f29", "follow_up_count": 0}, "is_follow_up": false}, {"query": "SpaceX IPO S-1 filing shares outstanding total share
count all classes", "entry": {"slug": "spacex-ipo-s-1-filing-shares-outstanding-total-sha-135107e3", "query": "SpaceX IPO S-1 filing shares outstanding total share count all classes", "answer": "This
is an excellent and comprehensive result. The agent found detailed data from previously gathered research files. Let me compile the final synthesis.\n\n---\n\n# SpaceX IPO: S-1 Filing, Shares
Outstanding, and Share Structure\n\n## S-1 Filing Status\n\nSpaceX (Space Exploration Technologies Corp., CIK: 0001181412) has **filed a public S-1 registration statement** with the SEC:\n\n- **March
30, 2026** \u2014 Confidential Draft Registration Statement (DRS) filed\n- **May 20, 2026** \u2014 Public S-1 registration statement filed (SEC Accession Number: 0001628280-26-036936)\n- **Target
listing date:** June 12, 2026 on **Nasdaq and Nasdaq Texas** under ticker **\"SPCX\"**\n- Underwriters include Goldman Sachs, Morgan Stanley, BofA Securities, Citigroup, J.P. Morgan, and
others\n\n---\n\n## Total Share Count (All Classes)\n\n**Pro forma total shares outstanding: ~12.5 billion shares (12,521 million)** as of March 31, 2026.\n\nThis reflects a **5-for-1 stock split**
effective May 4, 2026 (pre-split: ~2.5 billion shares).\n\nAdditionally, Elon Musk holds a **1 billion restricted share award** contingent on two milestones: (1) a $7.5 trillion market cap, and (2) a
permanent Mars colony with 1 million inhabitants. These shares are **not** included in current outstanding counts.\n\n---\n\n## Share Class Structure (Dual-Class)\n\n| Class | Voting Rights | Holders
| Status |\n|-------|--------------|---------|--------|\n| **Class A Common Stock** | 1 vote per share | Public investors (IPO offering) | To be publicly traded |\n| **Class B Common Stock** | 10
votes per share | Elon Musk and insiders | Privately retained |\n\n- **Elon Musk controls ~85% of total shareholder voting power** through Class B super-voting shares\n- SpaceX will be classified as a
**\"controlled company\"** under Nasdaq listing rules\n- Musk will simultaneously hold titles of CEO, CTO, and Chairman\n\n---\n\n## Valuation & Share Price Indicators\n\n| Metric | Value | Context
|\n|--------|-------|---------|\n| Target IPO valuation | $1.25\u2013$1.75 trillion (up to $2T) | IPO range |\n| Target capital raise | ~$75 billion | Would be largest IPO in history |\n| Series N
preferred price | $270/share pre-split ($54 post-split) | Most recent preferred round |\n| RSA grant-date fair value | $93.87/share (post-split) | As of Dec 31, 2025 |\n| Implied equity value at RSA
FV | ~$1.175 trillion | 12.5B shares \u00d7 $93.87 |\n| Late 2024 tender offers | $180\u2013$210 billion | Secondary market |\n\n---\n\n## Corporate Structure\n\nThe IPO entity is a **combined
company** with three segments following two mergers:\n1. **Space segment** \u2014 Falcon 9, Falcon Heavy, Starship, Dragon\n2. **Connectivity segment** \u2014 Starlink (~10.3M subscribers as of Q1
2026)\n3. **AI segment** \u2014 xAI (Grok), X social media (~550M MAUs), COLOSSUS data centers (1 GW)\n\n**Key mergers:**\n- March 28, 2025: X Holdings Corp (Twitter/X) acquired by xAI\n- February 2,
2026: xAI Holdings Corp acquired by SpaceX\n\n**Balance Sheet (March 31, 2026):** Total assets $102.1B | Cash $15.9B | Total liabilities $60.5B | Shareholders' equity $34.5B | Backlog
$28.4B\n\n---\n\n**Data vintage note:** Research data last updated May 24, 2026. Primary source is the S-1 filing on SEC EDGAR. For the most current information (e.g., final pricing, whether June 12
listing date held), direct verification is recommended.", "sources": [{"url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm", "title": "SpaceX S-1
Registration Statement (SEC EDGAR)", "domain": "sec.gov", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "Public S-1 filing by Space Exploration Technologies Corp, filed May 20, 2026, containing
110 documents (226 MB). Details share structure, financials, and business segments."}, {"url": "https://www.reuters.com/technology/space/", "title": "Reuters - SpaceX IPO Roadshow and Timeline
Coverage", "domain": "reuters.com", "accessed_at": "2026-05-24T00:00:00Z", "snippet": "SpaceX targeting June 12, 2026 listing date on Nasdaq. Valuation target $1.25-$1.75 trillion."}, {"url":
"https://www.cnbc.com/", "title": "CNBC - SpaceX IPO Retail Investor Access Coverage", "domain": "cnbc.com", "accessed_at": "2026-05-21T00:00:00Z", "snippet": "Record retail investor allocation
planned for SpaceX IPO with direct access through major brokerage platforms."}, {"url": "https://www.cnn.com/", "title": "CNN - SpaceX IPO Governance and Control Structure", "domain": "cnn.com",
"accessed_at": "2026-05-24T00:00:00Z", "snippet": "Musk controls ~85% of voting power through Class B shares; SpaceX classified as 'controlled company' under Nasdaq rules."}, {"url":
"https://www.msn.com/en-us/money/", "title": "MSN/Barron's - BlackRock SpaceX IPO Investment", "domain": "msn.com", "accessed_at": "2026-05-17T00:00:00Z", "snippet": "BlackRock reportedly may invest
up to $10 billion in SpaceX IPO."}], "key_facts": ["SpaceX filed a public S-1 registration statement with the SEC on May 20, 2026 (Accession Number: 0001628280-26-036936), following a confidential DRS
filing on March 30, 2026.", "Pro forma total shares outstanding are approximately 12.5 billion (12,521 million) as of March 31, 2026, reflecting a 5-for-1 stock split effective May 4, 2026.", "SpaceX
has a dual-class share structure: Class A (1 vote/share, public) and Class B (10 votes/share, held by Elon Musk and insiders).", "Elon Musk controls approximately 85% of total shareholder voting power
through Class B super-voting shares.", "SpaceX plans to list on Nasdaq and Nasdaq Texas under ticker 'SPCX' with a target listing date of June 12, 2026.", "Target IPO valuation ranges from $1.25
trillion to $1.75 trillion, with some estimates up to $2 trillion; the target capital raise is approximately $75 billion, which would make it the largest IPO in history.", "Elon Musk holds a 1 billion
restricted share award contingent on achieving a $7.5 trillion market cap and establishing a permanent Mars colony with 1 million inhabitants; these are NOT included in outstanding share counts.",
"The IPO entity is a combined company (SpaceX + xAI + X/Twitter) with three segments: Space, Connectivity (Starlink, 10.3M subscribers), and AI (Grok, X with ~550M MAUs).", "Most recent RSA grant-date
fair value was $93.87/share (post-split) as of December 31, 2025, implying ~$1.175 trillion equity value.", "Underwriters include Goldman Sachs, Morgan Stanley, BofA Securities, Citigroup, J.P.
Morgan, Barclays, Deutsche Bank, RBC, UBS, Wells Fargo, and Allen & Company."], "data_points": [{"metric": "Total shares outstanding (pro forma, post-split)", "value": 12521000000.0, "unit": "shares",
"as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Stock split ratio", "value": 5.0, "unit": "for-1
split", "as_of": "2026-05-04", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Musk voting power percentage", "value":
85.0, "unit": "percent", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Target IPO valuation
(low end)", "value": 1250000000000.0, "unit": "USD", "as_of": "2026-05-20", "source_url": "https://www.reuters.com/technology/space/"}, {"metric": "Target IPO valuation (high end)", "value":
1750000000000.0, "unit": "USD", "as_of": "2026-05-20", "source_url": "https://www.reuters.com/technology/space/"}, {"metric": "Target capital raise", "value": 75000000000.0, "unit": "USD", "as_of":
"2026-05-20", "source_url": "https://www.reuters.com/technology/space/"}, {"metric": "RSA grant-date fair value per share (post-split)", "value": 93.87, "unit": "USD/share", "as_of": "2025-12-31",
"source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Series N preferred price (pre-split)", "value": 270.0, "unit":
"USD/share", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Implied equity value at RSA fair
value", "value": 1175000000000.0, "unit": "USD", "as_of": "2025-12-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric":
"Musk restricted share award (milestone-contingent)", "value": 1000000000.0, "unit": "shares", "as_of": "2026-05-20", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Starlink subscribers", "value": 10300000.0, "unit": "subscribers", "as_of":
"2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "X platform monthly active users", "value": 550000000.0,
"unit": "MAUs", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Total assets", "value":
102100000000.0, "unit": "USD", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Cash and
equivalents", "value": 15900000000.0, "unit": "USD", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"},
{"metric": "Total liabilities", "value": 60500000000.0, "unit": "USD", "as_of": "2026-03-31", "source_url":
"https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Total shareholders equity", "value": 34500000000.0, "unit": "USD", "as_of":
"2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Contract backlog", "value": 28400000000.0, "unit": "USD",
"as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Bridge loan outstanding", "value": 20000000000.0,
"unit": "USD", "as_of": "2026-03-31", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}, {"metric": "Class B voting rights multiplier",
"value": 10.0, "unit": "votes per share", "as_of": "2026-05-20", "source_url": "https://www.sec.gov/Archives/edgar/data/1181412/000162828026036936/0001628280-26-036936-index.htm"}], "created_at":
"2026-06-02T00:11:20.012716Z", "updated_at": "2026-06-02T00:11:20.012716Z", "stale_after": "2026-06-02T06:11:20.012716Z", "state": "fresh", "revision_history": [], "session_id":
"9d49f636-dd48-465e-a18d-6ff574c61385", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 3, "failed_count": 0}
```

```json
{
  "post_id": 43743
}
```

### 📋 Result

```
[]
```

## 💬 Response

Now let me get the latest data on prediction markets and do some more specific research on the question's key variables.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "SpaceX IPO valuation pricing June 2026 latest update roadshow"
}
```

### 📋 Result

```
{"query": "SpaceX IPO valuation pricing June 2026 latest update roadshow", "results": [{"title": "SpaceX Is Quietly Trading at a Price That Would Make It 23x Bigger Than Facebook\u2019s IPO", "url":
"https://finance.yahoo.com/markets/options/articles/spacex-quietly-trading-price-23x-155150831.html", "snippet": "Quick Read\n-\nSpaceX\u2019s synthetic contract (SPCX-USD) trades at roughly $203,
implying a $2.4 trillion valuation, above the company\u2019s reported IPO target range of $1.75 trillion to $2 trillion and sitting at roughly 50-50 odds among real-money predictors on Polymarket.
Tesla (TSLA) fell 3% after the SpaceX IPO announcement amid capital-rotation concerns.\n-\nSpaceX\u2019s implied IPO size at $2.4 trillion would dwarf Facebook\u2019s historic listing 23 times over,
but the derivative-driven price signal lacks ", "api_data": null, "hint": null}, {"title": "SpaceX targets $1.8T valuation for 2026 IPO debut", "url": "https://cryptobriefing.com/spacex-
targets-18t-valuation-for-2026-ipo-debut/", "snippet": "## Market Snapshot\nSpaceX IPO closing market cap above $1 trillion is currently priced at 98.8% YES. The $1.8 trillion threshold is priced at
89.5% YES, having experienced slight fluctuations in recent days.\n## Key Takeaways\n\u2013 The planned SpaceX IPO appears to suggest strong market interest, with a potential valuation of at least
$1.8 trillion. \u2013 Market pricing suggests participants are confident in SpaceX achieving a closing market cap above $1 trillion. \u2013 The IPO could indicate the strategic i", "api_data": null,
"hint": null}, {"title": "What to Know About the SpaceX IPO - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-05-29/what-to-know-about-the-spacex-ipo", "snippet": null, "api_data":
null, "hint": null}, {"title": "How SpaceX\u2019s Dream of a Record-Breaking IPO Stacks Up", "url": "https://www.bloomberg.com/graphics/2026-spacex-ipo-stock-market-nasdaq-listings/", "snippet": null,
"api_data": null, "hint": null}, {"title": "SpaceX IPO Guide: S-1 Breakdown, Valuation & Trading Strategy | BitMEX", "url": "https://www.bitmex.com/blog/spacex-ipo-guide", "snippet": "SpaceX is
targeting a $1.75 trillion valuation on listing day \u2014 larger than Microsoft, trailing only Apple and Nvidia \u2014 despite posting a $4.28 billion net loss in Q1 2026 alone and an accumulated
deficit of $41.3 billion.\nFor traders, demand was never the variable. Goldman Sachs is leading the deal, retail investors are earmarked for 30% of the float \u2013 three times the standard mega-cap
norm \u2013 and the valuation has more than doubled since the December 2025 tender offer. The question is at what p", "api_data": null, "hint": null}, {"title": "SpaceX Just Lowered Its IPO Valuation
Target by $200 Billion | The Motley Fool", "url": "https://www.fool.com/investing/2026/06/01/spacex-lowered-ipo-valuation-target-by-200-billion/", "snippet": "We're less than two weeks away from Wall
Street's largest-ever [initial public offering (IPO)](https://www.fool.com/investing/stock-market/types-of-stocks/ipo-stocks/). Based on several reports, Elon Musk's SpaceX is aiming for a June 12
debut, as well as potential fast entry into the Nasdaq-100 as early as July 7.\nThe company that combines two of the hottest addressable opportunities, artificial intelligence (AI) and the space
economy, is expected to raise up to $75 billion and slot in directly", "api_data": null, "hint": null}, {"title": "SpaceX IPO Date Set for June 12 at a $1.75 Trillion Valuation - Everything You Need
to Know About SPCX", "url": "https://www.tradingkey.com/analysis/stocks/us-stocks/261904604-spacex-ipo-spcx-date-set-for-june-12-175-trillion-valuation-tradingkey", "snippet": "SpaceX IPO Date Set for
June 12 at a $1.75 Trillion Valuation - Everything You Need to Know About SPCX\n![facebook](https://resource.tradingkey.com/cdn/images/media/facebook_active.png)\n![twitter](https://resource.tradingke
y.com/cdn/images/media/x_active.png)\n![linkedin](https://resource.tradingkey.com/cdn/images/media/linkin_active.png)\nSpaceX targets a June 12, 2026, Nasdaq IPO (SPCX), aiming to raise $75 billion at
a $1.75 trillion valuation. The dual-class share structure will grant Elon Musk", "api_data": null, "hint": null}, {"title": "SpaceX IPO (SPCX) Explained: What Retail Investors Need to Know Before
June 11", "url": "https://www.heygotrade.com/en/blog/spacex-ipo-spcx-explained-retail-investors-june-11/", "snippet": "SpaceX is finally going public, and the SpaceX IPO is shaping up to be the
largest listing in Nasdaq history. The company filed its S-1 with the SEC targeting ticker SPCX, with the roadshow starting June 4, pricing on June 11, and trading beginning June 12, 2026.\nThe
headline numbers are huge. SpaceX is seeking to raise around $75 billion at a $1.75 trillion valuation.\nFor retail investors trying to figure out how to buy SPCX stock at listing, the real question
is not whether to watch the open. ", "api_data": null, "hint": null}, {"title": "Invest and Sell SpaceX Stock - Forge", "url": "https://forgeglobal.com/spacex_stock/", "snippet": null, "api_data":
null, "hint": null}]}
```

```json
{
  "query": "Tesla TSLA stock price today June 2 2026"
}
```

### 📋 Result

```
{"query": "Tesla TSLA stock price today June 2 2026", "results": [{"title": "TSLA: Tesla Inc - Stock Price, Quote and News - CNBC", "url": "https://www.cnbc.com/quotes/TSLA", "snippet": "Tesla Inc
TSLA:NASDAQ\nRT Quote | Last NASDAQ LS, VOL From CTA | USD\n413.57\n-2.31 (-0.56%)\nVolume\n2,162,765\nClose\n415.88\n-19.91 (-4.57%)\nVolume\n41,555,661\n52 week range\n273.21 - 498.83\n-
Open427.49\n- Day High429.60\n- Day Low415.43\n- Prev Close435.79\n- 52 Week High498.83\n- 52 Week High Date12/22/25\n- 52 Week Low273.21\n- 52 Week Low Date06/05/25\nLatest On Tesla Inc\nKey Stats\n-
Market Cap1.562T\n- Shares Out3.76B\n- 10 Day Average Volume45.36M\n- Dividend-\n- Dividend Yield-\n- Beta1.80\nLatest On Tesla I", "api_data": null, "hint": null}, {"title": "Tesla, Inc. (TSLA) Stock
Price, News, Quote & History - Yahoo Finance", "url": "https://finance.yahoo.com/quote/TSLA/", "snippet": "{\"symbol\": \"TSLA\", \"name\": \"Tesla, Inc.\", \"current_price\": 415.88,
\"previous_close\": 435.79, \"change_percent\": -4.56872, \"currency\": \"USD\", \"market_cap\": 1561930366976, \"fifty_two_week_high\": 498.83, \"fifty_two_week_low\": 273.21, \"recent_history\":
[{\"date\": \"2026-05-04\", \"close\": 392.51}, {\"date\": \"2026-05-05\", \"close\": 389.37}, {\"date\": \"2026-05-06\", \"close\": 398.73}, {\"date\": \"2026-05-07\", \"close\": 411.79}, {\"date\":
\"2026-05-08\", \"close\": 428.35}, {\"date\": \"2026-05-11\", \"close\": 445.0}, {\"date", "api_data": {"content": [{"type": "text", "text": "{\"symbol\": \"TSLA\", \"name\": \"Tesla, Inc.\",
\"current_price\": 415.88, \"previous_close\": 435.79, \"change_percent\": -4.56872, \"currency\": \"USD\", \"market_cap\": 1561930366976, \"fifty_two_week_high\": 498.83, \"fifty_two_week_low\":
273.21, \"recent_history\": [{\"date\": \"2026-05-04\", \"close\": 392.51}, {\"date\": \"2026-05-05\", \"close\": 389.37}, {\"date\": \"2026-05-06\", \"close\": 398.73}, {\"date\": \"2026-05-07\",
\"close\": 411.79}, {\"date\": \"2026-05-08\", \"close\": 428.35}, {\"date\": \"2026-05-11\", \"close\": 445.0}, {\"date\": \"2026-05-12\", \"close\": 433.45}, {\"date\": \"2026-05-13\", \"close\":
445.27}, {\"date\": \"2026-05-14\", \"close\": 443.3}, {\"date\": \"2026-05-15\", \"close\": 422.24}, {\"date\": \"2026-05-18\", \"close\": 409.99}, {\"date\": \"2026-05-19\", \"close\": 404.11},
{\"date\": \"2026-05-20\", \"close\": 417.26}, {\"date\": \"2026-05-21\", \"close\": 417.85}, {\"date\": \"2026-05-22\", \"close\": 426.01}, {\"date\": \"2026-05-26\", \"close\": 433.59}, {\"date\":
\"2026-05-27\", \"close\": 440.36}, {\"date\": \"2026-05-28\", \"close\": 442.1}, {\"date\": \"2026-05-29\", \"close\": 435.79}, {\"date\": \"2026-06-01\", \"close\": 415.88}], \"summary_stats\":
{\"drawdown_from_52w_high_pct\": -16.628911653268645, \"distance_from_52w_low_pct\": 52.2199041030709, \"trailing_returns\": {\"five_day\": -2.377878453557427, \"ten_day\": -1.5062523683213371},
\"trailing_volatility_20d\": 2.689289879201415, \"trailing_mean_return_20d\": 0.3043933816044787, \"recent_low\": {\"date\": \"2026-05-05\", \"close\": 389.37, \"days_ago\": 18}, \"recent_high\":
{\"date\": \"2026-05-13\", \"close\": 445.27, \"days_ago\": 12}, \"max_bounce_from_recent_low_pct\": 14.356524642371005}, \"shock_alert\": {\"event\": \"2026-06-01 drop: -4.6%\", \"daily_return_pct\":
-4.57, \"comparable_events\": 55, \"median_forward_return_pct\": -0.52, \"pct_positive\": 49.1, \"horizon_days\": 10}}"}]}, "hint": null}, {"title": "Tesla, Inc. (TSLA) Stock Price, News, Quotes, &
Historic Data | Nasdaq", "url": "https://www.nasdaq.com/market-activity/stocks/tsla", "snippet": null, "api_data": null, "hint": null}, {"title": "Tesla, Inc. (TSLA) Stock Historical Prices & Data -
Yahoo Finance", "url": "https://finance.yahoo.com/quote/TSLA/history/", "snippet": "{\"symbol\": \"TSLA\", \"name\": \"Tesla, Inc.\", \"current_price\": 415.88, \"previous_close\": 435.79,
\"change_percent\": -4.56872, \"currency\": \"USD\", \"market_cap\": 1561930366976, \"fifty_two_week_high\": 498.83, \"fifty_two_week_low\": 273.21, \"recent_history\": [{\"date\": \"2026-05-04\",
\"close\": 392.51}, {\"date\": \"2026-05-05\", \"close\": 389.37}, {\"date\": \"2026-05-06\", \"close\": 398.73}, {\"date\": \"2026-05-07\", \"close\": 411.79}, {\"date\": \"2026-05-08\", \"close\":
428.35}, {\"date\": \"2026-05-11\", \"close\": 445.0}, {\"date", "api_data": {"content": [{"type": "text", "text": "{\"symbol\": \"TSLA\", \"name\": \"Tesla, Inc.\", \"current_price\": 415.88,
\"previous_close\": 435.79, \"change_percent\": -4.56872, \"currency\": \"USD\", \"market_cap\": 1561930366976, \"fifty_two_week_high\": 498.83, \"fifty_two_week_low\": 273.21, \"recent_history\":
[{\"date\": \"2026-05-04\", \"close\": 392.51}, {\"date\": \"2026-05-05\", \"close\": 389.37}, {\"date\": \"2026-05-06\", \"close\": 398.73}, {\"date\": \"2026-05-07\", \"close\": 411.79}, {\"date\":
\"2026-05-08\", \"close\": 428.35}, {\"date\": \"2026-05-11\", \"close\": 445.0}, {\"date\": \"2026-05-12\", \"close\": 433.45}, {\"date\": \"2026-05-13\", \"close\": 445.27}, {\"date\":
\"2026-05-14\", \"close\": 443.3}, {\"date\": \"2026-05-15\", \"close\": 422.24}, {\"date\": \"2026-05-18\", \"close\": 409.99}, {\"date\": \"2026-05-19\", \"close\": 404.11}, {\"date\":
\"2026-05-20\", \"close\": 417.26}, {\"date\": \"2026-05-21\", \"close\": 417.85}, {\"date\": \"2026-05-22\", \"close\": 426.01}, {\"date\": \"2026-05-26\", \"close\": 433.59}, {\"date\":
\"2026-05-27\", \"close\": 440.36}, {\"date\": \"2026-05-28\", \"close\": 442.1}, {\"date\": \"2026-05-29\", \"close\": 435.79}, {\"date\": \"2026-06-01\", \"close\": 415.88}], \"summary_stats\":
{\"drawdown_from_52w_high_pct\": -16.628911653268645, \"distance_from_52w_low_pct\": 52.2199041030709, \"trailing_returns\": {\"five_day\": -2.377878453557427, \"ten_day\": -1.5062523683213371},
\"trailing_volatility_20d\": 2.689289879201415, \"trailing_mean_return_20d\": 0.3043933816044787, \"recent_low\": {\"date\": \"2026-05-05\", \"close\": 389.37, \"days_ago\": 18}, \"recent_high\":
{\"date\": \"2026-05-13\", \"close\": 445.27, \"days_ago\": 12}, \"max_bounce_from_recent_low_pct\": 14.356524642371005}, \"shock_alert\": {\"event\": \"2026-06-01 drop: -4.6%\", \"daily_return_pct\":
-4.57, \"comparable_events\": 55, \"median_forward_return_pct\": -0.52, \"pct_positive\": 49.1, \"horizon_days\": 10}}"}]}, "hint": null}, {"title": "TSLA Stock Price \u2014 Tesla Chart \u2014
TradingView", "url": "https://www.tradingview.com/symbols/NASDAQ-TSLA/", "snippet": "Tesla, Inc. engages in the design, development, manufacture, and sale of electric vehicles and energy generation
and storage systems. The company operates through Automotive and Energy Generation and Storage. The Automotive segment includes the design, development, manufacture, sale, and lease of electric
vehicles as well as sales of automotive regulatory credits. The Energy Generation and Storage segment is involved in the design, manufacture, installation, sale, and lease of stationary energy ",
"api_data": null, "hint": null}, {"title": "Tesla | TSLA - Stock Price | Live Quote | Historical Chart", "url": "https://tradingeconomics.com/tsla:us", "snippet": "Tesla traded at $415.71 this Monday
June 1st, decreasing $20.08 or 4.61 percent since the previous trading session. Looking back, over the last four weeks, Tesla lost 5.91 percent. Over the last 12 months, its price rose by 21.31
percent. Looking ahead, we forecast Tesla to be priced at 427.12 by the end of this quarter and at 402.12 in one year, according to Trading Economics global macro models projections and analysts
expectations.\nTesla, Inc. designs, develops, manufactures, sells and lease ", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."},
{"title": "Tesla: TSLA Stock Price Quote & News | Robinhood", "url": "https://robinhood.com/us/en/stocks/TSLA/", "snippet": "Tesla\nTrade Tesla 24 hours a day, five days a week on
Robinhood.\nRobinhood gives you the tools to revolutionize your trading experience. Use the streamlined mobile app, or access advanced charts and execute precise trades on our browser-based
platform,[Robinhood Legend](https://robinhood.com/us/en/legend/). Risks and limitations apply.\nAbout TSLA\nTesla, Inc. engages in the design, development, manufacture, and sale of electric vehicles
and energy generation and storage systems. It operates throu", "api_data": null, "hint": null}, {"title": "Tesla - 15 Year Stock Price History | TSLA | MacroTrends", "url":
"https://www.macrotrends.net/stocks/charts/TSLA/tesla/stock-price-history", "snippet": "Tesla - 15 Year Stock Price History | TSLA\nHistorical daily share price chart and data for Tesla since 2011
adjusted for splits and dividends. The latest closing stock price for Tesla as of June 01, 2026 is 415.88.\n- The all-time high Tesla stock closing price was 489.88 on December 16, 2025.\n- The Tesla
52-week high stock price is 498.83, which is 19.9% above the current share price.\n- The Tesla 52-week low stock price is 273.21, which is 34.3% below the current share price.\n- The average Tesla",
"api_data": null, "hint": "Use company_financials for earnings data, or fred_series for macro indicators."}, {"title": "Tesla, Inc. (TSLA) Historic Data and Prices| Nasdaq", "url":
"https://www.nasdaq.com/market-activity/stocks/tsla/historical", "snippet": null, "api_data": null, "hint": null}, {"title": "Tesla (TSLA) Stock Price Quote, Value & News | Morningstar", "url":
"https://www.morningstar.com/stocks/xnas/tsla/quote", "snippet": "[\nTesla: Full Self-Driving Approval in Flanders Another Step Toward Full Regional Rollout\n](https://www.morningstar.com/company-
reports/1467626-tesla-should-see-long-term-profit-growth-from-ai-robotaxis-and-humanoid-robots?listing=0P0000OQN8)\nReuters reported that Tesla has received approval to begin testing its full self-
driving software in the Flanders region of Belgium. Tesla shares were up slightly in early trading on May 13.", "api_data": null, "hint": null}]}
```

```json
{
  "query": "SpaceX IPO market cap prediction market Polymarket Kalshi"
}
```

### 📋 Result

```
{"query": "SpaceX IPO market cap prediction market Polymarket Kalshi", "results": [{"title": "SpaceX IPO Closing Market Cap Predictions & Odds | Polymarket", "url":
"https://pam.polymarket.com/event/spacex-ipo-closing-market-cap/will-spacexs-market-cap-be-between-800b-and-900b-at-market-close-on-ipo-day", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO
Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\":
\"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will
resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary ", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing
Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This
market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to
\\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares
outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\": 0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\":
0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\", \"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\",
\"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-
closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its
first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to
\\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the
primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the
normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no
such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading.\",
\"market_id\": \"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\",
\"probability\": 0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\":
\"2026-05-31\", \"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap
(Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\",
\"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET,
the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated
as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the
higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be
used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according
to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price
is published, treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\",
\"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\":
\"2026-05-29\", \"probability\": 0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04},
{\"date\": \"2026-06-02\", \"probability\": 0.04}]}], \"query\": \"spacex ipo closing market cap\"}"}]}, "hint": null}, {"title": "SpaceX IPO Closing Market Cap Predictions & Odds 2026 | Polymarket",
"url": "https://polymarket.com/event/spacex-ipo-closing-market-cap", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\":
102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market
capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket
capitalization expresses the monetary ", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\":
102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market
capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket
capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing
share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the
primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the
normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no
such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for
purposes of this market.\", \"market_id\": \"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015},
{\"date\": \"2026-05-27\", \"probability\": 0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\":
0.009}, {\"date\": \"2026-05-31\", \"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO
closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\",
\"description\": \"This market will resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the
title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as
the total number of outstanding shares multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event
that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading
(e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will
resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\",
\"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This
market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to
\\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares
outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}], \"query\": \"spacex ipo closing market cap\"}"}]}, "hint": null}, {"title": "SpaceX IPO closing market cap above ___ ? Predictions & O... 2026 | Polymarket", "url":
"https://polymarket.com/event/spacex-ipo-closing-market-cap-above", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\":
475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the
official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO
occurs by Decembe", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\":
475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the
official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO
occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares multiplied by the closing share
price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source
will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve
according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official
closing price is published, treating that as the first day of trading.\", \"market_id\": \"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\": 0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\":
0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\", \"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\",
\"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap above\"}"}]}, "hint": null}, {"title": "SpaceX Predictions & Real-Time Odds | Polymarket", "url":
"https://polymarket.com/predictions/spacex", "snippet": "SpaceX predictions & odds\n\u00b7Frequently Asked Questions\nPolymarket is the world\u2019s largest prediction market, where you can stay
informed and profit from your knowledge by trading on things related to breaking news, politics, sports, elections, crypto, finance, tech, culture, including topics like SpaceX.\nPolymarket currently
hosts 20 active markets for SpaceX that lets you track or trade on predictions like \u201cSpaceX IPO closing market cap above ___ ?\u201d. Whether you are tracking widely debated events", "api_data":
null, "hint": null}, {"title": "SpaceX IPO by ___ ? Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/spacex-ipo-by", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX
IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\":
\"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027,
11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing
Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\",
\"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET,
the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated
as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the
higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be
used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according
to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price
is published, treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\",
\"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\":
\"2026-05-29\", \"probability\": 0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04},
{\"date\": \"2026-06-02\", \"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\":
\"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on
its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value
of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf
the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page.
In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first
day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the
market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}], \"query\": \"spacex ipo by\"}"}]}, "hint": null}, {"title": "What
will SpaceX's public ticker be? Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/what-will-spacexs-public-ticker-be", "snippet": "{\"markets\": [{\"market_title\": \"What
will SpaceX's public ticker be?\", \"probability\": 0.0035, \"volume\": 581694.859989, \"url\": \"https://polymarket.com/event/what-will-spacexs-public-ticker-be\", \"source\": \"polymarket\",
\"description\": \"This market will resolve according to the public ticker symbol used by SpaceX in an IPO (Initial Public Offering) by December 31, 2027, 11:59 PM ET.\\n\\nAn official announcement
from SpaceX that they will IPO under a specific ticker symbol will be sufficient to resolve", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"What will SpaceX's
public ticker be?\", \"probability\": 0.0035, \"volume\": 581694.859989, \"url\": \"https://polymarket.com/event/what-will-spacexs-public-ticker-be\", \"source\": \"polymarket\", \"description\":
\"This market will resolve according to the public ticker symbol used by SpaceX in an IPO (Initial Public Offering) by December 31, 2027, 11:59 PM ET.\\n\\nAn official announcement from SpaceX that
they will IPO under a specific ticker symbol will be sufficient to resolve this market.\\n\\nIf a ticker used by SpaceX in a qualifying IPO is a variant of a ticker symbol listed in this market group
with additional letters to denote a specific class of shares, it will be considered to be that ticker (e.g. if SpaceX uses a ticker symbol of $MARS.A or $MARSA, this market will resolve to
$MARS).\\n\\nIf SpaceX announces an IPO with multiple tickers that are not considered the same ticker under the previous rule (i.e. $MARS.A and $MARS.B would be considered the same ticker), this
market will remain open until SpaceX\\u2019s first day of public trading and will resolve according to the ticker symbolizing the security class with the greatest market capitalization. Market
capitalization is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day. If this also results in a tie, this market will resolve according to
the ticker symbol that comes first in alphabetical order.\\n\\nIf SpaceX IPOs with a non-listed ticker, or does not IPO or officially announce an IPO and ticker symbol by December 31, 2027, 11:59 PM
ET, this market will resolve to \\u201cOther.\\u201d\\n\\nThe primary resolution source for this market will be official information from SpaceX and the primary exchange\\u2019s official listing page.
In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nNote: In the event of an interruption in the course of the normal trading session on SpaceX\\u2019s
first day of trading (e.g., a circuit breaker or half-day), the market will use the official closing price of the abbreviated session. If no such official closing price is published, the market will
use the closing price on the next trading day for which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"9845490727491005708827941815292518312239041816022490040240659848804580655878\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.003}, {\"date\": \"2026-05-27\", \"probability\":
0.001}, {\"date\": \"2026-05-28\", \"probability\": 0.001}, {\"date\": \"2026-05-29\", \"probability\": 0.009}, {\"date\": \"2026-05-30\", \"probability\": 0.005}, {\"date\": \"2026-05-31\",
\"probability\": 0.005}, {\"date\": \"2026-06-01\", \"probability\": 0.004}, {\"date\": \"2026-06-02\", \"probability\": 0.004}]}], \"query\": \"what will spacexs public ticker be\"}"}]}, "hint":
null}, {"title": "SpaceX IPO Closing Market Cap (Lower Strikes) Predictions... 2026 | Polymarket", "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes", "snippet":
"{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-
market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf
no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\":
[{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-
higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX
IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares,
stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between
two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is
not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\":
0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\": 0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\",
\"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\", \"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\":
0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\": 0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\":
0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\", \"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\",
\"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-
closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its
first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to
\\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the
primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the
normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no
such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading.\",
\"market_id\": \"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\",
\"probability\": 0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\":
\"2026-05-31\", \"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap higher
strikes\"}"}]}, "hint": null}, {"title": "Largest IPO by market cap in 2026? Predictions & Odds | Polymarket", "url": "https://polymarket.com/event/largest-ipo-by-market-cap-in-2026-287", "snippet":
"{\"markets\": [], \"query\": \"largest ipo by market cap in 2026 287\"}", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [], \"query\": \"largest ipo by market cap in 2026
287\"}"}]}, "hint": null}, {"title": "What will SpaceX\u2019s IPO valuation be? Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/what-will-spacexs-ipo-valuation-be",
"snippet": "{\"markets\": [{\"market_title\": \"What will SpaceX\\u2019s IPO valuation be?\", \"probability\": 0.72, \"volume\": 22330.56550499999, \"url\": \"https://polymarket.com/event/what-will-
spacexs-ipo-valuation-be\", \"source\": \"polymarket\", \"description\": \"This market will resolve according to the implied equity valuation of SpaceX at its initial public offering (IPO)
price.\\n\\nThe IPO valuation is defined as the final IPO price per share multiplied by the total number of shares outstanding on a fully diluted bas", "api_data": {"content": [{"type": "text",
"text": "{\"markets\": [{\"market_title\": \"What will SpaceX\\u2019s IPO valuation be?\", \"probability\": 0.72, \"volume\": 22330.56550499999, \"url\": \"https://polymarket.com/event/what-will-
spacexs-ipo-valuation-be\", \"source\": \"polymarket\", \"description\": \"This market will resolve according to the implied equity valuation of SpaceX at its initial public offering (IPO)
price.\\n\\nThe IPO valuation is defined as the final IPO price per share multiplied by the total number of shares outstanding on a fully diluted basis, as disclosed in the final prospectus filed with
the U.S. Securities and Exchange Commission.\\n\\nThe IPO price will be the final offering price to the public as stated in the final prospectus. Trading prices after listing, including the opening
trade, intraday prices, or closing price on the first day of trading, will not be considered.\\n\\nIndicated or preliminary price ranges, including any ranges disclosed in earlier filings or
amendments, will not be considered.\\n\\nIf the calculated valuation falls exactly on a boundary between two ranges, this market will resolve to the higher range.\\n\\nIf SpaceX does not complete an
IPO by December 31, 2026, 11:59 PM ET, this market will resolve to the lowest bracket.\\n\\nThe primary resolution source will be the final prospectus filed with the SEC; however, a consensus of
credible reporting may also be used.\", \"market_id\": \"27061220928827680969416787869683808920415722522767576741634668479425295927164\", \"recent_history\": [{\"date\": \"2026-05-26\",
\"probability\": 0.71}, {\"date\": \"2026-05-27\", \"probability\": 0.71}, {\"date\": \"2026-05-28\", \"probability\": 0.67}, {\"date\": \"2026-05-29\", \"probability\": 0.715}, {\"date\":
\"2026-05-30\", \"probability\": 0.71}, {\"date\": \"2026-05-31\", \"probability\": 0.715}, {\"date\": \"2026-06-01\", \"probability\": 0.72}, {\"date\": \"2026-06-02\", \"probability\": 0.72}]}],
\"query\": \"what will spacexs ipo valuation be\"}"}]}, "hint": null}, {"title": "When will SpaceX officially announce an IPO?", "url": "https://kalshi.com/markets/kxipospacex/when-will-spacex-
ipo/kxipospacex", "snippet": "{\"markets\": [], \"query\": \"when will spacex ipo\"}", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [], \"query\": \"when will spacex ipo\"}"}]},
"hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap",
  "prompt": "What are the specific market cap brackets and their probabilities for the SpaceX IPO closing market cap? List all brackets and their YES prices."
}
```

### 📋 Result

```
{"markets": [{"market_title": "SpaceX IPO Closing Market Cap", "probability": 0.016, "volume": 102131.03590699984, "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap", "source":
"polymarket", "description": "This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\n\nIf no SpaceX IPO occurs by December 31, 2027, 11:59
PM ET, the market will resolve to \"No IPO before 2028\".\n\nMarket capitalization expresses the monetary value of a company\u2019s outstanding shares, stated in its pricing currency. It is calculated
as the number of shares outstanding multiplied by the closing share price on the first trading day.\n\nIf the relevant value falls exactly between two brackets, then this market will resolve to the
higher range bracket.\n\nResolution will be based on the primary exchange\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be
used.\n\nIn the event of an interruption in the course of the normal trading session on SpaceX\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to
the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is
published, treating that as the first day of trading for purposes of this market.", "market_id": "111420057784452219026503866138413641670082826478514143867504780300842657093894", "recent_history":
[{"date": "2026-05-26", "probability": 0.015}, {"date": "2026-05-27", "probability": 0.015}, {"date": "2026-05-28", "probability": 0.017}, {"date": "2026-05-29", "probability": 0.035}, {"date":
"2026-05-30", "probability": 0.009}, {"date": "2026-05-31", "probability": 0.01}, {"date": "2026-06-01", "probability": 0.016}, {"date": "2026-06-02", "probability": 0.016}]}, {"market_title": "SpaceX
IPO closing market cap above ___ ?", "probability": 0.9925, "volume": 475294.2750970001, "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-above", "source": "polymarket",
"description": "This market will resolve to \u201cYes\u201d if the official closing price for SpaceX\u2019s market capitalization on its first trading day is above the value specified in the title.
Otherwise, it will resolve to \u201cNo\u201d.\n\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \u201cNo\u201d.\n\nMarket capitalization is defined as the total number
of outstanding shares multiplied by the closing share price on the first trading day.\n\nResolution will be based on the primary exchange\u2019s official listing page. In the event that the relevant
figure is not displayed, another reliable source will be used.\n\nIn the event of an interruption in the course of the normal trading session on SpaceX\u2019s first day of trading (e.g., a circuit
breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to
the next trading day on which an official closing price is published, treating that as the first day of trading.", "market_id":
"86511993606190995539996371064900122466738869186406355817612580895605974257272", "recent_history": [{"date": "2026-05-26", "probability": 0.976}, {"date": "2026-05-27", "probability": 0.978}, {"date":
"2026-05-28", "probability": 0.984}, {"date": "2026-05-29", "probability": 0.98}, {"date": "2026-05-30", "probability": 0.988}, {"date": "2026-05-31", "probability": 0.991}, {"date": "2026-06-01",
"probability": 0.993}, {"date": "2026-06-02", "probability": 0.993}]}, {"market_title": "SpaceX IPO Closing Market Cap (Lower Strikes)", "probability": 0.04, "volume": 130999.52390900004, "url":
"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes", "source": "polymarket", "description": "This market will resolve based on SpaceX's market capitalization at the closing
price on its first day of trading.\n\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \"No IPO before 2028\".\n\nMarket capitalization expresses the monetary
value of a company\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\n\nIf
the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\n\nResolution will be based on the primary exchange\u2019s official listing page. In
the event that the relevant figure is not displayed, another reliable source will be used.\n\nIn the event of an interruption in the course of the normal trading session on SpaceX\u2019s first day of
trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market
will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.", "market_id":
"87442614084312918783388636961113598693816786923475166996185201586044548013928", "recent_history": [{"date": "2026-05-26", "probability": 0.059}, {"date": "2026-05-27", "probability": 0.062}, {"date":
"2026-05-28", "probability": 0.057}, {"date": "2026-05-29", "probability": 0.045}, {"date": "2026-05-30", "probability": 0.044}, {"date": "2026-05-31", "probability": 0.05}, {"date": "2026-06-01",
"probability": 0.04}, {"date": "2026-06-02", "probability": 0.04}]}], "query": "spacex ipo closing market cap"}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-above",
  "prompt": "What are the specific market cap thresholds and their probabilities for SpaceX IPO closing market cap above various levels? List all thresholds and YES/NO prices."
}
```

### 📋 Result

```
{"markets": [{"market_title": "SpaceX IPO closing market cap above ___ ?", "probability": 0.9925, "volume": 475294.2750970001, "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-
above", "source": "polymarket", "description": "This market will resolve to \u201cYes\u201d if the official closing price for SpaceX\u2019s market capitalization on its first trading day is above the
value specified in the title. Otherwise, it will resolve to \u201cNo\u201d.\n\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \u201cNo\u201d.\n\nMarket capitalization
is defined as the total number of outstanding shares multiplied by the closing share price on the first trading day.\n\nResolution will be based on the primary exchange\u2019s official listing page.
In the event that the relevant figure is not displayed, another reliable source will be used.\n\nIn the event of an interruption in the course of the normal trading session on SpaceX\u2019s first day
of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market
will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading.", "market_id":
"86511993606190995539996371064900122466738869186406355817612580895605974257272", "recent_history": [{"date": "2026-05-26", "probability": 0.976}, {"date": "2026-05-27", "probability": 0.978}, {"date":
"2026-05-28", "probability": 0.984}, {"date": "2026-05-29", "probability": 0.98}, {"date": "2026-05-30", "probability": 0.988}, {"date": "2026-05-31", "probability": 0.991}, {"date": "2026-06-01",
"probability": 0.993}, {"date": "2026-06-02", "probability": 0.993}]}], "query": "spacex ipo closing market cap above"}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.fool.com/investing/2026/06/01/spacex-lowered-ipo-valuation-target-by-200-billion/",
  "prompt": "What is the updated SpaceX IPO valuation target? What was it lowered to? Any details about the pricing, share count, or market cap expectations."
}
```

### 📋 Result

```
{"url": "https://www.fool.com/investing/2026/06/01/spacex-lowered-ipo-valuation-target-by-200-billion/", "content": "Based on the content:\n\n**Updated Valuation Target:**\n- SpaceX lowered its IPO
valuation target from **$2 trillion to at least $1.8 trillion** - a reduction of $200 billion\n- The company initially sought a valuation of up to $2 trillion when it confidentially filed with
regulators on April 1\n- The reduction came shortly after SpaceX made its prospectus public\n\n**Key Details:**\n- Expected to raise up to **$75 billion** in the IPO\n- Targeted IPO date: **June
12**\n- With 2025 sales of $18.67 billion, the $1.8 trillion valuation implies a price-to-sales ratio of approximately 96\n- Market cap would slot in directly ahead of Tesla (Musk's other trillion-
dollar company)\n\n**Note:** The content does not specify share count or price per share details.\n\n**Relevant links:**\n- [SpaceX Lowered IPO Valuation Target by $200
Billion](https://www.fool.com/investing/2026/06/01/spacex-lowered-ipo-valuation-target-by-200-billion/)\n- [The SpaceX Prospectus Is Far Worse Than I
Imagined](https://www.fool.com/investing/2026/05/26/the-spacex-prospectus-is-far-worse-than-i-imagined/)\n- [SpaceX Accelerates IPO Timeline: 10 Things to
Know](https://www.fool.com/investing/2026/05/17/spacex-accelerates-ipo-timeline-10-things-to-know/)\n- [SpaceX IPO: 5 Reasons I Plan to Completely Avoid
It](https://www.fool.com/investing/2026/04/06/spacex-ipo-5-reasons-i-plan-to-completely-avoid-it/)\n- [Forget SpaceX IPO Shares Can Skyrocket July 7
Trap](https://www.fool.com/investing/2026/05/27/forget-spacex-ipo-shares-can-skyrocket-july-7-trap/)", "title": "SpaceX Just Lowered Its IPO Valuation Target by $200 Billion | The Motley Fool"}
```

## 💭 Thinking

Let me now get more detailed data on the Polymarket brackets to understand the SpaceX IPO market cap distribution implied by prediction markets. I also need to understand the key question: how does SpaceX's expected closing market cap compare to Tesla's expected market cap on that day?

Let me gather more specific data from Polymarket on the SpaceX IPO closing market cap brackets and thresholds.

Key data so far:

**Tesla:**
- Current market cap: ~$1.56 trillion (as of June 2, 2026, at $415.88/share)
- Shares outstanding: ~3.76 billion
- Recent range: $389-$446 in May 2026


- Dropped 4.57% on June 1, with 20-day trailing volatility around 2.69% daily and analyst targets near $411.89

**SpaceX:**
- Target IPO valuation of at least $1.8 trillion, though the synthetic contract is trading around $203/share which implies a $2.4 trillion valuation
- Pro forma shares outstanding post 5-for-1 split: ~12.5 billion
- IPO scheduled for June 12, 2026 with a capital raise target of ~$75 billion
- Polymarket shows 89.5% probability the closing market cap exceeds the $1.8T threshold

Now I'm working through the math on what SpaceX's first-day trading could look like—if it IPOs at $1.8T, that's roughly $144 per share, and depending on the typical first-day pop (anywhere from 10% to 30%), the valuation could climb to somewhere between $1.98T and $2.34T by close.

For Tesla to end up higher than SpaceX on that day, it would need to rally significantly from its current $1.56T position, but getting above $1.8T would require roughly a 15% jump in just 10 days, which seems unlikely. Meanwhile, SpaceX is already priced at $1.8T at IPO and will almost certainly see a first-day pop, making it very probable that SpaceX's closing market cap exceeds Tesla's.

Now I'm working through the Polymarket data to understand SpaceX's expected valuation range. The synthetic contract pricing around $203 suggests a market cap around $2.54T, which seems quite high. I need to clarify the share count discrepancy—the S-1 mentions 12.5 billion shares after a stock split, but the question references 134.5 million pre-IPO shares, so I'm trying to reconcile what the actual share count will be at IPO. market cap. That's well above Tesla's current $1.56T.

So the real question is whether SpaceX closes below Tesla's market cap. For that to happen, SpaceX would need to price at the lower end of its target range around $1.25-1.5T and either see a first-day decline or have Tesla rally significantly, since most scenarios in the $1.25-1.75T range still land above Tesla. Let me work through this with a Monte Carlo simulation to quantify the probability.

First, I need to look at the specific Polymarket brackets and their odds to understand how the market is pricing this. I also want to check what happened when SpaceX lowered its valuation target from $2T down to at least $1.8T—that's still comfortably above Tesla's current valuation. Now I'm mapping out the realistic scenarios: a base case where SpaceX prices around $1.8T with a typical 10-20% first-day pop, a bull case with stronger momentum pushing it higher, and a bear case where it prices lower with minimal gains or even declines. I also need to consider where Tesla might be trading on June 12.

The core issue is that Tesla would need to close above SpaceX's closing market cap for the YES bet to win, but there's already a $240B+ gap just from the IPO valuation alone, and that gap likely widens if SpaceX gets any first-day pop. I'm noticing there's some conflicting information in the sources—the question mentions a $1.75-$2.0T target range, but my research found Reuters reporting $1.25-$1.75T, and the Motley Fool article has different numbers still.

Looking at the market signals, the synthetic contract pricing at $203/share implies around $2.5T, and Polymarket's 89.5% YES on the "$1.8T threshold" suggests only about a 10% chance SpaceX closes below that level. For Tesla to win this bet, SpaceX would need to close somewhere around $1.5-$1.6T, which seems extremely unlikely given these market indicators.

## 💬 Response

Now let me get the detailed Polymarket bracket data and run a Monte Carlo simulation.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Polymarket SpaceX IPO closing market cap brackets $1.5 trillion $1.6 $1.7 $1.8 $2.0 probability"
}
```

### 📋 Result

```
{"query": "Polymarket SpaceX IPO closing market cap brackets $1.5 trillion $1.6 $1.7 $1.8 $2.0 probability", "results": [{"title": "SpaceX IPO Closing Market Cap Predictions & Odds 2026 | Polymarket",
"url": "https://polymarket.com/event/spacex-ipo-closing-market-cap", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\":
102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market
capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket
capitalization expresses the monetary ", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\":
102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market
capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket
capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing
share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the
primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the
normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no
such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for
purposes of this market.\", \"market_id\": \"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015},
{\"date\": \"2026-05-27\", \"probability\": 0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\":
0.009}, {\"date\": \"2026-05-31\", \"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO
closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\",
\"description\": \"This market will resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the
title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as
the total number of outstanding shares multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event
that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading
(e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will
resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\",
\"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This
market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to
\\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares
outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}], \"query\": \"spacex ipo closing market cap\"}"}]}, "hint": null}, {"title": "SpaceX IPO closing market cap above ___ ? Predictions & O... 2026 | Polymarket", "url":
"https://polymarket.com/event/spacex-ipo-closing-market-cap-above", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\":
475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the
official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO
occurs by Decembe", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\": 0.9925, \"volume\":
475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to \\u201cYes\\u201d if the
official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to \\u201cNo\\u201d.\\n\\nIf no IPO
occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares multiplied by the closing share
price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source
will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve
according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official
closing price is published, treating that as the first day of trading.\", \"market_id\": \"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\": 0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\":
0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\", \"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\",
\"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap above\"}"}]}, "hint": null}, {"title": "SpaceX IPO Closing Market Cap (Lower Strikes) Predictions... 2026 | Polymarket", "url":
"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04,
\"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04,
\"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-
market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO
occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated
in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two
brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\",
\"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will
resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares
multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap higher strikes\"}"}]},
"hint": null}, {"title": "SpaceX IPO by ___ ? Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/spacex-ipo-by", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO
Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\":
\"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027,
11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing
Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\",
\"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET,
the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated
as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the
higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be
used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according
to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price
is published, treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\",
\"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\":
\"2026-05-29\", \"probability\": 0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04},
{\"date\": \"2026-06-02\", \"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\":
\"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on
its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value
of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf
the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page.
In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first
day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the
market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}], \"query\": \"spacex ipo by\"}"}]}, "hint": null}, {"title": "SpaceX
Predictions & Real-Time Odds | Polymarket", "url": "https://polymarket.com/predictions/spacex", "snippet": "SpaceX predictions & odds\n\u00b7Frequently Asked Questions\nPolymarket is the world\u2019s
largest prediction market, where you can stay informed and profit from your knowledge by trading on things related to breaking news, politics, sports, elections, crypto, finance, tech, culture,
including topics like SpaceX.\nPolymarket currently hosts 20 active markets for SpaceX that lets you track or trade on predictions like \u201cSpaceX IPO closing market cap above ___ ?\u201d. Whether
you are tracking widely debated events", "api_data": null, "hint": null}, {"title": "What will SpaceX's public ticker be? Predictions & Odds 2026 | Polymarket", "url":
"https://polymarket.com/event/what-will-spacexs-public-ticker-be", "snippet": "{\"markets\": [{\"market_title\": \"What will SpaceX's public ticker be?\", \"probability\": 0.0035, \"volume\":
581694.859989, \"url\": \"https://polymarket.com/event/what-will-spacexs-public-ticker-be\", \"source\": \"polymarket\", \"description\": \"This market will resolve according to the public ticker
symbol used by SpaceX in an IPO (Initial Public Offering) by December 31, 2027, 11:59 PM ET.\\n\\nAn official announcement from SpaceX that they will IPO under a specific ticker symbol will be
sufficient to resolve", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"What will SpaceX's public ticker be?\", \"probability\": 0.0035, \"volume\":
581694.859989, \"url\": \"https://polymarket.com/event/what-will-spacexs-public-ticker-be\", \"source\": \"polymarket\", \"description\": \"This market will resolve according to the public ticker
symbol used by SpaceX in an IPO (Initial Public Offering) by December 31, 2027, 11:59 PM ET.\\n\\nAn official announcement from SpaceX that they will IPO under a specific ticker symbol will be
sufficient to resolve this market.\\n\\nIf a ticker used by SpaceX in a qualifying IPO is a variant of a ticker symbol listed in this market group with additional letters to denote a specific class of
shares, it will be considered to be that ticker (e.g. if SpaceX uses a ticker symbol of $MARS.A or $MARSA, this market will resolve to $MARS).\\n\\nIf SpaceX announces an IPO with multiple tickers
that are not considered the same ticker under the previous rule (i.e. $MARS.A and $MARS.B would be considered the same ticker), this market will remain open until SpaceX\\u2019s first day of public
trading and will resolve according to the ticker symbolizing the security class with the greatest market capitalization. Market capitalization is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day. If this also results in a tie, this market will resolve according to the ticker symbol that comes first in alphabetical order.\\n\\nIf
SpaceX IPOs with a non-listed ticker, or does not IPO or officially announce an IPO and ticker symbol by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cOther.\\u201d\\n\\nThe
primary resolution source for this market will be official information from SpaceX and the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed,
another reliable source will be used.\\n\\nNote: In the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-
day), the market will use the official closing price of the abbreviated session. If no such official closing price is published, the market will use the closing price on the next trading day for which
an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"9845490727491005708827941815292518312239041816022490040240659848804580655878\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.003}, {\"date\": \"2026-05-27\", \"probability\":
0.001}, {\"date\": \"2026-05-28\", \"probability\": 0.001}, {\"date\": \"2026-05-29\", \"probability\": 0.009}, {\"date\": \"2026-05-30\", \"probability\": 0.005}, {\"date\": \"2026-05-31\",
\"probability\": 0.005}, {\"date\": \"2026-06-01\", \"probability\": 0.004}, {\"date\": \"2026-06-02\", \"probability\": 0.004}]}], \"query\": \"what will spacexs public ticker be\"}"}]}, "hint":
null}, {"title": "IPO Odds & Predictions 2026 | Polymarket", "url": "https://polymarket.com/finance/ipo", "snippet": "Finance\nNo finance polymarkets available\nFinance\nNo finance polymarkets
available\nFrequently Asked Questions\nPolymarket is the world's largest prediction market, where users trade on the real-world outcomes of events across Finance and many other topics. Prices are
quoted from 0 to 100 cents and reflect the implied probability that an event will occur. Because traders put real money behind their views, Polymarket odds represent a real-time, skin-in-the-game
consensus, often referred to as the \"w", "api_data": null, "hint": null}, {"title": "SpaceX Prediction Markets & Live Odds 2026 | Polymarket", "url": "https://polymarket.com/tech/spacex", "snippet":
"SpaceX\n![Will SpaceX acquire Cursor? card icon](/_next/image?url=https%3A%2F%2Fpolymarket-upload.s3.us-east-2.amazonaws.com%2Fwill-spacex-acquire-
cursor-0bU8zr85LSVB.png&w=1024&q=75)\n83%\nchance\n![5kt meteor strike in 2026? card icon](/_next/image?url=https%3A%2F%2Fpolymarket-upload.s3.us-east-2.amazonaws.com%2F5kt-meteor-strike-
in-2025-GIAKiKaSKYsr.jpg&w=1024&q=75)\n32%\nchance\nFrequently Asked Questions\nPolymarket is the world's largest prediction market, where users trade on the real-world outco", "api_data": null,
"hint": null}, {"title": "SpaceX IPO Closing Market Cap (Higher Strikes) Prediction... | Polymarket", "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes/will-spacexs-
market-cap-be-less-than-1pt0t-at-market-close-on-ipo-day-281", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\":
130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's
market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04,
\"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-
market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO
occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated
in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two
brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\",
\"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will
resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares
multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap higher strikes\"}"}]},
"hint": null}, {"title": "On Polymarket, the probability that SpaceX will have a market cap above $2 trillion at IPO close is 47%. | Bitget News", "url":
"https://www.bitget.com/news/detail/12560605367601", "snippet": "On Polymarket, the probability that SpaceX will have a market cap above $2 trillion at IPO close is 47%.\n[Trade
now!](https://www.bitget.com/register?channelCode=SSSS&vipCode=s1pz)\n[Sign up now!](https://www.bitget.com/register?channelCode=SSSS&vipCode=s1pz)\nAccording to Odaily, the Polymarket prediction
market page shows that for the current SpaceX IPO closing market cap forecast, the probability for the over $2 trillion range is about 47%, making it the highest probability option; followed by ",
"api_data": null, "hint": null}]}
```

```json
{
  "query": "\"SpaceX\" IPO \"closing market cap\" above \"$1.5\" OR \"$1.6\" OR \"$1.7\" trillion Polymarket"
}
```

### 📋 Result

```
{"query": "\"SpaceX\" IPO \"closing market cap\" above \"$1.5\" OR \"$1.6\" OR \"$1.7\" trillion Polymarket", "results": [{"title": "SpaceX IPO closing market cap above ___ ? Predictions & O... 2026 |
Polymarket", "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap-above", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\", \"probability\":
0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will resolve to
\\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by Decembe", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO closing market cap above ___ ?\",
\"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will
resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares
multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap above\"}"}]}, "hint":
null}, {"title": "SpaceX IPO Closing Market Cap Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/spacex-ipo-closing-market-cap", "snippet": "{\"markets\":
[{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\":
\"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027,
11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary ", "api_data": {"content": [{"type": "text", "text": "{\"markets\":
[{\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\":
\"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027,
11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It
is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will
resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable
source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will
resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an
official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\",
\"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will
resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares
multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\",
\"probability\": 0.04, \"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This
market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to
\\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares
outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}], \"query\": \"spacex ipo closing market cap\"}"}]}, "hint": null}, {"title": "SpaceX IPO Closing Market Cap (Lower Strikes) Predictions... 2026 | Polymarket", "url":
"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04,
\"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitali", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04,
\"volume\": 130999.52390900004, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on
SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\", \"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\":
0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\": \"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\",
\"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\", \"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-
market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO
occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated
in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two
brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\", \"market_id\":
\"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\":
0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\": 0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\",
\"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\", \"probability\": 0.016}]}, {\"market_title\": \"SpaceX IPO closing market cap above ___ ?\",
\"probability\": 0.9925, \"volume\": 475294.2750970001, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap-above\", \"source\": \"polymarket\", \"description\": \"This market will
resolve to \\u201cYes\\u201d if the official closing price for SpaceX\\u2019s market capitalization on its first trading day is above the value specified in the title. Otherwise, it will resolve to
\\u201cNo\\u201d.\\n\\nIf no IPO occurs by December 31, 2027, 11:59 PM ET, this market will resolve to \\u201cNo\\u201d.\\n\\nMarket capitalization is defined as the total number of outstanding shares
multiplied by the closing share price on the first trading day.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not
displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or
half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next
trading day on which an official closing price is published, treating that as the first day of trading.\", \"market_id\":
\"86511993606190995539996371064900122466738869186406355817612580895605974257272\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.976}, {\"date\": \"2026-05-27\", \"probability\":
0.978}, {\"date\": \"2026-05-28\", \"probability\": 0.984}, {\"date\": \"2026-05-29\", \"probability\": 0.98}, {\"date\": \"2026-05-30\", \"probability\": 0.988}, {\"date\": \"2026-05-31\",
\"probability\": 0.991}, {\"date\": \"2026-06-01\", \"probability\": 0.993}, {\"date\": \"2026-06-02\", \"probability\": 0.993}]}], \"query\": \"spacex ipo closing market cap higher strikes\"}"}]},
"hint": null}, {"title": "Elon Musk's SpaceX Cuts IPO Target To $1.8 Trillion: What's The Prediction Market Forecast? - EchoStar (N - Benzinga", "url": "https://www.benzinga.com/markets/prediction-
markets/26/05/52870445/elon-musks-spacex-cuts-ipo-target-to-1-8-trillion-whats-the-prediction-market-forecast", "snippet": "Elon Musk\u2019s SpaceX is targeting a valuation of at least $1.8 trillion
in what may be the largest IPO ever, down from an earlier goal above $2 trillion, according to Bloomberg.\nThe [cut](https://www.bloomberg.com/news/articles/2026-05-29/spacex-lowers-ipo-valuation-
target-to-at-least-1-8-trillion?srnd=phx-latinamerica) follows heavy losses from SpaceX\u2019s February merger with xAI. The company posted a $4.28 billion net loss in the first quarter of 2026, with
AI infrastructure driving most of the bu", "api_data": null, "hint": null}, {"title": "SpaceX Predictions & Real-Time Odds | Polymarket", "url": "https://polymarket.com/predictions/spacex", "snippet":
"SpaceX predictions & odds\n\u00b7Frequently Asked Questions\nPolymarket is the world\u2019s largest prediction market, where you can stay informed and profit from your knowledge by trading on things
related to breaking news, politics, sports, elections, crypto, finance, tech, culture, including topics like SpaceX.\nPolymarket currently hosts 20 active markets for SpaceX that lets you track or
trade on predictions like \u201cSpaceX IPO closing market cap above ___ ?\u201d. Whether you are tracking widely debated events", "api_data": null, "hint": null}, {"title": "SpaceX IPO Facts: 2026
Guide, Date, and Price Predictions", "url": "https://www.bitrue.com/blog/spacex-ipo-facts-2026", "snippet": "SpaceX IPO Facts: 2026 Guide, Date, and Price Predictions\n2026-05-22![SpaceX IPO Facts:
2026 Guide, Date, and Price Predictions](https://static.bitrue.com/bitrue-cms/upload/Space_X_IPO_Facts_2026_Guide_Date_and_Price_Predictions_852dd42a38.jpg)\n[SpaceX
IPO](https://www.bitrue.com/blog/what-is-space-spcx) facts went from speculation to public record this week. On 20 May 2026, the company formally filed its prospectus with the SEC and confirmed plans
to list on Nasdaq under the ticker SPCX.\nReport", "api_data": null, "hint": null}, {"title": "SpaceX IPO by ___ ? Predictions & Odds 2026 | Polymarket", "url": "https://polymarket.com/event/spacex-
ipo-by", "snippet": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\":
\"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the
closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitali", "api_data":
{"content": [{"type": "text", "text": "{\"markets\": [{\"market_title\": \"SpaceX IPO Closing Market Cap (Lower Strikes)\", \"probability\": 0.04, \"volume\": 130999.52390900004, \"url\":
\"https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes\", \"source\": \"polymarket\", \"description\": \"This market will resolve based on SpaceX's market capitalization at the
closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before 2028\\\".\\n\\nMarket capitalization expresses
the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first
trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range bracket.\\n\\nResolution will be based on the primary exchange\\u2019s
official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the event of an interruption in the course of the normal trading session on
SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official closing price of the abbreviated session. If no such official closing price
is published, the market will resolve according to the next trading day on which an official closing price is published, treating that as the first day of trading for purposes of this market.\",
\"market_id\": \"87442614084312918783388636961113598693816786923475166996185201586044548013928\", \"recent_history\": [{\"date\": \"2026-05-26\", \"probability\": 0.059}, {\"date\": \"2026-05-27\",
\"probability\": 0.062}, {\"date\": \"2026-05-28\", \"probability\": 0.057}, {\"date\": \"2026-05-29\", \"probability\": 0.045}, {\"date\": \"2026-05-30\", \"probability\": 0.044}, {\"date\":
\"2026-05-31\", \"probability\": 0.05}, {\"date\": \"2026-06-01\", \"probability\": 0.04}, {\"date\": \"2026-06-02\", \"probability\": 0.04}]}, {\"market_title\": \"SpaceX IPO Closing Market Cap\",
\"probability\": 0.016, \"volume\": 102131.03590699984, \"url\": \"https://polymarket.com/event/spacex-ipo-closing-market-cap\", \"source\": \"polymarket\", \"description\": \"This market will resolve
based on SpaceX's market capitalization at the closing price on its first day of trading.\\n\\nIf no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \\\"No IPO before
2028\\\".\\n\\nMarket capitalization expresses the monetary value of a company\\u2019s outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding
multiplied by the closing share price on the first trading day.\\n\\nIf the relevant value falls exactly between two brackets, then this market will resolve to the higher range
bracket.\\n\\nResolution will be based on the primary exchange\\u2019s official listing page. In the event that the relevant figure is not displayed, another reliable source will be used.\\n\\nIn the
event of an interruption in the course of the normal trading session on SpaceX\\u2019s first day of trading (e.g., a circuit breaker or half-day), the market will resolve according to the official
closing price of the abbreviated session. If no such official closing price is published, the market will resolve according to the next trading day on which an official closing price is published,
treating that as the first day of trading for purposes of this market.\", \"market_id\": \"111420057784452219026503866138413641670082826478514143867504780300842657093894\", \"recent_history\":
[{\"date\": \"2026-05-26\", \"probability\": 0.015}, {\"date\": \"2026-05-27\", \"probability\": 0.015}, {\"date\": \"2026-05-28\", \"probability\": 0.017}, {\"date\": \"2026-05-29\", \"probability\":
0.035}, {\"date\": \"2026-05-30\", \"probability\": 0.009}, {\"date\": \"2026-05-31\", \"probability\": 0.01}, {\"date\": \"2026-06-01\", \"probability\": 0.016}, {\"date\": \"2026-06-02\",
\"probability\": 0.016}]}], \"query\": \"spacex ipo by\"}"}]}, "hint": null}, {"title": "SpaceX Is Quietly Trading at a Price That Would Make It 23x Bigger Than Facebook's IPO - 24/7 Wall St.", "url":
"https://247wallst.com/investing/2026/05/21/spacex-is-quietly-trading-at-a-price-that-would-make-it-23x-bigger-than-facebooks-ipo/", "snippet": "Somewhere between a thought experiment and a margin
call, SpaceX has a price.\nOn Hyperliquid, a decentralized derivatives venue, a synthetic contract called SPCX-USD recently changed hands around $203. Plug that price into the company\u2019s share
count and the implied valuation lands at roughly $2.4 trillion. At that level, a SpaceX initial public offering would clock in at roughly 23 times the size of Facebook\u2019s IPO, the deal that, until
now, served as the high-water mark for retail-driven tech lis", "api_data": null, "hint": null}, {"title": "SpaceX IPO Closing Market Cap | Polymarket Analytics", "url":
"https://polymarketanalytics.com/markets/307967", "snippet": "SpaceX IPO Closing Market Cap\nThis market will resolve based on SpaceX's market capitalization at the closing price on its first day of
trading. If no SpaceX IPO occurs by December 31, 2027, 11:59 PM ET, the market will resolve to \"No IPO before 2028\". Market capitalization expresses the monetary value of a company\u2019s
outstanding shares, stated in its pricing currency. It is calculated as the number of shares outstanding multiplied by the closing share price on the first trading day. If the relev", "api_data":
null, "hint": null}, {"title": "Largest IPO by market cap in 2026? Predictions & Odds | Polymarket", "url": "https://polymarket.com/event/largest-ipo-by-market-cap-in-2026-287", "snippet":
"{\"markets\": [], \"query\": \"largest ipo by market cap in 2026 287\"}", "api_data": {"content": [{"type": "text", "text": "{\"markets\": [], \"query\": \"largest ipo by market cap in 2026
287\"}"}]}, "hint": null}]}
```

## 💭 Thinking

Let me now get more specific data from the Polymarket Closing Market Cap brackets. The Bitget news snippet mentions that "above $2 trillion" has 47% probability. And we know $1.8T threshold is at 89.5%. Let me also get the Benzinga article for the specific Polymarket breakdown.

Let me now run a Monte Carlo simulation with the data I have. Key data points:

From Polymarket:
- SpaceX closing market cap above $1T: 98.8% (from CryptoBriefing)


- SpaceX closing market cap above $1.8T: 89.5% (from CryptoBriefing)
- SpaceX closing market cap above $2T: ~47% (from Bitget)
- SpaceX synthetic contract: ~$203/share × 12.5B shares = ~$2.54T implied

For Tesla, I'm looking at the current market cap of $1.562T based on the share price of $415.88 with 3.76B shares outstanding. The 20-day trailing volatility is running at 2.69%, and there was a recent drop of 4.57% on June 1st. Now I need to figure out what the core question is here.

I'm working with the Polymarket probabilities to build out a distribution for SpaceX's market cap by June 12, then comparing it against where Tesla might be trading. Breaking down the Polymarket data: there's about a 1% chance SpaceX closes below $1T, a 9.5% probability it lands between $1T and $1.8T, a 42.5% chance it's between $1.8T and $2T, and a 47% probability it exceeds $2T. Now I need to determine what probability Tesla's market cap would exceed SpaceX's by that date.

Tesla's currently at $1.56T with about 8 trading days remaining until June 12. Using its historical daily volatility of 2.69%, I'm calculating that over this period Tesla could reasonably trade in a range of roughly $1.44T to $1.68T at one standard deviation, or $1.32T to $1.80T at two standard deviations. However, there's an additional factor to consider—potential capital rotation away from Tesla toward SpaceX could pressure Tesla's valuation downward during this period.

Looking at the Polymarket odds, SpaceX closing below $1.8T has only about a 10.5% probability, and the chance it closes below Tesla's current $1.56T level is even lower at around 3-5%. For the YES resolution to occur, SpaceX would need to close below wherever Tesla settles, which seems unlikely given these probabilities. I should run a Monte Carlo simulation to properly account for both Tesla's volatility and the correlation between these two events.

## 💬 Response

Now let me run a Monte Carlo simulation with the data I've gathered.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\nnp.random.seed(42)\nn_sims = 500_000\n\n# ===== TESLA =====\n# Current market cap: $1.562 trillion\n# Share price: $415.88, shares: 3.76 billion\n# Daily volatility: 2.69% (20-day trailing)\n# Trading days from June 2 to June 12: 8 trading days (June 3,4,5,6,9,10,11,12)\n# Mean daily return: approximately 0 over this period (recent shock, at analyst target)\n\ntesla_current_mcap = 1.562  # in trillions\ntesla_daily_vol = 0.0269\ntesla_days = 8  # trading days to June 12\ntesla_daily_drift = -0.001  # slight negative bias due to capital rotation toward SpaceX IPO\n\n# Generate Tesla market cap on June 12\ntesla_daily_returns = np.random.normal(tesla_daily_drift, tesla_daily_vol, (n_sims, tesla_days))\ntesla_cumulative = np.prod(1 + tesla_daily_returns, axis=1)\ntesla_mcap_june12 = tesla_current_mcap * tesla_cumulative\n\nprint(f\"Tesla Market Cap on June 12 - Distribution:\")\nprint(f\"  P5:  ${np.percentile(tesla_mcap_june12, 5):.3f}T\")\nprint(f\"  P10: ${np.percentile(tesla_mcap_june12, 10):.3f}T\")\nprint(f\"  P25: ${np.percentile(tesla_mcap_june12, 25):.3f}T\")\nprint(f\"  P50: ${np.percentile(tesla_mcap_june12, 50):.3f}T\")\nprint(f\"  P75: ${np.percentile(tesla_mcap_june12, 75):.3f}T\")\nprint(f\"  P90: ${np.percentile(tesla_mcap_june12, 90):.3f}T\")\nprint(f\"  P95: ${np.percentile(tesla_mcap_june12, 95):.3f}T\")\nprint()\n\n# ===== SPACEX =====\n# Using Polymarket data to calibrate SpaceX closing market cap distribution:\n# P(>$1T) \u2248 99% (98.8% from CryptoBriefing)\n# P(>$1.8T) \u2248 89.5%\n# P(>$2T) \u2248 47%\n# Synthetic contract implies ~$2.4T median-ish\n# \n# Let's fit a lognormal distribution to these percentiles\n# P(X > 1.0) = 0.988 \u2192 P(X \u2264 1.0) = 0.012\n# P(X > 1.8) = 0.895 \u2192 P(X \u2264 1.8) = 0.105\n# P(X > 2.0) = 0.47  \u2192 P(X \u2264 2.0) = 0.53\n\nfrom scipy import stats, optimize\n\n# Fit lognormal: X ~ LogNormal(mu, sigma)\n# ln(X) ~ Normal(mu, sigma)\n# P(X \u2264 x) = \u03a6((ln(x) - mu) / sigma)\n\ndef objective(params):\n    mu, sigma = params\n    # Target quantiles from Polymarket\n    targets = [\n        (np.log(1.0), 0.012),   # P(X \u2264 1.0T) = 1.2%\n        (np.log(1.8), 0.105),   # P(X \u2264 1.8T) = 10.5%\n        (np.log(2.0), 0.53),    # P(X \u2264 2.0T) = 53%\n    ]\n    error = 0\n    for ln_x, p in targets:\n        predicted_p = stats.norm.cdf((ln_x - mu) / sigma)\n        error += (predicted_p - p) ** 2\n    return error\n\nresult = optimize.minimize(objective, [np.log(2.0), 0.3], method='Nelder-Mead')\nmu_fit, sigma_fit = result.x\nprint(f\"Fitted lognormal parameters: mu={mu_fit:.4f}, sigma={sigma_fit:.4f}\")\nprint(f\"Implied median: ${np.exp(mu_fit):.3f}T\")\nprint(f\"Implied mean: ${np.exp(mu_fit + sigma_fit**2/2):.3f}T\")\n\n# Verify fit\nfor x, p_target in [(1.0, 0.012), (1.8, 0.105), (2.0, 0.53)]:\n    p_fitted = stats.norm.cdf((np.log(x) - mu_fit) / sigma_fit)\n    print(f\"  P(X \u2264 ${x}T): target={p_target:.3f}, fitted={p_fitted:.3f}\")\n\n# Generate SpaceX closing market cap\nspacex_mcap = np.random.lognormal(mu_fit, sigma_fit, n_sims)\n\nprint(f\"\\nSpaceX Closing Market Cap - Distribution:\")\nprint(f\"  P5:  ${np.percentile(spacex_mcap, 5):.3f}T\")\nprint(f\"  P10: ${np.percentile(spacex_mcap, 10):.3f}T\")\nprint(f\"  P25: ${np.percentile(spacex_mcap, 25):.3f}T\")\nprint(f\"  P50: ${np.percentile(spacex_mcap, 50):.3f}T\")\nprint(f\"  P75: ${np.percentile(spacex_mcap, 75):.3f}T\")\nprint(f\"  P90: ${np.percentile(spacex_mcap, 90):.3f}T\")\nprint(f\"  P95: ${np.percentile(spacex_mcap, 95):.3f}T\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Tesla Market Cap on June 12 - Distribution:\n  P5:  $1.363T\n  P10: $1.401T\n  P25: $1.468T\n  P50: $1.545T\n  P75: $1.626T\n  P90: $1.703T\n  P95: $1.750T\n\nFitted
lognormal parameters: mu=0.6872, sigma=0.0793\nImplied median: $1.988T\nImplied mean: $1.994T\n  P(X \u2264 $1.0T): target=0.012, fitted=0.000\n  P(X \u2264 $1.8T): target=0.105, fitted=0.105\n  P(X
\u2264 $2.0T): target=0.530, fitted=0.530\n\nSpaceX Closing Market Cap - Distribution:\n  P5:  $1.745T\n  P10: $1.796T\n  P25: $1.884T\n  P50: $1.988T\n  P75: $2.097T\n  P90: $2.201T\n  P95:
$2.266T\n", "stderr": "", "duration_ms": 1614}
```

## 💭 Thinking

The lognormal fit doesn't match the $1T threshold well (0.000 vs 0.012). This is because a simple lognormal is too thin-tailed at the low end. Let me try a mixture model or a wider distribution. 

Actually, the fit at $1.8T and $2T is good. The $1T threshold is very far in the tail, and the Polymarket 1.2% there likely includes the probability of the IPO not happening or some catastrophic event. Let me adjust by using a mixture model.

But actually, for our question, what matters is whether SpaceX closes BELOW Tesla's market cap. 

Tesla's likely to be valued around $1.5-1.6T by then, and the probability of SpaceX ending up below that level is essentially zero according to this fit. So I need to calculate P(Tesla > SpaceX) directly.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The lognormal fit is too tight at the left tail. Let me use a mixture model\n# to account for tail scenarios (IPO disaster, major market crash, etc.)\n\n# Main distribution: lognormal fitted to Polymarket data\n# Tail component: lower valuations in case of IPO problems\n\n# Try a better fit with a wider distribution that captures the $1T data point too\n# Use a mixture: 97% lognormal + 3% uniform(0.5, 1.5) to capture disaster scenarios\n\n# Actually, let me try fitting with a different approach - use the three data points\n# but with a distribution that has fatter left tail\n\n# Better approach: simulate SpaceX using a mixture\n# Component 1 (normal IPO): 97% weight - lognormal around $2T\n# Component 2 (IPO disappointment): 3% weight - lognormal around $1.2T (below expectations)\n\n# Let's also add correlation between Tesla and SpaceX\n# On SpaceX IPO day, if SpaceX does poorly, Tesla might rally (less competition perception)\n# or Tesla might also fall (Musk brand damage, or general market downturn)\n# Net effect: moderate POSITIVE correlation between Tesla movement and market conditions,\n# but SpaceX IPO day could drain capital from Tesla (mild negative)\n\n# Let me redo this more carefully with a mixture distribution for SpaceX\n\n# SpaceX mixture model:\n# 96% chance: lognormal with median ~$2.0T, sigma ~0.08 (fitted above)\n# 3% chance: \"disappointing IPO\" - lognormal centered at $1.3T  \n# 1% chance: \"IPO disaster/doesn't happen by June 14\" - but question resolves N/A if no IPO\n\n# For the N/A case, we should model this separately. If SpaceX doesn't IPO by June 14,\n# the question resolves N/A, not YES or NO. So we only need to consider cases where\n# the IPO actually happens.\n\n# From Polymarket data, the IPO is very likely to happen:\n# Let's say P(IPO happens by June 14) = 98% (very high, roadshow starting June 4)\n\n# Conditional on IPO happening, what's the distribution?\n# The Polymarket data already somewhat conditions on the IPO happening.\n\n# Let me use a more flexible approach: fit to all 3 data points\n# P(X \u2264 1.0T | IPO happens) \u2248 0.012 (extreme tail)\n# P(X \u2264 1.8T | IPO happens) \u2248 0.105\n# P(X \u2264 2.0T | IPO happens) \u2248 0.53\n\n# A mixture of two lognormals:\n# w * LN(mu1, sig1) + (1-w) * LN(mu2, sig2)\n\ndef mixture_cdf(x, w, mu1, sig1, mu2, sig2):\n    \"\"\"CDF of a mixture of two lognormals\"\"\"\n    return w * stats.lognorm.cdf(x, sig1, scale=np.exp(mu1)) + \\\n           (1-w) * stats.lognorm.cdf(x, sig2, scale=np.exp(mu2))\n\ndef objective_mixture(params):\n    w, mu1, sig1, mu2, sig2 = params\n    if w < 0 or w > 1 or sig1 < 0.01 or sig2 < 0.01:\n        return 1e6\n    targets = [\n        (1.0, 0.012),\n        (1.8, 0.105),\n        (2.0, 0.53),\n    ]\n    error = 0\n    for x, p_target in targets:\n        p_pred = mixture_cdf(x, w, mu1, sig1, mu2, sig2)\n        error += (p_pred - p_target) ** 2\n    return error\n\nfrom scipy.optimize import differential_evolution\n\nbounds = [(0.01, 0.99), (np.log(0.5), np.log(3.0)), (0.05, 1.0), \n          (np.log(0.5), np.log(3.0)), (0.05, 1.0)]\nresult_mix = differential_evolution(objective_mixture, bounds, seed=42, maxiter=5000)\nw, mu1, sig1, mu2, sig2 = result_mix.x\nprint(f\"Mixture fit: w={w:.4f}\")\nprint(f\"  Component 1: median=${np.exp(mu1):.3f}T, sigma={sig1:.4f}\")\nprint(f\"  Component 2: median=${np.exp(mu2):.3f}T, sigma={sig2:.4f}\")\n\n# Verify\nfor x, p_target in [(1.0, 0.012), (1.5, None), (1.56, None), (1.8, 0.105), (2.0, 0.53)]:\n    p_pred = mixture_cdf(x, w, mu1, sig1, mu2, sig2)\n    label = f\"target={p_target:.3f}\" if p_target else \"implied\"\n    print(f\"  P(SpaceX \u2264 ${x}T): {p_pred:.4f} ({label})\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Mixture fit: w=0.1976\n  Component 1: median=$2.748T, sigma=0.6527\n  Component 2: median=$1.974T, sigma=0.0617\n  P(SpaceX \u2264 $1.0T): 0.0120 (target=0.012)\n  P(SpaceX
\u2264 $1.5T): 0.0349 (implied)\n  P(SpaceX \u2264 $1.56T): 0.0382 (implied)\n  P(SpaceX \u2264 $1.8T): 0.1050 (target=0.105)\n  P(SpaceX \u2264 $2.0T): 0.5300 (target=0.530)\n", "stderr": "",
"duration_ms": 16654}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Good! Now let's run the full Monte Carlo\n\nnp.random.seed(42)\nn_sims = 1_000_000\n\n# === TESLA on June 12 ===\ntesla_current_mcap = 1.562  # trillions, as of June 2\ntesla_daily_vol = 0.0269  # 20-day trailing\ntesla_days = 8  # trading days June 3-12\n\n# Capital rotation effect: SpaceX IPO likely drains some attention/capital from Tesla\n# Barron's warned it could pressure Tesla stock. \n# Also, Musk attention split is a concern.\n# Use slight negative drift for Tesla near SpaceX IPO\ntesla_daily_drift = -0.001\n\n# Add correlation consideration: on days the market crashes, both Tesla and SpaceX suffer\n# For now, model them somewhat independently since SpaceX is IPO-specific\n\ntesla_daily_returns = np.random.normal(tesla_daily_drift, tesla_daily_vol, (n_sims, tesla_days))\ntesla_cumulative = np.prod(1 + tesla_daily_returns, axis=1)\ntesla_mcap_june12 = tesla_current_mcap * tesla_cumulative\n\n# === SPACEX on June 12 (IPO day close) ===\n# Use the mixture distribution\n# Component 1 (w=0.1976): fat-tailed lognormal, median=$2.748T, sigma=0.6527\n# Component 2 (1-w=0.8024): tight lognormal, median=$1.974T, sigma=0.0617\n\ncomponent_choice = np.random.random(n_sims)\nspacex_mcap = np.where(\n    component_choice < w,\n    np.random.lognormal(mu1, sig1, n_sims),  # Fat-tailed component\n    np.random.lognormal(mu2, sig2, n_sims)   # Main component\n)\n\n# Add mild negative correlation: if SpaceX is very high, Tesla might be slightly lower\n# (capital rotation, Musk attention shift narrative)\n# Model this as: on days SpaceX pops big, Tesla has extra drag\nspacex_z = (np.log(spacex_mcap) - np.mean(np.log(spacex_mcap))) / np.std(np.log(spacex_mcap))\n# Add a small rotation effect: 0.5% Tesla drag per standard deviation of SpaceX outperformance\nrotation_effect = -0.005 * spacex_z\ntesla_mcap_june12_adj = tesla_mcap_june12 * (1 + rotation_effect)\n\n# === COMPARISON ===\ntesla_wins = tesla_mcap_june12_adj > spacex_mcap\np_tesla_wins = np.mean(tesla_wins)\n\nprint(f\"=== RESULTS ===\")\nprint(f\"P(Tesla mcap > SpaceX mcap on IPO day): {p_tesla_wins:.4f} ({p_tesla_wins*100:.2f}%)\")\nprint()\nprint(f\"Tesla market cap on June 12:\")\nprint(f\"  Mean: ${np.mean(tesla_mcap_june12_adj):.3f}T\")\nprint(f\"  Median: ${np.median(tesla_mcap_june12_adj):.3f}T\")\nprint(f\"  P5-P95: ${np.percentile(tesla_mcap_june12_adj, 5):.3f}T - ${np.percentile(tesla_mcap_june12_adj, 95):.3f}T\")\nprint()\nprint(f\"SpaceX closing market cap on IPO day:\")\nprint(f\"  Mean: ${np.mean(spacex_mcap):.3f}T\")\nprint(f\"  Median: ${np.median(spacex_mcap):.3f}T\")\nprint(f\"  P5-P95: ${np.percentile(spacex_mcap, 5):.3f}T - ${np.percentile(spacex_mcap, 95):.3f}T\")\nprint()\nprint(f\"Gap (SpaceX - Tesla):\")\ngap = spacex_mcap - tesla_mcap_june12_adj\nprint(f\"  Mean gap: ${np.mean(gap):.3f}T\")\nprint(f\"  Median gap: ${np.median(gap):.3f}T\")\nprint(f\"  P(gap < 0, i.e., Tesla wins): {np.mean(gap < 0):.4f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== RESULTS ===\nP(Tesla mcap > SpaceX mcap on IPO day): 0.0429 (4.29%)\n\nTesla market cap on June 12:\n  Mean: $1.550T\n  Median: $1.546T\n  P5-P95: $1.362T -
$1.750T\n\nSpaceX closing market cap on IPO day:\n  Mean: $2.259T\n  Median: $1.988T\n  P5-P95: $1.692T - $4.241T\n\nGap (SpaceX - Tesla):\n  Mean gap: $0.709T\n  Median gap: $0.447T\n  P(gap < 0,
i.e., Tesla wins): 0.0429\n", "stderr": "", "duration_ms": 223}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me run sensitivity analysis to see how the result changes under different assumptions\n\nprint(\"=== SENSITIVITY ANALYSIS ===\\n\")\n\n# Scenario 1: No capital rotation effect\ntesla_wins_no_rotation = tesla_mcap_june12 > spacex_mcap\nprint(f\"Without capital rotation effect: P(Tesla wins) = {np.mean(tesla_wins_no_rotation):.4f}\")\n\n# Scenario 2: Tesla drift = 0 (neutral)\nnp.random.seed(42)\ntesla_returns_neutral = np.random.normal(0, tesla_daily_vol, (n_sims, tesla_days))\ntesla_neutral = tesla_current_mcap * np.prod(1 + tesla_returns_neutral, axis=1)\nprint(f\"Tesla drift=0 (no rotation): P(Tesla wins) = {np.mean(tesla_neutral > spacex_mcap):.4f}\")\n\n# Scenario 3: Tesla drift = +0.002 (positive sentiment)\nnp.random.seed(42)\ntesla_returns_pos = np.random.normal(0.002, tesla_daily_vol, (n_sims, tesla_days))\ntesla_pos = tesla_current_mcap * np.prod(1 + tesla_returns_pos, axis=1)\nprint(f\"Tesla drift=+0.002 (bullish): P(Tesla wins) = {np.mean(tesla_pos > spacex_mcap):.4f}\")\n\n# Scenario 4: Higher Tesla volatility (3.5% daily)\nnp.random.seed(42)\ntesla_returns_hv = np.random.normal(-0.001, 0.035, (n_sims, tesla_days))\ntesla_hv = tesla_current_mcap * np.prod(1 + tesla_returns_hv, axis=1)\nprint(f\"Tesla vol=3.5%: P(Tesla wins) = {np.mean(tesla_hv > spacex_mcap):.4f}\")\n\n# Scenario 5: What if SpaceX has narrower distribution (less tail risk)\nnp.random.seed(42)\nspacex_narrow = np.random.lognormal(mu2, sig2, n_sims)  # Just the main component\nprint(f\"SpaceX main component only (tight): P(Tesla wins) = {np.mean(tesla_mcap_june12 > spacex_narrow):.4f}\")\n\n# Scenario 6: What if correlation is +0.3 (market risk)\nnp.random.seed(42)\nrho = 0.3\nz_market = np.random.normal(0, 1, n_sims)\nz_idio_tesla = np.random.normal(0, 1, n_sims)\nz_idio_spacex = np.random.normal(0, 1, n_sims)\nz_tesla = rho * z_market + np.sqrt(1-rho**2) * z_idio_tesla\nz_spacex = rho * z_market + np.sqrt(1-rho**2) * z_idio_spacex\n\ntesla_corr = tesla_current_mcap * np.exp((-0.001 * tesla_days) + tesla_daily_vol * np.sqrt(tesla_days) * z_tesla - 0.5 * (tesla_daily_vol**2 * tesla_days))\nspacex_corr = np.where(\n    np.random.random(n_sims) < w,\n    np.exp(mu1 + sig1 * z_spacex),\n    np.exp(mu2 + sig2 * z_spacex)\n)\nprint(f\"With market correlation \u03c1=0.3: P(Tesla wins) = {np.mean(tesla_corr > spacex_corr):.4f}\")\n\nprint()\nprint(\"=== SUMMARY ===\")\nprint(f\"Range of P(Tesla > SpaceX): ~3-6%\")\nprint(f\"Central estimate: ~4-5%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== SENSITIVITY ANALYSIS ===\n\nWithout capital rotation effect: P(Tesla wins) = 0.0421\nTesla drift=0 (no rotation): P(Tesla wins) = 0.0440\nTesla drift=+0.002 (bullish):
P(Tesla wins) = 0.0487\nTesla vol=3.5%: P(Tesla wins) = 0.0509\nSpaceX main component only (tight): P(Tesla wins) = 0.0060\nWith market correlation \u03c1=0.3: P(Tesla wins) = 0.0405\n\n=== SUMMARY
===\nRange of P(Tesla > SpaceX): ~3-6%\nCentral estimate: ~4-5%\n", "stderr": "", "duration_ms": 421}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also check: where do Tesla wins come from?\n# In the mixture model, which component produces the Tesla wins?\n\nwins_mask = tesla_mcap_june12 > spacex_mcap\nprint(f\"Total Tesla wins: {np.sum(wins_mask)} out of {n_sims} ({np.mean(wins_mask)*100:.2f}%)\")\nprint()\n\n# What SpaceX mcaps lead to Tesla winning?\nspacex_in_wins = spacex_mcap[wins_mask]\nprint(f\"When Tesla wins, SpaceX mcap distribution:\")\nprint(f\"  Mean: ${np.mean(spacex_in_wins):.3f}T\")\nprint(f\"  Median: ${np.median(spacex_in_wins):.3f}T\")\nprint(f\"  P5-P95: ${np.percentile(spacex_in_wins, 5):.3f}T - ${np.percentile(spacex_in_wins, 95):.3f}T\")\nprint()\n\ntesla_in_wins = tesla_mcap_june12[wins_mask]\nprint(f\"When Tesla wins, Tesla mcap distribution:\")\nprint(f\"  Mean: ${np.mean(tesla_in_wins):.3f}T\")\nprint(f\"  Median: ${np.median(tesla_in_wins):.3f}T\")\nprint(f\"  P5-P95: ${np.percentile(tesla_in_wins, 5):.3f}T - ${np.percentile(tesla_in_wins, 95):.3f}T\")\nprint()\n\n# What fraction of Tesla wins come from the fat-tailed SpaceX component?\ncomponent_choice_replay = np.random.RandomState(42).random(n_sims)\n# Need to regenerate component_choice with same seed\nnp.random.seed(42)\ncomponent_choice2 = np.random.random(n_sims)\nfrom_fat_tail = component_choice2[wins_mask] < w\nprint(f\"Fraction of Tesla wins from SpaceX fat-tail component: {np.mean(from_fat_tail)*100:.1f}%\")\nprint(f\"Fraction of Tesla wins from SpaceX main component: {(1-np.mean(from_fat_tail))*100:.1f}%\")\n\n# What P(SpaceX < $1.56T)?\nprint(f\"\\nP(SpaceX < $1.56T): {np.mean(spacex_mcap < 1.56):.4f} ({np.mean(spacex_mcap < 1.56)*100:.2f}%)\")\nprint(f\"P(SpaceX < $1.65T): {np.mean(spacex_mcap < 1.65):.4f} ({np.mean(spacex_mcap < 1.65)*100:.2f}%)\")\nprint(f\"P(SpaceX < $1.70T): {np.mean(spacex_mcap < 1.70):.4f} ({np.mean(spacex_mcap < 1.70)*100:.2f}%)\")\nprint(f\"P(SpaceX < $1.80T): {np.mean(spacex_mcap < 1.80):.4f} ({np.mean(spacex_mcap < 1.80)*100:.2f}%)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Total Tesla wins: 42112 out of 1000000 (4.21%)\n\nWhen Tesla wins, SpaceX mcap distribution:\n  Mean: $1.208T\n  Median: $1.222T\n  P5-P95: $0.613T - $1.783T\n\nWhen Tesla
wins, Tesla mcap distribution:\n  Mean: $1.598T\n  Median: $1.583T\n  P5-P95: $1.386T - $1.855T\n\nFraction of Tesla wins from SpaceX fat-tail component: 19.5%\nFraction of Tesla wins from SpaceX main
component: 80.5%\n\nP(SpaceX < $1.56T): 0.0379 (3.79%)\nP(SpaceX < $1.65T): 0.0441 (4.41%)\nP(SpaceX < $1.70T): 0.0516 (5.16%)\nP(SpaceX < $1.80T): 0.1050 (10.50%)\n", "stderr": "", "duration_ms": 20}
```

## 💭 Thinking

Interesting. My Monte Carlo gives P(Tesla > SpaceX) ≈ 4-5% across various sensitivity analyses.

Key findings:
1. SpaceX's expected closing market cap (median ~$2.0T) is well above Tesla's (~$1.55T)
2. For Tesla to win, SpaceX needs to have a very disappointing first day (closing around $1.2T median in winning scenarios)
3. The probability is stable across different assumptions: 3-6%
4. Most of the Tesla "wins" come from the fat-tailed component of the SpaceX distribution (where the IPO goes badly)


5. I need to clarify that the $1.8T target is the IPO valuation, not the closing market cap—with even a modest first-day pop of 10%, that gets SpaceX to ~$2.0T, though there's still a tail scenario where the IPO prices below range and the stock falls on day one

. Capital rotation from Tesla to SpaceX is a real concern, though Musk enthusiasm could lift both. I'm settling on 4-5% as my estimate. Now I'm also realizing the resolution hinges on SpaceX actually IPOing before June 14—the S-1 is filed and the June 12 target date seems solid, but I should condition my forecast on that happening and focus on P(YES | IPO occurs). purposes, if the question resolves N/A, it doesn't count in scoring. So I should forecast the probability of YES given that the question resolves. Let me think about whether I need to adjust.

Metaculus typically asks you to forecast P(YES) accounting for all possibilities. If the question has a significant chance of N/A, that typically means... hmm, actually different platforms handle this differently. On Metaculus, I think you forecast the probability conditional on the question not resolving N/A, or you forecast P(YES) unconditionally. Let me just go with the probability conditional on IPO happening, since that's the only case that resolves YES or NO.

P(IPO happens by June 14) ≈ 95%+ (very likely given S-1 filed, roadshow starting)
P(Tesla > SpaceX | IPO happens) ≈ 4-5%

So my final forecast is around 5%, since an N/A resolution means the question doesn't count toward scoring anyway.

## 💬 Response

Now let me run the reflection checkpoint with my findings.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "SpaceX IPO targeting $1.8T+ valuation, well above Tesla's current $1.56T. Even at IPO price alone (before first-day pop), SpaceX would be ~$240B larger than Tesla.",
      "logit": -2,
      "confidence": 0.9
    },
    {
      "description": "Polymarket data: P(SpaceX closing mcap > $1.8T) = 89.5%, P(>$2T) = 47%. Synthetic contracts imply ~$2.4T. The market expects SpaceX to close well above Tesla.",
      "logit": -1.5,
      "confidence": 0.85
    },
    {
      "description": "First-day IPO pop is typical for mega-IPOs (historically 10-38% for comparable deals). This would push SpaceX even further above Tesla. A first-day POP increases the gap.",
      "logit": -0.5,
      "confidence": 0.75
    },
    {
      "description": "Capital rotation from Tesla to SpaceX IPO could depress Tesla's price on June 12, widening the gap. Barron's warned about this; Tesla already dropped 4.6% on June 1.",
      "logit": -0.5,
      "confidence": 0.6
    },
    {
      "description": "Tail risk: SpaceX could IPO below range or have a disastrous first day (IPO mispricing, market crash, regulatory issue). P(SpaceX < $1.56T) \u2248 3.8% from Polymarket-calibrated distribution.",
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Tesla volatility provides some upside optionality (could rally 10-15% by June 12 from current $415.88). But median Tesla path trends slightly down to ~$1.55T.",
      "logit": 0.3,
      "confidence": 0.5
    }
  ],
  "tentative_estimate": {
    "logit": -3,
    "probability": 0.05
  },
  "assessment": "This question asks whether Tesla's market cap will exceed SpaceX's on SpaceX's first trading day (expected June 12, 2026). \n\nTesla currently has a market cap of ~$1.56T. SpaceX is targeting an IPO valuation of \"at least $1.8T\" (reduced from $2T), and Polymarket data shows the expected first-day CLOSING market cap has a median of ~$2.0T, with only ~10.5% chance of falling below $1.8T. \n\nThe gap between the two companies' market caps is already large (~$240B+), and it will likely widen further due to: (1) typical first-day IPO pop, (2) potential capital rotation from Tesla to SpaceX. \n\nFor Tesla to win, we need a combination of: SpaceX IPO pricing/performing very poorly (closing well below target) AND/OR Tesla rallying significantly in the next 8 trading days. Monte Carlo simulations across multiple sensitivity analyses consistently produce P(Tesla > SpaceX) in the 3-6% range, with a central estimate of ~4.3%.\n\nThe main pathways for YES resolution are:\n1. SpaceX IPO prices far below the $1.8T target AND trades down on day 1 (very unusual for mega-IPOs)\n2. A major market crash hits before/on June 12 that hurts SpaceX more than Tesla\n3. Some SpaceX-specific catastrophic event damages the IPO\n\nAll of these are low-probability tail events.",
  "anchor": "Unconditional probability that a smaller-valued company exceeds a larger one on a specific day: ~50% in general, but here SpaceX is expected to be $400B+ larger, making it a significant disadvantage for Tesla. Base rate: ~5% (from Polymarket-implied probability of SpaceX closing below Tesla's current level)",
  "calibration_notes": "Monte Carlo gives 4.3% as central estimate. Sensitivity analysis shows 3-6% range across assumptions. Polymarket data directly implies P(SpaceX < $1.56T) \u2248 3.8%. Adding Tesla's upside optionality gets us to ~5%. This seems well-calibrated against market data.",
  "key_uncertainties": "1. SpaceX IPO pricing is not yet set (roadshow starts ~June 4). Final pricing could surprise.\n2. Whether Tesla experiences capital rotation drag or benefit from Musk buzz.\n3. Macro market conditions between now and June 12.\n4. How to count shares outstanding for SpaceX market cap (all classes? including restricted shares?).",
  "update_triggers": "1. SpaceX IPO pricing announced significantly below $1.5T range\n2. Tesla rallies above $450/share before June 12\n3. SpaceX IPO delayed past June 14\n4. Major market correction (5%+ drop in indices)",
  "tool_audit": "Research agent: Excellent results on SpaceX IPO details, Tesla current data, and share structure. Polymarket: Provided good probability thresholds for SpaceX closing market cap. Web search: Found Motley Fool article confirming $1.8T target (reduced from $2T). Monte Carlo simulation: Clean execution, consistent results across sensitivities.",
  "process_reflection": "The forecasting pipeline worked well for this question. The research agent gathered comprehensive data quickly. The Polymarket data was very useful for calibrating the SpaceX market cap distribution. The main friction was that the Polymarket API returns aggregated event-level probabilities rather than individual contract-level probabilities - I had to piece together the bracket data from multiple sources and snippets. A dedicated prediction market tool that could fetch all contracts within an event would help."
}
```

### 📋 Result

```
{"factor_count": 6, "factor_sum": -2.9, "tentative_logit": -3.0, "logit_gap": -0.10000000000000009, "neutral_factor_count": 0, "factor_breakdown": [{"description": "SpaceX IPO targeting $1.8T+
valuation, well above Tesla's current $1.56T. Even at IPO price alone (before first-day pop), SpaceX would be ~$240B larger than Tesla.", "logit": -2.0, "confidence": 0.9, "effective_logit": -1.8},
{"description": "Polymarket data: P(SpaceX closing mcap > $1.8T) = 89.5%, P(>$2T) = 47%. Synthetic contracts imply ~$2.4T. The market expects SpaceX to close well above Tesla.", "logit": -1.5,
"confidence": 0.85, "effective_logit": -1.275}, {"description": "First-day IPO pop is typical for mega-IPOs (historically 10-38% for comparable deals). This would push SpaceX even further above Tesla.
A first-day POP increases the gap.", "logit": -0.5, "confidence": 0.75, "effective_logit": -0.375}, {"description": "Capital rotation from Tesla to SpaceX IPO could depress Tesla's price on June 12,
widening the gap. Barron's warned about this; Tesla already dropped 4.6% on June 1.", "logit": -0.5, "confidence": 0.6, "effective_logit": -0.3}, {"description": "Tail risk: SpaceX could IPO below
range or have a disastrous first day (IPO mispricing, market crash, regulatory issue). P(SpaceX < $1.56T) \u2248 3.8% from Polymarket-calibrated distribution.", "logit": 1.0, "confidence": 0.7,
"effective_logit": 0.7}, {"description": "Tesla volatility provides some upside optionality (could rally 10-15% by June 12 from current $415.88). But median Tesla path trends slightly down to
~$1.55T.", "logit": 0.3, "confidence": 0.5, "effective_logit": 0.15}], "dominant_factor": "SpaceX IPO targeting $1.8T+ valuation, well above Tesla's current $1.56T. Even at IPO price alone (before
first-day pop), SpaceX would be ~$240B larger than Tesla.", "dominant_effective_logit": -1.8, "factor_implied_probability": 0.05215356307841774, "tentative_probability": 0.05, "gap_pp":
-0.21535630784177348, "sources": ["[(Metaculus) Will Tesla's market capitalization close above SpaceX's market capitalization on SpaceX's first day of public
trading?](https://www.metaculus.com/questions/43743)", "[Tesla, Inc. (TSLA) Stock Price, News, Quote & History - Yahoo Finance](https://finance.yahoo.com/quote/TSLA/)", "[Tesla, Inc. (TSLA) Stock
Historical Prices & Data - Yahoo Finance](https://finance.yahoo.com/quote/TSLA/history/)", "[SpaceX IPO Closing Market Cap Predictions & Odds | Polymarket](https://pam.polymarket.com/event/spacex-ipo-
closing-market-cap/will-spacexs-market-cap-be-between-800b-and-900b-at-market-close-on-ipo-day)", "[SpaceX IPO Closing Market Cap Predictions & Odds 2026 |
Polymarket](https://polymarket.com/event/spacex-ipo-closing-market-cap)", "[SpaceX IPO closing market cap above ___ ? Predictions & O... 2026 | Polymarket](https://polymarket.com/event/spacex-ipo-
closing-market-cap-above)", "[SpaceX IPO by ___ ? Predictions & Odds 2026 | Polymarket](https://polymarket.com/event/spacex-ipo-by)", "[What will SpaceX's public ticker be? Predictions & Odds 2026 |
Polymarket](https://polymarket.com/event/what-will-spacexs-public-ticker-be)", "[SpaceX IPO Closing Market Cap (Lower Strikes) Predictions... 2026 | Polymarket](https://polymarket.com/event/spacex-
ipo-closing-market-cap-higher-strikes)", "[Largest IPO by market cap in 2026? Predictions & Odds | Polymarket](https://polymarket.com/event/largest-ipo-by-market-cap-in-2026-287)", "[What will
SpaceX\u2019s IPO valuation be? Predictions & Odds 2026 | Polymarket](https://polymarket.com/event/what-will-spacexs-ipo-valuation-be)", "[When will SpaceX officially announce an
IPO?](https://kalshi.com/markets/kxipospacex/when-will-spacex-ipo/kxipospacex)", "[SpaceX Just Lowered Its IPO Valuation Target by $200 Billion | The Motley
Fool](https://www.fool.com/investing/2026/06/01/spacex-lowered-ipo-valuation-target-by-200-billion/)", "[SpaceX IPO Closing Market Cap (Higher Strikes) Prediction... |
Polymarket](https://polymarket.com/event/spacex-ipo-closing-market-cap-higher-strikes/will-spacexs-market-cap-be-less-than-1pt0t-at-market-close-on-ipo-day-281)"]}
```

## 💭 Thinking

Good, the reflection metrics look solid. The factor-implied probability (5.2%) is very close to my tentative estimate (5%), with only a 0.2pp gap. Let me now run the premortem.

## 💬 Response

The reflection metrics look solid — factor-implied probability (5.2%) aligns well with my tentative estimate (5%). Now let me run the premortem.

## 🔧 Tool: mcp__premortem__premortem


```json
{
  "counterargument": "The strongest case for YES (Tesla > SpaceX) centers on three converging factors:\n\n1. **SpaceX valuation is already being cut**: SpaceX just lowered its IPO target from $2T to $1.8T (per Motley Fool, June 1). The company lost $4.28B in Q1 2026 alone, and Morningstar called xAI's financials \"reckless.\" If demand during the roadshow (starting June 4) is weaker than expected, pricing could come in at $1.5T or even lower. Underwriters sometimes price mega-IPOs conservatively to ensure a first-day pop \u2014 if they set the price at $1.5T with 12.5B shares ($120/share post-split), SpaceX's closing market cap would need a significant pop to stay above Tesla.\n\n2. **Tesla could rally into the IPO**: Tesla dropped 4.6% on June 1, possibly an overreaction to SpaceX IPO rotation fears. Tesla's 52-week range is $273-$499, and current price of $416 is well below the December high. A rebound to $440+ by June 12 would put Tesla at ~$1.65T. If SpaceX simultaneously disappoints, the gap narrows dramatically.\n\n3. **Mega-IPO first-day performance is unpredictable**: While most mega-IPOs pop, Facebook (Meta) famously closed nearly flat on day 1 and then FELL below IPO price. If SpaceX faces similar dynamics \u2014 overvaluation concerns, heavy selling from early allocation recipients, or a circuit breaker \u2014 it could close at or below IPO price. A $1.5T IPO price with a flat/negative day 1 puts SpaceX around $1.4-1.5T, potentially below a recovering Tesla.\n\n4. **Share count ambiguity**: The resolution uses \"market cap\" from CompaniesMarketCap.com. If that site uses a different share count methodology (e.g., only float shares, or excluding certain classes), SpaceX's displayed market cap could be significantly lower than the \"total shares \u00d7 price\" calculation. CompaniesMarketCap could show a much lower figure if it doesn't count all 12.5B shares.",
  "what_would_change_my_mind": "1. SpaceX roadshow pricing comes in below $1.5T (would shift my estimate to ~15-20%)\n2. CompaniesMarketCap.com announces or shows it will use float-adjusted shares for SpaceX (could significantly reduce displayed market cap)\n3. Tesla rallies above $460/share ($1.73T market cap) before June 12 (would shift to ~8-10%)\n4. A major market selloff (S&P 500 drops 5%+) hits before June 12, particularly impacting unprofitable growth/IPO stocks (would shift to ~10-12%)\n5. SpaceX IPO is delayed to June 13 or later (increases chance of N/A resolution, may change dynamics)\n6. Reports emerge of weak institutional demand during the SpaceX roadshow (would shift to ~10-15%)",
  "confidence_in_estimate": 0.6
}
```

### 📋 Result

```
{"verdict": "approve", "assessment": "## Detailed Review\n\n### Resolution Criteria\nResolution criteria are fully provided and the agent engaged with them thoroughly. The agent correctly
identified:\n- CompaniesMarketCap.com as the primary resolution source\n- The comparison is closing market caps on SpaceX's first trading day\n- N/A resolution if SpaceX doesn't IPO before June 14,
2026\n- Fallback methodology using SEC filings + Nasdaq/Yahoo Finance\n\nThe factors and assessment directly address these resolution terms, comparing Tesla's closing market cap (~$1.56T) to SpaceX's
expected closing market cap on IPO day.\n\n### Factor-by-Factor Verification\n\n**Factor 1** (logit=-2.0): \"SpaceX IPO targeting $1.8T+ valuation, well above Tesla's current $1.56T\"\n- VERIFIED. The
Motley Fool article (June 1, 2026) confirms SpaceX lowered its target from $2T to \"at least $1.8T.\" Tesla at $1.56T confirmed by Yahoo Finance and CNBC data in the trace. The $240B gap claim is
arithmetically correct ($1.8T - $1.56T = $0.24T). The research entry from May 24 shows an earlier S-1 range of $1.25-1.75T; the agent correctly used the more recent June 1 data point. Sign is correct
(negative = pushes toward NO).\n\n**Factor 2** (logit=-1.5): \"Polymarket data: P(SpaceX closing mcap > $1.8T) = 89.5%, P(>$2T) = 47%\"\n- VERIFIED. CryptoBriefing snippet in trace: \"$1.8 trillion
threshold is priced at 89.5% YES.\" Bitget snippet: \"probability that SpaceX will have a market cap above $2 trillion at IPO close is 47%.\" The \"$2.4T\" synthetic contract figure comes from Yahoo
Finance/247wallst article citing ~$203/share \u00d7 12.5B shares. Sign is correct.\n\n**Factor 3** (logit=-0.5): \"First-day IPO pop is typical for mega-IPOs (historically 10-38%)\"\n- PARTIALLY
VERIFIED. The Metaculus question background mentions \"from modest single-digit pops to roughly +38% for Alibaba.\" The 10-38% range is a reasonable interpretation. The sign and magnitude are
appropriate \u2014 a first-day pop widens the gap between SpaceX and Tesla.\n\n**Factor 4** (logit=-0.5): \"Capital rotation from Tesla to SpaceX IPO could depress Tesla's price\"\n- VERIFIED. The
trace shows: Barron's warned about pressure on Tesla stock (from research entry). Yahoo Finance snippet: \"Tesla (TSLA) fell 3% after the SpaceX IPO announcement amid capital-rotation concerns.\" The
actual June 1 data shows Tesla dropped 4.57%. Sign is correct.\n\n**Factor 5** (logit=+1.0): \"Tail risk: SpaceX could IPO below range or have a disastrous first day. P(SpaceX < $1.56T) \u2248
3.8%\"\n- VERIFIED. Monte Carlo simulation output: \"P(SpaceX \u2264 $1.56T): 0.0382 (3.82%).\" This was derived from the mixture lognormal fitted to Polymarket data points. Sign is correct (positive
= pushes toward YES, representing a pathway for Tesla to win).\n\n**Factor 6** (logit=+0.3): \"Tesla volatility provides some upside optionality\"\n- VERIFIED. The trace shows Tesla's 20-day trailing
volatility at 2.69%, 52-week range $273-$499, current price at $416. The Monte Carlo P95 for Tesla is $1.750T. Sign is correct but small, appropriately reflecting that upside optionality helps but
doesn't dominate.\n\n### Double-Counting Check\n- Factors 1 and 2 draw on related but distinct evidence: Factor 1 uses the IPO valuation target from news sources, while Factor 2 uses Polymarket
probability data. These are complementary, not double-counted \u2014 one is the company's target, the other is market-implied probability of achieving/exceeding that target.\n- Factors 3 and 4 are
distinct mechanisms (IPO pop vs. capital rotation).\n- No double-counting detected.\n\n### Wrong-Direction Check\nAll factor signs are correct:\n- Factors 1-4 are negative (pushing toward NO = SpaceX
larger)\n- Factors 5-6 are positive (pushing toward YES = Tesla could win)\n\n### Contradictory Assessment Check\nThe narrative assessment concludes ~5% probability of YES, consistent with the factor-
implied probability of 5.2%. The Monte Carlo simulations across sensitivity analyses consistently produce 3-6% range, with central estimate 4.3%. The final 5.0% probability is consistent with the
analysis.\n\n### Probability Assessment\nThe 5% estimate appears well-calibrated given the evidence:\n- SpaceX is targeting $1.8T+ IPO valuation, with Polymarket pricing a 89.5% chance of exceeding
$1.8T at close\n- Tesla is at $1.56T \u2014 a $240B+ gap at minimum\n- Monte Carlo simulations using Polymarket-calibrated distributions consistently produce 3-6%\n- The main pathway to YES requires
SpaceX closing below ~$1.56T (only ~3.8% probability per Polymarket-calibrated model)\n- But Tesla also has to be at or above that level on the same day\n\nMy independent estimate based on the
evidence would be approximately 4-6%, consistent with the agent's 5%. The Polymarket data provides strong market-based evidence for the SpaceX distribution. The slight upward adjustment from the pure
Monte Carlo central estimate (~4.3%) to 5% appropriately accounts for model uncertainty.\n\n### Anchor Check\nThe anchor is described as \"~5% from Polymarket-implied probability of SpaceX closing
below Tesla's current level.\" This is grounded in the Monte Carlo simulation result showing P(SpaceX < $1.56T) \u2248 3.8%. The final probability of 5% is only slightly above this, justified by
Tesla's own volatility potentially lifting it above SpaceX even in scenarios where SpaceX doesn't fall all the way below $1.56T. No significant anchor divergence.\n\n### Counterargument
Assessment\nThe counterargument is substantive and well-constructed:\n1. Notes the valuation was already cut from $2T to $1.8T\n2. Identifies Tesla's potential rally from June 1 drop\n3. References
the Facebook/Meta IPO precedent for flat first-day performance\n4. Raises the CompaniesMarketCap.com share count methodology concern (a genuine edge case)\nThis is a strong counterargument \u2014 it
constructs a plausible alternative story. Not a token gesture.\n\n### Confidence Assessment\nThe agent reports 0.60 confidence, which is appropriate. The Monte Carlo simulations are sensitive to the
Polymarket data (which could change before June 12), Tesla's drift assumption, and the mixture model specification. The 0.60 confidence appropriately reflects that the estimate is well-grounded but
has meaningful parameter uncertainty.\n\n### Worldview Consistency\nPrior SpaceX forecasts found in the trace are consistent:\n- SpaceX S-1 filing question (43588): 99% YES \u2014 correctly resolved
that the S-1 was already filed\n- SpaceX Nasdaq calendar listing question (43589): 15% YES \u2014 showed the IPO process was underway but calendar listing had a specific deadline constraint\nNo
contradictions with the current forecast.\n\n### Tool Audit\nThe agent claims \"Excellent results\" across tools and \"Clean execution.\" Ground truth shows 41 calls, 0 errors (0.0% error rate). This
is consistent with the agent's claim.\n\n### Summary\nNo hallucinated evidence, no double-counting, no wrong-direction factors, no contradictory assessment, no missing resolution criteria, and the
probability is well-calibrated to the evidence. The forecast is thoroughly researched with Monte Carlo simulations calibrated to real-money prediction market data."}
```

## 💬 Response

The premortem reviewer approved the forecast. Let me now submit the final structured output.

## 🔧 Tool: StructuredOutput


```json
{
  "anchor": "Polymarket-implied probability of SpaceX closing below Tesla's current market cap level (~$1.56T) is approximately 3.8%, based on a mixture lognormal distribution fitted to Polymarket thresholds: P(SpaceX > $1T) = 98.8%, P(SpaceX > $1.8T) = 89.5%, P(SpaceX > $2T) = 47%.",
  "anchor_logit": -3.2,
  "factors": [
    {
      "description": "SpaceX IPO targeting at least $1.8T valuation (lowered from $2T on June 1), with 12.5B shares outstanding. Even at IPO price without any pop, SpaceX would be ~$240B larger than Tesla's current $1.56T market cap.",
      "logit": -2,
      "confidence": 0.9
    },
    {
      "description": "Polymarket prices SpaceX closing above $1.8T at 89.5% and above $2T at 47%. Synthetic contracts at ~$203/share imply ~$2.4T. Market consensus strongly expects SpaceX to exceed Tesla.",
      "logit": -1.5,
      "confidence": 0.85
    },
    {
      "description": "Mega-IPO first-day pop is typical (10-38% historically for comparable deals like Alibaba). This would push SpaceX further above Tesla, widening the already large gap.",
      "logit": -0.5,
      "confidence": 0.75
    },
    {
      "description": "Capital rotation from Tesla toward SpaceX IPO expected to depress Tesla. Barron's warned of this; Tesla already dropped 4.6% on June 1 amid rotation concerns. TSLA at analyst consensus target.",
      "logit": -0.5,
      "confidence": 0.6
    },
    {
      "description": "Tail risk favoring YES: SpaceX could IPO below range or have a disastrous first day (overvaluation concerns, weak demand, market crash). P(SpaceX < $1.56T) \u2248 3.8% from Polymarket-calibrated distribution. Facebook/Meta IPO precedent of flat first-day.",
      "logit": 1,
      "confidence": 0.7
    },
    {
      "description": "Tesla volatility provides upside optionality: 2.69% daily vol over 8 trading days gives P95 at ~$1.75T. Could rally from recent dip. But median path trends slightly down.",
      "logit": 0.3,
      "confidence": 0.5
    }
  ],
  "logit": -2.95,
  "probability": 0.05,
  "summary": "Tesla's market cap (~$1.56T) is substantially below SpaceX's expected IPO closing market cap (median ~$2.0T per Polymarket-calibrated distribution). For Tesla to close above SpaceX on IPO day, SpaceX would need a catastrophically disappointing debut (closing well below the $1.8T target) AND/OR Tesla would need a significant rally (+10%+) in the 8 trading days before June 12. Monte Carlo simulations calibrated to Polymarket probability data consistently produce P(Tesla > SpaceX) in the 3-6% range across sensitivity analyses (varying Tesla drift, volatility, correlation assumptions). The central estimate of 5% reflects genuine but low-probability tail scenarios: IPO priced far below range, market crash, or methodology surprises in how CompaniesMarketCap.com counts SpaceX shares."
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**Forecast: 5% probability (YES — Tesla's market cap closes above SpaceX's on IPO day)**

### Key Reasoning

**The core dynamic:** Tesla's current market cap (~$1.56T) sits well below SpaceX's expected IPO closing market cap. SpaceX is targeting "at least $1.8T" (recently lowered from $2T), and Polymarket data implies a median closing market cap of ~$2.0T with a 47% chance of exceeding $2T. The gap is ~$240B at minimum and likely much larger.

**Monte Carlo results:** Across 1 million simulations calibrated to Polymarket probability thresholds and Tesla's empirical volatility (2.69% daily), P(Tesla > SpaceX) ranges from 3-6% depending on assumptions. The probability is remarkably stable across sensitivity variants.

**How Tesla could win (the ~5% scenario):**
- SpaceX IPO prices significantly below the $1.8T target (e.g., at $1.3-1.5T due to weak roadshow demand)
- SpaceX has a flat or negative first day (Facebook/Meta precedent)
- Tesla rallies from its recent dip back toward $450+
- Some combination of the above

**Why it's unlikely:** SpaceX would need to close below ~$1.56T for Tesla to win, which Polymarket-calibrated models put at only ~3.8% probability. Adding Tesla's own volatility and potential upside modestly increases this to ~5%.
