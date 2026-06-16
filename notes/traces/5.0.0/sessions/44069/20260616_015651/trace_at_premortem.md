# Reasoning Log: Will Kyushu Electric Power Transmission and Distribution announce that the missing customer-data SSD has been recovered before June 28, 2026?

*Generated: 2026-06-16T02:04:23.752118+00:00*


## 💭 Thinking

Let me analyze this question about whether Kyushu Electric Power Transmission and Distribution will announce that a missing customer-data SSD has been recovered before June 28, 2026.

Key facts:
- SSD went missing between April 27 and May 26, 2026
- Disclosed publicly on June 8, 2026
- Theft report filed June 4, 2026
- 57 individuals from ~10 contractor firms had access
- As of mid-June 2026, SSD NOT recovered
- No data leak confirmed
- The resolution window is June 13-28, 2026, and we're currently at June 16, 2026

I need to check for any recent updates on whether the SSD has been recovered.

## 🔧 Tool: mcp__metaculus__get_metaculus_questions


```json
{
  "post_id_list": [
    44069
  ]
}
```

### 📋 Result

```
{"post_id": 44069, "title": "Will Kyushu Electric Power Transmission and Distribution announce that the missing customer-data SSD has been recovered before June 28, 2026?", "type": "binary", "url":
"https://www.metaculus.com/questions/44069", "background_info": "On June 8, 2026, Kyushu Electric Power Transmission and Distribution (\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb, \"Kyuden T&D\"), a
subsidiary of Kyushu Electric Power based in Fukuoka, Japan, publicly disclosed that a backup SSD (solid-state drive) containing personal data for up to about 10.9 million customer records had gone
missing from a server room. The data covers nearly all electricity contracts on mainland Kyushu (excluding remote islands) and includes customer names, service addresses, telephone numbers, and
electricity usage; no bank account or credit card information was on the device, which was reportedly neither encrypted nor password-protected.\n\nAccording to the company and media (NHK, Nishinippon
Shimbun), the drive was last confirmed present in its storage cabinet on April 27, 2026, and was found missing on May 26, 2026 when staff attempted a backup. The cabinet in the biometrically-secured
server room was found unlocked. The company filed a theft report with the Fukuoka Prefectural Police on June 4, 2026, which was accepted. Some 57 individuals from about 10 contractor firms had access
to the room during the roughly 30-day window. As of mid-June 2026 reporting, the SSD had NOT been recovered despite interviews with people who accessed the room and review of camera footage, and no
data leak had been confirmed.\n\n`{\"format\": \"llm_question\", \"info\": {\"rating\": {\"quality\": 3, \"ambiguity\": 3, \"resolvability\": 4, \"passes\": true}}}`", "resolution_criteria": "This
question resolves YES if, between June 13, 2026 and June 28, 2026 (inclusive), Kyushu Electric Power Transmission and Distribution publicly announces \u2014 via a press release or news/notice item on
its official website (https://www.kyuden.co.jp/td_index) \u2014 or it is reported by [credible sources](https://www.metaculus.com/faq/#definitions) that the specific missing backup SSD has been
physically located or recovered (whether found internally, returned, or seized/recovered by police). It resolves NO if no such recovery is announced or reported in that window.", "fine_print": "\"The
missing backup SSD\" refers to the single solid-state drive containing up to about 10.9 million customer records that Kyuden T&D disclosed missing on June 8, 2026. Recovery means the physical drive
itself is confirmed found, returned, or seized \u2014 an arrest, identification of a suspect, or confirmation of a data leak does NOT by itself count as recovery unless the physical drive is confirmed
recovered. Mere statements that the investigation is ongoing, or that the drive remains missing, do not count. If sources conflict on whether the drive was recovered, the question resolves based on an
official Kyuden T&D statement; absent such a statement, it resolves NO. If the official website is unavailable, equivalent reporting from credible sources governs.", "num_forecasters": 0,
"community_prediction": null}
```

## 🔧 Tool: mcp__research__research


```json
{
  "questions": [
    {
      "query": "Kyushu Electric Power Transmission Distribution missing SSD customer data recovery status June 2026 \u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD \u7d1b\u5931",
      "ttl": "6h"
    },
    {
      "query": "Base rate for recovery of stolen data storage devices corporate theft cases Japan",
      "ttl": "7d"
    }
  ]
}
```

### 📋 Result

```
{"results": [{"query": "Kyushu Electric Power Transmission Distribution missing SSD customer data recovery status June 2026 \u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD \u7d1b\u5931", "entry":
{"slug": "kyushu-electric-power-transmission-distribution-mi-522fe8fd", "query": "Kyushu Electric Power Transmission Distribution missing SSD customer data recovery status June 2026
\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD \u7d1b\u5931", "answer": "This research yielded comprehensive results. Here is my full synthesis:\n\n---\n\n# Kyushu Electric Power Transmission &
Distribution \u2014 SSD Customer Data Loss Incident (June 2026)\n\n## Incident Overview\n\nOn **June 8, 2026**, Kyushu Electric Power Transmission and Distribution
(\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u682a\u5f0f\u4f1a\u793e) publicly announced that a portable external SSD containing massive amounts of customer data had gone missing from a server room.
The incident is one of the largest personal data exposure risks in Japan's utility sector.\n\n## Timeline of Events\n\n| Date | Event |\n|------|-------|\n| **April 27, 2026** | A contractor's
employee completed a backup operation and placed the SSD in an **unlocked cabinet** inside a secure server room. |\n| **May 26, 2026** | The SSD was discovered missing when the next scheduled backup
was to be prepared \u2014 a **~30-day detection gap**. |\n| **June 4, 2026** | A **theft report (\u88ab\u5bb3\u5c4a)** was filed with and accepted by the **Fukuoka Prefectural Police**. |\n| **June 8,
2026** | Public announcement via press conference and press release. METI issued a formal order under the Electricity Business Act. |\n\n## Scale of Affected Data\n\n- **Up to 10.9 million customer
accounts (\u7d041,090\u4e07\u53e3)** \u2014 covering virtually all electricity customers across the Kyushu mainland (excluding remote islands).\n- Data spanned contracts from **July 2016 through April
2026** (nearly a decade).\n- Includes customers of both Kyushu Electric Power and other retail electricity providers in the Kyushu service area.\n\n## Data Categories on the SSD\n\n- Customer names
(\u9700\u8981\u8005\u540d)\n- Supply location addresses (\u4f9b\u7d66\u5834\u6240\u4f4f\u6240)\n- Electricity usage data (\u4f7f\u7528\u96fb\u529b\u91cf\u30c7\u30fc\u30bf)\n- Phone numbers
(\u96fb\u8a71\u756a\u53f7)\n- Retail electricity provider names (\u5c0f\u58f2\u96fb\u6c17\u4e8b\u696d\u8005\u540d)\n\n**Not included:** Bank account numbers, credit card information, or customer
ages.\n\n**Critically, the SSD had NO encryption and NO password protection.**\n\n## Security Failures Identified\n\n1. **No encryption** \u2014 The SSD was completely unencrypted, violating industry
best practices.\n2. **No password protection** \u2014 No access credential was set.\n3. **Unlocked storage** \u2014 The cabinet within the server room was not locked.\n4. **One-month detection gap**
\u2014 No asset tracking or periodic inventory system existed.\n5. **Contractor management gaps** \u2014 Insufficient tracking of media handled by contractor personnel.\n\n## Recovery Status (as of
mid-June 2026)\n\n- **The SSD has NOT been recovered.**\n- **No confirmed data leak or misuse** has been detected so far.\n- Investigation is **ongoing** \u2014 both internal and via Fukuoka
Prefectural Police.\n- The company committed to **individually notifying all affected customers**.\n- Recurrence prevention measures are **under development** but specifics have not yet been publicly
announced.\n\n## Government & Regulatory Response\n\n- **METI (\u7d4c\u6e08\u7523\u696d\u7701)** issued an order on June 8, 2026 under **Article 106, Paragraph 3 of the Electricity Business Act**,
requiring the company to report facts, identify root causes, and submit recurrence prevention measures.\n- The **Personal Information Protection Commission
(\u500b\u4eba\u60c5\u5831\u4fdd\u8b77\u59d4\u54e1\u4f1a)** was notified.\n\n## Official Statements\n\n- **Vice President Katsumi Inatsuki (\u7a32\u6708\u52dd\u5df3)** led a press conference on June 8,
2026 in Fukuoka, apologizing and pledging preventive measures.\n- Official statement: *\"We deeply apologize for causing great concern and inconvenience to our customers.\"*\n\n## Key Sources\n\n-
Kyushu Electric Power T&D official press release (June 8, 2026)\n- Sankei Shimbun, Yomiuri Shimbun, Mainichi Shimbun (June 8, 2026)\n- METI press release on regulatory order (June 8, 2026)\n- Nikkei
xTECH security analysis\n- FBS Fukuoka Broadcasting\n\n---", "sources": [{"url": "https://www.kyuden.co.jp/td/press/2026/260608.html", "title": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb
SSD\u7d1b\u5931\u306b\u95a2\u3059\u308b\u30d7\u30ec\u30b9\u30ea\u30ea\u30fc\u30b9", "domain": "kyuden.co.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Official press release from Kyushu
Electric Power Transmission & Distribution regarding the SSD data loss incident announced June 8, 2026."}, {"url": "https://www.sankei.com/article/20260608-GVATPTIH7NOW3BWGGQVKL4MQ6A/", "title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD\u7d1b\u5931 1090\u4e07\u53e3\u306e\u9867\u5ba2\u30c7\u30fc\u30bf", "domain": "sankei.com", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Sankei
Shimbun report on the SSD loss affecting up to 10.9 million customer accounts."}, {"url": "https://www.yomiuri.co.jp/national/20260608-GYT1T00316/", "title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb \u5916\u4ed8\u3051SSD\u7d1b\u5931\u5831\u9053", "domain": "yomiuri.co.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Yomiuri Shimbun report
covering the incident details and press conference."}, {"url": "https://www.meti.go.jp/press/2026/06/20260608001/20260608001.html", "title": "\u7d4c\u6e08\u7523\u696d\u7701
\u96fb\u6c17\u4e8b\u696d\u6cd5\u306b\u57fa\u3065\u304f\u5831\u544a\u5fb4\u53ce\u547d\u4ee4", "domain": "meti.go.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "METI order under Article 106
Paragraph 3 of Electricity Business Act requiring Kyushu Electric Power T&D to report and submit prevention measures."}, {"url": "https://xtech.nikkei.com/atcl/nxt/news/24/03260/", "title": "Nikkei
xTECH \u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u5206\u6790", "domain": "xtech.nikkei.com", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Nikkei xTECH analysis of the security failures in the Kyushu
Electric Power T&D SSD incident."}, {"url": "https://mainichi.jp/articles/20260608/k00/00m/020/280000c", "title": "\u6bce\u65e5\u65b0\u805e
\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fbSSD\u7d1b\u5931\u5831\u9053", "domain": "mainichi.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Mainichi Shimbun coverage of the incident and
regulatory response."}, {"url": "https://innovatopia.jp/cyber-security/cyber-security-news/107789/", "title": "Innovatopia \u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u5206\u6790
\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fbSSD\u7d1b\u5931", "domain": "innovatopia.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Security analysis noting the lack of encryption, password
protection, and asset tracking as critical failures."}], "key_facts": ["On June 8, 2026, Kyushu Electric Power Transmission & Distribution (\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb) announced a
portable external SSD containing customer data had gone missing from a server room.", "The SSD contained data on up to 10.9 million customer accounts (\u7d041,090\u4e07\u53e3), covering virtually all
electricity customers across the Kyushu mainland from July 2016 through April 2026.", "Data on the SSD included: customer names, supply location addresses, electricity usage data, phone numbers, and
retail electricity provider names. No bank or credit card data was included.", "The SSD had NO encryption and NO password protection.", "A contractor's employee completed a backup on April 27, 2026
and placed the SSD in an unlocked cabinet. The loss was not discovered until May 26, 2026 \u2014 a ~30-day detection gap.", "A theft report (\u88ab\u5bb3\u5c4a) was filed with Fukuoka Prefectural
Police on June 4, 2026.", "METI issued a formal order under Article 106, Paragraph 3 of the Electricity Business Act on June 8, 2026, requiring root cause analysis and recurrence prevention
measures.", "As of mid-June 2026, the SSD has NOT been recovered, but no confirmed data leak or misuse has been detected.", "The company pledged to individually notify all affected customers and
develop recurrence prevention measures.", "Vice President Katsumi Inatsuki (\u7a32\u6708\u52dd\u5df3) led a press conference on June 8, 2026 in Fukuoka apologizing for the incident."], "data_points":
[{"metric": "Customer accounts affected", "value": 10900000.0, "unit": "accounts", "as_of": "2026-06-08", "source_url": "https://www.kyuden.co.jp/td/press/2026/260608.html"}, {"metric": "Data time
span (years)", "value": 9.8, "unit": "years (July 2016 - April 2026)", "as_of": "2026-06-08", "source_url": "https://www.sankei.com/article/20260608-GVATPTIH7NOW3BWGGQVKL4MQ6A/"}, {"metric": "Days
between SSD loss and discovery", "value": 29.0, "unit": "days (April 27 to May 26, 2026)", "as_of": "2026-05-26", "source_url": "https://www.kyuden.co.jp/td/press/2026/260608.html"}, {"metric": "Days
between discovery and public announcement", "value": 13.0, "unit": "days (May 26 to June 8, 2026)", "as_of": "2026-06-08", "source_url": "https://www.kyuden.co.jp/td/press/2026/260608.html"},
{"metric": "SSD recovered", "value": 0.0, "unit": "boolean (0=No, 1=Yes)", "as_of": "2026-06-16", "source_url": "https://www.kyuden.co.jp/td/press/2026/260608.html"}, {"metric": "Confirmed data leaks
or misuse detected", "value": 0.0, "unit": "incidents", "as_of": "2026-06-16", "source_url": "https://www.kyuden.co.jp/td/press/2026/260608.html"}], "created_at": "2026-06-16T02:02:09.852155Z",
"updated_at": "2026-06-16T02:02:09.852155Z", "stale_after": "2026-06-16T08:02:09.852155Z", "state": "fresh", "revision_history": [], "session_id": "523202ab-aa0d-41b7-926b-87a128c9c88f",
"follow_up_count": 0}, "is_follow_up": false}, {"query": "Base rate for recovery of stolen data storage devices corporate theft cases Japan", "entry": {"slug": "base-rate-for-recovery-of-stolen-data-
storage-devi-15f20ad0", "query": "Base rate for recovery of stolen data storage devices corporate theft cases Japan", "answer": "The research synthesis is complete. Note that web search and fetch
tools were unavailable during this session, so the findings are based on my existing knowledge of Japanese crime statistics, JNSA data breach surveys, and notable incidents. The key takeaway is that
**no single authoritative base rate exists** for this specific metric, but a reasonable constructed estimate is **approximately 25\u201340% overall device recovery**, with significant variation by
whether the theft is insider vs. external and whether it's reported to police.", "sources": [{"url": "https://www.npa.go.jp/publications/statistics/sousa/statistics.html", "title": "NPA Crime
Statistics \u2014 Annual Report on Crime Clearance Rates", "domain": "npa.go.jp", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Japan National Police Agency publishes annual property crime
clearance rates; overall theft clearance approximately 37% as of 2022 report"}, {"url": "https://www.jnsa.org/result/incident/", "title": "JNSA Information Security Incident Survey Reports", "domain":
"jnsa.org", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "JNSA annual surveys categorize data breach incidents by cause including theft, loss, unauthorized access; theft accounts for 2-5% of
incidents"}, {"url": "https://www.ppc.go.jp/en/", "title": "Personal Information Protection Commission \u2014 APPI Enforcement", "domain": "ppc.go.jp", "accessed_at": "2026-06-16T00:00:00Z",
"snippet": "2022 APPI revision mandates breach notification for incidents involving theft of personal data, increasing reported incident volumes"}, {"url": "https://www.security-next.com/", "title":
"Security NEXT \u2014 Japanese Information Security News (Kanagawa HDD Incident Coverage)", "domain": "security-next.com", "accessed_at": "2026-06-16T00:00:00Z", "snippet": "Coverage of 2019 Kanagawa
Prefecture HDD theft incident; Broadlink contractor stole 18 HDDs, approximately 9 recovered after arrest"}], "key_facts": ["No single authoritative Japanese source publishes a specific 'device
recovery rate' for corporate data storage theft \u2014 estimates must be constructed from adjacent data", "Japan's National Police Agency (NPA) reports overall property crime clearance rates of
approximately 37% (2022 data), which serves as a broad proxy", "JNSA incident surveys show theft (as distinct from loss) accounts for roughly 2-5% of reported personal data breach incidents in Japan",
"Insider corporate theft cases have higher perpetrator identification rates (estimated 60-80%) due to access logs and CCTV, but physical device recovery is lower (estimated 40-60%)", "External theft
(break-ins, supply chain) device recovery rates are estimated at 10-25%, consistent with small electronics stolen property recovery", "The 2019 Kanagawa Prefecture HDD incident (Broadlink contractor)
resulted in approximately 9 of 18 stolen drives being recovered (~50%), even after the perpetrator was arrested", "The 2014 Benesse breach (35 million records exfiltrated by insider) demonstrated that
perpetrator arrest does not guarantee data containment", "Japan's 2022 APPI revision mandates breach notification, increasing disclosure of incidents but not necessarily improving recovery rates",
"Many corporate data thefts in Japan are handled internally without police reporting, creating significant reporting and survivorship bias in official statistics", "Overall weighted estimate for
device recovery in Japanese corporate theft cases: approximately 25-40%"], "data_points": [{"metric": "Japan overall property crime clearance rate (NPA)", "value": 37.0, "unit": "percent", "as_of":
"2022-12-31", "source_url": "https://www.npa.go.jp/publications/statistics/sousa/statistics.html"}, {"metric": "Theft as share of reported data breach incidents in Japan (JNSA)", "value": 3.5, "unit":
"percent (midpoint of 2-5% range)", "as_of": "2020-12-31", "source_url": "https://www.jnsa.org/result/incident/"}, {"metric": "Kanagawa HDD incident device recovery rate", "value": 50.0, "unit":
"percent (9 of 18 drives)", "as_of": "2019-12-31", "source_url": "https://www.security-next.com/"}, {"metric": "Estimated insider theft device recovery rate (reported to police)", "value": 50.0,
"unit": "percent (midpoint of 40-60% range)", "as_of": "2024-12-31", "source_url": "https://www.npa.go.jp/publications/statistics/sousa/statistics.html"}, {"metric": "Estimated external theft device
recovery rate", "value": 17.5, "unit": "percent (midpoint of 10-25% range)", "as_of": "2024-12-31", "source_url": "https://www.npa.go.jp/publications/statistics/sousa/statistics.html"}, {"metric":
"Estimated overall weighted device recovery rate (corporate theft Japan)", "value": 32.5, "unit": "percent (midpoint of 25-40% range)", "as_of": "2024-12-31", "source_url":
"https://www.npa.go.jp/publications/statistics/sousa/statistics.html"}, {"metric": "Benesse breach affected records (insider data theft)", "value": 35000000.0, "unit": "customer records", "as_of":
"2014-07-01", "source_url": "https://www.security-next.com/"}], "created_at": "2026-06-16T01:58:33.678939Z", "updated_at": "2026-06-16T01:58:33.678939Z", "stale_after": "2026-06-23T01:58:33.678939Z",
"state": "fresh", "revision_history": [], "session_id": "6e833123-7e7c-4524-a7ae-5fe5145327a1", "follow_up_count": 0}, "is_follow_up": false}], "successful_count": 2, "failed_count": 0}
```

## 💬 Response

Now let me check for any very recent updates and search for similar precedents with timelines:

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD \u7d1b\u5931 \u56de\u53ce 2026\u5e746\u6708"
}
```

### 📋 Result

```
{"query": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb SSD \u7d1b\u5931 \u56de\u53ce 2026\u5e746\u6708", "results": [{"title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u30011090\u4e07\u53e3\u5206\u306e\u9867\u5ba2\u60c5\u5831\u5165\u308aSSD\u7d1b\u5931 \u60c5\u5831\u6f0f\u6d29\u306e\u304a\u305d\u308c |
\u74b0\u5883\u30d3\u30b8\u30cd\u30b9\u30aa\u30f3\u30e9\u30a4\u30f3", "url": "https://www.kankyo-business.jp/news/4ad7fc1a-8a27-470b-abcd-79e764684fb8", "snippet":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u30011090\u4e07\u53e3\u5206\u306e\u9867\u5ba2\u60c5\u5831\u5165\u308aSSD\u7d1b\u5931
\u60c5\u5831\u6f0f\u6d29\u306e\u304a\u305d\u308c\n![\u74b0\u5883\u30d3\u30b8\u30cd\u30b9\u7de8\u96c6\u90e8](https://www.kankyo-business.jp/uploads/2025/09/26/Od2wNMPMjS9TiNqJu7lIUBa1zhGBqVpliqqChpeJ.p
ng)\n\u74b0\u5883\u30d3\u30b8\u30cd\u30b9\u7de8\u96c6\u90e8\n\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\uff08\u798f\u5ca1\u770c\u798f\u5ca1\u5e02\uff09\u306f6\u67088\u65e5\u3001\u4e00\u90e8\u30b7\u30b
9\u30c6\u30e0\u306e\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u306b\u4f7f\u7528\u3057\u3066\u3044\u305f\u5916\u90e8\u8a18\u61b6\u5a92\u4f53\uff08SSD\uff09\u304c\u6240\u5728\u4e0d\u660e\u306b\u306a\u3063\u30
5f\u3068\u767a\u8868\u3057\u305f\u3002\u540c\u5a92\u4f53\u306b\u306f\u6700\u59271090\u4e07\u53e3\u5206\u306e\u9867\u5ba2\u60c5\u5831\u304c\u4fdd\u5b58\u3055\u308c\u3066\u304a\u308a\u3001\u793e\u5916\u
3078\u6f0f\u6d29\u3057\u305f\u304a\u305d\u308c\u304c\u3042\u308b\u3068\u3044\u3046\u3002\u73fe\u6642\u70b9\u3067\u60c5\u5831\u6d41\u51fa\u306e\u4e8b\u5b9f\u306f\u78ba\u8a8d\u3055\u308c\u3066\u3044\u30
6a\u3044\u3068\u3057\u3066\u3044\u308b\u3002\n\u9700\u8981\u8005\u540d\u3084\u4f7f\u7528\u96fb\u529b\u91cf\u30c7\u30fc\u30bf\u306a\u3069\u3092\u4fdd\u5b58\n\u3053\u3061\u3089\u306fKAIGI
ID\u30e6\u30fc\u30b6\u30fc\u9650\u5b9a\u306e\u8a18\u4e8b\u3067\u3059\u3002\n-
\u74b0\u5883\u5bfe\u7b56\u30fb\u74b0\u5883\u63a8\u9032\u306b\u5f79\u7acb\u3064\u30cb\u30e5\u30fc\u30b9\u8a18\u4e8b\u304c\u8aad\u3081\u308b\uff01\uff08\u5e74\u95931500\u672c\u4ee5\u4e0a\uff09\n-
\u5e73\u65e5\u6bce\u671d\u3001\u81ea\u5206\u306e\u8208\u5473\u306b\u5408\u3063\u305f\u6700\u65b0\u30cb\u30e5\u30fc\u30b9\u3092\u30e1\u30fc\u30eb\u3067\u53d7\u3051\u53d6\u308c\u308b\n- \u69d8\u3005\u30
6a\u30b5\u30fc\u30d3\u30b9\u306b\u4f7f\u3048\u308b\u30dd\u30a4\u30f3\u30c8\u3092\u8caf\u3081\u3089\u308c\u308b\n\u6ce8\u76ee\u60c5\u5831\uff08PR\uff09\n\u3053\u306e\u8a18\u4e8b\u306b\u30ea\u30a2\u30af
\u30b7\u30e7\u30f3\u3057\u30661\u30dd\u30a4\u30f3\u30c8\uff01\n\uff08\u203b[KAIGI ID\u767b\u9332](https://www.kankyo-bus", "api_data": null, "hint": null}, {"title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb 1090\u4e07\u4ef6\u306e\u500b\u4eba\u60c5\u5831\u3092\u7d1b\u5931 \u4fdd\u7ba1\u5834\u6240\u306bSSD\u304c\u306a\u304f\u767a\u899a
(2026\u5e746\u67088\u65e5\u63b2\u8f09) - \u30e9\u30a4\u30d6\u30c9\u30a2\u30cb\u30e5\u30fc\u30b9", "url": "https://news.livedoor.com/topics/detail/31492276/", "snippet": null, "api_data": null, "hint":
null}, {"title": "\u4e5d\u96fb\u9001\u914d\u96fb \u9867\u5ba21,090\u4e07\u4ef6\u306eSSD\u7d1b\u5931 \u2014
\u300c\u7121\u65bd\u9320\u30fb\u6697\u53f7\u5316\u306a\u3057\u300d\u306f\u3069\u306e\u6bb5\u968e\u3067\u6b62\u3081\u3089\u308c\u305f\u304b\uff5czephel01", "url":
"https://note.com/zephel01/n/n680ed674ed0f", "snippet": "![\u898b\u51fa\u3057\u753b\u50cf](https://assets.st-
note.com/production/uploads/images/283723263/rectangle_large_type_2_02f4bf20f6f7427a21103b78328007de.png?width=1280)\n\u4e5d\u96fb\u9001\u914d\u96fb \u9867\u5ba21,090\u4e07\u4ef6\u306eSSD\u7d1b\u5931
\u2014 \u300c\u7121\u65bd\u9320\u30fb\u6697\u53f7\u5316\u306a\u3057\u300d\u306f\u3069\u306e\u6bb5\u968e\u3067\u6b62\u3081\u3089\u308c\u305f\u304b\n\u3053\u3093\u306b\u3061\u306f\u3001\u304f\u30fc\u308
b\u305c\u308d\u3067\u3059\u3002\n\u4e5d\u5dde\u96fb\u529b\u306e\u5b50\u4f1a\u793e\u30fb\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u304c\u3001\u6700\u5927\u5ef6\u30791,090\u4e07\u4ef6\uff08\u96e2\u5cf6
\u3092\u9664\u304f\u4e5d\u5dde\u672c\u571f\u306e\u307b\u307c\u5168\u9867\u5ba2\uff09\u306e\u500b\u4eba\u60c5\u5831\u3092\u4fdd\u5b58\u3057\u305fSSD 1\u53f0\u3092\u7d1b\u5931\u3057\u305f\u3068\u3001202
6\u5e746\u67088\u65e5\u306b\u767a\u8868\u3057\u307e\u3057\u305f\u3002\u30b5\u30fc\u30d0\u30fc\u5ba4\u304b\u3089\u306e\u7121\u65ad\u6301\u3061\u51fa\u3057\u306e\u53ef\u80fd\u6027\u3082\u542b\u3081\u306
6\u8abf\u67fb\u4e2d\u3068\u3057\u3066\u3044\u307e\u3059\u3002\n\u666e\u6bb5\u306f\u30ed\u30fc\u30ab\u30ebLLM\u3084\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u306e\u691c\u8a3c\u8a18\u4e8b\u3092\u66f8\u3044\u
3066\u3044\u307e\u3059\u304c\u3001\u4eca\u56de\u306f\u300c\u7d44\u7e54\u306e\u30c7\u30fc\u30bf\u7ba1\u7406\u306f\u4f55\u91cd\u306b\u30c1\u30a7\u30c3\u30af\u304c\u3042\u308c\u3070\u4e8b\u6545\u3092\u96
32\u3052\u305f\u306e\u304b\u300d\u3068\u3044\u3046\u89b3\u70b9\u3067\u6574\u7406\u3057\u307e\u3059\u3002\u72af\u4eba\u63a2\u3057\u3067\u306f\u306a\u304f\u3001\u3069\u306e\u9632\u58c1\u304c1\u679a\u306
7\u3082\u3042\u308c\u3070\u88ab\u5bb3\u898f\u6a21\u304c\u5909\u308f\u3063\u305f\u304b\u304c\u672c\u984c\u3067\u3059\u3002\n\u4f55\u304c\u8d77\u304d\u305f\u304b\n\u7d4c\u7def: 2026\u5e744\u670827\u65e5
\u3001\u30b7\u30b9\u30c6\u30e0\u306e\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u6642\u306b\u30b5\u30fc\u30d0\u30fc\u5bb9\u91cf\u304c\u903c\u8feb\u3057\u3001\u4e00\u6642\u7684\u306a\u5916\u90e8\u4fdd\u7ba1\u
5148\u3068\u3057\u3066\u6301\u3061", "api_data": null, "hint": null}, {"title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u3001\u6700\u59271090\u4e07\u4ef6\u306e\u9867\u5ba2\u60c5\u5831\u6f0f\u6d29\u304b \u30c7\u30fc\u30bf\u3092\u4fdd\u5b58\u3057\u305fSSD\u7d1b\u5931", "url":
"https://xtech.nikkei.com/atcl/nxt/news/24/03260/", "snippet": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u306f2026\u5e746\u67088\u65e5\u3001\u6700\u59271090\u4e07\u4ef6\u306e\u9867\u5ba2\u60c5\u5831
\u3092\u4fdd\u5b58\u3057\u305fSSD\uff08\u30bd\u30ea\u30c3\u30c9\u30fb\u30b9\u30c6\u30fc\u30c8\u30fb\u30c9\u30e9\u30a4\u30d6\uff09\u304c\u6240\u5728\u4e0d\u660e\u306b\u306a\u3063\u305f\u3068\u767a\u886
8\u3057\u305f\u3002\u7d1b\u5931\u3057\u305fSSD\u306b\u306f\u6c0f\u540d\u3084\u4f4f\u6240\u3001\u4f7f\u7528\u96fb\u529b\u91cf\u30c7\u30fc\u30bf\u3001\u96fb\u8a71\u756a\u53f7\u306a\u3069\u3092\u4fdd\u5b
58\u3057\u3066\u3044\u305f\u3002\u3053\u308c\u3089\u306e\u9867\u5ba2\u60c5\u5831\u304c\u6f0f\u6d29\u3057\u305f\u53ef\u80fd\u6027\u304c\u3042\u308b\u3002\u9280\u884c\u53e3\u5ea7\u3084\u30af\u30ec\u30b8
\u30c3\u30c8\u30ab\u30fc\u30c9\u306e\u60c5\u5831\u306f\u542b\u307e\u308c\u3066\u3044\u306a\u3044\u3068\u3044\u3046\u3002\n\u540c\u793e\u306f\u30b5\u30fc\u30d0\u30fc\u5185\u306e\u30c7\u30fc\u30bf\u5bb9
\u91cf\u3092\u7ba1\u7406\u3059\u308b\u305f\u3081\u3001\u6708\u306b1\u5ea6USB\u63a5\u7d9a\u306eSSD\u306b\u30c7\u30fc\u30bf\u3092\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u3057\u3066\u3044\u308b\u3002\u540c\
u5e745\u670826\u65e5\u306b\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u3092\u6e96\u5099\u3092\u3057\u305f\u969b\u306bSSD\u306e\u7d1b\u5931\u304c\u5224\u660e\u3057\u305f\u30024\u670827\u65e5\u306e\u30d0\u30c3
\u30af\u30a2\u30c3\u30d7\u5b8c\u4e86\u6642\u306b\u306fSSD\u3092\u4fdd\u7ba1\u3057\u305f\u3053\u3068\u3092\u78ba\u8a8d\u3057\u3066\u3044\u305f\u3002SSD\u306f\u30b5\u30fc\u30d0\u30fc\u5ba4\u5185\u306e\u
30ad\u30e3\u30d3\u30cd\u30c3\u30c8\u306b\u4fdd\u7ba1\u3057\u3066\u3044\u305f\u304c\u3001\u65bd\u9320\u306f\u3057\u3066\u3044\u306a\u304b\u3063\u305f\u3002\n\u30b5\u30fc\u30d0\u30fc\u5ba4\u3078\u306e\u
5165\u9000\u5834\u306b\u306f\u30ab\u30fc\u30c9\u306b\u3088\u308b\u8a8d\u8a3c\u3084\u751f\u4f53\u8a8d\u8a3c\u306a\u3069\u3067\u500b\u4eba\u3092\u7279\u5b9a\u3067\u304d\u308b\u3088\u3046\u306b\u3057\u30
66\u3044\u305f\u30024\u670827\u65e5\u304b\u30895\u670826\u65e5\u307e\u3067\u306e\u5165\u9000\u5ba4\u8005\u3078\u306e\u30d2\u30a2\u30ea\u30f3\u30b0\u3084\u73fe\u5730\u8abf\u67fb\u3092\u5b9f\u65bd\u3057
\u305f\u304c\u3001SSD\u306f\u767a\u898b\u3067\u304d\u305a\u3001\u539f\u56e0\u3082\u7279\u5b9a\u3067\u304d\u3066\u3044\u306a\u3044\u3068\u3044\u3046\u3002\n[\u3053\u306e\u8a18\u4e8b\u306e\u76ee\u6b21\u
3078\u623b\u308b](https://xtech.nikkei.com/news/?i_cid=nbpnxt_backindex_child)", "api_data": null, "hint": null}, {"title": "\u4e5d\u96fb\u9001\u914d\u96fb
\u9867\u5ba2\u60c5\u5831\u5165\u308aSSD\u7d1b\u5931 - Yahoo!\u30cb\u30e5\u30fc\u30b9", "url": "https://news.yahoo.co.jp/pickup/6583471", "snippet": null, "api_data": null, "hint": null}, {"title":
"\u9867\u5ba2\u60c5\u5831\u5165\u308aSSD\u3092\u7d1b\u5931 \u4e5d\u96fb\u9001\u914d\u96fb\u30011090\u4e07\u4ef6\u5206\uff08\u5171\u540c\u901a\u4fe1\uff09 - Yahoo!\u30cb\u30e5\u30fc\u30b9", "url":
"https://news.yahoo.co.jp/articles/faf603b319816385c52b069994c7a0175c4161d5", "snippet": null, "api_data": null, "hint": null}, {"title": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb
1000\u4e07\u4ef6\u8d85\u306e\u500b\u4eba\u60c5\u5831\u4fdd\u5b58\u3057\u305f\u8a18\u9332\u5a92\u4f53(SSD)\u3092\u7d1b\u5931 [\u5c11\u8003\u3055\u3093\u2605]", "url":
"https://asahi.5ch.io/test/read.cgi/newsplus/1780916732/l50", "snippet": null, "api_data": null, "hint": null}, {"title": "kouseikyoku.mhlw.go.jp", "url":
"https://kouseikyoku.mhlw.go.jp/kyushu/chotatsu/nyusatsu/index.html", "snippet": "2026\u5e746\u67083\u65e5\n\u5165\u672d\u516c\u544a\uff08\u4e00\u822c\u7af6\u4e89\uff09\n[\u696d\u52d9\u7528\u30cf\u30a
4\u30d6\u30ea\u30c3\u30c9\u81ea\u52d5\u8eca\uff08SUV\u30bf\u30a4\u30d7\uff09\u306e\u4ea4\u63db\u8cfc\u5165\uff3b172KB\uff3d](https://kouseikyoku.mhlw.go.jp/kyushu/000485963.pdf)\uff08\u4ee4\u548c8\u5e
746\u67083\u65e5\u516c\u544a\uff09\n[\u5fc3\u795e\u55aa\u5931\u8005\u7b49\u533b\u7642\u89b3\u5bdf\u6cd5\u306b\u57fa\u3065\u304f\u79fb\u9001\u88dc\u52a9\u696d\u52d9\uff3b168KB\uff3d](https://kouseikyok
u.mhlw.go.jp/kyushu/R080224_nyuusatukoukoku.pdf)\uff08\u4ee4\u548c8\u5e742\u670824\u65e5\u516c\u544a\uff09\uff08\u7d42\u4e86\u3057\u307e\u3057\u305f\uff09\n[\u30b3\u30d4\u30fc\u7528\u7d19\u8cfc\u5165\
uff08\u5358\u4fa1\u5951\u7d04\uff09\uff3b155KB\uff3d](https://kouseikyoku.mhlw.go.jp/kyushu/R080212_nyuusatukoukoku.pdf.pdf)\uff08\u4ee4\u548c8\u5e742\u670812\u65e5\u516c\u544a\uff09\uff08\u7d42\u4e86
\u3057\u307e\u3057\u305f\uff09\n[\u30d5\u30fc\u30ea\u30a8\u5909\u63db\u8d64\u5916\u5206\u5149\u5149\u5ea6\u8a08\u4e00\u5f0f\u8cc3\u8cb8\u501f\uff3b170KB\uff3d](https://kouseikyoku.mhlw.go.jp/kyushu/00
0420174.pdf)\uff08\u4ee4\u548c7\u5e7411\u670818\u65e5\u516c\u544a\uff09\uff08\u7d42\u4e86\u3057\u307e\u3057\u305f\uff09\n[\u696d\u52d9\u7528\u30cf\u30a4\u30d6\u30ea\u30c3\u30c9\u81ea\u52d5\u8eca\uff08
\u30df\u30cb\u30d0\u30f3\u30bf\u30a4\u30d7\uff09\u306e\u8cfc\u5165\uff3b170KB\uff3d](https://", "api_data": null, "hint": null}, {"title": "20220701 hegurajima shougai fukkyuu", "url":
"https://www.jma.go.jp/jma/press/2207/01c/20220701_hegurajima_shougai_fukkyuu.html", "snippet": "\u300c\u8233\u5009\u5cf6\u300d\u5730\u9707\u89b3\u6e2c\u70b9\uff08\u77f3\u5ddd\u770c\uff09\u306e\u969c\
u5bb3\u5fa9\u65e7\u306b\u3064\u3044\u3066\n\uff5e\u4ee4\u548c\uff14\u5e74\uff16\u670822\u65e5\u4ed8\u5831\u9053\u767a\u8868\u95a2\u9023\uff5e\n\u5831\u9053\u767a\u8868\u65e5\n\u4ee4\u548c\uff14\u5e74\
uff17\u6708\uff11\u65e5\n\u6982\u8981\n\uff16\u670822\u65e513\u664225\u5206\u9803\u306b\u300c\n\u672c\u6587\n\uff16\u670822\u65e513\u664225\u5206\u9803\u304b\u3089\u3001\u969c\u5bb3\u306b\u3088\u308a\
u89b3\u6e2c\u30c7\u30fc\u30bf\u304c\u6d3b\u7528\u3067\u304d\u306a\u3044\u72b6\u614b\u306b\u3042\u308a\u307e\u3057\u305f\u300c\u8233\u5009\u5cf6\u300d\u5730\u9707\u89b3\u6e2c\u70b9\u306b\u3064\u304d\u3
07e\u3057\u3066\u3001\u672c\u65e5\uff08\uff11\u65e5\uff09\u73fe\u5730\u3067\u4f5c\u696d\u3092\u884c\u3044\u300114\u6642\u306b\u5fa9\u65e7\u3057\u307e\u3057\u305f\u3002\n\u4eca\u56de\u306e\u969c\u5bb3\
u306b\u4f34\u3044\u3001\u77f3\u5ddd\u770c\u80fd\u767b\u5730\u65b9\u3092\u9707\u6e90\u3068\u3059\u308b\u5730\u9707\u304c\u767a\u751f\u3057\u305f\u5834\u5408\u3001\u7dca\u6025\u5730\u9707\u901f\u5831\u7
67a\u8868\u306b\u9045\u5ef6\u304c\u751f\u3058\u308b\u53ef\u80fd\u6027\u304c\u3042\u308a\u307e\u3057\u305f\u304c\u3001\u305d\u306e\u72b6\u614b\u306f\u89e3\u6d88\u3057\u307e\u3057\u305f\u3002\u307e\u305
f\u3001\u9707\u5ea6\u306b\u3064\u3044\u3066\u3082\u6b63\u5e38\u306b\u767a\u8868\u53ef\u80fd\u3068\u306a\u3063\u3066\u304a\u308a\u307e\u3059\u3002\n\u672c\u969c\u5bb3\u306b\u3088\u308a\u3054\u8ff7\u60d
1\u3092\u304a\u304b\u3051\u3057\u307e\u3057\u305f\u3053\u3068\u3092\u304a\u8a6b\u3073\u3044\u305f\u3057\u307e\u3059\u3002\n\u554f\u5408\u305b\u5148\n\u5730\u9707\u706b\u5c71\u90e8\u5730\u9707\u706b\u5
c71\u6280\u8853\u30fb\u8abf\u67fb\u8ab2 \u62c5\u5f53 \u6674\u5c71\u3001\u8fd1\u6fa4\n\u96fb\u8a7103-6758-3900\uff08\u5185\u7dda5246\u30015282\uff09", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Kyushu Electric Power SSD missing recovery update June 2026"
}
```

### 📋 Result

```
{"query": "Kyushu Electric Power SSD missing recovery update June 2026", "results": [{"title": "Japan Data Breach: Kyushu Electric Loses Unencrypted SSD with 10.9 Million Customer Records", "url":
"https://www.techtimes.com/articles/318287/20260612/japan-data-breach-kyushu-electric-loses-unencrypted-ssd-109-million-customer-records.htm", "snippet":
"![Kyushu](https://d.techtimes.com/en/full/466614/kyushu.png?w=836&f=cdb7e25ac0fb3620eba50dfd4750ac51)\nKyushu Electric Power Transmission and Distribution Co., a wholly owned subsidiary of one of
Japan's largest regional utilities, [disclosed on June 8](https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-of-109-million-clients/) that a palm-sized solid-
state drive containing personal records for up to 10.9 million customers is missing \u2014 and that the drive was", "api_data": null, "hint": null}, {"title": "Kyushu Electric Power Co. reports data
breach affecting over 10 million customers | brief | SC Media", "url": "https://www.scworld.com/brief/kyushu-electric-power-co-reports-data-breach-affecting-over-10-million-customers", "snippet":
"Coverage from Bleeping Computer indicates that Kyushu Electric Power Co., Inc. has disclosed a physical security incident that potentially exposed the private data of over 10 million customers. The
incident occurred due to the loss of an external storage device used for regular data backups.On April 27, Kyushu Electric Power Co. utilized an external storage device for data backups due to
capacity constraints. The device was reportedly stored in a secured server room cabinet. However, on May 26, ", "api_data": null, "hint": null}, {"title": "Kyushu Electric Power subsidiary reports
data on 10.9m customers missing | MLex | Specialist news and analysis on legal risk and regulation", "url": "https://www.mlex.com/mlex/data-privacy-security/articles/2487255/kyushu-electric-power-
subsidiary-reports-data-on-10-9m-customers-missing", "snippet": "( June 9, 2026, 03:07 GMT | Official Statement) -- MLex Summary: Kyushu Electric Power Transmission and Distribution, Kyushu Electric
Power\u2019s wholly owned subsidiary in southern Japan, said Monday that an external storage device for backing up system data is missing, potentially exposing the personal data of around 10.9 million
of its customers. The device contained names, addresses and electricity-usage data, but no bank account or credit card details, and there is no evidence of a data leak. T", "api_data": null, "hint":
null}, {"title": "Japanese electricity giant apologises after physical drive with data of 10.9 million clients goes missing | TechRadar", "url": "https://www.techradar.com/pro/japanese-electricity-
giant-apologises-after-physical-drive-with-data-of-10-9-million-clients-goes-missing", "snippet": "Sign up with your email below to instantly access member features, newsletters and exclusive Insider
perks\nBy submitting your information, you confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nJapanese power giant
reveals it lost drive containing data of millions of clients\nDrive was left in an apparently unlocked cabinet\nNearly 11 million clients at risk, but no bank or card data was affected\nA Japanese
energy giant has ", "api_data": null, "hint": null}, {"title": "Kyuden Loses Customer Data Drive | Fukuoka Now", "url": "https://www.fukuoka-now.com/en/news/kyuden-loses-customer-data-drive/",
"snippet": "Kyuden Transmission and Distribution, a subsidiary of Kyushu Electric Power, announced on June 8 that it had lost a solid-state drive (SSD) containing personal information linked to about
10.9 million customer records, covering nearly all electricity users on Kyushu\u2019s mainland. The data included names, addresses, and contact details but did not contain bank account or credit card
information. The company said the SSD was used for routine data transfers because of limited server capacity. The dev", "api_data": null, "hint": null}, {"title": "Kyushu Electric Power Subsidiary
Reports Potential Theft of SSD Containing 10.9 Million Customer Records", "url": "https://beyondmachines.net/event_details/kyushu-electric-power-subsidiary-reports-potential-theft-of-ssd-
containing-10-9-million-customer-records-q-7-8-p-6", "snippet": "Kyushu Electric Power Subsidiary Reports Potential Theft of SSD Containing 10.9 Million Customer Records\nLearn More\nKyushu Electric
Power Transmission and Distribution Co., a subsidiary of Japan-based Kyushu Electric Power Co., reported a [data breach](https://www.asahi.com/ajw/articles/16629979) on June 8, 2026. The utility
reported that a portable solid-state drive (SSD) containing the personal information of approximately 10.9 million customers is missing from a restricted server room.\nThe se", "api_data": null,
"hint": null}, {"title": "[Kyushu Electric Power 9508.T] Regarding the Missing External Storage Medium Containing Customer Information at Kyushu Electric Power Transmission and Distribution Co., Inc.
\u2014 BigGo Finance", "url": "https://finance.biggo.com/news/jpx_tdnet_140120260608565052", "snippet": "[Kyushu Electric Power 9508.T] Regarding the Missing External Storage Medium Containing
Customer Information at Kyushu Electric Power Transmission and Distribution Co., Inc.\nKyushu Electric Power (9508.T) Timely Disclosure\nDisclosure Date/Time: 2026-06-08 15:30 Category: Other
Exchange: Tokyo/Fukuoka\nJune 8, 2026\nTo Whom It May Concern\nCompany Name: Kyushu Electric Power Company, Incorporated Representative: Masaru Nishiyama, President, CEO & Executive Officer Contact:
Toshihide Higashi, General", "api_data": null, "hint": null}, {"title": "Power company in Japan loses storage drive containing personal details for nearly 11 million customers", "url":
"https://mustsharenews.com/company-drive-personal-details/", "snippet": "Power company in Japan fears data breach after losing storage drive containing customer details\nPrivate personal information
of nearly 11 million people may have been leaked after a Kyushu power company lost a storage drive earlier this year.\nAccording to Asahi Shimbun, the storage drive was [discovered missing on 26
May](https://www.asahi.com/ajw/articles/16629979). The company insists that sensitive financial information was not leaked.\n![company drive personal details apology](https://mustsha", "api_data":
null, "hint": null}, {"title": "Japanese energy firm loses drive with data of 10.9 million clients", "url": "https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-
of-109-million-clients/", "snippet": "![Japanese energy firm loses drive with data of 10.9 million clients](https://www.bleepstatic.com/content/hl-images/2026/06/11/kyushu.jpg)\nKyushu Electric Power
Co., Inc. has disclosed a physical security incident that affects private data of more than 10 million customers.\nIn an official announcement, the company explains that the IT staff regularly
performs backups to manage server storage. Due to capacity constraints, on April 27 an external storage device was used for the task.\nThe drive was", "api_data": null, "hint": null}, {"title":
"Kyushu Electric Power", "url": "https://en.wikipedia.org/wiki/Kyushu_Electric_Power", "snippet": "Ky\u016bsh\u016b Electric Power Co., Inc. (\u4e5d\u5dde\u96fb\u529b\u682a\u5f0f\u4f1a\u793e,
Ky\u016bsh\u016b Denryoku Kabushiki Gaisha), sometimes abbreviated to Ky\u016bden (\u4e5d\u96fb), is a Japanese energy company that provides power to seven prefectures (Fukuoka, Nagasaki, \u014cita,
Saga, Miyazaki, Kumamoto, Kagoshima), and recently, to some parts of Hiroshima Prefecture.", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"Kyushu Electric Power\", \"url\":
\"https://en.wikipedia.org/wiki/Kyushu_Electric_Power\", \"extract\": \"Ky\\u016bsh\\u016b Electric Power Co., Inc. (\\u4e5d\\u5dde\\u96fb\\u529b\\u682a\\u5f0f\\u4f1a\\u793e, Ky\\u016bsh\\u016b
Denryoku Kabushiki Gaisha), sometimes abbreviated to Ky\\u016bden (\\u4e5d\\u96fb), is a Japanese energy company that provides power to seven prefectures (Fukuoka, Nagasaki, \\u014cita, Saga,
Miyazaki, Kumamoto, Kagoshima), and recently, to some parts of Hiroshima Prefecture.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "\"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\" \"SSD\" \"\u56de\u53ce\" OR \"\u767a\u898b\" OR \"\u898b\u3064\u304b\u3063\u305f\" 2026\u5e746\u6708"
}
```

### 📋 Result

```
{"query": "\"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\" \"SSD\" \"\u56de\u53ce\" OR \"\u767a\u898b\" OR \"\u898b\u3064\u304b\u3063\u305f\" 2026\u5e746\u6708", "results": [{"title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb 1090\u4e07\u4ef6\u306e\u500b\u4eba\u60c5\u5831\u3092\u7d1b\u5931 \u4fdd\u7ba1\u5834\u6240\u306bSSD\u304c\u306a\u304f\u767a\u899a
(2026\u5e746\u67088\u65e5\u63b2\u8f09) - \u30e9\u30a4\u30d6\u30c9\u30a2\u30cb\u30e5\u30fc\u30b9", "url": "https://news.livedoor.com/topics/detail/31492276/", "snippet": null, "api_data": null, "hint":
null}, {"title": "\u4e5d\u96fb\u9001\u914d\u96fb \u9867\u5ba21,090\u4e07\u4ef6\u306eSSD\u7d1b\u5931 \u2014
\u300c\u7121\u65bd\u9320\u30fb\u6697\u53f7\u5316\u306a\u3057\u300d\u306f\u3069\u306e\u6bb5\u968e\u3067\u6b62\u3081\u3089\u308c\u305f\u304b\uff5czephel01", "url":
"https://note.com/zephel01/n/n680ed674ed0f", "snippet": "![\u898b\u51fa\u3057\u753b\u50cf](https://assets.st-
note.com/production/uploads/images/283723263/rectangle_large_type_2_02f4bf20f6f7427a21103b78328007de.png?width=1280)\n\u4e5d\u96fb\u9001\u914d\u96fb \u9867\u5ba21,090\u4e07\u4ef6\u306eSSD\u7d1b\u5931
\u2014 \u300c\u7121\u65bd\u9320\u30fb\u6697\u53f7\u5316\u306a\u3057\u300d\u306f\u3069\u306e\u6bb5\u968e\u3067\u6b62\u3081\u3089\u308c\u305f\u304b\n\u3053\u3093\u306b\u3061\u306f\u3001\u304f\u30fc\u308
b\u305c\u308d\u3067\u3059\u3002\n\u4e5d\u5dde\u96fb\u529b\u306e\u5b50\u4f1a\u793e\u30fb\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u304c\u3001\u6700\u5927\u5ef6\u30791,090\u4e07\u4ef6\uff08\u96e2\u5cf6
\u3092\u9664\u304f\u4e5d\u5dde\u672c\u571f\u306e\u307b\u307c\u5168\u9867\u5ba2\uff09\u306e\u500b\u4eba\u60c5\u5831\u3092\u4fdd\u5b58\u3057\u305fSSD 1\u53f0\u3092\u7d1b\u5931\u3057\u305f\u3068\u3001202
6\u5e746\u67088\u65e5\u306b\u767a\u8868\u3057\u307e\u3057\u305f\u3002\u30b5\u30fc\u30d0\u30fc\u5ba4\u304b\u3089\u306e\u7121\u65ad\u6301\u3061\u51fa\u3057\u306e\u53ef\u80fd\u6027\u3082\u542b\u3081\u306
6\u8abf\u67fb\u4e2d\u3068\u3057\u3066\u3044\u307e\u3059\u3002\n\u666e\u6bb5\u306f\u30ed\u30fc\u30ab\u30ebLLM\u3084\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u306e\u691c\u8a3c\u8a18\u4e8b\u3092\u66f8\u3044\u
3066\u3044\u307e\u3059\u304c\u3001\u4eca\u56de\u306f\u300c\u7d44\u7e54\u306e\u30c7\u30fc\u30bf\u7ba1\u7406\u306f\u4f55\u91cd\u306b\u30c1\u30a7\u30c3\u30af\u304c\u3042\u308c\u3070\u4e8b\u6545\u3092\u96
32\u3052\u305f\u306e\u304b\u300d\u3068\u3044\u3046\u89b3\u70b9\u3067\u6574\u7406\u3057\u307e\u3059\u3002\u72af\u4eba\u63a2\u3057\u3067\u306f\u306a\u304f\u3001\u3069\u306e\u9632\u58c1\u304c1\u679a\u306
7\u3082\u3042\u308c\u3070\u88ab\u5bb3\u898f\u6a21\u304c\u5909\u308f\u3063\u305f\u304b\u304c\u672c\u984c\u3067\u3059\u3002\n\u4f55\u304c\u8d77\u304d\u305f\u304b\n\u7d4c\u7def: 2026\u5e744\u670827\u65e5
\u3001\u30b7\u30b9\u30c6\u30e0\u306e\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u6642\u306b\u30b5\u30fc\u30d0\u30fc\u5bb9\u91cf\u304c\u903c\u8feb\u3057\u3001\u4e00\u6642\u7684\u306a\u5916\u90e8\u4fdd\u7ba1\u
5148\u3068\u3057\u3066\u6301\u3061", "api_data": null, "hint": null}, {"title":
"\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u3001\u6700\u59271090\u4e07\u4ef6\u306e\u9867\u5ba2\u60c5\u5831\u6f0f\u6d29\u304b \u30c7\u30fc\u30bf\u3092\u4fdd\u5b58\u3057\u305fSSD\u7d1b\u5931", "url":
"https://xtech.nikkei.com/atcl/nxt/news/24/03260/", "snippet": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u306f2026\u5e746\u67088\u65e5\u3001\u6700\u59271090\u4e07\u4ef6\u306e\u9867\u5ba2\u60c5\u5831
\u3092\u4fdd\u5b58\u3057\u305fSSD\uff08\u30bd\u30ea\u30c3\u30c9\u30fb\u30b9\u30c6\u30fc\u30c8\u30fb\u30c9\u30e9\u30a4\u30d6\uff09\u304c\u6240\u5728\u4e0d\u660e\u306b\u306a\u3063\u305f\u3068\u767a\u886
8\u3057\u305f\u3002\u7d1b\u5931\u3057\u305fSSD\u306b\u306f\u6c0f\u540d\u3084\u4f4f\u6240\u3001\u4f7f\u7528\u96fb\u529b\u91cf\u30c7\u30fc\u30bf\u3001\u96fb\u8a71\u756a\u53f7\u306a\u3069\u3092\u4fdd\u5b
58\u3057\u3066\u3044\u305f\u3002\u3053\u308c\u3089\u306e\u9867\u5ba2\u60c5\u5831\u304c\u6f0f\u6d29\u3057\u305f\u53ef\u80fd\u6027\u304c\u3042\u308b\u3002\u9280\u884c\u53e3\u5ea7\u3084\u30af\u30ec\u30b8
\u30c3\u30c8\u30ab\u30fc\u30c9\u306e\u60c5\u5831\u306f\u542b\u307e\u308c\u3066\u3044\u306a\u3044\u3068\u3044\u3046\u3002\n\u540c\u793e\u306f\u30b5\u30fc\u30d0\u30fc\u5185\u306e\u30c7\u30fc\u30bf\u5bb9
\u91cf\u3092\u7ba1\u7406\u3059\u308b\u305f\u3081\u3001\u6708\u306b1\u5ea6USB\u63a5\u7d9a\u306eSSD\u306b\u30c7\u30fc\u30bf\u3092\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u3057\u3066\u3044\u308b\u3002\u540c\
u5e745\u670826\u65e5\u306b\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u3092\u6e96\u5099\u3092\u3057\u305f\u969b\u306bSSD\u306e\u7d1b\u5931\u304c\u5224\u660e\u3057\u305f\u30024\u670827\u65e5\u306e\u30d0\u30c3
\u30af\u30a2\u30c3\u30d7\u5b8c\u4e86\u6642\u306b\u306fSSD\u3092\u4fdd\u7ba1\u3057\u305f\u3053\u3068\u3092\u78ba\u8a8d\u3057\u3066\u3044\u305f\u3002SSD\u306f\u30b5\u30fc\u30d0\u30fc\u5ba4\u5185\u306e\u
30ad\u30e3\u30d3\u30cd\u30c3\u30c8\u306b\u4fdd\u7ba1\u3057\u3066\u3044\u305f\u304c\u3001\u65bd\u9320\u306f\u3057\u3066\u3044\u306a\u304b\u3063\u305f\u3002\n\u30b5\u30fc\u30d0\u30fc\u5ba4\u3078\u306e\u
5165\u9000\u5834\u306b\u306f\u30ab\u30fc\u30c9\u306b\u3088\u308b\u8a8d\u8a3c\u3084\u751f\u4f53\u8a8d\u8a3c\u306a\u3069\u3067\u500b\u4eba\u3092\u7279\u5b9a\u3067\u304d\u308b\u3088\u3046\u306b\u3057\u30
66\u3044\u305f\u30024\u670827\u65e5\u304b\u30895\u670826\u65e5\u307e\u3067\u306e\u5165\u9000\u5ba4\u8005\u3078\u306e\u30d2\u30a2\u30ea\u30f3\u30b0\u3084\u73fe\u5730\u8abf\u67fb\u3092\u5b9f\u65bd\u3057
\u305f\u304c\u3001SSD\u306f\u767a\u898b\u3067\u304d\u305a\u3001\u539f\u56e0\u3082\u7279\u5b9a\u3067\u304d\u3066\u3044\u306a\u3044\u3068\u3044\u3046\u3002\n[\u3053\u306e\u8a18\u4e8b\u306e\u76ee\u6b21\u
3078\u623b\u308b](https://xtech.nikkei.com/news/?i_cid=nbpnxt_backindex_child)", "api_data": null, "hint": null}, {"title": "\u4e5d\u96fb\u9001\u914d\u96fb
\u9867\u5ba2\u60c5\u5831\u5165\u308aSSD\u7d1b\u5931 - Yahoo!\u30cb\u30e5\u30fc\u30b9", "url": "https://news.yahoo.co.jp/pickup/6583471", "snippet": null, "api_data": null, "hint": null}, {"title": "\u
4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u682a\u5f0f\u4f1a\u793e\u3067\u5916\u90e8\u8a18\u61b6\u5a92\u4f53\u304c\u6240\u5728\u4e0d\u660e\u3001\u6700\u59271,090\u4e07\u53e3\u5206\u306e\u9867\u5ba2\u60c
5\u5831\u304c\u6f0f\u3048\u3044\u3057\u305f\u53ef\u80fd\u6027 | \u30b5\u30a4\u30d0\u30fc\u30bb\u30ad\u30e5\u30ea\u30c6\u30a3\u30e9\u30dc", "url": "https://www.gate02.ne.jp/lab/incident-news/kyushu-
electric-power-20260610/", "snippet": "2026.06.10\n\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u682a\u5f0f\u4f1a\u793e\u3067\u5916\u90e8\u8a18\u61b6\u5a92\u4f53\u304c\u6240\u5728\u4e0d\u660e\u3001\u670
0\u59271,090\u4e07\u53e3\u5206\u306e\u9867\u5ba2\u60c5\u5831\u304c\u6f0f\u3048\u3044\u3057\u305f\u53ef\u80fd\u6027\n\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb\u682a\u5f0f\u4f1a\u793e\u306f\u3001\u9867
\u5ba2\u60c5\u5831\u3092\u4fdd\u5b58\u3057\u305f\u5916\u90e8\u8a18\u61b6\u5a92\u4f53\u304c\u6240\u5728\u4e0d\u660e\u3068\u306a\u308a\u3001\u60c5\u5831\u304c\u6f0f\u3048\u3044\u3057\u305f\u53ef\u80fd\u
6027\u304c\u3042\u308b\u3053\u3068\u30922026\u5e746\u67088\u65e5\u306b\u516c\u8868\u3057\u307e\u3057\u305f\u3002\n\u516c\u8868\u306b\u3088\u308b\u3068\u3001\u540c\u5e745\u670826\u65e5\u306b\u5b9a\u671
f\u30d0\u30c3\u30af\u30a2\u30c3\u30d7\u4f5c\u696d\u3092\u884c\u304a\u3046\u3068\u3057\u305f\u3068\u3053\u308d\u3001\u30b5\u30fc\u30d0\u30fc\u5ba4\u306e\u30ad\u30e3\u30d3\u30cd\u30c3\u30c8\u306b\u5916\
u90e8\u8a18\u61b6\u5a92\u4f53\u304c\u5b58\u5728\u3057\u306a\u3044\u3053\u3068\u304c\u5224\u660e\u3057\u305f\u3068\u306e\u3053\u3068\u3067\u3059\u3002\u5f53\u8a72\u30ad\u30e3\u30d3\u30cd\u30c3\u30c8\u3
06f\u65bd\u9320\u3055\u308c\u3066\u304a\u3089\u305a\u3001\u6700\u5f8c\u306b\u4fdd\u7ba1\u304c\u78ba\u8a8d\u3055\u308c\u305f\u306e\u306f\u540c\u5e744\u670827\u65e5\u3068\u3057\u3066\u3044\u307e\u3059\u
3002\n\u6f0f\u3048\u3044\u3057\u305f\u53ef\u80fd\u6027\u304c\u3042\u308b\u306e\u306f\u3001\u6700\u59271,090\u4e07\u53e3\u5206\u306e\u9700\u8981\u8005\u540d\u3001\u4f9b\u7d66\u5834\u6240\u4f4f\u6240\u3
001\u4f7f\u7528\u96fb\u529b\u91cf\u30c7\u30fc\u30bf\u3001\u96fb\u8a71\u756a\u53f7\u3001\u5c0f\u58f2\u96fb\u6c17\u4e8b\u696d\u8005\u540d\u7b49\u3068\u306e\u3053\u3068\u3067\u3059\u3002\u306a\u304a\u300
1\u9280\u884c\u53e3\u5ea7\u3084\u30af\u30ec\u30b8\u30c3\u30c8\u30ab\u30fc\u30c9\u306e\u60c5\u5831\u306f\u542b\u307e\u308c\u3066\u3044\u306a\u3044\u3068\u3057\u3066\u3044\u307e\u3059\u3002\n\u540c\u793
e\u306f\u95a2\u4fc2\u8005\u3078\u306e\u30d2\u30a2\u30ea\u30f3\u30b0\u3084\u73fe\u5730\u8abf\u67fb\u3092\u5b9f\u65bd\u3057\u3001\u7121\u65ad\u6301\u3061\u51fa\u3057\u306e\u53ef\u80fd\u6027\u3082\u542b\
u3081\u3066\u8abf\u67fb\u3057\u3066\u3044\u307e\u3059\u304c\u3001\u516c\u8868\u6642\u70b9\u306b\u304a\u3044\u3066\u767a\u898b\u306b\u306f\u81f3\u3063\u3066\u3044\u307e\u305b\u3093\u3002\n\u307e\u305f\
u3001\u500b\u4eba\u60c5\u5831\u4fdd\u8b77\u59d4\u54e1\u4f1a\u53ca\u3073\u76e3\u7763\u5b98\u5e81\u3078\u306e\u5831\u544a\u3092\u884c\u3063\u3066\u304a\u308a\u3001\u4eca\u5f8c\u306f\u6240\u5728\u78ba\u8
a8d\u3092\u7d99\u7d9a\u3059\u308b\u3068\u3068\u3082\u306b\u3001\u5bfe\u8c61\u9867\u5ba2\u3078\u306e\u500b\u5225\u901a\u77e5\u3092\u5b9f\u65bd\u3057\u3001\u5916\u90e8\u8a18\u61b6\u5a92\u4f53\u306e\u7ba
1\u7406\u306b\u95a2\u3059\u308b\u518d\u767a\u9632\u6b62", "api_data": null, "hint": null}, {"title": "\u4e5d\u5dde\u96fb\u529b\u9001\u914d\u96fb
1000\u4e07\u4ef6\u8d85\u306e\u500b\u4eba\u60c5\u5831\u4fdd\u5b58\u3057\u305f\u8a18\u9332\u5a92\u4f53(SSD)\u3092\u7d1b\u5931 [\u5c11\u8003\u3055\u3093\u2605]", "url":
"https://asahi.5ch.io/test/read.cgi/newsplus/1780916732/l50", "snippet": null, "api_data": null, "hint": null}, {"title": "kaisyuu2004 2 1467", "url":
"https://www.mhlw.go.jp/topics/bukyoku/iyaku/kaisyu/kaisyuu2004-2-1467.html", "snippet": "|\n\ufffd\ufffd\ufffd\ufffd\u033e\ufffd\u06a4\ufffd\ufffd\ufffd\ufffd\ufffd\u033e\n\ufffd\ufffd\ufffd\ufffd\u0
33e\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u0136\ufffd\ufffd\ufffd\u0232\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\u033e\ufffd\ufffd\ufffd\ufffd\ufffd\uff
fd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u9861SSD-
1000\n\ufffd\u043e\u0765\ufffd\ufffd\u00e5\u0221\ufffd\ufffd\ufffd\ufffd\u0335\u06a4\u04fd\u0432\u067b\ufffd\ufffd\ufffd\n\ufffd\ufffd\u00a4\ufffd\u05b9\u6867M06751\ufffd\ufffdM06754\ufffd\ufffdM06756
\ufffd\ufffdM06759\ufffd\ufffdM06761\ufffd\ufffdM06764\ufffd\ufffdM06766\ufffd\ufffdM06789
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM06791\ufffd\ufffdM06802\ufffd\ufffdM06804\ufffd\ufffdM06806\ufffd\ufffdM06812\ufffd\ufffdM06816\ufffd\ufffdM6818\ufffd\ufffdM06820
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM06851C\ufffd\ufffdM06855\ufffd\ufffdM06859\ufffd\ufffdM06861C\ufffd\ufffdM06864\ufffd\ufffdM06865
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM06867C\ufffd\ufffdM06879C\ufffd\ufffdM06882C\ufffd\ufffdM06886C\ufffd\ufffdM0688C\ufffd\ufffdM06890C\ufffd\ufffdM06895C
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM06923C\ufffd\ufffdM06924C\ufffd\ufffdM06926C\ufffd\ufffdM06929C\ufffd\ufffdM06931C\ufffd\ufffdM06933C
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM06935C\ufffd\ufffdM06947C\ufffd\ufffdM07152C\ufffd\ufffdM07154C\ufffd\ufffdM07167C\ufffd\ufffdM07169C
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdM0", "api_data": null, "hint": null}, {"title": "kaisyuu2010 2 3854", "url":
"https://www.mhlw.go.jp/topics/bukyoku/iyaku/kaisyu/2010/kaisyuu2010-2-3854.html", "snippet": "|\n\u02bf\ufffd\ufffd22\u01ef 4\ufffd\ufffd
1\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\n\ufffd\ufffd\ufffd\ufffd\u033e\ufffd\u06a4\ufffd\ufffd\ufffd\ufffd\ufffd\u033e\n\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd
\ufffd\ufffd\ufffd\ufffd\u016a\u033e\ufffd\u03a1\ufffd\u00f1\ufffd\ufffd\ufffd\ufffd\u0465\ufffd\ufffd\u9979III\ufffd\ufffd\ufffd\u05a5\ufffd\ufffd\u00e5\ufffd
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\u03a1\ufffd\ufffd\u4861\u033e\ufffd\ufffd\ufffd\ufffd\u0474\ufffd\ufffd\u0725\ufffd\ufffd\u00e5\ufffd\n\ufffd\u043e\u0765\ufffd\ufffd\u00e5\u022
1\ufffd\ufffd\ufffd\ufffd\u0335\u06a4\u04fd\u0432\u067b\ufffd\ufffd\ufffd\n\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd
\ufffd\ufffd\ufffd\ufffd\u043e\u077f\ufffd\ufffd\u0321\ufffd\ufffd\ufffd\ufffd\u00e5\ufffd\ufffd\ufffd\ufffd\u02a1\ufffd1327\ufffd\ufffd(\ufffd\ufffd\ufffd\ufffd)
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd \ufffd\u0661\ufffd\ufffd\ufffd
\ufffd\ufffd\ufffd\ufffd\u02bf\ufffd\ufffd22\u01ef1\ufffd\ufffd14\ufffd\ufffd\ufffd\ufffd\u02bf\ufffd\ufffd22\u01ef3\ufffd\ufffd30\ufffd\ufffd
\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u02a1\ufffd\ufffd\ufffd\ufffd\u05a1\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u00e5\ufffd\ufffd\u05b9\u6861\ufffd\ufffd
\ufffd\ufffd\ufffd\u0321\ufffd\ufffd\ufffd\u00f1\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd123013055601
\ufffd\ufffd\ufffd\ufffd100114100\ufffd\ufffd\ufffd\ufffd12\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd123013055601
\ufffd\ufffd\ufffd\ufffd100127100\ufffd\ufffd\ufffd\ufffd12\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd123013055601
\ufffd\ufffd\ufffd\ufffd100226100\ufffd\ufffd\ufffd\ufffd12\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd123023092900
\ufffd\ufffd\ufffd\ufffd100212100\ufffd\ufffd\ufffd\ufffd 4\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd123023093000
\ufffd\ufffd\ufffd\ufffd100212100\ufffd\ufffd\ufffd\ufffd 2\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd \ufffd\ufffd\ufffd\ufffd\ufffd\ufffd", "api_data": null, "hint": null}, {"title": "20220701 hegurajima
shougai fukkyuu", "url": "https://www.jma.go.jp/jma/press/2207/01c/20220701_hegurajima_shougai_fukkyuu.html", "snippet": "\u300c\u8233\u5009\u5cf6\u300d\u5730\u9707\u89b3\u6e2c\u70b9\uff08\u77f3\u5ddd
\u770c\uff09\u306e\u969c\u5bb3\u5fa9\u65e7\u306b\u3064\u3044\u3066\n\uff5e\u4ee4\u548c\uff14\u5e74\uff16\u670822\u65e5\u4ed8\u5831\u9053\u767a\u8868\u95a2\u9023\uff5e\n\u5831\u9053\u767a\u8868\u65e5\n
\u4ee4\u548c\uff14\u5e74\uff17\u6708\uff11\u65e5\n\u6982\u8981\n\uff16\u670822\u65e513\u664225\u5206\u9803\u306b\u300c\n\u672c\u6587\n\uff16\u670822\u65e513\u664225\u5206\u9803\u304b\u3089\u3001\u969c
\u5bb3\u306b\u3088\u308a\u89b3\u6e2c\u30c7\u30fc\u30bf\u304c\u6d3b\u7528\u3067\u304d\u306a\u3044\u72b6\u614b\u306b\u3042\u308a\u307e\u3057\u305f\u300c\u8233\u5009\u5cf6\u300d\u5730\u9707\u89b3\u6e2c\u
70b9\u306b\u3064\u304d\u307e\u3057\u3066\u3001\u672c\u65e5\uff08\uff11\u65e5\uff09\u73fe\u5730\u3067\u4f5c\u696d\u3092\u884c\u3044\u300114\u6642\u306b\u5fa9\u65e7\u3057\u307e\u3057\u305f\u3002\n\u4eca
\u56de\u306e\u969c\u5bb3\u306b\u4f34\u3044\u3001\u77f3\u5ddd\u770c\u80fd\u767b\u5730\u65b9\u3092\u9707\u6e90\u3068\u3059\u308b\u5730\u9707\u304c\u767a\u751f\u3057\u305f\u5834\u5408\u3001\u7dca\u6025\u
5730\u9707\u901f\u5831\u767a\u8868\u306b\u9045\u5ef6\u304c\u751f\u3058\u308b\u53ef\u80fd\u6027\u304c\u3042\u308a\u307e\u3057\u305f\u304c\u3001\u305d\u306e\u72b6\u614b\u306f\u89e3\u6d88\u3057\u307e\u30
57\u305f\u3002\u307e\u305f\u3001\u9707\u5ea6\u306b\u3064\u3044\u3066\u3082\u6b63\u5e38\u306b\u767a\u8868\u53ef\u80fd\u3068\u306a\u3063\u3066\u304a\u308a\u307e\u3059\u3002\n\u672c\u969c\u5bb3\u306b\u30
88\u308a\u3054\u8ff7\u60d1\u3092\u304a\u304b\u3051\u3057\u307e\u3057\u305f\u3053\u3068\u3092\u304a\u8a6b\u3073\u3044\u305f\u3057\u307e\u3059\u3002\n\u554f\u5408\u305b\u5148\n\u5730\u9707\u706b\u5c71\u
90e8\u5730\u9707\u706b\u5c71\u6280\u8853\u30fb\u8abf\u67fb\u8ab2 \u62c5\u5f53 \u6674\u5c71\u3001\u8fd1\u6fa4\n\u96fb\u8a7103-6758-3900\uff08\u5185\u7dda5246\u30015282\uff09", "api_data": null, "hint":
null}, {"title": "www.mhlw.go.jp", "url": "https://www.mhlw.go.jp/topics/bukyoku/iyaku/kaisyu/00-3-011.html", "snippet": "2000\ufffdN5\ufffd\ufffd15\ufffd\ufffd\ufffd\uc42c\n\ufffd@\n1.\ufffd@\ufffd\u
fffd\u0296\ufffd\ufffdy\ufffd\u0454\u0314\ufffd\ufffd\ufffd\n\ufffd\ufffd\u0293I\ufffd\ufffd\ufffd\u0301F\ufffd\u0117p\ufffd\ufffd\ufffd\ufffd\ufffdg\ufffd\u645c\ufffdf\ufffdf\ufffd\ufffd\ufffdu\n\uff
fd\u0314\ufffd\ufffd\ufffd \ufffdF\ufffd\ufffd\ufffd\ufffd\ufffdg\ufffdf\ufffdf\ufffd\ufffd\ufffdu \ufffdr\ufffdr\ufffdg\ufffd|\ufffdP\ufffdU\ufffdO\ufffd`\ufffd`\n2.\ufffd@\ufffd\u038f\u06c3\ufffd\uf
ffdb\ufffdg\ufffdA\ufffd\ufffd\ufffd\u028by\ufffd\u044fo\ufffd\ufffd\ufffd\ufffd\n\ufffd^\ufffd\ufffd\ufffd\ufffd\ufffdF\ufffdr\ufffdr\ufffdg\ufffd|\ufffdP\ufffdU\ufffdO\ufffd`\n\ufffd\ufffd\ufffd\uff
fd\ufffd\u050d\ufffd\ufffdF\ufffd\ufffd\ufffd\ufffd\ufffd\u050d\ufffd\ufffd\u0301u\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdv\ufffd\u0242\u0
115\\\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u0102\ufffd\ufffd\u0702\ufffd\ufffdB\n\ufffd@\ufffd@\ufffd@\ufffd@\ufffd@\ufffdu\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdv\ufffdF\ufffdR\ufffd[\u
fffdh\ufffd\ufffd\ufffd\ufffd\ufffd\ua0bd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdp\ufffd\ufffd\ufffd\ufffd\ufffd\u0142\ufffd\ufffd\u8361\ufffd\ufffd\u0309\ufffd\ufffdC\n\ufffd@\ufffd@\uf
ffd@\ufffd@\ufffd@\ufffd\u0182\u034aW\ufffd\ufffd\ufffd\ufffd\u0702\ufffd\ufffd\ufffdB\n\ufffd@\ufffd@\ufffd@\ufffd@\ufffd@\ufffdu\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\ufffdv\ufffdF\ufffd\u
353c\ufffd\u030el\ufffd\ufffd\ufffd\u0350\ufffd\ufffd\ufffd\ufffd\u0142\ufffd\ufffd\ufffdA\ufffd\ufffd\ufffd\ufffd\ufffd\u050d\ufffd\ufffd\ufffd\u01c2\ufffd\ufffd\u0502\u0242\u010e\ufffd\n\ufffd@\ufff
d@\ufffd@\ufffd@\ufffd@\ufffd\ufffd\ufffd\u0102\ufffd\ufffd\ufffdA
\ufffd\ufffd\ufffdL\ufffd\u050d\ufffd\ufffd\u0311\ufffd\ufffdu\ufffd\ufffd\ufffd\ufffd\ufffd\ufffd\u0309\ufffd\ufffdC\ufffd\u024aY\ufffd\ufffd\ufffdv\ufffd\ufffd\ufffd\u0702\ufffd\ufffdB****2972
****2987 \ufffd` ****2989 ****2991 \ufffd` ****2993 ****2995 \ufffd` ****2998 ****3003 ****3", "api_data": null, "hint": null}]}
```

```json
{
  "query": "Kyushu Electric SSD found recovered seized June 2026"
}
```

### 📋 Result

```
{"query": "Kyushu Electric SSD found recovered seized June 2026", "results": [{"title": "Japan Data Breach: Kyushu Electric Loses Unencrypted SSD with 10.9 Million Customer Records", "url":
"https://www.techtimes.com/articles/318287/20260612/japan-data-breach-kyushu-electric-loses-unencrypted-ssd-109-million-customer-records.htm", "snippet":
"![Kyushu](https://d.techtimes.com/en/full/466614/kyushu.png?w=836&f=cdb7e25ac0fb3620eba50dfd4750ac51)\nKyushu Electric Power Transmission and Distribution Co., a wholly owned subsidiary of one of
Japan's largest regional utilities, [disclosed on June 8](https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-of-109-million-clients/) that a palm-sized solid-
state drive containing personal records for up to 10.9 million customers is missing \u2014 and that the drive was", "api_data": null, "hint": null}, {"title": "Japanese electricity giant apologises
after physical drive with data of 10.9 million clients goes missing | TechRadar", "url": "https://www.techradar.com/pro/japanese-electricity-giant-apologises-after-physical-drive-with-data-
of-10-9-million-clients-goes-missing", "snippet": "Sign up with your email below to instantly access member features, newsletters and exclusive Insider perks\nBy submitting your information, you
confirm you are aged 16 or over,\nhave read our\nPrivacy Policy\nand agree to the\nTerms & Conditions. Geographical rules apply.\nJapanese power giant reveals it lost drive containing data of millions
of clients\nDrive was left in an apparently unlocked cabinet\nNearly 11 million clients at risk, but no bank or card data was affected\nA Japanese energy giant has ", "api_data": null, "hint": null},
{"title": "Power company in Japan fears data breach after losing storage drive containing customer details - DataBreaches.Net", "url": "https://databreaches.net/2026/06/10/power-company-in-japan-
fears-data-breach-after-losing-storage-drive-containing-customer-details/", "snippet": null, "api_data": null, "hint": null}, {"title": "Electric company loses drive containing 10M customer records -
Business Insurance", "url": "https://www.businessinsurance.com/electric-company-loses-drive-containing-10m-customer-records/", "snippet": "Japanese firm Kyushu Electric Power Company Inc. has lost an
external storage device that contains private data of more than 10 million customers \u2013 including names and phone numbers \u2013 after IT staff performed backups to manage server storage,
BleepingComputer reported. The \\ security incident occurred after the drive was stored in a server cabinet that was later found unlocked. The company is investigating the incident.", "api_data":
null, "hint": null}, {"title": "Kyushu Electric Power Subsidiary Reports Potential Theft of SSD Containing 10.9 Million Customer Records", "url": "https://beyondmachines.net/event_details/kyushu-
electric-power-subsidiary-reports-potential-theft-of-ssd-containing-10-9-million-customer-records-q-7-8-p-6", "snippet": "Kyushu Electric Power Subsidiary Reports Potential Theft of SSD Containing
10.9 Million Customer Records\nLearn More\nKyushu Electric Power Transmission and Distribution Co., a subsidiary of Japan-based Kyushu Electric Power Co., reported a [data
breach](https://www.asahi.com/ajw/articles/16629979) on June 8, 2026. The utility reported that a portable solid-state drive (SSD) containing the personal information of approximately 10.9 million
customers is missing from a restricted server room.\nThe se", "api_data": null, "hint": null}, {"title": "Kyushu Electric Power subsidiary reports data on 10.9m customers missing | MLex | Specialist
news and analysis on legal risk and regulation", "url": "https://www.mlex.com/mlex/data-privacy-security/articles/2487255/kyushu-electric-power-subsidiary-reports-data-on-10-9m-customers-missing",
"snippet": "( June 9, 2026, 03:07 GMT | Official Statement) -- MLex Summary: Kyushu Electric Power Transmission and Distribution, Kyushu Electric Power\u2019s wholly owned subsidiary in southern
Japan, said Monday that an external storage device for backing up system data is missing, potentially exposing the personal data of around 10.9 million of its customers. The device contained names,
addresses and electricity-usage data, but no bank account or credit card details, and there is no evidence of a data leak. T", "api_data": null, "hint": null}, {"title": "Kyuden Loses Customer Data
Drive | Fukuoka Now", "url": "https://www.fukuoka-now.com/en/news/kyuden-loses-customer-data-drive/", "snippet": "Kyuden Transmission and Distribution, a subsidiary of Kyushu Electric Power, announced
on June 8 that it had lost a solid-state drive (SSD) containing personal information linked to about 10.9 million customer records, covering nearly all electricity users on Kyushu\u2019s mainland. The
data included names, addresses, and contact details but did not contain bank account or credit card information. The company said the SSD was used for routine data transfers because of limited server
capacity. The dev", "api_data": null, "hint": null}, {"title": "Power company in Japan loses storage drive containing personal details for nearly 11 million customers", "url":
"https://mustsharenews.com/company-drive-personal-details/", "snippet": "Power company in Japan fears data breach after losing storage drive containing customer details\nPrivate personal information
of nearly 11 million people may have been leaked after a Kyushu power company lost a storage drive earlier this year.\nAccording to Asahi Shimbun, the storage drive was [discovered missing on 26
May](https://www.asahi.com/ajw/articles/16629979). The company insists that sensitive financial information was not leaked.\n![company drive personal details apology](https://mustsha", "api_data":
null, "hint": null}, {"title": "Japanese energy firm loses drive with data of 10.9 million clients", "url": "https://www.bleepingcomputer.com/news/security/japanese-energy-firm-loses-drive-with-data-
of-109-million-clients/", "snippet": "![Japanese energy firm loses drive with data of 10.9 million clients](https://www.bleepstatic.com/content/hl-images/2026/06/11/kyushu.jpg)\nKyushu Electric Power
Co., Inc. has disclosed a physical security incident that affects private data of more than 10 million customers.\nIn an official announcement, the company explains that the IT staff regularly
performs backups to manage server storage. Due to capacity constraints, on April 27 an external storage device was used for the task.\nThe drive was", "api_data": null, "hint": null}, {"title":
"SSNDOB", "url": "https://en.wikipedia.org/wiki/SSNDOB", "snippet": "SSNDOB was an online marketplace that sold stolen Social Security numbers, birth dates and other personal information of U.S.
citizens starting in 2012 until it was shut down in June 2022 following a U.S. government seizure. It used the domain names ssndob.ws, ssndob.vip, ssndob.club, and blackjob.biz.", "api_data":
{"content": [{"type": "text", "text": "{\"title\": \"SSNDOB\", \"url\": \"https://en.wikipedia.org/wiki/SSNDOB\", \"extract\": \"SSNDOB was an online marketplace that sold stolen Social Security
numbers, birth dates and other personal information of U.S. citizens starting in 2012 until it was shut down in June 2022 following a U.S. government seizure. It used the domain names ssndob.ws,
ssndob.vip, ssndob.club, and blackjob.biz.\", \"mode\": \"full\"}"}]}, "hint": null}]}
```

## 💬 Response

No evidence of recovery. Let me now analyze this systematically.

## 💬 Response

The factor-implied probability is ~3.4%, and my tentative is 8%. The gap is modest. Let me adjust slightly downward and run the premortem.
