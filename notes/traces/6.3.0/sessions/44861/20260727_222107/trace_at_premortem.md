# Reasoning Log: Will a Russian gasoline export ban be in force during August 1–8, 2026?

*Generated: 2026-07-27T22:24:20.314041+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "prompt": "",
  "questions": [
    {
      "query": "Did Russia extend or reimpose its gasoline (motor gasoline) export ban beyond July 31, 2026? Was a government resolution (postanovlenie) published in late July or early August 2026 extending the gasoline export ban into August 2026 or Q3 2026?",
      "ttl": "6h",
      "context": "Russia had a gasoline export ban until July 31 2026 via Resolution No.78 and No.362. Interfax reported a renewed producer gasoline ban was 'almost decided' and would cover a full quarter. Need to know if it was actually extended/reimposed for August 2026."
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Did Russia extend or reimpose its gasoline (motor gasoline) export ban beyond July 31, 2026? Was a government resolution (postanovlenie) published in late July or early August
2026 extending the gasoline export ban into August 2026 or Q3 2026?", "entry": {"slug": "did-russia-extend-or-reimpose-its-gasoline-motor-g-287011a0", "query": "Did Russia extend or reimpose its
gasoline (motor gasoline) export ban beyond July 31, 2026? Was a government resolution (postanovlenie) published in late July or early August 2026 extending the gasoline export ban into August 2026 or
Q3 2026?", "answer": "I've completed the research. Here's the summary:\n\n**Answer: Yes \u2014 Russia extended its gasoline export ban beyond July 31, 2026, all the way through the end of 2026
(December 31, 2026).**\n\nKey findings:\n- **Deputy PM Alexander Novak announced the decision** in Omsk on July 25, 2026 (reported by TASS July 25; Interfax and Meduza July 27): the gasoline/petrol
export ban is extended \"until the end of the year\" for **both producers and non-producers**.\n- This **exceeds** the \"full quarter\" that Interfax had earlier reported as \"almost decided\" \u2014
the actual extension runs through year-end.\n- **Diesel** is treated differently: to be lifted \"as the market recovers.\"\n- The prior producer ban ran to July 31, 2026 (per the April 2, 2026 decree,
consistent with the Resolution No. 78/No. 362 framework you cited).\n\n**One caveat on the formal postanovlenie:** The late-July reporting confirms the government's *decision* (via Novak's statement
at a headquarters meeting), but these articles do not cite a specific published resolution number for the year-end gasoline extension. Historically, the formal government resolution is signed and
takes effect on its official publication date shortly after such announcements \u2014 but I could not confirm a specific published postanovlenie number/date for the year-end extension in these
searches. The substantive extension decision itself is firmly cross-validated across TASS, Interfax, Bloomberg, Xinhua, Meduza, and RBC-Ukraine.", "sources": [], "key_facts": [], "data_points": [],
"created_at": "2026-07-27T22:23:55.361233Z", "updated_at": "2026-07-27T22:23:55.361233Z", "stale_after": "2026-07-28T04:23:55.361233Z", "state": "fresh", "revision_history": [], "session_id":
"292687ee-c351-4b20-af7d-e0d286b989e8", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1, "failed_count": 0}
```


### ↳ Nested research agent trace

# Reasoning Log: Did Russia extend or reimpose its gasoline (motor gasoline) export ban beyond July 31, 2026? Was a government resolution (postanovlenie) published in late July or early August 2026 extending the gasoline export ban into August 2026 or Q3 2026?

*Generated: 2026-07-27T22:23:55.358439+00:00*


## 💬 Response

I'll research whether Russia extended or reimposed its gasoline export ban beyond July 31, 2026.

## 🔧 Tool: ToolSearch


```json
{
  "query": "news search recent events",
  "max_results": 5
}
```

### 📋 Result

```

```

## 🔧 Tool: ToolSearch


```json
{
  "query": "web search",
  "max_results": 5
}
```

### 📋 Result

```

```

## 💬 Response

I have the search tools I need. Let me search for the latest news on Russia's gasoline export ban.

## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Russia gasoline export ban extended August 2026 government resolution",
  "n_articles": 15,
  "hours_back": 1440,
  "return_type": "string"
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403000 - API access is reserved for Spelunker and Analyst tiers only. Please upgrade your Free plan at https://my.asknews.app/plans
```

```json
{
  "query": "Russia gasoline export ban extended August 2026 postanovlenie"
}
```

### 📋 Result

```
{"query": "Russia gasoline export ban extended August 2026 postanovlenie", "results": [{"title": "Russia extends gasoline export ban through end of 2026", "url": "https://en.apa.az/cis-
countries/russia-extends-gasoline-export-ban-through-end-of-2026-517594", "snippet": "The Russian government will extend its ban on gasoline exports until the end of 2026.\nRussian Deputy Prime
Minister Alexander Novak announced the decision while speaking to journalists.\n\"We have decided that the ban on gasoline exports will remain in force until the end of the year for both producers and
non-producers,\" Novak said.\nHe added that restrictions on diesel fuel exports would be lifted gradually as the domestic market stabilizes. According to Novak, the measure is intended to prevent ",
"api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until year-end: deputy PM-Xinhua", "url": "https://english.news.cn/20260726/4473ef9ef08c4c5c9ce699e9a835f405/c.html",
"snippet": "MOSCOW, July 25 (Xinhua) -- Russia will extend its ban on gasoline exports through the end of 2026 to ensure stable domestic fuel supplies, Russia's Deputy Prime Minister Alexander Novak
said on Saturday.\nSpeaking to reporters in the Siberian city of Omsk, Novak said the decision was made at a government operational meeting and would apply to both gasoline producers and non-
producers.\nHe added that the ban on diesel exports would be lifted once the domestic market recovers, allowing oil refineri", "api_data": null, "hint": null}, {"title": "Russia extends gasoline
export ban through end of 2026 amid fuel shortages | RBC-Ukraine", "url": "https://newsukraine.rbc.ua/news/russia-extends-gasoline-export-ban-through-1785010838.html", "snippet": "Russia extends
gasoline export ban through 2026\n![Russia extends gasoline export ban through 2026](https://newsukraine.rbc.ua/static/img/_/b/_benzin_cherga_zapravka_rosnafta__rosiya__gettyimages_2282016183_6c2659b5
80392f001e3ef9b290010017_1300x820_cd088116976fe081e99aa601e424a7b7_650x410.jpg)\nRussia decided to extend its ban on gasoline exports for all producers through the end of 2026. At the same time, it
plans to lift restrictions on diesel fuel exports, Russian Deputy Prime Minister [Alexand", "api_data": null, "hint": null}, {"title": "Russia extends ban on gasoline exports until end of year due to
fuel crisis - Bloomberg | Ukrainian news", "url": "https://ukranews.com/en/news/1164925-russia-extends-ban-on-gasoline-exports-until-end-of-year-due-to-fuel-crisis-bloomberg", "snippet": "The
government of the aggressor country has decided to extend the ban on gasoline exports until the end of 2026. The restrictions will apply to both direct producers and traders. This was stated by
russian Vice Prime Minister Aleksandr Novak, [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers) reports.\nThe reason for the
fuel shortage in russia this summer was the regular strikes by Ukrainian forces on russian oil refiner", "api_data": null, "hint": null}, {"title": "Russia will extend its ban on gasoline exports
through the end of 2026 \u2013 Famagusta Gazette", "url": "https://famagusta-gazette.com/russia-will-extend-its-ban-on-gasoline-exports-through-the-end-of-2026/", "snippet": "Russia will extend its
ban on gasoline exports through the end of 2026 to ensure stable domestic fuel supplies, Russia\u2019s Deputy Prime Minister Alexander Novak said on Saturday.\nSpeaking to reporters in the Siberian
city of Omsk, Novak said the decision was made at a government operational meeting and would apply to both gasoline producers and non-producers.\nHe added that the ban on diesel exports would be
lifted once the domestic market recovers, allowing oil refineries to avoid oversupply and r", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until end of year \u2014
Meduza", "url": "https://meduza.io/amp/en/news/2026/07/27/russia-to-extend-gasoline-export-ban-until-end-of-year", "snippet": "Russia to extend gasoline export ban until end of year\nRussia will
extend its ban on gasoline exports until the end of 2026, Deputy Prime Minister Alexander Novak said, according to the Russian state news agency TASS.\n\u201cOn the gasoline export ban, we also
decided at the headquarters meeting to extend it for both producers and non-producers. That is, it will be extended until the end of the year,\u201d Novak said.\nNovak added that authorities would
lift the diesel export ban \u201cas the market recovers,\u201d t", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until year-end: deputy PM", "url":
"https://radio.cgtn.com/podcast/news/5/Russia-to-extend-gasoline-export-ban-until-year-end-deputy-PM/2721269", "snippet": "From:\nSUBSCRIBE\nHeavy rain and strong winds batter southern China as Noul
makes landfall\nKyrgyz president meets Chinese FM\nOver 40 rescued after Vietnamese ship sinks in South China Sea\nDR Congo Ebola cases top 3,000\nProlonged power outages spark protests in
Libya\nRussia to extend gasoline export ban until year-end: deputy PM\nJapan sees temperatures over 40 degrees Celsius for record 5th straight day\nJordan's Aqaba Marine Reserve added to UNESCO World
Heritage List\nBeginning of dialog window. Es", "api_data": null, "hint": null}, {"title": "Russia Moves to Extend Gasoline Export Ban Until 2026 as Shortages Persist - The Moscow Times", "url":
"https://www.themoscowtimes.com/2025/09/25/russia-moves-to-extend-gasoline-export-ban-until-2026-as-shortages-show-no-sign-of-letting-up-a90619", "snippet": "Russia\u2019s government plans to extend
its ban on gasoline exports through the end of the year as shortages continue to hit the domestic market, Deputy Prime Minister Alexander Novak said on Thursday.\n\u201cIn the near future, we will
extend the ban on gasoline exports until the end of the year, and a ban on diesel fuel exports by non-producers will also be introduced until the end of the year,\u201d Novak
[told](https://tass.ru/ekonomika/25159143) state media, without specifying when an official announcemen", "api_data": null, "hint": null}, {"title": "Russia to Extend Gasoline Export Ban, May Lift
Diesel Ban | Energy Intelligence", "url": "https://www.energyintel.com/0000019f-a3e6-d20c-ad9f-a7f6a6060000", "snippet": "Nick N A/Shutterstock Save for later Print Download Share LinkedIn Twitter
Russia will extend its ban on gasoline exports for another five months, while similar restrictions on sales of diesel outside the country will be lifted \"as the market recovers,\" Deputy Prime
Minister Alexander Novak said over the weekend.", "api_data": null, "hint": null}, {"title": "Russia Extends Gasoline Export Ban, Plans to Lift Diesel Ban After Recovery - Bloomberg", "url":
"https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers", "snippet": null, "api_data": null, "hint": null}]}
```

## 💬 Response

This is very clear. Russia decided to extend the gasoline export ban through the end of 2026. Let me get more detail on the official resolution and specific dates.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Russia gasoline export ban resolution signed Mishustin end of 2026 producers"
}
```

### 📋 Result

```
{"query": "Russia gasoline export ban resolution signed Mishustin end of 2026 producers", "results": [{"title": "Mishustin allows Euro 3 gasoline sales across Russia until 2026 | Ukraine news -
#Mezha", "url": "https://mezha.net/eng/bukvy/43cb8657_mishustin_allows_euro_3/", "snippet": "Mishustin allows Euro 3 gasoline sales across Russia until 2026\n[\n]\n![Mishustin allows Euro 3 gasoline
sales across Russia until 2026 Mishustin allows Euro 3 gasoline sales across Russia until 2026](https://mezha.net/wp-content/uploads/2026/07/03/mishustin-dozvoliv-prodavati-benzin.webp)\nThe decree
allows higher sulfur Euro 3 fuel back into Russia to prevent shortages, raising immediate supply relief and longer term environmental concerns.\nAs reported by
[hromadske.ua](https://hromadske.ua/svit/", "api_data": null, "hint": null}, {"title": "2025\u20132026 Russian fuel crisis - Wikipedia", "url":
"https://en.wikipedia.org/wiki/2025%E2%80%932026_Russian_fuel_crisis", "snippet": "Starting in August 2025, increased Ukrainian drone attacks on Russian oil refineries during the Russo-Ukrainian War
caused widespread damage and a significant decrease in production of refined products across the Russian oil industry, leading to a fuel crisis in the country. The crisis escalated in the middle of
2026, with Russian-controlled Crimea declaring a state of emergency in June and banning fuel sales. \nBy July 2026, most of Russia's regions were experiencing fuel restrictions, directly ",
"api_data": {"content": [{"type": "text", "text": "{\"title\": \"2025\\u20132026 Russian fuel crisis\", \"url\": \"https://en.wikipedia.org/wiki/2025%E2%80%932026_Russian_fuel_crisis\", \"extract\":
\"Starting in August 2025, increased Ukrainian drone attacks on Russian oil refineries during the Russo-Ukrainian War caused widespread damage and a significant decrease in production of refined
products across the Russian oil industry, leading to a fuel crisis in the country. The crisis escalated in the middle of 2026, with Russian-controlled Crimea declaring a state of emergency in June and
banning fuel sales. \\nBy July 2026, most of Russia's regions were experiencing fuel restrictions, directly affecting 50 million people, approximately 35% of the Russian population. Russia suspended
civilian shipping through the Don\\u2013Azov Shipping Canal and the Kerch Strait following concentrated attacks on oil tankers in the Sea of Azov and surrounding anchorages. A decree was signed
allowing certain oil refineries to lower their production quality standards from Euro-5 gasoline to Euro-3 gasoline until the end of the year.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title":
"Russian govt bans gasoline exports by producers to end of July", "url": "https://interfax.com/newsroom/top-stories/116918/", "snippet": "Russian govt bans gasoline exports by producers to end of
July\nMOSCOW. April 2 (Interfax) - The Russian government said that it has extended the ban on gasoline exports in effect to the end of July to producers of the fuel.\nThe corresponding resolution has
been signed and takes effect on the day of its official publication.\n\"The decision was made to maintain a stable situation on the domestic fuel market during the period of high seasonal demand and
agricultural field work, as well as in light o", "api_data": null, "hint": null}, {"title": "Russia extends gasoline export ban through end of 2026 amid fuel shortages | RBC-Ukraine", "url":
"https://newsukraine.rbc.ua/news/russia-extends-gasoline-export-ban-through-1785010838.html", "snippet": "Russia extends gasoline export ban through 2026\n![Russia extends gasoline export ban through 
2026](https://newsukraine.rbc.ua/static/img/_/b/_benzin_cherga_zapravka_rosnafta__rosiya__gettyimages_2282016183_6c2659b580392f001e3ef9b290010017_1300x820_cd088116976fe081e99aa601e424a7b7_650x410.jpg)
\nRussia decided to extend its ban on gasoline exports for all producers through the end of 2026. At the same time, it plans to lift restrictions on diesel fuel exports, Russian Deputy Prime Minister
[Alexand", "api_data": null, "hint": null}, {"title": "Ban on gasoline exports from Russia extended to producers of petroleum products - Business & Economy - TASS", "url":
"https://tass.com/economy/2110669", "snippet": "MOSCOW, April 2. /TASS/. The Russian government has extended gasoline export restrictions effective until July 31, 2026, to direct producers of
petroleum products. The corresponding decree has been signed, the cabinet\u2019s press service reported.\n\"The decision was made to maintain a stable situation on the domestic fuel market during a
period of high seasonal demand and agricultural field work, as well as in connection with the rise in global oil prices due to the current geopolitical situation in ", "api_data": null, "hint": null},
{"title": "Russia extends ban on gasoline exports until end of year due to fuel crisis - Bloomberg | Ukrainian news", "url": "https://ukranews.com/en/news/1164925-russia-extends-ban-on-gasoline-
exports-until-end-of-year-due-to-fuel-crisis-bloomberg", "snippet": "The government of the aggressor country has decided to extend the ban on gasoline exports until the end of 2026. The restrictions
will apply to both direct producers and traders. This was stated by russian Vice Prime Minister Aleksandr Novak, [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-
diesel-export-ban-when-market-recovers) reports.\nThe reason for the fuel shortage in russia this summer was the regular strikes by Ukrainian forces on russian oil refiner", "api_data": null, "hint":
null}, {"title": "Russia to extend gasoline export ban until year-end: deputy PM-Xinhua", "url": "https://english.news.cn/20260726/4473ef9ef08c4c5c9ce699e9a835f405/c.html", "snippet": "MOSCOW, July 25
(Xinhua) -- Russia will extend its ban on gasoline exports through the end of 2026 to ensure stable domestic fuel supplies, Russia's Deputy Prime Minister Alexander Novak said on Saturday.\nSpeaking
to reporters in the Siberian city of Omsk, Novak said the decision was made at a government operational meeting and would apply to both gasoline producers and non-producers.\nHe added that the ban on
diesel exports would be lifted once the domestic market recovers, allowing oil refineri", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until end of year \u2014
Meduza", "url": "https://meduza.io/en/news/2026/07/27/russia-to-extend-gasoline-export-ban-until-end-of-year", "snippet": "Russia to extend gasoline export ban until end of year\nRussia will extend
its ban on gasoline exports until the end of 2026, Deputy Prime Minister Alexander Novak said, according to the Russian state news agency TASS.\n\u201cOn the gasoline export ban, we also decided at
the headquarters meeting to extend it for both producers and non-producers. That is, it will be extended until the end of the year,\u201d Novak said.\nNovak added that authorities would lift the
diesel export ban \u201cas the market recovers,\u201d t", "api_data": null, "hint": null}, {"title": "Russia Moves to Extend Gasoline Export Ban Until 2026 as Shortages Persist - The Moscow Times",
"url": "https://www.themoscowtimes.com/2025/09/25/russia-moves-to-extend-gasoline-export-ban-until-2026-as-shortages-show-no-sign-of-letting-up-a90619", "snippet": "Russia\u2019s government plans to
extend its ban on gasoline exports through the end of the year as shortages continue to hit the domestic market, Deputy Prime Minister Alexander Novak said on Thursday.\n\u201cIn the near future, we
will extend the ban on gasoline exports until the end of the year, and a ban on diesel fuel exports by non-producers will also be introduced until the end of the year,\u201d Novak
[told](https://tass.ru/ekonomika/25159143) state media, without specifying when an official announcemen", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Russia gasoline export ban Interfax quarter extension July 2026"
}
```

### 📋 Result

```
{"query": "Russia gasoline export ban Interfax quarter extension July 2026", "results": [{"title": "Russian govt bans gasoline exports by producers to end of July", "url":
"https://interfax.com/newsroom/top-stories/116918/", "snippet": "Russian govt bans gasoline exports by producers to end of July\nMOSCOW. April 2 (Interfax) - The Russian government said that it has
extended the ban on gasoline exports in effect to the end of July to producers of the fuel.\nThe corresponding resolution has been signed and takes effect on the day of its official
publication.\n\"The decision was made to maintain a stable situation on the domestic fuel market during the period of high seasonal demand and agricultural field work, as well as in light o",
"api_data": null, "hint": null}, {"title": "Russia to extend its petrol export ban until end of 2026, lift diesel export ban as market recovers - deputy PM", "url": "https://interfax.com/newsroom/top-
stories/118517/", "snippet": "Russia to extend its petrol export ban until end of 2026, lift diesel export ban as market recovers - deputy PM\nOMSK. July 27 (Interfax) - The Russian petrol export ban
will be extended until the end of this year, Deputy Prime Minister Alexander Novak told journalists on Saturday.\n\"In regard to the petrol export ban, at a headquarters [meeting] we also made a
decision to extend it both for producers and non-producers, i.e. it will be extended until the end of year,\" Novak said.\nAs for the diesel", "api_data": null, "hint": null}, {"title": "Ban on
gasoline exports from Russia extended to producers of petroleum products - Business & Economy - TASS", "url": "https://tass.com/economy/2110669", "snippet": "MOSCOW, April 2. /TASS/. The Russian
government has extended gasoline export restrictions effective until July 31, 2026, to direct producers of petroleum products. The corresponding decree has been signed, the cabinet\u2019s press
service reported.\n\"The decision was made to maintain a stable situation on the domestic fuel market during a period of high seasonal demand and agricultural field work, as well as in connection with
the rise in global oil prices due to the current geopolitical situation in ", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until year-end: deputy PM-Xinhua", "url":
"https://english.news.cn/20260726/4473ef9ef08c4c5c9ce699e9a835f405/c.html", "snippet": "MOSCOW, July 25 (Xinhua) -- Russia will extend its ban on gasoline exports through the end of 2026 to ensure
stable domestic fuel supplies, Russia's Deputy Prime Minister Alexander Novak said on Saturday.\nSpeaking to reporters in the Siberian city of Omsk, Novak said the decision was made at a government
operational meeting and would apply to both gasoline producers and non-producers.\nHe added that the ban on diesel exports would be lifted once the domestic market recovers, allowing oil refineri",
"api_data": null, "hint": null}, {"title": "Russia could re-impose gasoline export ban as prices rise - sources", "url": "https://interfax.com/newsroom/top-stories/116808/", "snippet": "Russia could
re-impose gasoline export ban as prices rise - sources\nMOSCOW. March 25 (Interfax) - The Russian authorities are discussing re-imposing the ban on gasoline exports for producers, sources with
knowledge of the situation told Interfax.\nA gasoline and diesel export ban for non-producers is in place until July 31, 2026.\nRussia needs to act as soon as possible to provide the domestic market
with fuel amid the global energy crisis, Deputy Prime Minister Alexander Novak said during an Ener", "api_data": null, "hint": null}, {"title": "Russia extends ban on gasoline exports until end of
year due to fuel crisis - Bloomberg | Ukrainian news", "url": "https://ukranews.com/en/news/1164925-russia-extends-ban-on-gasoline-exports-until-end-of-year-due-to-fuel-crisis-bloomberg", "snippet":
"The government of the aggressor country has decided to extend the ban on gasoline exports until the end of 2026. The restrictions will apply to both direct producers and traders. This was stated by
russian Vice Prime Minister Aleksandr Novak, [Bloomberg](https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers) reports.\nThe reason for the
fuel shortage in russia this summer was the regular strikes by Ukrainian forces on russian oil refiner", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until end of
year \u2014 Meduza", "url": "https://meduza.io/en/news/2026/07/27/russia-to-extend-gasoline-export-ban-until-end-of-year", "snippet": "Russia to extend gasoline export ban until end of year\nRussia
will extend its ban on gasoline exports until the end of 2026, Deputy Prime Minister Alexander Novak said, according to the Russian state news agency TASS.\n\u201cOn the gasoline export ban, we also
decided at the headquarters meeting to extend it for both producers and non-producers. That is, it will be extended until the end of the year,\u201d Novak said.\nNovak added that authorities would
lift the diesel export ban \u201cas the market recovers,\u201d t", "api_data": null, "hint": null}, {"title": "Russia Eyes Longer Diesel Export Ban as Ukraine Hits Oil Assets - Bloomberg", "url":
"https://www.bloomberg.com/news/articles/2026-07-23/russia-eyes-longer-diesel-export-ban-as-ukraine-hits-oil-assets", "snippet": null, "api_data": null, "hint": null}, {"title": "Russia Extends
Gasoline Export Ban, Plans to Lift Diesel Ban After Recovery - Bloomberg", "url": "https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers",
"snippet": null, "api_data": null, "hint": null}, {"title": "www.mexc.com", "url": "https://www.mexc.com/tr-CT/news/989393", "snippet": "Russia will ban gasoline export ban beginning April 1 and will
run until July 31, targeting domestic fuel price stability. Authorities confirmed the policy as a response to global energy volatility and increasing external market pressures affecting supply
chains.\nThe ban was announced following a government meeting led by Deputy Prime Minister Alexander Novak. The measure focuses on safeguarding domestic fuel availability during periods of global
uncertainty.\nAuthorities stated that the decision", "api_data": null, "hint": null}]}
```

## 💬 Response

I have strong confirmation. Let me verify whether the official government resolution (postanovlenie) was formally signed/published, as Novak's July 27 statement announced the decision but the formal decree may follow. Let me check the latest news for the actual signed resolution.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: WebFetch


```json
{
  "query": "Russia government resolution gasoline export ban signed extended December 31 2026 TASS"
}
```

### 📋 Result

```
{"query": "Russia government resolution gasoline export ban signed extended December 31 2026 TASS", "results": [{"title": "The Government extends temporary ban on exports of petrol, diesel, and other
fuels", "url": "http://government.ru/en/docs/57435/", "snippet": "Resolutions No. 2126 and No. 2150 of 25 December 2025 and 26 December 2025, respectively\nThe Government is continuing its efforts to
maintain stability in the domestic fuel market. Accordingly, a new resolution has extended the temporary ban on the export of motor petrol until 28 February 2026, inclusive. This prohibition will
apply to all exporters, including direct producers.\nAnother resolution has extended, until 28 February 2026, inclusive, the ban on the export of diesel, as well as marine ", "api_data": null, "hint":
null}, {"title": "Ban on gasoline exports from Russia extended to producers of petroleum products - Business & Economy - TASS", "url": "https://tass.com/economy/2110669", "snippet": "MOSCOW, April 2.
/TASS/. The Russian government has extended gasoline export restrictions effective until July 31, 2026, to direct producers of petroleum products. The corresponding decree has been signed, the
cabinet\u2019s press service reported.\n\"The decision was made to maintain a stable situation on the domestic fuel market during a period of high seasonal demand and agricultural field work, as well
as in connection with the rise in global oil prices due to the current geopolitical situation in ", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until end of year
\u2014 Meduza", "url": "https://meduza.io/amp/en/news/2026/07/27/russia-to-extend-gasoline-export-ban-until-end-of-year", "snippet": "Russia to extend gasoline export ban until end of year\nRussia
will extend its ban on gasoline exports until the end of 2026, Deputy Prime Minister Alexander Novak said, according to the Russian state news agency TASS.\n\u201cOn the gasoline export ban, we also
decided at the headquarters meeting to extend it for both producers and non-producers. That is, it will be extended until the end of the year,\u201d Novak said.\nNovak added that authorities would
lift the diesel export ban \u201cas the market recovers,\u201d t", "api_data": null, "hint": null}, {"title": "Russia extends gasoline export ban through end of 2026", "url": "https://en.apa.az/cis-
countries/russia-extends-gasoline-export-ban-through-end-of-2026-517594", "snippet": "The Russian government will extend its ban on gasoline exports until the end of 2026.\nRussian Deputy Prime
Minister Alexander Novak announced the decision while speaking to journalists.\n\"We have decided that the ban on gasoline exports will remain in force until the end of the year for both producers and
non-producers,\" Novak said.\nHe added that restrictions on diesel fuel exports would be lifted gradually as the domestic market stabilizes. According to Novak, the measure is intended to prevent ",
"api_data": null, "hint": null}, {"title": "Russia extends gasoline export ban", "url": "https://news.laodong.vn/the-gioi/nga-gia-han-cam-xuat-khau-xang-1741008.ldo", "snippet": "Russia extends
gasoline export ban\n[Russia](https://news.laodong.vn/the-gioi/nga-tuyen-bo-pha-huy-loat-uav-ma-ca-rong-cua-ukraina-1737378.ldo) extends gasoline export ban until the end of 2026.\n![Russia extends
gasoline export ban](https://media-cdn-v2.laodong.vn/storage/newsportal/2026/7/26/1741008/IMG_6928.jpeg?w=660)\nOn July 25 (Moscow time), according to TASS news agency, Russian Deputy Prime Minister
Alexander Novak said that the country's government will extend the ban on [gasoline exports", "api_data": null, "hint": null}, {"title": "Russia extends gasoline export ban until end of 2026, Novak
says | Ukraine news - #Mezha", "url": "https://mezha.net/eng/bukvy/3554f7b6_russia_extends_gasoline/", "snippet": "Russia extends gasoline export ban until end of 2026, Novak says\n[\n]\n![Russia
extends gasoline export ban until end of 2026, Novak says](https://mezha.net/wp-content/uploads/2026/07/25/russia-extends-gasoline-export.webp)\nDrivers are forming a queue, waiting to refuel their
cars at the Rosneft gas station in Moscow, July 3, 2026.\nMoscow will keep gasoline exports blocked through 2026 to protect domestic supplies. Officials say diesel exports will be lifted gradually as
the market recovers.\nAccor", "api_data": null, "hint": null}, {"title": "Russia to extend gasoline export ban until year-end: deputy PM-Xinhua", "url":
"https://english.news.cn/20260726/4473ef9ef08c4c5c9ce699e9a835f405/c.html", "snippet": "MOSCOW, July 25 (Xinhua) -- Russia will extend its ban on gasoline exports through the end of 2026 to ensure
stable domestic fuel supplies, Russia's Deputy Prime Minister Alexander Novak said on Saturday.\nSpeaking to reporters in the Siberian city of Omsk, Novak said the decision was made at a government
operational meeting and would apply to both gasoline producers and non-producers.\nHe added that the ban on diesel exports would be lifted once the domestic market recovers, allowing oil refineri",
"api_data": null, "hint": null}, {"title": "Russia extends ban on gasoline exports until end of year due to fuel crisis - Bloomberg | Ukrainian news", "url":
"https://ukranews.com/en/news/1164925-russia-extends-ban-on-gasoline-exports-until-end-of-year-due-to-fuel-crisis-bloomberg", "snippet": "The government of the aggressor country has decided to extend
the ban on gasoline exports until the end of 2026. The restrictions will apply to both direct producers and traders. This was stated by russian Vice Prime Minister Aleksandr Novak,
[Bloomberg](https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers) reports.\nThe reason for the fuel shortage in russia this summer was the
regular strikes by Ukrainian forces on russian oil refiner", "api_data": null, "hint": null}, {"title": "European Parliament resolution of 17 December 2025 on phasing out Russian natural gas imports",
"url": "https://en.wikipedia.org/wiki/European_Parliament_resolution_of_17_December_2025_on_phasing_out_Russian_natural_gas_imports", "snippet": "The European Parliament legislative resolution of 17
December 2025 on phasing out Russian natural gas imports is a first-reading position adopted by the European Parliament on a European Commission proposal for a regulation that would ban imports of
Russian natural gas by late 2027.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"European Parliament resolution of 17 December 2025 on phasing out Russian natural gas imports\",
\"url\": \"https://en.wikipedia.org/wiki/European_Parliament_resolution_of_17_December_2025_on_phasing_out_Russian_natural_gas_imports\", \"extract\": \"The European Parliament legislative resolution
of 17 December 2025 on phasing out Russian natural gas imports is a first-reading position adopted by the European Parliament on a European Commission proposal for a regulation that would ban imports
of Russian natural gas by late 2027.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Russia to extend ban on gasoline exports until year-end \u2014 deputy premier - Business & Economy - TASS",
"url": "https://tass.com/economy/2165321", "snippet": "OMSK, July 25. /TASS/. The ban on gasoline exports from Russia will be extended until the end of the year, Russian Deputy Prime Minister
Alexander Novak said.\n\"Regarding the ban on gasoline exports, we also made the decision to extend it for both manufacturers and non-manufacturers. Therefore, it will be extended until the end of the
year,\" he told reporters.\nThe deputy premier added that diesel exports will be lifted \"as the market rebounds.\"\nFuel production in Russia has been partially reduced", "api_data": null, "hint":
null}]}
```

```json
{
  "url": "https://interfax.com/newsroom/top-stories/118517/",
  "prompt": "Extract details about Russia's gasoline/petrol export ban extension: exact dates, whether a resolution was signed, effective through what date, producers and non-producers coverage."
}
```

### 📋 Result

```
# Russia's Petrol Export Ban Extension

**Announcement Date:** July 27, 2026

**Key Details:**

**Petrol Ban:** According to Deputy PM Alexander Novak, the petrol export ban will be "extended until the end of this year" and applies to "both producers and non-producers."

**Effective Through:** December 31, 2026

**Resolution Status:** The article does not specify whether a formal resolution was signed. Novak stated that "at a headquarters [meeting] we also made a decision to extend it," but no documentation
of an official decree or resolution is mentioned.

**Diesel Ban:** Unlike the petrol ban, the diesel export restriction will be lifted "as the market recovers," according to Novak's comments. The rationale is to prevent refineries from facing surplus
inventory issues.

**Context:** The previous fuel export ban was set to expire on July 31, 2026. The government implemented these measures in response to summer fuel supply disruptions caused by logistics changes.
```

## 💬 Response

I have comprehensive, well-cross-validated findings. Let me provide the synthesis.

## Research Report: Russia's Gasoline Export Ban Beyond July 31, 2026

### Bottom Line

**Yes — Russia decided to extend its gasoline (motor petrol) export ban beyond July 31, 2026, and specifically extended it through the end of 2026 (December 31, 2026), not merely for August or one quarter.** The extension covers **both producers and non-producers**. The decision was announced by Deputy Prime Minister Alexander Novak on **Saturday, July 25–27, 2026** (reported by TASS on July 25 from Omsk; Interfax and Meduza reporting July 27).

### Key Details

**The extension decision:**
- Deputy PM Alexander Novak, speaking to reporters in Omsk, stated: *"Regarding the ban on gasoline exports, we also made the decision to extend it for both manufacturers and non-manufacturers. Therefore, it will be extended until the end of the year"* (TASS, July 25, 2026).
- The decision was made at a government "headquarters"/operational meeting (штаб).
- Coverage: **both producers and non-producers** (a full ban on all gasoline exports).
- This goes **beyond** the "full quarter" that Interfax had earlier reported as "almost decided" — the actual extension runs through the end of 2026.

**Prior legal basis (context provided):**
- The producer gasoline export ban had been extended to run until **July 31, 2026** via a decree signed and reported by TASS/Interfax on **April 2, 2026**. (This aligns with the Resolution No. 78 / No. 362 framework referenced in the question.)
- The non-producer gasoline and diesel export ban was also in place until July 31, 2026.

**Diesel treatment (differs from gasoline):**
- Novak said the **diesel** export ban would be lifted **"as the market recovers,"** to prevent refinery oversupply — a divergence from the gasoline policy.

**Resolution/postanovlenie status:**
- As of the reporting (July 25–27, 2026), sources documented the **government decision** (announced by Novak) to extend the ban through year-end. The Interfax article (July 27) and Meduza confirm the decision but do **not** explicitly cite a formally signed/published postanovlenie number for the year-end gasoline extension in these late-July reports. The pattern historically (e.g., April 2 producer ban, December 2025 Resolutions No. 2126/No. 2150) is that a formal government resolution is signed and takes effect on the day of official publication shortly after the announcement.
- I did not find in these searches a specific published resolution number for the December-2026 gasoline extension, but the substantive government decision to extend beyond July 31, 2026 (through Dec 31, 2026) is firmly and repeatedly confirmed across TASS, Interfax, Bloomberg, Xinhua, Meduza, and RBC-Ukraine.

### Underlying Cause
The extension responds to Russia's 2025–2026 fuel crisis: intensified Ukrainian drone strikes on refineries reduced refined-product output; by July 2026 most Russian regions faced fuel restrictions affecting ~50 million people (~35% of population). A separate decree also allowed refineries to sell lower-grade Euro-3 gasoline (down from Euro-5) through year-end.

## 🔧 Tool: StructuredOutput


```json
{
  "answer": "Yes \u2014 Russia decided to extend its gasoline (motor petrol) export ban beyond July 31, 2026, extending it through the end of 2026 (December 31, 2026), covering both producers and non-producers. This exceeds the \"one quarter\" that Interfax had earlier reported as \"almost decided.\"\n\nThe decision was announced by Deputy Prime Minister Alexander Novak in Omsk on Saturday, reported by TASS on July 25, 2026, and by Interfax and Meduza on July 27, 2026. Novak stated: \"Regarding the ban on gasoline exports, we also made the decision to extend it for both manufacturers and non-manufacturers. Therefore, it will be extended until the end of the year.\" Diesel exports, by contrast, will be lifted \"as the market recovers\" to avoid refinery oversupply.\n\nThe prior producer gasoline export ban ran until July 31, 2026 (extended via a decree signed and reported April 2, 2026, consistent with the Resolution No. 78/No. 362 framework). The non-producer gasoline/diesel ban was likewise in place until July 31, 2026.\n\nOn the formal resolution (postanovlenie): as of the late-July reporting, sources document the government's decision (via Novak) to extend the ban through year-end, but these late-July articles do not cite a specific published resolution number for the year-end gasoline extension. Historically (e.g., the April 2 producer ban, and Resolutions No. 2126/No. 2150 of December 2025), a formal government resolution is signed and takes effect on its day of official publication shortly after such announcements. The substantive government decision to extend beyond July 31 (through Dec 31, 2026) is firmly and repeatedly confirmed across TASS, Interfax, Bloomberg, Xinhua, Meduza, and RBC-Ukraine.\n\nCause: the 2025\u20132026 Russian fuel crisis, driven by Ukrainian drone strikes on refineries; by July 2026 most regions faced fuel restrictions affecting ~50 million people (~35% of population). A separate decree also permitted lower-grade Euro-3 gasoline sales through year-end.</answer>\n<data_points>[{\"metric\": \"Gasoline export ban new end date (extension)\", \"value\": 20261231, \"unit\": \"date (YYYYMMDD)\", \"as_of\": \"2026-07-25\", \"source_url\": \"https://tass.com/economy/2165321\"}, {\"metric\": \"Prior gasoline export ban end date (pre-extension)\", \"value\": 20260731, \"unit\": \"date (YYYYMMDD)\", \"as_of\": \"2026-04-02\", \"source_url\": \"https://tass.com/economy/2110669\"}, {\"metric\": \"Russians affected by fuel restrictions (July 2026)\", \"value\": 50000000, \"unit\": \"people\", \"as_of\": \"2026-07-01\", \"source_url\": \"https://en.wikipedia.org/wiki/2025%E2%80%932026_Russian_fuel_crisis\"}, {\"metric\": \"Share of Russian population affected by fuel restrictions\", \"value\": 35, \"unit\": \"percent\", \"as_of\": \"2026-07-01\", \"source_url\": \"https://en.wikipedia.org/wiki/2025%E2%80%932026_Russian_fuel_crisis\"}]</data_points>\n<key_facts>[\"Russia extended its gasoline (motor petrol) export ban beyond July 31, 2026, through December 31, 2026 (end of year), covering both producers and non-producers.\", \"The decision was announced by Deputy PM Alexander Novak in Omsk, reported by TASS on July 25, 2026 and by Interfax/Meduza on July 27, 2026, made at a government headquarters/operational meeting.\", \"This exceeds the 'full quarter' extension Interfax had earlier reported as 'almost decided' \u2014 the ban was extended through year-end.\", \"Diesel export ban treated differently: to be lifted 'as the market recovers' to avoid refinery oversupply.\", \"Prior producer gasoline ban ran until July 31, 2026 via a decree signed/reported April 2, 2026 (consistent with Resolution No. 78/No. 362 framework).\", \"Late-July reports confirm the government decision but do not cite a specific published postanovlenie number for the year-end gasoline extension; a formal resolution typically follows and takes effect on its official publication date.\", \"Driver: 2025\u20132026 Russian fuel crisis from Ukrainian drone strikes on refineries; by July 2026 most regions had fuel restrictions affecting ~50M people (~35% of population).\", \"A separate decree allowed lower-grade Euro-3 gasoline sales through year-end to ease shortages.\"]</key_facts>\n<sources>[{\"url\": \"https://tass.com/economy/2165321\", \"title\": \"Russia to extend ban on gasoline exports until year-end \u2014 deputy premier\", \"domain\": \"tass.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"The ban on gasoline exports from Russia will be extended until the end of the year... it will be extended for both manufacturers and non-manufacturers.\"}, {\"url\": \"https://interfax.com/newsroom/top-stories/118517/\", \"title\": \"Russia to extend its petrol export ban until end of 2026, lift diesel export ban as market recovers - deputy PM\", \"domain\": \"interfax.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"The Russian petrol export ban will be extended until the end of this year... extended both for producers and non-producers.\"}, {\"url\": \"https://tass.com/economy/2110669\", \"title\": \"Ban on gasoline exports from Russia extended to producers of petroleum products\", \"domain\": \"tass.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"The Russian government has extended gasoline export restrictions effective until July 31, 2026, to direct producers of petroleum products. The corresponding decree has been signed.\"}, {\"url\": \"https://meduza.io/en/news/2026/07/27/russia-to-extend-gasoline-export-ban-until-end-of-year\", \"title\": \"Russia to extend gasoline export ban until end of year\", \"domain\": \"meduza.io\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"Russia will extend its ban on gasoline exports until the end of 2026, Deputy Prime Minister Alexander Novak said, according to TASS.\"}, {\"url\": \"https://english.news.cn/20260726/4473ef9ef08c4c5c9ce699e9a835f405/c.html\", \"title\": \"Russia to extend gasoline export ban until year-end: deputy PM\", \"domain\": \"english.news.cn\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"Russia will extend its ban on gasoline exports through the end of 2026 to ensure stable domestic fuel supplies... apply to both gasoline producers and non-producers.\"}, {\"url\": \"https://www.bloomberg.com/news/articles/2026-07-25/russia-says-it-will-end-diesel-export-ban-when-market-recovers\", \"title\": \"Russia Extends Gasoline Export Ban, Plans to Lift Diesel Ban After Recovery\", \"domain\": \"bloomberg.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"Government decided to extend the ban on gasoline exports until the end of 2026, applying to both direct producers and traders.\"}, {\"url\": \"https://newsukraine.rbc.ua/news/russia-extends-gasoline-export-ban-through-1785010838.html\", \"title\": \"Russia extends gasoline export ban through end of 2026 amid fuel shortages\", \"domain\": \"newsukraine.rbc.ua\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"Russia decided to extend its ban on gasoline exports for all producers through the end of 2026, plans to lift diesel restrictions.\"}, {\"url\": \"https://interfax.com/newsroom/top-stories/116808/\", \"title\": \"Russia could re-impose gasoline export ban as prices rise - sources\", \"domain\": \"interfax.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"Russian authorities discussing re-imposing the gasoline export ban for producers; non-producer ban in place until July 31, 2026.\"}, {\"url\": \"https://interfax.com/newsroom/top-stories/116918/\", \"title\": \"Russian govt bans gasoline exports by producers to end of July\", \"domain\": \"interfax.com\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"The Russian government extended the ban on gasoline exports to end of July to producers; resolution signed, takes effect on official publication.\"}, {\"url\": \"http://government.ru/en/docs/57435/\", \"title\": \"The Government extends temporary ban on exports of petrol, diesel, and other fuels (Resolutions No. 2126 and No. 2150)\", \"domain\": \"government.ru\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"A new resolution extended the temporary ban on the export of motor petrol; applies to all exporters including direct producers.\"}, {\"url\": \"https://en.wikipedia.org/wiki/2025%E2%80%932026_Russian_fuel_crisis\", \"title\": \"2025\u20132026 Russian fuel crisis\", \"domain\": \"en.wikipedia.org\", \"accessed_at\": \"2026-07-28\", \"snippet\": \"By July 2026 most of Russia's regions were experiencing fuel restrictions, affecting 50 million people, ~35% of population; Euro-5 to Euro-3 downgrade decree signed.\"}]</sources>\n</invoke>\n"
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

I've completed the research. Here's the summary:

**Answer: Yes — Russia extended its gasoline export ban beyond July 31, 2026, all the way through the end of 2026 (December 31, 2026).**

Key findings:
- **Deputy PM Alexander Novak announced the decision** in Omsk on July 25, 2026 (reported by TASS July 25; Interfax and Meduza July 27): the gasoline/petrol export ban is extended "until the end of the year" for **both producers and non-producers**.
- This **exceeds** the "full quarter" that Interfax had earlier reported as "almost decided" — the actual extension runs through year-end.
- **Diesel** is treated differently: to be lifted "as the market recovers."
- The prior producer ban ran to July 31, 2026 (per the April 2, 2026 decree, consistent with the Resolution No. 78/No. 362 framework you cited).

**One caveat on the formal postanovlenie:** The late-July reporting confirms the government's *decision* (via Novak's statement at a headquarters meeting), but these articles do not cite a specific published resolution number for the year-end gasoline extension. Historically, the formal government resolution is signed and takes effect on its official publication date shortly after such announcements — but I could not confirm a specific published postanovlenie number/date for the year-end extension in these searches. The substantive extension decision itself is firmly cross-validated across TASS, Interfax, Bloomberg, Xinhua, Meduza, and RBC-Ukraine.


### ↳ End nested research agent trace

## 💭 Thinking



## 💬 Response

The research confirms the key fact. Let me checkpoint and finalize.
