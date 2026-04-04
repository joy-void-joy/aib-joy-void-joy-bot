# Reasoning Log: Will any single oil spill larger than 50,000 barrels occur in the Gulf of Oman before May 1, 2026?

*Generated: 2026-04-04T13:43:38.959864+00:00*


## 💭 Thinking

Let me analyze this forecasting question carefully.

## Step 1: Parse the Resolution Criteria

**What exactly must happen for YES resolution?**
- A single oil spill larger than 50,000 barrels must occur in the Gulf of Oman
- The spill must be conflict-related
- It must be reported by ITOPF, UNEP, NOAA, or another credible source before May 1, 2026
- Multiple smaller spills do NOT aggregate

**Deadline:** May 1, 2026


The question closes today with only about 27 days until resolution, so I'm essentially evaluating whether a conflict-related oil spill exceeding 50,000 barrels has already occurred or will happen very soon in the Gulf of Oman. The threshold is substantial—roughly 6,800 metric tonnes—and must be a single event, not accumulated from multiple incidents.

## 💬 Response

I'll analyze this question systematically. Let me start by understanding the current situation in the Gulf of Oman region.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43054
  ]
}
```

### 📋 Result

```
{"post_id": 43054, "title": "Will any single oil spill larger than 50,000 barrels occur in the Gulf of Oman before May 1, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43054",
"background_info": "This question tracks whether the conflict produces a major marine environmental disaster in a critical energy
corridor.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"4ec9605bd62d7cde\",\"sheet_id\":505.2}}`", "resolution_criteria": "This question resolves to yes if ITOPF, UNEP, NOAA, or
another credible source under the Metaculus policy at https://www.metaculus.com/faq/#definitions reports before May 1, 2026 that a single spill larger than 50000 barrels occurred in the Gulf of Oman.
Otherwise, this question resolves to no.", "fine_print": "The spill must be both conflict-related and larger than 50,000 barrels. Multiple smaller spills do not aggregate. Candidate Sources: ITOPF
https://www.itopf.org/ ; UNEP https://www.unep.org/", "num_forecasters": 58, "community_prediction": null}
```

## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "oil spill Gulf of Oman 2026",
  "n_articles": 10,
  "hours_back": 720
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

```json
{
  "query": "Gulf of Oman conflict attack shipping tanker 2026",
  "n_articles": 10,
  "hours_back": 720
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

## 💬 Response

Let me search for relevant news through other channels.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "oil spill Gulf of Oman 2026 conflict"
}
```

### 📋 Result

```
{"query": "oil spill Gulf of Oman 2026 conflict", "results": [{"title": "2026 Strait of Hormuz crisis - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The
Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the
United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli
territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz
crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing
geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei.
In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings
prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and
later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21
confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit, with tanker traffic dropping first by approximately 70% and over 150
ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about 20% of the world's daily oil supply and significant volumes of
liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the
ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other conflict in recent history; Brent crude oil prices surpassed
US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has been described as the largest disruption to the energy supply
since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price increases from the crisis include aluminum, fertilizer, and
helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a strait used for international navigation.\\n\\n\", \"mode\":
\"full\"}"}]}, "hint": null}, {"title": "Oman Evacuates Oil Port as Ships Hit in Gulf", "url":
"https://www.rigzone.com/news/wire/oman_evacuates_oil_port_as_ships_hit_in_gulf-12-mar-2026-183189-article/", "snippet": "Oman Evacuates Oil Port as Ships Hit in Gulf\n![Oman Evacuates Oil Port as
Ships Hit in Gulf](https://images.rigzone.com/images/news/articles/Oman-Evacuates-Oil-Port-as-Ships-Hit-in-Gulf-183189-582x327.webp)\nTwo crude tankers were hit in Iraqi waters and Oman's key oil
export terminal was evacuated, as risks to global energy supply from the Middle East war deepened.\nThe attacks on the vessels off the coast of Iraq prompted the nation's oil terminals to suspend
operations. Ships, meanwhile, were o", "api_data": null, "hint": null}, {"title": "Tanker War of 2026: Strait of Hormuz Closure Disrupts Global Oil and LNG Trade", "url":
"https://openthemagazine.com/world/strait-of-hormuz-shut-tanker-war-of-2026-disrupts-global-oil-and-lng-trade", "snippet": "The US-Israel coalition\u2019s intensifying war with Iran, marked by
Operation Epic Fury, has triggered the Tanker War of 2026 -- the gravest maritime trade disruption since World War II. Western-flagged vessels now shun key chokepoints, forcing radical rerouting and
skyrocketing costs across the shipping industry.\nHere\u2019s a deeper insight.\nThe Tanker War erupted as Operation Epic Fury targeted Iranian assets, prompting retaliatory strikes on shipping lanes.
Reportedly, Iran mined the Strait of Hormuz", "api_data": null, "hint": null}, {"title": "The Iran War and the End of the US-Gulf \u201cOil for Security\u201d Deal", "url":
"https://arabcenterdc.org/resource/the-iran-war-and-the-end-of-the-us-gulf-oil-for-security-deal/", "snippet": "![](https://arabcenterdc.org/wp-content/smush-webp/2026/03/tankers-stuck-strait-of-
Hormuz-768x432.jpg.webp)\nIn early March 2026, Iran effectively [closed](https://www.reuters.com/world/middle-east/iran-vows-attack-any-ship-trying-pass-through-strait-hormuz-2026-03-02/) the Strait
of Hormuz in response to the war launched by the United States and Israel, making it impossible for oil and gas to be exported from the Gulf without its agreement. The Hormuz blockage is the biggest
market [disruption](", "api_data": null, "hint": null}, {"title": "Which oil and gas facilities in the Gulf have been attacked? | Infographic News | Al Jazeera", "url":
"https://www.aljazeera.com/news/2026/3/4/which-oil-and-gas-facilities-in-the-gulf-have-been-attacked", "snippet": "Which oil and gas facilities in the Gulf have been attacked?\nDamage to several
energy facilities has caused global prices to spike, but Iran denies it is targeting energy sites.\n![INTERACTIVE_IRAN_GCC_OIL AND GAS SUPPLY-OUTSIDE IMAGE](/wp-
content/uploads/2026/03/INTERACTIVE_IRAN_GCC_OIL-AND-GAS-SUPPLY-06-1772630810.png?resize=770%2C513&quality=80)\nGlobal energy markets remain in a state of high alert after several Gulf states
suspended oil and gas production following escalating tensions in the ", "api_data": null, "hint": null}, {"title": "Oman Says Oil Tanker Targeted Off Its North Coast", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "Strait of Hormuz Global Oil, Gas
Trade Disrupted Amid Iran War", "url": "https://time.com/7382242/strait-of-hormuz-closure-threat-iran-war-trade-gas-oil-prices/", "snippet": "Global oil and gas prices have surged as the [Iran
war](https://time.com/7381950/iran-war-khamenei-strikes-tehran/) has brought the crucial Strait of Hormuz, a narrow passage between the Persian Gulf and the Gulf of Oman through which around a fifth
of global oil production flows, to a halt.\nAs of Tuesday, Brent crude oil prices [have risen](https://tradingeconomics.com/commodity/brent-crude-oil) by around 7%, reaching as high as $83 per barrel.
When markets closed on Friday, ahead of the Iran w", "api_data": null, "hint": null}, {"title": "Another oil tanker hit by drone boat as Strait of Hormuz tensions rise | Euronews", "url":
"https://www.euronews.com/business/2026/03/02/another-oil-tanker-hit-by-drone-boat-as-strait-of-hormuz-tensions-rise", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2875186)\nAn oil
tanker has been struck near the Strait of Hormuz, marking another attack in the area that triggered an explosion and left one crew member dead.\nAn oil tanker flying the flag of the Republic of the
Marshall Islands was attacked by a drone boat 52 nautical miles (96.3km) off the coast of Muscat, according to Oman\u2019s Maritime Security Centre (MSC).\nThe vessel, named MKD VYOM, was carrying
approximately 59,463 metric tonnes of cargo ", "api_data": null, "hint": null}, {"title": "After Strait of Hormuz opens, turmoil would still last months, analysts say | US-Israel war on Iran News | Al
Jazeera", "url": "https://www.aljazeera.com/news/2026/3/31/after-strait-of-hormuz-opens-turmoil-would-still-last-months-analysts-say", "snippet": "After Strait of Hormuz opens, turmoil would still
last months, analysts say\nEffective shutdown of key waterway could lead to permanent changes in how shipping industry does business.\n![Strait of Hormuz](/wp-
content/uploads/2026/03/AFP__20260225__98WG8TR__v5__MidRes__UaeMaritimeTransport-2-1773792612.jpg?resize=730%2C410&quality=80)\nAsian governments scramble to contain fuel costs amid Strait of Hormuz
crisis\nThe effective shutdown of the Strait of Hormuz has blocked the flow of a substantial por", "api_data": null, "hint": null}, {"title": "Iran Conflict and the Strait of Hormuz: Impacts on Oil,
Gas, and Other Commodities | Congress.gov | Library of Congress", "url": "https://www.congress.gov/crs-product/R45281", "snippet": null, "api_data": null, "hint": "Use search_exa for cached content,
or web_search for legislative information."}]}
```

```json
{
  "query": "Gulf of Oman tanker attack conflict 2026"
}
```

### 📋 Result

```
{"query": "Gulf of Oman tanker attack conflict 2026", "results": [{"title": "Tankers Struck Near Gulf as Hormuz Traffic All But Halted - Bloomberg", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "2026 Strait of Hormuz crisis -
Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing
geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei.
In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings
prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The
Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the
United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli
territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US
President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed
Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline
in maritime transit, with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This
disruption affected about 20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the
IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster
than during any other conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The
closure of the strait has been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity
markets to suffer price increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea
by denying transit in a strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Another oil tanker hit by drone boat as Strait of Hormuz tensions rise |
Euronews", "url": "https://www.euronews.com/business/2026/03/02/another-oil-tanker-hit-by-drone-boat-as-strait-of-hormuz-tensions-rise", "snippet": "[Comments](https://www.euronews.com#vuukle-
comments-2875186)\nAn oil tanker has been struck near the Strait of Hormuz, marking another attack in the area that triggered an explosion and left one crew member dead.\nAn oil tanker flying the flag
of the Republic of the Marshall Islands was attacked by a drone boat 52 nautical miles (96.3km) off the coast of Muscat, according to Oman\u2019s Maritime Security Centre (MSC).\nThe vessel, named MKD
VYOM, was carrying approximately 59,463 metric tonnes of cargo ", "api_data": null, "hint": null}, {"title": "Iran starts \u2018indiscriminate\u2019 strikes across Gulf of Oman, hits shadow tanker
tied to regime", "url": "https://www.foxnews.com/world/iran-starts-indiscriminate-strikes-gulf-oman-hits-shadow-tanker-tied-regime", "snippet": "[Oil tanker blazes near the coast of Oman in
'indiscriminate' attack](https://www.foxnews.com/video/6390283404112)\nShadow oil tanker with ties to Iranian regime attacked near Oman coast (Reuters)\nIran is conducting \"indiscriminate\" targeting
of vessels across the Gulf of Oman and the wider Persian Gulf following the launch of U.S.-Israeli strikes under Operation Epic Fury, according to a maritime intelligence firm.\n[Windward
AI](https://windward.ai/blog/march-2-iran-war-maritime-intelligence-dai", "api_data": null, "hint": null}, {"title": "Day 32 of Middle East conflict \u2014 Iran threatens US tech companies, Kuwaiti
oil tanker attacked | CNN", "url": "https://www.cnn.com/2026/03/31/world/live-news/iran-war-us-trump-oil", "snippet": "Our live coverage has ended\n\u2022 Get the latest updates on[ the war with Iran
here.](https://www.cnn.com/2026/04/01/world/live-news/iran-war-us-trump-oil)\nWhat we know so far\n\u2022 A new timeline: President Donald Trump will deliver an address to the nation on Wednesday
night regarding Iran. It comes after Trump said the US could be done with its war with Iran [within two to three weeks](https://www.cnn.com/2026/03/31/world/live-news/iran-war-us-trump-oil?post-
id=cmnf60zv200003b6qhbhserhd). Iran has in", "api_data": null, "hint": null}, {"title": "Strait of Hormuz Crisis Halts Tanker Traffic March 2026 - Maritime News", "url":
"https://www.maritimenews.com/iran-conflict-maritime-disruptions/iran-conflict-maritime-disruptions-hormuz", "snippet": "On March 1-3, 2026, maritime trade through the Strait of Hormuz experienced
unprecedented disruptions due to an ongoing crisis. Military strikes, Islamic Revolutionary Guard Corps warnings and insurance hurdles effectively stopped commercial tanker traffic - having an
enormously negative effect on global energy supply chains.\nStrikes against commercial tankers\nFour commercial tankers sustained strikes in the Strait of Hormuz and Gulf of Oman within 36 hours
following Operation Epic Fury. Confirm", "api_data": null, "hint": null}, {"title": "Iran War Confirmed Vessel Attacks and Maritime Infrastructure Strikes", "url": "https://windward.ai/blog/iran-war-
vessel-attacks-and-maritime-infrastructure-strikes/", "snippet": "[April 2, 2026: Iran War Maritime Intelligence Daily](https://windward.ai/blog/april-2-maritime-intelligence-daily/)\nNumber of
confirmed incidents: 32 (22 vessels and 10 oil, gas, and port facilities).\nSince the start of the Iran war, [maritime security](https://windward.ai/glossary/what-is-maritime-security/) incidents have
expanded across the commercial operating environment, affecting vessels at anchor, in transit, in drydock, and during [ship-to-ship operations](https://windward.ai/glossary/", "api_data": null,
"hint": null}, {"title": "2026-004-Persian Gulf, Strait of Hormuz, and Gulf of Oman-Iranian Attacks on Commercial Vessels | MARAD", "url": "https://www.maritime.dot.gov/msci/2026-004-persian-gulf-
strait-hormuz-and-gulf-oman-iranian-attacks-commercial-vessels", "snippet": null, "api_data": null, "hint": null}, {"title": "2026 Iranian strikes on Oman - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Iranian_strikes_on_Oman", "snippet": "From 1 March 2026, as part of the 2026 Iran War, Iran began launching a series of drone strikes on sites in Oman, initially
targeting the Port of Duqm and the Port of Salalah, which are used by the United States. The attacks also struck two oil tankers, one off the coast of Muscat and another about five kilometres north of
the Port of Khasab. A separate drone strike targeted an industrial zone in Sohar. The attacks killed fourteen people and injured sixteen others.", "api_data": {"content": [{"type": "text", "text":
"{\"title\": \"2026 Iranian strikes on Oman\", \"url\": \"https://en.wikipedia.org/wiki/2026_Iranian_strikes_on_Oman\", \"extract\": \"From 1 March 2026, as part of the 2026 Iran War, Iran began
launching a series of drone strikes on sites in Oman, initially targeting the Port of Duqm and the Port of Salalah, which are used by the United States. The attacks also struck two oil tankers, one
off the coast of Muscat and another about five kilometres north of the Port of Khasab. A separate drone strike targeted an industrial zone in Sohar. The attacks killed fourteen people and injured
sixteen others.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Drone attack on key port in Oman hits fuel tank: State media | Daily Sabah", "url":
"https://www.dailysabah.com/business/energy/drone-attack-on-key-port-in-oman-hits-fuel-tank-state-media", "snippet": "A fuel storage tank at Oman's Port of Duqm was struck in a drone attack, state
media said on Tuesday, as Iran presses its campaign against the Gulf in response to U.S. and Israeli strikes.\nSeveral tanks at the commercial port were targeted by multiple drones, but the damage was
contained and no casualties were reported, the local news agency said.\n\"A security source reported that fuel tanks at the commercial port of Duqm were targeted by a number of drones, one of which
hit a fuel tank. The resu", "api_data": null, "hint": null}]}
```

```json
{
  "query": "ITOPF major oil spill 2026"
}
```

### 📋 Result

```
{"query": "ITOPF major oil spill 2026", "results": [{"title": "Home - ITOPF", "url": "https://www.itopf.org/", "snippet": "ITOPF produces a wide range of publications and papers, a number of which are
available for downloading free of charge from our [Document & Guides](https://www.itopf.org/knowledge-resources/documents-guides/) section.\n[News](https://www.itopf.org/news/news/)\n- 02/02/2026
-\n[ITOPF engages with Seven Islands Shipping Ltd. in Dubai](https://www.itopf.org/news/news/itopf-engages-with-seven-islands-shipping-ltd-in-dubai/) - 23/01/2026 -\n[ITOPF publishes 2025 Oil tanker
spill statistics](https://www.i", "api_data": null, "hint": null}, {"title": "Oil Tanker Spill Statistics 2023 - ITOPF", "url": "https://www.itopf.org/knowledge-resources/data-statistics/statistics/",
"snippet": "Oil Tanker Spill Statistics 2025\nBackground\nITOPF maintains a database of oil spills from tank vessels, including combined carriers, FPSOs and barges. This contains information on
accidental spillages of persistent and non-persistent hydrocarbon oil since 1970, except those resulting from acts of war. The data held includes the location and cause of the incident, the vessel
involved, the type of oil spilled and the spill amount.\nSpills are categorised by size, <7 tonnes or <50 bbls (small), 7-70", "api_data": null, "hint": null}, {"title": "Oil Tanker Spill Statistics
2025 - ITOPF", "url": "https://www.itopf.org/knowledge-resources/data-statistics/oil-tanker-spill-statistics-2025/", "snippet": "Oil Tanker Spill Statistics 2025\nBackground\nITOPF maintains a
database of oil spills from tank vessels, including combined carriers, FPSOs and barges. This contains information on accidental spillages of persistent and non-persistent hydrocarbon oil since 1970,
except those resulting from acts of war. The data held includes the location and cause of the incident, the vessel involved, the type of oil spilled and the spill amount.\nSpills are categorised by
size, <7 tonnes or <50 bbls (small), 7-70", "api_data": null, "hint": null}, {"title": "ITOPF publishes 2025 Oil tanker spill statistics", "url": "https://www.itopf.org/news/news/itopf-
publishes-2025-oil-tanker-spill-statistics", "snippet": "ITOPF publishes 2025 Oil tanker spill statistics\n23 January 2026\n![A graph showing the decline in oil tanker spills since the 1970s to
present](/fileadmin/_processed_/c/6/csm_Fig2_-_Oil_tanker_stats_2025_2f61e43d17.jpg)\nThree large spills of more than 700 tonnes and three medium spills, between 7-700 tonnes, were recorded from
tanker incidents in the year 2025.\nThis brings the current decade average to seven tanker spills per year, a dramatic reduction from the numbers reported from earlier deca", "api_data": null, "hint":
null}, {"title": "Global annual average quantity of oil spilled from tankers per decade - Our World in Data", "url": "https://ourworldindata.org/grapher/quantity-oil-spills-decadal-average",
"snippet": "Global annual average quantity of oil spilled from tankers per decade\n![](/grapher/quantity-oil-spills-decadal-average.png)\nWhat you should know about this indicator\n- Decadal average
quantity of oil lost to the environment from tanker spills.\n- Includes oil that was burned, remained in sunken vessels, or otherwise unrecovered.\n[with minor
processing](https://ourworldindata.org#sources-and-processing)by Our World in Data\nMore Data on Oil Spills\nSources and processing\nThis data is based on the fo", "api_data": null, "hint": null},
{"title": "Global quantity of oil spilled from tankers - Our World in Data", "url": "https://ourworldindata.org/grapher/quantity-oil-spills", "snippet": "Global quantity of oil spilled from
tankers\n![](/grapher/quantity-oil-spills.png)\nWhat you should know about this indicator\n- Total volume of oil lost to the environment from tanker spills.\n- Includes oil that was burned, remained
in sunken vessels, or otherwise unrecovered.\n- Annual figures can vary significantly due to the occurrence of large spills.\n[with minor processing](https://ourworldindata.org#sources-and-
processing)by Our World in Data\nMore Data on Oil Spills\nSources and processing\nThi", "api_data": null, "hint": null}, {"title": "Data & Statistics - ITOPF", "url": "https://www.itopf.org/knowledge-
resources/data-statistics/", "snippet": "Data & Statistics\nWe maintain a worldwide database of accidental oil spills from tankers, combined carriers and barges. This is used to generate statistics on
numbers and sizes of spill, and to identify the causes of spills.\nLong-term trends are analysed, which has proved useful for assessing the risk of oil spills for contingency planning, and for
evaluating the possible consequences of changes in tanker design and operations.\nUsing our geographical information system, GIS, spills are displayed", "api_data": null, "hint": null}, {"title":
"ITOPF Handbook 2025 just published - ITOPF", "url": "https://www.itopf.org/news/news/itopf-handbook-2025-just-published/", "snippet": "ITOPF Handbook 2025 just published\n6 August 2025\n![ITOPF
Handbook 2025](/fileadmin/_processed_/d/9/csm_Handbook25_8c3e8d550f.png)\nITOPF has just published its annual Handbook for 2025/26. This contains a wealth of valuable information and guidance for
those likely to be involved in spills of oil, chemicals or other cargo from ships.\nThis year's edition includes an expanded section on plastic pellets, a new section on ESG at ITOPF, updated tanker
spill statistics and staff information, as well as", "api_data": null, "hint": null}, {"title": "Oil Tanker Spill Statistics - ITOPF", "url": "https://www.itopf.org/knowledge-resources/documents-
guides/oil-tanker-spill-statistics", "snippet": "Oil Tanker Spill Statistics\n30 January 2025\n![Oil tanker spill statistics
2024](/fileadmin/_processed_/f/f/csm_Oil_Spill_Stats_2024_front_cover_ee84ac209c.jpg)\nAn annual publication providing data on accidental oil spills from tankers, combined carriers and barges since
1970, derived from ITOPF's database. Published each January.\nSingle copies are available free of charge - contact the [Office & Administration Team. ](mailto:office@itopf.org)\nCategories:
[Information Services](https://www.itopf.", "api_data": null, "hint": null}, {"title": "IOPC FUNDS | Events", "url": "https://iopcfunds.org/news-events/events/", "snippet": "IOPC Funds participates in
Adriaspillcon 2026\nThe IOPC Funds will participate in the 6th edition of ADRIASPILLCON 2026, an international conference and exhibition focused on oil spill prevention, preparedness, and
response.\nThe event will take place from 21 to 23 April 2026 in Zadar, Croatia. It is being organised by the Adriatic Training and Research Centre (ATRAC), under the auspices of the Ministry of
Maritime Affairs, Transport, and Infrastructure of the Republic of Croatia, and is supported", "api_data": null, "hint": null}]}
```

## 💬 Response

This is a very active conflict zone. Let me get more specific details about tanker attacks in the Gulf of Oman and whether any resulted in a spill exceeding 50,000 barrels.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "\"Gulf of Oman\" oil spill barrels tanker sunk cargo leaked 2026"
}
```

### 📋 Result

```
{"query": "\"Gulf of Oman\" oil spill barrels tanker sunk cargo leaked 2026", "results": [{"title": "How oil tankers stuck in the Strait of Hormuz south of Iran threatens the Gulf ecosystem -
Greenpeace International", "url": "https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/", "snippet": "More than 85 large oil tankers are [currently trapped in the Persian
Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-gulf/). The reason: following attacks launched on Iran by Israel and the United States on
28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and disrupted vessel position signals dramatically [increase the risk of oil
spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}, {"title": "First oil tanker attacked in the Strait of Hormuz according to Oman | Euronews", "url":
"https://www.euronews.com/business/2026/03/01/first-oil-tanker-attacked-in-the-strait-of-hormuz-according-to-oman", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2874940)\nAn oil
tanker was attacked off the coast of Musandam in the Strait of Hormuz. Four people were injured and all 20 crew members were evacuated, according to Oman's Maritime Security Centre.\nThe first attack
against a ship in the Strait of Hormuz occurred on Sunday morning.\nOman's Maritime Security Centre announced that an oil tanker named Skylight, flying the flag of the Republic of Palau, was targeted
around five nautical miles (9.26km", "api_data": null, "hint": null}, {"title": "Gulf of Oman oil spill: Greenpeace warns of environmental disaster - Greenpeace International", "url":
"https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-spill-environmental-disaster/", "snippet": "Beirut, Lebanon \u2013 Greenpeace Middle East and North Africa (MENA) has
warned of a potential environmental disaster after two crude oil tankers collided between Iran and the United Arab Emirates on Tuesday.\nSatellite
[imagery](https://media.greenpeace.org/Detail/27MZIFJRBAFKQ) indicates a large plume of oil stretching up to around 1500 hectares from the site of the crash between two vessels, \u2018Adalynn\u2019
and \u2018Front Eagle\u2019, in the Gulf of Oman, approximately 22 nautical miles east of Khor Fakkan, near", "api_data": null, "hint": null}, {"title": "Which oil and gas facilities in the Gulf have
been attacked? | Infographic News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/3/4/which-oil-and-gas-facilities-in-the-gulf-have-been-attacked", "snippet": "Which oil and gas facilities
in the Gulf have been attacked?\nDamage to several energy facilities has caused global prices to spike, but Iran denies it is targeting energy sites.\n![INTERACTIVE_IRAN_GCC_OIL AND GAS SUPPLY-OUTSIDE
IMAGE](/wp-content/uploads/2026/03/INTERACTIVE_IRAN_GCC_OIL-AND-GAS-SUPPLY-06-1772630810.png?resize=770%2C513&quality=80)\nGlobal energy markets remain in a state of high alert after several Gulf
states suspended oil and gas production following escalating tensions in the ", "api_data": null, "hint": null}, {"title": "2026 Strait of Hormuz crisis - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic
disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran
launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a
major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and
Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf
states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump
announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military
campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit,
with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about
20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the
strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other
conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has
been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price
increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a
strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Oil spill gets detected following tanker collision in Gulf of Oman - SAFETY4SEA", "url":
"https://safety4sea.com/oil-spill-gets-detected-following-tanker-collision-in-gulf-of-oman/", "snippet": "Greenpeace Middle East and North Africa (MENA) has warned of a potential environmental
disaster [after two crude oil tankers, Adalynn and Front Eagle,](https://safety4sea.com/tanker-collision-in-gulf-of-oman-unrelated-to-israel-iran-conflict/) collided in the Gulf of Oman near the
Strait of Hormuz.\nAccording to Greenpeace, satellite imagery indicates a large plume of oil stretching up to around 1500 hectares from the site of the crash between two vessels, Adalynn and Front
Eagle in the Gulf of O", "api_data": null, "hint": null}, {"title": "Oil spill threat grows after tanker collision in Gulf of Oman - Port Technology International", "url":
"https://www.porttechnology.org/news/oil-spill-threat-grows-after-tanker-collision-in-gulf-of-oman/", "snippet": null, "api_data": null, "hint": null}, {"title": "More than 68 stranded oil tankers
increase the risk of oil spills in the Strait of Hormuz", "url": "https://www.ecoticias.com/en/more-than-68-stranded-oil-tankers-increase-the-risk-of-oil-spills-in-the-strait-of-hormuz/29182/",
"snippet": "More than 68 loaded oil tankers are sitting nearly motionless near the [Strait of Hormuz](https://www.eia.gov/international/analysis/special-topics/World_Oil_Transit_Chokepoints), carrying
at least 16 billion liters of crude oil. That is roughly three months of oil consumption for Spain, all concentrated in one of the narrowest and most sensitive sea lanes on Earth.\nAn [investigation
by Greenpeace](https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/) warns that this", "api_data": null, "hint": null}, {"title": "Oil tanker collision and fire in Gulf of
Oman caused by 'navigational misjudgment' | The National", "url": "https://www.thenationalnews.com/news/uae/2025/06/17/uae-coast-guard-rescues-24-crew-members-after-oil-tanker-collision-in-sea-of-
oman/", "snippet": "The probable cause of a collision between an oil tanker and another vessel in the Gulf of [Oman](https://www.thenationalnews.com/tags/oman) on Tuesday was \u201cnavigational
misjudgment\u201d, the [UAE](https://www.thenationalnews.com/uae/)'s Ministry of Energy and Infrastructure has said.\nThe ministry said on Wednesday that early findings suggest \u201cthat the incident
was caused by a navigational misjudgment by one of the vessels\u201d, state news agency Wam reported.\nThe UAE Coast Guard evacuated 24 crew member", "api_data": null, "hint": null}, {"title": "Russia
uses shadow fleet for $29M oil transfer operation in Gulf of Oman | Fox News", "url": "https://www.foxnews.com/world/putin-caught-executing-enormous-semi-dark-ship-to-ship-oil-transfer-gulf-oman",
"snippet": "[Trump warns Iran against disrupting global oil supply](https://www.foxnews.com/video/6390687510112)\nAlex Gray and Erin Maguire give their take on the president's warning to Iran, their
reaction to Stephen A. Smith throwing his support behind Marco Rubio in 2028 and more.\nRussia has turned to its so-called \"shadow fleet\" to carry out a roughly $29.3 million \"semi-dark\" ship-to-
ship oil transfer in the Gulf of Oman, deliberately sidestepping Western sanctions, according to reports.\nMaritime intel", "api_data": null, "hint": null}]}
```

```json
{
  "query": "tanker attack Gulf of Oman oil leak spill size March April 2026"
}
```

### 📋 Result

```
{"query": "tanker attack Gulf of Oman oil leak spill size March April 2026", "results": [{"title": "First oil tanker attacked in the Strait of Hormuz according to Oman | Euronews", "url":
"https://www.euronews.com/business/2026/03/01/first-oil-tanker-attacked-in-the-strait-of-hormuz-according-to-oman", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2874940)\nAn oil
tanker was attacked off the coast of Musandam in the Strait of Hormuz. Four people were injured and all 20 crew members were evacuated, according to Oman's Maritime Security Centre.\nThe first attack
against a ship in the Strait of Hormuz occurred on Sunday morning.\nOman's Maritime Security Centre announced that an oil tanker named Skylight, flying the flag of the Republic of Palau, was targeted
around five nautical miles (9.26km", "api_data": null, "hint": null}, {"title": "How oil tankers stuck in the Strait of Hormuz south of Iran threatens the Gulf ecosystem - Greenpeace International",
"url": "https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/", "snippet": "More than 85 large oil tankers are [currently trapped in the Persian
Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-gulf/). The reason: following attacks launched on Iran by Israel and the United States on
28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and disrupted vessel position signals dramatically [increase the risk of oil
spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}, {"title": "Oman Says Oil Tanker Targeted Off Its North Coast", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "Oil Tanker Attacked Near Oman
Coast: One Crew Member Killed in Maritime Incident", "url": "https://gulfnews.com/world/gulf/oman/oil-tanker-attacked-off-oman-coast-one-crew-member-killed-1.500460744", "snippet": "Omani Maritime
Security Centre responds as one Indian national dies in explosion\nDubai/Oman: An oil tanker flying the flag of the Republic of the Marshall Islands was attacked by an unmanned boat about 52 nautical
miles off the coast of Muscat, leaving one crew member dead, the Omani Maritime Security Centre said.\nThe attack comes amid an already tense regional situation involving Iran, the United States, and
Israel, with GCC countries also directly affected.\nThe tanker, MKD VYOM, was carrying a", "api_data": null, "hint": null}, {"title": "Iran War Confirmed Vessel Attacks and Maritime Infrastructure
Strikes", "url": "https://windward.ai/blog/iran-war-vessel-attacks-and-maritime-infrastructure-strikes/", "snippet": "[April 2, 2026: Iran War Maritime Intelligence
Daily](https://windward.ai/blog/april-2-maritime-intelligence-daily/)\nNumber of confirmed incidents: 32 (22 vessels and 10 oil, gas, and port facilities).\nSince the start of the Iran war, [maritime
security](https://windward.ai/glossary/what-is-maritime-security/) incidents have expanded across the commercial operating environment, affecting vessels at anchor, in transit, in drydock, and during
[ship-to-ship operations](https://windward.ai/glossary/", "api_data": null, "hint": null}, {"title": "2026 Strait of Hormuz crisis - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic
disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran
launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a
major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and
Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf
states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump
announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military
campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit,
with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about
20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the
strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other
conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has
been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price
increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a
strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Strait of Hormuz Global Oil, Gas Trade Disrupted Amid Iran War", "url":
"https://time.com/7382242/strait-of-hormuz-closure-threat-iran-war-trade-gas-oil-prices/", "snippet": "Global oil and gas prices have surged as the [Iran war](https://time.com/7381950/iran-war-
khamenei-strikes-tehran/) has brought the crucial Strait of Hormuz, a narrow passage between the Persian Gulf and the Gulf of Oman through which around a fifth of global oil production flows, to a
halt.\nAs of Tuesday, Brent crude oil prices [have risen](https://tradingeconomics.com/commodity/brent-crude-oil) by around 7%, reaching as high as $83 per barrel. When markets closed on Friday, ahead
of the Iran w", "api_data": null, "hint": null}, {"title": "Oil Tanker Explosions in Gulf of Oman: Everything We Know About Blasts, Fires As U.S. Navy Races to Assist - Newsweek", "url":
"https://www.newsweek.com/oil-tankers-explosions-attacks-gulf-oman-fire-us-navy-5th-fleet-1443738", "snippet": "Two oil tankers are reportedly ablaze on the Gulf of Oman after being hit by explosions,
according to Iranian media reports.\nThe incident, details of which are still emerging, has prompted an uptick in crude oil prices. The cause is not yet clear, but reports suggest a similarity with
attacks on four oil tankers off the coast of the United Arab Emirates last month, which was blamed on Iran.\nAccording to [Press TV](https://www.presstv.com/Detail/2019/06/13/598390/Oil-tankers-Sea-
of-Oman), the Ira", "api_data": null, "hint": null}, {"title": "Which oil and gas facilities in the Gulf have been attacked? | Infographic News | Al Jazeera", "url":
"https://www.aljazeera.com/news/2026/3/4/which-oil-and-gas-facilities-in-the-gulf-have-been-attacked", "snippet": "Which oil and gas facilities in the Gulf have been attacked?\nDamage to several
energy facilities has caused global prices to spike, but Iran denies it is targeting energy sites.\n![INTERACTIVE_IRAN_GCC_OIL AND GAS SUPPLY-OUTSIDE IMAGE](/wp-
content/uploads/2026/03/INTERACTIVE_IRAN_GCC_OIL-AND-GAS-SUPPLY-06-1772630810.png?resize=770%2C513&quality=80)\nGlobal energy markets remain in a state of high alert after several Gulf states
suspended oil and gas production following escalating tensions in the ", "api_data": null, "hint": null}, {"title": "Day 31 of Middle East conflict \u2013 Iran says US proposal
\u2018unrealistic,\u2019 Trump threatens to \u2018take the oil in Iran\u2019 | CNN", "url": "https://www.cnn.com/2026/03/30/world/live-news/iran-war-us-israel-trump", "snippet": "Our live coverage has
ended\nWhat we covered\n\u2022 Tanker full of oil struck: A fully loaded [Kuwaiti tanker in Dubai](https://www.cnn.com/2026/03/30/world/live-news/iran-war-us-israel-trump?post-
id=cmndslorj0002356tjlgjs5og) waters was hit by a drone attack, triggering fears of an oil spill, as Trump again threatened to blow up Iran\u2019s energy sources if the Hormuz Strait isn\u2019t
reopened fully. Meanwhile, least two people were killed [in a US-Israeli strike on an orphanage in Iran](https://www.cnn.com/", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis",
  "prompt": "Extract all details about attacks on oil tankers, especially in the Gulf of Oman. How many tankers were attacked? Were any sunk? How much oil was spilled? Were any spills larger than 50,000 barrels or 6,800 tonnes? List every confirmed vessel attack with details about cargo, damage, and any oil spill that resulted."
}
```

### 📋 Result

```
{"title": "2026 Strait of Hormuz crisis", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "extract": "The Strait of Hormuz, a major maritime choke point for global energy trade,
has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's
supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps
(IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump announced his intent to seize control of the Strait of
Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military campaign to open the strait.\nAs of 12 March 2026, Iran
has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit, with tanker traffic dropping first by approximately 70% and
over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about 20% of the world's daily oil supply and significant volumes of
liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the strait is closed to any vessel going \"to and from\" the ports
of the US, Israel, and their allies.\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other conflict in recent history; Brent crude oil prices surpassed US$100 per
barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has been described as the largest disruption to the energy supply since the
1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price increases from the crisis include aluminum, fertilizer, and helium.\nIran's
closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a strait used for international navigation.\n\n", "mode": "full"}
```

## 💭 Thinking

Let me dig deeper into the specific tanker attacks and oil spill details. I need to find out:
1. Whether any specific attack in the Gulf of Oman resulted in a spill >50,000 barrels
2. The Adalynn/Front Eagle collision details - was it conflict-related? How large was the spill?
3. The MKD VYOM attack details
4. Other tanker attacks and their spillage

Key findings so far:
- Major Iran-US/Israel conflict since Feb 28, 2026
- 32+ confirmed maritime incidents (22 vessels, 10 facilities)


- Multiple tanker attacks in/near Gulf of Oman with the Adalynn/Front Eagle collision showing a detected oil spill of 1500 hectares, though I'm still trying to confirm if it was conflict-related
- 85+ tankers trapped in Persian Gulf with traffic effectively halted

Now I need to search for more specific information about whether the Adalynn/Front Eagle collision meets the criteria: a single spill exceeding 50,000 barrels, confirmed as conflict-related, occurring in the Gulf of Oman specifically, and reported by a credible source before May 1, 2026.

## 💬 Response

Let me get more details on the specific tanker incidents and spill sizes.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-spill-environmental-disaster/",
  "prompt": "What was the size of the oil spill from the Adalynn and Front Eagle collision? How many barrels or tonnes? Was it conflict-related? When did it happen? Where exactly in the Gulf of Oman?"
}
```

### 📋 Result

```
{"url": "https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-spill-environmental-disaster/", "content": "Based on the content provided:\n\n**Size of oil spill:** \n-
Satellite imagery showed a large plume stretching up to approximately **1,500 hectares** from the crash site\n- The Adalynn was estimated to be carrying approximately **70,000 tons of crude oil**
based on its draught, though this is the vessel's cargo capacity, not the confirmed amount spilled\n- The exact volume spilled is not specified in the article\n\n**Conflict-related:** \nNot directly
stated as conflict-related. However, the Adalynn is noted as part of the Russian \"shadow fleet\" - vessels that operate below basic security standards and carry Russian oil.\n\n**When:**
\n**Tuesday** (specific date not provided in the article, but the press release is from Beirut, Lebanon)\n\n**Where:** \n- Gulf of Oman\n- Approximately **22 nautical miles east of Khor Fakkan**\n-
Near the **Strait of Hormuz**\n- Between Iran and the United Arab Emirates\n\n**Relevant links:**\n- [Satellite imagery of the oil spill](https://media.greenpeace.org/Detail/27MZIFJRBAFKQ)\n-
[Greenpeace shadow fleet report (PDF)](https://www.greenpeace.org/static/planet4-sweden-stateless/2024/10/fb3d5709-greenpeace-shadow-fleet-baltic-tankers-list.pdf)", "title": "Gulf of Oman oil spill:
Greenpeace warns of environmental disaster - Greenpeace International"}
```

```json
{
  "url": "https://safety4sea.com/oil-spill-gets-detected-following-tanker-collision-in-gulf-of-oman/",
  "prompt": "Details of the oil spill from the tanker collision in the Gulf of Oman. How large was the spill in barrels or tonnes? Was it conflict-related?"
}
```

### 📋 Result

```
{"url": "https://safety4sea.com/oil-spill-gets-detected-following-tanker-collision-in-gulf-of-oman/", "content": "Based on the provided content:\n\n**Spill Details:**\n- Satellite imagery shows an oil
plume stretching approximately **1,500 hectares** from the collision site\n- The Adalynn may be carrying approximately **70,000 tons of crude oil** based on its draught analysis, though the exact
amount spilled is not specified in the article\n- The collision occurred approximately 22 nautical miles east of Khor Fakkan, near the Strait of Hormuz\n\n**Conflict-Related:**\nNo, the collision was
**not conflict-related** according to the content (the linked article specifically notes it was \"unrelated to Israel-Iran conflict\")\n\n**Note:** The article does not provide a precise measurement
of the actual spill volume in barrels or tonnes - only the size of the visible plume (1,500 hectares) and the estimated cargo capacity of the Adalynn (70,000 tons).\n\n**Relevant links:**\n- [Tanker
collision in Gulf of Oman unrelated to Israel-Iran conflict](https://safety4sea.com/tanker-collision-in-gulf-of-oman-unrelated-to-israel-iran-conflict/)", "title": "Oil spill gets detected following
tanker collision in Gulf of Oman"}
```

```json
{
  "query": "Adalynn Front Eagle tanker collision Gulf of Oman oil spill size barrels tonnes"
}
```

### 📋 Result

```
{"query": "Adalynn Front Eagle tanker collision Gulf of Oman oil spill size barrels tonnes", "results": [{"title": "Oil spill detected from Tuesday\u2019s tanker collision in the Gulf of Oman -
Splash247", "url": "https://splash247.com/oil-spill-detected-from-tuesdays-tanker-collision-in-the-gulf-of-oman/", "snippet":
"[Environment](https://splash247.com/category/sector/environment/)\n[Middle East](https://splash247.com/category/region/middle-east/)\n[Tankers](https://splash247.com/category/sector/tankers/)\nOil
spill detected from Tuesday\u2019s tanker collision in the Gulf of Oman\n![](https://splash247.com/wp-content/uploads/2025/06/X.com-Avalynn-fire-780x470.jpg)\nAn oil spill is growing rapidly in the
Gulf of Oman after Tuesday\u2019s spectacular collision between a Frontline VLCC and a suezmax belonging to Russia\u2019s sha", "api_data": null, "hint": null}, {"title": "Oil spill gets detected
following tanker collision in Gulf of Oman - SAFETY4SEA", "url": "https://safety4sea.com/oil-spill-gets-detected-following-tanker-collision-in-gulf-of-oman/", "snippet": "Greenpeace Middle East and
North Africa (MENA) has warned of a potential environmental disaster [after two crude oil tankers, Adalynn and Front Eagle,](https://safety4sea.com/tanker-collision-in-gulf-of-oman-unrelated-to-
israel-iran-conflict/) collided in the Gulf of Oman near the Strait of Hormuz.\nAccording to Greenpeace, satellite imagery indicates a large plume of oil stretching up to around 1500 hectares from the
site of the crash between two vessels, Adalynn and Front Eagle in the Gulf of O", "api_data": null, "hint": null}, {"title": "NEXTA on X: \"\ud83d\udca5\ud83d\udca5Oil Tanker Adalynn Engulfed in
Flames After Collision A massive oil tanker, Adalynn, caught fire after colliding with the Front Eagle in the Gulf of Oman \u2014 right next to the world's busiest oil artery. The Front Eagle was
transporting 2 million barrels of Iraqi crude to https://t.co/HHy8kXeEqP\" / X", "url": "https://x.com/nexta_tv/status/1934980020008620155", "snippet": "We\u2019ve detected that JavaScript is disabled
in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy
Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "Mid-East tanker collision was an accident, says UAE - Shipping Australia", "url":
"https://www.shippingaustralia.com.au/mid-east-tanker-collision-was-an-accident-says-uae/", "snippet": "A collision between two tankers that led to an oil spill and a raging shipboard fire in the Gulf
of Oman (to the south of Iran), was an accident, according to an official statement both from the United Arab Emirates, and also from the UK Maritime Trade Operations (part of the UK Royal
Navy).\nInitial reporting raised speculative concerns that ships could have been hit (accidentally or otherwise) as part of the Israel-Iran war; however, it now appears that such concerns were
unfounded.\n\u201cThere is n", "api_data": null, "hint": null}, {"title": "Laden Frontline VLCC collides with shadow suezmax tanker off Khorfakkan - Splash247", "url": "https://splash247.com/laden-
frontline-vlcc-collides-with-shadow-aframax-tanker-off-khorfakkan/", "snippet": "[Middle East](https://splash247.com/category/region/middle-
east/)\n[Operations](https://splash247.com/category/sector/operations/)\n[Tankers](https://splash247.com/category/sector/tankers/)\nLaden Frontline VLCC collides with shadow suezmax tanker off
Khorfakkan\n![](https://splash247.com/wp-content/uploads/2025/06/X.com-Avalynn-fire-780x470.jpg)\nA collision occurred at 1:14 am Dubai time overnight between two tankers, the Antigua Barbuda-flagged
Adalynn suezmax, part of the shadow fleet, and the Li", "api_data": null, "hint": null}, {"title": "Oil Slick in Gulf of Oman Near Shadow Tanker as Greenpeace Calls for Action", "url":
"https://maritime-executive.com/article/oil-slick-in-gulf-of-oman-near-shadow-tanker-as-greenpeace-calls-for-action", "snippet": "Oil Slick in Gulf of Oman Near Shadow Tanker as Greenpeace Calls for
Action\n![oil slick](https://maritime-executive.com/media/images/article/Photos/Oil_Gas_Energy/Greenpeace-oil-slick-Gulf-of-Oman.fa31bb.jpg)\nAn analysis of satellite images from the Gulf of Oman
shows a potential oil slick forming in the hours after the tanker Front Eagle and the shadow fleet tanker Adalynn collided about 24 nautical miles off the coast of the UAE. Environmental activists
from the Middle East and North Africa se", "api_data": null, "hint": null}, {"title": "Oil tanker collision and fire in Gulf of Oman caused by 'navigational misjudgment' | The National", "url":
"https://www.thenationalnews.com/news/uae/2025/06/17/uae-coast-guard-rescues-24-crew-members-after-oil-tanker-collision-in-sea-of-oman/", "snippet": "The probable cause of a collision between an oil
tanker and another vessel in the Gulf of [Oman](https://www.thenationalnews.com/tags/oman) on Tuesday was \u201cnavigational misjudgment\u201d, the [UAE](https://www.thenationalnews.com/uae/)'s
Ministry of Energy and Infrastructure has said.\nThe ministry said on Wednesday that early findings suggest \u201cthat the incident was caused by a navigational misjudgment by one of the
vessels\u201d, state news agency Wam reported.\nThe UAE Coast Guard evacuated 24 crew member", "api_data": null, "hint": null}, {"title": "Oil spill threat grows after tanker collision in Gulf of Oman
- Port Technology International", "url": "https://www.porttechnology.org/news/oil-spill-threat-grows-after-tanker-collision-in-gulf-of-oman/", "snippet": null, "api_data": null, "hint": null},
{"title": "Russian shadow tanker involved in potentially \u2018catastrophic\u2019 collision in Gulf of Oman", "url": "https://novayagazeta.eu/amp/articles/2025/06/19/russian-shadow-tanker-involved-in-
potentially-catastrophic-collision-in-gulf-of-oman-en-news", "snippet": "Greenpeace has [warned](https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-spill-environmental-
disaster/) of a potential regional \u201cenvironmental disaster\u201d after two oil tankers, one of which belongs to the Russian shadow fleet, collided in the Gulf of Oman on Tuesday, leading to an
oil spill.\nThe collision between oil tankers Adalynn and Front Eagle, which occurred off the coasts of the UAE and Iran near midnight on Tuesday, caused a fire to break out on the 23-year-ol",
"api_data": null, "hint": null}, {"title": "Fact Check: Video Does NOT Show American Oil Tanker Struck By Iran, Burning In Strait Of Hormuz", "url": "https://www.yahoo.com/news/articles/fact-check-
video-does-not-004429014.html", "snippet": "Fact Check: Video Does NOT Show American Oil Tanker Struck By Iran, Burning In Strait Of Hormuz\n- Video circulating online claiming American oil tanker
struck by Iran actually shows aftermath of collision between two oil tankers in Gulf of Oman in 2025.\nDoes a video show an American oil tanker struck by Iran and burning in the Strait of Hormuz? No,
that's not true: The video shows the aftermath of a collision between two oil tankers, neither owned by the United States, in the Gulf of Oman, east ", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Key finding: The Adalynn/Front Eagle collision happened in June 2025, not during the 2026 conflict. It was NOT conflict-related - it was a navigational accident. So this doesn't qualify.

Now let me focus on the actual conflict-related attacks on tankers. From the data:
- 32 confirmed incidents (22 vessels, 10 facilities) as of April 2, 2026
- Multiple tanker attacks in the Gulf of Oman/Strait of Hormuz area
- The MKD VYOM was carrying ~59,463 metric tonnes of cargo and was attacked by drone boat


- Iran appears to be conducting indiscriminate targeting of vessels across the Gulf of Oman

I need to find whether any of these conflict-related tanker attacks actually resulted in spills exceeding 50,000 barrels in the Gulf of Oman specifically.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"oil spill\" tanker sinking \"Gulf of Oman\" 2026 environmental damage barrels"
}
```

### 📋 Result

```
{"query": "\"oil spill\" tanker sinking \"Gulf of Oman\" 2026 environmental damage barrels", "results": [{"title": "2026 Strait of Hormuz crisis - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic
disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran
launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a
major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and
Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf
states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump
announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military
campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit,
with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about
20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the
strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other
conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has
been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price
increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a
strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Another oil tanker hit by drone boat as Strait of Hormuz tensions rise | Euronews", "url":
"https://www.euronews.com/business/2026/03/02/another-oil-tanker-hit-by-drone-boat-as-strait-of-hormuz-tensions-rise", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2875186)\nAn oil
tanker has been struck near the Strait of Hormuz, marking another attack in the area that triggered an explosion and left one crew member dead.\nAn oil tanker flying the flag of the Republic of the
Marshall Islands was attacked by a drone boat 52 nautical miles (96.3km) off the coast of Muscat, according to Oman\u2019s Maritime Security Centre (MSC).\nThe vessel, named MKD VYOM, was carrying
approximately 59,463 metric tonnes of cargo ", "api_data": null, "hint": null}, {"title": "Oman Says Oil Tanker Targeted Off Its North Coast", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "Hormuz Crisis: How Shadow Tankers
Defy Global Sanctions - QuantoSei News", "url": "https://news.quantosei.com/2026/03/11/why-shadow-tankers-are-the-only-ships-still-moving-through-the-strait-of-hormuz/", "snippet": "The Strait of
Hormuz, a narrow yet profoundly vital maritime artery, has been thrust into the heart of a global crisis. Since February 28, 2026, a simmering conflict involving the United States, Israel, and Iran
has brought mainstream oil tanker traffic to a near standstill. An astonishing 90% of legitimate shipping through this crucial choke point has vanished. Yet, even as hundreds of vessels remain
trapped, one clandestine segment of the shipping world thrives: the Strait of Hormuz shadow fle", "api_data": null, "hint": null}, {"title": "Tanker \u2018Skylight\u2019 struck as Strait of Hormuz
shipping threat intensifies amid fresh regional strikes | CNN", "url": "https://www.cnn.com/2026/03/02/world/video/tanker-skylight-struck-hormuz-oman-hnk-digvid", "snippet":
"![16x9_LOOP.00_00_06_18.Still005.jpg](https://media.cnn.com/api/v1/images/stellar/prod/16x9-loop-00-00-06-18-still005.jpg?c=16x9&q=w_1280,c_fill)\nVideo Ad Feedback\nTanker \u2018Skylight\u2019
struck as Strait of Hormuz shipping threat intensifies amid fresh regional strikes\nThe vital waterway faces mounting disruption after German shipping giant Hapag\u2011Lloyd halts transits, an oil
tanker \u201cSkylight\u201d was attacked off Oman, and Iran reports a vessel sinking following an \u201cunauthorized passage.\u201d Maritime author", "api_data": null, "hint": null}, {"title": "Gulf
of Oman oil spill: Greenpeace warns of environmental disaster - Greenpeace International", "url": "https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-spill-environmental-
disaster/", "snippet": "Beirut, Lebanon \u2013 Greenpeace Middle East and North Africa (MENA) has warned of a potential environmental disaster after two crude oil tankers collided between Iran and the
United Arab Emirates on Tuesday.\nSatellite [imagery](https://media.greenpeace.org/Detail/27MZIFJRBAFKQ) indicates a large plume of oil stretching up to around 1500 hectares from the site of the crash
between two vessels, \u2018Adalynn\u2019 and \u2018Front Eagle\u2019, in the Gulf of Oman, approximately 22 nautical miles east of Khor Fakkan, near", "api_data": null, "hint": null}, {"title": "How
oil tankers stuck in the Strait of Hormuz south of Iran threatens the Gulf ecosystem - Greenpeace International", "url": "https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-
iran/", "snippet": "More than 85 large oil tankers are [currently trapped in the Persian Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-
gulf/). The reason: following attacks launched on Iran by Israel and the United States on 28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and
disrupted vessel position signals dramatically [increase the risk of oil spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}, {"title": "Ships avoid the Strait of
Hormuz, tanker hit off Oman", "url": "https://www.seatrade-maritime.com/security/ships-avoid-the-strait-of-hormuz-tanker-hit-off-oman", "snippet": null, "api_data": null, "hint": null}, {"title":
"Strait of Hormuz Global Oil, Gas Trade Disrupted Amid Iran War", "url": "https://time.com/7382242/strait-of-hormuz-closure-threat-iran-war-trade-gas-oil-prices/", "snippet": "Global oil and gas
prices have surged as the [Iran war](https://time.com/7381950/iran-war-khamenei-strikes-tehran/) has brought the crucial Strait of Hormuz, a narrow passage between the Persian Gulf and the Gulf of
Oman through which around a fifth of global oil production flows, to a halt.\nAs of Tuesday, Brent crude oil prices [have risen](https://tradingeconomics.com/commodity/brent-crude-oil) by around 7%,
reaching as high as $83 per barrel. When markets closed on Friday, ahead of the Iran w", "api_data": null, "hint": null}, {"title": "Oman Evacuates Oil Port as Ships Hit in Gulf", "url":
"https://www.rigzone.com/news/wire/oman_evacuates_oil_port_as_ships_hit_in_gulf-12-mar-2026-183189-article/", "snippet": "Oman Evacuates Oil Port as Ships Hit in Gulf\n![Oman Evacuates Oil Port as
Ships Hit in Gulf](https://images.rigzone.com/images/news/articles/Oman-Evacuates-Oil-Port-as-Ships-Hit-in-Gulf-183189-582x327.webp)\nTwo crude tankers were hit in Iraqi waters and Oman's key oil
export terminal was evacuated, as risks to global energy supply from the Middle East war deepened.\nThe attacks on the vessels off the coast of Iraq prompted the nation's oil terminals to suspend
operations. Ships, meanwhile, were o", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://windward.ai/blog/iran-war-vessel-attacks-and-maritime-infrastructure-strikes/",
  "prompt": "List all vessel attacks with details. Which vessels were sunk or had major oil spills? How much oil was spilled in each attack? Were any attacks in the Gulf of Oman? Were any spills larger than 50,000 barrels?"
}
```

### 📋 Result

```
{"url": "https://windward.ai/blog/iran-war-vessel-attacks-and-maritime-infrastructure-strikes/", "content": "Based on the provided content, here are the details:\n\n## All Vessel Attacks\n\n1.
**SKYLIGHT** - Struck by projectile at anchor; fire, 4 injuries, crew evacuated\n2. **HERCULES STAR** - Struck by projectile while transiting outbound; fire, no injuries, returned to Dubai
anchorage\n3. **OCEAN ELECTRA** - Projectile detonated nearby during transit; no damage or injuries\n4. **MKD VYOM** - Struck by USV while transiting northbound; fire, 1 fatality, towed to safety\n5.
**STENA IMPERATIVE** - Struck by 2 projectiles while berthed at Port of Bahrain; fire extinguished, 1 shoreside fatality, 2 workers injured\n6. **PELAGIA** - UAV impact near vessel; no damage\n7.
**GOLD OAK** - Struck by projectile at anchor; structural damage to steel plating, no fire\n8. **LIBRA TRADER** - Struck by projectile at anchor; minor funnel damage, no injuries\n9. **SAFEEN
PRESTIGE** - Explosion near stern; hull damage, engine room fire, crew abandoned (no injuries)\n10. **MSC GRACE** - Projectile detonated ~1 nm away while drifting; no damage\n11. **SONANGOL NAMIBE** -
Struck by explosion at anchor near Khor al Zubair; cargo hold damage, **oil leakage** (visible oil on water)\n12. **MUSSAFAH 2** - Struck by 2 missiles; 4 fatalities, 3 severe injuries\n13. **GH
KAHLO** - Splash and bang nearby; no damage\n14. **ONE MAJESTY** - Struck by projectile at stern while at anchor; minor damage, no injuries\n15. **MAYUREE NAREE** - Projectile strike, engine room
fire; 3 crew missing, 20 evacuated\n16. **STAR GWYNETH** - Projectile strike; cargo hold and ballast tank breach, vessel listing, no environmental impact\n17. **SAFESEA VISHNU** - Struck during ship-
to-ship operation; fire, 1 casualty\n18. **ZEFYROS** - Struck during ship-to-ship operation; significant fire (extinguished), crew safe\n19. **SOURCE BLESSING** - Projectile struck accommodation
block; fire (extinguished), no pollution\n20. **GAS AL AHMADIAH** - Struck by projectile at anchor offshore Fujairah; minor structural damage\n21. **HALUL 50** - Struck by falling debris; bridge
window damage, crew safe\n\n## Infrastructure Attacks (mentioned but details not in tracker)\n- **ARABIA III** - Drilling rig struck by UAV; injuries, crew evacuated\n- **Arctic Metagaz platform** -
Mentioned as damaged asset\n\n## Vessels Sunk or Major Oil Spills\n\n**No vessels were confirmed sunk.** Only **SONANGOL NAMIBE** had a confirmed oil spill with \"visible oil on the water\" - however,
**no specific volume/quantity was provided** in the content.\n\n## Oil Spill Quantities\n\n**The content does not provide any numerical data on oil spill volumes** (no barrel counts, gallons, or tons
mentioned for any incident).\n\n## Gulf of Oman Attacks\n\n**Yes**, attacks occurred in the Gulf of Oman:\n- **PELAGIA** (March 3)\n- **GOLD OAK** (March 3)\n- **LIBRA TRADER** (March 3)\n\n## Spills
Larger than 50,000 Barrels\n\n**Cannot determine** - no oil spill quantities are provided in the content.\n\n---\n\n**Relevant links:**\n- [April 2, 2026: Iran War Maritime Intelligence
Daily](https://windward.ai/blog/april-2-maritime-intelligence-daily/)\n- [March 1 - First major cluster of attacks](https://windward.ai/blog/48-hours-into-the-iran-war/)\n- [March 3 Maritime
Intelligence Daily](https://windward.ai/blog/march-3-iran-war-maritime-intelligence-daily/)\n- [March 4 Maritime Intelligence Daily](https://windward.ai/blog/march-4-iran-war-maritime-intelligence-
daily/)\n- [March 6 - One Week Into the Iran War](https://windward.ai/blog/one-week-into-the-iran-war/)\n- [March 8 Maritime Intelligence Daily](https://windward.ai/blog/march-8-maritime-intelligence-
daily/)\n- [March 10 Maritime Intelligence Daily](https://windward.ai/blog/march-10-maritime-intelligence-daily/)\n- [March 11 Maritime Intelligence Daily](https://windward.ai/blog/march-11-maritime-
intelligence-daily/)\n- [March 12 Maritime Intelligence Daily](https://windward.ai/blog/march-12-maritime-intelligence-daily/)\n- [March 16 Maritime Intelligence
Daily](https://windward.ai/blog/march-16-maritime-intelligence-daily/)", "title": "Iran War Vessel Attacks and Maritime Infrastructure Strikes"}
```

```json
{
  "query": "tanker sunk oil spill Hormuz Oman war Iran attack cargo lost environmental 2026"
}
```

### 📋 Result

```
{"query": "tanker sunk oil spill Hormuz Oman war Iran attack cargo lost environmental 2026", "results": [{"title": "2026 Strait of Hormuz crisis - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic
disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran
launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a
major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and
Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf
states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump
announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military
campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit,
with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about
20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the
strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other
conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has
been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price
increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a
strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "First oil tanker attacked in the Strait of Hormuz according to Oman | Euronews", "url":
"https://www.euronews.com/business/2026/03/01/first-oil-tanker-attacked-in-the-strait-of-hormuz-according-to-oman", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2874940)\nAn oil
tanker was attacked off the coast of Musandam in the Strait of Hormuz. Four people were injured and all 20 crew members were evacuated, according to Oman's Maritime Security Centre.\nThe first attack
against a ship in the Strait of Hormuz occurred on Sunday morning.\nOman's Maritime Security Centre announced that an oil tanker named Skylight, flying the flag of the Republic of Palau, was targeted
around five nautical miles (9.26km", "api_data": null, "hint": null}, {"title": "Iran targets UAE energy infrastructure as gas field set ablaze, tanker struck near Strait of Hormuz", "url":
"https://www.cnbc.com/2026/03/17/iran-war-uae-energy-gas-field-oil-fujairah-strait-of-hormuz.html", "snippet": "A [fresh wave of attacks](https://www.cnbc.com/2026/03/15/iran-us-war-uae-target-
aggression.html) on the United Arab Emirates' energy infrastructure has ramped up concerns over prolonged supply disruptions amid the Iran war.\nIt comes after the world's largest ultra-sour gas
development was struck by a drone, a fire broke out in the UAE's Fujairah Oil Industry Zone, and another tanker was hit near the strategically vital [Strait of
Hormuz](https://www.cnbc.com/2026/03/16/us-is-allowing-iranian-ta", "api_data": null, "hint": null}, {"title": "Iran confirms attack on oil tanker for \u2018defying orders\u2019 not to cross Strait of
Hormuz", "url": "https://www.middleeastmonitor.com/20260301-iran-confirms-attack-on-oil-tanker-for-defying-orders-not-to-cross-strait-of-hormuz/", "snippet": "Iran confirmed Sunday that it had
attacked an oil tanker for defying orders not to cross the strategic Strait of Hormuz, Anadolu reports.\nThe state television reported that the tanker \u201cwas illegally attempting\u201d to cross the
passage.\nActivists on social media circulated images of the oil tanker on the verge of sinking, with plumes of smoke rising from it after it was targeted.\nOman\u2019s Maritime Security Center said
early Sunday that four people were injured in an attack on a Palau-flagged oil tanke", "api_data": null, "hint": null}, {"title": "Three more ships struck in the Persian Gulf as Iran warns of oil
prices hitting $200", "url": "https://www.cnbc.com/2026/03/12/iran-war-persian-gulf-strait-of-hormuz-ships-uae-iraq.html", "snippet": "Three more foreign ships were struck in the Persian Gulf
overnight, authorities said, as attacks intensify on vessels sailing through or near the [strategically vital Strait of Hormuz](https://www.cnbc.com/2026/03/11/strait-of-hormuz-closure-shipping-
economy-oil.html).\nThe latest incidents come after [three separate vessels](https://www.cnbc.com/2026/03/11/cargo-ship-struck-strait-of-hormuz-uk-iran-war.html) sustained damage in Gulf waters on
Wednesday and as Iran warns oil prices could climb to", "api_data": null, "hint": null}, {"title": "Oman Says Oil Tanker Targeted Off Its North Coast", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "Is the Strait of Hormuz a ticking
environmental time bomb? | South China Morning Post", "url": "https://www.scmp.com/week-asia/health-environment/article/3348680/environmental-risks-grow-iran-war-traps-oil-tankers-strait-hormuz",
"snippet": "Is the Strait of Hormuz a ticking environmental time bomb?\nA major oil spill in the Gulf could damage fragile marine habitats, leading to dire consequences for the region,
conservationists warn\n![Oil tankers and cargo ships line up in the Strait of Hormuz as seen from Khor Fakkan, the United Arab Emirates, on March 11. Photo:
AP](https://cdn.i-scmp.com/sites/default/files/styles/1020x680/public/d8/images/canvas/2026/04/01/9b95d96e-cdc0-445b-a7ce-7b1ed5a39bfe_7aaec9c8.jpg?itok=aU-r0a-K&v=17750387", "api_data": null, "hint":
null}, {"title": "Iran confirms attack on oil tanker for \u2018defying orders\u2019 not to cross Strait of Hormuz", "url": "https://www.aa.com.tr/en/energy/general/iran-confirms-attack-on-oil-tanker-
for-defying-orders-not-to-cross-strait-of-hormuz/55053", "snippet": null, "api_data": null, "hint": null}, {"title": "How oil tankers stuck in the Strait of Hormuz south of Iran threatens the Gulf
ecosystem - Greenpeace International", "url": "https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/", "snippet": "More than 85 large oil tankers are [currently trapped in
the Persian Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-gulf/). The reason: following attacks launched on Iran by Israel and the
United States on 28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and disrupted vessel position signals dramatically [increase the risk of oil
spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}, {"title": "Three cargo ships struck off Iran's coast, UK says, including one in Strait of Hormuz", "url":
"https://www.cnbc.com/2026/03/11/cargo-ship-struck-strait-of-hormuz-uk-iran-war.html", "snippet": "Three vessels off Iran's coast have been struck by projectiles, the United Kingdom Maritime Trade
Operations center said on Wednesday, the latest in a [flurry of incidents](https://www.ukmto.org/recent-incidents) reported in or near the Strait of Hormuz.\nOne of the ships reported it had been
struck 11 nautical miles north of Oman in the Strait of Hormuz, causing a fire onboard and forcing the crew to evacuate, the UKMTO said, without identifying the vessels.\nTwo other incidents were also
reporte", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Key findings from Windward's detailed tracker:
- 22 vessel attacks confirmed as of April 2, 2026
- NO vessels sunk
- Only SONANGOL NAMIBE had "visible oil on water" (not quantified)
- Other attacks caused fires, structural damage, but not major oil spills
- Most attacks involved projectile strikes, not the kind that would sink a loaded tanker
- Three attacks in the Gulf of Oman (PELAGIA, GOLD OAK, LIBRA TRADER on March 3) - but no major oil spills

Now let me check the SCMP article about environmental time bomb and the Greenpeace article about trapped tankers to see if any spill has occurred.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.scmp.com/week-asia/health-environment/article/3348680/environmental-risks-grow-iran-war-traps-oil-tankers-strait-hormuz",
  "prompt": "Has a major oil spill actually occurred? How large? Have any tankers been sunk? What is the current environmental impact? Any specific spill measured in barrels or tonnes?"
}
```

### 📋 Result

```
{"url": "https://www.scmp.com/week-asia/health-environment/article/3348680/environmental-risks-grow-iran-war-traps-oil-tankers-strait-hormuz", "content": "Based on the provided content:\n\n**No major
oil spill has actually occurred yet.** The article discusses the **risk** and **potential** for environmental disaster, not an actual spill.\n\n**Specific incidents mentioned:**\n- A Kuwaiti crude
tanker was set ablaze at Dubai Port in an Iranian attack that damaged its hull, sparking \"warnings of a possible oil spill\" (not a confirmed spill)\n\n**No tankers have been sunk** according to this
content.\n\n**Current environmental impact:** None specifically documented. The article focuses on warnings from conservationists about what **could** happen if a spill occurs.\n\n**Spill
measurements:** No actual spill volumes are provided. The only quantity mentioned is \"at least 21 billion litres of oil trapped on tankers\" in the Strait - this refers to oil cargo on vessels, not
spilled oil.\n\nThe article is essentially a warning piece about mounting environmental risks due to the concentration of oil tankers in a conflict zone, not a report of an actual environmental
disaster.\n\n---\n\n**Relevant links:**\nThe content does not contain any embedded hyperlinks to other sources.", "title": "Is the Strait of Hormuz a ticking environmental time bomb?"}
```

```json
{
  "query": "UNEP NOAA oil spill Gulf Oman Hormuz 2026 report assessment"
}
```

### 📋 Result

```
{"query": "UNEP NOAA oil spill Gulf Oman Hormuz 2026 report assessment", "results": [{"title": "Strait of Hormuz disruptions: Implications for global trade and development | UN Trade and Development
(UNCTAD)", "url": "https://unctad.org/publication/strait-hormuz-disruptions-implications-global-trade-and-development", "snippet":
"![](/sites/default/files/styles/cover_image/public/2026-03/osgttinf2026d1_1000x1414.jpg?itok=6NounUKD)\nThe Strait of Hormuz is one of the world\u2019s most critical maritime chokepoints, carrying
around a quarter of global seaborne oil trade and significant volumes of liquefied natural gas and fertilizers.\n![Bar graph showing the share of global trade passing through the Strait, based on
average flows during the week before the military escalation that began on 28 February.](/sites/default/files/inli", "api_data": null, "hint": null}, {"title": "2026 Strait of Hormuz crisis -
Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing
geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei.
In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings
prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The
Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the
United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli
territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US
President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed
Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline
in maritime transit, with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This
disruption affected about 20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the
IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster
than during any other conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The
closure of the strait has been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity
markets to suffer price increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea
by denying transit in a strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Sustained attacks in Gulf fuel fears of environmental disaster | The
National", "url": "https://www.thenationalnews.com/news/gulf/2026/03/24/sustained-attacks-in-gulf-fuel-fears-of-environmental-disaster/", "snippet": "Live updates: Follow the latest news on [US-Iran
war](https://www.thenationalnews.com/news/mena/2026/03/22/live-us-israel-iran-war-hormuz-trump/)\nThe conflict between Israel and the US and Iran presents a major risk of environmental damage to the
Gulf, experts have said.\nThe region\u2019s dense oil infrastructure, desalination plants and fragile ecosystems make it particularly vulnerable to attacks on energy facilities and ships at sea since
war broke out on February 28, with a lack of accurate infor", "api_data": null, "hint": null}, {"title": "Status of Oil Pollution in the Arabian Gulf and Shatt Al-Arab Estuary: A Review | Springer
Nature Link", "url": "https://link.springer.com/chapter/10.1007/978-90-481-3002-3_3", "snippet": "Abstract\nThe Arabian Gulf has enormous number of offshore oil and gas platforms and many major oil
terminals. It is also extremely busy shipping line for oil transports. Accidental spilling is unavoidable. About 25,000 tanker movements sail in and out of the Strait of Hormuz annually and transport
about 60% of all the oil carried by ships. In combination, these sources provide on a long-term a kind of input sources of petroleum. Activities associated with oil traffic include shores heavily
conta", "api_data": null, "hint": null}, {"title": "Is the Strait of Hormuz a ticking environmental time bomb? | South China Morning Post", "url": "https://www.scmp.com/week-asia/health-
environment/article/3348680/environmental-risks-grow-iran-war-traps-oil-tankers-strait-hormuz", "snippet": "Is the Strait of Hormuz a ticking environmental time bomb?\nA major oil spill in the Gulf
could damage fragile marine habitats, leading to dire consequences for the region, conservationists warn\n![Oil tankers and cargo ships line up in the Strait of Hormuz as seen from Khor Fakkan, the
United Arab Emirates, on March 11. Photo:
AP](https://cdn.i-scmp.com/sites/default/files/styles/1020x680/public/d8/images/canvas/2026/04/01/9b95d96e-cdc0-445b-a7ce-7b1ed5a39bfe_7aaec9c8.jpg?itok=aU-r0a-K&v=17750387", "api_data": null, "hint":
null}, {"title": "How oil tankers stuck in the Strait of Hormuz south of Iran threatens the Gulf ecosystem - Greenpeace International", "url":
"https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/", "snippet": "More than 85 large oil tankers are [currently trapped in the Persian
Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-gulf/). The reason: following attacks launched on Iran by Israel and the United States on
28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and disrupted vessel position signals dramatically [increase the risk of oil
spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}, {"title": "2026-004-Persian Gulf, Strait of Hormuz, and Gulf of Oman-Iranian Attacks on Commercial Vessels | MARAD",
"url": "https://www.maritime.dot.gov/msci/2026-004-persian-gulf-strait-hormuz-and-gulf-oman-iranian-attacks-commercial-vessels", "snippet": null, "api_data": null, "hint": null}, {"title": "2026
Hormuz Strait Disruption: Oil Market Impacts and Supply Risks - LNRG Technology", "url": "https://www.lnrg.technology/2026/03/15/2026-hormuz-strait-disruption-oil-market-impacts-and-supply-risks/",
"snippet": "![A narrow strait with oil tankers](https://image.jimcdn.com/app/cms/image/transf/dimension=435x1024:format=jpg/path/sc191c2ffc4c777b6/image/if5af73dbd53d86a8/version/1773649600/a-narrow-
strait-with-oil-tankers.jpg)\nThe near-total disruption of the Strait of Hormuz oil transit route is now in its third week as of mid-March 2026, as the escalating U.S.-Israeli conflict with Iran is
creating perhaps the most severe supply shock in modern oil market history. This analysis evaluates its operational ", "api_data": null, "hint": null}, {"title": "Iran Conflict and the Strait of
Hormuz: Impacts on Oil, Gas, and Other Commodities | Congress.gov | Library of Congress", "url": "https://www.congress.gov/crs-product/R45281", "snippet": null, "api_data": null, "hint": "Use
search_exa for cached content, or web_search for legislative information."}, {"title": "Affected Gulf Resources - Gulf Spill Restoration - NOAA", "url":
"https://www.gulfspillrestoration.noaa.gov/affected-gulf-resources", "snippet": "![A turtle with oil on it hangs in a net near the edge of a
boat](/sites/default/files/styles/4_3_960x720/public/2024-02/DWH%20effects%20on%20sea%20turtles%20and%20marine%20mammals.jpg?h=2d828ae9&itok=qvK9WtBn)\nOil released during the Deepwater Horizon
disaster injured plants, wildlife, and entire ecosystems. The oil posed a widespread threat from the deepest reaches of the Gulf to its shorelines. Both private and public lands were adversely
affected, including critically important federal and s", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Now I have a comprehensive picture. Let me synthesize:

## Key Facts:

1. **Active conflict**: US-Israel strikes on Iran began Feb 28, 2026. Iran retaliated with attacks on merchant ships, closure of Strait of Hormuz. As of April 2, 2026: 32 confirmed incidents (22 vessels, 10 facilities).

2. **No major oil spill has occurred yet**: Despite 22+ vessel attacks, no tanker has been sunk. The only confirmed oil leakage was from SONANGOL NAMIBE ("visible oil on water") but no quantification. No 50,000+ barrel spill has been reported.
   
3. **The Adalynn/Front Eagle collision** happened in June 2025 as a navigational accident, completely separate from the current conflict, so it's irrelevant to this question.

4. **Risk factors**: 85+ oil tankers are currently trapped in the Persian Gulf carrying 21 billion liters of oil cargo. With ongoing attacks and an active military campaign, environmental experts are warning of a "ticking time bomb" scenario.

5. **Question timeline**: The betting closes today (April 4) and resolves May 1. The conflict has been escalating for over 35 days now, and the question specifically asks whether a 50,000+ barrel conflict-related spill will occur in the Gulf of Oman before May 1.

## Analysis:

**For**

The case against a major spill: Despite 35+ days of intense conflict and 22+ vessel attacks, no catastrophic oil spill has materialized yet. No ships have actually sunk, and while attacks have caused fires and structural damage, they haven't breached hulls catastrophically. Traffic has dropped so dramatically that there are fewer laden tankers in the area to target. The US is actively working to reopen the strait and protect shipping. Historically, the Iran-Iraq tanker war saw 400+ ships attacked but very few exceeded the 50,000-barrel threshold—that's an enormous amount of oil, only reached by the largest spills on record.

**For YES:**
The case for a major spill: The conflict zone remains extremely active with relentless attacks. There are still 85+ loaded tankers trapped in the area. The US military campaign to open the strait could escalate into direct confrontation. Iran continues targeting shipping aggressively, and a single VLCC carrying 2 million barrels could exceed 50,000 barrels even with partial cargo loss. Mines may be present, shadow fleet tankers with poor maintenance are still operating, and the conflict appears to be escalating rather than de-escalating. Looking at historical precedent, most tanker attacks cause fires but ships survive—you typically need a vessel to sink or suffer catastrophic hull failure to reach that 50,000-barrel threshold. The question is whether the escalating nature of this conflict will eventually produce those conditions.

The conflict is serious and ongoing, but despite 35 days and 22+ attacks, no massive spill has occurred yet. Traffic has nearly stopped which reduces available targets, and modern double-hulled tankers are quite resilient to missile and drone strikes. I'm also noticing the question specifically requires the spill to occur in the Gulf of Oman—many attacks have been in the Persian Gulf or Strait of Hormuz instead. Given that 50,000 barrels is an extremely high threshold and even the much larger 1980s tanker war rarely produced spills of this magnitude from individual attacks, I'm settling on a probability around 8-12%, accounting for the ongoing conflict and potential for further escalation through operations like Epic Fury, but weighted heavily by the lack of such a spill despite weeks of active hostilities.

## 💬 Response

Now let me check for any very recent developments or specific large spill reports in the last few days.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "oil spill tanker attack Gulf Oman April 2026"
}
```

### 📋 Result

```
{"query": "oil spill tanker attack Gulf Oman April 2026", "results": [{"title": "First oil tanker attacked in the Strait of Hormuz according to Oman | Euronews", "url":
"https://www.euronews.com/business/2026/03/01/first-oil-tanker-attacked-in-the-strait-of-hormuz-according-to-oman", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2874940)\nAn oil
tanker was attacked off the coast of Musandam in the Strait of Hormuz. Four people were injured and all 20 crew members were evacuated, according to Oman's Maritime Security Centre.\nThe first attack
against a ship in the Strait of Hormuz occurred on Sunday morning.\nOman's Maritime Security Centre announced that an oil tanker named Skylight, flying the flag of the Republic of Palau, was targeted
around five nautical miles (9.26km", "api_data": null, "hint": null}, {"title": "Oman Says Oil Tanker Targeted Off Its North Coast", "url": "https://www.bloomberg.com/news/articles/2026-03-01/oman-
says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "Oil Tanker Attacked Near Oman Coast: One Crew Member Killed in Maritime Incident", "url":
"https://gulfnews.com/world/gulf/oman/oil-tanker-attacked-off-oman-coast-one-crew-member-killed-1.500460744", "snippet": "Omani Maritime Security Centre responds as one Indian national dies in
explosion\nDubai/Oman: An oil tanker flying the flag of the Republic of the Marshall Islands was attacked by an unmanned boat about 52 nautical miles off the coast of Muscat, leaving one crew member
dead, the Omani Maritime Security Centre said.\nThe attack comes amid an already tense regional situation involving Iran, the United States, and Israel, with GCC countries also directly affected.\nThe
tanker, MKD VYOM, was carrying a", "api_data": null, "hint": null}, {"title": "Iran Strikes Oman Port and Tanker, Escalating Gulf Tensions", "url": "https://gulfnews.com/world/gulf/oman-port-and-
tanker-hit-as-iran-strikes-gulf-states-1.500459743", "snippet": "Attacks mark first strikes on the sultanate which mediated US-Iran talks\nMUSCAT Iran expanded its retaliation campaign across the Gulf
on Sunday, striking [Oman for the first time](https://gulfnews.com/world/gulf/oman/drone-attack-targets-omans-duqm-port-one-worker-injured-1.500459511) since the conflict began and targeting an oil
tanker off its coast, in a dramatic escalation that threatens to widen the regional war.\nThe attack on Duqm commercial port marks the first direct Iranian strike on th", "api_data": null, "hint":
null}, {"title": "Gulf of Oman oil spill: Greenpeace warns of environmental disaster - Greenpeace International", "url": "https://www.greenpeace.org/international/press-release/75704/gulf-of-oman-oil-
spill-environmental-disaster/", "snippet": "Beirut, Lebanon \u2013 Greenpeace Middle East and North Africa (MENA) has warned of a potential environmental disaster after two crude oil tankers collided
between Iran and the United Arab Emirates on Tuesday.\nSatellite [imagery](https://media.greenpeace.org/Detail/27MZIFJRBAFKQ) indicates a large plume of oil stretching up to around 1500 hectares from
the site of the crash between two vessels, \u2018Adalynn\u2019 and \u2018Front Eagle\u2019, in the Gulf of Oman, approximately 22 nautical miles east of Khor Fakkan, near", "api_data": null, "hint":
null}, {"title": "Oil tanker attacked near the coast of Oman, 4 injured | The Times of Israel", "url": "https://www.timesofisrael.com/liveblog_entry/oil-tanker-attacked-near-the-coast-of-oman/",
"snippet": null, "api_data": null, "hint": null}, {"title": "Iran War Confirmed Vessel Attacks and Maritime Infrastructure Strikes", "url": "https://windward.ai/blog/iran-war-vessel-attacks-and-
maritime-infrastructure-strikes/", "snippet": "[April 2, 2026: Iran War Maritime Intelligence Daily](https://windward.ai/blog/april-2-maritime-intelligence-daily/)\nNumber of confirmed incidents: 32
(22 vessels and 10 oil, gas, and port facilities).\nSince the start of the Iran war, [maritime security](https://windward.ai/glossary/what-is-maritime-security/) incidents have expanded across the
commercial operating environment, affecting vessels at anchor, in transit, in drydock, and during [ship-to-ship operations](https://windward.ai/glossary/", "api_data": null, "hint": null}, {"title":
"2026 Strait of Hormuz crisis - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade,
has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's
supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps
(IRGC) issued warnings prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\":
\"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and
economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response,
Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel
passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran
to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on
merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit, with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside
the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about 20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG),
prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and
their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026
for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has been described as the largest disruption to the energy supply since the 1970s energy crisis, as
well as the largest in the history of the global oil market. Other commodity markets to suffer price increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait
of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null},
{"title": "Ships avoid the Strait of Hormuz, tanker hit off Oman", "url": "https://www.seatrade-maritime.com/security/ships-avoid-the-strait-of-hormuz-tanker-hit-off-oman", "snippet": null,
"api_data": null, "hint": null}, {"title": "4 injured in attack on oil tanker near Oman\u2019s coast", "url": "https://www.aa.com.tr/en/middle-east/4-injured-in-attack-on-oil-tanker-near-oman-s-
coast/3844826", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "oil spill 50000 barrels Gulf of Oman conflict tanker April 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "Dubai puts out Kuwaiti oil tanker fire after Iranian attack; no spill, crew safe | Ship Accidents | Shipping Telegraph", "url": "https://shippingtelegraph.com/ship-accidents/dubai-puts-
out-kuwaiti-oil-tanker-fire-after-iranian-attack-no-spill-crew-safe/", "snippet": "Dubai puts out Kuwaiti oil tanker fire after Iranian attack; no spill, crew safe | Ship Accidents | Shipping
Telegraph \n\n- Photo credit: Kuwait Oil Tanker Company S.A.K (KOTC) / Image for illustration purposes only.\n\n- Ship Accidents, Tankers\n\n# Dubai puts out Kuwaiti oil tanker fire after Iranian
attack; no spill, crew safe\n\n- 01/04/2026\n- by Shipping Telegraph\n\nTehran attacked and set ablaze a Kuwait-flagged crude oil tanker off Dubai on Tuesday, despite a threat by President Donald
Trump that", "highlights": ["Dubai puts out Kuwaiti oil tanker fire after Iranian attack; no spill, crew safe | Ship Accidents | Shipping Telegraph - Photo credit: Kuwait Oil Tanker Company S.A.K
(KOTC) / Image for illustration purposes only. - Ship Accidents, Tankers\n\n# Dubai puts out Kuwaiti oil tanker fire after Iranian attack; no spill, crew safe - 01/04/2026\n- by Shipping Telegraph
Tehran attacked and set ablaze a Kuwait-flagged crude oil tanker off Dubai on Tuesday, despite a threat by President Donald Trump that the US will obliterate Iran\u2019s energy plants if it does not
agree to a peace deal and open the Strait of Hormuz. The national oil company of the State of Kuwait, Kuwait Petroleum Corporation (KPC), said the fire on the Al-Salmi had been brought under control
following an Iranian attack, with no oil leak and no injuries to the crew. The VLCC ship was targeted outside of Al-Mikhtaf, Dubai, the KPC announced. KPC confirmed on Tuesday that the crew of the
VLCC Al-Salmi successfully extinguished the fire caused by a direct   ...    The crew members brought the fire under control by 4:26 a.m. Kuwait time in coordination with UAE authorities. No injuries
were reported among the 24 crew members, and no oil spill or environmental damage occurred, the statement of KPC reads. KPC said it is continuing to assess the damage in coordination with relevant
authorities. Authorities in Dubai confirmed their response to an incident involving a drone affecting a Kuwaiti oil tanker in Dubai waters (Anchorage \u201cE\u201d). No injuries have been reported,
and the safety of all 24 crew members has been secured, the government of Dubai media office reported. Dubai authorities also said that response teams successfully extinguished the fire involving the
Kuwaiti oil tanker in Dubai waters, with no oil leakage and no injuries reported. Relevant teams continue to assess the situation and take the necessary measures. The ship Al-Salmi is a 319660-dwt
crude oil tanker, built in 2011, and flagged in Kuwait. Dubai authorities confirm that response teams have successfully contained the incident involving the Kuwaiti oil tanker in Dubai waters, with no
oil leakage and no injuries reported. > \u2014 Dubai Media Office (@DXBMediaOffice) March 31, 2026 KPC Press Release on the attack on the Kuwaiti VLCC Al-Salmi outside of Al-Mikhtaf, Dubai.
pic.twitter.com/n5GtVmVI6n > \u2014 KPC | \u0645\u0624\u0633\u0633\u0629 \u0627\u0644\u0628\u062a\u0631\u0648\u0644 \u0627\u0644\u0643\u0648\u064a\u062a\u064a\u0629 (@kpcofficialkw) March 31,
2026\n\n#### Subscribe to our Newsletter We bring the latest news about the shipping industry\n\nEmail\n\nSubmit\n\n#### Most Read ### Danish icebreakers \u201cDanbjoern\u201d and \u201cIsbjoern\u201d
sold for recycling\n\n- 07/08/2023 ### NYK sends end-of-life Bulk Carrier for green recycling to Bangladesh\n\n- 07/07/2023 ### Hong Kong Convention Enter into Force\n\n- 27/06/2023\n\n#### Share This
Article\n\n#### Related news #### QatarEnergy chartered tanker hit by missile attack in Qatar\u2019s waters\n\n02/04/2026 #### No sign of three missing Thai crew after search of projectile-hit
Precious bulker\n\n01/04/202"], "published_date": "2026-04-01T00:53:00.000", "score": null}, {"title": "300m Empire Tanker Struck Near Hormuz | Oil Spills as ... - YouTube", "url":
"https://www.youtube.com/watch?v=cg1wmjzXu5g", "snippet": "# 1.2 MILLION BARRELS LOST: 300m Empire Tanker Struck Near Hormuz | Oil Spills as Prices Explode N18G\n\n- Channel: CNN-News18\n- Length:
02:18\n- Views: 6.1K\n- Likes: 86\n- Published: 2026-03-30T21:35:07-07:00\n- Category: News & Politics\n- Keywords: news18, cnn news18, latest news, Empire oil tanker strike, Suezmax tanker 300m, 1.2
million barrels oil spill, Strait of Hormuz tanker attack, Shahed drone vs tanker, oil price 100 2026, UKMTO latest report, Oman oil spill 2026, Iran maritime war, Empire", "highlights": ["# 1.2
MILLION BARRELS LOST: 300m Empire Tanker Struck Near Hormuz | Oil Spills as Prices Explode N18G - Channel: CNN-News18\n- Length: 02:18\n- Views: 6.1K\n- Likes: 86\n- Published:
2026-03-30T21:35:07-07:00   ...    - Keywords: news18, cnn news18, latest news, Empire oil tanker strike, Suezmax tanker 300m, 1.2 million barrels oil spill, Strait of Hormuz tanker attack, Shahed
drone vs tanker, oil price 100 2026, UKMTO latest report, Oman oil spill 2026, Iran maritime war, Empire Navigation ship news   ...    A Suezmax oil tanker carrying a massive 1.2 million barrels has
been struck and is reportedly sinking. We look at the \"Empire\" vessel's final coordinates, the drone strike that caused the breach, and why this disaster has pushed oil prices to a 4-year high. Is
the Gulf facing its worst environmental catastrophe? #OilSpill #BreakingNews #EnergyCrisis #EmpireTanker #StraitOfHormuz #WarUpdate #Economy2026 #Environment   ...    All right. Right now you are
looking at a picture of the oil super tanker Alsi in better times. Right now in a full load of its oil on fire in a port in Dubai after an Iranian strike. Cena's Matthew Chance has more on this for us
now.   ...    >> Yeah, John. I mean look this is exactly the sort of attack that the region and the global oil markets have been so worried about because this is you a really you know huge uh super
tanker. It's a Kuwaiti flagship. Um it's about 300 m long which is about three football fields long. So it's an enormous vessel uh carrying uh a maximum capacity of 1.2 million barrels of oil. And
we're told uh by the uh Kuwaiti news agency which is reporting on this uh that it was fully laden. And so this is a uh an oil tanker that is filled to the brim with perhaps more than a million barrels
of oil. It's been struck by a drone according to the authorities in Dubai. Uh it is currently on fire. Um there is damage to the hull with a potential for an oil spill in the surrounding waters.
That's the statement that's been released by the uh Kuwaiti Petroleum Corporation via their state news agency. Apparently, firefighters and emergency workers are on the scene uh trying to contain the
situation as best as they can. Uh there are no injuries that have been reported and the uh Dubai authorities in fact say, excuse me, that the 24 crew members that were on board have now been uh uh
brought to brought to safety. So there's no there's no injuries. Um but you know, look again, it comes as Iran uh strikes out, lashes out at the surrounding Gulf Arab states in response in retaliation
for the attacks that it's uh suffering from the United States and from Israeli strikes inside Iran. It's lashing out uh firing missiles in the past few hours towards Kuwait"], "published_date":
"2026-03-31T04:35:07.000", "score": null}, {"title": "Iran Attacks Oil Tanker After Trump Wavers on War Escalation - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-03-31/iran-
attacks-oil-tanker-after-trump-wavers-on-war-escalation", "snippet": "Iran Attacks Oil Tanker After Trump Wavers on War Escalation - Bloomberg\n\nWar With Iran:\n\nLive\n\nLatest\n\nHormuz Oil
Shock\n\nPakistan\u2019s Mediator Role\n\nKharg Island\n\nRed Sea Shipping\n\nBackForward\n\nWorld\n\nThe damaged Al-Salmi oil tanker on March 31.Source: Kuwait Oil Tankers Co.\n\nGift this
article\n\nContact us:Provide news feedback or report an error\n\nConfidential tip?Send a tip to our reporters\n\nSite feedback:Take our Survey\n\nBy Dana Khraiche and Sherif Tarek\n\nMarch 31, 2026
at 8:06 AM UTC\n\nUpdated o", "highlights": ["Iran Attacks Oil Tanker After Trump Wavers on War Escalation - Bloomberg\n\nWar With Iran:\n\nLive\n\nLatest\n\nHormuz Oil Shock Pakistan\u2019s Mediator
Role\n\nKharg Island\n\nRed Sea Shipping\n\nBackForward\n\nWorld The damaged Al-Salmi oil tanker on March 31.Source: Kuwait Oil Tankers Co.\n\nGift this article Contact us:Provide news feedback or
report an error\n\nConfidential tip?Send a tip to our reporters Site feedback:Take our Survey\n\nBy Dana Khraiche and Sherif Tarek\n\nMarch 31, 2026 at 8:06 AM UTC\n\nUpdated on March 31, 2026 at
11:46 AM UTC\n\nSave\n\nTranslate Iran hit a fully laden Kuwaiti oil tanker off the coast of Dubai during a fresh wave of attacks around the Persian Gulf, a sign it\u2019s willing to escalate strikes
on energy assets as the war drags on. The Tuesday assault on the Al-Salmi, a large crude carrier in an area packed with ships, is one of the most significant on a vessel since the US and Israel began
bombarding the Islamic Republic more than a month ago. Dubai authorities said a fire was contained and all 24 crew members are safe, with no oil leaking. Before it's here, it's on the Bloomberg
Terminal LEARN MORE Home BTV+ Market Data Opinion Audio Originals Magazine Events\n\nNews Markets Economics Technology Politics Green Crypto AI\n\nWork & Life Wealth Pursuits Businessweek CityLab
Sports Equality Management & Work\n\nMarket Data Stocks Commodities Rates & Bonds Currencies Futures Sectors Economic Calendar\n\nExplore Newsletters Explainers Pointed News Quiz Alphadots Game The
Big Take Graphics Submit a Tip About Us Terms of ServiceManage CookiesTrademarksPrivacy Policy\n\nCareersAdvertise\n\nAd Choices Help\u00a92026 Bloomberg L.P. All Rights Reserved."], "published_date":
"2026-03-31T00:00:00.000", "score": null}, {"title": "Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port", "url": "https://www.insurancejournal.com/news/international/2026/03/31/864006.htm",
"snippet": "Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port \n\n \n\n \n\n- Subscribe\n- Article\n- 0 Comments\n\nAn Iranian drone hit a fully laden Kuwaiti oil tanker off Dubai early on
Tuesday in one of the most significant attacks on a vessel in a month of war, pushing crude prices higher and heightening tension around the vital Strait of Hormuz.\n\nThe Al-Salmi, a Kuwait-flagged
very large crude carrier, was in the anchorage zone of Dubai\u2019s port, just 31 nautical miles northwest of the emirate and in an ar", "highlights": ["Iran Strikes Fully Laden Kuwait Oil Tanker in
Dubai Port \n\n \n\n \n\n- Subscribe\n- Article\n- 0 Comments An Iranian drone hit a fully laden Kuwaiti oil tanker off Dubai early on Tuesday in one of the most significant attacks on a vessel in a
month of war, pushing crude prices higher and heightening tension around the vital Strait of Hormuz. The Al-Salmi, a Kuwait-flagged very large crude carrier, was in the anchorage zone of Dubai\u2019s
port, just 31 nautical miles northwest of the emirate and in an area packed with ships waiting to exit the Persian Gulf. The strike \u2014 which happened just after midnight local time \u2014 damaged
the hull and started a fire on board, state-run Kuwait Petroleum   ...    The Dubai Media Office said on X later on Tuesday that the fire had been extinguished and the incident had been contained,
with no oil leakage. All 24 crew members were safe. The incident is yet another sign that a deepening Middle East conflict shows little sign of nearing a resolution, with mooted peace plans still at
odds with reality on the ground and inconsistent rhetoric from Washington. US President Donald Trump earlier issued threats against Iranian infrastructure, including power plants and oil facilities,
and has sent more troops to the region as the war extends into a fifth week. The tanker attack pushed oil prices higher, with West Texas Intermediate futures jumping almost 4% toward $107 a barrel,
before paring gains. The Al-Salmi entered the gulf in late February and has been there since. Straight lines shown in the map indicate that its geolocation signals were interfered with. Iran has near-
total control of the Strait of Hormuz \u2014 the narrow waterway that\u2019s the gateway to the Persian Gulf \u2014 and has effectively closed it to all but a trickle of vessels, paralyzing shipments
of energy and other goods. Tehran has targeted ships and energy infrastructure on several occasions, but attacks on vessels in and around the strait appeared to have eased in recent days. The last
reported incident was on March 21, when a bulk carrier reported a near miss. The latest attack will revive shipowners\u2019 concerns, even as Iran takes steps toward restoring some traffic through the
strait on its own terms. Dubai\u2019s anchorage area is a frequent stopping point as vessels wait to secure war-risk insurance cover and finalize details before exiting via the narrow corridor. As of
Tuesday morning, there were more than 400 ships of all types in and around the anchorage where Al-Salmi was   ...    Read More: Iran\u2019s Grip on Hormuz Is Tighter Than Ever After a Month of War Al-
Salmi crossed the strait into the Gulf in late February, reaching Saudi Arabia\u2019s Khafji port to pick up some barrels, ship-tracking data show. The tanker then sailed onward to Kuwait\u2019s Mina
Al Ahmadi for another cargo, before moving, fully laden, to the United Arab Emirates. It has been off Dubai since. The ship\u2019s signals through this time indicate that it wanted to make clear its
associations as Iran stepped up attacks on vessels. It said it was sailing under the Kuwaiti flag as it entered the Gulf, adding that it was bound for China\u2019s   ...    Related: - US Warns on Bab
El-Mandeb Strait After Iran Shipping Threat - Bessent Says Hormuz Ships Insurance Program to Start Soon - Chubb Outlines Structure of $20B Gulf Reinsurance Facility, Now Including Liability Cover - US
$20B Reinsurance Plan Unlikely to Restart Gulf Shipping Without Liability Cover Copyright 2026 Bloomberg.\n\nTopics Energy Oil Gas\n\nWas this article valuable?\n\nYes No   ...    - Categories:
International & Reinsurance News Topics: marine cargo insurance, marine hull insurance, marine liability insurance, marine war risks, Ocean marine, protection and indemnity (P&I), Reinsurance, US Iran
conflict, war risk   ...    - Restaurants & Bars: Liquor Sales, Risk Transfer & Other Trends - Oil Prices Jump After Trump Says Attacks on Iran Will Continue\n- \"Ask The Expert\" Webinar - Tap Into
Our Expertise - April 2 The Additional Insured Illusion (and Other Feats of Contractual Risk Transfer Magic) - April 9 Cyber: No Biz Too Small\n- April 16 When Employees Travel to Other States to
Work, Which WC Law Applies? - April "], "published_date": "2026-03-31T07:13:52.000", "score": null}, {"title": "Iran War: Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port Area - Bloomberg",
"url": "https://www.bloomberg.com/news/articles/2026-03-30/iran-strikes-fully-laden-kuwait-oil-tanker-in-dubai-port-area", "snippet": "Iran War: Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai
Port Area - Bloomberg\n\nWar With Iran:\n\nLive\n\nHormuz Oil Shock\n\nTrump\u2019s NATO Warning\n\nPakistan\u2019s Mediator Role\n\nKharg Island\n\nRed Sea
Shipping\n\nBackForward\n\nMarkets\n\nMarkets\n\nGift this article\n\nContact us:Provide news feedback or report an error\n\nConfidential tip?Send a tip to our reporters\n\nSite feedback:Take our
Survey\n\nBy Fiona MacDonald, Sherif Tarek, and Weilun Soon\n\nMarch 30, 2026 at 11:32 PM UTC\n\nUpdated on\n\nMarch 31, 2026 at 5:", "highlights": ["Iran War: Iran Strikes Fully Laden Kuwait Oil
Tanker in Dubai Port Area - Bloomberg\n\nWar With Iran:\n\nLive Hormuz Oil Shock\n\nTrump\u2019s NATO Warning\n\nPakistan\u2019s Mediator Role\n\nKharg Island\n\nRed Sea
Shipping\n\nBackForward\n\nMarkets Markets\n\nGift this article\n\nContact us:Provide news feedback or report an error Confidential tip?Send a tip to our reporters\n\nSite feedback:Take our Survey By
Fiona MacDonald, Sherif Tarek, and Weilun Soon\n\nMarch 30, 2026 at 11:32 PM UTC\n\nUpdated on March 31, 2026 at 5:57 AM UTC\n\nSave An Iranian drone hit a fully laden Kuwaiti oil tanker off Dubai
early on Tuesday in one of the most significant attacks on a vessel in a month of war, pushing crude prices higher and heightening tension around the vital Strait of Hormuz. The Al-Salmi, a Kuwait-
flagged very large crude carrier, was in the anchorage zone of Dubai\u2019s port, just 31 nautical miles northwest of the emirate and in an area packed with ships waiting to exit the Persian Gulf. The
strike \u2014 which happened just after midnight local time \u2014 damaged the hull and started a fire on board, state-run Kuwait Petroleum Corp. said in a statement. Home BTV+ Market Data Opinion
Audio Originals Magazine Events\n\nNews Markets Economics Technology Politics Green Crypto AI\n\nWork & Life Wealth Pursuits Businessweek CityLab Sports Equality Management & Work\n\nMarket Data
Stocks Commodities Rates & Bonds Currencies Futures Sectors Economic Calendar\n\nExplore Newsletters Explainers Pointed News Quiz Alphadots Game The Big Take Graphics Submit a Tip About Us Terms of
ServiceDo Not Sell or Share My Personal InformationTrademarksPrivacy Policy\n\nCareersAdvertise\n\nAd Choices Help\u00a92026 Bloomberg L.P. All Rights Reserved."], "published_date":
"2026-03-30T23:32:51.000", "score": null}]
```

## 💭 Thinking

This is very important - I found a CNN-News18 YouTube video with the title "1.2 MILLION BARRELS LOST: 300m Empire Tanker Struck Near Hormuz | Oil Spills as Prices Explode" from March 30/31, 2026. But I need to verify this carefully. The video description mentions keywords like "Empire oil tanker strike, Suezmax tanker 300m, 1.2 million barrels oil spill, Strait of Hormuz tanker attack, Oman oil spill 2026" but the actual transcript seems to be talking about the Al-Salmi tanker (the Kuwaiti VLCC in Dubai), which was confirmed to have NO oil leakage.
 
The transcript clearly references the Al-Salmi tanker, and Kuwaiti authorities confirmed there was no oil leakage from that incident. The video's sensationalist title claiming "1.2 MILLION BARRELS LOST" appears to be clickbait when the actual fire was contained with no confirmed oil spill. I should search specifically for "Empire oil tanker" and "Empire Navigation" to see if this is a separate incident from the Al-Salmi event, since the timing and details don't align.

## 💬 Response

I found a potentially critical lead - a CNN-News18 video mentioning "Empire Tanker" and "1.2 million barrels lost" near Hormuz. Let me verify this claim.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "\"Empire\" tanker struck Hormuz oil spill 2026"
}
```

### 📋 Result

```
{"query": "\"Empire\" tanker struck Hormuz oil spill 2026", "results": [{"title": "2026 Strait of Hormuz crisis - Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis",
"snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military
strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military
bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait
of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced
ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali
Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings
prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and
later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21
confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline in maritime transit, with tanker traffic dropping first by approximately 70% and over 150
ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This disruption affected about 20% of the world's daily oil supply and significant volumes of
liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the
ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster than during any other conflict in recent history; Brent crude oil prices surpassed
US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The closure of the strait has been described as the largest disruption to the energy supply
since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity markets to suffer price increases from the crisis include aluminum, fertilizer, and
helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea by denying transit in a strait used for international navigation.\\n\\n\", \"mode\":
\"full\"}"}]}, "hint": null}, {"title": "Tankers Struck Near Gulf as Hormuz Traffic All But Halted - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-
targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "First oil tanker attacked in the Strait of Hormuz according to Oman | Euronews", "url":
"https://www.euronews.com/business/2026/03/01/first-oil-tanker-attacked-in-the-strait-of-hormuz-according-to-oman", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2874940)\nAn oil
tanker was attacked off the coast of Musandam in the Strait of Hormuz. Four people were injured and all 20 crew members were evacuated, according to Oman's Maritime Security Centre.\nThe first attack
against a ship in the Strait of Hormuz occurred on Sunday morning.\nOman's Maritime Security Centre announced that an oil tanker named Skylight, flying the flag of the Republic of Palau, was targeted
around five nautical miles (9.26km", "api_data": null, "hint": null}, {"title": "Iran targets UAE energy infrastructure as gas field set ablaze, tanker struck near Strait of Hormuz", "url":
"https://www.cnbc.com/2026/03/17/iran-war-uae-energy-gas-field-oil-fujairah-strait-of-hormuz.html", "snippet": "A [fresh wave of attacks](https://www.cnbc.com/2026/03/15/iran-us-war-uae-target-
aggression.html) on the United Arab Emirates' energy infrastructure has ramped up concerns over prolonged supply disruptions amid the Iran war.\nIt comes after the world's largest ultra-sour gas
development was struck by a drone, a fire broke out in the UAE's Fujairah Oil Industry Zone, and another tanker was hit near the strategically vital [Strait of
Hormuz](https://www.cnbc.com/2026/03/16/us-is-allowing-iranian-ta", "api_data": null, "hint": null}, {"title": "Burning Oil, Narrow Waters: The Tanker Strike That Brings Gulf War Danger to the
Surface", "url": "https://scheerpost.com/2026/03/31/burning-oil-narrow-waters-the-tanker-strike-that-brings-gulf-war-danger-to-the-surface/", "snippet": "In one of the scariest moments in modern
history, we're doing our best at ScheerPost to pierce the fog of lies that conceal it but we need some help to pay our writers and staff. Please consider a[tax-deductible donation].\nScheerPost
Staff\nThe fire on the Kuwaiti supertanker Al-Salmi off Dubai is more than another war headline\u2014it is the kind of event that turns elite military brinkmanship into immediate global danger.\nA
vessel carrying roughly two million barrels of crude oil\u2014cargo worth more th", "api_data": null, "hint": null}, {"title": "Iran War: Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port Area
- Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-03-30/iran-strikes-fully-laden-kuwait-oil-tanker-in-dubai-port-area", "snippet": null, "api_data": null, "hint": null}, {"title":
"Does video show Pakistani-flagged tanker burning in Strait of Hormuz? Here's the truth | Snopes.com", "url": "https://www.snopes.com/fact-check/video-strait-of-hormuz-pakistani-flagged-tanker/",
"snippet": "The footage appears to show the Malta-flagged Safeen Prestige, which was reportedly struck twice in the Strait of Hormuz in March 2026. According to online databases, the Safeen Prestige
is a container ship, not an oil tanker. Snopes could not independently verify the authenticity of the footage, nor claims that Iran was behind the reported strikes on the ship.\nIn March 2026, a
[video](https://www.instagram.com/p/DWZBKfdiqPR/) ([archived](https://perma.cc/98YL-EBUB)) circulated online that socia", "api_data": null, "hint": null}, {"title": "Why it's so hard to get oil
through the Strait of Hormuz right now", "url": "https://www.nbcnews.com/world/iran/strait-of-hormuz-closure-shipping-oil-strikes-rcna262898", "snippet": "Three ships were attacked [in the Strait of
Hormuz](https://www.nbcnews.com/news/us-news/us-destroys-mine-laying-ships-strait-hormuz-audacious-plan-refill-grea-rcna262885) on Wednesday, a British navy-run monitoring service said, the latest in
a flurry of attacks on the vital oil choke point.\nAs Iran targets ships with missiles and drones, even attempting to navigate [the strategic waterway](https://www.nbcnews.com/world/iran/live-
blog/live-updates-iran-war-israel-us-lebanon-tehran-oil-prices-ho", "api_data": null, "hint": null}, {"title": "LIVE UPDATES: Cargo ship struck in Strait of Hormuz as Iran launches drone, missile
attacks | Fox News Digital", "url": "https://www.foxnews.com/live-news/us-iran-israel-war-latest-march-11-live-updates", "snippet": "Cargo ship hit by projectile in Strait of Hormuz while Iran
launches fresh attacks on Middle East\nA cargo ship was struck on Wednesday by a projectile in the Strait of Hormuz, setting it on fire. It happened as Iran launched another wave of attacks across the
Middle East in response to Operation Epic Fury, targeting countries including Israel, Qatar and the United Arab Emirates.\nCoverage for this event has ended.\nContainer ship struck by projectile 40
miles off Dubai, British military says\nThe U", "api_data": null, "hint": null}, {"title": "Day 32 of Middle East conflict \u2014 Iran threatens US tech companies, Kuwaiti oil tanker attacked | CNN",
"url": "https://www.cnn.com/2026/03/31/world/live-news/iran-war-us-trump-oil", "snippet": "Our live coverage has ended\n\u2022 Get the latest updates on[ the war with Iran
here.](https://www.cnn.com/2026/04/01/world/live-news/iran-war-us-trump-oil)\nWhat we know so far\n\u2022 A new timeline: President Donald Trump will deliver an address to the nation on Wednesday
night regarding Iran. It comes after Trump said the US could be done with its war with Iran [within two to three weeks](https://www.cnn.com/2026/03/31/world/live-news/iran-war-us-trump-oil?post-
id=cmnf60zv200003b6qhbhserhd). Iran has in", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Empire tanker oil spill sinking Strait of Hormuz Gulf of Oman March 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "300m Empire Tanker Struck Near Hormuz | Oil Spills as ...", "url": "https://www.youtube.com/watch?v=cg1wmjzXu5g", "snippet": "# 1.2 MILLION BARRELS LOST: 300m Empire Tanker Struck Near
Hormuz | Oil Spills as Prices Explode N18G\n\n- Channel: CNN-News18\n- Length: 02:18\n- Views: 6.1K\n- Likes: 86\n- Published: 2026-03-30T21:35:07-07:00\n- Category: News & Politics\n- Keywords:
news18, cnn news18, latest news, Empire oil tanker strike, Suezmax tanker 300m, 1.2 million barrels oil spill, Strait of Hormuz tanker attack, Shahed drone vs tanker, oil price 100 2026, UKMTO latest
report, Oman oil spill 2026, Iran maritime war, Empire", "highlights": ["# 1.2 MILLION BARRELS LOST: 300m Empire Tanker Struck Near Hormuz | Oil Spills as Prices Explode N18G - Channel: CNN-News18\n-
Length: 02:18\n- Views: 6.1K\n- Likes: 86\n- Published: 2026-03-30T21:35:07-07:00   ...    - Keywords: news18, cnn news18, latest news, Empire oil tanker strike, Suezmax tanker 300m, 1.2 million
barrels oil spill, Strait of Hormuz tanker attack, Shahed drone vs tanker, oil price 100 2026, UKMTO latest report, Oman oil spill 2026, Iran maritime war, Empire Navigation ship news   ...    A
Suezmax oil tanker carrying a massive 1.2 million barrels has been struck and is reportedly sinking. We look at the \"Empire\" vessel's final coordinates, the drone strike that caused the breach, and
why this disaster has pushed oil prices to a 4-year high. Is the Gulf facing its worst environmental catastrophe? #OilSpill #BreakingNews #EnergyCrisis #EmpireTanker #StraitOfHormuz #WarUpdate
#Economy2026 #Environment   ...    All right. Right now you are looking at a picture of the oil super tanker Alsi in better times. Right now in a full load of its oil on fire in a port in Dubai after
an Iranian strike. Cena's Matthew Chance has more on this for us now.   ...    >> Yeah, John. I mean look this is exactly the sort of attack that the region and the global oil markets have been so
worried about because this is you a really you know huge uh super tanker. It's a Kuwaiti flagship. Um it's about 300 m long which is about three football fields long. So it's an enormous vessel uh
carrying uh a maximum capacity of 1.2 million barrels of oil. And we're told uh by the uh Kuwaiti news agency which is reporting on this uh that it was fully laden. And so this is a uh an oil tanker
that is filled to the brim with perhaps more than a million barrels of oil. It's been struck by a drone according to the authorities in Dubai. Uh it is currently on fire. Um there is damage to the
hull with a potential for an oil spill in the surrounding waters. That's the statement that's been released by the uh Kuwaiti Petroleum Corporation via their state news agency. Apparently,
firefighters and emergency workers are on the scene uh trying to contain the situation as best as they can. Uh there are no injuries that have been reported and the uh Dubai authorities in fact say,
excuse me, that the 24 crew members that were on board have now been uh uh brought to brought to safety. So there's no there's no injuries. Um but you know, look again, it comes as Iran uh strikes
out, lashes out at the surrounding Gulf Arab states in response in retaliation for the attacks that it's uh suffering from the United States and from Israeli strikes inside Iran. It's lashing out uh
firing missiles in the past few hours towards Kuwait"], "published_date": "2026-03-31T04:35:07.000", "score": null}, {"title": "Two Gulf Attacks in 12 Hours: Container Ships Now in the Crosshairs as
Iran Strikes Beyond Tankers", "url": "https://eagleintelmari.com/news/express-rome-al-salmi-dual-strike-gulf-container-tanker-escalation", "snippet": "Two Gulf Attacks in 12 Hours: Container Ships Now
in the Crosshairs as Iran Strikes Beyond Tankers\n\n\u2190 Eagle Intelligence News\n\nWar Risk\n\n# Two Gulf Attacks in 12 Hours: Container Ships Now in the Crosshairs as Iran Strikes Beyond
Tankers\n\nEAGLE Intelligence Unit\u00b7EAGLE Intelligence Unit\u00b7March 31, 2026 \u00b7 10:29 UTC\u00b74 min read\n\nWhy This Matters\n\nProjectiles targeted the Liberian-flagged container ship
Express Rome near Saudi Arabia's Ras Tanura, hours before an Iranian drone struck the VLCC Al Salmi", "highlights": ["Two Gulf Attacks in 12 Hours: Container Ships Now in the Crosshairs as Iran
Strikes Beyond Tankers   ...    # Two Gulf Attacks in 12 Hours: Container Ships Now in the Crosshairs as Iran Strikes Beyond Tankers EAGLE Intelligence Unit\u00b7EAGLE Intelligence Unit\u00b7March 31,
2026 \u00b7 10:29 UTC\u00b74 min read\n\nWhy This Matters Projectiles targeted the Liberian-flagged container ship Express Rome near Saudi Arabia's Ras Tanura, hours before an Iranian drone struck the
VLCC Al Salmi off Dubai. The escalation from tankers to container vessels signals a fundamental shift in targeting doctrine. The Gulf's commercial shipping lanes absorbed two attacks in under twelve
hours on March 31, 2026, marking the first time container vessels have been directly targeted alongside crude carriers since the Hormuz crisis began on February 28. At 13:52 UTC on March 31, two
unidentified projectiles splashed into the water approximately 22 nautical miles northeast of Saudi Arabia's Ras Tanura terminal \u2014 the Kingdom's largest oil export facility \u2014 narrowly
missing the Liberian-flagged container ship Express Rome (IMO 9484936, MMSI 636015019). The 349-meter Neo-Panamax vessel, built in   ...    Hours earlier, at approximately 00:10 local time (20:10 UTC
March 30), an Iranian drone struck the Kuwait-flagged VLCC Al Salmi (IMO 9534793) while she sat fully laden with approximately 2 million barrels of crude oil at the Dubai   ...    The targeting of the
Express Rome represents a qualitative shift. Since February 28, Iranian strikes and proxies have concentrated on crude carriers, tankers, and petroleum infrastructure \u2014 high-value targets with
direct energy market   ...    That calculus has changed. The Express Rome was transiting near Ras Tanura, Saudi Aramco's primary crude export   ...    War-risk premiums for Gulf transits have already
reached approximately 10% of vessel value \u2014 up from 0.05% before the crisis. The dual-strike pattern accelerates the insurance deterioration in three ways. First, container ship operators now
face the same premium escalation that tanker operators absorbed weeks ago.   ...    Third, Brent crude has surged 59% in March alone \u2014 the largest monthly gain on record \u2014 closing above $116
per barrel.   ...    Brent crude prices briefly spiked after the Al Salmi attack before settling above $113. The Express Rome near-miss   ...    The boardroom sentence: When projectiles are landing 22
nautical miles from Ras Tanura and drones are hitting VLCCs at   ...    # war-risk# gulf-shipping# express-rome# al-salmi# ras-tanura# container-shipping# hormuz-crisis# insurance#   ...    ##
\ud83d\udcf0 Related Analysis\n\n### Seven Seafarers Killed as Hormuz Attacks Persist; Shipping at Near-Zero War RiskCommercial shipping through the Strait of Hormuz has collapsed to near-zero levels
as maritime attacks continue into the 10th day of the Iran conflict. At least seven seafarers have been killed and several injured. The United Kingdom Maritime Trade Operations center (UKMTO) reported
13 maritime security incidents between February 28 and March 8, with 10 classified as attacks. The Joint Maritime Information Center (JMIC) maintains the threat environment at 'CRITICAL' level despite
a temporary pause in recent attacks.Mar 9, 2026 ### When a Chokepoint Closes: The Hormuz Crisis and Global Supply Shock in Real Time War RiskFour weeks into Iran-Israel conflict, Strait of Hormuz
near-closure threatens 20% of global oil supply. Brent crude surges 51% this month; Navy escorts begin. At current pace, economic fallout unavoidable by mid-April.Mar 31, 2026 ### Iran Drone Strikes
Fully Laden Kuwaiti VLCC Off Dubai: Al-Salmi Fire Ignites Insurance Reckoning as Brent Tops $115 War RiskIranian drone hits Kuwait-flagged VLCC Al-Salmi off Dubai with 2M barrels aboard, igniting
fire. Brent surges   ...    ### The IRGC Toll Booth's Legal Trap: Why Paying $2 Million to Pass Hormuz Could Land Shipowners in a US Federal Court War RiskIran's $2"], "published_date":
"2026-03-31T10:29:00.000", "score": null}, {"title": "Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port", "url": "https://www.insurancejournal.com/news/international/2026/03/31/864006.htm",
"snippet": "Iran Strikes Fully Laden Kuwait Oil Tanker in Dubai Port \n\n \n\n \n\n- Subscribe\n- Article\n- 0 Comments\n\nAn Iranian drone hit a fully laden Kuwaiti oil tanker off Dubai early on
Tuesday in one of the most significant attacks on a vessel in a month of war, pushing crude prices higher and heightening tension around the vital Strait of Hormuz.\n\nThe Al-Salmi, a Kuwait-flagged
very large crude carrier, was in the anchorage zone of Dubai\u2019s port, just 31 nautical miles northwest of the emirate and in an ar", "highlights": ["Iran Strikes Fully Laden Kuwait Oil Tanker in
Dubai Port \n\n \n\n \n\n- Subscribe\n- Article\n- 0 Comments An Iranian drone hit a fully laden Kuwaiti oil tanker off Dubai early on Tuesday in one of the most significant attacks on a vessel in a
month of war, pushing crude prices higher and heightening tension around the vital Strait of Hormuz. The Al-Salmi, a Kuwait-flagged very large crude carrier, was in the anchorage zone of Dubai\u2019s
port, just 31 nautical miles northwest of the emirate and in an area packed with ships waiting to exit the Persian Gulf. The strike \u2014 which happened just after midnight local time \u2014 damaged
the hull and started a fire on board, state-run Kuwait Petroleum Corp. said in a statement. The Dubai Media Office said on X later on Tuesday that the fire had been extinguished and the incident had
been contained, with no oil leakage. All 24 crew members were safe. The incident is yet another sign that a deepening Middle East conflict shows little sign of nearing a resolution, with mooted peace
plans still at odds with reality on the ground and inconsistent rhetoric from Washington. US President   ...    sent more troops to the region as the war extends into a fifth week. The tanker attack
pushed oil prices higher, with West Texas Intermediate futures jumping almost 4% toward $107 a barrel, before paring gains. The Al-Salmi entered the gulf in late February and has been there since.
Straight lines shown in the map indicate that its geolocation signals were interfered with. Iran has near-total control of the Strait of Hormuz \u2014 the narrow waterway that\u2019s the gateway to
the Persian Gulf \u2014 and has effectively closed it to all but a trickle of vessels, paralyzing shipments of energy and other goods. Tehran has targeted ships and energy infrastructure on several
occasions, but attacks on vessels in and around the strait appeared to have eased in recent days. The last reported incident was on March 21, when a bulk carrier reported a near miss. The latest
attack will revive shipowners\u2019 concerns, even as Iran takes steps toward restoring some traffic through the strait on its own terms. Dubai\u2019s anchorage area is a frequent stopping point as
vessels wait to secure war-risk insurance cover and finalize details before exiting via the narrow corridor. As of Tuesday morning, there were more than 400 ships of all types in and around the
anchorage where Al-Salmi was struck, according to data compiled by Bloomberg. Electronic interference can potentially misrepresent ships\u2019 true   ...    Read More: Iran\u2019s Grip on Hormuz Is
Tighter Than Ever After a Month of War Al-Salmi crossed the strait into the Gulf in late February, reaching Saudi Arabia\u2019s Khafji port to pick up some barrels, ship-tracking data show. The tanker
then sailed onward to Kuwait\u2019s Mina Al Ahmadi for another cargo, before moving, fully laden, to the United Arab Emirates. It has been off Dubai since. The ship\u2019s signals through this time
indicate that it wanted to make clear its associations as Iran stepped up attacks on vessels. It said it was sailing under the Kuwaiti flag as it entered the Gulf, adding that it was bound for
China\u2019s   ...    Related: - US Warns on Bab El-Mandeb Strait After Iran Shipping Threat - Bessent Says Hormuz Ships Insurance Program to Start Soon - Chubb Outlines Structure of $20B Gulf
Reinsurance Facility, Now Including Liability Cover - US $20B Reinsurance Plan Unlikely to Restart Gulf Shipping Without Liability Cover Copyright 2026 Bloomberg.\n\nTopics Energy Oil Gas\n\nWas this
article valuable?\n\nYes No   ...    - Oil Prices Jump After Trump Says Attacks on Iran Will Continue\n- \"Ask The Expert\" Webinar - Tap Into Our Expertise - April 2 The Additional Insured Illusion
(and Other Feats of Contractual Risk Transfer Magic)   ...    - April"], "published_date": "2026-03-31T07:13:52.000", "score": null}, {"title": "Iran Escalates Beyond Transit: First Direct Attack on
Anchored Tanker at Dubai Port", "url": "https://eagleintelmari.com/news/hormuz-oil-tanker-strike-dubai-anchorage-iran-escalation", "snippet": "Iran Escalates Beyond Transit: First Direct Attack on
Anchored Tanker at Dubai Port\n\n\u2190 Eagle Intelligence News\n\nEnergy\n\n# Iran Escalates Beyond Transit: First Direct Attack on Anchored Tanker at Dubai Port\n\nEagle Intelligence\u00b7EAGLE
Intelligence Unit\u00b7March 31, 2026 \u00b7 09:36 UTC\u00b73 min read\n\nWhy This Matters\n\nKuwaiti crude tanker hit off Dubai anchorage by Iranian projectile; fire contained, crew safe. First
strike on commercial vessel at anchor near UAE, signaling new operational scope.\n\nA fully lo", "highlights": ["Iran Escalates Beyond Transit: First Direct Attack on Anchored Tanker at Dubai
Port\n\n\u2190 Eagle Intelligence News\n\nEnergy   ...    Eagle Intelligence\u00b7EAGLE Intelligence Unit\u00b7March 31, 2026 \u00b7 09:36 UTC\u00b73 min read\n\nWhy This Matters Kuwaiti crude tanker
hit off Dubai anchorage by Iranian projectile; fire contained, crew safe. First strike on commercial vessel at anchor near UAE, signaling new operational scope. A fully loaded Kuwaiti crude oil tanker
caught fire after being struck by a projectile while anchored off Dubai on Monday, marking a critical escalation in Iran's maritime campaign. The attack, the first confirmed strike on a commercial
vessel at anchor within UAE territorial waters, occurred roughly 31 nautical miles northwest of Dubai. Local authorities contained the blaze with no reported oil leakage and all 24 crew members
remained safe. The incident represents a dangerous shift in targeting doctrine. For three weeks, Iranian operations focused on vessels transiting the Strait of Hormuz and Gulf shipping lanes. This
anchorage strike demonstrates Iran's willingness to extend its reach into what traders viewed as relatively secure zones. Dubai Port is one of the world's busiest,   ...    Oil Price Implications:
Brent crude surged past $115 per barrel on the news, with analysts warning a sustained blockade   ...    report margins tightening as shipping costs spike and fuel surcharges kick in. Asia,
particularly India, faces acute exposure: Indian refiners depend on Gulf crude, yet their navy-flagged fleet remains stranded (18 vessels, 485 seafarers reported stuck in Hormuz as of Monday).
Insurance & P&I Exposure: The strike widens P&I club exposure in several ways. First, the vessel was fully laden at anchor, maximizing pollution liability if the hull had breached. Second, war risk
premiums in the region are now   ...    Crew Safety & Repatriation: The 24 crew were evacuated safely, but the broader seafarer crisis is acute. Indian and Thai crews remain stranded on 500 vessels
locked in the Gulf. The Mayuree Naree, struck on March 11, still has three   ...    dislocation. Operational Pattern: This strike marks the 32nd confirmed maritime incident in Operation Epic Fury.
Unlike earlier attacks concentrated on in-transit vessels, this one exploited a commercial chokepoint: the anchorage zone where tankers stage before discharge or waiting for canal slots. If
replicated, it forces port operators to reroute vessels   ...    Longer Game: The UAE has launched a 1 billion dirham economic stimulus (fee deferrals, customs extensions), signaling concern about
prolonged disruption. But economic triage cannot substitute for open shipping lanes. As long as Iran maintains tactical capability in Hormuz, the risk premium stays embedded in every barrel.   ...
AI-Assisted \u00b7 Human Verified\n\nFlag Inaccuracy\n\n# hormuz# iran-war# oil-tanker# dubai-anchorage# war-risk ## \ud83d\udcf0 Related Analysis\n\n### Kharg Island Becomes the New Lever in the
Hormuz Standoff EnergyTrump administration publicly considers occupying or blockading Kharg Island to pressure Iran into reopening Strait of Hormuz; island handles 90% of Iranian oil exports and
represents IRGC's economic lifeline.Mar 21, 2026 ### The Oil Shock Countdown: Why Early April Is the Economic Deadline for Hormuz Reopening EnergyEnergy analysts warn Hormuz must reopen within 1-3
weeks or SPR depletion will exhaust stopgap measures, triggering sharp oil/LNG price spike. Brent could reach $130+; inflation and recession risks escalate by early April.Mar 30, 2026 ### LNG Price
Shock Accelerates: Japan and Korea Face 48% Surge as Oil Cliff Looms in April; Industry Warns Physical   ...    EnergyLiquified natural gas prices in Japan and Korea surge 48% amid Hormuz closure; oil
industry executives warn mid-April physical supply cliff when strategic reserves and sanctions exemptions deplete.Mar 29, 2026 ### Europe's Energy Crisis Deepens: LNG Prices Spike 72% Since Early
March as Hormuz Closure Triggers Liquefaction   ...    EnergyLNG prices surge 72% since March 1; Hormuz blockade prevents gas carriers from accessing Persian Gulf export routes, forcing Qatar"],
"published_date": "2026-03-31T09:36:02.000", "score": null}, {"title": "A Bad Day for Merchant Mariners in the Strait of Hormuz", "url": "https://www.youtube.com/watch?v=sXNHYWyRAl0", "snippet": "# A
Bad Day for Merchant Mariners in the Strait of Hormuz | March 11, 2026\n\n- Channel: What's Going on With Shipping?\n- Length: 18:42\n- Views: 699.2K\n- Language: en\n\n## Description\n\nMarch 11,
2026, proved a bad day for merchant mariners with three attacks on ships - one in the Strait of Hormuz that led to three mariners going missing and the crew having to abandon their ship, which was on
fire. There were two other attacks inside the Persian Gulf, and all seem to be victims of unmanned surface v", "highlights": ["A Bad Day for Merchant Mariners in the Strait of Hormuz | March 11, 2026
...    March 11, 2026, proved a bad day for merchant mariners with three attacks on ships - one in the Strait of Hormuz that led to three mariners going missing and the crew having to abandon their
ship, which was on fire. There were two other attacks inside the Persian Gulf, and all seem to be victims of unmanned surface vessels. There was also an attack on the port of Sallah, Oman and tankers
are shifting to the port of Yanbu in the Red Sea.   ...    Behind Closed Doors, U.S. Navy Says Hormuz Escorts Are Too Dangerous\u2014for Now   ...    Maritime Attacks Reach 13 in First 12 Days of
Middle East Conflict   ...    Port of Salalah attacked and operations suspended   ...    Red Sea tanker loadings rise as Aramco ramps up pipeline contingency   ...    Fallout will ripple across globe
amid Strait of Hormuz \u2018doomsday scenario\u2019 https://www.lloydslist.com/LL1156575/Fallout-will-ripple-across-globe-amid-Strait-of-Hormuz-doomsday-scenario Maersk Says Hormuz Crisis is Squeezing
Global Marine Fuel Supply https://gcaptain.com/maersk-says-hormuz-crisis-is-squeezing-global-marine-fuel-supply/   ...    Shadow tankers divert to India after US green lights Russia imports   ...
## Transcript on this the March 11th 2026 edition of what's going on with shipping. It was a bad day in the straight of Hormuz. I'm your host Sal Maglano. Welcome to today's episode. So a bad day in
that a bull carrier Thailand flagged outbound was struck by an unmanned surface vessel. Three crew members reported missing. We had two other ships in the Persian Gulf   ...    We're going to update
you on everything going on in and around the straight of Hormuz, the Persian Gulf, and the Gulf of Oman. If you're new to the channel, hey, take a moment, subscribe to the channel, and hit the bell so
be alerted   ...    it. So, here are the three vessels that were attacked within the past 24 hours. Oe Majesty, a container ship laden uh was underway and had departed in the incident area. It was hit
by a projectile. Minor damage to the ships about 50   ...    by an unknown projectile. Crew is safe and the vessel remains float. Also 70 mi northwest of Dubai, we have this story of multiple fuel
storage tanks at the port of Salala in Oman were struck by uncrrewed aerial systems. We have some very dramatic imagery of that. So the average historical transits through the straight of Hormuz on a
daily basis 138. On   ...    bit here with seven. So chart on the left shows you the frequency of attacks with high percentage of attacks taking place in and around the straight. But you will see that
attacks have taken all the way up the Persian Gulf to right off the coast of Kuwait along the coast of Saudi Arabia around the major oil terminals at Rastanora and El Jale and then even out into the
Gulf of Oman. And in particular, we're still seeing massive amounts of spoofing in AIS throughout this region. It's causing a lot of   ...    joint war committee expansion of the listed areas across
the Arabian Gulf, Gulf of Oman, adjacent waters continues to   ...    attacks. That's what's keeping the ships locked in right now. So this is the outlook over the next 24 28 hours. Everything remains
critical. Offshore energy infrastructure and select port areas remain exposed.   ...    style of attacks, global navigation system interference, AIS anomalies, and communication disruption. The
Straight of Hormuz traffic is expected to remain heavily suppressed in the near term. Any vessel transiting the   ...    see later on in the report. So, the big issue, as we've talked about, is
insurance has been largely settled.   ...    at G Captain. Behind closed doors, the US Navy says Hormuz escorts are too dangerous for now. So that Navy's assessment spell continued disruptions to the
Middle East oil exports and reflect a divergence from President Donald Trump's   ...    Now, Saudi Arabia's Aramco, the world's top oil exporter, said on Tuesday, \"There would be catastrophic
consequences for the world's oil market if the war in Iran continues to disrupt shipping in the straight of Hormuz.\" Goes on here,   ...    that came out today about the attacks on shipping. Mike
Schuller over at G Captain. Three additional commercial ships have been struck by projectiles in and around the  straight of Hormuz over the past 24 hours as the maritime security situation in the
region continues to deteriorate amid the escalating US-Israeli conflict. Adding to the latest advisory from the joint maritime information center, the attacks involved the container ship OE Majesty
and the bulk carriers   ...    standoff kinetic threats. The latest attacks bring the total number of confirmed  vessel strikes in the region to 13. Meanwhile, the number of seafarer fatalities has
reached seven according to the UN International Maritime Organization. and the maritime threat environment across the Arabian Gulf straight of Hormuz in Gulf of Oman remains at critical. So at times
this channel can be very abstract and kind of big high ranging looking at global shipping and really taking   ...    there. Uh that that whatever  Quick reminder, the last ship that got hit like that
in the Straight of Hormuz.  That's   ...    wounding three others. SenCom has issued a statement on Tuesday"], "published_date": "2026-03-14T13:41:09.164", "score": null}]
```

## 💭 Thinking

The CNN-News18 video title "1.2 MILLION BARRELS LOST: 300m Empire Tanker Struck Near Hormuz" appears to be clickbait. When I look at the actual transcript, it's discussing the Al-Salmi tanker (the Kuwaiti VLCC) which was confirmed to have NO oil leakage. The "Empire" tanker mentioned in the title seems to be a click-bait reference or confusion.

However, looking more carefully, the video description mentions "Empire oil tanker strike" and "Empire Navigation ship news" as keywords separately from the Al-Salmi. 

I need to dig deeper into whether there's actually a separate Empire vessel incident, or if this is just sensationalized naming. I'm also noticing references to other recent attacks in the region—there's a QatarEnergy tanker hit by missile attack mentioned in the related results from April 2026. Looking at the broader pattern of incidents, particularly the recent ones, I'm finding that while there have been multiple tanker strikes in the Gulf of Oman, no confirmed large-scale oil spill has actually resulted from any of these conflict-related attacks, despite the alarming headlines. The video transcript actually discusses the Al-Salmi incident, which multiple authoritative sources confirm had no oil leakage, so the "Empire" tanker title appears to be clickbait. I should check for any very recent April attacks that might have caused a significant spill, especially since the question resolves on May 1st and we're only at April 4th now.

Looking at what's actually happened so far: despite over a month of intense maritime attacks with drones and projectiles, no confirmed spill exceeding 50,000 barrels has been reported. Modern double-hulled tankers are fairly resilient to this type of damage, and the dramatic drop in traffic means fewer laden tankers are in the area as targets. The Gulf of Oman specifically has seen fewer attacks than other parts of the region, and hitting the 50,000 barrel threshold would require a catastrophic breach—that's an extremely high bar to clear in the remaining 27 days.

Now I'm realizing ITOPF explicitly excludes war-related incidents from their database, but the question allows for reporting from UNEP, NOAA, or other credible sources, so even if ITOPF doesn't track it, military authorities or other organizations could still document a major spill if one occurs. This shifts where the evidence would come from rather than whether it would be recorded at all.

Weighing the scenarios: there's active conflict with numerous laden tankers in the region and Iran's demonstrated willingness to target vessels, but 35+ days of attacks have produced zero confirmed large spills despite 22+ vessel incidents. Modern double-hulled tankers are remarkably resilient, most attacks use drones or projectiles too small to breach hulls, and the question's specific geographic requirement of the Gulf of Oman excludes many of the actual attack locations. The 50,000-barrel threshold is also quite high. I'm settling on roughly 10-15% for YES given the ongoing risk, but the historical pattern of attacks without major environmental damage and the structural resilience of modern tankers makes NO significantly more likely at 85-90%.

Now I'm reconsidering that "Empire tanker" claim—if a Suezmax with 1.2 million barrels was actually sinking, every major news outlet would be covering it, not just a YouTube video title. The fact that I can only find this in clickbait suggests it's not credible. The vessel capacity figures also don't quite match up with what's being claimed, and the video transcript actually discusses the Al-Salmi, which had no spill at all.

So I'm settling on around 8% probability for a major tanker spill from this conflict.

## 💬 Response

Now I have a comprehensive picture. Let me check for any very recent April developments and the QatarEnergy tanker attack.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "QatarEnergy tanker missile attack April 2026 oil spill"
}
```

### 📋 Result

```
{"query": "QatarEnergy tanker missile attack April 2026 oil spill", "results": [{"title": "QatarEnergy confirms oil tanker hit by missiles in Gulf waters - BusinessToday", "url":
"https://www.businesstoday.in/world/story/qatarenergy-confirms-oil-tanker-hit-by-missiles-in-gulf-waters-523504-2026-04-01", "snippet": "![QatarEnergy confirms oil tanker hit by missiles in Gulf
waters QatarEnergy confirms oil tanker hit by missiles in Gulf waters](https://akm-img-a-in.tosshub.com/businesstoday/images/story/202604/69cccf8b9681b-missile-attack-hits-qatarenergy-tanker-
represenational-image-015549904-16x9.png?size=948:533)\nA fuel oil tanker chartered by QatarEnergy was hit by a missile in Qatar's northern territorial waters early on Wednesday, the company said. The
vessel, Aqua 1, was struck in the early hours of Ap", "api_data": null, "hint": null}, {"title": "Missile Hits Oil Tanker Leased to QatarEnergy | Rigzone", "url":
"https://www.rigzone.com/news/missile_hits_oil_tanker_leased_to_qatarenergy-02-apr-2026-183355-article/", "snippet": "Missile Hits Oil Tanker Leased to QatarEnergy\n[Jov
Onsat](https://www.rigzone.com/news/Author/82/JovOnsat/ )\n![Missile Hits Oil Tanker Leased to QatarEnergy](https://images.rigzone.com/images/news/articles/Missile-Hits-Oil-Tanker-Leased-to-
QatarEnergy-183355-582x327.webp)\nQatarEnergy said Wednesday a missile had hit the Aqua 1 fuel oil tanker, chartered to the state-owned energy company, in the \"early morning hours\".\n\"None of the
crew members on board were injured, and there is no impact on the ", "api_data": null, "hint": null}, {"title": "Iran\u2019s Missile Strike on Qatar-Leased Tanker Deepens Gulf Crisis and Raises Global
Energy Fears", "url": "https://yournews.com/2026/04/01/6750599/irans-missile-strike-on-qatar-leased-tanker-deepens-gulf-crisis-and/", "snippet": "By Elsie Kamsiyochi\nA fuel oil tanker leased by
state-owned QatarEnergy was struck by an Iranian cruise missile on Wednesday, Qatar\u2019s defence ministry confirmed, in what officials are calling one of the most alarming escalations to date in the
rapidly intensifying regional conflict involving the United States, Israel and Iran.\nAccording to a detailed statement from Qatari authorities, three cruise missiles were launched from Iranian
territory toward Qatari waters in the early hours of the mornin", "api_data": null, "hint": null}, {"title": "LIVE UPDATES: Qatar intercepts missiles, one hits QatarEnergy oil tanker | The Peninsula
Qatar", "url": "http://thepeninsulaqatar.com/article/01/04/2026/live-updates-qatar-intercepts-missiles-one-hits-qatarenergy-oil-tanker", "snippet": "Doha, Qatar: Qatar's Defence Ministry confirmed
that three cruise missiles were launched from Iran with the armed forces intercepting two, while one hit an oil tanker in the country's territorial waters.\nStay tuned for more
updates\n----------------------------------\n7:29pm Doha Time\nKuwait Interior Ministry handles 13 reports of debris from defensive interceptions\nKuwait's Ministry of Interior announced that
explosive ordnance disposal teams responded to 13 reports involving debris resulting fro", "api_data": null, "hint": null}, {"title": "QatarEnergy statement on missile attack on oil tanker | The
Peninsula Qatar", "url": "https://thepeninsulaqatar.com/article/01/04/2026/qatarenergy-statement-on-missile-attack-on-oil-tanker", "snippet": "Doha, Qatar: QatarEnergy confirmed that the Aqua 1, a
fuel oil tanker chartered to QatarEnergy, was the subject of a missile attack in the territorial waters of the State of Qatar in the early morning hours of Wednesday, April 1, 2026.\nNone of the crew
members on board were injured, and there is no impact on the environment as a result of this incident.\nThis comes following an announcement by the Ministry of Defence stating that Qatar was targeted
by three cruise missiles launched from Iran.\nIt ", "api_data": null, "hint": null}, {"title": "Fuel oil tanker on charter to QatarEnergy targeted in missile attack| Gulf Times", "url":
"https://www.gulf-times.com/article/723200/qatar/fuel-oil-tanker-on-charter-to-qatarenergy-targeted-in-missile-attack/amp", "snippet": "[Qatar](https://www.gulf-times.com/qatar)\nFuel oil tanker on
charter to QatarEnergy targeted in missile attack\nApril 01, 2026 | 10:47 AM\nQatarEnergy confirms that the Aqua 1, a fuel oil tanker on charter to QatarEnergy, has been the subject of a missile
attack in the northern territorial waters of the State of Qatar in the early morning hours of Wednesday.None of the crew members on board were injured, and there is no impact on the environment as a
result of this incident, QatarEnergy confirmed ", "api_data": null, "hint": null}, {"title": "QATARENERGY announced that a missile attack was carried out on a fuel oil tanker - Pravda Turkey", "url":
"https://turkey.news-pravda.com/en/turkey/2026/04/01/79986.html", "snippet": "QATARENERGY announced that a missile attack was carried out on a fuel oil tanker\nQATARENERGY announced that a missile
attack was carried out on a fuel oil tanker\nThe statement said the tanker was 'subjected to a missile attack in the northern territorial waters of the state of Qatar in the early morning hours of
Wednesday, April 1, 2026'.\nIt was stated that the crew members on board were not injured and there was no impact on the environment.", "api_data": null, "hint": null}, {"title": "Iran strikes tanker
off Qatar coast as Tehran's attacks on Gulf states persist | Euronews", "url": "https://www.euronews.com/2026/04/01/iran-strikes-tanker-off-qatar-coast-as-tehrans-attacks-on-gulf-states-persist",
"snippet": "[Aadel Haleem](https://www.euronews.com/profiles/3539)\n[Comments](https://www.euronews.com#vuukle-comments-2882962)\nQatar said it had intercepted two Iranian cruise missiles, while a
third struck a fuel tanker off its coast. All 21 crew members were safely evacuated, with no injuries or environmental damage reported.\nA cruise missile struck an oil tanker off the coast of Qatar
early Wednesday after Iran launched three missiles toward the country, according to the Qatari Ministry of Defence.\nAir ", "api_data": null, "hint": null}, {"title": "Qatari-leased fuel oil tanker
targeted in missile attack: QatarEnergy - Read Qatar Tribune on the go for unrivalled news coverage", "url": "https://www.qatar-tribune.com/article/226784/latest-news/qatari-leased-fuel-oil-tanker-
targeted-in-missile-attack-qatarenergy", "snippet": "+ A\nA -\nDOHA: QatarEnergy announced that the tanker Aqua 1, a fuel oil tanker leased by QatarEnergy, was targeted by a missile attack this
morning in Qatari territorial waters north of the country.\nQatarEnergy confirmed in a statement that none of the tanker's crew members were injured and that the attack caused no environmental
damage.", "api_data": null, "hint": null}, {"title": "Iran Escalates Gulf Conflict: Drone Strike Hits Kuwait Airport, Missile Strikes QatarEnergy Tanker", "url": "https://www.pingtvindia.com/iran-
drone-missile-attacks-kuwait-qatar-gulf-escalation-2026/", "snippet": "DUBAI, April 1, 2026 \u2013 Regional stability in the Middle East faced a fresh crisis on Wednesday as Iranian forces launched
coordinated strikes against key energy and aviation infrastructure in Kuwait and Qatar. The attacks mark a significant expansion of the ongoing friction between Tehran and the US-Israel
coalition.\nKuwait International Airport Fuel Tanks Ignited\nEarly Wednesday morning, an Iranian-launched drone successfully targeted fuel storage facilities at [Kuwait International Airport](ht",
"api_data": null, "hint": null}]}
```

```json
{
  "query": "tanker attack April 2 3 4 2026 Gulf Oman Hormuz oil spill"
}
```

### 📋 Result

```
{"query": "tanker attack April 2 3 4 2026 Gulf Oman Hormuz oil spill", "results": [{"title": "Another oil tanker hit by drone boat as Strait of Hormuz tensions rise | Euronews", "url":
"https://www.euronews.com/business/2026/03/02/another-oil-tanker-hit-by-drone-boat-as-strait-of-hormuz-tensions-rise", "snippet": "[Comments](https://www.euronews.com#vuukle-comments-2875186)\nAn oil
tanker has been struck near the Strait of Hormuz, marking another attack in the area that triggered an explosion and left one crew member dead.\nAn oil tanker flying the flag of the Republic of the
Marshall Islands was attacked by a drone boat 52 nautical miles (96.3km) off the coast of Muscat, according to Oman\u2019s Maritime Security Centre (MSC).\nThe vessel, named MKD VYOM, was carrying
approximately 59,463 metric tonnes of cargo ", "api_data": null, "hint": null}, {"title": "Tankers Struck Near Gulf as Hormuz Traffic All But Halted - Bloomberg", "url":
"https://www.bloomberg.com/news/articles/2026-03-01/oman-says-oil-tanker-targeted-off-its-north-coast", "snippet": null, "api_data": null, "hint": null}, {"title": "2026 Strait of Hormuz crisis -
Wikipedia", "url": "https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis", "snippet": "The Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing
geopolitical and economic disruption since 28 February 2026, following joint military strikes by the United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei.
In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings
prohibiti", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 Strait of Hormuz crisis\", \"url\": \"https://en.wikipedia.org/wiki/2026_Strait_of_Hormuz_crisis\", \"extract\": \"The
Strait of Hormuz, a major maritime choke point for global energy trade, has experienced ongoing geopolitical and economic disruption since 28 February 2026, following joint military strikes by the
United States and Israel on Iran, which included the killing of Iran's supreme leader Ali Khamenei. In response, Iran launched retaliatory missile and drone attacks on US military bases, Israeli
territory, and Gulf states, while its Islamic Revolutionary Guard Corps (IRGC) issued warnings prohibiting vessel passage through the strait, leading to an effective halt in shipping traffic. US
President Donald Trump announced his intent to seize control of the Strait of Hormuz on 9 March and later warned Iran to not lay mines in the body of water. On 19 March 2026, the United States Armed
Forces began a military campaign to open the strait.\\nAs of 12 March 2026, Iran has made 21 confirmed attacks on merchant ships. The warnings and subsequent attacks on vessels caused a sharp decline
in maritime transit, with tanker traffic dropping first by approximately 70% and over 150 ships anchoring outside the strait to avoid risks. Soon afterwards traffic dropped to about zero. This
disruption affected about 20% of the world's daily oil supply and significant volumes of liquefied natural gas (LNG), prompting major shipping firms to suspend operations in the area. On 27 March, the
IRGC announced that the strait is closed to any vessel going \\\"to and from\\\" the ports of the US, Israel, and their allies.\\nAmid fears of prolonged supply shortages, oil prices surged faster
than during any other conflict in recent history; Brent crude oil prices surpassed US$100 per barrel on 8 March 2026 for the first time in four years, rising to US$126 per barrel at its peak. The
closure of the strait has been described as the largest disruption to the energy supply since the 1970s energy crisis, as well as the largest in the history of the global oil market. Other commodity
markets to suffer price increases from the crisis include aluminum, fertilizer, and helium.\\nIran's closure of the strait of Hormuz constitutes a violation of the UN Convention on the Law of the Sea
by denying transit in a strait used for international navigation.\\n\\n\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Black smoke pours from oil tanker near Strait of Hormuz | US-Israel war on
Iran | Al Jazeera", "url": "https://www.aljazeera.com/video/newsfeed/2026/3/1/black-smoke-pours-from-oil-tanker-near-strait-of-hormuz", "snippet": "![Smoke billows from an oil tanker under U.S.
sanctions, that was hit off Oman's Musandam peninsula, in this screen grab from a video obtained by Reuters on March 1, 2026. [Reuters]](/wp-
content/uploads/2026/03/oil_tanker_strait_of_hormuz_oman_hit_projectile-1772386633.jpg?resize=730%2C410&quality=80)\nBlack smoke pours from oil tanker in Strait of
Hormuz\n[NewsFeed](https://www.aljazeera.com/video/newsfeed/)\nBlack smoke pours from oil tanker near Strait of Hormuz\nFootage from near the Strait of H", "api_data": null, "hint": null}, {"title":
"Iran War Confirmed Vessel Attacks and Maritime Infrastructure Strikes", "url": "https://windward.ai/blog/iran-war-vessel-attacks-and-maritime-infrastructure-strikes/", "snippet": "[April 2, 2026:
Iran War Maritime Intelligence Daily](https://windward.ai/blog/april-2-maritime-intelligence-daily/)\nNumber of confirmed incidents: 32 (22 vessels and 10 oil, gas, and port facilities).\nSince the
start of the Iran war, [maritime security](https://windward.ai/glossary/what-is-maritime-security/) incidents have expanded across the commercial operating environment, affecting vessels at anchor, in
transit, in drydock, and during [ship-to-ship operations](https://windward.ai/glossary/", "api_data": null, "hint": null}, {"title": "Why it's so hard to get oil through the Strait of Hormuz right
now", "url": "https://www.nbcnews.com/world/iran/strait-of-hormuz-closure-shipping-oil-strikes-rcna262898", "snippet": "Three ships were attacked [in the Strait of
Hormuz](https://www.nbcnews.com/news/us-news/us-destroys-mine-laying-ships-strait-hormuz-audacious-plan-refill-grea-rcna262885) on Wednesday, a British navy-run monitoring service said, the latest in
a flurry of attacks on the vital oil choke point.\nAs Iran targets ships with missiles and drones, even attempting to navigate [the strategic waterway](https://www.nbcnews.com/world/iran/live-
blog/live-updates-iran-war-israel-us-lebanon-tehran-oil-prices-ho", "api_data": null, "hint": null}, {"title": "Three more ships struck in the Persian Gulf as Iran warns of oil prices hitting $200",
"url": "https://www.cnbc.com/2026/03/12/iran-war-persian-gulf-strait-of-hormuz-ships-uae-iraq.html", "snippet": "Three more foreign ships were struck in the Persian Gulf overnight, authorities said,
as attacks intensify on vessels sailing through or near the [strategically vital Strait of Hormuz](https://www.cnbc.com/2026/03/11/strait-of-hormuz-closure-shipping-economy-oil.html).\nThe latest
incidents come after [three separate vessels](https://www.cnbc.com/2026/03/11/cargo-ship-struck-strait-of-hormuz-uk-iran-war.html) sustained damage in Gulf waters on Wednesday and as Iran warns oil
prices could climb to", "api_data": null, "hint": null}, {"title": "Tanker \u2018Skylight\u2019 struck as Strait of Hormuz shipping threat intensifies amid fresh regional strikes | CNN", "url":
"https://www.cnn.com/2026/03/02/world/video/tanker-skylight-struck-hormuz-oman-hnk-digvid", "snippet":
"![16x9_LOOP.00_00_06_18.Still005.jpg](https://media.cnn.com/api/v1/images/stellar/prod/16x9-loop-00-00-06-18-still005.jpg?c=16x9&q=w_1280,c_fill)\nVideo Ad Feedback\nTanker \u2018Skylight\u2019
struck as Strait of Hormuz shipping threat intensifies amid fresh regional strikes\nThe vital waterway faces mounting disruption after German shipping giant Hapag\u2011Lloyd halts transits, an oil
tanker \u201cSkylight\u201d was attacked off Oman, and Iran reports a vessel sinking following an \u201cunauthorized passage.\u201d Maritime author", "api_data": null, "hint": null}, {"title": "Which
oil and gas facilities in the Gulf have been attacked? | Infographic News | Al Jazeera", "url": "https://www.aljazeera.com/news/2026/3/4/which-oil-and-gas-facilities-in-the-gulf-have-been-attacked",
"snippet": "Which oil and gas facilities in the Gulf have been attacked?\nDamage to several energy facilities has caused global prices to spike, but Iran denies it is targeting energy
sites.\n![INTERACTIVE_IRAN_GCC_OIL AND GAS SUPPLY-OUTSIDE IMAGE](/wp-content/uploads/2026/03/INTERACTIVE_IRAN_GCC_OIL-AND-GAS-SUPPLY-06-1772630810.png?resize=770%2C513&quality=80)\nGlobal energy
markets remain in a state of high alert after several Gulf states suspended oil and gas production following escalating tensions in the ", "api_data": null, "hint": null}, {"title": "How oil tankers
stuck in the Strait of Hormuz south of Iran threatens the Gulf ecosystem - Greenpeace International", "url": "https://www.greenpeace.org/international/story/81999/hormuz-oil-tanker-leak-iran/",
"snippet": "More than 85 large oil tankers are [currently trapped in the Persian Gulf](https://www.greenpeace.org/international/press-release/82052/greenpeace-disaster-oil-tankers-in-persian-gulf/).
The reason: following attacks launched on Iran by Israel and the United States on 28 February, Iran has restricted access to the strategically important Hormuz Strait. Ongoing hostilities and
disrupted vessel position signals dramatically [increase the risk of oil spills](https://edition.cnn.com/2026/03/13/world", "api_data": null, "hint": null}]}
```

## 💭 Thinking

OK, so the QatarEnergy Aqua 1 tanker was hit by a missile on April 1 in Qatar's territorial waters (northern Qatar), with NO environmental impact, no injuries. This is in the Persian Gulf, NOT the Gulf of Oman.

Let me now compile all my findings and do the reflection.

Summary of all confirmed tanker/vessel attacks with spill assessment:

1. **Skylight** (March 1): Struck at anchor, Strait of Hormuz off Musandam - fire, crew evacuated - NO major spill reported


2. **Hercules Star** (March 1): Struck during transit - fire, returned to Dubai - NO spill
3. **Ocean Electra**: Near miss - no damage
4. **MKD VYOM** (March 2): Struck by USV 52nm off Muscat (Gulf of Oman) - fire, 1 fatality, towed - carrying 59,463 tonnes. NO major spill confirmed
5. **Stena Imperative**: At port of Bahrain - fire - NO spill
6. **Pelagia** (March 3): Gulf of Oman - UAV near miss - no damage
7. **Gold Oak** (March 3): Gulf of Oman - structural damage - NO spill

Now I'm going through the remaining incidents to complete the full accounting of all vessel strikes and their environmental outcomes. attacks: Express Rome near-miss, etc.

Key conclusion: **NO single conflict-related spill exceeding 50,000 barrels has been confirmed in the Gulf of Oman.**

Now for the forward-looking assessment:

The remaining time window is ~27 days (April 4 to May 1). 

Factors pushing toward YES:
- Active conflict continuing, possibly escalating
- Hundreds of ships trapped/anchored in the region
- Iran using increasingly powerful weapons (cruise missiles)
- US military operations to open strait could trigger new attacks
- Trump threatening to escalate
- Mines may be present
- If US tries to push convoys through, those laden tankers become targets in narrow waters

Factors pushing toward NO:
- 35 days of conflict, 22+ attacks, zero large spills - strong empirical evidence
- Modern double-hulled tankers are remarkably resilient
- Most attacks have caused minimal environmental damage despite direct hits

So I'm weighing the escalation risks over the next month against the empirical track record showing that even direct strikes on major tankers haven't produced significant spills. The conflict is clearly intensifying and there are more opportunities for a catastrophic hit, but the resilience of modern vessels and the fact that nothing major has leaked yet despite dozens of incidents suggests the bar for a 50,000+ barrel spill is quite high.

Looking at historical precedent from the 1980s tanker war, massive individual spills were surprisingly uncommon even across hundreds of attacks over years. Given what we've seen so far, I'm settling on roughly 8-10% probability for the remaining window.

## 💬 Response

Now I have all the data I need. Let me synthesize and run the reflection.
