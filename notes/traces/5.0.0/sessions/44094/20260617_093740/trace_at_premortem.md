# Reasoning Log: Will a second 2026 batch of Bureau 1440 Rassvet satellites reach orbit before June 28, 2026?

*Generated: 2026-06-17T09:49:40.402992+00:00*


## 💭 Thinking

Let me analyze this forecasting question about whether a second 2026 batch of Bureau 1440 Rassvet satellites will reach orbit before June 28, 2026.

Key details:
- The window is June 13-27, 2026 (23:59 UTC)
- Today is June 17, 2026
- The first batch launched March 23, 2026
- A second batch was originally planned for April 24-28 but was postponed
- Independent calendars tentatively target around June 18, 2026
- The date is "TBD" based on airspace notices, not official announcements
- Bureau 1440 keeps launch schedules confidential, and there's concern about whether they can sustain this rapid cadence given production constraints.

## 💬 Response

I'll start by parsing the question and then research the current status of this launch.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    44094
  ]
}
```

### 📋 Result

```
{"post_id": 44094, "title": "Will a second 2026 batch of Bureau 1440 Rassvet satellites reach orbit before June 28, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/44094",
"background_info": "Bureau 1440 (also styled \"Byuro 1440\") is a Russian company building \"Rassvet,\" a low-Earth-orbit broadband satellite constellation intended as a domestic alternative to
Starlink. After experimental Rassvet-1/-2 missions in 2023\u20132024, the company began deploying operational \"Rassvet-3\" satellites in 2026.\n\nThe first 2026 operational batch \u2014 16 Rassvet-3
satellites \u2014 launched on a Soyuz-2.1b rocket from Plesetsk Cosmodrome (Site 43/4) on 23 March 2026 (17:24 UTC). The launch was conducted without prior public announcement and later confirmed
successful by Bureau 1440 and orbital tracking sources.\n\nRussia's stated plan is to deploy roughly 156 Rassvet satellites in 2026 (about ten launches of ~16 each), implying additional launches
throughout the year. A second batch of 16 satellites was originally listed for a 24\u201328 April 2026 window (inferred from NOTAMs) but was postponed. As of early-to-mid June 2026, independent launch
calendars (e.g., RocketLaunch.Live, RocketLaunch.org) tentatively target the second batch for around 18 June 2026 on a Soyuz-2.1b from Plesetsk, but the date remains \"TBD\" and is based on airspace
notices rather than an official Bureau 1440 announcement. Bureau 1440 generally does not disclose specific launch dates in advance, and independent observers have expressed skepticism about the
aggressive cadence given production-line bottlenecks.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`",
"resolution_criteria": "This question resolves YES if, between June 13, 2026 and 23:59 UTC on June 27, 2026, a launch carrying a second 2026 batch of Bureau 1440 Rassvet (Rassvet-3) satellites
successfully reaches orbit \u2014 that is, a Soyuz-family launch (distinct from and after the 23 March 2026 batch) that places one or more Rassvet satellites into orbit. The 23 March 2026 launch does
not count toward this question. Resolution will be based on the orbital launch log on the Wikipedia \"[2026 in spaceflight](https://en.wikipedia.org/wiki/2026_in_spaceflight)\" page, or on [credible
sources](https://www.metaculus.com/faq/#definitions) such as Bureau 1440 press releases or orbital-tracking reports if Wikipedia has not yet been updated. If such a qualifying launch reaches orbit in
the window, the question resolves YES; otherwise it resolves NO.", "fine_print": "\"Reaches orbit\" means the launch vehicle achieves orbital insertion of the Rassvet payload; a launch failure that
does not place any Rassvet satellite into orbit does not count as YES. The relevant launch must lift off within the window of June 13, 2026 through 23:59 UTC on June 27, 2026; a launch scheduled but
not yet flown by that time resolves NO. A launch carrying Rassvet satellites qualifies regardless of the exact number of satellites, and rideshare or experimental Rassvet payloads also count, provided
they are Bureau 1440 Rassvet satellites and the launch is distinct from the 23 March 2026 mission. If sources conflict on whether orbit was achieved, the determination of credible orbital-tracking
reporting governs.", "num_forecasters": 8, "community_prediction": null}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Bureau 1440 Rassvet satellite launch June 2026 Soyuz Plesetsk second batch status",
      "ttl": "6h"
    },
    {
      "query": "Soyuz 2.1b launch schedule June 2026 Plesetsk cosmodrome upcoming launches",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Bureau 1440 Rassvet satellite launch June 2026 Soyuz Plesetsk second batch status", "entry": {"slug": "bureau-1440-rassvet-satellite-launch-june-2026-soy-3963705c", "query":
"Bureau 1440 Rassvet satellite launch June 2026 Soyuz Plesetsk second batch status", "answer": "## Research Report: Bureau 1440 Rassvet Satellite Launch \u2014 June 2026 / Second Batch Status\n\n###
1. Company Overview\n\n**Bureau 1440** (\u0411\u044e\u0440\u043e 1440) is a Russian aerospace company under IKS Holding, developing a LEO satellite internet constellation \u2014 often called
\"Russia's Starlink.\" Founded in November 2020 (originally as \"MegaFon 1440\"), headquartered in Moscow, and led by CEO Alexey Shelobkov.\n\n---\n\n### 2. Launch History\n\n| Flight | Date (UTC) |
Satellites | Vehicle | Site | Outcome |\n|--------|-----------|------------|---------|------|---------|\n| Rassvet-1 | 27 June 2023 | 3 (experimental) | Soyuz-2.1b / Fregat-M | Vostochny | \u2705
Success |\n| Rassvet-2 | 16 May 2024 | 3 (experimental) | Soyuz-2.1b / Fregat-M | Plesetsk LC-43 | \u2705 Success |\n| **Rassvet-3** | **23 March 2026** | **16 (first operational batch)** |
**Soyuz-2.1b / Fregat-M** | **Plesetsk LC-43/4** | **\u2705 Success** |\n\n---\n\n### 3. The March 2026 Launch (Rassvet-3) \u2014 Key Details\n\nOn **23 March 2026 at 20:24 UTC**, Bureau 1440 launched
its **first batch of 16 production satellites** from Plesetsk Cosmodrome. Key features of these satellites (~370 kg each):\n- 5G NTN communication systems\n- Inter-satellite laser communication
terminals\n- Plasma propulsion systems\n- Updated power systems\n\nAll 16 were successfully deployed into a parking orbit (~288 \u00d7 324 km, 82.3\u00b0 inclination) and taken under Bureau 1440's
Mission Control Center.\n\n---\n\n### 4. Current Constellation Status (as of mid-June 2026)\n\n- **1 satellite lost:** Object 4 (NORAD 68363, COSPAR 2026-061D) reentered the atmosphere around **June
6, 2026**, never having performed orbital maneuvers. Bureau 1440 confirmed the loss.\n- **6 satellites actively climbing** to higher target orbits\n- **8 satellites maintaining altitude** via station-
keeping\n- **15 of 16 operational Rassvet-3 satellites remain in orbit**\n- **6 experimental satellites** (from 2023 & 2024 missions) also still in orbit\n- **Total Bureau 1440 satellites in orbit:
~21**\n\n---\n\n### 5. Second Batch Launch Status \u2014 No Confirmed June 2026 Launch\n\n**No second batch of operational satellites has been confirmed as launched as of June 17, 2026.** Key
findings:\n\n- The March 23, 2026 launch was the **first operational batch** (third overall mission), not the second.\n- No upcoming Soyuz/Rassvet launches are listed in current launch schedules for
June 2026.\n- Gunter's Space Page lists further Rassvet-3 satellites as \"TBD,\" indicating more are expected but no date is set.\n- Bureau 1440 plans **10\u201312 launches per year** carrying ~15
satellites each (150\u2013180 satellites/year).\n- Target: **~250 satellites by 2027** for commercial service launch.\n- By 2030: 292 satellites; by 2035: 900+ satellites.\n\n---\n\n### 6. Funding &
Future Plans\n\n- Financed under Russia's \"Data Economy\" national program: **102.8 billion rubles** from the federal budget + **329 billion rubles** from company funds through 2030.\n- Pilot
connectivity projects planned for 2026 in several Russian regions (e.g., Nenets Autonomous Okrug).\n- CEO Shelobkov: \"Ahead lies the constellation deployment phase, which will require dozens of
launches.\"\n\n---\n\n### 7. Summary\n\nThe question about a \"second batch\" launch in June 2026 from Plesetsk does **not** correspond to any confirmed event. The most recent launch was the **first
operational batch of 16 Rassvet-3 satellites on March 23, 2026**. One satellite has since been lost. No second operational batch launch date has been publicly confirmed, though Bureau 1440's roadmap
calls for many more launches in 2026\u20132027 to build toward the ~250-satellite threshold needed for commercial service.", "sources": [{"url": "https://en.wikipedia.org/wiki/Bureau_1440", "title":
"Bureau 1440 - Wikipedia", "domain": "en.wikipedia.org", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Bureau 1440 is a Russian aerospace company developing a LEO satellite internet
constellation, founded November 2020."}, {"url": "https://www.kommersant.ru/doc/8533373", "title": "Kommersant - Bureau 1440 Rassvet-3 Launch Report", "domain": "kommersant.ru", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "16 operational Rassvet-3 satellites launched March 23, 2026 from Plesetsk on Soyuz-2.1b."}, {"url": "https://meduza.io/en/news/2026/06/09/russia-loses-one-of-the-
satellites-in-its-rassvet-constellation-billed-as-a-starlink-rival", "title": "Russia loses one of the satellites in its Rassvet constellation - Meduza", "domain": "meduza.io", "accessed_at":
"2026-06-17T00:00:00Z", "snippet": "One Rassvet-3 satellite (NORAD 68363) reentered atmosphere around June 6, 2026 without performing maneuvers."}, {"url": "https://defence-blog.com/russias-answer-to-
starlink-just-lost-its-first-satellite/", "title": "Russia's answer to Starlink just lost its first satellite - Defence Blog", "domain": "defence-blog.com", "accessed_at": "2026-06-17T00:00:00Z",
"snippet": "Bureau 1440 confirmed loss of one Rassvet-3 satellite."}, {"url": "https://space.skyrocket.de/doc_sdat/rassvet-3.htm", "title": "Rassvet-3 - Gunter's Space Page", "domain":
"space.skyrocket.de", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "16 Rassvet-3 satellites cataloged (2026-061A through 2026-061R), ~370 kg each, launched from Plesetsk LC-43/4."}, {"url":
"https://ria.ru/20260324/sputniki-2082543161.html", "title": "RIA Novosti - Rassvet-3 Launch Coverage", "domain": "ria.ru", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Russian state media
coverage of March 23, 2026 Rassvet-3 operational satellite launch."}, {"url": "https://www.vedomosti.ru/technology/news/2026/03/24/1184996-sputniki-svyazi", "title": "Vedomosti - Bureau 1440 Satellite
Communications Plans", "domain": "vedomosti.ru", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Pilot connectivity projects planned for 2026 in Nenets Autonomous Okrug and other Russian
regions."}, {"url": "https://www.n2yo.com/satellite/?s=68369", "title": "N2YO - RASSVET-3 NO. 10 Tracking", "domain": "n2yo.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Current orbit ~274
x 287 km, 82.29\u00b0 inclination, orbital period ~90.13 min."}, {"url": "https://www.russianspaceweb.com/spacecraft-2026-0323.html", "title": "RussianSpaceWeb - Rassvet-3 Mission", "domain":
"russianspaceweb.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Detailed mission profile and satellite status for the March 23 Rassvet-3 launch."}, {"url":
"https://vz.ru/society/2026/5/25/1422067.html", "title": "Vzglyad - Military Applications of Rassvet Satellites", "domain": "vz.ru", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Discussion of
potential military UAV applications of Rassvet constellation technology."}], "key_facts": ["Bureau 1440 launched its first operational batch of 16 Rassvet-3 satellites on March 23, 2026, from Plesetsk
Cosmodrome (LC-43/4) via Soyuz-2.1b/Fregat-M \u2014 this was the company's third overall launch.", "No second batch of operational Rassvet satellites has been confirmed as launched as of June 17,
2026.", "One of the 16 Rassvet-3 satellites (NORAD 68363, COSPAR 2026-061D) was lost around June 6, 2026, after reentering the atmosphere without performing orbital maneuvers.", "15 of the 16
operational Rassvet-3 satellites remain in orbit: 6 actively climbing to higher orbits, 8 maintaining station-keeping.", "Total Bureau 1440 satellites currently in orbit: approximately 21 (6
experimental from 2023-2024 + 15 operational from March 2026).", "Bureau 1440 plans 10-12 launches per year with ~15 satellites each (150-180 satellites/year) to reach ~250 satellites by 2027 for
commercial service.", "The constellation is funded under Russia's 'Data Economy' program: 102.8 billion rubles federal + 329 billion rubles company funds through 2030.", "Each Rassvet-3 satellite
weighs ~370 kg and features 5G NTN comms, inter-satellite laser links, and plasma propulsion.", "Satellites were inserted into parking orbit at approximately 288 x 324 km, 82.3\u00b0 inclination.",
"Pilot connectivity projects are planned for 2026 in Russian regions including Nenets Autonomous Okrug."], "data_points": [{"metric": "Rassvet-3 satellites launched (first operational batch)",
"value": 16.0, "unit": "satellites", "as_of": "2026-03-23", "source_url": "https://www.kommersant.ru/doc/8533373"}, {"metric": "Rassvet-3 satellites lost (atmospheric reentry)", "value": 1.0, "unit":
"satellites", "as_of": "2026-06-06", "source_url": "https://meduza.io/en/news/2026/06/09/russia-loses-one-of-the-satellites-in-its-rassvet-constellation-billed-as-a-starlink-rival"}, {"metric":
"Rassvet-3 satellites remaining in orbit", "value": 15.0, "unit": "satellites", "as_of": "2026-06-17", "source_url": "https://defence-blog.com/russias-answer-to-starlink-just-lost-its-first-
satellite/"}, {"metric": "Total Bureau 1440 satellites in orbit", "value": 21.0, "unit": "satellites", "as_of": "2026-06-17", "source_url": "https://space.skyrocket.de/doc_sdat/rassvet-3.htm"},
{"metric": "Rassvet-3 satellite mass", "value": 370.0, "unit": "kg", "as_of": "2026-03-23", "source_url": "https://space.skyrocket.de/doc_sdat/rassvet-3.htm"}, {"metric": "Parking orbit perigee
(initial)", "value": 288.0, "unit": "km", "as_of": "2026-03-31", "source_url": "https://www.n2yo.com/satellite/?s=68369"}, {"metric": "Parking orbit apogee (initial)", "value": 324.0, "unit": "km",
"as_of": "2026-03-31", "source_url": "https://www.n2yo.com/satellite/?s=68369"}, {"metric": "Orbital inclination", "value": 82.3, "unit": "degrees", "as_of": "2026-06-14", "source_url":
"https://www.n2yo.com/satellite/?s=68369"}, {"metric": "Planned launches per year", "value": 12.0, "unit": "launches/year", "as_of": "2026-03-24", "source_url":
"https://www.kommersant.ru/doc/8533373"}, {"metric": "Satellites per launch", "value": 15.0, "unit": "satellites", "as_of": "2026-03-24", "source_url": "https://www.kommersant.ru/doc/8533373"},
{"metric": "Target constellation size for commercial service (2027)", "value": 250.0, "unit": "satellites", "as_of": "2026-03-24", "source_url": "https://en.wikipedia.org/wiki/Bureau_1440"},
{"metric": "Federal budget allocation through 2030", "value": 102.8, "unit": "billion rubles", "as_of": "2026-03-24", "source_url":
"https://www.vedomosti.ru/technology/news/2026/03/24/1184996-sputniki-svyazi"}, {"metric": "Company funding through 2030", "value": 329.0, "unit": "billion rubles", "as_of": "2026-03-24",
"source_url": "https://www.vedomosti.ru/technology/news/2026/03/24/1184996-sputniki-svyazi"}, {"metric": "Bureau 1440 total launches to date", "value": 3.0, "unit": "launches", "as_of": "2026-06-17",
"source_url": "https://en.wikipedia.org/wiki/Bureau_1440"}], "created_at": "2026-06-17T09:42:25.730491Z", "updated_at": "2026-06-17T09:42:25.730491Z", "stale_after": "2026-06-17T15:42:25.730491Z",
"state": "fresh", "revision_history": [], "session_id": "79139bb5-197f-49ba-a976-a2d8e330e876", "follow_up_count": 0}, "is_follow_up": false}, {"query": "Soyuz 2.1b launch schedule June 2026 Plesetsk
cosmodrome upcoming launches", "entry": {"slug": "soyuz-2-1b-launch-schedule-june-2026-plesetsk-cosm-5afc0419", "query": "Soyuz 2.1b launch schedule June 2026 Plesetsk cosmodrome upcoming launches",
"answer": "\n\nUnfortunately, my web search and web fetch tools are all unavailable in this session, which significantly limits my ability to gather real-time data. Let me compile what I can report
based on my training knowledge and clearly flag the limitations.\n\n---\n\n# Soyuz 2.1b Launch Schedule \u2014 Plesetsk Cosmodrome \u2014 June 2026 & Upcoming\n\n## Key Context\n\n### About Soyuz
2.1b\n- The **Soyuz 2.1b** is a modernized variant of the venerable Soyuz rocket family, operated by Roscosmos. It features a digital flight control system and an upgraded RD-0124 third-stage
engine.\n- It launches from two primary Russian cosmodromes: **Plesetsk** (northern Russia, primarily military/government payloads) and **Vostochny** (civilian/commercial payloads). Baikonur
(Kazakhstan) is also used but less frequently for 2.1b.\n\n### Plesetsk Cosmodrome\n- Located in Arkhangelsk Oblast, Russia (62.9\u00b0N). Primarily used for **military and government missions**,
including GLONASS navigation satellites, Bars-M reconnaissance satellites, and other classified payloads.\n- Russia's most active military launch site.\n\n### Historical Launch Cadence (Soyuz 2.1b
from Plesetsk)\n- Russia has maintained a steady cadence of Soyuz 2.1b launches from Plesetsk, typically **4\u20138 launches per year** from this site.\n- Common payloads from Plesetsk include:\n  -
**GLONASS-K/K2** navigation satellites (often launched with Fregat upper stage)\n  - **Bars-M** Earth observation/reconnaissance satellites\n  - **Lotos-S** ELINT satellites (Liana system)\n  -
**Cosmos-series** classified military payloads\n  - **Gonets-M** communication satellites\n\n### 2025\u20132026 Trajectory\n- Through 2025, Soyuz 2.1b remained one of Russia's workhorse rockets, with
the GLONASS constellation requiring periodic replenishment launches.\n- Russia has been working to deploy **GLONASS-K2** satellites, the latest generation of its navigation system.\n- The broader
Russian launch rate has been relatively stable at ~20 orbital launches per year across all vehicle types.\n\n## Specific June 2026 / Upcoming Launch Data\n\n**I was unable to retrieve real-time launch
schedule data** due to tool unavailability. The following caveats apply:\n\n- **Russian military launches from Plesetsk are often not announced far in advance.** Many are only confirmed days before or
even after launch.\n- Tracking sites such as **NextSpaceflight.com**, **SpaceFlightNow.com**, and **RussianSpaceWeb.com** are the best sources for near-real-time schedule updates.\n- The Wikipedia
**\"List of Soyuz-2 launches\"** page is generally well-maintained and includes both past and planned launches.\n\n### Likely Upcoming Mission Types (Based on Historical Patterns)\n1. **GLONASS-K /
GLONASS-K2** replenishment missions (Soyuz 2.1b/Fregat)\n2. **Military reconnaissance** satellites (classified Cosmos designations)\n3. **Lotos-S1** signals intelligence satellites\n4. **Possible
Bars-M** follow-on missions\n\n## Data Limitations\n| Issue | Impact |\n|---|---|\n| Web search tools unavailable | Cannot retrieve real-time schedule |\n| Russian military secrecy | Plesetsk launches
often unannounced until shortly before flight |\n| Training data cutoff | My knowledge does not extend to June 2026 specifics |\n\n## Recommended Sources for Live Data\n- **NextSpaceflight.com**
\u2014 comprehensive upcoming launch list\n- **SpaceFlightNow.com/launch-schedule** \u2014 regularly updated\n- **RussianSpaceWeb.com** \u2014 Anatoly Zak's authoritative coverage of Russian space
programs\n- **Wikipedia: List of Soyuz-2 launches** \u2014 community-maintained, generally current\n\n---", "sources": [{"url": "https://nextspaceflight.com/launches", "title": "Next Spaceflight -
Launch Schedule", "domain": "nextspaceflight.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Could not access - tool unavailable. Recommended as primary source for real-time launch schedule
data."}, {"url": "https://spaceflightnow.com/launch-schedule/", "title": "Spaceflight Now - Launch Schedule", "domain": "spaceflightnow.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Could
not access - tool unavailable. Recommended as primary source for upcoming launches."}, {"url": "https://en.wikipedia.org/wiki/List_of_Soyuz-2_launches", "title": "List of Soyuz-2 launches -
Wikipedia", "domain": "en.wikipedia.org", "accessed_at": "2026-06-17T00:00:00Z", "snippet": "Could not access - tool unavailable. Community-maintained list of all Soyuz-2 launches including planned
missions."}, {"url": "https://www.russianspaceweb.com", "title": "RussianSpaceWeb - Encyclopaedia Astronautica", "domain": "russianspaceweb.com", "accessed_at": "2026-06-17T00:00:00Z", "snippet":
"Could not access - tool unavailable. Authoritative source for Russian space program coverage by Anatoly Zak."}], "key_facts": ["Soyuz 2.1b is Russia's primary medium-lift launch vehicle, featuring an
RD-0124 third-stage engine and digital flight control system.", "Plesetsk cosmodrome (62.9\u00b0N, Arkhangelsk Oblast) is Russia's primary military launch site.", "Typical Soyuz 2.1b launch cadence
from Plesetsk is approximately 4\u20138 launches per year.", "Common Plesetsk payloads: GLONASS-K/K2 navigation satellites, Bars-M reconnaissance, Lotos-S ELINT, and classified Cosmos-series military
satellites.", "Russian military launches from Plesetsk are frequently not announced publicly until days before or after launch.", "Russia's overall orbital launch rate has been approximately 20
launches per year across all vehicle types.", "GLONASS-K2 (latest generation navigation satellites) deployment has been ongoing, requiring periodic Soyuz 2.1b/Fregat launches.", "Real-time schedule
data for June 2026 could not be retrieved due to tool unavailability."], "data_points": [{"metric": "Typical Soyuz 2.1b annual launches from Plesetsk", "value": 6.0, "unit": "launches/year", "as_of":
"2025-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Soyuz-2_launches"}, {"metric": "Russia total annual orbital launches (approximate)", "value": 20.0, "unit": "launches/year", "as_of":
"2025-12-31", "source_url": "https://en.wikipedia.org/wiki/2025_in_spaceflight"}], "created_at": "2026-06-17T09:39:04.792215Z", "updated_at": "2026-06-17T09:39:04.792215Z", "stale_after":
"2026-06-17T15:39:04.792215Z", "state": "fresh", "revision_history": [], "session_id": "a3e747ed-1218-44c2-9640-48d3fd86d4b4", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2,
"failed_count": 0}
```

## 💬 Response

Good. Now let me check the latest launch tracking sources and the Wikipedia 2026 in spaceflight page for real-time status.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Bureau 1440 Rassvet second launch June 2026"
}
```

### 📋 Result

```
{"query": "Bureau 1440 Rassvet second launch June 2026", "results": [{"title": "Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic World", "url":
"https://militarnyi.com/en/articles/rassvet-threat-ukraine-democratic-world/", "snippet": "![Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic
World](https://militarnyi.com/wp-content/uploads/2026/04/1-.jpg)\nOn March 23, 2026, the Russian company Bureau 1440 launched its first operational group of 16 satellites into orbit. These satellites
will serve as the foundation of the future Rassvet satellite system.\nThis launch marked the [beginning](https://militarnyi.com/en/news/russia-cluster-satellites-starlink-rassvet/) of Russia\u2019s
deployment of a Starlink-l", "api_data": null, "hint": null}, {"title": "First Satellite of Russia's Rassvet Broadband Constellation Reenters Atmosphere After Less Than Three Months in Orbit", "url":
"https://www.thedefensenews.com/First-Satellite-of-Russias-Rassvet-Broadband-Constellation-Reenters-Atmosphere-After-Less-Than-Three-Months-in-Orbit/", "snippet": "MOSCOW \u2014 June 6, 2026 :
Russia's effort to develop a domestic low Earth orbit (LEO) broadband satellite network has recorded its first confirmed satellite loss after one of the spacecraft launched under the Rassvet program
reentered Earth's atmosphere and burned up less than three months after launch.\nThe satellite, designated Object 4 and assigned NORAD tracking number 68363, reentered the atmosphere on or around June
6, according to orbital tracking data analyzed by space journalist Anatoly Za", "api_data": null, "hint": null}, {"title": "Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units
remain | Ukraine news - #Mezha", "url": "https://mezha.net/eng/bukvy/2cc5f0f1_bureau_1440_confirms/", "snippet": "Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units
remain\n[\n]\n![Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units remain](https://mezha.net/wp-content/uploads/2026/06/09/bureau-1440-confirms-loss.webp)\nLaunch from
Russia\u2019s Vostochny Cosmodrome; illustrative photo.\nA company monitoring data revealed a missing satellite from the March deployment, raising questions about early reliability and future
rollouts.\nAs reported by the publication [Kommersan", "api_data": null, "hint": null}, {"title": "Russia\u2019s Answer to Starlink Loses One of Its First Satellites", "url":
"https://www.kyivpost.com/post/77850", "snippet": "Russia\u2019s Answer to Starlink Loses One of Its First Satellites\nIn brief: Bureau 1440, the Russian company building the \u201cRassvet\u201d low-
Earth orbit satellite internet service, has confirmed the loss of one of its first operational satellites, launched in March. The remaining 15 satellites from the batch are functioning normally, the
company said. The project \u2013 Moscow\u2019s domestic alternative to SpaceX\u2019s Starlink \u2013 is slated for commercial launch by 2027.\nRussian satellite internet service \u201cRassvet,\u201d
w", "api_data": null, "hint": null}, {"title": "Russia Delays Launch of First Batch of Starlink Rival Satellites - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/01/23/russia-delays-
launch-of-first-batch-of-starlink-rival-satellites-a91761", "snippet": "Russia has postponed the launch of the first batch of low-orbit broadband internet satellites under a project meant to rival
SpaceX\u2019s Starlink, the Kommersant business daily [reported](https://www.kommersant.ru/doc/8364882) Friday.\nThe launch of 16 satellites, originally scheduled for late 2025 and to be carried out
by private aerospace company Bureau 1440, has been pushed back to 2026, according to the report.\nRoscosmos chief Dmitry Bakanov said in September that deployment of the first 300 sat", "api_data":
null, "hint": null}, {"title": "Russian Starlink | Bureau 1440 | | Secret Projects Forum", "url": "https://www.secretprojects.co.uk/threads/russian-starlink-bureau-1440.50822/", "snippet": null,
"api_data": null, "hint": null}, {"title": "Launch of \u201cRussian Starlink\u201d Postponed Due to Satellite Production Failure", "url": "https://militarnyi.com/en/news/launch-of-russian-starlink-
postponed-due-to-satellite-production-failure/", "snippet": "The launch of the first batch of 16 communications satellites, which was to be carried out by the Russian company Bureau 1440 at the end of
last year, has been postponed.\nThis was reported by [The Moscow Times](https://ru.themoscowtimes.com/2026/01/23/zapusk-rossiiskogo-analoga-starlink-perenesli-iz-za-provala-proizvodstva-
sputnikov-a185296).\nIn September 2025, Roscosmos head Dmitry Bakanov promised that by the end of 2025, the first 300 satellites would begin to be deployed in orbit as part of ", "api_data": null,
"hint": null}, {"title": "Rassvet-2 1, 2, 3 - Gunter's Space Page", "url": "https://space.skyrocket.de/doc_sdat/rassvet-2.htm", "snippet": "Rassvet-2 [Byuro 1440]\nThe Russian Rassvet-2 satellites are
improved prototypes for the Byuro-1440 (Bureau 1440) low earth orbit constellation for broadband high-speed internet access.\nThe satellites of the second prototype series feature two laser
communications terminals on each satellites for intersatellite links.\nStarting in 2025, they plan to launch 10-12 rockets into orbit each year, with each rocket capable of carrying approximately 15
satellites. The Russian satellite Internet service is", "api_data": null, "hint": null}, {"title": "Russian \u201cStarlink\u201d Launch Pushed to 2026 Amid Production Shortfalls \u2013 SatNews",
"url": "https://news.satnews.com/2026/01/24/russian-starlink-launch-pushed-to-2026-amid-production-shortfalls/", "snippet": "In a report released on Friday, January 23, 2026, the Russian aerospace
company Bureau 1440 announced the postponement of its initial deployment of 16 high-speed internet satellites. Originally scheduled for late 2025, the launch of the first batch for the
\u201cRassvet\u201d (Dawn) Low Earth Orbit (LEO) constellation has been rescheduled for 2026.\n![](https://satnews.com/wp-content/uploads/2026/01/Rassvet-1-1024x615.jpg)\nThe delay is attributed to
production failures and incomplete assembly of the requir", "api_data": null, "hint": null}, {"title": "Bureau 1440", "url": "https://en.wikipedia.org/wiki/Bureau_1440", "snippet": "Bureau 1440
(Russian: \u0411\u044e\u0440\u043e 1440) is a Russian aerospace company within X Holding (\u0418\u041a\u0421 \u0425\u043e\u043b\u0434\u0438\u043d\u0433), developing a satellite internet constellation
in low Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027
(by which time the 288-satellite constellation should provide global coverage).", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Bureau 1440\", \"url\":
\"https://en.wikipedia.org/wiki/Bureau_1440\", \"extract\": \"Bureau 1440 (Russian: \\u0411\\u044e\\u0440\\u043e 1440) is a Russian aerospace company within X Holding (\\u0418\\u041a\\u0421
\\u0425\\u043e\\u043b\\u0434\\u0438\\u043d\\u0433), developing a satellite internet constellation in low Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched
the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027 (by which time the 288-satellite constellation should provide global coverage).\", \"mode\":
\"full\"}"}]}, "hint": null}]}
```

```json
{
  "url": "https://en.wikipedia.org/wiki/2026_in_spaceflight",
  "prompt": "Find any Bureau 1440 or Rassvet satellite launches listed for June 2026. Also check the upcoming launches section for any Soyuz launches from Plesetsk scheduled for June 2026."
}
```

### 📋 Result

```
{"title": "2026 in spaceflight", "url": "https://en.wikipedia.org/wiki/2026_in_spaceflight", "extract": "This article documents expected notable spaceflight events during the year 2026.", "mode":
"full"}
```

```json
{
  "query": "Soyuz Plesetsk launch June 2026 NOTAM"
}
```

### 📋 Result

```
{"query": "Soyuz Plesetsk launch June 2026 NOTAM", "results": [{"title": "Space Launch Now - Launch Schedule", "url": "https://spacelaunchnow.me/launch/upcoming/?q=Soyuz", "snippet": "Soyuz MS-29 will
carry three cosmonauts and one astronaut to the International Space Station aboard the Soyuz spacecraft from the Baikonur Cosmodrome in Kazakhstan. The crew consists of Roscosmos cosmonauts Pyotr
Dubrov and Anna Kikina, as well as NASA astronaut Anil Menon.\nLow Earth OrbitGlonass-K are the third generation of satellite design for GLONASS satellite navigation system. GLONASS is a Russian
space-based navigation system comparable to the similar GPS and Galileo systems. This generat", "api_data": null, "hint": null}, {"title": "Launch Preview: SLS, Falcon 9, Atlas V, and Soyuz launches
comprise busy launch manifest - NASASpaceFlight.com", "url": "https://www.nasaspaceflight.com/2026/03/launch-preview-033026/", "snippet": "Nine launches are scheduled this week, with rockets expected
to liftoff from Florida, California, Russia, Kazakhstan, and China. Most notably, NASA\u2019s long-awaited Artemis II mission is scheduled to launch the first humans to the Moon in over 50 years on
Wednesday. SpaceX has four Starlink missions scheduled for the week, with Falcon 9 launching two from Florida and two from California. The United Launch Alliance is also expected to launch a new batch
of Amazon Leo internet satellites on an Atlas", "api_data": null, "hint": null}, {"title": "An unannounced launch from Plesetsk delivers payloads into low orbit", "url":
"https://www.russianspaceweb.com/spacecraft-2026-0323.html", "snippet": "![]() |\n|\n|\n|\n![]() |\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n![]() |\nAn
unannounced launch from Plesetsk delivers \"Russian Starlink\"\nOn the evening of March 23, 2026, multiple witnesses in and around the town of Ukhta, northeast of the [Plesetsk launch sit",
"api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Launch Schedule", "url": "https://rocketlaunch.org/launch-schedule/plesetsk-cosmodrome", "snippet": "Plesetsk Cosmodrome Launch
Schedule\nStay updated on Plesetsk Cosmodrome's rocket launches with our real-time schedule. You can see 2 planned space missions on our website. Watch the live stream of any Plesetsk Cosmodrome
rocket launch happening today.\n[All Scheduled Launches](https://rocketlaunch.org/launch-schedule)Plesetsk Cosmodrome\nLaunch Service Provider\nVehicle\nMission\nGlonass-K1 No. 19\nMission
Type\nNavigation\nDestination\nMedium Earth Orbit\nGlonass-K are the third generation of satellite d", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Site 43", "url":
"https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_43", "snippet": "Plesetsk Cosmodrome Site 43, is a launch complex at the Plesetsk Cosmodrome in Russia. It consists of two pads, Sites 43/3 and
43/4 (also known as SK-3 and SK-4) and has been used by R-7-derived rockets since the early 1960s. As of 2025, both pads remain in use for the Soyuz-2.1a and Soyuz-2.1b rockets.\nOriginally
constructed for the R-7A Semyorka missiles, the site hosted its first launch on 21 December 1965, when an R-7A test flight was conducted from Site 43/3. The first launch from Site 43/4", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"Plesetsk Cosmodrome Site 43\", \"url\": \"https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_43\", \"extract\": \"Plesetsk Cosmodrome Site 43,
is a launch complex at the Plesetsk Cosmodrome in Russia. It consists of two pads, Sites 43/3 and 43/4 (also known as SK-3 and SK-4) and has been used by R-7-derived rockets since the early 1960s. As
of 2025, both pads remain in use for the Soyuz-2.1a and Soyuz-2.1b rockets.\\nOriginally constructed for the R-7A Semyorka missiles, the site hosted its first launch on 21 December 1965, when an R-7A
test flight was conducted from Site 43/3. The first launch from Site 43/4 followed on 25 July 1967. After its decommissioning as a missile base, the complex was repurposed for space launches. The
first orbital launch occurred on 3 December 1969, when a Voskhod rocket carried the Kosmos 313 satellite into orbit.\\nBoth pads suffered significant damage due to explosions in the 1980s. The first
incident, on 18 March 1980, which came to be known as the Plesetsk launch pad disaster, occurred when a Vostok-2M rocket exploded during fueling operations at Site 43/4, killing 48 people and injuring
dozens more. The damage was so extensive that the pad remained inactive until 1984. On 18 June 1987, a Soyuz-U rocket exploded at liftoff from Site 43/3.\", \"mode\": \"full\"}"}]}, "hint": null},
{"title": "2026 in spaceflight", "url": "https://en.wikipedia.org/wiki/2026_in_spaceflight", "snippet": "This article documents expected notable spaceflight events during the year 2026.", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"2026 in spaceflight\", \"url\": \"https://en.wikipedia.org/wiki/2026_in_spaceflight\", \"extract\": \"This article documents expected notable
spaceflight events during the year 2026.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "List of R-7 launches (2025%E2%80%932029)", "url":
"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)", "snippet": "This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives between 2025 and 2029. All launches
are orbital satellite launches, unless stated otherwise.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of R-7 launches (2025\\u20132029)\", \"url\":
\"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)\", \"extract\": \"This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives between 2025 and 2029. All
launches are orbital satellite launches, unless stated otherwise.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russian Aerospace Forces Launched \"Soyuz-2.1a\" from Plesetsk", "url":
"https://www1.ru/en/news/2026/04/03/vks-rossii-zapustili-soiuz-21a-s-plesecka.html", "snippet": "The Russian Aerospace Forces successfully launched a Soyuz-2.1a rocket from the Plesetsk cosmodrome,
located in the Arkhangelsk region. The launch took place on April 3 at 9:28 Moscow time. As a result of this launch, a spacecraft intended for use by the Ministry of Defense was put into orbit.\nThe
military department reported that the launch was carried out by the combat crew of the Aerospace Forces, and it proceeded as normal. The device was successfully put into the target orbit, the flight
pa", "api_data": null, "hint": null}, {"title": "List of R-7 launches (2020%E2%80%932024)", "url": "https://en.wikipedia.org/wiki/List_of_R-7_launches_(2020%E2%80%932024)", "snippet": "This is a list
of launches made by the R-7 Semyorka ICBM, and its derivatives between 2020 and 2024. All launches are orbital satellite launches, unless stated otherwise.", "api_data": {"content": [{"type": "text",
"text": "{\"title\": \"List of R-7 launches (2020\\u20132024)\", \"url\": \"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2020%E2%80%932024)\", \"extract\": \"This is a list of launches made by
the R-7 Semyorka ICBM, and its derivatives between 2020 and 2024. All launches are orbital satellite launches, unless stated otherwise.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russia
Space Forces Launch Military Satellites on Soyuz-2.1b from Plesetsk Cosmodrome | TheDefenseWatch.com", "url": "https://thedefensewatch.com/global-news/russia-space-forces-launch-military-satellites-
on-soyuz-2-1b-from-plesetsk/", "snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

Let me check the specific launch tracking pages and the RocketLaunch.org page for the current schedule:

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://rocketlaunch.org/launch-schedule/plesetsk-cosmodrome",
  "prompt": "What launches are scheduled from Plesetsk Cosmodrome? Look for any Bureau 1440, Rassvet, or Soyuz-2.1b launches in June 2026. List all upcoming missions with dates."
}
```

### 📋 Result

```
{"url": "https://rocketlaunch.org/launch-schedule/plesetsk-cosmodrome", "content": "Based on the provided content, here are the scheduled launches from Plesetsk Cosmodrome:\n\n**Upcoming
Missions:**\n\n1. **Glonass-K1 No. 19**\n   - Date: Not specified (updated Dec 20, 3:30am UTC)\n   - Vehicle: Not specified\n   - Mission: Navigation satellite for GLONASS system\n   - Destination:
Medium Earth Orbit\n\n2. **Rassvet-3 Communication Satellites**\n   - Date: **TBD 2026** (no specific date in June 2026 mentioned)\n   - Vehicle: Not specified (but you asked about Soyuz-2.1b - not
mentioned in content)\n   - Mission: Batch of 16 Rassvet-3 satellites for Russian Bureau 1440 constellation\n   - Purpose: Broadband high-speed internet access in Russia\n   - Destination: Low Earth
Orbit\n   - Updated: Jun 17, 9:30am UTC\n\n**Note:** No launches are specifically scheduled for June 2026. The Rassvet-3/Bureau 1440 mission only shows \"TBD 2026\" without a specific month or date.
The launch vehicle (Soyuz-2.1b or other) is not specified in the content.\n\n**Relevant links:**\n- [All Scheduled Launches](https://rocketlaunch.org/launch-schedule)", "title": "Plesetsk Cosmodrome
Launch Schedule"}
```

```json
{
  "query": "\"Rassvet\" OR \"Bureau 1440\" launch June 18 2026"
}
```

### 📋 Result

```
{"query": "\"Rassvet\" OR \"Bureau 1440\" launch June 18 2026", "results": [{"title": "Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic World", "url":
"https://militarnyi.com/en/articles/rassvet-threat-ukraine-democratic-world/", "snippet": "![Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic
World](https://militarnyi.com/wp-content/uploads/2026/04/1-.jpg)\nOn March 23, 2026, the Russian company Bureau 1440 launched its first operational group of 16 satellites into orbit. These satellites
will serve as the foundation of the future Rassvet satellite system.\nThis launch marked the [beginning](https://militarnyi.com/en/news/russia-cluster-satellites-starlink-rassvet/) of Russia\u2019s
deployment of a Starlink-l", "api_data": null, "hint": null}, {"title": "First Satellite of Russia's Rassvet Broadband Constellation Reenters Atmosphere After Less Than Three Months in Orbit", "url":
"https://www.thedefensenews.com/First-Satellite-of-Russias-Rassvet-Broadband-Constellation-Reenters-Atmosphere-After-Less-Than-Three-Months-in-Orbit/", "snippet": "MOSCOW \u2014 June 6, 2026 :
Russia's effort to develop a domestic low Earth orbit (LEO) broadband satellite network has recorded its first confirmed satellite loss after one of the spacecraft launched under the Rassvet program
reentered Earth's atmosphere and burned up less than three months after launch.\nThe satellite, designated Object 4 and assigned NORAD tracking number 68363, reentered the atmosphere on or around June
6, according to orbital tracking data analyzed by space journalist Anatoly Za", "api_data": null, "hint": null}, {"title": "Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units
remain | Ukraine news - #Mezha", "url": "https://mezha.net/eng/bukvy/2cc5f0f1_bureau_1440_confirms/", "snippet": "Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units
remain\n[\n]\n![Bureau 1440 confirms loss of one Svitanok satellite, 15 first-launch units remain](https://mezha.net/wp-content/uploads/2026/06/09/bureau-1440-confirms-loss.webp)\nLaunch from
Russia\u2019s Vostochny Cosmodrome; illustrative photo.\nA company monitoring data revealed a missing satellite from the March deployment, raising questions about early reliability and future
rollouts.\nAs reported by the publication [Kommersan", "api_data": null, "hint": null}, {"title": "Russia\u2019s answer to Starlink just lost its first satellite", "url": "https://defence-
blog.com/russias-answer-to-starlink-just-lost-its-first-satellite/", "snippet": "- Object 4 (NORAD ID 68363) from Russia's Rassvet satellite constellation reentered the atmosphere around June 6, 2026,
after performing no orbital maneuvers since its March 23 launch.\n- As of early June 2026, six Rassvet satellites were raising their orbits while eight others were maintaining altitude, according to
tracking data analyzed by journalist Anatoly Zak.\nThe first satellite from Russia\u2019s nascent attempt to build a domestic broadband constellation fell back into Earth\u2019s atmosphere and ",
"api_data": null, "hint": null}, {"title": "Russia\u2019s new \u2018Starlink\u2011Style\u2019 Rassvet fleet loses its first satellite after weeks \u2014 Object 4 drops out of orbit but 15 others
remain | Tom's Hardware", "url": "https://www.tomshardware.com/tech-industry/russias-rassvet-constellation-loses-its-first-satellite-to-orbital-decay", "snippet": "Join for quick access. Enter your
email below and we'll send confirmation plus sign you up to our newsletter.\nBy submitting your information, you confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to
the\nTerms & Conditions. Geographical rules apply.\nStay On the Cutting Edge: Get the Tom's Hardware Newsletter\nGet Tom's Hardware's best news and in-depth reviews, straight to your inbox.\nYou are
now subscribed\nYour newsletter sign-up was successful\nAn account already exists for ", "api_data": null, "hint": null}, {"title": "Russia Launched First Cluster of Satellites for Its Analog of
Starlink \u2014 the Rassvet Project", "url": "https://militarnyi.com/en/news/russia-cluster-satellites-starlink-rassvet/", "snippet": "The Russian company Bureau 1440 launched the first satellites of
the low-Earth orbit cluster Rassvet, which is considered a Russian alternative to the Starlink system.\nAfter reaching their target orbit, the 16 spacecraft successfully separated from the Soyuz-2.1B
launch vehicle and were transferred to the company\u2019s Flight Control Center.\nOnce all systems have been tested and activated, the satellites will begin their transition to operational orbits,
according to [Bureau 1440](https://t.me/burea", "api_data": null, "hint": null}, {"title": "Russia\u2019s Answer to Starlink Loses One of Its First Satellites", "url":
"https://www.kyivpost.com/post/77850", "snippet": "Russia\u2019s Answer to Starlink Loses One of Its First Satellites\nIn brief: Bureau 1440, the Russian company building the \u201cRassvet\u201d low-
Earth orbit satellite internet service, has confirmed the loss of one of its first operational satellites, launched in March. The remaining 15 satellites from the batch are functioning normally, the
company said. The project \u2013 Moscow\u2019s domestic alternative to SpaceX\u2019s Starlink \u2013 is slated for commercial launch by 2027.\nRussian satellite internet service \u201cRassvet,\u201d
w", "api_data": null, "hint": null}, {"title": "Russian Aerospace Company Launches First Batch of Starlink Rival Satellites - The Moscow Times", "url":
"https://www.themoscowtimes.com/2026/03/24/russian-aerospace-company-launches-first-batch-of-starlink-rival-satellites-a92318", "snippet": "A Russian aerospace company has launched the first batch of
low-orbit satellites that will eventually make up a vast satellite internet constellation under a project meant to rival SpaceX\u2019s Starlink, the business newspaper Kommersant
[reported](https://www.kommersant.ru/doc/8533373) Tuesday.\nThe first elements of the state-funded satellite constellation, known as Rassvet, were supposed to go up into space late last year, but
delays pushed the start of the launch schedule back to this month.\nBure", "api_data": null, "hint": null}, {"title": "Russian \u201cStarlink\u201d Launch Pushed to 2026 Amid Production Shortfalls
\u2013 SatNews", "url": "https://news.satnews.com/2026/01/24/russian-starlink-launch-pushed-to-2026-amid-production-shortfalls/", "snippet": "In a report released on Friday, January 23, 2026, the
Russian aerospace company Bureau 1440 announced the postponement of its initial deployment of 16 high-speed internet satellites. Originally scheduled for late 2025, the launch of the first batch for
the \u201cRassvet\u201d (Dawn) Low Earth Orbit (LEO) constellation has been rescheduled for 2026.\n![](https://satnews.com/wp-content/uploads/2026/01/Rassvet-1-1024x615.jpg)\nThe delay is attributed
to production failures and incomplete assembly of the requir", "api_data": null, "hint": null}, {"title": "Bureau 1440", "url": "https://en.wikipedia.org/wiki/Bureau_1440", "snippet": "Bureau 1440
(Russian: \u0411\u044e\u0440\u043e 1440) is a Russian aerospace company within X Holding (\u0418\u041a\u0421 \u0425\u043e\u043b\u0434\u0438\u043d\u0433), developing a satellite internet constellation
in low Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027
(by which time the 288-satellite constellation should provide global coverage).", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Bureau 1440\", \"url\":
\"https://en.wikipedia.org/wiki/Bureau_1440\", \"extract\": \"Bureau 1440 (Russian: \\u0411\\u044e\\u0440\\u043e 1440) is a Russian aerospace company within X Holding (\\u0418\\u041a\\u0421
\\u0425\\u043e\\u043b\\u0434\\u0438\\u043d\\u0433), developing a satellite internet constellation in low Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched
the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027 (by which time the 288-satellite constellation should provide global coverage).\", \"mode\":
\"full\"}"}]}, "hint": null}]}
```

```json
{
  "url": "https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)",
  "prompt": "Find all Soyuz 2.1b launches listed for 2026, especially any Bureau 1440 or Rassvet missions planned for June 2026. List the dates and payloads for all 2026 launches."
}
```

### 📋 Result

```
{"title": "List of R-7 launches (2025\u20132029)", "url": "https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)", "extract": "This is a list of launches made by the R-7 Semyorka
ICBM, and its derivatives between 2025 and 2029. All launches are orbital satellite launches, unless stated otherwise.", "mode": "full"}
```

## 💭 Thinking

Let me check more specific sources for the latest launch schedule information, particularly RocketLaunch.Live and NextSpaceflight which might have more recent data about the Rassvet second batch.

## 💬 Response

Let me check a few more specific sources for the most up-to-date launch status:

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://nextspaceflight.com/launches/details/7867",
  "prompt": "Find details about any Bureau 1440 Rassvet launch scheduled. What is the current date and status?"
}
```

### 📋 Result

```
{"url": "https://nextspaceflight.com/launches/details/7867", "content": "The provided content does **not** contain any information about a Bureau 1440 Rassvet launch. \n\nThe text describes a **SpaceX
Falcon 9** launch that occurred on **Tuesday, June 3, 2025** carrying Starlink v2-mini satellites. This launch was successful and marked the 500th launch within the Falcon family.\n\nThere is no
mention of Bureau 1440 or Rassvet in the content provided.\n\nRelevant links:\n- [NASASpaceflight.com](https://www.nasaspaceflight.com) - Watch Replay and Read Article options mentioned but specific
URLs not provided in the text", "title": "Starlink Group 12-19"}
```

```json
{
  "query": "Soyuz 2.1b Rassvet launch site:nextspaceflight.com OR site:rocketlaunch.live 2026"
}
```

### 📋 Result

```
{"query": "Soyuz 2.1b Rassvet launch site:nextspaceflight.com OR site:rocketlaunch.live 2026", "results": [{"title": "Soyuz 2.1b | Cosmos 2550", "url":
"https://nextspaceflight.com/launches/details/4094/", "snippet": "/\n/\nLaunch Success\nLiftoff Time (GMT)\n19:50:00\nFriday June 25, 2021\nWatch Replay\nOfficial Livestream\nRead Article\nPayload
identity unconfirmed.\nThe russian Pion-NKS (14F139) satellites are the naval component of the next generation ELINT satellite system Liana. As a replacement for both the passive Soviet ELINT US-PM
and the Soviet active radar US-A, they carry both ELINT sensors as well as an active radar. The Liana system replaces both the Tselina-2 with Lotos satellites and the naval US-PM an", "api_data":
null, "hint": null}, {"title": "Soyuz 2.1b | Cosmos 2580", "url": "https://nextspaceflight.com/launches/details/7695/", "snippet": "/\n/\nLaunch Success\nLiftoff Time (GMT)\n18:03:13\nWednesday
December 4, 2024\nWatch Replay\nOfficial Livestream\nRead Article\nPayload type not confirmed.\nThe Russian Lotos-S1 (14F145) satellites are one component of the next-generation ELINT satellite
system, Liana. A development version was flown as Lotos-S. The Liana system replaces both the Tselina-2 with Lotos satellites and the naval US-PM with Pion-NKS (14F139) spacecraft.\nLow Earth Orbit\n1
Payload\n6,000 kilograms\nManufacturer\nPrice\n$20.00 milli", "api_data": null, "hint": null}, {"title": "Soyuz 2.1b | Resurs-P No.5", "url": "https://nextspaceflight.com/launches/details/3919/",
"snippet": "/\n/\nLaunch Success\nLiftoff Time (GMT)\n07:45:42\nWednesday December 25, 2024\nWatch Replay\nOfficial Livestream\nRead Article\n2000th R-7 rocket series launch.\nResurs-P is a series of
Russian commercial Earth observation satellites capable of acquiring high-resolution imagery (resolution up to 1.0 m). The spacecraft is operated by Roscosmos as a replacement for the Resurs-DK No.1
satellite.\nSun-Synchronous Orbit\n1 Payload\n6,570 kilograms\nManufacturer\nPrice\n$20.00 million\nRocket\nHeight: 44.08m\nPayload ", "api_data": null, "hint": null}, {"title": "Rassvet-3 (16 x)
Mission (Soyuz-2) - RocketLaunch.Live", "url": "https://www.rocketlaunch.live/launch/rassvet-3-16-x", "snippet": "|\nAll changes are verified for accuracy before being published!\n|\n| Provider
|\n|\n| Vehicle |\n|\n| Location |\nLC-43/4 Plesetsk Cosmodrome\n[Russia](/?filter=russia)\n|\n|\nAll dates and times should be submitted in UTC timezone.\nUse Estimated Date if you don't know the
official launch date and time; otherwise, use Window Opens/Closes and/or Planned T-0, which will override the Estimated Date.\n|\n| \u2014 Estimated Date \u2014 |\n| Date |\n|\n| \u2014 Window Opens
\u2014 |\n| Date |\n|\n| Time |\n|\n| Launch Date |\n|\n| Launch Time", "api_data": null, "hint": null}, {"title": "Cosmos 2584 | Soyuz 2.1b/Fregat-M", "url":
"https://nextspaceflight.com/launches/details/2725/", "snippet": "/\n/\nLaunch Success\nLiftoff Time (GMT)\n22:22:17\nSunday March 2, 2025\nWatch Replay\nOfficial Livestream\nRead Article\nGLONASS-K
is the latest satellite design intended as a part of the Russian GLONASS radio-based satellite navigation system. Developed by ISS Reshetnev (Reshetnev Information Satellite Systems) and first
launched on 26 February 2011, it is a substantial improvement of the previous GLONASS-M second-generation satellites, having a longer lifespan and better accuracy.\nMedium Earth Orbit\n", "api_data":
null, "hint": null}, {"title": "Rassvet-3 batch 2 (16 x) Mission (Soyuz-2) - RocketLaunch.Live", "url": "https://www.rocketlaunch.live/launch/rassvet-3-batch-2-16", "snippet": "|\nAll changes are
verified for accuracy before being published!\n|\n| Provider |\n|\n| Vehicle |\n|\n| Location |\nLC-43/4 Plesetsk Cosmodrome\n[Russia](/?filter=russia)\n|\n|\nAll dates and times should be submitted
in UTC timezone.\nUse Estimated Date if you don't know the official launch date and time; otherwise, use Window Opens/Closes and/or Planned T-0, which will override the Estimated Date.\n|\n| \u2014
Estimated Date \u2014 |\n| Date |\n|\n| \u2014 Window Opens \u2014 |\n| Date |\n|\n| Time |\n|\n| Launch Date |\nJune 18, 2026\n|", "api_data": null, "hint": null}, {"title": "Soyuz-2 Launch Schedule
- RocketLaunch.Live", "url": "https://www.rocketlaunch.live/?filter=soyuz-2", "snippet": "Select only the launch providers and facilities you care about to filter this page (tags coming soon). Save
your feed for ease of access, then subscribe to it in your favorite calendar app!\nThe second batch of Rassvet-3 satellites for Bureau 1440 is scheduled to launch between April 24 and 28, 2026 with
launch window 11:00-21:00 UTC. This information is based on...\nRocketLaunch.Live is supported by our Premium Members!\nThis site thrives on the contributions from space enthusiasts like you!\nOur c",
"api_data": null, "hint": null}, {"title": "Baikonur Cosmodrome Site 31", "url": "https://en.wikipedia.org/wiki/Baikonur_Cosmodrome_Site_31", "snippet": "Baikonur Site 31, also designated as Site
31/6, is a launch complex at the Baikonur Cosmodrome in Kazakhstan. It serves as a key launch site, supporting Soyuz-2 launches for both crewed and uncrewed missions. The site was first utilized on 14
January 1961 for a test flight of the R-7A, an intercontinental ballistic missile on which the Soyuz rocket family was based. Since 2020, following Roscosmos' transition from the Soyuz-FG to the
Soyuz-2 rocket for crewed missions, Site 31/6 has become Russi", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Baikonur Cosmodrome Site 31\", \"url\":
\"https://en.wikipedia.org/wiki/Baikonur_Cosmodrome_Site_31\", \"extract\": \"Baikonur Site 31, also designated as Site 31/6, is a launch complex at the Baikonur Cosmodrome in Kazakhstan. It serves as
a key launch site, supporting Soyuz-2 launches for both crewed and uncrewed missions. The site was first utilized on 14 January 1961 for a test flight of the R-7A, an intercontinental ballistic
missile on which the Soyuz rocket family was based. Since 2020, following Roscosmos' transition from the Soyuz-FG to the Soyuz-2 rocket for crewed missions, Site 31/6 has become Russia's only
operational facility for crewed Soyuz flights to the International Space Station (ISS). This shift occurred after Site 1/5, also known as Gagarin's Start, failed to secure funding for upgrades to
accommodate the slightly larger Soyuz-2 rocket. Before that, it only saw a handful of crewed flights when Site 1/5 was unavailable.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Soyuz MS-30",
"url": "https://en.wikipedia.org/wiki/Soyuz_MS-30", "snippet": "Soyuz MS-30 is a planned Russian crewed Soyuz spaceflight to launch from Baikonur in March 2027 to the International Space Station.",
"api_data": {"content": [{"type": "text", "text": "{\"title\": \"Soyuz MS-30\", \"url\": \"https://en.wikipedia.org/wiki/Soyuz_MS-30\", \"extract\": \"Soyuz MS-30 is a planned Russian crewed Soyuz
spaceflight to launch from Baikonur in March 2027 to the International Space Station.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Vostochny Cosmodrome Site 1S", "url":
"https://en.wikipedia.org/wiki/Vostochny_Cosmodrome_Site_1S", "snippet": "The Vostochny Cosmodrome Site 1S (Russian: \u041f\u043b\u043e\u0449\u0430\u0434\u043a\u0430-1\u0421)  is a launch complex at
the Vostochny Cosmodrome in Russia. It consists of a single pad for use by the Soyuz-2 launch vehicles.\nOn 28 April 2016, the first launch from the Vostochny Cosmodrome took place from this pad. The
third launch took place on 1 February 2018. The Meteor M2-2 mission, the fifth launch from this site, took place 5 July 2019. Since December 2020, Arianespace uses this site to launch OneWeb
satellites, with 6 batches lau", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Vostochny Cosmodrome Site 1S\", \"url\":
\"https://en.wikipedia.org/wiki/Vostochny_Cosmodrome_Site_1S\", \"extract\": \"The Vostochny Cosmodrome Site 1S (Russian: \\u041f\\u043b\\u043e\\u0449\\u0430\\u0434\\u043a\\u0430-1\\u0421)  is a
launch complex at the Vostochny Cosmodrome in Russia. It consists of a single pad for use by the Soyuz-2 launch vehicles.\\nOn 28 April 2016, the first launch from the Vostochny Cosmodrome took place
from this pad. The third launch took place on 1 February 2018. The Meteor M2-2 mission, the fifth launch from this site, took place 5 July 2019. Since December 2020, Arianespace uses this site to
launch OneWeb satellites, with 6 batches launched between December 2020 and October 2021.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

```json
{
  "query": "Plesetsk cosmodrome launch June 17 18 19 2026"
}
```

### 📋 Result

```
{"query": "Plesetsk cosmodrome launch June 17 18 19 2026", "results": [{"title": "Plesetsk Cosmodrome Overview", "url": "https://rocketlaunch.org/rocket-launch-sites/plesetsk-cosmodrome", "snippet":
"Plesetsk Cosmodrome Overview\nA complete overview of the Plesetsk Cosmodrome launch site, including key info, launch stats and the companies that launch from it.\n[Rocket Launch
Sites](https://rocketlaunch.org/rocket-launch-sites)Plesetsk Cosmodrome\n![Plesetsk Cosmodrome launch site](https://rocket-launch-today.s3.us-
east-1.amazonaws.com/plesetsk_cosmodrome_88f6d69a0b.jpg)\nBasic Info\nName\nPlesetsk Cosmodrome\nTotal Launch Count\n1685\nFirst Launch\n17 Mar 1966\nLast Launch\n23 Apr 2026\nLocation\nRussia\nP",
"api_data": null, "hint": null}, {"title": "ESA - Earth from Space: Plesetsk Cosmodrome", "url": "https://www.esa.int/Applications/Observing_the_Earth/Earth_from_Space_Plesetsk_Cosmodrome", "snippet":
"Earth from Space: Plesetsk Cosmodrome\nThis image shows a part of the vast territory of the Plesetsk Cosmodrome \u2013 the only orbital launch site situated within European territory \u2013 located
in the Archangel region (Arkhangelsk Oblast) of northern Russia.\nSurrounded by boreal forest, the Severnaya River is visible flowing across the top. The city of Plesetsk is situated some 30 km
southwest of the large bend in the river.\nPlesetsk was founded as the world\u2019s first operational intercontinental ballist", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Site
35", "url": "https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_35", "snippet": "Site 35 at the Plesetsk Cosmodrome is a launch complex used by the Angara rocket. The complex has a single launch
pad, Site 35/1, which was first used for the maiden flight of the Angara in July 2014.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Plesetsk Cosmodrome Site 35\", \"url\":
\"https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_35\", \"extract\": \"Site 35 at the Plesetsk Cosmodrome is a launch complex used by the Angara rocket. The complex has a single launch pad,
Site 35/1, which was first used for the maiden flight of the Angara in July 2014.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Plesetsk Cosmodrome Site 43", "url":
"https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_43", "snippet": "Plesetsk Cosmodrome Site 43, is a launch complex at the Plesetsk Cosmodrome in Russia. It consists of two pads, Sites 43/3 and
43/4 (also known as SK-3 and SK-4) and has been used by R-7-derived rockets since the early 1960s. As of 2025, both pads remain in use for the Soyuz-2.1a and Soyuz-2.1b rockets.\nOriginally
constructed for the R-7A Semyorka missiles, the site hosted its first launch on 21 December 1965, when an R-7A test flight was conducted from Site 43/3. The first launch from Site 43/4", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"Plesetsk Cosmodrome Site 43\", \"url\": \"https://en.wikipedia.org/wiki/Plesetsk_Cosmodrome_Site_43\", \"extract\": \"Plesetsk Cosmodrome Site 43,
is a launch complex at the Plesetsk Cosmodrome in Russia. It consists of two pads, Sites 43/3 and 43/4 (also known as SK-3 and SK-4) and has been used by R-7-derived rockets since the early 1960s. As
of 2025, both pads remain in use for the Soyuz-2.1a and Soyuz-2.1b rockets.\\nOriginally constructed for the R-7A Semyorka missiles, the site hosted its first launch on 21 December 1965, when an R-7A
test flight was conducted from Site 43/3. The first launch from Site 43/4 followed on 25 July 1967. After its decommissioning as a missile base, the complex was repurposed for space launches. The
first orbital launch occurred on 3 December 1969, when a Voskhod rocket carried the Kosmos 313 satellite into orbit.\\nBoth pads suffered significant damage due to explosions in the 1980s. The first
incident, on 18 March 1980, which came to be known as the Plesetsk launch pad disaster, occurred when a Vostok-2M rocket exploded during fueling operations at Site 43/4, killing 48 people and injuring
dozens more. The damage was so extensive that the pad remained inactive until 1984. On 18 June 1987, a Soyuz-U rocket exploded at liftoff from Site 43/3.\", \"mode\": \"full\"}"}]}, "hint": null},
{"title": "Plesetsk Cosmodrome", "url": "https://www.daviddarling.info/encyclopedia/P/Plesetsk.html", "snippet": "Plesetsk Cosmodrome\n![Plesetsk
Cosmodrome](../../images/Plesetsk_Cosmodrome.jpg)\nPlesetsk Cosmodrome is a Russian launch complex and missile test range, located at 62.8\u00b0 N, 40.4\u00b0\nE, which has launched the most
satellites since the beginning of the Space\nAge. Built in 1960, south of Archangel in northern Russia, its existence\nwas not officially acknowledged by the Soviet Union until 1987 but
became\npublicly known in the West after the tracking of Cosmos 112 by a schoolboy-team\nat Kettering Gramma", "api_data": null, "hint": null}, {"title": "Plesetsk", "url":
"http://www.astronautix.com/p/plesetsk.html", "snippet": "[Home](../index.html) - [Search](../s/search.html) - [Browse](../b/browse.html) - Alphabetic Index: [0](../0/index.html)-
[1](../1/index.html)- [2](../2/index.html)- [3](../3/index.html)- [4](../4/index.html)- [5](../5/index.html)- [6](../6/index.html)- [7](../7/index.html)- [8](../8/index.html)-
[9](../9/index.html)\n[A](../a/index.html)- [B](../b/index.html)- [C](../c/index.html)- [D](../d/index.html)- [E](../e/index.html)- [F](../f/index.html)- [G](../g/index.html)- [H](../h/index.html)-
[I](.", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome - Space Launch Schedule", "url": "https://www.spacelaunchschedule.com/category/plesetsk-cosmodrome/", "snippet": "Join our
community of space enthusiasts for just $3/month and enjoy an ad-free experience across our app and website. Your support helps us deliver the best rocket launch tracking experience in the galaxy!
\ud83d\ude80\nTrack every Plesetsk Cosmodrome rocket launch with our comprehensive schedule featuring real-time updates on today's launches and upcoming missions. Get instant access to live streams,
detailed mission profiles, launch countdowns, and complete coverage of Plesetsk Cosmodrome space operations", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Launch Schedule", "url":
"https://rocketlaunch.org/launch-schedule/plesetsk-cosmodrome", "snippet": "Plesetsk Cosmodrome Launch Schedule\nStay updated on Plesetsk Cosmodrome's rocket launches with our real-time schedule. You
can see 2 planned space missions on our website. Watch the live stream of any Plesetsk Cosmodrome rocket launch happening today.\n[All Scheduled Launches](https://rocketlaunch.org/launch-
schedule)Plesetsk Cosmodrome\nLaunch Service Provider\nVehicle\nMission\nGlonass-K1 No. 19\nMission Type\nNavigation\nDestination\nMedium Earth Orbit\nGlonass-K are the third generation of satellite
d", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Launch Facilities - Russia and Space Transportation Systems", "url":
"https://www.globalsecurity.org/space/world/russia/plesetsk3.htm", "snippet": "Plesetsk Cosmodrome\n62.8 N 40.7 E\nOverview, Supporting Facilities and Launch Vehicles of the\nSoviet Space Program
*\n1981-1987\n1. Prepared by the late Geoffrey E. Perry M.B.E. [1927-2000] Mr. Perry was a Senior Teacher at Kettering Boys School, England, and the leader of the Kettering Group of amateur satellite
observers.\nLAUNCH SITES IN THE SOVIET UNION\nThe Soviet Union has three collections of space launch pads, just as does the United States. Curiously, even the functions of these three locati",
"api_data": null, "hint": null}]}
```

## 💭 Thinking

Very important finding from RocketLaunch.Live: The "Rassvet-3 batch 2 (16 x)" mission page shows "Launch Date: June 18, 2026" from "LC-43/4 Plesetsk Cosmodrome." Let me also look at the Soyuz-2 launch schedule from RocketLaunch.Live, which mentioned the April 24-28 window that was postponed.

Also note: The RocketLaunch.org Plesetsk page shows "Last Launch: 23 Apr 2026" — that was a military launch (Soyuz-2.1a with Cosmos-series payload), not Rassvet.
So I'm seeing some interesting discrepancies across sources: RocketLaunch.Live pins the second batch to June 18, 2026, while RocketLaunch.org just says "TBD 2026," and the independent calendars align with that June 18 estimate. The original April window got pushed back, and Bureau 1440 hasn't made any official announcement yet—they typically keep launch dates under wraps anyway.

Now I'm noticing the question's close time is June 17, 2026, which means we're essentially at the launch window right now (June 13-27). I should look for the most recent updates to see if anything has actually happened or if there's breaking news about this mission.

## 💬 Response

Critical finding - RocketLaunch.Live shows "Rassvet-3 batch 2" with a launch date of June 18, 2026. Let me check for the very latest status:

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.rocketlaunch.live/launch/rassvet-3-batch-2-16",
  "prompt": "What is the current scheduled date and time for this Rassvet-3 batch 2 launch? What is the launch status - is it confirmed, tentative, or TBD? Any NOTAMs or window information?"
}
```

### 📋 Result

```
{"url": "https://www.rocketlaunch.live/launch/rassvet-3-batch-2-16", "content": "Based on the provided content:\n\n**Launch Date & Time:**\n- **Date:** June 18, 2026\n- **Time:** Not specified in the
content (appears to be blank/TBD)\n\n**Launch Status:**\nThe content doesn't explicitly state whether this is confirmed, tentative, or TBD. However, the presence of specific dates in multiple fields
(Planned T-0, Window Opens/Closes) all showing June 18, 2026 suggests it's at least tentatively scheduled.\n\n**NOTAMs/Window Information:**\n- Window Opens: June 18, 2026 (time not specified)\n-
Window Closes: June 18, 2026 (time not specified)\n- No NOTAM information is provided in the content\n\n**Additional Details:**\n- Provider: Not specified in content\n- Vehicle: Not specified in
content  \n- Location: LC-43/4, Plesetsk Cosmodrome, Russia\n\n**Relevant links:**\n- [Russia launches](/?filter=russia)", "title": "Rassvet-3 batch 2 (16 x) Mission (Soyuz-2)"}
```

```json
{
  "query": "Rassvet Soyuz launch Plesetsk June 2026 NOTAM airspace closure"
}
```

### 📋 Result

```
{"query": "Rassvet Soyuz launch Plesetsk June 2026 NOTAM airspace closure", "results": [{"title": "Space Launch Now - Launch Schedule", "url": "https://spacelaunchnow.me/launch/upcoming/?q=Soyuz",
"snippet": "Soyuz MS-29 will carry three cosmonauts and one astronaut to the International Space Station aboard the Soyuz spacecraft from the Baikonur Cosmodrome in Kazakhstan. The crew consists of
Roscosmos cosmonauts Pyotr Dubrov and Anna Kikina, as well as NASA astronaut Anil Menon.\nLow Earth OrbitGlonass-K are the third generation of satellite design for GLONASS satellite navigation system.
GLONASS is a Russian space-based navigation system comparable to the similar GPS and Galileo systems. This generat", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Launch Schedule",
"url": "https://rocketlaunch.org/launch-schedule/plesetsk-cosmodrome", "snippet": "Plesetsk Cosmodrome Launch Schedule\nStay updated on Plesetsk Cosmodrome's rocket launches with our real-time
schedule. You can see 2 planned space missions on our website. Watch the live stream of any Plesetsk Cosmodrome rocket launch happening today.\n[All Scheduled
Launches](https://rocketlaunch.org/launch-schedule)Plesetsk Cosmodrome\nLaunch Service Provider\nVehicle\nMission\nGlonass-K1 No. 19\nMission Type\nNavigation\nDestination\nMedium Earth
Orbit\nGlonass-K are the third generation of satellite d", "api_data": null, "hint": null}, {"title": "An unannounced launch from Plesetsk delivers payloads into low orbit", "url":
"https://www.russianspaceweb.com/spacecraft-2026-0323.html", "snippet": "![]() |\n|\n|\n|\n![]() |\n||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n![]() |\nAn
unannounced launch from Plesetsk delivers \"Russian Starlink\"\nOn the evening of March 23, 2026, multiple witnesses in and around the town of Ukhta, northeast of the [Plesetsk launch sit",
"api_data": null, "hint": null}, {"title": "Russian Federal Space Agency (ROSCOSMOS) - Space Launch Schedule", "url": "https://www.spacelaunchschedule.com/category/russian-federal-space-agency-
roscosmos/", "snippet": "Join our community of space enthusiasts for just $3/month and enjoy an ad-free experience across our app and website. Your support helps us deliver the best rocket launch
tracking experience in the galaxy! \ud83d\ude80\nTrack every Russian Federal Space Agency (ROSCOSMOS) rocket launch with our comprehensive schedule featuring real-time updates on today's launches and
upcoming missions. Get instant access to live streams, detailed mission profiles, launch countdowns, and complete coverage of Russian Federal", "api_data": null, "hint": null}, {"title": "ROSCOSMOS
Launch Schedule", "url": "https://rocketlaunch.org/launch-schedule/roscosmos", "snippet": "ROSCOSMOS Launch Schedule\nStay updated on ROSCOSMOS's rocket launches with our real-time schedule. You can
see 6 planned space missions on our website. Watch the live stream of any ROSCOSMOS rocket launch happening today.\n[All Scheduled Launches](https://rocketlaunch.org/launch-schedule)ROSCOSMOS\nLaunch
Service Provider\nVehicle\nSpacecraft Stage\nSoyuz MS\nCrew\n![RU flag](https://flagcdn.com/w40/ru.png)\nPyotr Dubrov\n![US flag](https://flagcdn.com/w40/us.png)\nAnil Menon\n![RU
flag](https://flagcdn.co", "api_data": null, "hint": null}, {"title": "Russia Launches First 16 \u201cRassvet\u201d Satellites in Bid to Build a Starlink\u2011Like Network - AeroMorning", "url":
"https://aeromorning.com/en/russia-launches-first-16-rassvet-satellites-in-bid-to-build-a-starlink-like-network/", "snippet": "AeroMorning March 24, 26\nOn March 23, 2026, Russian aerospace firm
Bureau 1440 successfully launched the first batch of low\u2011Earth orbit (LEO) satellites under the Rassvet project \u2014 a state\u2011backed effort aimed at creating a domestic alternative to
Starlink, the global broadband constellation operated by SpaceX.\nThe launch, which occurred from the Plesetsk Cosmodrome aboard a Soyuz 2.1b rocket, placed 16 satellites into orbit. According to
company statements and Russian media, each spacecraft sepa", "api_data": null, "hint": null}, {"title": "RFSA 16 x Rassvet-3 Soyuz 2.1b Rocket Launch", "url":
"https://www.spacelaunchschedule.com/launch/soyuz-2-1b-16-x-rassvet-3-2/", "snippet": "Russian Federal Space Agency (ROSCOSMOS) 16 x Rassvet-3 Soyuz 2.1b\nAbout the 16 x Rassvet-3 Mission\n- Type:
Communications\n- Orbit: Polar Orbit\n- Launch Cost: $80,000,000\nNote: Payload identities uncertain.\nBatch of 16 Rassvet-3 Low Earth Orbit communication satellites for the Russian Byuro-1440 (Bureau
1440) constellation for broadband high-speed internet access in Russia.\nLaunch Pad & Location\nUnknown Pad\nPlesetsk Cosmodrome, Russian Federation\nPlesetsk Cosmodrome is a Russian spaceport
locate", "api_data": null, "hint": null}, {"title": "Soyuz MS-22 - Supercluster", "url": "https://www.supercluster.com/launches/ms-22", "snippet": "The Soyuz spacecraft is a crew capsule launched on
the Russian-built Soyuz rocket. It is one of the most reliable human spacecraft in the world and has a longer service record than any other human space system.\nConstructed by the Soviet Union for
their lunar program, the Soyuz capsule flew an uncrewed test flight in November 1966 and carried people for the first time on April 23rd, 1967.\nWhile the Russians never made it to the Moon, the Soyuz
spacecraft became a workhorse for human low Earth orb", "api_data": null, "hint": null}, {"title": "16 x Rassvet-3 | Soyuz 2.1b", "url": "https://nextspaceflight.com/launches/details/5655/",
"snippet": "/\n/\nLaunch Success\nLiftoff Time (GMT)\n17:24:00\nMonday March 23, 2026\nTrack Payloads\nBatch of 16 Rassvet-3 Low Earth Orbit communication satellites for the Russian Byuro-1440 (Bureau
1440) constellation for broadband high-speed internet access in Russia.\nPolar Orbit\n16 Payloads\nManufacturer\nPrice\n$20.00 million\nRocket\nHeight: 44.08m\nPayload to Orbit\nLEO: 8,020 kg\nGTO: 0
kg\nLiftoff Thrust\n4,550 Kilonewtons\nFairing\nDiameter: 4.11m\nHeight: 8.36m\nStages\n3\nStrap-ons\n4\n101st\nMission\n2nd\nMission of 2026", "api_data": null, "hint": null}, {"title": "List of R-7
launches (2025%E2%80%932029)", "url": "https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)", "snippet": "This is a list of launches made by the R-7 Semyorka ICBM, and its
derivatives between 2025 and 2029. All launches are orbital satellite launches, unless stated otherwise.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of R-7 launches
(2025\\u20132029)\", \"url\": \"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)\", \"extract\": \"This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives
between 2025 and 2029. All launches are orbital satellite launches, unless stated otherwise.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

```json
{
  "query": "\"Bureau 1440\" OR \"Rassvet\" launch 2026 second batch schedule delay"
}
```

### 📋 Result

```
{"query": "\"Bureau 1440\" OR \"Rassvet\" launch 2026 second batch schedule delay", "results": [{"title": "Russia Delays Launch of First Batch of Starlink Rival Satellites - The Moscow Times", "url":
"https://www.themoscowtimes.com/2026/01/23/russia-delays-launch-of-first-batch-of-starlink-rival-satellites-a91761", "snippet": "Russia has postponed the launch of the first batch of low-orbit
broadband internet satellites under a project meant to rival SpaceX\u2019s Starlink, the Kommersant business daily [reported](https://www.kommersant.ru/doc/8364882) Friday.\nThe launch of 16
satellites, originally scheduled for late 2025 and to be carried out by private aerospace company Bureau 1440, has been pushed back to 2026, according to the report.\nRoscosmos chief Dmitry Bakanov
said in September that deployment of the first 300 sat", "api_data": null, "hint": null}, {"title": "Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic World", "url":
"https://militarnyi.com/en/articles/rassvet-threat-ukraine-democratic-world/", "snippet": "![Russian Rassvet Satellite System: Strategic Threat to Ukraine and the Democratic
World](https://militarnyi.com/wp-content/uploads/2026/04/1-.jpg)\nOn March 23, 2026, the Russian company Bureau 1440 launched its first operational group of 16 satellites into orbit. These satellites
will serve as the foundation of the future Rassvet satellite system.\nThis launch marked the [beginning](https://militarnyi.com/en/news/russia-cluster-satellites-starlink-rassvet/) of Russia\u2019s
deployment of a Starlink-l", "api_data": null, "hint": null}, {"title": "Russian \u201cStarlink\u201d Launch Pushed to 2026 Amid Production Shortfalls \u2013 SatNews", "url":
"https://satnews.com/2026/01/24/russian-starlink-launch-pushed-to-2026-amid-production-shortfalls/", "snippet": "In a report released on Friday, January 23, 2026, the Russian aerospace company Bureau
1440 announced the postponement of its initial deployment of 16 high-speed internet satellites. Originally scheduled for late 2025, the launch of the first batch for the \u201cRassvet\u201d (Dawn) Low
Earth Orbit (LEO) constellation has been rescheduled for 2026.\n![](https://satnews.com/wp-content/uploads/2026/01/Rassvet-1-1024x615.jpg)\nThe delay is attributed to production failures and
incomplete assembly of the requir", "api_data": null, "hint": null}, {"title": "Putin Implied That Rassvet Satellites Will Be Used to Control Drones", "url": "https://militarnyi.com/en/news/putin-
implied-rassvet-satellite-control-uav/", "snippet": "Russia is working on deploying a constellation of low-Earth orbit satellites to control \u201cheavy drones.\u201d This likely refers to the Rassvet
communication system from the Bureau 1440.\nThis was stated by Russian President [Vladimir Putin](http://kremlin.ru/events/president/news/80017).\n\u201cPerhaps such work is ongoing. By 2023, the
first satellites capable of performing the tasks you mentioned will already be in space. In 2024-2025, this work will continue,\u201d he said.\nAccording to him, the system is com", "api_data": null,
"hint": null}, {"title": "Russia\u2019s Answer to Starlink Loses One of Its First Satellites", "url": "https://www.kyivpost.com/post/77850", "snippet": "Russia\u2019s Answer to Starlink Loses One of
Its First Satellites\nIn brief: Bureau 1440, the Russian company building the \u201cRassvet\u201d low-Earth orbit satellite internet service, has confirmed the loss of one of its first operational
satellites, launched in March. The remaining 15 satellites from the batch are functioning normally, the company said. The project \u2013 Moscow\u2019s domestic alternative to SpaceX\u2019s Starlink
\u2013 is slated for commercial launch by 2027.\nRussian satellite internet service \u201cRassvet,\u201d w", "api_data": null, "hint": null}, {"title": "Launch of \u201cRussian Starlink\u201d
Postponed Due to Satellite Production Failure", "url": "https://militarnyi.com/en/news/launch-of-russian-starlink-postponed-due-to-satellite-production-failure/", "snippet": "The launch of the first
batch of 16 communications satellites, which was to be carried out by the Russian company Bureau 1440 at the end of last year, has been postponed.\nThis was reported by [The Moscow
Times](https://ru.themoscowtimes.com/2026/01/23/zapusk-rossiiskogo-analoga-starlink-perenesli-iz-za-provala-proizvodstva-sputnikov-a185296).\nIn September 2025, Roscosmos head Dmitry Bakanov promised
that by the end of 2025, the first 300 satellites would begin to be deployed in orbit as part of ", "api_data": null, "hint": null}, {"title": "Russian Aerospace Company Launches First Batch of
Starlink Rival Satellites - The Moscow Times", "url": "https://www.themoscowtimes.com/2026/03/24/russian-aerospace-company-launches-first-batch-of-starlink-rival-satellites-a92318", "snippet": "A
Russian aerospace company has launched the first batch of low-orbit satellites that will eventually make up a vast satellite internet constellation under a project meant to rival SpaceX\u2019s
Starlink, the business newspaper Kommersant [reported](https://www.kommersant.ru/doc/8533373) Tuesday.\nThe first elements of the state-funded satellite constellation, known as Rassvet, were supposed
to go up into space late last year, but delays pushed the start of the launch schedule back to this month.\nBure", "api_data": null, "hint": null}, {"title": "Rassvet's 16-Satellite Launch Marks
Exponential Gap Behind Starlink's S-Curve", "url": "https://www.ainvest.com/news/rassvet-16-satellite-launch-marks-exponential-gap-starlink-curve-2603/", "snippet":
"[.](https://www.ainvest.com/news/origin-proof/sb_0a9dcda14c89f5bf)\nRassvet's 16-Satellite Launch Marks Exponential Gap Behind Starlink's S-Curve\n[Eli Grant](https://www.ainvest.com/news/author/eli-
grant/)Reviewed by\n[The Newsroom](https://www.ainvest.com/news/author/newsroom/)\n![Speaker
1](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/shelley_cec5c0ae1755765151507.png)\n![Speaker
2](https://cdn.ainvest.com/articles/focusnews/coverimage/content/pictures/beth_5ba90823175576", "api_data": null, "hint": null}, {"title": "Rassvet-3 batch 2 (16 x) Mission (Soyuz-2) -
RocketLaunch.Live", "url": "https://www.rocketlaunch.live/launch/rassvet-3-batch-2-16", "snippet": "|\nAll changes are verified for accuracy before being published!\n|\n| Provider |\n|\n| Vehicle
|\n|\n| Location |\nLC-43/4 Plesetsk Cosmodrome\n[Russia](/?filter=russia)\n|\n|\nAll dates and times should be submitted in UTC timezone.\nUse Estimated Date if you don't know the official launch
date and time; otherwise, use Window Opens/Closes and/or Planned T-0, which will override the Estimated Date.\n|\n| \u2014 Estimated Date \u2014 |\n| Date |\n|\n| \u2014 Window Opens \u2014 |\n| Date
|\n|\n| Time |\n|\n| Launch Date |\nJune 18, 2026\n|", "api_data": null, "hint": null}, {"title": "Bureau 1440", "url": "https://en.wikipedia.org/wiki/Bureau_1440", "snippet": "Bureau 1440 (Russian:
\u0411\u044e\u0440\u043e 1440) is a Russian aerospace company within X Holding (\u0418\u041a\u0421 \u0425\u043e\u043b\u0434\u0438\u043d\u0433), developing a satellite internet constellation in low
Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027 (by
which time the 288-satellite constellation should provide global coverage).", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Bureau 1440\", \"url\":
\"https://en.wikipedia.org/wiki/Bureau_1440\", \"extract\": \"Bureau 1440 (Russian: \\u0411\\u044e\\u0440\\u043e 1440) is a Russian aerospace company within X Holding (\\u0418\\u041a\\u0421
\\u0425\\u043e\\u043b\\u0434\\u0438\\u043d\\u0433), developing a satellite internet constellation in low Earth orbit for high-speed broadband data transmission. In 2023 and 2024, the company launched
the experimental missions Rassvet-1 and Rassvet-2, with commercial operations scheduled for 2027 (by which time the 288-satellite constellation should provide global coverage).\", \"mode\":
\"full\"}"}]}, "hint": null}]}
```

## 💭 Thinking

Let me also check the SpaceLaunchSchedule page for the Rassvet-3 batch 2 and see if there are any recent updates or NOTAMs. Also, let me check RussianSpaceWeb for any latest updates.

## 💬 Response

Let me check a few more critical sources for the very latest status:

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.spacelaunchschedule.com/launch/soyuz-2-1b-16-x-rassvet-3-2/",
  "prompt": "What is the scheduled launch date for this Rassvet-3 batch 2 mission? Is it confirmed or tentative? What is the current status?"
}
```

### 📋 Result

```
{"url": "https://www.spacelaunchschedule.com/launch/soyuz-2-1b-16-x-rassvet-3-2/", "content": "Based on the content provided, **no specific launch date is shown** for this Rassvet-3 mission. The text
indicates \"The Russian Federal Space Agency (ROSCOSMOS) Soyuz 2.1b 16 x Rassvet-3 launch is currently scheduled for: .\" (with the date field appearing empty or blank).\n\nThere is no information
about whether the date is confirmed or tentative, and no current status is provided in the content.\n\n**Relevant links:**\n- [Soyuz 2.1b Rocket
details](https://www.spacelaunchschedule.com?rocket_id=15)\n- [Space Launch Schedule main page](https://www.spacelaunchschedule.com/)\n- [Launch pad
details](https://www.spacelaunchschedule.com#launch-pad)\n- [Rocket details](https://www.spacelaunchschedule.com#rocket)\n- [Launch weather forecast](https://www.spacelaunchschedule.com#weather-
forecast)", "title": "RFSA 16 x Rassvet-3 Soyuz 2.1b Rocket Launch"}
```

```json
{
  "url": "https://nextspaceflight.com/launches",
  "prompt": "Look for any Rassvet, Bureau 1440, or Soyuz-2.1b/Plesetsk launches listed as upcoming. What are the next scheduled launches? Are there any Rassvet-3 batch 2 launches listed?"
}
```

### 📋 Result

```
{"url": "https://nextspaceflight.com/launches", "content": "Based on the provided content, **there are no Rassvet, Bureau 1440, Soyuz-2.1b/Plesetsk, or Rassvet-3 batch 2 launches listed** in the
upcoming launches.\n\nThe upcoming launches shown are:\n1. Long March 12 (Wenchang, China)\n2. Kuaizhou 11 (Jiuquan, China)\n3. Ariane 64 (French Guiana, France)\n4. Electron/Curie (New Zealand)\n5.
Spectrum (Norway)\n6. Falcon 9 Block 5 (Cape Canaveral, USA)\n7. Long March 7A (Wenchang, China)\n8. Pegasus XL (Marshall Islands)\n9. South Korean ADD Solid-Fuel SLV\n10. Falcon 9 Block 5 (Cape
Canaveral, USA)\n11. Jielong 3 (Haiyang, China)\n\n**Relevant links:**\n- [Ariane 64 launch stream](https://www.youtube.com/watch?v=oZ1pzt4VFFc)\n- [Spectrum launch
stream](https://www.youtube.com/watch?v=uUc2d_NPBN0)", "title": "Up Next"}
```

```json
{
  "query": "Soyuz Plesetsk launch today June 17 2026 OR June 18 2026"
}
```

### 📋 Result

```
{"query": "Soyuz Plesetsk launch today June 17 2026 OR June 18 2026", "results": [{"title": "Plesetsk Cosmodrome Launch Schedule", "url": "https://rocketlaunch.org/launch-schedule/plesetsk-
cosmodrome", "snippet": "Plesetsk Cosmodrome Launch Schedule\nStay updated on Plesetsk Cosmodrome's rocket launches with our real-time schedule. You can see 2 planned space missions on our website.
Watch the live stream of any Plesetsk Cosmodrome rocket launch happening today.\n[All Scheduled Launches](https://rocketlaunch.org/launch-schedule)Plesetsk Cosmodrome\nLaunch Service
Provider\nVehicle\nMission\nGlonass-K1 No. 19\nMission Type\nNavigation\nDestination\nMedium Earth Orbit\nGlonass-K are the third generation of satellite d", "api_data": null, "hint": null}, {"title":
"List of R-7 launches (2020%E2%80%932024)", "url": "https://en.wikipedia.org/wiki/List_of_R-7_launches_(2020%E2%80%932024)", "snippet": "This is a list of launches made by the R-7 Semyorka ICBM, and
its derivatives between 2020 and 2024. All launches are orbital satellite launches, unless stated otherwise.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of R-7 launches
(2020\\u20132024)\", \"url\": \"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2020%E2%80%932024)\", \"extract\": \"This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives
between 2020 and 2024. All launches are orbital satellite launches, unless stated otherwise.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "List of R-7 launches (2025%E2%80%932029)", "url":
"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)", "snippet": "This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives between 2025 and 2029. All launches
are orbital satellite launches, unless stated otherwise.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of R-7 launches (2025\\u20132029)\", \"url\":
\"https://en.wikipedia.org/wiki/List_of_R-7_launches_(2025%E2%80%932029)\", \"extract\": \"This is a list of launches made by the R-7 Semyorka ICBM, and its derivatives between 2025 and 2029. All
launches are orbital satellite launches, unless stated otherwise.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russia Launches Soyuz-2.1b Rocket from Plesetsk, Payload Reaches Orbit |
Firstpost News | N18G - YouTube", "url": "https://www.youtube.com/shorts/Jwet41bUS3Q", "snippet": "- Fran\u00e7aisFrance\n- Deutsch\n- English\n- Espa\u00f1ol\n- Italiano\n-
\u0627\u0644\u0639\u0631\u0628\u064a\u0629\n- Toutes les langues\n- Afrikaans\n- az\u0259rbaycan\n- bosanski\n- catal\u00e0\n- \u010ce\u0161tina\n- Cymraeg\n- Dansk\n- Deutsch\n- eesti\n-
EnglishUnited Kingdom\n- EnglishUnited States\n- Espa\u00f1olEspa\u00f1a\n- Espa\u00f1olLatinoam\u00e9rica\n- euskara\n- Filipino\n- Fran\u00e7aisCanada\n- Gaeilge\n- galego\n- Hrvatski\n-
Indonesia\n- isiZulu\n- \u00edslenska\n- Italiano\n- Kiswahili\n- latvie\u0161u\n- lietuvi\u0173\n- magyar\n- Melayu\n- Nederlands\n- norsk\n- o\u2018zbek\n- polski\n- Portugu\u00easBrasil\n-
Portugu\u00easPo", "api_data": null, "hint": null}, {"title": "2026 in spaceflight", "url": "https://en.wikipedia.org/wiki/2026_in_spaceflight", "snippet": "This article documents expected notable
spaceflight events during the year 2026.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"2026 in spaceflight\", \"url\": \"https://en.wikipedia.org/wiki/2026_in_spaceflight\",
\"extract\": \"This article documents expected notable spaceflight events during the year 2026.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russia Launches Soyuz-2.1b Rocket From Plesetsk,
Payload Reaches Orbit #shorts - YouTube", "url": "https://www.youtube.com/shorts/KYRKOW0IxrE", "snippet": "- Fran\u00e7aisFrance\n- Deutsch\n- English\n- Espa\u00f1ol\n- Italiano\n-
\u0627\u0644\u0639\u0631\u0628\u064a\u0629\n- Toutes les langues\n- Afrikaans\n- az\u0259rbaycan\n- bosanski\n- catal\u00e0\n- \u010ce\u0161tina\n- Cymraeg\n- Dansk\n- Deutsch\n- eesti\n-
EnglishUnited Kingdom\n- EnglishUnited States\n- Espa\u00f1olEspa\u00f1a\n- Espa\u00f1olLatinoam\u00e9rica\n- euskara\n- Filipino\n- Fran\u00e7aisCanada\n- Gaeilge\n- galego\n- Hrvatski\n-
Indonesia\n- isiZulu\n- \u00edslenska\n- Italiano\n- Kiswahili\n- latvie\u0161u\n- lietuvi\u0173\n- magyar\n- Melayu\n- Nederlands\n- norsk\n- o\u2018zbek\n- polski\n- Portugu\u00easBrasil\n-
Portugu\u00easPo", "api_data": null, "hint": null}, {"title": "Russia Space Forces Launch Military Satellites on Soyuz-2.1b from Plesetsk Cosmodrome | TheDefenseWatch.com", "url":
"https://thedefensewatch.com/global-news/russia-space-forces-launch-military-satellites-on-soyuz-2-1b-from-plesetsk/", "snippet": null, "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome
- Space Launch Schedule", "url": "https://www.spacelaunchschedule.com/category/plesetsk-cosmodrome/", "snippet": "Join our community of space enthusiasts for just $3/month and enjoy an ad-free
experience across our app and website. Your support helps us deliver the best rocket launch tracking experience in the galaxy! \ud83d\ude80\nTrack every Plesetsk Cosmodrome rocket launch with our
comprehensive schedule featuring real-time updates on today's launches and upcoming missions. Get instant access to live streams, detailed mission profiles, launch countdowns, and complete coverage of
Plesetsk Cosmodrome space operations", "api_data": null, "hint": null}, {"title": "Plesetsk Cosmodrome Overview", "url": "https://rocketlaunch.org/rocket-launch-sites/plesetsk-cosmodrome", "snippet":
"Plesetsk Cosmodrome Overview\nA complete overview of the Plesetsk Cosmodrome launch site, including key info, launch stats and the companies that launch from it.\n[Rocket Launch
Sites](https://rocketlaunch.org/rocket-launch-sites)Plesetsk Cosmodrome\n![Plesetsk Cosmodrome launch site](https://rocket-launch-today.s3.us-
east-1.amazonaws.com/plesetsk_cosmodrome_88f6d69a0b.jpg)\nBasic Info\nName\nPlesetsk Cosmodrome\nTotal Launch Count\n1685\nFirst Launch\n17 Mar 1966\nLast Launch\n23 Apr 2026\nLocation\nRussia\nP",
"api_data": null, "hint": null}, {"title": "Soyuz rocket launches a military payload", "url": "https://www.russianspaceweb.com/spacecraft-military-soyuz2-volga-2026-0417.html", "snippet": "![]()
|\n|\n|\n|\n![]()
|\n|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||\n![]() |\nSoyuz
rocket launches a military payload\nIn the early hours of April 17, 2026, a Soyuz-2-1b rocket lifted off from the Plesetsk military launch site with a classified cargo for the Ministry of
Defense.\n![launch](images/spacecraft/military/milsat_2026_0417/milsat_2026_0417_launch_1.jpg)\nS", "api_data": null, "hint": null}, {"title": "Russian Military Launch Schedule - RocketLaunch.Live",
"url": "https://www.rocketlaunch.live/?filter=russian-military", "snippet": "Premium Members can get\nemail and push notifications\nfor upcoming launches \u2014 straight to your inbox or browser, no
app required.\nThis site thrives on the contributions from space enthusiasts like you!\nOur community has made over 68 contributions in the last month.", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Now let me synthesize what I've found and assess the probability.

Key findings:
1. **RocketLaunch.Live** lists "Rassvet-3 batch 2 (16 x)" with a launch date of **June 18, 2026** from LC-43/4 Plesetsk Cosmodrome. However, the time is not specified.
2. **RocketLaunch.org** lists the mission as "TBD 2026" (updated Jun 17, 9:30am UTC).
3. **SpaceLaunchSchedule.com** shows the date field as blank/empty.
4. **NextSpaceflight.com** doesn't include any Rassvet launch in their upcoming schedule.
5. There's no official Bureau 1440 announcement about a second launch date—the June 18 date appears to come from airspace notices rather than formal confirmation.
6. The second batch was originally scheduled for April but got postponed, and observers have raised concerns about whether the aggressive timeline is realistic given production constraints.
7. The first batch itself slipped from late 2025 to March 2026 due to manufacturing delays.
8. Bureau 1440 typically keeps launch dates confidential until shortly before or after they happen—the March 23 launch went unannounced beforehand.
9. The most recent Plesetsk launch was April 23, 2026, which was a military mission, not Rassvet.

I'm now setting up an assessment framework to evaluate the likelihood of a launch within the remaining window. The question closes June 17 but resolves June 28, giving roughly 10 days for a Soyuz-2.1b carrying Rassvet-3 batch 2 to launch successfully from Plesetsk.

On the YES side, RocketLaunch.Live tentatively shows June 18 as the target date, and the question description itself references that approximate timeframe based on airspace notices. Bureau 1440 has strong motivation to stick to their ambitious deployment schedule, needing around 10 launches in 2026. The Soyuz-2.1b has proven reliability, the first batch succeeded, and three months have passed since March 23 for satellite production.

Against a launch happening, the second batch was already delayed once from its April window, and production bottlenecks had already pushed the entire deployment from late 2025 into March 2026. Most tracking sites like NextSpaceflight and SpaceLaunchSchedule don't currently show a confirmed date for this mission.

The critical issue is whether the NOTAM-based June 18 date is actually reliable. Only RocketLaunch.Live shows it, and even there the time is blank. There's no official Bureau 1440 announcement, and they typically don't announce dates publicly anyway. Independent observers have questioned whether they can really maintain that launch cadence, and the loss of one satellite from the first batch might trigger additional quality checks that could push timelines further. or June 18 based on NOTAM patterns), so there's real uncertainty about whether a launch attempt will actually happen in this window. I'm breaking this down probabilistically: the Soyuz-2.1b has about a 97% success rate if a launch attempt occurs, but the bigger question is whether an attempt will happen at all given the previous postponement and the lack of official confirmation beyond tracker reports. In the June 18-27 window, I'm working through the probability that a launch actually happens given the NOTAM signal. The April NOTAMs were filed but the launch slipped, so NOTAMs alone aren't a guarantee. Still, a NOTAM filed this close to the proposed date is a meaningful indicator—it suggests someone is confident enough to file airspace notices. I'm settling on a probability range around 40-55% for an actual launch attempt in the window, which translates to roughly 39-53% when accounting for the high success rate of reaching orbit once a launch is attempted. So my estimate lands around 45-50%. But I should double-check this against what the various launch trackers are showing. RocketLaunch.Live has pinned down June 18, 2026 as the date, which suggests they have decent confidence based on NOTAM data. However, the other major trackers—RocketLaunch.org showing only "TBD 2026" and SpaceLaunchSchedule leaving it blank—indicate there's still significant uncertainty in the broader community. If tomorrow's launch were highly probable, I'd expect better alignment across these sources.

I'm also noticing that the RocketLaunch.Live description text still references the original April 24-28 window, which suggests the June 18 update is recent and the page hasn't been fully refreshed. That's worth factoring in. And since Bureau 1440 doesn't announce launches beforehand—their March 23 mission went public only after the fact—the lack of an official announcement doesn't really tell me anything. The NOTAM is the real signal here.

Putting it together, I'd estimate around 45% probability for a launch between June 13-27, with roughly 35% confidence in the June 18 date holding (give or take a day) and another 10% accounting for potential slips that still land before June 28. If it slips again from June, we could be looking at July or beyond, especially with those production constraints. I'm settling on around 45% probability—the NOTAM evidence and the remaining window are meaningful, but the April postponement and manufacturing bottlenecks are real headwinds. Let me work through the reflection and premortem to stress-test this estimate.

## 💬 Response

Now I have a comprehensive picture. Let me synthesize the evidence and run my reflection.

**Key findings summary:**
- RocketLaunch.Live lists June 18, 2026 as the launch date for "Rassvet-3 batch 2" from Plesetsk
- Other trackers (RocketLaunch.org, SpaceLaunchSchedule, NextSpaceflight) show TBD or no date
- The date is based on NOTAMs/airspace notices, not official announcements
- The second batch was already postponed from an April 24-28 window
- Production bottlenecks caused the first batch to slip from late 2025 to March 2026
- Bureau 1440 typically doesn't announce launches in advance (March 23 was unannounced)
- Window: 10 more days remaining (June 18-27)

## 💭 Thinking

The factor sum is essentially 0 (0.01), implying ~50% probability. My tentative estimate of 45% is slightly below that, which makes sense given I weight the prior postponement and tracker disagreement somewhat more. The gap is only ~5pp which is acceptable.

Let me now run the premortem.

## 💬 Response

Good - the factor sum is essentially neutral (0.01 logit ≈ 50%), and my 45% is a slight adjustment toward NO given the delay pattern. The gap is only 5pp, which is reasonable. Let me run the premortem.
