# Reasoning Log: How many Artemis Accords signatories will NASA list on its Artemis Accords page before April 30, 2026?

*Generated: 2026-03-16T04:53:03.636230+00:00*


## 💭 Thinking

Let me analyze this forecasting question about the number of Artemis Accords signatories NASA will list on its page before April 30, 2026.

Key details:
- Resolution: Count of signatories on NASA's Artemis Accords page as of April 30, 2026
- Options: ≤61, 62, >62
- Close: March 16, 2026
- Resolve: April 30, 2026
- Published: March 16, 2026

I need to find:
1. Current number of signatories
2. Rate of new signatories joining
3. Whether any are expected to join before April 30, 2026


4. The most recent NASA Artemis Accords page to get the current count

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    42637
  ]
}
```

### 📋 Result

```
{"post_id": 42637, "title": "How many Artemis Accords signatories will NASA list on its Artemis Accords page before April 30, 2026?", "type": "multiple_choice", "url":
"https://www.metaculus.com/questions/42637", "background_info": "This forecasts the number of countries NASA will list as Artemis Accords signatories by the end of April
2026.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"f6b1c582d4b28338\",\"sheet_id\":392.1}}`", "resolution_criteria": "This question resolves to the number of signatories listed
on NASA\u2019s Artemis Accords page at https://www.nasa.gov/artemis-accords/ as of  April 30, 2026.", "fine_print": "Use the count implied by the signatories listed on the official NASA page. If NASA
changes the layout, count the countries shown as current signatories on that page. Candidate Sources: NASA's main Artemis site at https://www.nasa.gov/artemis/ ; the Artemis Accords page itself.",
"num_forecasters": 19, "community_prediction": null, "options": ["Less than or equal to 61", "62", "Greater than 62"]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.nasa.gov/artemis-accords/",
  "prompt": "How many countries are listed as signatories? List them all and count them."
}
```

### 📋 Result

```
{"url": "https://www.nasa.gov/artemis-accords/", "content": "Based on the provided content, **61 countries** are signatories to the Artemis Accords as of January 26, 2026, when Oman became the 61st
nation to sign.\n\nHowever, **the content does not list all 61 countries by name**. It only mentions:\n- Seven initial signatory nations (2020) - not named\n- Oman (61st signatory, January 26,
2026)\n\nThe content indicates that a complete list exists in a PDF document but does not provide the actual names of all signatories in the text.\n\n**Relevant links:**\n- [Read the Artemis Accords
(1MB PDF)](https://www.nasa.gov/artemis-accords/) - Full text of the accords\n- [List of the Signatories by Date (36KB PDF)](https://www.nasa.gov/artemis-accords/) - Complete list of all signatory
countries\n- [NASA, International Partners Advance Cooperation with First Signings of Artemis Accords](https://www.nasa.gov/artemis-accords/) - Original NASA news release", "title": "Artemis Accords -
NASA"}
```

```json
{
  "query": "Artemis Accords signatories 2026 count how many countries"
}
```

### 📋 Result

```
{"query": "Artemis Accords signatories 2026 count how many countries", "results": [{"title": "Artemis Accords - Wikipedia", "url": "https://en.wikipedia.org/wiki/Artemis_Accords", "snippet": "The
Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world governments that elaborates on the norms expected to be followed in outer space.
The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the ultimate goal of expanding space exploration to Mars and beyond.\nAs of 26 January
2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe,", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Artemis Accords\", \"url\":
\"https://en.wikipedia.org/wiki/Artemis_Accords\", \"extract\": \"The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world
governments that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the
ultimate goal of expanding space exploration to Mars and beyond.\\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe, 15 in Asia, seven in
South America, five in North America, four in Africa, and two in Oceania.\\nDrafted by NASA and the U.S. Department of State, the Accords establish a framework for cooperation in the civil exploration
and peaceful use of the Moon, Mars, and other astronomical objects. They are explicitly grounded in the United Nations Outer Space Treaty of 1967, which signatories are obliged to uphold, and cite
most major U.N.-brokered conventions constituting space law.\\nThe Accords were originally signed on 13 October 2020 by representatives of the national space agencies of eight countries: Australia,
Canada, Italy, Japan, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States. The Accords remain open for signature indefinitely, as NASA anticipates more nations joining.
Additional signatories can choose to directly participate in Artemis program activities, or may agree simply to commit to the principles for responsible exploration of the Moon as set out in the
Accords.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Artemis Accords - NASA", "url": "https://www.nasa.gov/artemis-accords/", "snippet": "Principles for a Safe, Peaceful, and Prosperous
Future in Space\nNASA, in coordination with the U.S. Department of State and seven other initial signatory nations, established the Artemis Accords in 2020. With many countries and private companies
conducting missions and operations around the Moon, the Artemis Accords provide a common set of principles to enhance the governance of the civil exploration and use of outer space.\nThe Artemis
Accords reinforce the commitment by signatory nations to the", "api_data": null, "hint": null}, {"title": "Artemis Accords - United States Department of State", "url": "https://www.state.gov/bureau-
of-oceans-and-international-environmental-and-scientific-affairs/artemis-accords", "snippet": "Official websites use .gov\nA .gov website belongs to an official government organization in the United
States.Secure .gov websites use HTTPS\nA lock ( ) or https:// means you\u2019ve safely connected to the .gov website. Share sensitive information only on official, secure websites.Americans in the
Middle East:\nFor consular information or assistance, call the Department of State\u2019s 24/7 Task Force at +1-202-501-4444 (from abroad) and 1-888-407-4747 (from the U.S. and Canada).", "api_data":
null, "hint": null}, {"title": "ESA - Gateway MoU and Artemis Accords \u2013 FAQs", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Gateway_MoU_and_Artemis_Accords_FAQs",
"snippet": "Gateway MoU and Artemis Accords \u2013 FAQs\nESA Director General Jan W\u00f6rner and NASA Administrator Jim Bridenstine
[signed](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Positive_signs_for_Europe_as_ESA_goes_forward_to_the_Moon) a Memorandum of Understanding (MoU) to take Europe to the
Moon.\nThe historic agreement will see ESA Member States contribute a number of essential elements to the first human outpost in lunar orbit, known as the Gateway.\nIt confirms ESA\u2019s commitment
to", "api_data": null, "hint": null}, {"title": "Artemis Accords: What are they & which countries are involved? | Space", "url": "https://www.space.com/artemis-accords-explained", "snippet": "The
Artemis Accords lay out the framework for collaborating nations as we enter the next era of lunar exploration and beyond.\nThe next era of space exploration is underway with the Artemis program aiming
to send the first woman and person of color to the lunar surface before targeting a crewed mission to Mars. The Artemis accords lay out a framework for nations collaborating in this exciting
endeavor.(Image credit: NASA)\nBreaking space news, the latest updates on rocket launches, skywatching eve", "api_data": null, "hint": null}, {"title": "Artemis Accords | NASA, United States, Outer
Space Treaty, Criticism, Summary, Russia, & China | Britannica", "url": "https://www.britannica.com/topic/Artemis-Accords", "snippet": "[Artemis
Accords](https://cdn.britannica.com/28/283728-050-7CCE29BC/Signing-Ceremony-Artemis-Accords-At-NASA-Headquarters-2024.jpg)Representatives from Uruguay signing the Artemis Accords, making Uruguay the
36th country to sign the accords.\nArtemis Accords\nWhat are the Artemis Accords?\nWhich countries were the initial signatories of the Artemis Accords?\nWhat are the stated objectives of the Artemis
Accords?\nWhy did Russia and China not sign the Artemis Accords?\nArtemis Accords, set of principle", "api_data": null, "hint": null}, {"title": "NASA Celebrates Five Years of Artemis Accords,
Welcomes 3 New Nations - NASA", "url": "https://www.nasa.gov/organizations/oiir/artemis-accords/nasa-celebrates-five-years-of-artemis-accords-welcomes-3-new-nations/", "snippet": "October marked the
fifth anniversary of NASA and the original founders signing the Artemis Accords, as well as the recognition of Hungary, Malaysia and the Philippines joining the expanding coalition dedicated to the
peaceful exploration of space. The number of countries involved now totals 59.\n\u201cNASA welcomes the newest signatories, whose participation strengthens the global commitment to responsible
exploration,\u201d said acting NASA Administrator Sean Duffy. \u201cTheir decision to sign the Artemis Acc", "api_data": null, "hint": null}, {"title": "The Artemis Accords By the Numbers", "url":
"https://payloadspace.com/the-artemis-accords-by-the-numbers/", "snippet": "This article was updated Jan. 27 to reflect Oman\u2019s addition to the Accords.\nOman announced this week that it had
signed on to the Artemis Accords, becoming the 61st nation to agree to the set of non-binding principles.\nA quick reminder: The US led the establishment of the Artemis Accords in 2020. Nations who
sign on commit to exploring space in a peaceful, transparent, and sustainable way.\nThe accords celebrated their fifth anniversary in October. As such, here\u2019s a roundup of where they stand.\nG",
"api_data": null, "hint": null}, {"title": "US Artemis Accords Hit 50 Signatories in 2024 - AIP.ORG", "url": "https://www.aip.org/fyi/us-artemis-accords-hit-50-signatories-in-2024", "snippet": "US
Artemis Accords Hit 50 Signatories in 2024\n![A NASA graphic showing the flags of the first 48 nations to sign on to the Artemis
Accords.](https://aip.brightspotcdn.com/dims4/default/bac391f/2147483647/strip/true/crop/4000x2250+0+0/resize/820x461!/quality/90/?url=https%3A%2F%2Fk1-prod-aip.s3.us-
east-2.amazonaws.com%2Fbrightspot%2F6e%2Fa3%2F2b796c474f51a15f51699f88712d%2Fartemis-accords-austria-50-121124.png)\nThe flags of the first 48 Artemis Accords signatories. On Dec. 11, 2024, Panama and
Au", "api_data": null, "hint": null}, {"title": "Artemis Accords Reach Another Milestone with Portugal \u2013 SpacePolicyOnline.com", "url": "https://spacepolicyonline.com/news/artemis-accords-reach-
another-milestone-with-portugal/", "snippet": "Artemis Accords Reach Another Milestone with Portugal\nPortugal became the 60th country to join the Artemis Accords today. It\u2019s another milestone
for the U.S.-led principles for responsible behavior on the Moon. The Accords recently celebrated the fifth anniversary of when the first eight countries \u2014 Australia, Canada, Japan, Italy,
Luxembourg, the United Arab Emirates, the United Kingdom, and the United States \u2014 signed the non-binding principles in October 2020.\nPortugal\u2019s Secretary of State for", "api_data": null,
"hint": null}]}
```

## 💬 Response

Now I have the key data. Let me research the rate of new signatories and any upcoming signings.

## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__wikipedia


```json
{
  "query": "Artemis Accords new signatory 2026",
  "hours_back": 720,
  "n_articles": 10
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: Чудо под лунной пылью: как роботы помогут построить первую базу на южном полюсе Луны\n\nSummary: \nNASA
is preparing to construct the first permanent base on the Moon's south pole, driven by the presence of water ice in craters like Shackleton and Mons Mouton, which can be processed into drinking water
and rocket fuel. According to the article, the US Senate has approved a presidential order to accelerate the project, citing competition from China and Russia as a key motivator. To address the 14-day
lunar night where solar panels are ineffective, NASA is developing nuclear reactors to be launched by 2030, activated on Earth's orbit, and buried away from living zones. Autonomous robots are
scheduled to arrive first to clear abrasive lunar dust, stabilize the ground, and identify resources. The base design includes expandable modules protected by lunar soil against radiation and
micrometeorites, with operations governed by the Artemis Accords and the Outer Space Treaty to ensure transparency and equal access for all nations.\n\nPublished date: March 15 2026, 15:24\n\nURL:
https://www.newsinfo.ru/articles/lunar-base-plans-nasa-0kk/968873/\nSource: NewsInfo.Ru\nClassification: Science\nSentiment: positive\nReporting voice: Explanatory\nContinent: North
America\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: How Congress became NASA's partner for the Artemis return to the moon\n\nSummary: \nThe Senate Commerce Committee, chaired by Sen. Ted Cruz
(R-Texas), passed the NASA Reauthorization Act of 2026, a bill described as a stark departure from the 2010 NASA Authorization Act. Unlike the 2010 legislation, which the article claims was designed
to 'provide jobs in certain states' by mandating the expensive Space Launch System, the 2026 Act grants NASA Administrator Jared Isaacman 'carte blanche' to execute the Artemis program. The shift in
congressional approach is attributed to the advocacy of former Administrator Jim Bridenstine, who 'sold the Artemis return to the moon program... to both sides of the aisle,' and the geopolitical
urgency created by fears of a Chinese victory in a new space race, a theme established by former Administrator Bill Nelson. Under Isaacman's direction, the Artemis program has been revamped to include
an Earth orbital mission in 2027 and up to two moon landings in 2028. While the Space Launch System was not immediately cancelled, it is undergoing 'standardization' to reduce costs and increase
reliability. The article notes that the bill must still pass the full Senate and be reconciled with the House version before becoming law.\n\nPublished date: March 15 2026, 14:00\n\nURL:
https://thehill.com/opinion/5783365-congress-partners-nasa-artemis/\nSource: The Hill\nClassification: Politics\nSentiment: positive\nReporting voice: Analytical\nContinent: North
America\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle: SpaceX, Boeing, and Lockheed Will Take America Back to the Moon -- but Not Just Yet | The Motley Fool\n\nSummary: \nOn February 27, 2026, newly
appointed NASA Administrator Jared Isaacman announced a strategic shift to the Artemis program to accelerate the return to the Moon. While the Artemis II mission remains delayed until April to orbit
the Moon without landing, and the original Artemis III landing in 2028 was reclassified as a Low Earth Orbit (LEO) docking practice, the actual Moon landing is now scheduled for Artemis IV in 2028.
Isaacman aims to increase the launch cadence from once every three years to once every 10 months, potentially allowing for two Moon landings in 2028 with Artemis IV and Artemis V. To achieve this and
control costs, NASA will standardize the Space Launch System (SLS) rocket built by Boeing by replacing the 'Exploration Upper Stage' with the proven 'Centaur 5' second stage used by Lockheed Martin's
United Launch Alliance. This standardization targets reducing the per-launch cost of $4.1 billion, a move that could prevent Congress from canceling the SLS in favor of SpaceX's Starship or Blue
Origin's New Glen, thereby securing contracts for Boeing, Northrop Grumman, and Lockheed Martin.\n\nPublished date: March 15 2026, 09:25\n\nURL: https://www.fool.com/investing/2026/03/15/spacex-
boeing-lockheed-take-america-to-the-moon/\nSource: The Motley Fool\nClassification: Technology\nSentiment: positive\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation
key: [4]\nTitle: USA kämpfen mit Verzögerungen: Rennen zum Mond - China fasst bereits Landeplätze ins Auge\n\nSummary: \nA new space race is underway between the USA and China to reach the Moon,
driven by the potential extraction of valuable resources like water ice, rare earth elements, and Helium-3, despite the lack of a signed treaty regulating resource extraction. While China is targeting
the 'Rimae Bode' region on the Moon's near side for its first manned landing, citing its geological diversity and safety in a study published in 'Nature Astronomy' by scientists including Maosheng
Yang from the Chinese University of Geosciences in Wuhan, the USA's NASA is focusing on the lunar South Pole under its 'Artemis' program to establish a permanent presence using permanent sunlight and
shadowed craters for solar power and water ice. The US faces significant delays with its 'Artemis 2' mission, originally scheduled for February 7, 2026, which has been pushed to April due to a fuel
leak and helium flow issues with the Space Launch System (SLS) rocket. This mission, involving astronauts Reid Wiseman, Victor Glover, Christina Koch, and Jeremy Hansen, will last 10 days and test the
'Orion' capsule, which offers nearly 9 cubic meters of habitable volume—significantly more than the 6.2 cubic meters of the 'Apollo' capsules—despite the SLS having only half the payload capacity of
the historic Saturn V. China aims to land by 2030 using its 'Long March' rocket series, potentially threatening US dominance. The legal status of lunar mining remains contested, as neither the USA nor
China has signed the 1979 'Moon Agreement', though the 1967 'Outer Space Treaty' prohibits national appropriation of territory. Meanwhile, SpaceX's 'Starship' is being developed as a reusable
alternative, though it requires untested orbital refueling technology.\n\nPublished date: March 15 2026, 08:44\n\nURL: https://www.n-tv.de/wissen/Rennen-zum-Mond-China-fasst-bereits-Landeplaetze-ins-
Auge-id30451478.html\nSource: N-tv\nClassification: Science\nSentiment: neutral\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: Ay'ın güney
kutbundaki 'Mavi Altın'! NASA'nın 50 yıllık uykudan uyanma nedeni\n\nSummary: \nIn March 2026, NASA is preparing for the Artemis II mission, which will send four astronauts aboard the Orion spacecraft
on a 'figure-8' trajectory around the Moon, marking the first human return to lunar vicinity in 50 years since the final 1972 Apollo mission. Unlike the 1960s ideological space race, the Artemis
program aims to transform the Moon into a permanent human outpost and 'fuel station' by utilizing frozen water resources at the lunar south pole. According to the article, extracting oxygen and
hydrogen from this water will enable In-Situ Resource Utilization (ISRU), reducing the prohibitive cost of transporting supplies from Earth. The mission will also test human biological limits in deep
space, specifically examining how space radiation and microgravity affect immune systems and dormant viruses, using 'organ chips' to monitor cellular resilience. The article notes that while the Outer
Space Treaty leaves ownership boundaries ambiguous, a new 'astro-legal' doctrine based on 'de facto occupation' is being constructed, raising questions about the geopolitical and legal implications of
resource exploitation in the Moon's pristine craters.\n\nPublished date: March 14 2026, 23:14\n\nURL: https://www.turkiyegazetesi.com.tr/kose-yazilari/muzeyyen-biyik/ayin-guney-kutbundaki-mavi-altin-
nasanin-50-yillik-uykudan-uyanma-nedeni-1777046\nSource: Türkiye\nClassification: Science\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key:
[6]\nTitle: أول مرة منذ 50 عاما.. ناسا تستعد لإطلاق أول رحلة مأهولة إلى القمر بداية أبريل - اليوم السابع\n\nSummary: \nNASA has announced that the Artemis II mission, the first crewed flight to the
Moon in over 50 years, is targeted for launch on Wednesday, April 1, 2026, following a readiness review and green light to proceed. According to NASA, the first launch window opens on the evening of
April 1, with up to four opportunities available over a six-day period, contingent on orbital path constraints, operational factors, weather, and the Eastern Range schedule in Florida. The mission,
which carries four astronauts—Americans Reid Wiseman, Victor Glover, and Christina Koch, alongside Canadian Jeremy Hansen—will involve a 10-day test flight where the Orion spacecraft orbits Earth,
flies around the Moon without landing, and performs a water landing in the ocean. The mission aims to test critical systems for future lunar landings, following a schedule adjustment caused by helium
flow issues in the rocket's upper stage that required returning the vehicle to the Vertical Integration Building for further checks before returning to the launch pad. NASA emphasizes that Artemis II
is a critical test of the spacecraft, rocket, and support systems, serving as a direct step toward establishing a long-term human presence in the lunar environment.\n\nPublished date: March 14 2026,
19:02\n\nURL: https://www.youm7.com/story/2026/3/14/%D8%A3%D9%88%D9%84-%D9%85%D8%B1%D8%A9-%D9%85%D9%86%D8%B0-50-%D8%B9%D8%A7%D9%85%D8%A7-%D9%86%D8%A7%D8%B3%D8%A7-%D8%AA%D8%B3%D8%AA%D8%B9%D8%AF-
%D9%84%D8%A5%D8%B7%D9%84%D8%A7%D9%82-%D8%A3%D9%88%D9%84-%D8%B1%D8%AD%D9%84%D8%A9/7340482\nSource: اليوم السابع\nClassification: Science\nSentiment: positive\nReporting voice: Objective\nContinent:
North America\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: NASA: Astronauten sollen am 1. April zum Mond | Heute.at\n\nSummary: \nAccording to NASA, the Artemis-2 mission is scheduled to launch on
April 1, 2026, marking the first time humans will travel to the Moon since 1972. Following a technical issue identified during a dress rehearsal on Thursday, March 12, 2026, where a defective seal in
a quick-connect coupling caused helium tanking problems, the component was repaired, clearing the way for the launch. The Space Launch System (SLS) rocket is set to roll to the launch pad on the
upcoming Thursday. If the April 1 date is missed, five additional launch windows are available, with a potential alternative start date of April 30. The mission will carry NASA astronauts Reid
Wiseman, Victor Glover, and Christina Koch, along with Canadian astronaut Jeremy Hansen, aboard the Orion spacecraft. The crew will spend ten days in space, orbiting Earth before heading toward the
Moon. The journey to the Moon will take four days, during which the crew will orbit the lunar surface but will not land. A future landing is planned for 2028. The Artemis program was initiated during
the first term of US President Donald Trump with the goal of establishing a permanent human presence on the Moon and preparing for future Mars missions. The first unmanned Artemis mission successfully
orbited the Moon in the autumn of 2022.\n\nPublished date: March 14 2026, 16:52\n\nURL: https://www.heute.at/s/nasa-astronauten-sollen-am-1-april-zum-mond-120169452\nSource: Heute.at\nClassification:
Science\nSentiment: positive\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: Norge og Canada inngår avtale om romsamarbeid\n\nSummary: \nOn March
14, 2026, Norwegian Prime Minister Jonas Gahr Støre and Canadian Prime Minister Mark Carney met in Oslo to sign a new agreement on strategic cooperation, including collaboration in space, digital
sovereignty, and critical minerals. The agreement was announced during Carney's visit to Norway for the NATO exercise 'Cold Response'. Prime Minister Støre emphasized the importance of Norway having
multiple pillars of security, stating that 'we are stronger when we stand together with countries like Canada, with large economies, solid democracies, significant resources, and strong institutions.'
The space cooperation aims to secure the Arctic region, while Defense Minister Tore O. Sandvik noted that in a serious security situation, standing with allies strengthens defense capabilities. This
new agreement builds upon a 2023 military cooperation pact between the two nations. The partnership will be strengthened in areas including the Arctic, support for Ukraine, energy, economic security,
climate, critical minerals, spaceflight, and artificial intelligence.\n\nPublished date: March 14 2026, 15:05\n\nURL: https://www.aftenposten.no/norge/politikk/i/ArvXoz/norge-og-canada-inngaar-avtale-
om-romsamarbeid\nImage description: Two men, identified in the text as Jonas Gahr Støre and Mark Carney, are standing side-by-side waving to a crowd. They are outdoors in front of a modern building
with large glass windows. Both men are wearing dark winter jackets. In the foreground, the top of a person's head wearing a red, white, and blue striped beanie is visible.\nSource: Aftenposten
Interaktiv\nClassification: Politics\nSentiment: neutral\nReporting voice: Objective\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: Accords Maroc-UE: le Parlement européen, nouvel
acteur décisif?\n\nSummary: \nFollowing a promise made by Ursula von der Leyen to European parliamentarians in July 2024, the European Parliament (PE) has significantly expanded its political power
over EU external agreements through a new framework agreement adopted in Strasbourg in March 2026. According to the text, this institutional shift, described as a 'sensitive evolution,' grants the PE
three key prerogatives: first, it strictly limits the use of Article 122 of the Treaty (a 'crisis right' previously used to bypass the PE during the Covid-19 pandemic and the Ukraine energy crisis),
requiring the Commission to justify its exceptional use; second, it establishes an 'indirect right of initiative,' compelling the Commission to publicly justify any refusal to follow PE legislative
proposals; and third, and most notably, it mandates that the European Commission must consult the PE from the opening of negotiations with third countries and guarantee systematic access to all
working documents, including confidential ones. Bernd Lange, President of the International Trade (INTA) committee, stated this will allow parliamentarians to exercise 'real influence at every stage
of trade negotiations.' Although the Council of the EU, led by France and signed by the ambassadors of the 27 member states, opposed the text in an autumn letter, arguing it creates an
unconstitutional 'equality of treatment' between the PE and the Council and threatened legal action before the Court of Justice of the EU, the PE proceeded without a formal legal battle. The article
notes that this new dynamic will particularly impact the EU-Morocco accords, specifically regarding the fisheries partnership and the Polisario dossier, as the PE will now be able to influence the
political orientation and timing of agreements like the Mercosur deal, which was previously finalized as a 'fait accompli' by von der Leyen.\n\nPublished date: March 14 2026, 11:23\n\nURL:
https://fr.le360.ma/politique/accords-maroc-ue-le-parlement-europeen-nouvel-acteur-decisif_C4MQKQ5BMNHETGUTRDVOEW3MXA/\nSource: www.le360.ma\nClassification: Politics\nSentiment: neutral\nReporting
voice: Analytical\nContinent: Europe\n\n</doc>\n\n<doc>\nCitation key: [10]\nTitle: ¿Imaginas viajar a la Luna? Tu nombre puede ir al espacio con la misión Artemis II de la NASA\n\nSummary: \nIn 2026,
NASA will launch the Artemis II mission, the first crewed lunar flyby since the Apollo era, with four astronauts: Reid Wiseman (commander), Victor Glover, Christina Koch, and Jeremy Hansen. The Orion
spacecraft, powered by the Space Launch System rocket, will orbit the Moon and splash down in the Pacific Ocean. To engage the public, NASA launched an initiative allowing people worldwide to register
on the official NASA website to have their names stored digitally on the spacecraft as a symbolic journey. Participants will receive a personalized virtual boarding pass. Although no landing will
occur, the mission aims to test vital life support, navigation, and communication systems, as well as new scientific instruments required for future expeditions to the Moon and eventually
Mars.\n\nPublished date: March 14 2026, 07:52\n\nURL: https://www.larazon.es/ciencia/imaginas-viajar-luna-nombre-puede-espacio-mision-artemis-nasa-b50m_2026031469b5108bd489bf782e19a547.html\nSource:
La Razón\nClassification: Science\nSentiment: positive\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: A new lunar race has begun. Infrastructure
will decide who wins - opinion\n\nSummary: \nAccording to an opinion piece published in The Jerusalem Post on March 11, 2026, by Elon Musk's associate and CEO of Moonshot Space, a new 'lunar race' has
begun where infrastructure, not just exploration, will determine geopolitical winners. Between December 2025 and February 2026, a United States executive order reframed space as a pillar of national
security, and Elon Musk announced SpaceX's plan to build a self-growing city on the Moon. The article argues that the Moon is becoming strategic infrastructure extending Earth's economic and security
architecture, with projections reaching into the trillions of dollars. Key strategic values include the ability to produce fuel, oxygen, and energy on the lunar surface to reduce dependence on Earth.
The next layer of power involves data centers and AI training powered by continuous solar exposure. Governance is described as following capability, with two strategic blocs emerging: the United
States-led Artemis Accords (which Israel has joined) and the Sino-Russian International Lunar Research Station initiative. Israel's strategy focuses on technological ingenuity over scale, highlighted
by the company Helios, backed by the Israel Space Agency (ISA) and selected for the DARPA LunA 10 program, which has developed technology to extract oxygen from lunar soil. However, the article
identifies transport as the primary bottleneck, noting that traditional chemical rockets are mass-constrained. Consequently, Moonshot Space is developing a high-power electromagnetic launcher to
increase payload efficiency by replacing onboard fuel with ground-based electrical acceleration. The author urges Jerusalem to modernize civilian space legislation, articulate a national lunar
strategy, and leverage defense-derived expertise in AI and advanced propulsion to avoid strategic marginalization and remain an indispensable allied partner within frameworks like
Artemis.\n\nPublished date: March 11 2026, 05:48\n\nURL: https://www.jpost.com/defense-and-tech/article-889549\nSource: The Jerusalem Post\nClassification: Politics\nSentiment: neutral\nReporting
voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: Returning to the Moon, this time to stay\n\nSummary: \nAs of March 4, 2026, NASA is preparing for the Artemis
II mission, a pivotal crewed lunar flight scheduled to launch in early April 2026 after being delayed from January 2026 due to a North American winter storm, hydrogen leaks, and helium flow issues.
According to Administrator Jared Isaacman, the mission aims to validate human-rated deep-space systems for the first time since Apollo 17 in 1972. The Artemis program, initiated in 2017, involves
international partners including Canada, Japan, the UAE, and Europe, and relies on the Space Launch System (SLS) and Orion capsule, with SpaceX and Blue Origin contracted to provide the Human Landing
System. Artemis II will serve as a critical test for the lunar orbit Gateway and future Mars missions, with safety protocols including a 'free return trajectory' ensuring crew return in case of major
failure. A successful mission is expected to reshape the risk profile for Artemis III and subsequent landings, supported by a $9.995 billion appropriation voted in July 2025, valid until September 30,
2032. Beyond NASA, the mission's success will strengthen the business case for commercial deep-space services and validate the Artemis Accords, a set of non-binding agreements signed by 61 countries
as of early 2026 to govern peaceful lunar exploration. The Moon Village Association, founded in 2017 in Vienna, continues to foster international collaboration through the UN Committee on the Peaceful
Uses of Outer Space (COPUOS), which has over 100 member countries, and the Action Team on Lunar Activities Consultation (ATLAC), operational since 2025. The ultimate goal is a sustainable, commercial,
and international presence on the Moon, with the 10th Global Moon Village Workshop scheduled for 2026 in Thailand.\n\nPublished date: March 04 2026, 14:15\n\nURL:
https://www.innovationnewsnetwork.com/artemis-ii-mission-sets-stage-for-lunar-return-beyond/67267/\nSource: Innovation News Network\nClassification: Science\nSentiment: positive\nReporting voice:
Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [13]\nTitle: Artemis, Chang'e, Chandrayaan... en quoi la course à la Lune des années 2020 diffère de celle des années
1960\n\nSummary: \nThe 2020s lunar race differs significantly from the 1960s Cold War era through a shift to a North-South geopolitical axis and new legal frameworks. In 2026, the NASA-led Artemis 2
mission is scheduled to launch, carrying four astronauts to fly around the Moon; this follows the 2017 inception of the Artemis program. Concurrently, China plans to launch the robotic Chang'e 7
mission to the lunar south pole by late 2026, while India aims to land Chandrayaan-4 in 2027. The international landscape has expanded beyond the two superpowers of the 1960s (USSR and USA) to include
the China-Russia International Lunar Research Station (ILRS), the European Space Agency (ESA) with its Argonaut lander targeting 2030, Japan (including startup ispace), and various nations like the
UAE and Pakistan participating in specific missions. \n\nA major shift involves the disruption of space law: the US Space Act of 2015 and the Artemis Accords (sections 10 and 11) assert the right to
appropriate space resources and establish 'safety zones' around installations, challenging the 1967 Outer Space Treaty's principle of non-appropriation. Over 50 states have signed the Artemis Accords,
though their legal status as a multilateral treaty is debated. Financially, the Artemis program is estimated to cost at least $93 billion (approx. €78.6 billion) by 2025, with a single launch costing
$4 billion (€3.3 billion), raising concerns about budgetary stability and environmental impact amidst climate change. The article notes that while the US and its partners cooperate with Europe and
Japan, the ILRS coalition includes nations such as Venezuela, South Africa, and Egypt, reflecting a new global geopolitical dynamic.\n\nPublished date: March 04 2026, 08:14\n\nURL:
http://theconversation.com/artemis-change-chandrayaan-en-quoi-la-course-a-la-lune-des-annees-2020-differe-de-celle-des-annees-1960-276469\nSource: The Conversation\nClassification: Science\nSentiment:
neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [14]\nTitle: NASA wraca do wyścigu o Księżyc. Trump chce zostać prezydentem od lądowania\n\nSummary:
\nAccording to a report published by Business Insider on March 03, 2026, NASA is accelerating the Artemis program under the leadership of Administrator Jared Isaacman, who was sworn in in December
2024, following a period of 'decision paralysis' that lasted from late 2022 to late 2025. The primary goal is to land humans on the Moon by 2028, within the second term of President Donald Trump, who
views the program as a political priority to be remembered as the president who returned humans to the Moon. \n\nKey milestones include: Artemis II, a crewed orbital flight with a four-person crew, is
scheduled to launch in early April 2026 (previously delayed from February due to a helium leak); Artemis III is planned for mid-2027 as a risk-reduction test; and Artemis IV and V are targeted for
2028 to achieve the first crewed landings. This timeline aims to complete four missions before Trump's term ends in January 2029.\n\nThe Artemis program was originally established by Space Policy
Directive-1 signed by Trump on December 11, 2017, which directed NASA to return to the Moon. However, the program faced significant delays due to costs exceeding $40 billion, the high complexity of
the Space Launch System (SLS) and Orion capsule, and delays in the Human Landing System (HLS) provided by SpaceX and the new xEMU spacesuits, which were not fully tested by 2025. The Artemis Accords,
signed by over 50 countries in 2020, aim to establish international norms for lunar exploration.\n\nThe article highlights a geopolitical race against China, which plans a crewed landing around 2030.
While Isaacman emphasizes safety and learning from errors, the article notes the historical risk of political pressure leading to disasters, citing two Space Shuttle and one Apollo catastrophe. The
narrative suggests that if NASA succeeds, it will be a triumph of public-private cooperation (involving SpaceX, Blue Origin, Boeing, and Lockheed Martin), but a failure due to rushing could result in
significant human and political costs.\n\nPublished date: March 03 2026, 05:56\n\nURL: https://businessinsider.com.pl/technologie/nowe-technologie/czlowiek-na-ksiezycu-za-prezydentury-trumpa-ambitny-
plan-nasa/cy2g9bz\nSource: Business Insider\nClassification: Science\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Japan
aims to draw up international recommendation to curb space debris near Moon\n\nSummary: \nJapan is leading efforts to develop an international recommendation to mitigate space debris around the Moon,
ahead of a potential escalation in lunar activity. The Japanese government, in collaboration with its space agency and private companies, is drafting a non-binding proposal to be presented to the 60
signatories of the Artemis Accords, possibly in autumn 2026. The draft calls for designing satellites with post-mission de-orbiting systems, avoiding the discarding of parts in space, selecting
disposal locations carefully, and planning for the controlled disposal of landing craft and rovers on the lunar surface. This initiative arises as lunar exploration intensifies, despite the current
low level of debris in lunar orbit—unlike Earth, where over 1.2 million debris pieces of at least 1cm in size already threaten active satellites and space stations. The Moon’s lack of atmosphere
prevents atmospheric re-entry as a disposal method, making debris removal extremely difficult due to the 380,000km distance and absence of infrastructure. Japan aims to establish sustainable space
practices through the Artemis missions, which seek to enable a long-term human presence on the Moon by the 2030s.\n\nPublished date: February 26 2026, 15:23\n\nURL:
https://www.straitstimes.com/asia/east-asia/japan-aims-to-draw-up-intl-recommendation-to-curb-space-debris-near-moon\nSource: The Straits Times\nClassification: Science\nSentiment: positive\nReporting
voice: Explanatory\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [16]\nTitle: 【独自】月の宇宙ごみ防止へ国際勧告　日本主導で準備、今秋決定目指し\n\nSummary: \nJapan is leading the preparation of an international recommendation
aimed at preventing space debris in lunar orbit, as countries increasingly pursue lunar exploration. According to sources including the Japan Aerospace Exploration Agency (JAXA), the recommendation,
which will be based on design and operational guidelines such as deorbiting satellites after mission completion, is being developed to prevent hazardous debris in the Moon’s vicinity. The draft
proposal urges avoiding the disposal of parts or equipment in space and promoting deorbiting capabilities. With only about 20 known defunct satellites currently in lunar orbit—compared to over 1.2
million pieces of debris larger than 1 cm in Earth’s orbit—the Japanese government recognizes the need for international cooperation to prevent a future crisis. The recommendation is targeted for
adoption by the signatories of the U.S.-led political declaration, the Artemis Accords, by autumn 2026. The Moon’s remote location—380,000 km from Earth and lacking infrastructure—makes debris removal
extremely difficult, reinforcing the importance of proactive prevention.\n\nPublished date: February 26 2026, 11:17\n\nURL: https://www.kobe-
np.co.jp/news/zenkoku/compact/202602/0020065091.shtml\nSource: 神戸新聞\nClassification: Science\nSentiment: positive\nReporting voice: Explanatory\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key:
[17]\nTitle: Portugal e os Acordos Artemis: oportunidade histórica ou desejo de pertença? Algumas notas sobre o futuro da exploração espacial\n\nSummary: \nPortugal signed the Artemis Accords on
January 12, 2026, during the 52nd meeting of the Portugal-United States Permanent Bilateral Commission, joining 59 other countries in this non-binding framework promoted by the U.S. NASA to guide
civil space activities. The Accords aim to establish principles for cooperation in space, including transparency, emergency assistance, and the protection of space heritage—such as lunar landing sites
and artifacts—while promoting peaceful, international collaboration. However, the Accords are politically driven and aligned with U.S. foreign policy, requiring signatories to negotiate bilateral
agreements with the U.S., despite affirming compliance with international law. Controversial elements include the concept of 'safety zones' around active sites, which lack defined duration or size,
potentially enabling de facto exclusions that could conflict with the Outer Space Treaty (OST) of 1967, which prohibits national appropriation of celestial bodies and ensures free access. The Accords
also address space resources, stating that extraction does not constitute national appropriation, a stance supported by U.S. law and adopted by Luxembourg, the UAE, Japan, and Brazil, though no global
consensus exists. China and Russia have criticized the Accords as a U.S.-led effort to shape international space norms, especially as they exclude major space-faring nations. The European Union and
ESA remain divided, with member states like Portugal, Germany, France, and Italy joining the Accords unilaterally, undermining coordinated European space policy. The lack of EU-wide coordination
weakens multilateralism and risks fragmenting global space governance, as alternative initiatives like the China-Russia-led Lunar Research Station Partnership (17 countries, 50 institutions) emerge.
The article questions whether Portugal’s adherence reflects a strategic opportunity or a symbolic gesture in a fragmented, bloc-based space order, highlighting the tension between national ambition
and global cooperation in space exploration.\n\nPublished date: February 25 2026, 21:35\n\nURL: https://expresso.pt/opiniao/2026-02-25-portugal-e-os-acordos-artemis-oportunidade-historica-ou-desejo-
de-pertenca--algumas-notas-sobre-o-futuro-da-exploracao-espacial-06b130d5\nSource: Jornal Expresso\nClassification: Politics\nSentiment: neutral\nReporting voice: Analytical\nContinent:
Europe\n\n</doc>\n\n<doc>\nCitation key: [18]\nTitle: U.S.-India 'Breakthrough' Interim Pact Boosts Defense & Space Ties, NASA-ISRO NISAR, Artemis Deal Elevated\n\nSummary: \nThe interim Indo-U.S.
Trade Agreement signed on February 6, 2026, marks a significant revival in the deepening defense and space partnership between India and the United States, despite prior setbacks. The U.S. has praised
India’s military performance during Operation Sindoor, with Admiral Samuel J. Paparo, Commander of Indo-Pacific Command, lauding the tactical execution and stating the U.S.-India defense relationship
is on a 'steeply upward trajectory.' The U.S.-India Space Business Forum, hosted in Bengaluru on February 10–11 by the U.S. Consulate General Chennai with support from the U.S.-India Strategic
Partnership Forum (USISPF), brought together 23 executives from 14 American space companies and over 200 participants from both nations, marking the first U.S. space-focused trade mission to India and
reinforcing U.S. leadership in commercial space innovation. Key areas of cooperation include joint monitoring of space assets, Indian participation in U.S. Space Command’s Global Sentinel exercise,
Indian astronaut training at NASA, and the Axiom Space Ax-4 mission. The U.S.-India Defense Acceleration Ecosystem (INDUS-X) supports Indian startups in satellite reconnaissance and secure
communications, with seven selected in 2025. Strategic agreements such as BECA, COMCASA, and the Space Situational Awareness (SSA) Agreement enable high-end data sharing and secure communications. The
NASA-ISRO NISAR mission provides advanced Earth observation data for civilian and security use. India’s ratification of the Artemis Accords in 2023 signaled a shift from multilateral frameworks, and
the launch of the U.S.-India iCET initiative—renamed TRUST in 2025—expanded cooperation in AI, semiconductors, and critical minerals, including the establishment of India’s first national security-
focused semiconductor fab in Kolkata. Despite this convergence, India maintains strategic autonomy, abstaining from U.S.-led UN resolutions on ASAT testing and responsible space behavior due to
concerns over exclusionary norm-making. India retains STA-1 status but still faces hurdles under U.S. ITAR and EAR regulations. Experts, including Dimitrios Stroikos of LSE IDEAS, note India’s
selective engagement and normative ambivalence in space governance, indicating alignment on operational levels but cautious posture on global governance frameworks.\n\nPublished date: February 19
2026, 04:08\n\nURL: https://www.eurasiantimes.com/u-s-india-breakthrough-interim-trade-pact/\nSource: Latest Asian, Middle-East, EurAsian, Indian News\nClassification: Politics\nSentiment:
positive\nReporting voice: Analytical\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [19]\nTitle: Artemis 2 y el \"salto lunar\" de Milei: las claves para entender la misión que puede abrir
mercados para Argentina - El Cronista\n\nSummary: \nThe Artemis II mission by NASA marks the beginning of a new era in crewed space exploration and represents the critical first step toward
establishing a permanent human presence on the Moon. President Javier Milei has operationalized the Artemis Accords as a cornerstone of Argentina's foreign policy. Argentina, which joined the Artemis
Accords in 2023 under former President Alberto Fernández and Foreign Minister Santiago Cafiero during a ceremony at the Casa Rosada with NASA Administrator Bill Nelson, is the 28th country to sign the
agreement. The Artemis Accords, launched on October 13, 2020, are based on the 1967 Outer Space Treaty and promote safe, sustainable space exploration. Argentina’s participation is channeled through
CONAE (National Space Activities Commission) and a network of technology-based companies. The country contributes specialized capabilities in areas where it has international competitiveness, enabling
Argentine 'New Space' firms to validate their processes under NASA standards, facilitating high-value technological exports. Artemis II, scheduled for launch no earlier than March 2026 from Kennedy
Space Center, will carry four astronauts—Reid Wiseman, Victor Glover, Christina Koch, and Jeremy Hansen—on the Orion capsule. The 10-day mission will orbit the Moon, reaching a record distance of
72,000 kilometers beyond it, to test life support and navigation systems ahead of the Artemis III lunar landing. Argentina will contribute the Atenea microsatellite, developed by CONAE, VENG S.A., the
Argentine Institute of Radioastronomy (IAR), the National Atomic Energy Commission (CNEA), and national universities. The satellite will deploy during the mission’s first phase, over 70,000 kilometers
from Earth, setting a record for an Argentine satellite. The mission opens three key opportunities: technological validation, international visibility, and economic leverage for Argentine industry.
However, despite the government’s promotional efforts, Argentina’s scientific community faces a severe transition. The 2026 budget approved by Congress shows a cumulative real-term decline of 46.4% in
science and technology funding since 2023, reducing investment to just 0.149% of GDP—far below the 0.52% target set by law. CONAE has suffered a real-term cut of nearly 59%, prompting staff to declare
'alert and mobilization' status over what they describe as a 'severe adjustment' under Milei’s administration. This has led to the suspension of flagship projects, including the Tronador II rocket,
SAOCOM 2, and the Sabia-Mar oceanographic satellite, which is now being maintained with minimal funding and is scheduled for launch in the first half of 2026. The Artemis II mission thus serves as a
symbolic platform for Milei’s vision of a modern, technologically advanced Argentina, with success measured not only by space achievements but also by the government’s ability to translate prestige
into contracts and investments. NASA also offers a public engagement initiative allowing anyone to submit their name to a USB drive traveling aboard Orion, creating a symbolic connection between
humanity and the mission.\n\nPublished date: February 17 2026, 14:14\n\nURL: https://www.cronista.com/economia-politica/artemis-2-y-el-salto-lunar-de-milei-las-claves-para-entender-la-mision-que-
puede-abrir-mercados-para-argentina/\nSource: El Cronista\nClassification: Science\nSentiment: neutral\nReporting voice: Analytical\nContinent: South America\n\n</doc>\n\n<doc>\nCitation key:
[20]\nTitle: ¿Por qué los humanos no han vuelto a la Luna en más de 50 años? - WTOP News\n\nSummary: \nSince the final Apollo 17 mission on December 14, 1972, no human has returned to the Moon,
despite ongoing efforts. The primary reason, according to Teasel Muir-Harmony, a Smithsonian National Air and Space Museum curator, is the lack of sustained political will: space programs require
long-term national commitment, but shifting presidential administrations have repeatedly changed priorities. Les Johnson, former NASA chief technologist, confirmed that goals for human spaceflight
have been altered every four to eight years—such as when George H.W. Bush ordered a return to the Moon, only for Clinton to cancel it, followed by George W. Bush restarting the effort, then Obama
shifting focus to asteroid sampling, and Trump re-centering on lunar missions. Joe Biden maintained continuity by supporting the Artemis program, and the current Trump administration has intensified
efforts to surpass China in a new space race. Technically, the Artemis program represents a major leap over Apollo: Orion’s computers are 20,000 times faster and have 128,000 times more memory than
Apollo’s; Orion offers more space, improved life support, and a real bathroom—unlike Apollo’s plastic bag waste system. Artemis aims not just to land humans but to establish a sustainable lunar
presence through infrastructure like habitats and long-duration stays. The program benefits from decades of experience, including the International Space Station’s 25+ years of human presence, robotic
missions like NASA’s Lunar Reconnaissance Orbiter, and advances in commercial spaceflight (e.g., SpaceX, Blue Origin). The Artemis Accords, signed by over 60 countries, promote peaceful, sustainable
lunar exploration based on the 1967 Outer Space Treaty, though some analysts argue they may conflict with its principles by allowing commercial mining. China, not a signatory, plans its own crewed
lunar landing by 2030. Despite the challenges, Artemis II—scheduled for March 2026—will mark the first human journey near the Moon since Apollo 17. The mission’s success hinges on political
continuity, technological maturity, and international cooperation. As John Young, Apollo 16 commander, once said, 'The geological history of Earth clearly shows that species on a single planet do not
endure,' underscoring the long-term strategic value of lunar exploration.\n\nPublished date: February 14 2026, 13:47\n\nURL: https://wtop.com/news/2026/02/por-que-los-humanos-no-han-vuelto-a-la-luna-
en-mas-de-50-anos/\nSource: WTOP\nClassification: Science\nSentiment: positive\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n------News Summaries
End------\n","offset":10,"hit_cache":false}
```

```json
{
  "query": "Artemis Accords new signatory February March 2026"
}
```

### 📋 Result

```
{"query": "Artemis Accords new signatory February March 2026", "results": [{"title": "Artemis Accords - NASA", "url": "https://www.nasa.gov/artemis-accords/", "snippet": "Principles for a Safe,
Peaceful, and Prosperous Future in Space\nNASA, in coordination with the U.S. Department of State and seven other initial signatory nations, established the Artemis Accords in 2020. With many
countries and private companies conducting missions and operations around the Moon, the Artemis Accords provide a common set of principles to enhance the governance of the civil exploration and use of
outer space.\nThe Artemis Accords reinforce the commitment by signatory nations to the", "api_data": null, "hint": null}, {"title": "Artemis Accords - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Artemis_Accords", "snippet": "The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world governments
that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the ultimate goal
of expanding space exploration to Mars and beyond.\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe,", "api_data": {"content": [{"type":
"text", "text": "{\"title\": \"Artemis Accords\", \"url\": \"https://en.wikipedia.org/wiki/Artemis_Accords\", \"extract\": \"The Artemis Accords are a set of non-binding multilateral arrangements
between the United States government and other world governments that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led
effort to return humans to the Moon by 2027, with the ultimate goal of expanding space exploration to Mars and beyond.\\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the
Accords, including 28 in Europe, 15 in Asia, seven in South America, five in North America, four in Africa, and two in Oceania.\\nDrafted by NASA and the U.S. Department of State, the Accords
establish a framework for cooperation in the civil exploration and peaceful use of the Moon, Mars, and other astronomical objects. They are explicitly grounded in the United Nations Outer Space Treaty
of 1967, which signatories are obliged to uphold, and cite most major U.N.-brokered conventions constituting space law.\\nThe Accords were originally signed on 13 October 2020 by representatives of
the national space agencies of eight countries: Australia, Canada, Italy, Japan, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States. The Accords remain open for signature
indefinitely, as NASA anticipates more nations joining. Additional signatories can choose to directly participate in Artemis program activities, or may agree simply to commit to the principles for
responsible exploration of the Moon as set out in the Accords.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Artemis Accords | NASA, United States, Outer Space Treaty, Criticism, Summary,
Russia, & China | Britannica", "url": "https://www.britannica.com/topic/Artemis-Accords", "snippet": "[Artemis Accords](https://cdn.britannica.com/28/283728-050-7CCE29BC/Signing-Ceremony-Artemis-
Accords-At-NASA-Headquarters-2024.jpg)Representatives from Uruguay signing the Artemis Accords, making Uruguay the 36th country to sign the accords.\nArtemis Accords\nWhat are the Artemis
Accords?\nWhich countries were the initial signatories of the Artemis Accords?\nWhat are the stated objectives of the Artemis Accords?\nWhy did Russia and China not sign the Artemis Accords?\nArtemis
Accords, set of principle", "api_data": null, "hint": null}, {"title": "US Artemis Accords Hit 50 Signatories in 2024 - AIP.ORG", "url": "https://www.aip.org/fyi/us-artemis-accords-hit-50-signatories-
in-2024", "snippet": "US Artemis Accords Hit 50 Signatories in 2024\n![A NASA graphic showing the flags of the first 48 nations to sign on to the Artemis
Accords.](https://aip.brightspotcdn.com/dims4/default/bac391f/2147483647/strip/true/crop/4000x2250+0+0/resize/820x461!/quality/90/?url=https%3A%2F%2Fk1-prod-aip.s3.us-
east-2.amazonaws.com%2Fbrightspot%2F6e%2Fa3%2F2b796c474f51a15f51699f88712d%2Fartemis-accords-austria-50-121124.png)\nThe flags of the first 48 Artemis Accords signatories. On Dec. 11, 2024, Panama and
Au", "api_data": null, "hint": null}, {"title": "Portugal signs the Artemis Accords - SpaceNews", "url": "https://spacenews.com/portugal-signs-the-artemis-accords/", "snippet": "WASHINGTON \u2014
Portugal has become the latest country to sign the Artemis Accords outlining best practices for responsible space exploration, beating out another European country to be the 60th to join.\nHelena
Canh\u00e3o, Portugal\u2019s state secretary for science and innovation, signed the Artemis Accords Jan. 11 on behalf of the government, with an event held in Lisbon Jan. 12 to formally announce the
signing as part of broader discussions between the governments of the United States and Portugal.\n\u201c2026", "api_data": null, "hint": null}, {"title": "Artemis Accords - United States Department
of State", "url": "https://www.state.gov/bureau-of-oceans-and-international-environmental-and-scientific-affairs/artemis-accords", "snippet": "Official websites use .gov\nA .gov website belongs to an
official government organization in the United States.Secure .gov websites use HTTPS\nA lock ( ) or https:// means you\u2019ve safely connected to the .gov website. Share sensitive information only on
official, secure websites.Americans in the Middle East:\nFor consular information or assistance, call the Department of State\u2019s 24/7 Task Force at +1-202-501-4444 (from abroad) and 1-888-407-4747
(from the U.S. and Canada).", "api_data": null, "hint": null}, {"title": "Artemis Accords | Current Affairs", "url": "https://www.shankariasparliament.com/current-affairs/artemis-accords", "snippet":
"Prelims \u2013 Current events of national and international importance.\nMains (GS III) \u2013 Awareness in the fields of IT, Space, Computers, robotics, nano-technology, bio-technology and issues
relating to intellectual property rights.\nBangladesh recently became the 54th nation to sign the Artemis Accords.\nNASA's Artemis Program aims to return humans to the Moon and Mars.\nCore Principles
of the Accord\nSignificance", "api_data": null, "hint": null}, {"title": "Gold: With 52 Members, Artemis Accords Now Represent Global Consensus \u2013 SpacePolicyOnline.com", "url":
"https://spacepolicyonline.com/news/gold-with-52-members-artemis-accords-now-represent-global-consensus/", "snippet": "Gold: With 52 Members, Artemis Accords Now Represent Global Consensus\nThailand
and Liechtenstein just joined the Artemis Accords, bringing the number of signatories to 52. Mike Gold, who was instrumental in creating the Accords, considers that a significant milestone because it
is half the membership of the U.N. Committee on Peaceful Uses of Outer Space. The Accords now constitute a \u201ctrue global consensus\u201d on principles for responsible behavior on the Moon.\nThe
Artemis Accords are named for the ", "api_data": null, "hint": null}, {"title": "Artemis Accords: What are they & which countries are involved? | Space", "url": "https://www.space.com/artemis-accords-
explained", "snippet": "The Artemis Accords lay out the framework for collaborating nations as we enter the next era of lunar exploration and beyond.\nThe next era of space exploration is underway
with the Artemis program aiming to send the first woman and person of color to the lunar surface before targeting a crewed mission to Mars. The Artemis accords lay out a framework for nations
collaborating in this exciting endeavor.(Image credit: NASA)\nBreaking space news, the latest updates on rocket launches, skywatching eve", "api_data": null, "hint": null}, {"title": "Why are the
Artemis Accords important?", "url": "https://plants4space.com/posts/why-are-the-artemis-accords-important", "snippet": "Why are the Artemis Accords important?\nThe Artemis Accords are of importance
for Australia as they were one of the original seven signatories alongside the United States in 2020. The Australian Space Agency highlights that Australia\u2019s support of the Accords aligns with
their aim to support \u201cthe development of rules, norms and principles for the safe, stable and sustainable use and exploration of outer space.\u201d The aim of the Artemis Accords to facilitate a
sustainable human presence in, and use o", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Artemis Accords",
  "mode": "full",
  "prompt": "List all signatories with dates they signed. How many total signatories as of the most recent update? What was the rate of new signatories in 2024 and 2025?"
}
```

### 📋 Result

```
{"title": "Artemis Accords", "url": "https://en.wikipedia.org/wiki/Artemis_Accords", "extract": "Based on the provided content:\n\n**Signatories with dates:**\n- **13 October 2020**: Australia,
Canada, Italy, Japan, Luxembourg, United Arab Emirates, United Kingdom, United States (original 8 signatories)\n- **26 January 2026**: Oman (most recent mentioned)\n\n**Total signatories:** 61
countries as of 26 January 2026\n\n**Rate of new signatories in 2024 and 2025:** This information is not provided in the content. The text only mentions the original 8 signatories from October 2020
and states there are 61 total as of January 2026, but does not break down the signing dates or annual rates for 2024-2025.\n\n**Regional breakdown (as of January 2026):**\n- Europe: 28\n- Asia: 15\n-
South America: 7\n- North America: 5\n- Africa: 4\n- Oceania: 2\n\n**Relevant links:**\nThe provided text content does not contain any hyperlinks to list.", "mode": "full"}
```

## 💬 Response

Let me get the detailed signing timeline to understand the rate of new signatories.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Artemis Accords signatories list by date 2024 2025 2026 timeline"
}
```

### 📋 Result

```
{"query": "Artemis Accords signatories list by date 2024 2025 2026 timeline", "results": [{"title": "Artemis Accords - Wikipedia", "url": "https://en.wikipedia.org/wiki/Artemis_Accords", "snippet":
"The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world governments that elaborates on the norms expected to be followed in outer
space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the ultimate goal of expanding space exploration to Mars and beyond.\nAs of 26
January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe,", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Artemis Accords\", \"url\":
\"https://en.wikipedia.org/wiki/Artemis_Accords\", \"extract\": \"The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world
governments that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the
ultimate goal of expanding space exploration to Mars and beyond.\\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe, 15 in Asia, seven in
South America, five in North America, four in Africa, and two in Oceania.\\nDrafted by NASA and the U.S. Department of State, the Accords establish a framework for cooperation in the civil exploration
and peaceful use of the Moon, Mars, and other astronomical objects. They are explicitly grounded in the United Nations Outer Space Treaty of 1967, which signatories are obliged to uphold, and cite
most major U.N.-brokered conventions constituting space law.\\nThe Accords were originally signed on 13 October 2020 by representatives of the national space agencies of eight countries: Australia,
Canada, Italy, Japan, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States. The Accords remain open for signature indefinitely, as NASA anticipates more nations joining.
Additional signatories can choose to directly participate in Artemis program activities, or may agree simply to commit to the principles for responsible exploration of the Moon as set out in the
Accords.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "US Artemis Accords Hit 50 Signatories in 2024 - AIP.ORG", "url": "https://www.aip.org/fyi/us-artemis-accords-hit-50-signatories-in-2024",
"snippet": "US Artemis Accords Hit 50 Signatories in 2024\n![A NASA graphic showing the flags of the first 48 nations to sign on to the Artemis
Accords.](https://aip.brightspotcdn.com/dims4/default/bac391f/2147483647/strip/true/crop/4000x2250+0+0/resize/820x461!/quality/90/?url=https%3A%2F%2Fk1-prod-aip.s3.us-
east-2.amazonaws.com%2Fbrightspot%2F6e%2Fa3%2F2b796c474f51a15f51699f88712d%2Fartemis-accords-austria-50-121124.png)\nThe flags of the first 48 Artemis Accords signatories. On Dec. 11, 2024, Panama and
Au", "api_data": null, "hint": null}, {"title": "Artemis Accords - NASA", "url": "https://www.nasa.gov/artemis-accords/", "snippet": "Principles for a Safe, Peaceful, and Prosperous Future in
Space\nNASA, in coordination with the U.S. Department of State and seven other initial signatory nations, established the Artemis Accords in 2020. With many countries and private companies conducting
missions and operations around the Moon, the Artemis Accords provide a common set of principles to enhance the governance of the civil exploration and use of outer space.\nThe Artemis Accords
reinforce the commitment by signatory nations to the", "api_data": null, "hint": null}, {"title": "Artemis Accords - United States Department of State", "url": "https://www.state.gov/bureau-of-oceans-
and-international-environmental-and-scientific-affairs/artemis-accords", "snippet": "Official websites use .gov\nA .gov website belongs to an official government organization in the United
States.Secure .gov websites use HTTPS\nA lock ( ) or https:// means you\u2019ve safely connected to the .gov website. Share sensitive information only on official, secure websites.Americans in the
Middle East:\nFor consular information or assistance, call the Department of State\u2019s 24/7 Task Force at +1-202-501-4444 (from abroad) and 1-888-407-4747 (from the U.S. and Canada).", "api_data":
null, "hint": null}, {"title": "The Artemis Accords By the Numbers", "url": "https://payloadspace.com/the-artemis-accords-by-the-numbers/", "snippet": "This article was updated Jan. 27 to reflect
Oman\u2019s addition to the Accords.\nOman announced this week that it had signed on to the Artemis Accords, becoming the 61st nation to agree to the set of non-binding principles.\nA quick reminder:
The US led the establishment of the Artemis Accords in 2020. Nations who sign on commit to exploring space in a peaceful, transparent, and sustainable way.\nThe accords celebrated their fifth
anniversary in October. As such, here\u2019s a roundup of where they stand.\nG", "api_data": null, "hint": null}, {"title": "Artemis Accords: What are they & which countries are involved? | Space",
"url": "https://www.space.com/artemis-accords-explained", "snippet": "The Artemis Accords lay out the framework for collaborating nations as we enter the next era of lunar exploration and beyond.\nThe
next era of space exploration is underway with the Artemis program aiming to send the first woman and person of color to the lunar surface before targeting a crewed mission to Mars. The Artemis
accords lay out a framework for nations collaborating in this exciting endeavor.(Image credit: NASA)\nBreaking space news, the latest updates on rocket launches, skywatching eve", "api_data": null,
"hint": null}, {"title": "Gold: With 52 Members, Artemis Accords Now Represent Global Consensus \u2013 SpacePolicyOnline.com", "url": "https://spacepolicyonline.com/news/gold-with-52-members-artemis-
accords-now-represent-global-consensus/", "snippet": "Gold: With 52 Members, Artemis Accords Now Represent Global Consensus\nThailand and Liechtenstein just joined the Artemis Accords, bringing the
number of signatories to 52. Mike Gold, who was instrumental in creating the Accords, considers that a significant milestone because it is half the membership of the U.N. Committee on Peaceful Uses of
Outer Space. The Accords now constitute a \u201ctrue global consensus\u201d on principles for responsible behavior on the Moon.\nThe Artemis Accords are named for the ", "api_data": null, "hint":
null}, {"title": "A/AC.105/C.1/2025/CRP.16/Rev.1 - An update on the work of the Artemis Accords Signatories: Conference room paper by Australia, the Kingdom of Bahrain, Canada, Ecuador, Germany,
Italy, Japan, Luxembourg, Mexico, Slovenia, Spain, the United Arab Emirates, the United Kingdom of Great Britain and Northern Ireland and the United States of America", "url":
"https://www.unoosa.org/oosa/en/oosadoc/data/documents/2025/aac.105c.12025crp/aac.105c.12025crp.16rev.1_0.html", "snippet": "| Symbol | A/AC.105/C.1/2025/CRP.16/Rev.1 |\n| Title | An update on the
work of the Artemis Accords Signatories |\n| Subtitle | Conference room paper by Australia, the Kingdom of Bahrain, Canada, Ecuador, Germany, Italy, Japan, Luxembourg, Mexico, Slovenia, Spain, the
United Arab Emirates, the United Kingdom of Great Britain and Northern Ireland and the United States of America |\n| Year | 2025 |\n| Series | A/AC.105/C.1/2025/CRP. |\n| Date of issue | 2025-02-11
|\n| Session | Sixty-second session |\n|", "api_data": null, "hint": null}, {"title": "Artemis Accords | Current Affairs", "url": "https://www.shankariasparliament.com/current-affairs/artemis-
accords", "snippet": "Prelims \u2013 Current events of national and international importance.\nMains (GS III) \u2013 Awareness in the fields of IT, Space, Computers, robotics, nano-technology, bio-
technology and issues relating to intellectual property rights.\nBangladesh recently became the 54th nation to sign the Artemis Accords.\nNASA's Artemis Program aims to return humans to the Moon and
Mars.\nCore Principles of the Accord\nSignificance", "api_data": null, "hint": null}, {"title": "NASA, Artemis Accords Signatories Progress on Sustainable Exploration - U.S. Embassy in Peru", "url":
"https://pe.usembassy.gov/nasa-artemis-accords-signatories-progress-on-sustainable-exploration/", "snippet": "![](https://pe.usembassy.gov/wp-
content/uploads/sites/74/2024/11/Artemis.jpg)\nRepresentatives of the Artemis Accords signatories, including NASA leadership, met Oct. 14, 2024, for a principals meeting in Milan, during the
International Astronautical Congress. With 42 of 45 signatories participating in the event, established and emerging spacefaring nations from every region of the world were represented. Credit: UAE
Space Agency\n![](https://pe.usembassy.gov/wp-content/uploads/sites/74/2024/11/Ar", "api_data": null, "hint": null}]}
```

```json
{
  "query": "\"Artemis Accords\" \"62nd\" OR \"62 countries\" OR \"new signatory\" 2026"
}
```

### 📋 Result

```
{"query": "\"Artemis Accords\" \"62nd\" OR \"62 countries\" OR \"new signatory\" 2026", "results": [{"title": "Artemis Accords - Wikipedia", "url": "https://en.wikipedia.org/wiki/Artemis_Accords",
"snippet": "The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world governments that elaborates on the norms expected to be followed
in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the ultimate goal of expanding space exploration to Mars and
beyond.\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe,", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Artemis
Accords\", \"url\": \"https://en.wikipedia.org/wiki/Artemis_Accords\", \"extract\": \"The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and
other world governments that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by
2027, with the ultimate goal of expanding space exploration to Mars and beyond.\\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe, 15 in
Asia, seven in South America, five in North America, four in Africa, and two in Oceania.\\nDrafted by NASA and the U.S. Department of State, the Accords establish a framework for cooperation in the
civil exploration and peaceful use of the Moon, Mars, and other astronomical objects. They are explicitly grounded in the United Nations Outer Space Treaty of 1967, which signatories are obliged to
uphold, and cite most major U.N.-brokered conventions constituting space law.\\nThe Accords were originally signed on 13 October 2020 by representatives of the national space agencies of eight
countries: Australia, Canada, Italy, Japan, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States. The Accords remain open for signature indefinitely, as NASA anticipates
more nations joining. Additional signatories can choose to directly participate in Artemis program activities, or may agree simply to commit to the principles for responsible exploration of the Moon
as set out in the Accords.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Artemis Accords - NASA", "url": "https://www.nasa.gov/artemis-accords/", "snippet": "Principles for a Safe, Peaceful,
and Prosperous Future in Space\nNASA, in coordination with the U.S. Department of State and seven other initial signatory nations, established the Artemis Accords in 2020. With many countries and
private companies conducting missions and operations around the Moon, the Artemis Accords provide a common set of principles to enhance the governance of the civil exploration and use of outer
space.\nThe Artemis Accords reinforce the commitment by signatory nations to the", "api_data": null, "hint": null}, {"title": "Artemis Accords | NASA, United States, Outer Space Treaty, Criticism,
Summary, Russia, & China | Britannica", "url": "https://www.britannica.com/topic/Artemis-Accords", "snippet": "[Artemis Accords](https://cdn.britannica.com/28/283728-050-7CCE29BC/Signing-Ceremony-
Artemis-Accords-At-NASA-Headquarters-2024.jpg)Representatives from Uruguay signing the Artemis Accords, making Uruguay the 36th country to sign the accords.\nArtemis Accords\nWhat are the Artemis
Accords?\nWhich countries were the initial signatories of the Artemis Accords?\nWhat are the stated objectives of the Artemis Accords?\nWhy did Russia and China not sign the Artemis Accords?\nArtemis
Accords, set of principle", "api_data": null, "hint": null}, {"title": "US Artemis Accords Hit 50 Signatories in 2024 - AIP.ORG", "url": "https://www.aip.org/fyi/us-artemis-accords-hit-50-signatories-
in-2024", "snippet": "US Artemis Accords Hit 50 Signatories in 2024\n![A NASA graphic showing the flags of the first 48 nations to sign on to the Artemis
Accords.](https://aip.brightspotcdn.com/dims4/default/bac391f/2147483647/strip/true/crop/4000x2250+0+0/resize/820x461!/quality/90/?url=https%3A%2F%2Fk1-prod-aip.s3.us-
east-2.amazonaws.com%2Fbrightspot%2F6e%2Fa3%2F2b796c474f51a15f51699f88712d%2Fartemis-accords-austria-50-121124.png)\nThe flags of the first 48 Artemis Accords signatories. On Dec. 11, 2024, Panama and
Au", "api_data": null, "hint": null}, {"title": "Artemis Accords: What are they & which countries are involved? | Space", "url": "https://www.space.com/artemis-accords-explained", "snippet": "The
Artemis Accords lay out the framework for collaborating nations as we enter the next era of lunar exploration and beyond.\nThe next era of space exploration is underway with the Artemis program aiming
to send the first woman and person of color to the lunar surface before targeting a crewed mission to Mars. The Artemis accords lay out a framework for nations collaborating in this exciting
endeavor.(Image credit: NASA)\nBreaking space news, the latest updates on rocket launches, skywatching eve", "api_data": null, "hint": null}, {"title": "Gold: With 52 Members, Artemis Accords Now
Represent Global Consensus \u2013 SpacePolicyOnline.com", "url": "https://spacepolicyonline.com/news/gold-with-52-members-artemis-accords-now-represent-global-consensus/", "snippet": "Gold: With 52
Members, Artemis Accords Now Represent Global Consensus\nThailand and Liechtenstein just joined the Artemis Accords, bringing the number of signatories to 52. Mike Gold, who was instrumental in
creating the Accords, considers that a significant milestone because it is half the membership of the U.N. Committee on Peaceful Uses of Outer Space. The Accords now constitute a \u201ctrue global
consensus\u201d on principles for responsible behavior on the Moon.\nThe Artemis Accords are named for the ", "api_data": null, "hint": null}, {"title": "ESA - Gateway MoU and Artemis Accords \u2013
FAQs", "url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Gateway_MoU_and_Artemis_Accords_FAQs", "snippet": "Gateway MoU and Artemis Accords \u2013 FAQs\nESA Director
General Jan W\u00f6rner and NASA Administrator Jim Bridenstine [signed](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Positive_signs_for_Europe_as_ESA_goes_forward_to_the_Moon)
a Memorandum of Understanding (MoU) to take Europe to the Moon.\nThe historic agreement will see ESA Member States contribute a number of essential elements to the first human outpost in lunar orbit,
known as the Gateway.\nIt confirms ESA\u2019s commitment to", "api_data": null, "hint": null}, {"title": "Artemis Accords | Current Affairs", "url": "https://www.shankariasparliament.com/current-
affairs/artemis-accords", "snippet": "Prelims \u2013 Current events of national and international importance.\nMains (GS III) \u2013 Awareness in the fields of IT, Space, Computers, robotics, nano-
technology, bio-technology and issues relating to intellectual property rights.\nBangladesh recently became the 54th nation to sign the Artemis Accords.\nNASA's Artemis Program aims to return humans
to the Moon and Mars.\nCore Principles of the Accord\nSignificance", "api_data": null, "hint": null}, {"title": "The Artemis Accords By the Numbers", "url": "https://payloadspace.com/the-artemis-
accords-by-the-numbers/", "snippet": "This article was updated Jan. 27 to reflect Oman\u2019s addition to the Accords.\nOman announced this week that it had signed on to the Artemis Accords, becoming
the 61st nation to agree to the set of non-binding principles.\nA quick reminder: The US led the establishment of the Artemis Accords in 2020. Nations who sign on commit to exploring space in a
peaceful, transparent, and sustainable way.\nThe accords celebrated their fifth anniversary in October. As such, here\u2019s a roundup of where they stand.\nG", "api_data": null, "hint": null},
{"title": "Artemis Accords Adds 25<sup>th</sup>, 26<sup>th</sup>, and 27<sup>th</sup> Signatory Countries", "url": "https://www.universetoday.com/articles/artemis-accords-adds-25th-26th-and-27th-
signatory-countries", "snippet": "NASA recently welcomed the newest signatories of the [Artemis Accords](https://www.nasa.gov/specials/artemis-accords/index.html) as Spain, Ecuador, and India became
the 25th, 26th, and 27thcountries, respectively, to sign on to the historic agreement for cooperation and partnership for space exploration, specifically pertaining to NASA's Artemis program.\nNASA
[announced on May 30](https://www.nasa.gov/press-release/nasa-welcomes-spain-as-25th-artemis-accords-signatory) that Spain had become the ", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me analyze what I know so far and get more data on the signing rate.

Key facts:
- Current count: 61 signatories (as of January 26, 2026, when Oman signed)
- The NASA page currently shows 61 signatories
- Question resolves on April 30, 2026
- Options: ≤61, 62, >62

I need to understand:
1. The rate of new signatories
2. Whether any new signatories are expected before April 30, 2026
3. Whether the Artemis II launch (scheduled for April 1, 2026) might catalyze new signings


4. The historical signing pattern to project forward

Looking at the timeline, I can see the pace has been accelerating—starting with 8 signatories in October 2020, reaching 27 by mid-2023, then jumping to 45 by October 2024, and hitting 61 by late January 2026. The most recent additions include Thailand, Liechtenstein, Bangladesh, and others joining throughout 2025 and into 2026.

The key observation is that the rate picked up significantly in 2025, with roughly 9-11 new countries signing on across the year and into January 2026. Now I'm trying to estimate how many more might join between now and the end of April 2026, which gives us about 6 weeks to consider.

There's been a notable pause since Oman signed on January 26 — about 7 weeks without any new announcements. But the Artemis II launch scheduled for April 1st could be a turning point, as NASA tends to use major mission milestones to announce fresh signatories. So I'm weighing whether we stay at 61, hit 62 with one more country, or jump to 63 or higher if the launch catalyzes multiple signings.

## 💬 Response

Let me look for the detailed signing rate and any imminent new signatories.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://payloadspace.com/the-artemis-accords-by-the-numbers/",
  "prompt": "What is the timeline of signatories? How many signed in each year? What is the growth rate?"
}
```

### 📋 Result

```
{"url": "https://payloadspace.com/the-artemis-accords-by-the-numbers/", "content": "Based on the content provided:\n\n**Timeline of Signatories:**\n- **2020**: The Artemis Accords were established
(initial signatories not specified)\n- **2024**: 19 nations signed - the highest number of additions in a single year\n- **As of Jan. 27, 2025**: 61 total nations have signed\n\n**Growth Rate:**\nThe
article mentions that 2024 was a \"banner year\" with 19 new signatories, but it doesn't provide a complete year-by-year breakdown for 2020-2023. Therefore, I cannot calculate precise annual growth
rates for each year.\n\n**Current Status:**\n- 61 signatories represent 31% of the 193 UN member states\n- Signatories span every continent except Antarctica\n- Europe has the most signatories (29
nations)\n\nThe content references charts showing \"Artemis accords signatories by year\" but doesn't include the specific numerical data from those visualizations in the text.\n\n**Relevant
links:**\n- [Payload Pro](https://payloadspace.com/pro) - subscription service mentioned for more detailed charts and analysis", "title": "The Artemis Accords By the Numbers"}
```

```json
{
  "query": "Artemis Accords country expected join sign 2026 upcoming"
}
```

### 📋 Result

```
{"query": "Artemis Accords country expected join sign 2026 upcoming", "results": [{"title": "Artemis Accords - NASA", "url": "https://www.nasa.gov/artemis-accords/", "snippet": "Principles for a Safe,
Peaceful, and Prosperous Future in Space\nNASA, in coordination with the U.S. Department of State and seven other initial signatory nations, established the Artemis Accords in 2020. With many
countries and private companies conducting missions and operations around the Moon, the Artemis Accords provide a common set of principles to enhance the governance of the civil exploration and use of
outer space.\nThe Artemis Accords reinforce the commitment by signatory nations to the", "api_data": null, "hint": null}, {"title": "Artemis Accords - Wikipedia", "url":
"https://en.wikipedia.org/wiki/Artemis_Accords", "snippet": "The Artemis Accords are a set of non-binding multilateral arrangements between the United States government and other world governments
that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led effort to return humans to the Moon by 2027, with the ultimate goal
of expanding space exploration to Mars and beyond.\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the Accords, including 28 in Europe,", "api_data": {"content": [{"type":
"text", "text": "{\"title\": \"Artemis Accords\", \"url\": \"https://en.wikipedia.org/wiki/Artemis_Accords\", \"extract\": \"The Artemis Accords are a set of non-binding multilateral arrangements
between the United States government and other world governments that elaborates on the norms expected to be followed in outer space. The Accords are related to the Artemis program, an American-led
effort to return humans to the Moon by 2027, with the ultimate goal of expanding space exploration to Mars and beyond.\\nAs of 26 January 2026, with the accession of Oman, 61 countries have signed the
Accords, including 28 in Europe, 15 in Asia, seven in South America, five in North America, four in Africa, and two in Oceania.\\nDrafted by NASA and the U.S. Department of State, the Accords
establish a framework for cooperation in the civil exploration and peaceful use of the Moon, Mars, and other astronomical objects. They are explicitly grounded in the United Nations Outer Space Treaty
of 1967, which signatories are obliged to uphold, and cite most major U.N.-brokered conventions constituting space law.\\nThe Accords were originally signed on 13 October 2020 by representatives of
the national space agencies of eight countries: Australia, Canada, Italy, Japan, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States. The Accords remain open for signature
indefinitely, as NASA anticipates more nations joining. Additional signatories can choose to directly participate in Artemis program activities, or may agree simply to commit to the principles for
responsible exploration of the Moon as set out in the Accords.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Artemis Accords Reach Another Milestone with Portugal \u2013
SpacePolicyOnline.com", "url": "https://spacepolicyonline.com/news/artemis-accords-reach-another-milestone-with-portugal/", "snippet": "Artemis Accords Reach Another Milestone with Portugal\nPortugal
became the 60th country to join the Artemis Accords today. It\u2019s another milestone for the U.S.-led principles for responsible behavior on the Moon. The Accords recently celebrated the fifth
anniversary of when the first eight countries \u2014 Australia, Canada, Japan, Italy, Luxembourg, the United Arab Emirates, the United Kingdom, and the United States \u2014 signed the non-binding
principles in October 2020.\nPortugal\u2019s Secretary of State for", "api_data": null, "hint": null}, {"title": "Artemis Accords | NASA, United States, Outer Space Treaty, Criticism, Summary, Russia,
& China | Britannica", "url": "https://www.britannica.com/topic/Artemis-Accords", "snippet": "[Artemis Accords](https://cdn.britannica.com/28/283728-050-7CCE29BC/Signing-Ceremony-Artemis-Accords-At-
NASA-Headquarters-2024.jpg)Representatives from Uruguay signing the Artemis Accords, making Uruguay the 36th country to sign the accords.\nArtemis Accords\nWhat are the Artemis Accords?\nWhich
countries were the initial signatories of the Artemis Accords?\nWhat are the stated objectives of the Artemis Accords?\nWhy did Russia and China not sign the Artemis Accords?\nArtemis Accords, set of
principle", "api_data": null, "hint": null}, {"title": "Portugal signs the Artemis Accords - SpaceNews", "url": "https://spacenews.com/portugal-signs-the-artemis-accords/", "snippet": "WASHINGTON
\u2014 Portugal has become the latest country to sign the Artemis Accords outlining best practices for responsible space exploration, beating out another European country to be the 60th to
join.\nHelena Canh\u00e3o, Portugal\u2019s state secretary for science and innovation, signed the Artemis Accords Jan. 11 on behalf of the government, with an event held in Lisbon Jan. 12 to formally
announce the signing as part of broader discussions between the governments of the United States and Portugal.\n\u201c2026", "api_data": null, "hint": null}, {"title": "NASA Welcomes Portugal as 60th
Artemis Accords Signatory - NASA", "url": "https://www.nasa.gov/news-release/nasa-welcomes-portugal-as-60th-artemis-accords-signatory/", "snippet": "Portugal is the latest nation to sign the Artemis
Accords alongside 59 other countries in a commitment to advancing principles for the responsible exploration of the Moon, Mars, and beyond with NASA.\n\u201cPortugal joins a cadre of nations building
the framework for safe, transparent, and prosperous activity in space,\u201d said NASA Administrator Jared Isaacman in recorded remarks. \u201cThis is our generation\u2019s Golden Age of Exploration.
Together, we are advancing innovation, driving international collaborat", "api_data": null, "hint": null}, {"title": "Artemis Accords: What are they & which countries are involved? | Space", "url":
"https://www.space.com/artemis-accords-explained", "snippet": "The Artemis Accords lay out the framework for collaborating nations as we enter the next era of lunar exploration and beyond.\nThe next
era of space exploration is underway with the Artemis program aiming to send the first woman and person of color to the lunar surface before targeting a crewed mission to Mars. The Artemis accords lay
out a framework for nations collaborating in this exciting endeavor.(Image credit: NASA)\nBreaking space news, the latest updates on rocket launches, skywatching eve", "api_data": null, "hint": null},
{"title": "NASA Welcomes Portugal as 60th Artemis Accords Signatory For Advancement of Space Exploration - Space Coast Daily", "url": "https://spacecoastdaily.com/2026/01/nasa-welcomes-portugal-
as-60th-artemis-accords-signatory-for-advancement-of-space-exploration/", "snippet": "NASA Welcomes Portugal as 60th Artemis Accords Signatory For Advancement of Space Exploration\nBy [Space Coast
Daily](https://spacecoastdaily.com/showme/bethyork/) // January 14, 2026\nthe first set of practical principles of civil space exploration\n![](https://spacecoastdaily.com/wp-
content/uploads/2026/01/Hugo-Costa-executive-director-for-the-Portuguese-Space-Agency-and-U.S.-Ambassador-to-Portugal-John-J.jpg)\n![](https://spacecoastdaily.com/wp-content/uploads/2026/01/Hugo-
Costa-executive-directo", "api_data": null, "hint": null}, {"title": "Oman set to become the 61st country to join the NASA Artemis Accords", "url": "https://www.wdbo.com/news/oman-set-become-61st-
country-join-nasa-artemis-accords/4JWKPSSC3JC23H4GCHPU34VH4E/", "snippet": "We\u2019re Sorry!\nThis website is unavailable in your location.\nError 451\nIt appears you are attempting to access this
website from a country outside of the United States, therefore access cannot be granted at this time.\nThis website is unavailable in your location.\nIt appears you are attempting to access this
website from a country outside of the United States, therefore access cannot be granted at this time.", "api_data": null, "hint": null}, {"title": "ESA - Gateway MoU and Artemis Accords \u2013 FAQs",
"url": "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Gateway_MoU_and_Artemis_Accords_FAQs", "snippet": "Gateway MoU and Artemis Accords \u2013 FAQs\nESA Director General Jan
W\u00f6rner and NASA Administrator Jim Bridenstine [signed](https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/Positive_signs_for_Europe_as_ESA_goes_forward_to_the_Moon) a
Memorandum of Understanding (MoU) to take Europe to the Moon.\nThe historic agreement will see ESA Member States contribute a number of essential elements to the first human outpost in lunar orbit,
known as the Gateway.\nIt confirms ESA\u2019s commitment to", "api_data": null, "hint": null}]}
```

## 💬 Response

Now let me compute the signing rate and run a simulation.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nfrom datetime import datetime, timedelta\n\n# Signing timeline reconstruction from sources:\n# Oct 2020: 8 (initial)\n# By end 2021: ~13 (5 new in 2021)\n# By end 2022: ~23 (10 new in 2022)\n# By end 2023: ~33 (10 new in 2023) -- India was 27th in mid-2023\n# By end 2024: ~50 (Panama & Austria were 49th & 50th on Dec 11, 2024) -- 19 new in 2024\n# 2025: ~9 new (from 50 to 59 by Oct 2025 - Hungary, Malaysia, Philippines were 57-59th)\n# Jan 2026: Portugal (#60 on Jan 11-12), Oman (#61 on Jan 26)\n\n# Let's focus on recent rate\n# 2024: 19 new signatories in ~12 months -> ~1.58/month\n# 2025: ~9 new in 12 months -> ~0.75/month  \n# Jan 2026: 2 new in 1 month -> 2/month (but this was a burst)\n\n# Since Oman signed on Jan 26, 2026, no new signatories have been announced\n# That's about 49 days (Jan 26 to March 16) with no new signatories\n\n# Time remaining: March 16 to April 30 = 45 days\n\n# More conservative estimate based on 2025 rate:\n# 2025: ~11 new signatories (50->61 including Jan 2026 ones, actually 50->59 in 2025, then 2 in Jan 2026)\n# Let's be more precise:\n# End 2024: 50\n# 2025 signatories: 9 in about 10 months (Jan-Oct 2025) \n# Then 2 more in Jan 2026\n\n# Average rate over last ~14 months: 11 signatories in 14 months = 0.786/month\n\n# But there's been a ~7 week gap since the last signing\n# Rate for simulation: ~0.5-1.0 per month seems reasonable\n\n# Monte Carlo simulation\nnp.random.seed(42)\nn_sims = 100000\n\n# Using a Poisson process for new signatories\n# Time window: March 16 to April 30 = 45 days = ~1.5 months\n\n# Let's consider different rate scenarios\n# Conservative (2025 rate, adjusted for slowing): ~0.5/month\n# Moderate (2025 average): ~0.75/month  \n# Optimistic (Artemis II launch boost): ~1.5/month\n\n# Key consideration: Artemis II launches April 1 - this is a major catalyst\n# NASA has historically timed new signatory announcements around major events\n\n# Weighted rate: 0.7/month seems reasonable as a base\n# With Artemis II boost potential\n\ndays_remaining = 45  # March 16 to April 30\nmonths_remaining = days_remaining / 30.0\n\nresults = {}\nfor rate_label, monthly_rate in [(\"conservative_0.5\", 0.5), (\"moderate_0.75\", 0.75), (\"high_1.5\", 1.5)]:\n    expected = monthly_rate * months_remaining\n    new_signatories = np.random.poisson(expected, n_sims)\n    total = 61 + new_signatories\n    \n    p_le61 = np.mean(total <= 61)\n    p_62 = np.mean(total == 62)\n    p_gt62 = np.mean(total > 62)\n    \n    results[rate_label] = {\n        'expected_new': expected,\n        'p_le61': p_le61,\n        'p_62': p_62,\n        'p_gt62': p_gt62,\n        'mean_total': np.mean(total)\n    }\n    print(f\"\\n{rate_label} (rate={monthly_rate}/mo, expected_new={expected:.2f}):\")\n    print(f\"  P(\u226461) = {p_le61:.4f}\")\n    print(f\"  P(=62) = {p_62:.4f}\")\n    print(f\"  P(>62) = {p_gt62:.4f}\")\n    print(f\"  Mean total = {np.mean(total):.2f}\")\n\n# Also consider the 7-week gap since last signing\nprint(\"\\n\\n--- Additional analysis ---\")\nprint(f\"Days since last signing (Jan 26 to Mar 16): ~49 days\")\nprint(f\"Days until resolution: ~45 days\")\nprint(f\"If rate is truly 0.75/month, probability of 0 new in 49 days = {np.exp(-0.75 * 49/30):.4f}\")\nprint(f\"The 49-day gap is somewhat long but not unprecedented\")\n\n# Let me think about the Artemis II factor\nprint(\"\\n--- Artemis II consideration ---\")\nprint(\"Artemis II launch scheduled for April 1, 2026\")\nprint(\"NASA frequently announces new signatories around major events\")\nprint(\"This is a HUGE catalyst - the first crewed lunar mission in 50+ years\")\nprint(\"High probability that NASA coordinates at least 1 new signing around the launch\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "\nconservative_0.5 (rate=0.5/mo, expected_new=0.75):\n  P(\u226461) = 0.4703\n  P(=62) = 0.3569\n  P(>62) = 0.1728\n  Mean total = 61.75\n\nmoderate_0.75 (rate=0.75/mo,
expected_new=1.12):\n  P(\u226461) = 0.3262\n  P(=62) = 0.3631\n  P(>62) = 0.3107\n  Mean total = 62.12\n\nhigh_1.5 (rate=1.5/mo, expected_new=2.25):\n  P(\u226461) = 0.1035\n  P(=62) = 0.2368\n
P(>62) = 0.6597\n  Mean total = 63.25\n\n\n--- Additional analysis ---\nDays since last signing (Jan 26 to Mar 16): ~49 days\nDays until resolution: ~45 days\nIf rate is truly 0.75/month, probability
of 0 new in 49 days = 0.2938\nThe 49-day gap is somewhat long but not unprecedented\n\n--- Artemis II consideration ---\nArtemis II launch scheduled for April 1, 2026\nNASA frequently announces new
signatories around major events\nThis is a HUGE catalyst - the first crewed lunar mission in 50+ years\nHigh probability that NASA coordinates at least 1 new signing around the launch\n", "stderr":
"", "duration_ms": 196}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me think more carefully about what rate to use\n\n# Historical yearly rates:\n# 2020: 8 (founding)\n# 2021: ~5 new\n# 2022: ~10 new\n# 2023: ~10 new  \n# 2024: 19 new (banner year)\n# 2025: 9 new (Jan-Oct 2025, signatories 51-59)\n# Jan 2026: 2 new (Portugal #60, Oman #61)\n\n# BUT: the question asks what NASA's page will show. The page might lag behind actual signings.\n# However, the page currently shows 61, so it's up to date.\n\n# Key factors for the rate:\n# 1. The 7-week gap suggests the rate may be slowing\n# 2. Artemis II launch April 1 is a MAJOR catalyst for new signings\n# 3. There are still many countries that haven't signed (~132 UN members)\n# 4. The pool of \"easy\" signatories may be shrinking (already have most Western, allied nations)\n# 5. Current US administration (Trump/Isaacman) seems to be actively promoting the Accords\n\n# My assessment: The rate is probably around 0.5-1.0/month\n# BUT Artemis II is a strong catalyst that might bump it\n\n# Let me model this more carefully:\n# Base rate without catalyst: ~0.5/month (reflecting the gap)\n# Artemis II bonus: ~40% chance of at least 1 new signatory timed to the launch\n# This is because NASA has historically coordinated signings with milestones\n\nnp.random.seed(42)\nn_sims = 100000\n\n# Model: Poisson(base_rate * time) + Bernoulli(catalyst_prob) * Poisson(catalyst_additions)\nbase_rate = 0.6  # per month, slightly below 2025 average to account for slowing\ntime_months = 45 / 30.0\n\n# For the Artemis II catalyst\ncatalyst_prob = 0.45  # probability that NASA orchestrates new signings around Artemis II\ncatalyst_mean = 1.5  # if catalyst fires, expected additional signatories (1-3)\n\nbase_new = np.random.poisson(base_rate * time_months, n_sims)\ncatalyst_fires = np.random.random(n_sims) < catalyst_prob\ncatalyst_new = np.random.poisson(catalyst_mean, n_sims) * catalyst_fires\n\n# But avoid double counting - catalyst replaces some of the base rate\n# Actually, let me just use a blended rate approach\n# Effective rate = base_rate + catalyst contribution\n\ntotal_new = base_new + catalyst_new.astype(int)\ntotal = 61 + total_new\n\np_le61 = np.mean(total <= 61)\np_62 = np.mean(total == 62)\np_gt62 = np.mean(total > 62)\n\nprint(\"=== Blended Model (base + Artemis II catalyst) ===\")\nprint(f\"P(\u226461) = {p_le61:.4f}\")\nprint(f\"P(=62) = {p_62:.4f}\")\nprint(f\"P(>62) = {p_gt62:.4f}\")\nprint(f\"Mean total = {np.mean(total):.2f}\")\nprint(f\"Median total = {np.median(total):.0f}\")\n\n# Distribution of totals\nfrom collections import Counter\ncounts = Counter(total)\nfor k in sorted(counts.keys()):\n    pct = counts[k] / n_sims * 100\n    if pct > 0.5:\n        print(f\"  Total={k}: {pct:.1f}%\")\n\n# Let me also think about whether the NASA page might not update promptly\n# The question says \"as of April 30, 2026\" so even if a country signs, \n# the page needs to be updated. This adds a delay factor.\nprint(\"\\n=== Consideration: NASA page update lag ===\")\nprint(\"If a country signs in late April, the page might not be updated by April 30\")\nprint(\"This slightly favors lower counts\")\n\n# Let me also consider a simpler approach:\n# What's the probability of at least 1 new signatory in 45 days?\n# Using different rate assumptions\nprint(\"\\n=== P(at least 1 new signatory) for different rates ===\")\nfor rate in [0.3, 0.5, 0.7, 0.9, 1.0, 1.2]:\n    lam = rate * time_months\n    p_zero = np.exp(-lam)\n    print(f\"  Rate={rate}/mo: P(0 new)={p_zero:.3f}, P(\u22651 new)={1-p_zero:.3f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Blended Model (base + Artemis II catalyst) ===\nP(\u226461) = 0.2650\nP(=62) = 0.2976\nP(>62) = 0.4374\nMean total = 62.58\nMedian total = 62\n  Total=61: 26.5%\n
Total=62: 29.8%\n  Total=63: 20.7%\n  Total=64: 12.2%\n  Total=65: 6.3%\n  Total=66: 2.8%\n  Total=67: 1.1%\n\n=== Consideration: NASA page update lag ===\nIf a country signs in late April, the page
might not be updated by April 30\nThis slightly favors lower counts\n\n=== P(at least 1 new signatory) for different rates ===\n  Rate=0.3/mo: P(0 new)=0.638, P(\u22651 new)=0.362\n  Rate=0.5/mo: P(0
new)=0.472, P(\u22651 new)=0.528\n  Rate=0.7/mo: P(0 new)=0.350, P(\u22651 new)=0.650\n  Rate=0.9/mo: P(0 new)=0.259, P(\u22651 new)=0.741\n  Rate=1.0/mo: P(0 new)=0.223, P(\u22651 new)=0.777\n
Rate=1.2/mo: P(0 new)=0.165, P(\u22651 new)=0.835\n", "stderr": "", "duration_ms": 15}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me think more carefully and conservatively.\n# \n# Key observations:\n# 1. Current count: 61 (as of Jan 26, 2026 - NASA page confirmed)\n# 2. No new signatories in ~49 days (Jan 26 - Mar 16)\n# 3. The 7-week gap is somewhat notable but not unprecedented\n#    - There were similar gaps in 2025 between signings\n# 4. Artemis II launch April 1 is a significant potential catalyst\n# 5. Question resolves April 30 - about 45 days from now\n# 6. The page update lag is a minor concern but NASA usually updates quickly\n#\n# The question is structured suspiciously around 62 - suggesting the question \n# maker thinks 62 is a plausible boundary. Currently at 61.\n#\n# Let me estimate more carefully:\n#\n# Rate analysis:\n# 2025 had 11 new (50->61, including Jan 2026 signings that were probably in pipeline)\n# Actually: 50 at end of 2024, 59 by Oct 2025, 60 in Jan 2026, 61 in Jan 2026\n# So 2025 calendar year: 9 new (Jan-Oct) = 0.9/month\n# But there was a gap from Oct 2025 to Jan 2026 (3 months with no signings? then 2 in Jan)\n# This suggests the rate is lumpy, not uniform.\n#\n# For the 45-day window, I'll use a moderate rate of ~0.6-0.7/month as the base\n# Plus account for Artemis II catalyst\n#\n# But I should also account for:\n# - The 7-week gap already observed (reduces confidence in high rate)\n# - Trump admin DOGE cuts potentially affecting State Dept outreach\n# - But Artemis II is a genuine catalyst\n\n# My adjusted model:\nnp.random.seed(123)\nn_sims = 200000\n\n# Two-component model:\n# Component 1: \"organic\" rate of ~0.5/month (reflecting recent slowdown)\n# Component 2: Artemis II catalyst event\n# - P(NASA coordinates signings for Artemis II) = 0.35\n# - If yes, typically 1-3 countries announced\n\ntime_months = 45 / 30.0  # 1.5 months\n\n# Organic new signatories\norganic = np.random.poisson(0.5 * time_months, n_sims)\n\n# Artemis II catalyst\ncatalyst_fires = np.random.random(n_sims) < 0.35\n# When catalyst fires, 1-3 new countries (geometric-ish)\ncatalyst_count = np.zeros(n_sims, dtype=int)\nfor i in range(n_sims):\n    if catalyst_fires[i]:\n        # 1-3 countries, weighted toward 1-2\n        catalyst_count[i] = np.random.choice([1, 2, 3], p=[0.5, 0.35, 0.15])\n\ntotal_new = organic + catalyst_count\ntotal = 61 + total_new\n\n# But there's overlap - if organic produces signatories AND catalyst fires,\n# some of those might be the same events. Let me just use total_new as is\n# since they could be independent countries.\n\np_le61 = np.mean(total <= 61)\np_62 = np.mean(total == 62)\np_gt62 = np.mean(total > 62)\n\nprint(\"=== Final Model ===\")\nprint(f\"P(\u226461) = {p_le61:.4f}\")\nprint(f\"P(=62) = {p_62:.4f}\")\nprint(f\"P(>62) = {p_gt62:.4f}\")\nprint(f\"Sum = {p_le61 + p_62 + p_gt62:.4f}\")\nprint(f\"Mean total = {np.mean(total):.2f}\")\nprint(f\"Median total = {np.median(total):.0f}\")\n\nprint(\"\\n--- Distribution ---\")\nfrom collections import Counter\ncounts = Counter(total)\nfor k in sorted(counts.keys()):\n    pct = counts[k] / n_sims * 100\n    if pct > 0.3:\n        print(f\"  Total={k}: {pct:.1f}%\")\n\n# Let me also think about what happens if I weight the organic rate differently\nprint(\"\\n=== Sensitivity to organic rate ===\")\nfor org_rate in [0.3, 0.4, 0.5, 0.6, 0.8]:\n    organic_s = np.random.poisson(org_rate * time_months, n_sims)\n    total_s = 61 + organic_s + catalyst_count\n    print(f\"Organic rate={org_rate}: P(\u226461)={np.mean(total_s<=61):.3f}, P(=62)={np.mean(total_s==62):.3f}, P(>62)={np.mean(total_s>62):.3f}\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "=== Final Model ===\nP(\u226461) = 0.3082\nP(=62) = 0.3116\nP(>62) = 0.3802\nSum = 1.0000\nMean total = 62.33\nMedian total = 62\n\n--- Distribution ---\n  Total=61:
30.8%\n  Total=62: 31.2%\n  Total=63: 20.4%\n  Total=64: 11.5%\n  Total=65: 4.5%\n  Total=66: 1.3%\n\n=== Sensitivity to organic rate ===\nOrganic rate=0.3: P(\u226461)=0.415, P(=62)=0.299,
P(>62)=0.286\nOrganic rate=0.4: P(\u226461)=0.355, P(=62)=0.311, P(>62)=0.335\nOrganic rate=0.5: P(\u226461)=0.308, P(=62)=0.311, P(>62)=0.381\nOrganic rate=0.6: P(\u226461)=0.267, P(=62)=0.306,
P(>62)=0.427\nOrganic rate=0.8: P(\u226461)=0.195, P(=62)=0.289, P(>62)=0.517\n", "stderr": "", "duration_ms": 410}
```

## 💬 Response

Now let me run the reflection checkpoint.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Current count is exactly 61, confirmed by NASA page and Wikipedia. Status quo = \u226461.",
      "supports": "Less than or equal to 61",
      "logit": 0.8,
      "confidence": 1
    },
    {
      "description": "7-week gap since last signing (Jan 26 to Mar 16) with no new announcements, suggesting the rate may be slowing",
      "supports": "Less than or equal to 61",
      "logit": 0.6,
      "confidence": 0.7
    },
    {
      "description": "Artemis II launch scheduled for April 1, 2026 - NASA historically coordinates new signatory announcements around major Artemis events (e.g., 3 countries at 5th anniversary in Oct 2025). This is a strong catalyst for at least 1 new signing.",
      "supports": "Greater than 62",
      "logit": 1,
      "confidence": 0.5
    },
    {
      "description": "Historical signing rate of ~0.75/month in 2025, which over 1.5 months gives ~1.1 expected new signatories. Median outcome would be exactly 62.",
      "supports": "62",
      "logit": 0.7,
      "confidence": 0.6
    },
    {
      "description": "Trump admin DOGE-era budget cuts may slow State Dept outreach for new signatories, but Artemis program remains a presidential priority",
      "supports": "Less than or equal to 61",
      "logit": 0.3,
      "confidence": 0.3
    },
    {
      "description": "2024 was a banner year (19 new), but 2025 slowed to ~9. The signing rate appears to be decelerating as the pool of 'easy' signatories shrinks",
      "supports": "Less than or equal to 61",
      "logit": 0.5,
      "confidence": 0.6
    },
    {
      "description": "45 days is a moderate window. Even at a reduced rate, probability of at least 1 new signatory is ~50-65%",
      "supports": "Greater than 62",
      "logit": 0.3,
      "confidence": 0.6
    }
  ],
  "tentative_estimate": {
    "probabilities": {
      "62": 0.3,
      "Less than or equal to 61": 0.38,
      "Greater than 62": 0.32
    }
  },
  "assessment": "The current count is exactly 61 signatories on NASA's Artemis Accords page, confirmed by both the page itself and Wikipedia. The last signatory (Oman) joined on January 26, 2026, meaning there has been a ~7-week gap with no new signatories.\n\nThe question asks what the count will be as of April 30, 2026, giving a ~45-day window. Historical rates suggest ~0.5-0.9 new signatories per month, but with significant lumpiness. The Artemis II launch on April 1 is a major potential catalyst, as NASA has historically coordinated signatory announcements around milestones.\n\nMonte Carlo simulations with various rate assumptions consistently show the three outcomes are fairly balanced, with \u226461 having a slight edge due to status quo persistence, but the Artemis II catalyst makes \u226562 collectively more likely than not. The median outcome across most reasonable rate assumptions lands near 62.\n\nKey tension: The 7-week gap suggests slowing vs. the Artemis II catalyst suggesting acceleration. These partially cancel out, leaving genuine uncertainty across all three buckets.",
  "tool_audit": "- NASA page fetch: Confirmed 61 signatories, very useful\n- Wikipedia: Confirmed 61 as of Jan 26, 2026, provided regional breakdown\n- Web search: Found signing timeline, Artemis II launch details, no evidence of imminent new signatories\n- AskNews search_news: Extensive coverage of Artemis II preparations, confirmed 61 count, no mention of upcoming signatories\n- Monte Carlo simulation: Ran multiple rate scenarios, useful for calibrating probabilities\n- No tools failed. The search for \"62nd\" signatory returned nothing, which is informative (no new signatory announced).",
  "process_reflection": "The question is well-suited to the toolset. The URL fetcher correctly extracted the count from NASA's page. The Monte Carlo simulation was helpful for understanding the distribution of outcomes. The main challenge is that the signing process is lumpy and event-driven rather than following a smooth Poisson process, which makes standard statistical modeling less reliable. A tool that could track diplomatic activity or State Department press releases would have been useful. The multi-option MC format is appropriate for this question.",
  "calibration_notes": "Base rate: ~0.75 new signatories per month based on 2025 data. Status quo (61) is the default if nothing changes. The 7-week gap is somewhat long but within normal variation. Key catalyst: Artemis II launch April 1. Status quo persistence and the recent gap push toward \u226461, while the Artemis II catalyst and historical rate push toward \u226562.",
  "key_uncertainties": "1. Will NASA coordinate new signatory announcements around Artemis II? This is the single biggest uncertainty.\n2. Is the 7-week gap signal (rate slowing) or noise (normal variation)?\n3. Could page update lag affect the count even if a country technically signs?",
  "update_triggers": "- Any announcement of a new Artemis Accords signatory would immediately shift probability away from \u226461\n- Artemis II mission delay beyond April 30 would reduce the catalyst effect\n- DOGE-related cuts to NASA or State Dept international outreach could slow signings"
}
```

### 📋 Result

```
{"factor_count": 7, "factor_sum": 2.71, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Current count is exactly 61, confirmed by NASA page and Wikipedia. Status quo = \u226461.",
"supports": "Less than or equal to 61", "logit": 0.8, "confidence": 1.0, "effective_logit": 0.8}, {"description": "7-week gap since last signing (Jan 26 to Mar 16) with no new announcements,
suggesting the rate may be slowing", "supports": "Less than or equal to 61", "logit": 0.6, "confidence": 0.7, "effective_logit": 0.42}, {"description": "Artemis II launch scheduled for April 1, 2026 -
NASA historically coordinates new signatory announcements around major Artemis events (e.g., 3 countries at 5th anniversary in Oct 2025). This is a strong catalyst for at least 1 new signing.",
"supports": "Greater than 62", "logit": 1.0, "confidence": 0.5, "effective_logit": 0.5}, {"description": "Historical signing rate of ~0.75/month in 2025, which over 1.5 months gives ~1.1 expected new
signatories. Median outcome would be exactly 62.", "supports": "62", "logit": 0.7, "confidence": 0.6, "effective_logit": 0.42}, {"description": "Trump admin DOGE-era budget cuts may slow State Dept
outreach for new signatories, but Artemis program remains a presidential priority", "supports": "Less than or equal to 61", "logit": 0.3, "confidence": 0.3, "effective_logit": 0.09}, {"description":
"2024 was a banner year (19 new), but 2025 slowed to ~9. The signing rate appears to be decelerating as the pool of 'easy' signatories shrinks", "supports": "Less than or equal to 61", "logit": 0.5,
"confidence": 0.6, "effective_logit": 0.3}, {"description": "45 days is a moderate window. Even at a reduced rate, probability of at least 1 new signatory is ~50-65%", "supports": "Greater than 62",
"logit": 0.3, "confidence": 0.6, "effective_logit": 0.18}], "dominant_factor": "Current count is exactly 61, confirmed by NASA page and Wikipedia. Status quo = \u226461.", "dominant_effective_logit":
0.8, "outcome_breakdown": [{"outcome": "Less than or equal to 61", "factor_count": 4, "logit_sum": 1.61, "factors": [{"description": "Current count is exactly 61, confirmed by NASA page and Wikipedia.
Status quo = \u226461.", "supports": "Less than or equal to 61", "logit": 0.8, "confidence": 1.0, "effective_logit": 0.8}, {"description": "7-week gap since last signing (Jan 26 to Mar 16) with no new
announcements, suggesting the rate may be slowing", "supports": "Less than or equal to 61", "logit": 0.6, "confidence": 0.7, "effective_logit": 0.42}, {"description": "Trump admin DOGE-era budget cuts
may slow State Dept outreach for new signatories, but Artemis program remains a presidential priority", "supports": "Less than or equal to 61", "logit": 0.3, "confidence": 0.3, "effective_logit":
0.09}, {"description": "2024 was a banner year (19 new), but 2025 slowed to ~9. The signing rate appears to be decelerating as the pool of 'easy' signatories shrinks", "supports": "Less than or equal
to 61", "logit": 0.5, "confidence": 0.6, "effective_logit": 0.3}]}, {"outcome": "Greater than 62", "factor_count": 2, "logit_sum": 0.6799999999999999, "factors": [{"description": "Artemis II launch
scheduled for April 1, 2026 - NASA historically coordinates new signatory announcements around major Artemis events (e.g., 3 countries at 5th anniversary in Oct 2025). This is a strong catalyst for at
least 1 new signing.", "supports": "Greater than 62", "logit": 1.0, "confidence": 0.5, "effective_logit": 0.5}, {"description": "45 days is a moderate window. Even at a reduced rate, probability of at
least 1 new signatory is ~50-65%", "supports": "Greater than 62", "logit": 0.3, "confidence": 0.6, "effective_logit": 0.18}]}, {"outcome": "62", "factor_count": 1, "logit_sum": 0.42, "factors":
[{"description": "Historical signing rate of ~0.75/month in 2025, which over 1.5 months gives ~1.1 expected new signatories. Median outcome would be exactly 62.", "supports": "62", "logit": 0.7,
"confidence": 0.6, "effective_logit": 0.42}]}], "mc_distribution_metrics": {"implied_probabilities": {"62": 0.17908273234793434, "Greater than 62": 0.2322577835843497, "Less than or equal to 61":
0.588659484067716}, "tentative_probabilities": {"62": 0.3, "Less than or equal to 61": 0.38, "Greater than 62": 0.32}, "per_option_gap_pp": {"62": 12.091726765206564, "Greater than 62":
8.774221641565031, "Less than or equal to 61": -20.865948406771594}, "max_gap_pp": -20.865948406771594, "max_gap_option": "Less than or equal to 61"}, "sources": ["[(Metaculus) How many Artemis
Accords signatories will NASA list on its Artemis Accords page before April 30, 2026?](https://www.metaculus.com/questions/42637)", "[Artemis Accords - NASA](https://www.nasa.gov/artemis-accords/)",
"[Artemis Accords - Wikipedia](https://en.wikipedia.org/wiki/Artemis_Accords)", "[The Artemis Accords By the Numbers](https://payloadspace.com/the-artemis-accords-by-the-numbers/)"],
"reviewer_critique": "## Verification Results\n\n**Resolution Criteria**: The question clearly specifies resolution based on NASA's Artemis Accords page count as of April 30, 2026. The agent correctly
fetched and analyzed this page. \u2713\n\n**Factor-by-Factor Verification**:\n\n1. **Factor 1 (Current count = 61)**: CONFIRMED. Trace line 63-64 shows NASA fetch result: \"61 countries are
signatories to the Artemis Accords as of January 26, 2026, when Oman became the 61st nation to sign.\" Wikipedia confirms same count.\n\n2. **Factor 2 (7-week gap since Jan 26)**: CONFIRMED. Math is
correct: Jan 26 to Mar 16 = ~49 days / ~7 weeks.\n\n3. **Factor 3 (Artemis II catalyst + 3 countries at 5th anniversary)**: CONFIRMED. Trace line 112 shows: \"October marked the fifth anniversary of
NASA... as well as the recognition of Hungary, Malaysia and the Philippines joining the expanding coalition\" - confirms 3 countries announced around a milestone event. Artemis II launch date of April
1, 2026 is confirmed across multiple news sources in the trace.\n\n4. **Factor 4 (0.75/month rate in 2025)**: CONFIRMED. Trace line 608 shows \"2024: 19 nations signed\" and agent's calculation of 9
new in 2025 (Jan-Oct) yields ~0.75-0.9/month.\n\n5. **Factor 5 (DOGE budget cuts)**: Appropriately low confidence (0.3). Not directly sourced in trace but contextually reasonable given Trump admin
mentions.\n\n6. **Factor 6 (Rate decelerating)**: CONFIRMED. 2024 had 19 new vs. 2025 had ~9 new - clear deceleration supported by trace.\n\n7. **Factor 7 (45-day window, 50-65% probability of \u22651
new)**: CONFIRMED. Trace Monte Carlo output shows at moderate 0.75/mo rate: P(\u22651 new) = 65%.\n\n**No Hallucinations Found**: All core factual claims are grounded in the research trace.\n\n**No
Double-Counting Found**: The factors address distinct evidence (current count, gap duration, catalyst events, historical rates, policy context).\n\n**No Wrong-Direction Factors**: All logit signs
align with described effects.\n\n**Probability Assessment**: The agent's Monte Carlo \"Final Model\" produced P(\u226461)=30.8%, P(=62)=31.2%, P(>62)=38.0%. The tentative estimate of 38%/30%/32%
shifts ~7 points from >62 to \u226461 compared to the model output. This adjustment is defensible given the observed 7-week gap (slight evidence update toward slower rate) and NASA page lag concerns
mentioned in the trace. The magnitude of adjustment is modest and all three outcomes remain within a reasonable 30-38% band reflecting genuine uncertainty. I see no basis to substantially revise the
probability estimate.\n\n**Verdict**: Approve. All factors are grounded in trace evidence, Monte Carlo methodology is sound, and final probability estimates are reasonable given the uncertain signing
rate and Artemis II catalyst dynamics."}
```

## 💬 Response

The reflection passed. Let me finalize my forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "As of March 16, 2026, NASA's Artemis Accords page lists exactly 61 signatories (most recent: Oman on January 26, 2026). The question asks for the count as of April 30, 2026 \u2014 a 45-day window. There has been a 7-week gap since the last signing, suggesting some rate deceleration from the ~0.75/month pace seen in 2025. However, the Artemis II launch scheduled for April 1, 2026 is a major catalyst, as NASA has historically coordinated new signatory announcements around milestones (e.g., 3 countries at the 5th anniversary in Oct 2025). Monte Carlo modeling with a blended rate + catalyst approach yields fairly balanced probabilities across all three buckets, with genuine uncertainty about whether any new signatories will join in the window.",
  "probabilities": {
    "62": 0.28,
    "Less than or equal to 61": 0.38,
    "Greater than 62": 0.34
  },
  "factors": [
    {
      "description": "Current count is exactly 61 signatories, confirmed by NASA page and Wikipedia. If nothing changes, question resolves \u226461.",
      "supports": "Less than or equal to 61",
      "logit": 0.8,
      "confidence": 1
    },
    {
      "description": "7-week gap since last signing (Jan 26 to Mar 16) with no new announcements, suggesting the signing rate may be slowing from the 2025 pace of ~0.75/month",
      "supports": "Less than or equal to 61",
      "logit": 0.6,
      "confidence": 0.7
    },
    {
      "description": "Artemis II launch scheduled for April 1, 2026 \u2014 NASA historically coordinates new signatory announcements around major Artemis events (e.g., 3 countries at the 5th anniversary in Oct 2025). This is the biggest catalyst for new signings in the window.",
      "supports": "Greater than 62",
      "logit": 1,
      "confidence": 0.5
    },
    {
      "description": "Historical signing rate of ~0.75/month in 2025. Over 1.5 months this gives ~1.1 expected new signatories, with the median outcome near exactly 62.",
      "supports": "62",
      "logit": 0.7,
      "confidence": 0.6
    },
    {
      "description": "2024 had 19 new signatories but 2025 only ~9 \u2014 the rate is decelerating as the pool of willing/ready signatories shrinks (already 61 of ~193 UN members, most aligned nations already signed)",
      "supports": "Less than or equal to 61",
      "logit": 0.5,
      "confidence": 0.6
    },
    {
      "description": "45 days is a moderate window. Even at a reduced rate of 0.5/month, Monte Carlo shows ~50% probability of at least 1 new signatory; at 0.75/month, ~65%",
      "supports": "Greater than 62",
      "logit": 0.3,
      "confidence": 0.6
    },
    {
      "description": "Trump administration maintains Artemis as a presidential priority, and NASA Administrator Isaacman is actively promoting the program, supporting continued outreach for new signatories",
      "supports": "Greater than 62",
      "logit": 0.3,
      "confidence": 0.4
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

**Forecast Summary:**

| Option | Probability |
|--------|------------|
| ≤61 | **38%** |
| 62 | **28%** |
| >62 | **34%** |

**Key reasoning:**

- **Current state:** NASA's page lists exactly 61 signatories (Oman was #61, signed Jan 26, 2026). No new signatories in the 7 weeks since.
- **Status quo favors ≤61:** If no country signs before April 30, the count stays at 61. The 7-week gap and decelerating rate (19 new in 2024, ~9 in 2025) suggest some slowing.
- **Artemis II catalyst:** The first crewed lunar mission in 50+ years launches April 1 — NASA has historically coordinated signatory announcements around major milestones (e.g., 3 countries at the Oct 2025 anniversary). This meaningfully raises the odds of new signings.
- **Balanced uncertainty:** Monte Carlo modeling with a ~0.5-0.6/month base rate + Artemis II catalyst produces roughly equal probability across all three buckets, reflecting genuine uncertainty about whether 0, 1, or 2+ countries will join in the 45-day window.
