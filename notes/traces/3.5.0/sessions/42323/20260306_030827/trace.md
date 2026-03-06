# Reasoning Log: As of April 30, 2026, what will be the cumulative number of people detected arriving in the UK in small boats in 2026?

*Generated: 2026-03-06T03:17:49.833279+00:00*


## 💭 Thinking

Let me analyze this question about cumulative small boat arrivals in the UK from January 1 to April 30, 2026.

Key aspects:
- Resolution based on Home Office small boats time series dataset
- Cumulative total of people detected arriving Jan 1 - Apr 30, 2026
- Options: 0-5,000 / 5,001-10,000 / 10,001-20,000 / 20,001+

I need to research:
1. Historical patterns of small boat arrivals (seasonal patterns, annual totals)
2. Current 2026 data if available
3. Policy changes that might affect numbers


4. Seasonal trends to project Q1-Q2 2026 figures

Now I'm pulling together the historical data on small boat arrivals to establish baseline patterns and see what information is available for early 2026.

## 💬 Response

I'll research this question about UK small boat arrivals systematically.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42323
  ]
}
```

### 📋 Result

```
{"post_id": 42323, "title": "As of April 30, 2026, what will be the cumulative number of people detected arriving in the UK in small boats in 2026?", "type": "multiple_choice", "url":
"https://www.metaculus.com/questions/42323", "background_info": "Cumulative small boat arrivals are a high-salience operational and political metric for UK border policy, asylum processing capacity,
and enforcement strategy.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"443aaf6af8122063\",\"sheet_id\":259.0}}`", "resolution_criteria": "This question resolves to the option
whose range contains the cumulative total number of people detected arriving in the UK in small boats from January 1, 2026 through April 30, 2026 (inclusive), as recorded in the Home Office small
boats time series dataset available before May 1, 2026. The primary source is the Home Office dataset file at
https://assets.publishing.service.gov.uk/media/6793689a5dc1be141475ff84/small_boats_time_series.ods.", "fine_print": "Compute the cumulative total by summing the daily \u201carrivals\u201d (people
detected arriving) values for all dates from January 1, 2026 through April 30, 2026 inclusive, using the values in the primary dataset as available before May 1, 2026. If the dataset is revised after
May 1, 2026, ignore those later revisions. If the primary dataset is unavailable at resolution time, resolve using credible sources per https://www.metaculus.com/faq/#definitions. Candidate Sources:
UK Home Office small boat activity statistics landing page at https://www.gov.uk/government/statistics/small-boat-activity", "num_forecasters": 10, "community_prediction": null, "options":
["0\u20135,000", "5,001\u201310,000", "10,001\u201320,000", "20,001+"]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "UK small boat arrivals 2026 cumulative total Home Office"
}
```

### 📋 Result

```
{"query": "UK small boat arrivals 2026 cumulative total Home Office", "results": [{"title": "English Channel illegal migrant crossings (2018\u2013present) - Wikipedia", "url":
"https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)", "snippet": "An increasing number of refugees and migrants have been entering the United Kingdom by
crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents the shortest sea crossing, and is a long-established shipping
route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover in the English county of Kent, to Cap Gris Nez, a cape near to
Calais in th", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"English Channel illegal migrant crossings (2018\\u2013present)\", \"url\":
\"https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)\", \"extract\": \"An increasing number of refugees and migrants have been entering the United Kingdom
by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents the shortest sea crossing, and is a long-established
shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover in the English county of Kent, to Cap Gris Nez, a
cape near to Calais in the French d\\u00e9partement of Pas-de-Calais.\\nAs of 4 March 2026, the Home Office has detected 195,298 migrants who have crossed the English Channel in small boats since
2018. Crossing the Channel without permission is a criminal offence under UK law, as is to attempt to use a dangerous type of vessel or any unregistered craft under French law. International refugee
law protects most persons who present a particularised claim to seek refugee status (asylum seekers) from being penalised, where their dominant purpose can be shown to be seeking entry to an initial,
or further, safe country.  More than 130 people are confirmed to have died in the northern French marine, as opposed to roads, sector during this period of shift to maritime routes. Many more deaths
of people attempting to enter Europe without prior permission occur on the Mediterranean routes each year.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Small boat activity in the English
Channel - GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats", "snippet": "Small boat activity in the English Channel\nData on
the number of migrants arriving in the UK in small boats and those who were prevented by French authorities from crossing the English Channel.\nDocuments\nDetails\nData on small boat arrivals for the
last 7 days is updated every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to 2018.\nThe figures for French prevention are updated weekly every
Friday. French prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "Weekly summary of small boat arrivals and preventions - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions", "snippet": "Weekly summary of small
boat arrivals and preventions\nUpdated 5 March 2026\nThis page shows the latest consolidated weekly figures for migrants attempting to cross the English Channel in small boats without permission to
enter the UK.\nWeek ending 22 February 2026\n| Migrants arrived | Boats arrived | Migrants prevented | Events prevented |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\nFor users of these statistics\nSee the
latest [press statement](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-stateme", "api_data": null, "hint": null}, {"title": "People crossing the English Channel in small boats - Migration
Observatory", "url": "https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people
crossing the English Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were
detected crossing the English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens
of six countries \u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "605 Small Boat Migrants Arrive in One Day \u2013 Guido Fawkes", "url":
"https://order-order.com/2026/02/26/605-small-boat-migrants-arrive-in-one-day/", "snippet": "New [figures](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-
small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days) from the Home Office confirm that 605 migrants arrived to Britain on ten small boats yesterday. The highest
single-day figure of 2026 so far in the sunshine and low winds\u2026\nAsked about warnings of a civil war in an [interview](https://www.politicshome.com/news/article/danny-kruger-if-dont-win-win-make-
mess", "api_data": null, "hint": null}, {"title": "Small boat arrivals and crossing days: data tables", "url": "https://assets.publishing.service.gov.uk/media/683d9157d23a62e5d32680aa/small-boat-
arrivals-and-crossing-days-data-tables.ods", "snippet": "### Result\n\"\"\n### Ran Playwright code\n```js\nawait page.evaluate('() => document.body.innerText');\n```", "api_data": null, "hint": null},
{"title": "UK border tech budget swells by \u00a3100M as Home Office targets small boat crossings", "url": "https://www.theregister.com/2026/01/24/home_office_small_boats", "snippet": "UK border tech
budget swells by \u00a3100M as Home Office targets small boat crossings\nDrone, satellite, and other data combined to monitor unwanted vessels\nThe UK Home Office is spending up to \u00a3100 million
on intelligence tech in part to tackle the so-called \"small boats\" issue of refugees and irregular immigrants coming across the English Channel.\nThe Whitehall department's Border Security Command
(BSC) is on the hunt for a \"maritime situational awareness system\" it says should \"autonomously detect", "api_data": null, "hint": null}, {"title": "Asylum statistics - House of Commons Library -
UK Parliament", "url": "https://commonslibrary.parliament.uk/research-briefings/sn01403/", "snippet": null, "api_data": null, "hint": null}, {"title": "Latest statement in response to small boat
crossings \u2013 Home Office in the media", "url": "https://homeofficemedia.blog.gov.uk/2026/02/06/latest-statement-in-response-to-small-boat-crossings/", "snippet": "A Home Office spokesperson
said:\n\u201cThis Government is bearing down on small boat crossings.\n\u201cWe have stopped 40,000 crossing attempts since this Government came into office through our joint work with the French. We
have removed or deported almost 60,000 people who were here illegally. Our pilot deal with the French means those who arrive on small boats are now being sent back.\n\u201cThe Home Secretary has also
announced the most sweeping reforms to tackle illegal migration in modern times, removing t", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker | Migration Watch UK", "url":
"https://www.migrationwatchuk.org/channel-crossings-tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s the cost?](#3)\n[What
happens when they arrive?](#4)\n[When is the peak crossing season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum work?](#7)\n[Where do they
come from?](#8)\n[What kind of people are crossing the channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the primary method of illegal
entry to t", "api_data": null, "hint": null}]}
```

```json
{
  "query": "UK small boat crossings 2025 annual total statistics"
}
```

### 📋 Result

```
{"query": "UK small boat crossings 2025 annual total statistics", "results": [{"title": "People crossing the English Channel in small boats - Migration Observatory", "url":
"https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people crossing the English
Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were detected crossing the
English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens of six countries
\u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "Small boat activity in the English Channel - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats", "snippet": "Small boat activity in the English Channel\nData on the number of migrants
arriving in the UK in small boats and those who were prevented by French authorities from crossing the English Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days is updated
every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to 2018.\nThe figures for French prevention are updated weekly every Friday. French
prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker | Migration Watch UK", "url": "https://www.migrationwatchuk.org/channel-crossings-
tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s the cost?](#3)\n[What happens when they arrive?](#4)\n[When is the peak crossing
season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum work?](#7)\n[Where do they come from?](#8)\n[What kind of people are crossing the
channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the primary method of illegal entry to t", "api_data": null, "hint": null}, {"title":
"UK Records 41,000 Small-Boat Arrivals in 2025, Home Office Says", "url": "https://www.visaverge.com/ukimmigration/uk-records-41000-small-boat-arrivals-in-2025-home-office-says/", "snippet": "(UNITED
KINGDOM) \u2014 [The Home Office reported that approximately](https://www.visaverge.com/17/uk-daily-migrant-crossings-peak-at-803-on-dec-20-2025-total-still-below-41000) 41,000 people reached the UK
by small boat in 2025, a tally it described as \u201c\u2018Shameful\u2019\u201d and one of the highest annual counts since records began.\nOverview of 2025 crossings and comparison with recent
years\n![UK Records 41,000 Small-Boat Arrivals in 2025, Home Office Says UK Records 41,000 Small-Boat Arrivals in 2025, Home Of", "api_data": null, "hint": null}, {"title": "English Channel illegal
migrant crossings (2018\u2013present) - Wikipedia", "url": "https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)", "snippet": "An increasing number of
refugees and migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents
the shortest sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover
in the English county of Kent, to Cap Gris Nez, a cape near to Calais in th", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"English Channel illegal migrant crossings
(2018\\u2013present)\", \"url\": \"https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)\", \"extract\": \"An increasing number of refugees and migrants have
been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents the shortest sea crossing,
and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover in the English county of
Kent, to Cap Gris Nez, a cape near to Calais in the French d\\u00e9partement of Pas-de-Calais.\\nAs of 4 March 2026, the Home Office has detected 195,298 migrants who have crossed the English Channel
in small boats since 2018. Crossing the Channel without permission is a criminal offence under UK law, as is to attempt to use a dangerous type of vessel or any unregistered craft under French law.
International refugee law protects most persons who present a particularised claim to seek refugee status (asylum seekers) from being penalised, where their dominant purpose can be shown to be seeking
entry to an initial, or further, safe country.  More than 130 people are confirmed to have died in the northern French marine, as opposed to roads, sector during this period of shift to maritime
routes. Many more deaths of people attempting to enter Europe without prior permission occur on the Mediterranean routes each year.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "UK says small
boat migrant arrivals approached record levels in 2025 - InfoMigrants", "url": "https://www.infomigrants.net/en/post/68994/uk-says-small-boat-migrant-arrivals-approached-record-levels-in-2025",
"snippet": null, "api_data": null, "hint": null}, {"title": "UK Small Boat Migrants Hit 39,292 in 2025", "url": "https://parliamentnews.co.uk/uk-records-longest-period-without-small-boat-migrants-
since-2018", "snippet": "UK (Parliament Politics Magazine) \u2013 UK sees small boat migrant arrivals resume after longest pause since 2018, bringing 39,292 people in 2025, the highest annual total
since 2022.\nAs reported by Sky News, official figures revealed that the [UK](https://parliamentnews.co.uk/uk-news-nationwide) has experienced its longest period in seven years without small boat
migrants crossing the Channel.\nWhat did the Home Office report about Channel migrant crossings?\nAccording to the recent Home Office figur", "api_data": null, "hint": null}, {"title": "Small boat
arrivals and the impact of crossing conditions - GOV.UK", "url": "https://www.gov.uk/government/statistics/small-boat-arrivals-and-the-impact-of-crossing-conditions/small-boat-arrivals-and-the-impact-
of-crossing-conditions", "snippet": "Small boat arrivals and the impact of crossing conditions\nPublished 3 June 2025\nThis note has been produced to provide an overview of the impact of crossing
conditions on small boat arrivals across the English Channel.\nSmall boat arrival numbers are subject to seasonal fluctuations in part due to changes in the weather, typically with peaks in warmer
summer months when crossing conditions are more favourable. Just as small boat arrivals are subject to seasonal variation through any given year, t", "api_data": null, "hint": null}, {"title": "UK
small boat crossings 2024| Statista", "url": "https://www.statista.com/statistics/1171253/small-boat-channel-crossings-in-the-uk/", "snippet": "In 2024, approximately 36,816 people reached the United
Kingdom by crossing the English Channel in a small boat. Attempts to reach the UK via the Channel have increased significantly since 2020, with travel and trade disruptions caused by the COVID-19
pandemic likely one of the main factors.\nAdvertisement\nAdvertisement\nNumber of people detected arriving or heading to the United Kingdom in small boats from 2018 to 2024\nProfit from the additional
features of your individual account\nCurrently, you ", "api_data": null, "hint": "Use search_exa or search_news for statistics and reports."}, {"title": "UK: More than 800 migrants cross Channel,
bringing annual total to more than 41,000 - InfoMigrants", "url": "https://www.infomigrants.net/en/post/68866/uk-more-than-800-migrants-cross-channel-bringing-annual-total-to-more-than-41000",
"snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

Good, I have key data points. Now let me get the detailed 2026 data so far and historical seasonal patterns.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)",
  "prompt": "What are the monthly and annual totals for small boat arrivals for each year from 2020-2026? Include any data on January, February, March, April arrivals specifically. What is the cumulative 2026 total so far?"
}
```

### 📋 Result

```
{"title": "English Channel illegal migrant crossings (2018\u2013present)", "url": "https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)", "extract": "An
increasing number of refugees and migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais
in France represents the shortest sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South
Foreland, northeast of Dover in the English county of Kent, to Cap Gris Nez, a cape near to Calais in the French d\u00e9partement of Pas-de-Calais.\nAs of 4 March 2026, the Home Office has detected
195,298 migrants who have crossed the English Channel in small boats since 2018. Crossing the Channel without permission is a criminal offence under UK law, as is to attempt to use a dangerous type of
vessel or any unregistered craft under French law. International refugee law protects most persons who present a particularised claim to seek refugee status (asylum seekers) from being penalised,
where their dominant purpose can be shown to be seeking entry to an initial, or further, safe country.  More than 130 people are confirmed to have died in the northern French marine, as opposed to
roads, sector during this period of shift to maritime routes. Many more deaths of people attempting to enter Europe without prior permission occur on the Mediterranean routes each year.", "mode":
"full"}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions",
  "prompt": "What are the latest weekly figures for small boat arrivals? What is the 2026 cumulative total so far? Show all weekly data available."
}
```

### 📋 Result

```
{"url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions", "content": "Based on the
content provided:\n\n## Latest Weekly Figures (Week ending 22 February 2026)\n- **Migrants arrived:** 0\n- **Boats arrived:** 0\n- **Migrants prevented:** 0\n- **Events prevented:** 0\n\n## 2026
Cumulative Total\nThe content does not provide cumulative totals for 2026. Only one weekly data point is shown (week ending 22 February 2026).\n\n## All Weekly Data Available\nOnly one week of data is
shown in the provided content:\n- Week ending 22 February 2026: 0 migrants arrived, 0 boats arrived, 0 migrants prevented, 0 events prevented\n\n**Note:** The content indicates this is a weekly
summary page that is updated regularly (last updated 5 March 2026), but only displays the most recent week's figures. Historical weekly data is not included in this summary page.\n\n---\n\n**Relevant
links:**\n- [Press statement on small boat crossings](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-statement-in-response-to-small-boat-crossings/)\n- [Time series of daily arrival numbers
from 1 January 2018 and weekly preventions data from 29 April 2024](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats)\n- [Immigration system
statistics (quarterly release with final authoritative statistics)](https://www.gov.uk/government/collections/immigration-statistics-quarterly-release)\n- [Migrants detected crossing the English
Channel in small boats - monthly data (historic data, 14 April 2022 to 30 January 2023)](https://www.gov.uk/government/statistics/migrants-detected-crossing-the-english-channel-in-small-boats-monthly-
data)", "title": "Weekly summary of small boat arrivals and preventions"}
```

```json
{
  "query": "UK small boat arrivals January February 2026 total number cumulative"
}
```

### 📋 Result

```
{"query": "UK small boat arrivals January February 2026 total number cumulative", "results": [{"title": "People crossing the English Channel in small boats - Migration Observatory", "url":
"https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people crossing the English
Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were detected crossing the
English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens of six countries
\u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "Small boat activity in the English Channel - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats", "snippet": "Small boat activity in the English Channel\nData on the number of migrants
arriving in the UK in small boats and those who were prevented by French authorities from crossing the English Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days is updated
every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to 2018.\nThe figures for French prevention are updated weekly every Friday. French
prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "Weekly summary of small boat arrivals and preventions - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions", "snippet": "Weekly summary of small
boat arrivals and preventions\nUpdated 5 March 2026\nThis page shows the latest consolidated weekly figures for migrants attempting to cross the English Channel in small boats without permission to
enter the UK.\nWeek ending 22 February 2026\n| Migrants arrived | Boats arrived | Migrants prevented | Events prevented |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\nFor users of these statistics\nSee the
latest [press statement](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-stateme", "api_data": null, "hint": null}, {"title": "UK small boat crossings 2024| Statista", "url":
"https://www.statista.com/statistics/1171253/small-boat-channel-crossings-in-the-uk/", "snippet": "In 2024, approximately 36,816 people reached the United Kingdom by crossing the English Channel in a
small boat. Attempts to reach the UK via the Channel have increased significantly since 2020, with travel and trade disruptions caused by the COVID-19 pandemic likely one of the main
factors.\nAdvertisement\nAdvertisement\nNumber of people detected arriving or heading to the United Kingdom in small boats from 2018 to 2024\nProfit from the additional features of your individual
account\nCurrently, you ", "api_data": null, "hint": "Use search_exa or search_news for statistics and reports."}, {"title": "How many people come to the UK via illegal entry routes? - GOV.UK", "url":
"https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-december-2025/how-many-people-come-to-the-uk-via-illegal-entry-routes", "snippet": "How many people come to the UK
via illegal entry routes?\nPublished 26 February 2026\n[Back to \u2018Immigration system statistics, year ending December 2025\u2019 contents
page](https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-december-2025)\nThis release goes up to the year ending (YE) December 2025. The \u201cyear ending\u201d period
includes the 12 months up to and including the YE month. For example, YE December 2025 includes the 12 months between 1 January 2025 and 31 December 2", "api_data": null, "hint": null}, {"title":
"Small boat arrivals: last 7 days - GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-
channel-in-small-boats-last-7-days", "snippet": "Small boat arrivals: last 7 days\nUpdated 5 March 2026\nSmall boats data\nThis page shows figures for the last 7 days for migrants attempting to cross
the English Channel in small boats without permission to enter the UK.\n| Date | Migrants arrived | Boats arrived | Boats involved in uncontrolled landings | Notes |\n|---|---|---|---|---|\n| 26
February 2026 | 0 | 0 | 0 | |\n| 27 February 2026 | 0 | 0 | 0 | |\n| 28 February 2026 | 0 | 0 | 0 | |\n| 1 March 2026 | 0 | 0 | 0 | |\n| 2 March 2026 | 0 | 0 | 0 | ", "api_data": null, "hint": null},
{"title": "How many people come to the UK irregularly? - GOV.UK", "url": "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2025/how-many-people-come-to-the-uk-
irregularly", "snippet": "How many people come to the UK irregularly?\nUpdated 20 October 2025\nBack to [\u2018Immigration system statistics, year ending June
2025\u2019](https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2025) content page.\nThis is not the latest release. [View latest
release](https://www.gov.uk/government/collections/immigration-statistics-quarterly-release).\nData relates to the year ending June 2025 and all comparisons are with the year ending June 2024 (unless
indicated other", "api_data": null, "hint": null}, {"title": "Latest statement in response to small boat crossings \u2013 Home Office in the media", "url":
"https://homeofficemedia.blog.gov.uk/2026/02/06/latest-statement-in-response-to-small-boat-crossings/", "snippet": "A Home Office spokesperson said:\n\u201cThis Government is bearing down on small
boat crossings.\n\u201cWe have stopped 40,000 crossing attempts since this Government came into office through our joint work with the French. We have removed or deported almost 60,000 people who were
here illegally. Our pilot deal with the French means those who arrive on small boats are now being sent back.\n\u201cThe Home Secretary has also announced the most sweeping reforms to tackle illegal
migration in modern times, removing t", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker | Migration Watch UK", "url": "https://www.migrationwatchuk.org/channel-crossings-tracker",
"snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s the cost?](#3)\n[What happens when they arrive?](#4)\n[When is the peak crossing
season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum work?](#7)\n[Where do they come from?](#8)\n[What kind of people are crossing the
channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the primary method of illegal entry to t", "api_data": null, "hint": null}, {"title":
"Migrants detected crossing the English Channel in small ...", "url": "https://assets.publishing.service.gov.uk/media/68fb8733c18f97edd2b637bd/24_October_2025_Small_boats_-_time_series.ods",
"snippet": "### Result\n\"\"\n### Ran Playwright code\n```js\nawait page.evaluate('() => document.body.innerText');\n```", "api_data": null, "hint": null}]}
```

## 💬 Response

Let me get more specific 2026 data and historical monthly patterns.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days",
  "prompt": "What are the daily arrival figures shown? What is the latest date with data?"
}
```

### 📋 Result

```
{"url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days", "content":
"Based on the content, here are the daily arrival figures for the last 7 days:\n\n- **26 February 2026**: 0 migrants, 0 boats\n- **27 February 2026**: 0 migrants, 0 boats\n- **28 February 2026**: 0
migrants, 0 boats\n- **1 March 2026**: 0 migrants, 0 boats\n- **2 March 2026**: 0 migrants, 0 boats\n- **3 March 2026**: 204 migrants, 3 boats\n- **4 March 2026**: 275 migrants, 4 boats\n\n**Latest
date with data**: 4 March 2026\n\nThe page was last updated on 5 March 2026.\n\n**Relevant links:**\n- [Press statement on small boat crossings](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-
statement-in-response-to-small-boat-crossings/)\n- [Time series data from 1 January 2018](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats)\n-
[Weekly small boat preventions data from 29 April 2024](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-
and-preventions)\n- [Immigration system statistics (quarterly release)](https://www.gov.uk/government/collections/immigration-statistics-quarterly-release)\n- [Historic monthly data (April 2022 -
January 2023)](https://www.gov.uk/government/statistics/migrants-detected-crossing-the-english-channel-in-small-boats-monthly-data)", "title": "Small boat arrivals: last 7 days"}
```

```json
{
  "query": "\"small boat\" arrivals 2026 total so far channel crossing tracker cumulative"
}
```

### 📋 Result

```
{"query": "\"small boat\" arrivals 2026 total so far channel crossing tracker cumulative", "results": [{"title": "Migrant crisis: First wave of small boat migrants reach UK in 2026 as dozens cross
Channel in sub-zero temperatures", "url": "https://www.gbnews.com/news/migrant-crisis-small-boats-channel-weather", "snippet": "First wave of small boat migrants reach UK in 2026 as dozens cross
Channel in sub-zero temperatures\n![First wave of small boat migrants reach UK in 2026 as dozens cross Channel in sub-zero temperatures](https://www.gbnews.com/media-library/tom-harwood-rages-over-
britain-s-migrant-crisis-as-he-takes-aim-at-labour-they-say-one-thing-and-doing-another-gb-news.jpg?id=62661516&width=1245&height=700&quality=85&coordinates=0%2C0%2C1%2C0)\nTom Harwood rages over
Britain's migrant crisis as he takes aim a", "api_data": null, "hint": null}, {"title": "Weekly summary of small boat arrivals and preventions - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions", "snippet": "Weekly summary of small
boat arrivals and preventions\nUpdated 5 March 2026\nThis page shows the latest consolidated weekly figures for migrants attempting to cross the English Channel in small boats without permission to
enter the UK.\nWeek ending 22 February 2026\n| Migrants arrived | Boats arrived | Migrants prevented | Events prevented |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\nFor users of these statistics\nSee the
latest [press statement](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-stateme", "api_data": null, "hint": null}, {"title": "People crossing the English Channel in small boats - Migration
Observatory", "url": "https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people
crossing the English Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were
detected crossing the English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens
of six countries \u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "Migrants arrive in Dover for first time this year after Channel crossing | ITV News
Meridian", "url": "https://www.itv.com/news/meridian/2026-01-06/migrants-arrive-in-uk-for-first-time-this-year-after-channel-crossing", "snippet": null, "api_data": null, "hint": null}, {"title":
"Migrant crisis: Britain braces for biggest surge of small boats so far this year as hundreds make their way across the Channel", "url": "https://www.gbnews.com/news/migrant-crisis-britain-small-boat-
crossings-channel", "snippet": "Britain braces for biggest surge of small boats so far this year as hundreds make their way across the Channel\n![Britain braces for biggest surge of small boats so far
this year as hundreds make their way across the Channel](https://www.gbnews.com/media-library/mark-white-delivers-verdict-as-keir-starmer-s-small-boat-record-reaches-highest-level-ever-gb-
news.jpg?id=65016546&width=1245&height=700&quality=85&coordinates=0%2C0%2C1%2C0)\nMark White delivers verdict as Keir Starmer's small boat record", "api_data": null, "hint": null}, {"title": "English
Channel illegal migrant crossings (2018\u2013present) - Wikipedia", "url": "https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)", "snippet": "An increasing
number of refugees and migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France
represents the shortest sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland,
northeast of Dover in the English county of Kent, to Cap Gris Nez, a cape near to Calais in th", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"English Channel illegal migrant
crossings (2018\\u2013present)\", \"url\": \"https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)\", \"extract\": \"An increasing number of refugees and
migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents the shortest
sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover in the
English county of Kent, to Cap Gris Nez, a cape near to Calais in the French d\\u00e9partement of Pas-de-Calais.\\nAs of 4 March 2026, the Home Office has detected 195,298 migrants who have crossed
the English Channel in small boats since 2018. Crossing the Channel without permission is a criminal offence under UK law, as is to attempt to use a dangerous type of vessel or any unregistered craft
under French law. International refugee law protects most persons who present a particularised claim to seek refugee status (asylum seekers) from being penalised, where their dominant purpose can be
shown to be seeking entry to an initial, or further, safe country.  More than 130 people are confirmed to have died in the northern French marine, as opposed to roads, sector during this period of
shift to maritime routes. Many more deaths of people attempting to enter Europe without prior permission occur on the Mediterranean routes each year.\", \"mode\": \"full\"}"}]}, "hint": null},
{"title": "UK: 605 migrants cross the Channel in one day - InfoMigrants", "url": "https://www.infomigrants.net/en/post/70067/uk-605-migrants-cross-the-channel-in-one-day", "snippet": null, "api_data":
null, "hint": null}, {"title": "Small boat activity in the English Channel - GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats",
"snippet": "Small boat activity in the English Channel\nData on the number of migrants arriving in the UK in small boats and those who were prevented by French authorities from crossing the English
Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days is updated every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to
2018.\nThe figures for French prevention are updated weekly every Friday. French prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker |
Migration Watch UK", "url": "https://www.migrationwatchuk.org/channel-crossings-tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s
the cost?](#3)\n[What happens when they arrive?](#4)\n[When is the peak crossing season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum
work?](#7)\n[Where do they come from?](#8)\n[What kind of people are crossing the channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the
primary method of illegal entry to t", "api_data": null, "hint": null}, {"title": "More Than 450 Small Boat Migrants Currently Crossing Channel \u2013 Guido Fawkes", "url": "https://order-
order.com/2026/02/25/more-than-450-small-boat-migrants-currently-crossing-channel/", "snippet": "According to [GB News](https://x.com/markwhiteTV), more than 450 small boat migrants are currently
attempting to make the journey across the channel. A total of ten boats departed from French beaches this morning, with smuggling gangs taking advantage of today\u2019s calmer waters. The biggest
surge in migrant crossings of the year so far\u2026\nAsked about warnings of a civil war in an [interview](https://www.politicshome.com/news/article/danny-kruger-if-dont-win-win-make-mess-it-fear-
country) with The Ho", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.migrationwatchuk.org/channel-crossings-tracker",
  "prompt": "What are the 2026 small boat arrival numbers? What is the cumulative total for 2026 so far? Monthly breakdown for Jan and Feb 2026?"
}
```

### 📋 Result

```
{"url": "https://www.migrationwatchuk.org/channel-crossings-tracker", "content": "The content does not contain any information about 2026 small boat arrival numbers. \n\nThe most recent data
referenced in the text is from 2025, which mentions that the 10,000 mark was reached before the end of April 2025. There is no monthly breakdown for January and February 2026, nor any cumulative total
for 2026.\n\nThe text only provides historical data up to 2024 and partial 2025 figures.\n\nRelevant links:\n- [Most recent government data on migrants detected crossing the English
Channel](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats)\n- [Past data published by the Ministry of
Defence](https://www.gov.uk/government/statistical-data-sets/migrants-detected-crossing-the-english-channel-in-small-boats)\n- [Overall irregular migration
statistics](https://www.gov.uk/government/collections/irregular-migration-to-the-uk-statistics)", "title": "Channel Crossing Tracker"}
```

## 💭 Thinking

Let me gather more data on the historical monthly patterns and the 2026 cumulative total so far. I need to understand:

1. What's the 2026 total so far (through early March)?
2. Historical Jan-Apr totals for previous years
3. Seasonal patterns

From what I've gathered:
- 2025 annual total: ~41,000 (13% increase on 2024's ~36,816)
- 2024 annual total: ~36,816
- 2022 was higher than 2025 (so >41,000)
- The 10,000 mark was reached before end of April 2025


- 2026 is showing a pattern of minimal winter activity with sporadic spikes—the Feb 25-26 period saw the year's highest single day at 605 arrivals, followed by another uptick in early March with 204 and 275 arrivals on consecutive days, while the rest of January and February remained quiet.

I should pull the Wikipedia monthly breakdown to get a clearer picture of seasonal trends and find the cumulative 2026 figures.

## 💬 Response

Let me get historical monthly data to understand the seasonal pattern and compute Jan-Apr totals for past years.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "UK small boat arrivals monthly breakdown 2022 2023 2024 2025 January February March April"
}
```

### 📋 Result

```
{"query": "UK small boat arrivals monthly breakdown 2022 2023 2024 2025 January February March April", "results": [{"title": "Small boat arrivals: last 7 days - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/migrants-detected-crossing-the-english-channel-in-small-boats-last-7-days", "snippet": "Small
boat arrivals: last 7 days\nUpdated 5 March 2026\nSmall boats data\nThis page shows figures for the last 7 days for migrants attempting to cross the English Channel in small boats without permission
to enter the UK.\n| Date | Migrants arrived | Boats arrived | Boats involved in uncontrolled landings | Notes |\n|---|---|---|---|---|\n| 26 February 2026 | 0 | 0 | 0 | |\n| 27 February 2026 | 0 | 0 |
0 | |\n| 28 February 2026 | 0 | 0 | 0 | |\n| 1 March 2026 | 0 | 0 | 0 | |\n| 2 March 2026 | 0 | 0 | 0 | ", "api_data": null, "hint": null}, {"title": "How many people come to the UK irregularly? -
GOV.UK", "url": "https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-june-2025/how-many-people-come-to-the-uk-irregularly", "snippet": "How many people come to the UK
irregularly?\nUpdated 20 October 2025\nBack to [\u2018Immigration system statistics, year ending June 2025\u2019](https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-
june-2025) content page.\nThis is not the latest release. [View latest release](https://www.gov.uk/government/collections/immigration-statistics-quarterly-release).\nData relates to the year ending
June 2025 and all comparisons are with the year ending June 2024 (unless indicated other", "api_data": null, "hint": null}, {"title": "Small boat arrivals and the impact of crossing conditions -
GOV.UK", "url": "https://www.gov.uk/government/statistics/small-boat-arrivals-and-the-impact-of-crossing-conditions/small-boat-arrivals-and-the-impact-of-crossing-conditions", "snippet": "Small boat
arrivals and the impact of crossing conditions\nPublished 3 June 2025\nThis note has been produced to provide an overview of the impact of crossing conditions on small boat arrivals across the English
Channel.\nSmall boat arrival numbers are subject to seasonal fluctuations in part due to changes in the weather, typically with peaks in warmer summer months when crossing conditions are more
favourable. Just as small boat arrivals are subject to seasonal variation through any given year, t", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker | Migration Watch UK", "url":
"https://www.migrationwatchuk.org/channel-crossings-tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s the cost?](#3)\n[What
happens when they arrive?](#4)\n[When is the peak crossing season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum work?](#7)\n[Where do they
come from?](#8)\n[What kind of people are crossing the channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the primary method of illegal
entry to t", "api_data": null, "hint": null}, {"title": "Small boat arrivals and crossing days: data tables", "url": "https://assets.publishing.service.gov.uk/media/683d9157d23a62e5d32680aa/small-
boat-arrivals-and-crossing-days-data-tables.ods", "snippet": "### Result\n\"\"\n### Ran Playwright code\n```js\nawait page.evaluate('() => document.body.innerText');\n```", "api_data": null, "hint":
null}, {"title": "People crossing the English Channel in small boats - Migration Observatory", "url": "https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-
small-boats/", "snippet": "This briefing examines the phenomenon of people crossing the English Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of
people making this journey.\n-\nKey Points\n- Around 41,000 people were detected crossing the English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in
2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens of six countries \u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint":
null}, {"title": "BRIEFING www.migrationobservatory.ox.ac.uk AUTHORS: \u0007Peter William Walsh", "url": "https://migrationobservatory.ox.ac.uk/wp-content/uploads/2023/07/2025-Briefing-People-
crossing-the-English-Channel-in-small-boats.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "UK Records 41,000 Small-Boat Arrivals in 2025, Home Office Says", "url":
"https://www.visaverge.com/ukimmigration/uk-records-41000-small-boat-arrivals-in-2025-home-office-says/", "snippet": "(UNITED KINGDOM) \u2014 [The Home Office reported that
approximately](https://www.visaverge.com/17/uk-daily-migrant-crossings-peak-at-803-on-dec-20-2025-total-still-below-41000) 41,000 people reached the UK by small boat in 2025, a tally it described as
\u201c\u2018Shameful\u2019\u201d and one of the highest annual counts since records began.\nOverview of 2025 crossings and comparison with recent years\n![UK Records 41,000 Small-Boat Arrivals in
2025, Home Office Says UK Records 41,000 Small-Boat Arrivals in 2025, Home Of", "api_data": null, "hint": null}, {"title": "Asylum statistics - House of Commons Library - UK Parliament", "url":
"https://commonslibrary.parliament.uk/research-briefings/sn01403/", "snippet": null, "api_data": null, "hint": null}, {"title": "United Kingdom: International Migration Outlook 2024 | OECD", "url":
"https://www.oecd.org/en/publications/2024/11/international-migration-outlook-2024_c6f3e803/full-report/united-kingdom_7b8a1eb9.html", "snippet": null, "api_data": null, "hint": null}, {"title":
"Weekly summary of small boat arrivals and preventions - GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-
small-boat-arrivals-and-preventions", "snippet": "Weekly summary of small boat arrivals and preventions\nUpdated 5 March 2026\nThis page shows the latest consolidated weekly figures for migrants
attempting to cross the English Channel in small boats without permission to enter the UK.\nWeek ending 22 February 2026\n| Migrants arrived | Boats arrived | Migrants prevented | Events prevented
|\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\nFor users of these statistics\nSee the latest [press statement](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-stateme", "api_data": null, "hint":
null}, {"title": "English Channel illegal migrant crossings (2018\u2013present) - Wikipedia", "url": "https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)",
"snippet": "An increasing number of refugees and migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in
England and Calais in France represents the shortest sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from
the South Foreland, northeast of Dover in the English county of Kent, to Cap Gris Nez, a cape near to Calais in th", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"English Channel
illegal migrant crossings (2018\\u2013present)\", \"url\": \"https://en.wikipedia.org/wiki/English_Channel_illegal_migrant_crossings_(2018%E2%80%93present)\", \"extract\": \"An increasing number of
refugees and migrants have been entering the United Kingdom by crossing the English Channel (La Manche) since 2018. The Strait of Dover section between Dover in England and Calais in France represents
the shortest sea crossing, and is a long-established shipping route. The shortest distance across the strait, at approximately 20 miles (32 kilometres), is from the South Foreland, northeast of Dover
in the English county of Kent, to Cap Gris Nez, a cape near to Calais in the French d\\u00e9partement of Pas-de-Calais.\\nAs of 4 March 2026, the Home Office has detected 195,298 migrants who have
crossed the English Channel in small boats since 2018. Crossing the Channel without permission is a criminal offence under UK law, as is to attempt to use a dangerous type of vessel or any
unregistered craft under French law. International refugee law protects most persons who present a particularised claim to seek refugee status (asylum seekers) from being penalised, where their
dominant purpose can be shown to be seeking entry to an initial, or further, safe country.  More than 130 people are confirmed to have died in the northern French marine, as opposed to roads, sector
during this period of shift to maritime routes. Many more deaths of people attempting to enter Europe without prior permission occur on the Mediterranean routes each year.\", \"mode\": \"full\"}"}]},
"hint": null}, {"title": "Small boat activity in the English Channel - GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats",
"snippet": "Small boat activity in the English Channel\nData on the number of migrants arriving in the UK in small boats and those who were prevented by French authorities from crossing the English
Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days is updated every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to
2018.\nThe figures for French prevention are updated weekly every Friday. French prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "Channel: Record Number of People
Make Crossings in Small Boats in First Three Months of 2024 as Home Office Launches New Social Media Campaign in Effort to Deter Channel Crossings \u2015 Footage Shows UK-Funded French Police
Employing \u2018Textbook Pushback\u2019 Tactics Against Small Boats | European Council on Refugees and Exiles (ECRE)", "url": "https://ecre.org/channel-record-number-of-people-make-crossings-in-small-
boats-in-first-three-months-of-2024-as-home-office-launches-new-social-media-campaign-in-effort-to-deter-channel-crossings-%E2%80%95-footage-sh/", "snippet": "- Provisional data from the UK Home
Office has shown that a record 4644 people crossed the Channel in small boats in the first three months of 2024.\n- The UK government has launched a new social media campaign in Vietnam as part of its
efforts to reduce the number of people crossing the Channel in small boats.\n- A recent investigation shows the UK-funded French police carrying out life-threatening manoeuvres and pullbacks against
migrant boats.\nNew statistics published by the UK Home Office have", "api_data": null, "hint": null}, {"title": "Channel Crossings Timeline", "url": "https://channelcrossings.org/home-2/timeline/",
"snippet": "OKJEK21 - Bandar Link Situs Slot Gacor Maxwin Hari Ini dan Slot88 Paling Gampang Menang\nOKJEK21 - Bandar Link Situs Slot Gacor Maxwin Hari Ini dan Slot88 Paling Gampang Menang\n$88.00
SGD\nUnit price per[Shipping](https://cornishfoodie.com/policies/shipping-policy)calculated at checkout.\nor\n[Pelajari Selengkapnya]\nProtection+ for OKJEK21 (1 year plan)\nGet it
fast\nPickup\nLoading store\nError loading\n![OKJEK21 - Bandar Link Situs Slot Gacor Maxwin Hari Ini dan Slot88 Paling Gampang Menang](/assets/ba", "api_data": null, "hint": null}, {"title": "UK small
boat crossings 2024| Statista", "url": "https://www.statista.com/statistics/1171253/small-boat-channel-crossings-in-the-uk/", "snippet": "In 2024, approximately 36,816 people reached the United
Kingdom by crossing the English Channel in a small boat. Attempts to reach the UK via the Channel have increased significantly since 2020, with travel and trade disruptions caused by the COVID-19
pandemic likely one of the main factors.\nAdvertisement\nAdvertisement\nNumber of people detected arriving or heading to the United Kingdom in small boats from 2018 to 2024\nProfit from the additional
features of your individual account\nCurrently, you ", "api_data": null, "hint": "Use search_exa or search_news for statistics and reports."}, {"title": "commonslibrary.parliament.uk By Esme Kirk-Wade
2 March 2026 Asylum statistics", "url": "https://researchbriefings.files.parliament.uk/documents/SN01403/SN01403.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Migration and the
asylum system statistics \u2013 Office for Statistics Regulation", "url": "https://osr.statisticsauthority.gov.uk/guidance/2026-what-to-look-out-for-migration-and-the-asylum-system-statistics/",
"snippet": "Summary\nThere are two main sources of official statistics for migration:\nThe Office for National Statistics\u2019 (ONS) [Long-term international migration
statistics](https://www.ons.gov.uk/peoplepopulationandcommunity/populationandmigration/internationalmigration/bulletins/longterminternationalmigrationprovisional/yearendingjune2025) estimate the
number of people entering and leaving the UK for 12 months or more. These statistics are published every six months with a five-month lag. They coincide wi", "api_data": null, "hint": null}, {"title":
"Boatwatch UK - daily, weekly and monthly small boat arrivals to March 2026", "url": "https://boatwatch.uk/", "snippet": "Welcome to Boatwatch. This website takes the daily small boat migrant crossing
figures supplied by the Home Office, and presents that as convenient and easy to understand graphs together with some additional data that you won't find anywhere else.\nYou can read more about the
rational behind this website at [About This Website](https://boatwatch.uk/page/about-this-website), and\nmore about the data we're using and what we're doing with it at [About the
Data](https://boatwatch.uk/page/about-the-dat", "api_data": null, "hint": null}, {"title": "Top facts from the latest statistics on refugees and people seeking asylum - Refugee Council", "url":
"https://www.refugeecouncil.org.uk/stay-informed/explainers/top-facts-from-the-latest-statistics-on-refugees-and-people-seeking-asylum/", "snippet": "Top facts from the latest statistics on refugees
and people seeking asylum\nHere are our top facts based on the UK Government's latest immigration statistics for the year ending September 2025.\nTop facts from the latest statistics on refugees and
people seeking asylum\nasylum applications (relating to 110,051 people) in the UK in the year to September 2025\n1. The number of people seeking asylum in the UK has increased\nThere were 89,509
asylum applications (relating to 110,051 people) in the UK in ", "api_data": null, "hint": null}, {"title": "Summary of latest statistics - GOV.UK", "url":
"https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-december-2025/summary-of-latest-statistics", "snippet": "Summary of latest statistics\nPublished 26 February
2026\n[Back to \u2018Immigration system statistics, year ending December 2025\u2019 contents page](https://www.gov.uk/government/statistics/immigration-system-statistics-year-ending-
december-2025)\nThis Accredited Official Statistics publication provides comprehensive statistics on the operation of the UK immigration system.\nThe UK immigration system undertakes a wide range of
activities including issuing visas to those outside of the UK, changes to visas, ", "api_data": null, "hint": null}]}
```

```json
{
  "query": "small boat channel crossings 2026 cumulative 1000 2000 total year"
}
```

### 📋 Result

```
{"query": "small boat channel crossings 2026 cumulative 1000 2000 total year", "results": [{"title": "Migrant crisis: First wave of small boat migrants reach UK in 2026 as dozens cross Channel in sub-
zero temperatures", "url": "https://www.gbnews.com/news/migrant-crisis-small-boats-channel-weather", "snippet": "First wave of small boat migrants reach UK in 2026 as dozens cross Channel in sub-zero
temperatures\n![First wave of small boat migrants reach UK in 2026 as dozens cross Channel in sub-zero temperatures](https://www.gbnews.com/media-library/tom-harwood-rages-over-britain-s-migrant-
crisis-as-he-takes-aim-at-labour-they-say-one-thing-and-doing-another-gb-news.jpg?id=62661516&width=1245&height=700&quality=85&coordinates=0%2C0%2C1%2C0)\nTom Harwood rages over Britain's migrant
crisis as he takes aim a", "api_data": null, "hint": null}, {"title": "Starmer Warned of Alarming Record in Channel Crossings - London Business News | Londonlovesbusiness.com", "url":
"https://londonlovesbusiness.com/starmer-warned-channel-crossings-could-hit-record-levels-this-year/", "snippet": "Sir Keir Starmer has been cautioned about an alarming trend: small boat crossings
across the Channel could hit record levels this year, as new arrivals have already pushed the 2026 total past 2,000.\nIn a compelling interview with GB News, human rights lawyer David Haigh emphasised
the urgency of the situation, asserting that this year\u2019s figures are on track to be \u201crecord-breaking.\u201d\nRecent footage from GB News vividly illustrated the plight of migrants being
brought ashore at the Port of Ramsgate", "api_data": null, "hint": null}, {"title": "More Than 450 Small Boat Migrants Currently Crossing Channel \u2013 Guido Fawkes", "url": "https://order-
order.com/2026/02/25/more-than-450-small-boat-migrants-currently-crossing-channel/", "snippet": "According to [GB News](https://x.com/markwhiteTV), more than 450 small boat migrants are currently
attempting to make the journey across the channel. A total of ten boats departed from French beaches this morning, with smuggling gangs taking advantage of today\u2019s calmer waters. The biggest
surge in migrant crossings of the year so far\u2026\nHome Secretary Shabana Mahmood introduced her speech on migration reforms at the IPPR:\n\u201cThere\u2019s no denying we meet at a difficult time
for my party.\u201d", "api_data": null, "hint": null}, {"title": "People crossing the English Channel in small boats - Migration Observatory", "url":
"https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people crossing the English
Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were detected crossing the
English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens of six countries
\u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "Migrant crisis: Britain braces for biggest surge of small boats so far this year as hundreds make
their way across the Channel", "url": "https://www.gbnews.com/news/migrant-crisis-britain-small-boat-crossings-channel", "snippet": "Britain braces for biggest surge of small boats so far this year as
hundreds make their way across the Channel\n![Britain braces for biggest surge of small boats so far this year as hundreds make their way across the Channel](https://www.gbnews.com/media-library/mark-
white-delivers-verdict-as-keir-starmer-s-small-boat-record-reaches-highest-level-ever-gb-news.jpg?id=65016546&width=1245&height=700&quality=85&coordinates=0%2C0%2C1%2C0)\nMark White delivers verdict
as Keir Starmer's small boat record", "api_data": null, "hint": null}, {"title": "Migrants arrive in Dover for first time this year after Channel crossing | ITV News Meridian", "url":
"https://www.itv.com/news/meridian/2026-01-06/migrants-arrive-in-uk-for-first-time-this-year-after-channel-crossing", "snippet": null, "api_data": null, "hint": null}, {"title": "Latest statement in
response to small boat crossings \u2013 Home Office in the media", "url": "https://homeofficemedia.blog.gov.uk/2026/02/06/latest-statement-in-response-to-small-boat-crossings/", "snippet": "A Home
Office spokesperson said:\n\u201cThis Government is bearing down on small boat crossings.\n\u201cWe have stopped 40,000 crossing attempts since this Government came into office through our joint work
with the French. We have removed or deported almost 60,000 people who were here illegally. Our pilot deal with the French means those who arrive on small boats are now being sent back.\n\u201cThe Home
Secretary has also announced the most sweeping reforms to tackle illegal migration in modern times, removing t", "api_data": null, "hint": null}, {"title": "Channel Crossing Tracker | Migration Watch
UK", "url": "https://www.migrationwatchuk.org/channel-crossings-tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the Channel?](#2)\n[What\u2019s the
cost?](#3)\n[What happens when they arrive?](#4)\n[When is the peak crossing season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How does claiming asylum
work?](#7)\n[Where do they come from?](#8)\n[What kind of people are crossing the channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English Channel has become the
primary method of illegal entry to t", "api_data": null, "hint": null}, {"title": "UK: 605 migrants cross the Channel in one day - InfoMigrants", "url":
"https://www.infomigrants.net/en/post/70067/uk-605-migrants-cross-the-channel-in-one-day", "snippet": null, "api_data": null, "hint": null}, {"title": "Small boat activity in the English Channel -
GOV.UK", "url": "https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats", "snippet": "Small boat activity in the English Channel\nData on the number
of migrants arriving in the UK in small boats and those who were prevented by French authorities from crossing the English Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days
is updated every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to 2018.\nThe figures for French prevention are updated weekly every Friday.
French prevention activity includes individuals", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/",
  "prompt": "What are the monthly arrival numbers for each year? Specifically looking for January through April data for 2022, 2023, 2024, and 2025. What is the seasonal pattern? How many arrived in Q1 each year?"
}
```

### 📋 Result

```
{"url": "https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "content": "Based on the content provided, **specific monthly arrival numbers
are not included in this briefing**. The document only provides:\n\n**Annual totals:**\n- 2022: ~46,000 (highest on record)\n- 2023: Not specified\n- 2024: ~36,500 (implied from \"41,000 in 2025 was
13% more than 2024\")\n- 2025: ~41,500\n- January 2026: ~1,000 (noted as \"similar to previous years\")\n\n**Seasonal pattern mentioned:**\nThe briefing states that \"Arrivals increased between the
autumn of 2024 and the summer of 2025 before falling slightly in the last months of the year,\" but does not provide Q1-specific data or detailed monthly breakdowns for any year.\n\nThe document does
not contain the January-April data or Q1 totals you requested.\n\n**Relevant links:**\n- [Home Office Immigration System Statistics Quarterly
Release](https://www.gov.uk/government/publications/source-of-asylum-claims-in-2024/source-of-asylum-claims-
in-2024#:~:text=Internally%20matched%20data%20shows%20that,11%2C500)%20had%20a%20work%20visa) - May contain more detailed monthly statistics\n- [UNHCR Europe Sea Arrivals
Data](https://data.unhcr.org/en/situations/europe-sea-arrivals) - For comparative European data", "title": "People crossing the English Channel in small boats - Migration Observatory"}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://boatwatch.uk/",
  "prompt": "What are the 2026 cumulative arrival totals? Monthly totals for January and February 2026? Any comparison data with prior years Jan-Apr?"
}
```

### 📋 Result

```
{"url": "https://boatwatch.uk/", "content": "Based on the content provided, I cannot determine the 2026 cumulative arrival totals, monthly totals for January and February 2026, or any comparison data
with prior years for Jan-Apr.\n\nThe content only shows:\n- Daily data for the first few days of March 2026 (March 1-4, 2026)\n- March 1-4 totals: 479 migrants across 7 boats\n- No January or February
2026 data is displayed\n- No year-over-year comparison data is shown in this excerpt\n\nThe website mentions that \"Monthly crossings and yearly comparisons have additional data,\" but this specific
information is not included in the text content provided.\n\n**Relevant links:**\n- [About This Website](https://boatwatch.uk/page/about-this-website)\n- [About the
Data](https://boatwatch.uk/page/about-the-data)", "title": "Boatwatch"}
```

```json
{
  "url": "https://londonlovesbusiness.com/starmer-warned-channel-crossings-could-hit-record-levels-this-year/",
  "prompt": "What is the cumulative 2026 small boat arrival total mentioned? When was this article published? What specific numbers are cited?"
}
```

### 📋 Result

```
{"url": "https://londonlovesbusiness.com/starmer-warned-channel-crossings-could-hit-record-levels-this-year/", "content": "Based on the content provided:\n\n**2026 small boat arrival total:** The
article states that with Wednesday's arrivals, the 2026 total exceeded 2,000. This surpasses numbers recorded at the same point in 2024 and 2025.\n\n**Publication date:** Not explicitly stated in the
content provided.\n\n**Specific numbers cited:**\n- 2026 total: Over 2,000 (as of the Wednesday referenced)\n- At least 10 boats departed from northern French beaches on Wednesday\n- Government claims
to have stopped 40,000 crossing attempts since taking office\n- Almost 60,000 people removed or deported who were here illegally\n- One asylum claim mentioned lasted up to 10 years\n\n**Relevant
links:**\n- [French unions block proposals for border patrols to intercept migrant boats](https://londonlovesbusiness.com/french-unions-block-proposals-for-border-patrols-to-intercept-migrant-
boats/)\n- [Grant Thornton research highlights record number of Indian owned businesses in the UK](https://londonlovesbusiness.com/grant-thornton-research-highlights-record-number-of-indian-owned-
businesses-in-the-uk/)\n- [Starmer urged to pause EU fishing surrender until France stops the small boats](https://londonlovesbusiness.com/starmer-urged-to-pause-eu-fishing-surrender-until-france-
stops-the-small-boats/)\n- [The Home Office to launch an appeal amid High Court blocking migrant deportation](https://londonlovesbusiness.com/the-home-office-to-launch-an-appeal-amid-high-court-
blocking-migrant-deportation/)", "title": "Starmer Warned of Alarming Record in Channel Crossings - London Business News | Londonlovesbusiness.com"}
```

```json
{
  "query": "boatwatch.uk 2026 cumulative arrivals January April monthly chart"
}
```

### 📋 Result

```
{"query": "boatwatch.uk 2026 cumulative arrivals January April monthly chart", "results": [{"title": "Boatwatch UK - daily, weekly and monthly small boat arrivals to March 2026", "url":
"https://boatwatch.uk/", "snippet": "Welcome to Boatwatch. This website takes the daily small boat migrant crossing figures supplied by the Home Office, and presents that as convenient and easy to
understand graphs together with some additional data that you won't find anywhere else.\nYou can read more about the rational behind this website at [About This
Website](https://boatwatch.uk/page/about-this-website), and\nmore about the data we're using and what we're doing with it at [About the Data](https://boatwatch.uk/page/about-the-dat", "api_data":
null, "hint": null}, {"title": "Boatwatch UK - Weekly small boat arrivals to October 2025", "url": "https://boatwatch.uk/weekly", "snippet": "This page is very graph-heavy, which will look better with
your fondleslab in landscape mode.\nShow graph for:\nUse the slider underneath the graph to zoom in on dates\nFor more information on the data and what it represents, see [About the
Data](https://boatwatch.uk/page/about-the-data).\n| Week Ending | Migrants | Boats | Migrants Prevented | Events Prevented |\n|---|---|---|---|---|\n| Sunday 22 February 2026 | 0 | 0 | 0 | 0 |\n|
Sunday 15 February 2026 | 322 | 5 | 72 | 5 |\n| Sunday 8 February 2026 ", "api_data": null, "hint": null}, {"title": "Small boat activity in the English Channel - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats", "snippet": "Small boat activity in the English Channel\nData on the number of migrants
arriving in the UK in small boats and those who were prevented by French authorities from crossing the English Channel.\nDocuments\nDetails\nData on small boat arrivals for the last 7 days is updated
every day.\nThe time series for small boat arrivals is updated weekly on Friday. The time series goes back to 2018.\nThe figures for French prevention are updated weekly every Friday. French
prevention activity includes individuals", "api_data": null, "hint": null}, {"title": "People crossing the English Channel in small boats - Migration Observatory", "url":
"https://migrationobservatory.ox.ac.uk/resources/briefings/people-crossing-the-english-channel-in-small-boats/", "snippet": "This briefing examines the phenomenon of people crossing the English
Channel in small boats. It reviews what we know about the numbers, characteristics, and motivations of people making this journey.\n-\nKey Points\n- Around 41,000 people were detected crossing the
English Channel in small boats in 2025, a 13% increase on 2024 but fewer than in 2022.\n[More\u2026](https://migrationobservatory.ox.ac.uk#kp1) - Between 2018 and 2024, citizens of six countries
\u2013 Iran, Afghanistan, Iraq, Albania, Syria, and E", "api_data": null, "hint": null}, {"title": "Weekly summary of small boat arrivals and preventions - GOV.UK", "url":
"https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats/weekly-summary-of-small-boat-arrivals-and-preventions", "snippet": "Weekly summary of small
boat arrivals and preventions\nUpdated 5 March 2026\nThis page shows the latest consolidated weekly figures for migrants attempting to cross the English Channel in small boats without permission to
enter the UK.\nWeek ending 22 February 2026\n| Migrants arrived | Boats arrived | Migrants prevented | Events prevented |\n|---|---|---|---|\n| 0 | 0 | 0 | 0 |\nFor users of these statistics\nSee the
latest [press statement](https://homeofficemedia.blog.gov.uk/2023/01/31/latest-stateme", "api_data": null, "hint": null}, {"title": "Small boat arrivals and the impact of crossing conditions -
GOV.UK", "url": "https://www.gov.uk/government/statistics/small-boat-arrivals-and-the-impact-of-crossing-conditions/small-boat-arrivals-and-the-impact-of-crossing-conditions", "snippet": "Small boat
arrivals and the impact of crossing conditions\nPublished 3 June 2025\nThis note has been produced to provide an overview of the impact of crossing conditions on small boat arrivals across the English
Channel.\nSmall boat arrival numbers are subject to seasonal fluctuations in part due to changes in the weather, typically with peaks in warmer summer months when crossing conditions are more
favourable. Just as small boat arrivals are subject to seasonal variation through any given year, t", "api_data": null, "hint": null}, {"title": "Academic Registry Page 1 of 2 5 November 2025", "url":
"https://www.bath.ac.uk/publications/academic-year-charts/attachments/academic-year-chart-for-january-2026-intake.pdf", "snippet": null, "api_data": null, "hint": null}, {"title": "Channel Crossing
Tracker | Migration Watch UK", "url": "https://www.migrationwatchuk.org/channel-crossings-tracker", "snippet": "Channel Crossing Tracker\n[How many people are illegally crossing the
Channel?](#2)\n[What\u2019s the cost?](#3)\n[What happens when they arrive?](#4)\n[When is the peak crossing season?](#5)\n[How successful have attempts to \u2018stop the boats\u2019 been?](#6)\n[How
does claiming asylum work?](#7)\n[Where do they come from?](#8)\n[What kind of people are crossing the channel?](#8b)\n[How many get returned to their home country or elsewhere?](#9)\nThe English
Channel has become the primary method of illegal entry to t", "api_data": null, "hint": null}, {"title": "UK small boat crossings 2024| Statista", "url":
"https://www.statista.com/statistics/1171253/small-boat-channel-crossings-in-the-uk/", "snippet": "In 2024, approximately 36,816 people reached the United Kingdom by crossing the English Channel in a
small boat. Attempts to reach the UK via the Channel have increased significantly since 2020, with travel and trade disruptions caused by the COVID-19 pandemic likely one of the main
factors.\nAdvertisement\nAdvertisement\nNumber of people detected arriving or heading to the United Kingdom in small boats from 2018 to 2024\nProfit from the additional features of your individual
account\nCurrently, you ", "api_data": null, "hint": "Use search_exa or search_news for statistics and reports."}, {"title": "Migrant Data UK | Small Boat Arrivals", "url":
"https://migrantdata.uk/small-boat-arrivals/", "snippet": "Small boat activity in the English Channel\nThis page displays data comparing small boat arrivals to the UK in 2025 and 2026.\n[ Small Boat
Arrivals # ](https://migrantdata.uk#small-boat-arrivals)\nThe data below represents amount of individual arrivals, not amount of boats.\n- Last sync:\n- Source:\n-\n[GOV.UK | Migrants detected
crossing the English Channel in small boats \u2013 time series](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats) - 27_Febr", "api_data": null,
"hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://boatwatch.uk/weekly",
  "prompt": "List all weekly data for 2026 and late 2025. Show the full table of weekly arrivals with dates and migrant numbers."
}
```

### 📋 Result

```
{"url": "https://boatwatch.uk/weekly", "content": "Based on the provided content, here is the complete table of weekly data showing all weeks from late 2025 through early 2026:\n\n| Week Ending |
Migrants | Boats | Migrants Prevented | Events Prevented |\n|---|---|---|---|---|\n| Sunday 22 February 2026 | 0 | 0 | 0 | 0 |\n| Sunday 15 February 2026 | 322 | 5 | 72 | 5 |\n| Sunday 8 February 2026
| 275 | 4 | 48 | 4 |\n| Sunday 1 February 2026 | 0 | 0 | 83 | 6 |\n| Sunday 25 January 2026 | 275 | 4 | 185 | 6 |\n| Sunday 18 January 2026 | 626 | 10 | 789 | 23 |\n| Sunday 11 January 2026 | 32 | 1 |
92 | 3 |\n| Sunday 4 January 2026 | 0 | 0 | 0 | 0 |\n| Sunday 28 December 2025 | 17 | 1 | 0 | 1 |\n| Sunday 21 December 2025 | 1,374 | 23 | 430 | 10 |\n| Sunday 14 December 2025 | 789 | 12 | 383 | 14
|\n| Sunday 7 December 2025 | 0 | 0 | 438 | 11 |\n| Sunday 30 November 2025 | 0 | 0 | 0 | 0 |\n| Sunday 23 November 2025 | 0 | 0 | 0 | 0 |\n| Sunday 16 November 2025 | 217 | 3 | 208 | 12 |\n| Sunday 9
November 2025 | 2,121 | 30 | 784 | 20 |\n\n**Key observations:**\n- The most recent week (Feb 22, 2026) shows no arrivals\n- Highest migrant arrivals in this period: 2,121 (Nov 9, 2025)\n- Multiple
weeks with zero arrivals throughout late 2025 and early 2026\n\n**Relevant links:**\n- [About the Data](https://boatwatch.uk/page/about-the-data)", "title": "Weekly small boat arrivals"}
```

```json
{
  "url": "https://migrantdata.uk/small-boat-arrivals/",
  "prompt": "What is the cumulative total of small boat arrivals for 2026? Any comparison with 2025 at the same point? Monthly or weekly breakdown?"
}
```

### 📋 Result

```
{"url": "https://migrantdata.uk/small-boat-arrivals/", "content": "Based on the content provided:\n\n**Cumulative total for 2026 (current year):** ~2,209 arrivals\n\n**Comparison with 2025 (last year)
at the same point:** \n- 2025: 2,056 arrivals\n- 2026: ~2,209 arrivals\n- Difference: ~153 more arrivals (+7%)\n\n**Weekly breakdown for 2026:**\n- Week ending Sun, 22 Feb: ~0\n- Week ending Sun, 15
Feb: ~322\n- Week ending Sun, 8 Feb: ~275\n- Week ending Sun, 1 Feb: ~0\n- Week ending Sun, 25 Jan: ~275\n- Week ending Sun, 18 Jan: ~626\n- Week ending Sun, 11 Jan: ~32\n- Week ending Sun, 4 Jan:
~0\n\n**Note:** The content does not provide a monthly breakdown, only weekly data. The figures for 2026 are marked with \"~\" indicating they are approximate values.\n\n**Relevant links:**\n- [GOV.UK
| Migrants detected crossing the English Channel in small boats \u2013 time series](https://www.gov.uk/government/publications/migrants-detected-crossing-the-english-channel-in-small-boats)", "title":
"Migrant Data UK | Small Boat Arrivals"}
```

## 💭 Thinking

Now I have good data. Let me compile what I know:

**2026 data through Feb 22:**
Weekly totals:
- Week ending Jan 4: 0
- Week ending Jan 11: 32
- Week ending Jan 18: 626
- Week ending Jan 25: 275
- Week ending Feb 1: 0
- Week ending Feb 8: 275
- Week ending Feb 15: 322
- Week ending Feb 22: 0

Sum through Feb 22: 0+32+626+275+0+275+322+0 = 1,530

Plus the 605 arrivals around Feb 25 mentioned in news (the "biggest surge" article), and then Mar 3 (204) and Mar 4 (275).


The migrantdata.uk site reports around 2,209 through late February, so let me cross-check my numbers. Adding the 605 from Feb 25-26 to my weekly total of 1,530 gets me to roughly 2,135 by late February, which is close to that 2,209 figure. The remaining gap might account for some arrivals I'm missing in the Feb 27-Mar 2 window or slight variations in how the dates are being counted. So the weekly data likely stops at Feb 22, with the Feb 25-26 arrivals coming after that window. Looking at the discrepancy between my calculation and migrantdata's ~2,209 figure, there might be some arrivals on Feb 23-24 I'm not accounting for, or the timing of when those Feb 25 crossings are recorded differs. Either way, by early March I'm looking at somewhere between 2,200 and 2,700 total. Now I need to extrapolate from these two months of data to estimate the full January through April period.

I'm checking historical patterns to understand seasonality. Winter months are typically the slowest, with crossings picking up as spring arrives. Looking at past years: 2024 saw about 4,644 people cross in the first three months, and by the end of April 2025 the total had reached 10,000. This gives me reference points for how the Jan-Apr period typically breaks down across the year. I'm pulling the weekly breakdown to get more precise numbers—January through early March 2026 totals around 2,600, and I need to extrapolate what happens through the end of April based on how the pattern played out in previous years.

Looking at 2025 as a comparison point: it was at roughly 2,000 by early March and climbed to about 10,000 by April 30, meaning roughly 8,000 arrivals spread across the remaining eight weeks. The London Business article mentions 2026 is already tracking as record-breaking, having surpassed the same early-March checkpoint from both 2024 and 2025, so I'm weighing two possibilities—either 2026 follows a similar growth trajectory to 2025 and lands in the 5,000-10,000 range by end of April, or it exceeds that pattern given the "record-breaking" indication.

Now I'm working through the math more carefully. If 2026 starts around 2,200-2,700 in early March and follows the same growth pattern as 2025, I need to figure out what multiplier applies. The 2025 data suggests roughly a 5x increase from early March to end of April, which would put 2026 somewhere around 12,500 if that ratio holds—landing it in the 10,001-20,000 range. But that multiplier feels off, so I'm reconsidering the actual growth rate.

The crossing pattern is really lumpy with many zero days punctuated by spikes of 300-800, so averaging doesn't capture the real dynamics. I should look at what we know about seasonal patterns—March typically sees improving weather and increased crossings, while April is substantially higher than the winter months. The 2024 data doesn't map cleanly onto 2025's pattern, so I need to dig into the actual monthly breakdown to make a better projection. I'm trying to work backwards from the annual totals to estimate what January through April looked like in each year. For 2024, if Q1 was 4,644 and I estimate January and February were around 500 and 800 respectively based on typical winter patterns, that puts March at roughly 3,344—suggesting a sharp acceleration that month. For 2025, the 10,000 figure by end of April against 41,000 annual implies the first four months captured about 24% of yearly arrivals. If 2024 followed a similar seasonal pattern at 36,816 annual, that would suggest roughly 8,800 for January through April, though I'm working with incomplete data here.

Let me try a different angle using the weekly Boatwatch data I have. I know Q1 2024 hit 4,644, and for 2025 I can see roughly 2,056 through early March and 10,000 by end of April, which means March and April combined were around 8,000. If I can pin down how those two months split—estimating March 2025 at 3,000-4,000 and April at around 4,000—I might be able to extrapolate the pattern.

For 2026, I'm currently at about 2,700 through March 4th. Using the historical March-April split, the remaining 27 days of March could add another 2,500-3,500, and April could contribute 3,000-6,000 depending on weather. That puts me looking at a range from roughly 7,700 on the low end to 12,700 on the high end, with a central estimate around 10,200.

The 2025 data is particularly telling—they hit about 2,056 by early March and reached roughly 10,000 by end of April. Since 2026 is already running ahead at 2,200-2,700, it seems likely they'll cross that 10,000 threshold by April. The article's claim that 2026 is already outpacing both 2024 and 2025 at comparable points and is "on track to be record-breaking" supports this trajectory.

That said, weather is the wild card here. A stretch of poor conditions in March or April could substantially dampen crossings, while favorable weather could trigger surge days that dramatically accelerate the numbers.

On the policy side, the UK government is rolling out new measures—a pilot deal with France to return some arrivals and £100M in border technology—but historically these haven't produced dramatic reductions in crossing attempts. Let me work through the probability ranges. For the 0-5,000 outcome to happen, the March 5 through April 30 period would need to add fewer than about 2,300 crossings to the current ~2,700 baseline, averaging just 40 per day over 57 days. Given that spring months typically see significantly higher volumes than winter, this scenario feels unlikely unless there's sustained poor weather—I'd estimate around 10-15% probability. But I should double-check my 2025 baseline numbers to make sure I'm calibrating this correctly.

Looking at the actual 2025 trajectory, the year started around 2,056 and reached approximately 10,000 by the end of April, meaning March-April added roughly 8,000 crossings. For 2026 to stay under 5,000 total, it would need to add less than 2,300 in that same window—less than a third of what 2025 added. That's a dramatic shortfall and would require something exceptional to occur. The 5,001-10,000 range seems more plausible if 2026 runs somewhat below 2025's pace due to policy effects or weather patterns, though the current data suggests 2026 is actually tracking ahead. I'd estimate maybe 30-40% for this band.

The 10,001-20,000 range is where 2025 landed, and given that 2026 appears to be running slightly faster than 2025 with an upward trend, this feels quite realistic—probably 40-50% likely. For 20,001 or higher, I'd need to look at historical context. Even 2022, the record year with 46,000 annual arrivals, likely had only around 11,000 in the January-April window based on the typical 24% seasonal distribution. Reaching 20,000+ would require truly exceptional circumstances, so I'm thinking 2-5% chance at most.

But I should reconsider the 2025 baseline. MigrationWatch noted that 10,000 was reached before the end of April, which suggests the final Jan-Apr total was probably closer to 11,000-12,000. That gives 2026 more room to edge higher. I also need to be clearer about what "record-breaking" actually means here—the articles are talking about a record year overall, not necessarily a record for just the January-April period. Q1 2024 had a strong start at 4,644 crossings, but the full year still came in lower than 2025. So I'm looking at Q1 2024 as 4,644 and Q1 2025 as likely higher than that.

Now I'm realizing the gap between Q1 2024's 4,644 and Q1 2025's 2,056 by early March is substantial—March 2024 must have had a particularly strong crossing period. For 2026, I'm seeing roughly 2,700 through early March, which puts it somewhere between the two prior years at this point.

If I extrapolate from 2025's pattern where March and April together added about 8,500 crossings to the early March total, and 2026 is running about 30% ahead of 2025's pace, that would suggest a January-April total around 13,800—comfortably in the 10,001-20,000 range. Though there's still uncertainty in how the rest of March and April will actually play out.

The real wildcard here is weather. Looking at the weekly data, there are plenty of weeks with zero arrivals, which tells me this is heavily weather-dependent. A stretch of poor conditions in March or April could easily knock thousands off the projection. And comparing back to 2024, where Q1 alone was 4,644 and the full year hit 36,816, there's clearly a lot of variability year to year. Looking at 2026's pace relative to 2025, it's tracking slightly ahead, though government enforcement claims haven't meaningfully slowed the upward trend historically. The French-UK pilot deal sounds promising in theory but past policy interventions suggest limited real-world impact on crossing numbers. Based on this trajectory, I'm estimating roughly an 8% chance of staying under 5,000 (would require severe weather or unprecedented policy success given 2026 is already near 2,700), about 35% for the 5,001-10,000 range where 2024 landed, and around 50% for 10,001-20,000.

Let me refine this though. With about 2,700 crossings through early March and roughly 57 days remaining, I need to project what March and April will add. Last year that period contributed around 8,000, but if 2026 continues its slightly faster pace, I'm looking at maybe 8,500-9,000 more, putting the total near 11,200—solidly in that 10,001-20,000 band.

Of course, there's real uncertainty here depending on weather patterns. A bad stretch could mean only 4,000 additional arrivals, dropping the total to 6,700. On the flip side, favorable conditions and sustained high crossing rates could push it to 14,700 or even higher. The scenario where it exceeds 20,000 would require truly exceptional circumstances that haven't been seen before. And for it to stay under 5,000 total, I'd need fewer than 2,300 more arrivals over the next two months—essentially just 40 per day on average—which would only happen during severe weather when crossing days become rare.

Now I'm assigning probabilities to each range: 8% chance it stays under 5,000, 30% for the 5,001-10,000 band, 55% for 10,001-20,000, and 7% for anything above 20,000. But I should verify my baseline assumption about the January-April 2025 figure. The source confirms the 10,000 threshold was crossed by April 30, though the exact total could have been anywhere from 10,500 to 12,000 or higher. If I work backward from the annual total of 41,000, the first four months likely represented between 20-30% of the year, which would put them at 8,200 to 12,300.

Given that 2026 is tracking slightly ahead of 2025, my estimates for January-April 2026 range from 8,000-10,000 on the low end if policy changes slow things down, to 11,000-13,000 as my central case, up to 13,000-15,000 if the pace accelerates. This analysis strengthens my confidence that the 10,001-20,000 range is most probable, so I'm adjusting my distribution slightly upward to 58% for that band while reducing the lower ranges accordingly.

The 20,001+ scenario is actually quite extreme—even at 2022's record annual pace of 46,000, you'd only see about 11,000-14,000 in four months unless the seasonal pattern was heavily front-loaded. Hitting 20,001 would require roughly a 60,000 annual rate, so I'm trimming that probability down to 5%. Meanwhile, we're already at 2,700 with 57 days left, so falling short of 5,000 total would mean adding less than 2,300 more—unlikely but possible if storm season extends, so I'll set that at 7%.

My refined probabilities are now 7% for 0-5,000, 30% for 5,001-10,000, 58% for 10,001-20,000, and 5% for 20,001+.

Running a Monte Carlo simulation to validate this more rigorously...

## 💬 Response

Now I have enough data to build a quantitative model. Let me compute this properly.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Historical data compilation\n# ===========================\n\n# 2026 weekly data through Feb 22 (from Boatwatch):\nweekly_2026 = {\n    'Jan 4': 0,\n    'Jan 11': 32,\n    'Jan 18': 626,\n    'Jan 25': 275,\n    'Feb 1': 0,\n    'Feb 8': 275,\n    'Feb 15': 322,\n    'Feb 22': 0,\n}\n# Total through Feb 22: \nthrough_feb22 = sum(weekly_2026.values())\nprint(f\"Through Feb 22, 2026: {through_feb22}\")\n\n# Additional known data:\n# Feb 25: 605 arrivals (big surge day)\n# Feb 26-Mar 2: 0\n# Mar 3: 204\n# Mar 4: 275\nadditional = 605 + 204 + 275\ntotal_through_mar4 = through_feb22 + additional\nprint(f\"Through Mar 4, 2026: {total_through_mar4}\")\n\n# Historical annual totals\n# 2022: ~46,000 (record)\n# 2023: ~29,437\n# 2024: ~36,816\n# 2025: ~41,000\n\n# Historical Jan-Apr patterns:\n# 2024 Q1: ~4,644 (ECRE data)\n# 2025: 10,000 reached before end of April\n# 2025 at early March: ~2,056 (migrantdata.uk comparison)\n\n# From 2025 comparison:\n# ~2,056 at early March \u2192 ~10,000+ by end of April\n# So remaining ~57 days added ~8,000-10,000\n\n# Key: 2026 is at ~2,614 vs 2025's ~2,056 at same point = 27% ahead\n\nprint(f\"\\n2026 vs 2025 ratio at early March: {total_through_mar4/2056:.2f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Through Feb 22, 2026: 1530\nThrough Mar 4, 2026: 2614\n\n2026 vs 2025 ratio at early March: 1.27\n", "stderr": "", "duration_ms": 161}
```

## 💭 Thinking

Let me now run a Monte Carlo simulation to estimate the Jan-Apr 2026 total.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\n\n# Monte Carlo simulation for Jan-Apr 2026 small boat arrivals\n# ============================================================\n\n# Known: ~2,614 through Mar 4, 2026\ncurrent_total = 2614\n# Days remaining: Mar 5 to Apr 30 = 27 + 30 = 57 days\ndays_remaining = 57\n\n# Historical reference: 2025 pattern\n# 2025 at early March: ~2,056\n# 2025 at end of April: estimate ~10,500-12,000 (10,000 reached \"before end of April\")\n# Let's estimate 2025 Jan-Apr as ~11,000 (conservative - could be higher)\n# So 2025 added ~9,000 in the remaining 57 days from early March\n\n# Key modeling approach:\n# Small boat crossings are highly weather-dependent and \"lumpy\"\n# Many days with 0, occasional days with 200-800+\n# Model: each day is either a \"crossing day\" or \"zero day\"\n# On crossing days, arrivals follow a distribution\n\n# From 2025 data (weekly breakdown shows pattern):\n# In 2025 Jan-Feb (similar to 2026), roughly 8-10 \"crossing events\" in 8 weeks\n# In March-April, crossings become more frequent\n\n# Estimate crossing probability and arrivals per crossing day\n# March: crossing probability ~25-35% (improving weather)\n# April: crossing probability ~35-45% (better weather)\n\n# Average arrivals per crossing day: ~200-400 (based on recent data showing\n# 32, 275, 322, 605, 204, 275 on individual crossing days/events)\n\nn_sims = 50000\n\n# Model parameters with uncertainty\nresults = []\nfor _ in range(n_sims):\n    total = current_total\n    \n    # Sample overall pace multiplier (accounts for year-to-year variation)\n    # 2026 is running ~27% ahead of 2025, but with uncertainty\n    pace_multiplier = np.random.lognormal(np.log(1.15), 0.25)\n    \n    # March (27 remaining days, 5-31)\n    march_crossing_prob = np.random.beta(6, 14)  # mean ~0.30\n    march_avg_per_crossing = np.random.lognormal(np.log(280), 0.4)\n    \n    for day in range(27):\n        if np.random.random() < march_crossing_prob * pace_multiplier:\n            arrivals = max(0, int(np.random.lognormal(np.log(march_avg_per_crossing), 0.5)))\n            total += arrivals\n    \n    # April (30 days) - more crossings expected\n    april_crossing_prob = np.random.beta(8, 12)  # mean ~0.40\n    april_avg_per_crossing = np.random.lognormal(np.log(320), 0.4)\n    \n    for day in range(30):\n        if np.random.random() < april_crossing_prob * pace_multiplier:\n            arrivals = max(0, int(np.random.lognormal(np.log(april_avg_per_crossing), 0.5)))\n            total += arrivals\n    \n    results.append(total)\n\nresults = np.array(results)\n\n# Calculate probabilities for each bucket\np_0_5000 = np.mean(results <= 5000)\np_5001_10000 = np.mean((results > 5000) & (results <= 10000))\np_10001_20000 = np.mean((results > 10000) & (results <= 20000))\np_20001_plus = np.mean(results > 20000)\n\nprint(\"Monte Carlo Results (50,000 simulations):\")\nprint(f\"  Median: {np.median(results):.0f}\")\nprint(f\"  Mean: {np.mean(results):.0f}\")\nprint(f\"  10th percentile: {np.percentile(results, 10):.0f}\")\nprint(f\"  25th percentile: {np.percentile(results, 25):.0f}\")\nprint(f\"  75th percentile: {np.percentile(results, 75):.0f}\")\nprint(f\"  90th percentile: {np.percentile(results, 90):.0f}\")\nprint()\nprint(\"Bucket probabilities:\")\nprint(f\"  0-5,000:       {p_0_5000:.3f} ({p_0_5000*100:.1f}%)\")\nprint(f\"  5,001-10,000:  {p_5001_10000:.3f} ({p_5001_10000*100:.1f}%)\")\nprint(f\"  10,001-20,000: {p_10001_20000:.3f} ({p_10001_20000*100:.1f}%)\")\nprint(f\"  20,001+:       {p_20001_plus:.3f} ({p_20001_plus*100:.1f}%)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Monte Carlo Results (50,000 simulations):\n  Median: 10697\n  Mean: 11513\n  10th percentile: 6743\n  25th percentile: 8329\n  75th percentile: 13716\n  90th percentile:
17294\n\nBucket probabilities:\n  0-5,000:       0.015 (1.5%)\n  5,001-10,000:  0.416 (41.6%)\n  10,001-20,000: 0.520 (52.0%)\n  20,001+:       0.049 (4.9%)\n", "stderr": "", "duration_ms": 1815}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Sensitivity analysis: also calibrate against the 2025 benchmark\n# 2025: ~2,056 at early March, ~11,000 by end of April (estimated)\n# That means 2025 added ~9,000 in the remaining 57 days\n\n# Alternative approach: use 2025 residual as base distribution\n# and scale by 2026/2025 ratio\n\nnp.random.seed(123)\nn_sims = 50000\n\n# 2025 remaining-period total (Mar 5 to Apr 30): estimate 8,500-10,000\n# with mean ~9,000 and some variance\nresults2 = []\nfor _ in range(n_sims):\n    # 2025 base: how much was added in remaining Mar-Apr\n    base_2025_remaining = np.random.normal(9000, 2000)\n    base_2025_remaining = max(1000, base_2025_remaining)\n    \n    # 2026 multiplier relative to 2025\n    # Currently 27% ahead, but with mean-reversion tendency \n    # (weather noise) and trend continuation (upward trend)\n    multiplier = np.random.lognormal(np.log(1.10), 0.30)\n    \n    remaining_2026 = base_2025_remaining * multiplier\n    total_2026 = current_total + remaining_2026\n    results2.append(total_2026)\n\nresults2 = np.array(results2)\n\np_0_5000 = np.mean(results2 <= 5000)\np_5001_10000 = np.mean((results2 > 5000) & (results2 <= 10000))\np_10001_20000 = np.mean((results2 > 10000) & (results2 <= 20000))\np_20001_plus = np.mean(results2 > 20000)\n\nprint(\"Alternative Model (2025-benchmark based):\")\nprint(f\"  Median: {np.median(results2):.0f}\")\nprint(f\"  Mean: {np.mean(results2):.0f}\")\nprint(f\"  10th percentile: {np.percentile(results2, 10):.0f}\")\nprint(f\"  25th percentile: {np.percentile(results2, 25):.0f}\")\nprint(f\"  75th percentile: {np.percentile(results2, 75):.0f}\")\nprint(f\"  90th percentile: {np.percentile(results2, 90):.0f}\")\nprint()\nprint(\"Bucket probabilities:\")\nprint(f\"  0-5,000:       {p_0_5000:.3f} ({p_0_5000*100:.1f}%)\")\nprint(f\"  5,001-10,000:  {p_5001_10000:.3f} ({p_5001_10000*100:.1f}%)\")\nprint(f\"  10,001-20,000: {p_10001_20000:.3f} ({p_10001_20000*100:.1f}%)\")\nprint(f\"  20,001+:       {p_20001_plus:.3f} ({p_20001_plus*100:.1f}%)\")\n\n# Average the two models\nprint(\"\\n\\nAveraged model probabilities:\")\ncombined = np.concatenate([results, results2])\np_0_5000 = np.mean(combined <= 5000)\np_5001_10000 = np.mean((combined > 5000) & (combined <= 10000))\np_10001_20000 = np.mean((combined > 10000) & (combined <= 20000))\np_20001_plus = np.mean(combined > 20000)\nprint(f\"  0-5,000:       {p_0_5000:.3f} ({p_0_5000*100:.1f}%)\")\nprint(f\"  5,001-10,000:  {p_5001_10000:.3f} ({p_5001_10000*100:.1f}%)\")\nprint(f\"  10,001-20,000: {p_10001_20000:.3f} ({p_10001_20000*100:.1f}%)\")\nprint(f\"  20,001+:       {p_20001_plus:.3f} ({p_20001_plus*100:.1f}%)\")\nprint(f\"\\n  Combined median: {np.median(combined):.0f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Alternative Model (2025-benchmark based):\n  Median: 12357\n  Mean: 12978\n  10th percentile: 8508\n  25th percentile: 10136\n  75th percentile: 15128\n  90th percentile:
18194\n\nBucket probabilities:\n  0-5,000:       0.001 (0.1%)\n  5,001-10,000:  0.234 (23.4%)\n  10,001-20,000: 0.708 (70.8%)\n  20,001+:       0.057 (5.7%)\n\n\nAveraged model probabilities:\n
0-5,000:       0.008 (0.8%)\n  5,001-10,000:  0.325 (32.5%)\n  10,001-20,000: 0.614 (61.4%)\n  20,001+:       0.053 (5.3%)\n\n  Combined median: 11592\n", "stderr": "", "duration_ms": 76}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also check: what was the Jan-Apr total in 2024?\n# Q1 2024 was 4,644 (record). 2024 annual was 36,816.\n# If Jan-Apr 2024 was roughly 25-30% of annual: 9,200-11,000\n# But Q1 was only 4,644, so April 2024 could have added 4,500-6,000.\n# That gives Jan-Apr 2024: ~9,000-10,600\n\n# Let me also think about this: what fraction of annual arrives in Jan-Apr?\n# These are rough estimates from what we know:\n# 2022: ~46,000 annual. If Jan-Apr ~25% \u2192 ~11,500\n# 2023: ~29,437 annual. If Jan-Apr ~20-25% \u2192 ~5,900-7,400\n# 2024: ~36,816 annual. Q1 was 4,644 (=12.6% of annual), so Jan-Apr likely ~22-28%\n# 2025: ~41,000 annual. Jan-Apr ~10,000-12,000 \u2192 24-29%\n\n# The proportion of annual that falls in Jan-Apr varies, \n# but is typically 20-30%, with higher years having slightly higher proportions\n# in early months (if weather cooperates)\n\n# For 2026: if annual is on \"record-breaking\" pace:\n# If 2026 annual were 45,000-50,000, Jan-Apr at 25% \u2192 11,250-12,500\n# If 2026 annual were 40,000, Jan-Apr at 25% \u2192 10,000\n\n# This all points to median around 10,000-12,000\n\n# Key insight: the boundary between options 2 and 3 is at 10,000\n# The median of our simulations is ~11,500\n# This means roughly 55-65% probability of being above 10,000\n\n# But I should also consider: the uncertainty about how much 2025 \n# actually had in Jan-Apr. \"10,000 before end of April\" could mean\n# 10,000 was reached in mid-April, and the total by Apr 30 was 12,000+\n\n# Final calibration check\nprint(\"Summary of evidence:\")\nprint(\"=\" * 60)\nprint(f\"Current 2026 total (through Mar 4): ~{current_total}\")\nprint(f\"2025 at same point: ~2,056\")\nprint(f\"2026/2025 ratio: {current_total/2056:.2f}\")\nprint(f\"2025 Jan-Apr total: ~10,000-12,000\")\nprint(f\"2024 Q1: 4,644; Jan-Apr est: ~8,500-10,500\")\nprint(f\"Simulation median Jan-Apr 2026: ~11,500\")\nprint(f\"10th-90th range: ~7,000-17,500\")\nprint()\nprint(\"The 10,000 threshold is near the median - genuine uncertainty about\")\nprint(\"whether total lands in 5,001-10,000 or 10,001-20,000 range.\")\nprint()\nprint(\"Policy context: government claims new enforcement measures,\")\nprint(\"but historical pattern shows limited impact on crossing numbers.\")\nprint(\"Trend is upward (36.8k\u219241k\u2192 track for higher).\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Summary of evidence:\n============================================================\nCurrent 2026 total (through Mar 4): ~2614\n2025 at same point: ~2,056\n2026/2025 ratio:
1.27\n2025 Jan-Apr total: ~10,000-12,000\n2024 Q1: 4,644; Jan-Apr est: ~8,500-10,500\nSimulation median Jan-Apr 2026: ~11,500\n10th-90th range: ~7,000-17,500\n\nThe 10,000 threshold is near the median
- genuine uncertainty about\nwhether total lands in 5,001-10,000 or 10,001-20,000 range.\n\nPolicy context: government claims new enforcement measures,\nbut historical pattern shows limited impact on
crossing numbers.\nTrend is upward (36.8k\u219241k\u2192 track for higher).\n", "stderr": "", "duration_ms": 0}
```

## 💬 Response

Now let me run the reflection checkpoint.
