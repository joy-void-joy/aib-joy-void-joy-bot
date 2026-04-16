# Reasoning Log: Will US existing home sales (seasonally adjusted annual rate) for March 2026 be at least 4.0 million?

*Generated: 2026-04-13T22:23:18.943577+00:00*


## 💭 Thinking

Let me analyze this forecasting question about US existing home sales for March 2026.

**Step 1: Parse Resolution Criteria**
- Question: Will US existing home sales (SAAR) for March 2026 be at least 4.0 million?
- Resolution source: NAR's first publication of March 2026 existing home sales
- Deadline: First publication before May 1, 2026
- Key: SAAR level, first reported value (ignore revisions)
- The question closed on March 7, 2026, and resolves April 1, 2026

**Step 2: Classify**


This is a measurement question where I need to estimate the probability that March 2026 existing home sales will reach or exceed 4.0 million SAAR. I'll need to look at historical sales data and recent trends to build a forecast model.

## 💬 Response

I'll analyze this step by step. Let me start by gathering data on existing home sales trends and current market conditions.

## 🔧 Tool: mcp__financial__fred_series


```json
{
  "series_id": "EXHOSLUSM495S",
  "observation_start": "2023-01-01",
  "limit": 50
}
```

### 📋 Result

```
{"series": {"id": "EXHOSLUSM495S", "title": "Existing Home Sales", "frequency": "Monthly", "units": "Number of Units", "seasonal_adjustment": "Seasonally Adjusted Annual Rate", "last_updated":
"2026-04-13"}, "latest_value": 3980000.0, "latest_date": "2026-03-01", "observation_start": "2023-01-01", "observation_end": "2026-04-14", "data_points": 14, "observations": [{"date": "2025-02-01",
"value": null}, {"date": "2025-03-01", "value": 4020000.0}, {"date": "2025-04-01", "value": 4020000.0}, {"date": "2025-05-01", "value": 4040000.0}, {"date": "2025-06-01", "value": 3980000.0}, {"date":
"2025-07-01", "value": 4030000.0}, {"date": "2025-08-01", "value": 4030000.0}, {"date": "2025-09-01", "value": 4080000.0}, {"date": "2025-10-01", "value": 4110000.0}, {"date": "2025-11-01", "value":
4090000.0}, {"date": "2025-12-01", "value": 4270000.0}, {"date": "2026-01-01", "value": 4020000.0}, {"date": "2026-02-01", "value": 4130000.0}, {"date": "2026-03-01", "value": 3980000.0}],
"regime_stats": {"stable_since": "2026-01-01", "stable_mean": 4043333.333333, "stable_std": 63420.991968, "observations_in_regime": 3, "prior_regime_mean": 4067000.0, "shift_magnitude": 23666.666667,
"shift_direction": "down"}}
```

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42499
  ]
}
```

### 📋 Result

```
{"post_id": 42499, "title": "Will US existing home sales (seasonally adjusted annual rate) for March 2026 be at least 4.0 million?", "type": "binary", "url":
"https://www.metaculus.com/questions/42499", "background_info": "This forecasts housing-market transaction volume, a key channel for consumption, credit demand, and construction-related
activity.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"0fcf1dc94baf791f\",\"sheet_id\":330.1}}`", "resolution_criteria": "This question resolves to yes if the National
Association of Realtors reports March 2026 existing home sales at a seasonally adjusted annual rate of 4.0 million or higher in its first publication reporting March 2026, released before May 1, 2026.
This question resolves to no if the first reported March 2026 SAAR is below 4.0 million. The value will be taken from NAR\u2019s Existing-Home Sales page at https://www.nar.realtor/research-and-
statistics/housing-statistics/existing-home-sales", "fine_print": "Use the first reported March 2026 SAAR (ignore later revisions). Use the headline \u201cExisting-home sales\u201d SAAR level.
Candidate Sources: NAR press release linked from the Existing-Home Sales page (backup) https://www.nar.realtor/newsroom | FRED series EXHOSLUSM495S (for cross-check only)
https://fred.stlouisfed.org/series/EXHOSLUSM495S", "num_forecasters": 120, "community_prediction": null, "prediction_history": [{"timestamp": "20260307_032151", "question_type": "binary", "summary":
"March 2026 existing home sales have been in a stable regime around 4.06M SAAR for 13 months, with 84.6% of months exceeding 4.0M. The January 2026 dip to 3.91M was explicitly weather-driven per NAR,
and the only prior sub-4.0M month (June 2025 at 3.98M) saw immediate recovery. With 2 months to recover, spring seasonal tailwinds, mortgage rates declining to ~6.0%, and weekly pending sales showing
YoY recovery, the odds favor crossing the 4.0M threshold. Modest headwinds from tariff uncertainty and weak (but weather-affected) January pending sales provide some downside risk. Monte Carlo models
weighted toward mean-reversion give ~64%, with qualitative spring/rate boost to ~67%.", "resolution": null, "probability": 0.67}]}
```

## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "existing home sales March 2026 NAR",
  "n_articles": 10,
  "hours_back": 168
}
```

### 📋 Result

```
Error calling tool 'search_news': APIError: 403015 - You've reached your maximum billable overage limit for 'requests'. To continue, you can increase your overage limit or upgrade your plan at
https://my.asknews.app/en/settings/usage/current-period
```

## 💬 Response

Excellent - FRED already has the March 2026 data. The FRED series shows the March 2026 value as **3,980,000** (3.98 million SAAR). But I need to verify this is the NAR's first reported value. Let me check the NAR source and recent news.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "NAR existing home sales March 2026 report"
}
```

### 📋 Result

```
{"query": "NAR existing home sales March 2026 report", "results": [{"title": "Existing-Home Sales", "url": "https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales",
"snippet": "-3.6%\nLatest News\nExisting-home sales decreased by 3.6% in March 2026. Month-over-month sales fell in all regions. Year-over-year sales rose in the South and West and declined in the
Northeast and Midwest.\nAccording to NAR Chief Economist Dr. Lawrence Yun. \u201cMarch home sales remained sluggish and below last year\u2019s pace. Lower consumer confidence and softer job growth
continue to hold back buyers.\u201d\n\u201cBecause inventory remains limited, the median home price rose to a new record high for the month of", "api_data": null, "hint": null}, {"title": "NAR
Existing-Home Sales Report Shows 3.6% Decrease in March", "url": "https://www.nar.realtor/newsroom/nar-existing-home-sales-report-shows-3-6-decrease-in-march", "snippet": "Month-Over-Month\n- 3.6%
decrease in existing-home sales\u2014seasonally adjusted annual rate of 3.98 million in March\n- 3.0% increase in unsold inventory\u20141.36 million units equal to 4.1 months\u2019 supply\nYear-Over-
Year\n- 1.0% decrease in existing-home sales\n- 1.4% increase in median existing-home sales price to $408,800\nWASHINGTON (April 13, 2026) \u2013 Existing-home sales decreased by 3.6% month-over-month
in March, according to the National Association of REALTORS\u00ae [Existing-Home Sales Report](https://www", "api_data": null, "hint": null}, {"title": "Existing home sales hit nine-month low in
March", "url": "https://thedailyrecord.com/2026/04/13/existing-home-sales-march/", "snippet": "WASHINGTON \u2013 U.S. existing home sales fell to a nine-month low in March amid tight inventory and
growing concerns over the [labor market](https://thedailyrecord.com/tag/labor-market/), and a recent increase in mortgage rates because of the war with Iran could limit activity this year.\nThe
larger-than-expected decline in sales reported by the National Association of Realtors on Monday was despite an improvement in [housing](https://thedailyrecord.com/tag/housing/) affordability at the
start of th", "api_data": null, "hint": null}, {"title": "Existing-Home Sales Fell 3.6 Percent In March As Buyer Confidence Erodes | Inman Real Estate News", "url":
"https://www.inman.com/2026/04/13/existing-home-sales-fell-3-6-in-march-as-buyer-confidence-erodes/", "snippet": "Existing-home sales fell in March for every region of the country, but home prices hit
a record high anyway.\nThat contradiction sits at the center of the [National Association of Realtors\u2019 March existing-home sales report](https://www.nar.realtor/newsroom/nar-existing-home-sales-
report-shows-3-6-decrease-in-march). Sales dropped 3.6 percent month-over-month to a seasonally adjusted annual rate of 3.98 million \u2014 down 1 percent from a year ago \u2014 while the median
existing-home price climbed to $408", "api_data": null, "hint": null}, {"title": "NAR Existing-Home Sales Report Shows 3.6% Decrease in March", "url": "https://www.globenewswire.com/news-
release/2026/04/13/3272613/0/en/NAR-Existing-Home-Sales-Report-Shows-3-6-Decrease-in-March.html", "snippet": "Washington, D.C., April 13, 2026 (GLOBE NEWSWIRE) -- Existing-home sales decreased by 3.6%
month-over-month in March, according to the National Association of REALTORS\u00ae [Existing-Home Sales report](https://www.globenewswire.com/Tracker?data=3d6LjC1PBEnobFEkmtQSQOlYYmRF1HDr2aTt9-
9fRE9AwoV7QjefVzMNo29HkjltEEAO1zYYKkkIxB4G6YzJweEbkGimy9AI2TXrQTTQOLQEDOC6jsWTwX7jbAa7eIYbPPy2z-tl2rSs1VBCAUY9xf9GCg3Hzij7vHFHskKSXgoeO9Ucb98mpooRqM-JYalD). The report provides the real estate
ecosystem\u2014including agents, ", "api_data": null, "hint": null}, {"title": "Existing Home Sales - March 2026 - Neil's Newsletter", "url": "https://neilsethi.substack.com/p/existing-home-sales-
march-2026", "snippet": "Existing Home Sales - March 2026\nExisting home sales fall to 9-month low in March (NE to the least on record) but prices remain firm on low inventories. NAR slashes 2026
sales forecasts.\nUS Existing Home Sales Mar: 3.98M (est 4.05M; prev 4.09M; prev R 4.13M)\n- Existing Home Sales (M/M): -3.6% (est -0.8%; prev 1.7%; prevR 2.7%)\n- Median Home Price For Existing Homes
(USD): 408.8K or +1.4% From Mar 2025 (prev 398.0K or +0.3%)\nMarch existing home sales fell -3.6% m/m \u2014 the second largest drop since", "api_data": null, "hint": null}, {"title": "United States
Existing Home Sales", "url": "https://tradingeconomics.com/united-states/existing-home-sales", "snippet": "Existing home sales in the United States fell by 3.6% from the previous month to an
annualized rate of 3.98 million in March of 2026, the lowest in nine months and missing market expectations of 4.06 million units. Inventory levels inched higher from the previous month to 1.36
million, equivalent to 4.1 months of supply at the latest sales rate, although both the level and sales ratio remain well below the historical average. Meanwhile, the median sales price of existing
homes were 1.4% higher f", "api_data": null, "hint": "Use fred_series/fred_search for US data, or world_bank_indicator for international data."}, {"title": "Existing-Home Sales Housing Snapshot",
"url": "https://www.nar.realtor/infographics/existing-home-sales-housing-snapshot", "snippet": "[Download](https://www.nar.realtor/sites/default/files/2026-04/2026-03-existing-home-sales-housing-
snapshot-infographic-04-13-2026-1000w-1500h.png) (PNG: 305 KB) | [Latest Data](https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales) | [News
Release](https://www.nar.realtor/newsroom/nar-existing-home-sales-report-shows-3-6-decrease-in-march)\nMarch 2026 brought 3.98 million in sales, a median sales price of $408,800, and 4.1 months of
inventory. The median sales pr", "api_data": null, "hint": null}, {"title": "NAR Report: Existing-Home Sales Drop 3.6% in March - El-Balad.com", "url": "https://www.el-balad.com/16911967", "snippet":
"NAR Report: Existing-Home Sales Drop 3.6% in March\n![NAR Report: Existing-Home Sales Drop 3.6% in March](https://www.el-balad.com/uploads/images/202604/image_870x_69dd3cc31bb28.webp)\nThe National
Association of REALTORS\u00ae (NAR) recently reported a notable decline in existing-home sales for March 2026. Sales dropped by 3.6% month-over-month, highlighting a continued sluggish market
performance compared to the previous year.\nOverview of Existing-Home Sales in March\nAccording to the NAR Existing-Hom", "api_data": null, "hint": null}, {"title": "Existing-Home Sales Receded 5.9%
in March", "url": "https://www.nar.realtor/newsroom/existing-home-sales-receded-5-9-in-march", "snippet": "-3.6%\nLatest News\nExisting-home sales decreased by 3.6% in March 2026. Month-over-month
sales fell in all regions. Year-over-year sales rose in the South and West and declined in the Northeast and Midwest.\nAccording to NAR Chief Economist Dr. Lawrence Yun. \u201cMarch home sales
remained sluggish and below last year\u2019s pace. Lower consumer confidence and softer job growth continue to hold back buyers.\u201d\n\u201cBecause inventory remains limited, the median home price
rose to a new record high for the month of", "api_data": null, "hint": null}]}
```

```json
{
  "query": "National Association Realtors existing home sales March 2026 SAAR",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "Existing Home Sales Fell in March \u2013 Eye On Housing", "url": "https://eyeonhousing.org/2026/04/existing-home-sales-fell-in-march/", "snippet": "Existing Home Sales Fell in March \u2013
Eye On Housing\n\n# Existing Home Sales Fell in March\n\nExisting home sales fell to a nine-month low in March as tight inventory, rising mortgage rates and growing concerns about the job market
constrained sales activity. While inventory has improved in recent months, it remains below historical norms, continuing to push home prices higher as demand outpaces supply. Meanwhile, the Iran war
has reversed the downward trend in mortgage rates, which jumped from 5.98%", "highlights": ["Existing Home Sales Fell in March \u2013 Eye On Housing\n\n# Existing Home Sales Fell in March Existing
home sales fell to a nine-month low in March as tight inventory, rising mortgage rates and growing concerns about the job market constrained sales activity. While inventory has improved in recent
months, it remains below historical norms, continuing to push home prices higher as demand outpaces supply. Meanwhile, the Iran war has reversed the downward trend in mortgage rates, which jumped from
5.98% before the conflict to 6.37% last week. These headwinds   ...    affordability. Total existing home sales, including single-family homes, townhomes, condominiums, and co-ops, fell 3.6% to a
seasonally adjusted annual rate of 3.98 million in March, the lowest level since June 2025, according to the National Association of Realtors (NAR). On a year-over-year basis, sales were 1.0% lower
than a year ago. The existing home inventory level was 1.4 million units in March, up 3.0% from February and 2.3% from a year ago. At the current sales rate, March unsold inventory sits at a
4.1-months\u2019 supply, up from 3.8-months in February and 4.0-months a year ago. Inventory between 4.5 to 6 months\u2019 supply is generally considered a balanced market. Homes stayed on the market
for a median of 41 days in March, down from 47 days in the previous month and 36 days in March 2025. The first-time buyer share was 32% in March, down from 34% in February and unchanged from a year
ago. The March all-cash sales share was 27% of transactions, down from 31% in February but up slightly from 26% a year ago. All-cash buyers are less affected by changes in interest rates. The March
median sales price of all existing homes was $408,800, up 1.4% from last year. This marks the 33rd consecutive month of year-over-year increases. The median condominium/co-op price in March was up
2.3% from a year ago at $371,500. Recent gains for home inventory will put downward pressure on resale home prices in most markets in 2026. All four major regions saw sales declines in March, ranging
from 1.3% in the West to 8.5% in the Northeast. On a year-over-year basis, sales rose in the West (+1.3%) and South (+2.2%), while sales in the Midwest and Northeast declined (-3.2% and 12.2%
respectively). The Pending Home Sales Index (PHSI) is a forward-looking indicator based on signed contracts. The PHSI rose from 70.8 to 72.1 in February due to improved affordability. On a year-over-
year basis, pending sales were 0.8% lower than a year ago, according to the National Association of Realtors\u2019 data. However, resurgence in mortgage rates driven by the Iran war could reverse the
increase. - existing home sales, National Association of Realtors (NAR)\n\n## Share this Page\n\n## Subscribe to Blog\n\nSubscribe ## Search by Category\n\n## Video Updates\n\nPlease leave this field
empty\n\n## Subscribe to Blog via Email Email Frequency Instant Daily Weekly\n\nCheck your inbox or spam folder to confirm your subscription. ## Construction Statistics\n\n## Labor Force\n\n##
Finance"], "published_date": "2026-04-13T18:02:29.000", "score": null}, {"title": "Existing-Home Sales Housing Snapshot", "url": "https://www.nar.realtor/infographics/existing-home-sales-housing-
snapshot", "snippet": "Existing-Home Sales Housing Snapshot\n\n# Existing-Home Sales Housing Snapshot\n\nDownload(PNG: 612 KB) | Latest Data| News Release\n\nFebruary 2026 brought 4.09 million in
sales, a median sales price of $398,000, and 3.8 months of inventory. The median sales price is up 0.3% year-over-year, and inventory was up 0.2 months from February 2025.", "highlights": ["Existing-
Home Sales Housing Snapshot\n\n# Existing-Home Sales Housing Snapshot Download(PNG: 612 KB) | Latest Data| News Release February 2026 brought 4.09 million in sales, a median sales price of $398,000,
and 3.8 months of inventory. The median sales price is up 0.3% year-over-year, and inventory was up 0.2 months from February 2025."], "published_date": "2018-12-21T15:44:35.000", "score": null},
{"title": "U.S. Existing Home Sales Drop in March to a Nine-Month Low - Haver Analytics", "url": "https://www.haver.com/articles/u-s-existing-home-sales-drop-in-march-to-a-nine-month-low", "snippet":
"U.S. Existing Home Sales Drop in March to a Nine-Month Low - Haver Analytics\n\nUSA| Apr 13 2026\n\n# U.S. Existing Home Sales Drop in March to a Nine-Month Low\n\n|in: Economy in Brief\n\n######
Summary\n\n- March sales -3.6% m/m to lower-than-expected 3.98 mil.; -1.0% y/y, fifth straight y/y decrease.\n- Broad-based regional m/m declines: Northeast (-8.5%), Midwest (-4.2%), South (-3.1%),
West (-1.3%); y/y sales up in the South and West but down in the Northeast and Midwest.\n- Median sales price +2.7% (+", "highlights": ["U.S. Existing Home Sales Drop in March to a Nine-Month Low -
Haver Analytics\n\nUSA| Apr 13 2026 # U.S. Existing Home Sales Drop in March to a Nine-Month Low\n\n|in: Economy in Brief\n\n###### Summary - March sales -3.6% m/m to lower-than-expected 3.98 mil.;
-1.0% y/y, fifth straight y/y decrease. - Broad-based regional m/m declines: Northeast (-8.5%), Midwest (-4.2%), South (-3.1%), West (-1.3%); y/y sales up in   ...    - Unsold inventory +3.0% (+2.3%
y/y) to four-month-high 1.36 mil. units; 4.1 months' supply. Existing home sales fell 3.6% m/m (-1.0% y/y) to 3.98 million units (SAAR) in March, the lowest level since June 2025, following a 2.7%
rebound to 4.13 million in February (previously +1.7%; 4.09 mil.), according to the National Association of Realtors (NAR). The Action Economics Forecast Survey had expected March sales of 4.08
million units. Sales remained 38.1% below a high of 6.43 million in January 2022 and 39.7% below a peak of 6.60 million in January 2021. The March fall coincided with an increase in the average
30-year fixed mortgage rate to a three-month-high 6.18% in March after declining to 6.05% in February, according to Freddie Mac. The sales figures are based on closings of sales contracts signed over
the past couple of months. Existing single-family home sales fell 3.5% (-0.3% y/y) to 3.63 million units in March, the second m/m fall in three months and the weakest reading since June 2025, after a
3.3% increase to 3.76 million in February. Sales of condos and co-ops slid 5.4% (-7.9% y/y) to 350,000, the fourth m/m slide in five months and the lowest level since May 2020, on   ...    y/y) to
430,000 in March after a 6.0% February decrease, marking the third consecutive m/m fall and a record low. Sales in the Midwest fell 4.2% (-3.2% y/y) to 920,000, the lowest reading since September
2024, reversing a 3.2% February   ...    following a 0.8% increase to $398,000 in February (unrevised) and three successive m/m declines. Prices were 5.5% below   ...    (+1.7%; +0.8% y/y).
Inventories of homes for sale increased for the third consecutive in March. The number of existing homes for sale (NSA) rose 3.0% (2.3% y/y) to 1.36 million units, the highest level since November,
following a 4.8% February rise to 1.32 million. The supply of homes on the market at the current selling rate (NSA) rose to 4.1 months, the highest in four months, after holding at 3.8 months in
February and January. The recent high of 4.6 months was in August 2025, while a record low in supply of 1.6 months was in January 2022. The data on existing home sales, prices and affordability are
compiled by the National Association of Realtors. The data on single-family home sales extend back to February 1968. Total sales and price data and regional sales can be found in Haver's USECON
database. Regional price and affordability data and national inventory data are available in the REALTOR database. Mortgage interest rates can be found in the WEEKLY database. The expectations figure
is from the Action Economics Forecast Survey, reported in the AS1"], "published_date": null, "score": null}, {"title": "Existing-Home Sales", "url": "http://www.realtor.org/research/research/ehsdata",
"snippet": "Existing-Home Sales\n\n# Existing-Home Sales\n\nSection Menu\n\nMap of EHS Regions\n\nMore\n\n+1.7%\n\n## Latest News\n\nExisting-home sales increased by 1.7% in February 2026. Month-over-
month sales rose in the Midwest, South and West, but fell in the Northeast. Year-over-year sales rose in the South and declined in the Northeast, Midwest and West.\n\n\u201cHousing affordability is
improving, and consumers are responding,\u201d said NAR Chief Economist Dr. Lawrence Yun. \u201cStill, there is a long way to go to return to pre", "highlights": ["Existing-Home Sales\n\n# Existing-
Home Sales\n\nSection Menu\n\nMap of EHS Regions\n\nMore\n\n+1.7%\n\n## Latest News Existing-home sales increased by 1.7% in February 2026. Month-over-month sales rose in the Midwest, South and West,
but fell in the Northeast. Year-over-year sales rose in the South and declined in the Northeast, Midwest and West. \u201cHousing affordability is improving, and consumers are responding,\u201d said
NAR Chief Economist Dr. Lawrence Yun. \u201cStill, there is a long way to go to return to pre-pandemic levels of transaction activity. There are more than 6 million more jobs than in 2019, yet home
sales per year are down by one million. Despite the modest gain in home sales, actual   ...    - Read the full news release.\n- See the summary of Existing Home Sales Statisticspdf(PDF: 511 KB) - View
supplemental market datapdf(PDF: 117 KB) The Existing-Home Sales data measures sales and prices of existing single-family homes for the nation overall, and gives breakdowns for the West, Midwest,
South, and Northeast regions of the country. These figures include condos and co-ops, in addition to single-family homes. Existing-Home Sales for March 2026 will be released on Monday, April 13, 2026
at 10:00 a.m. Eastern. Existing Home Sales data are provided by NAR solely for use as a reference. No part of this data may be reproduced, stored in a retrieval system, transmitted or redistributed in
any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without NAR's prior written consent for those who are not members of NAR. Members of the media who need copies
of previous months' existing-home sales news releases can contact the NAR media communications team at 202-383-7515. ## Data\n\nCitation guidelines for NAR research and statistics\n\nExpand
All\n\nOverview Breakouts of Single-family, Condo and Co-op\n\nSingle-Family Existing-Home Sales and Prices Condo and Co-op Sales and Prices\n\nAverage (Mean) Price\n\nHistorical
Information\n\nQuestions Existing-Home Sales for March 2026 will be released on Monday, April 13, 2026 at 10:00 a.m. Eastern. NAR Media Communications issues a news release close to mid-month with the
latest existing-home sales figures. The releases include analysis and quotes by NAR's Chief Economist Lawrence Yun regarding the sales volume, prices, inventory and interest rates. NAR Research Data
Release Dates\n\n### Existing-Home Sales Housing Snapshot\n\ninfographic\n\nMarch 10, 2026 February 2026 brought 4.09 million in sales, a median sales price of $398,000, and 3.8 months of inventory.
...    The Pending Home Sales Index is based on signed real estate contracts for existing single-family homes,"], "published_date": "2017-05-16T16:57:37.000", "score": null}, {"title": "US Existing
Home Sales Rebound", "url": "https://tradingeconomics.com/united-states/existing-home-sales/news/532323", "snippet": "US Existing Home Sales Rebound\n\n# US Existing Home Sales Rebound\n\n2026-03-10
14:07 By Andre Joaquim 1 min. read\n\nExisting home sales in the United States rose by 1.7% from the previous month to an annualized rate of 4.09 million in February of 2026, ahead of market
expectations that they would fall to 3.89 million.\n\nDespite the rebound, unsold inventory rose by a sharper 2.4% to a total of 1.29 million, which is equivalent to 3.8 months of supply at the latest
sales rate.\n\nSales price of existin", "highlights": ["US Existing Home Sales Rebound\n\n# US Existing Home Sales Rebound\n\n2026-03-10 14:07 By Andre Joaquim 1 min. read Existing home sales in the
United States rose by 1.7% from the previous month to an annualized rate of 4.09 million in February of 2026, ahead of market expectations that they would fall to 3.89 million. Despite the rebound,
unsold inventory rose by a sharper 2.4% to a total of 1.29 million, which is equivalent to 3.8 months of supply at the latest sales rate. Sales price of existing homes inched higher by 0.3% from the
previous year to $398,000, despite the drop in mortgage   ...    \u201cHousing affordability is improving, and consumers are responding,\u201d said NAR Chief Economist Dr. Lawrence Yun.   ...    News
Stream\n\nUS Existing Home Sales Fall to 9-Month Low Existing home sales in the United States fell by 3.6% from the previous month to an annualized rate of 3.98 million in March of 2026, the lowest in
nine months and missing market expectations of 4.06 million units. Inventory levels inched higher from the previous month to 1.36 million, equivalent to 4.1 months of supply at the latest sales rate,
although both the level and sales ratio remain well below the historical average. Meanwhile, the median sales price of existing homes were 1.4% higher from the previous year at $408,800, the highest
since November. According to NAR Chief Economist Dr. Lawrence Yun. \u201cMarch home sales remained sluggish and below last year\u2019s pace. Lower consumer confidence and softer job growth continue to
hold back buyers. Because inventory remains limited, the median home price rose to a new record high for the month of March. That price growth has helped the typical homeowner accumulate $128,100 in
housing wealth   ...    2026-04-13\n\nUS Existing Home Sales Rebound Existing home sales in the United States rose by 1.7% from the previous month to an annualized rate of 4.09 million in February of
2026, ahead of market expectations that they would fall to 3.89 million. Despite the rebound, unsold inventory rose by a sharper 2.4% to a total of 1.29 million, which is equivalent to 3.8 months of
supply at the latest sales rate. Sales price of existing homes inched higher by 0.3% from the previous year to $398,000, despite the drop in mortgage rates since the period. \u201cHousing
affordability is improving, and consumers are responding,\u201d said NAR Chief Economist Dr. Lawrence Yun. \u201cStill, there is a long way to go to return to pre-pandemic levels of transaction
activity.   ...    2026-03-10\n\nUS Existing Home Sales Fall the Most in 4 Years Existing home sales in the United States sank by 8.4% from the previous month to an annualized rate of 3.91 million in
January of 2026, firmly below market expectations of 4.18 million, after having reached a 3-year high of 4.35 million in the last month of 2025. It was the sharpest drop in nearly 4 years to the
lowest level since September 2024. Unsold inventory fell by 0.8% to 1.22 million units, equal to 3.7 months of supply. \"The below-normal temperatures and   ...    determine if this month\u2019s
numbers are an aberration,\u201d said NAR Chief Economist Dr. Lawrence Yun. \u201cAffordability conditions are improving, with NAR\u2019s Housing"], "published_date": "2026-03-10T14:07:14.000",
"score": null}, {"title": "Existing-Home Sales Explained", "url": "https://nar.realtor/research-and-statistics/housing-statistics/existing-home-sales/existing-home-sales-explained", "snippet":
"Existing-Home Sales Explained\n\nPhoto by Aldric Rivat on Unsplash\n\nPhoto by Aldric Rivat on Unsplash\n\n# Existing-Home Sales Explained\n\n#### What are existing-home sales, and why does the data
matter?\n\nDownload/Print Page Textdoc(DOC: 28KB)\n\nThe Existing-Home Sales data measures sales and prices of existing single-family homes for the nation overall, and gives breakdowns for the West,
Midwest, South, and Northeast regions of the country. These figures include condos and co-ops, in addition to sing", "highlights": ["Existing-Home Sales Explained\n\nPhoto by Aldric Rivat on
Unsplash\n\nPhoto by Aldric Rivat on Unsplash   ...    Download/Print Page Textdoc(DOC: 28KB) The Existing-Home Sales data measures sales and prices of existing single-family homes for the nation
overall, and gives breakdowns for the West, Midwest, South, and Northeast regions of the country. These figures include condos and co-ops, in addition to single-family homes. NAR Media Communications
issues a news release on or near the 25th of each month with the latest existing-home sales figures. The releases include analysis and quotes by NAR's Chief Economist Lawrence Yun regarding the sales
volume,   ...    NAR Research Data Release Dates\n\n## What Are Existing-Home Sales? Existing-home sales data are a monthly measure of the sales volume and prices of existing single-family homes,
condos,   ...    Existing-home sales account for more than 90% of total home sales, and the monthly data captures completed transactions. Each month, NAR surveys a representative sample of 160 Boards
and MLSs, which account for approximately 40% of all   ...    CC by 4.0\n\nCC by 4.0 The raw sales volume from the participating Boards/MLSs is carefully evaluated by the NAR Research team to ensure
...    The median sales price is computed for the nation and four census regions on a monthly basis. The median price is where   ...    Photo by Wiktor Karkocha on Unsplash\n\nCC by 4.0 The national
median condo/co-op price often is higher than the median single-family home price because condos are   ...    condos (as seen in NAR's quarterly metro area price reports). Visit the NAR Newsroom for
the latest existing-home sales news release. ## Why is the Data Seasonally Adjusted, and What Does That Mean? Every year sales activity tends to increase in spring and summer while typically slowing
down in winter. Sales activity between February and March typically increases by 34% while prices rise by 3%. In contrast, the slowest months of selling activity are November, December, January, and
February, with January being the slowest. When the weather is   ...    Photo by ranunculus on Unsplash\n\nCC by 4.0 However, these disparities don\u2019t represent actual trends in the housing market
because they are mostly due to seasonal variances. As a result, taking the seasonal differences out of the equation and creating an annualized rate really   ...    The annual rate for a particular
month represents what the total number of sales for a year would be if the relative   ...    Read more on seasonality in the housing market.\n\n## Why is Existing-Home Sales Data Important to
REALTORS\u00ae? NAR releases EHS data on a monthly basis to provide accurate and timely information on the state of the U.S. housing market. Knowing the monthly changes in home sales and price can
provide a snapshot of what is happening in the market, and what trends and challenges face the market both nationally and in each region. CC by 4.0\n\nPhoto by Louis Velazquez on Unsplash In addition
to providing a basis for our membership to understand the latest housing trends, it is widely reported by the national press. Moreover, the data enhances the effectiveness of NAR's political and
representational efforts on   ...    ## More About Existing-Home Sales\n\n### Existing-Home Sales The Existing-Home Sales data measures sales and prices of existing single-family homes. ### Existing-
Home Sales Housing Snapshot\n\ninfographic\n\nMarch 10, 2026 February 2026 brought 4.09 million in sales, a median sales price of $398,000, and 3.8 months of inventory. ### Housing Statistics and Real
Estate Market Trends NAR provides housing statistics and real estate market trends on the national, regional, and metro-market level"], "published_date": "2022-02-18T14:31:21.000", "score": null},
{"title": "NAR Existing-Home Sales Report Shows 1.7% Increase in February", "url": "https://www.realtor.org/newsroom/nar-existing-home-sales-report-shows-8-4-decrease-in-january", "snippet": "NAR
Existing-Home Sales Report Shows 1.7% Increase in February\n\n# NAR Existing-Home Sales Report Shows 1.7% Increase in February\n\nSection Menu\n\nOp-Eds & Letters to the Editor\n\nNAR in the
News\n\nMore\n\n## Month-Over-Month\n\n- 1.7% increase in existing-home sales\u2014seasonally adjusted annual rate of 4.09 million in February\n- 2.4% increase in unsold inventory\u20141.29 million
units equal to 3.8 months\u2019 supply\n\n## Year-Over-Year\n\n- 1.4% decrease in existing-home sales\n- 0.3% increase in median existing-home", "highlights": ["NAR Existing-Home Sales Report Shows
1.7% Increase in February # NAR Existing-Home Sales Report Shows 1.7% Increase in February\n\nSection Menu\n\nOp-Eds & Letters to the Editor NAR in the News\n\nMore\n\n## Month-Over-Month - 1.7%
increase in existing-home sales\u2014seasonally adjusted annual rate of 4.09 million in February - 2.4% increase in unsold inventory\u20141.29 million units equal to 3.8 months\u2019 supply ## Year-
Over-Year - 1.4% decrease in existing-home sales\n- 0.3% increase in median existing-home sales price to $398,000 WASHINGTON (March 10, 2026) \u2013 Existing-home sales increased by 1.7% month-over-
month in February, according to the National Association of REALTORS\u00ae Existing-Home Sales Report. The report provides the real estate ecosystem\u2014including agents, homebuyers and
sellers\u2014with data on the level of home sales, price, and inventory. Month-over-month sales rose in the Midwest, South and West, and fell in the Northeast. Year-over-year sales rose in the South
and fell in the Northeast, Midwest and West. Affordability improved for the eighth consecutive month, according to NAR\u2019s Housing Affordability Index\u2014increasing to 117.6 in February from
117.1 in January and 103.1 a year ago. This marks the highest level since March 2022. \u201cHousing affordability is improving, and consumers are responding,\u201d said NAR Chief Economist Dr.
Lawrence Yun. \u201cStill,   ...    growth, improve housing affordability, and boost transactions.\u201d ## National Snapshot\n\n### Total Existing-Home Sales for February - 1.7% increase in existing-
home sales 1 month-over-month to a seasonally adjusted annual rate of 4.09 million. - 1.4% decrease in sales year-over-year. ### Inventory in February - 1.29 million units: Total housing inventory2,
up 2.4% from January and 4.9% from February 2025. - 3.8-month supply of unsold inventory, unchanged from last month and up from 3.6 months one year ago.   ...    - $398,000: Median existing-home
price3 for all housing types, up 0.3% from one year ago ($396,800)\u2014the 32nd   ...    - Northeast +10.0%\n- Midwest +11.7%\n- South +14.1%\n- West +17.0%\n\n## Single-Family and Condo/Co-op Sales
...    ## Regional Snapshot for Existing-Home Sales in February\n\n### Northeast - 6.0% decrease in sales month-over-month to an annual rate of 470,000, down 4.1% year-over-year. - $479,800: Median
price, up 3.3% from February 2025.   ...    - 1.1% increase in sales month-over-month to an annual rate of 940,000, down 4.1% year-over-year.   ...    ### South - 1.6% increase in sales month-over-
month to an annual rate of 1.89 million, up 0.5% year-over-year.   ...    - 47 days: Median time on market for properties, up from 46 days last month and 42 days in February 2025. - 34% of sales were
first-time homebuyers, up from 31% in January and one year ago.   ...    6.84% one year ago.   ...    The National Association of REALTORS\u00ae is involved in all aspects of residential and
commercial real estate. The term   ...    # # # For local information, please contact the local association of REALTORS\u00ae for data from local multiple listing services (MLS). Local MLS data is the
most accurate source of sales and price information in specific areas, although there may be differences in reporting methodology. NOTE: NAR's Pending Home Sales Index for February will be released
March 17, and Existing-Home Sales for March will be released April 13. Release times are 10 a.m. Eastern. See NAR's statistical news release schedule.   ...    1 Existing-home sales, which include
single-family, townhomes, condominiums and co-ops, are based on transaction   ...    The annual rate for a particular month represents what the total number of actual sales for a year would be if the
relative pace for that month were maintained for 12 consecutive months. Seasonally"], "published_date": "2026-03-10T13:17:39.000", "score": null}, {"title": "Your privacy choices", "url":
"https://finance.yahoo.com/news/nar-existing-home-sales-report-140000488.html", "snippet": "Your privacy choices\n\nYour privacy choices\n# guce\n  guce \nYour privacy is important to us\nYahoo is
part of the Yahoo family of brandsThe sites and apps that we own and operate, including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands.\nWhen you use
our sites and apps, we use CookiesCookies (including similar technologies such as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in
our", "highlights": ["Your privacy choices Your privacy choices\n# guce\n  guce \nYour privacy is important to us Yahoo is part of the Yahoo family of brandsThe sites and apps that we own and operate,
including Yahoo and Engadget, and our digital advertising service, Yahoo Advertising.Yahoo family of brands. When you use our sites and apps, we use CookiesCookies (including similar technologies such
as web storage) allow the operators of websites and apps to store and read information from your device. Learn more in our cookie policy.cookies to: * provide our sites and apps to you\n* authenticate
users, apply security measures, and prevent spam and abuse, and * MeasurementWe count the number of visitors to our pages, the type of device they use (iOS or Android), the browser they use and the
duration of their visit to our websites and apps. This data is collected in aggregate and is not tied to specific users.measure your use of our sites and apps Your privacy choices If you click
'**Accept all**', we and our partners, including 251 who are part of the IAB Transparency & Consent Framework, will also store and / or access information on a device (in other words, use cookies) and
use precise geolocation data and other personal data such as Technical identifiersTechnical identifiers are system-generated strings of letters and numbers that can identify your device or you as a
user. They include browser cookies, device IDs and your IP address. They may be derived from hashed and / or encrypted email addresses or the statistical matching of other identifiers.technical
identifiers and browsing and search data, for analytics, personalised advertising and content, advertising and content measurement, and audience research and services development. If you do not want
us and our partners to use cookies and personal data for these additional purposes, click '**Reject all**'. If you would like to customise your choices, click '**Manage privacy settings**'. You can
withdraw your consent or change your choices at any time by clicking on the 'Privacy and Cookie settings' or 'Privacy dashboard' links on our sites and apps. Find out more about how we use your
personal data in our Privacy Policy and Cookie Policy. Accept all\nReject all\nManage privacy settings\nGo to end"], "published_date": "2026-03-10T00:00:00.000", "score": null}, {"title": "Existing
Home Sales - Charts and Data", "url": "http://www.mortgagenewsdaily.com/data/home-sales-existing.aspx", "snippet": "Existing Home Sales - Charts and Data iPhone and Android app. Download the NEW
APP\">\n\nShare\n\nMore Housing Data\n\nExisting Home Sales\n\nExisting home sales data is published monthly by the National Association of Realtors (more). The units displayed are in thousands and is
the seasonally adjusted annual rate.\n\nAdditional Charts: vs. Supply | vs. New Home Sales | vs. Mortgage Rates\n\n| Northeast | Midwest | South | West | Total |\n| --- | --- | --- | --- | --- |\n|
February 2026 | 470,000 | 940,000 | 1", "highlights": ["Existing home sales data is published monthly by the National Association of Realtors (more). The units displayed are   ...    | Northeast |
Midwest | South | West | Total |\n| --- | --- | --- | --- | --- | | February 2026 | 470,000 | 940,000 | 1,890,000 | 790,000 | 4,090,000 | | Change Month over Month | -6.00% | 1.08% | 1.61% | 8.22% |
1.74% | | Change Year over Year | -6.00% | -6.00% | -1.05% | -7.06% | -3.99% |\n| Previous | | January 2026 | 500,000 | 930,000 | 1,860,000 | 730,000 | 4,020,000 | | December 2025 | 520,000 |
1,000,000 | 2,020,000 | 810,000 | 4,350,000 | | November 2025 | 510,000 | 980,000 | 1,890,000 | 760,000 | 4,140,000 |   ...    | September 2025 | 490,000 | 940,000 | 1,860,000 | 770,000 | 4,060,000 |
| August 2025 | 400,000 | 910,000 | 1,660,000 | 660,000 | 3,630,000 | | July 2025 | 500,000 | 940,000 | 1,850,000 | 720,000 | 4,010,000 | | June 2025 | 460,000 | 950,000 | 1,810,000 | 710,000 |
3,930,000 | | May 2025 | 420,000 | 940,000 | 1,680,000 | 630,000 | 3,670,000 | | April 2025 | 480,000 | 970,000 | 1,810,000 | 740,000 | 4,000,000 | | March 2025 | 490,000 | 950,000 | 1,810,000 |
770,000 | 4,020,000 | | February 2025 | 500,000 | 1,000,000 | 1,910,000 | 850,000 | 4,260,000 | | February 2026 | Permits | MoM | YoY |\n| --- | --- | --- | --- |\n| Northeast | 470,000 | -6.00% |
-6.00% | | Midwest | 940,000 | 1.08% | -6.00% |\n| South | 1,890,000 | 1.61% | -1.05% |\n| West | 790,000 | 8.22% | -7.06% | | Total | 4,090,000 | 1.74% | -3.99% |   ...    Existing Home Sales report
on the number of completed real estate sales transactions on single-family homes, townhomes, condominiums and co-ops. Each month the National Association of Realtor\u00ae receives data on existing-
home sales from local associations/boards and multiple listing services (MLS) nationwide. NAR captures 30-40% of all existing-home sale transactions with its monthly   ...    The methodology in
calculating existing-home sales statistics is really quite simple. The monthly EHS economic indicator is based on a representative sample of 160 Boards/MLSs. The home sales data (raw data) is divided
into the   ...    volume is then converted into seasonally-adjusted annualized rates. Median and mean (average) prices are computed for   ...    4/7"], "published_date": null, "score": null},
{"title": "Existing-Home Sales - National Association of REALTORS\u00ae", "url": "https://www.nar.realtor/research-and-statistics/housing-statistics/existing-home-sales", "snippet": "Existing-Home
Sales\n\n# Existing-Home Sales\n\nSection Menu\n\nMap of EHS Regions\n\nMore\n\n-3.6%\n\n## Latest News\n\nExisting-home sales decreased by 3.6% in March 2026. Month-over-month sales fell in all
regions. Year-over-year sales rose in the South and West and declined in the Northeast and Midwest.\n\nAccording to NAR Chief Economist Dr. Lawrence Yun. \u201cMarch home sales remained sluggish and
below last year\u2019s pace. Lower consumer confidence and softer job growth continue to hold back buyers.\u201d\n\n\u201cBecause ", "highlights": ["Existing-Home Sales\n\n# Existing-Home
Sales\n\nSection Menu\n\nMap of EHS Regions\n\nMore\n\n-3.6%\n\n## Latest News Existing-home sales decreased by 3.6% in March 2026. Month-over-month sales fell in all regions. Year-over-year sales
rose in the South and West and declined in the Northeast and Midwest. According to NAR Chief Economist Dr. Lawrence Yun. \u201cMarch home sales remained sluggish and below last year\u2019s pace. Lower
consumer confidence and softer job growth continue to hold back buyers.\u201d \u201cBecause inventory remains limited, the median home price rose to a new record high for the month of March,\u201d Yun
added. \u201cThat price growth has helped the typical homeowner accumulate $128,100 in housing wealth over the past six years.\u201d - Read the full news release.\n- See the summary of Existing Home
Sales Statisticspdf(PDF: 484 KB) - View supplemental market datapdf(PDF: 117 KB) The Existing-Home Sales data measures sales and prices of existing single-family homes for the nation overall, and
gives breakdowns for the West, Midwest, South, and Northeast regions of the country. These figures include condos and co-ops, in addition to single-family homes. Existing-Home Sales for March 2026
will be released on Monday, April 13, 2026 at 10:00 a.m. Eastern. Existing Home Sales data are provided by NAR solely for use as a reference. No part of this data may be reproduced, stored in a
retrieval system, transmitted or redistributed in any form or by any means, electronic, mechanical, photocopying, recording or otherwise, without NAR's prior written consent for those who are not
members of NAR. Members of the media who need copies of previous months' existing-home sales news releases can contact the NAR media communications team at 202-383-7515. ## Data\n\nCitation guidelines
for NAR research and statistics\n\nExpand All\n\nOverview Breakouts of Single-family, Condo and Co-op\n\nSingle-Family Existing-Home Sales and Prices Condo and Co-op Sales and Prices\n\nAverage (Mean)
Price\n\nHistorical Information\n\nQuestions Existing-Home Sales for April 2026 will be released on Monday, May 11, 2026 at 10:00 a.m. Eastern. NAR Media Communications issues a news release close to
mid-month with the latest existing-home sales figures. The releases include analysis and quotes by NAR's Chief Economist Lawrence Yun regarding the sales volume, prices, inventory and interest rates.
NAR Research Data Release Dates\n\n### Existing-Home Sales Housing Snapshot\n\ninfographic\n\nApril 13, 2026 March 2026 brought 3.98 million in sales, a median sales price of $408,800, and 4.1 months
of inventory.   ...    The Pending Home Sales Index is based on signed real estate contracts for existing single-family homes,"], "published_date": "2017-05-16T16:57:37.000", "score": null}]
```

## 💬 Response

The data is now clear. The NAR released the March 2026 existing home sales report on **April 13, 2026** (today/yesterday), and the headline number is **3.98 million SAAR** — which is **below 4.0 million**.

This is confirmed by multiple sources:
- NAR press release: "3.6% decrease in existing-home sales—seasonally adjusted annual rate of 3.98 million in March"
- FRED series EXHOSLUSM495S: latest value = 3,980,000 for March 2026
- Trading Economics, Haver Analytics, Eye on Housing all confirm 3.98 million

The question asks whether the **first published** March 2026 SAAR is at least 4.0 million. The first publication has now occurred (April 13, 2026), and the value is 3.98 million — below the 4.0 million threshold.

This question resolves **NO**.

Let me call reflection to finalize.
