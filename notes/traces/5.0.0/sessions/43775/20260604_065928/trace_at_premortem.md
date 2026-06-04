# Reasoning Log: How many distinct Russian oil refineries will be publicly reported as struck by Ukrainian drones between June 1, 2026 and June 13, 2026?

*Generated: 2026-06-04T07:17:50.056086+00:00*


## 💭 Thinking

Let me analyze this forecasting question about Ukrainian drone strikes on Russian oil refineries between June 1-13, 2026.

Key aspects:
- Discrete question: How many distinct Russian oil refineries struck by Ukrainian drones
- Window: June 1-13, 2026 (13 days)
- Resolution source: Wikipedia "Timeline of the Russo-Ukrainian war (1 January 2026 – present)"
- Each refinery counted at most once
- Range: -0.5 to 15.5 (open upper bound)
- Published: June 4, 2026 - so we're already 3 days into the window


- Now I need to look at the recent pattern of Ukrainian drone strikes against Russian refineries to establish a baseline for what might happen in the remaining 10 days.

## 💬 Response

I need to forecast the number of distinct Russian oil refineries struck by Ukrainian drones between June 1-13, 2026. Let me start by gathering data on the current tempo of strikes and checking the Wikipedia source.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43775
  ]
}
```

### 📋 Result

```
{"post_id": 43775, "title": "How many distinct Russian oil refineries will be publicly reported as struck by Ukrainian drones between June 1, 2026 and June 13, 2026?", "type": "discrete", "url":
"https://www.metaculus.com/questions/43775", "background_info": "Since 2024, Ukraine has waged an extensive long-range drone campaign against Russian oil refineries, and the tempo has accelerated
sharply in 2026. According to industry data cited by Reuters and summarized by The Moscow Times in mid-May 2026, attacks in early-to-mid May knocked out or significantly cut output at major refineries
including Kirishi (KINEF, offline since May 5), Ryazan (suspended May 15), Moscow (shut May 17), Yaroslavl (YANOS, ~25% capacity), and Nizhny Novgorod (NORSI, hit May 20). Additional strikes were
reported in late May on Syzran (Samara region, May 21), Volgograd (night of May 28\u201329), Novorossiysk's Sheskharis terminal, and others. Combined affected capacity exceeded ~83 million tons/year,
roughly a quarter of Russia's total refining capacity. The Caspian Policy Center's live tracker has logged 61 attacks across 24 refineries since January 2024. The English Wikipedia article 'Timeline
of the Russo-Ukrainian war (1 January 2026 \u2013 present)' maintains a citation-backed day-by-day log of these strikes, naming the targeted refinery in each entry, and is updated within days of
events.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves as the
number of distinct Russian oil refineries (i.e., crude oil refining plants located in the Russian Federation, excluding standalone oil storage depots, pumping stations, chemical plants, and
export/marine terminals) reported as struck by Ukrainian drones on dates between June 1, 2026 and June 13, 2026 inclusive, as listed in the 'Timeline of the Russo-Ukrainian war (1 January 2026 \u2013
present)' Wikipedia article (https://en.wikipedia.org/wiki/Timeline_of_the_Russo-Ukrainian_war_(1_January_2026_%E2%80%93_present)) as of 23:59 UTC on June 13, 2026. Each refinery is counted at most
once regardless of how many times it is struck during the window. For example, if Volgograd, Ryazan, and Saratov refineries are each listed as struck in the window, the answer is 3. A value of 4
refineries would be entered as '4'. If that Wikipedia article is unavailable or omits coverage of this window, the resolver will instead compile the count from [credible
sources](https://www.metaculus.com/faq/#definitions) such as Reuters wire reports on Ukrainian strikes on Russian refineries during the same window.", "fine_print": "A 'strike' means the Wikipedia
entry (or fallback source) reports that Ukrainian drones hit, damaged, or set on fire the refinery or its territory/processing units. Entries reporting only intercepted drones with no impact on a
refinery do not count. If a strike is reported as combining drones with cruise/ballistic missiles, the refinery still counts provided drones are described as part of the attack. Combined oil/gas
processing plants (e.g., Gazprom gas processing facilities) count only if the source describes them as an oil refinery. Refineries in Russian-occupied Ukrainian territory (e.g., Crimea) count as
Russian for this question. Refineries located in Belarus or other non-Russian territory do not count.", "num_forecasters": 3, "community_prediction": null, "lower_bound": -0.5, "upper_bound": 15.5}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/wiki/Timeline_of_the_Russo-Ukrainian_war_(1_January_2026_%E2%80%93_present)",
  "prompt": "Extract all mentions of Ukrainian drone strikes on Russian oil refineries from June 1, 2026 onwards. List each refinery name and date struck. Also look at May 2026 entries for recent strike tempo on refineries."
}
```

### 📋 Result

```
{"title": "Timeline of the Russo-Ukrainian war (1 January 2026 \u2013 present)", "url": "https://en.wikipedia.org/wiki/Timeline_of_the_Russo-Ukrainian_war_(1_January_2026_%E2%80%93_present)",
"extract": "This timeline of the Russo-Ukrainian war covers the period from 1 January 2026 to the present day.", "mode": "full"}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Ukrainian drone strikes Russian oil refineries June 2026 - which refineries have been hit in the first days of June 2026?",
      "ttl": "6h"
    },
    {
      "query": "Ukrainian drone campaign Russian oil refineries May 2026 tempo frequency - how many distinct refineries were struck per week in May 2026?",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Ukrainian drone strikes Russian oil refineries June 2026 - which refineries have been hit in the first days of June 2026?", "entry": {"slug": "ukrainian-drone-strikes-russian-
oil-refineries-jun-2f43a9b4", "query": "Ukrainian drone strikes Russian oil refineries June 2026 - which refineries have been hit in the first days of June 2026?", "answer": "The agent found extensive
cached research data. Let me compile the final report.\n\n---\n\n## Ukrainian Drone Strikes on Russian Oil Refineries \u2014 Early June 2026\n\n### Summary\n\nUkraine's drone campaign against Russian
oil infrastructure has been sustained and escalating throughout 2025\u20132026. While specific June 1\u20134, 2026 individual strike reports were not retrievable via live web sources, cached
intelligence compiled through June 2, 2026 confirms that strikes continued through May 30\u201331 with no cessation or durable ceasefire in effect. The campaign's cumulative impact is massive:
approximately **25% of Russia's refining capacity (~1 million bpd) remains offline** as of late May 2026.\n\n---\n\n### Most Recent Confirmed Strikes (Late May \u2013 Early June 2026)\n\n| Date |
Target | Location | Source |\n|------|--------|----------|--------|\n| May 29\u201330 | Kurganneftoprodukt oil terminal | Kurgan region | ISW |\n| May 29\u201330 | Shadow fleet oil tanker (direct hit)
| Unspecified | ISW |\n| ~May 23 | Sheskharis oil terminal | Novorossiysk, Black Sea | ISW |\n| ~May 23 | Grushova oil depot | Novorossiysk | ISW |\n| May 3 | Primorsk port + shadow fleet tankers |
Baltic Sea | BBC, France 24, Al Jazeera |\n| Late March | Ust-Luga oil terminal (4+ strikes in one week) | Baltic Sea | Reuters |\n| Late March | Primorsk oil terminal (40% storage capacity lost) |
Baltic Sea | Reuters, satellite imagery |\n\nStrikes continued through May 30\u201331 with no pause reported.\n\n---\n\n### Key Refineries Hit in the Broader Campaign (2025\u20132026)\n\n- **21 of
Russia's 38 large refineries** had been struck by October 2025\n- Notable facilities: **Ryazan, Novokuibyshevsk, Syzran, Volgograd** refineries (August 2025)\n- **14 refineries** targeted in August
2025 alone; **8 more** in September 2025\n- **Metafrax Chemicals plant** (Perm Krai) \u2014 struck at **1,700+ km from the frontline**, demonstrating deep-strike capability\n\n---\n\n### Damage &
Production Impact\n\n| Metric | Value | Date |\n|--------|-------|------|\n| Refining capacity offline | ~25% (~1M bpd) | Late May 2026 |\n| Refineries hit (cumulative) | 21 of 38 large refineries |
Oct 2025 |\n| Baltic export capacity shut down (peak) | ~40% | March 2026 |\n| Russian oil production forecast | ~10.2M bpd (lowest since 2009) | IEA 2026 forecast |\n\n**Paradox:** Despite
infrastructure damage, Russia's crude **exports rose** (3.66M bpd seaborne, highest of 2026) because unrefined crude is exported raw at elevated Brent prices (~$107/bbl). Revenue hit \u20ac733M/day in
April 2026 \u2014 highest in 2.5 years.\n\n---\n\n### Domestic Russian Impact\n\n- **Worst fuel crisis since the 1990s**: gasoline rationing in Crimea (20L cap), dry pumps across southern/central
Russia\n- **Near-continuous gasoline export ban** since mid-2025; current ban runs April 1 \u2013 July 31, 2026\n- Senior Russian finance/central bank officials warned Putin that defense spending is
\"unsustainable\" (Bloomberg, June 1, 2026)\n\n---\n\n### Ceasefire Status\n\n- The **Trump-brokered January 2026 energy ceasefire collapsed** by late March 2026\n- Brief holiday ceasefires (Easter,
Victory Day) violated by both sides\n- **No durable energy ceasefire in effect as of June 1, 2026**\n- Ukraine's Defense Minister announced a **\"logistics lockdown\" campaign** on May 27,
2026\n\n---\n\n### Data Gaps\n\nSpecific individual refinery strikes on **June 1\u20134, 2026** could not be confirmed from the available sources. Live web search tools were unavailable. The most
recent confirmed strike activity is from May 30\u201331, 2026, with the operational tempo suggesting continued attacks into June.", "sources": [{"url": "https://www.bloomberg.com", "title": "Bloomberg
\u2014 Russia refinery capacity and crude export tracking", "domain": "bloomberg.com", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Approximately 25% of Russia's refining capacity (~1M bpd)
offline as of late May 2026; seaborne exports reached 3.66M bpd highest of 2026"}, {"url": "https://www.reuters.com", "title": "Reuters \u2014 Primorsk and Ust-Luga port damage reporting", "domain":
"reuters.com", "accessed_at": "2026-06-01T00:00:00Z", "snippet": "Primorsk lost 40% storage capacity; confirmed by satellite imagery April 2, 2026; ~40% of Russia's oil export capacity shut down"},
{"url": "https://www.bbc.com", "title": "BBC \u2014 Ukraine refinery strike campaign coverage", "domain": "bbc.com", "accessed_at": "2026-06-01T00:00:00Z", "snippet": "21 of 38 large Russian
refineries hit by October 2025; 14 targeted in August 2025, 8 in September"}, {"url": "https://www.understandingwar.org", "title": "ISW \u2014 Russia-Ukraine Campaign Assessment, Late May 2026",
"domain": "understandingwar.org", "accessed_at": "2026-06-02T00:00:00Z", "snippet": "Sheskharis terminal, Grushova depot, Kurganneftoprodukt terminal struck; Metafrax plant at 1700km; shadow fleet
tanker directly hit May 29-30"}, {"url": "https://www.iea.org", "title": "IEA \u2014 Russian oil production forecast 2026", "domain": "iea.org", "accessed_at": "2026-06-01T00:00:00Z", "snippet":
"Russian production forecast at ~10.2M bpd in 2026, lowest since 2009"}, {"url": "https://www.france24.com", "title": "France 24 \u2014 Primorsk port strikes May 2026", "domain": "france24.com",
"accessed_at": "2026-06-01T00:00:00Z", "snippet": "New wave of strikes on Primorsk May 3, 2026, targeting port infrastructure and shadow fleet tankers"}, {"url": "https://www.aljazeera.com", "title":
"Al Jazeera \u2014 Ukraine-Russia energy infrastructure attacks", "domain": "aljazeera.com", "accessed_at": "2026-06-01T00:00:00Z", "snippet": "Coverage of Primorsk strikes and shadow fleet targeting
in May 2026"}], "key_facts": ["As of late May 2026, approximately 25% of Russia's total refining capacity (~1 million bpd) remains offline due to Ukrainian drone strikes (Bloomberg, May 27, 2026)",
"21 of Russia's 38 large refineries had been struck by October 2025 (BBC)", "Strikes continued through May 30-31, 2026 with no durable ceasefire in effect", "Kurganneftoprodukt oil terminal struck May
29-30, 2026; a shadow fleet oil tanker was directly hit the same dates (ISW)", "Sheskharis oil terminal and Grushova oil depot (both Novorossiysk, Black Sea) struck around May 23, 2026 (ISW)",
"Primorsk oil terminal lost 40% of storage capacity in late March 2026 strikes (Reuters, satellite imagery)", "Ust-Luga oil terminal attacked at least 4 times in a single week in late March 2026",
"Metafrax Chemicals plant in Perm Krai struck at 1,700+ km from the frontline, demonstrating deep-strike capability", "Despite infrastructure damage, Russia's seaborne crude exports reached 3.66
million bpd (4-week average to May 24, 2026) \u2014 highest of 2026", "Russia's oil export revenue hit EUR 733 million/day in April 2026 \u2014 highest in 2.5 years", "Russia experiencing worst fuel
crisis since the 1990s with gasoline rationing in Crimea (20L cap) and dry pumps across multiple regions", "Gasoline export ban in effect April 1 \u2013 July 31, 2026 (near-continuous since
mid-2025)", "Trump-brokered January 2026 energy ceasefire collapsed by late March 2026", "IEA forecasts Russian oil production at ~10.2 million bpd in 2026 \u2014 lowest since 2009", "Ukraine's
Defense Minister announced a 'logistics lockdown' campaign on May 27, 2026", "Shadow fleet carried a record 54% of Russia's fossil fuel exports", "India's Russian crude imports up ~70% since February
2026, reaching ~1.85 million bpd", "Specific individual June 1-4, 2026 strike targets could not be confirmed from available sources; most recent confirmed activity is May 30-31"], "data_points":
[{"metric": "Russian refining capacity offline", "value": 25.0, "unit": "percent (~1M bpd)", "as_of": "2026-05-27", "source_url": "https://www.bloomberg.com"}, {"metric": "Large Russian refineries
struck (cumulative)", "value": 21.0, "unit": "of 38 total", "as_of": "2025-10-01", "source_url": "https://www.bbc.com"}, {"metric": "Russia seaborne crude exports (4-week avg)", "value": 3.66, "unit":
"million bpd", "as_of": "2026-05-24", "source_url": "https://www.bloomberg.com"}, {"metric": "Russia oil export revenue", "value": 733.0, "unit": "EUR million/day", "as_of": "2026-04-30",
"source_url": "https://www.bloomberg.com"}, {"metric": "Brent crude price", "value": 107.0, "unit": "USD/barrel", "as_of": "2026-05-27", "source_url": "https://www.bloomberg.com"}, {"metric": "IEA
forecast Russian oil production 2026", "value": 10.2, "unit": "million bpd", "as_of": "2026-05-01", "source_url": "https://www.iea.org"}, {"metric": "Primorsk storage capacity lost", "value": 40.0,
"unit": "percent", "as_of": "2026-04-02", "source_url": "https://www.reuters.com"}, {"metric": "Baltic oil export capacity shut down (peak)", "value": 40.0, "unit": "percent", "as_of": "2026-03-31",
"source_url": "https://www.reuters.com"}, {"metric": "Shadow fleet share of Russian fossil fuel exports", "value": 54.0, "unit": "percent (record)", "as_of": "2026-05-24", "source_url":
"https://www.bloomberg.com"}, {"metric": "India Russian crude imports", "value": 1.85, "unit": "million bpd", "as_of": "2026-05-24", "source_url": "https://www.bloomberg.com"}, {"metric": "Refineries
targeted in August 2025", "value": 14.0, "unit": "refineries", "as_of": "2025-08-31", "source_url": "https://www.bbc.com"}, {"metric": "Refineries targeted in September 2025", "value": 8.0, "unit":
"refineries", "as_of": "2025-09-30", "source_url": "https://www.bbc.com"}, {"metric": "Brent crude YoY price increase", "value": 66.0, "unit": "percent", "as_of": "2026-05-27", "source_url":
"https://www.bloomberg.com"}], "created_at": "2026-06-04T07:03:25.429881Z", "updated_at": "2026-06-04T07:03:25.429881Z", "stale_after": "2026-06-04T13:03:25.429881Z", "state": "fresh",
"revision_history": [], "session_id": "61d0fbcd-6e72-464c-9ade-0b7d3ec2abd1", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Ukrainian drone campaign Russian oil refineries May 2026 tempo
frequency - how many distinct refineries were struck per week in May 2026?", "entry": {"slug": "ukrainian-drone-campaign-russian-oil-refineries-ma-b5d84bc9", "query": "Ukrainian drone campaign Russian
oil refineries May 2026 tempo frequency - how many distinct refineries were struck per week in May 2026?", "answer": "Now I have comprehensive findings. Let me compile the final research
report.\n\n---\n\n# Ukrainian Drone Campaign Against Russian Oil Refineries \u2014 May 2026: Tempo & Frequency\n\n## Executive Summary\n\nThe Ukrainian drone campaign against Russian oil refineries
and energy infrastructure continued at a **sustained but unevenly documented tempo throughout May 2026**. Based on available reporting from ISW daily assessments, Reuters, Bloomberg, BBC, and other
sources, **at least 5\u20136 distinct oil infrastructure facilities were confirmed struck in May 2026**, spread across at least 3 of the month's 4+ weeks. However, **a precise week-by-week count of
all distinct refineries/terminals struck is not available from any single public tracker** \u2014 the true number is almost certainly higher than what is documented, as many strikes go unreported or
are only confirmed days later via satellite imagery.\n\n---\n\n## Confirmed Oil Infrastructure Strikes in May 2026\n\n| Date | Facility | Location | Type | Source
|\n|------|----------|----------|------|--------|\n| **~May 3** | Primorsk oil export terminal + shadow fleet tankers | Leningrad Oblast (Baltic) | Export port & tankers | BBC, France 24, CBS News, Al
Jazeera |\n| **May 23** | Sheskharis oil terminal | Novorossiysk (Black Sea) | Export terminal (75M t/yr capacity) | ISW May 23 assessment |\n| **May 23** | Grushova oil depot | Novorossiysk (Black
Sea) | Oil depot | ISW May 23 assessment |\n| **May 23** | Metafrax Chemicals plant | Perm Krai (>1,700 km from frontline) | Petrochemical plant | ISW May 23 assessment |\n| **May 29\u201330** |
Kurganneftoprodukt oil terminal | Kurgan Oblast | Oil terminal | ISW May 30 assessment |\n| **May 29\u201330** | Shadow fleet oil tanker | Near Taganrog | Tanker at sea/port | ISW May 30 assessment
|\n\n### Weekly Distribution of Confirmed Strikes\n\n| Week | Dates | Confirmed Distinct Targets | Notes |\n|------|-------|---------------------------|-------|\n| **Week 1** | May 1\u20137 | **1**
(Primorsk + tankers) | Major escalation: first direct targeting of shadow fleet tankers |\n| **Week 2** | May 8\u201314 | **0 confirmed** | Victory Day ceasefire (May 5\u201310), though violated;
likely underreported |\n| **Week 3** | May 15\u201321 | **0 confirmed** | ISW assessments for this period not cached; strikes likely ongoing but undocumented in available sources |\n| **Week 4** | May
22\u201328 | **3** (Sheskharis, Grushova, Metafrax) | ISW assessments available; targets span Black Sea to Urals |\n| **Week 5** | May 29\u201331 | **2** (Kurganneftoprodukt, shadow tanker) | Strikes
continued through month's end |\n\n**Important caveat:** ISW daily assessments for May 1\u201321 were not available in the research cache. Only May 22\u2013June 1 assessments were accessible. The true
strike count for weeks 1\u20133 is almost certainly higher than documented above.\n\n---\n\n## Cumulative Campaign Context\n\n| Metric | Value | As Of | Source
|\n|--------|-------|-------|--------|\n| Russian refining capacity offline | ~25% (~1M bpd) | End of May 2026 | Bloomberg, May 27 |\n| Large refineries struck (cumulative) | 21 of 38 | October 2025 |
BBC |\n| Primorsk storage capacity destroyed | 40% | April 2, 2026 | Reuters |\n| Oil export capacity halted (March peak) | ~40% | March 25, 2026 | Reuters |\n| Seaborne crude exports (4-week avg) |
3.66M bpd (2026 high) | May 24, 2026 | Bloomberg |\n| Fossil fuel export revenue | \u20ac733M/day (2.5-year high) | April 2026 | CREA |\n| Shadow fleet share of exports | 54% (record) | April 2026 |
CREA |\n| Gasoline export ban | Active (Apr 1 \u2013 Jul 31, 2026) | Current | Russian gov't decree |\n| IEA forecast Russian oil production | ~10.2M bpd (lowest since 2009) | 2026 forecast | IEA
|\n\n---\n\n## Key Qualitative Findings\n\n- **No durable ceasefire** was in effect during May 2026. The Trump-brokered January 2026 energy ceasefire collapsed by late March. Brief holiday ceasefires
(Victory Day, May 5\u201310) were violated by both sides.\n- **Unprecedented range**: Ukrainian drones demonstrated the ability to strike targets **over 1,700 km from the frontline** (Metafrax
Chemicals in Perm Krai), indicating significant improvements in drone range and navigation.\n- **\"Logistics lockdown\" doctrine**: Ukrainian Defense Minister Fedorov announced on May 27 a strategic
\"logistics lockdown\" targeting Russian ground lines of communication across the entire theater, with oil infrastructure as a key component.\n- **Paradox of increased crude exports**: Damaged
refineries actually *increased* crude exports because crude that cannot be refined domestically is redirected for export. India's Russian crude imports surged ~70% since February 2026.\n- **Domestic
fuel crisis**: Russia's fuel crisis is described as the worst since the 1990s, with rationing (20 liters per customer in Crimea), dry pumps, gas station closures, and a near-continuous gasoline export
ban since mid-2025.\n\n---\n\n## Data Gaps\n\n1. **ISW assessments for May 1\u201321** are not available in cached sources \u2014 these would likely reveal additional oil infrastructure strikes in
weeks 1\u20133.\n2. **No comprehensive public OSINT tracker** exists that logs every individual refinery/terminal strike with dates. The closest sources are ISW daily assessments and Ukrainian General
Staff daily reports.\n3. **Total drone counts per attack** on oil infrastructure in May 2026 are not reported (though the Russian retaliatory strike on Ukraine on May 23\u201324 used 90 missiles and
600 drones).\n4. **The true weekly strike rate is almost certainly higher** than the 1\u20133 distinct targets/week documented above, given reporting lags and operational security.\n\n---\n\n##
Sources\n\n- ISW Daily Assessments (May 22\u2013June 1, 2026) \u2014 understandingwar.org\n- Reuters \u2014 Multiple articles on refinery strikes, port damage, export capacity\n- Bloomberg (May 27,
2026) \u2014 Tanker tracking, crude export data\n- BBC \u2014 Cumulative refinery strike count (21 of 38)\n- The Guardian \u2014 Fuel crisis reporting\n- CREA (Centre for Research on Energy and Clean
Air) \u2014 Revenue and shadow fleet data\n- France 24, CBS News, Al Jazeera \u2014 Primorsk/shadow fleet strike reporting (May 3)\n- Washington Post, Japan Today \u2014 Continuing strikes late May
2026", "sources": [{"url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-may-23-2026/", "title": "ISW Russian Offensive Campaign Assessment, May 23,
2026", "domain": "understandingwar.org", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Documents Ukrainian strikes on Sheskharis oil terminal, Grushova oil depot (Novorossiysk), and Metafrax
Chemicals plant (Perm Krai, >1,700 km from frontline)"}, {"url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-may-30-2026/", "title": "ISW Russian
Offensive Campaign Assessment, May 30, 2026", "domain": "understandingwar.org", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Documents destruction of Kurganneftoprodukt oil terminal and a shadow
fleet oil tanker near Taganrog"}, {"url": "https://www.bloomberg.com/news/articles/2026-05-27/russia-boosts-crude-oil-exports-to-cash-in-on-middle-east-war", "title": "Russia Boosts Crude Oil Exports
to Cash In on Middle East War", "domain": "bloomberg.com", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Reports ~25% of Russian refining capacity offline; seaborne crude exports at 3.66M bpd
4-week average as of May 24"}, {"url": "https://www.reuters.com/business/energy/least-40-russias-oil-export-capacity-halted-reuters-calculations-show-2026-03-25/", "title": "At least 40% of Russia's
oil export capacity halted, Reuters calculations show", "domain": "reuters.com", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Documents ~40% of Russian oil export capacity halted following
Ukrainian strikes on Baltic ports; Primorsk lost 40% of storage capacity confirmed by satellite"}, {"url": "https://www.bbc.com/news/articles/czx020k4056o", "title": "BBC: 21 of Russia's 38 large
refineries struck by Ukrainian drones", "domain": "bbc.com", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Cumulative count of 21 of 38 large Russian refineries struck as of October 2025"},
{"url": "https://energyandcleanair.org/", "title": "CREA - Centre for Research on Energy and Clean Air", "domain": "energyandcleanair.org", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Reports
EUR 733M/day Russian fossil fuel export revenue in April 2026; 54% shadow fleet share (record)"}, {"url": "https://www.theguardian.com/world/2025/aug/27/frustrated-russians-grapple-with-fuel-crisis-
as-ukraine-attacks-oil-refineries", "title": "Frustrated Russians grapple with fuel crisis as Ukraine attacks oil refineries", "domain": "theguardian.com", "accessed_at": "2026-06-04T00:00:00Z",
"snippet": "Documents Ryazan refinery strike and emerging domestic fuel crisis in Russia"}, {"url": "https://www.reuters.com/business/energy/parts-russia-face-gasoline-shortages-after-ukraine-struck-
refineries-2025-08-21/", "title": "Parts of Russia face gasoline shortages after Ukraine struck refineries", "domain": "reuters.com", "accessed_at": "2026-06-04T00:00:00Z", "snippet": "Reports 14
refineries struck in August 2025 including Novokuibyshevsk, Syzran, and Volgograd"}], "key_facts": ["At least 5-6 distinct Russian oil infrastructure facilities were confirmed struck by Ukrainian
drones in May 2026: Primorsk port (~May 3), Sheskharis terminal (May 23), Grushova depot (May 23), Metafrax Chemicals (May 23), Kurganneftoprodukt terminal (May 29-30), and a shadow fleet tanker (May
29-30).", "The confirmed weekly rate of distinct facilities struck ranged from 0-3 per week, but this is a lower bound \u2014 ISW daily assessments for May 1-21 were unavailable, so weeks 1-3 are
significantly underreported.", "Approximately 25% of Russia's total refining capacity (~1 million barrels per day) remained offline throughout May 2026 due to cumulative drone strike damage
(Bloomberg, May 27).", "By October 2025, 21 of Russia's 38 large refineries had been struck at least once (BBC), and the campaign continued through May 2026 without cessation.", "Ukrainian drones
demonstrated unprecedented range in May 2026, striking the Metafrax Chemicals plant in Perm Krai over 1,700 km from the frontline.", "Ukraine struck shadow fleet oil tankers directly for the first
time on ~May 3 at Primorsk, marking a significant escalation.", "No durable ceasefire was in effect \u2014 the January 2026 Trump-brokered energy ceasefire collapsed by late March; Victory Day
ceasefire (May 5-10) was violated.", "Despite refinery damage, Russia's seaborne crude exports hit a 2026 high of 3.66M bpd (4-week average as of May 24) because unrefined crude was redirected to
export.", "Russia's domestic fuel crisis was described as the worst since the 1990s, with gasoline rationing, dry pumps, and a continuous gasoline export ban (April 1 - July 31, 2026).", "Ukrainian
Defense Minister Fedorov announced a 'logistics lockdown' strategy on May 27, targeting Russian ground lines of communication including oil infrastructure.", "No comprehensive public OSINT tracker
exists that logs every individual refinery/terminal strike by date; ISW daily assessments and Ukrainian General Staff reports are the closest available sources."], "data_points": [{"metric": "Russian
refining capacity offline", "value": 25.0, "unit": "percent (~1M bpd)", "as_of": "2026-05-31", "source_url": "https://www.bloomberg.com/news/articles/2026-05-27/russia-boosts-crude-oil-exports-to-
cash-in-on-middle-east-war"}, {"metric": "Large refineries struck cumulatively (of 38 total)", "value": 21.0, "unit": "refineries", "as_of": "2025-10-31", "source_url":
"https://www.bbc.com/news/articles/czx020k4056o"}, {"metric": "Confirmed distinct oil facilities struck in May 2026 (lower bound)", "value": 6.0, "unit": "facilities", "as_of": "2026-05-31",
"source_url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-may-30-2026/"}, {"metric": "Russian seaborne crude exports (4-week average)", "value": 3.66,
"unit": "million bpd", "as_of": "2026-05-24", "source_url": "https://www.bloomberg.com/news/articles/2026-05-27/russia-boosts-crude-oil-exports-to-cash-in-on-middle-east-war"}, {"metric": "Russian
fossil fuel export revenue", "value": 733.0, "unit": "EUR million per day", "as_of": "2026-04-30", "source_url": "https://energyandcleanair.org/"}, {"metric": "Shadow fleet share of Russian oil
exports", "value": 54.0, "unit": "percent", "as_of": "2026-04-30", "source_url": "https://energyandcleanair.org/"}, {"metric": "Primorsk storage capacity destroyed", "value": 40.0, "unit": "percent",
"as_of": "2026-04-02", "source_url": "https://www.reuters.com/business/energy/least-40-russias-oil-export-capacity-halted-reuters-calculations-show-2026-03-25/"}, {"metric": "Russian oil export
capacity halted (March peak)", "value": 40.0, "unit": "percent", "as_of": "2026-03-25", "source_url": "https://www.reuters.com/business/energy/least-40-russias-oil-export-capacity-halted-reuters-
calculations-show-2026-03-25/"}, {"metric": "Maximum confirmed drone strike range (Metafrax, Perm Krai)", "value": 1700.0, "unit": "km from frontline", "as_of": "2026-05-23", "source_url":
"https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-may-23-2026/"}, {"metric": "IEA forecast Russian oil production for 2026", "value": 10.2, "unit": "million
bpd (lowest since 2009)", "as_of": "2026-05-31", "source_url": "https://www.reuters.com/business/energy/"}], "created_at": "2026-06-04T07:06:07.216635Z", "updated_at": "2026-06-04T07:06:07.216635Z",
"stale_after": "2026-06-04T13:06:07.216635Z", "state": "fresh", "revision_history": [], "session_id": "052ced4d-1294-43e2-9eb1-675926377df9", "follow_up_count": 0}, "is_follow_up": false}],
"successful_count": 2, "failed_count": 0}
```

## 💬 Response

Now let me get more specific data on the question description's referenced strikes and check the Wikipedia article more carefully, plus look for the most recent data on early June strikes.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Ukrainian drone strike Russian oil refinery June 2026"
}
```

### 📋 Result

```
{"query": "Ukrainian drone strike Russian oil refinery June 2026", "results": [{"title": "Drone Strike Sets Ilsky Oil Refinery in Russia Ablaze", "url": "https://militarnyi.com/en/news/drone-strike-
sets-ilsky-oil-refinery-in-russia-ablaze/", "snippet": "In Russia, the Ilsky oil refinery in the Krasnodar region is on fire after being hit by Ukrainian drones.\nThe
[Exilenova+](https://t.me/exilenova_plus/21661?single) Telegram channel shared a video showing the fire at the refinery.\nEyewitnesses started reporting the strike on social media after 3 a.m. on June
2, describing numerous explosions in the area.\nVideos and photos from local residents show a large fire and thick plumes of smoke rising from the oil refinery. The fire is visible from nearb",
"api_data": null, "hint": null}, {"title": "Ukrainian drone attacks hit multiple Russian targets, including refinery | News | Al Jazeera", "url":
"https://www.aljazeera.com/amp/news/2026/5/31/ukrainian-drone-attacks-hit-multiple-russian-targets-including-refinery", "snippet": "Ukrainian drone attacks hit multiple Russian targets, including
refinery\nSaratov refinery hit as Ukrainian strikes intensify across Russian regions, damaging civilian infrastructure.\nUkrainian drones have struck energy and industrial targets across several
Russian regions, Russian authorities say, in an escalating campaign of strikes against infrastructure.\nIn Saratov, a region on the Volga River with several oil refineries that has come under regular
Ukrainian attack in recent years, Governor R", "api_data": null, "hint": null}, {"title": "Ukrainian drones strike Russian oil refinery, Kyiv says", "url":
"https://www.euronews.com/2026/05/21/ukraine-strikes-russian-oil-refinery-in-long-range-drone-attack-kyiv-says", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2895449)\nUkraine has
been ramping up its retaliatory long-range strikes on Russia in recent weeks, particularly targeting oil infrastructure.\nUkrainian forces have carried out a long-range drone strike on a Russian oil
refinery, Ukrainian President Volodymyr Zelenskyy and the military said on Thursday.\nPosting on X, Zelenskyy said his forces had struck the Syzran oil refinery in western Russia, sharing video
footage showing flames and black smo", "api_data": null, "hint": null}, {"title": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows | Russia-Ukraine war News | Al Jazeera",
"url": "https://www.aljazeera.com/news/2026/5/30/ukraine-drones-strike-russian-oil-facility-as-kyiv-and-moscow-trade-blows", "snippet": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow
trade blows\nStrikes have seen 13,000 residents without power in Zaporizhzhia as Russia and Ukraine trade drone attacks.\n![A Ukraine-made P1-Sun drone operated by servicemen of the 116th Mechanised
Brigade to intercept Russian 'Shahed' type, and other strike or reconnaissance drones [FILE: Yevhen Titov/ EPA]](/wp-
content/uploads/2026/05/14004194-1780124557.jpg?resize=770%2C513&quality=80)\nUkraine has launched coordinated drone attacks", "api_data": null, "hint": null}, {"title": "Russia strikes Ukraine with
drones, missiles in major attack; 11 dead, scores hurt | The Times of Israel", "url": "https://www.timesofisrael.com/russia-strikes-ukraine-with-drones-missiles-in-major-attack-11-dead-scores-
hurt/amp/", "snippet": null, "api_data": null, "hint": null}, {"title": "Ukrainian long range drones strike Lukoil refinery deep inside Russia - YouTube", "url":
"https://www.youtube.com/watch?v=TQUB91ISzno", "snippet": "Pr\u00e9sentation\nPresse\nDroits d'auteur\nNous contacter\nCr\u00e9ateurs\nPublicit\u00e9\nD\u00e9veloppeurs\nR\u00e9silier vos
abonnements\nConditions d'utilisation\nConfidentialit\u00e9\nR\u00e8gles et s\u00e9curit\u00e9\nPremiers pas sur YouTube\nTester de nouvelles fonctionnalit\u00e9s\n\u00a9 2026 Google LLC", "api_data":
null, "hint": null}]}
```

```json
{
  "query": "\"oil refinery\" Ukraine drone strike Russia June 1 2 3 4 2026"
}
```

### 📋 Result

```
{"query": "\"oil refinery\" Ukraine drone strike Russia June 1 2 3 4 2026", "results": [{"title": "Ukrainian Drones Hit Ilsky Oil Refinery for 16th Time: June 2026 | war | informed, clearly", "url":
"https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026", "snippet": "Ukraine Strikes Key Russian Oil Refinery in Latest Deep-Strike Campaign\nUkrainian drones struck the
Ilsky oil refinery in Russia's Krasnodar region overnight on June 2, 2026, igniting a large fire at one of southern Russia's largest fuel processing facilities. The attack marks the 16th time the
refinery has been targeted since the full-scale invasion began, as Kyiv intensifies its campaign to disrupt Russian energy infrastructure and military logistics. The strike on the Ilsky refinery,
located ", "api_data": null, "hint": null}, {"title": "Ukrainian drone attacks hit multiple Russian targets, including refinery | News | Al Jazeera", "url":
"https://www.aljazeera.com/amp/news/2026/5/31/ukrainian-drone-attacks-hit-multiple-russian-targets-including-refinery", "snippet": "Ukrainian drone attacks hit multiple Russian targets, including
refinery\nSaratov refinery hit as Ukrainian strikes intensify across Russian regions, damaging civilian infrastructure.\nUkrainian drones have struck energy and industrial targets across several
Russian regions, Russian authorities say, in an escalating campaign of strikes against infrastructure.\nIn Saratov, a region on the Volga River with several oil refineries that has come under regular
Ukrainian attack in recent years, Governor R", "api_data": null, "hint": null}, {"title": "Ukrainian Drones Strike Oil Refinery Deep Inside Russia", "url": "https://www.rferl.org/a/ukrainian-drones-
strike-oil-refinery-deep-inside-russia/33761797.html", "snippet": null, "api_data": null, "hint": null}, {"title": "Ukrainian long range drones strike Lukoil refinery deep inside Russia - YouTube",
"url": "https://www.youtube.com/watch?v=TQUB91ISzno", "snippet": "Pr\u00e9sentation\nPresse\nDroits d'auteur\nNous contacter\nCr\u00e9ateurs\nPublicit\u00e9\nD\u00e9veloppeurs\nR\u00e9silier vos
abonnements\nConditions d'utilisation\nConfidentialit\u00e9\nR\u00e8gles et s\u00e9curit\u00e9\nPremiers pas sur YouTube\nTester de nouvelles fonctionnalit\u00e9s\n\u00a9 2026 Google LLC", "api_data":
null, "hint": null}, {"title": "Major Russian missile, drone attack on Ukraine kills at least 22, topples apartment building, officials say - CBS News", "url": "https://www.cbsnews.com/news/russia-
ukraine-war-major-attacks-missile-drone-kill-several-wound-dozens/", "snippet": "Major Russian missile, drone attack on Ukraine kills at least 22, topples apartment building, officials say\nA barrage
of Russian missiles and drone strikes killed at least 22 civilians and wounded more than 100 people across Ukraine, authorities said Tuesday, just days after Ukrainian President Volodymyr [Zelenskyy
warned that Moscow](https://www.cbsnews.com/news/zelenskyy-ukraine-bracing-for-russia-attacks/) was preparing a \"massive new strike.\"\nZelenskyy called the latest attack \"a brutal stri",
"api_data": null, "hint": null}, {"title": "Ukraine strikes Russian oil refinery in long-range drone attack, Kyiv says | Euronews", "url": "https://www.euronews.com/2026/05/21/ukraine-strikes-russian-
oil-refinery-in-long-range-drone-attack-kyiv-says", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2895449)\nUkraine has been ramping up its retaliatory long-range strikes on Russia
in recent weeks, particularly targeting oil infrastructure.\nUkrainian forces have carried out a long-range drone strike on a Russian oil refinery, Ukrainian President Volodymyr Zelenskyy and the
military said on Thursday.\nPosting on X, Zelenskyy said his forces had struck the Syzran oil refinery in western Russia, sharing video footage showing flames and black smo", "api_data": null, "hint":
null}, {"title": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows | Russia-Ukraine war News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/5/30/ukraine-drones-
strike-russian-oil-facility-as-kyiv-and-moscow-trade-blows", "snippet": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows\nStrikes have seen 13,000 residents without power in
Zaporizhzhia as Russia and Ukraine trade drone attacks.\n![A Ukraine-made P1-Sun drone operated by servicemen of the 116th Mechanised Brigade to intercept Russian 'Shahed' type, and other strike or
reconnaissance drones [FILE: Yevhen Titov/ EPA]](/wp-content/uploads/2026/05/14004194-1780124557.jpg?resize=770%2C513&quality=80)\nUkraine has launched coordinated drone attacks", "api_data": null,
"hint": null}]}
```

```json
{
  "query": "Wikipedia \"Timeline of the Russo-Ukrainian war\" June 2026 refinery"
}
```

### 📋 Result

```
{"query": "Wikipedia \"Timeline of the Russo-Ukrainian war\" June 2026 refinery", "results": [{"title": "Timeline of the Russo-Ukrainian war (1 January 2026 \u2013 present) - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Timeline_of_the_Russo-Ukrainian_war_(1_January_2026_%E2%80%93_present)", "snippet": "This timeline of the Russo-Ukrainian war covers the period from 1 January 2026 to
the present day.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Timeline of the Russo-Ukrainian war (1 January 2026 \\u2013 present)\", \"url\":
\"https://en.wikipedia.org/wiki/Timeline_of_the_Russo-Ukrainian_war_(1_January_2026_%E2%80%93_present)\", \"extract\": \"This timeline of the Russo-Ukrainian war covers the period from 1 January 2026
to the present day.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russo-Ukrainian war - Wikipedia", "url": "https://en.wikipedia.org/wiki/Russo-Ukrainian_war", "snippet": "The Russo-Ukrainian
war began in February 2014 and is ongoing. Following Ukraine's Revolution of Dignity, Russia occupied Crimea and annexed it from Ukraine. It then supported Russian separatist armed groups who started
a war in the eastern Donbas region against Ukraine's military. In 2018, Ukraine declared the region to be occupied by Russia. The first eight years of conflict also involved naval incidents and
cyberwarfare. In February 2022, Russia launched a full-scale invasion of Ukraine and b", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Russo-Ukrainian war\", \"url\":
\"https://en.wikipedia.org/wiki/Russo-Ukrainian_war\", \"extract\": \"The Russo-Ukrainian war began in February 2014 and is ongoing. Following Ukraine's Revolution of Dignity, Russia occupied Crimea
and annexed it from Ukraine. It then supported Russian separatist armed groups who started a war in the eastern Donbas region against Ukraine's military. In 2018, Ukraine declared the region to be
occupied by Russia. The first eight years of conflict also involved naval incidents and cyberwarfare. In February 2022, Russia launched a full-scale invasion of Ukraine and began occupying more of the
country, starting the current phase of the war, the biggest conflict in Europe since World War II. The war has resulted in a refugee crisis and hundreds of thousands of deaths.\\nIn early 2014, the
Euromaidan protests led to the Revolution of Dignity and the ousting of Ukraine's pro-Russian president Viktor Yanukovych. Immediately after, unmarked Russian troops occupied Crimea. In March 2014,
Russia annexed Crimea after an illegitimate referendum. Meanwhile, pro-Russian protests began in parts of southeastern Ukraine. In April 2014, Russian-backed militants seized towns and cities in
Ukraine's eastern Donbas region and proclaimed the Donetsk People's Republic (DPR) and the Luhansk People's Republic (LPR) as independent states, starting the Donbas war. Russia covertly supported the
separatists with its own troops, tanks and artillery, preventing Ukraine from fully retaking the territory. The International Criminal Court (ICC) judged that the war was both a national and
international armed conflict involving Russia, and the European Court of Human Rights judged that Russia controlled the DPR and LPR from 2014 onward. In February 2015, Russia and Ukraine signed the
Minsk II agreements, but they were never fully implemented in the following years. The Donbas war became a static conflict likened to trench warfare; ceasefires were repeatedly broken but the
frontlines did not move.\\nBeginning in 2021, there was a massive Russian military buildup near Ukraine's borders, including within neighbouring Belarus. Russian officials repeatedly denied plans to
attack Ukraine. Russia's president Vladimir Putin voiced expansionist views and challenged Ukraine's right to exist. He demanded that Ukraine be barred from ever joining the NATO military alliance.
Ukraine had been officially a neutral country when the conflict began, but because of Russia's attacks it revived plans to join NATO. In early 2022, Russia recognised the DPR and LPR as independent
states. While Russian troops surrounded Ukraine, its proxies stepped up attacks on Ukrainian forces in the Donbas.\\nOn 24 February 2022, Putin announced a \\\"special military operation\\\" to
\\\"demilitarize and denazify\\\" Ukraine, claiming Russia had no plans to occupy the country. The Russian invasion that followed was internationally condemned; many countries imposed sanctions
against Russia, and sent humanitarian and military aid to Ukraine. In the face of fierce resistance, Russia abandoned an attempt to seize Kyiv in early April. In August, Ukrainian forces began
liberating territories in the north-east and south. In September, Russia declared the annexation of four partially occupied provinces, which was internationally condemned. Since then, Russian
offensives and Ukrainian counteroffensives have gained only small amounts of territory. The invasion has also led to attacks in Russia by Ukrainian and Ukrainian-backed forces, among them a cross-
border offensive into Russia's Kursk region in August 2024. Russia has repeatedly carried out deliberate and indiscriminate attacks on civilians far from the frontline. The UN Human Rights Office
reported that Russia was committing severe human rights violations in occupied Ukraine. The ICC opened an investigation into war crimes and issued arrest warrants for Putin and several other Russian
officials. Russia has repeatedly refused calls for a ceasefire.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Outline of the Russo-Ukrainian war - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Outline_of_the_Russo-Ukrainian_war", "snippet": "The following outline is provided as an overview of and topical guide to the Russo-Ukrainian war.\nThe war is an ongoing
international conflict between Russia (alongside Russian-backed separatists) and Ukraine which began in February 2014. Following Ukraine's Revolution of Dignity, Russia annexed Ukrainian Crimea and
supported pro-Russian separatists fighting the Ukrainian military in the Donbas war. The first eight years of conflict included naval incidents, cyberwarfare, and heightened politica", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"Outline of the Russo-Ukrainian war\", \"url\": \"https://en.wikipedia.org/wiki/Outline_of_the_Russo-Ukrainian_war\", \"extract\": \"The following
outline is provided as an overview of and topical guide to the Russo-Ukrainian war.\\nThe war is an ongoing international conflict between Russia (alongside Russian-backed separatists) and Ukraine
which began in February 2014. Following Ukraine's Revolution of Dignity, Russia annexed Ukrainian Crimea and supported pro-Russian separatists fighting the Ukrainian military in the Donbas war. The
first eight years of conflict included naval incidents, cyberwarfare, and heightened political tensions. In February 2022, Russia launched a full-scale invasion of Ukraine in a major escalation of the
conflict.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "War in Ukraine | Global Conflict Tracker", "url": "https://www.cfr.org/global-conflict-tracker/conflict/conflict-ukraine", "snippet":
"Four years since Russia\u2019s February 2022 full-scale invasion of Ukraine, Russia still occupies roughly 20 percent of the country after gaining almost [five thousand square
kilometers](https://www.bbc.com/news/articles/c0l0k4389g2o) of territory in 2025. Russia continues to [bombard](https://www.voanews.com/a/russia-says-it-is-advancing-toward-flashpoint-ukrainian-
city/7959302.html) Ukrainian cities, while Ukraine maintains [drone attacks](https://united24media.com/latest-news/revealed-full-list-o", "api_data": null, "hint": null}, {"title": "Russia-Ukraine War
| Map, Casualties, Timeline, Death Toll, Causes, & Significance | Britannica", "url": "https://www.britannica.com/event/Russia-Ukraine-War", "snippet": "[Russia-Ukraine
War](https://cdn.britannica.com/25/236625-050-69AADC7C/Russia-Ukraine-War-residential-building-damaged-by-a-missile-February-25-2022-in-Kyiv-Ukraine.jpg)A child on a swing outside an apartment
building damaged by a Russian missile in Kyiv, Ukraine, February 25, 2022.\nRussia-Ukraine War\nWhy did Vladimir Putin invade Ukraine in 2022?\nWhat are the military casualty estimates for the Russia-
Ukraine War?\nHow many civilians have died since Russia\u2019s invasion of Ukraine?\nWhen did the Rus", "api_data": null, "hint": null}, {"title": "How Ukraine Turned the War Back on Russia: A
Timeline \u2014 UNITED24 Media", "url": "https://united24media.com/war-in-ukraine/how-ukraine-turned-the-war-back-on-russian-soil-a-timeline-17571", "snippet": "How Ukraine Turned the War Back on
Russian Soil: A Timeline\nRussia is routinely hit by deep strikes; Ukraine is now capable of mass-launching drones, creating its own long-range missiles, and firing them at Russian military and oil
infrastructure. Four years ago, this would have been unthinkable.\n\u201cNo region of Russia can feel safe\u201d due to Ukrainian drones, including the Ural region, Russian Security Council Secretary
Sergei Shoigu said in 2026. Russia is too large to defend against Ukrainian str", "api_data": null, "hint": null}, {"title": "Ryazan refinery - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Ryazan_refinery", "snippet": "The Ryazan Refinery (Russian: \u0420\u044f\u0437\u0430\u043d\u0441\u043a\u0438\u0439
\u043d\u0435\u0444\u0442\u0435\u043f\u0435\u0440\u0435\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u044e\u0449\u0438\u0439 \u0437\u0430\u0432\u043e\u0434\u0437) is an oil refinery in the Russian
city of Ryazan, one of the largest in the country. This refinery has belonged to the Russian state-owned company Rosneft since 2013.", "api_data": {"content": [{"type": "text", "text": "{\"title\":
\"Ryazan refinery\", \"url\": \"https://en.wikipedia.org/wiki/Ryazan_refinery\", \"extract\": \"The Ryazan Refinery (Russian: \\u0420\\u044f\\u0437\\u0430\\u043d\\u0441\\u043a\\u0438\\u0439
\\u043d\\u0435\\u0444\\u0442\\u0435\\u043f\\u0435\\u0440\\u0435\\u0440\\u0430\\u0431\\u0430\\u0442\\u044b\\u0432\\u0430\\u044e\\u0449\\u0438\\u0439 \\u0437\\u0430\\u0432\\u043e\\u0434\\u0437) is an
oil refinery in the Russian city of Ryazan, one of the largest in the country. This refinery has belonged to the Russian state-owned company Rosneft since 2013.\", \"mode\": \"full\"}"}]}, "hint":
null}, {"title": "War in Ukraine - The Washington Post", "url": "https://www.washingtonpost.com/world/ukraine-russia/", "snippet": null, "api_data": null, "hint": null}, {"title": "Russo-Ukrainian war
(2022\u2013present) - Wikipedia", "url": "https://en.wikipedia.org/wiki/Russian_invasion_of_Ukraine", "snippet": "On 24 February 2022, Russia invaded Ukraine, starting the largest and deadliest war in
Europe since World War II, in a major escalation of the existing war between the two countries that began when Russia attacked Ukraine in 2014. The fighting has caused hundreds of thousands of
military casualties and tens of thousands of Ukrainian civilian casualties. As of June 2026, Russian troops occupy roughly 20% of Ukraine. From a population of 41 million, about 8 million Ukrainians
have been internally ", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Russo-Ukrainian war (2022\\u2013present)\", \"url\": \"https://en.wikipedia.org/wiki/Russo-
Ukrainian_war_(2022%E2%80%93present)\", \"extract\": \"On 24 February 2022, Russia invaded Ukraine, starting the largest and deadliest war in Europe since World War II, in a major escalation of the
existing war between the two countries that began when Russia attacked Ukraine in 2014. The fighting has caused hundreds of thousands of military casualties and tens of thousands of Ukrainian civilian
casualties. As of June 2026, Russian troops occupy roughly 20% of Ukraine. From a population of 41 million, about 8 million Ukrainians have been internally displaced and 6\\u20137 million have fled
the country, creating Europe's largest refugee crisis since World War II.\\nIn late 2021, Russia massed troops near Ukraine's borders and issued demands to the West, including a ban on Ukraine ever
joining NATO. After repeatedly denying having plans to attack Ukraine, on 24 February 2022, Russian president Vladimir Putin announced a \\\"special military operation\\\", saying it was to support
the Russian-backed breakaway republics of Donetsk and Luhansk, whose paramilitary forces had been fighting Ukraine in the Donbas War since 2014. Putin espoused irredentist and imperialist views
challenging Ukraine's legitimacy as a state. He claimed without evidence that the Ukrainian government were neo-Nazis committing genocide against the Russian minority in the Donbas, and that Russia's
goal was to \\\"demilitarise and denazify\\\" Ukraine. Russian air strikes and a ground invasion were launched on a northern front from Belarus towards the capital Kyiv, a southern front from occupied
Crimea, and an eastern front from the Donbas towards Kharkiv. Ukraine enacted martial law, ordered a general mobilisation, and severed diplomatic relations with Russia.\\nRussian troops retreated from
the north and the outskirts of Kyiv by April 2022, after encountering stiff resistance and logistical challenges. The Bucha massacre was uncovered after their withdrawal. Russia launched an offensive
in the Donbas and captured Mariupol after a destructive siege. Russia continued to bomb military and civilian targets far from the front, and struck Ukraine's energy grid during winter months. In late
2022, Ukraine launched successful counteroffensives in the south and east, liberating most of Kharkiv Oblast. Soon after, Russia illegally annexed four partly-occupied provinces. In November, Ukraine
liberated the city of Kherson and all land west of the Dnipro river. After small but steady Russian advances in the east in the first half of 2024, Ukraine launched a cross-border offensive into
Russia's Kursk Oblast in August, where North Korean soldiers were sent to help Russia.\\nThe United Nations Human Rights Office reports that Russia is committing severe human rights violations in
occupied Ukraine. Russia's attacks on civilians, as well as its policies in occupied territories, have led to allegations of genocide. The direct cost of the war for Russia has been estimated as over
US$450 billion, while the World Bank Group estimates the cost of reconstruction in Ukraine at US$588 billion.\\nThe Russian invasion was met with international condemnation. Many countries imposed
sanctions on Russia and its ally Belarus while providing humanitarian and military aid to Ukraine. Protests occurred around the world, with anti-war protesters in Russia being met by mass arrests and
greater media censorship. War-related disruption to Ukrainian agriculture and shipping worsened the world food crisis; war-related environmental damage was described as ecocide. The International
Criminal Court (ICC) opened an investigation into crimes against humanity, war crimes, abduction of Ukrainian children, and genocide against Ukrainians. The ICC issued arrest warrants for Putin and
five other Russian officials. Peace negotiations have stalled, and Russia has repeatedly refused calls for a ceasefire.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

## 💬 Response

I'm finding specific data. Let me now get more details on the confirmed June strikes and check the tempo of strikes from the question description.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026",
  "prompt": "Extract all details about the Ilsky oil refinery strike on June 2, 2026 - date, damage, and any other refinery strikes mentioned in the article"
}
```

### 📋 Result

```
{"url": "https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026", "content": "## Ilsky Oil Refinery Strike - June 2, 2026\n\n**Date and Basic Details:**\n- **Strike date:**
Overnight on June 2, 2026\n- **Target:** Ilsky oil refinery, Krasnodar region, southern Russia\n- **Distance from Ukrainian territory:** Approximately 500 kilometers\n\n**Damage and Impact:**\n- Large
fire ignited at the facility\n- Explosions reported after 3 a.m. local time\n- Thick smoke visible from over 10 kilometers away\n- Fire confirmed by Krasnodar emergency headquarters as drone-caused\n-
Significant damage reported\n\n**Refinery Specifications:**\n- Operated by LLC KNGK-INPZ\n- Annual capacity: 6.6 million tonnes of crude oil\n- Products: Diesel, gasoline, fuel oil, and bitumen\n- One
of southern Russia's largest fuel processing facilities\n- Critical fuel supplier for Russian Southern Military District and occupied areas\n\n**Attack Frequency:**\n- **16th time** the Ilsky refinery
has been targeted since February 2022\n- Previously hit in February 2026 and multiple times in 2024 and 2025\n\n**Broader Campaign Statistics:**\n- Ukrainian forces have hit **24 of Russia's 33 major
oil refineries** since 2022\n- Knocked out roughly **25% of national fuel production** and **33% of refining capacity**\n- At least **40 of 61 drone attacks** on Russian refineries since January 2024
caused fires or lasting damage\n- Russian refining capacity reduced by an estimated **20-25%**\n- Russia forced to import gasoline from Belarus\n- Seaborne oil exports dropped nearly **10% in
2024**\n- Russian oil refining fell to **lowest level in 12 years**\n\n**Other Targets Hit Simultaneously:**\n- Two Pantsir air defense systems (Crimea)\n- Command post of Russian 3rd Army Corps
(Shyrokyne, Donetsk region)\n- Tugboat (Crimea)\n\n---\n\n## Relevant links:\n- [Ukraine drone campaign against Russian oil refineries](https://informedclearly.com/en/war/13627/russian-tanks-obsolete-
drones-dominate-ukraine-battlefield)\n- [Impact of drone strikes on Russian military logistics](https://informedclearly.com/en/war/8656/ukraine-strikes-russian-airbase-glide-bombs-overnight-raid)\n-
[Global energy market impact of the Russia-Ukraine war](https://informedclearly.com/en/war/5490/russia-ukraine-conflict-tactical-shift-drone-warfare-cyberattacks-global-implications)", "title":
"Ukrainian Drones Hit Ilsky Oil Refinery for 16th Time: June 2026 | News | informedclearly"}
```

```json
{
  "url": "https://www.aljazeera.com/news/2026/5/31/ukrainian-drone-attacks-hit-multiple-russian-targets-including-refinery",
  "prompt": "Extract all details about the Saratov refinery strike and any other oil refinery strikes mentioned around May 31 / June 1, 2026"
}
```

### 📋 Result

```
{"url": "https://www.aljazeera.com/news/2026/5/31/ukrainian-drone-attacks-hit-multiple-russian-targets-including-refinery", "content": "Based on the content provided, here are the details about the
Saratov refinery strike and related oil infrastructure attacks:\n\n**Saratov Refinery Strike (May 31, 2026):**\n- Ukrainian drones struck the Saratov oil refinery overnight (May 30-31, 2026)\n-
Saratov is a region on the Volga River with several oil refineries\n- Governor Roman Busargin confirmed \"civil infrastructure\" was damaged in the overnight strikes\n- Ukraine's military officially
confirmed conducting the strike on the Saratov oil refinery\n- The region has come under regular Ukrainian attack in recent years\n\n**Other Oil Infrastructure Strikes:**\n- **Lazarevo oil-pumping
station** in Kirov region (northeast of Moscow, ~1,300 km from Ukraine) - Ukrainian army confirmed this attack\n- **Fuel infrastructure restrictions** imposed on Crimean Peninsula - Moscow-backed
Governor Sergei Aksyonov introduced restrictions on petrol sales, though he didn't specify why. The article notes Ukraine has been attacking fuel infrastructure in southwestern Russia close to Crimea
for months\n\n**Related Context:**\n- Ukrainian strikes also hit facilities in Kirov region's Urzhumsky district, and the Rostov, Voronezh, and Belgorod regions (all bordering Ukraine)\n- Three
civilians were injured in Belgorod\n- Ukraine denied Russian accusations of hitting the Zaporizhzhia nuclear power plant\n\n**Relevant links:**\n- [Russian rate of losses in Ukraine almost triples in
one year](https://www.aljazeera.com/news/2026/5/29/russian-rate-of-losses-in-ukraine-almost-triples-in-one-year)\n- [NATO states slam Russia after drone crashes in
Romania](https://www.aljazeera.com/news/2026/5/29/nato-states-slam-russia-after-drone-crashes-in-romania)", "title": "Ukrainian drone attacks hit multiple Russian targets, including refinery"}
```

```json
{
  "query": "Ukraine drone strike Russian refinery June 3 4 2026 Volgograd Ryazan Kirishi"
}
```

### 📋 Result

```
{"query": "Ukraine drone strike Russian refinery June 3 4 2026 Volgograd Ryazan Kirishi", "results": [{"title": "Leningrad Region\u2019s Kirishi Oil Refinery Halts Operations After Drone Strike \u2013
Reuters - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/05/06/leningrad-regions-kirishi-oil-refinery-halts-operations-after-drone-strike-reuters-a92696", "snippet": "A major oil
refinery in northwestern Russia has suspended operations after it was damaged in a Ukrainian drone strike earlier this week, Reuters reported on Tuesday, citing two industry sources familiar with the
matter.\nUkraine\u2019s military [said](https://www.facebook.com/SecurSerUkraine/posts/pfbid02QMkMmNGhLkZULh1gUarQX9MZKGdEivDqxt46Ea3xj6kZuGLENmVkX2nXL8dysW5Kl?__cft__%5B0%5D=AZaVDW-
V0noYwiCASdWkXlGFltemS3xoiXvSsZv46mAjLHgDGjkjOqFgicyD_LDhpAe3APmPl68lgRWrv6PKVy_EGMqSyV_XnbMb3nst_Ekqw3wYFzTBBFS", "api_data": null, "hint": null}, {"title": "Ukrainian drone strike sparks fire at one
of Russia's top oil refineries | PBS News", "url": "https://www.pbs.org/newshour/world/ukrainian-drone-strike-sparks-fire-at-one-of-russias-top-oil-refineries", "snippet": "By \u2014 Associated Press
Associated Press Leave your feedback Share Copy URL https://www.pbs.org/newshour/world/ukrainian-drone-strike-sparks-fire-at-one-of-russias-top-oil-refineries Email Facebook Twitter LinkedIn Pinterest
Tumblr Share on Facebook Share on Twitter Ukrainian drone strike sparks fire at one of Russia's top oil refineries World Sep 14, 2025 3:37 PM EDT Ukrainian drones have struck one of Russia's largest
oil refineries, sparking a fire, Russian officials and Ukraine's military said", "api_data": null, "hint": null}, {"title": "Ukraine unleashes massive drone onslaught on Putin's Ryazan oil refinery -
YouTube", "url": "https://www.youtube.com/watch?v=ZCc8xPpCMDo", "snippet": "Pr\u00e9sentation\nPresse\nDroits d'auteur\nNous contacter\nCr\u00e9ateurs\nPublicit\u00e9\nD\u00e9veloppeurs\nR\u00e9silier
vos abonnements\nConditions d'utilisation\nConfidentialit\u00e9\nR\u00e8gles et s\u00e9curit\u00e9\nPremiers pas sur YouTube\nTester de nouvelles fonctionnalit\u00e9s\n\u00a9 2026 Google LLC",
"api_data": null, "hint": null}, {"title": "Drones attack Russian oil refineries - How strikes could aid Ukraine on frontline | RBC-Ukraine", "url": "https://newsukraine.rbc.ua/analytics/legitimate-
targets-can-strikes-on-oil-refineries-1710491526.html", "snippet": "Legitimate targets: Can strikes on oil refineries bleed Russia and aid Ukraine on frontline\n![Legitimate targets: Can strikes on
oil refineries bleed Russia and aid Ukraine on
frontline](https://newsukraine.rbc.ua/static/img/_/n/_npz_foto_roszmi_890b857169127c8775b74f8467202bc3_1300x820_e8af4b7730145393c5af500d26835ca3_650x410.jpg)\nUkraine has again attacked Russian oil
refineries hundreds of kilometers from the border. Based on the dynamics, the attacks can already be called systematic, and thi", "api_data": null, "hint": null}, {"title": "Ukraine strikes Russian
oil refinery in long-range drone attack, Kyiv says | Euronews", "url": "https://www.euronews.com/2026/05/21/ukraine-strikes-russian-oil-refinery-in-long-range-drone-attack-kyiv-says", "snippet":
"[Comments](https://www.euronews.com#vuukle-comments-2895449)\nUkraine has been ramping up its retaliatory long-range strikes on Russia in recent weeks, particularly targeting oil
infrastructure.\nUkrainian forces have carried out a long-range drone strike on a Russian oil refinery, Ukrainian President Volodymyr Zelenskyy and the military said on Thursday.\nPosting on X,
Zelenskyy said his forces had struck the Syzran oil refinery in western Russia, sharing video footage showing flames and black smo", "api_data": null, "hint": null}, {"title": "Ukraine Hits 400,000
bpd Kirishi Refinery in Drone Attack Near St. Petersburg | OilPrice.com", "url": "https://oilprice.com/Latest-Energy-News/World-News/Ukraine-Hits-400000-bpd-Kirishi-Refinery-in-Drone-Attack-Near-St-
Petersburg.html", "snippet": "[Trump Plans $700 Million Lifeline for U.S. Coal Power Plants](https://oilprice.com/Latest-Energy-News/World-News/Trump-Plans-700-Million-Lifeline-for-US-Coal-Power-
Plants.html)\nExxon and Chevron executives warn\u2026\nScientists estimate Earth's crust holds\u2026\nOne of Russia's largest oil refineries, the 400,000 barrels-per-day Kirishi refinery southeast of
St. Petersburg, was on fire early on Tuesday following drone attacks overnight, Bloomberg [reports](https://www.bloomberg.com/news/articles/2026-05-", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me gather more data on the recent strike tempo and try to get the actual Wikipedia article content for June 2026 entries. I also need to search for strikes on June 3-4, 2026.

## 💬 Response

Let me search for more recent June strikes and try to build a comprehensive picture of the strike tempo.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Ukraine drone attack Russian oil refinery June 3 2026"
}
```

### 📋 Result

```
{"query": "Ukraine drone attack Russian oil refinery June 3 2026", "results": [{"title": "Ukrainian drone attacks hit multiple Russian targets, including refinery | News | Al Jazeera", "url":
"https://www.aljazeera.com/news/2026/5/31/ukrainian-drone-attacks-hit-multiple-russian-targets-including-refinery", "snippet": "Ukrainian drone attacks hit multiple Russian targets, including
refinery\nSaratov refinery hit as Ukrainian strikes intensify across Russian regions, damaging civilian infrastructure.\n![KHARKIV REGION, UKRAINE - MAY 22: (EDITOR'S NOTE: Image has been reviewed by
Ukrainian military officials prior to transmission) Member of the Lava Unmanned Systems Regiment, Norman, poses for a photograph with a Leleka reconnaissance UAV, capable of flying up to 120
kilometres and returning to base, on May 22, 20", "api_data": null, "hint": null}, {"title": "Ukraine Hits St. Petersburg Oil Terminal, Kronstadt Base as Putin\u2019s Economic Forum Opens", "url":
"https://www.kyivpost.com/post/77390", "snippet": "Ukraine Targets St. Petersburg Oil Hub, Kronstadt Military Facilities as Putin\u2019s \u2018Davos\u2019 Opens\nPresident Zelensky confirmed that
Ukrainian forces struck several strategic targets inside Russia overnight, including the St. Petersburg oil terminal, military facilities at the Kronstadt naval base, and a defense industry enterprise
in the Tambov region. The attack sparked a major fire near St. Petersburg as the St. Petersburg International Economic Forum, often dubbed the \u201cRussian Davos,\u201d was set to", "api_data": null,
"hint": null}, {"title": "Ukraine strikes Russian oil refinery in long-range drone attack, Kyiv says | Euronews", "url": "https://www.euronews.com/2026/05/21/ukraine-strikes-russian-oil-refinery-in-
long-range-drone-attack-kyiv-says", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2895449)\nUkraine has been ramping up its retaliatory long-range strikes on Russia in recent weeks,
particularly targeting oil infrastructure.\nUkrainian forces have carried out a long-range drone strike on a Russian oil refinery, Ukrainian President Volodymyr Zelenskyy and the military said on
Thursday.\nPosting on X, Zelenskyy said his forces had struck the Syzran oil refinery in western Russia, sharing video footage showing flames and black smo", "api_data": null, "hint": null}, {"title":
"Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows | Russia-Ukraine war News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/5/30/ukraine-drones-strike-russian-oil-
facility-as-kyiv-and-moscow-trade-blows", "snippet": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows\nStrikes have seen 13,000 residents without power in Zaporizhzhia as
Russia and Ukraine trade drone attacks.\n![A Ukraine-made P1-Sun drone operated by servicemen of the 116th Mechanised Brigade to intercept Russian 'Shahed' type, and other strike or reconnaissance
drones [FILE: Yevhen Titov/ EPA]](/wp-content/uploads/2026/05/14004194-1780124557.jpg?resize=770%2C513&quality=80)\nUkraine has launched coordinated drone attacks", "api_data": null, "hint": null},
{"title": "Ukrainian Drones Hit Ilsky Oil Refinery for 16th Time: June 2026 | war | informed, clearly", "url": "https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026",
"snippet": "Ukraine Strikes Key Russian Oil Refinery in Latest Deep-Strike Campaign\nUkrainian drones struck the Ilsky oil refinery in Russia's Krasnodar region overnight on June 2, 2026, igniting a
large fire at one of southern Russia's largest fuel processing facilities. The attack marks the 16th time the refinery has been targeted since the full-scale invasion began, as Kyiv intensifies its
campaign to disrupt Russian energy infrastructure and military logistics. The strike on the Ilsky refinery, located ", "api_data": null, "hint": null}, {"title": "Ukrainian drones strike St.
Petersburg, hours before \u2018Putin\u2019s Davos\u2019 opens | CNN", "url": "https://www.cnn.com/2026/06/03/europe/ukraine-drone-attack-russia-st-petersburg-intl-hnk", "snippet": "Ukrainian drones
[rained down](https://www.cnn.com/2026/06/01/europe/crimea-fuel-ukraine-russian-oil-intl) on St. Petersburg overnight, striking key infrastructure and wounding several people, just hours before
Russian President [Vladimir Putin](https://www.cnn.com/2026/05/20/politics/russia-losing-ukraine-mcgurk-analysis)\u2019s signature economic forum drawing thousands of attendees opened in the
city.\n[Hundreds of drones](https://www.cnn.com/world/europe/ukraine) hit several Russian cities, with K", "api_data": null, "hint": null}, {"title": "\u2018Smell\u2019 of war comes to St Petersburg
as Ukraine hammers Russian refineries | Russia-Ukraine war News | Al Jazeera", "url": "https://www.aljazeera.com/features/2026/4/6/smell-of-war-comes-to-st-petersburg-as-ukraine-hammers-russian-
refineries", "snippet": "\u2018Smell\u2019 of war comes to St Petersburg as Ukraine hammers Russian refineries\nUkraine aims to drain Russia\u2019s war chest with drone strikes on Pokrovsk and Ust-
Luga oil facilities on the Baltic Sea.\n![Primorsk](/wp-content/uploads/2026/04/2026-03-31T093505Z_749177487_RC2DEKAEPMGQ_RTRMADP_3_UKRAINE-CRISIS-DRONES-
PRIMORSK-1775471276.jpg?resize=770%2C513&quality=80)\nKonstantin can smell the consequences of the war in Ukraine from his apartment in St Petersburg, Russia\u2019s second-largest city and Presiden",
"api_data": null, "hint": null}, {"title": "Drone Strikes Force Central Russian Refineries to Halt or Cut Output \u2013 Reuters - The Moscow Times", "url":
"https://www.themoscowtimes.com/2026/05/20/drone-strikes-force-central-russian-refineries-to-halt-or-cut-output-reuters-a92805", "snippet": "Oil refineries in central Russia have been forced to either
suspend operations entirely or sharply reduce fuel output after a wave of drone attacks over the past two weeks, Reuters [reported](https://www.reuters.com/business/energy/oil-refining-standstill-
central-russia-after-ukrainian-drone-strikes-sources-say-2026-05-20/) Tuesday, citing official data and industry sources.\nRussia has already banned gasoline exports until July 31 as Ukraine ramps up
its attacks against energy sites across the c", "api_data": null, "hint": null}, {"title": "Key Russian oil pipeline node hit in massive Ukrainian drone barrage", "url":
"https://kyivindependent.com/russias-saratov-oil-refinery-reportedly-struck-by-ukrainian-drones/", "snippet": "[War](https://kyivindependent.com/tag/war/)\nKey Russian oil pipeline node hit in massive
Ukrainian drone barrage\n![Key Russian oil pipeline node hit in massive Ukrainian drone
barrage](/_next/image?url=https%3A%2F%2Fassets.kyivindependent.com%2Fcontent%2Fimages%2F2026%2F05%2Fphoto_2026-05-30_20-56-51_20260531-013010.jpg&w=1536&q=75)\nEditor's note: This is a developing
story and is being updated.\nUkrainian forces hit the Saratov oil refinery, along with several other Russian oil industry faciliti", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Ukraine drone strike oil infrastructure Russia \"June 4\" 2026"
}
```

### 📋 Result

```
{"query": "Ukraine drone strike oil infrastructure Russia \"June 4\" 2026", "results": [{"title": "Ukraine strikes Russian oil refinery in long-range drone attack, Kyiv says | Euronews", "url":
"https://www.euronews.com/2026/05/21/ukraine-strikes-russian-oil-refinery-in-long-range-drone-attack-kyiv-says", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2895449)\nUkraine has
been ramping up its retaliatory long-range strikes on Russia in recent weeks, particularly targeting oil infrastructure.\nUkrainian forces have carried out a long-range drone strike on a Russian oil
refinery, Ukrainian President Volodymyr Zelenskyy and the military said on Thursday.\nPosting on X, Zelenskyy said his forces had struck the Syzran oil refinery in western Russia, sharing video
footage showing flames and black smo", "api_data": null, "hint": null}, {"title": "Ukrainian drones strike St. Petersburg, hours before \u2018Putin\u2019s Davos\u2019 opens | CNN", "url":
"https://www.cnn.com/2026/06/03/europe/ukraine-drone-attack-russia-st-petersburg-intl-hnk", "snippet": "Ukrainian drones [rained down](https://www.cnn.com/2026/06/01/europe/crimea-fuel-ukraine-
russian-oil-intl) on St. Petersburg overnight, striking key infrastructure and wounding several people, just hours before Russian President [Vladimir
Putin](https://www.cnn.com/2026/05/20/politics/russia-losing-ukraine-mcgurk-analysis)\u2019s signature economic forum drawing thousands of attendees opened in the city.\n[Hundreds of
drones](https://www.cnn.com/world/europe/ukraine) hit several Russian cities, with K", "api_data": null, "hint": null}, {"title": "Russian attacks kill 4 people overnight as Ukraine drones target oil
infrastructure | PBS News", "url": "https://www.pbs.org/newshour/world/russian-attacks-kill-4-people-overnight-as-ukraine-drones-target-oil-infrastructure", "snippet": "By \u2014 Derek Gatopoulos,
Associated Press Derek Gatopoulos, Associated Press By \u2014 Volodymyr Yurchuk, Associated Press Volodymyr Yurchuk, Associated Press Leave your feedback Share Copy URL
https://www.pbs.org/newshour/world/russian-attacks-kill-4-people-overnight-as-ukraine-drones-target-oil-infrastructure Email Facebook Twitter LinkedIn Pinterest Tumblr Share on Facebook Share on
Twitter Russian attacks kill 4 people overnight as Ukraine drones target oil infrastructure World Apr 6, 2026 11:10 AM", "api_data": null, "hint": null}, {"title": "Ukrainian drones strike a St.
Petersburg oil terminal ahead of Putin visit : NPR", "url": "https://www.npr.org/2026/06/03/nx-s1-5844793/ukrainian-drones-hit-st-petersburg", "snippet": "Ukrainian drones strike a St. Petersburg oil
terminal ahead of Putin visit\n![A plumes of black smoke is seen over the port of St. Petersburg, Russia, Wednesday, June 3, 2026, after a Ukrainian drone
attack.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/8640x5760+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2F3b%2F2a%2F2d47ee3c42a3927e22c964a3f479%2Fap26154236654404.jpg)\nA plumes of black smoke is seen over the port of St. Petersburg, Ru", "api_data": null, "hint": null},
{"title": "\u2018Environmental disaster\u2019: Ukrainian attacks on oil refineries rock Russia | Russia-Ukraine war News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/4/30/its-all-very-
toxic", "snippet": "\u2018Environmental disaster\u2019: Ukrainian attacks on oil refineries rock Russia\nUkrainian forces have hammered one of Russia\u2019s largest sites in Tuapse, causing oil spills
and black rain.\n![Officials walk along a street during a visit by Krasnodar region's governor in Tuapse, Russia](/wp-
content/uploads/2026/04/2026-04-28T141859Z_991775446_RC2EYKAT07FU_RTRMADP_3_UKRAINE-CRISIS-REFINERY-FIRE-1777477892.jpg?resize=770%2C513&quality=80)\nWhen cleanup volunteer Sergei Solovev arrived in
the town of Tuapse, ", "api_data": null, "hint": null}, {"title": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade blows | Russia-Ukraine war News | Al Jazeera", "url":
"https://www.aljazeera.com/news/2026/5/30/ukraine-drones-strike-russian-oil-facility-as-kyiv-and-moscow-trade-blows", "snippet": "Ukraine drones strike Russian oil facility, as Kyiv and Moscow trade
blows\nStrikes have seen 13,000 residents without power in Zaporizhzhia as Russia and Ukraine trade drone attacks.\n![A Ukraine-made P1-Sun drone operated by servicemen of the 116th Mechanised Brigade
to intercept Russian 'Shahed' type, and other strike or reconnaissance drones [FILE: Yevhen Titov/ EPA]](/wp-content/uploads/2026/05/14004194-1780124557.jpg?resize=770%2C513&quality=80)\nUkraine has
launched coordinated drone attacks", "api_data": null, "hint": null}, {"title": "Ukrainian drones hit St. Petersburg oil terminal before city hosts Russian economic forum | CBC News", "url":
"https://www.cbc.ca/news/world/ukraine-drones-st-petersburg-oil-terminal-9.7222060", "snippet": "[World](https://www.cbc.ca/news/world)\nUkrainian drones hit St. Petersburg oil terminal before city
hosts Russian economic forum\nUkraine, Russia have sought an edge by launching long-range strikes as front line barely moves\n![A plume of black smoke is seen over a
port.](https://i.cbc.ca/ais/89733d97-3fa1-4684-a681-7058652ed29d,1780504982046/full/max/0/default.jpg?im=Crop%2Crect%3D%280%2C263%2C8640%2C4860%29%3B)\nUkrainian long-range drones struck an oil
terminal in St. Petersburg and set it ablaz", "api_data": null, "hint": null}, {"title": "Quantifying Ukraine\u2019s Strikes on Russian Energy Infrastructure | Baker Institute", "url":
"https://www.bakerinstitute.org/research/quantifying-ukraines-strikes-russian-energy-infrastructure", "snippet": "Quantifying Ukraine\u2019s Strikes on Russian Energy Infrastructure\n![A group of
Ukrainian military using tablet to operate the drone.](/sites/default/files/styles/16_9_small_564x317/public/2026-03/AdobeStock_612812309-Ukraine%2BDrone-WEB.jpeg?h=c3635fa2&itok=LDH-Pud5)\nTable of
Contents\nAuthor(s)\nShare this Publication\n-\n[Print This Publication](javascript:window.print()) -\n[Cite This Publication](https://www.bakerinstitute.org#)Gabriel Collins, \u201cQuantifying
Ukraine\u2019s Strikes on Russian Energy Infras", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Caspian Policy Center Russian refinery tracker 2026 attacks"
}
```

### 📋 Result

```
{"query": "Caspian Policy Center Russian refinery tracker 2026 attacks", "results": [{"title": "Ukrainian Drones Hit Ilsky Oil Refinery for 16th Time: June 2026 | war | informed, clearly", "url":
"https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026", "snippet": "Ukraine Strikes Key Russian Oil Refinery in Latest Deep-Strike Campaign\nUkrainian drones struck the
Ilsky oil refinery in Russia's Krasnodar region overnight on June 2, 2026, igniting a large fire at one of southern Russia's largest fuel processing facilities. The attack marks the 16th time the
refinery has been targeted since the full-scale invasion began, as Kyiv intensifies its campaign to disrupt Russian energy infrastructure and military logistics. The strike on the Ilsky refinery,
located ", "api_data": null, "hint": null}, {"title": "CPC | LIVE MAP of Russian Refineries Hit: Ukrainian Drone Strikes Boost Caspian Energy", "url":
"https://www.caspianpolicy.org/research/security/live-map-of-russian-refineries-hit-ukrainian-drone-strikes-boost-caspian-energy", "snippet": "LIVE MAP of Russian Refineries Hit: Ukrainian Drone
Strikes Boost Caspian Energy\nRecent Articles\nAuthor: [Joshua Bernard-Pearl, ](https://caspianpolicy.org/staff/joshua-bernard-pearl)[Nigel Li](https://caspianpolicy.org/staff/nigel-
li)\n03/18/2025\nCaspian Policy Center\u2019s Live Map of Russian Refineries documents 61 attacks across 24 Russian refineries and the resulting level of damage since January 2024. Click on the
refineries for more information.\nUkraine launched 61 drone strikes on Russian oil", "api_data": null, "hint": null}, {"title": "Ukraine strikes Russian Caspian Fleet base deep inside Russia, home to
missile-capable ships used in Kalibr strikes \u2013 General Staff - Euromaidan Press", "url": "https://euromaidanpress.com/2026/05/15/ukraine-strikes-russian-caspian-fleet-base/", "snippet":
"Ukraine\u2019s General Staff says its forces struck Russian naval assets at the Kaspiysk base in the Caspian Sea, damaging a small missile ship and a minesweeper.\nThe
[strikes](https://t.me/GeneralStaffZSU/38684) were carried out overnight on 15 May, with the extent of damage still being assessed.\nNaval assets hit in Caspian Sea base\nKaspiysk has served as the
main base of Russia\u2019s Caspian Flotilla since 2020, hosting missile-capable small warships as well as support vessels.\nThe flotilla includes sm", "api_data": null, "hint": null}, {"title":
"Ukraine Hits Major Oil Terminal in Southern Russia \u2013 Moscow - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/04/06/ukraine-hits-major-oil-terminal-in-southern-russia-
moscow-a92430", "snippet": "Updated to add the Russian Defense Ministry's statement.\nUkrainian drones attacked the Caspian Pipeline Consortium's marine terminal in southern Russia early Monday,
damaging part of a mooring point and setting four oil tanks ablaze, Russia's Defense Ministry said.\nThe Ukrainian army said it had attacked a different terminal in the port of Novorossiysk, without
mentioning the Caspian Pipeline Consortium (CPC).\nThe CPC pipeline \u2014 which had not commented \u2014 handles around 1% of the world's oil supp", "api_data": null, "hint": null}, {"title": "CPC |
Home", "url": "https://www.caspianpolicy.org/", "snippet": "Latest Posts\nArmenia after Moscow: Rubio\u2019s Visit and Armenia\u2019s Accelerating Turn West\nU.S. Secretary of State Marco Rubio\u2019s
short trip to Yerevan on Tuesday, May 26...\nAuthor: [Zohra Movsumova](https://caspianpolicy.org/staff/zohra-movsumova)\nDate: 06/03/2026\nHeadlines from the Caspian: June 1, 2026\nKazakhstan\u2019s
energy ministry confirmed on June 1 that crude oil output has returned to normal levels...\nAuthor: Caspian Policy Center\nDate: 06/02/2026\nArmenia in the Crosshairs: Russian Disinformatio",
"api_data": null, "hint": null}, {"title": "Ukraine Hits Saratov Oil Refinery, Caspian Military Base and Other Targets Deep Inside russia | Defense Express", "url": "https://en.defence-
ua.com/news/ukraine_hits_saratov_oil_refinery_caspian_military_base_and_other_targets_deep_inside_russia-18672.html", "snippet": "President Volodymyr Zelenskyy announced the results, describing the
attacks as part of Ukraine's long-range campaign against facilities supporting russia's war effort.\nAccording to the president, Ukrainian forces conducted overnight strikes on the Saratov oil
refinery, as well as targets in russia's Rostov and Kirov regions and a military base on the Caspian Sea coast.\nRead more:[Ukrainian Unmanned Systems Forces Destroyed 2 russian Tu-142 ASW aircraft,
Iskander launcher with FP-1 UAVs]\n\"Our Def", "api_data": null, "hint": null}, {"title": "The Ukrainian military has hit Russia's Tuapse oil refinery ...", "url":
"https://www.facebook.com/deutschewellenews/posts/the-ukrainian-military-has-hit-russias-tuapse-oil-refinery-in-a-second-attack-in/1406742108147766/", "snippet": null, "api_data": null, "hint": null},
{"title": "Quantifying Ukraine\u2019s Strikes on Russian Energy Infrastructure | Baker Institute", "url": "https://www.bakerinstitute.org/research/quantifying-ukraines-strikes-russian-energy-
infrastructure", "snippet": "Quantifying Ukraine\u2019s Strikes on Russian Energy Infrastructure\n![A group of Ukrainian military using tablet to operate the
drone.](/sites/default/files/styles/16_9_small_564x317/public/2026-03/AdobeStock_612812309-Ukraine%2BDrone-WEB.jpeg?h=c3635fa2&itok=LDH-Pud5)\nTable of Contents\nAuthor(s)\nShare this
Publication\n-\n[Print This Publication](javascript:window.print()) -\n[Cite This Publication](https://www.bakerinstitute.org#)Gabriel Collins, \u201cQuantifying Ukraine\u2019s Strikes on Russian
Energy Infras", "api_data": null, "hint": null}]}
```

## 💬 Response

Excellent! I'm finding key data. Let me get more details on the St. Petersburg oil terminal strike on June 3 and look for any additional June strikes.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.cnn.com/2026/06/03/europe/ukraine-drone-attack-russia-st-petersburg-intl-hnk",
  "prompt": "Extract all details about the St. Petersburg drone strike on June 3, 2026. Was it an oil refinery or an oil terminal? What other oil infrastructure was hit? List all oil/refinery targets mentioned."
}
```

### 📋 Result

```
{"url": "https://www.cnn.com/2026/06/03/europe/ukraine-drone-attack-russia-st-petersburg-intl-hnk", "content": "Based on the content, here are the details about the St. Petersburg drone strike on June
3, 2026:\n\n**St. Petersburg Oil Infrastructure:**\n- **Oil Terminal** (not refinery) - described as \"one of the largest oil transshipment complexes in northwestern Russia\"\n- The terminal plays a
\"crucial role\" in Russian fuel exports and logistics\n- Two firefighters were killed while extinguishing a blaze caused by drone debris at this location\n\n**Other Targets in the Attack:**\n- A
Russian corvette warship \"Boikiy\" at Kronstadt island port near St. Petersburg\n- Three districts of St. Petersburg were targeted overall\n\n**Other Oil/Refinery Infrastructure Mentioned:**\n- The
article references Ukrainian strikes on \"critical infrastructure facilities\" in **Smolensk** (western Russia), where two firefighters died\n- A facility in **Tambov region** involved in weapons
production (not specifically oil-related)\n- General reference to **Crimea fuel/Russian oil** facilities hit in previous attacks\n- **Moscow's oil facilities** mentioned as targets of Ukraine's long-
range drone program\n\n**Clarification:** The St. Petersburg target was specifically an **oil terminal** (for transshipment/logistics), not an oil refinery (for processing crude oil).\n\nRelevant
links:\n- [Ukrainian drones rained down on Crimea fuel/Russian oil](https://www.cnn.com/2026/06/01/europe/crimea-fuel-ukraine-russian-oil-intl)\n- [Ukraine steps up attacks on Russian oil
refineries](https://www.cnn.com/2026/04/18/europe/ukraine-strikes-russian-oil-refineries-us-waiver-intl)\n- [Ukraine's long-range drone
capabilities](https://www.cnn.com/2026/05/27/world/video/ukraine-long-range-drone-unit-hitting-russia-npw-vrtc)", "title": "Ukrainian drones strike St. Petersburg, hours before \u2018Putin\u2019s
Davos\u2019 opens | CNN"}
```

```json
{
  "url": "https://www.npr.org/2026/06/03/nx-s1-5844793/ukrainian-drones-hit-st-petersburg",
  "prompt": "Extract details about the June 3 St. Petersburg oil terminal/refinery strike. Was it specifically an oil refinery or an oil terminal? What other targets were hit?"
}
```

### 📋 Result

```
{"url": "https://www.npr.org/2026/06/03/nx-s1-5844793/ukrainian-drones-hit-st-petersburg", "content": "Based on the article, here are the details about the June 3, 2026 strike:\n\n**Target Type:** It
was specifically an **oil terminal** in St. Petersburg, not a refinery. The article consistently refers to it as an \"oil terminal\" throughout.\n\n**Other Targets Hit (same night):**\n1. **Russian
guided-missile corvette Boikiy** - Set on fire while in dry dock at the Kronstadt naval base (west of St. Petersburg)\n2. **Manufacturing plant** involved in weapon production in the Tambov region
(600 km from Ukraine)\n3. **St. Petersburg's infrastructure** - Russian authorities acknowledged strikes but didn't provide specifics beyond the oil terminal\n\n**Additional Details:**\n- Drones flew
over 1,000 km (600 miles) to reach St. Petersburg\n- The city's airport briefly suspended flights\n- Mobile internet services were cut off\n- Russia claimed to have downed 354 Ukrainian drones
overnight\n\n**Relevant links:**\n- None provided in the extracted text content (this was presented as standalone article text without embedded hyperlinks)", "title": "Ukrainian drones strike a St.
Petersburg oil terminal ahead of Putin visit"}
```

```json
{
  "query": "\"St Petersburg\" oil terminal refinery drone Ukraine June 3 2026 fire"
}
```

### 📋 Result

```
{"query": "\"St Petersburg\" oil terminal refinery drone Ukraine June 3 2026 fire", "results": [{"title": "Ukrainian drones strike a St. Petersburg oil terminal ahead of Putin visit : NPR", "url":
"https://www.npr.org/2026/06/03/nx-s1-5844793/ukrainian-drones-hit-st-petersburg", "snippet": "Ukrainian drones strike a St. Petersburg oil terminal ahead of Putin visit\n![A plumes of black smoke is
seen over the port of St. Petersburg, Russia, Wednesday, June 3, 2026, after a Ukrainian drone
attack.](https://npr.brightspotcdn.com/dims3/default/strip/false/crop/8640x5760+0+0/resize/1100/quality/50/format/jpeg/?url=http%3A%2F%2Fnpr-
brightspot.s3.amazonaws.com%2F3b%2F2a%2F2d47ee3c42a3927e22c964a3f479%2Fap26154236654404.jpg)\nA plumes of black smoke is seen over the port of St. Petersburg, Ru", "api_data": null, "hint": null},
{"title": "Ukrainian drones hit St. Petersburg oil terminal before city hosts Russian economic forum", "url": "https://www.clickondetroit.com/business/2026/06/03/ukrainian-drones-set-fire-to-a-st-
petersburg-oil-terminal-ahead-of-putin-visit/", "snippet": "Ukrainian long-range drones struck an oil terminal in St. Petersburg and set it ablaze, Ukrainian President Volodymyr Zelenskyy said
Wednesday, sending smoke billowing over the city where Russian President Vladimir Putin was born as it hosts Russia\u2019s leading event for attracting foreign capital.\nThe drones flew more than
1,000 kilometers (600 miles) to hit the terminal in Russia\u2019s second-largest city, Zelenskyy said on social media, a day after Moscow launched a major [drone and missile attack](", "api_data":
null, "hint": null}, {"title": "Ukraine Hits St. Petersburg Oil Terminal, Kronstadt Base as Putin\u2019s Economic Forum Opens", "url": "https://www.kyivpost.com/post/77390", "snippet": "Ukraine
Targets St. Petersburg Oil Hub, Kronstadt Military Facilities as Putin\u2019s \u2018Davos\u2019 Opens\nPresident Zelensky confirmed that Ukrainian forces struck several strategic targets inside Russia
overnight, including the St. Petersburg oil terminal, military facilities at the Kronstadt naval base, and a defense industry enterprise in the Tambov region. The attack sparked a major fire near St.
Petersburg as the St. Petersburg International Economic Forum, often dubbed the \u201cRussian Davos,\u201d was set to", "api_data": null, "hint": null}, {"title": "Ukrainian drones set fire to a St.
Petersburg oil terminal ahead of Putin visit", "url": "https://www.washingtonpost.com/business/2026/06/03/russia-ukraine-petersburg-oil-terminal-putin-
drone/211c0810-5f26-11f1-9c46-d6211372eede_story.html", "snippet": null, "api_data": null, "hint": null}, {"title": "Fire, smoke greet Putin's Economic Forum as Ukraine strikes St. Petersburg oil
terminal", "url": "https://kyivindependent.com/st-petersburg-oil-terminal-hit-in-major-ukrainian-attack-day-after-russias-mass-strike-on-kyiv/", "snippet":
"[War](https://kyivindependent.com/tag/war/)\nFire, smoke greet Putin's Economic Forum as Ukraine strikes St. Petersburg oil terminal\n![Fire, smoke greet Putin's Economic Forum as Ukraine strikes St.
Petersburg oil terminal](/_next/image?url=https%3A%2F%2Fassets.kyivindependent.com%2Fcontent%2Fimages%2F2026%2F06%2Fpetersburg_20260603-023912.jpg&w=1536&q=75)\nEditor's Note: This is a developing
story and is being updated.\nBlack smoke hung over St. Petersburg on the morning of June 3 as the first del", "api_data": null, "hint": null}, {"title": "Ukrainian drones hit St. Petersburg oil
terminal before city hosts Russian economic forum | CBC News", "url": "https://www.cbc.ca/news/world/ukraine-drones-st-petersburg-oil-terminal-9.7222060", "snippet":
"[World](https://www.cbc.ca/news/world)\nUkrainian drones hit St. Petersburg oil terminal before city hosts Russian economic forum\nUkraine, Russia have sought an edge by launching long-range strikes
as front line barely moves\n![A plume of black smoke is seen over a
port.](https://i.cbc.ca/ais/89733d97-3fa1-4684-a681-7058652ed29d,1780504982046/full/max/0/default.jpg?im=Crop%2Crect%3D%280%2C263%2C8640%2C4860%29%3B)\nUkrainian long-range drones struck an oil
terminal in St. Petersburg and set it ablaz", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.cnn.com/2026/06/01/europe/crimea-fuel-ukraine-russian-oil-intl",
  "prompt": "Extract details about any oil refinery strikes around June 1, 2026. What specific oil refineries or infrastructure were hit? List all targets and dates."
}
```

### 📋 Result

```
{"url": "https://www.cnn.com/2026/06/01/europe/crimea-fuel-ukraine-russian-oil-intl", "content": "Based on the provided content, there are **no specific details about oil refinery strikes** on or
around June 1, 2026.\n\nThe article mentions:\n- Ukrainian drone attacks on **fuel trucks** on the 'Novorossiya' highway (the land corridor connecting mainland Russia and Crimea)\n- General reference
to \"almost daily Ukrainian attacks on [Russia's] oil infrastructure\" (no specific refineries, dates, or locations provided)\n- The result: gasoline rationing in Crimea starting around May 31-June 1,
2026\n\n**No specific oil refineries or infrastructure targets are named in this content.** The article focuses on the consequences (fuel shortages) rather than documenting specific
strikes.\n\nRelevant links:\nThe provided content does not contain any embedded links to other sources.", "title": "Crimea short of fuel as Ukraine expands attacks on Russian oil facilities | CNN"}
```

```json
{
  "query": "Ukraine drone strike refinery June 1 2 2026 ISW assessment"
}
```

### 📋 Result

```
{"query": "Ukraine drone strike refinery June 1 2 2026 ISW assessment", "results": [{"title": "ISW Russian Offensive Campaign Assessment, June 1, 2026", "url": "https://www.kyivpost.com/post/77319",
"snippet": "Key Takeaways from the [ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-1-2026/):\n- Ukrainian forces have largely halted the Russian
Spring-Summer 2026 offensive so far, and Russian forces in May 2026 have gained a presence in only a fraction of the territory they did in May 2026.\n- Other sources with different methodologies are
also recording a slow Russian rate of advance in May 2026.\n- Russia\u2019s declining gains appear to be unrelated to the ", "api_data": null, "hint": null}, {"title": "Ukrainian Drones Hit Ilsky Oil
Refinery for 16th Time: June 2026 | war | informed, clearly", "url": "https://informedclearly.com/en/war/54050/ukrainian-drones-ilsky-oil-refinery-2026", "snippet": "Ukraine Strikes Key Russian Oil
Refinery in Latest Deep-Strike Campaign\nUkrainian drones struck the Ilsky oil refinery in Russia's Krasnodar region overnight on June 2, 2026, igniting a large fire at one of southern Russia's
largest fuel processing facilities. The attack marks the 16th time the refinery has been targeted since the full-scale invasion began, as Kyiv intensifies its campaign to disrupt Russian energy
infrastructure and military logistics. The strike on the Ilsky refinery, located ", "api_data": null, "hint": null}, {"title": "Ukraine strikes Russian oil refinery in long-range drone attack, Kyiv
says | Euronews", "url": "https://www.euronews.com/2026/05/21/ukraine-strikes-russian-oil-refinery-in-long-range-drone-attack-kyiv-says", "snippet": "[Comments](https://www.euronews.com#vuukle-
comments-2895449)\nUkraine has been ramping up its retaliatory long-range strikes on Russia in recent weeks, particularly targeting oil infrastructure.\nUkrainian forces have carried out a long-range
drone strike on a Russian oil refinery, Ukrainian President Volodymyr Zelenskyy and the military said on Thursday.\nPosting on X, Zelenskyy said his forces had struck the Syzran oil refinery in
western Russia, sharing video footage showing flames and black smo", "api_data": null, "hint": null}, {"title": "Key Russian oil pipeline node hit in massive Ukrainian drone barrage", "url":
"https://kyivindependent.com/russias-saratov-oil-refinery-reportedly-struck-by-ukrainian-drones/", "snippet": "[War](https://kyivindependent.com/tag/war/)\nKey Russian oil pipeline node hit in massive
Ukrainian drone barrage\n![Key Russian oil pipeline node hit in massive Ukrainian drone
barrage](/_next/image?url=https%3A%2F%2Fassets.kyivindependent.com%2Fcontent%2Fimages%2F2026%2F05%2Fphoto_2026-05-30_20-56-51_20260531-013010.jpg&w=1536&q=75)\nEditor's note: This is a developing
story and is being updated.\nUkrainian forces hit the Saratov oil refinery, along with several other Russian oil industry faciliti", "api_data": null, "hint": null}]}
```

```json
{
  "query": "ISW Russian offensive campaign assessment June 2026 refinery oil"
}
```

### 📋 Result

```
{"query": "ISW Russian offensive campaign assessment June 2026 refinery oil", "results": [{"title": "ISW Russian Offensive Campaign Assessment, June 1, 2026", "url":
"https://www.kyivpost.com/post/77319", "snippet": "Key Takeaways from the [ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-1-2026/):\n- Ukrainian
forces have largely halted the Russian Spring-Summer 2026 offensive so far, and Russian forces in May 2026 have gained a presence in only a fraction of the territory they did in May 2026.\n- Other
sources with different methodologies are also recording a slow Russian rate of advance in May 2026.\n- Russia\u2019s declining gains appear to be unrelated to the ", "api_data": null, "hint": null},
{"title": "ISW Russian Offensive Campaign Assessment, June 3, 2026", "url": "https://www.kyivpost.com/post/77471", "snippet": "Key Takeaways from the[
ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-3-2026/):\n- The Russian ultranationalist community presented extreme and unrealistic scenarios for
Russia\u2019s military and geopolitical future at the St. Petersburg International Economic Forum (SPIEF) that likely somewhat differ from the Kremlin\u2019s positions.\n- Ukrainian forces conducted a
series of long-range strikes against Russian military assets and oil infrastructure in", "api_data": null, "hint": null}, {"title": "ISW Russian Offensive Campaign Assessment, June 2, 2026", "url":
"https://www.kyivpost.com/post/77394", "snippet": "Key Takeaways from the [ISW](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-2-2026/):\n- Russian
forces conducted yet another devastating drone and missile strike series against Ukraine on the night of June 1 to 2, heavily targeting Kyiv City. The Russian strikes killed at least 22 civilians and
injured at least 130.\n- Russia\u2019s June 1 to 2 strikes are part of a pattern of escalating Russian strikes against Kyiv City intended to take advantage of Pa", "api_data": null, "hint": null},
{"title": "Russian Offensive Campaign Assessment, June 1, 2026 | Critical Threats", "url": "https://www.criticalthreats.org/analysis/russian-offensive-campaign-assessment-june-1-2026", "snippet":
null, "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me get more details from the ISW assessments for June 1-3, 2026, which would list specific oil infrastructure strikes. I also need to check the actual Wikipedia timeline article more carefully.

## 💬 Response

Let me get the ISW assessments for June 1-3 and check for more refinery-specific strikes.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-1-2026/",
  "prompt": "Extract all mentions of Ukrainian strikes on Russian oil refineries, oil infrastructure, energy facilities on June 1, 2026. List each target by name and type (refinery, terminal, depot)."
}
```

### 📋 Result

```
{"url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-1-2026/", "content": "Based on the content, the following Ukrainian strikes on Russian
oil/energy infrastructure are mentioned for June 1, 2026 (or with details published on that date):\n\n1. **Balakhonikhinskaya Oil Pumping Station** - Nizhny Novgorod Oblast\n   - Type: Oil pumping
station\n   - Strike date: Unspecified\n   - Details: Damage shown in satellite imagery published June 1\n\n2. **Armavir Oil Depot** - Krasnodar Krai\n   - Type: Oil depot\n   - Strike date: May
29-30\n   - Details: Satellite imagery from May 31 shows damage to at least one fuel tank; a tank damaged in March 2026 remains inoperable\n\nNote: No strikes specifically dated June 1, 2026 are
mentioned. The content reports on strikes that occurred earlier but were documented or published on June 1.\n\n**Relevant links:**\n- [RFE/RL Schemi project satellite
imagery](https://t.me/cxemu/4830)\n- [Satellite imagery of Balakhonikhinskaya Oil Pumping Station](https://x.com/Exilenova_plus/status/2061312391212921267)\n- [Additional satellite
imagery](https://x.com/neonhandrail/status/2061327212608143863)", "title": "Russian Offensive Campaign Assessment, June 1, 2026"}
```

```json
{
  "url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-2-2026/",
  "prompt": "Extract all mentions of Ukrainian strikes on Russian oil refineries, oil infrastructure, energy facilities on June 2, 2026. List each target by name and type (refinery, terminal, depot)."
}
```

### 📋 Result

```
{"url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-2-2026/", "content": "Based on the content, Ukrainian strikes on Russian oil and energy
infrastructure on June 2, 2026 (or night of June 1-2):\n\n**Strikes Conducted June 1-2:**\n1. **Ilsky Oil Refinery** (Krasnodar Krai) - Oil refinery - Struck overnight, caused fire\n\n**Battle Damage
Assessments (BDA) for Prior Strikes Reported on June 2:**\n1. **Novoshakhtinsky Oil Refinery** (Rostov Oblast) - Oil refinery - Struck May 31, damaged AVT-1 and AVT-2 primary oil refining units\n2.
**Lazarevo Linear Production and Dispatching Station** (Kirov Oblast) - Oil pumping/storage facility - Struck May 31, damaged two RVS-50,000 M3 tanks and main pumping station buildings\n3. **Saratov
Oil Refinery** (Saratov Oblast) - Oil refinery - Struck May 31, damaged AVT-6 primary oil processing unit\n4. **Matveev Kurgan Oil Depot** (Rostov Oblast) - Oil depot - Struck May 31, satellite
imagery shows damage\n5. **Yaroslavl-3 Oil Pumping Station** - Oil pumping station - Struck May 19 and 29, destroyed storage tank\n6. **Volgograd Oil Refinery** - Oil refinery - Struck May 29, damaged
ELOU-AVT-1, ELOU-AVT-5, and technical overpasses; halted CDU-1, CDU-5, and CDU-6 units\n\n**Relevant links:**\n- [Ukrainian General Staff report on strikes](https://t.me/GeneralStaffZSU/39428)\n-
[Ukrainian Unmanned Systems Forces report on Ilsky refinery](https://t.me/usf_army/2010)\n- [Reuters report on Volgograd refinery halting operations](https://www.reuters.com/business/energy/russias-
volgograd-oil-refinery-halts-processing-after-may-29-drone-attack-2026-06-01/)", "title": "Russian Offensive Campaign Assessment, June 2, 2026"}
```

```json
{
  "url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-3-2026/",
  "prompt": "Extract all mentions of Ukrainian strikes on Russian oil refineries, oil infrastructure, energy facilities on June 3, 2026. List each target by name and type (refinery, terminal, depot)."
}
```

### 📋 Result

```
{"url": "https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-3-2026/", "content": "Based on the content, Ukrainian strikes on Russian oil/energy
infrastructure on June 3, 2026:\n\n1. **St. Petersburg Oil Terminal** (St. Petersburg, Leningrad Oblast) - Type: Oil terminal\n   - One of the largest oil transfer complexes in the Baltic Sea with 10
million tons/year capacity\n   - Struck and caused fire\n\nThe content notes this was \"the 20th Ukrainian strike against oil refining infrastructure in St. Petersburg since May 1,
2026.\"\n\n**Additional strikes reported on the night of June 2-3, 2026:**\n\n2. **Ilsky Oil Refinery** (Krasnodar Krai) - Type: Oil refinery\n   - Damaged technological overpass, AVT primary oil
processing unit, and two RVS-5000 tanks\n   - (Strike occurred June 2, damage assessment reported June 3)\n\n3. **Zenzevatka oil pumping station** (Volgograd Oblast) - Type: Oil pumping station\n   -
Forced to stop pumping operations\n   - (Strike occurred June 2, damage assessment reported June 3)\n\n**Note:** The content also mentions Ukrainian strikes on other military and industrial targets on
June 3, but these were not oil/energy facilities (e.g., Michurinsk Progress Plant producing weapons components, fuel and lubricants depot near Bilolutsk, naval assets).\n\nRelevant links:\n-
[Understanding War - Russian Offensive Campaign Assessment June 3, 2026](https://understandingwar.org/research/russia-ukraine/russian-offensive-campaign-assessment-june-3-2026/)", "title": "Russian
Offensive Campaign Assessment, June 3, 2026"}
```

## 💬 Response

Now I have excellent data. Let me compile the strikes in the June 1-3 window and estimate forward. Let me also check the question description's mentioned strikes from May to build a rate estimate.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "Moscow Times Russian oil refineries drone strikes May 2026 list capacity"
}
```

### 📋 Result

```
{"query": "Moscow Times Russian oil refineries drone strikes May 2026 list capacity", "results": [{"title": "Drone Strikes Force Central Russian Refineries to Halt or Cut Output \u2013 Reuters - The
Moscow Times", "url": "https://www.themoscowtimes.com/2026/05/20/drone-strikes-force-central-russian-refineries-to-halt-or-cut-output-reuters-a92805", "snippet": "Oil refineries in central Russia have
been forced to either suspend operations entirely or sharply reduce fuel output after a wave of drone attacks over the past two weeks, Reuters [reported](https://www.reuters.com/business/energy/oil-
refining-standstill-central-russia-after-ukrainian-drone-strikes-sources-say-2026-05-20/) Tuesday, citing official data and industry sources.\nRussia has already banned gasoline exports until July 31
as Ukraine ramps up its attacks against energy sites across the c", "api_data": null, "hint": null}, {"title": "Moscow Faces Record Drone Strikes, Dozens Injured as Oil Refinery Targeted - Bloomberg",
"url": "https://www.bloomberg.com/news/articles/2026-05-17/record-drone-attack-on-moscow-kills-three-targets-refinery", "snippet": null, "api_data": null, "hint": null}, {"title": "Ukrainian Drone
Attack Sparks Fire at Russian Oil Depot - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/05/23/ukrainian-drone-attack-sparks-fire-at-russian-oil-depot-a92826", "snippet": "A fire broke
out at an oil depot in the southern Russian port of Novorossiysk following a Ukrainian drone attack, the city's mayor said on Saturday.\n\"As a result of falling UAV (unmanned aerial vehicle) debris,
a fire broke out at the oil depot. Several technical and administrative buildings caught fire. Fragments of the drones also fell onto the fuel terminal site,\" Mayor Andrey Kravchenko wrote on
Telegram.\nTwo people were wounded, he added.\nNovorossiysk handles around a fifth of Russia's crud", "api_data": null, "hint": null}, {"title": "Ukrainian Drones Kill 4 and Set Ryazan Oil Refinery
Ablaze - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/05/15/ukrainian-drones-kill-4-and-set-ryazan-oil-refinery-ablaze-a92760", "snippet": "A Ukrainian drone barrage killed at least
four people and ignited a huge fire at an oil refinery in the city of Ryazan on Friday, in what appeared to be a direct retaliation for a deadly Russian strike on Kyiv a day earlier.\nRyazan region
Governor Pavel Malkov confirmed the deaths in posts on Telegram, adding that dozens of people, including children, were wounded in the attack. He [said](https://t.me/pavelmalkov_official/6325) drones
struck two apartment buildings and an industrial site, which ", "api_data": null, "hint": null}, {"title": "Reuters: Ukrainian Strikes Halt Nearly All Central Russian Oil Refineries", "url":
"https://militarnyi.com/en/news/ukraine-halt-most-cen-russia-oil-refineries/", "snippet": "Nearly all major oil refineries in central Russia have been forced to either shut down or cut fuel production
after a series of recent Ukrainian drone attacks.\n[Reuters](https://www.reuters.com/business/energy/oil-refining-standstill-central-russia-after-ukrainian-drone-strikes-sources-say-2026-05-20/)
reported this, citing its own sources and official data.\nAccording to the report, the refineries affected, either fully or partially, have a combined processing capacity of more than 83 million me",
"api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.themoscowtimes.com/2026/05/20/drone-strikes-force-central-russian-refineries-to-halt-or-cut-output-reuters-a92805",
  "prompt": "Extract the full list of refineries mentioned as struck or having halted/cut output in May 2026. List each refinery name and date."
}
```

### 📋 Result

```
{"url": "https://www.themoscowtimes.com/2026/05/20/drone-strikes-force-central-russian-refineries-to-halt-or-cut-output-reuters-a92805", "content": "Based on the article, here are the refineries
mentioned as struck or having halted/cut output in May 2026:\n\n1. **Kirishinefteorgsintez (KINEF)** - Fully offline since May 5\n2. **Yaroslavnefteorgsintez (YANOS)** - Operating at ~25% capacity
since last week (before May 20)\n3. **Ryazan refinery** - Suspended operations completely on May 15\n4. **Moscow refinery** - Shut down on May 17\n5. **Nizhny Novgorodnefteorgsintez (NORSI)** - Came
under attack on May 20 (partial operations status unclear)\n\nThe article also mentions refineries in **Kirishi** and **Nizhny Novgorod** as being \"among the large refineries targeted,\" though KINEF
is located in Kirishi and NORSI in Nizhny Novgorod, so these may refer to the same facilities already listed.\n\n**Relevant links:**\n- [Reuters report on oil refining standstill in central
Russia](https://www.reuters.com/business/energy/oil-refining-standstill-central-russia-after-ukrainian-drone-strikes-sources-say-2026-05-20/)\n- [Russian language version of this
article](https://ru.themoscowtimes.com/2026/05/20/neftepererabotka-v-tsentralnoi-rossii-prakticheski-ostanovilas-iz-za-atak-bpla-a195819)", "title": "Drone Strikes Force Central Russian Refineries to
Halt or Cut Output \u2013 Reuters - The Moscow Times"}
```

## 💬 Response

Now let me compile all the data and build my forecast model. Let me compute.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Compiling data on distinct oil REFINERIES struck by Ukrainian drones in the question window (June 1-13, 2026)\n# Key distinction: the question asks about oil REFINERIES specifically, NOT terminals, depots, pumping stations\n\n# == ALREADY CONFIRMED STRIKES (June 1-3, 2026) ==\n# Based on ISW assessments and news reports:\n\n# June 1: No new refinery strikes specifically reported for June 1 \n# (ISW June 1 assessment mentions satellite imagery of prior strikes at pumping stations/depots, not new refinery strikes)\n\n# June 2 (overnight June 1-2):\n# 1. Ilsky Oil Refinery (Krasnodar Krai) - CONFIRMED REFINERY, struck overnight June 1-2\n\n# ISW June 2 also reports BDA for prior strikes (May 29-31):\n# - Novoshakhtinsky Oil Refinery (Rostov Oblast) - struck May 31 - THIS IS IN THE WINDOW (June 1+)? \n#   Wait - May 31 is BEFORE June 1. So this doesn't count.\n# - Saratov Oil Refinery - struck May 31 - BEFORE June 1\n# - Volgograd Oil Refinery - struck May 29 - BEFORE June 1\n\n# June 3 (overnight June 2-3):\n# - St. Petersburg Oil Terminal - TERMINAL, NOT REFINERY (excluded by resolution criteria)\n# - Ilsky Oil Refinery damage assessment (already counted)\n# - Zenzevatka oil pumping station - PUMPING STATION (excluded)\n\n# Also from May 31 (just before window):\n# - Saratov Oil Refinery struck May 31\n# - Novoshakhtinsky Oil Refinery struck May 31\n# - Volgograd Oil Refinery struck May 29\n\n# So as of June 3 (today), confirmed REFINERIES struck in the June 1-13 window:\n# 1. Ilsky Oil Refinery (June 2) - CONFIRMED\n\nconfirmed_refineries = [\"Ilsky (June 2)\"]\nprint(f\"Confirmed distinct refineries struck June 1-3: {len(confirmed_refineries)}\")\nprint(f\"Refineries: {confirmed_refineries}\")\n\n# Note: St. Petersburg was an oil TERMINAL (excluded)\n# Note: Zenzevatka was a pumping station (excluded)\n# Note: Saratov, Novoshakhtinsky, Volgograd were struck May 29-31 (before window)\n\nprint(\"\\n== TEMPO ANALYSIS ==\")\n# From the question description and research, refineries struck in May 2026:\nmay_refineries = {\n    \"Kirishi (KINEF)\": \"May 5\",\n    \"Ryazan\": \"May 15\", \n    \"Moscow\": \"May 17\",\n    \"Yaroslavl (YANOS)\": \"~May 15-20\",\n    \"Nizhny Novgorod (NORSI)\": \"May 20\",\n    \"Syzran\": \"May 21\",\n    \"Volgograd\": \"May 28-29\",\n    \"Saratov\": \"May 31\",\n    \"Novoshakhtinsky\": \"May 31\",\n}\nprint(f\"Distinct refineries struck in May 2026: {len(may_refineries)}\")\nfor name, date in may_refineries.items():\n    print(f\"  - {name}: {date}\")\n\n# Rate calculation\n# May 2026 had ~9 distinct refineries struck over ~31 days\n# That's about 0.29 refineries/day or ~2 per week\n# But the rate was not uniform - there was a cluster in early-mid May (Kirishi, Ryazan, Moscow, YANOS, NORSI)\n# and then another cluster late May (Syzran, Volgograd, Saratov, Novoshakhtinsky)\n\n# For our 13-day window (June 1-13):\nrate_per_day = len(may_refineries) / 31\nexpected_from_rate = rate_per_day * 13\nprint(f\"\\nMay 2026 rate: {rate_per_day:.2f} refineries/day\")\nprint(f\"Expected from rate over 13 days: {expected_from_rate:.1f}\")\n\n# But some refineries are already offline and may not be re-struck (or may be re-struck for good measure)\n# The pool of available targets matters - 24 of 38 refineries have been hit at some point\n# Many are already damaged/offline, so strikes may shift to new or recovering targets\n\n# Also note: the question counts DISTINCT refineries, so hitting the same one twice doesn't increase the count\n# The Ilsky refinery has been hit 16 times - repeat strikes are common\n\nprint(\"\\n== ADDITIONAL CONTEXT ==\")\nprint(\"- Ukraine announced 'logistics lockdown' campaign May 27\")\nprint(\"- No ceasefire in effect\")\nprint(\"- 25% of Russian refining capacity already offline\")\nprint(\"- Campaign tempo has been ACCELERATING in 2026\")\nprint(\"- St. Petersburg Economic Forum (June 3-4) may provoke additional strikes\")\nprint(\"- Remaining 10 days in window (June 4-13)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Confirmed distinct refineries struck June 1-3: 1\nRefineries: ['Ilsky (June 2)']\n\n== TEMPO ANALYSIS ==\nDistinct refineries struck in May 2026: 9\n  - Kirishi (KINEF):
May 5\n  - Ryazan: May 15\n  - Moscow: May 17\n  - Yaroslavl (YANOS): ~May 15-20\n  - Nizhny Novgorod (NORSI): May 20\n  - Syzran: May 21\n  - Volgograd: May 28-29\n  - Saratov: May 31\n  -
Novoshakhtinsky: May 31\n\nMay 2026 rate: 0.29 refineries/day\nExpected from rate over 13 days: 3.8\n\n== ADDITIONAL CONTEXT ==\n- Ukraine announced 'logistics lockdown' campaign May 27\n- No
ceasefire in effect\n- 25% of Russian refining capacity already offline\n- Campaign tempo has been ACCELERATING in 2026\n- St. Petersburg Economic Forum (June 3-4) may provoke additional strikes\n-
Remaining 10 days in window (June 4-13)\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom scipy import stats\n\nnp.random.seed(42)\n\n# Monte Carlo simulation for distinct refineries struck June 1-13, 2026\nn_sims = 100000\n\n# Key parameters:\n# - 13-day window\n# - Already confirmed: 1 refinery (Ilsky) in first 3 days\n# - May 2026 had ~9 distinct refineries over 31 days\n\n# But we need to be careful about what Wikipedia will actually report\n# The resolution source is the Wikipedia timeline article\n# Not all strikes make it to Wikipedia - only well-documented ones with citations\n\n# Approach: Model the number of distinct refineries using empirical rates\n\n# Historical data points for strike rates (distinct refineries per 13-day period):\n# May 2026: 9 refineries in 31 days = ~3.8 per 13 days\n# But this was with ISW + Reuters confirmed; Wikipedia may be similar\n# August 2025: 14 refineries targeted in the month = ~5.9 per 13 days (peak period)\n# September 2025: 8 refineries in the month = ~3.4 per 13 days\n\n# Key considerations:\n# 1. Already 1 confirmed in first 3 days\n# 2. The \"logistics lockdown\" announced May 27 suggests continued high tempo\n# 3. Some days may have no refinery strikes (attacks on terminals, depots instead)\n# 4. Wikipedia lag - some June 1-13 strikes may not be logged by June 13\n\n# Model 1: Poisson process based on May 2026 rate\n# \u03bb = 9/31 * 13 = 3.77 per 13 days\n# But this is for TOTAL strikes - we need DISTINCT refineries\n# Since May had 9 distinct refineries, the distinct count IS the count (each was hit once in May)\n\n# Model 2: Consider the remaining 10 days (June 4-13) separately\n# Already have 1 confirmed. Need to model June 4-13 additions.\n\n# Rate for remaining period:\n# May rate: ~0.29 distinct refineries/day\n# But there's variance - some days have 0, some have 2-3\n\n# Let's model it as a Poisson process with some overdispersion\n# Using negative binomial to capture the clustering of strikes\n\n# From May data:\n# Week 1 (May 1-7): ~1 (Kirishi)\n# Week 2 (May 8-14): ~0 confirmed\n# Week 3 (May 15-21): ~5 (Ryazan, Moscow, YANOS, NORSI, Syzran)\n# Week 4 (May 22-28): ~1 (Volgograd)\n# Week 5 (May 29-31): ~2 (Saratov, Novoshakhtinsky)\n\n# This shows high variance/clustering\n# Mean per week: ~1.8, variance much higher\n\n# Let's use a negative binomial model\n# For 13 days at rate ~0.29/day, mean = 3.77\n# But with clustering, the variance is higher\n\n# Method: simulate day-by-day with a mixture model\n# On any given day, probability of at least one new distinct refinery being struck: ~0.25\n# (from May: 9 distinct refineries, some struck on same day, over 31 days)\n# When a strike day occurs, number of new refineries: mostly 1, sometimes 2\n\n# Actually, let me reconsider the data more carefully\n# The question asks for what Wikipedia reports, which filters for well-documented strikes\n\n# Let's think about it differently:\n# From the question description: The Caspian Policy Center logged 61 attacks across 24 refineries since Jan 2024\n# That's about 61 attacks / (24 months * 13/30) \u2248 over roughly equivalent periods\n# But the rate has accelerated sharply in 2026\n\n# May 2026 distinct refineries: ~9 in 31 days\n# BUT some of these might not all make it to the Wikipedia timeline article\n# The Wikipedia article is described as citation-backed and updated within days\n\n# Let me model three scenarios:\n\n# Scenario 1: Continued high tempo (like mid-May to early June)\n# ~0.35 distinct refineries/day \u2192 ~4.5 over 13 days (already have 1, add ~3.5 more)\n\n# Scenario 2: Moderate tempo (overall May average)\n# ~0.29 distinct refineries/day \u2192 ~3.8 over 13 days\n\n# Scenario 3: Lower tempo (if Russia improves air defenses, or strikes shift to non-refinery targets)\n# ~0.15 distinct refineries/day \u2192 ~2 over 13 days\n\n# Note: We already KNOW 1 refinery (Ilsky) for the first 3 days\n# For the remaining 10 days, we model additions\n\n# Monte Carlo with day-by-day Poisson arrivals + some clustering\n\nresults = []\nfor _ in range(n_sims):\n    # Already have 1 confirmed for June 1-3\n    distinct_count = 1\n    \n    # For remaining 10 days (June 4-13):\n    # Daily rate varies - draw from a distribution\n    # Base rate: ~0.29/day, but with uncertainty\n    daily_rate = np.random.gamma(shape=3.0, scale=0.29/3.0)  # mean 0.29, some variance\n    \n    # Each day, Poisson arrivals of new distinct refineries\n    for day in range(10):\n        new_today = np.random.poisson(daily_rate)\n        distinct_count += new_today\n    \n    results.append(distinct_count)\n\nresults = np.array(results)\n\n# But wait - there's a saturation effect. There are only ~38 major refineries in Russia\n# and 24 have already been hit. The pool of targets is finite but large enough\n# that saturation isn't a real constraint for 13 days at this rate.\n\n# Also need to account for: maybe some June 1-3 strikes haven't been confirmed yet\n# (e.g., a refinery struck on June 1 that hasn't been reported yet)\n# Let's add a probability of 0-1 additional \"hidden\" June 1-3 strikes\n\nresults_adjusted = []\nfor r in results:\n    # Probability of additional unreported June 1-3 refinery strike\n    hidden = np.random.binomial(1, 0.3)  # 30% chance of 1 more from first 3 days\n    results_adjusted.append(r + hidden)\n\nresults_adjusted = np.array(results_adjusted)\n\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nprint(\"Percentile distribution of distinct refineries struck (June 1-13):\")\nfor p in percentiles:\n    val = np.percentile(results_adjusted, p)\n    print(f\"  P{p:2d}: {val:.1f}\")\n\nprint(f\"\\nMean: {np.mean(results_adjusted):.2f}\")\nprint(f\"Median: {np.median(results_adjusted):.1f}\")\nprint(f\"Std: {np.std(results_adjusted):.2f}\")\nprint(f\"Min: {np.min(results_adjusted)}, Max: {np.max(results_adjusted)}\")\nprint(f\"\\nP(0): {np.mean(results_adjusted == 0)*100:.1f}%\")\nprint(f\"P(1): {np.mean(results_adjusted == 1)*100:.1f}%\")\nprint(f\"P(2): {np.mean(results_adjusted == 2)*100:.1f}%\")\nprint(f\"P(3): {np.mean(results_adjusted == 3)*100:.1f}%\")\nprint(f\"P(4): {np.mean(results_adjusted == 4)*100:.1f}%\")\nprint(f\"P(5): {np.mean(results_adjusted == 5)*100:.1f}%\")\nprint(f\"P(6): {np.mean(results_adjusted == 6)*100:.1f}%\")\nprint(f\"P(7+): {np.mean(results_adjusted >= 7)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Percentile distribution of distinct refineries struck (June 1-13):\n  P 1: 1.0\n  P 5: 1.0\n  P10: 2.0\n  P20: 2.0\n  P25: 2.0\n  P30: 3.0\n  P40: 3.0\n  P50: 4.0\n  P60:
4.0\n  P70: 5.0\n  P75: 5.0\n  P80: 6.0\n  P90: 7.0\n  P95: 9.0\n  P99: 12.0\n\nMean: 4.19\nMedian: 4.0\nStd: 2.43\nMin: 1, Max: 21\n\nP(0): 0.0%\nP(1): 9.3%\nP(2): 17.7%\nP(3): 19.2%\nP(4):
16.7%\nP(5): 12.6%\nP(6): 8.9%\nP(7+): 15.6%\n", "stderr": "", "duration_ms": 1903}
```

## 💭 Thinking

Let me refine this model. I need to think more carefully about:

1. The distinction between refineries vs terminals/depots/pumping stations
2. The Wikipedia reporting lag and what actually gets listed
3. The actual rate of distinct REFINERY strikes specifically

Let me also consider that the question asks specifically about what Wikipedia reports, and there may be a filtering effect - not all strikes get documented on Wikipedia.

Let me also reconsider the May data more carefully. The question description mentions specific refineries in May:
- Kirishi (KINEF) - May 5
- Ryazan - May 15
- Moscow - May 17


- Yaroslavl (YANOS) - ~25% capacity
- Nizhny Novgorod (NORSI) - May 20
- Syzran - May 21
- Volgograd - May 28-29
- Saratov - May 31
- Novoshakhtinsky - May 31

That gives me 9 distinct refineries in May, though I need to distinguish between new strikes and re-strikes of previously damaged facilities. For June, the ISW data shows Ilsky Oil Refinery on June 2 as a confirmed refinery strike, while the St. Petersburg facility on June 3 is a terminal so it gets excluded from the count.

Looking at the Saratov strike timing, both Al Jazeera and ISW confirm it occurred on May 31, placing it before my June 1-3 window. So for the first three days of June, I only have one confirmed new refinery strike. Now I need to estimate how many additional distinct refineries might be targeted during June 4-13. Looking back at my May data, I'm confirming that all nine targets I listed were actually refineries, not mixed in with terminals or depots—so the 0.29 per day rate specifically applies to refinery strikes.

But I need to account for Wikipedia's reporting lag. Since the article is described as updated within days of events, strikes near the end of the June 13 window might not have made it into the snapshot yet. That effectively shortens my observation window by roughly a day, which is a modest adjustment to factor into my simulation alongside the actual refinery rate and the clustering pattern I've observed.

Now I'm refining my approach to focus on the core question: given the current strike tempo, how many distinct refineries will actually appear in the Wikipedia article over this 13-day period? I should verify whether ISW has captured all the refinery strikes or if there are gaps that other sources like Reuters might fill, though ISW tends to be fairly thorough.

Looking at the historical data, May 2026 shows roughly 2-3 distinct refineries per week, which would suggest somewhere between 3-6 refineries over 13 days. Given that one is already confirmed in the first three days, the escalation context with the logistics lockdown, and the absence of any ceasefire, I'm leaning toward the higher end of that range.

But I should also account for what could derail this trajectory—improved Russian air defenses, a sudden ceasefire announcement, drone supply constraints, or a shift in targeting priorities away from refineries. On the flip side, there's potential for major escalation with multiple hits per night, or for Wikipedia to capture additional strikes that weren't initially tracked by ISW. Let me adjust my simulation parameters to reflect these scenarios.

## 💬 Response

Let me refine the simulation with better parameters and sensitivity analysis.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom collections import Counter\n\nnp.random.seed(42)\nn_sims = 200000\n\n# REFINED MODEL\n# \n# Key data points:\n# - May 2026: 9 distinct REFINERIES struck over 31 days = 0.290/day\n# - Already confirmed: 1 refinery (Ilsky) in first 3 days of June\n# - Remaining window: 10 days (June 4-13)\n# - But Wikipedia has ~1 day reporting lag, so effectively ~9-10 days of additional reporting\n#\n# Important: Many non-refinery targets are also hit (terminals, depots, pumping stations)\n# The question ONLY counts refineries (crude oil refining plants)\n# \n# From June 1-3 data: lots of non-refinery targets hit (St. Pete terminal, \n# Zenzevatka pumping station, Armavir depot, etc.) - only Ilsky was a REFINERY\n#\n# So the refinery-specific rate may be slightly lower than what we'd expect\n# from May data, as Ukraine increasingly targets terminals and logistics too\n\n# May weekly pattern (distinct refineries):\n# Week 1 (May 1-7): 1 (Kirishi)\n# Week 2 (May 8-14): 0 \n# Week 3 (May 15-21): 5 (Ryazan, Moscow, YANOS, NORSI, Syzran) \n# Week 4 (May 22-28): 1 (Volgograd)\n# Week 5 (May 29-31): 2 (Saratov, Novoshakhtinsky) - 3 days only \u2192 equivalent to ~4.7/week\n\n# The variance is HIGH - ranges from 0 to 5 per week\n# This suggests negative binomial is appropriate\n\n# Fit negative binomial to weekly data\nweekly_counts = [1, 0, 5, 1]  # 4 full weeks\n# 3-day partial: 2 refineries in 3 days\n\nmean_weekly = np.mean(weekly_counts)\nvar_weekly = np.var(weekly_counts, ddof=1)\nprint(f\"Weekly mean: {mean_weekly:.2f}\")\nprint(f\"Weekly variance: {var_weekly:.2f}\")\nprint(f\"Overdispersion ratio: {var_weekly/mean_weekly:.2f}\")\n\n# Scale to 13-day period\n# mean_13d = mean_weekly * 13/7 = 1.75 * 1.857 = 3.25\n# But including the partial week (2 in 3 days), the overall rate is 9/31 * 13 = 3.77\n\n# Let me use multiple scenarios\n\ndef simulate_scenario(base_rate_per_day, rate_uncertainty, n_sims, confirmed=1, remaining_days=10):\n    \"\"\"Simulate distinct refinery count with rate uncertainty\"\"\"\n    results = []\n    for _ in range(n_sims):\n        # Draw rate from distribution reflecting uncertainty\n        rate = np.random.gamma(\n            shape=base_rate_per_day**2 / rate_uncertainty**2,\n            scale=rate_uncertainty**2 / base_rate_per_day\n        )\n        rate = max(0, rate)\n        \n        # New refineries in remaining period\n        new_refineries = np.random.poisson(rate * remaining_days)\n        \n        results.append(confirmed + new_refineries)\n    return np.array(results)\n\n# Scenario 1: Base case - May 2026 rate continues\n# Rate: 9/31 = 0.290/day, uncertainty ~0.15\nbase_results = simulate_scenario(0.290, 0.15, n_sims)\n\n# Scenario 2: Accelerating tempo (logistics lockdown escalation)\n# Rate: ~0.35/day (like peak week of May)\nhigh_results = simulate_scenario(0.35, 0.18, n_sims)\n\n# Scenario 3: Lower tempo (strikes shifting to non-refinery targets, some AD improvement)\n# Rate: ~0.20/day\nlow_results = simulate_scenario(0.20, 0.12, n_sims)\n\n# Scenario 4: Wikipedia reporting filter\n# Not all strikes make it to Wikipedia by June 13\n# Effective capture rate ~85-90% (some June 11-13 strikes might be missed)\n# Apply filter to base case\nwiki_filter = np.random.binomial(1, 0.90, size=(n_sims, 15))  # pre-generate\n\n# Weight scenarios\n# Base: 50%, High: 25%, Low: 25%\nweights = [0.50, 0.25, 0.25]\ncombined = np.zeros(n_sims, dtype=int)\nfor i in range(n_sims):\n    r = np.random.random()\n    if r < weights[0]:\n        combined[i] = base_results[i]\n    elif r < weights[0] + weights[1]:\n        combined[i] = high_results[i]\n    else:\n        combined[i] = low_results[i]\n\n# Apply Wikipedia reporting lag discount (~10% chance a late-window strike is missed)\n# This effectively reduces the count by 0 or 1 with some probability\nfor i in range(n_sims):\n    if combined[i] > 1 and np.random.random() < 0.10:\n        combined[i] -= 1\n\n# Also add small probability of unreported June 1-3 refinery strike\nfor i in range(n_sims):\n    if np.random.random() < 0.20:  # 20% chance of 1 additional from first 3 days\n        combined[i] += 1\n\nprint(\"\\n=== COMBINED FORECAST ===\")\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nfor p in percentiles:\n    val = np.percentile(combined, p)\n    print(f\"  P{p:2d}: {val:.0f}\")\n\nprint(f\"\\nMean: {np.mean(combined):.2f}\")\nprint(f\"Median: {np.median(combined):.1f}\")\nprint(f\"Std: {np.std(combined):.2f}\")\n\nprint(\"\\n=== PROBABILITY MASS FUNCTION ===\")\ncounter = Counter(combined)\ntotal = len(combined)\nfor k in sorted(counter.keys()):\n    pct = counter[k] / total * 100\n    if pct >= 0.1:\n        print(f\"  P(X={k:2d}): {pct:5.1f}%  {'\u2588' * int(pct)}\")\n\nprint(f\"\\n  P(X>=10): {np.mean(combined >= 10)*100:.1f}%\")\nprint(f\"  P(X>=15): {np.mean(combined >= 15)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Weekly mean: 1.75\nWeekly variance: 4.92\nOverdispersion ratio: 2.81\n\n=== COMBINED FORECAST ===\n  P 1: 1\n  P 5: 1\n  P10: 1\n  P20: 2\n  P25: 2\n  P30: 2\n  P40: 3\n
P50: 3\n  P60: 4\n  P70: 5\n  P75: 5\n  P80: 6\n  P90: 7\n  P95: 8\n  P99: 11\n\nMean: 3.94\nMedian: 3.0\nStd: 2.36\n\n=== PROBABILITY MASS FUNCTION ===\n  P(X= 1):  12.4%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 2):  18.8%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 3):  19.1%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 4):  16.0%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 5):  12.0%  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 6):   8.1%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 7):   5.4%  \u2588\u2588\u2588\u2588\u2588\n  P(X= 8):   3.4%  \u2588\u2588\u2588\n  P(X= 9):   2.1%  \u2588\u2588\n  P(X=10):   1.1%  \u2588\n
P(X=11):   0.7%  \n  P(X=12):   0.4%  \n  P(X=13):   0.2%  \n  P(X=14):   0.1%  \n\n  P(X>=10): 2.7%\n  P(X>=15): 0.2%\n", "stderr": "", "duration_ms": 858}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also run a sensitivity analysis and check the model against the data\n\n# Sanity check: If I apply this model to May 2026 (31 days), what do I get?\nmay_sim = simulate_scenario(0.290, 0.15, 100000, confirmed=0, remaining_days=31)\nprint(f\"Model applied to May (31 days): mean={np.mean(may_sim):.1f}, median={np.median(may_sim):.0f}\")\nprint(f\"Actual May count: 9 distinct refineries\")\nprint(f\"Model P(X>=9) for May: {np.mean(may_sim >= 9)*100:.1f}%\")\nprint(f\"Model P5-P95 for May: {np.percentile(may_sim, 5):.0f} - {np.percentile(may_sim, 95):.0f}\")\n\n# The model's mean (9.0 for May) matches the observed 9, good.\n\nprint(\"\\n=== ALTERNATIVE APPROACH: Use weekly counts directly ===\")\n# Model 13 days as roughly 2 weeks\n# Weekly counts from May: [1, 0, 5, 1] (first 4 full weeks)\n# Mean 1.75/week, high variance\n\n# Bootstrap from observed weekly data\nweekly_data = [1, 0, 5, 1, 2*7/3]  # last is scaled 3-day partial\n# Actually, better to use the 4 full weeks + recognize the half-week\nweekly_data_full = [1, 0, 5, 1]\n\nn_boot = 200000\nboot_results = []\nfor _ in range(n_boot):\n    # Sample 2 \"weeks\" (to cover ~13 days, which is ~1.86 weeks)\n    # Sample 1 full week and then a partial\n    w1 = np.random.choice(weekly_data_full)\n    # For partial week (6/7 of a week), scale proportionally\n    w2_full = np.random.choice(weekly_data_full) \n    w2 = np.random.binomial(w2_full, 6/7) if w2_full > 0 else 0\n    \n    total = w1 + w2\n    # Ensure at least 1 (we have confirmed data)\n    total = max(total, 1)\n    boot_results.append(total)\n\nboot_results = np.array(boot_results)\nprint(f\"Bootstrap mean: {np.mean(boot_results):.2f}\")\nprint(f\"Bootstrap median: {np.median(boot_results):.0f}\")\n\nprint(\"\\nBootstrap percentiles:\")\nfor p in [5, 10, 25, 50, 75, 90, 95]:\n    print(f\"  P{p}: {np.percentile(boot_results, p):.0f}\")\n\nprint(\"\\nBootstrap PMF:\")\nfor k in range(12):\n    pct = np.mean(boot_results == k) * 100\n    if pct >= 0.5:\n        print(f\"  P(X={k}): {pct:.1f}%\")\n\n# Compare the two approaches\nprint(\"\\n=== COMPARISON ===\")\nprint(f\"Poisson-mixture model: mean={np.mean(combined):.2f}, median={np.median(combined):.0f}\")\nprint(f\"Bootstrap model: mean={np.mean(boot_results):.2f}, median={np.median(boot_results):.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Model applied to May (31 days): mean=9.0, median=8\nActual May count: 9 distinct refineries\nModel P(X>=9) for May: 46.5%\nModel P5-P95 for May: 2 - 19\n\n=== ALTERNATIVE
APPROACH: Use weekly counts directly ===\nBootstrap mean: 3.32\nBootstrap median: 2\n\nBootstrap percentiles:\n  P5: 1\n  P10: 1\n  P25: 1\n  P50: 2\n  P75: 5\n  P90: 6\n  P95: 9\n\nBootstrap PMF:\n
P(X=1): 34.8%\n  P(X=2): 21.7%\n  P(X=3): 1.1%\n  P(X=4): 4.0%\n  P(X=5): 15.7%\n  P(X=6): 16.6%\n  P(X=8): 0.8%\n  P(X=9): 2.3%\n  P(X=10): 2.8%\n\n=== COMPARISON ===\nPoisson-mixture model:
mean=3.94, median=3\nBootstrap model: mean=3.32, median=2\n", "stderr": "", "duration_ms": 1595}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The bootstrap is bimodal due to the highly variable weekly data (0 vs 5)\n# The Poisson-mixture model is more reasonable for continuous outcomes\n# Let me create a final combined estimate using both approaches\n\n# The bootstrap shows the clustering effect more strongly\n# But with only 4 data points, it's noisy\n\n# Let me use a better approach: negative binomial with observed parameters\n\nfrom scipy.stats import nbinom\n\n# From May weekly data: mean=1.75, var=4.92\n# Negative binomial: r = mean^2/(var - mean) = 1.75^2/(4.92-1.75) = 3.0625/3.17 = 0.966\n# p = mean/var = 1.75/4.92 = 0.356\n# Actually, parameterization: nbinom with n=r, p\n# mean = n(1-p)/p, var = n(1-p)/p^2\n# So p = mean/var = 1.75/4.92 = 0.356\n# n = mean*p/(1-p) = 1.75*0.356/0.644 = 0.965\n\n# For 13 days = 1.857 weeks, scale parameters\n# New mean = 1.75 * 1.857 = 3.25\n# New variance = var scales with time (approximately, for overdispersed process)\n# var_13d = 4.92 * 1.857 = 9.13\n\n# But actually, for a negative binomial process, over a longer period the \n# overdispersion ratio changes. Let me just use a simple model.\n\n# Final model: Use the Poisson-mixture as the primary model, but\n# adjust for the high variance observed in the data\n\n# The May weekly data has mean 1.75 and variance 4.92 (overdispersion ratio 2.81)\n# This means the arrival process is quite \"bursty\"\n\n# For 13 days (~1.86 weeks):\n# Expected mean: ~3.25 (from weekly rate * 1.86)\n# But with overdispersion\n\n# Let me use a negative binomial directly\n# NB parameters for 13-day period:\nmean_13d = 1.75 * 13/7\nvar_13d = 4.92 * (13/7)  # assuming variance scales linearly (generous)\n\n# Actually overdispersion might not scale linearly. Let me use a more conservative approach.\n# Over 2 weeks, the two weeks are somewhat independent, so variance is additive\n# But clustering within weeks means some carries over.\n\n# Use: compound Poisson with random rate\n# Rate ~ Gamma(alpha, beta) where mean=0.290/day, cv ~0.5-0.7\n# Then X|rate ~ Poisson(rate * 13)\n\n# Let me compute final percentiles using a proper negative binomial\n# parameterized by the 13-day mean and overdispersion\n\nfrom scipy.stats import nbinom\nimport warnings\nwarnings.filterwarnings('ignore')\n\n# Mean of 3.25, overdispersion parameter\n# NB: mean = r(1-p)/p, var = r(1-p)/p^2\n# So overdispersion factor (var/mean) = 1/p\n# From weekly data: overdispersion = 4.92/1.75 = 2.81\n# For 13 days, assume overdispersion reduces slightly (longer periods average out)\n# Use overdispersion = 2.5\n\nmean_val = 3.5  # slightly higher than 3.25 to account for escalation trend\noverdispersion = 2.3  # variance/mean ratio\n\np_nb = 1.0 / overdispersion  # probability parameter\nr_nb = mean_val * p_nb / (1 - p_nb)  # size parameter\n\nprint(f\"Negative binomial parameters: r={r_nb:.2f}, p={p_nb:.3f}\")\nprint(f\"NB mean: {r_nb*(1-p_nb)/p_nb:.2f}\")\nprint(f\"NB variance: {r_nb*(1-p_nb)/p_nb**2:.2f}\")\n\n# Generate samples\nnb_samples = nbinom.rvs(r_nb, p_nb, size=200000)\n# Ensure minimum of 1 (since we have confirmed data)\nnb_samples = np.maximum(nb_samples, 1)\n\n# Add the \"hidden June 1-3 strike\" probability\nfor i in range(len(nb_samples)):\n    if np.random.random() < 0.15:\n        nb_samples[i] += 1\n\nprint(f\"\\n=== FINAL MODEL (NB + floor at 1) ===\")\nprint(f\"Mean: {np.mean(nb_samples):.2f}\")\nprint(f\"Median: {np.median(nb_samples):.0f}\")\n\nprint(\"\\nPercentiles:\")\nfinal_pcts = {}\nfor p in [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]:\n    val = np.percentile(nb_samples, p)\n    final_pcts[str(p)] = val\n    print(f\"  P{p:2d}: {val:.0f}\")\n\nprint(\"\\nPMF:\")\nfor k in range(16):\n    pct = np.mean(nb_samples == k) * 100\n    if pct >= 0.1:\n        print(f\"  P(X={k:2d}): {pct:5.1f}%  {'\u2588' * int(pct)}\")\n\nprint(f\"\\n  P(X>=10): {np.mean(nb_samples >= 10)*100:.1f}%\")\nprint(f\"  P(X>=15): {np.mean(nb_samples >= 15)*100:.1f}%\")\nprint(f\"  P(X>=16): {np.mean(nb_samples >= 16)*100:.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Negative binomial parameters: r=2.69, p=0.435\nNB mean: 3.50\nNB variance: 8.05\n\n=== FINAL MODEL (NB + floor at 1) ===\nMean: 3.76\nMedian: 3\n\nPercentiles:\n  P 1: 1\n
P 5: 1\n  P10: 1\n  P20: 1\n  P25: 2\n  P30: 2\n  P40: 2\n  P50: 3\n  P60: 4\n  P70: 5\n  P75: 5\n  P80: 6\n  P90: 7\n  P95: 9\n  P99: 13\n\nPMF:\n  P(X= 1):  22.6%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 2):  18.4%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 3):  15.2%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 4):  12.5%  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 5):
9.5%  \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 6):   7.0%  \u2588\u2588\u2588\u2588\u2588\u2588\n  P(X= 7):   4.9%  \u2588\u2588\u2588\u2588\n  P(X= 8):   3.4%
\u2588\u2588\u2588\n  P(X= 9):   2.2%  \u2588\u2588\n  P(X=10):   1.5%  \u2588\n  P(X=11):   1.0%  \n  P(X=12):   0.6%  \n  P(X=13):   0.4%  \n  P(X=14):   0.3%  \n  P(X=15):   0.2%  \n\n  P(X>=10):
4.2%\n  P(X>=15): 0.4%\n  P(X>=16): 0.3%\n", "stderr": "", "duration_ms": 84}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Now let me reconcile the two models (Poisson-mixture and NB) and create final percentiles\n\n# Both models give similar results:\n# Poisson-mixture: mean=3.94, median=3, P10=1, P50=3, P90=7\n# NB model: mean=3.76, median=3, P10=1, P50=3, P90=7\n\n# They're quite consistent. Let me average them for the final estimate.\n\n# But first, let me think about whether the models are too conservative or too aggressive:\n\n# Arguments for HIGHER count:\n# 1. \"Logistics lockdown\" announced May 27 - explicit escalation\n# 2. The tempo in late May was ~4-5 refineries/week (Syzran May 21, Volgograd May 28, \n#    Saratov May 31, Novoshakhtinsky May 31, plus Ilsky June 2)\n# 3. St. Petersburg Economic Forum timing (June 3-7) motivates spectacular strikes\n# 4. Ukraine has demonstrated 1700km+ range - more targets accessible\n\n# Arguments for LOWER count:\n# 1. Many refineries already offline - less strategic value in re-striking\n# 2. Russia improving air defenses (354 drones claimed intercepted June 3)\n# 3. Strikes may shift to military targets, terminals, depots instead of refineries\n# 4. Wikipedia reporting lag may miss some late-window strikes\n# 5. Only 1 confirmed refinery in first 3 days despite heavy strikes\n\n# The rate of 1 refinery in first 3 days (0.33/day) is actually close to the May rate (0.29/day)\n# So the current tempo seems consistent with May.\n\n# I'll weight toward the Poisson-mixture model slightly as it better captures\n# the scenario mixing effect.\n\n# FINAL PERCENTILES (integer values for discrete question):\nfinal_percentiles = {\n    \"1\": 0,    # Can't go below 0, but with confirmed 1, min is 1\n    \"5\": 1,\n    \"10\": 1,\n    \"20\": 2,\n    \"25\": 2,\n    \"30\": 2,\n    \"40\": 3,\n    \"50\": 3,\n    \"60\": 4,\n    \"70\": 5,\n    \"75\": 5,\n    \"80\": 6,\n    \"90\": 7,\n    \"95\": 9,\n    \"99\": 12\n}\n\nprint(\"=== FINAL PERCENTILE ESTIMATES ===\")\nfor p, v in final_percentiles.items():\n    print(f\"  P{p:>2}: {v}\")\n\nprint(f\"\\nImplied distribution center (median): 3\")\nprint(f\"Implied P10-P90 range: 1-7\")\nprint(f\"Key probability masses:\")\nprint(f\"  P(X=0): ~0% (impossible - already have 1 confirmed)\")\nprint(f\"  P(X=1): ~15% (only the already-confirmed Ilsky)\")  \nprint(f\"  P(X=2-3): ~35% (1-2 more refineries)\")\nprint(f\"  P(X=4-6): ~30% (steady May-like tempo)\")\nprint(f\"  P(X=7-9): ~12% (accelerated tempo)\")\nprint(f\"  P(X>=10): ~4% (major escalation)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== FINAL PERCENTILE ESTIMATES ===\n  P 1: 0\n  P 5: 1\n  P10: 1\n  P20: 2\n  P25: 2\n  P30: 2\n  P40: 3\n  P50: 3\n  P60: 4\n  P70: 5\n  P75: 5\n  P80: 6\n  P90: 7\n  P95:
9\n  P99: 12\n\nImplied distribution center (median): 3\nImplied P10-P90 range: 1-7\nKey probability masses:\n  P(X=0): ~0% (impossible - already have 1 confirmed)\n  P(X=1): ~15% (only the already-
confirmed Ilsky)\n  P(X=2-3): ~35% (1-2 more refineries)\n  P(X=4-6): ~30% (steady May-like tempo)\n  P(X=7-9): ~12% (accelerated tempo)\n  P(X>=10): ~4% (major escalation)\n", "stderr": "",
"duration_ms": 0}
```

## 💬 Response

Now let me run the reflection and premortem steps.

## 💬 Response

Good - the reflection metrics show my tentative estimate (center=3) is 15% below the factor-implied median of 3.7, which is a modest gap. The spread ratio of 1.26 means my distribution is slightly wider than the factors imply, which seems appropriate given the high overdispersion. Let me run the premortem.
