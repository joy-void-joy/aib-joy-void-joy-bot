# Reasoning Log: Will the CPSC publish any computer-related recalls in July or August 2026?

*Generated: 2026-07-01T21:21:22.037028+00:00*


## 💭 Thinking



## 🔧 Tool: mcp__research__research


```json
{
  "query": "How frequently does the US CPSC publish computer-related recalls? Looking at the SaferProducts.gov and CPSC.gov recall history for the category \"computers\" - how many recalls per year, and are there typically gaps of 2 months with no computer recalls? List recent computer-related recalls in 2025 and 2026 with dates.",
  "ttl": "7d"
}
```

### 📋 Result

```
Invalid input: 1 validation error for ResearchInput
questions
  Field required [type=missing, input_value={'query': 'How frequently...th dates.', 'ttl': '7d'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.12/v/missing
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "How frequently does the US CPSC publish computer-related recalls? Looking at CPSC.gov and SaferProducts.gov recall history for the category 'computers' - approximately how many recalls per year, and are there typically gaps of 2 months with no computer recalls? List recent computer-related recalls in 2024, 2025 and 2026 with dates (including laptops, power supplies, monitors, batteries, chargers).",
      "ttl": "7d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "How frequently does the US CPSC publish computer-related recalls? Looking at CPSC.gov and SaferProducts.gov recall history for the category 'computers' - approximately how many
recalls per year, and are there typically gaps of 2 months with no computer recalls? List recent computer-related recalls in 2024, 2025 and 2026 with dates (including laptops, power supplies,
monitors, batteries, chargers).", "entry": {"slug": "how-frequently-does-the-us-cpsc-publish-computer-r-4abd5957", "query": "How frequently does the US CPSC publish computer-related recalls? Looking
at CPSC.gov and SaferProducts.gov recall history for the category 'computers' - approximately how many recalls per year, and are there typically gaps of 2 months with no computer recalls? List recent
computer-related recalls in 2024, 2025 and 2026 with dates (including laptops, power supplies, monitors, batteries, chargers).", "answer": "I've completed the research. Here's a summary of the key
findings:\n\n**Frequency of CPSC computer-related recalls:**\n\nThe most important finding is structural: **CPSC's literal \"Computers\" product category is essentially empty** \u2014 the
SaferProducts.gov API returns an empty array for `ProductType=Computers` from 2024 onward. Computer-related recalls are instead filed under adjacent categories (power banks, chargers, AC adapters,
batteries).\n\nThis creates two very different answers depending on definition:\n\n- **Narrow (laptops, AC adapters, PC power supplies):** Only ~1\u20133 recalls/year. **Gaps of 2+ months \u2014 even
1\u20132+ years \u2014 are completely normal.** For instance, there was a ~26-month gap between the Dynabook/Toshiba laptop-adapter recall (Feb 2024) and the Apex Gaming ATX power-supply recall (Apr
2026).\n- **Broad (adding power banks, chargers, lithium batteries):** ~15\u201325+ recalls/year \u2014 roughly one every 4\u20136 weeks in 2025. At this breadth, **2-month gaps are
rare.**\n\n**Recent recalls listed with dates (2024\u20132026)** include the flagship laptop-hardware recalls \u2014 Dynabook/Toshiba 15.5M AC adapters (2024-02-21) and Apex Gaming ATX PC power
supplies (2026-04-16, ~17,730 units) \u2014 plus a steady cadence of power-bank/charger recalls (Anker >1M units 2025-06-12, Belkin, INIU, ESR HaloLock, Casely, IKEA VARMFRONT, Baseus, HTRC chargers,
etc.).\n\n**Bottom line on the gap question:** If a monitor watches only the exact \"computers\" category, 2-month gaps are expected and routine. If it watches the broader charger/battery/power-bank
universe, recalls arrive roughly monthly. Full sourced data has been provided in the structured output.", "sources": [{"url":
"https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=power%20bank&RecallDateStart=2024-01-01&format=json", "title": "SaferProducts.gov REST Web Service \u2014 power bank recalls since
2024", "domain": "saferproducts.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Lists power-bank recalls 2024-2026 including Anker, Belkin, INIU, ESR, Casely, IKEA VARMFRONT, Baseus, etc.,
with recall dates."}, {"url": "https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=battery%20charger&RecallDateStart=2024-01-01&format=json", "title": "SaferProducts.gov REST Web Service
\u2014 battery charger recalls since 2024", "domain": "saferproducts.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "HTRC/Haisito T400 (2026-04-02), CT-ENERGY (2025-08-28), HTRC C240
(2024-12-12), Belkin smartwatch chargers (2024-12-05)."}, {"url": "https://www.saferproducts.gov/RestWebServices/Recall?RecallDateStart=2024-01-01&ProductType=Computers&format=json", "title":
"SaferProducts.gov REST Web Service \u2014 ProductType=Computers (empty result)", "domain": "saferproducts.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Returns empty array [] \u2014 no
recalls classified under 'Computers' product type since 2024-01-01."}, {"url": "https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=laptop&format=json", "title": "SaferProducts.gov REST
Web Service \u2014 laptop recall history", "domain": "saferproducts.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Historical laptop recalls: Dynabook/Toshiba AC adapters 2024-02-21, Lenovo
USB-C power banks 2023-11-22, Apple MacBook Pro 2019, Lenovo ThinkPad 2018, Sony VAIO, Toshiba, Panasonic battery packs 2016-2017."}, {"url": "https://www.cpsc.gov/Recalls/2026/Apex-Gaming-PCs-
Recalls-Manik-and-Apex-branded-ATX-Computer-Power-Supplies-Due-to-Risk-of-Serious-Injury-or-Death-from-Electrical-Shock-and-Electrocution-Hazards", "title": "Apex Gaming PCs Recalls Manik and Apex-
branded ATX Computer Power Supplies", "domain": "cpsc.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Recall Date: April 16, 2026. Units: about 17,730 (plus about 500 in Canada). Electrical
shock/electrocution; missing on-product safety label."}, {"url": "https://www.cpsc.gov/Recalls/2024/Dynabook-Americas-Recalls-15-5-Million-Toshiba-Laptop-AC-Adapters-Due-to-Burn-and-Fire-Hazards",
"title": "Dynabook Americas Recalls 15.5 Million Toshiba Laptop AC Adapters", "domain": "cpsc.gov", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Announced February 21, 2024. AC adapters bundled
with or sold separately for Toshiba-brand laptops; burn/fire hazard."}, {"url": "https://www.tomshardware.com/pc-components/power-supplies/apex-gaming-pcs-recalls-nearly-18000-power-supplies-over-
missing-safety-labels", "title": "Apex Gaming PCs recalls nearly 18,000 power supplies over missing safety labels", "domain": "tomshardware.com", "accessed_at": "2026-07-01T00:00:00Z", "snippet":
"CPSC issued recall on April 16 for approximately 17,730 Manik and Apex-branded ATX power supplies."}, {"url": "https://recalls-rappels.canada.ca/en/alert-recall/atx-computer-power-supplies-recalled-
due-electrical-hazard", "title": "ATX Computer Power Supplies recalled due to electrical hazard (Health Canada)", "domain": "canada.ca", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "Recall date
2026-04-16; Apex/Manik ATX power supplies; electrical hazard."}, {"url": "https://www.prnewswire.com/news-releases/cpsc-posts-product-recalls-and-product-safety-warnings-to-its-web-
site-302744973.html", "title": "CPSC Posts Product Recalls and Product Safety Warnings (April 16, 2026)", "domain": "prnewswire.com", "accessed_at": "2026-07-01T00:00:00Z", "snippet": "April 16, 2026
CPSC recall roundup including Casely power-bank re-announcement after a fatality."}], "key_facts": ["CPSC/SaferProducts.gov API returns an empty array for ProductType=Computers for 2024 onward \u2014
the literal 'Computers' recall category is essentially unused.", "Computer-related recalls are filed under adjacent categories: power banks/chargers (largest volume), battery chargers, AC adapters,
laptop computers (rare), computer power supplies (rare).", "Narrow computer/laptop-hardware definition: only ~1-3 recalls per year; gaps of 2+ months (often much longer) with no recall are normal.",
"Between the Feb 2024 Dynabook laptop-adapter recall and the April 2026 Apex Gaming PC power-supply recall there were no clear PC-hardware recalls \u2014 a gap over two years at the strict
definition.", "Broad computer-electronics definition (incl. power banks, chargers, batteries): ~15-25+ recalls per year; 2-month gaps are rare.", "Power-bank recalls ran roughly one every 4-6 weeks
through 2025.", "Dynabook recalled 15.5 million Toshiba laptop AC adapters on 2024-02-21 (burn/fire hazard) \u2014 the flagship 2024 laptop-hardware recall.", "Apex Gaming PCs recalled ~17,730
Manik/Apex ATX computer power supplies on 2026-04-16 (electrocution/missing safety label) \u2014 the clearest 2026 PC-hardware recall.", "Anker recalled more than 1 million power banks on 2025-06-12
(fire/burn).", "Genuine laptop-computer recalls are rare; most 'laptop' recalls concern the battery, adapter, or power bank rather than the computer."], "data_points": [{"metric": "Recalls under
literal 'Computers' product type (2024-present)", "value": 0.0, "unit": "recalls", "as_of": "2026-07-01", "source_url":
"https://www.saferproducts.gov/RestWebServices/Recall?RecallDateStart=2024-01-01&ProductType=Computers&format=json"}, {"metric": "Approx. narrow computer/laptop-hardware recalls per year", "value":
2.0, "unit": "recalls/year (range 1-3)", "as_of": "2026-07-01", "source_url": "https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=laptop&format=json"}, {"metric": "Approx. broad
computer-electronics recalls per year (power banks, chargers, batteries)", "value": 20.0, "unit": "recalls/year (range 15-25+)", "as_of": "2026-07-01", "source_url":
"https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=power%20bank&RecallDateStart=2024-01-01&format=json"}, {"metric": "Dynabook Toshiba laptop AC adapters recalled", "value": 15500000.0,
"unit": "units", "as_of": "2024-02-21", "source_url": "https://www.cpsc.gov/Recalls/2024/Dynabook-Americas-Recalls-15-5-Million-Toshiba-Laptop-AC-Adapters-Due-to-Burn-and-Fire-Hazards"}, {"metric":
"Apex Gaming ATX computer power supplies recalled (US)", "value": 17730.0, "unit": "units", "as_of": "2026-04-16", "source_url": "https://www.cpsc.gov/Recalls/2026/Apex-Gaming-PCs-Recalls-Manik-and-
Apex-branded-ATX-Computer-Power-Supplies-Due-to-Risk-of-Serious-Injury-or-Death-from-Electrical-Shock-and-Electrocution-Hazards"}, {"metric": "Anker power banks recalled (2025)", "value": 1000000.0,
"unit": "units (more than)", "as_of": "2025-06-12", "source_url": "https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=power%20bank&RecallDateStart=2024-01-01&format=json"}, {"metric":
"Gap between consecutive strict PC-hardware recalls (Dynabook Feb 2024 to Apex Apr 2026)", "value": 26.0, "unit": "months", "as_of": "2026-04-16", "source_url":
"https://www.saferproducts.gov/RestWebServices/Recall?RecallTitle=laptop&format=json"}], "created_at": "2026-07-01T21:16:32.445166Z", "updated_at": "2026-07-01T21:16:32.445166Z", "stale_after":
"2026-07-08T21:16:32.445166Z", "state": "fresh", "revision_history": [], "session_id": "48dc8371-c0bb-4526-8756-65746d5aa3ad", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 1,
"failed_count": 0}
```

## 💭 Thinking



## 💬 Response

Let me query the actual SaferProducts data to understand the frequency of recalls under the "computers" search category.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=computer&RecallDateStart=2023-01-01&format=json",
  "prompt": "List all recalls returned, with their recall dates and titles. Focus on how many computer-related recalls appear per year and the dates."
}
```

### 📋 Result

```
{"url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=computer&RecallDateStart=2023-01-01&format=json", "content": "Based on the provided content, here are the recalls
returned:\n\n## Recalls Listed\n\n1. **Recall Date: April 16, 2026**\n   - **Title:** Apex Gaming PCs Recalls Manik and Apex-branded ATX Computer Power Supplies Due to Risk of Serious Injury or Death
from Electrical Shock and Electrocution Hazards\n\n2. **Recall Date: June 22, 2023**\n   - **Title:** Poseidon Diving Systems Recalls Poseidon M28A Dive Computers Due to Injury Hazard\n\n## Computer-
Related Recalls by Year\n\n- **2023:** 1 recall (June 22, 2023 - Poseidon M28A Dive Computers)\n- **2026:** 1 recall (April 16, 2026 - Apex/Manik ATX Computer Power Supplies)\n\nNote: The search
parameters requested recalls from January 1, 2023 onward with \"computer\" in the product name. Only 2 recalls were returned, appearing in 2023 and 2026.\n\n---\n\n**Relevant links:**\n\n- [Apex
Gaming PCs Power Supply Recall Details](https://www.cpsc.gov/Recalls/2026/Apex-Gaming-PCs-Recalls-Manik-and-Apex-branded-ATX-Computer-Power-Supplies-Due-to-Risk-of-Serious-Injury-or-Death-from-
Electrical-Shock-and-Electrocution-Hazards)\n- [Apex Gaming PCs Recall Information Page](https://apexgamingpcs.com/pages/psu-recall)\n- [Canadian Recall Notice for ATX Power Supplies](https://recalls-
rappels.canada.ca/en/alert-recall/atx-computer-power-supplies-recalled-due-electrical-hazard)\n- [Poseidon Diving Systems M28A Recall Details](https://www.cpsc.gov/Recalls/2023/Poseidon-Diving-
Systems-Recalls-Poseidon-M28A-Dive-Computers-Due-to-Injury-Hazard)\n- [Poseidon M28A Support Page](https://www.poseidon.com/en-us/support/m28a/)"}
```

```json
{
  "url": "https://www.saferproducts.gov/PublicSearch",
  "prompt": "What categories are available for searching Recalls/Repairs? Is there a \"computers\" category? How does the product category search work?"
}
```

### 📋 Result

```
HTTP 403 for https://www.saferproducts.gov/PublicSearch. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series, company_financials,
world_bank_indicator).
```

## 💭 Thinking



## 💬 Response

The strict "computer" name search is very sparse (only June 2023 and April 2026). But the PublicSearch portal likely uses a broader product category. Let me investigate what the portal actually returns for "computers" and get the full frequency picture.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=laptop&RecallDateStart=2020-01-01&format=json",
  "prompt": "List all recalls with their dates and titles. How many per year?"
}
```

### 📋 Result

```
{"url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=laptop&RecallDateStart=2020-01-01&format=json", "content": "Based on the provided content, **no recall data is available**.
\n\nThe API response contains an error message: \"Error retrieving Recalls: The underlying provider failed on Open.\"\n\nThis indicates a database or service connectivity issue on the server side,
preventing any recall information from being retrieved. Therefore:\n\n- **Number of recalls**: 0 (due to error, not actual absence of recalls)\n- **Recalls per year**: Unable to determine\n\nThe query
was for laptop-related recalls from January 1, 2020 onward, but the system could not complete the request.\n\n---\n\n**Relevant links:**\nNone - the response contains only an error message with no
URLs or references to additional resources."}
```

```json
{
  "query": "saferproducts.gov PublicSearch computers category recalls how search works product category dropdown"
}
```

### 📋 Result

```
{"query": "saferproducts.gov PublicSearch computers category recalls how search works product category dropdown", "results": [{"title": "Search Home - SaferProducts", "url":
"https://www.saferproducts.gov/PublicSearch", "snippet": null, "api_data": null, "hint": null}, {"title": "Home - SaferProducts", "url": "https://www.saferproducts.gov/", "snippet": null, "api_data":
null, "hint": null}, {"title": "Recalls & Product Safety Warnings | CPSC.gov", "url": "https://www.cpsc.gov/Recalls", "snippet": null, "api_data": null, "hint": null}, {"title": "SaferProducts.gov",
"url": "https://www.datalumos.org/datalumos/project/231861/version/V1/view", "snippet": null, "api_data": null, "hint": null}, {"title": "Here is the incident description - SaferProducts", "url":
"https://www.saferproducts.gov/PublicSearch/Detail?ReportId=1890219", "snippet": null, "api_data": null, "hint": null}, {"title": "Search Result - SaferProducts", "url":
"https://www.saferproducts.gov/PublicSearch/Result", "snippet": null, "api_data": null, "hint": null}, {"title": "About SaferProducts.gov - SaferProducts", "url":
"https://www.saferproducts.gov/About", "snippet": null, "api_data": null, "hint": null}, {"title": "How To Get Information on Consumer Product Safety Recalls | Child Safe Kit", "url":
"https://www.childsafekit.com/articles/how-to-get-information-on-consumer-produt-safety-recalls.html", "snippet": "Americans buy and use hundreds of products every day. The United States Consumer
Product Safety Commission (CPSC) is tasked with helping to protect the public against the unreasonable risk of injury or death as a result of these products.\nOne way the CPSC fulfills its mission is
by issuing product safety recalls. This article will help inform you about how to get information on product safety recalls.\nFirst, let\u2019s explore what a consumer product is.\nWhat is a consumer
product?\n15 U.S. Code \u00a7 205", "api_data": null, "hint": null}, {"title": "CPSC Data | CPSC.gov", "url": "https://www.cpsc.gov/Data", "snippet": null, "api_data": null, "hint": null}, {"title":
"CPSC Posts Product Recalls to its Web Site", "url": "https://finance.yahoo.com/news/cpsc-posts-product-recalls-144100139.html", "snippet": "WASHINGTON, Oct. 23, 2025 /PRNewswire/ -- The CPSC
announces today the following recalls conducted in cooperation with the firms listed below. Recalls can be viewed at
[www.cpsc.gov](https://edge.prnewswire.com/c/link/?t=0&l=en&o=4540107-1&h=1028227646&u=http%3A%2F%2Fwww.cpsc.gov%2F&a=www.cpsc.gov).\nLifepro Fitness Recalls Bioremedy Infrared Sauna Blankets Due to
Risk of Burn Injuries (26-036)\n[Lifepro Fitness Recalls Bioremedy Infrared Sauna Blankets Due to Risk of Burn Injuries | CPSC.gov](htt", "api_data": null, "hint": null}]}
```

## 💭 Thinking



## 💬 Response

Let me query the more reliable CPSC.gov recall API which supports product-name search to establish the base rate over time.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.cpsc.gov/Recalls/CPSC-Recalls-Restful-API-Documentation",
  "prompt": "How do I query recalls by product name/category? What is the API endpoint format for searching recalls containing the word \"computer\"?"
}
```

### 📋 Result

```
HTTP 403 for https://www.cpsc.gov/Recalls/CPSC-Recalls-Restful-API-Documentation. Access denied. Try search_exa for cached content, search_news for articles, or a primary data source (fred_series,
company_financials, world_bank_indicator).
```

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=computer&format=json",
  "prompt": "List ALL recalls returned with recall dates and titles, sorted by date. I want to count how many computer recalls occurred each year and see the gaps between them."
}
```

### 📋 Result

```
{"url": "https://www.saferproducts.gov/RestWebServices/Recall?ProductName=computer&format=json", "content": "Based on the JSON data provided, here are all 100 computer-related recalls sorted by
date:\n\n## 2026\n1. **2026-04-16** - Apex Gaming PCs Recalls Manik and Apex-branded ATX Computer Power Supplies Due to Risk of Serious Injury or Death from Electrical Shock and Electrocution
Hazards\n\n## 2023\n2. **2023-06-22** - Poseidon Diving Systems Recalls Poseidon M28A Dive Computers Due to Injury Hazard\n\n## 2022\n3. **2022-07-21** - Aqualung Recalls i330R SCUBA Diving Computers
Due to Injury and Drowning Hazards\n\n## 2021\n4. **2021-02-12** - NZXT Recalls H1 Computer Cases Due to Fire Hazard\n\n## 2020\n5. **2020-09-02** - Advantus Recalls Fluorescent Computer Task Lamps
Due to Burn Hazard\n\n## 2019\n6. **2019-06-27** - Apple Recalls 15-Inch MacBook Pro Laptop Computers Due to Fire Hazard\n7. **2019-03-12** - HP Expands Recall of Batteries for Notebook Computers and
Mobile Workstations Due to Fire and Burn Hazards\n\n## 2018\n8. **2018-02-08** - Fujitsu Recalls Battery Packs for Fujitsu Notebook Computers and Workstations Due to Fire and Burn Hazards\n9.
**2018-01-04** - HP Recalls Batteries for Notebook Computers and Mobile Workstations Due to Fire and Burn Hazards\n\n## 2017\n10. **2017-02-07** - Sony Expands Recall of VAIO Laptop Computer Battery
Packs Due to Burn and Fire Hazards (Recall Alert)\n11. **2017-01-24** - HP Expands Recall of Batteries for HP and Compaq Notebook Computers Due to Fire and Burn Hazards\n12. **2017-01-04** - Toshiba
Expands Recall of Laptop Computer Battery Packs Due to Burn and Fire Hazards\n\n## 2016\n13. **2016-10-18** - TUSA Recalls Diving Computers Due to Drowning and Injury Hazards\n14. **2016-06-15** -
Sony Recalls VAIO Laptop Computer Battery Packs Due to Burn and Fire Hazards\n15. **2016-04-20** - Panasonic Recalls Lithium-ion Laptop Battery Packs Due to Fire Hazard\n16. **2016-03-30** - Toshiba
Recalls Laptop Computer Battery Packs Due to Burn and Fire Hazards\n17. **2016-02-02** - Scubapro Recalls Dive Computers\n\n## 2015\n18. **2015-09-24** - Fujitsu America Recalls Battery Packs for
Fujitsu Notebook Computers Due to Fire Hazard\n19. **2015-07-31** - NVIDIA Recalls Tablet Computers Due to Fire Hazard\n20. **2015-04-21** - Lenovo Expands Recall of Battery Packs for ThinkPad
Notebook Computers Due to Fire Hazard\n\n## 2014\n21. **2014-08-26** - Hewlett-Packard Recalls Notebook Computer AC Power Cords Due to Fire and Burn Hazards\n22. **2014-08-05** - Johnson Outdoors
Diving Recalls Dive Computers Due to Injury Hazard\n23. **2014-07-01** - Sony Recalls VAIO Flip PC Laptops Due to Fire and Burn Hazards\n24. **2014-03-27** - Lenovo Recalls Battery Packs for ThinkPad
Notebook Computers Due to Fire Hazard\n\n## 2013\n25. **2013-07-11** - Hollis Recalls Digital Dive Computers Due to Drowning Hazard\n\n## 2012\n26. **2012-09-27** - Atomic Aquatics Recalls Cobalt Dive
Computer Due to Impact and Drowning Hazard\n27. **2012-04-24** - Lenovo Expands Recall of ThinkCentre Desktop Computers Due to Fire Hazard\n28. **2012-03-08** - Lenovo Recalls ThinkCentre Desktop
Computers Due to Fire Hazard\n\n## 2011\n29. **2011-05-27** - HP Expands Recall of Notebook Computer Batteries Due to Fire Hazard\n\n## 2010\n30. **2010-09-02** - Toshiba Recalls T Series Notebook
Computers Due to Burn Hazard\n31. **2010-06-30** - Sony Recalls VAIO Laptop Computers Due to Burn Hazard\n32. **2010-05-21** - HP Expands Recall of Notebook Computer Batteries Due to Fire Hazard\n33.
**2010-04-14** - Dive Computers Recalled by Mares Due to Drowning Hazard\n34. **2010-01-07** - Acer Recalls Notebook Computers Due to Burn Hazard\n\n## 2009\n35. **2009-10-28** - Sony Recalls Computer
AC Adapters Due to Shock Hazard\n36. **2009-05-14** - HP Recalls Notebook Computer Batteries Due to Fire Hazard\n37. **2009-03-19** - Desktop Computers Recalled By Acer America Corp. Due to
Overheating, Burn Hazard\n\n## 2008\n38. **2008-10-30** - PC Notebook Computer Batteries Recalled Due to Fire and Burn Hazard\n39. **2008-10-28** - Power Adapters Used with Notebook Computers Recalled
by Battery-Biz Due To Burn Hazard\n40. **2008-09-04** - Sony Recalls Notebook Computers Due to Burn Hazard\n\n## 2007\n41. **2007-08-09** - Toshiba Recalls Notebook Computer Batteries Due to Fire
Hazard\n42. **2007-04-25** - Acer America Corporation Recalls Notebook Computer Batteries Due to Previous Fires\n43. **2007-03-01** - Lenovo Recalls ThinkPad Notebook PC Extended-Life Batteries Due to
Fire Hazard\n44. **2007-02-28** - Pelagic Recalls Digital Dive Computers Due to Decompression Hazard\n\n## 2006\n45. **2006-10-23** - Sony Recalls Notebook Computer Batteries Due to Previous
Fires\n46. **2006-09-28** - Lenovo and IBM Announce Recall of ThinkPad Notebook Computer Batteries Due to Fire Hazard\n47. **2006-08-24** - Apple Announces Recall of Batteries Used in Previous iBook
and PowerBook Computers Due to Fire Hazard\n48. **2006-07-19** - Suunto Dive Computers Recalled Due to Decompression Hazard\n49. **2006-06-22** - Oceanic Recalls Digital Dive Computer Due to
Decompression Hazard\n50. **2006-04-20** - HP Recalls Notebook Computer Batteries Due to Fire Hazard\n51. **2006-04-06** - Computer Desk Set Sold at Office Depot Recalled Due to Risk of Falls\n\n##
2005\n52. **2005-12-16** - CPSC, Dell Announce Recall of Notebook Computer Batteries\n53. **2005-10-14** - CPSC, Hewlett-Packard Company Announce Recall of Notebook Computer Batteries\n54.
**2005-06-22** - CPSC, Battery-Biz Announce Recall of Notebook Computer Batteries\n55. **2005-05-20** - CPSC, Apple Announce Recall of iBook and PowerBook Computer Batteries\n56. **2005-02-22** -
CPSC, Head USA Inc. Announce Recall of SCUBA Diving Computers\n\n## 2004\n57. **2004-12-14** - CPSC, Psion Teklogix Corp. Announce Recall of AC Power Adapters\n58. **2004-10-08** - CPSC, Dell Inc.
Announce Recall of AC Adapters for Notebook Computers\n59. **2004-08-19** - CPSC, Apple Announce Recall of PowerBook Computer Batteries\n60. **2004-07-01** - CPSC, Dell Inc. Announce Recall of Power
Adapters for Notebook Computers\n\n## 2003\n61. **2003-09-25** - CPSC, Sony Electronics Inc. Announce Recall of Certain VAIO Notebook Computers\n62. **2003-07-17** - CPSC, UWATEC Announce Recall of
Smart Dive Computers\n63. **2003-03-04** - CPSC, IBM Announce Recall to Repair Computer Monitors\n\n## 2002\n64. **2002-07-18** - CPSC, Johnson Outdoors Inc. Announce Recall of SCUBAPRO/UWATEC\u2122
Dive Computer Consoles\n\n## 2001\n65. **2001-11-28** - CPSC, KB Gear Announce Recall of Computer Mouse Sets\n66. **2001-11-13** - CPSC, Computer Distributors Announce Recall of Batteries for Notebook
Computers\n67. **2001-10-04** - CPSC, Compaq Announce Recall of Notebook Computer AC Adapters\n\n## 2000\n68. **2000-10-27** - CPSC, Compaq Announce Recall of Notebook Computer Battery Packs\n69.
**2000-10-13** - CPSC, Dell Announce Recall of Batteries for Notebook-Computers\n70. **2000-05-18** - CPSC, IBM Announce Recall of AC Adapters for Notebook Computers, Mobile Devices\n71.
**2000-01-18** - CPSC, Sauder Woodworking Announce Recall of Computer Armoires\n\n## 1997\n72. **1997-10-21** - CPSC, Dell Announce Recall of AC Adapters for Latitude LM Notebook Computers and
Latitude LM Port Replicators\n73. **1997-10-15** - CPSC, Mares America Corp. Announce Recall of Guardian Dive Computers\n74. **1997-09-03** - CPSC, Digital Equipment Corp. Announce Recall of AC
Adapters for Notebook Computers\n\n## 1996\n75. **1996-12-05** - CPSC and Compaq Computer Announce Recall of AC Adapters for Armada 4100 Notebook Computers\n76. **1996-06-07** - CPSC and Visioneer,
Inc. Announce Software and Hardware Correction Program for Computer Scanners\n77. **1996-05-30** - CPSC, Kingston Technology Announce Recall of Kingston DIMM Module for IBM ThinkPads\n78.
**1996-01-25** - CPSC, Texas Instruments Announce Battery Charger Recall For Travelmate 4000m Notebook Computers\n\n## 1995\n79. **1995-09-22** - CPSC And IBM Announce Recall Program To Repair 9527
Series Color Monitor\n80. **1995-01-20** - CPSC And IBM Announce Recall Of Thinkpad AC Adapters\n\n## 1994\n81. **1994-11-22** - NEC Technologies Inc. Recalls PC-17-01 And PC-17-02 Laptop Computer
Batteries\n82. **1994-05-20** - Dell DL-1460NI Computer Monitors Recalled Due To Fire Risk\n\n## 1990\n83. **1990-06-08** - Computer Monitors Recalled For Electrocution And Fire Hazard\n\n## 1988\n84.
**1988-03-21** - GE Recalls 45,000 Surge Suppressors\n\n## 1984\n85. **1984-05-02** - Tiger Electronics Hippo-Lot-O-Fun Musical Computer Toy May Present Hazard To Infants And Small
Children\n\n---\n\n## Yearly Count:\n- 2026: 1\n- 2023: 1\n- 2022: 1\n- 2021: 1\n- 2020: 1\n- 2019: 2\n- 2018: 2\n- 2017: 3\n- 2016: 5\n- 2015: 3\n- 2014: 4\n- 2013: 1\n- 2012: 3\n- 2011: 1\n- 2010:
5\n- 2009: 3\n- 2008: 3\n- 2007: 4\n- 2006: 7\n- 2005: 5\n- 2004: 4\n- 2003: 3\n- 2002: 1\n- 2001: 3\n- 2000: 4\n- 1997: 3\n- 1996: 4\n- 1995: 2\n- 1994: 2\n- 1990: 1\n- 1988: 1\n- 1984:
1\n\n**Notable gaps:** 1985-1987, 1989, 1991-1993, 1998-1999, 2024-2025 (no recalls in the data)\n\n**Peak years:** 2006 (7 recalls), 2010 (5 recalls), 2016 (5 recalls), 2005 (5 recalls)\n\nRelevant
links:\n- All individual recall URLs are available in the \"URL\" field of each recall entry in the JSON data, accessible at https://www.cpsc.gov/Recalls/[YEAR]/[specific-recall-path]"}
```

## 💭 Thinking



## 💬 Response

I now have comprehensive historical data. Let me compute the base rate with a Poisson model.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import numpy as np\nfrom math import exp\n\n# Recent computer recalls (ProductName contains \"computer\" on saferproducts.gov)\n# This is the same DB the PublicSearch resolves against\nrecent = {\n2020:1, 2021:1, 2022:1, 2023:1, 2024:0, 2025:0, 2026:1  # 2026 partial (Jan-Jun known: 1 in April)\n}\n# Window: Sept 2020 -> July 2026 ~ 70 months, 5 recalls\nmonths = 70\nn = 5\nrate_month = n/months\nprint(\"rate/month:\", rate_month, \"rate/year:\", rate_month*12)\n\nfor ry in [0.7, 0.85, 1.0, 1.3]:\n    lam2 = ry*(2/12)\n    print(f\"rate/yr={ry}: 2-mo P(>=1)={1-exp(-lam2):.3f}\")\n\n# Broader search interpretation (catches description mentions, ~1.5-2/yr)\nfor ry in [1.5, 2.0]:\n    lam2 = ry*(2/12)\n    print(f\"broad rate/yr={ry}: 2-mo P(>=1)={1-exp(-lam2):.3f}\")\n\n# Weighted mixture: 70% name-match (~0.85/yr), 30% broader (~1.7/yr)\np_narrow = 1-exp(-0.85*2/12)\np_broad = 1-exp(-1.7*2/12)\nmix = 0.7*p_narrow + 0.3*p_broad\nprint(\"mixture P:\", round(mix,3))\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "rate/month: 0.07142857142857142 rate/year: 0.8571428571428571\nrate/yr=0.7: 2-mo P(>=1)=0.110\nrate/yr=0.85: 2-mo P(>=1)=0.132\nrate/yr=1.0: 2-mo P(>=1)=0.154\nrate/yr=1.3:
2-mo P(>=1)=0.195\nbroad rate/yr=1.5: 2-mo P(>=1)=0.221\nbroad rate/yr=2.0: 2-mo P(>=1)=0.283\nmixture P: 0.166\n", "stderr": "", "duration_ms": 230}
```

## 💭 Thinking



## 💬 Response

The data gives a clear base rate. The saferproducts.gov "computer" search resolves against the same recall database, showing ~1 computer-related recall per year recently (2020-2023 one each, 2024-2025 zero, 2026 one in April). A Poisson mixture across narrow/broad search interpretations gives ~0.15-0.17.

## 💭 Thinking



## 💬 Response

Factor-implied is 0.22, my computed mixture ~0.16. I'll settle at 0.16, slightly above the narrow Poisson to account for search-breadth uncertainty. Let me run the premortem.
