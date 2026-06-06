# Reasoning Log: How many Falcon 9 and Falcon Heavy launches will SpaceX conduct between May 28, 2026 and June 14, 2026?

*Generated: 2026-06-06T02:36:34.852758+00:00*


## 💭 Thinking

Let me analyze this forecasting question about SpaceX Falcon 9 and Falcon Heavy launches between May 28 and June 14, 2026.

Key details:
- Window: May 28, 2026 (00:00 UTC) through June 14, 2026 (00:00 UTC) - that's 17 days (May 28-June 13 inclusive)
- Wait, let me recount: May 28 to June 13 inclusive. May has 31 days, so May 28, 29, 30, 31 = 4 days in May, plus June 1-13 = 13 days in June = 17 days total.
- The description mentions an 18-day window, but when I count the actual dates from May 28 through June 13 inclusive, I get 17 days. The resolution criteria specifies "on or after 00:00 UTC on May 28, 2026 and before 00:00 UTC on June 14, 2026," which confirms the 17-day period.

Since today is June 6, 2026 and the question closes at 05:11 UTC today, the window is partially elapsed—9 days have already passed (May 28 through June 5) and 8 days remain (June 6 through June 13). I need to find out how many launches have already occurred during the first part of the window and then estimate how many more will happen in the remaining days.

## 💬 Response

I'll start by understanding the question and researching recent SpaceX launch data.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    43786
  ]
}
```

### 📋 Result

```
{"post_id": 43786, "title": "How many Falcon 9 and Falcon Heavy launches will SpaceX conduct between May 28, 2026 and June 14, 2026?", "type": "discrete", "url":
"https://www.metaculus.com/questions/43786", "background_info": "SpaceX operates the Falcon 9 and Falcon Heavy launch vehicles, with Falcon 9 being its workhorse rocket flying multiple Starlink,
government, and commercial missions per week. In 2025 SpaceX conducted a record number of Falcon launches, and the 2026 cadence has continued at a similar pace. As of May 30, 2026, the Falcon 9 family
had logged 656 launches total, with roughly 60 Falcon 9 launches in 2026 year-to-date. Starship remains separate (and is not counted in this question). Recent May 2026 activity shows roughly 9-10
Falcon 9 launches in the month, with confirmed launches on May 29 (Starlink Group 10-53) and May 30 (Starlink Group 17-41). The 18-day window covered by this question (May 28 through June 13, 2026
inclusive) historically corresponds to about 5-7 Falcon launches at current cadence.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 4, \"resolvability\": 4,
\"passes\": true}}}`", "resolution_criteria": "This question resolves as the number of orbital launches of the Falcon 9 or Falcon Heavy rocket conducted by SpaceX with liftoff occurring on or after
00:00 UTC on May 28, 2026 and before 00:00 UTC on June 14, 2026, as listed in the Wikipedia article 'List of Falcon 9 and Falcon Heavy launches'
(https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches). A launch counts if the vehicle lifts off from the pad during the window, regardless of whether the mission ultimately
succeeds or fails (i.e., partial failures and in-flight failures still count as launches). A pad abort or scrubbed attempt where the vehicle does not lift off does NOT count. For example, if 7 Falcon
9 launches occur in this window, the answer is '7'. If the Wikipedia page is unavailable or has not been updated, the resolver may use SpaceX's official launches page (https://www.spacex.com/launches)
or [credible sources](https://www.metaculus.com/faq/#definitions) to count the launches.", "fine_print": "Only Falcon 9 and Falcon Heavy launches are counted; Starship launches are excluded. Static
fire tests and wet dress rehearsals do not count. Liftoff time is determined in UTC.", "num_forecasters": 9, "community_prediction": null, "lower_bound": -0.5, "upper_bound": 15.5}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "SpaceX Falcon 9 launches May 28 to June 6 2026, how many launches occurred in this period?",
      "ttl": "6h"
    },
    {
      "query": "SpaceX Falcon 9 launch schedule June 2026, upcoming launches",
      "ttl": "6h"
    },
    {
      "query": "SpaceX Falcon 9 2026 launch cadence rate per week",
      "ttl": "6h"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "SpaceX Falcon 9 launches May 28 to June 6 2026, how many launches occurred in this period?", "entry": {"slug": "spacex-falcon-9-launches-may-28-to-june-6-2026-how-99a1969b",
"query": "SpaceX Falcon 9 launches May 28 to June 6 2026, how many launches occurred in this period?", "answer": "**Summary**: I was unable to retrieve the exact count of SpaceX Falcon 9 launches
between May 28 and June 6, 2026, because all web search and fetch tools were unavailable during this session. Based on SpaceX's historical launch cadence (~2.5\u20133 launches per week in recent
years), a rough estimate would be **4\u20135 launches** in this 10-day window, but this is unverified. I recommend consulting Wikipedia's Falcon 9 launch list or NextSpaceflight.com for the confirmed
count.", "sources": [], "key_facts": ["All web search and fetch tools were unavailable; exact launch count for May 28\u2013June 6, 2026 could not be verified.", "SpaceX's historical Falcon 9 cadence
in 2025 was approximately 130+ launches per year (~2.5/week).", "SpaceX has been increasing launch cadence year-over-year, with 2026 potentially targeting 150+ Falcon 9 launches.", "Based on
historical cadence, approximately 4\u20135 Falcon 9 launches would be expected in a typical 10-day window in mid-2026, but this is an estimate, not a confirmed count.", "Authoritative sources for
verification include Wikipedia's Falcon 9 launch list, NextSpaceflight.com, and SpaceX.com."], "data_points": [{"metric": "Approximate Falcon 9 launches per year (2025 actual)", "value": 130.0,
"unit": "launches", "as_of": "2025-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2025)"}, {"metric": "Estimated average Falcon 9 launches per week
(2025)", "value": 2.5, "unit": "launches/week", "as_of": "2025-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2025)"}, {"metric": "Estimated Falcon 9
launches in 10-day window at 2026 cadence (unverified estimate)", "value": 4.5, "unit": "launches", "as_of": "2026-06-06", "source_url": "N/A - estimate based on historical cadence"}], "created_at":
"2026-06-06T02:29:30.041845Z", "updated_at": "2026-06-06T02:29:30.041845Z", "stale_after": "2026-06-06T08:29:30.041845Z", "state": "fresh", "revision_history": [], "session_id":
"da9bf99a-f979-4f23-bdfb-c7f5f1eea2fb", "follow_up_count": 0}, "is_follow_up": false}, {"query": "SpaceX Falcon 9 launch schedule June 2026, upcoming launches", "entry": {"slug": "spacex-
falcon-9-launch-schedule-june-2026-upcoming-48e1552b", "query": "SpaceX Falcon 9 launch schedule June 2026, upcoming launches", "answer": "I now have comprehensive data. Here is my full
synthesis:\n\n---\n\n# SpaceX Falcon 9 Launch Schedule \u2014 June 2026 & Upcoming\n\n## Overview\n\nAs of June 6, 2026, SpaceX has already completed **65 Falcon 9/Falcon Heavy launches** in 2026
(January 1 \u2013 June 6), maintaining a remarkable cadence of approximately **one launch every 2.4 days** (~12.7 launches/month). There are **15 Falcon launches listed for June 2026** and **117
additional Falcon missions** manifested from July 2026 onward.\n\n## Recent Completed Launches (Late May \u2013 Early June 2026)\n\n| Date | Mission | Pad | Status
|\n|------|---------|-----|--------|\n| Jun 4, 2026 | Starlink Group 10-43 | SLC-40, Cape Canaveral | \u2705 Success |\n| Jun 3, 2026 | Starlink Group 17-47 | SLC-4E, Vandenberg | \u2705 Success |\n|
May 30, 2026 | Starlink Group 17-41 | SLC-4E, Vandenberg | \u2705 Success |\n| May 29, 2026 | Starlink Group 10-53 | SLC-40, Cape Canaveral | \u2705 Success |\n| May 26, 2026 | Starlink Group 17-37 |
SLC-4E, Vandenberg | \u2705 Success |\n| May 25, 2026 | Starlink Group 10-47 | SLC-40, Cape Canaveral | \u2705 Success |\n| May 21, 2026 | Starlink Group 10-31 | SLC-40, Cape Canaveral | \u2705
Success |\n| May 20, 2026 | Starlink Group 17-42 | SLC-4E, Vandenberg | \u2705 Success |\n| May 15, 2026 | Dragon CRS-2 SpX-34 | SLC-40, Cape Canaveral | \u2705 Success |\n| May 12, 2026 | NROL-172 |
SLC-4E, Vandenberg | \u2705 Success |\n\n## Upcoming June 2026 Launches \u2014 Confirmed Dates (\"Go for Launch\")\n\n| Date (UTC) | Mission | Satellites | Pad | Orbit
|\n|------------|---------|------------|-----|-------|\n| Jun 7, 02:00 | **Starlink Group 17-43** | 21 Starlink + 2 Starshield | SLC-4E, Vandenberg | LEO |\n| Jun 8, 10:07 | **Starlink Group 10-35** |
29 Starlink | SLC-40, Cape Canaveral | LEO |\n| Jun 10, 14:00 | **Starlink Group 17-44** | 24 Starlink | SLC-4E, Vandenberg | LEO |\n| Jun 12, 12:27 | **Starlink Group 10-54** | 29 Starlink | SLC-40,
Cape Canaveral | LEO |\n| Jun 14, 14:00 | **Starlink Group 17-54** | 24 Starlink | SLC-4E, Vandenberg | LEO |\n\n## June 2026 \u2014 \"To Be Determined\" (date TBD, listed as June 30 placeholder)\n\n|
Mission | Customer | Pad | Orbit |\n|---------|----------|-----|-------|\n| **BlueBird Block 2 #3-5** | AST SpaceMobile | SLC-40, Cape Canaveral | LEO |\n| **Globalstar 2-R Mission 1 (x9)** |
Globalstar | SLC-40, Cape Canaveral | LEO |\n| **SDA Tranche 1 Tracking Layer A** | US Space Force/SDA | SLC-4E, Vandenberg | Polar |\n| **SDA Tranche 1 Tracking Layer C** | US Space Force/SDA |
SLC-4E, Vandenberg | Polar |\n| **SDA Tranche 1 Tracking Layer E** | US Space Force/SDA | SLC-4E, Vandenberg | Polar |\n| **SDA Tranche 1 Transport Layer A** | US Space Force/SDA | SLC-4E, Vandenberg
| Polar |\n| **SDA Tranche 1 Transport Layer D** | US Space Force/SDA | SLC-4E, Vandenberg | Polar |\n| **SDA Tranche 1 Transport Layer E** | US Space Force/SDA | SLC-4E, Vandenberg | Polar |\n| **SDA
Tranche 1 Transport Layer F** | US Space Force/SDA | SLC-4E, Vandenberg | Polar |\n| **Sirius SXM-11** | SiriusXM | SLC-40, Cape Canaveral | GTO |\n\n> **Note:** Many of the TBD missions (especially
the seven SDA missions) may slip into later months. The June 30 date is a placeholder indicating \"sometime in June or later.\"\n\n## Key Upcoming Missions Beyond June 2026\n\n| Target Date | Mission
| Vehicle | Details |\n|-------------|---------|---------|---------|\n| Jul 2026 | **BlueBird Block 2 #6-8** | Falcon 9 | AST SpaceMobile (LEO) |\n| Jul 2026 | **Transporter 17** | Falcon 9 |
Rideshare to SSO |\n| Aug 2026 | **Nancy Grace Roman Space Telescope** | **Falcon Heavy** | NASA flagship telescope to Sun-Earth L2 |\n| Aug 2026 | **Dragon CRS-2 SpX-35** | Falcon 9 | ISS resupply
|\n| Sep 2026 | **Crew-13** | Falcon 9 | ISS crew rotation |\n| Sep 2026 | **O3b mPower 11-13** | Falcon 9 | SES satellites (MEO) |\n| Nov 2026 | **Griffin Mission One** | **Falcon Heavy** |
Astrobotic lunar lander |\n| Dec 2026 | **Blue Ghost Lunar Lander Mission 2** | Falcon 9 | Firefly lunar mission |\n| Dec 2026 | **Nova-C IM-3** | Falcon 9 | Intuitive Machines lunar mission |\n| Dec
2026 | **Telesat Lightspeed 1** | Falcon 9 | LEO broadband constellation |\n\n## Launch Cadence & Statistics\n\n- **65 Falcon launches completed** in 2026 through June 6 (156 days)\n- **Average
cadence: 1 launch every 2.4 days** (~12.7/month)\n- **Two active pads** for Falcon 9: SLC-40 (Cape Canaveral) and SLC-4E (Vandenberg), with LC-39A used for Falcon Heavy\n- **Alternating pattern**:
SpaceX is alternating between East Coast (Group 10-xx) and West Coast (Group 17-xx) Starlink launches roughly every 2-3 days\n- **117 additional Falcon missions** manifested from July 2026 onward
(many with placeholder dates)\n- Dominant payload: Starlink constellation deployment continues to drive the majority of launches\n\n## Data Sources\n\nAll data retrieved from **The Space Devs Launch
Library 2 API** (`ll.thespacedevs.com/2.2.0/`) and cross-validated with **RocketLaunch.Live API** (`fdo.rocketlaunch.live`), accessed June 6, 2026.\n\n---", "sources": [{"url":
"https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon", "title": "The Space Devs Launch Library 2 API - Upcoming Falcon Launches", "domain": "ll.thespacedevs.com", "accessed_at":
"2026-06-06T00:00:00Z", "snippet": "API providing upcoming launch data including dates, pads, missions, and status for all Falcon 9 and Falcon Heavy launches."}, {"url":
"https://ll.thespacedevs.com/2.2.0/launch/previous/?search=falcon", "title": "The Space Devs Launch Library 2 API - Previous Falcon Launches", "domain": "ll.thespacedevs.com", "accessed_at":
"2026-06-06T00:00:00Z", "snippet": "API providing historical launch data for completed Falcon 9 missions."}, {"url": "https://fdo.rocketlaunch.live/json/launches/next/10", "title": "RocketLaunch.Live
API - Next 10 Launches", "domain": "fdo.rocketlaunch.live", "accessed_at": "2026-06-06T00:00:00Z", "snippet": "Cross-validation source confirming upcoming Falcon 9 launch dates and details."}],
"key_facts": ["SpaceX has completed 65 Falcon 9/Heavy launches in 2026 (Jan 1 \u2013 Jun 6), averaging one launch every 2.4 days (~12.7 per month).", "Five Falcon 9 launches are confirmed 'Go for
Launch' in the next week: Starlink 17-43 (Jun 7), Starlink 10-35 (Jun 8), Starlink 17-44 (Jun 10), Starlink 10-54 (Jun 12), and Starlink 17-54 (Jun 14).", "15 total Falcon launches are listed for June
2026, including 5 with firm dates and 10 with TBD/placeholder dates (Jun 30).", "TBD June missions include: BlueBird Block 2 #3-5 (AST SpaceMobile), Globalstar 2-R Mission 1, seven SDA Tranche 1
missions, and Sirius SXM-11.", "Starlink Group 17-43 (Jun 7) will carry 21 Starlink satellites plus 2 US military Starshield satellites.", "SpaceX alternates launches between SLC-40 (Cape Canaveral,
FL) and SLC-4E (Vandenberg, CA) every 2-3 days.", "117 additional Falcon missions are manifested from July 2026 onward.", "Key upcoming high-profile missions: Nancy Grace Roman Space Telescope (Falcon
Heavy, Aug 2026), Crew-13 (Sep 2026), Griffin Mission One lunar lander (Falcon Heavy, Nov 2026).", "Most recent completed launches: Starlink 10-43 (Jun 4) and Starlink 17-47 (Jun 3), both
successful.", "Dragon CRS-2 SpX-34 ISS resupply mission launched successfully on May 15, 2026."], "data_points": [{"metric": "Falcon 9/Heavy launches completed in 2026 (Jan 1 \u2013 Jun 6)", "value":
65.0, "unit": "launches", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/?search=falcon&net__gte=2026-01-01&net__lte=2026-06-06"}, {"metric": "Average launch cadence
(days between launches)", "value": 2.4, "unit": "days per launch", "as_of": "2026-06-06", "source_url":
"https://ll.thespacedevs.com/2.2.0/launch/?search=falcon&net__gte=2026-01-01&net__lte=2026-06-06"}, {"metric": "Approximate monthly Falcon launch rate", "value": 12.7, "unit": "launches per month",
"as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/?search=falcon&net__gte=2026-01-01&net__lte=2026-06-06"}, {"metric": "Falcon launches listed for June 2026", "value":
15.0, "unit": "launches", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon&net__gte=2026-06-01&net__lte=2026-06-30"}, {"metric": "Falcon launches
with confirmed Go for Launch status in June 2026", "value": 5.0, "unit": "launches", "as_of": "2026-06-06", "source_url":
"https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon&net__gte=2026-06-01&net__lte=2026-06-30"}, {"metric": "Falcon missions manifested from July 2026 onward", "value": 117.0, "unit":
"launches", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon&net__gte=2026-07-01"}, {"metric": "Starlink satellites on Starlink Group 17-43 (Jun
7)", "value": 21.0, "unit": "satellites", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon"}, {"metric": "Starshield satellites on Starlink Group
17-43 (Jun 7)", "value": 2.0, "unit": "satellites", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon"}, {"metric": "Starlink satellites on
Starlink Group 10-35 (Jun 8)", "value": 29.0, "unit": "satellites", "as_of": "2026-06-06", "source_url": "https://ll.thespacedevs.com/2.2.0/launch/upcoming/?search=falcon"}], "created_at":
"2026-06-06T02:31:45.558900Z", "updated_at": "2026-06-06T02:31:45.558900Z", "stale_after": "2026-06-06T08:31:45.558900Z", "state": "fresh", "revision_history": [], "session_id":
"82f0c103-7b2a-41b4-b05f-aa607b59a01c", "follow_up_count": 0}, "is_follow_up": false}, {"query": "SpaceX Falcon 9 2026 launch cadence rate per week", "entry": {"slug": "spacex-falcon-9-2026-launch-
cadence-rate-per-week-45ac678f", "query": "SpaceX Falcon 9 2026 launch cadence rate per week", "answer": "Now I have comprehensive data. Let me compile the full research report.\n\n---\n\n# SpaceX
Falcon 9 2026 Launch Cadence \u2014 Research Report\n\n## Key Finding: ~3.0 launches per week in 2026\n\n### Current 2026 Status (as of June 4, 2026)\n\nAs of June 4, 2026, SpaceX has conducted **66
Falcon family vehicle launches** (65 Falcon 9 and 1 Falcon Heavy), according to Wikipedia's continuously-updated launch list. This translates to:\n\n- **Weekly cadence: ~2.98 launches/week** (~3.0
rounded)\n- **Average days between launches: 2.3 days**\n- **Monthly average: 13.0 launches/month**\n- **Daily rate: 0.43 launches/day**\n\nThe all-time Falcon 9/Heavy family total stands at **656
launches** as of May 30, 2026 (653 full mission successes).\n\n### 2026 Monthly Breakdown\n\n| Month | Launches |\n|-------|----------|\n| January | 13 |\n| February | 12 |\n| March | 13 |\n| April |
11 |\n| May | 11 |\n| June (through 4th) | 2 |\n\nThree dates saw **two launches in a single day**: March 17, March 30, and April 11.\n\nPeak weekly activity reached **4 launches in a single ISO
week**, occurring in ISO weeks 3, 8, 9, 12, 18, and 22.\n\n### Company Guidance for 2026\n\nSpaceX President **Gwynne Shotwell** stated in *Time* magazine that the company expects **\"maybe 140,
145-ish\"** Falcon 9 launches in 2026. This is notably lower than the 2025 total of 165, possibly reflecting some missions shifting to Starship or other factors.\n\n### Year-over-Year Comparison\n\n|
Year | Total Falcon Launches | Weekly Rate | Monthly Rate |\n|------|----------------------|-------------|--------------|\n| 2022 | 61 | 1.17/week | 5.1/month |\n| 2023 | 96 | 1.85/week | 8.0/month
|\n| 2024 | 134 (132 F9 + 2 FH) | 2.58/week | 11.2/month |\n| 2025 | 165 (all F9) | 3.17/week | 13.8/month |\n| 2026 YTD (annualized) | ~155 projected | 2.98/week | 13.0/month |\n\n### Trajectory
Analysis\n\n- The 2026 YTD pace (~2.98/week) is **below** the 2025 full-year pace of 3.17/week\n- The 2026 pace is **above** the 2024 full-year pace of 2.58/week\n- At the current pace, SpaceX is
projected to reach **~155 launches** for the full year, which is **above** Shotwell's 140-145 target\n- To meet the lower end of Shotwell's target (140), SpaceX would need only ~2.60/week for the
remainder of the year\n- In 2025, the company initially targeted 175-180 launches but revised down to 165\n\n### Booster Reusability Records (as of mid-2026)\n\n- Total booster landings: **616
successful out of 629 attempts** (97.93%)\n- Falcon 9 Block 5 landing success rate: **591/597** (98.99%)\n- Record booster re-flights: **34 missions** by booster B1067\n- Most reflown fairing half:
SN185 at **36 flights**\n\n### Sources\n\nAll data extracted from:\n1. **Wikipedia \u2014 List of Falcon 9 and Falcon Heavy launches** (en.wikipedia.org, accessed June 6, 2026) \u2014 last updated May
30\u2013June 4, 2026\n2. **Wikipedia \u2014 2026 in spaceflight** (en.wikipedia.org, accessed June 6, 2026)", "sources": [{"url":
"https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches", "title": "List of Falcon 9 and Falcon Heavy launches - Wikipedia", "domain": "en.wikipedia.org", "accessed_at":
"2026-06-06T02:30:00Z", "snippet": "As of June 4, SpaceX has conducted 66 Falcon family vehicle launches (65 Falcon 9 and 1 Falcon Heavy) in 2026. SpaceX President Gwynne Shotwell stated in Time
magazine they are expecting 'maybe 140, 145-ish' Falcon 9 launches in 2026."}, {"url": "https://en.wikipedia.org/wiki/2026_in_spaceflight", "title": "2026 in spaceflight - Wikipedia", "domain":
"en.wikipedia.org", "accessed_at": "2026-06-06T02:30:00Z", "snippet": "Falcon 9 new: 2 launches, Falcon 9 reused: 62 launches, Falcon Heavy: 1 launches (bar chart data for 2026 as of late May)"}],
"key_facts": ["As of June 4, 2026, SpaceX has conducted 66 Falcon family launches (65 Falcon 9, 1 Falcon Heavy) in 2026", "2026 weekly launch cadence: ~2.98 launches/week (approximately 3.0/week)",
"Average days between launches in 2026: 2.3 days", "Monthly average in 2026: 13.0 launches/month", "SpaceX President Gwynne Shotwell stated 2026 target of 'maybe 140, 145-ish' Falcon launches (per
Time magazine)", "At current pace, 2026 is projected to reach ~155 Falcon launches for the full year", "2025 full-year total was 165 Falcon launches (all Falcon 9), a record year", "2024 full-year
total was 134 Falcon launches (132 F9 + 2 FH)", "2026 YTD cadence (2.98/week) is below 2025 pace (3.17/week) but above 2024 pace (2.58/week)", "All-time Falcon 9/Heavy family total: 656 launches as of
May 30, 2026 (653 full mission successes)", "Booster B1067 holds the record with 34 missions; 616 successful booster landings out of 629 attempts (97.93%)", "Three dates in 2026 had two launches in a
single day: March 17, March 30, April 11", "Peak weekly launch rate in 2026: 4 launches in a single ISO week (occurred in weeks 3, 8, 9, 12, 18, 22)"], "data_points": [{"metric": "Falcon family
launches in 2026 YTD", "value": 66.0, "unit": "launches", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2026 weekly
launch cadence", "value": 2.98, "unit": "launches/week", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2026 average days
between launches", "value": 2.3, "unit": "days", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2026 monthly launch
average", "value": 13.0, "unit": "launches/month", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2026 annualized
projection at current pace", "value": 155.0, "unit": "launches", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Shotwell
2026 target (low end)", "value": 140.0, "unit": "launches", "as_of": "2026-01-01", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Shotwell 2026
target (high end)", "value": 145.0, "unit": "launches", "as_of": "2026-01-01", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2025 total Falcon
launches (full year)", "value": 165.0, "unit": "launches", "as_of": "2025-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2025 weekly
launch cadence", "value": 3.17, "unit": "launches/week", "as_of": "2025-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2024 total Falcon
launches (full year)", "value": 134.0, "unit": "launches", "as_of": "2024-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2024 weekly
launch cadence", "value": 2.58, "unit": "launches/week", "as_of": "2024-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "2023 total Falcon
launches (full year)", "value": 96.0, "unit": "launches", "as_of": "2023-12-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "All-time Falcon
9/Heavy launches", "value": 656.0, "unit": "launches", "as_of": "2026-05-30", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Booster landing
success rate", "value": 97.93, "unit": "percent", "as_of": "2026-05-30", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Successful booster
landings", "value": 616.0, "unit": "landings", "as_of": "2026-05-30", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Peak launches in single
week (2026)", "value": 4.0, "unit": "launches", "as_of": "2026-06-04", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Falcon 9 launches in
January 2026", "value": 13.0, "unit": "launches", "as_of": "2026-01-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Falcon 9 launches in
February 2026", "value": 12.0, "unit": "launches", "as_of": "2026-02-28", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Falcon 9 launches in
March 2026", "value": 13.0, "unit": "launches", "as_of": "2026-03-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Falcon 9 launches in April
2026", "value": 11.0, "unit": "launches", "as_of": "2026-04-30", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}, {"metric": "Falcon 9 launches in May 2026",
"value": 11.0, "unit": "launches", "as_of": "2026-05-31", "source_url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches"}], "created_at": "2026-06-06T02:32:14.330593Z",
"updated_at": "2026-06-06T02:32:14.330593Z", "stale_after": "2026-06-06T08:32:14.330593Z", "state": "fresh", "revision_history": [], "session_id": "33f0eda1-43d8-4053-a9de-4000aaa9ab91",
"follow_up_count": 0}, "is_follow_up": false}], "successful_count": 3, "failed_count": 0}
```

## 💬 Response

Excellent - I now have comprehensive data. Let me compile the confirmed launches in the window and run a simulation.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches",
  "prompt": "List all Falcon 9 and Falcon Heavy launches from May 28, 2026 onwards. Include date, mission name, and status for each launch. I need to count launches between May 28 and June 13, 2026 inclusive."
}
```

### 📋 Result

```
{"title": "List of Falcon 9 and Falcon Heavy launches", "url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches", "extract": "As of May 30, 2026, rockets from the Falcon 9
family have been launched 656 times, with 653 full mission successes, two mission failures during launch, one mission failure before launch, and one partial failure.\nDesigned and operated by SpaceX,
the Falcon 9 family includes the retired versions Falcon 9 v1.0, launched five times from June 2010 to March 2013; Falcon 9 v1.1, launched 15 times from September 2013 to January 2016; and Falcon 9
v1.2 \"Full Thrust\" (blocks 3 and 4), launched 36 times from December 2015 to June 2018. The active \"Full Thrust\" variant Falcon 9 Block 5 has launched 588 times since May 2018. Falcon Heavy, a
heavy-lift derivative of Falcon 9, combining a strengthened central core with two Falcon 9 first stages as side boosters has launched 12 times since February 2018.\n\nThe Falcon design features
reusable first-stage boosters, which land either on a ground pad near the launch site or on a drone ship at sea. In December 2015, Falcon 9 became the first rocket to land propulsively after
delivering a payload into orbit. This reusability results in significantly reduced launch costs, as the cost of the first stage constitutes the majority of the cost of a new rocket. Falcon family
boosters have successfully landed 616 times in 629 attempts. A total of 55 boosters have flown multiple missions, with a record of 34 missions by a booster, B1067. SpaceX has also reflown fairing
halves more than 300 times, with SN185 (36 times; 2nd most reflown rocket part to space) and SN168 (33 times) being the most reflown active and passive fairing halves respectively.\nTypical missions
include launches of SpaceX's Starlink satellites (accounting for a majority of the Falcon manifest since January 2020), Dragon crew and cargo missions to the International Space Station, and launches
of commercial and military satellites to LEO, polar, and geosynchronous orbits. The heaviest payload launched on Falcon is a batch of 24 Starlink V2-Mini satellites weighing about 17,500 kg (38,600
lb) total, first flown in February 2024, landing on JRTI. The heaviest payload launched to geostationary transfer orbit (GTO) was the 9,200 kg (20,300 lb) Jupiter-3 on July 29, 2023. Launches to
higher orbits have included DSCOVR and IMAP to Sun\u2013Earth Lagrange point L1, TESS to a lunar flyby, a Tesla Roadster demonstration payload to a heliocentric orbit extending past the orbit of Mars,
DART and Hera to the asteroid Didymos, Euclid to Sun-Earth Lagrange point L2, Psyche to the asteroid 16 Psyche, and Europa Clipper to Europa (a moon of Jupiter).", "mode": "full"}
```

```json
{
  "query": "SpaceX Falcon 9 launch June 5 6 2026"
}
```

### 📋 Result

```
{"query": "SpaceX Falcon 9 launch June 5 6 2026", "results": [{"title": "List of Falcon 9 and Falcon Heavy launches - Wikipedia", "url":
"https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches", "snippet": "As of May 30, 2026, rockets from the Falcon 9 family have been launched 656 times, with 653 full mission
successes, two mission failures during launch, one mission failure before launch, and one partial failure.\nDesigned and operated by SpaceX, the Falcon 9 family includes the retired versions Falcon 9
v1.0, launched five times from June 2010 to March 2013; Falcon 9 v1.1, launched 15 times from September 2013 to January 2016; and Falcon 9 v1.2 \"Full Thrust\" (blocks 3 and 4), launched 36 times fr",
"api_data": {"content": [{"type": "text", "text": "{\"title\": \"List of Falcon 9 and Falcon Heavy launches\", \"url\": \"https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches\",
\"extract\": \"As of May 30, 2026, rockets from the Falcon 9 family have been launched 656 times, with 653 full mission successes, two mission failures during launch, one mission failure before
launch, and one partial failure.\\nDesigned and operated by SpaceX, the Falcon 9 family includes the retired versions Falcon 9 v1.0, launched five times from June 2010 to March 2013; Falcon 9 v1.1,
launched 15 times from September 2013 to January 2016; and Falcon 9 v1.2 \\\"Full Thrust\\\" (blocks 3 and 4), launched 36 times from December 2015 to June 2018. The active \\\"Full Thrust\\\" variant
Falcon 9 Block 5 has launched 588 times since May 2018. Falcon Heavy, a heavy-lift derivative of Falcon 9, combining a strengthened central core with two Falcon 9 first stages as side boosters has
launched 12 times since February 2018.\\n\\nThe Falcon design features reusable first-stage boosters, which land either on a ground pad near the launch site or on a drone ship at sea. In December
2015, Falcon 9 became the first rocket to land propulsively after delivering a payload into orbit. This reusability results in significantly reduced launch costs, as the cost of the first stage
constitutes the majority of the cost of a new rocket. Falcon family boosters have successfully landed 616 times in 629 attempts. A total of 55 boosters have flown multiple missions, with a record of
34 missions by a booster, B1067. SpaceX has also reflown fairing halves more than 300 times, with SN185 (36 times; 2nd most reflown rocket part to space) and SN168 (33 times) being the most reflown
active and passive fairing halves respectively.\\nTypical missions include launches of SpaceX's Starlink satellites (accounting for a majority of the Falcon manifest since January 2020), Dragon crew
and cargo missions to the International Space Station, and launches of commercial and military satellites to LEO, polar, and geosynchronous orbits. The heaviest payload launched on Falcon is a batch
of 24 Starlink V2-Mini satellites weighing about 17,500 kg (38,600 lb) total, first flown in February 2024, landing on JRTI. The heaviest payload launched to geostationary transfer orbit (GTO) was the
9,200 kg (20,300 lb) Jupiter-3 on July 29, 2023. Launches to higher orbits have included DSCOVR and IMAP to Sun\\u2013Earth Lagrange point L1, TESS to a lunar flyby, a Tesla Roadster demonstration
payload to a heliocentric orbit extending past the orbit of Mars, DART and Hera to the asteroid Didymos, Euclid to Sun-Earth Lagrange point L2, Psyche to the asteroid 16 Psyche, and Europa Clipper to
Europa (a moon of Jupiter).\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Launch Schedule \u2013 Spaceflight Now", "url": "https://spaceflightnow.com/launch-schedule/", "snippet": "A regularly
updated listing of planned orbital missions from spaceports around the globe. Dates and times are given in Greenwich Mean Time. \u201cNET\u201d stands for no earlier than. \u201cTBD\u201d means to be
determined.\nSee our [Launch Log](http://spaceflightnow.com/launch-log/) for a listing of completed space missions since 2004.\nJune 6/7\nFalcon 9 \u2022 Starlink 17-43\nLaunch time:\nWindow opens at
7 p.m. PDT / 10 p.m. EDT on June 6 (0200 UTC on June 7)\nLaunch site: SLC-4E, Vandenberg Space Force Base, California\nA", "api_data": null, "hint": null}, {"title": "Nextspaceflight", "url":
"https://nextspaceflight.com/launches/", "snippet": "Launches | Next Spaceflight![ZhuQue-2E Block 2 rocket launch](https://storage.googleapis.com/nextspaceflight/media/rockets-
thumb/ZQ-2E_Block2.webp)\nZhuQue-2E Block 2 | Landspace Jiuquan Satellite Launch Center, China ![H3-30S rocket launch](https://storage.googleapis.com/nextspaceflight/media/rockets-
thumb/3RzL4Ew72htAj3xMyJGJTE.webp)\nTanegashima Space Center, Japan ![Long March 5 rocket launch](https://storage.googleapis.com/nextspaceflight/media/rockets-thumb/Long_March_5.webp)\nWenchang Space
", "api_data": null, "hint": null}, {"title": "Falcon 9 Launch Schedule - RocketLaunch.Live", "url": "https://www.rocketlaunch.live/?filter=falcon-9", "snippet": "Premium Members can get\nemail and
push notifications\nfor upcoming launches \u2014 straight to your inbox or browser, no app required.\nThis site thrives on the contributions from space enthusiasts like you!\nOur community has made
over 58 contributions in the last month.", "api_data": null, "hint": null}, {"title": "SpaceX Launch Schedule", "url": "https://rocketlaunch.org/launch-schedule/spacex", "snippet": "SpaceX Launch
Schedule\nStay updated on SpaceX's rocket launches with our real-time schedule. You can see 134 planned space missions on our website. Watch the live stream of any SpaceX rocket launch happening
today.\n[All Scheduled Launches](https://rocketlaunch.org/launch-schedule)SpaceX\nLaunch Service Provider\nVehicle\nBooster\nB1097\n10th flight (25d since last use)\nLanding\nDrone Ship (Of Course I
Still Love You)\nMission\nStarlink Group 17-43\nMission Type\nCommunications\nDestination\nLow Earth Orbit\n", "api_data": null, "hint": null}, {"title": "SpaceX - Launches", "url":
"https://www.spacex.com/launches", "snippet": "Ongoing missions\n- 6\n- 5\n- 8\n- 6\n- 1\n- 9\n- 5\n- 8\n- 1\n| Mission | Time On-Orbit | Return Date And Time |\n|---|---|---|\nCRS-34 Mission | T+ 0 1
2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 0 1 2 3 4 5 6 7 8 9 | June 2026 |\nCrew-12 Mission | T+ 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8
9 0 1 2 3 4 5 6 7 8 9 0 1 2 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 0 1 2 3 4 5 6 7 8 9 | October 2026 |\nUpcoming launches\n| Mission | ", "api_data": null, "hint": null},
{"title": "Falcon 9 Launch Schedule", "url": "https://rocketlaunch.org/launch-schedule/spacex/falcon-9", "snippet": "Falcon 9 Launch Schedule\nStay up-to-date on upcoming Falcon 9 rocket launches with
our live schedule. You can browse all 117 planned Falcon 9 missions on our website, and you can live stream any Falcon 9 rocket launch happening today.\n[All Scheduled
Launches](https://rocketlaunch.org/launch-schedule)\n[SpaceX](https://rocketlaunch.org/launch-schedule/spacex)Falcon 9\nLaunch Service Provider\nVehicle\nBooster\nB1097\n10th flight (25d since last
use)\nLanding\nDrone Ship (Of Course I Still Love You)\nMissi", "api_data": null, "hint": null}, {"title": "SpaceX launches sunrise Starlink mission following weather scrub \u2013 Spaceflight Now",
"url": "https://spaceflightnow.com/2026/06/03/live-coverage-spacex-to-launch-29-starlink-satellites-on-falcon-9-rocket-from-cape-canaveral-15/", "snippet": "![](http://spaceflightnow.com/wp-
content/uploads/2026/06/20260604_Starlink_10-43_liftoff_AB-1.jpeg)\nUpdate June 4, 6:54 a.m. EDT (1054 UTC): SpaceX landed its booster on the drone ship.\nUpdate June 3, 7:24 a.m. EDT (1124 UTC):
SpaceX scrubbed the launch.\nThe second time proved to be the charm as SpaceX launched its Falcon 9 rocket from Cape Canaveral Space Force Station on Thursday morning. It came about 24 hours after a
scrub on Wednesday due to poor weather that proved insurmountable.\nThe Star", "api_data": null, "hint": null}, {"title": "2026 Space Launch Schedule: Every Mission This Year | SpaceNexus | SpaceNexus
Guide", "url": "https://spacenexus.us/guide/space-launch-schedule-2026", "snippet": "Launch Activity Overview\n2026 is shaping up to be the busiest year in spaceflight history. The global space
industry is projected to conduct over 250 orbital launches, building on the record-breaking cadence of 2024 and 2025. SpaceX continues to dominate with roughly 40% of global launches, while China
maintains a robust 50+ launch campaign.\nNew entrants are reshaping the landscape: Blue Origin's New Glenn ramps toward operational cadence after its 2025 debut, Ariane 6 reaches full cadence in Eu",
"api_data": null, "hint": null}, {"title": "Rocket Launch Schedule & Countdown | Space Coast", "url": "https://www.visitspacecoast.com/launches/", "snippet": "Never miss a launch with the Space Coast
Launches App! Download now for the most up-to-date launch information.\n3 Unexpected Ways to Experience a Rocket Launch\nMake Your Launch Viewing Experience Special Rocket launches have drawn visitors
to the Space Coast for decades. With SpaceX, ULA, and NASA booking launch pads on an almost weekly basis, seeing a launch while you\u2019re vacationing on the Space Coast is a high probability. While
you know about going to Kennedy...\n[View Article](https://www.vis", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://spaceflightnow.com/launch-schedule/",
  "prompt": "List all SpaceX Falcon 9 and Falcon Heavy launches from late May through mid-June 2026. I need specific dates and mission names. Include both completed launches and upcoming scheduled launches."
}
```

### 📋 Result

```
{"url": "https://spaceflightnow.com/launch-schedule/", "content": "Based on the provided content, here are the SpaceX Falcon 9 and Falcon Heavy launches from late May through mid-June
2026:\n\n**Scheduled Upcoming Launches:**\n\n1. **June 6/7** - Falcon 9 \u2022 Starlink 17-43\n   - Launch window opens: 7 p.m. PDT / 10 p.m. EDT on June 6 (0200 UTC on June 7)\n   - Location:
Vandenberg Space Force Base, California\n\n2. **June 8** - Falcon 9 \u2022 Starlink 10-35\n   - Launch window opens: 6:07 a.m. EDT (1007 UTC)\n   - Location: Cape Canaveral Space Force Station,
Florida\n\n3. **June 10** - Falcon 9 \u2022 Starlink 17-44\n   - Launch window opens: 7 a.m. PDT (10 a.m. EDT / 1400 UTC)\n   - Location: Vandenberg Space Force Base, California\n\n4. **TBD** - Falcon
9 \u2022 Globalstar 2-R Launch 1\n   - Location: Cape Canaveral Space Force Station, Florida\n   - (Previously delayed from May 18 and May 20)\n\n**Note:** The content does not include information
about completed launches from late May. It only shows upcoming scheduled launches starting from June 6/7, 2026. No Falcon Heavy launches are listed for this timeframe.\n\n**Relevant links:**\n-
[Launch Log](http://spaceflightnow.com/launch-log/) - for listing of completed space missions since 2004", "title": "Launch Schedule"}
```

```json
{
  "url": "https://nextspaceflight.com/launches/",
  "prompt": "List all upcoming SpaceX Falcon 9 launches in June 2026 with dates and mission names."
}
```

### 📋 Result

```
{"url": "https://nextspaceflight.com/launches/", "content": "Based on the provided content, there is **one SpaceX Falcon 9 launch** mentioned:\n\n- **Falcon 9 Block 5** launching from Cape Canaveral
SFS, Florida, USA\n\nHowever, the content does **not provide specific dates or mission names** for this or any other launches. The webpage appears to show a list of upcoming launches with images but
without the detailed scheduling information needed to answer your question about June 2026 launches specifically.\n\n**Relevant links:**\n- [Watch
livestream](https://www.youtube.com/watch?v=uUc2d_NPBN0) (Note: This link appears to be associated with the Spectrum rocket launch, not the Falcon 9)\n\nTo get current launch dates and mission details
for SpaceX Falcon 9 launches in June 2026, you would need to access the full webpage at https://nextspaceflight.com/launches/ directly.", "title": "Up Next"}
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://spaceflightnow.com/launch-log/",
  "prompt": "Find all SpaceX Falcon 9 launches that occurred between May 28 and June 6, 2026. List dates and mission names."
}
```

### 📋 Result

```
{"url": "https://spaceflightnow.com/launch-log/", "content": "The provided text is from 2023, not 2026. It shows completed space launches from 2023, with references to earlier missions from 2004-2022.
There are no launches listed from May 28 to June 6, 2026, as that content is not included in this document.\n\nThe document states at the beginning: \"This listing shows the completed space launches
from spaceports around the globe in 2023.\"\n\nRelevant links:\n- [Launches from 2004 through 2008](http://spaceflightnow.com/launch-log-2004-2008/)\n- [Launches from 2009 through
2011](http://spaceflightnow.com/launch-log-2009-2011/)\n- [Launches from 2012 through 2014](http://spaceflightnow.com/launch-log-2012-2014/)\n- [Launches from 2015 through
2016](http://spaceflightnow.com/launch-log-2015-2016/)\n- [Launches from 2019 through 2020](http://spaceflightnow.com/launch-log-2019-2020/)\n- [Launches from 2021 through
2022](http://spaceflightnow.com/launch-log-2021-2022/)", "title": "Launch Log"}
```

## 💬 Response

Let me try to get the specific Wikipedia page for 2026 launches and the SpaceX launches page.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches_(2026)",
  "prompt": "List ALL Falcon 9 and Falcon Heavy launches from May 28, 2026 through June 13, 2026. Include date, mission name, launch site, and outcome. I need the complete count of launches in this window."
}
```

### 📋 Result

```
ValueError: Article not found: List of Falcon 9 and Falcon Heavy launches (2026)
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.spacex.com/launches",
  "prompt": "List all SpaceX Falcon 9 launches from late May 2026 through mid-June 2026. Include dates and mission names for both completed and upcoming launches."
}
```

### 📋 Result

```
{"url": "https://www.spacex.com/launches", "content": "Based on the provided content, here are the SpaceX Falcon 9 launches from late May 2026 through mid-June 2026:\n\n**Completed Missions:**\n- June
4, 2026 - Starlink Mission (SLC-40, Florida)\n- June 3, 2026 - Starlink Mission (SLC-4E, California)\n- May 30, 2026 - Starlink Mission (SLC-4E, California)\n- May 29, 2026 - Starlink Mission (SLC-40,
Florida)\n- May 26, 2026 - Starlink Mission (SLC-4E, California)\n- May 25, 2026 - Starlink Mission (SLC-40, Florida)\n- May 21, 2026 - Starlink Mission (SLC-40, Florida)\n\n**Upcoming
Launches:**\nThe content shows 5 upcoming Starlink missions on Falcon 9 rockets, but specific dates are not clearly displayed. One launch shows a countdown timer suggesting it's imminent, launching
from SLC-4E, California. The others are from SLC-40, Florida and SLC-4E, California, but exact dates are not provided in the text.\n\nRelevant links:\n- [SpaceX
Launches](https://www.spacex.com/launches)", "structured_data": ["### Result\n\"[]\"\n### Ran Playwright code\n```js\nawait page.evaluate('() => {\\n    const results = [];\\n\\n    // Next.js
embedded data\\n    if (window.__NEXT_DATA__) {\\n        try {\\n            const s = JSON.stringify(window.__NEXT_DATA__);\\n            if (s.length < 500000) results.push(s);\\n        } catch
{}\\n    }\\n\\n    // JSON script tags (common in SSR frameworks)\\n    for (const el of document.querySelectorAll(\\'script[type=\"application/json\"]\\')) {\\n        const t = el.textContent;\\n
if (t && t.length > 10 && t.length < 500000) results.push(t);\\n    }\\n\\n    // Common global state patterns\\n    for (const key of [\\n        \\'__INITIAL_STATE__\\', \\'__PRELOADED_STATE__\\',
\\'__APP_DATA__\\',\\n        \\'__NUXT__\\', \\'__APOLLO_STATE__\\',\\n    ]) {\\n        if (window[key]) {\\n            try {\\n                const s = JSON.stringify(window[key]);\\n
if (s.length < 500000) results.push(s);\\n            } catch {}\\n        }\\n    }\\n\\n    return JSON.stringify(results);\\n}');\n```"]}
```

## 💭 Thinking

Now I have good data. Let me compile what I know:

**Confirmed launches in the window (May 28 - June 13 inclusive):**

From the research:
1. May 29, 2026 - Starlink Group 10-53 (SLC-40, Cape Canaveral) ✅
2. May 30, 2026 - Starlink Group 17-41 (SLC-4E, Vandenberg) ✅
3. June 3, 2026 - Starlink Group 17-47 (SLC-4E, Vandenberg) ✅
4. June 4, 2026 - Starlink Group 10-43 (SLC-40, Cape Canaveral) ✅

That gives me four confirmed completed launches through June 4. There's no launch on May 28, and the next one after June 4 appears to be June 7.

Looking at the confirmed launches coming up between June 7 and June 13, I've got four scheduled: Starlink 17-43 on June 7 at Vandenberg, Starlink 10-35 on June 8 at Cape Canaveral, Starlink 17-44 on June 10 at Vandenberg, and Starlink 10-54 on June 12 at Cape Canaveral. The June 14 launch falls outside the window since it's after the 00:00 UTC cutoff.

Beyond these confirmed missions, there are other possibilities to consider. The Globalstar 2-R mission that was originally scheduled for May could potentially slip into this window, and there are several TBD June missions like BlueBird Block 2 and SDA missions that might get scheduled. SpaceX also tends to add unscheduled Starlink missions, so the actual count could be higher. Given the typical cadence of about three launches per week, I'm trying to estimate what the remaining launches might look like. I'm reviewing the completed launches more carefully—there were actually 7 launches from late May through early June (May 21, 25, 26, 29, 30, and June 3, 4), with gaps on May 28, June 1, 2, 5, and 6. Now I need to reconcile this with the question's mention of roughly 9-10 launches in May and figure out which launches fall within the relevant timeframe. So looking at the confirmed launches from June 6-13, I've got 4 more scheduled missions, bringing the total to 8 launches in this window. At their current cadence of about 2.98 launches per week, 17 days should yield around 7.2 launches, so 8 seems reasonable—possibly even slightly above their typical rate. The alternating East and West coast pad operations let them sustain roughly 2 per week from each location, and there could be additional TBD missions added to the schedule.

I'm wondering if there might be launches on the gaps between the confirmed dates—June 6, 9, 11, or 13—since SpaceX has shown they can do rapid-fire launches. The current pattern of every ~2 days (June 7, 8, 10, 12) matches their typical cadence, but they've done double launches on the same day a few times this year. I should also account for the possibility of scrubs pushing some missions beyond June 13 or earlier. Let me model this with a Monte Carlo simulation to get a better sense of the probability distribution. Possible additional launches could happen on Jun 6 or 9 (20-30% chance each), plus there's a small chance for Globalstar or other TBD missions. Looking at the monthly patterns from January through May, the average is around 11-13 launches per month, which translates to roughly 6-7 launches in a 17-day window. With 4 already completed and 4 confirmed upcoming, hitting 8 total seems reasonable and slightly above the typical monthly rate.

Breaking down the specific timeframe: May 28 to June 13 spans two months, with only 2 launches visible in late May and 2 more in early June, giving about 3.5 launches per week—above average but plausible. For the remaining 8 days, I have 4 confirmed launches, and there could realistically be 0-2 additional ones. I should model this with a simulation that accounts for the confirmed launches plus the probability of additional missions occurring.

## 💬 Response

Now let me compile the data and run a Monte Carlo simulation.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# ==========================================\n# SpaceX Falcon 9/Heavy launches: May 28 - June 13, 2026 (UTC)\n# ==========================================\n\n# COMPLETED launches in window (confirmed)\ncompleted = [\n    \"May 29 - Starlink Group 10-53\",\n    \"May 30 - Starlink Group 17-41\",\n    \"Jun 3 - Starlink Group 17-47\",\n    \"Jun 4 - Starlink Group 10-43\",\n]\nn_completed = len(completed)\nprint(f\"Completed launches in window: {n_completed}\")\n\n# UPCOMING confirmed \"Go for Launch\" in window\nupcoming_confirmed = [\n    \"Jun 7 - Starlink Group 17-43 (0200 UTC)\",\n    \"Jun 8 - Starlink Group 10-35 (1007 UTC)\",\n    \"Jun 10 - Starlink Group 17-44 (1400 UTC)\",\n    \"Jun 12 - Starlink Group 10-54 (1227 UTC)\",\n]\nn_upcoming = len(upcoming_confirmed)\nprint(f\"Upcoming confirmed in window: {n_upcoming}\")\nprint(f\"Base count (completed + upcoming): {n_completed + n_upcoming}\")\n\n# Jun 14 launch (Starlink 17-54) is at 14:00 UTC on June 14 - OUTSIDE window\n# Window ends before 00:00 UTC June 14\n\n# ==========================================\n# Cadence statistics from 2026 data\n# ==========================================\n# 66 launches in ~155 days (Jan 1 - Jun 4) \n# = 0.426 launches/day = 2.98/week\n# Monthly: Jan=13, Feb=12, Mar=13, Apr=11, May=11, Jun(partial)=2+\n# Days between launches: avg 2.3 days\n# Peak: 4 launches in a single ISO week (occurred 6 times)\n# Double-launch days: 3 times (Mar 17, Mar 30, Apr 11)\n\ndaily_rate = 66 / 155  # 0.426\nprint(f\"\\n2026 daily launch rate: {daily_rate:.3f}\")\nprint(f\"2026 weekly launch rate: {daily_rate * 7:.2f}\")\n\n# For 17-day window at this rate:\nexpected_17day = daily_rate * 17\nprint(f\"Expected launches in 17-day window at avg rate: {expected_17day:.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Completed launches in window: 4\nUpcoming confirmed in window: 4\nBase count (completed + upcoming): 8\n\n2026 daily launch rate: 0.426\n2026 weekly launch rate:
2.98\nExpected launches in 17-day window at avg rate: 7.2\n", "stderr": "", "duration_ms": 229}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\nnp.random.seed(42)\nn_sims = 100000\n\n# ==========================================\n# Monte Carlo Simulation\n# ==========================================\n# Structure:\n# 1. 4 completed launches (certain)\n# 2. 4 confirmed upcoming launches, each with some probability of scrub \n#    pushing beyond window\n# 3. Additional unscheduled launches in remaining days\n\nn_completed = 4\n\n# Probability each confirmed upcoming launch actually happens in window\n# Scrub probability: historically ~10-15% of Falcon 9 launches get scrubbed once,\n# but usually they fly within 1-2 days. Given Jun 7, 8, 10, 12 - if scrubbed,\n# they'd likely fly next day which is still within window.\n# Only Jun 12 scrub could push to Jun 14+ (outside window)\n# Jun 7 scrub -> Jun 8 or 9 (still in window, 97%)\n# Jun 8 scrub -> Jun 9 or 10 (still in window, 97%)\n# Jun 10 scrub -> Jun 11 or 12 (still in window, 97%)\n# Jun 12 scrub -> Jun 13 (still in window, but tight, 93%)\n\np_confirmed = [0.97, 0.97, 0.97, 0.93]\n\n# Additional launches: there are TBD missions for June (Globalstar 2-R, \n# BlueBird, SDA missions, SXM-11). Could one get scheduled?\n# Also SpaceX sometimes adds Starlink missions to fill gaps.\n# \n# Remaining days without confirmed launches: Jun 6, 9, 11, 13\n# Probability of an additional launch on each of these days:\n# Jun 6: today, no launch announced, very unlikely (~5%)\n# Jun 9: gap between Jun 8 and Jun 10, possible (~15%)\n# Jun 11: gap between Jun 10 and Jun 12, possible (~15%)\n# Jun 13: after Jun 12, possible (~12%)\n# Plus: Globalstar 2-R could happen any day (~10% total in window)\n# Overall probability of at least 1 additional launch: ~35%\n\nresults = np.zeros(n_sims)\n\nfor i in range(n_sims):\n    total = n_completed\n    \n    # Each confirmed launch\n    for p in p_confirmed:\n        if np.random.random() < p:\n            total += 1\n    \n    # Additional unscheduled launches\n    # Model as: each of 4 gap days has an independent probability of a launch\n    gap_day_probs = [0.05, 0.15, 0.15, 0.12]  # Jun 6, 9, 11, 13\n    for p in gap_day_probs:\n        if np.random.random() < p:\n            total += 1\n    \n    # Small probability of a double-launch day (happened 3/155 days = ~2%)\n    # On any of the confirmed launch days\n    for _ in range(4):\n        if np.random.random() < 0.02:\n            total += 1\n    \n    results[i] = total\n\n# Results\nprint(\"=== Monte Carlo Results (100k sims) ===\")\nprint(f\"Mean: {np.mean(results):.2f}\")\nprint(f\"Median: {np.median(results):.1f}\")\nprint(f\"Mode: {np.argmax(np.bincount(results.astype(int)))}\")\nprint(f\"Std Dev: {np.std(results):.2f}\")\nprint()\n\n# Distribution\nfor val in range(0, 16):\n    count = np.sum(results == val)\n    pct = count / n_sims * 100\n    if pct > 0.01:\n        bar = '\u2588' * int(pct * 2)\n        print(f\"  {val:2d}: {pct:6.2f}% {bar}\")\n\nprint()\n\n# Percentiles\npercentiles = [1, 5, 10, 20, 25, 30, 40, 50, 60, 70, 75, 80, 90, 95, 99]\nprint(\"Percentiles:\")\nfor p in percentiles:\n    v = np.percentile(results, p)\n    print(f\"  P{p:02d}: {v:.1f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Monte Carlo Results (100k sims) ===\nMean: 8.39\nMedian: 8.0\nMode: 8\nStd Dev: 0.80\n\n   5:   0.01% \n   6:   0.51% \u2588\n   7:   8.24%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n   8:  52.48% \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u25
88\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u
2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n   9:  30.59% \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u
2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  10:   7.25%
\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2588\n  11:   0.88% \u2588\n  12:   0.05% \n\nPercentiles:\n  P01: 7.0\n  P05: 7.0\n  P10: 8.0\n  P20: 8.0\n  P25: 8.0\n
P30: 8.0\n  P40: 8.0\n  P50: 8.0\n  P60: 8.0\n  P70: 9.0\n  P75: 9.0\n  P80: 9.0\n  P90: 9.0\n  P95: 10.0\n  P99: 10.0\n", "stderr": "", "duration_ms": 367}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# Let me also do a sensitivity analysis with a different model\n# Instead of per-launch probabilities, model using a Poisson process\n# based on historical daily launch rate\n\nimport numpy as np\nnp.random.seed(123)\nn_sims = 100000\n\n# Historical daily rate for 2026: 0.426 launches/day\n# But let's also consider that this window already has 4 completed + 4 confirmed\n# So we know the \"truth\" partially\n\n# Alternative: just use historical 17-day windows\n# From monthly data: Jan=13, Feb=12, Mar=13, Apr=11, May=11\n# 17 days is about 56% of a month\n# Expected per 17 days: 11*0.56=6.2 to 13*0.56=7.3\n\n# But we ALREADY KNOW 4 completed launches happened.\n# And we have 4 confirmed upcoming.\n# The question is mainly about:\n# 1. Do all 4 confirmed launches happen? (very likely)\n# 2. Are there any additional launches? (some probability)\n\n# Let me also check: what if I'm missing a launch?\n# The question description says \"roughly 9-10 Falcon 9 launches in May\" \n# but research says 11. The description was written as context, may not be precise.\n\n# Let me also model with a higher additional launch probability\n# to see sensitivity\n\nprint(\"=== Sensitivity Analysis ===\\n\")\n\nfor scenario_name, gap_probs, scrub_probs in [\n    (\"Conservative\", [0.03, 0.10, 0.10, 0.08], [0.97, 0.97, 0.97, 0.93]),\n    (\"Base case\", [0.05, 0.15, 0.15, 0.12], [0.97, 0.97, 0.97, 0.93]),\n    (\"Aggressive\", [0.10, 0.25, 0.25, 0.20], [0.98, 0.98, 0.98, 0.95]),\n    (\"Very Aggressive (maybe missed a launch)\", [0.20, 0.30, 0.30, 0.25], [0.98, 0.98, 0.98, 0.95]),\n]:\n    results = np.zeros(n_sims)\n    for i in range(n_sims):\n        total = 4  # completed\n        for p in scrub_probs:\n            if np.random.random() < p:\n                total += 1\n        for p in gap_probs:\n            if np.random.random() < p:\n                total += 1\n        for _ in range(4):\n            if np.random.random() < 0.02:\n                total += 1\n        results[i] = total\n    \n    print(f\"{scenario_name}:\")\n    print(f\"  Mean: {results.mean():.2f}, P10: {np.percentile(results,10):.0f}, \"\n          f\"P50: {np.percentile(results,50):.0f}, P90: {np.percentile(results,90):.0f}\")\n    # Show probability of each value\n    probs = {}\n    for v in range(5, 14):\n        probs[v] = np.sum(results == v) / n_sims\n        if probs[v] > 0.005:\n            print(f\"    P({v}) = {probs[v]*100:.1f}%\")\n    print()\n\n# The base case is my primary model\n# Let me also check: could there be a launch on June 5 that we missed?\n# The SpaceX page and research both show Jun 4 as the last completed launch.\n# Jun 5 would have been yesterday - if it happened, it should be in the records.\n# I'll assume we have complete data for completed launches.\n\n# What about today (June 6)?\n# The Spaceflightnow schedule shows next launch is Jun 6/7 (Starlink 17-43)\n# with window opening at 0200 UTC Jun 7. So no launch on Jun 6.\nprint(\"Today (Jun 6): No Falcon 9 launch scheduled (next is Jun 7 at 0200 UTC)\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Sensitivity Analysis ===\n\nConservative:\n  Mean: 8.23, P10: 7, P50: 8, P90: 9\n    P(6) = 0.6%\n    P(7) = 9.8%\n    P(8) = 60.7%\n    P(9) = 24.5%\n    P(10) =
4.0%\n\nBase case:\n  Mean: 8.39, P10: 8, P50: 8, P90: 9\n    P(7) = 8.3%\n    P(8) = 52.4%\n    P(9) = 30.8%\n    P(10) = 7.2%\n    P(11) = 0.8%\n\nAggressive:\n  Mean: 8.77, P10: 8, P50: 9, P90:
10\n    P(7) = 3.9%\n    P(8) = 37.7%\n    P(9) = 39.1%\n    P(10) = 15.7%\n    P(11) = 3.1%\n\nVery Aggressive (maybe missed a launch):\n  Mean: 9.02, P10: 8, P50: 9, P90: 10\n    P(7) = 2.9%\n
P(8) = 28.6%\n    P(9) = 39.1%\n    P(10) = 22.4%\n    P(11) = 6.0%\n    P(12) = 0.8%\n\nToday (Jun 6): No Falcon 9 launch scheduled (next is Jun 7 at 0200 UTC)\n", "stderr": "", "duration_ms": 1244}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nnp.random.seed(42)\nn_sims = 200000\n\n# Final model: Use base case with slight adjustment\n# I'm fairly confident in the data: 4 completed, 4 confirmed upcoming\n# Small probability of additional launches\n\nn_completed = 4\n\n# Confirmed upcoming with scrub probabilities\np_confirmed = [0.97, 0.97, 0.97, 0.93]\n\n# Gap days for additional launches\n# Jun 6 (today, nothing announced), Jun 9, Jun 11, Jun 13\ngap_day_probs = [0.05, 0.15, 0.15, 0.12]\n\n# Double-launch days (2% per confirmed launch day)\np_double = 0.02\n\nresults = np.zeros(n_sims, dtype=int)\n\nfor i in range(n_sims):\n    total = n_completed\n    \n    for p in p_confirmed:\n        if np.random.random() < p:\n            total += 1\n    \n    for p in gap_day_probs:\n        if np.random.random() < p:\n            total += 1\n    \n    for _ in range(4):\n        if np.random.random() < p_double:\n            total += 1\n    \n    results[i] = total\n\n# Generate percentile values for discrete distribution\n# For discrete distributions, I need to properly compute the CDF\npercentiles = [1, 2, 5, 10, 15, 20, 25, 30, 40, 50, 60, 70, 75, 80, 85, 90, 95, 98, 99]\n\nprint(\"=== Final Distribution ===\")\nprint(f\"Mean: {results.mean():.2f}\")\nprint(f\"Std Dev: {results.std():.2f}\")\nprint()\n\n# PMF\nprint(\"Probability Mass Function:\")\nfor v in range(4, 16):\n    p = np.mean(results == v) * 100\n    if p > 0.001:\n        print(f\"  P(X={v:2d}) = {p:6.3f}%\")\n\nprint()\n\n# CDF\nprint(\"Cumulative Distribution:\")\nfor v in range(4, 16):\n    p = np.mean(results <= v) * 100\n    if 0.001 < p:\n        print(f\"  P(X<={v:2d}) = {p:7.3f}%\")\n\nprint()\n\n# Percentiles (for discrete, use quantile function)\nprint(\"Percentiles:\")\npct_dict = {}\nfor p in percentiles:\n    v = np.percentile(results, p, method='nearest')\n    pct_dict[str(p)] = int(v)\n    print(f\"  P{p:02d}: {v}\")\n\nprint()\nprint(f\"Percentile dict: {pct_dict}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Final Distribution ===\nMean: 8.39\nStd Dev: 0.80\n\nProbability Mass Function:\n  P(X= 5) =  0.013%\n  P(X= 6) =  0.493%\n  P(X= 7) =  8.215%\n  P(X= 8) = 52.419%\n
P(X= 9) = 30.643%\n  P(X=10) =  7.276%\n  P(X=11) =  0.883%\n  P(X=12) =  0.055%\n\nCumulative Distribution:\n  P(X<= 5) =   0.015%\n  P(X<= 6) =   0.507%\n  P(X<= 7) =   8.723%\n  P(X<= 8) =
61.142%\n  P(X<= 9) =  91.785%\n  P(X<=10) =  99.061%\n  P(X<=11) =  99.944%\n  P(X<=12) =  99.999%\n  P(X<=13) = 100.000%\n  P(X<=14) = 100.000%\n  P(X<=15) = 100.000%\n\nPercentiles:\n  P01: 7\n
P02: 7\n  P05: 7\n  P10: 8\n  P15: 8\n  P20: 8\n  P25: 8\n  P30: 8\n  P40: 8\n  P50: 8\n  P60: 8\n  P70: 9\n  P75: 9\n  P80: 9\n  P85: 9\n  P90: 9\n  P95: 10\n  P98: 10\n  P99: 10\n\nPercentile dict:
{'1': 7, '2': 7, '5': 7, '10': 8, '15': 8, '20': 8, '25': 8, '30': 8, '40': 8, '50': 8, '60': 8, '70': 9, '75': 9, '80': 9, '85': 9, '90': 9, '95': 10, '98': 10, '99': 10}\n", "stderr": "",
"duration_ms": 663}
```

## 💬 Response

Now let me run the reflection and premortem.
