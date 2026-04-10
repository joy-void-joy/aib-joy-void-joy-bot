# Reasoning Log: Will Waymo make fully autonomous rides available to public riders in any of these cities before May 1, 2026?

*Generated: 2026-04-10T16:45:45.042463+00:00*


## 💭 Thinking

Let me analyze this forecasting question about Waymo making fully autonomous rides available in specific cities before May 1, 2026.

Key details:
- Question published: April 10, 2026
- Scheduled close: April 10, 2026 at 18:00 UTC
- Resolution: May 1, 2026
- Cities listed: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, or Washington, DC
- Resolution source: Waymo's "Where Waymo is driving" tracker at waymo.com/rides/#rides-map

The question was just published today (April 10, 2026) and closes today. 

So I have until May 1st to determine if Waymo has launched fully autonomous rides in any of these cities. Let me check their current operations across these locations.

## 💬 Response

I'll start by parsing the resolution criteria carefully, then research the current state of Waymo's operations in these cities.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43124
  ]
}
```

### 📋 Result

```
{"post_id": 43124, "title": "Will Waymo make fully autonomous rides available to public riders in any of these cities before May 1, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/43124", "background_info": "[Next stop for Waymo One: Washington, D.C.](https://waymo.com/rides/#rides-map): \n\n>\"It\u2019s official: Waymo One, the world\u2019s
leading fully autonomous ride-hailing service, will be ready for riders in the nation\u2019s capital on the Waymo One app in 2026.\n\n>We\u2019re laying the groundwork for our fully autonomous ride-
hailing service after returning to Washington, D.C. earlier this year, and we\u2019ll continue introducing ourselves to D.C.\u2019s communities and emergency responders over the coming months.
We\u2019ll also continue to work closely with policymakers to formalize the regulations needed to operate without a human behind the wheel in the District.\n\n>\u201cWaymo One is making fully
autonomous driving a reality for millions of people across the U.S.\u201d said Waymo co-CEO Tekedra Mawakana. \u201cWe\u2019re excited to bring the comfort, consistency, and safety of Waymo One to
Washingtonians, those who work and play in the city every day, and the millions of people from around the world who travel to the District every
year.\u201d\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"bf5652bf95baac8a\",\"sheet_id\":534.0}}`", "resolution_criteria": "This question resolves as **Yes** if Waymo at its
[Where Waymo is driving](https://waymo.com/rides/#rides-map) tracker reports that it is serving riders in any of these cities: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New
York, Seattle or Washington, DC", "fine_print": "", "num_forecasters": 6, "community_prediction": null}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://waymo.com/rides/#rides-map",
  "prompt": "Which cities does Waymo currently serve riders in? What cities are listed on the map? Is Waymo serving riders in any of these cities: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, Washington DC?"
}
```

### 📋 Result

```
{"url": "https://waymo.com/rides/#rides-map", "content": "Based on the content provided:\n\n**Cities where Waymo currently serves riders:**\nThe content states that Waymo is \"safely operating a fully
autonomous, publicly available ride-hailing service\" in:\n- Phoenix, AZ\n- San Francisco, CA (Bay Area)\n- Los Angeles, CA\n\n**Cities listed on the map:**\nThe map shows a comprehensive list of US
cities and some international locations, divided into \"Serving Riders In\" and \"Up Next\" categories, though the content doesn't specify which cities fall into which category. The US cities listed
are:\n- San Francisco Bay Area, Sacramento, Los Angeles, San Diego (CA)\n- Seattle (WA)\n- Las Vegas, Phoenix (AZ/NV)\n- Denver (CO)\n- San Antonio, Austin, Dallas, Houston (TX)\n- Minneapolis (MN)\n-
St. Louis (MO)\n- New Orleans (LA)\n- Chicago, Detroit (IL/MI)\n- Nashville, Atlanta, Charlotte (TN/GA/NC)\n- Pittsburgh, Philadelphia (PA)\n- Tampa, Orlando, Miami (FL)\n- Washington DC, Baltimore
(MD)\n- New York (NY)\n- Boston (MA)\n\nInternational: Tokyo (Japan), London (UK)\n\n**Regarding the specific cities you asked about:**\nAll of them appear on the map list: Baltimore, Boston,
Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, and Washington DC. However, the content doesn't clearly indicate which are currently serving riders versus \"up next,\" except that
Phoenix, San Francisco, and Los Angeles are confirmed as currently operational.\n\n**Relevant links:**\n- [Visit FAQs](https://waymo.com/faq)\n- [Learn why Eva chooses
Waymo](https://blog.waymo.com/2022/09/why-i-ride-with-waymo-eva)\n- [Learn more about community partners](https://waymo.com/community)", "title": "Ride-Hailing App - Make the Most of Your Drive -
Waymo"}
```

```json
{
  "query": "Waymo fully autonomous rides 2026 new cities launch"
}
```

### 📋 Result

```
{"query": "Waymo fully autonomous rides 2026 new cities launch", "results": [{"title": "Ready to Ride: Dallas, Houston, San Antonio, and Orlando", "url": "https://waymo.com/blog/2026/02/dallas-
houston-san-antonio-orlando/", "snippet": "[Back](https://waymo.com/blog)\nReady to Ride: Dallas, Houston, San Antonio, and Orlando\nToday, we continue our accelerated growth and welcome the first
public riders into our fully autonomous ride-hailing service in four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the public in
multiple cities simultaneously, this brings our total commercial metro areas to 10, and deepens our commitment in the states of Texas and Florida.\nSelect ri", "api_data": null, "hint": null},
{"title": "Waymo Updates | Get updates on cities Waymo serves", "url": "https://waymo.com/updates/", "snippet": "Waymo is coming soon to your city\nKeep in touch\nThank you. You\u2019re all
set.\nThank you for joining us on our journey. We're excited to keep you in the loop as we bring the safety and mobility benefits of the Waymo Driver to more communities.\n- San Francisco Bay Area,
CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle, WA\n- San Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver, CO\n- San Antonio, TX\n- Austin, TX\n- Dallas, TX\n- Houston, TX\n- Minneapolis,
MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL", "api_data": null, "hint": null}, {"title": "Waymo ride quietly arrives in a new key U.S. city - TheStreet", "url":
"https://www.thestreet.com/automotive/waymo-ride-quietly-arrives-in-a-new-key-us-city-nashville", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo: Where it\u2019s available,
upcoming cities, and new features [Feb 2026]", "url": "https://9to5google.com/2026/02/24/waymo-new-cities-features/", "snippet": "![](https://9to5google.com/wp-content/uploads/sites/4/2023/09/waymo-
cover-1.jpg?quality=82&strip=all&w=1600)\nWaymo autonomous vehicles date back to Google\u2019s self-driving car project that started in 2009. As of today, you can get a ride in 10 cities across the
US.\nTable of contents\nWhere Waymo is fully available\nUsing the Waymo app on [Android](https://play.google.com/store/apps/details?id=com.waymo.carapp) and
[iOS](https://apps.apple.com/us/app/waymo/id1343524838), you can hail a ride in Phoeni", "api_data": null, "hint": null}, {"title": "Waymo says it will launch in more Texas and Florida cities in
2026", "url": "https://www.cnbc.com/2025/11/18/waymo-texas-florida-2026.html", "snippet": "Waymo on Tuesday said it will bring its robotaxi service to new cities in Texas and Florida in 2026.\nThe
[Alphabet](https://www.cnbc.com/quotes/GOOG/)-owned company said it plans to start operating its vehicles with no human driver assistants in Dallas, Houston, San Antonio, Miami and Orlando in the
coming weeks before opening service in those markets to the public next year, the company said in a [blog](https://waymo.com/blog/2025/11/safe-routine-ready-autonomous-driving-in-new-cities).\n\"Waymo
", "api_data": null, "hint": null}, {"title": "Waymo Expands Fully Autonomous Ride Hailing to 4 Cities: Dallas, Houston, San Antonio, Orlando \u2014 2026 Launch Analysis | AI News Detail", "url":
"https://blockchain.news/ainews/waymo-expands-fully-autonomous-ride-hailing-to-4-cities-dallas-houston-san-antonio-orlando-2026-launch-analysis", "snippet": "Waymo Expands Fully Autonomous Ride
Hailing to 4 Cities: Dallas, Houston, San Antonio, Orlando \u2014 2026 Launch Analysis\n![Waymo Expands Fully Autonomous Ride Hailing to 4 Cities: Dallas, Houston, San Antonio, Orlando \u2014 2026
Launch Analysis](https://blockchainstock.blob.core.windows.net:443/features/2242046FCF14090589D5A49FFC590D13A9AF6032D71ECDBD82C9F012CD661799.jpg)\nAccording to Sawyer Merritt on X, Waymo has begun
serving its first public riders with fully autonomous robotaxis in Dallas, Houston", "api_data": null, "hint": null}, {"title": "Waymo robotaxis are now operating in 10 US cities | TechCrunch", "url":
"https://techcrunch.com/2026/02/24/waymo-robotaxis-are-now-operating-in-10-us-cities/", "snippet": "Waymo is opening its robotaxi services to the public in Dallas, Houston, San Antonio, and Orlando,
as the Alphabet-owned autonomous vehicle company quickens its pace of expansion.\nWaymo\u2019s rollout will mimic its public launches in previous cities. Select riders who have downloaded the Waymo
app will receive an invitation to take their first rides, starting Tuesday. New riders will be added on a rolling basis, and eventually anyone who downloads the app will be able to hail a ride.\nThe
addition of", "api_data": null, "hint": null}, {"title": "Beginning fully autonomous operations with the 6th-generation Waymo Driver", "url": "https://waymo.com/blog/2026/02/ro-on-6th-gen-waymo-
driver/", "snippet": "[Back](https://waymo.com/blog)\nBeginning fully autonomous operations with the 6th-generation Waymo Driver\nWaymo will begin fully autonomous operations with its 6th-generation
Driver \u2014an important step in bringing our technology to more riders in more cities. This latest system serves as the primary engine for our next era of expansion, with a streamlined configuration
that drives down costs while maintaining our uncompromising safety standards. Designed for long-term growth across multiple vehic", "api_data": null, "hint": null}, {"title": "Waymo ride quietly
arrives in a new key U.S. city - Madres Travels", "url": "https://wp.madrestravels.com/2026/04/08/waymo-ride-quietly-arrives-in-a-new-key-u-s-city/", "snippet": "Think about opening an app, reserving
a journey, and a automobile with no driver reveals as much as take you to a long-awaited errand. That\u2019s now not an idea. It\u2019s a actuality in Nashville.\nWaymo, a subsidiary of Alphabet Inc.,
is a U.S.-based autonomous driving expertise firm headquartered in Mountain View, California.\nAs of March 2026, Waymo operates business robotaxi companies throughout 10 main U.S. metropolitan areas,
with a fleet of about 3,000 automobiles. Waymo additionally delivers roug", "api_data": null, "hint": null}, {"title": "Why 2026 could be Waymo's year", "url":
"https://finance.yahoo.com/news/why-2026-could-be-waymos-year-195850263.html", "snippet": "From Los Angeles to Austin to Atlanta, Waymo robotaxis are everywhere. And 2026 could be the year Waymo
expands its lead in the space.\nWaymo, part of Alphabet (GOOG, GOOGL), began in 2009 as an in-house startup within Google's X initiative and officially became Waymo in 2016. In 2018, Waymo and Jaguar
paired up, using the British automaker's I-Pace EV for its testing. This is the vehicle most users are accustomed to seeing.\nSince 2020, anyone in its service area can download the Waymo app and ha",
"api_data": null, "hint": null}]}
```

## 💬 Response

Good, I'm getting a clearer picture. Let me dig deeper into which cities Waymo currently serves and which are "up next," focusing on the specific cities in the question.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://9to5google.com/2026/02/24/waymo-new-cities-features/",
  "prompt": "Which cities does Waymo currently serve riders in as of this article? Which cities are coming next? Is Waymo serving in any of: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, Washington DC?"
}
```

### 📋 Result

```
{"url": "https://9to5google.com/2026/02/24/waymo-new-cities-features/", "content": "Based on the article:\n\n**Cities Waymo currently serves riders in (as of February 2026):**\n\n*Fully available:*\n-
Phoenix, AZ\n- San Francisco Bay Area, CA\n- Los Angeles, CA\n- Atlanta, GA (via Uber partnership)\n- Austin, TX (via Uber partnership)\n\n*Early access (rolling invitations):*\n- Miami, FL\n- Dallas,
TX\n- Houston, TX\n- San Antonio, TX\n- Orlando, FL\n\n**Cities coming next (announced expansions):**\n- Denver, CO\n- Detroit, MI\n- Las Vegas, NV\n- Nashville, TN (2026 with Lyft)\n- San Diego,
CA\n- Washington, DC (2026)\n- London, UK (2026, first international expansion)\n\n**From your list:**\n- **Currently serving:** Detroit (upcoming, announced), Denver (upcoming, announced), Las Vegas
(upcoming, announced), Washington DC (upcoming, announced for 2026)\n- **Testing only (not yet serving riders):** Baltimore, Boston, New York, Seattle\n- **Not mentioned:** Charlotte,
Chicago\n\n**Relevant links:**\n- [Waymo Android app](https://play.google.com/store/apps/details?id=com.waymo.carapp)\n- [Waymo iOS app](https://apps.apple.com/us/app/waymo/id1343524838)\n- [Miami
launch announcement](https://waymo.com/blog/2026/01/miami-your-waymo-ride-is-ready)\n- [Dallas, Houston, San Antonio, Orlando announcement](https://waymo.com/blog/2026/02/dallas-houston-san-antonio-
orlando)\n- [Waymo London 2026 expansion](https://9to5google.com/2025/10/15/waymo-london-2026/)", "title": "Waymo: Where it\u2019s available, upcoming cities, and new features [Feb 2026]"}
```

```json
{
  "query": "Waymo Austin Atlanta Nashville launch 2026 serving riders"
}
```

### 📋 Result

```
{"query": "Waymo Austin Atlanta Nashville launch 2026 serving riders", "results": [{"title": "Waymo opens robotaxi service in Nashville, partners with Lyft | TechCrunch", "url":
"https://techcrunch.com/2026/04/07/waymo-opens-robotaxi-service-in-nashville-partners-with-lyft/", "snippet": "Waymo has been in [Nashville for months](https://techcrunch.com/2025/09/17/lyft-and-
waymo-are-partnering-to-bring-robotaxis-to-nashville/), first manually driving, then testing its self-driving software with a human safety operator behind the wheel \u2014 all in preparation of
launching a robotaxi service in the city. That day has arrived, making Nashville the 11th city where the public can hail a Waymo robotaxi.\nWaymo said Tuesday it has opened its robotaxi service to the
public. However, Waymo is s", "api_data": null, "hint": null}, {"title": "Your Waymo ride, now arriving in Nashville", "url": "https://waymo.com/blog/2026/04/your-waymo-ride-now-arriving-in-
nashville/", "snippet": "[Back](https://waymo.com/blog)\nYour Waymo ride, now arriving in Nashville\nStarting today, Waymo is welcoming the first public riders into our fully autonomous ride-hailing
service in Nashville. Download the Waymo app and get ready to ride, as we begin inviting riders on a rolling basis. This approach allows us to thoughtfully scale while delivering a consistent, high-
quality experience.\nWaymo offers a new way to move through Nashville\u2014whether you\u2019re catching a show, meeting friends, or exploring", "api_data": null, "hint": null}, {"title": "Waymo says
it will launch in more Texas and Florida cities in 2026", "url": "https://www.cnbc.com/2025/11/18/waymo-texas-florida-2026.html", "snippet": "Waymo on Tuesday said it will bring its robotaxi service
to new cities in Texas and Florida in 2026.\nThe [Alphabet](https://www.cnbc.com/quotes/GOOG/)-owned company said it plans to start operating its vehicles with no human driver assistants in Dallas,
Houston, San Antonio, Miami and Orlando in the coming weeks before opening service in those markets to the public next year, the company said in a [blog](https://waymo.com/blog/2025/11/safe-routine-
ready-autonomous-driving-in-new-cities).\n\"Waymo ", "api_data": null, "hint": null}, {"title": "Lyft and Waymo Launch Partnership in Nashville", "url": "https://www.lyft.com/blog/posts/lyft-and-
waymo-launch-partnership-to-expand-autonomous-mobility-to-nashville", "snippet": "Waymo and Lyft to expand to Nashville next year, with Lyft's Flexdrive managing Waymo\u2019s fully autonomous
vehicles.\nSept. 17, 2025 - SAN FRANCISCO - Lyft, a global mobility platform, and Waymo, the world\u2019s leading autonomous driving technology company, today announced a new partnership to bring
Waymo\u2019s fully autonomous ride-hailing service to Nashville in 2026.\nThis new collaboration will leverage Lyft's proprietary [integrated fleet management
services](https://www.lyft.com/blog/posts/beyond-the", "api_data": null, "hint": null}, {"title": "Waymo Service Areas in the US: A Definitive Guide - Fifth Level Consulting", "url":
"https://fifthlevelconsulting.com/waymo-service-areas-in-the-u-s/", "snippet": "Last updated: November 2025\n[Waymo ](https://fifthlevelconsulting.com/autonomous-vehicles-10-amazing-things-to-know-
about-waymo/)operates commercial robotaxi services available to the public through its Waymo One app in several major U.S. cities. The Alphabet-owned company currently provides over 250,000 paid rides
per week, marking a significant milestone in [autonomous vehicle adoption](https://fifthlevelconsulting.com/key-components-of-autonomous-vehicles/). These [Waymo rides](https://fifthl", "api_data":
null, "hint": null}, {"title": "Scaling our fleet through U.S. manufacturing", "url": "https://waymo.com/blog/2025/05/scaling-our-fleet-through-us-manufacturing/", "snippet":
"[Back](https://waymo.com/blog)\nScaling our fleet through U.S. manufacturing\nThe U.S. is leading the world in the development and deployment of autonomous driving technology. Today, Waymo One
provides more than 250,000 paid trips each week across Phoenix, San Francisco, Los Angeles, and Austin, and we\u2019re preparing to bring our fully autonomous ride-hailing to Atlanta, Miami, and
Washington, D.C. in 2026. We\u2019re proud to bring this technology \u2013 once thought to be the stuff of science fiction \u2013 to m", "api_data": null, "hint": null}, {"title": "Waymo launches
autonomous ride service in Nashville", "url": "https://www.wsmv.com/2026/04/07/waymo-launches-autonomous-ride-service-nashville/", "snippet": "Waymo launches autonomous ride service in Nashville\nThe
rideshare company is now welcoming members of the public to use its service in Nashville.\nNASHVILLE, Tenn. (WSMV) - [Waymo](https://www.wsmv.com/2025/09/17/new-driverless-rideshare-service-coming-
nashville-roads/) will begin welcoming its first public riders [in Nashville](https://www.wsmv.com/2026/02/05/driverless-waymo-vehicles-start-operating-parts-nashville-this-month-police-say/) starting
Tuesday, Apr. 7.\nThe company said thousands of ", "api_data": null, "hint": null}, {"title": "Waymo ride quietly arrives in a new key U.S. city - Madres Travels", "url":
"https://wp.madrestravels.com/2026/04/08/waymo-ride-quietly-arrives-in-a-new-key-u-s-city/", "snippet": "Think about opening an app, reserving a journey, and a automobile with no driver reveals as
much as take you to a long-awaited errand. That\u2019s now not an idea. It\u2019s a actuality in Nashville.\nWaymo, a subsidiary of Alphabet Inc., is a U.S.-based autonomous driving expertise firm
headquartered in Mountain View, California.\nAs of March 2026, Waymo operates business robotaxi companies throughout 10 main U.S. metropolitan areas, with a fleet of about 3,000 automobiles. Waymo
additionally delivers roug", "api_data": null, "hint": null}, {"title": "Lyft and Waymo Launch Partnership to Expand Autonomous Mobility to Nashville :: Lyft, Inc. (LYFT)", "url":
"https://investor.lyft.com/news-events/press-releases/detail/89/lyft-and-waymo-launch-partnership-to-expand-autonomous-mobility-to-nashville", "snippet": "Lyft and Waymo Launch Partnership to Expand
Autonomous Mobility to Nashville\nWaymo and Lyft to expand to Nashville next year, with Lyft's Flexdrive managing Waymo\u2019s fully autonomous vehicles.\nSAN FRANCISCO--(BUSINESS WIRE)-- Lyft
(\u201cLyft\u201d) (NASDAQ: LYFT), a global mobility platform, and Waymo, the world\u2019s leading autonomous driving technology company, today announced a new partnership to bring Waymo\u2019s fully
autonomous ride-hailing service to Nashville in 2026.\nThis press release features multimed", "api_data": null, "hint": null}, {"title": "Waymo ride quietly arrives in a new key U.S. city -
TheStreet", "url": "https://www.thestreet.com/automotive/waymo-ride-quietly-arrives-in-a-new-key-us-city-nashville", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "Waymo Las Vegas launch date 2026 public riders"
}
```

### 📋 Result

```
{"query": "Waymo Las Vegas launch date 2026 public riders", "results": [{"title": "Waymo bringing driverless rides to Las Vegas roads in 2026 - Las Vegas Sun News", "url":
"https://lasvegassun.com/news/2025/nov/04/waymo-bringing-driverless-rides-to-las-vegas/", "snippet": "Waymo bringing driverless rides to Las Vegas roads in
2026\n![waymo](http://media.lasvegassun.com/media/img/photos/2025/11/03/AP25301719767242_t650.jpg?5711a3b57decb389a12ba40e20471e031ff69545)\nWaymo vehicles wait at an intersection in San Francisco,
Wednesday, Oct. 22, 2025. The autonomous ride-hailing service is coming to Las Vegas in 2026. Photo by: Jeff Chiu / AP\nTuesday, Nov. 4, 2025 | 2 a.m.\nEditor's note: [Este art\u00edculo est\u00e1
traducido al espa\u00f1ol.](https://lasvegassun.com/news/2025/nov/04/w", "api_data": null, "hint": null}, {"title": "Waymo hints at 2026 San Diego launch date", "url":
"https://fox5sandiego.com/traffic/waymo-san-diego-2026/", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo Plans Las Vegas Launch in Summer 2026 - 102.7 Coyote Country", "url":
"https://coyotecountrylv.com/2025/12/18/waymo-plans-las-vegas-launch-in-summer-2026/", "snippet": "Waymo Plans Las Vegas Launch in Summer 2026\nWaymo is preparing to bring its autonomous ride-hailing
service to Las Vegas, expanding from its established operations in Los Angeles and Phoenix. The company expects a full launch in the\u2026\n![SAN FRANCISCO, CALIFORNIA - APRIL 11: A Waymo autonomous
vehicle drives along Masonic Avenue on April 11, 2022 in San Francisco, California. San Francisco is serving as testing grounds for autonomous vehicles with Waymo, a Google subsidiary and Cruise, a
subsidiar", "api_data": null, "hint": null}, {"title": "Waymo Plans Las Vegas Launch in Summer 2026 - Las Vegas Newsroom", "url": "https://lasvegasnewsroom.com/2025/12/18/waymo-plans-las-vegas-launch-
in-summer-2026/", "snippet": "Waymo Plans Las Vegas Launch in Summer 2026\nWaymo is preparing to bring its autonomous ride-hailing service to Las Vegas, expanding from its established operations in
Los Angeles and Phoenix. The company expects a full launch in the\u2026\n![SAN FRANCISCO, CALIFORNIA - APRIL 11: A Waymo autonomous vehicle drives along Masonic Avenue on April 11, 2022 in San
Francisco, California. San Francisco is serving as testing grounds for autonomous vehicles with Waymo, a Google subsidiary and Cruise, a subsidiar", "api_data": null, "hint": null}, {"title": "Waymo
is bringing its robotaxis to Las Vegas, San Diego, and Detroit - The Robot Report", "url": "https://www.therobotreport.com/waymo-brings-robotaxis-las-vegas-san-diego-detroit/", "snippet": "![A person
walking towards a Waymo vehicle with a bag.](https://www.therobotreport.com/wp-content/uploads/2025/11/waymo-featured.jpg)\n![A person walking towards a Waymo vehicle with a
bag.](https://www.therobotreport.com/wp-content/uploads/2025/11/waymo-featured.jpg)\nWaymo said each deployment starts with mapping the city, which its AVs use to keep track of their location at all
times. | Source: Waymo\nToday, Waymo LLC announced it\u2019s bringing its autonomous ride-hailing service to three more citi", "api_data": null, "hint": null}, {"title": "Robotaxi company Waymo says
it will expand to Las Vegas in 2026", "url": "https://news3lv.com/news/local/autonomous-car-robotaxi-waymo-expanding-las-vegas-self-driving-ride-hailing-nevada-travel-driving-2026", "snippet":
"Robotaxi company Waymo says it will expand to Las Vegas in 2026\n![IPACE_2.jpg](/resources/media2/16x9/9504/986/0x495/90/5abc1cfb-4690-44b8-b000-814b83ade0f5-IPACE_2.jpg)\nLAS VEGAS (KSNV) \u2014 The
autonomous car company Waymo announced it plans to expand its robotaxi service to Las Vegas next summer.\nWaymo says its autonomous ride-hailing service will become available for residents and
visitors after it coordinates with local officials.\n\"The introduction of Waymo and its autonomous driving technolog", "api_data": null, "hint": null}, {"title": "Waymo prepares to launch self-
driving cars in Las Vegas", "url": "https://news3lv.com/news/local/waymo-prepares-to-launch-self-driving-cars-in-las-vegas", "snippet": "Waymo prepares to launch self-driving cars in Las
Vegas\n![gettyimages-2244379880-612x612.jpg](/resources/media2/16x9/612/986/0x32/90/2037b33b-f67b-40d2-9570-dfaf95a994b3-gettyimages2244379880612x612.jpg)\nLAS VEGAS (KSNV) \u2014 Waymo is gearing up
to introduce its self-driving cars to the streets of Las Vegas.\nThe company, which has already operated in cities like Los Angeles and Phoenix, is deploying sensor-equipped vehicles in Southern
Nevada as part of its preparation.\n\"We've done over 14 million ", "api_data": null, "hint": null}, {"title": "Waymo Plans Las Vegas Launch in Summer 2026 - 105.7 MAXIMA", "url":
"https://1057maxima.com/2025/12/18/waymo-plans-las-vegas-launch-in-summer-2026/", "snippet": "Waymo Plans Las Vegas Launch in Summer 2026\nWaymo is preparing to bring its autonomous ride-hailing
service to Las Vegas, expanding from its established operations in Los Angeles and Phoenix. The company expects a full launch in the\u2026\n![SAN FRANCISCO, CALIFORNIA - APRIL 11: A Waymo autonomous
vehicle drives along Masonic Avenue on April 11, 2022 in San Francisco, California. San Francisco is serving as testing grounds for autonomous vehicles with Waymo, a Google subsidiary and Cruise, a
subsidiar", "api_data": null, "hint": null}, {"title": "Waymo Service Areas in the US: A Definitive Guide - Fifth Level Consulting", "url": "https://fifthlevelconsulting.com/waymo-service-areas-in-
the-u-s/", "snippet": "Last updated: November 2025\n[Waymo ](https://fifthlevelconsulting.com/autonomous-vehicles-10-amazing-things-to-know-about-waymo/)operates commercial robotaxi services available
to the public through its Waymo One app in several major U.S. cities. The Alphabet-owned company currently provides over 250,000 paid rides per week, marking a significant milestone in [autonomous
vehicle adoption](https://fifthlevelconsulting.com/key-components-of-autonomous-vehicles/). These [Waymo rides](https://fifthl", "api_data": null, "hint": null}, {"title": "Waymo Expands Service to
Las Vegas, San Diego, and Detroit", "url": "https://www.thedriverlessdigest.com/p/waymo-expands-service-to-las-vegas", "snippet": "Waymo Expands Service to Las Vegas, San Diego, and Detroit\nBaidu
hits 250,000 weekly rides, Why unions are becoming a problem for self-driving cars, and \u2018I tried a Tesla FSD Dupe\u2019\nTop Stories of the Week\nWaymo\u2019s robotaxi expansion accelerates with
3 new cities ([link](https://techcrunch.com/2025/11/03/waymos-robotaxi-expansion-accelerates-with-3-new-cities/)). The company plans to launch service in Detroit, Las Vegas, and San Diego, rolling out
a mix of self-driving Jaguar I-Pace and Zeekr RT ve", "api_data": null, "hint": null}]}
```

## 💬 Response

Now let me search for the most recent Waymo news to understand the current status (April 2026) for these specific cities.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__asknews__search_news


```json
{
  "query": "Waymo Denver launch April 2026 riders"
}
```

### 📋 Result

```
{"query": "Waymo Denver launch April 2026 riders", "results": [{"title": "Waymo's robotaxis set for driverless launch in Denver in 2026 - Axios Denver", "url":
"https://www.axios.com/local/denver/2025/12/05/waymo-denver-colorado-autonomous-robotaxi-2026", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo Updates | Get updates on cities Waymo
serves", "url": "https://waymo.com/updates/", "snippet": "Waymo is coming soon to your city\nKeep in touch\nThank you. You\u2019re all set.\nThank you for joining us on our journey. We're excited to
keep you in the loop as we bring the safety and mobility benefits of the Waymo Driver to more communities.\n- San Francisco Bay Area, CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle, WA\n- San
Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver, CO\n- San Antonio, TX\n- Austin, TX\n- Dallas, TX\n- Houston, TX\n- Minneapolis, MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL",
"api_data": null, "hint": null}, {"title": "Waymo robotaxis are now operating in 10 US cities | TechCrunch", "url": "https://techcrunch.com/2026/02/24/waymo-robotaxis-are-now-operating-in-10-us-
cities/", "snippet": "Waymo is opening its robotaxi services to the public in Dallas, Houston, San Antonio, and Orlando, as the Alphabet-owned autonomous vehicle company quickens its pace of
expansion.\nWaymo\u2019s rollout will mimic its public launches in previous cities. Select riders who have downloaded the Waymo app will receive an invitation to take their first rides, starting
Tuesday. New riders will be added on a rolling basis, and eventually anyone who downloads the app will be able to hail a ride.\nThe addition of", "api_data": null, "hint": null}, {"title": "Buckle Up:
Is Waymo Ready for Denver's Winter Roads and Angry Drivers?", "url": "https://www.westword.com/news/can-waymo-overcome-denver-winter-roads-angry-drivers-40790292/", "snippet": "![cartoon of a waymo
car driving through Denver](https://www.westword.com/wp-content/uploads/sites/2/2025/10/image-1-1.png)\nBradley Hansen\n![Carbonatix Pre-Player Loader](https://gamalpha.com/images/tts-pre-
loader.gif)\nAudio By Carbonatix\nKeep Westword Free\nWe\u2019re aiming to raise $20,000 by April 26. Your support ensures Westword can continue watching out for you and our community. No paywall.
Always accessible. Daily online and weekly in print.\nA new type of vehicle has emerged on Denver\u2019s roads", "api_data": null, "hint": null}, {"title": "Despite not-so-snowy winter, Waymo still
steering toward 2026 Denver rollout", "url": "https://www.denver7.com/money/science-and-tech/despite-not-so-snowy-winter-waymo-still-steering-toward-2026-denver-rollout", "snippet": "DENVER \u2014
Autonomous taxi company Waymo is still on track to start giving rides in Denver \"later this year,\" despite a warm and dry winter, the company told Denver7 this week.\nWaymo \u2014 a subsidiary of
Google parent company Alphabet \u2014 [announced in September](https://www.denver7.com/news/local-news/googles-autonomous-ride-service-waymo-is-coming-to-denver) that it plans to expand to Denver. It
has been testing its self-driving SUVs and vans on city streets in recent months, with humans still sittin", "api_data": null, "hint": null}, {"title": "Waymo self-driving cars set to launch in
Denver, amid Colorado governor's push for safer roads (CBS News Colorado) \u2014 Colorado Department of Transportation", "url": "https://www.codot.gov/safety/shift-into-safe-news/2025/november/waymo-
self-driving-cars-set-to-launch-in-denver-amid-colorado-governors-push-for-safer-roads-cbs-news-colorado", "snippet": "Waymo self-driving cars set to launch in Denver, amid Colorado governor's push
for safer roads (CBS News Colorado)\nShift into Safe News\nWaymo announced its launch in Denver in September, but it's going to take a while before Denverites will be able to take a ride in one.
They're rolling out their service in phases.\n\u201cIt's really exciting to be one of the earlier cities in the country that's moving forward with this exciting new technology,\u201d Gov. Jared Polis
said.\nThe autonomous car company is her", "api_data": null, "hint": null}, {"title": "Self-driving car company Waymo heading to metro Denver in 2026 - The Colorado Sun", "url":
"https://coloradosun.com/2025/09/02/self-driving-car-company-waymo-heading-to-metro-denver-in-2026/", "snippet": "Waymo is on the way to Denver, the autonomous-driving technology company said
Tuesday.\nThe Silicon Valley company, a subsidiary of Alphabet and formerly known as the Google Self-Driving Car Project, will be one of first driverless car services to hit the road in Colorado, at
least for ride-hailing passengers. The company is already offering rides to customers in Atlanta, Austin, Los Angeles, Phoenix and San Francisco.\nBut for locals hoping to hail a ride soon,
that\u2019s not happening just yet, Waym", "api_data": null, "hint": null}, {"title": "Waymo\u2019s autonomous cars are testing on Denver streets. Are rides to the airport in the future?", "url":
"https://coloradosun.com/2025/09/18/waymos-autonomous-cars-denver-airport/", "snippet": "Autonomous cars from Waymo began driving around Denver\u2019s streets [this
month](https://coloradosun.com/2025/09/02/self-driving-car-company-waymo-heading-to-metro-denver-in-2026/). While they\u2019re still in training mode and have a human driver doing the legwork, the
driverless ride-service company has big plans for Colorado\u2019s future: airport service.\n\u201cWe can\u2019t wait to at some point serve Denver International Airport,\u201d said Suzanne Philion,
Waymo\u2019s vice president of marketing, communications and publ", "api_data": null, "hint": null}, {"title": "Waymo\u2019s 2025 Year in Review: The Year Robotaxis Scaled", "url":
"https://www.thedriverlessdigest.com/p/waymos-2025-year-in-review-the-year", "snippet": "Waymo\u2019s 2025 Year in Review: The Year Robotaxis Scaled\nToday\u2019s post comes from [Daniel Abreu
Marques](https://www.linkedin.com/in/daniel-abreu-marques-/), who works in autonomous driving strategy and writes about Waymo and the broader robotaxi space in a personal capacity over at [The AV
Market Strategist](https://open.substack.com/pub/avmarketstrategist).\nWaymo has had an impressive 2025, so today I wanted to look back at the year and review the incredible progress the company has
made, from sk", "api_data": null, "hint": null}, {"title": "Waymo\u2019s Self-Driving Cars Arrive in Denver. But Colorado Has No Regulatory Oversight", "url": "https://www.governing.com/policy/waymos-
self-driving-cars-arrive-in-denver-but-colorado-has-no-regulatory-oversight", "snippet": "[white Jaguars](https://waymo.com/blog/2018/03/meet-our-newest-self-driving-vehicle)and\n[powder-blue
Zeekrs](https://waymo.com/blog/2021/12/expanding-our-waymo-one-fleet-with)topped with rotating black cameras and radar \u2014 have been\n[rolling around Denver for two
months](https://www.denverpost.com/2025/09/03/waymo-denver-driverless-car/), ingesting data into their artificial-intelligence computers ahead of public activation next
year.\nThe\n[Waymo](https://waymo.com/)expansion here, part of a push ", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Waymo Washington DC launch riders 2026"
}
```

### 📋 Result

```
{"query": "Waymo Washington DC launch riders 2026", "results": [{"title": "Next stop for Waymo One: Washington, D.C.", "url": "https://waymo.com/blog/2025/03/next-stop-for-waymo-one-washingtondc/",
"snippet": "[Back](https://waymo.com/blog)\nNext stop for Waymo One: Washington, D.C.\nIt\u2019s official: Waymo One, the world\u2019s leading fully autonomous ride-hailing service, will be ready for
riders in the nation\u2019s capital on the Waymo One app in 2026.\nWe\u2019re laying the groundwork for our fully autonomous ride-hailing service after
[returning](https://x.com/Waymo/status/1885327172786671985) to Washington, D.C. earlier this year, and we\u2019ll continue introducing ourselves to D.C.\u2019s communities and emergency respond",
"api_data": null, "hint": null}, {"title": "Waymo Updates | Get updates on cities Waymo serves", "url": "https://waymo.com/updates/", "snippet": "Waymo is coming soon to your city\nKeep in
touch\nThank you. You\u2019re all set.\nThank you for joining us on our journey. We're excited to keep you in the loop as we bring the safety and mobility benefits of the Waymo Driver to more
communities.\n- San Francisco Bay Area, CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle, WA\n- San Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver, CO\n- San Antonio, TX\n- Austin, TX\n-
Dallas, TX\n- Houston, TX\n- Minneapolis, MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL", "api_data": null, "hint": null}, {"title": "Waymo will launch Washington, D.C., robotaxi service in
2026", "url": "https://www.cnbc.com/2025/03/25/waymo-will-launch-washington-dc-robotaxi-service-in-2026.html", "snippet": "Waymo's officially on its way to the nation's capital.\nThe
[Alphabet](https://www.cnbc.com/quotes/GOOGL/)-owned autonomous driving robotaxi service will be available in Washington, D.C., in 2026, the company announced Tuesday.\n\"I've experienced firsthand
how safely the Waymo Driver operates around pedestrians, cyclists, and other vulnerable road users,\" said Governors Highway Safety Association CEO Jonathan Adkins. \"Waymo has worked with GHSA and
our first responder network as they've expanded t", "api_data": null, "hint": null}, {"title": "Waymo Confirms Washington DC Robotaxi Plan 2026 | Silicon UK", "url":
"https://www.silicon.co.uk/e-innovation/green-it/waymo-confirms-washington-dc-robotaxi-plan-for-2026-605701", "snippet": "|\nGetting your\n|\nAlphabet\u2019s Waymo self-driving division has confirmed
the expansion of its driverless robotaxi service, known as Waymo One, to the US capitol city Washington, DC.\nWaymo in a [blog post](https://waymo.com/blog/2025/03/next-stop-for-waymo-one-
washingtondc) confirmed that \u201cWaymo One, the world\u2019s leading fully autonomous ride-hailing service, will be ready for riders in the nation\u2019s capital on the Waymo One app in
2026.\u201d\nIt comes after Waymo has [spent](https://www.silicon.co.uk/e-in", "api_data": null, "hint": null}, {"title": "Waymo launching in Washington DC in 2026", "url":
"https://9to5google.com/2025/03/25/waymo-washington-dc-2026/", "snippet": "![](https://9to5google.com/wp-content/uploads/sites/4/2025/03/waymo-dc-1.jpg?quality=82&strip=all&w=1600)\nWaymo has
announced that it will be expanding to yet another new city, with robotaxi services set to begin in Washington DC next year.\nIn a [blog post](https://waymo.com/blog/2025/03/next-stop-for-waymo-one-
washingtondc) today, Waymo says that its \u201cfully autonomous ride-hailing service\u201d is coming to Washington DC sometime in 2026. A specific date wasn\u2019t provided, but Waymo says it plans to
r", "api_data": null, "hint": null}, {"title": "Waymo to launch robotaxi service in Washington, D.C., in 2026 | TechCrunch", "url": "https://techcrunch.com/2025/03/25/waymo-to-launch-robotaxi-service-
in-washington-d-c-in-2026/", "snippet": "Waymo said Tuesday it will begin offering robotaxi rides via the Waymo One app in Washington, D.C., in 2026.\nBefore it can launch commercially, the company
will have to up its lobbying game in the capital, where autonomous vehicle permits still require a human behind the wheel.\nThe news from Waymo comes as the Alphabet-owned company aggressively expands
its robotaxi coverage to cement its lead ahead of potential competitors like Amazon\u2019s Zoox and Elon Musk\u2019s Tesla. Musk said Tesla will launch a ", "api_data": null, "hint": null}, {"title":
"Waymo self-driving cars could launch in DC by 2026, but skeptics remain", "url": "https://www.wusa9.com/article/tech/waymo-autonomous-vehicles-self-driving-dc-council-ethan-teicher-advocates-highway-
auto-safety/65-902851dc-0be6-4712-87b6-822ae2ea5d6f", "snippet": null, "api_data": null, "hint": null}, {"title": "Scaling our fleet through U.S. manufacturing", "url":
"https://waymo.com/blog/2025/05/scaling-our-fleet-through-us-manufacturing/", "snippet": "[Back](https://waymo.com/blog)\nScaling our fleet through U.S. manufacturing\nThe U.S. is leading the world in
the development and deployment of autonomous driving technology. Today, Waymo One provides more than 250,000 paid trips each week across Phoenix, San Francisco, Los Angeles, and Austin, and we\u2019re
preparing to bring our fully autonomous ride-hailing to Atlanta, Miami, and Washington, D.C. in 2026. We\u2019re proud to bring this technology \u2013 once thought to be the stuff of science fiction
\u2013 to m", "api_data": null, "hint": null}, {"title": "Waymo's self-driving car launch in DC delayed after federal budget cuts halt safety study", "url":
"https://www.wusa9.com/article/news/local/dc/waymo-autonomous-vehicles-washington-dc-council-charles-allen-ddot-safety-study/65-470f58be-8c9d-4b5b-96fe-d831a9b1db50", "snippet": null, "api_data":
null, "hint": null}, {"title": "Waymo to Launch Autonomous Ride-Hailing Service in Washington, D.C. | Future Transport-News", "url": "https://futuretransport-news.com/waymo-to-launch-autonomous-ride-
hailing-service-in-washington-d-c/", "snippet": "Waymo has announced that its autonomous ride-hailing service, Waymo One, will begin operations in Washington, D.C., in 2026.\nThe company is currently
engaging with local communities, policymakers, and emergency responders to prepare for the introduction of its fully autonomous vehicles in the city.\n![Next stop for Waymo One: Washington,
D.C.](https://futuretransport-news.com/wp-content/uploads/sites/3/2025/03/Screenshot-2025-03-28-at-12.56.18-800x447.png)\nFollowing its return to Washington, D.C.", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Waymo new city launch expansion April 2026",
  "hours_back": 168
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

## 💭 Thinking

Let me now piece together what I know and search for the most recent information about whether any of these specific cities already have Waymo serving riders.

Current state as of April 10, 2026:
- Waymo is serving riders in 11 cities: Phoenix, SF Bay Area, LA, Atlanta (via Uber), Austin (via Uber), Miami, Dallas, Houston, San Antonio, Orlando, Nashville (launched April 7, 2026)
- Cities "up next" include: Denver, Detroit, Las Vegas, San Diego, Washington DC, Seattle, and others

The question asks about: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, or Washington DC


Looking at the timeline for each city, Las Vegas won't launch until summer, Denver and Washington DC are still in testing or regulatory phases with no confirmed dates, while Detroit, Seattle, and Chicago are on expansion lists but lack specific timelines. Baltimore, Boston, Charlotte, and New York don't appear to have near-term launch plans, which means none of these cities will likely have Waymo service by the May resolution date.

## 💬 Response

Let me search for the latest news on whether any launches in these specific cities are imminent.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "query": "\"Waymo\" \"serving riders\" OR \"public riders\" OR \"launch\" Denver OR \"Las Vegas\" OR Seattle OR Chicago OR Detroit April 2026"
}
```

### 📋 Result

```
{"query": "\"Waymo\" \"serving riders\" OR \"public riders\" OR \"launch\" Denver OR \"Las Vegas\" OR Seattle OR Chicago OR Detroit April 2026", "results": [{"title": "Waymo Updates | Get updates on
cities Waymo serves", "url": "https://waymo.com/updates/", "snippet": "Waymo is coming soon to your city\nKeep in touch\nThank you. You\u2019re all set.\nThank you for joining us on our journey. We're
excited to keep you in the loop as we bring the safety and mobility benefits of the Waymo Driver to more communities.\n- San Francisco Bay Area, CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle,
WA\n- San Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver, CO\n- San Antonio, TX\n- Austin, TX\n- Dallas, TX\n- Houston, TX\n- Minneapolis, MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL",
"api_data": null, "hint": null}, {"title": "Waymo Service Areas in the US: A Definitive Guide - Fifth Level Consulting", "url": "https://fifthlevelconsulting.com/waymo-service-areas-in-the-u-s/",
"snippet": "Last updated: November 2025\n[Waymo ](https://fifthlevelconsulting.com/autonomous-vehicles-10-amazing-things-to-know-about-waymo/)operates commercial robotaxi services available to the
public through its Waymo One app in several major U.S. cities. The Alphabet-owned company currently provides over 250,000 paid rides per week, marking a significant milestone in [autonomous vehicle
adoption](https://fifthlevelconsulting.com/key-components-of-autonomous-vehicles/). These [Waymo rides](https://fifthl", "api_data": null, "hint": null}, {"title": "Waymo\u2019s 2025 Year in Review:
The Year Robotaxis Scaled", "url": "https://www.thedriverlessdigest.com/p/waymos-2025-year-in-review-the-year", "snippet": "Waymo\u2019s 2025 Year in Review: The Year Robotaxis Scaled\nToday\u2019s
post comes from [Daniel Abreu Marques](https://www.linkedin.com/in/daniel-abreu-marques-/), who works in autonomous driving strategy and writes about Waymo and the broader robotaxi space in a personal
capacity over at [The AV Market Strategist](https://open.substack.com/pub/avmarketstrategist).\nWaymo has had an impressive 2025, so today I wanted to look back at the year and review the incredible
progress the company has made, from sk", "api_data": null, "hint": null}, {"title": "Waymo begins deploying next-gen Ojai robotaxis to extend its U.S. lead", "url":
"https://www.cnbc.com/2026/02/12/waymo-begins-deploying-next-gen-ojai-robotaxis-to-extend-its-us-lead.html", "snippet": "Waymo on Thursday said it has begun using its sixth-generation driverless
system to provide robotaxi rides to employees on Ojai vehicles, which use a base model made by Chinese automaker Geely.\nBy upgrading their driverless tech, and adding more vehicles to its fleet,
Waymo aims to extend its U.S. lead and lock in loyal riders. The [Alphabet](https://www.cnbc.com/quotes/GOOG/)-owned company said its sixth-generation Waymo Driver uses more cost-effective parts, and
should be able to navigate thro", "api_data": null, "hint": null}, {"title": "Waymo in Chicago? Autonomous rideshare company confirms 'laying the groundwork' in The Windy City", "url":
"https://electrek.co/2026/02/25/waymo-chicago-autonomous-rideshare/", "snippet": "![Waymo Chicago](https://electrek.co/wp-content/uploads/sites/3/2026/02/Waymo-
Chicago.jpg?quality=82&strip=all&w=1400)\nAfter Chicago residents began posting images of [Waymo](https://electrek.co/guides/waymo/) vehicles being unloaded on the city\u2019s streets, the autonomous
rideshare company confirmed it is exploring expanding its network to the Second City. However, an obstacle currently stands in the way of that deployment.\nWaymo continues to support the argument that
it is the leader in autonomo", "api_data": null, "hint": null}, {"title": "Waymo - Wikipedia", "url": "https://en.wikipedia.org/wiki/Waymo", "snippet": "Waymo LLC ( WAY-moh) is an American autonomous
driving technology company headquartered in Mountain View, California. It is a subsidiary of Alphabet Inc., Google's parent company. As of March 2026, Waymo operates public commercial robotaxi
services in 10 US metropolitan areas, has 3,000 robotaxis in service, provides 500,000 paid rides per week and had logged 200 million fully autonomous miles. \nThe company traces its origins to the
Stanford Racing Team, which competed in the 2005 and 2007 Defen", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Waymo\", \"url\": \"https://en.wikipedia.org/wiki/Waymo\",
\"extract\": \"Waymo LLC ( WAY-moh) is an American autonomous driving technology company headquartered in Mountain View, California. It is a subsidiary of Alphabet Inc., Google's parent company. As of
March 2026, Waymo operates public commercial robotaxi services in 10 US metropolitan areas, has 3,000 robotaxis in service, provides 500,000 paid rides per week and had logged 200 million fully
autonomous miles. \\nThe company traces its origins to the Stanford Racing Team, which competed in the 2005 and 2007 Defense Advanced Research Projects Agency (DARPA) Grand Challenges. Google's
development of self-driving technology began in January 2009 and the project was revealed in October 2010. In December 2016, the project was renamed Waymo and spun out of Google as part of Alphabet.
In October 2020, Waymo became the first company to offer service to the public without safety drivers.\\nWaymo is run by co-CEOs Tekedra Mawakana and Dmitri Dolgov since April 2021. The company raised
$11 billion in multiple outside funding rounds by 2024. In February 2026, Waymo raised $16 billion, which valued the company at $126 billion.\\nIn January 2026, The National Transportation Safety
Board and National Highway Traffic Safety Administration opened investigations into Waymo's robotaxis for recurring incidents of illegally passing stopped school buses, and one incident where a
robotaxi hit a child who ran out from behind a parked SUV in a school zone.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Waymo to begin manual drives in Minneapolis, Tampa and New Orleans,
aims to open service in 2026", "url": "https://www.cnbc.com/2025/11/20/waymo-to-begin-manual-drives-in-minneapolis-tampa-and-new-orleans.html", "snippet":
"[Alphabet's](https://www.cnbc.com/quotes/GOOG/) Waymo on Thursday announced that it will soon begin manually driving its robotaxi vehicles in Minneapolis, Tampa and New Orleans.\nThe Google sister
company will start operating test drives in that trio of towns with human drivers in hopes of launching its driverless robotaxi service there as soon as next year, the company said.\nIf Waymo does
begin operating in those markets next year, that would bring the robotaxi company's list of 2026 planned exp", "api_data": null, "hint": null}, {"title": "Waymo's robotaxi expansion accelerates with 3
new cities | TechCrunch", "url": "https://techcrunch.com/2025/11/03/waymos-robotaxi-expansion-accelerates-with-3-new-cities/", "snippet": "Waymo said Monday it will launch a robotaxi service in
Detroit, Las Vegas, and San Diego as the Alphabet-owned company hits the accelerator on its expansion plans.\nThe announcement illustrates Waymo\u2019s recent evolution from autonomous vehicle
technology developer to commercial enterprise. It also follows comments by Waymo co-CEO Tekedra Mawakana, who said last week during TechCrunch Disrupt 2025 that it is [imperative the company
scales](https://techcrunch.com/2025/10/27/waymos-co-ceo-on-the-chal", "api_data": null, "hint": null}, {"title": "Waymo Launches Driverless Rides in Four New Cities, Expanding to 10 US Markets | EV",
"url": "https://eletric-vehicles.com/waymo/waymo-launches-driverless-rides-in-four-new-cities-expanding-to-10-us-markets/", "snippet": "[Waymo](https://eletric-vehicles.com/category/waymo/), the
autonomous driving unit of Alphabet, announced on Tuesday that it launched its ride-hailing service in four new cities \u2014 Dallas, Houston, San Antonio, and Orlando \u2014 expanding its footprint
to ten major US metropolitan markets.\nIt is the first time the company has opened to the public in multiple cities simultaneously.\nSelect riders will receive invitations through the
[Waymo](https://eletric-vehicles.com/category/waymo/) app starting Tue", "api_data": null, "hint": null}, {"title": "Waymo Stats 2026: Funding, Growth, Coverage, Fleet Size ...", "url":
"https://www.thedriverlessdigest.com/p/waymo-stats-2025-funding-growth-coverage", "snippet": "Waymo Stats 2026: Funding, Growth, Coverage, Fleet Size & More\nA look at the key stats and milestones
from Waymo, Google\u2019s former self-driving project and now an autonomous vehicle subsidiary under Alphabet\nWaymo has been leading the autonomous vehicle revolution for almost two decades now. What
started as Google\u2019s self-driving car project in 2009 has now become one of the biggest autonomous ride-hailing services around, just less than 10 years after becoming a
[separate](https://www.theguardian", "api_data": null, "hint": null}]}
```

```json
{
  "url": "https://www.wusa9.com/article/news/local/dc/waymo-autonomous-vehicles-washington-dc-council-charles-allen-ddot-safety-study/65-470f58be-8c9d-4b5b-96fe-d831a9b1db50",
  "prompt": "What is the status of Waymo's launch in Washington DC? Has it been delayed? What are the regulatory barriers?"
}
```

### 📋 Result

```
Timeout fetching https://www.wusa9.com/article/news/local/dc/waymo-autonomous-vehicles-washington-dc-council-charles-allen-ddot-safety-study/65-470f58be-8c9d-4b5b-96fe-d831a9b1db50. Try Playwright or
search_exa.
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://electrek.co/2026/02/25/waymo-chicago-autonomous-rideshare/",
  "prompt": "What is the current status of Waymo in Chicago? Is Waymo serving riders there? What obstacles exist?"
}
```

### 📋 Result

```
{"url": "https://electrek.co/2026/02/25/waymo-chicago-autonomous-rideshare/", "content": "Based on the content:\n\n**Current Status:**\nWaymo has begun deploying vehicles in Chicago and is \"laying
the groundwork\" for operations, but is **NOT** currently serving riders there. The vehicles are being tested with human drivers behind the wheel for mapping purposes only.\n\n**Obstacles:**\nThe main
obstacle is **lack of regulatory approval**. Illinois has no law or regulatory framework authorizing autonomous (driverless) vehicles to operate in either Chicago or the state of Illinois. Chicago
Mayor Brandon Johnson confirmed that while licensed individuals can drive in Chicago, autonomous vehicles have not been authorized.\n\nChicago is currently listed as a \"Testing/Expansion City\"
rather than a \"Public Service City\" where Waymo offers rides.\n\n**Relevant links:**\n- [Waymo's official announcement on X/Twitter](https://x.com/Waymo/status/2026658440525881481?s=20)\n- [CBS
Chicago coverage with Waymo statement](https://www.cbsnews.com/chicago/news/waymo-coming-to-chicago/#:~:text=We%20are%20coordinating%20closely%20with%20community%20leaders%20and%20policymakers%20and%2
0believe%20autonomous%20technology%20can%20strongly%20support%20Chicago%27s%20goals%20for%20road%20safety%20and%20enhanced%20accessibility%20for%20all%20communities%2C)\n- [Waymo blog post on four new
cities](https://waymo.com/blog/2026/02/dallas-houston-san-antonio-orlando)", "title": "Waymo in Chicago? Autonomous rideshare company confirms 'laying the groundwork' in The Windy City"}
```

```json
{
  "query": "Waymo DC delayed safety study federal budget cuts 2026"
}
```

### 📋 Result

```
{"query": "Waymo DC delayed safety study federal budget cuts 2026", "results": [{"title": "Waymo's self-driving car launch in DC delayed after federal budget cuts halt safety study", "url":
"https://www.wusa9.com/article/news/local/dc/waymo-autonomous-vehicles-washington-dc-council-charles-allen-ddot-safety-study/65-470f58be-8c9d-4b5b-96fe-d831a9b1db50", "snippet": null, "api_data":
null, "hint": null}, {"title": "Opinion | D.C. stalls on autonomous vehicles despite impressive safety record - The Washington Post", "url":
"https://www.washingtonpost.com/opinions/2026/03/21/autonomous-vehicles-dc-waymo-ddot/", "snippet": null, "api_data": null, "hint": null}, {"title": "After icy DC launch, Waymo heads to Boston to test
self-driving cars in snowy conditions - Safety21", "url": "https://safety21.cmu.edu/2026/02/10/after-icy-dc-launch-waymo-heads-to-boston-to-test-self-driving-cars-in-snowy-conditions/", "snippet":
null, "api_data": null, "hint": null}, {"title": "Scoop: Waymo steps up lobbying after D.C. delays robotaxis", "url": "https://www.axios.com/local/washington-dc/2026/02/27/waymo-robotaxis-lobbying-
self-driving-cars", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo robotaxis may soon navigate DC\u2019s motorcades and protests", "url":
"https://cronkitenews.azpbs.org/2025/11/20/waymo-robotaxi-washington-dc-motorcades/", "snippet": "WASHINGTON \u2013 Just outside the White House, sirens blared and emergency lights flashed as a
multivehicle motorcade carrying Saudi Crown Prince Mohammed bin Salman sped down Pennsylvania Avenue.\nSecret Service and Metropolitan Police officers blocked cars from crossing the street. Commuters
sat idling in gridlock for more than 10 minutes.\nFor D.C. residents, and especially for downtown workers, motorcades are nothing new. But even for the most seasoned Washingtonian, having to pull over
as a strea", "api_data": null, "hint": null}, {"title": "Why self-driving Waymo car service isn't available yet in DC", "url": "https://www.nbcwashington.com/news/local/transportation/why-self-
driving-waymo-car-service-isnt-available-yet-in-dc/4004752/", "snippet": "News4 has learned a key report that would essentially help pave the way for self-driving vehicles to start service is being
held back. News4 Transportation Reporter Adam Tuss has the details\nPlans to bring self-driving autonomous vehicles to D.C. may be taking a detour.\nNews4 has learned a key report that would pave the
way for the cars to start service is being held back.\nStream NBC4 newscasts for free right here, right now.\n[ ](https://www.nbcwashington.com/watch/)\nWATCH HERE\n![Watch button](h", "api_data":
null, "hint": null}, {"title": "After icy D.C. launch, Waymo heads to Boston to test self-driving cars in snowy conditions | wusa9.com", "url":
"https://www.wusa9.com/article/news/community/transportation/waymo-boston-snow-driving-self-driving-cars/65-657109b4-0b09-4244-9866-322d67a60b57", "snippet": null, "api_data": null, "hint": null},
{"title": "Tech Talk | Councilmember Charles Allen on Waymo: \u2018Autonomous vehicles will likely operate in the District of Columbia\u2019 | DC News Now", "url": "https://www.dcnewsnow.com/tech-
talk/tech-talk-councilmember-charles-allen-on-waymo-autonomous-vehicles-will-likely-operate-in-the-district-of-columbia/", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo Turns Up
Pressure On D.C. Over Robotaxi Permits", "url": "https://hoodline.com/2026/02/waymo-floods-d-c-with-lobbyists-as-robotaxi-showdown-drags-on/", "snippet": "![Waymo Floods D.C. With Lobbyists As
Robotaxi Showdown Drags On](https://img.hoodline.com/2026/2/waymo-floods-dc-with-lobbyists-as-robotaxi-showdown-drags-on.webp?max-h=442&w=760&fit=crop&crop=faces,center)\nWaymo is quietly turning up
the heat in Washington, D.C., pouring money into local lobbying while the city keeps its driverless robotaxis firmly in park. The company continues to run sensor-loaded Jaguars around D.C. with human
safety drivers behind the wheel, but council members say they wi", "api_data": null, "hint": null}, {"title": "Why DC doesn't have Waymo and other robotaxis yet - Axios Washington D.C.", "url":
"https://www.axios.com/local/washington-dc/2025/12/04/when-waymo-robotaxi-dc-council-mayor-bowser", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "Waymo Seattle launch timeline 2026 riders"
}
```

### 📋 Result

```
{"query": "Waymo Seattle launch timeline 2026 riders", "results": [{"title": "Waymo Updates | Get updates on cities Waymo serves", "url": "https://waymo.com/updates/", "snippet": "Waymo is coming soon
to your city\nKeep in touch\nThank you. You\u2019re all set.\nThank you for joining us on our journey. We're excited to keep you in the loop as we bring the safety and mobility benefits of the Waymo
Driver to more communities.\n- San Francisco Bay Area, CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle, WA\n- San Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver, CO\n- San Antonio, TX\n-
Austin, TX\n- Dallas, TX\n- Houston, TX\n- Minneapolis, MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL", "api_data": null, "hint": null}, {"title": "Waymo\u2019s 2025 Year in Review: The Year
Robotaxis Scaled", "url": "https://www.thedriverlessdigest.com/p/waymos-2025-year-in-review-the-year", "snippet": "Waymo\u2019s 2025 Year in Review: The Year Robotaxis Scaled\nToday\u2019s post comes
from [Daniel Abreu Marques](https://www.linkedin.com/in/daniel-abreu-marques-/), who works in autonomous driving strategy and writes about Waymo and the broader robotaxi space in a personal capacity
over at [The AV Market Strategist](https://open.substack.com/pub/avmarketstrategist).\nWaymo has had an impressive 2025, so today I wanted to look back at the year and review the incredible progress
the company has made, from sk", "api_data": null, "hint": null}, {"title": "Waymo Stats 2026: Funding, Growth, Coverage, Fleet Size ...", "url": "https://www.thedriverlessdigest.com/p/waymo-
stats-2025-funding-growth-coverage", "snippet": "Waymo Stats 2026: Funding, Growth, Coverage, Fleet Size & More\nA look at the key stats and milestones from Waymo, Google\u2019s former self-driving
project and now an autonomous vehicle subsidiary under Alphabet\nWaymo has been leading the autonomous vehicle revolution for almost two decades now. What started as Google\u2019s self-driving car
project in 2009 has now become one of the biggest autonomous ride-hailing services around, just less than 10 years after becoming a [separate](https://www.theguardian", "api_data": null, "hint":
null}, {"title": "Waymo coming to Seattle: Driverless rideshare service announces US expansion", "url": "https://www.fox13seattle.com/news/waymo-seattle-expansion", "snippet": "Waymo coming to
Seattle: Driverless rideshare service announces US expansion\n![Waymo to expand to
Seattle](https://h107833-ecdn.mp.lura.live/1/938756/pvw/9E7/1B5/9E71B58EB0D949C2B7C80AB7DDCFFF95_5.jpg?aktaexp=2082787200&aktasgn=7cd0b85053b2d081a11317462be56bdb)\n[Waymo to expand to
Seattle](https://www.fox13seattle.com/video/1701291)\nWaymo, the autonomous rideshare service, is bringing its self-driving cars to Seattle.\nSEATTLE - Waymo, the fully-autonomous rideshare service,
is coming to [Seattle", "api_data": null, "hint": null}, {"title": "Waymo Self-Driving Taxis Will Hit 12 U.S. Cities By 2026. Is Yours Next?", "url": "https://insideevs.com/news/777811/waymo-
expansion-us-cities-autonomous/", "snippet": "Waymo's rollout progressed slowly at first. Now it's happening all at once. After tinkering with its autonomous driving technology for well over a decade,
the Alphabet-owned firm is rapidly expanding its driverless taxi service into new territory.\nOn Monday, Waymo announced its self-driving cars will hit three more cities in 2026: San Diego, Detroit
and Las Vegas. That should bring the tally to at least 12 operational U.S. cities by the end of next year, if all goes to plan.\n\"We'll follow our sa", "api_data": null, "hint": null}, {"title":
"Waymo: Where it\u2019s available, upcoming cities, and new features [Feb 2026]", "url": "https://9to5google.com/2026/02/24/waymo-new-cities-features/", "snippet": "![](https://9to5google.com/wp-
content/uploads/sites/4/2023/09/waymo-cover-1.jpg?quality=82&strip=all&w=1600)\nWaymo autonomous vehicles date back to Google\u2019s self-driving car project that started in 2009. As of today, you can
get a ride in 10 cities across the US.\nTable of contents\nWhere Waymo is fully available\nUsing the Waymo app on [Android](https://play.google.com/store/apps/details?id=com.waymo.carapp) and
[iOS](https://apps.apple.com/us/app/waymo/id1343524838), you can hail a ride in Phoeni", "api_data": null, "hint": null}, {"title": "Waymo faces protests in Seattle amid concerns over impact on local
rideshare drivers", "url": "https://komonews.com/news/local/waymo-seattle-expansion-safety-concerns-driverless-cars-prepares-for-autonomous-operations", "snippet": "Waymo faces protests in Seattle
amid concerns over impact on local rideshare drivers\nSEATTLE \u2014 Protesters greeted the arrival of [Waymo](https://waymo.com/) into Seattle on Wednesday, raising concerns about the company's
safety record and that the introduction of autonomous ride-hailing services could take away jobs from drivers who work for companies such as Uber and Lyft.\n\"When I heard they were coming, I had the
feeling of these big companies coming here to take food and to take income from t", "api_data": null, "hint": null}, {"title": "Waymo expands self-driving vehicle service to Seattle | king5.com",
"url": "https://www.king5.com/article/traffic/traffic-news/autonomous-rideshare-waymo-seattle-expansion/281-0ea27688-6afa-401d-8d21-07fb4e5c3044", "snippet": null, "api_data": null, "hint": null},
{"title": "Waymo - Wikipedia", "url": "https://en.wikipedia.org/wiki/Waymo", "snippet": "Waymo LLC ( WAY-moh) is an American autonomous driving technology company headquartered in Mountain View,
California. It is a subsidiary of Alphabet Inc., Google's parent company. As of March 2026, Waymo operates public commercial robotaxi services in 10 US metropolitan areas, has 3,000 robotaxis in
service, provides 500,000 paid rides per week and had logged 200 million fully autonomous miles. \nThe company traces its origins to the Stanford Racing Team, which competed in the 2005 and 2007
Defen", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Waymo\", \"url\": \"https://en.wikipedia.org/wiki/Waymo\", \"extract\": \"Waymo LLC ( WAY-moh) is an American autonomous
driving technology company headquartered in Mountain View, California. It is a subsidiary of Alphabet Inc., Google's parent company. As of March 2026, Waymo operates public commercial robotaxi
services in 10 US metropolitan areas, has 3,000 robotaxis in service, provides 500,000 paid rides per week and had logged 200 million fully autonomous miles. \\nThe company traces its origins to the
Stanford Racing Team, which competed in the 2005 and 2007 Defense Advanced Research Projects Agency (DARPA) Grand Challenges. Google's development of self-driving technology began in January 2009 and
the project was revealed in October 2010. In December 2016, the project was renamed Waymo and spun out of Google as part of Alphabet. In October 2020, Waymo became the first company to offer service
to the public without safety drivers.\\nWaymo is run by co-CEOs Tekedra Mawakana and Dmitri Dolgov since April 2021. The company raised $11 billion in multiple outside funding rounds by 2024. In
February 2026, Waymo raised $16 billion, which valued the company at $126 billion.\\nIn January 2026, The National Transportation Safety Board and National Highway Traffic Safety Administration opened
investigations into Waymo's robotaxis for recurring incidents of illegally passing stopped school buses, and one incident where a robotaxi hit a child who ran out from behind a parked SUV in a school
zone.\", \"mode\": \"full\"}"}]}, "hint": null}, {"title": "Scaling our fleet through U.S. manufacturing", "url": "https://waymo.com/blog/2025/05/scaling-our-fleet-through-us-manufacturing/",
"snippet": "[Back](https://waymo.com/blog)\nScaling our fleet through U.S. manufacturing\nThe U.S. is leading the world in the development and deployment of autonomous driving technology. Today, Waymo
One provides more than 250,000 paid trips each week across Phoenix, San Francisco, Los Angeles, and Austin, and we\u2019re preparing to bring our fully autonomous ride-hailing to Atlanta, Miami, and
Washington, D.C. in 2026. We\u2019re proud to bring this technology \u2013 once thought to be the stuff of science fiction \u2013 to m", "api_data": null, "hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://komonews.com/news/local/waymo-seattle-expansion-safety-concerns-driverless-cars-prepares-for-autonomous-operations",
  "prompt": "What is the status of Waymo in Seattle? When did Waymo arrive? Is it serving public riders or just testing? When is the launch expected?"
}
```

### 📋 Result

```
{"url": "https://komonews.com/news/local/waymo-seattle-expansion-safety-concerns-driverless-cars-prepares-for-autonomous-operations", "content": "Based on the content:\n\n**Status:** Waymo is in the
early testing phase in Seattle. About a dozen vehicles are circulating in Seattle and the Eastside, being manually driven by trained specialists to collect data. The driverless cars are **not yet
allowed to operate** in Washington.\n\n**Arrival:** Waymo arrived in Seattle on **Wednesday** (the article doesn't specify the exact date, only that protesters greeted them \"on
Wednesday\").\n\n**Current operations:** **Testing only** - not serving public riders. Specialists are manually driving the vehicles to gather data on the area.\n\n**Launch timeline:** **No timeline
has been set** for autonomous testing in Seattle. The company will need to complete testing and receive necessary certification/permits before deploying autonomous services.\n\nThe typical Waymo
rollout process involves: 1) Manual driving for data collection (current phase), 2) Autonomous driving with specialist in driver's seat, 3) Fully autonomous operations once permitted and safety
frameworks are satisfied.\n\n**Relevant links:**\n- [Waymo](https://waymo.com/)\n- [Jaguar I-Pace (vehicle being used)](https://www.jaguarusa.com/all-models/i-pace/index.html)", "title": "Waymo faces
protests in Seattle amid concerns over impact on local rideshare drivers"}
```

```json
{
  "url": "https://hoodline.com/2026/02/waymo-floods-d-c-with-lobbyists-as-robotaxi-showdown-drags-on/",
  "prompt": "What is the status of Waymo's DC launch? Has it been delayed? What regulatory barriers exist? When might Waymo start serving riders in DC?"
}
```

### 📋 Result

```
{"url": "https://hoodline.com/2026/02/waymo-floods-d-c-with-lobbyists-as-robotaxi-showdown-drags-on/", "content": "## Status of Waymo's DC Launch\n\n**Current Status:**\nWaymo is **NOT** operating
driverless robotaxis in DC. The company is only running sensor-loaded Jaguars with human safety drivers, collecting data and mapping streets.\n\n**Has it been delayed?**\nYes. The launch has been
delayed due to regulatory barriers. DC Council members will not approve rider-only service until they receive a required safety study.\n\n**Regulatory Barriers:**\n\n1. **Missing DDOT Study**: The
main blocker is an unfinished safety report from the District Department of Transportation (DDOT). The 2020 Autonomous Vehicles Testing Program Amendment Act mandated this study with recommendations
and draft legislation for safe AV integration.\n\n2. **Agency Capacity Issues**: DDOT has faced budget and staffing constraints that have slowed completion of the report.\n\n3. **Divided Council**: \n
- Some members (like Janeese Lewis George) oppose robotaxis over job loss concerns\n   - Others (like Kenyan McDuffie) support them and have introduced legislation to legalize AVs\n   - Most want to
see the DDOT study before voting\n\n4. **Permitting Standoff**: Council members blame Mayor Bowser for not issuing driverless testing permits; the mayor's office says \"it's not
us.\"\n\n**Timeline:**\nDDOT told Waymo the study \"could be finished by this summer\" and expects to put forward recommendations \"later this year\" (2026). However, no firm date is set, and even
after the study is released, the Council would still need to vote on legislation before driverless service could begin.\n\n**Relevant links:**\n- [Axios: Waymo robotaxis
lobbying](https://www.axios.com/local/washington-dc/2026/02/27/waymo-robotaxis-lobbying-self-driving-cars)\n- [DC Law: Autonomous Vehicles Testing Program Amendment
Act](https://code.dccouncil.gov/us/dc/council/laws/23-156)\n- [Wired: Waymo hits a rough patch in Washington DC](https://www.wired.com/story/waymo-hits-a-rough-patch-in-washington-dc/)", "title":
"Waymo Turns Up Pressure On D.C. Over Robotaxi Permits"}
```

## 💬 Response

Now let me check the cities most likely to launch before May 1 - Las Vegas and Denver seem the closest.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "Waymo Las Vegas launch date spring 2026 public rides"
}
```

### 📋 Result

```
{"query": "Waymo Las Vegas launch date spring 2026 public rides", "results": [{"title": "Waymo bringing driverless rides to Las Vegas roads in 2026 - Las Vegas Sun News", "url":
"https://lasvegassun.com/news/2025/nov/04/waymo-bringing-driverless-rides-to-las-vegas/", "snippet": "Waymo bringing driverless rides to Las Vegas roads in
2026\n![waymo](http://media.lasvegassun.com/media/img/photos/2025/11/03/AP25301719767242_t650.jpg?5711a3b57decb389a12ba40e20471e031ff69545)\nWaymo vehicles wait at an intersection in San Francisco,
Wednesday, Oct. 22, 2025. The autonomous ride-hailing service is coming to Las Vegas in 2026. Photo by: Jeff Chiu / AP\nTuesday, Nov. 4, 2025 | 2 a.m.\nEditor's note: [Este art\u00edculo est\u00e1
traducido al espa\u00f1ol.](https://lasvegassun.com/news/2025/nov/04/w", "api_data": null, "hint": null}, {"title": "Waymo Plans Las Vegas Launch in Summer 2026 - 102.7 Coyote Country", "url":
"https://coyotecountrylv.com/2025/12/18/waymo-plans-las-vegas-launch-in-summer-2026/", "snippet": "Waymo Plans Las Vegas Launch in Summer 2026\nWaymo is preparing to bring its autonomous ride-hailing
service to Las Vegas, expanding from its established operations in Los Angeles and Phoenix. The company expects a full launch in the\u2026\n![SAN FRANCISCO, CALIFORNIA - APRIL 11: A Waymo autonomous
vehicle drives along Masonic Avenue on April 11, 2022 in San Francisco, California. San Francisco is serving as testing grounds for autonomous vehicles with Waymo, a Google subsidiary and Cruise, a
subsidiar", "api_data": null, "hint": null}, {"title": "Waymo Service Areas in the US: A Definitive Guide - Fifth Level Consulting", "url": "https://fifthlevelconsulting.com/waymo-service-areas-in-
the-u-s/", "snippet": "Last updated: November 2025\n[Waymo ](https://fifthlevelconsulting.com/autonomous-vehicles-10-amazing-things-to-know-about-waymo/)operates commercial robotaxi services available
to the public through its Waymo One app in several major U.S. cities. The Alphabet-owned company currently provides over 250,000 paid rides per week, marking a significant milestone in [autonomous
vehicle adoption](https://fifthlevelconsulting.com/key-components-of-autonomous-vehicles/). These [Waymo rides](https://fifthl", "api_data": null, "hint": null}, {"title": "Robotaxi company Waymo says
it will expand to Las Vegas in 2026", "url": "https://news3lv.com/news/local/autonomous-car-robotaxi-waymo-expanding-las-vegas-self-driving-ride-hailing-nevada-travel-driving-2026", "snippet":
"Robotaxi company Waymo says it will expand to Las Vegas in 2026\n![IPACE_2.jpg](/resources/media2/16x9/9504/986/0x495/90/5abc1cfb-4690-44b8-b000-814b83ade0f5-IPACE_2.jpg)\nLAS VEGAS (KSNV) \u2014 The
autonomous car company Waymo announced it plans to expand its robotaxi service to Las Vegas next summer.\nWaymo says its autonomous ride-hailing service will become available for residents and
visitors after it coordinates with local officials.\n\"The introduction of Waymo and its autonomous driving technolog", "api_data": null, "hint": null}, {"title": "Waymo Plans Las Vegas Launch in
Summer 2026 - Las Vegas Newsroom", "url": "https://lasvegasnewsroom.com/2025/12/18/waymo-plans-las-vegas-launch-in-summer-2026/", "snippet": "Waymo Plans Las Vegas Launch in Summer 2026\nWaymo is
preparing to bring its autonomous ride-hailing service to Las Vegas, expanding from its established operations in Los Angeles and Phoenix. The company expects a full launch in the\u2026\n![SAN
FRANCISCO, CALIFORNIA - APRIL 11: A Waymo autonomous vehicle drives along Masonic Avenue on April 11, 2022 in San Francisco, California. San Francisco is serving as testing grounds for autonomous
vehicles with Waymo, a Google subsidiary and Cruise, a subsidiar", "api_data": null, "hint": null}, {"title": "Waymo is bringing its robotaxis to Las Vegas, San Diego, and Detroit - The Robot Report",
"url": "https://www.therobotreport.com/waymo-brings-robotaxis-las-vegas-san-diego-detroit/", "snippet": "![A person walking towards a Waymo vehicle with a bag.](https://www.therobotreport.com/wp-
content/uploads/2025/11/waymo-featured.jpg)\n![A person walking towards a Waymo vehicle with a bag.](https://www.therobotreport.com/wp-content/uploads/2025/11/waymo-featured.jpg)\nWaymo said each
deployment starts with mapping the city, which its AVs use to keep track of their location at all times. | Source: Waymo\nToday, Waymo LLC announced it\u2019s bringing its autonomous ride-hailing
service to three more citi", "api_data": null, "hint": null}, {"title": "Autonomous driving company set to expand to Las Vegas in 2026", "url": "https://www.fox5vegas.com/2025/11/03/autonomous-
driving-company-set-expand-las-vegas-2026/", "snippet": "Autonomous driving company set to expand to Las Vegas in 2026\nLAS VEGAS ([FOX5](http://fox5vegas.com/)) \u2014 Autonomous driving company
Waymo announced on Monday that its robotaxi service will be available in Las Vegas in 2026.\nThe company, whose service is already available in San Francisco, Los Angeles, Phoenix, Atlanta and Austin,
has accumulated 100 million autonomous miles and 10 million trips, according to the news release from Waymo. Officials said the service\u2019s safety record demonstrates it", "api_data": null, "hint":
null}, {"title": "Waymo prepares to launch self-driving cars in Las Vegas", "url": "https://news3lv.com/news/local/waymo-prepares-to-launch-self-driving-cars-in-las-vegas", "snippet": "Waymo prepares
to launch self-driving cars in Las Vegas\n![gettyimages-2244379880-612x612.jpg](/resources/media2/16x9/612/986/0x32/90/2037b33b-f67b-40d2-9570-dfaf95a994b3-gettyimages2244379880612x612.jpg)\nLAS VEGAS
(KSNV) \u2014 Waymo is gearing up to introduce its self-driving cars to the streets of Las Vegas.\nThe company, which has already operated in cities like Los Angeles and Phoenix, is deploying sensor-
equipped vehicles in Southern Nevada as part of its preparation.\n\"We've done over 14 million ", "api_data": null, "hint": null}, {"title": "Waymo\u2019s metric for 2026 success: one million weekly
rides | Automotive World", "url": "https://www.automotiveworld.com/news/waymos-metric-for-2026-success-one-million-weekly-rides/", "snippet": "Waymo\u2019s metric for success in 2026 is reaching one
million paid weekly robotaxi rides in the US by the year\u2019s end, according to Co-Chief Executive Tekedra Mawakana, who described the milestone as an \u201cinflection point\u201d for the Alphabet
autonomous driving unit. The company currently provides roughly 400,000 paid rides per week across six cities and plans to expand testing and launch commercial services across 20 cities this year
within the US and internationally.\nMultiplying its scale by 2.5 will ", "api_data": null, "hint": null}, {"title": "Waymo launching self-driving service in Las Vegas: here\u2019s when", "url":
"https://www.8newsnow.com/news/local-news/waymo-launching-self-driving-service-in-las-vegas-heres-when/", "snippet": null, "api_data": null, "hint": null}]}
```

```json
{
  "query": "Waymo Denver public rides launch date spring April May 2026"
}
```

### 📋 Result

```
{"query": "Waymo Denver public rides launch date spring April May 2026", "results": [{"title": "Waymo's robotaxis set for driverless launch in Denver in 2026 - Axios Denver", "url":
"https://www.axios.com/local/denver/2025/12/05/waymo-denver-colorado-autonomous-robotaxi-2026", "snippet": null, "api_data": null, "hint": null}, {"title": "Waymo self-driving cars set to launch in
Denver, amid Colorado governor's push for safer roads (CBS News Colorado) \u2014 Colorado Department of Transportation", "url": "https://www.codot.gov/safety/shift-into-safe-news/2025/november/waymo-
self-driving-cars-set-to-launch-in-denver-amid-colorado-governors-push-for-safer-roads-cbs-news-colorado", "snippet": "Waymo self-driving cars set to launch in Denver, amid Colorado governor's push
for safer roads (CBS News Colorado)\nShift into Safe News\nWaymo announced its launch in Denver in September, but it's going to take a while before Denverites will be able to take a ride in one.
They're rolling out their service in phases.\n\u201cIt's really exciting to be one of the earlier cities in the country that's moving forward with this exciting new technology,\u201d Gov. Jared Polis
said.\nThe autonomous car company is her", "api_data": null, "hint": null}, {"title": "Despite not-so-snowy winter, Waymo still steering toward 2026 Denver rollout", "url":
"https://www.denver7.com/money/science-and-tech/despite-not-so-snowy-winter-waymo-still-steering-toward-2026-denver-rollout", "snippet": "DENVER \u2014 Autonomous taxi company Waymo is still on track
to start giving rides in Denver \"later this year,\" despite a warm and dry winter, the company told Denver7 this week.\nWaymo \u2014 a subsidiary of Google parent company Alphabet \u2014 [announced
in September](https://www.denver7.com/news/local-news/googles-autonomous-ride-service-waymo-is-coming-to-denver) that it plans to expand to Denver. It has been testing its self-driving SUVs and vans
on city streets in recent months, with humans still sittin", "api_data": null, "hint": null}, {"title": "Waymo Updates | Get updates on cities Waymo serves", "url": "https://waymo.com/updates/",
"snippet": "Waymo is coming soon to your city\nKeep in touch\nThank you. You\u2019re all set.\nThank you for joining us on our journey. We're excited to keep you in the loop as we bring the safety and
mobility benefits of the Waymo Driver to more communities.\n- San Francisco Bay Area, CA\n- Sacramento, CA\n- Los Angeles, CA\n- Seattle, WA\n- San Diego, CA\n- Las Vegas, NV\n- Phoenix, AZ\n- Denver,
CO\n- San Antonio, TX\n- Austin, TX\n- Dallas, TX\n- Houston, TX\n- Minneapolis, MN\n- St. Louis, MO\n- New Orleans, LA\n- Chicago, IL", "api_data": null, "hint": null}, {"title": "Self-driving car
company Waymo heading to metro Denver in 2026 - The Colorado Sun", "url": "https://coloradosun.com/2025/09/02/self-driving-car-company-waymo-heading-to-metro-denver-in-2026/", "snippet": "Waymo is on
the way to Denver, the autonomous-driving technology company said Tuesday.\nThe Silicon Valley company, a subsidiary of Alphabet and formerly known as the Google Self-Driving Car Project, will be one
of first driverless car services to hit the road in Colorado, at least for ride-hailing passengers. The company is already offering rides to customers in Atlanta, Austin, Los Angeles, Phoenix and San
Francisco.\nBut for locals hoping to hail a ride soon, that\u2019s not happening just yet, Waym", "api_data": null, "hint": null}, {"title": "Waymo\u2019s autonomous cars are testing on Denver
streets. Are rides to the airport in the future?", "url": "https://coloradosun.com/2025/09/18/waymos-autonomous-cars-denver-airport/", "snippet": "Autonomous cars from Waymo began driving around
Denver\u2019s streets [this month](https://coloradosun.com/2025/09/02/self-driving-car-company-waymo-heading-to-metro-denver-in-2026/). While they\u2019re still in training mode and have a human
driver doing the legwork, the driverless ride-service company has big plans for Colorado\u2019s future: airport service.\n\u201cWe can\u2019t wait to at some point serve Denver International
Airport,\u201d said Suzanne Philion, Waymo\u2019s vice president of marketing, communications and publ", "api_data": null, "hint": null}, {"title": "Waymo Service Areas in the US: A Definitive Guide -
Fifth Level Consulting", "url": "https://fifthlevelconsulting.com/waymo-service-areas-in-the-u-s/", "snippet": "Last updated: November 2025\n[Waymo ](https://fifthlevelconsulting.com/autonomous-
vehicles-10-amazing-things-to-know-about-waymo/)operates commercial robotaxi services available to the public through its Waymo One app in several major U.S. cities. The Alphabet-owned company
currently provides over 250,000 paid rides per week, marking a significant milestone in [autonomous vehicle adoption](https://fifthlevelconsulting.com/key-components-of-autonomous-vehicles/). These
[Waymo rides](https://fifthl", "api_data": null, "hint": null}, {"title": "Waymo self-driving cars set to launch in Denver, amid Colorado governor's push for safer roads - CBS Colorado", "url":
"https://www.cbsnews.com/colorado/news/waymo-self-driving-cars-denver-colorado-governors-safer-roads/", "snippet": "Waymo self-driving cars set to launch in Denver, amid Colorado governor's push for
safer roads\nWaymo announced its launch in Denver about two weeks ago, but it's going to take a while before Denverites will be able to take a ride in one. They're rolling out their service in
phases.\n\"It's really exciting to be one of the earlier cities in the country that's moving forward with this exciting new technology,\" Gov. Jared Polis.\nThe autonomous car company is here thanks
to the support from Gov. Polis", "api_data": null, "hint": null}, {"title": "Waymo bringing self-driving ride-hailing to Denver; public rides will follow testing phase", "url":
"https://kdvr.com/news/local/waymo-bringing-self-driving-ride-hailing-to-denver-public-rides-will-follow-testing-phase/", "snippet": null, "api_data": null, "hint": null}, {"title": "Buckle Up: Is
Waymo Ready for Denver's Winter Roads and Angry Drivers?", "url": "https://www.westword.com/news/can-waymo-overcome-denver-winter-roads-angry-drivers-40790292/", "snippet": "![cartoon of a waymo car
driving through Denver](https://www.westword.com/wp-content/uploads/sites/2/2025/10/image-1-1.png)\nBradley Hansen\n![Carbonatix Pre-Player Loader](https://gamalpha.com/images/tts-pre-
loader.gif)\nAudio By Carbonatix\nKeep Westword Free\nWe\u2019re aiming to raise $20,000 by April 26. Your support ensures Westword can continue watching out for you and our community. No paywall.
Always accessible. Daily online and weekly in print.\nA new type of vehicle has emerged on Denver\u2019s roads", "api_data": null, "hint": null}]}
```

## 💭 Thinking

Let me now synthesize what I know. The question asks whether Waymo will make fully autonomous rides available to public riders in ANY of these cities before May 1, 2026: Baltimore, Boston, Charlotte, Chicago, Detroit, Denver, Las Vegas, New York, Seattle, or Washington DC.

Key findings for each city:

1. **Las Vegas**: Planned for "Summer 2026" - this is AFTER May 1, 2026. Still in testing/preparation phase.

2. **Denver**: "Later this year" (2026) - still testing with human drivers. No specific launch date. Denver7 article says "later this year" which is vague.


3. **Washington DC**: Regulatory hurdles are significant—the DDOT study won't be complete until potentially summer 2026, and council approval depends on it. Highly unlikely before May 1.

4. **Seattle**: Only just arrived with manual operations, nowhere near autonomous service yet.

5. **Chicago**: Still in groundwork phase with no regulatory framework in place in Illinois.

6. **Detroit**: Expansion announced but no concrete timeline provided.

7. **Baltimore, Boston, Charlotte, New York**: No imminent launch plans on the horizon. Boston is limited to snowy condition testing only.

The question was published today (April 10, 2026), so I'm working with current information as of this date.

With only about three weeks until the May 1 deadline, I need to assess what's actually feasible. Waymo currently operates in 11 metro areas as of Nashville's April 7 launch, but none of the cities listed in the question are among them. Las Vegas is targeted for summer 2026, Denver for later this year, and Detroit remains in early expansion phases—all well beyond the tight timeframe. Given Waymo's typical months-long testing period before public service launches and the absence of any recent announcements suggesting an imminent rollout in any of these cities, the odds of a YES resolution are quite low.

That said, I should account for the possibility that Waymo could accelerate—they did manage to expand to four cities simultaneously in February 2026. The question only requires one city from the list to launch, so there's a non-zero chance of a surprise announcement. I'm also realizing I should double-check the Waymo website directly to see what their tracker currently shows about which cities are actively serving riders versus which are upcoming, since that's the actual resolution source. on April 7, so another launch within 20 days is possible given their pace, but the explicit "Summer 2026" timeline for Las Vegas and lack of concrete announcements for other cities makes it unlikely. I'm settling on roughly 10% probability, accounting for the small chance of a surprise early launch or unannounced acceleration, but weighted heavily toward the status quo holding through May 1.

The question being published today suggests there's genuine uncertainty rather than a trivial answer either way, though I should be careful not to over-interpret the framing since this appears to be auto-generated. Let me check if there's any recent news or market signals that might shift my estimate.

## 💬 Response

Let me check for very recent news and prediction markets.

## 🔧 Tool: mcp__search__search_exa


## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "query": "Waymo launch new city April 2026",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "Waymo Launches Driverless Ride-Share Service in Nashville | Months after announcing plans to bring fully autonomous ride-hailing to Nashville, Waymo has officially launched its first
public robotaxi service in the city.", "url": "http://thestarnewsnetwork.com/2026/04/08/waymo-launches-driverless-ride-share-service-in-nashville/?redirected=1", "snippet": "Waymo Launches Driverless
Ride-Share Service in Nashville | Months after announcing plans to bring fully autonomous ride-hailing to Nashville, Waymo has officially launched its first public robotaxi service in the city.\n\n#
Waymo Launches Driverless Ride-Share Service in Nashville\n\nMonths after announcing plans to bring fully autonomous ride-hailing to Nashville, Waymo has officially launched its first public robotaxi
service in the city.\n\nIn a press release on Tuesday, Waymo confirmed that it ha", "highlights": ["Waymo Launches Driverless Ride-Share Service in Nashville | Months after announcing plans to bring
fully autonomous ride-hailing to Nashville, Waymo has officially launched its first public robotaxi service in the city. # Waymo Launches Driverless Ride-Share Service in Nashville Months after
announcing plans to bring fully autonomous ride-hailing to Nashville, Waymo has officially launched its first public robotaxi service in the city. In a press release on Tuesday, Waymo confirmed that
it has begun inviting riders to use its driverless vehicles, with access rolling out gradually through the Waymo app. The company said the phased approach is designed to ensure a smooth and consistent
user experience as demand for the service in the area grows. Nashville, meet your new favorite way to move \u2728 Starting today, we\u2019re welcoming the first riders in Music City!
pic.twitter.com/LixK7IVAP7 \u2014 Waymo (@Waymo) April 7, 2026 The initial service area spans roughly 60 square miles, covering some of Nashville\u2019s busiest and most recognizable neighborhoods,
including Downtown, Midtown, East Nashville, and Music Row. The company also said it is actively testing service at Nashville International Airport, with plans to include airport rides in the near
future. Waymo Co-CEO Tekedra Mawakana said the launch reflects the city\u2019s rapid growth and vibrant culture. She noted that the service aims to provide a \u201csafe, reliable, and magical\u201d
transportation option for both residents and visitors navigating Nashville\u2019s busy entertainment and tourism scene. The launch builds on last year\u2019s announcement of a partnership with Lyft.
While rides are currently booked through Waymo\u2019s own app, integration with Lyft is expected later in 2026, with Lyft also serving as the fleet management partner through its Flexdrive program.
Governor Bill Lee supported the rollout, saying autonomous vehicle technology represents an important opportunity to   ...    \u201cAs families and businesses move to Tennessee in record numbers, our
state continues to lead the nation in finding innovative solutions to transportation challenges,\u201d Lee said. \u201cBy leveraging private sector technologies like Waymo\u2019s   ...    economic
growth.\u201d Waymo\u2019s Nashville rollout follows the company\u2019s testing of its self-driving technology on the streets of Music City last year. Before launching in a new area, Waymo says it
first creates detailed maps that include lane markings, stop signs, curbs, and crosswalks. Instead of relying solely on GPS, which the company says can be unreliable, its self-driving system uses
custom maps, real-time sensor data, and artificial intelligence to precisely determine its location on the road at all times. The company pointed to safety data from more than 170 million autonomous
miles driven, saying its vehicles have shown roughly a 13-fold reduction in crashes involving serious injuries or pedestrians compared to human drivers.   ...    Name *\n\nEmail *\n\nWebsite\n\nSave
my name, email,"], "published_date": "2026-04-08T19:05:03.000", "score": null}, {"title": "Your Waymo ride, now arriving in Nashville", "url": "https://waymo.com/blog/2026/04/your-waymo-ride-now-
arriving-in-nashville/", "snippet": "Your Waymo ride, now arriving in Nashville\n\nStarting today, Waymo is welcoming the first public riders into our fully autonomous ride-hailing service in
Nashville. Download the Waymo app and get ready to ride, as we begin inviting riders on a rolling basis. This approach allows us to thoughtfully scale while delivering a consistent, high-quality
experience.\n\nWaymo offers a new way to move through Nashville\u2014whether you\u2019re catching a show, meeting friends, or exploring the city. Our initial 60-squ", "highlights": ["Your Waymo ride,
now arriving in Nashville Starting today, Waymo is welcoming the first public riders into our fully autonomous ride-hailing service in Nashville. Download the Waymo app and get ready to ride, as we
begin inviting riders on a rolling basis. This approach allows us to thoughtfully scale while delivering a consistent, high-quality experience. Waymo offers a new way to move through
Nashville\u2014whether you\u2019re catching a show, meeting friends, or exploring the city. Our initial 60-square-mile service area covers Music City\u2019s most iconic spots, from the honky tonks of
Broadway and the boutiques of 12 South, to the energy of Midtown and the foodie scene in East Nashville. Plus, we are currently testing at Nashville International Airport and intend to serve travelers
there in the near future. \u201cNashville is buzzing with music, tourism, and nightlife, and now Waymo helps connect it all,\u201d said Tekedra Mawakana, co-CEO of Waymo. \u201cAs Nashville continues
to grow, Waymo is proud to support that momentum by providing a safe, reliable, and magical way for locals and visitors to experience everything the city has to offer.\u201d We are honored to have the
support of community and elected leaders in Tennessee and Nashville. They have embraced Waymo\u2019s fully autonomous service, recognizing the opportunity to expand access to innovative and safe
transportation   ...    \u201cAs families and businesses move to Tennessee in record numbers, our state continues to lead the nation in finding   ...    technologies like Waymo's fully autonomous
vehicles, we're expanding mobility in ways we couldn't achieve on our own   ...    \u201cWaymo is an opportunity for older adults to embrace new technology and new ways of getting around,\u201d said
Grace Sutherland Smith, Executive Director, AgeWell Middle Tennessee. \u201cIt's so important as we grow older to stay connected to the community and transportation is a key to that. We also believe
the advance booking feature can help lighten the load on family caregivers who may have to take time off work to drive loved ones to appointments. So we're excited about Waymo coming to Nashville and
being an option for the older adults and caregivers we serve.\u201d We\u2019re looking forward to helping make roads safer in Nashville. Data from over 170 million miles traveled shows that, compared
to human drivers, we achieved a 13 fold reduction in crashes that involved serious injury or worse and the same reduction in crashes that involved injuries with pedestrians. We\u2019re excited to
provide riders with more choice. In addition to hailing fully autonomous rides on the Waymo app, we'll also start serving rides on the Lyft app later this year. Lyft will also serve as our fleet
management partner in Nashville via Flexdrive. Nashville, we can\u2019t wait for you to experience the future of driving in Music City. If you want to be one of the first riders, make sure you
download the Waymo app and keep an eye on our social channels for access codes to skip the line."], "published_date": "2026-04-07T15:45:12.000", "score": null}, {"title": "Waymo is live in Nashville.
| The Verge", "url": "https://www.theverge.com/transportation/907851/waymo-is-live-in-nashville", "snippet": "Waymo is live in Nashville. | The Verge\n\nThe homepageThe Verge logo.\n\nThe homepageThe
Verge logo.\n\nSelf-driving cars: Google and others map the road to automated vehiclesSee all Stories\n\nPosted Apr 7, 2026 at 1:00 PM UTC\n\nA\n\nWaymo is live in Nashville.\n\nThe robotaxi company
said today that it will start accepting its first public riders in Music City. Customers, who will be invited to ride on a rolling basis, can initially hail a ride through the Waymo app, and then
later matched with a vehicle ", "highlights": ["Waymo is live in Nashville. | The Verge\n\nThe homepageThe Verge logo.\n\nThe homepageThe Verge logo. Self-driving cars: Google and others map the road
to automated vehiclesSee all Stories Posted Apr 7, 2026 at 1:00 PM UTC\n\nA\n\nWaymo is live in Nashville. The robotaxi company said today that it will start accepting its first public riders in Music
City. Customers, who will be invited to ride on a rolling basis, can initially hail a ride through the Waymo app, and then later matched with a vehicle through the Lyft app. Lyft will also handle
fleet services, such as cleaning, maintenance, and EV charging. Waymo first started testing its vehicles in Nashville in early 2025. For those keeping score, the company now operates commercially in
11 cities. Waymo\u2019s service area in Nashville. Image: Waymo Follow topics and authors from this story to see more like this in your personalized homepage feed and to receive email updates. Andrew
J. Hawkins\n\nAutonomous Cars\n\nTransportation\n\nWaymo\n\nComments\n\nLoading comments Getting the conversation ready...\n\n## Most Popular\n\nMost Popular I tested three Windows laptops in the
MacBook Neo\u2019s price range \u2014 there\u2019s no contest The MacBook Neo is the best thing to happen to Windows in years   ...    ## The Verge Daily\n\nA free daily digest of the news that
matters most.\n\nEmail (required)\n\nSign Up By submitting your email, you agree to our Terms and Privacy Notice. This site is protected by reCAPTCHA and the Google   ...    ## More in
Transportation\n\nTesla is un-canceling its plan to build a smaller, cheaper EV: report Waymo is offering to help cities fix their potholes\n\nAmflow\u2019s latest e-bikes with Avinox motors raise the
bar again Intel will help build Elon Musk\u2019s Terafab AI chip factory Robotaxi companies won\u2019t say how often remote operators intervene\n\nIs the Slate Truck too minimal for its own good?
Tesla is un-canceling its plan to build a smaller, cheaper EV: report\n\nAndrew J. HawkinsApr 9 Waymo is offering to help cities fix their potholes\n\nAndrew J. HawkinsApr 9 Amflow\u2019s latest
e-bikes with Avinox motors raise the bar again\n\nThomas RickerApr 9 Intel will help build Elon Musk\u2019s Terafab AI chip factory\n\nAndrew J. HawkinsApr 7 Robotaxi companies won\u2019t say how
often remote operators intervene\n\nAndrew J. HawkinsApr 6 Is the Slate Truck too minimal for its own good?\n\nAndrew J. HawkinsApr 5 Advertiser Content FromThis is the title for the native ad\n\n##
Top Stories\n\nApr 9 The MacBook Neo is the best thing to happen to Windows in years\n\nApr 9 The AI industry\u2019s race for profits is now existential\ufeff\n\nApr 9\n\nA jury is about to decide the
fate of Ticketmaster Apr 9\n\nI tested three Windows laptops in the MacBook Neo\u2019s price range \u2014 there\u2019s no contest\n\nApr 8 I finally get the iPhone Air\n\nApr 9\n\nThe Exit 8 movie is
even better if you play the game first"], "published_date": "2026-04-07T13:00:00.000", "score": null}, {"title": "Ready to Ride: Dallas, Houston, San Antonio, and Orlando", "url":
"http://waymo.com/blog/2026/02/dallas-houston-san-antonio-orlando", "snippet": "Ready to Ride: Dallas, Houston, San Antonio, and Orlando\n\nToday, we continue our accelerated growth and welcome the
first public riders into our fully autonomous ride-hailing service in four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the public
in multiple cities simultaneously, this brings our total commercial metro areas to 10, and deepens our commitment in the states of Texas and Florida.\n\nSelect riders from the tens of thousan",
"highlights": ["Ready to Ride: Dallas, Houston, San Antonio, and Orlando Today, we continue our accelerated growth and welcome the first public riders into our fully autonomous ride-hailing service in
four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the public in multiple cities simultaneously, this brings our total commercial
metro areas to 10, and deepens our commitment in the states of Texas and Florida. Select riders from the tens of thousands in these cities who have downloaded the Waymo app will receive an invitation
to take their first local rides today. We will be inviting new riders on a rolling basis to ensure a seamless experience across our initial service areas, as we meaningfully scale our operations ahead
of opening our service to everyone later this year. Waymo is the only company successfully operating a commercial fully autonomous ride-hailing service at scale in multiple complex urban environments,
and we\u2019re ramping up with these new expansions. We\u2019ll continue to follow our   ...    \u201cWaymo is serving more riders than ever, as we are on track to serve over one million rides per
week by the end of this year,\u201d said Tekedra Mawakana, co-CEO of Waymo. \u201cDallas, Houston, San Antonio, and Orlando are critical to our plans, as we lay groundwork for service in 20+ cities.
Each community has its own unique charm and transportation needs, and we\u2019re eager to provide a safe, reliable, and magical way for locals and visitors to travel.\u201d Our generalizable
technology handles each city\u2019s unique environment, from the bright midday sun to sudden downpours to freezing temperatures. New riders will use our reliable service to travel to their city\u2019s
popular destinations, like a night out in Dallas\u2019s Bishop Arts District, seeing a show at Houston\u2019s Toyota Center, catching a San Antonio Spurs game, or experiencing one of Orlando\u2019s
latest attractions. City and community leaders have welcomed Waymo\u2019s fully autonomous service in their communities: \u201cDallas is excited for Waymo to launch operations in our city, providing
Dallas residents and visitors with new, innovative transportation options,\u201d said Eric L. Johnson, Dallas Mayor. \u201cThe availability of Waymo\u2019s fully autonomous ride service further
cements Dallas\u2019s reputation as one of America\u2019s most innovative and dynamic cities. Together, we   ...    \u201cWe\u2019ve been working with Waymo for several months to make today\u2019s
announcement possible,\u201d said Orlando Mayor Buddy Dyer. \u201cThe launch of their commercial service in Orlando is another example of our city\u2019s forward thinking and commitment to innovation.
Starting today, our residents will have another option to safely move about the area, and our visitors will be welcomed with the world class mobility they deserve. Welcome to Orlando, Waymo!\u201d
...    said Houston City Council Member Sallie Alcorn. \u201cI'm thrilled that we are now launching limited access public rides   ...    upcoming events like the World Baseball Classic and the World
Cup.\" \u201cThe Greater San Antonio Chamber is proud to celebrate Waymo\u2019s expansion to limited public rides here in San Antonio,\u201d   ...    Antonio\u2019s workforce, infrastructure, and
forward-thinking business climate.\u201d With over 200 million fully autonomous miles traveled, we are proud to improve road safety in cities where we operate. Data from over 127 million miles
traveled shows we achieved a ten-fold reduction in serious injury or worse crashes and 12-fold reduction in injury crashes with pedestrians compared to human drivers, and we are excited to bring these
safety benefits to Dallas, Houston, San Antonio, and Orlando. We believe that the best way to serve a community is to listen to the people who live there. That\u2019s why we\u2019re working closely
with local organizations in these new cities -"], "published_date": "2026-02-24T08:01:30.000", "score": null}, {"title": "Ready to Ride: Dallas, Houston, San Antonio, and Orlando", "url":
"https://blog.waymo.com/blog/2026/02/dallas-houston-san-antonio-orlando", "snippet": "Ready to Ride: Dallas, Houston, San Antonio, and Orlando\n\nToday, we continue our accelerated growth and welcome
the first public riders into our fully autonomous ride-hailing service in four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the
public in multiple cities simultaneously, this brings our total commercial metro areas to 10, and deepens our commitment in the states of Texas and Florida.\n\nSelect riders from the tens of thousan",
"highlights": ["Ready to Ride: Dallas, Houston, San Antonio, and Orlando Today, we continue our accelerated growth and welcome the first public riders into our fully autonomous ride-hailing service in
four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the public in multiple cities simultaneously, this brings our total commercial
metro areas to 10, and deepens our commitment in the states of Texas and Florida. Select riders from the tens of thousands in these cities who have downloaded the Waymo app will receive an invitation
to take their first local rides today. We will be inviting new riders on a rolling basis to ensure a seamless experience across our initial service areas, as we meaningfully scale our operations ahead
of opening our service to everyone later this year. Waymo is the only company successfully operating a commercial fully autonomous ride-hailing service at scale in multiple complex urban environments,
and we\u2019re ramping up with these new expansions. We\u2019ll continue to follow our   ...    \u201cWaymo is serving more riders than ever, as we are on track to serve over one million rides per
week by the end of this year,\u201d said Tekedra Mawakana, co-CEO of Waymo. \u201cDallas, Houston, San Antonio, and Orlando are critical to our plans, as we lay groundwork for service in 20+ cities.
Each community has its own unique charm and transportation needs, and we\u2019re eager to provide a safe, reliable, and magical way for locals and visitors to travel.\u201d Our generalizable
technology handles each city\u2019s unique environment, from the bright midday sun to sudden downpours to freezing temperatures. New riders will use our reliable service to travel to their city\u2019s
popular destinations, like a night out in Dallas\u2019s Bishop Arts District, seeing a show at Houston\u2019s Toyota Center, catching a San Antonio Spurs game, or experiencing one of Orlando\u2019s
latest attractions. City and community leaders have welcomed Waymo\u2019s fully autonomous service in their communities: \u201cDallas is excited for Waymo to launch operations in our city, providing
Dallas residents and visitors with new, innovative transportation options,\u201d said Eric L. Johnson, Dallas Mayor. \u201cThe availability of Waymo\u2019s fully autonomous ride service further
cements Dallas\u2019s reputation as one of America\u2019s most innovative and dynamic cities. Together, we   ...    \u201cWe\u2019ve been working with Waymo for several months to make today\u2019s
announcement possible,\u201d said Orlando Mayor Buddy Dyer. \u201cThe launch of their commercial service in Orlando is another example of our city\u2019s forward thinking and commitment to innovation.
Starting today, our residents will have another option to safely move about the area, and our visitors will be welcomed with the world class mobility they deserve. Welcome to Orlando, Waymo!\u201d
...    said Houston City Council Member Sallie Alcorn. \u201cI'm thrilled that we are now launching limited access public rides   ...    upcoming events like the World Baseball Classic and the World
Cup.\" \u201cThe Greater San Antonio Chamber is proud to celebrate Waymo\u2019s expansion to limited public rides here in San Antonio,\u201d   ...    Antonio\u2019s workforce, infrastructure, and
forward-thinking business climate.\u201d With over 200 million fully autonomous miles traveled, we are proud to improve road safety in cities where we operate. Data from over 127 million miles
traveled shows we achieved a ten-fold reduction in serious injury or worse crashes and 12-fold reduction in injury crashes with pedestrians compared to human drivers, and we are excited to bring these
safety benefits to Dallas, Houston, San Antonio, and Orlando. We believe that the best way to serve a community is to listen to the people who live there. That\u2019s why we\u2019re working closely
with local organizations in these new cities -"], "published_date": "2026-02-24T14:29:46.000", "score": null}, {"title": "Waymo debuts driverless ride-share vehicles on Nashville streets", "url":
"https://www.tennessean.com/story/money/cars/2026/04/07/waymo-driverless-rideshare-vehicles-nashville-autonomous/89450952007/", "snippet": "Waymo debuts driverless ride-share vehicles on Nashville
streets\n\n# Waymo launches driverless ride-share service in Nashville\n\nNashville Tennessean\n\nUpdated April 7, 2026, 10:43 a.m. CT\n\nNashville\u2019s first driverless ride\u2011share vehicles
began operating April 7, featuring an empty driver\u2019s seat and a self\u2011steering wheel.\n\nThe service, operated by Waymo, is now available citywide.\n\n\u201cToday\u2019s an important day
because it\u2019s the first time people in Nashville and the general public can take a Waymo,\u201d Wa", "highlights": ["Waymo debuts driverless ride-share vehicles on Nashville streets # Waymo
launches driverless ride-share service in Nashville\n\nNashville Tennessean Updated April 7, 2026, 10:43 a.m. CT Nashville\u2019s first driverless ride\u2011share vehicles began operating April 7,
featuring an empty driver\u2019s seat and a self\u2011steering wheel. The service, operated by Waymo, is now available citywide. \u201cToday\u2019s an important day because it\u2019s the first time
people in Nashville and the general public can take a Waymo,\u201d   ...    Riders won\u2019t find a driver\u2019s seat to claim up front. The vehicle will detect unauthorized seating and trigger a
call   ...    pedestrians and vehicles \u2014 even those outside the rider\u2019s direct line of sight. A subsidiary of Alphabet, Google\u2019s parent company, Waymo will deploy \u201ca couple
dozen\u201d autonomous vehicles throughout a 60-square-mile service area in Nashville Tuesday, Lewis said. While Lewis declined to specify how many autonomous vehicles will be operating in Music City,
he said the company is planning to expand its Nashville footprint. \u201cAs we gain more experience here and we have more vehicles, we\u2019ll be able to serve more of the territory and we   ...
Currently, Waymo is selecting riders who have joined the waitlist on the company\u2019s mobile app. The price is slightly   ...    thousands strong,\" Lewis said, adding \"that will allow you to test
the magic of Waymo yourself.\" In late April, ride-share giant Lyft will manage the Waymo fleet in Nashville. \u201cLater in the year, the Lyft app will also serve rides, but it\u2019s in addition to
the Waymo app,\u201d Lewis said. \u201cSo, when that happens, if you definitely want a Waymo, to be matched with a Waymo, just order through the Waymo app. \u201cBut if you\u2019re indifferent and
you\u2019re looking for a ride, we\u2019re part of the options of the Lyft family.\u201d   ...    A Waymo vehicle, known as a Jaguar I-pace, is equipped with six radars for speed and distance
accuracy, five lidars for   ...    For the last six months, Waymo has been training on Nashville\u2019s streets to learn traffic patterns and awkward   ...    13 times fewer crashes with serious
injuries, 13 times fewer pedestrian injuries and six times fewer crashes resulting   ...    Waymo robotaxis after one of the autonomous vehicles reportedly failed to stop for a parked Atlanta school
bus. ## What cities have Waymo driverless cars? Nashville marks the company\u2019s 11th city across the U.S., according to Waymo. Waymo also operates in these cities: - Atlanta\n- Austin\n- Dallas\n-
Houston\n- Los Angeles\n- Miami\n- Nashville\n- Orlando\n- Phoenix\n- San Antonio - San Francisco Bay Area ### Waymo plans to expand to these cities: - Baltimore\n- Boston\n- Charlotte\n- Chicago\n-
Denver\n- Detroit\n- Las Vegas\n- London\n- Minneapolis\n- New Orleans - Philadelphia\n- Pittsburgh\n- Sacramento\n- San Diego\n- Seattle\n- St. Louis\n- Tampa\n- Tokyo\n- Washington, D."],
"published_date": "2026-04-07T13:01:09.000", "score": null}, {"title": "Waymo - From the road", "url": "https://waymo.com/blog?modal=short-back-to-boston", "snippet": "Waymo - From the road\n\n##
Ready to Ride: Dallas, Houston, San Antonio, and Orlando\n\nToday, we continue our accelerated growth and welcome the first public riders into our fully autonomous ride-hailing service in four new
cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking the first time we\u2019ve opened to the public in multiple cities simultaneously, this brings our total commercial metro areas
to 10, and deepens our commitment in the states of Texas and Florida.\n\nThe Waymo Te", "highlights": ["Waymo - From the road\n\n## Ready to Ride: Dallas, Houston, San Antonio, and Orlando Today, we
continue our accelerated growth and welcome the first public riders into our fully autonomous ride-hailing service in four new cities: Dallas, Houston, San Antonio, and Orlando. In addition to marking
the first time we\u2019ve opened to the public in multiple cities simultaneously, this brings our total commercial metro areas to 10, and deepens   ...    The Waymo Team\n\nFebruary 24, 2026\n\nRead
more   ...    be awarded to students and working technicians in Boston, Washington, D.C., New York City, Seattle, Denver, Phoenix, Chicago, Houston, and Miami, and we\u2019ll explore expanding the
partnership\u2019s scope as we grow together. The Waymo Team\n\nFebruary 19, 2026\n\nRead more   ...    Waymo will begin fully autonomous operations with its 6th-generation Driver \u2014an important
step in bringing our   ...    Satish Jeyachandran, Vice President of Engineering\n\nFebruary 12, 2026\n\nRead more It\u2019s time for Waymo in the Windy City! Chicago is a city of culture, ambition,
and an unyielding spirit of innovation, making it the perfect next stop for the World\u2019s Most Experienced Driver\u2122. We are excited to begin laying the early   ...    Charlotte blends its
historic charm with North Carolina\u2019s economic dynamism. Uptown \u2013 the city\u2019s sports hub \u2013 is surrounded by vibrant neighborhoods, from South End with its breweries and restaurants
to the arts of NoDa. The Queen City is constantly redefining itself, and it\u2019s this same forward-looking culture that makes us thrilled to announce Waymo\u2019s intention to bring our safe, magic,
fully autonomous ride-hailing to Charlotte, North Carolina.   ...    Ryan McNamara, Vice President and Global Head of Operations at Waymo\n\nFebruary 17, 2026\n\nRead more In America\u2019s 250th
year, we\u2019re excited to return to Boston \u2013 one of the nation\u2019s oldest cities \u2013 to build on insights   ...    We learned a lot from last year\u2019s visit, and we\u2019re excited to
cont  Want to help bring Waymo to Boston and experience a new way of getting around? Join us at waymo.com/updates. The Waymo Team\n\nFebruary 5, 2026\n\nRead more Waymo is headed to Sacramento! As
California\u2019s capital and a growing center for progress, Sacramento\u2019s spirit of innovation makes it the perfect next step for our expansion. We are eager to bring the future of mobility to
this vibrant community, connecting its historic landmarks with its modern neighborhoods.  Ready to experience Waymo in Sacramento? Sign up for updates and be among the first to ride when we\u2019re
ready: waymo.com/updates. The Waymo Team\n\nFebruary 5, 2026\n\nRead more  The Waymo Team\n\nFebruary 4, 2026\n\nRead more Charlotte blends its historic charm with North Carolina\u2019s economic
dynamism. Uptown \u2013 the city\u2019s sports hub \u2013 is surrounded by vibrant neighborhoods, from South End with its breweries and restaurants to the arts of NoDa. The Queen City is constantly
redefining itself, and it\u2019s this same forward-looking culture that makes us thrilled to announce Waymo\u2019s intention to bring our safe, magic, fully autonomous ride-hailing to Charlotte, North
Carolina.  \u201cCharlotte is   ...    fully autonomous driving shows the Waymo Driver was involved  It\u2019s time for Waymo in the Windy City! Chicago is a city   ...    Experienced Driver\u2122. We
are excited to begin laying the early groundwork for our ride-hailing operations in Chicago,   ...    Mariah Carey holiday design!  We\u2019re making it official, Philly: Waymo will bring our service
to the City of Brotherly Love!  We\u2019ve made great progress since arriving in Philadelphia this summer. After a period of manual testing, we   ...    transportation goals.  This week, we\u2019ll
start manually driving in Pittsburgh\u2019s downtown core with a fleet of our 5th   ...    groundwork for fully autonomous rides, beginning with the first permit ever issued by New York City\u2019s
Department of   ...    Spotify is now integrated with the Waymo app. \ud83c\udfb6\ud83d\udc96 Why choose when you can have #boffum. Vibe today  We\u2019re elevating the Waymo experience in the Mile
High City as we arrive in Denver this fall to lay the groundwork for a fully autonomous service in the future.  We\u2019ll arrive with a mixed fleet of Jaguar I-PACE with the 5th-generation Waymo
Driver and Zeekr   ...    operations in harsher climates.  \u201cAcross San Francisco, we are expanding safe, reliable, and modern transportation   ...    to everything our city has to offer,\u201d
said Mayor Lurie. \u201cWe announced in March that we wanted visitors to be able to ride in a Waymo as soon as they arrived in San Francisco, and today, we are taking another important step to get
there.\u201d  Waymo arrived in Tokyo this April and has been adapting our technology and operations for Japan\u2019s capital as we expand to major cities across the U.S. and globally. As we continue
our work in Japan, we were delighted to welcome Japan\u2019s Transport Minister Nakano and other officials to experience a fully autonomous ride in San Francisco and tour our operations center.  Waymo
is headed to Motown! Detroit is the city that put the world on wheels, and we\u2019re excited to keep those wheels turning with our fully autonomous ride-hailing service. You\u2019ll soon see us
around as we familiarize ourselves with the city\u2019s historic streets, ahead of serving riders.  Ready to experience Waymo in Detroit?   ...    We roll autonomously like"], "published_date": null,
"score": null}, {"title": "Waymo Is Quickly Expanding to More Cities. Everything to Know About the Robotaxi - CNET", "url": "https://cnet.com/roadshow/news/waymo-adds-4-new-cities-to-its-roster-
everything-to-know-about-the-robotaxi-service/", "snippet": "Waymo Is Quickly Expanding to More Cities. Everything to Know About the Robotaxi - CNET\n\nX\n\n- Cars\n- Autonomous Vehicles\n\n# Waymo Is
Quickly Expanding to More Cities. Everything to Know About the Robotaxi\n\nHere's where the self-driving company operates and where it's headed soon.\n\nAbrar Al-Heeti Senior Technology
Reporter\n\nAbrar's interests include phones, streaming, autonomous vehicles, internet trends, entertainment, pop culture and digital accessibility. In addition to her current role, she's",
"highlights": ["Waymo Is Quickly Expanding to More Cities. Everything to Know About the Robotaxi - CNET\n\nX\n\n- Cars\n- Autonomous Vehicles   ...    Abrar Al-Heeti\n\nMarch 31, 2026 10:32 p.m.
PT\n\n15 min read\n\nWaymo Self-driving cars are slowly becoming less sci-fi and more real-world as companies such as Waymo rapidly expand into   ...    Waymo, which is owned by Google's parent
Alphabet, now operates fully autonomous rides in a handful of cities across the US, with dozens more on the horizon, including in international locations. It first rolled out in areas with more   ...
expand testing to cities with harsh winters, such as Minneapolis and Detroit, as well as rainy cities like Seattle and   ...    Passengers can hail a ride either via the Waymo app or Uber (or both),
depending on the city. In November, Waymo began   ...    lighting and weather conditions, Waymo said in a blog post. The self-driving company has added several new cities to its roster in recent
months. In an Aug. 29 blog post, Waymo noted it's \"entering a new chapter and accelerating our commercial expansion.\" Below, you can find a full list of where   ...    Waymo's growth extends to its
manufacturing facilities. In May, the company said it's opening a new, 239,000-square-foot autonomous vehicle factory in the Phoenix area. The plan is to add 2,000 more fully autonomous   ...
technology into new vehicles, starting with the all-electric Zeekr RT, which Waymo has dubbed Ojai. In February 2026, Waymo said it was beginning fully autonomous operations with the sixth-generation
driver aboard the Ojai, starting with   ...    Waymo app. Testing with these vehicles began in 2025 and they'll become available \"in the years to follow.\" And in April 2025, Waymo said it reached a
preliminary agreement with Toyota to \"explore a collaboration\" geared toward   ...    Watch this: Testing Waymo's Safe Exit Feature in a Self-Driving Taxi\n\n05:29\n\n---\n\n### Phoenix Phoenix was
the first city to open up fully autonomous Waymo rides to the public in 2020. To hail a ride, download the   ...    Waymo added freeway access for passengers in Phoenix in November 2025.\n\n---\n\n###
San Francisco Bay Area   ...    In November 2024, Waymo scrapped its waitlist for Los Angeles and began welcoming all public riders via the Waymo app.   ...    the driverless ride each time.  Waymo
opened up to its first public riders in Miami in January 2026, starting with a handful of people from its waitlist. Its current service area includes the Design District, Wynwood, Brickell and Coral
Gables, with plans to expand to Miami International Airport \"soon.\" Riders can use the Waymo app to hitch a ride, if they've been granted access.  Waymo is collaborating with Moove, a   ...    ###
Dallas, Houston and San Antonio  In February 2026, Waymo expanded to Dallas, Houston and San Antonio. Riders are   ...    its operations and opens up to all members of the general public later in
2026, the company said.   ...    fleet, including vehicle cleaning and maintenance.  In March 2026, Waymo expanded its service to San Antonio   ...    ---\n\n### Orlando In February 2026, Waymo began
allowing public riders to use its service in Orlando. Like the company's debut in Dallas,   ...    scales its operations.  Riders can hail a ride using the Waymo app. ---\n\nWaymo vehicles can now
drive passengers on freeways in Phoenix, San Francisco and Los Angeles.\n\nWaymo ## Upcoming expansions\n\n---\n\n### Chicago In February 2026, Waymo shared its expansion into the Windy City. The
company is starting with manual mapping and data   ...    ### Charlotte  In addition to Chicago, Waymo in February 2026 said it's heading to Charlotte. It'll begin with manual   ...    ---\n\n###
Baltimore In December 2025, Waymo said it was beginning manual driving in Baltimore. It'll gradually work toward autonomous   ...    ### New Orleans  In November 2025, Waymo said it would begin manual
driving in New Orleans as it builds toward a   ...    ### London  In mid-October 2025, Waymo said its vehicles are headed to London, making the city its first European   ...    necessary permissions
to offer fully autonomous  Waymo is partnering with Lyft to expand to Nashville. Waymo began driving in the city autonomously in February 2026, as it prepares to open to the public later this year.
Riders will be   ...    Lyft app, too.  Waymo arrived in Denver in the fall of 2025 \"to lay the groundwork for a fully autonomous service in   ...    ### New York City  In June 2025, Waymo shared
plans to bring its autonomous tech back to New York, after having first   ...    ride-hailing service to the city in the future.\"  In February 2026, New York Governor Kathy Hochul withdrew a proposal
...    ### Philadelphia and Pittsburgh  Waymo plans to start offering rides through its Waymo app in Washington, DC, in 2026. The company returned to the nation's capital in January 2025 to test its
autonomous driving tech. In late March, it   ...    ---\n\n### Tokyo In December 2024, Waymo announced it's expanding to Tokyo, making it the company's first international"], "published_date":
"2026-04-01T05:32:34.000", "score": null}, {"title": "Partnering with Waze to help cities patch their potholes - Waymo", "url": "https://waymo.com/blog/2026/04/partnering-with-waze-to-help-cities-
patch-their-potholes/", "snippet": "Partnering with Waze to help cities patch their potholes\n\nToday, Waymo and Waze are announcing a new pilot to provide cities with sharper tools to combat a common
enemy of cyclists, pedestrians, and drivers alike: potholes.\n\nThe pilot program uses Waymo\u2019s perception and physical feedback systems to detect and provide up-to-date information on potholes
where Waymo operates. The data will be available to cities and state Departments of Transportation through the free-to-use Waze for Cities platfor", "highlights": ["Partnering with Waze to help cities
patch their potholes Today, Waymo and Waze are announcing a new pilot to provide cities with sharper tools to combat a common enemy of cyclists, pedestrians, and drivers alike: potholes. The pilot
program uses Waymo\u2019s perception and physical feedback systems to detect and provide up-to-date information on potholes where Waymo operates. The data will be available to cities and state
Departments of Transportation through the free-to-use Waze for Cities platform alongside user-reported pothole information, giving officials an additional view of surface street and highway conditions
that enables them to more efficiently and effectively fill potholes. The data will also be visible to Waze users in the cities where Waymo operates, keeping road users safe by alerting them as they
...    \u201cWaymo is already making roads safer where we operate. We want to build on the safety benefits of our service by partnering with organizations and city officials to help improve the
infrastructure we all depend on,\u201d said Arielle Fleisher, Policy Development and Research Manager at Waymo. \u201cWaymo\u2019s mission is to be the world\u2019s most trusted driver; we\u2019re
also committed to becoming a trusted partner to the cities we serve.\u201d Potholes can cause significant vehicle damage and contribute to crashes. Today, many cities rely on non-emergency 311   ...
maintenance resources equitably. This pilot program, based on feedback gathered from city officials over the years, is   ...    \u201cWe\u2019re always looking for innovative ways to deliver better
services for residents, including our own work using object detection through cameras on City vehicles,\u201d said San Jose Mayor Matt Mahan. \u201cAs Waymo\u2019s autonomous fleet travels across San
Jose, we appreciate the collaboration with Waymo and Waze as we explore how technology can help identify   ...    \u201cWaymo is showing the good neighbor principle in action: sharing data that helps
cities fix problems faster and make   ...    \u201cIt\u2019s a simple step, but it reflects a broader principle of responsibility, that companies operating on public streets can help improve
them.\u201d We\u2019ll launch this pilot in our first five cities \u2013 the San Francisco Bay Area and the Los Angeles, Phoenix, Austin, and Atlanta metro areas \u2013 where Waymo has already
identified approximately 500 potholes. Over time, we\u2019ll expand this partnership to more cities we serve, including those with winter weather and harsh freeze-thaw cycles that exacerbate the
pothole problem. \u201cFor years, drivers on Waze have helped each other by reporting potholes for a smoother, safer ride,\u201d said Andrew Stober, Strategic Partner Manager, Waze. \u201cThis pilot
program with Waymo adds another source of data to that effort, giving cities a clearer picture of road conditions through our Waze for Cities platform. It's a great example of how working together
helps our community and makes our roads better for everyone.\" Together, Waymo and Waze can help improve road quality in communities where Waymo operates. We\u2019ll seek feedback from cities using
this data on how we can further improve this pilot program, and explore bringing more actionable data to the cities we serve. If you\u2019re interested in following Waymo\u2019s journey or want to
advocate for Waymo coming to your community, sign up at https://waymo.com/updates/."], "published_date": "2026-04-09T16:07:21.000", "score": null}, {"title": "Waymo opens self-driving cars to the
public in Nashville - AOL", "url": "https://www.aol.com/articles/waymo-opens-self-driving-cars-234216723.html", "snippet": "Waymo opens self-driving cars to the public in Nashville - AOL\n\nTue, April
7, 2026 at 11:42 PM UTC\n\n0\n\nNASHVILLE, Tenn. (WKRN) \u2014 As of Tuesday, Nashville is the 11th city in the U.S. where you can hop into a rideshare without a driver. Waymo is now offering rides to
the public.\n\n\u201cWe are here to make sure we are going to have a really consistent, comfortable, and especially safe rider experience from day one,\u201d Waymo Spokesperson Mark Lewis
said.\n\nPowered entirely by sensors and 360-degree cameras", "highlights": ["Waymo opens self-driving cars to the public in Nashville - AOL\n\nTue, April 7, 2026 at 11:42 PM UTC\n\n0 NASHVILLE, Tenn.
(WKRN) \u2014 As of Tuesday, Nashville is the 11th city in the U.S. where you can hop into a rideshare without a driver. Waymo is now offering rides to the public. \u201cWe are here to make sure we
are going to have a really consistent, comfortable, and especially safe rider experience from day one,\u201d Waymo Spokesperson Mark Lewis said. Powered entirely by sensors and 360-degree cameras, the
cars spent months learning the roads and mapping a 60-square-mile service area of Davidson County. \ud83d\udce7 Have breaking news come to you: Subscribe to News 2 email alerts\u2192 \u201cFor the
last six months, we have been driving both with a person behind the wheel and also autonomously to make sure that we know the ins and outs of Nashville traffic and traffic behavior,\u201d Lewis
explained. With thousands of Nashvillians already signed up, passenger rides are rolling out in phases. \u201cWe are starting on surface streets and in the future, we will be adding freeway access,
and we are in talks with the airport also to add access,\u201d Lewis said. The cars follow the same rules of the road and are programmed to reroute to changes on the road. \u201cConstruction was not
there earlier, and it was trying to turn, and there\u2019s a car coming out so it understood, \u2018Hey, you know this isn\u2019t the greatest spot to turn, so I\u2019m going to reroute and go a
different way,'\u201d Lewis described. If something goes wrong, more than 700 first responders in Nashville are trained to handle the vehicle.   ...    Waymo said its track record in other cities
shows fewer crashes than human drivers, with 13 times fewer injury crashes, along with 13 times fewer crashes with injuries to pedestrians. \u201cEvery year, over 40,000 people die because of road
deaths, and that\u2019s really why Waymo was created: to be the world\u2019s most trusted driver, and we are living up to that commitment,\u201d Lewis said. When it comes to staging in between rides,
the company said they only park in legal spots, but if residents have concerns, they have a form on the app. \u201cIt removes itself from the traffic flow so we are not adding to congestion when we
don\u2019t need to be, and we will find   ...    community if that\u2019s not an ideal spot, you can give us feedback in our app.\u201d As far as the future of the rideshare market, a Waymo
representative told News 2 it is a developing market. \u201cThe autonomous revolution is still very new and autonomous vehicles how we integrate into communities is still a process that is
unfolding,\u201d Lewis said. \u201cBut we know that in the markets that we already serve, we are not seeing a big impact in job transitions, but we want to be a partner in doing that, and you\u2019ll
see as we set up service in new markets that we are creating jobs within our depot and technicians, maintenance, and fleet response.\u201d \u23e9 Read today\u2019s top stories on wkrn.com Inside, the
passenger can control everything from music to seat position and temperature, all designed to get you there   ...    \u201cNo matter what Waymo vehicle you get into, it is the Waymo driver, and you
always know it is going to be a consistent,   ...    Copyright 2026 Nexstar Media, Inc. All rights reserved. This material may not be published, broadcast, rewritten, or   ...    For the latest news,
weather, sports, and streaming video, head to WKRN News 2.\n\nShow comments\n\n0\n\nAdvertisement   ...    ##### 25 child stars who became true Hollywood success stories ##### Dow soars more than
1,30"], "published_date": "2026-04-07T23:42:16.000", "score": null}]
```

```json
{
  "query": "Waymo city launch 2026"
}
```

### 📋 Result

```
{"markets": [], "query": "Waymo city launch 2026"}
```

## 💭 Thinking

Now I have a very comprehensive picture. Let me summarize:

**Current Waymo cities (11 as of April 7, 2026):**
1. Phoenix
2. San Francisco Bay Area
3. Los Angeles
4. Atlanta (via Uber)
5. Austin (via Uber)
6. Miami
7. Dallas
8. Houston
9. San Antonio
10. Orlando
11. Nashville (launched April 7, 2026)

**Status of cities in the question (all in "Upcoming expansions" / "Plans to expand"):**

1. **Baltimore** - Manual driving began December 2025. Working toward autonomous operations. NOT serving riders.


2. **Boston** - Returned February 2026 for testing. NOT serving riders.
3. **Charlotte** - Announced February 2026, starting with manual mapping. NOT serving riders.
4. **Chicago** - Announced February 2026 for manual mapping, but Illinois lacks a regulatory framework. NOT serving riders.
5. **Detroit** - Announced November 2025, currently testing. NOT serving riders.
6. **Denver** - Arrived fall 2025 for groundwork, targeting launch later in the year but still operating with human drivers. NOT serving riders.
7. **Las Vegas** - Targeted for summer 2026 and still in preparation phase. NOT serving riders.
8. **New York** - Got its first permit in June 2025, but Governor Hochul withdrew a proposal in February 2026. NOT serving riders.
9. **Seattle** - Early testing with manual driving, no timeline announced. NOT serving riders.
10. **Washington DC** - Regulatory delays blocking progress; DDOT study incomplete and council approval unlikely without it. NOT serving riders.

With today being April 10, 2026 and the resolution deadline just 20 days away on May 1, none of these cities are currently serving riders. Las Vegas remains the closest to potential launch with its summer 2026 target, but that falls outside the resolution window.

Waymo's typical expansion timeline requires months of progression through testing phases before public launch, and even their fastest deployments like Nashville took roughly six months from initial testing to serving riders. While Waymo did aggressively expand to four cities simultaneously in February 2026 and launched Nashville in April, all those cities had undergone extensive preparation beforehand. There's no indication any of these ten cities are in the final pre-launch stages, and no news suggests an imminent surprise launch in the next three weeks.

The most prepared cities—Las Vegas and Denver—have publicly stated timelines extending past May 1st, while cities facing regulatory hurdles like DC, Chicago, and NYC are even further out. The March 31st CNET article explicitly categorizes all ten as "upcoming expansions" rather than active services. I'm settling on roughly 6% probability, accounting for the small chance of an unexpected acceleration in Las Vegas or Denver, the possibility of very recent developments I haven't seen, and Waymo's demonstrated ability to move faster than expected—but heavily weighted against the clear evidence that these cities remain months away from launch.

## 💬 Response

Now I have a comprehensive picture. Let me run the reflection checkpoint.
