# Reasoning Log: Will SpaceX launch Starship Flight 13 on or before June 14, 2026?

*Generated: 2026-06-05T10:39:51.281827+00:00*


## 💭 Thinking

Let me analyze this question about SpaceX launching Starship Flight 13 on or before June 14, 2026.

Key facts from the question:
1. Flight 12 launched May 22, 2026 - had engine failures, hard splashdown
2. FAA classified it as a "mishap" on May 27, 2026
3. FAA requires mishap investigation to close before return to flight
4. SpaceX has FCC STA for Flight 13 covering May 29 - Nov 29, 2026
5. Ship 40 in final integration with mid-June static fire target


6. Booster 20 is lagging behind schedule

The timeline is extremely tight—historical mishap investigations typically run about two months, but there's only roughly nine and a half days between now and the June 14 deadline. Even if the FAA investigation somehow wrapped up immediately, the hardware still isn't ready for launch, with Booster 20 trailing and Ship 40 still needing its static fire test. I should check if there's been any recent update on the investigation status that might change this assessment.

## 💬 Response

I'll start by parsing the resolution criteria, then research the current status.

**Key observations from the question:**
- Resolution window: May 31 - June 14, 2026 (~9.5 days remaining)
- FAA mishap investigation ongoing since May 27
- Historical Starship mishap investigations took ~2 months each
- Hardware not ready (Booster 20 lagging, Ship 40 needs mid-June static fire)
- Question closes TODAY (June 5)

Let me research the latest status:

## 🔧 Tool: mcp__research__research


## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "questions": [
    {
      "query": "SpaceX Starship Flight 13 launch date FAA investigation status June 2026",
      "ttl": "6h"
    },
    {
      "query": "FAA Starship mishap investigation Flight 12 timeline closure 2026",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "SpaceX Starship Flight 13 launch date FAA investigation status June 2026", "entry": {"slug": "spacex-starship-flight-13-launch-date-faa-investig-c260b6ee", "query": "SpaceX
Starship Flight 13 launch date FAA investigation status June 2026", "answer": "\n\nBased on my thorough attempts, all web search, fetch, and MCP search tools are unavailable in this environment. I
must be transparent about the limitations of what I can report. I'll provide what I know from my training data (cutoff early 2025) and clearly flag the gaps.\n\n---\n\n## SpaceX Starship Flight 13
\u2014 Research Findings\n\n### What Is Known (from training data, cutoff ~early 2025)\n\n**Starship Flight Test Program Timeline (through early 2025):**\n- **Flight 1 (IFT-1):** April 20, 2023 \u2014
vehicle exploded ~4 minutes after launch\n- **Flight 2 (IFT-2):** November 18, 2023 \u2014 stage separation achieved; both stages lost\n- **Flight 3 (IFT-3):** March 14, 2024 \u2014 reached space;
Ship lost on reentry\n- **Flight 4 (IFT-4):** June 6, 2024 \u2014 successful splashdowns of both stages\n- **Flight 5 (IFT-5):** October 13, 2024 \u2014 first booster catch with \"chopsticks\"
mechazilla arms\n- **Flight 6 (IFT-6):** November 19, 2024 \u2014 second booster catch; Ship lost during reentry\n- **Flight 7 (IFT-7):** Occurred in early 2025 \u2014 reports indicated an upper-stage
anomaly/loss, triggering an FAA post-mishap investigation\n\n**FAA Regulatory Pattern:**\n- The FAA has conducted post-mishap investigations after several Starship flights (notably Flights 1, 2, and
7)\n- Each investigation typically grounds subsequent flights until the FAA issues a closure letter or updated launch license\n- Investigation timelines have ranged from weeks to several months\n- The
FAA has faced political pressure both to expedite and to be thorough in its oversight of Starship\n\n### What Is NOT Known (beyond training data cutoff)\n\n- **Flight 13 launch date**: No information
available. Flights 8\u201312 would have occurred between early 2025 and mid-2026, but I have no data on their dates or outcomes.\n- **Flight 13 specific status**: Whether Flight 13 has been scheduled,
is awaiting regulatory clearance, or has already flown is unknown to me.\n- **Current FAA investigation status (June 2026)**: I cannot confirm whether there is an active FAA investigation related to
Flight 13 or any recent Starship flight. The FAA's investigation cadence and any regulatory holds as of June 2026 are outside my knowledge.\n- **Flight cadence in 2025\u20132026**: SpaceX had
ambitious plans to accelerate Starship launches, but actual achieved cadence is unknown.\n\n### Key Caveats\n- **All web-based research tools were unavailable** during this session (WebSearch,
WebFetch, and all MCP search/news tools were blocked).\n- The information above is from training data with a cutoff of approximately early 2025 and may be incomplete or outdated.\n- For authoritative
current data, consult: FAA.gov, SpaceX.com, or space journalism outlets (SpaceNews, Ars Technica, NASASpaceflight.com).\n\n---", "sources": [{"url":
"https://en.wikipedia.org/wiki/SpaceX_Starship_flight_test_program", "title": "SpaceX Starship flight test program - Wikipedia", "domain": "en.wikipedia.org", "accessed_at": "2026-06-05T00:00:00Z",
"snippet": "Unable to fetch; used training data knowledge of this article's content through early 2025"}, {"url": "https://www.faa.gov/space", "title": "FAA Office of Commercial Space Transportation",
"domain": "faa.gov", "accessed_at": "2026-06-05T00:00:00Z", "snippet": "Unable to fetch; FAA is the regulatory authority for Starship launch licenses and mishap investigations"}], "key_facts": ["All
web search and fetch tools were unavailable during this research session; findings are limited to training data (cutoff ~early 2025)", "Starship completed at least 7 integrated flight tests by early
2025, with Flight 5 (Oct 2024) achieving the first-ever booster catch", "Flight 7 (early 2025) experienced an upper-stage anomaly that triggered an FAA post-mishap investigation", "FAA post-mishap
investigations have historically grounded Starship flights for weeks to months", "No verified data could be obtained on Starship Flights 8\u201313, their dates, outcomes, or any FAA investigation
status as of June 2026", "SpaceX had publicly stated goals to accelerate Starship launch cadence through 2025\u20132026, but actual progress is unverified"], "data_points": [{"metric": "Starship
integrated flight tests completed (as of early 2025)", "value": 7.0, "unit": "flights", "as_of": "2025-02-01", "source_url": "https://en.wikipedia.org/wiki/SpaceX_Starship_flight_test_program"},
{"metric": "Starship Flight 5 date (first booster catch)", "value": 20241013.0, "unit": "date (YYYYMMDD)", "as_of": "2024-10-13", "source_url":
"https://en.wikipedia.org/wiki/SpaceX_Starship_flight_test_program"}, {"metric": "Starship Flight 6 date", "value": 20241119.0, "unit": "date (YYYYMMDD)", "as_of": "2024-11-19", "source_url":
"https://en.wikipedia.org/wiki/SpaceX_Starship_flight_test_program"}], "created_at": "2026-06-05T10:34:52.538397Z", "updated_at": "2026-06-05T10:34:52.538397Z", "stale_after":
"2026-06-05T16:34:52.538397Z", "state": "fresh", "revision_history": [], "session_id": "35573ea1-3a83-4950-acbc-afe2a9ba1270", "follow_up_count": 0}, "is_follow_up": false}, {"query": "FAA Starship
mishap investigation Flight 12 timeline closure 2026", "entry": {"slug": "faa-starship-mishap-investigation-flight-12-timeli-35e42569", "query": "FAA Starship mishap investigation Flight 12 timeline
closure 2026", "answer": "\n\nThe research agent returned comprehensive findings. Let me compile the full synthesis.\n\n---\n\n## FAA Starship Flight 12 Mishap Investigation \u2014 Research
Report\n\n### Overview\n\nSpaceX's Starship Flight 12 (IFT-12), launched on **May 22, 2026**, was the **first flight of the Starship Version 3 (V3)** configuration, debuting the new **Raptor 3
engines**. The flight experienced a significant anomaly with the Super Heavy booster, leading the FAA to formally classify the event as a **mishap** on **May 27, 2026** and require a formal
investigation. As of **June 5, 2026**, the investigation remains **open** with no public closure or return-to-flight determination announced.\n\n---\n\n### What Happened During Flight 12\n\n-
**Launch:** May 22, 2026, 6:30 PM Eastern, from Starbase, Boca Chica, Texas.\n- **Booster anomaly:** After stage separation (~2.5 min into flight), the Super Heavy booster's boostback burn failed
\u2014 only a handful of engines ignited, and those shut down within ~20 seconds (of a planned ~60-second burn). The booster fell uncontrolled into the Gulf of Mexico at approximately **1,500
km/h**.\n- **Additional engine issues:** One of 33 Raptor engines on Super Heavy shut down prematurely ~1 min 40 sec after liftoff; one of six Raptor engines on the Starship upper stage shut down ~30
sec after staging.\n- **Mitigating factors:** The booster impacted within the FAA-activated debris response area; no injuries or property damage. However, commercial aviation suffered departure delays
and airborne holding events.\n- **Partial mission success:** The upper stage deployed 20 Starlink mass simulators and 2 \"Dodger Dog\" test spacecraft, completed reentry, and performed a soft
splashdown in the Indian Ocean ~66.5 minutes after liftoff.\n\n---\n\n### FAA Investigation Timeline\n\n| Date | Event |\n|---|---|\n| **May 22, 2026** | Flight 12 launches; FAA begins assessing the
anomaly but does not immediately classify it as a mishap |\n| **May 27, 2026** | FAA formally determines the event constitutes a **mishap** under 14 CFR 401.7 (\"failure to complete a launch or
reentry as planned\") |\n| **May 28, 2026** | SpaceNews publishes confirmation of FAA's formal mishap determination and required investigation |\n| **June 5, 2026 (today)** | Investigation remains
**open**; no closure or return-to-flight determination has been publicly announced |\n\nThe FAA stated: *\"After a thorough assessment of the operation, the FAA has determined the May 22 SpaceX
Starship Flight 12 launch resulted in a mishap. The mishap involved the Super Heavy booster as it flew back to the Gulf of America after stage separation.\"*\n\n---\n\n### Investigation Status &
Corrective Actions\n\n- The investigation is **still open** as of today (only ~9 days since formal mishap determination).\n- **No specific corrective actions have been publicly disclosed** yet.\n- The
investigation must address: root cause of multiple Raptor 3 engine failures during boostback, premature engine shutdowns on both stages, and public safety/airspace implications.\n\n### Pathways to
Resume Flights\n\nThe FAA has two mechanisms to allow SpaceX to fly again:\n\n1. **Full investigation closure:** Root cause identified, corrective actions implemented, FAA accepts final report.\n2.
**Return-to-Flight Determination:** SpaceX can request early clearance by demonstrating preventive measures are in place and further flights pose no unacceptable risk. (This expedited pathway was used
after the Flight 8 mishap to clear Flight 9.)\n\n### Precedent Investigation Timelines\n\n| Mishap | Duration to Resolution |\n|---|---|\n| **Starship IFT-1** (April 2023) | ~5 months; 63 corrective
actions |\n| **Starship Flight 8** (March 2025) | ~2.5 months (return-to-flight determination for Flight 9) |\n| **New Glenn** (April 2025) | ~1 month |\n\n### Context\n\n- SpaceX's IPO prospectus
(filed May 20, 2026) stated the company expected to begin **orbital payload delivery missions with Starship in the second half of 2026**.\n- The relatively contained nature of the anomaly (booster
fell in designated area, no damage) could facilitate a faster resolution, but the novelty of the V3 hardware and Raptor 3 engines may complicate root-cause analysis.\n\n---\n\n### Sources\n\n-
SpaceNews: *FAA requires mishap investigation into latest Starship launch* \u2014 May 28, 2026, Jeff Foust\n- SpaceNews: *SpaceX launches first Starship V3* \u2014 May 22\u201323, 2026\n- SpaceNews:
*SpaceX sets date for first Starship version 3 launch* \u2014 May 12, 2026\n- Ars Technica: *SpaceX's Starship V3 still a work in progress, mostly successful on first flight* \u2014 May 23, 2026\n-
FAA: *Compliance, Enforcement & Mishap* \u2014 official FAA procedures page", "sources": [{"url": "https://spacenews.com/faa-requires-mishap-investigation-into-latest-starship-launch/", "title": "FAA
requires mishap investigation into latest Starship launch", "domain": "spacenews.com", "accessed_at": "2026-06-05T00:00:00Z", "snippet": "FAA formally determined May 22 Starship Flight 12 launch
resulted in a mishap involving the Super Heavy booster during boostback."}, {"url": "https://spacenews.com/spacex-launches-first-starship-v3/", "title": "SpaceX launches first Starship V3", "domain":
"spacenews.com", "accessed_at": "2026-06-05T00:00:00Z", "snippet": "Starship V3 launched May 22, 2026; booster boostback burn failed with only a few engines igniting briefly; upper stage completed
mission successfully."}, {"url": "https://spacenews.com/spacex-sets-date-for-first-starship-version-3-launch/", "title": "SpaceX sets date for first Starship version 3 launch", "domain":
"spacenews.com", "accessed_at": "2026-06-05T00:00:00Z", "snippet": "SpaceX announced the first Starship V3 launch date for May 2026."}, {"url": "https://arstechnica.com/space/2026/05/spacexs-
starship-v3-still-a-work-in-progress-mostly-successful-on-first-flight/", "title": "SpaceX's Starship V3 still a work in progress, mostly successful on first flight", "domain": "arstechnica.com",
"accessed_at": "2026-06-05T00:00:00Z", "snippet": "Analysis of Flight 12 anomalies including booster engine failures and upper stage engine shutdown."}, {"url":
"https://www.faa.gov/space/compliance_enforcement_mishap", "title": "FAA Compliance, Enforcement & Mishap", "domain": "faa.gov", "accessed_at": "2026-06-05T00:00:00Z", "snippet": "Official FAA page
describing mishap investigation procedures and return-to-flight determination process for commercial space launches."}], "key_facts": ["SpaceX Starship Flight 12 (IFT-12) launched May 22, 2026 from
Starbase, Boca Chica, TX \u2014 the first flight of the Starship V3 configuration with Raptor 3 engines.", "The Super Heavy booster's boostback burn failed: only a handful of engines ignited, shutting
down within ~20 seconds of a planned ~60-second burn, causing the booster to fall uncontrolled into the Gulf of Mexico at ~1,500 km/h.", "One of 33 Raptor engines on Super Heavy shut down prematurely
during ascent (~1 min 40 sec); one of six upper-stage Raptors shut down ~30 sec after staging.", "The booster impacted within the FAA-designated debris response area; no injuries or property damage
reported, but commercial aviation experienced delays and holding events.", "The Starship upper stage largely succeeded: deployed 20 Starlink mass simulators and 2 test spacecraft, completed reentry,
and soft-splashed in the Indian Ocean ~66.5 min after liftoff.", "The FAA formally classified the event as a mishap on May 27, 2026, under 14 CFR 401.7 ('failure to complete a launch or reentry as
planned').", "As of June 5, 2026, the FAA mishap investigation remains open \u2014 only ~9 days since the formal determination. No closure or return-to-flight determination has been announced.", "No
specific corrective actions have been publicly disclosed yet for Flight 12.", "The FAA can clear SpaceX to fly via full investigation closure OR an expedited return-to-flight determination (used
previously for Flight 9 after the Flight 8 mishap).", "Precedent investigation durations: IFT-1 ~5 months (63 corrective actions); Flight 8 ~2.5 months (return-to-flight path); New Glenn ~1 month.",
"SpaceX's IPO prospectus (filed May 20, 2026) stated the company expected to begin orbital payload delivery missions with Starship in the second half of 2026."], "data_points": [{"metric": "Starship
Flight 12 launch date", "value": 20260522.0, "unit": "YYYYMMDD", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "FAA formal mishap
determination date", "value": 20260527.0, "unit": "YYYYMMDD", "as_of": "2026-05-27", "source_url": "https://spacenews.com/faa-requires-mishap-investigation-into-latest-starship-launch/"}, {"metric":
"Booster impact speed (approximate)", "value": 1500.0, "unit": "km/h", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "Boostback burn
actual duration before shutdown", "value": 20.0, "unit": "seconds", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "Boostback burn planned
duration", "value": 60.0, "unit": "seconds", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "Days since mishap determination (as of
today)", "value": 9.0, "unit": "days", "as_of": "2026-06-05", "source_url": "https://spacenews.com/faa-requires-mishap-investigation-into-latest-starship-launch/"}, {"metric": "Starlink mass
simulators deployed", "value": 20.0, "unit": "units", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "Upper stage flight duration to
splashdown", "value": 66.5, "unit": "minutes", "as_of": "2026-05-22", "source_url": "https://spacenews.com/spacex-launches-first-starship-v3/"}, {"metric": "IFT-1 mishap investigation duration
(precedent)", "value": 5.0, "unit": "months", "as_of": "2023-09-01", "source_url": "https://www.faa.gov/space/compliance_enforcement_mishap"}, {"metric": "IFT-1 corrective actions required
(precedent)", "value": 63.0, "unit": "corrective actions", "as_of": "2023-09-01", "source_url": "https://www.faa.gov/space/compliance_enforcement_mishap"}, {"metric": "Flight 8 mishap to return-to-
flight duration (precedent)", "value": 2.5, "unit": "months", "as_of": "2025-05-22", "source_url": "https://www.faa.gov/space/compliance_enforcement_mishap"}, {"metric": "New Glenn mishap
investigation duration (precedent)", "value": 1.0, "unit": "months", "as_of": "2025-05-22", "source_url": "https://www.faa.gov/space/compliance_enforcement_mishap"}], "created_at":
"2026-06-05T10:38:27.923611Z", "updated_at": "2026-06-05T10:38:27.923611Z", "stale_after": "2026-06-05T16:38:27.923611Z", "state": "fresh", "revision_history": [], "session_id":
"0ab68723-5db8-4fb8-983c-7563735b418e", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

```json
{
  "post_id_list": [
    43782
  ]
}
```

### 📋 Result

```
{"post_id": 43782, "title": "Will SpaceX launch Starship Flight 13 on or before June 14, 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/43782", "background_info": "SpaceX's
Starship Flight 12 launched on May 22, 2026 from Starbase, Texas \u2014 the debut flight of the Starship V3 (Block 3) vehicle. During ascent, one of the Super Heavy booster's 33 Raptor engines shut
down, and after stage separation additional booster engines failed during the boostback burn, leading to a hard splashdown in the Gulf of Mexico. The Starship upper stage also experienced an engine-
out. There were no public injuries or property damage.\n\nOn May 27, 2026, the FAA formally classified Flight 12 as a 'mishap' under 14 CFR Part 450 and required SpaceX to conduct an FAA-overseen
mishap investigation. The FAA has explicitly stated that Starship-Super Heavy cannot return to flight until the investigation is closed and any corrective actions are approved. As a result, Starship
is currently grounded.\n\nSpaceX holds an FCC Special Temporary Authority for Flight 13 covering May 29 \u2013 November 29, 2026. Ship 40 is reportedly in final integration with a mid-June static fire
target, while Booster 20 is lagging. Launch-tracking sites list Flight 13 as 'NET June 2026' or later, with the specific date TBD. Historical Starship mishap investigations have ranged from a few
weeks to several months (e.g., Flight 7/8 V2 investigations took ~2 months each). Past Falcon 9 mishap investigations have occasionally closed in days, but no Starship investigation has closed that
quickly.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 4, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This question resolves YES if
SpaceX initiates a launch attempt of Starship Flight 13 (Integrated Flight Test 13, the next full-stack Starship/Super Heavy launch from Starbase after Flight 12 of May 22, 2026) in which the vehicle
lifts off the pad (clears the launch mount under its own power) at any time from 00:00 UTC on May 31, 2026 through 23:59 UTC on June 14, 2026. The launch attempt counts whether or not the mission
succeeds. Resolution will be based on the Wikipedia 'List of Starship launches' page (https://en.wikipedia.org/wiki/List_of_Starship_launches), which records each flight's launch date and outcome. If
Wikipedia has not been updated, resolution may instead use [credible sources](https://www.metaculus.com/faq/#definitions) reporting the liftoff. The question resolves NO if no Starship Flight 13
liftoff occurs in that window (e.g., the vehicle remains grounded by the FAA mishap investigation, hardware is not ready, or only static fires / wet dress rehearsals occur without a launch attempt).",
"fine_print": "A 'liftoff' means the integrated Starship/Super Heavy vehicle physically leaves the launch mount under thrust. Aborts before engine ignition, static fires, and wet dress rehearsals do
not count. A liftoff followed by an immediate explosion still counts as a launch for resolution purposes. If SpaceX flies a Starship mission from Starbase that it does not officially label 'Flight 13'
but is unambiguously the next integrated flight test after Flight 12, that flight counts.", "num_forecasters": 0, "community_prediction": null}
```

## 💬 Response

Excellent. The research provides clear data. Let me now do a quick search for any very recent developments:

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "SpaceX Starship Flight 13 FAA investigation update June 2026"
}
```

### 📋 Result

```
{"query": "SpaceX Starship Flight 13 FAA investigation update June 2026", "results": [{"title": "SpaceX Starship Grounded After Flight 12 Booster Failure: FAA Investigation Threatens IPO Timeline",
"url": "https://www.techtimes.com/articles/317326/20260528/spacex-starship-grounded-after-flight-12-booster-failure-faa-investigation-threatens-ipo-timeline.htm", "snippet": "![SpaceX
Engine](https://d.techtimes.com/en/full/465560/spacex-engine.jpg?w=836&f=9ccf0e52d48bd0d706a86472148a54e4)\nSpaceX's newest and most powerful rocket is grounded \u2014 five days after its debut \u2014
after the Federal Aviation Administration formally declared the May 22 Starship Flight 12 launch a mishap and ordered a full investigation before Flight 13 can proceed. The booster's Raptor 3 engines
failed to reignite properly after stage separation, sending Super Heavy Booster 19 to a hard splashdo", "api_data": null, "hint": null}, {"title": "FAA grounds SpaceX Starship after V3 debut", "url":
"https://www.astronomy.com/space-exploration/faa-grounds-spacex-starship-after-v3-debut/", "snippet": "![SpaceX's Starship rocket stands fully stacked on its launch mount at Boca Chica, Texas, with
the towering mechazilla catch arm structure rising alongside it on the left. Thick white clouds of venting propellant or water vapor billow around the base and drift to the left, while a blue sky with
scattered white clouds fills the background. A second launch structure is visible in the far left of the frame.](https://www.astronomy.com/wp-
content/uploads/2026/05/Flight_12_Website_Desktop_1_2d4e5ab784", "api_data": null, "hint": null}, {"title": "FAA requires SpaceX-led mishap investigation before resumption of Starship launches \u2013
Spaceflight Now", "url": "https://spaceflightnow.com/2026/05/27/faa-requires-spacex-led-mishap-investigation-before-resumption-of-starship-launches/", "snippet": "![](http://spaceflightnow.com/wp-
content/uploads/2026/05/20260527_Starship_Flight-12_liftoff.jpeg)\nFAA requires SpaceX-led mishap investigation before resumption of Starship launches\nThe Federal Aviation Administration made the
determination after analyzing the results of Starship Flight 12, which took place on Friday, May 22.\nThe Federal Aviation Administration said that SpaceX needs to complete a mishap investigation into
the 12th flight of its Starship-Super Heavy rocket before it can launch ", "api_data": null, "hint": null}, {"title": "FAA requires mishap investigation into latest Starship launch - SpaceNews",
"url": "https://spacenews.com/faa-requires-mishap-investigation-into-latest-starship-launch/", "snippet": "AMSTERDAM \u2014 The Federal Aviation Administration will require SpaceX to complete an
investigation into its latest Starship test flight before allowing the vehicle to fly again.\nIn a May 27 statement, the FAA said it determined that [the Flight 12 launch of Starship on May
22](https://spacenews.com/spacex-launches-first-starship-v3/) from the company\u2019s Starbase, Texas, facilities resulted in a mishap. The FAA defines a mishap as [meeting one of several
criteria](https://www.faa.gov/space/complianc", "api_data": null, "hint": null}, {"title": "SpaceX - Updates", "url": "https://www.spacex.com/updates", "snippet": "Updates\nChun Wang, Mission
Commander of Fram2, the first human spaceflight mission to fly over Earth\u2019s poles, announced today he will fly aboard Starship\u2019s first human spaceflight interplanetary missions to Mars! The
two-year mission will explore outside the Earth-Moon system before flying-by the Red Planet and returning to Earth.\nPrior to this interplanetary mission, Chun will join Dennis and Akiko Tito on the
first planned Starship commercial human spaceflight around the Moon. The week-long ci", "api_data": null, "hint": null}, {"title": "FAA Halts Starship After Mishap Investigation Order | KeepTrack X
Report - KeepTrack", "url": "https://keeptrack.space/x-report/spacex-brief-2026-05-29", "snippet": "\u00b7 [x report](/category/x-report) \u00b7 6 min read\nFAA Halts Starship After Mishap
Investigation Order | KeepTrack X Report\nThe FAA has mandated a mishap investigation into Starship's latest flight, grounding the vehicle while SpaceX's V3 variant eyes its next steps.\n![The FAA has
mandated a mishap investigation into Starship's latest flight, grounding the vehicle while SpaceX's V3 variant eyes its next steps.](/_astro/26.BqhjC6Ac.jpg)\nLatest Developments\nThe FAA has ordered
SpaceX to conduct a forma", "api_data": null, "hint": null}, {"title": "SpaceX conducting third mishap investigation since January 2025 | MyRGV.com", "url": "https://myrgv.com/local-
news/2026/06/02/spacex-conducting-third-mishap-investigation-since-january-2025/", "snippet": null, "api_data": null, "hint": null}, {"title": "FAA Closes SpaceX Starship Mishap Investigation |
Federal Aviation Administration", "url": "https://www.faa.gov/newsroom/faa-closes-spacex-starship-mishap-investigation", "snippet": "FAA Closes SpaceX Starship Mishap Investigation\nThe FAA has
[closed the SpaceX Starship Super Heavy mishap investigation](https://www.faa.gov/media/70901). The final report cites multiple root causes of the April 20, 2023, mishap and 63 corrective actions
SpaceX must take to prevent mishap reoccurrence. Corrective actions include redesigns of vehicle hardware to prevent leaks and fires, redesign of the launch pad to increase its robustness,
incorporation of additional reviews in the design proce", "api_data": null, "hint": null}]}
```

```json
{
  "query": "SpaceX Starship grounded FAA return to flight June 2026"
}
```

### 📋 Result

```
{"query": "SpaceX Starship grounded FAA return to flight June 2026", "results": [{"title": "FAA grounds SpaceX Starship after V3 debut", "url": "https://www.astronomy.com/space-exploration/faa-
grounds-spacex-starship-after-v3-debut/", "snippet": "![SpaceX's Starship rocket stands fully stacked on its launch mount at Boca Chica, Texas, with the towering mechazilla catch arm structure rising
alongside it on the left. Thick white clouds of venting propellant or water vapor billow around the base and drift to the left, while a blue sky with scattered white clouds fills the background. A
second launch structure is visible in the far left of the frame.](https://www.astronomy.com/wp-content/uploads/2026/05/Flight_12_Website_Desktop_1_2d4e5ab784", "api_data": null, "hint": null},
{"title": "SpaceX Starship Grounded After Flight 12 Booster Failure: FAA Investigation Threatens IPO Timeline", "url": "https://www.techtimes.com/articles/317326/20260528/spacex-starship-grounded-
after-flight-12-booster-failure-faa-investigation-threatens-ipo-timeline.htm", "snippet": "![SpaceX Engine](https://d.techtimes.com/en/full/465560/spacex-
engine.jpg?w=836&f=9ccf0e52d48bd0d706a86472148a54e4)\nSpaceX's newest and most powerful rocket is grounded \u2014 five days after its debut \u2014 after the Federal Aviation Administration formally
declared the May 22 Starship Flight 12 launch a mishap and ordered a full investigation before Flight 13 can proceed. The booster's Raptor 3 engines failed to reignite properly after stage separation,
sending Super Heavy Booster 19 to a hard splashdo", "api_data": null, "hint": null}, {"title": "FAA grounds SpaceX's Starship megarocket after Flight 12 'mishap' | Space", "url":
"https://www.space.com/space-exploration/launches-spacecraft/faa-grounds-spacexs-starship-v3-megarocket-after-flight-12-mishap", "snippet": "FAA grounds SpaceX's Starship V3 megarocket after Flight 12
'mishap'\n![a large silver rocket launches above a plume of fire](https://cdn.mos.cms.futurecdn.net/WD2Rmreoor9FWTASiZPhy5.jpg)\n[Follow us](https://google.com/preferences/source?q=space.com)\nJust
five days after its debut flight, SpaceX's Starship V3 megarocket has been grounded.\nThe U.S. Federal Aviation Administration (FAA) just declared the [May 22 Starship V3
launch](https://www.space.com/space-exploration/launches-spacecraft/spacex-", "api_data": null, "hint": null}, {"title": "FAA Grounds SpaceX Starship After V3 Debut", "url":
"https://www.flyingmag.com/faa-grounds-spacex-starship-super-heavy-v3/", "snippet": "After completing what it said was a \u201cthorough assessment,\u201d the FAA on Wednesday ordered SpaceX to
investigate anomalies that its Super Heavy booster experienced during the [12th test flight](https://www.flyingmag.com/what-starship-flight-12-means-spacex-ipo/) of its behemoth Starship rocket.\nThe
aviation regulator on Tuesday was ambiguous about whether an investigation would be required into Starship Flight 12, which launched Friday evening from SpaceX\u2019s Starbase facility in Texas. Now,
it is gr", "api_data": null, "hint": null}, {"title": "SpaceX Starship Rocket Grounded by FAA After Launch Mishap", "url": "https://www.bloomberg.com/news/articles/2026-05-27/spacex-starship-rocket-
grounded-by-faa-after-launch-mishap", "snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

The research confirms the situation clearly. No evidence of any investigation closure or return-to-flight. Let me now run my analysis.

## 💬 Response

The factors imply an even lower probability than my tentative 2%. Let me run the premortem:
