# Reasoning Log: How many U.S. metropolitan areas will have Tesla robotaxi service on August 31, 2026?

*Generated: 2026-07-21T00:13:50.929064+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "What US metropolitan areas currently have Tesla Robotaxi service as of July 2026? List the metro areas with 'Full commercial service' or 'Safety-driver service' status on the Wikipedia 'Tesla Robotaxi' Service areas in the United States table. Include recent expansion news and announced expansion plans for summer 2026.",
  "ttl": "6h"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': "What US metrop...mer 2026.", 'ttl': '6h'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi",
  "prompt": "List all US metropolitan areas in the \"Service areas in the United States\" table, along with each area's service status (Full commercial service, Safety-driver service, or other). Count how many have Full commercial service or Safety-driver service."
}
```

### 📋 Result

```
{"title": "Tesla Robotaxi", "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "extract": "Tesla Robotaxi is a ride-hailing service operated by Tesla, Inc. that uses its vehicles equipped with its
Full Self-Driving (FSD) software. The service launched in a limited capacity in Austin, Texas, on June 22, 2025 and currently operates in Texas in Austin, Dallas and Houston, and in Miami,
Florida.\nThe service represents a key part of Tesla CEO Elon Musk's long-term strategy for the company, which envisions a future where Tesla owners can add their personal vehicles to a shared
autonomous ride-hailing network. The launch in Austin initially operated with a human \"safety monitor\" in the front passenger seat. The launch attracted significant media attention and scrutiny,
with early riders documenting incidents such as the vehicle driving on the wrong side of the road, phantom braking, dropping passengers off in intersections and committing traffic violations that led
to an investigation by the National Highway Traffic Safety Administration.\nTesla plans to have the Robotaxi network work with all current Tesla vehicles, but as of May 2026, the network is composed
of only Model Y vehicles. Tesla plans to add the Cybercab when it begins volume production in mid-2026 with the Model 3, Model S, Model X, and Cybertruck later. During Tesla's October 2024 We, Robot
event it also demonstrated the Robovan which it plans to add to the network, but no timelines were given.", "mode": "full"}
```

## 💭 Thinking



## 🔧 Tool: mcp__research__research


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "questions": [
    {
      "query": "What US metropolitan areas currently have Tesla Robotaxi service as of July 2026? List the metro areas with 'Full commercial service' or 'Safety-driver service' status on the Wikipedia 'Tesla Robotaxi' Service areas in the United States table. Include recent expansion news and announced expansion plans for summer 2026.",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "What US metropolitan areas currently have Tesla Robotaxi service as of July 2026? List the metro areas with 'Full commercial service' or 'Safety-driver service' status on the
Wikipedia 'Tesla Robotaxi' Service areas in the United States table. Include recent expansion news and announced expansion plans for summer 2026.", "entry": {"slug": "what-us-metropolitan-areas-
currently-have-tesla-ro-52414982", "query": "What US metropolitan areas currently have Tesla Robotaxi service as of July 2026? List the metro areas with 'Full commercial service' or 'Safety-driver
service' status on the Wikipedia 'Tesla Robotaxi' Service areas in the United States table. Include recent expansion news and announced expansion plans for summer 2026.", "answer": "I've completed the
research. Here's a summary of the key findings:\n\n## Tesla Robotaxi US Service Areas (as of July 2026)\n\n### Metros with the two requested Wikipedia status labels\n\n**Full commercial service
(unsupervised \u2014 no safety driver):**\n1. **Austin, TX** \u2014 Nov 18, 2025 (launched June 22, 2025 with safety monitor; entire metro coverage as of June 3, 2026)\n2. **Dallas, TX** \u2014 April
18, 2026\n3. **Houston, TX** \u2014 April 18, 2026\n4. **Miami, FL** \u2014 July 3, 2026 (first Florida market)\n\n**Safety-driver service:**\n5. **San Francisco Bay Area, CA** \u2014 human safety
driver required due to California DMV permit rules (no driverless deployment permit)\n\n*(Phoenix, Orlando, Tampa, and Las Vegas appear in the table only as \"Service announced / 1H 2026\" \u2014 not
yet in either requested status.)*\n\n### Expansion news & announced plans\n- **Jan 28, 2026 earnings call:** Tesla confirmed 7-city H1 2026 expansion (Dallas, Houston, Phoenix, Miami, Orlando, Tampa,
Las Vegas); ~700,000 paid miles logged.\n- **April 2026:** Dallas & Houston went unsupervised \u2014 first expansion beyond Austin/Bay Area.\n- **June 3, 2026:** Austin expanded to entire metro (~245
sq mi, 12x growth).\n- **July 3, 2026:** Miami launched (city #4).\n- **Summer/2H 2026 pipeline:** Phoenix, Orlando, Tampa, Las Vegas \"on deck\"; New Orleans cited by Morgan Stanley as a possible
year-end market. Musk projected a \"widespread\" US network by end of 2026, though skeptical reporting (Electrek, Feb 2026) noted only ~42 Austin cars and sub-20% availability.\n\nThe full report,
structured data points, and all sources have been recorded via the StructuredOutput tool.", "sources": [{"url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "title": "Tesla Robotaxi", "domain":
"en.wikipedia.org", "accessed_at": "2026-07-21", "snippet": "Service areas in the US table: Austin/Dallas/Houston/Miami Full commercial service; SF Bay Area Safety-driver service;
Phoenix/Orlando/Tampa/Las Vegas Service announced 1H 2026."}, {"url": "https://www.evbase.com/blogs/ev-news/tesla-robotaxi-service-reaches-five-cities", "title": "Tesla Robotaxi Service Reaches Five
Cities", "domain": "evbase.com", "accessed_at": "2026-07-21", "snippet": "Tesla operates in five metros: Austin, Dallas, Houston, Miami (unsupervised), and SF Bay Area (safety monitor required due to
CA DMV permit)."}, {"url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/", "title": "Tesla confirms Robotaxi expansion plans with new cities and
aggressive timeline", "domain": "teslarati.com", "accessed_at": "2026-07-21", "snippet": "Tesla plans to launch in Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas in H1 2026; Bay Area
'Safety Driver', Austin 'Ramping Unsupervised'; ~700,000 paid miles."}, {"url": "https://eletric-vehicles.com/tesla/tesla-launches-unsupervised-robotaxi-in-dallas-and-houston/", "title": "Tesla
Launches Unsupervised Robotaxi in Dallas and Houston", "domain": "eletric-vehicles.com", "accessed_at": "2026-07-21", "snippet": "Tesla began offering unsupervised rides in Dallas and Houston, first
expansion beyond Austin and the SF Bay Area, days before Q1 2026 earnings (April 22)."}, {"url": "https://www.learnmyev.com/post/tesla-robotaxi-miami-launch-2026", "title": "Tesla Robotaxi Just
Launched in Miami \u2014 City #4 Goes Live", "domain": "learnmyev.com", "accessed_at": "2026-07-21", "snippet": "As of July 3, 2026, Tesla's autonomous service is live in Miami \u2014 4th US
commercial market and first in Florida."}, {"url": "https://electrek.co/2026/07/03/tesla-robotaxi-miami-service-area-map/", "title": "Tesla maps a tiny Robotaxi zone in Miami while it still can't
scale Texas", "domain": "electrek.co", "accessed_at": "2026-07-21", "snippet": "Tesla mapped a Miami geofence covering only a small slice of the metro \u2014 mostly West Miami toward Doral and
Sweetwater."}, {"url": "https://www.teslaoracle.com/2026/06/08/tesla-expands-unsupervised-robotaxi-service-to-the-entire-austin-metro-area-cybercabs-spotted-across-the-us/", "title": "Tesla expands
Unsupervised Robotaxi Service to the entire Austin Metro Area", "domain": "teslaoracle.com", "accessed_at": "2026-07-21", "snippet": "Tesla expanded to the entire Austin Metropolitan Area after
gradual extensions since launch."}, {"url": "https://tslna.com/en/tesla-robotaxi-guide/", "title": "Tesla Robotaxi in Austin 2026: How to Ride, Cost & the Real Story", "domain": "tslna.com",
"accessed_at": "2026-07-21", "snippet": "On June 3, 2026 Tesla opened driverless service across nearly all of Austin (~245 sq mi), a 12x expansion from the ~20 sq mi launch zone."}, {"url":
"https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026", "title": "Tesla Robotaxi Expansion Gains Momentum as Morgan Stanley Flags Fleet
Targets", "domain": "roic.ai", "accessed_at": "2026-07-21", "snippet": "Miami live with unsupervised operations; Phoenix, Orlando, Tampa, Las Vegas and potentially New Orleans on deck by year-end. MS
Equalweight $415 PT; fleet ~1,500 in 2026, 30,000 by 2030."}, {"url": "https://www.cnbc.com/2026/01/22/musk-tesla-robotaxis-us-expansion.html", "title": "Musk: Tesla's robotaxis will be widespread in
the U.S. by end of 2026", "domain": "cnbc.com", "accessed_at": "2026-07-21", "snippet": "Musk said Tesla will have a 'widespread' network of driverless robotaxis in the US by end of 2026."}, {"url":
"https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/", "title": "Tesla 'Robotaxi' status check: 8 months in", "domain": "electrek.co", "accessed_at": "2026-07-21", "snippet":
"Reported ~42 cars in Austin, availability below 20%, with many earlier Musk promises unmet."}, {"url": "https://www.engadget.com/2207974/tesla-expands-robotaxi-service-to-small-section-of-miami/",
"title": "Tesla expands robotaxi service to small section of Miami", "domain": "engadget.com", "accessed_at": "2026-07-21", "snippet": "Tesla expanded service to a small section of West Miami; roadmap
mentions future expansions to Orlando and Tampa."}], "key_facts": ["Wikipedia's 'Service areas in the United States' table lists 9 metros: Austin, Dallas, Houston, Miami (Full commercial service), San
Francisco Bay Area (Safety-driver service), and Phoenix, Orlando, Tampa, Las Vegas (Service announced, 1H 2026).", "Four metros have 'Full commercial service' (unsupervised) status: Austin TX (Nov 18,
2025), Dallas TX (April 18, 2026), Houston TX (April 18, 2026), Miami FL (July 3, 2026).", "One metro has 'Safety-driver service' status: San Francisco Bay Area, CA \u2014 required by California DMV
permit rules (testing-with-driver only, no driverless deployment permit).", "Tesla Robotaxi launched in Austin on June 22, 2025 with an in-car human safety monitor.", "On Jan 28, 2026 (Q4 2025
earnings call), Tesla confirmed expansion to 7 new cities in H1 2026: Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas.", "Unsupervised service launched in Dallas and Houston on ~April 18,
2026 \u2014 the first expansion beyond Austin and the Bay Area.", "On June 3, 2026, Austin's service area expanded to the entire metro (~245 sq mi, ~12x the original ~20 sq mi launch zone).", "Miami
went live with unsupervised service on July 3, 2026 \u2014 the 4th US commercial market and first in Florida; initial geofence covers only a small slice (West Miami toward Doral/Sweetwater).",
"Phoenix, Orlando, Tampa, and Las Vegas remain 'Service announced' (not yet live commercial/safety-driver as of mid-July 2026); New Orleans cited by Morgan Stanley as a possible year-end market.",
"Morgan Stanley (July 6, 2026): Equalweight rating, $415 price target, forecasting fleet growth to ~1,500 vehicles in 2026 and 30,000 by 2030.", "Tesla logged nearly 700,000 paid Robotaxi miles since
the June 2025 launch (as of the Jan 2026 earnings call).", "Elon Musk predicted (Davos/WEF, Jan 22, 2026) a 'widespread' US robotaxi network by end of 2026; Electrek (Feb 16, 2026) reported only ~42
cars in Austin with availability below 20%."], "data_points": [{"metric": "Tesla Robotaxi metros with Full commercial service status (Wikipedia table)", "value": 4.0, "unit": "metro areas", "as_of":
"2026-07-21", "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"}, {"metric": "Tesla Robotaxi metros with Safety-driver service status (Wikipedia table)", "value": 1.0, "unit": "metro
areas", "as_of": "2026-07-21", "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"}, {"metric": "Tesla Robotaxi metros with 'Service announced' status (Wikipedia table)", "value": 4.0,
"unit": "metro areas", "as_of": "2026-07-21", "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"}, {"metric": "Austin metro service area size after June 2026 expansion", "value": 245.0,
"unit": "square miles", "as_of": "2026-06-03", "source_url": "https://tslna.com/en/tesla-robotaxi-guide/"}, {"metric": "Austin original launch service area size (June 2025)", "value": 20.0, "unit":
"square miles", "as_of": "2025-06-22", "source_url": "https://tslna.com/en/tesla-robotaxi-guide/"}, {"metric": "Cumulative paid Robotaxi miles since June 2025 (as of Jan 2026 call)", "value":
700000.0, "unit": "miles", "as_of": "2026-01-28", "source_url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/"}, {"metric": "New cities announced
for H1 2026 expansion", "value": 7.0, "unit": "cities", "as_of": "2026-01-28", "source_url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/"},
{"metric": "Morgan Stanley forecast Tesla Robotaxi fleet size 2026", "value": 1500.0, "unit": "vehicles", "as_of": "2026-07-06", "source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-
momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"}, {"metric": "Morgan Stanley forecast Tesla Robotaxi fleet size 2030", "value": 30000.0, "unit": "vehicles", "as_of": "2026-07-06",
"source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"}, {"metric": "Morgan Stanley Tesla price target", "value": 415.0,
"unit": "USD per share", "as_of": "2026-07-06", "source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"}, {"metric": "Reported
Tesla Robotaxi cars in Austin (Feb 2026)", "value": 42.0, "unit": "vehicles", "as_of": "2026-02-16", "source_url": "https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/"}],
"created_at": "2026-07-21T00:13:01.842630Z", "updated_at": "2026-07-21T00:13:01.842630Z", "stale_after": "2026-07-21T06:13:01.842630Z", "state": "fresh", "revision_history": [], "session_id":
"ab1c9161-6c83-4c18-b74b-85e66352a74f", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1, "failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: What US metropolitan areas currently have Tesla Robotaxi service as of July 2026? List the metro areas with 'Full commercial service' or 'Safety-driver service' status on the Wikipedia 'Tesla Robotaxi' Service areas in the United States table. Include recent expansion news and announced expansion plans for summer 2026.

*Generated: 2026-07-21T00:13:01.837652+00:00*


## 💬 Response

I'll research Tesla Robotaxi service areas in the US as of July 2026. Let me start by gathering information from Wikipedia and recent news sources.

## 🔧 Tool: ToolSearch


```json
{
  "query": "select:mcp__search__wikipedia",
  "max_results": 3
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "select:mcp__search__web_search",
  "max_results": 3
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "select:mcp__asknews__search_news",
  "max_results": 3
}
```

### 📋 Result

```

```

## 💬 Response

Now let me search for the relevant information in parallel.

## 🔧 Tool: mcp__search__wikipedia


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Tesla Robotaxi",
  "mode": "full",
  "prompt": "List all US metropolitan areas with Tesla Robotaxi service and their status (Full commercial service or Safety-driver service). Include dates of launch and expansion."
}
```

### 📋 Result

```
{"title": "Tesla Robotaxi", "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "extract": "Based on the provided content, here are the US metropolitan areas with Tesla Robotaxi
service:\n\n**Metropolitan Areas with Service:**\n\n1. **Austin, Texas**\n   - Status: Safety-driver service (human \"safety monitor\" in front passenger seat)\n   - Launch date: June 22, 2025\n\n2.
**Dallas, Texas**\n   - Status: Not specified (currently operates)\n   - Launch/expansion date: Not provided\n\n3. **Houston, Texas**\n   - Status: Not specified (currently operates)\n   -
Launch/expansion date: Not provided\n\n4. **Miami, Florida**\n   - Status: Not specified (currently operates)\n   - Launch/expansion date: Not provided\n\n**Note:** The content only explicitly
mentions that Austin launched with safety monitors. The operational status (full commercial vs. safety-driver) for Dallas, Houston, and Miami is not specified in the provided text. No specific launch
or expansion dates are given for any city except Austin.\n\nRelevant links:\nThe provided content does not contain any links to reference.", "mode": "full"}
```

```json
{
  "query": "Tesla Robotaxi expansion new metro areas launch service",
  "n_articles": 15,
  "hours_back": 2160
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403000 - More than 10 n_articles is reserved for Spelunker and Analyst tier. Please reduce n_articles or  upgrade your plan at
https://my.asknews.app/plans.
```

## 💬 Response

The Wikipedia summary is incomplete. Let me get the full article content and search for recent news in parallel.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Tesla Robotaxi service areas Wikipedia United States metro areas full commercial safety-driver 2026"
}
```

### 📋 Result

```
{"query": "Tesla Robotaxi service areas Wikipedia United States metro areas full commercial safety-driver 2026", "results": [{"title": "Tesla Robotaxi Expands to 7 US Cities in 2026: Dallas, Miami,
Las Vegas & More", "url": "https://www.tesery.com/blogs/news/tesla-confirms-aggressive-robotaxi-expansion-to-seven-major-us-cities-in-first-half-of-2026", "snippet": "\u26a1 Quick Summary\n-
Announcement: Tesla confirms Robotaxi expansion to 7 new US cities in H1 2026\n- New Cities: Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas\n- Current Operations: Austin (Ramping
Unsupervised) + Bay Area (Safety Driver)\n- Milestone: Nearly 700,000 paid Robotaxi miles logged since June launch\n- Key Threat: Direct competition with Uber, Lyft, and Waymo\nTesla has officially
confirmed its most ambitious autonomous vehicle deployment to date: a rapid expansion of its Robot", "api_data": null, "hint": null}, {"title": "Musk: Tesla's robotaxis will be widespread in the U.S.
by end of 2026", "url": "https://www.cnbc.com/2026/01/22/musk-tesla-robotaxis-us-expansion.html", "snippet": "![Elon Musk: My prediction is that there will be more robots than
people](https://image.cnbcfm.com/api/v1/image/108255772-17690971051769097103-43628898705-1080pnbcnews.jpg?v=1769097105&w=750&h=422&vtcrop=y)\n[Tesla](https://www.cnbc.com/quotes/TSLA/) CEO [Elon
Musk](https://www.cnbc.com/elon-musk/) said Thursday that his company will have a \"widespread\" network of driverless robotaxis in the U.S. by the end of 2026.\n\"Tesla's rolled out robotaxi service
in a few cities, and will be very, very wide", "api_data": null, "hint": null}, {"title": "Tesla maps a tiny Robotaxi zone in Miami while it still can't scale Texas | Electrek", "url":
"https://electrek.co/2026/07/03/tesla-robotaxi-miami-service-area-map/", "snippet": "![Tesla Robotaxi Miami launch map](https://electrek.co/wp-content/uploads/sites/3/2026/07/Tesla-Robotaxi-Miami-
launch-map.jpeg?quality=82&strip=all&w=1600)\nTesla has mapped out a Robotaxi service area in Miami, publishing a geofence that covers only a small slice of the metro \u2014 mostly West Miami and a
strip stretching toward Doral and Sweetwater.\nIt\u2019s the latest city Tesla has drawn a box around, but the announcement lands with a thud when you consider what\u2019s happened in Texas over the
past year", "api_data": null, "hint": null}, {"title": "Tesla expands Unsupervised Robotaxi Service to the entire Austin Metro Area, Cybercabs spotted across the US - Tesla Oracle", "url":
"https://www.teslaoracle.com/2026/06/08/tesla-expands-unsupervised-robotaxi-service-to-the-entire-austin-metro-area-cybercabs-spotted-across-the-us/", "snippet": "After a gradual extension of the
Tesla Robotaxi Service area in the last 12 months since [its launch](https://www.teslaoracle.com/2025/07/18/tesla-expands-robotaxi-service-area-in-austin-the-new-map-looks-like-the-tesla-logo-upside-
down-says-the-automaker/), Tesla (NASDAQ: TSLA) has finally expanded to the entire Austin Metropolitan Area.\nThe latest service area map displayed in the [Tesla Robotaxi
App](https://www.teslaoracle.com/2025/09/05/tesla-tsla-robotaxi-app-crosses-2-million-downloads-on", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi Cities | Expansion Tracker 2026", "url":
"https://robotaxi-safety-tracker.com/expansion.html", "snippet": "Expansion Tracking\nCity-by-city status of Tesla's autonomous ride-hailing rollout \u2014 see also our [robotaxi safety
tracker](https://robotaxi-safety-tracker.com/#trend)\nGeographic view of Tesla's robotaxi rollout across the United States\nDetailed breakdown of each market's operational status\n| City | State |
Status | Launch Date | Fleet Size | Incidents | Notes |\n|---|\nKey milestones in Tesla's robotaxi rollout\nHow the two leading autonomous ride-hailing services compare geographically\nCommon ques",
"api_data": null, "hint": null}, {"title": "Tesla Robotaxi Launches in Miami: What You Need to Know", "url": "https://www.basenor.com/blogs/news/tesla-robotaxi-launches-in-miami-what-you-need-to-
know", "snippet": "\ud83d\udccc UPDATE \u2014 July 4, 2026\nA Tesla Cybercab has been spotted on the streets of Miami, Florida, just one day after the unsupervised Robotaxi service went live in the
city. This marks the first confirmed sighting of the dedicated Cybercab vehicle in the Miami fleet, suggesting Tesla is moving quickly to deploy its purpose-built autonomous vehicle alongside the
Model Y units already in service. The Cybercab's arrival in Miami signals a significant escalation in Tesla's robotaxi rollout \u2014 the two-seat,", "api_data": null, "hint": null}, {"title":
"reuters.com,2025:newsml L4N3T706E:0 tesla to expand robotaxi service to san francisco bay area within two months", "url": "https://tr.tradingview.com/news/reuters.com,2025:newsml_L4N3T706E:0-tesla-
to-expand-robotaxi-service-to-san-francisco-bay-area-within-two-months", "snippet": "Haberler/Reuters/Tesla to expand robotaxi service to San Francisco Bay Area within two months\u00d6nemliTesla to
expand robotaxi service to San Francisco Bay Area within two monthsRefinitivBu haberi okumak i\u00e7in \u00fccretsiz deneme ba\u015flat\u0131n30-g\u00fcnl\u00fck \u00fccretsiz deneme", "api_data":
null, "hint": null}, {"title": "Tesla to Launch Robotaxi Service in Austin, Texas in June 2025", "url": "https://curatedtechnologynews.substack.com/p/f76eb5eb1e617d19dd688ddafa2aa5d8", "snippet":
"Tesla to Launch Robotaxi Service in Austin, Texas in June 2025\nKey Takeaways (TLDR)\nTesla's robotaxi service launch in Austin gives early adopters a competitive edge in the future transportation
market.\nTesla's robotaxi service in Austin will start with a limited fleet, utilizing teleoperators for safety in selected areas.\nTesla's robotaxis aim to make transportation safer and more
efficient, contributing to a sustainable energy future.\nElon Musk's emphasis on cautious geofencing for robotaxis c", "api_data": null, "hint": null}, {"title": "Tesla's Robotaxi Plans for 2026: Is
Musk's Timeline Finally Realistic?", "url": "https://finviz.com/news/297324/teslas-robotaxi-plans-for-2026-is-musks-timeline-finally-realistic", "snippet": "Tesla TSLA is betting big on autonomous
driving, and its robotaxi program is a key part of its long-term growth strategy. Tesla started its first robotaxi service in Austin, TX, on June 22, 2025, and the program has been growing steadily
since. After missing ambitious autonomy timelines in the past, the big question now is whether Tesla\u2019s expanding Robotaxi footprint makes Musk\u2019s latest targets more realistic.\nEarly
Progress and Expansion Plans\nToday, Tesla\u2019s robotaxis operate in Austin and the ", "api_data": null, "hint": null}, {"title": "www.mexc.com", "url": "https://www.mexc.com/news/549569",
"snippet": "Tesla\u2019s robotaxi service hit a new milestone this week. The company started offering rides without safety monitors in Austin.\nElon Musk shared the news on X. He congratulated the
Tesla AI team for the achievement. This marks the first time since the service launched in June 2025 that passengers can ride without a human backup driver.\nThe timing comes with Musk\u2019s latest
prediction. Speaking at the World Economic Forum in Davos, he claimed Tesla\u2019s robotaxis will be widespread across the U.S. by th", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Tesla Robotaxi expansion new metro areas launch service summer 2026",
  "n_articles": 10,
  "hours_back": 2160
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403011 - Your subscription is not currently active, please update your billing information at https://my.asknews.app/settings
```

## 💬 Response

Let me fetch the actual Wikipedia page content directly to get the precise Service areas table, and get recent expansion news.

## 🔧 Tool: WebFetch


```json
{
  "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi",
  "prompt": "Find the \"Service areas in the United States\" table. List every metropolitan area in the table along with its status (e.g., \"Full commercial service\", \"Safety-driver service\", or other), launch date, and any notes. Reproduce the table contents exactly."
}
```

### 📋 Result

```
Request failed with status code 403
```

## 🔧 Tool: WebFetch


```json
{
  "url": "https://www.tesery.com/blogs/news/tesla-confirms-aggressive-robotaxi-expansion-to-seven-major-us-cities-in-first-half-of-2026",
  "prompt": "What cities is Tesla Robotaxi expanding to in 2026? What is the current operational status of each city (safety driver vs unsupervised/full commercial)? Include dates and any announced summer 2026 plans."
}
```

### 📋 Result

```
<tool_use_error>Sibling tool call errored</tool_use_error>
```

## 💬 Response

Wikipedia blocked WebFetch. Let me use the Wikipedia tool's full mode with a targeted extraction prompt, and fetch the news articles.

## 🔧 Tool: mcp__search__wikipedia


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Tesla Robotaxi",
  "mode": "full",
  "prompt": "Reproduce the entire \"Service areas in the United States\" table exactly. For each row give: metropolitan area/city name, status label (such as Full commercial service, Safety-driver service, Announced, Planned), launch/start date, and any notes. List ALL rows including Austin, Dallas, Houston, Miami, San Francisco Bay Area, Phoenix, Las Vegas, Orlando, Tampa and any others."
}
```

### 📋 Result

```
{"title": "Tesla Robotaxi", "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "extract": "Based on the provided Wikipedia content, **there is no \"Service areas in the United States\" table
present in the text**. \n\nThe content only mentions that the service:\n- Launched in Austin, Texas on June 22, 2025\n- Currently operates in Texas (Austin, Dallas, Houston) and Miami, Florida\n\nThe
text does not contain a table with the cities you mentioned (San Francisco Bay Area, Phoenix, Las Vegas, Orlando, Tampa) nor does it provide status labels, specific launch dates for
Dallas/Houston/Miami, or detailed notes for different service areas.\n\nThe provided excerpt appears to be only the introductory section of the Wikipedia article and does not include any tables or
comprehensive service area information.\n\n**Relevant links:**\nSince no links were included in the provided text content, I cannot list any relevant links from the source material.", "mode": "full"}
```

```json
{
  "query": "Tesla Robotaxi Wikipedia service areas table full commercial service safety-driver Austin Bay Area Phoenix July 2026"
}
```

### 📋 Result

```
{"query": "Tesla Robotaxi Wikipedia service areas table full commercial service safety-driver Austin Bay Area Phoenix July 2026", "results": [{"title": "Tesla Launches Unsupervised Robotaxi in Dallas
and Houston | EV", "url": "https://eletric-vehicles.com/tesla/tesla-launches-unsupervised-robotaxi-in-dallas-and-houston/", "snippet": "[Tesla](https://eletric-vehicles.com/category/tesla/) started on
Saturday offering unsupervised rides on its Robotaxi service in Dallas and Houston, marking the first expansion of the autonomous ride-hailing programme beyond Austin and the San Francisco Bay
Area.\nThe launch comes four days before the company is scheduled to report first-quarter 2026 earnings on April 22.\n\u201cRobotaxi now rolling out in Dallas & Houston,\u201d [Tesla](https://eletric-
vehicles.com/category/tesla/)\u2018s official \u2018robotaxi\u2019 ac", "api_data": null, "hint": null}, {"title": "Tesla robotaxi service finally covers an entire metro area\u2014with a handful of
cars", "url": "https://www.howtogeek.com/tesla-robotaxi-service-covers-entire-austin-metro-area/", "snippet": "You no longer have to be picky about where you hail a [Tesla
robotaxi](https://www.howtogeek.com/companies-leading-the-charge-in-autonomous-and-electric-vehicles/) in its flagship city, provided you aren't too picky about when your ride arrives. The company has
confirmed that its \"unsupervised\" service now operates across the \"entire\" Austin metro area.\nThe move greatly [expands coverage](https://x.com/robotaxi/status/2062201854214521159) beyond the
previous South Austin footprint. That could be", "api_data": null, "hint": null}, {"title": "Tesla 'Robotaxi' status check: 8 months in, 19% availability, and all of Musk's promises are missing",
"url": "https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/", "snippet": "![](https://electrek.co/wp-content/uploads/sites/3/2025/06/tesla-robotaxi-
hero.jpg?quality=82&strip=all&w=1600)\nTesla launched its \u201cRobotaxi\u201d service in Austin eight months ago. In that time, Elon Musk promised 500 cars in Austin, coverage for half the US
population, fully unsupervised rides, and expansion to 8-10 cities, all by the end of 2025. None of it happened.\nToday, the service has roughly 42 cars in Austin, availability below 20%, a crash rate
9 times worse than human drivers, and the \u201cu", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi", "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "snippet": "Tesla Robotaxi is a
ride-hailing service operated by Tesla, Inc. that uses its vehicles equipped with its Full Self-Driving (FSD) software. The service launched in a limited capacity in Austin, Texas, on June 22, 2025
and currently operates in Texas in Austin, Dallas and Houston, and in Miami, Florida.\nThe service represents a key part of Tesla CEO Elon Musk's long-term strategy for the company, which envisions a
future where Tesla owners can add their personal vehicles to a shared autonomous ri", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Tesla Robotaxi\", \"url\":
\"https://en.wikipedia.org/wiki/Tesla_Robotaxi\", \"extract\": \"Tesla Robotaxi is a ride-hailing service operated by Tesla, Inc. that uses its vehicles equipped with its Full Self-Driving (FSD)
software. The service launched in a limited capacity in Austin, Texas, on June 22, 2025 and currently operates in Texas in Austin, Dallas and Houston, and in Miami, Florida.\\nThe service represents a
key part of Tesla CEO Elon Musk's long-term strategy for the company, which envisions a future where Tesla owners can add their personal vehicles to a shared autonomous ride-hailing network. The
launch in Austin initially operated with a human \\\"safety monitor\\\" in the front passenger seat. The launch attracted significant media attention and scrutiny, with early riders documenting
incidents such as the vehicle driving on the wrong side of the road, phantom braking, dropping passengers off in intersections and committing traffic violations that led to an investigation by the
National Highway Traffic Safety Administration.\\nTesla plans to have the Robotaxi network work with all current Tesla vehicles, but as of May 2026, the network is composed of only Model Y vehicles.
Tesla plans to add the Cybercab when it begins volume production in mid-2026 with the Model 3, Model S, Model X, and Cybertruck later. During Tesla's October 2024 We, Robot event it also demonstrated
the Robovan which it plans to add to the network, but no timelines were given.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Tesla Robotaxi Service Reaches Five Cities \u2013 EVBASE-Premium
EV&Tesla Accessories", "url": "https://www.evbase.com/blogs/ev-news/tesla-robotaxi-service-reaches-five-cities", "snippet": "Tesla Robotaxi is operating in five metropolitan areas, according to a July
3 update from Tesla-focused reporter Sawyer Merritt. The current list includes Austin, Dallas, Houston, Miami and the San Francisco Bay Area.\nFive cities sounds like broad coverage. In practice,
Tesla is running a different version of the service in each market.\nFive markets, three service models\nThe latest breakdown says Tesla offers unsupervised Model Y rides in Miami, Dallas and Houston.
Austin, where the company firs", "api_data": null, "hint": null}, {"title": "Robotaxi Status July 2026 \u2014 Waymo, Tesla & Zoox", "url": "https://thechargeport.com/robotaxi-tracker", "snippet":
"Tesla FSD (Supervised) / Autopilot\nTesla\nL2 Level 2 (supervised) \u2014 by far the widest operational scope of any production system\nWhere it works: The only production system that operates on
essentially ANY road. Highways + city streets + intersections + traffic lights + stop signs + unprotected turns + roundabouts + parking. Every other hands-off system on this page is restricted to a
mapped highway network and explicitly will not handle intersections or traffic signals. FSD currently has 10+ bill", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi in Austin 2026: How to
Ride, Cost & the Real Story - Tesla North America Guide", "url": "https://tslna.com/en/tesla-robotaxi-guide/", "snippet": "On June 3, 2026, Tesla quietly did something big: it opened up its driverless
Robotaxi service across nearly all of Austin, Texas, in a single move. The service area jumped to roughly 245 square miles overnight, sweeping in suburbs like Pflugerville and Manor and even reaching
stretches of the I-35 corridor and Austin\u2019s airport. Compared with the tiny 20-square-mile pocket the program launched with back in June 2025, that\u2019s a twelvefold expansion \u2014 the fifth
and by far the largest enlargement si", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi Service Areas in the US: Updated - Fifth Level Consulting", "url":
"https://fifthlevelconsulting.com/tesla-robotaxi-service-areas-in-the-us/", "snippet": "Tesla\u2019s self-driving taxi service is now a reality. If you\u2019re wondering where you can actually catch a
ride in one of these cars, this guide covers everything you need to know about Tesla Robotaxi service areas, how to book a ride, and what\u2019s coming next.\nWhat Are Tesla Robotaxi Service
Areas?\n[Tesla Robotaxi](https://fifthlevelconsulting.com/tesla-fsd-supervised-drives-362-miles/) service areas are the specific zones where Tesla\u2019s self-driving taxi service operates. These
areas are also called ", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi Cities | Expansion Tracker 2026", "url": "https://robotaxi-safety-tracker.com/expansion.html", "snippet": "Expansion
Tracking\nCity-by-city status of Tesla's autonomous ride-hailing rollout \u2014 see also our [robotaxi safety tracker](https://robotaxi-safety-tracker.com/#trend)\nGeographic view of Tesla's robotaxi
rollout across the United States\nDetailed breakdown of each market's operational status\n| City | State | Status | Launch Date | Fleet Size | Incidents | Notes |\n|---|\nKey milestones in Tesla's
robotaxi rollout\nHow the two leading autonomous ride-hailing services compare geographically\nCommon ques", "api_data": null, "hint": null}]}
```

## 💬 Response

The Wikipedia tool is only returning the intro, not the table. Let me fetch the raw Wikipedia content via the API and gather the key news sources.

## 🔧 Tool: Bash


```json
{
  "command": "curl -s \"https://en.wikipedia.org/w/api.php?action=parse&page=Tesla_Robotaxi&prop=wikitext&section=0&format=json\" -H \"User-Agent: research-bot/1.0\" | head -c 200; echo; echo \"---TRYING SECTIONS---\"; curl -s \"https://en.wikipedia.org/w/api.php?action=parse&page=Tesla_Robotaxi&prop=sections&format=json\" -H \"User-Agent: research-bot/1.0\"",
  "description": "Fetch Wikipedia section list for Tesla Robotaxi"
}
```

### 📋 Result

```
Bash is not available.
```

## 💬 Response

Bash isn't available. Let me use the mcp fetch_url tool to get the raw Wikipedia content.

## 🔧 Tool: ToolSearch


```json
{
  "query": "select:mcp__search__fetch_url",
  "max_results": 2
}
```

### 📋 Result

```

```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/w/index.php?title=Tesla_Robotaxi&action=raw",
  "prompt": "Find the \"Service areas in the United States\" table. List every metropolitan area/city with its Status (Full commercial service, Safety-driver service, Announced, Planned, etc.), launch date, and notes. Reproduce all rows exactly."
}
```

### 📋 Result

```
{"url": "https://en.wikipedia.org/w/index.php?title=Tesla_Robotaxi&action=raw", "content": "Based on the \"Service areas in the United States\" table in the content:\n\n| State | Metro Area | Status |
Launch Date | Notes |\n|-------|------------|--------|-------------|-------|\n| Arizona | Phoenix | Service announced | 1H 2026 | - |\n| California | San Francisco Bay Area | Safety-driver service |
\u2014 | - |\n| Florida | Miami | Full commercial service | July 3, 2026 | - |\n| Florida | Orlando | Service announced | 1H 2026 | - |\n| Florida | Tampa | Service announced | 1H 2026 | - |\n| Nevada
| Las Vegas | Service announced | 1H 2026 | - |\n| Texas | Austin | Full commercial service | November 18, 2025 | - |\n| Texas | Dallas | Full commercial service | April 18, 2026 | - |\n| Texas |
Houston | Full commercial service | April 18, 2026 | - |\n\n**Relevant links:**\n- [Tesla Robotaxi official website](https://www.tesla.com/robotaxi)\n- [Tesla confirms Robotaxi expansion plans with
new cities and aggressive timeline](https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/)\n- [Tesla opens Robotaxi access to everyone \u2014 but there's
one catch](https://www.teslarati.com/tesla-opens-robotaxi-access-to-everyone-one-catch-ios/)\n- [Tesla Launches Unsupervised Robotaxi Service in Dallas and
Houston](https://www.notateslaapp.com/news/4004/tesla-launches-unsupervised-robotaxi-service-in-dallas-and-houston)\n- [Tesla Launches Unsupervised Robotaxi Rides in
Miami](https://www.notateslaapp.com/news/4394/tesla-launches-unsupervised-robotaxi-rides-in-miami)"}
```

```json
{
  "url": "https://www.evbase.com/blogs/ev-news/tesla-robotaxi-service-reaches-five-cities",
  "prompt": "List the cities where Tesla Robotaxi operates and the service model (unsupervised/full commercial vs safety driver) for each. Include dates."
}
```

### 📋 Result

```
{"url": "https://www.evbase.com/blogs/ev-news/tesla-robotaxi-service-reaches-five-cities", "content": "**Tesla Robotaxi Operating Cities (as of July 3, 2024):**\n\n1. **Miami** - Unsupervised (first
announced July 3, 2024)\n2. **Dallas** - Unsupervised\n3. **Houston** - Unsupervised  \n4. **Austin** - Mixed: both unsupervised vehicles and cars with safety monitors (first launch city)\n5. **San
Francisco Bay Area** - Safety monitor required (California DMV permit only allows autonomous testing with a driver; no driverless testing or deployment permit)\n\n**Key Details:**\n- Texas and Miami
markets: Unsupervised Model Y rides\n- Bay Area: Human safety monitor in all vehicles due to regulatory restrictions\n- Service hours (TX markets): 6 a.m. to 2 a.m. Central Time\n- Coverage is
geofenced and limited within each city\n\n**Relevant links:**\n- [Sawyer Merritt's July 3 update on five-city availability](https://x.com/SawyerMerritt/status/2073068325815402731)\n- [Tesla Robotaxi
Support Page](https://www.tesla.com/support/robotaxi)\n- [Tesla Robotaxi Main Page](https://www.tesla.com/robotaxi)\n- [Reuters: Tesla rolls out robotaxi service in Miami (July
3)](https://www.investing.com/news/stock-market-news/tesla-rolls-out-robotaxi-service-in-miami-4775262)\n- [California DMV Autonomous Vehicle Permit Holders](https://www.dmv.ca.gov/portal/vehicle-
industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/)", "title": "Tesla Robotaxi Service Reaches Five Cities"}
```

## 💬 Response

I now have the Wikipedia Service areas table. Let me confirm the expansion news details with a couple more targeted fetches to complete the picture on summer 2026 plans.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/",
  "prompt": "What new cities has Tesla announced for Robotaxi expansion and what is the timeline? Any specific summer 2026 plans? Include dates and quotes."
}
```

### 📋 Result

```
{"url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/", "content": "Based on the content, here are the key details about Tesla's Robotaxi
expansion:\n\n**New Cities Announced:**\nTesla plans to launch Robotaxi service in seven new cities:\n- Dallas\n- Houston\n- Phoenix\n- Miami\n- Orlando\n- Tampa\n- Las Vegas\n\n**Timeline:**\nAll
seven cities are targeted for launch in the **first half of 2026** (announced during Tesla's Q4 2025 Earnings Call on January 28, 2026).\n\n**Current Status:**\n- Bay Area: Listed as \"Safety
Driver\"\n- Austin: Listed as \"Ramping Unsupervised\"\n\n**Key Milestone:**\nThe article notes that \"Tesla launched driverless rides in Austin last week\" (relative to the January 28, 2026 article
date).\n\n**Performance Data:**\nTesla announced it \"achieved nearly 700,000 paid Robotaxi miles since launching Robotaxi last June\" (June 2025).\n\n**Summer 2026 Plans:**\nThe content does not
contain any specific information about summer 2026 Robotaxi plans. The latest timeline mentioned is \"first half of this year\" (2026), which would end in June 2026.\n\n**Relevant links:**\n- [Tesla
Q4 and FY 2025 Earnings Call details](https://www.teslarati.com/tesla-tsla-q4-and-fy-2025-earnings-call-the-most-important-points/)\n- [Tesla confirms Robotaxi heading to five new U.S.
cities](https://www.teslarati.com/tesla-confirms-robotaxi-heading-five-new-cities-u-s/)\n- [Tesla launches Robotaxi rides in Austin with no safety monitor](https://www.teslarati.com/tesla-launches-
robotaxi-rides-in-austin-with-no-safety-monitor/)", "title": "Tesla confirms Robotaxi expansion plans with new cities and aggressive timeline"}
```

```json
{
  "query": "Tesla Robotaxi expansion summer 2026 new cities announced Phoenix Las Vegas Orlando Tampa timeline"
}
```

### 📋 Result

```
{"query": "Tesla Robotaxi expansion summer 2026 new cities announced Phoenix Las Vegas Orlando Tampa timeline", "results": [{"title": "Tesla Robotaxi Expands to 7 US Cities in 2026: Dallas, Miami, Las
Vegas & More", "url": "https://www.tesery.com/blogs/news/tesla-confirms-aggressive-robotaxi-expansion-to-seven-major-us-cities-in-first-half-of-2026", "snippet": "\u26a1 Quick Summary\n- Announcement:
Tesla confirms Robotaxi expansion to 7 new US cities in H1 2026\n- New Cities: Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas\n- Current Operations: Austin (Ramping Unsupervised) + Bay
Area (Safety Driver)\n- Milestone: Nearly 700,000 paid Robotaxi miles logged since June launch\n- Key Threat: Direct competition with Uber, Lyft, and Waymo\nTesla has officially confirmed its most
ambitious autonomous vehicle deployment to date: a rapid expansion of its Robot", "api_data": null, "hint": null}, {"title": "Tesla Adds Two Unsupervised Robotaxi Cities as It Pushes Beyond EVs -
Autoblog", "url": "https://www.autoblog.com/news/tesla-adds-two-unsupervised-robotaxi-cities-as-it-pushes-beyond-evs", "snippet": null, "api_data": null, "hint": null}, {"title": "Tesla confirms
Robotaxi expansion plans with new cities and aggressive timeline", "url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/", "snippet":
"[News](https://www.teslarati.com/category/news/)\nTesla confirms Robotaxi expansion plans with new cities and aggressive timeline\nTesla plans to launch in Dallas, Houston, Phoenix, Miami, Orlando,
Tampa, and Las Vegas. It lists the Bay Area as \u201cSafety Driver,\u201d and Austin as \u201cRamping Unsupervised.\u201d\n![](https://www.teslarati.com/wp-content/uploads/2026/01/tesla-robotaxi-
driverless.jpg)\nTesla confirmed its intentions to expand the Robotaxi program in the United States with an aggressive timeline tha", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi
Expansion Gains Momentum as Morgan Stanley Flags Fleet Targets | Roic News", "url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026",
"snippet": "[Tesla (TSLA)](https://www.roic.ai/quote/TSLA)'s robotaxi service expands to Miami with unsupervised operations, with Phoenix, Orlando, Tampa, Las Vegas, and potentially New Orleans on
deck by year-end.- Morgan Stanley reiterates Equalweight rating and $415 price target, forecasting fleet growth to 1,500 vehicles by 2026 and 30,000 by 2030.\n- Investors focus on fleet expansion pace
and safety data as key indicators of autonomous driving progress.\nMorgan Stanley has maintained its Equalweight rat", "api_data": null, "hint": null}, {"title": "Tesla maps a tiny Robotaxi zone in
Miami while it still can't scale Texas | Electrek", "url": "https://electrek.co/2026/07/03/tesla-robotaxi-miami-service-area-map/", "snippet": "![Tesla Robotaxi Miami launch
map](https://electrek.co/wp-content/uploads/sites/3/2026/07/Tesla-Robotaxi-Miami-launch-map.jpeg?quality=82&strip=all&w=1600)\nTesla has mapped out a Robotaxi service area in Miami, publishing a
geofence that covers only a small slice of the metro \u2014 mostly West Miami and a strip stretching toward Doral and Sweetwater.\nIt\u2019s the latest city Tesla has drawn a box around, but the
announcement lands with a thud when you consider what\u2019s happened in Texas over the past year", "api_data": null, "hint": null}, {"title": "Tesla expands robotaxi service to small section of Miami
- Engadget", "url": "https://www.engadget.com/2207974/tesla-expands-robotaxi-service-to-small-section-of-miami/", "snippet": "Tesla expands robotaxi service to small section of Miami\nThe
company\u2019s robotaxi roadmap mentions future expansions to Orlando and Tampa.\nMiami residents are getting another option for autonomous taxi services, at least for those who live in a specific
portion of the Floridian city. As [posted on X](https://x.com/robotaxi/status/2073030246161367153), Tesla has expanded its Robotaxi service to a small section of West Miami.\nLike we saw with the
[robotaxi rollout](https://www.engadget.com/transport", "api_data": null, "hint": null}, {"title": "Tesla tipped its hand at where Robotaxi is heading next", "url": "https://www.teslarati.com/tesla-
tipped-its-hand-where-robotaxi-heading-next/", "snippet": "[Elon Musk](https://www.teslarati.com/category/elon-musk/)\nTesla tipped its hand at where Robotaxi is heading next\n![Tesla Cybercab
production units rolling off the factory line in Gigafactory Texas (Credit: Tesla)](https://www.teslarati.com/wp-content/uploads/2026/04/tesla-cybercab-production-line-gigafactory-scaled.jpg)\nIn the
world of autonomous ride-hailing, there are only a handful of names. Among those few companies lies a strategy play by each to keep the opposition on their toes. Tesla, ", "api_data": null, "hint":
null}, {"title": "Tesla Robotaxi Cities | Expansion Tracker 2026", "url": "https://robotaxi-safety-tracker.com/expansion.html", "snippet": "Expansion Tracking\nCity-by-city status of Tesla's
autonomous ride-hailing rollout \u2014 see also our [robotaxi safety tracker](https://robotaxi-safety-tracker.com/#trend)\nGeographic view of Tesla's robotaxi rollout across the United
States\nDetailed breakdown of each market's operational status\n| City | State | Status | Launch Date | Fleet Size | Incidents | Notes |\n|---|\nKey milestones in Tesla's robotaxi rollout\nHow the two
leading autonomous ride-hailing services compare geographically\nCommon ques", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi Expansion: 7 New Cities Coming in 2026", "url":
"https://www.basenor.com/blogs/news/tesla-robotaxi-expansion-7-new-cities-coming-in-2026", "snippet": "\ud83d\udccc UPDATE \u2014 April 20, 2026\nTesla has officially launched unsupervised Robotaxi
rides in Houston and Dallas, marking a significant milestone in its expansion timeline. Morgan Stanley analyst Andrew Percoco responded with a bullish note, calling the launch \"tangible progress at a
time when the market was growing increasingly skeptical about Tesla's robotaxi expansion timeline.\" The move directly counters doubts about whether Tesla could execute its H1 2026 rollout targets on
schedule. Wall Street's", "api_data": null, "hint": null}, {"title": "Tesla Robotaxi Just Launched in Miami \u2014 City #4 Goes Live as National Expansion Accelerates | Learn My EV", "url":
"https://www.learnmyev.com/post/tesla-robotaxi-miami-launch-2026", "snippet": "Miami woke up this morning with a new way to get around. As of July 3, 2026, Tesla's autonomous ride-hailing service is
live in the city \u2014 making Miami the fourth US market to go commercial, and the first to launch in Florida.\nThe announcement came from @robotaxi on X this morning: \"Robotaxi now available in
Miami.\" The service area covers a meaningful chunk of the metro, centered around West Miami and stretching into neighboring corridors \u2014 visible in the map released alongside the launch.\nThe ",
"api_data": null, "hint": null}]}
```

## 💬 Response

I now have comprehensive information. Let me compile the findings.

## Research Report: Tesla Robotaxi US Service Areas (as of July 2026)

### Wikipedia "Service areas in the United States" Table

Based on the current Wikipedia "Tesla Robotaxi" article, the Service areas in the United States table lists the following rows:

| State | Metro Area | Status | Launch Date |
|-------|------------|--------|-------------|
| Texas | **Austin** | **Full commercial service** | November 18, 2025 |
| Texas | **Dallas** | **Full commercial service** | April 18, 2026 |
| Texas | **Houston** | **Full commercial service** | April 18, 2026 |
| Florida | **Miami** | **Full commercial service** | July 3, 2026 |
| California | **San Francisco Bay Area** | **Safety-driver service** | — |
| Arizona | Phoenix | Service announced | 1H 2026 |
| Florida | Orlando | Service announced | 1H 2026 |
| Florida | Tampa | Service announced | 1H 2026 |
| Nevada | Las Vegas | Service announced | 1H 2026 |

### Metros with "Full commercial service" or "Safety-driver service" status (the requested subset)

**Full commercial service (unsupervised — no safety driver):**
1. **Austin, TX** — launched June 22, 2025 with in-car safety monitor; began unsupervised/driverless rides ~Nov 18, 2025; expanded to the entire Austin metro area (~245 sq mi) on June 3, 2026.
2. **Dallas, TX** — unsupervised service launched April 18, 2026.
3. **Houston, TX** — unsupervised service launched April 18, 2026.
4. **Miami, FL** — unsupervised service launched July 3, 2026 (first Florida market; initial geofence covers only a small slice — West Miami toward Doral/Sweetwater).

**Safety-driver service (human safety driver required):**
5. **San Francisco Bay Area, CA** — operates with a human safety driver in all vehicles because California's DMV permit only allows autonomous testing with a driver present (no driverless deployment permit). Service began ~late 2025/early 2026.

*(Note: Phoenix, Orlando, Tampa, and Las Vegas appear in the table with status "Service announced" — NOT yet "Full commercial" or "Safety-driver" — so they fall outside the requested status subset but represent the announced pipeline.)*

### Recent Expansion News & Announced Plans

- **Q4 2025 Earnings Call (Jan 28, 2026):** Tesla officially confirmed expansion to **seven new cities in the first half of 2026**: Dallas, Houston, Phoenix, Miami, Orlando, Tampa, and Las Vegas. At that time Austin was "Ramping Unsupervised" and the Bay Area was "Safety Driver."
- **Milestone:** Nearly **700,000 paid Robotaxi miles** logged since the June 2025 launch (as of Jan 2026 call).
- **April 18/20, 2026:** Unsupervised service launched in Dallas and Houston (first expansion beyond Austin and the Bay Area).
- **June 3, 2026:** Austin service area expanded to the entire metro (~245 sq mi, a ~12x increase from the original ~20 sq mi launch zone).
- **July 3, 2026:** Miami went live with unsupervised service (city #4 to go commercial); a Cybercab was reportedly spotted in Miami on July 4, 2026.
- **Summer/Second-half 2026 pipeline (announced, not yet launched):** Phoenix, Orlando, Tampa, and Las Vegas are "on deck," with **New Orleans** cited by Morgan Stanley (July 6, 2026) as a potential additional market by year-end.
- **Analyst view (Morgan Stanley, July 6, 2026):** Equalweight, $415 PT; forecasts fleet growth to ~1,500 vehicles in 2026 and 30,000 by 2030.
- **Musk (Davos/WEF, Jan 22, 2026):** Predicted "widespread" driverless robotaxi network across the US by end of 2026.
- **Skeptical reporting (Electrek, Feb 16, 2026):** Reported ~42 cars in Austin, availability below 20%, criticizing gaps between Musk's promises and actual deployment.

### Caveats on Data Vintage
- Table values reflect the Wikipedia article as accessed July 21, 2026. Bay Area launch date shows "—" (blank) in the table.
- "1H 2026" (first half of 2026) announced-launch dates for Phoenix/Orlando/Tampa/Las Vegas had not clearly converted to live commercial/safety-driver service in the sources reviewed as of early-to-mid July 2026.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "## Tesla Robotaxi US Service Areas (as of July 2026)\n\n### Wikipedia \"Service areas in the United States\" Table\nThe Wikipedia \"Tesla Robotaxi\" article lists nine rows:\n- Austin, TX \u2014 Full commercial service \u2014 Nov 18, 2025\n- Dallas, TX \u2014 Full commercial service \u2014 April 18, 2026\n- Houston, TX \u2014 Full commercial service \u2014 April 18, 2026\n- Miami, FL \u2014 Full commercial service \u2014 July 3, 2026\n- San Francisco Bay Area, CA \u2014 Safety-driver service \u2014 (date blank)\n- Phoenix, AZ \u2014 Service announced \u2014 1H 2026\n- Orlando, FL \u2014 Service announced \u2014 1H 2026\n- Tampa, FL \u2014 Service announced \u2014 1H 2026\n- Las Vegas, NV \u2014 Service announced \u2014 1H 2026\n\n### Metros with the requested status labels\n**Full commercial service (unsupervised, no safety driver):** Austin TX, Dallas TX, Houston TX, Miami FL.\n**Safety-driver service (human safety driver required):** San Francisco Bay Area CA \u2014 required because California's DMV permit only allows autonomous testing with a driver; no driverless deployment permit.\n\nPhoenix, Orlando, Tampa, and Las Vegas are listed only as \"Service announced\" (1H 2026), NOT the two requested statuses, but represent the announced pipeline.\n\n### Timeline & Expansion News\n- June 22, 2025: Austin launched with in-car safety monitor.\n- Late 2025: Austin began unsupervised/driverless rides (Wikipedia dates full commercial as Nov 18, 2025).\n- Jan 28, 2026 (Q4 2025 earnings call): Tesla confirmed expansion to 7 new cities in H1 2026 \u2014 Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas. ~700,000 paid Robotaxi miles logged since June 2025.\n- April 18/20, 2026: Unsupervised service launched in Dallas and Houston (first expansion beyond Austin and Bay Area).\n- June 3, 2026: Austin expanded to entire metro (~245 sq mi, ~12x the original ~20 sq mi zone).\n- July 3, 2026: Miami went live with unsupervised service (city #4 commercial; first in Florida). Cybercab reportedly spotted in Miami July 4, 2026.\n\n### Announced summer/2H-2026 plans\n- Phoenix, Orlando, Tampa, Las Vegas \"on deck\"; New Orleans cited by Morgan Stanley (July 6, 2026) as a possible additional market by year-end.\n- Morgan Stanley (July 6, 2026): Equalweight, $415 PT; forecasts ~1,500 fleet vehicles in 2026, 30,000 by 2030.\n- Musk (Davos/WEF, Jan 22, 2026): predicted \"widespread\" US robotaxi network by end of 2026.\n- Skeptical reporting (Electrek, Feb 16, 2026): ~42 cars in Austin, availability below 20%.\n\n### Caveats\nTable values reflect Wikipedia as accessed July 21, 2026. Bay Area launch date shows blank. Announced 1H-2026 cities (Phoenix/Orlando/Tampa/Las Vegas) had not clearly converted to live commercial/safety-driver service in sources reviewed as of mid-July 2026.",
  "key_facts": [
    "Wikipedia's 'Service areas in the United States' table lists 9 metros: Austin, Dallas, Houston, Miami (Full commercial service), San Francisco Bay Area (Safety-driver service), and Phoenix, Orlando, Tampa, Las Vegas (Service announced, 1H 2026).",
    "Four metros have 'Full commercial service' (unsupervised) status: Austin TX (Nov 18, 2025), Dallas TX (April 18, 2026), Houston TX (April 18, 2026), Miami FL (July 3, 2026).",
    "One metro has 'Safety-driver service' status: San Francisco Bay Area, CA \u2014 required by California DMV permit rules (testing-with-driver only, no driverless deployment permit).",
    "Tesla Robotaxi launched in Austin on June 22, 2025 with an in-car human safety monitor.",
    "On Jan 28, 2026 (Q4 2025 earnings call), Tesla confirmed expansion to 7 new cities in H1 2026: Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas.",
    "Unsupervised service launched in Dallas and Houston on ~April 18, 2026 \u2014 the first expansion beyond Austin and the Bay Area.",
    "On June 3, 2026, Austin's service area expanded to the entire metro (~245 sq mi, ~12x the original ~20 sq mi launch zone).",
    "Miami went live with unsupervised service on July 3, 2026 \u2014 the 4th US commercial market and first in Florida; initial geofence covers only a small slice (West Miami toward Doral/Sweetwater).",
    "Phoenix, Orlando, Tampa, and Las Vegas remain 'Service announced' (not yet live commercial/safety-driver as of mid-July 2026); New Orleans cited by Morgan Stanley as a possible year-end market.",
    "Morgan Stanley (July 6, 2026): Equalweight rating, $415 price target, forecasting fleet growth to ~1,500 vehicles in 2026 and 30,000 by 2030.",
    "Tesla logged nearly 700,000 paid Robotaxi miles since the June 2025 launch (as of the Jan 2026 earnings call).",
    "Elon Musk predicted (Davos/WEF, Jan 22, 2026) a 'widespread' US robotaxi network by end of 2026; Electrek (Feb 16, 2026) reported only ~42 cars in Austin with availability below 20%."
  ],
  "sources": [
    {
      "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi",
      "title": "Tesla Robotaxi",
      "domain": "en.wikipedia.org",
      "accessed_at": "2026-07-21",
      "snippet": "Service areas in the US table: Austin/Dallas/Houston/Miami Full commercial service; SF Bay Area Safety-driver service; Phoenix/Orlando/Tampa/Las Vegas Service announced 1H 2026."
    },
    {
      "url": "https://www.evbase.com/blogs/ev-news/tesla-robotaxi-service-reaches-five-cities",
      "title": "Tesla Robotaxi Service Reaches Five Cities",
      "domain": "evbase.com",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla operates in five metros: Austin, Dallas, Houston, Miami (unsupervised), and SF Bay Area (safety monitor required due to CA DMV permit)."
    },
    {
      "url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/",
      "title": "Tesla confirms Robotaxi expansion plans with new cities and aggressive timeline",
      "domain": "teslarati.com",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla plans to launch in Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas in H1 2026; Bay Area 'Safety Driver', Austin 'Ramping Unsupervised'; ~700,000 paid miles."
    },
    {
      "url": "https://eletric-vehicles.com/tesla/tesla-launches-unsupervised-robotaxi-in-dallas-and-houston/",
      "title": "Tesla Launches Unsupervised Robotaxi in Dallas and Houston",
      "domain": "eletric-vehicles.com",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla began offering unsupervised rides in Dallas and Houston, first expansion beyond Austin and the SF Bay Area, days before Q1 2026 earnings (April 22)."
    },
    {
      "url": "https://www.learnmyev.com/post/tesla-robotaxi-miami-launch-2026",
      "title": "Tesla Robotaxi Just Launched in Miami \u2014 City #4 Goes Live",
      "domain": "learnmyev.com",
      "accessed_at": "2026-07-21",
      "snippet": "As of July 3, 2026, Tesla's autonomous service is live in Miami \u2014 4th US commercial market and first in Florida."
    },
    {
      "url": "https://electrek.co/2026/07/03/tesla-robotaxi-miami-service-area-map/",
      "title": "Tesla maps a tiny Robotaxi zone in Miami while it still can't scale Texas",
      "domain": "electrek.co",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla mapped a Miami geofence covering only a small slice of the metro \u2014 mostly West Miami toward Doral and Sweetwater."
    },
    {
      "url": "https://www.teslaoracle.com/2026/06/08/tesla-expands-unsupervised-robotaxi-service-to-the-entire-austin-metro-area-cybercabs-spotted-across-the-us/",
      "title": "Tesla expands Unsupervised Robotaxi Service to the entire Austin Metro Area",
      "domain": "teslaoracle.com",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla expanded to the entire Austin Metropolitan Area after gradual extensions since launch."
    },
    {
      "url": "https://tslna.com/en/tesla-robotaxi-guide/",
      "title": "Tesla Robotaxi in Austin 2026: How to Ride, Cost & the Real Story",
      "domain": "tslna.com",
      "accessed_at": "2026-07-21",
      "snippet": "On June 3, 2026 Tesla opened driverless service across nearly all of Austin (~245 sq mi), a 12x expansion from the ~20 sq mi launch zone."
    },
    {
      "url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026",
      "title": "Tesla Robotaxi Expansion Gains Momentum as Morgan Stanley Flags Fleet Targets",
      "domain": "roic.ai",
      "accessed_at": "2026-07-21",
      "snippet": "Miami live with unsupervised operations; Phoenix, Orlando, Tampa, Las Vegas and potentially New Orleans on deck by year-end. MS Equalweight $415 PT; fleet ~1,500 in 2026, 30,000 by 2030."
    },
    {
      "url": "https://www.cnbc.com/2026/01/22/musk-tesla-robotaxis-us-expansion.html",
      "title": "Musk: Tesla's robotaxis will be widespread in the U.S. by end of 2026",
      "domain": "cnbc.com",
      "accessed_at": "2026-07-21",
      "snippet": "Musk said Tesla will have a 'widespread' network of driverless robotaxis in the US by end of 2026."
    },
    {
      "url": "https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/",
      "title": "Tesla 'Robotaxi' status check: 8 months in",
      "domain": "electrek.co",
      "accessed_at": "2026-07-21",
      "snippet": "Reported ~42 cars in Austin, availability below 20%, with many earlier Musk promises unmet."
    },
    {
      "url": "https://www.engadget.com/2207974/tesla-expands-robotaxi-service-to-small-section-of-miami/",
      "title": "Tesla expands robotaxi service to small section of Miami",
      "domain": "engadget.com",
      "accessed_at": "2026-07-21",
      "snippet": "Tesla expanded service to a small section of West Miami; roadmap mentions future expansions to Orlando and Tampa."
    }
  ],
  "data_points": [
    {
      "metric": "Tesla Robotaxi metros with Full commercial service status (Wikipedia table)",
      "value": 4,
      "unit": "metro areas",
      "as_of": "2026-07-21",
      "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"
    },
    {
      "metric": "Tesla Robotaxi metros with Safety-driver service status (Wikipedia table)",
      "value": 1,
      "unit": "metro areas",
      "as_of": "2026-07-21",
      "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"
    },
    {
      "metric": "Tesla Robotaxi metros with 'Service announced' status (Wikipedia table)",
      "value": 4,
      "unit": "metro areas",
      "as_of": "2026-07-21",
      "source_url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi"
    },
    {
      "metric": "Austin metro service area size after June 2026 expansion",
      "value": 245,
      "unit": "square miles",
      "as_of": "2026-06-03",
      "source_url": "https://tslna.com/en/tesla-robotaxi-guide/"
    },
    {
      "metric": "Austin original launch service area size (June 2025)",
      "value": 20,
      "unit": "square miles",
      "as_of": "2025-06-22",
      "source_url": "https://tslna.com/en/tesla-robotaxi-guide/"
    },
    {
      "metric": "Cumulative paid Robotaxi miles since June 2025 (as of Jan 2026 call)",
      "value": 700000,
      "unit": "miles",
      "as_of": "2026-01-28",
      "source_url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/"
    },
    {
      "metric": "New cities announced for H1 2026 expansion",
      "value": 7,
      "unit": "cities",
      "as_of": "2026-01-28",
      "source_url": "https://www.teslarati.com/tesla-confirms-robotaxi-expansion-plans-new-cities-aggressive-timeline/"
    },
    {
      "metric": "Morgan Stanley forecast Tesla Robotaxi fleet size 2026",
      "value": 1500,
      "unit": "vehicles",
      "as_of": "2026-07-06",
      "source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"
    },
    {
      "metric": "Morgan Stanley forecast Tesla Robotaxi fleet size 2030",
      "value": 30000,
      "unit": "vehicles",
      "as_of": "2026-07-06",
      "source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"
    },
    {
      "metric": "Morgan Stanley Tesla price target",
      "value": 415,
      "unit": "USD per share",
      "as_of": "2026-07-06",
      "source_url": "https://www.roic.ai/news/tesla-robotaxi-expansion-gains-momentum-as-morgan-stanley-flags-fleet-targets-07-06-2026"
    },
    {
      "metric": "Reported Tesla Robotaxi cars in Austin (Feb 2026)",
      "value": 42,
      "unit": "vehicles",
      "as_of": "2026-02-16",
      "source_url": "https://electrek.co/2026/02/16/tesla-robotaxi-status-check-8-months-in/"
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's a summary of the key findings:

## Tesla Robotaxi US Service Areas (as of July 2026)

### Metros with the two requested Wikipedia status labels

**Full commercial service (unsupervised — no safety driver):**
1. **Austin, TX** — Nov 18, 2025 (launched June 22, 2025 with safety monitor; entire metro coverage as of June 3, 2026)
2. **Dallas, TX** — April 18, 2026
3. **Houston, TX** — April 18, 2026
4. **Miami, FL** — July 3, 2026 (first Florida market)

**Safety-driver service:**
5. **San Francisco Bay Area, CA** — human safety driver required due to California DMV permit rules (no driverless deployment permit)

*(Phoenix, Orlando, Tampa, and Las Vegas appear in the table only as "Service announced / 1H 2026" — not yet in either requested status.)*

### Expansion news & announced plans
- **Jan 28, 2026 earnings call:** Tesla confirmed 7-city H1 2026 expansion (Dallas, Houston, Phoenix, Miami, Orlando, Tampa, Las Vegas); ~700,000 paid miles logged.
- **April 2026:** Dallas & Houston went unsupervised — first expansion beyond Austin/Bay Area.
- **June 3, 2026:** Austin expanded to entire metro (~245 sq mi, 12x growth).
- **July 3, 2026:** Miami launched (city #4).
- **Summer/2H 2026 pipeline:** Phoenix, Orlando, Tampa, Las Vegas "on deck"; New Orleans cited by Morgan Stanley as a possible year-end market. Musk projected a "widespread" US network by end of 2026, though skeptical reporting (Electrek, Feb 2026) noted only ~42 Austin cars and sub-20% availability.

The full report, structured data points, and all sources have been recorded via the StructuredOutput tool.


### ↳ End nested research agent trace

```json
{
  "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi#Services",
  "prompt": "List every row in the \"Service areas in the United States\" table with the metro area name and its service status column value (e.g. Full commercial service, Safety-driver service, Testing, Announced). I need the exact statuses."
}
```

### 📋 Result

```
{"title": "Tesla Robotaxi", "url": "https://en.wikipedia.org/wiki/Tesla_Robotaxi", "extract": "Tesla Robotaxi is a ride-hailing service operated by Tesla, Inc. that uses its vehicles equipped with its
Full Self-Driving (FSD) software. The service launched in a limited capacity in Austin, Texas, on June 22, 2025 and currently operates in Texas in Austin, Dallas and Houston, and in Miami,
Florida.\nThe service represents a key part of Tesla CEO Elon Musk's long-term strategy for the company, which envisions a future where Tesla owners can add their personal vehicles to a shared
autonomous ride-hailing network. The launch in Austin initially operated with a human \"safety monitor\" in the front passenger seat. The launch attracted significant media attention and scrutiny,
with early riders documenting incidents such as the vehicle driving on the wrong side of the road, phantom braking, dropping passengers off in intersections and committing traffic violations that led
to an investigation by the National Highway Traffic Safety Administration.\nTesla plans to have the Robotaxi network work with all current Tesla vehicles, but as of May 2026, the network is composed
of only Model Y vehicles. Tesla plans to add the Cybercab when it begins volume production in mid-2026 with the Model 3, Model S, Model X, and Cybertruck later. During Tesla's October 2024 We, Robot
event it also demonstrated the Robovan which it plans to add to the network, but no timelines were given.", "mode": "full"}
```

## 💭 Thinking



## 💬 Response

Current state (July 21, 2026): The Wikipedia table shows **5 qualifying metros** — Austin, Dallas, Houston, Miami (Full commercial service) + San Francisco Bay Area (Safety-driver service). Four more (Phoenix, Orlando, Tampa, Las Vegas) are "Service announced, 1H 2026" but not yet live.

Let me checkpoint my reasoning.

## 💬 Response

My distribution is close to the factor-implied values. Let me run the premortem.
