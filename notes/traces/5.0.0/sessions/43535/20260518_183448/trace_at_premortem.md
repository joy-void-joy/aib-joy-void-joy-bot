# Reasoning Log: How many Nintendo Switch 2 units will Famitsu report sold in Japan during the week of May 18–24, 2026?

*Generated: 2026-05-18T18:46:38.403263+00:00*


## 💭 Thinking

Let me analyze this forecasting question about Nintendo Switch 2 sales in Japan during the week of May 18-24, 2026.

Key facts from the question:
1. Nintendo announced a ¥10,000 price increase on the Japan-only Switch 2 model, effective May 25, 2026
2. The week of May 18-24 is the FINAL full week before the price hike
3. Recent weekly sales data:
   - Week of March 30 – April 5: ~59,543 units
   - Week of April 13-19: ~44,280 units
   - Two-week period April 27 – May 10: 214,438 total (~93k and ~96k per week)
4. There's been a surge in pre-hike buying with reports of sell-outs

Now I'm looking at the broader sales trends and trying to understand how much demand might be pulled forward into this final week before the price increase takes effect.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43535
  ]
}
```

### 📋 Result

```
{"post_id": 43535, "title": "How many Nintendo Switch 2 units will Famitsu report sold in Japan during the week of May 18\u201324, 2026?", "type": "numeric", "url":
"https://www.metaculus.com/questions/43535", "background_info": "Famitsu, a Japanese gaming publication, releases weekly hardware sales data for the Japanese market, aggregating sales across all
hardware variants of a given platform. These figures are widely reposted in English by Gematsu and discussed on community forums such as Famiboards.\n\nOn May 8, 2026, Nintendo announced a
\u00a510,000 price increase on the Japan-only (Japanese-language only) Nintendo Switch 2 model, taking effect on May 25, 2026. The announcement triggered a surge in pre-hike buying, with reports of
sell-outs at major Japanese retailers.\n\nRecent Famitsu weekly hardware sales for Switch 2 in Japan:\n- Week of March 30 \u2013 April 5, 2026: ~59,543 units\n- Week of April 13\u201319, 2026: ~44,280
units\n- Two-week period April 27 \u2013 May 10, 2026 (covering Golden Week and the price-hike announcement): 214,438 units total (roughly ~93k and ~96k across the two weeks, per VGChartz/Famitsu
summaries)\n\nThe week of May 18\u201324, 2026 is the final full week before the price hike takes effect, and is widely expected to see elevated demand, although the size of any spike is constrained
by retail inventory and Nintendo's ability to replenish stock.\n\nFamitsu typically publishes its weekly hardware sales chart on the following Wednesday in Japan, with Gematsu reposting in English
within a day.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 4, \"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves
as the number of Nintendo Switch 2 hardware units (summed across all variants sold in Japan, including the Japan-only model) reported by Famitsu as having sold in Japan during the week of May 18, 2026
through May 24, 2026, as reposted in Gematsu's weekly \"Famitsu Sales\" article covering that week. Report the value as a count of units (e.g., a reported value of 125,000 units resolves as
125000).\n\nThe primary source is Gematsu's Famitsu Sales tag page: https://www.gematsu.com/tag/famitsu-sales \u2014 specifically the article covering the 5/18/26 \u2013 5/24/26 week. If Gematsu has
not published the relevant article by May 31, 2026, the figure may be sourced from any other outlet that explicitly attributes the number to Famitsu's official weekly hardware chart for that week
(e.g., Famiboards, Nintendo Life, or [credible sources](https://www.metaculus.com/faq/#definitions)).", "fine_print": "If Famitsu reports separate sub-totals for individual Switch 2 SKUs/variants, the
resolution value is the sum across all Switch 2 variants. If no Famitsu figure for the May 18\u201324, 2026 week is available from any credible source by May 31, 2026, the question resolves
Ambiguous.", "num_forecasters": 1, "community_prediction": null, "lower_bound": 0.0, "upper_bound": 250000.0}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Nintendo Switch 2 Japan weekly sales Famitsu May 2026 price hike surge",
      "ttl": "6h"
    },
    {
      "query": "Nintendo Switch 2 Japan inventory stock availability May 2026 retailers",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Nintendo Switch 2 Japan weekly sales Famitsu May 2026 price hike surge", "entry": {"slug": "nintendo-switch-2-japan-weekly-sales-famitsu-may-2-58d3879d", "query": "Nintendo
Switch 2 Japan weekly sales Famitsu May 2026 price hike surge", "answer": "## Research Report: Nintendo Switch 2 Japan Weekly Sales (Famitsu) \u2014 May 2026 & Price Hike Surge\n\n### 1. Weekly
Hardware Sales in Japan (Famitsu-Tracked)\n\nThe following Famitsu-tracked weekly hardware sales data for Nintendo Switch 2 in Japan has been compiled from Gematsu and Famitsu:\n\n| Week Period |
Weekly Units | Cumulative (Lifetime) |\n|---|---|---|\n| Mar 30 \u2013 Apr 5, 2026 | **59,543** | **5,011,059** |\n| Apr 6 \u2013 Apr 12, 2026 | **52,058** | **5,063,117** |\n| Apr 13 \u2013 Apr 19,
2026 | **44,280** | **5,107,397** |\n| Apr 20 \u2013 Apr 26, 2026 | **45,825** | **5,153,222** |\n| Apr 27 \u2013 May 10, 2026 (2-week combined) | **214,438** | **5,367,660** |\n\nThe April
27\u2013May 10 figure is a combined two-week report covering Japan's **Golden Week** holiday period. This averages ~107,000 units/week \u2014 a **4\u20135x increase** over the ~45,000\u201352,000
weekly pace in earlier April.\n\n**Japan Cumulative Total**: As of May 10, 2026, the Switch 2 has sold **5,367,660 units** in Japan.\n\n---\n\n### 2. Price Hike Details\n\nNintendo announced sweeping
price increases, citing **\"changes in market conditions\"** and the **\"global business outlook\"** (widely interpreted as tariff/cost pressures):\n\n**Japan (effective May 25, 2026):**\n- **Switch 2
(Japan-only model)**: **+20.0% increase** (~+10,000 yen, from ~\u00a549,980)\n- The region-free Switch 2 model reportedly unchanged in Japan\n- All original Switch models in Japan also affected\n-
Nintendo Switch Online pricing increased effective **July 1, 2026**\n\n**Western Markets (effective September 1, 2026):**\n- **US**: +$50 increase (~11.1%)\n- **EU**: +\u20ac30 increase (~6.4%)\n-
**UK**: Not affected at time of announcement\n\n---\n\n### 3. Pre-Price-Hike Surge Analysis\n\nThe Japan price hike takes effect **May 25, 2026** \u2014 only ~2 weeks after the latest available
Famitsu data (May 10). The Golden Week period (Apr 27\u2013May 10) already showed a massive **214,438-unit** two-week surge. A further pre-price-hike rush-buy is anticipated in the **May 11\u201324
window**, but that Famitsu data has not yet been published. The next weekly report will be the key indicator.\n\n---\n\n### 4. Global Context\n\nPer Nintendo's official financial results (~May
2026):\n- **Switch 2 global lifetime sales**: **19.86 million units** (as of ~March 31, 2026)\n- This surpassed Nintendo's revised forecast of 19 million\n- Already exceeded Wii U's entire lifetime
sales (13.56 million)\n- **FY2027 global forecast**: Lowered to **16.5 million units**, reflecting anticipated price increase impact\n- **Net sales**: Up 98.6% at \u00a52,313.0 billion\n- **Operating
profit**: Up 27.5% at \u00a5360.1 billion\n\n---\n\n### 5. Competitive Context (Apr 27 \u2013 May 10, Japan)\n\n| Platform | Two-Week Units | Cumulative |\n|---|---|---|\n| Switch 2 | 214,438 |
5,367,660 |\n| Switch OLED | 16,850 | 9,571,489 |\n| PS5 Digital | 16,539 | 1,283,342 |\n| PS5 Pro | 5,248 | 355,220 |\n| Xbox Series (all) | 513 | ~698,834 |\n\nSwitch 2 outsells the entire PS5
family combined by roughly **9:1** in Japan.\n\n---\n\n### 6. Software Performance (Famitsu, May 4\u201310, Physical Only)\n\nTop Switch 2 titles in Japan:\n- **Mario Kart World**: 10,941 weekly /
**2,925,858 cumulative** (approaching 3M physical)\n- **Pok\u00e9mon Pokopia**: 28,312 weekly / **978,706 cumulative** (approaching 1M)\n- **Pok\u00e9mon Legends: Z-A SW2 Ed.**: 2,283 weekly /
**1,120,703 cumulative** (past 1M)\n- **Kirby Air Riders**: 3,157 weekly / **527,490 cumulative**\n- **Donkey Kong Bananza**: 1,717 weekly / **498,585 cumulative**\n\n---", "sources": [{"url":
"https://www.gematsu.com/tag/famitsu-sales", "title": "Famitsu Sales Tag - Weekly Hardware and Software Charts", "domain": "gematsu.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Famitsu-
tracked weekly hardware sales data for Japan, including Switch 2 cumulative and weekly unit figures through May 10, 2026."}, {"url": "https://www.famitsu.com/ranking/game-sales", "title": "Famitsu
Game Sales Rankings", "domain": "famitsu.com", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Top 30 software sales chart with exact unit counts for Switch 2 titles in Japan, physical sales
only."}, {"url": "https://www.nintendolife.com/news", "title": "Nintendo Life News - Switch 2 Price Hike and Global Sales Milestone", "domain": "nintendolife.com", "accessed_at":
"2026-05-18T00:00:00Z", "snippet": "Coverage of Nintendo's price hike announcement (20% Japan increase effective May 25, 2026) and global sales milestone of 19.86 million units."}, {"url":
"https://www.eurogamer.net/nintendo", "title": "Eurogamer Nintendo Coverage", "domain": "eurogamer.net", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Confirmation of Switch 2 price hike details
and Nintendo financial results."}], "key_facts": ["Nintendo Switch 2 has sold 5,367,660 cumulative units in Japan as of May 10, 2026 (Famitsu-tracked).", "Golden Week period (Apr 27\u2013May 10) saw a
combined 214,438 units sold \u2014 roughly 4\u20135x the normal weekly pace of ~45,000\u201352,000 units.", "Nintendo announced a 20% price hike for the Japan-only Switch 2 model, effective May 25,
2026 (~+\u00a510,000 from ~\u00a549,980).", "A pre-price-hike buying surge is expected in the May 11\u201324 window but Famitsu data for that period has not yet been published.", "US price hike of
+$50 and EU price hike of +\u20ac30 are scheduled for September 1, 2026.", "Switch 2 global lifetime sales reached 19.86 million units as of ~March 31, 2026, surpassing Nintendo's revised 19M
forecast.", "Nintendo lowered its FY2027 global forecast to 16.5 million Switch 2 units, reflecting anticipated price hike impact.", "Switch 2 outsells the entire PS5 family combined by roughly 9:1 in
Japan during the Golden Week period.", "Mario Kart World has reached nearly 3 million cumulative physical sales in Japan.", "Nintendo cited 'changes in market conditions' and 'global business outlook'
as reasons for the price increase.", "Switch 2 has already surpassed the Wii U's entire lifetime sales (13.56 million) globally in under 10 months.", "Nintendo Switch Online pricing in Japan will
increase effective July 1, 2026."], "data_points": [{"metric": "Switch 2 Japan cumulative sales (Famitsu-tracked)", "value": 5367660.0, "unit": "units", "as_of": "2026-05-10", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 Japan weekly sales (Mar 30\u2013Apr 5)", "value": 59543.0, "unit": "units", "as_of": "2026-04-05", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 Japan weekly sales (Apr 6\u201312)", "value": 52058.0, "unit": "units", "as_of": "2026-04-12", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 Japan weekly sales (Apr 13\u201319)", "value": 44280.0, "unit": "units", "as_of": "2026-04-19", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 Japan weekly sales (Apr 20\u201326)", "value": 45825.0, "unit": "units", "as_of": "2026-04-26", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 Japan 2-week sales Golden Week (Apr 27\u2013May 10)", "value": 214438.0, "unit": "units", "as_of": "2026-05-10", "source_url":
"https://www.gematsu.com/tag/famitsu-sales"}, {"metric": "Switch 2 global lifetime sales", "value": 19860000.0, "unit": "units", "as_of": "2026-03-31", "source_url":
"https://www.nintendolife.com/news"}, {"metric": "Japan price hike percentage (Japan-only model)", "value": 20.0, "unit": "percent", "as_of": "2026-05-25", "source_url":
"https://www.nintendolife.com/news"}, {"metric": "US price hike amount", "value": 50.0, "unit": "USD", "as_of": "2026-09-01", "source_url": "https://www.nintendolife.com/news"}, {"metric": "EU price
hike amount", "value": 30.0, "unit": "EUR", "as_of": "2026-09-01", "source_url": "https://www.nintendolife.com/news"}, {"metric": "Nintendo FY2027 Switch 2 global sales forecast", "value": 16500000.0,
"unit": "units", "as_of": "2026-05-18", "source_url": "https://www.nintendolife.com/news"}, {"metric": "Nintendo net sales", "value": 2313000000000.0, "unit": "JPY", "as_of": "2026-03-31",
"source_url": "https://www.nintendolife.com/news"}, {"metric": "Nintendo operating profit", "value": 360100000000.0, "unit": "JPY", "as_of": "2026-03-31", "source_url":
"https://www.nintendolife.com/news"}, {"metric": "Mario Kart World Japan cumulative physical sales", "value": 2925858.0, "unit": "units", "as_of": "2026-05-10", "source_url":
"https://www.famitsu.com/ranking/game-sales"}, {"metric": "Pokemon Pokopia Japan cumulative physical sales", "value": 978706.0, "unit": "units", "as_of": "2026-05-10", "source_url":
"https://www.famitsu.com/ranking/game-sales"}, {"metric": "Pokemon Legends Z-A SW2 Ed. Japan cumulative physical sales", "value": 1120703.0, "unit": "units", "as_of": "2026-05-10", "source_url":
"https://www.famitsu.com/ranking/game-sales"}], "created_at": "2026-05-18T18:39:37.130140Z", "updated_at": "2026-05-18T18:39:37.130140Z", "stale_after": "2026-05-19T00:39:37.130140Z", "state":
"fresh", "revision_history": [], "session_id": "b609532e-57ea-4ca0-bf62-e56783d1d040", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Nintendo Switch 2 Japan inventory stock availability
May 2026 retailers", "entry": {"slug": "nintendo-switch-2-japan-inventory-stock-availabili-1b86a5c3", "query": "Nintendo Switch 2 Japan inventory stock availability May 2026 retailers", "answer":
"Unfortunately, all web search and fetch tools are currently unavailable in this environment. However, I can provide a research synthesis based on what is known from my training data and publicly
established facts leading up to this period. Let me compile what's available.\n\n---\n\n# Nintendo Switch 2 \u2014 Japan Inventory & Stock Availability (May 2026)\n\n## Background & Launch
Timeline\n\n- **January 16, 2025**: Nintendo officially revealed the Switch 2 via a teaser trailer, confirming backward compatibility and a larger screen form factor.\n- **April 2, 2025**: Nintendo
held a dedicated Nintendo Direct for Switch 2, revealing full specifications, launch titles (including *Mario Kart World*), and the price.\n- **June 5, 2025**: The Nintendo Switch 2 launched
worldwide, including in Japan, at a price of \u00a549,980 (approx. $330 USD at launch).\n\n## Japan Stock Situation at Launch (June\u2013July 2025)\n\n- As with previous Nintendo hardware launches
(Wii, Switch 1), **initial demand far exceeded supply** in Japan.\n- Major Japanese retailers (Yodobashi Camera, Bic Camera, Amazon Japan, GEO, Joshin, Nojima, etc.) adopted a **lottery/raffle system
(\u62bd\u9078\u8ca9\u58f2)** rather than first-come-first-served sales, mirroring the approach used during the PS5 launch.\n- Nintendo reportedly **increased production orders** with assembly partners
(primarily Foxconn/Sharp) ahead of launch, but global semiconductor and component constraints still limited initial shipments.\n- Scalper/resale prices on Mercari and Yahoo Auctions Japan were
reported significantly above MSRP in the initial weeks.\n\n## Current Trajectory (Approaching May 2026 \u2014 ~11 Months Post-Launch)\n\nBased on historical patterns with Nintendo hardware in
Japan:\n\n- **Gradual improvement in supply**: By 6\u201312 months post-launch, Nintendo hardware typically transitions from severe scarcity to intermittent availability. The original Switch took
roughly 12\u201318 months to achieve consistent walk-in availability in Japan.\n- **Lottery systems**: Some major retailers likely continued lottery-based sales for several months post-launch, though
these typically phase out as supply stabilizes.\n- **Nintendo's production ramp**: Nintendo President Shuntaro Furukawa stated in 2025 that the company aimed to avoid the prolonged shortages that
plagued the original Switch and Wii launches. Nintendo reportedly targeted **15\u201320 million units shipped in the first fiscal year** (April 2025\u2013March 2026).\n- **Golden Week effect (late
April\u2013early May 2026)**: This major Japanese holiday period historically drives a spike in gaming hardware demand, potentially causing temporary restocking pressure.\n\n## Key Retailers &
Channels in Japan\n\n| Retailer | Type | Typical Availability Method |\n|---|---|---|\n| Amazon Japan | Online | Periodic restocks, invitation-based early on |\n| Yodobashi Camera | Electronics chain
| Lottery (\u62bd\u9078), then walk-in |\n| Bic Camera | Electronics chain | Lottery, then walk-in |\n| GEO | Game specialty | Lottery, then walk-in |\n| Joshin | Electronics chain | Lottery/online
|\n| Nintendo Store (Tokyo/Osaka) | Official | Lottery, limited walk-in |\n| My Nintendo Store (online) | Official online | Queue/lottery system |\n\n## Caveats & Limitations\n\n> **Important**: My
training data has a cutoff, and I was unable to access live web sources for this query. The specific May 2026 on-the-ground stock situation \u2014 whether Switch 2 units are freely available on
shelves, still lottery-only at certain retailers, or fully normalized \u2014 **cannot be confirmed with real-time data**. The above represents the most likely trajectory based on Nintendo's historical
patterns, stated production goals, and the known launch timeline.\n\n---", "sources": [{"url": "https://www.nintendo.co.jp/switch2/", "title": "Nintendo Switch 2 Official Page (Japan)", "domain":
"nintendo.co.jp", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Official Nintendo Japan page for Switch 2 \u2014 unable to fetch live content due to tool restrictions"}, {"url":
"https://www.nintendo.co.jp/ir/", "title": "Nintendo Investor Relations", "domain": "nintendo.co.jp", "accessed_at": "2026-05-18T00:00:00Z", "snippet": "Source for production targets and executive
statements \u2014 based on training data, not live fetch"}], "key_facts": ["Nintendo Switch 2 launched worldwide including Japan on June 5, 2025, at \u00a549,980 MSRP", "Japanese retailers adopted
lottery/raffle (\u62bd\u9078\u8ca9\u58f2) sales systems at launch due to demand exceeding supply", "Major retailers using lottery systems included Yodobashi Camera, Bic Camera, Amazon Japan, GEO,
Joshin, and Nintendo Store", "Nintendo targeted 15-20 million units shipped in the first fiscal year (April 2025-March 2026)", "Nintendo President Furukawa stated the company aimed to avoid prolonged
shortages seen with original Switch and Wii", "Scalper/resale prices on Mercari and Yahoo Auctions Japan exceeded MSRP in initial post-launch weeks", "Golden Week (late April-early May 2026) likely
created seasonal demand spike roughly 11 months post-launch", "Historical pattern: Nintendo hardware typically takes 12-18 months to achieve consistent walk-in availability in Japan", "CAVEAT: Live
web sources were unavailable; May 2026 real-time stock conditions could not be verified"], "data_points": [{"metric": "Nintendo Switch 2 Japan MSRP", "value": 49980.0, "unit": "JPY", "as_of":
"2025-06-05", "source_url": "https://www.nintendo.co.jp/switch2/"}, {"metric": "Nintendo Switch 2 first fiscal year shipment target", "value": 15000000.0, "unit": "units (low estimate)", "as_of":
"2025-04-02", "source_url": "https://www.nintendo.co.jp/ir/"}, {"metric": "Nintendo Switch 2 first fiscal year shipment target (high)", "value": 20000000.0, "unit": "units (high estimate)", "as_of":
"2025-04-02", "source_url": "https://www.nintendo.co.jp/ir/"}, {"metric": "Months since Japan launch as of May 2026", "value": 11.0, "unit": "months", "as_of": "2026-05-18", "source_url":
"https://www.nintendo.co.jp/switch2/"}], "created_at": "2026-05-18T18:36:38.769526Z", "updated_at": "2026-05-18T18:36:38.769526Z", "stale_after": "2026-05-19T00:36:38.769526Z", "state": "fresh",
"revision_history": [], "session_id": "ce91de07-1b31-49c0-a813-7acab8e9c23b", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

Now let me search for more specific data on the May 11-17 week and any additional context about the pre-price-hike rush.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Famitsu Switch 2 Japan sales May 11-17 2026 weekly"
}
```

### 📋 Result

```
{"query": "Famitsu Switch 2 Japan sales May 11-17 2026 weekly", "results": [{"title": "Famitsu sales (4/27/26 \u2013 5/10/26) \u2013 big numbers for Nintendo Switch 2", "url":
"https://nintendoeverything.com/famitsu-sales-4-27-26-5-10-26-big-numbers-for-nintendo-switch-2/", "snippet": "Famitsu sales (4/27/26 \u2013 5/10/26) \u2013 big numbers for Nintendo Switch 2\nThe
latest Japanese hardware sales from Famitsu are as follows:\nSwitch 2 \u2013 214,438\nSwitch OLED \u2013 16,580\nPS5 Digital Edition \u2013 16,539\nSwitch Lite \u2013 16,039\nSwitch \u2013 7,960\nPS5
Pro \u2013 5,248\nPS5 \u2013 1,973\nXbox Series X Digital Edition \u2013 352\nXbox Series S \u2013 97\nXbox Series X \u2013 64\nFor comparison\u2019s sake, here are the hardware numbers from last
week:\nSwitch 2 \u2013 45,825\nSwitch Lite \u2013 11,263\nSwitch OLED \u2013 10,796\nPS5 Digital Edition \u2013 6,361\nSw", "api_data": null, "hint": null}, {"title": "Famitsu Sales - Gematsu", "url":
"https://www.gematsu.com/tag/famitsu-sales", "snippet": "PS5SwitchSwitch 2Xbox Series4 days ago0Famitsu Sales: 4/27/26 \u2013 5/10/26 [Update 2]Famitsu has published its estimated physical game
software data for Japan for the two weeks \u2026\nPS5SwitchSwitch 2Xbox Series2 weeks ago0Famitsu Sales: 4/20/26 \u2013 4/26/26 [Update]Famitsu has published its estimated physical game software data
for Japan for the week of \u2026\nPS5SwitchSwitch 2Xbox Series3 weeks ago0Famitsu Sales: 4/13/26 \u2013 4/19/26 [Update]Famitsu has published its estimated physical game software data for Ja",
"api_data": null, "hint": null}, {"title": "[Japan] Famitsu sales for April 2026 (Top 5 Software, Publishers, Hardware) \u2013 Perfectly Nintendo", "url": "https://www.perfectly-nintendo.com/japan-
famitsu-sales-for-april-2026-top-5-software-publishers-hardware/", "snippet": "[Japan] Famitsu sales for April 2026 (Top 5 Software, Publishers, Hardware)\nHere\u2019s the latest sales report from
Famitsu, with Hardware and Software sales for April 2026 in Japan (March 30th to April 26th, so 4 weeks in total).\nFamitsu\nTop 5 Software\nTomodachi Life: Living the Dream is off to a great start
with over 740,000 units sold in just 10 days. Unsurprisingly, it was the best-selling game in April by a wide margin.\nTomodachi Life: Living the Dream sold significantly better than its predece",
"api_data": null, "hint": null}, {"title": "Famitsu sales (2/16/26 - 2/22/26)", "url": "https://nintendoeverything.com/famitsu-sales-2-16-26-2-22-26/", "snippet": "Famitsu sales (2/16/26 \u2013
2/22/26)\nThe latest Japanese hardware sales from Famitsu are as follows:\nSwitch 2 \u2013 63,313\nSwitch OLED \u2013 19,858\nSwitch Lite \u2013 8,079\nPS5 Digital Edition \u2013 5,641\nPS5 \u2013
2,776\nPS5 Pro \u2013 1,926\nXbox Series X \u2013 760\nXbox Series X Digital Edition \u2013 294\nXbox Series S \u2013 134\nSwitch \u2013 489\nPS4 \u2013 37\nFor comparison\u2019s sake, here are the
hardware numbers from last week:\nSwitch 2 \u2013 57,779\nSwitch OLED \u2013 20,226\nSwitch Lite \u2013 4,882\nSwitch \u2013 1,373\nPS5 Digital Edition \u2013 6,341\nPS5 \u2013 3,562\nPS5 Pr",
"api_data": null, "hint": null}, {"title": "Famitsu sales (4/13/26 - 4/19/26) - first week sales revealed for Tomodachi Life: Living the Dream, massive debut", "url":
"https://nintendoeverything.com/famitsu-sales-4-13-26-4-19-26-first-week-sales-revealed-for-tomodachi-life-living-the-dream-massive-debut/", "snippet": "Famitsu sales (4/13/26 \u2013 4/19/26) \u2013
first week sales revealed for Tomodachi Life: Living the Dream, massive debut\nThe latest Japanese hardware sales from Famitsu are as follows:\nSwitch 2 \u2013 44,280\nSwitch Lite \u2013
16,511\nSwitch OLED \u2013 10,472\nPS5 Digital Edition \u2013 5,501\nSwitch \u2013 4,513\nPS5 Pro \u2013 3,066\nPS5 \u2013 2,163\nXbox Series X \u2013 223\nXbox Series X Digital Edition \u2013
147\nXbox Series S \u2013 84\nFor comparison\u2019s sake, here are the hardware numbers from last week:\nSwitch 2 \u2013 52,058\nSwitch Lite \u2013 10,630\nSwitch O", "api_data": null, "hint": null},
{"title": "Famitsu Sales: 4/13/26 - 4/19/26 [Update] - Gematsu", "url": "https://www.gematsu.com/2026/04/famitsu-sales-4-13-26-4-19-26", "snippet": "Famitsu Sales: 4/13/26 \u2013 4/19/26
[Update]\nTomodachi Life: Living the Dream opens at 565,405 retail sales.![](https://www.gematsu.com/wp-content/uploads/2026/04/Famitsu-
Sales_04-23-26_Tomodachi-320x180.jpg)\n[Famitsu](https://www.famitsu.com/article/202604/72822) has published its estimated physical game software data for Japan for the week of April 13, 2026 to April
19, 2026.\n[Tomodachi Life: Living the Dream](https://www.gematsu.com/games/tomodachi-life-living-the-dream) for [Switch](https://www", "api_data": null, "hint": null}, {"title": "[Japan] Famitsu
sales for Week 18 + 19, 2026 (Apr. 27 \u2013 May 10)", "url": "https://www.perfectly-nintendo.com/japan-famitsu-sales-for-week-18-19-2026-apr-27-may-10/", "snippet": "[Japan] Famitsu sales for Week 18
+ 19, 2026 (Apr. 27 \u2013 May 10)\nHere\u2019s the latest sales reports from [Famitsu](https://www.perfectly-nintendo.com/tag/famitsu/) with Hardware and Software sales data for Week 18 and Week 19,
2026 in Japan!\nYou can find separate reports for Week 18 and Week 19 on these pages: [Week 18](https://www.perfectly-nintendo.com/japan-taiwan-s-korea-famitsu-media-create-oricon-sales-for-
week-18-2026-apr-27-may-03-top-30/) / [Week 19](https://www.perfectly-nintendo.com/japan", "api_data": null, "hint": null}, {"title": "Nintendo Everything", "url": "https://nintendoeverything.com/",
"snippet": "A new version 1.7 update has been announced for Star Trek: Voyager \u2013 Across the Unknown. On Nintendo Switch 2, it should be out in early June.\nVersion 1.7 is highlighted by the Delta
Flyer, completely free for all players. Also included is a brand-new questline with Tom Paris in Sector 7, construction mechanics, and a combat ally role that won\u2019t split your rewards.
That\u2019s along with new Delta Flyer-specific branches in several existing quests, including Old Friends, New Enemies, The Drone, and U", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Nintendo Switch 2 Japan price hike May 25 2026 rush buying sell out inventory"
}
```

### 📋 Result

```
{"query": "Nintendo Switch 2 Japan price hike May 25 2026 rush buying sell out inventory", "results": [{"title": "Nintendo to Raise Switch 2 Price by 10,000 Yen | Nippon.com", "url":
"https://www.nippon.com/en/news/yjj2026050800853/", "snippet": "Nintendo to Raise Switch 2 Price by 10,000 Yen\nNewsfrom Japan\n[Economy](https://www.nippon.com/en/articlelist.html?f=ncf-
category&s=Economy)\n- English\n- \u65e5\u672c\u8a9e\n- \u7b80\u4f53\u5b57\n- \u7e41\u9ad4\u5b57\n- Fran\u00e7ais\n- Espa\u00f1ol\n- \u0627\u0644\u0639\u0631\u0628\u064a\u0629\n-
\u0420\u0443\u0441\u0441\u043a\u0438\u0439\nKyoto, May 8 (Jiji Press)--Nintendo Co. said Friday that it will raise the suggested retail price of its Nintendo Switch 2 video game console in Japan by
10,000 yen to 59,980 yen on May 25.\nThe Japanese game giant cited soaring semiconductor memory prices as the reason for the markup. It w", "api_data": null, "hint": null}, {"title": "News Release :
May 8, 2026 \"Notice Regarding Price Revisions for Nintendo Products and Services\"", "url": "https://www.nintendo.co.jp/corporate/release/en/2026/260508.html", "snippet": "May 8, 2026\nTo Whom It May
Concern\nNintendo Co., Ltd.\nNintendo Co., Ltd. (HQ: Kyoto, Minami-ku, Japan; President and Representative Director: Shuntaro Furukawa, \u201cNintendo\u201d hereafter) hereby announces that it has
decided to revise the prices of the following products and services.\nIn light of changes in market conditions, and after considering the global business outlook, Nintendo will revise the
manufacturer\u2019s suggested retail prices (MSRP) of the Nintendo Switch 2 system and Nintendo Switch sys", "api_data": null, "hint": null}, {"title": "Nintendo Announces Sweeping Price Hikes For
Switch 2 | Nintendo Life", "url": "https://www.nintendolife.com/news/2026/05/nintendo-announces-sweeping-price-hikes-for-switch-2", "snippet": "Nintendo [has
announced](https://www.nintendo.co.jp/corporate/release/en/2026/260508.html) that the Switch 2 will be going up in price globally, with Nintendo Switch Online also receiving a price hike in
Japan.\nHardware price revisions are effective from 25th May 2026 in Japan and 1st September in Western markets. Nintendo states that the changes are due to \"changes in market conditions\" and the
\"global business outlook\".\n\"We sincerely apologize for the impact these price revisions may have on o", "api_data": null, "hint": null}, {"title": "Nintendo hikes Switch 2 prices and expects
console sales to decline as memory crunch bites", "url": "https://www.cnbc.com/2026/05/08/nintendo-switch-2-price-hike-sales-fall-memory-crunch.html", "snippet":
"[Nintendo](https://www.cnbc.com/quotes/7974.T-JP/) will hike the retail price of the Switch 2 after forecasting a decline in sales for its flagship console as the memory chip crunch hits the Japanese
gaming giant.\nThe company said on Friday it expects to sell 16.5 million units of the Switch 2 in its fiscal year ended Mar. 31, 2027. That is a decline from the 19.86 million units sold in the
fiscal year just ended.\nMeanwhile, the company's forecasts for the current year were far below analyst est", "api_data": null, "hint": null}, {"title": "Nintendo raises Switch price, forecasts lower
profits - Japan Today", "url": "https://japantoday.com/category/business/japanese-video-game-maker-nintendo-raises-switch-price-forecasts-lower-profits", "snippet": "Nintendo\u2019s annual profit
surged 52% in the last fiscal year, lifted by solid sales of its Switch 2 machines and software.\nThe Japanese video-game company behind the Super Mario and Pokemon franchises announced it was raising
prices, citing challenging business conditions.\nIt recorded a 424 billion yen ($2.7 billion) net profit for the fiscal year that ended in March, up from nearly 279 billion yen the year
before.\nAnnual sales rose 99% to 2.3 trillion yen ($15 billion) from 1.2 trillion yen a ye", "api_data": null, "hint": null}, {"title": "Nintendo Switch 2 Global Price Hike Confirmed: $499.99 in the
U.S., \u00a559,980 in Japan, \u20ac499.99 in Europe \u2014 Here's When It Hits and Why It's Happening", "url": "https://nintendoinquirer.com/nintendo-switch-2-global-price-hike-
september-2026-details/", "snippet": "![Nintendo Switch 2 Global Price Hike Confirmed](https://nintendoinquirer.com/wp-content/uploads/2026/05/Nintendo-Switch-2-Global-Price-Hike-
Confirmed.webp)\nNintendo has confirmed what many fans feared: the Nintendo Switch 2 is getting a global price increase. The announcement, embedded in the company\u2019s fiscal year earnings report on
May 8, 2026, means the console will soon cost more in every major market.\nThe hikes are staggered by region. Japan absorbs the blow first on May 25. The United Stat", "api_data": null, "hint": null},
{"title": "Japanese retailer limiting Switch 2 purchases after price increase announcement | GoNintendo", "url": "https://www.gonintendo.com/contents/60683-japanese-retailer-limiting-
switch-2-purchases-after-price-increase-announcement", "snippet": "[Japanese retailer limiting Switch 2 purchases after price increase announcement](https://gonintendo.com/contents/60683-japanese-
retailer-limiting-switch-2-purchases-after-price-increase-announcement)\nStock up if you can\nNintendo recently announced that the Switch 2 would be receiving a price increase later this year. In the
US, that will bring its price from $449.99 to $499.99, while in Japan it will go from 49,980 yen to 59,980 yen. That new pricing is scheduled to go into effect shortly in Ja", "api_data": null,
"hint": null}, {"title": "Nintendo announces Switch 2 price increase, going into effect worldwide", "url": "https://nintendoeverything.com/nintendo-announces-switch-2-price-increase-going-into-effect-
worldwide/", "snippet": "Nintendo announces Switch 2 price increase, going into effect worldwide\nNintendo is increasing the price of Switch 2 worldwide, the company has announced.\nIn the U.S. and
Canada, the system is going up by $50. Europe will essentially see the console rise by \u20ac30. Over in Japan, Nintendo Switch 2 will increase by 10,000 yen, and there\u2019ll be increases for Switch
1 there as well.\nThe dates for the Nintendo Switch 2 price increase vary by region. In Japan, this is happening on May 26. For pretty much", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Japan console price hike pre-announcement sales spike historical precedent"
}
```

### 📋 Result

```
{"query": "Japan console price hike pre-announcement sales spike historical precedent", "results": [{"title": "Switch 2 price increase in Japan causes hysteria, as stores restrict console sales -
Notebookcheck News", "url": "https://www.notebookcheck.net/Switch-2-price-increase-in-Japan-causes-hysteria-as-stores-restrict-console-sales.1293250.0.html", "snippet": "The Nintendo Switch 2 price
hike in Japan has produced a surge in console sales. Reminiscent of its launch, jam-packed retailers are again waging war against scalpers. The changes take effect much sooner than in other regions,
with buyers suffering a higher percentage increase.\nWhile the Switch 2 price increase affects gamers worldwide, Japanese buyers are among the most impacted. With an MSRP rising by a higher
percentage, the news has sparked mass panic at retailers. Stores are now imposing re", "api_data": null, "hint": null}, {"title": "Nintendo hikes Switch 2 prices and expects console sales to decline
as memory crunch bites", "url": "https://www.cnbc.com/2026/05/08/nintendo-switch-2-price-hike-sales-fall-memory-crunch.html", "snippet": "[Nintendo](https://www.cnbc.com/quotes/7974.T-JP/) will hike
the retail price of the Switch 2 after forecasting a decline in sales for its flagship console as the memory chip crunch hits the Japanese gaming giant.\nThe company said on Friday it expects to sell
16.5 million units of the Switch 2 in its fiscal year ended Mar. 31, 2027. That is a decline from the 19.86 million units sold in the fiscal year just ended.\nMeanwhile, the company's forecasts for
the current year were far below analyst est", "api_data": null, "hint": null}, {"title": "US PlayStation 5 Sales Spike Following Global Price Hike News", "url": "https://attractmo.de/gaming-
business/ps5-sales-skyrocket-in-us-after-price-hike-announcement", "snippet": "The United States saw a dramatic increase in PlayStation 5 sales last week, a surge directly following Sony's
announcement of a price hike for the console in several major international markets. This spike in both unit sales and revenue suggests consumers acted quickly on the news, possibly fearing similar
price adjustments in the U.S. market.\nSony attributed the price increase to challenging global economic conditions, including high inflation rates and adverse currency trends. While the United",
"api_data": null, "hint": null}, {"title": "News Release : May 8, 2026 \"Notice Regarding Price Revisions for Nintendo Products and Services\"", "url":
"https://www.nintendo.co.jp/corporate/release/en/2026/260508.html", "snippet": "May 8, 2026\nTo Whom It May Concern\nNintendo Co., Ltd.\nNintendo Co., Ltd. (HQ: Kyoto, Minami-ku, Japan; President and
Representative Director: Shuntaro Furukawa, \u201cNintendo\u201d hereafter) hereby announces that it has decided to revise the prices of the following products and services.\nIn light of changes in
market conditions, and after considering the global business outlook, Nintendo will revise the manufacturer\u2019s suggested retail prices (MSRP) of the Nintendo Switch 2 system and Nintendo Switch
sys", "api_data": null, "hint": null}, {"title": "Nintendo's Stock Price Has Plummeted Following Switch 2 Price Hike Announcement", "url": "https://www.thegamer.com/nintendo-stock-share-price-drops-
switch-2-increase/", "snippet": "Nintendo finally caved last week and confirmed that, starting this month in Japan and in September everywhere else, [the Switch 2's price is going
up](https://www.thegamer.com/nintendo-switch-2-price-increase/). The aftermath of that announcement has seen Nintendo's stock price fall 12 percent over the weekend, leaving it at its lowest point
since the end of 2023.\nNintendo's Stock Price Hits A Three-Year Low\nNintendo confirmed on Friday that the Switch 2 will cost $50 more in the US starting fro", "api_data": null, "hint": null},
{"title": "Xbox Series X Sales in Japan Increased Considerably Following PlayStation 5 Price Hike Announcement", "url": "https://wccftech.com/xbox-series-x-sales-increase-japan/", "snippet": "The Xbox
Series X sales have increased significantly in Japan following the announcement of a [PlayStation 5 price increase](https://wccftech.com/playstation-5-gets-price-rise-in-japan-increasing-by-90/) which
will go into effect next week.\nAs reported by [Automaton](https://automaton-media.com/en/news/ps5-price-increase-in-japan-sends-xbox-consoles-soaring-up-sales-charts/), on Yodobashi, one of Japan's
biggest retailers, the console reached number 8 in the games and consoles charts this mornin", "api_data": null, "hint": null}, {"title": "Nintendo to Raise Switch 2 Price by 10,000 Yen | Nippon.com",
"url": "https://www.nippon.com/en/news/yjj2026050800853/", "snippet": "Nintendo to Raise Switch 2 Price by 10,000 Yen\nNewsfrom Japan\n[Economy](https://www.nippon.com/en/articlelist.html?f=ncf-
category&s=Economy)\n- English\n- \u65e5\u672c\u8a9e\n- \u7b80\u4f53\u5b57\n- \u7e41\u9ad4\u5b57\n- Fran\u00e7ais\n- Espa\u00f1ol\n- \u0627\u0644\u0639\u0631\u0628\u064a\u0629\n-
\u0420\u0443\u0441\u0441\u043a\u0438\u0439\nKyoto, May 8 (Jiji Press)--Nintendo Co. said Friday that it will raise the suggested retail price of its Nintendo Switch 2 video game console in Japan by
10,000 yen to 59,980 yen on May 25.\nThe Japanese game giant cited soaring semiconductor memory prices as the reason for the markup. It w", "api_data": null, "hint": null}, {"title": "Hardware -
Sales-Age - Platform - PS5 Price increase in Japan has made Xbox Series console sales shot up | NeoGAF", "url": "https://www.neogaf.com/threads/ps5-price-increase-in-japan-has-made-xbox-series-
console-sales-shot-up.1674393/", "snippet": null, "api_data": null, "hint": null}, {"title": "Nintendo Switch 2 Is Harder To Get In Japan Ahead Of May 25 Price Hike", "url":
"https://www.thegamer.com/switch-2-nintendo-japan-price-hike-retailers/", "snippet": "We found out just the other day that the [Nintendo Switch 2](http://thegamer.com/tag/nintendo-switch-2/) is going
up in price worldwide soon. How soon? For most places, not until September 1, which gives buyers plenty of time to lock in on the current price point instead. For native Japan, however, the change is
effective May 25. That's rough.\nNow, in the final weeks of the launch price tag, Japanese retailers are gearing up. Many face long lines as consumers flock to purchase a console sure to ",
"api_data": null, "hint": null}]}
```

## 💬 Response

Let me get more details on the specific inventory situation and the May 11-17 data.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.notebookcheck.net/Switch-2-price-increase-in-Japan-causes-hysteria-as-stores-restrict-console-sales.1293250.0.html",
  "prompt": "What specific details are given about the surge in Switch 2 sales in Japan before the price hike? Any sales numbers, inventory details, retailer restrictions?"
}
```

### 📋 Result

```
{"url": "https://www.notebookcheck.net/Switch-2-price-increase-in-Japan-causes-hysteria-as-stores-restrict-console-sales.1293250.0.html", "content": "Based on the content provided, here are the
specific details about the surge in Switch 2 sales in Japan:\n\n**Retailer Restrictions:**\n- Bic Camera now restricts purchases to only customers with a store-issued credit card\n- This strategy is
similar to what retailers employed at the Switch 2's original launch\n- Stores like Yodobashi Camera and competitors are experiencing \"huge crowds\"\n- Retailers are described as \"jam-packed\" and
\"waging war against scalpers\"\n\n**Sales Context:**\n- The surge is described as \"reminiscent of its launch\"\n- The Switch 2 has enjoyed \"faster adoption in Japan than in the U.S.\" (accounting
for population differences)\n- The article notes the system \"may experience a drop-off in sales after May 25th\" (the price increase date)\n\n**No specific sales numbers or inventory details are
provided** in the content. The article describes the situation qualitatively (panic, chaos, mass crowds) but does not include actual sales figures, unit counts, or stock levels.\n\nRelevant links:\n-
No additional links are provided in the extracted content beyond the main article URL already referenced.", "title": "Switch 2 price increase in Japan causes hysteria, as stores restrict console
sales"}
```

```json
{
  "url": "https://www.thegamer.com/switch-2-nintendo-japan-price-hike-retailers/",
  "prompt": "What specific details about Switch 2 availability, stock limitations, retailer restrictions, and sales surge in Japan before the May 25 price hike?"
}
```

### 📋 Result

```
{"url": "https://www.thegamer.com/switch-2-nintendo-japan-price-hike-retailers/", "content": "Based on the content, here are the specific details about Switch 2 in Japan before the May 25 price
hike:\n\n**Price Change:**\n- Current price: ~$319 USD equivalent (Japanese domestic units)\n- New price (effective May 25): $382 USD equivalent\n- Japan's price increase takes effect much sooner than
other regions (September 1)\n\n**Retailer Restrictions:**\n- **Bic Camera** (major retail chain): Now restricting Switch 2 sales to customers who possess a Bic Camera-branded credit card\n- This
tactic mirrors what **Yodobashi** (rival chain) did during PS5 shortages, limiting sales to Yodobashi credit card holders\n\n**Sales Surge:**\n- Many retailers facing long lines as consumers rush to
buy before the price increase\n- Consumers seeking to lock in the lower price before May 25 deadline\n\n**Availability Notes:**\n- Japanese domestic units are region-locked to Japanese-language
functionality only (to prevent overseas sales)\n- The article questions how supply will hold and whether demand will decrease after the price hike\n\nThe content doesn't specify exact stock
quantities, how many retailers are participating, or specific data on sales volumes.\n\n**Relevant links:**\n- [Nintendo Switch 2 tag page](http://thegamer.com/tag/nintendo-switch-2/)\n- [Serkan
Toto's tweet about retail tactics](https://x.com/serkantoto/status/2053000223413395709?s=20)", "title": "Some Japanese Retailers Are Now Heavily Restricting Nintendo Switch 2 Purchases"}
```

```json
{
  "query": "Famitsu sales May 11-17 2026 Switch 2 hardware Japan Gematsu"
}
```

### 📋 Result

```
{"query": "Famitsu sales May 11-17 2026 Switch 2 hardware Japan Gematsu", "results": [{"title": "Famitsu Sales - Gematsu", "url": "https://www.gematsu.com/tag/famitsu-sales", "snippet":
"PS5SwitchSwitch 2Xbox Series4 days ago0Famitsu Sales: 4/27/26 \u2013 5/10/26 [Update 2]Famitsu has published its estimated physical game software data for Japan for the two weeks
\u2026\nPS5SwitchSwitch 2Xbox Series2 weeks ago0Famitsu Sales: 4/20/26 \u2013 4/26/26 [Update]Famitsu has published its estimated physical game software data for Japan for the week of
\u2026\nPS5SwitchSwitch 2Xbox Series3 weeks ago0Famitsu Sales: 4/13/26 \u2013 4/19/26 [Update]Famitsu has published its estimated physical game software data for Ja", "api_data": null, "hint": null},
{"title": "Famitsu Sales: 3/2/26 - 3/8/26 [Update] - Gematsu", "url": "https://www.gematsu.com/2026/03/famitsu-sales-3-2-26-3-8-26", "snippet": "Famitsu Sales: 3/2/26 \u2013 3/8/26 [Update]\nPokemon
Pokopia sells 541,371 retail copies in first week.![](https://www.gematsu.com/wp-content/uploads/2026/03/Famitsu-
Sales_03-12-26_Pokopia-320x180.jpg)\n[Famitsu](https://www.famitsu.com/article/202603/68555) has published its estimated physical game software data for Japan for the week of March 2, 2026 to March 8,
2026.\n[Pokemon Pokopia](https://www.gematsu.com/games/pokemon-pokopia) for [Switch](https://www.gematsu.com/platforms/nintendo/switch) 2 wa", "api_data": null, "hint": null}, {"title": "Sales -
Gematsu", "url": "https://www.gematsu.com/tag/sales", "snippet": "PCXbox Series3 days ago0Subnautica 2 Early Access sales top two million in 12 hoursTotal sales for the Early Access version of
Subnautica 2 surpassed two million copies sold \u2026\nPS5SwitchSwitch 2Xbox Series4 days ago0Famitsu Sales: 4/27/26 \u2013 5/10/26 [Update 2]Famitsu has published its estimated physical game software
data for Japan for the two weeks \u2026\nPCPS5Xbox Series5 days ago0Silent Hill f shipments and digital sales top two millionTotal shipments and digital sales for Silent Hill f have surpass",
"api_data": null, "hint": null}, {"title": "Famitsu Sales (3/30/26 - 4/5/26) | Famiboards", "url": "https://famiboards.com/threads/famitsu-sales-3-30-26-4-5-26.17103/", "snippet": "- Pronouns\n-
He/Him\nHardware Sales\nwww.famitsu.com\nwww.gematsu.com\nSwitch 2 now reportedly sold over 5M units in Japan!\n- Switch2 - 59,543\uff085,011,059\uff09\n- PS5 Digital Edition -
12,141\uff081,248,515\uff09\n- Switch OLED - 7,468\uff089,526,329\uff09\n- Switch Lite - 4,807\uff086,903,964\uff09\n- Switch - 4,067\uff0820,271,045\uff09\n- PS5 Pro - 840\uff0831,548\uff09\n- PS5 -
558\uff085,910,474\uff09\n- Xbox Series X - 525\uff08325,952\uff09\n- Xbox Series X Digital Edition - 278\uff0829,362\uff09\n- Xbox Series S - 129\uff08341,622\uff09\n- [SW2] Pokemon Pokopia\u2013
45,484 (867,171)\n- [SW2] Mario Ka", "api_data": null, "hint": null}, {"title": "Famitsu sales (4/27/26 \u2013 5/10/26) \u2013 big numbers for Nintendo Switch 2", "url":
"https://nintendoeverything.com/famitsu-sales-4-27-26-5-10-26-big-numbers-for-nintendo-switch-2/", "snippet": "Famitsu sales (4/27/26 \u2013 5/10/26) \u2013 big numbers for Nintendo Switch 2\nThe
latest Japanese hardware sales from Famitsu are as follows:\nSwitch 2 \u2013 214,438\nSwitch OLED \u2013 16,580\nPS5 Digital Edition \u2013 16,539\nSwitch Lite \u2013 16,039\nSwitch \u2013 7,960\nPS5
Pro \u2013 5,248\nPS5 \u2013 1,973\nXbox Series X Digital Edition \u2013 352\nXbox Series S \u2013 97\nXbox Series X \u2013 64\nFor comparison\u2019s sake, here are the hardware numbers from last
week:\nSwitch 2 \u2013 45,825\nSwitch Lite \u2013 11,263\nSwitch OLED \u2013 10,796\nPS5 Digital Edition \u2013 6,361\nSw", "api_data": null, "hint": null}, {"title": "Sales-Age - Predictions: Switch
2 Launch Sales in Japan (Famitsu) for Hardware and Software. | NeoGAF", "url": "https://www.neogaf.com/threads/predictions-switch-2-launch-sales-in-japan-famitsu-for-hardware-and-software.1684898/",
"snippet": null, "api_data": null, "hint": null}, {"title": "Famitsu Sales (2/23/26\uff5e3/1/26) | Famiboards", "url": "https://famiboards.com/threads/famitsu-sales-2-23-26%EF%BD%9E3-1-26.16782/",
"snippet": "- Pronouns\n- He/Him\nHardware Sales\nFor Reference, this is the first week sale for RE8\n[PS4] Resident Evil Village: 111,171 (206,312)\n[PS5] Resident Evil Village: 38,713 (87,151)\nFor
RE7\n[PS4] Resident Evil 7: biohazard: 231,188 (343,382)\nSource\nFamitsu\nwww.famitsu.com\nGematsu\nwww.gematsu.com\nRE7/8 Famitsu Sales\nnichebarrier.com\n- Switch 2 \u2013 85,830 (4,579,815)\n-
Switch OLED Model \u2013 10,881 (9,483,819)\n- Switch Lite \u2013 10,880 (6,877,731)\n- PlayStation 5 Digital Edition \u2013 8,272 (1,198,192)\n- PlayStat", "api_data": null, "hint": null}, {"title":
"[Japan] Famitsu sales for April 2026 (Top 5 Software, Publishers, Hardware) \u2013 Perfectly Nintendo", "url": "https://www.perfectly-nintendo.com/japan-famitsu-sales-for-april-2026-top-5-software-
publishers-hardware/", "snippet": "[Japan] Famitsu sales for April 2026 (Top 5 Software, Publishers, Hardware)\nHere\u2019s the latest sales report from Famitsu, with Hardware and Software sales for
April 2026 in Japan (March 30th to April 26th, so 4 weeks in total).\nFamitsu\nTop 5 Software\nTomodachi Life: Living the Dream is off to a great start with over 740,000 units sold in just 10 days.
Unsurprisingly, it was the best-selling game in April by a wide margin.\nTomodachi Life: Living the Dream sold significantly better than its predece", "api_data": null, "hint": null}, {"title":
"Famitsu sales (2/16/26 - 2/22/26)", "url": "https://nintendoeverything.com/famitsu-sales-2-16-26-2-22-26/", "snippet": "Famitsu sales (2/16/26 \u2013 2/22/26)\nThe latest Japanese hardware sales from
Famitsu are as follows:\nSwitch 2 \u2013 63,313\nSwitch OLED \u2013 19,858\nSwitch Lite \u2013 8,079\nPS5 Digital Edition \u2013 5,641\nPS5 \u2013 2,776\nPS5 Pro \u2013 1,926\nXbox Series X \u2013
760\nXbox Series X Digital Edition \u2013 294\nXbox Series S \u2013 134\nSwitch \u2013 489\nPS4 \u2013 37\nFor comparison\u2019s sake, here are the hardware numbers from last week:\nSwitch 2 \u2013
57,779\nSwitch OLED \u2013 20,226\nSwitch Lite \u2013 4,882\nSwitch \u2013 1,373\nPS5 Digital Edition \u2013 6,341\nPS5 \u2013 3,562\nPS5 Pr", "api_data": null, "hint": null}, {"title": "Famitsu Sales
(11/10/25 - 11/16/25) | Famiboards", "url": "https://famiboards.com/threads/famitsu-sales-11-10-25-11-16-25.15687/", "snippet": "- Pronouns\n- He/Him\nHardware Sales\nSoftware
Sales\nSource\nFamitsu:\nGematsu:\n- Switch 2 \u2013 101,549 (2,743,805)\n- Switch OLED Model \u2013 10,772 (9,302,422)\n- Switch Lite \u2013 8,916 (6,726,165)\n- PlayStation 5 \u2013 3,309
(5,849,146)\n- Switch \u2013 3,048 (20,169,240)\n- PlayStation 5 Pro \u2013 2,057 (268,809)\n- PlayStation 5 Digital Edition \u2013 489 (1,024,795)\n- Xbox Series X Digital Edition \u2013 270
(23,879)\n- Xbox Series X \u2013 266 (323,565)\n- Xbox Series S \u2013 38 (340,067)\n- PlayStation 4 \u2013 15 (7,930,061)\nSoftware Sales\n- [NS", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me analyze the data I have so far and look for the May 11-17 week data, which would be the week just before the one we're forecasting. It seems like the latest Famitsu data published is for April 27 - May 10. The May 11-17 data hasn't been published yet (it's published on the following Wednesday, so it would come out around May 20-21).

Let me think about what I know:

**Weekly Switch 2 sales in Japan (Famitsu):**
- Feb 16-22: 63,313


- Feb 23-Mar 1: 85,830
- Mar 2-8: (need to check - Pokemon Pokopia launched)
- Mar 30-Apr 5: 59,543
- Apr 6-12: 52,058
- Apr 13-19: 44,280
- Apr 20-26: 45,825
- Apr 27-May 3: ~107,000 (part of 214,438 two-week total - Golden Week)
- May 4-10: ~107,000 (second half of two-week total)

The price hike announcement on May 8 likely boosted sales during that May 4-10 week, so I'm working with these figures to understand the baseline demand and how the announcement affected purchasing patterns.

The real surge should show up in the May 11-17 and May 18-24 weeks, especially since May 18-24 is the final full week before the May 25 price hike takes effect. Reports mention retailer restrictions, long lines, and sell-outs, which suggests supply constraints are limiting how much Nintendo can actually ship during this panic-buying period. The Golden Week boost combined with the price hike announcement already pushed weekly sales to around 107,000 units, but I need to see what happens in those final two weeks to understand the full magnitude of the pre-hike surge. to "last week" for the Apr 27-May 10 data shows "Switch 2 – 45,825" for the previous week (Apr 20-26). This confirms the combined two-week was 214,438.

For the individual weeks of the combined period, the question description says "roughly ~93k and ~96k across the two weeks, per VGChartz/Famitsu summaries." So:
- Apr 27-May 3: ~93,000 (Golden Week boost)
- May 4-10: ~96,000 (Golden Week + price hike announced May 8)

Wait, the question says the two weeks covered Golden Week AND the price-hike announcement. But the price hike was announced May 8, so only the last few days of the May 4-10 week would show the announcement effect. The May 4-10 week was already at ~96k largely due to Golden Week.

Now I'm thinking about May 18-24, the final full week before the May 25 price hike. There's clearly panic buying happening, but supply constraints are a real factor—retailers are limiting purchases and some have already sold out. The key question is whether the urgency of a 20% price increase and reports of buying hysteria will push sales above the ~96-107k Golden Week levels, or whether inventory shortages will cap the numbers despite the demand.

Looking at historical precedent with the PS5 price hike in Japan and comparing to Switch 2's launch performance, I need to find the actual launch week data to establish what kind of ceiling we're working with here.

Tracing through the cumulative sales figures from the data, I can see the baseline weekly sales have been hovering around 45,000-60,000 units before the price announcement surge. Now I'm trying to understand the supply constraints more carefully—Nintendo's global production gets distributed across regions, and Japan's allocation is what matters for this forecast. The May 18-24 week is critical because it's the last chance before the 20% price hike, so demand will be extremely high, but supply is the real limiting factor since retailers are already restricting purchases.

Given that Nintendo only had about 2.5 weeks to respond to the May 8 announcement by shifting supply to Japan, and considering that the May 11-17 week likely already saw a rush of pre-hike buying that depleted inventory, I'm working through different scenarios for what's actually available to sell in the May 18-24 window. The low scenario assumes retailers have already run through most of their stock and can't restock in time despite the strong demand.

For the base and high scenarios, I'm assuming Nintendo managed to get some additional shipments into Japan during that narrow window, with the difference being how aggressively they prioritized Japan over other markets. The very high scenario seems unrealistic given the physical constraints of getting product from China to Japan and into retail channels in just a couple of weeks.

Now I'm trying to figure out what the actual launch week looked like to calibrate these estimates, since the cumulative data through mid-November shows an average of about 119k per week over 23 weeks, but that's clearly dragged down by the launch week being much higher than the average. The May 18-24 week is critical since it's the last chance to buy at the old price, so demand will spike, but supply constraints and retailer sell-outs over the previous two weeks mean Nintendo might struggle to fulfill that surge. Given the tight timeline between announcement and price hike, the supply ramp-up probably can't keep pace with demand, so I'll need to model different scenarios to estimate the actual sales.

Running a Monte Carlo simulation...

## 💬 Response

The most recent Famitsu data is for April 27-May 10 (a combined 2-week report). The May 11-17 and May 18-24 data haven't been published yet. Let me search for any data on the May 11-17 week and look at historical precedents for pre-price-hike surges.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"Switch 2\" Japan weekly sales launch week June 2025 Famitsu first week"
}
```

### 📋 Result

```
{"query": "\"Switch 2\" Japan weekly sales launch week June 2025 Famitsu first week", "results": [{"title": "Sales-Age - Famitsu Sales: Week 23, 2025 (Jun 02 - Jun 08) Nintendo Switch 2 Launch |
NeoGAF", "url": "https://www.neogaf.com/threads/famitsu-sales-week-23-2025-jun-02-jun-08-nintendo-switch-2-launch.1685252/", "snippet": null, "api_data": null, "hint": null}, {"title": "Sales-Age -
Famitsu Sales: Week 23, 2025 (Jun 02 - Jun 08) Nintendo Switch 2 Launch | Page 2 | NeoGAF", "url": "https://www.neogaf.com/threads/famitsu-sales-week-23-2025-jun-02-jun-08-nintendo-
switch-2-launch.1685252/page-2", "snippet": null, "api_data": null, "hint": null}, {"title": "Famitsu Sales: 6/2/25 - 6/8/25 [Update] - Gematsu", "url": "https://www.gematsu.com/2025/06/famitsu-
sales-6-2-25-6-8-25", "snippet": "![](https://www.gematsu.com/wp-content/uploads/2025/06/Famitsu-Sales_06-12-25-320x180.jpg)\n[Famitsu](https://www.famitsu.com/article/202506/44654) has published its
estimated physical game software data for Japan for week of June 2, 2025 to June 8, 2025.\n[Mario Kart World](https://www.gematsu.com/games/mario-kart-world) for [Switch
2](https://www.gematsu.com/platforms/nintendo/switch-2) was the highest selling new release of the week, opening at 782,566 retail copies sold. [Rune Factory: Guardia", "api_data": null, "hint":
null}, {"title": "Famitsu sales (6/9/25 - 6/15/25) - Nintendo Switch 2's second week of sales are in", "url": "https://nintendoeverything.com/famitsu-sales-6-9-25-6-15-25-nintendo-switch-2s-second-
week-of-sales-are-in/", "snippet": "Famitsu sales (6/9/25 \u2013 6/15/25) \u2013 Nintendo Switch 2\u2019s second week of sales are in\nThe latest Japanese hardware sales from Famitsu are as
follows:\nSwitch 2 \u2013 153,205\nPS5 \u2013 9,612\nSwitch Lite \u2013 5,485\nSwitch OLED \u2013 5,447\nPS5 Pro \u2013 3,125\nSwitch \u2013 2,387\nPS5 Digital Edition \u2013 1,392\nXbox Series S
\u2013 125\nXbox Series X \u2013 102\nXbox Series X Digital Edition \u2013 34\nPS4 \u2013 22\nFor comparison\u2019s sake, here are the hardware numbers from last week:\nSwitch 2 \u2013 947,931\nPS5
\u2013 14,535\nSwitch OLED \u2013 8,040\nSwitch Lite \u2013 6,08", "api_data": null, "hint": null}, {"title": "Famitsu Sales: Week 23, 2025 (Jun 02 - Jun 08) - Switch 2 launch", "url":
"https://gamrconnect.vgchartz.com/thread/249354/famitsu-sales-week-23-2025-jun-02-jun-08-switch-2-launch/3/", "snippet": "[xl-klaudkil](https://gamrconnect.vgchartz.com/profile/106383/xl-klaudkil/)on
12 June 2025\nBut but consoles are dead!\nDead i tell you\nAnd just like that Switch 2 is ahead of every console YTD.\nSignature goes here!\nAre these sales gonna be included in VGCHartz's Japan June
sales numbers article ? @ |\nWithout any information from Nintendo we have no way of knowing how well it sold at My Nintendo Store. However, with Circana (NPD) data that will give us US numbers and
what other data we have should", "api_data": null, "hint": null}, {"title": "Sales-Age - Predictions: Switch 2 Launch Sales in Japan (Famitsu) for Hardware and Software. | NeoGAF", "url":
"https://www.neogaf.com/threads/predictions-switch-2-launch-sales-in-japan-famitsu-for-hardware-and-software.1684898/", "snippet": null, "api_data": null, "hint": null}, {"title": "Famitsu Sales:
Nintendo Switch 2 Is Japan's Fastest Selling Console Ever | GameLuster", "url": "https://gameluster.com/famitsu-sales-nintendo-switch-2-is-japans-fastest-selling-console-ever/", "snippet": "Every
Thursday we share the weekly Famitsu sales charts, which tracks physical boxed game sales and hardware sales in Japan. This week\u2019s [chart covers June 2 \u2013
8](https://www.famitsu.com/article/202506/44654), as the long-anticipated Nintendo Switch 2 finally hit the market in an explosive debut week. As many anticipated, the Switch 2 has obliterated the
record for fastest selling console in Japan previously held by the PlayStation 2\u2019s launch week, as the Switch 2 sold over 940,000 consoles in i", "api_data": null, "hint": null}, {"title":
"Sales-Age - Famitsu Sales: Week 25, 2025 (Jun 16 - Jun 22) | NeoGAF", "url": "https://www.neogaf.com/threads/famitsu-sales-week-25-2025-jun-16-jun-22.1685736/", "snippet": null, "api_data": null,
"hint": null}, {"title": "Famitsu sales (6/16/25 \u2013 6/22/25) \u2013 Nintendo Switch 2 still dominating in Japan", "url": "https://nintendoeverything.com/famitsu-sales-6-16-25-6-22-25-nintendo-
switch-2-still-dominating-in-japan/", "snippet": "Famitsu sales (6/16/25 \u2013 6/22/25) \u2013 Nintendo Switch 2 still dominating in Japan\nThe latest Japanese hardware sales from Famitsu are as
follows:\nSwitch 2 \u2013 140,026\nSwitch Lite \u2013 5,212\nSwitch OLED \u2013 5,110\nPS5 \u2013 3,581\nSwitch \u2013 2,442\nPS5 Pro \u2013 1,676\nPS5 Digital Edition \u2013 749\nXbox Series S \u2013
107\nXbox Series X Digital Edition \u2013 47\nXbox Series X \u2013 37\nPS4 \u2013 28\nFor comparison\u2019s sake, here are the hardware numbers from last week:\nSwitch 2 \u2013 153,205\nPS5 \u2013
9,612\nSwitch Lite \u2013 5,485\nSwitch OLED \u2013 5,447\nPS5 P", "api_data": null, "hint": null}, {"title": "Famitsu sales (6/9/25 - 6/15/25) | Famiboards", "url":
"https://famiboards.com/threads/famitsu-sales-6-9-25-6-15-25.14169/", "snippet": "- Pronouns\n- He/him\nHardware\nSwitch 2 \u2013 153,205\nPS5 \u2013 9,612\nSwitch Lite \u2013 5,485\nSwitch OLED
\u2013 5,447\nPS5 Pro \u2013 3,125\nSwitch \u2013 2,387\nPS5 Digital Edition \u2013 1,392\nXbox Series S \u2013 125\nXbox Series X \u2013 102\nXbox Series X Digital Edition \u2013 34\nPS4 \u2013
22\nSoftware\n1. [NS2] Mario Kart World \u2013 134,900 / 917,466\n2. [NSW] Fantasy Life i: The Girl Who Steals Time \u2013 11,217 / 123,121\n3. [NSW] Rune Factory: Guardians of Azuma \u2013 9,724 /
55,427\n4. [NSW] Mario Kart 8 Deluxe \u2013 6,460 / 6,347,853\n5. [NSW] Minecraft \u2013 5,91", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Famiboards Switch 2 sales May 2026 week price hike"
}
```

### 📋 Result

```
{"query": "Famiboards Switch 2 sales May 2026 week price hike", "results": [{"title": "Nintendo hikes Switch 2 prices and expects console sales to decline as memory crunch bites", "url":
"https://www.cnbc.com/2026/05/08/nintendo-switch-2-price-hike-sales-fall-memory-crunch.html", "snippet": "[Nintendo](https://www.cnbc.com/quotes/7974.T-JP/) will hike the retail price of the Switch 2
after forecasting a decline in sales for its flagship console as the memory chip crunch hits the Japanese gaming giant.\nThe company said on Friday it expects to sell 16.5 million units of the Switch
2 in its fiscal year ended Mar. 31, 2027. That is a decline from the 19.86 million units sold in the fiscal year just ended.\nMeanwhile, the company's forecasts for the current year were far below
analyst est", "api_data": null, "hint": null}, {"title": "Nintendo Switch 2 price hike, sales forecast cut 2026", "url": "https://finance.yahoo.com/markets/stocks/articles/nintendo-switch-2-price-
hike-125304028.html", "snippet": "Nintendo [raised the price of its Switch 2 console](https://finance.yahoo.com/markets/stocks/articles/nintendo-switch-2-price-hike-121235594.html) across major
markets and issued a downbeat financial outlook for the fiscal year ending March 2027, as surging memory chip costs and tariff headwinds weigh on the company's bottom line.\nThe price of the Switch 2
in the U.S. will rise by $50 to $499.99, effective Sept. 1. In Japan, the price climbs \u00a510,000 to \u00a559,980 starting May 25, and in Canada the ", "api_data": null, "hint": null}, {"title":
"Nintendo Stock Plummets 10% on Bleak $500 Switch 2 Sales Forecast | Outlook Respawn", "url": "https://respawn.outlookindia.com/gaming/gaming-news/nintendo-stock-plummets-10-on-
bleak-500-switch-2-sales-forecast", "snippet": null, "api_data": null, "hint": null}, {"title": "Switch Lifetime Sales Inch Toward PS2, But Price Hikes May Hurt Its Chances | Nintendo Life", "url":
"https://www.nintendolife.com/news/2026/05/switch-lifetime-sales-inch-toward-ps2-but-price-hikes-may-hurt-its-chances", "snippet": "![PS2 /
Switch](https://images.nintendolife.com/bd5b69c9f1191/ps2-switch.900x.jpg)\n![PS2 / Switch](https://images.nintendolife.com/bd5b69c9f1191/ps2-switch.900x.jpg)\nThe Switch is an absolute juggernaut,
taking pride a place as Nintendo's best-selling console of all time. Yet with the company only shifting 3.8 million in its latest fiscal year and prices on the rise, does it have any hope of
surpassing the mighty PS2?\n[Current figures](https://www.nintendo.co.jp/ir/en/finance/hard_soft/index.htm", "api_data": null, "hint": null}, {"title": "Everything we know about the Switch 2 price
hike | Creative Bloq", "url": "https://www.creativebloq.com/entertainment/gaming/the-switch-2-price-hike-everything-you-need-to-know", "snippet": "Nintendo announced last week that it would be raising
prices on its popular Switch 2 console, almost one year following its release date. The company is claiming that a multitude of factors have influenced this decision, though rumour has it that
pressure from investors, profit concerns, US tariffs, and chip prices are the core contributors.\nSo what does this mean for consumers? The price of the Nintendo Switch 2as it stands is currently
$449.99 / \u00a3395.99 for the console alone (no games included", "api_data": null, "hint": null}, {"title": "Starting May 2026, Nintendo of America will price exclusive Switch 2 digital games
differently | Page 2 | Famiboards", "url": "https://famiboards.com/threads/starting-may-2026-nintendo-of-america-will-price-exclusive-switch-2-digital-games-differently.16974/page-2", "snippet":
"Mario Tennis might be why they\u2019re going for this to begin with, honestly. Very interested to see what sales numbers are like for it, because if they\u2019re bad I could see Nintendo pivoting to
a cheaper digitally price. I just can\u2019t imagine them putting an $80 tennis game on store shelves, honestly.\nI do wonder if this is Nintendos attempt at dynamic pricing in a backwards way.
Instead of everything being a flat $70, some games are $10 cheaper digitally while other games are $10 more expensive physi", "api_data": null, "hint": null}, {"title": "Famitsu sales (4/27/26 \u2013
5/10/26) \u2013 big numbers for Nintendo Switch 2", "url": "https://nintendoeverything.com/famitsu-sales-4-27-26-5-10-26-big-numbers-for-nintendo-switch-2/", "snippet": "Famitsu sales (4/27/26 \u2013
5/10/26) \u2013 big numbers for Nintendo Switch 2\nThe latest Japanese hardware sales from Famitsu are as follows:\nSwitch 2 \u2013 214,438\nSwitch OLED \u2013 16,580\nPS5 Digital Edition \u2013
16,539\nSwitch Lite \u2013 16,039\nSwitch \u2013 7,960\nPS5 Pro \u2013 5,248\nPS5 \u2013 1,973\nXbox Series X Digital Edition \u2013 352\nXbox Series S \u2013 97\nXbox Series X \u2013 64\nFor
comparison\u2019s sake, here are the hardware numbers from last week:\nSwitch 2 \u2013 45,825\nSwitch Lite \u2013 11,263\nSwitch OLED \u2013 10,796\nPS5 Digital Edition \u2013 6,361\nSw", "api_data":
null, "hint": null}, {"title": "Why Nintendo Expects Fewer Second-Year Switch 2 Hardware Sales - GameSpot", "url": "https://www.gamespot.com/articles/why-nintendo-expects-fewer-second-year-
switch-2-hardware-sales/1100-6539861/", "snippet": null, "api_data": null, "hint": null}, {"title": "Nintendo Announces Sweeping Price Hikes For Switch 2 | Nintendo Life", "url":
"https://www.nintendolife.com/news/2026/05/nintendo-announces-sweeping-price-hikes-for-switch-2", "snippet": "Nintendo [has announced](https://www.nintendo.co.jp/corporate/release/en/2026/260508.html)
that the Switch 2 will be going up in price globally, with Nintendo Switch Online also receiving a price hike in Japan.\nHardware price revisions are effective from 25th May 2026 in Japan and 1st
September in Western markets. Nintendo states that the changes are due to \"changes in market conditions\" and the \"global business outlook\".\n\"We sincerely apologize for the impact these price
revisions may have on o", "api_data": null, "hint": null}, {"title": "Famitsu Sales (4/27/26 \u2013 5/10/26) | Famiboards", "url": "https://famiboards.com/threads/famitsu-
sales-4-27-26-%E2%80%93-5-10-26.17417/", "snippet": "- Pronouns\n- He/Him\nHardware Sales\nwww.gematsu.com\n- Switch 2 \u2013 214,438 (5,367,660)\n- Switch OLED Model \u2013 16,850 (9,571,489)\n-
PlayStation 5 Digital Edition \u2013 16,539 (1,283,342)\n- Switch Lite \u2013 16,039 (6,958,407)\n- Switch \u2013 7,960 (20,292,060)\n- PlayStation 5 Pro \u2013 5,248 (355,220)\n- PlayStation 5 \u2013
1,973 (5,918,111)\n- Xbox Series X Digital Edition \u2013 352 (30,490)\n- Xbox Series S \u2013 97 (341,958)\n- Xbox Series X \u2013 64 (326,386)\n- [NSW] Tomodachi Life: Living the Dream \u2013
299,619 (1,043,557)\n- [SW2] Pok", "api_data": null, "hint": null}]}
```

```json
{
  "query": "PS5 Japan price hike sales spike weekly data Famitsu before after"
}
```

### 📋 Result

```
{"query": "PS5 Japan price hike sales spike weekly data Famitsu before after", "results": [{"title": "PS5 Price Hike Hits Japan Hard as PS5 Pro Sales Sink to Xbox Levels | Push Square", "url":
"https://www.pushsquare.com/news/2026/04/ps5-price-hike-hits-japan-hard-as-ps5-pro-sales-sink-to-xbox-levels", "snippet": "![PS5 Price Hike Hits Japan Hard as PS5 Pro Sales Collapse
1](https://images.pushsquare.com/23d46c5099b24/ps5-price-hike-hits-japan-hard-as-ps5-pro-sales-collapse-1.900x.jpg)\n![PS5 Price Hike Hits Japan Hard as PS5 Pro Sales Collapse
1](https://images.pushsquare.com/23d46c5099b24/ps5-price-hike-hits-japan-hard-as-ps5-pro-sales-collapse-1.900x.jpg)\nThere\u2019s really no reason to purchase a non-language locked PS5 console in
Japan after [Sony\u2019s latest price hike](https://www.pushsquare.com/news/2026/", "api_data": null, "hint": null}, {"title": "Famitsu: the effect of PS5 price hike in Japan | IconEra", "url":
"https://icon-era.com/threads/famitsu-the-effect-of-ps5-price-hike-in-japan.19830/", "snippet": "Switch 2 \u2013 59,543 (5,011,059)\nPlayStation 5 Digital Edition \u2013 12,141 (1,248,515)\nSwitch
OLED Model \u2013 7,468 (9,526,329)\nSwitch Lite \u2013 4,807 (6,903,964)\nSwitch \u2013 4,067 (20,0271,045)\nPlayStation 5 Pro \u2013 840 (341,548)\nPlayStation 5 \u2013 558 (5,910,474)\nXbox Series
X \u2013 525 (325,952)\nXbox Series X Digital Edition \u2013 278 (29,362)\nXbox Series S \u2013 129 (341,622)\nwww.gematsu.com\nPlayStation 5 Digital Edition \u2013 12,141 (1,248,515)\nSwitch OLED
Model \u2013 7,468 (9,526,329)\nSwitch Lite \u2013 4,807 (6,903,964)\nSwitch \u2013 4,0", "api_data": null, "hint": null}, {"title": "Japanese Charts: Combined PS5 Sales Can't Even Beat Switch Lite |
Nintendo Life", "url": "https://www.nintendolife.com/news/2026/04/japanese-charts-combined-ps5-sales-cant-even-beat-switch-lite", "snippet": "![Switch
Lite](https://images.nintendolife.com/2a141a9c61df7/switch-lite.900x.jpg)\n![Switch Lite](https://images.nintendolife.com/2a141a9c61df7/switch-lite.900x.jpg)\nThe latest Japanese charts are here
thanks to [Famitsu](https://www.famitsu.com/article/202604/72113), and yet again, we can see that [Pok\u00e9mon Pokopia](https://www.nintendolife.com/games/nintendo-switch-2/pokemon-pokopia) has
beaten the competition to take the top spot with 23,738 sales. It's inching toward that 1 million milestone!", "api_data": null, "hint": null}, {"title": "PS5 Consoles Only Sold 13,539 Units in Japan
Last Week, Nintendo Switch 2 Sold 59,543 Units", "url": "https://gamingbolt.com/ps5-consoles-only-sold-13539-units-in-japan-last-week-nintendo-switch-2-sold-59543-units", "snippet": "The [worldwide
price hikes for PS5 and PS5 Pro](https://gamingbolt.com/ps5-ps5-pro-and-playstation-portal-prices-increasing-worldwide-on-april-2nd) have seemingly hit the Japanese market particularly hard. As caught
by [PushSquare](https://www.pushsquare.com/news/2026/04/ps5-price-hike-hits-japan-hard-as-ps5-pro-sales-sink-to-xbox-levels), the latest hardware sales data from Japanese publication
[Famitsu](https://www.famitsu.com/article/202604/71349) indicates that only 840 units of the PS5 Pro ", "api_data": null, "hint": null}, {"title": "PS5 Price increase collapses PlayStation console
sales in Japan, with Xbox gaining - Notebookcheck News", "url": "https://www.notebookcheck.net/PS5-Price-increase-collapses-PlayStation-console-sales-in-Japan-with-Xbox-gaining.1270302.0.html",
"snippet": "If Japan is any indication, buyers worldwide are avoiding PlayStation consoles. Following the latest PS5 and PS5 Pro price increase, the systems experienced a dramatic decline in weekly
sales. With the Xbox Series X making up ground, only the region-locked digital option remains appealing.\nAnalysts have wondered how the significant PS5 price increases may hurt PlayStation console
sales. Courtesy of Gematsu, Famitsu has provided the first glimpse of the impact in Japan. For the week ending on Apr", "api_data": null, "hint": null}, {"title": "Miscalculated, but where: Sony
ruined PS5 Pro sales in Japan with its price increase", "url": "https://ixbt.games/en/news/2026/04/13/409802-sony-zagubila-prodazi-ps5-v-iaponii-svoim-povyseniem-cen.html", "snippet": "Japanese gamers
simply don't see the point in buying an expensive device.\nAfter the recent price increase by Sony, the game console market in Japan reacted sharply and unequivocally: demand for expensive versions of
PlayStation 5 is plummeting, while the more affordable model with language blocking is showing steady sales growth.\nAccording to recent Famitsu data, only 840 units of PlayStation 5 Pro and 558
standard disc PS5s were sold in the first week of April. These figures look extremely weak", "api_data": null, "hint": null}, {"title": "[Japan] Famitsu sales for April 2026 (Top 5 Software,
Publishers, Hardware) \u2013 Perfectly Nintendo", "url": "https://www.perfectly-nintendo.com/japan-famitsu-sales-for-april-2026-top-5-software-publishers-hardware/", "snippet": "[Japan] Famitsu sales
for April 2026 (Top 5 Software, Publishers, Hardware)\nHere\u2019s the latest sales report from Famitsu, with Hardware and Software sales for April 2026 in Japan (March 30th to April 26th, so 4 weeks
in total).\nFamitsu\nTop 5 Software\nTomodachi Life: Living the Dream is off to a great start with over 740,000 units sold in just 10 days. Unsurprisingly, it was the best-selling game in April by a
wide margin.\nTomodachi Life: Living the Dream sold significantly better than its predece", "api_data": null, "hint": null}, {"title": "Famitsu Sales: Week 17, 2026 (Apr 20 - Apr 26)", "url":
"https://gamrconnect.vgchartz.com/thread/250403/famitsu-sales-week-17-2026-apr-20-apr-26/", "snippet": "[firebush03](https://gamrconnect.vgchartz.com/profile/500807/firebush03/)on 30 April 2026\nNote
regarding Famitsu sales data next week: Golden Week starts Wednesday (4-29-2026), meaning we will not be seeing data until the week following (Week of 5-11-2026).\nFamitsu Sales: Week 17, 2026 (Apr 20
- Apr 26)\n01./01. [NSW] Tomodachi Life: Living the Dream <ETC> (Nintendo) {2026.04.16} (\u00a56.480) - 178.533 / 743.938 (-68%)\n02./03. [NS2] Pokemon Pokopia <ADV> (Pokemon Co.) {2026.03.05}
(\u00a58.164) - 17.039 /", "api_data": null, "hint": null}, {"title": "According to Famitsu, PS5 sales in Japan dropped to just ...", "url": "https://www.facebook.com/gamenewsplusnet/posts/according-
to-famitsu-ps5-sales-in-japan-dropped-to-just-5855-units-last-week-far/1413683743662540/", "snippet": null, "api_data": null, "hint": null}]}
```

## 💭 Thinking

Excellent! Now I have the launch week data:
- Switch 2 launch week (June 2-8, 2025): **947,931 units** - this was a record
- Second week (June 9-15): 153,205
- Third week (June 16-22): 140,026

So the launch week was nearly 1 million, then dropped to ~150k in week 2, ~140k in week 3.

By late 2025 (Nov):  ~101,549
By early 2026 (Feb): ~57,000-85,000 range
By March/April: ~44,000-60,000 range


Then the Golden Week + price hike announcement period: ~107k/week average

Now I'm looking at the May 18-24 week—the final window before the price increase hits. Demand should spike dramatically as consumers rush to buy at the current price, but supply is the real bottleneck here. I'm seeing reports of widespread sell-outs and purchase limits at major retailers, which suggests we're already hitting capacity constraints. Looking back at the post-launch weeks when supply was clearly maxed out, weeks 2 and 3 hit around 150k and 140k respectively, so that's probably the realistic ceiling for what can actually be produced and distributed in a single week.

The timing is interesting though—Nintendo had 11 months to ramp production, but the question is whether they can surge supply specifically to Japan in just 17 days between the announcement and the price hike. From a retailer's perspective, the MSRP increase means they'll be buying new inventory at different wholesale prices going forward, so there's actually an incentive for them to stock up at the old price point before May 25.

The real constraint is Nintendo's manufacturing capacity and whether they can divert units from other regions to Japan. Based on their annual forecast, Japan typically receives around 80-95k units weekly, but the data around the announcement period shows they were already hitting roughly 107k per week—so there's some room to surge, but probably not dramatically.

Looking at the post-launch weeks, Nintendo managed 140-160k units in weeks 2-3, but that was with months of preparation. A sudden push with only two weeks' notice would be much harder to replicate. The May 11-17 week likely already saw elevated demand that depleted retailer inventory, so by the final week before the price increase, stock could be tight.

On the demand side, the ¥10,000 price increase represents a significant 20% jump—that's roughly $67 USD in savings for anyone buying before May 25, which creates strong pull-forward incentive for consumers who were already considering a purchase.

The real constraint here appears to be supply, not demand. The reports of long lines, purchase restrictions, and sell-outs all point to demand far exceeding what Nintendo can deliver. So the ceiling for this week really comes down to how many units Nintendo can actually get into Japanese retail channels in that narrow window.

Looking at the timing around the price hike announcement on May 8, the May 11-17 week would've been the first full week of surge buying, with retailers scrambling to restock while Nintendo tries to redirect inventory to Japan. By May 18-24—the final week before the price takes effect—there's maximum urgency on both sides, but the stock depletion from the previous week means Nintendo's fighting against inventory that's already been sold through. Given all this, I'm estimating the May 18-24 week lands somewhere between 80,000 and 150,000 units, likely toward the higher end of that range. estimate around 100,000-120,000.

Reasoning:
1. Demand is essentially unlimited (much higher than supply)
2. Supply is the constraint
3. Normal capacity seems to be ~80-100k/week in Japan
4. Nintendo may have been able to surge somewhat above normal (~100-130k is plausible with extra shipments)
5. But inventory depletion from May 11-17 may limit what's available on shelves
6. Some retailers selling out = zero inventory at those locations

Actually, the Golden Week period already showed ~107k/week. If the price hike announcement was on May 8, then the May 11-17 week would be the first full week of panic buying, likely seeing significantly higher sales around 120-160k. By May 18-24, inventory would be more depleted, though Nintendo would also be ramping up shipments to meet demand.

I should model this more systematically using a Monte Carlo approach, accounting for key parameters like the pre-announcement baseline around 45-52k/week, the Golden Week boost to 80-90k, a post-announcement surge multiplier of 1.5-2.5x on top of those levels, and a supply ceiling around 130-170k based on post-launch capacity. The inventory depletion after two weeks of elevated buying would also be a constraining factor.

Let me break down what actually happened week by week. The description mentions roughly 93k and 96k across the two weeks, with the price hike announced May 8 (Friday). So the April 27-May 3 period would be pure Golden Week boost without the announcement effect. The real question is whether May 18-24 will exceed or fall short of May 11-17, which hinges on inventory availability and Nintendo's restocking capacity during that final week before the price increase. My best guess is that May 11-17 likely hit 130-170k units as panic buying peaked, while May 18-24 probably landed in the 100-140k range due to stock depletion—though if Nintendo managed a significant inventory push, that final week could have actually driven even higher sales from the maximum urgency to buy before prices rose.

Now I'm comparing this against historical benchmarks: the Switch 2 launch weeks showed 150k+ units under supply constraints, Golden Week averaged around 93k, and normal pre-announcement weeks were 44-60k. The key is whether the price hike urgency can replicate launch-level demand in the 130-160k range or if it'll settle into the 90-120k band.

I'm weighing the factors—the "hysteria" effect and Nintendo's ability to surge supply against the reality that two weeks isn't much time, retailers are already depleted, and this lacks the novelty of an actual launch. So I'm setting my median estimate at around 115,000 units, with a P10 floor of 70,000 if supply really tightens and a P90 ceiling of 175,000 if Nintendo successfully floods the market. Now I'll run a Monte Carlo simulation to formalize this distribution.

## 💬 Response

Now I have excellent data. Let me compile all the key data points and run a Monte Carlo simulation.

**Key data points found:**
- Launch week (Jun 2-8, 2025): **947,931** units (record)
- Week 2 (Jun 9-15): **153,205**
- Week 3 (Jun 16-22): **140,026**
- Normal weeks (Apr 2026): 44,000-52,000
- Golden Week/announcement period (Apr 27-May 10): **214,438** total (~93k + ~96k)
- Price hike announced May 8, effective May 25
- Reports of "hysteria," sell-outs, retailer restrictions (Bic Camera requiring credit card)

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\nnp.random.seed(42)\nN = 100_000\n\n# ---- Key historical data points ----\n# Normal weeks (post-stabilization, Apr 2026): 44-52k\n# Golden Week boost (no price hike effect): ~93k (week of Apr 27-May 3)\n# Post-launch week 2-3 (max throughput non-launch): 140-153k\n# Golden Week + price announcement barely: ~96k (May 4-10, announcement was May 8 Friday)\n# Price hike: \u00a510,000 increase (20%) effective May 25\n\n# The May 18-24 week is the LAST full week before price hike.\n# Key dynamics:\n# 1. Demand >> Supply (supply-constrained, reports of sell-outs)\n# 2. Supply ceiling matters more than demand\n# 3. Two weeks of elevated buying (May 11-17 already drew down stock)\n# 4. Nintendo has had ~10 days since announcement to reroute inventory\n\n# ---- Scenario-based Monte Carlo ----\n\n# Scenario 1: Severe supply depletion (20% weight)\n# May 11-17 depleted most inventory. Retailers largely sold out.\n# Nintendo can't restock fast enough. Sales limited to trickle.\n# Range: 50,000 - 85,000\ns1_weight = 0.15\ns1_samples = np.random.triangular(50000, 70000, 90000, int(N * s1_weight))\n\n# Scenario 2: Moderate supply constraint (40% weight)  \n# Stock is tight but not depleted. Nintendo manages moderate resupply.\n# Sales around Golden Week levels or slightly above.\n# Range: 85,000 - 140,000\ns2_weight = 0.40\ns2_samples = np.random.triangular(85000, 115000, 145000, int(N * s2_weight))\n\n# Scenario 3: Strong resupply (30% weight)\n# Nintendo aggressively routes inventory to Japan before price hike.\n# Sales comparable to post-launch week 2-3 supply levels.\n# Range: 120,000 - 175,000\ns3_weight = 0.30\ns3_samples = np.random.triangular(120000, 145000, 175000, int(N * s3_weight))\n\n# Scenario 4: Exceptional supply surge (15% weight)\n# Nintendo prioritizes Japan shipments, retailers well-stocked.\n# Approaches or exceeds post-launch maximums.\n# Range: 155,000 - 220,000\ns4_weight = 0.15\ns4_samples = np.random.triangular(155000, 185000, 225000, int(N * s4_weight))\n\n# Combine all scenarios\nall_samples = np.concatenate([s1_samples, s2_samples, s3_samples, s4_samples])\nnp.random.shuffle(all_samples)\n\n# Calculate percentiles\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nvalues = np.percentile(all_samples, percentiles)\n\nprint(\"=== Monte Carlo Results (Scenario Mixture) ===\")\nprint(f\"Total samples: {len(all_samples)}\")\nprint(f\"\\nMean: {np.mean(all_samples):,.0f}\")\nprint(f\"Median: {np.median(all_samples):,.0f}\")\nprint(f\"Std Dev: {np.std(all_samples):,.0f}\")\nprint()\nfor p, v in zip(percentiles, values):\n    print(f\"  P{p:2d}: {v:>10,.0f}\")\n\nprint(f\"\\n=== Scenario Statistics ===\")\nprint(f\"Scenario 1 (Supply depleted): mean={np.mean(s1_samples):,.0f}, weight={s1_weight}\")\nprint(f\"Scenario 2 (Moderate supply): mean={np.mean(s2_samples):,.0f}, weight={s2_weight}\")\nprint(f\"Scenario 3 (Strong resupply): mean={np.mean(s3_samples):,.0f}, weight={s3_weight}\")\nprint(f\"Scenario 4 (Exceptional):     mean={np.mean(s4_samples):,.0f}, weight={s4_weight}\")\n\n# Check: what fraction is above the 250k upper bound?\nabove_250k = np.mean(all_samples > 250000) * 100\nprint(f\"\\nFraction above 250k: {above_250k:.2f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Monte Carlo Results (Scenario Mixture) ===\nTotal samples: 100000\n\nMean: 128,723\nMedian: 128,069\nStd Dev: 36,858\n\n  P 1:     57,292\n  P 5:     66,255\n  P10:
73,540\n  P20:     99,991\n  P25:    106,266\n  P30:    110,991\n  P40:    119,064\n  P50:    128,069\n  P60:    137,146\n  P70:    146,382\n  P75:    151,662\n  P80:    158,231\n  P90:    181,138\n
P95:    194,218\n  P99:    211,182\n\n=== Scenario Statistics ===\nScenario 1 (Supply depleted): mean=69,910, weight=0.15\nScenario 2 (Moderate supply): mean=115,012, weight=0.4\nScenario 3 (Strong
resupply): mean=146,712, weight=0.3\nScenario 4 (Exceptional):     mean=188,121, weight=0.15\n\nFraction above 250k: 0.00%\n", "stderr": "", "duration_ms": 274}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also think about this from another angle - what was the actual weekly supply throughput?\n# And validate my scenarios against known constraints.\n\nprint(\"=== Supply Capacity Analysis ===\")\nprint()\nprint(\"Known weekly throughputs (Famitsu-tracked Japan):\")\nprint(f\"  Launch week (Jun 2-8, 2025): 947,931 (extreme, pre-produced inventory)\")\nprint(f\"  Week 2 (Jun 9-15):            153,205 (ongoing supply stream)\")\nprint(f\"  Week 3 (Jun 16-22):           140,026\")\nprint(f\"  Nov 10-16, 2025:              101,549\")\nprint(f\"  Feb 16-22, 2026:               63,313\")\nprint(f\"  Feb 23-Mar 1:                  85,830 (Pokemon Pokopia launch)\")\nprint(f\"  Mar 30-Apr 5:                  59,543\")\nprint(f\"  Apr 6-12:                      52,058\")\nprint(f\"  Apr 13-19:                     44,280\")\nprint(f\"  Apr 20-26:                     45,825\")\nprint(f\"  Apr 27-May 3 (est):           ~93,000 (Golden Week)\")\nprint(f\"  May 4-10 (est):               ~96,000 (GW + announcement May 8)\")\nprint()\n\n# Key insight: Week 2-3 post-launch (153k, 140k) represent maximum weekly throughput\n# when Nintendo was actively trying to maximize Japan supply.\n# Normal supply capacity seems to be ~50-60k (pre-announcement Apr)\n# Surge supply capacity seems to be 80-100k (Golden Week, Nov)\n# Maximum non-launch supply: ~150k (weeks 2-3 post-launch, extreme priority)\n\n# For May 18-24:\n# - Nintendo would want to maximize pre-hike sales\n# - But only 10 days notice from announcement to start of this week\n# - Manufacturing \u2192 shipping \u2192 retail takes time\n# - Japan has short supply chain (domestic or from nearby Asia)\n\nprint(\"=== Key constraints for May 18-24 ===\")\nprint()\nprint(\"1. Time from announcement (May 8) to week start (May 18): 10 days\")\nprint(\"   - Enough for air freight from China/Vietnam (~2-3 days)\")\nprint(\"   - Enough to redirect sea shipments already in transit (~5-7 days)\")\nprint(\"   - NOT enough for new production orders (weeks to ramp)\")\nprint()\nprint(\"2. What was available:\")\nprint(\"   - Normal pipeline inventory: ~50-60k/week\")\nprint(\"   - Additional units diverted from other regions/warehoused\")\nprint(\"   - Pre-existing safety stock at Nintendo Japan warehouses\")\nprint()\nprint(\"3. Demand pull-forward from May 11-17:\")\nprint(\"   - First full week of panic buying likely depleted much stock\")\nprint(\"   - But retail restocking would happen continuously\")\nprint()\nprint(\"4. Best analog: Post-launch weeks 2-3 (140-153k)\")\nprint(\"   - These were also demand >> supply weeks\")\nprint(\"   - Nintendo had months to prepare launch inventory\")\nprint(\"   - For price hike, only 10 days of exceptional prep time\")\nprint()\n\n# My assessment: \n# - The ceiling is probably ~130-160k in the best case\n# - More likely in the 100-130k range\n# - Could be lower (70-90k) if inventory was severely depleted May 11-17\n# - The median around 125-130k seems reasonable\n\n# Let me also check: what if my scenarios are slightly off?\n# Sensitivity: what if supply depletion is more likely?\n\nprint(\"=== Sensitivity Test: Higher depletion probability ===\")\n# Give more weight to scenarios 1 and 2\ns1_w2 = 0.25  # higher depletion\ns2_w2 = 0.40\ns3_w2 = 0.25\ns4_w2 = 0.10\n\ns1_s = np.random.triangular(50000, 70000, 90000, int(N * s1_w2))\ns2_s = np.random.triangular(85000, 115000, 145000, int(N * s2_w2))\ns3_s = np.random.triangular(120000, 145000, 175000, int(N * s3_w2))\ns4_s = np.random.triangular(155000, 185000, 225000, int(N * s4_w2))\n\nalt_samples = np.concatenate([s1_s, s2_s, s3_s, s4_s])\nalt_values = np.percentile(alt_samples, percentiles)\nprint(f\"Median: {np.median(alt_samples):,.0f}\")\nprint(f\"P10: {np.percentile(alt_samples, 10):,.0f}\")\nprint(f\"P90: {np.percentile(alt_samples, 90):,.0f}\")\n\nprint()\nprint(\"=== Sensitivity Test: Higher resupply probability ===\")\n# Give more weight to scenarios 3 and 4\ns1_w3 = 0.10\ns2_w3 = 0.30\ns3_w3 = 0.40\ns4_w3 = 0.20\n\ns1_s3 = np.random.triangular(50000, 70000, 90000, int(N * s1_w3))\ns2_s3 = np.random.triangular(85000, 115000, 145000, int(N * s2_w3))\ns3_s3 = np.random.triangular(120000, 145000, 175000, int(N * s3_w3))\ns4_s3 = np.random.triangular(155000, 185000, 225000, int(N * s4_w3))\n\nalt2_samples = np.concatenate([s1_s3, s2_s3, s3_s3, s4_s3])\nprint(f\"Median: {np.median(alt2_samples):,.0f}\")\nprint(f\"P10: {np.percentile(alt2_samples, 10):,.0f}\")\nprint(f\"P90: {np.percentile(alt2_samples, 90):,.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Supply Capacity Analysis ===\n\nKnown weekly throughputs (Famitsu-tracked Japan):\n  Launch week (Jun 2-8, 2025): 947,931 (extreme, pre-produced inventory)\n  Week 2
(Jun 9-15):            153,205 (ongoing supply stream)\n  Week 3 (Jun 16-22):           140,026\n  Nov 10-16, 2025:              101,549\n  Feb 16-22, 2026:               63,313\n  Feb 23-Mar 1:
85,830 (Pokemon Pokopia launch)\n  Mar 30-Apr 5:                  59,543\n  Apr 6-12:                      52,058\n  Apr 13-19:                     44,280\n  Apr 20-26:                     45,825\n
Apr 27-May 3 (est):           ~93,000 (Golden Week)\n  May 4-10 (est):               ~96,000 (GW + announcement May 8)\n\n=== Key constraints for May 18-24 ===\n\n1. Time from announcement (May 8) to
week start (May 18): 10 days\n   - Enough for air freight from China/Vietnam (~2-3 days)\n   - Enough to redirect sea shipments already in transit (~5-7 days)\n   - NOT enough for new production
orders (weeks to ramp)\n\n2. What was available:\n   - Normal pipeline inventory: ~50-60k/week\n   - Additional units diverted from other regions/warehoused\n   - Pre-existing safety stock at Nintendo
Japan warehouses\n\n3. Demand pull-forward from May 11-17:\n   - First full week of panic buying likely depleted much stock\n   - But retail restocking would happen continuously\n\n4. Best analog:
Post-launch weeks 2-3 (140-153k)\n   - These were also demand >> supply weeks\n   - Nintendo had months to prepare launch inventory\n   - For price hike, only 10 days of exceptional prep time\n\n===
Sensitivity Test: Higher depletion probability ===\nMedian: 119,091\nP10: 67,804\nP90: 167,762\n\n=== Sensitivity Test: Higher resupply probability ===\nMedian: 139,027\nP10: 87,321\nP90: 187,555\n",
"stderr": "", "duration_ms": 12}
```

## 💭 Thinking

Good. Let me now think about which scenario weights are most appropriate.

The key considerations:
1. Price hike was announced May 8, effective May 25 - only 17 days between announcement and implementation
2. May 18-24 is the LAST full week
3. Reports from around May 12-16 show "hysteria," sell-outs, retailer restrictions
4. Nintendo would want to supply Japan to the extent possible
5. Supply chain from China/Vietnam to Japan is short (2-5 days by air/sea)

For the scenario weights, I think my base case weights (15/40/30/15) are reasonable. 

The sell-outs point to supply constraints, but the retailer restrictions suggest they're managing limited stock rather than being completely depleted—they expect to have some inventory, just not enough for everyone. The "reminiscent of launch" language and sell-out reports both support a moderate constraint scenario in the 85-145k range as most likely, with a solid 30% probability of stronger resupply. My initial model captures this well, so I'll stick with those weights and also factor in the May 11-17 week data.

Since that week hasn't been published yet, it'll be crucial context—if it came in very high around 150k+, then May 18-24 might dip due to inventory running low, but if it was moderate at 100-120k, we could see similar or even higher sales as the deadline approaches. I should also remember the PS5 price hike in Japan actually caused sales to collapse rather than surge beforehand, but the Switch 2 situation is different—people are rushing to buy before the price increase takes effect, not fleeing from it.

My base case median of around 128k with a range from roughly 73k at the 10th percentile to 181k at the 90th percentile feels solid. I want to make sure I'm not being overly uncertain here, so let me ground this in the strongest evidence, starting with what happened during the Golden Week period.

The data shows that even when the price hike was barely announced, we saw about 107k per week, and retailers are describing conditions that match launch weeks 2-3 when we hit 140-153k. Sell-outs are clearly happening, but that's more about inventory limits than demand disappearing. Nintendo had over a week and a half from the announcement to push additional stock into Japan, which should matter. Given all this, I'm confident the May 18-24 range sits between 100-150k, and my model's P25-P75 band of 106-152k captures that well. I'll lock in these numbers.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Final model - let me refine scenario weights based on all evidence\n\n# Key evidence synthesis:\n# 1. Golden Week (BEFORE price hike effect) already showed ~93-96k/week\n# 2. Post-launch max throughput: 140-153k/week (when Nintendo was fully prioritizing)\n# 3. Reports of \"launch-like hysteria\" \u2192 suggests demand is massive\n# 4. But sell-outs and restrictions \u2192 supply is the bottleneck\n# 5. Nintendo has 10 days from announcement to reroute supply\n# 6. Japan supply chain is SHORT (China/Vietnam \u2192 Japan = days)\n# 7. Nintendo benefits from selling units before hike (customers goodwill)\n# 8. The week of May 11-17 already drew down inventory\n\n# I'll slightly adjust: the \"reminiscent of launch\" language and the \n# retailer restrictions suggest demand is truly explosive, but supply \n# is genuinely constrained. The sell-outs happening BEFORE our target week\n# suggest May 18-24 might face more depletion.\n\n# Final scenario weights:\n# Scenario 1 (Supply severely depleted): 15%  - multiple retailers sold out\n# Scenario 2 (Moderate supply): 40%  - most likely, some stock but constrained\n# Scenario 3 (Strong resupply): 30%  - Nintendo manages good throughput\n# Scenario 4 (Exceptional): 15%  - matches post-launch maximums\n\n# This matches my original model. Let me produce the final output.\n\nprint(\"=== FINAL FORECAST: Switch 2 Japan Sales, May 18-24, 2026 ===\")\nprint()\nprint(\"Base case scenario weights:\")\nprint(f\"  Supply depleted (50-90k):    15%\")\nprint(f\"  Moderate supply (85-145k):   40%\")\nprint(f\"  Strong resupply (120-175k):  30%\")\nprint(f\"  Exceptional (155-225k):      15%\")\nprint()\n\n# Use the main model results\npercentile_dict = {}\nfor p, v in zip(percentiles, values):\n    percentile_dict[str(p)] = round(v)\n    \nprint(\"Final percentile estimates:\")\nfor p, v in sorted(percentile_dict.items(), key=lambda x: int(x[0])):\n    print(f\"  P{p:>2}: {v:>10,}\")\n\nprint()\nprint(f\"Weighted mean: {np.mean(all_samples):,.0f}\")\nprint(f\"Weighted median: {np.median(all_samples):,.0f}\")\nprint(f\"80% CI: [{np.percentile(all_samples, 10):,.0f} - {np.percentile(all_samples, 90):,.0f}]\")\nprint(f\"50% CI: [{np.percentile(all_samples, 25):,.0f} - {np.percentile(all_samples, 75):,.0f}]\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== FINAL FORECAST: Switch 2 Japan Sales, May 18-24, 2026 ===\n\nBase case scenario weights:\n  Supply depleted (50-90k):    15%\n  Moderate supply (85-145k):   40%\n
Strong resupply (120-175k):  30%\n  Exceptional (155-225k):      15%\n\nFinal percentile estimates:\n  P 1:     57,292\n  P 5:     66,255\n  P10:     73,540\n  P20:     99,991\n  P25:    106,266\n
P30:    110,991\n  P40:    119,064\n  P50:    128,069\n  P60:    137,146\n  P70:    146,382\n  P75:    151,662\n  P80:    158,231\n  P90:    181,138\n  P95:    194,218\n  P99:    211,182\n\nWeighted
mean: 128,723\nWeighted median: 128,069\n80% CI: [73,540 - 181,138]\n50% CI: [106,266 - 151,662]\n", "stderr": "", "duration_ms": 7}
```

## 💬 Response

Now let me run the reflection to checkpoint my reasoning.

## 💭 Thinking

The reflection shows a spread_ratio of 2.26, meaning my distribution is about 2.3x wider than what the factor-weighted implied distribution suggests. This is because my scenarios include more extreme possibilities (supply depletion at 50-90k and exceptional surge at 155-225k) that go beyond what the factor mini-distributions directly imply. This seems justified given the genuine uncertainty about inventory levels.

The implied median from the factors is ~122k, and my tentative estimate is 128k - a gap of ~5.9k (about 12% in the metric). This seems reasonable.

Let me now run the premortem and then submit.

## 💬 Response

The reflection metrics look reasonable. My distribution is wider than the factor-implied range (spread_ratio 2.26) because my scenarios include tail outcomes (severe depletion, exceptional surge) that the individual factor mini-distributions don't fully capture. This is intentional given the genuine uncertainty about unobserved inventory levels.

Let me now run the premortem:
