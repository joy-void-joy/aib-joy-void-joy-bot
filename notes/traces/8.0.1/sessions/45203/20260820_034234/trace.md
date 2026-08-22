# Reasoning Log: Will a U.S. federal agency announce new or expanded model evaluation agreements with both OpenAI and Anthropic before September 3, 2026?

*Generated: 2026-08-20T03:59:43.363140+00:00*


## 💬 Response

I'll start by parsing the resolution criteria carefully, then research the current state of CAISI agreements.

**Step 1: Parse the resolution criteria**

## 🔧 Tool: mcp__search__search


## 🔧 Tool: mcp__search__search


```json
{
  "query": "CAISI NIST agreement OpenAI Anthropic frontier model evaluation 2026"
}
```

### 📋 Result

```
Error: result (81,627 characters across 1 line) exceeds maximum allowed tokens. Output has been saved to /tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-
cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-search-1787197396339.txt.
Format: Plain text
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-
search-1787197396339.txt in sequential chunks until 100% of the content has been read.
- Note: this file's lines are too long for Read's offset/limit chunking. If a shell tool is available, slice by character range (e.g. python read()[A:B], dd, or cut -c) instead.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to read, explicitly state
which portion you could not read and why, and proceed.
```

```json
{
  "query": "Center for AI Standards and Innovation announcement August 2026"
}
```

### 📋 Result

```
Error: result (69,666 characters across 1 line) exceeds maximum allowed tokens. Output has been saved to /tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-
cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-search-1787197415329.txt.
Format: Plain text
Use offset and limit parameters to read specific portions of the file, search within it for specific content, and jq to make structured queries.
REQUIREMENTS FOR SUMMARIZATION/ANALYSIS/REVIEW:
- You MUST read the content from the file at /tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-
search-1787197415329.txt in sequential chunks until 100% of the content has been read.
- Note: this file's lines are too long for Read's offset/limit chunking. If a shell tool is available, slice by character range (e.g. python read()[A:B], dd, or cut -c) instead.
- If you receive truncation warnings when reading the file, reduce the chunk size until you have read 100% of the content without truncation.
- Before producing ANY summary or analysis, you MUST explicitly describe what portion of the content you have read. ***If you did not read the entire content, you MUST explicitly state this.***
- If after a few attempts you cannot read the file (file not found, lines too long for Read's offset/limit, no shell access), STOP retrying. Summarize what you were able to read, explicitly state
which portion you could not read and why, and proceed.
```

## 💭 Thinking



## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "import os\np=\"/tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-search-1787197396339.txt\"\nprint(os.path.exists(p))\n"
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"exit_code\": 0, \"stdout\": \"False\\n\", \"stderr\": \"\", \"duration_ms\": 0}"}]
```

## 🔧 Tool: mcp__search__search


```json
{
  "query": "CAISI voluntary agreement OpenAI Anthropic pre-deployment evaluation announcement",
  "lanes": [
    "news"
  ],
  "limit": 10
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"CAISI voluntary agreement OpenAI Anthropic pre-deployment evaluation announcement\", \"lanes_run\": [], \"web\": [], \"markets\": [], \"news\": [],
\"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [], \"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

The sandbox can't see that path. Let me extract from the saved results using Grep.

## 🔧 Tool: mcp__Grep


```json
{
  "pattern": ".{0,400}CAISI.{0,600}",
  "path": "/tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-search-1787197396339.txt",
  "output_mode": "content",
  "-o": "true",
  "head_limit": "25"
}
```

### 📋 Result

```
<tool_use_error>Error: No such tool available: mcp__Grep</tool_use_error>
```

## 🔧 Tool: Grep


```json
{
  "pattern": ".{0,300}CAISI.{0,500}",
  "path": "/tmp/aib-agent-cwd/.lup/sessions/aib-agent-cwd-999728ae595d/projects/-tmp-aib-agent-cwd/be972142-4d06-4e38-abaa-dcedb6beee77/tool-results/mcp-search-search-1787197396339.txt",
  "output_mode": "content",
  "-o": true,
  "head_limit": 30
}
```

### 📋 Result

```
Grep denied. Allowed: ['/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/sandbox-shared', '/home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads', '/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/notes/traces/8.0.1/sessions/45203/20260820_034234', '/home/pfftz/job/onit/aib-joy-
void-joy-bot.git/tree/main/notes/traces/8.0.1/forecasts/45203/20260820_034234', '/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/notes/traces']
```

## 💭 Thinking



## 💬 Response

Path access is restricted. Let me re-run searches with tighter limits.

## 🔧 Tool: mcp__search__search


```json
{
  "query": "CAISI NIST agreements OpenAI Anthropic model evaluation",
  "lanes": [
    "web"
  ],
  "limit": 4
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"CAISI NIST agreements OpenAI Anthropic model evaluation\", \"lanes_run\": [\"web\"], \"web\": [{\"title\": \"Institutionalizing AI Safety: CISA\\u2019s Agentic
Guide and CAISI Agreements\", \"url\": \"https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-ai-governance-cisa-nist-caisi-2026/\", \"snippet\": \"Published:
2026-05-07\\nCategories: AI Governance, AI Security, Regulatory Compliance\\nKey Takeaways\\n- On May 1, 2026, six national cybersecurity agencies \\u2014 CISA, NSA, and the cyber arms of Australia,
Canada, New Zealand, and the United Kingdom \\u2014 jointly published \\u201cCareful Adoption of Agentic AI Services,\\u201d the first coordinated multinational security guidance specifically
addressing agentic AI systems [1].\\n- The guidance defines five categories of agentic AI risk \\u2014 privilege escalation, design and \", \"api_data\": null, \"hint\": null, \"text\": \"Published:
2026-05-07\\nCategories: AI Governance, AI Security, Regulatory Compliance\\nKey Takeaways\\n- On May 1, 2026, six national cybersecurity agencies \\u2014 CISA, NSA, and the cyber arms of Australia,
Canada, New Zealand, and the United Kingdom \\u2014 jointly published \\u201cCareful Adoption of Agentic AI Services,\\u201d the first coordinated multinational security guidance specifically
addressing agentic AI systems [1].\\n- The guidance defines five categories of agentic AI risk \\u2014 privilege escalation, design and configuration failures, behavioral misalignment, structural
brittleness, and accountability gaps \\u2014 and requires each agent to carry a verified, cryptographically anchored identity with short-lived credentials [1][2].\\n- On May 5, 2026, NIST\\u2019s
Center for AI Standards and Innovation (CAISI) announced pre-deployment testing agreements with Google DeepMind, Microsoft, and xAI, expanding its frontier model evaluation program to five major labs
alongside existing partners OpenAI and Anthropic [3].\\n- CAISI evaluations, now numbering more than 40 completed assessments including unreleased models, cover cybersecurity, biosecurity, and
chemical weapons risks; some are conducted in classified environments by the interagency TRAINS Taskforce [3][4].\\n- Together, these developments signal a significant shift in AI safety governance
\\u2014 from voluntary industry pledges toward institutionalized government evaluation and operational guidance \\u2014 with implications for how enterprises should consider structuring their own
agentic AI programs.\\nBackground\\nThe question of who governs frontier AI \\u2014 and how \\u2014 has been contested since the first wave of large language model deployments. For most of 2022 and
2023, the primary mechanism was voluntary: companies made public pledges and internal commitments while governments convened forums and published principles. In July 2023, seven U.S. AI developers
signed voluntary commitments to the White House covering internal safety testing, protection of unreleased m\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/b02592301994.txt]\"}, {\"title\": \"Google, Microsoft and xAI\\u2019s frontier AI to face national security testing | CIO Dive\", \"url\":
\"https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/\", \"snippet\": null, \"api_data\": null, \"hint\": null, \"text\": null}, {\"title\": \"US government agency to
safety test frontier AI models before release | CIO\", \"url\": \"https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-before-release.html\", \"snippet\":
\"CAISI\\u2019s agreements with Google, Microsoft, and xAI preceded a report that the White House may be planning to create its own AI vetting system.\\n![Checklist, checking boxes, testing,
QA](https://www.cio.com/wp-content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation
(CAISI), a division of the US Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that wo\", \"api_data\": null, \"hint\": null, \"text\": \"CAISI\\u2019s agreements
with Google, Microsoft, and xAI preceded a report that the White House may be planning to create its own AI vetting system.\\n![Checklist, checking boxes, testing, QA](https://www.cio.com/wp-
content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation (CAISI), a division of the US
Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that would give the agency the ability to vet AI models from these organizations and others prior to their being
made publicly available.\\nAccording to a [release](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) from CAISI, which is part of
the department\\u2019s National Institute of Standards and Technology ([NIST](https://www.csoonline.com/article/4134743/us-dominance-of-agentic-ai-at-the-heart-of-new-nist-initiative.html)), it will
\\u201cconduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI security.\\u201d\\nThe three join Anthropic and OpenAI, which
signed [similar agreements](https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research) almost two years ago during the Biden administration,
when CAISI was known as the US Artificial Intelligence Safety Institute.\\nAn August 2024 release about those agreements indicated that the institute planned to provide feedback to both companies on
\\u201cpotential safety improvements to their models, in close collaboration with its partners at the UK AI Safety Institute (AISI).\\u201d\\nMicrosoft said Tuesday in a
[blog](https://blogs.microsoft.com/on-the-issues/2026/05/05/advancing-ai-evaluation-with-the-center-for-ai-standards-us-and-innovation-and-the-ai-security-institute-uk/) about the latest agreement
that it, and others like it, are essential to building trust and confidenc\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/ed1d0f300aec.txt]\"}, {\"title\": \"CAISI Signs Frontier AI Testing Agreements With Google DeepMind, Microsoft, and xAI: What You Need to
Know | Knowledge Hub Media\", \"url\": \"https://knowledgehubmedia.com/caisi-signs-frontier-ai-testing-agreements-with-google-deepmind-microsoft-and-xai-what-you-need-to-know/\", \"snippet\": \"![The
words Innovation Explained with the ai underlined on gradient background with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node
pattern.](https://knowledgehubmedia.com/wp-content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the
Department of Commerce\\u2019s National Institute of Standards and Technology (NIST). It serves as the U.S. g\", \"api_data\": null, \"hint\": null, \"text\": \"![The words Innovation Explained with
the ai underlined on gradient background with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node
pattern.](https://knowledgehubmedia.com/wp-content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the
Department of Commerce\\u2019s National Institute of Standards and Technology (NIST). It serves as the U.S. government\\u2019s primary point of contact for the AI industry, facilitating voluntary
testing, collaborative research, and the development of best practices for commercial AI systems. On May 5, 2026, CAISI announced new agreements with three major AI developers, Google DeepMind,
Microsoft, and xAI, to conduct pre-deployment evaluations and targeted research on their frontier AI models.\\nIn this article, we\\u2019ll discuss what these new agreements mean for the future of AI
oversight in the United States, how they build on earlier partnerships with companies like Anthropic and OpenAI, and why the involvement of an interagency taskforce adds a new layer of depth to the
government\\u2019s approach to AI security. We\\u2019ll also look at CAISI\\u2019s origins, its evolving mission, and what this development signals for the broader AI industry.\\nTL;DR
Snapshot\\nUnder the new agreements, Google DeepMind, Microsoft, and xAI will provide their frontier AI models to CAISI for government evaluation before public release. The arrangement also covers
post-deployment assessments and ongoing research. According to [NIST\\u2019s official announcement](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-
security-testing), CAISI has already completed more than 40 such evaluations, including on state-of-the-art models that have never been released to the public.\\nKey takeaways include\\u2026\\n-
Expanded government access: AI developers will frequently hand over versions of their models wit\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/9a249c95f70f.txt]\"}], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [],
\"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Now let me check for any recent August 2026 developments.

## 🔧 Tool: mcp__search__search


## 🔧 Tool: mcp__search__search


```json
{
  "query": "CAISI new agreement August 2026 frontier AI testing announcement",
  "lanes": [
    "web"
  ],
  "limit": 4
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"CAISI new agreement August 2026 frontier AI testing announcement\", \"lanes_run\": [\"web\"], \"web\": [{\"title\": \"NIST's CAISI Announces New Frontier AI
Testing Agreements with Google DeepMind, Microsoft, xAI - HPCwire\", \"url\": \"https://www.hpcwire.com/off-the-wire/nists-caisi-announces-new-frontier-ai-testing-agreements-with-google-deepmind-
microsoft-xai/\", \"snippet\": \"NIST\\u2019s CAISI Announces New Frontier AI Testing Agreements with Google DeepMind, Microsoft, xAI\\nMay 5, 2026\\nShares\\nWASHINGTON, May 5, 2026 \\u2014 Today,
the Center for AI Standards and Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology announced new agreements with Google DeepMind, Microsoft and
xAI. Through these expanded industry collaborations, CAISI will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities\", \"api_data\": null, \"hint\":
null, \"text\": \"NIST\\u2019s CAISI Announces New Frontier AI Testing Agreements with Google DeepMind, Microsoft, xAI\\nMay 5, 2026\\nShares\\nWASHINGTON, May 5, 2026 \\u2014 Today, the Center for AI
Standards and Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology announced new agreements with Google DeepMind, Microsoft and xAI. Through these
expanded industry collaborations, CAISI will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI security. These agreements
build on previously announced partnerships, which have been renegotiated to reflect CAISI\\u2019s directives from the secretary of commerce and America\\u2019s AI Action Plan.\\nCredit:
Grandbrothers/Shutterstock\\nUnder the direction of Secretary Howard Lutnick, CAISI has been designated to serve as industry\\u2019s primary point of contact within the U.S. government to facilitate
testing, collaborative research and best practice development related to commercial AI systems.\\nCAISI\\u2019s agreements with frontier AI developers enable government evaluation of AI models before
they are publicly available, as well as post-deployment assessment and other research. To date, CAISI has completed more than 40 such evaluations, including on state-of-the-art models that remain
unreleased.\\n\\u201cIndependent, rigorous measurement science is essential to understanding frontier AI and its national security implications,\\u201d said CAISI Director Chris Fall. \\u201cThese
expanded industry collaborations help us scale our work in the public interest at a critical moment.\\u201d\\nThese agreements support information-sharing, driving voluntary product improvements and
ensuring a clear understanding in government of AI capabilities and the state of international AI competition. To thoroughly evaluate national security-related capabilities and risks, developers
frequently provide CAISI with models that have reduced or removed safeguards. Evaluators from across government may participate in\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/1e066ce34068.txt]\"}, {\"title\": \"CAISI expands frontier AI testing with Google DeepMind, Microsoft and xAI | Digital Watch
Observatory\", \"url\": \"https://dig.watch/updates/caisi-frontier-ai-testing-agreements\", \"snippet\": \"CAISI expands frontier AI testing with Google DeepMind, Microsoft and xAI\\nNew CAISI
agreements will support pre-deployment AI testing, post-deployment assessments and targeted security research.\\nThe Center for AI Standards and Innovation (CAISI), part of the US National Institute
of Standards and Technology (NIST), has [announced new agreements](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) with Google
DeepMind, Microsoft, a\", \"api_data\": null, \"hint\": null, \"text\": \"CAISI expands frontier AI testing with Google DeepMind, Microsoft and xAI\\nNew CAISI agreements will support pre-deployment
AI testing, post-deployment assessments and targeted security research.\\nThe Center for AI Standards and Innovation (CAISI), part of the US National Institute of Standards and Technology (NIST), has
[announced new agreements](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) with Google DeepMind, Microsoft, and xAI to expand
government evaluations of frontier AI models and support research on AI security.\\nAccording to the announcement, the agreements will support pre-deployment evaluations and targeted research intended
to improve understanding of frontier AI capabilities and their national security implications.\\n[CAISI](https://dig.watch/updates/deepseek-v4-pro-caisi-us-nist-evaluation) says the updated
arrangements build on earlier partnerships that were renegotiated to reflect directives from the Secretary of Commerce and the US [AI Action Plan](https://dig.watch/updates/white-house-launches-ai-
action-plan-with-executive-orders-on-exports-and-regulation).\\nCAISI also says it has been designated to serve as the main point of contact within the [US](https://dig.watch/countries/united-states-
of-america) government for collaboration with industry on testing, joint research, and best-practice development for commercial AI systems. To date, it says it has completed more than 40 evaluations,
including assessments of advanced unreleased models.\\nCAISI Director Chris Fall said independent and rigorous measurement is essential to understanding frontier AI and its national security
implications. The announcement adds that the agreements are intended to support information-sharing, voluntary product improvements, and a clearer government understanding of AI capabilities and
international AI competition.\\nThe agency notes that developers often provide models with reduced or removed safeguards\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/3f1b326ba5b9.txt]\"}, {\"title\": \"CAISI Signs Frontier AI Testing Agreements With Google DeepMind, Microsoft, and xAI: What You Need to
Know | Knowledge Hub Media\", \"url\": \"https://knowledgehubmedia.com/caisi-signs-frontier-ai-testing-agreements-with-google-deepmind-microsoft-and-xai-what-you-need-to-know/\", \"snippet\": \"![The
words Innovation Explained with the ai underlined on gradient background with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node
pattern.](https://knowledgehubmedia.com/wp-content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the
Department of Commerce\\u2019s National Institute of Standards and Technology (NIST). It serves as the U.S. g\", \"api_data\": null, \"hint\": null, \"text\": \"![The words Innovation Explained with
the ai underlined on gradient background with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node
pattern.](https://knowledgehubmedia.com/wp-content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the
Department of Commerce\\u2019s National Institute of Standards and Technology (NIST). It serves as the U.S. government\\u2019s primary point of contact for the AI industry, facilitating voluntary
testing, collaborative research, and the development of best practices for commercial AI systems. On May 5, 2026, CAISI announced new agreements with three major AI developers, Google DeepMind,
Microsoft, and xAI, to conduct pre-deployment evaluations and targeted research on their frontier AI models.\\nIn this article, we\\u2019ll discuss what these new agreements mean for the future of AI
oversight in the United States, how they build on earlier partnerships with companies like Anthropic and OpenAI, and why the involvement of an interagency taskforce adds a new layer of depth to the
government\\u2019s approach to AI security. We\\u2019ll also look at CAISI\\u2019s origins, its evolving mission, and what this development signals for the broader AI industry.\\nTL;DR
Snapshot\\nUnder the new agreements, Google DeepMind, Microsoft, and xAI will provide their frontier AI models to CAISI for government evaluation before public release. The arrangement also covers
post-deployment assessments and ongoing research. According to [NIST\\u2019s official announcement](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-
security-testing), CAISI has already completed more than 40 such evaluations, including on state-of-the-art models that have never been released to the public.\\nKey takeaways include\\u2026\\n-
Expanded government access: AI developers will frequently hand over versions of their models wit\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/9a249c95f70f.txt]\"}, {\"title\": \"US government agency to safety test frontier AI models before release | CIO\", \"url\":
\"https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-before-release.html\", \"snippet\": \"CAISI\\u2019s agreements with Google, Microsoft, and xAI preceded a
report that the White House may be planning to create its own AI vetting system.\\n![Checklist, checking boxes, testing, QA](https://www.cio.com/wp-
content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation (CAISI), a division of the US
Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that wo\", \"api_data\": null, \"hint\": null, \"text\": \"CAISI\\u2019s agreements with Google, Microsoft, and
xAI preceded a report that the White House may be planning to create its own AI vetting system.\\n![Checklist, checking boxes, testing, QA](https://www.cio.com/wp-
content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation (CAISI), a division of the US
Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that would give the agency the ability to vet AI models from these organizations and others prior to their being
made publicly available.\\nAccording to a [release](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) from CAISI, which is part of
the department\\u2019s National Institute of Standards and Technology ([NIST](https://www.csoonline.com/article/4134743/us-dominance-of-agentic-ai-at-the-heart-of-new-nist-initiative.html)), it will
\\u201cconduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI security.\\u201d\\nThe three join Anthropic and OpenAI, which
signed [similar agreements](https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research) almost two years ago during the Biden administration,
when CAISI was known as the US Artificial Intelligence Safety Institute.\\nAn August 2024 release about those agreements indicated that the institute planned to provide feedback to both companies on
\\u201cpotential safety improvements to their models, in close collaboration with its partners at the UK AI Safety Institute (AISI).\\u201d\\nMicrosoft said Tuesday in a
[blog](https://blogs.microsoft.com/on-the-issues/2026/05/05/advancing-ai-evaluation-with-the-center-for-ai-standards-us-and-innovation-and-the-ai-security-institute-uk/) about the latest agreement
that it, and others like it, are essential to building trust and confidenc\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/ed1d0f300aec.txt]\"}], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [],
\"social\": [], \"failed\": []}"}]
```

```json
{
  "query": "OpenAI Anthropic federal government model evaluation agreement August 2026",
  "lanes": [
    "news"
  ],
  "limit": 6
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"OpenAI Anthropic federal government model evaluation agreement August 2026\", \"lanes_run\": [], \"web\": [], \"markets\": [], \"news\": [], \"metaculus\": [],
\"papers\": [], \"series\": [], \"reference\": [], \"neural\": [], \"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Key finding: the May 5 announcement already noted OpenAI/Anthropic partnerships "have been renegotiated." Let me check the NIST news feed for anything in the Aug 10–Sep 3 window.

## 🔧 Tool: mcp__search__fetch


## 🔧 Tool: mcp__search__search


```json
{
  "ref": "https://www.nist.gov/news-events/news/2026/08",
  "prompt": "List all NIST news items from August 2026, especially any about CAISI, AI agreements, OpenAI, or Anthropic. Include dates and titles."
}
```

### 📋 Result

```
HTTP 404 for https://www.nist.gov/news-events/news/2026/08. The URL may have changed. Try WebSearch to find the current URL.
```

```json
{
  "query": "NIST CAISI news August 2026 OpenAI Anthropic agreement expanded evaluation",
  "limit": 6
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"NIST CAISI news August 2026 OpenAI Anthropic agreement expanded evaluation\", \"lanes_run\": [\"web\", \"markets\", \"metaculus\", \"papers\", \"series\",
\"reference\", \"neural\"], \"web\": [{\"title\": \"CAISI Signs Frontier AI Testing Agreements With Google DeepMind, Microsoft, and xAI: What You Need to Know | Knowledge Hub Media\", \"url\":
\"https://knowledgehubmedia.com/caisi-signs-frontier-ai-testing-agreements-with-google-deepmind-microsoft-and-xai-what-you-need-to-know/\", \"snippet\": \"![The words Innovation Explained with the ai
underlined on gradient background with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node pattern.](https://knowledgehubmedia.com/wp-
content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the Department of Commerce\\u2019s National
Institute of Standards and Technology (NIST). It serves as the U.S. g\", \"api_data\": null, \"hint\": null, \"text\": \"![The words Innovation Explained with the ai underlined on gradient background
with a data node pattern.The words Innovation Explained with the ai underlined on gradient background with a data node pattern.](https://knowledgehubmedia.com/wp-
content/uploads/2026/03/InnovationExplainedBannerImage-1024x372.jpg)\\nThe Center for AI Standards and Innovation (CAISI) is a federal body housed within the Department of Commerce\\u2019s National
Institute of Standards and Technology (NIST). It serves as the U.S. government\\u2019s primary point of contact for the AI industry, facilitating voluntary testing, collaborative research, and the
development of best practices for commercial AI systems. On May 5, 2026, CAISI announced new agreements with three major AI developers, Google DeepMind, Microsoft, and xAI, to conduct pre-deployment
evaluations and targeted research on their frontier AI models.\\nIn this article, we\\u2019ll discuss what these new agreements mean for the future of AI oversight in the United States, how they build
on earlier partnerships with companies like Anthropic and OpenAI, and why the involvement of an interagency taskforce adds a new layer of depth to the government\\u2019s approach to AI security.
We\\u2019ll also look at CAISI\\u2019s origins, its evolving mission, and what this development signals for the broader AI industry.\\nTL;DR Snapshot\\nUnder the new agreements, Google DeepMind,
Microsoft, and xAI will provide their frontier AI models to CAISI for government evaluation before public release. The arrangement also covers post-deployment assessments and ongoing research.
According to [NIST\\u2019s official announcement](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing), CAISI has already completed
more than 40 such evaluations, including on state-of-the-art models that have never been released to the public.\\nKey takeaways include\\u2026\\n- Expanded government access: AI developers will
frequently hand over versions of their models wit\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/9a249c95f70f.txt]\"},
{\"title\": \"US government agency to safety test frontier AI models before release | CIO\", \"url\": \"https://www.cio.com/article/4168122/us-government-agency-to-safety-test-frontier-ai-models-
before-release.html\", \"snippet\": \"CAISI\\u2019s agreements with Google, Microsoft, and xAI preceded a report that the White House may be planning to create its own AI vetting
system.\\n![Checklist, checking boxes, testing, QA](https://www.cio.com/wp-
content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation (CAISI), a division of the US
Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that wo\", \"api_data\": null, \"hint\": null, \"text\": \"CAISI\\u2019s agreements with Google, Microsoft, and
xAI preceded a report that the White House may be planning to create its own AI vetting system.\\n![Checklist, checking boxes, testing, QA](https://www.cio.com/wp-
content/uploads/2026/05/4168122-0-40719900-1778121780-shutterstock_201256211-100963008-orig.jpg?quality=50&strip=all&w=1024)\\nThe Center for AI Standards and Innovation (CAISI), a division of the US
Department of Commerce, has signed agreements with Google DeepMind, Microsoft, and xAI that would give the agency the ability to vet AI models from these organizations and others prior to their being
made publicly available.\\nAccording to a [release](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) from CAISI, which is part of
the department\\u2019s National Institute of Standards and Technology ([NIST](https://www.csoonline.com/article/4134743/us-dominance-of-agentic-ai-at-the-heart-of-new-nist-initiative.html)), it will
\\u201cconduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI security.\\u201d\\nThe three join Anthropic and OpenAI, which
signed [similar agreements](https://www.nist.gov/news-events/news/2024/08/us-ai-safety-institute-signs-agreements-regarding-ai-safety-research) almost two years ago during the Biden administration,
when CAISI was known as the US Artificial Intelligence Safety Institute.\\nAn August 2024 release about those agreements indicated that the institute planned to provide feedback to both companies on
\\u201cpotential safety improvements to their models, in close collaboration with its partners at the UK AI Safety Institute (AISI).\\u201d\\nMicrosoft said Tuesday in a
[blog](https://blogs.microsoft.com/on-the-issues/2026/05/05/advancing-ai-evaluation-with-the-center-for-ai-standards-us-and-innovation-and-the-ai-security-institute-uk/) about the latest agreement
that it, and others like it, are essential to building trust and confidenc\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/ed1d0f300aec.txt]\"}, {\"title\": \"Microsoft, Google, xAI giving government early access to AI models for review\", \"url\":
\"https://thehill.com/homenews/5863937-google-microsoft-xai-ai-testing/\", \"snippet\": null, \"api_data\": null, \"hint\": null, \"text\": null}, {\"title\": \"Major U.S. AI Labs Now Subject to Pre-
Release Government Security Reviews\", \"url\": \"https://www.secureworld.io/industry-news/us-ai-labs-government-security-reviews\", \"snippet\": \"The U.S. government has quietly secured something
the AI industry has resisted for years: a seat at the table before models ship. The Commerce Department's Center for AI Standards and Innovation (CAISI) [announced Tuesday](https://www.nist.gov/news-
events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) that Google DeepMind, Microsoft, and Elon Musk's xAI have agreed to provide access to unreleased versions of
their AI models for pre-deployment security and ca\", \"api_data\": null, \"hint\": null, \"text\": \"The U.S. government has quietly secured something the AI industry has resisted for years: a seat
at the table before models ship. The Commerce Department's Center for AI Standards and Innovation (CAISI) [announced Tuesday](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-
regarding-frontier-ai-national-security-testing) that Google DeepMind, Microsoft, and Elon Musk's xAI have agreed to provide access to unreleased versions of their AI models for pre-deployment
security and capability evaluations, [Reuters ](https://www.reuters.com/legal/litigation/microsoft-xai-google-will-share-ai-models-with-us-govt-security-reviews-2026-05-05/)and [Bloomberg
](https://www.bloomberg.com/news/articles/2026-05-05/ai-firms-agree-to-give-us-early-access-to-evaluate-their-models)first reported. Combined with existing\\u2014and recently
renegotiated\\u2014agreements from Anthropic and OpenAI, every major U.S. frontier AI lab now participates in voluntary pre-release government evaluations.\\nCAISI has completed more than 40 model
assessments to date, including evaluations of unreleased state-of-the-art systems. Notably, developers sometimes hand over versions of their models with safety guardrails reduced specifically so the
Center can probe for national security risks. The announcements arrived one day after [The New York Times](https://www.nytimes.com/2026/05/04/opinion/ai-national-security-risk-politics.html) first
reported that the Trump Administration was weighing a separate mandatory pre-release review process via Executive Order\\u2014with Anthropic's Mythos model cited as the catalyst. The voluntary
agreements and any mandatory framework would run in parallel, though their interaction remains undefined.\\nThe timing is deliberate, even if the policy mechanics are still being sorted. After years
of self-regulation and voluntary safety commitments that lacked teeth, the U.S. government is establishing a consistent pre-deployment review process for the world's most powerful AI system\\n\\n[...
continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/eb5868629279.txt]\"}, {\"title\": \"Center for AI Standards and Innovation (CAISI) |
NIST\", \"url\": \"https://www.nist.gov/caisi\", \"snippet\": \"The Center for AI Standards and Innovation (CAISI) will serve as industry\\u2019s primary point of contact within the U.S. government to
facilitate testing and collaborative research related to harnessing and securing the potential of commercial AI systems. To that end, CAISI will:\\n[Read the
statement](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai) from Secretary of Commerce Howard Lutnick about the Center for AI
Standards and In\", \"api_data\": null, \"hint\": null, \"text\": \"The Center for AI Standards and Innovation (CAISI) will serve as industry\\u2019s primary point of contact within the U.S.
government to facilitate testing and collaborative research related to harnessing and securing the potential of commercial AI systems. To that end, CAISI will:\\n[Read the
statement](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai) from Secretary of Commerce Howard Lutnick about the Center for AI
Standards and Innovation.\"}, {\"title\": \"Commerce AI center will evaluate Google Deepmind, Microsoft and xAI models - Nextgov/FCW\", \"url\": \"https://www.nextgov.com/artificial-
intelligence/2026/05/commerce-ai-center-will-evaluate-google-deepmind-microsoft-and-xai-models/413349/\", \"snippet\": null, \"api_data\": null, \"hint\": null, \"text\": null}], \"markets\":
[{\"market_title\": \"Will Elon Musk visit Mars before Aug 1, 2099?\", \"probability\": 0.11, \"volume\": 117243.65, \"url\": \"https://kalshi.com/markets/KXELONMARS-99\", \"source\": \"kalshi\",
\"description\": \"If Elon Musk visits Mars before the earlier of his death or Aug 1, 2099, then the market resolves to Yes.\", \"market_id\": \"KXELONMARS-99\", \"recent_history\": null},
{\"market_title\": \"Will Klaus Iohannis be the next Secretary General of NATO?\", \"probability\": 0.14, \"volume\": 257.0, \"url\": \"https://kalshi.com/markets/KXNEXTNATOSECGEN-99-KIOH\",
\"source\": \"kalshi\", \"description\": \"If Klaus Iohannis formally holds the position of Secretary General of NATO, and is the first such subject to do so after Issuance, then the market resolves
to Yes.\", \"market_id\": \"KXNEXTNATOSECGEN-99-KIOH\", \"recent_history\": null}, {\"market_title\": \"Will Kaja Kallas be the next Secretary General of NATO?\", \"probability\": 0.14, \"volume\":
1337.81, \"url\": \"https://kalshi.com/markets/KXNEXTNATOSECGEN-99-KKAL\", \"source\": \"kalshi\", \"description\": \"If Kaja Kallas formally holds the position of Secretary General of NATO, and is
the first such subject to do so after Issuance, then the market resolves to Yes.\", \"market_id\": \"KXNEXTNATOSECGEN-99-KKAL\", \"recent_history\": null}, {\"market_title\": \"Will Ben Wallace be the
next Secretary General of NATO?\", \"probability\": 0.09, \"volume\": 896.0, \"url\": \"https://kalshi.com/markets/KXNEXTNATOSECGEN-99-BWAL\", \"source\": \"kalshi\", \"description\": \"If Ben Wallace
formally holds the position of Secretary General of NATO, and is the first such subject to do so after Issuance, then the market resolves to Yes.\", \"market_id\": \"KXNEXTNATOSECGEN-99-BWAL\",
\"recent_history\": null}, {\"market_title\": \"Will Mette Frederiksen be the next Secretary General of NATO?\", \"probability\": 0.06, \"volume\": 521.54, \"url\":
\"https://kalshi.com/markets/KXNEXTNATOSECGEN-99-MFRE\", \"source\": \"kalshi\", \"description\": \"If Mette Frederiksen formally holds the position of Secretary General of NATO, and is the first such
subject to do so after Issuance, then the market resolves to Yes.\", \"market_id\": \"KXNEXTNATOSECGEN-99-MFRE\", \"recent_history\": null}, {\"market_title\": \"Will Ursula von der Leyen be the next
Secretary General of NATO?\", \"probability\": 0.1, \"volume\": 532.84, \"url\": \"https://kalshi.com/markets/KXNEXTNATOSECGEN-99-ULEY\", \"source\": \"kalshi\", \"description\": \"If Ursula von der
Leyen formally holds the position of Secretary General of NATO, and is the first such subject to do so after Issuance, then the market resolves to Yes.\", \"market_id\": \"KXNEXTNATOSECGEN-99-ULEY\",
\"recent_history\": null}], \"news\": [], \"metaculus\": [{\"post_id\": 44708, \"title\": \"Will a U.S. federal agency announce new or expanded model evaluation agreements with both OpenAI and
Anthropic before September 3, 2026?\", \"type\": \"binary\", \"url\": \"https://www.metaculus.com/questions/44708\", \"community_prediction\": null}, {\"post_id\": 45203, \"title\": \"Will a U.S.
federal agency announce new or expanded model evaluation agreements with both OpenAI and Anthropic before September 3, 2026?\", \"type\": \"binary\", \"url\":
\"https://www.metaculus.com/questions/45203\", \"community_prediction\": null}, {\"post_id\": 31688, \"title\": \"Will any frontier model be released in 2029 without a third-party evaluation of
dangerous capabilities?\", \"type\": \"binary\", \"url\": \"https://www.metaculus.com/questions/31688\", \"community_prediction\": null}, {\"post_id\": 17728, \"title\": \"Will OpenAI announce that it
has solved the core technical challenges of superintelligence alignment by June 30, 2027?\", \"type\": \"binary\", \"url\": \"https://www.metaculus.com/questions/17728\", \"community_prediction\":
null}, {\"post_id\": 43731, \"title\": \"Will OpenAI or Anthropic have a higher valuation on January 1, 2027?\", \"type\": \"multiple_choice\", \"url\": \"https://www.metaculus.com/questions/43731\",
\"community_prediction\": null}, {\"post_id\": 15615, \"title\": \"Will global-catastrophic-risk-focused evaluation of certain AI systems by accredited bodies become mandatory in the US before
2035?\", \"type\": \"binary\", \"url\": \"https://www.metaculus.com/questions/15615\", \"community_prediction\": null}], \"papers\": [{\"id\": \"http://arxiv.org/abs/1808.00177v5\", \"title\":
\"Learning Dexterous In-Hand Manipulation\", \"summary\": \"We use reinforcement learning (RL) to learn dexterous in-hand manipulation policies which can perform vision-based object reorientation on a
physical Shadow Dexterous Hand. The training is performed in a simulated environment in which we randomize many of the physical properties of the system like friction coefficients and an object's
appearance. Our policies transfer to the physical robot despite being trained entirely in simulation. Our method does not rely on any human demonstrations, but many behaviors found in human
manipulation emerge naturally, including finger gaiting, multi-finger coordination, and the controlled use of gravity. Our results were obtained using the same distributed RL system that was used to
train OpenAI Five. We also include a video of our results: https://youtu.be/jwSbzNHGflM\", \"authors\": [\"OpenAI\", \"Marcin Andrychowicz\", \"Bowen Baker\", \"Maciek Chociej\", \"Rafal Jozefowicz\",
\"Bob McGrew\", \"Jakub Pachocki\", \"Arthur Petron\", \"Matthias Plappert\", \"Glenn Powell\", \"Alex Ray\", \"Jonas Schneider\", \"Szymon Sidor\", \"Josh Tobin\", \"Peter Welinder\", \"Lilian
Weng\", \"Wojciech Zaremba\"], \"published\": \"2018-08-01\", \"updated\": \"2019-01-18\", \"categories\": [\"cs.LG\", \"cs.AI\", \"cs.RO\", \"stat.ML\"], \"primary_category\": \"cs.LG\", \"pdf_url\":
\"https://arxiv.org/pdf/1808.00177v5\"}, {\"id\": \"http://arxiv.org/abs/2510.00952v2\", \"title\": \"CL-UZH submission to the NIST SRE 2024 Speaker Recognition Evaluation\", \"summary\": \"The CL-UZH
team submitted one system each for the fixed and open conditions of the NIST SRE 2024 challenge. For the closed-set condition, results for the audio-only trials were achieved using the X-vector system
developed with Kaldi. For the audio-visual results we used only models developed for the visual modality. Two sets of results were submitted for the open-set and closed-set conditions, one based on a
pretrained model using the VoxBlink2 and VoxCeleb2 datasets. An Xvector-based model was trained from scratch using the CTS superset dataset for the closed set. In addition to the submission of the
results of the SRE24 evaluation to the competition website, we talked about the performance of the proposed systems on the SRE24 evaluation in this report.\", \"authors\": [\"Aref Farhadipour\",
\"Shiran Liu\", \"Masoumeh Chapariniya\", \"Valeriia Vyshnevetska\", \"Srikanth Madikeri\", \"Teodora Vukovic\", \"Volker Dellwo\"], \"published\": \"2025-10-01\", \"updated\": \"2025-10-07\",
\"categories\": [\"eess.AS\", \"cs.SD\"], \"primary_category\": \"eess.AS\", \"pdf_url\": \"https://arxiv.org/pdf/2510.00952v2\"}, {\"id\": \"http://arxiv.org/abs/2607.03399v1\", \"title\": \"Second
MOASEI Competition at AAMAS'2026: A Technical Report\", \"summary\": \"We describe the 2026 Methods for Open Agent Systems Evaluation Initiative (MOASEI) Competition, a benchmark event for evaluating
multi-agent decision-making under open-system conditions. Building on the inaugural 2025 competition, the 2026 edition retained wildfire fighting, cybersecurity, and ride-sharing domains while adding
a bonus wildfire track with frame openness, in which agent equipment states such as suppressant capacities and firefighting range vary over time. The competition also expanded its reporting metrics to
emphasize total task completions, mean task-completion time, and mean value of completed tasks. Participation in 2026 was limited: eight teams registered, but only one team submitted a final entry,
and that entry targeted the ride-sharing track. The submitted DLC approach used planning and replanning to solve routing problems across agents as passengers appeared. This report summarizes the 2026
competition design, highlights differences from the previous year, and reports ride-sharing evaluation results against baseline policies. DLC is recognized as the 2026 ride-sharing track winner among
submitted teams.\", \"authors\": [\"Ceferino Patino\", \"Tyler J. Billings\", \"Alireza Saleh Abadi\", \"Daniel Redder\", \"Adam Eck\", \"Prashant Doshi\", \"Leen-Kiat Soh\"], \"published\":
\"2026-07-03\", \"updated\": \"2026-07-03\", \"categories\": [\"cs.MA\"], \"primary_category\": \"cs.MA\", \"pdf_url\": \"https://arxiv.org/pdf/2607.03399v1\"}, {\"id\":
\"http://arxiv.org/abs/2607.01063v1\", \"title\": \"AutoRestTest at the SBFT 2026 Tool Competition\", \"summary\": \"Large input spaces and complex inter-operation dependencies make black-box REST API
testing challenging. AutoRestTest combines a Semantic Property Dependency Graph, multi-agent reinforcement learning, and large language models to intelligently explore large API input spaces. In the
SBFT 2026 REST League, AutoRestTest ranked first in all three evaluation categories -- fault detection, overall efficiency, and overall effectiveness -- on 11 APIs (317 operations, approximately 29
per API), averaging 67.09 unique server errors and 17.27 successfully processed operations per API under a one-hour testing budget.\", \"authors\": [\"Tyler Stennett\", \"Myeongsoo Kim\", \"Saurabh
Sinha\", \"Alessandro Orso\"], \"published\": \"2026-07-01\", \"updated\": \"2026-07-01\", \"categories\": [\"cs.SE\"], \"primary_category\": \"cs.SE\", \"pdf_url\":
\"https://arxiv.org/pdf/2607.01063v1\"}, {\"id\": \"http://arxiv.org/abs/2601.07237v1\", \"title\": \"The ICASSP 2026 Automatic Song Aesthetics Evaluation Challenge\", \"summary\": \"This paper
summarizes the ICASSP 2026 Automatic Song Aesthetics Evaluation (ASAE) Challenge, which focuses on predicting the subjective aesthetic scores of AI-generated songs. The challenge consists of two
tracks: Track 1 targets the prediction of the overall musicality score, while Track 2 focuses on predicting five fine-grained aesthetic scores. The challenge attracted strong interest from the
research community and received numerous submissions from both academia and industry. Top-performing systems significantly surpassed the official baseline, demonstrating substantial progress in
aligning objective metrics with human aesthetic preferences. The outcomes establish a standardized benchmark and advance human-aligned evaluation methodologies for modern music generation systems.\",
\"authors\": [\"Guobin Ma\", \"Yuxuan Xia\", \"Jixun Yao\", \"Huixin Xue\", \"Hexin Liu\", \"Shuai Wang\", \"Hao Liu\", \"Lei Xie\"], \"published\": \"2026-01-12\", \"updated\": \"2026-01-12\",
\"categories\": [\"eess.AS\", \"cs.SD\"], \"primary_category\": \"eess.AS\", \"pdf_url\": \"https://arxiv.org/pdf/2601.07237v1\"}, {\"id\": \"http://arxiv.org/abs/2607.00787v1\", \"title\": \"In
Memoriam: Igal Talmi (1925-2026)\", \"summary\": \"A brief obituary of Igal Talmi (1925-2026) focusing on his scientific heritage. Published in Nuclear Physics News 36 (2026) 39-40.\", \"authors\":
[\"Amiram Leviatan\", \"Avraham Gal\"], \"published\": \"2026-07-01\", \"updated\": \"2026-07-01\", \"categories\": [\"physics.hist-ph\", \"nucl-ex\", \"nucl-th\"], \"primary_category\":
\"physics.hist-ph\", \"pdf_url\": \"https://arxiv.org/pdf/2607.00787v1\"}], \"series\": [], \"reference\": [{\"title\": \"Artificial intelligence safety institute\", \"snippet\": \"UK&#039;s AI Safety
Institute was renamed the &quot;AI Security Institute&quot;, and its US counterpart became the Center for AI Standards and Innovation (CAISI). In\", \"url\":
\"https://en.wikipedia.org/wiki/Artificial_intelligence_safety_institute\", \"word_count\": 2520}, {\"title\": \"Regulation of artificial intelligence in the United States\", \"snippet\": \"2026,
Anthropic, Google, Microsoft, and OpenAI had established AI model review agreements with CAISI. In August 2025, Silicon Valley companies and investors\", \"url\":
\"https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence_in_the_United_States\", \"word_count\": 5837}, {\"title\": \"Regulation of artificial intelligence\", \"snippet\": \"Safety
Institute (CAISI) as part of a 2.4 billion CAD federal AI investment package. This includes 2 billion CAD to support a new AI Sovereign Computing\", \"url\":
\"https://en.wikipedia.org/wiki/Regulation_of_artificial_intelligence\", \"word_count\": 17744}], \"neural\": [{\"title\": \"CAISI Signs Agreements Regarding Frontier AI National Security Testing With
Google DeepMind, Microsoft and xAI | NIST\", \"url\": \"https://web.archive.org/web/20260505134747/https:/www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-
security-testing\", \"snippet\": \"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI | NIST\\n\\n05 May 2026 - 24 Jul 2026\\n\\n| Apr | MAY
| Jun |\\n| --- | --- | --- |\\n| | 05 | |\\n| 2025 | 2026 | 2027 |\\n\\nsuccess\\n\\nfail\\n\\nSign In Get some help using the Wayback Machine\\n\\nAbout this capture\\n\\nCOLLECTED
BY\\n\\nTIMESTAMPS\\n\\nThe Wayback Machine - https://web.archive.org/web/20260505134747/https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-secu\",
\"highlights\": [\"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI | NIST\\n...\\n# CAISI Signs Agreements Regarding Frontier AI National
Security Testing With Google DeepMind, Microsoft and xAI\\n...\\n### Expanded collaborations with leading U.S. AI labs provide for pre-deployment evaluations and other research.\\n...\\nMay 5,
2026\\n...\\nWASHINGTON \\u2014 Today, the Center for AI Standards and Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology announced new agreements
with Google DeepMind, Microsoft and xAI. Through these expanded industry collaborations, CAISI will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities
and advance the state of AI security. These agreements build on previously announced partnerships, which have been renegotiated to reflect CAISI\\u2019s directives from the secretary of commerce and
America\\u2019s AI Action Plan.\\n...\\nCAISI\\u2019s agreements with frontier AI developers enable government evaluation of AI models before they are publicly available, as well as post-deployment
assessment and other research. To date, CAISI has completed more than 40 such evaluations, including on state-of-the-art models that remain unreleased.\\n...\\n\\u201cIndependent, rigorous measurement
science is essential to understanding frontier AI and its national security implications,\\u201d said CAISI Director Chris Fall. \\u201cThese expanded industry collaborations help us scale our work in
the public interest at a critical moment.\\u201d\\n...\\nThese agreements support information-sharing, driving voluntary product improvements and ensuring a clear understanding in government of AI
capabilities and the state of international AI competition. To thoroughly evaluate national security-related capabilities and risks, developers frequently provide CAISI with models that have reduced
or removed safeguards. Evaluators from across government may participate in evaluations and regularly provide feedback through the CAISI-convened TRAINS Taskforce, a group of interagency experts
focused on AI national security concerns. The agreements support testing in classified environments and were drafted with the flexibility required to rapidly respond to continued AI
advancements.\\n...\\nReleased May 5, 2026\"], \"published_date\": \"2026-05-05T00:00:00.000\", \"score\": null}, {\"title\": \"CAISI Works with OpenAI and Anthropic to Promote Secure AI Innovation |
NIST\", \"url\": \"https://www.nist.gov/news-events/news/2025/09/caisi-works-openai-and-anthropic-promote-secure-ai-innovation\", \"snippet\": \"CAISI Works with OpenAI and Anthropic to Promote Secure
AI Innovation | NIST\\n\\nhttps://www.nist.gov/news-events/news/2025/09/caisi-works-openai-and-anthropic-promote-secure-ai-innovation\\n\\n# CAISI Works with OpenAI and Anthropic to Promote Secure AI
Innovation\\n\\nSeptember 25, 2025\\n\\n## Share\\n\\nThrough America\\u2019s AI Action Plan, President Trump tasked the Center for AI Standards and Innovation (CAISI) to collaborate with leading
American AI developers in order to actively protect the private sector fro\", \"highlights\": [\"CAISI Works with OpenAI and Anthropic to Promote Secure AI Innovation | NIST\\n...\\n# CAISI Works with
OpenAI and Anthropic to Promote Secure AI Innovation\\n...\\nSeptember 25, 2025\\n...\\nThrough America\\u2019s AI Action Plan, President Trump tasked the Center for AI Standards and Innovation
(CAISI) to collaborate with leading American AI developers in order to actively protect the private sector from AI security risks, including malicious cyber actors. CAISI has assembled a leading group
of scientists with expertise in machine learning and cybersecurity to protect American AI innovations, and has assisted American AI developers in this area for the last year.\\n...\\nMost recently,
CAISI worked with OpenAI and Anthropic to identify security issues with their advanced AI systems and bolster measurement of AI security. OpenAI and Anthropic recently published blog posts describing
concrete security improvements made as a result of CAISI\\u2019s research and evaluations, which were completed in partnership with the UK AI Security Institute. Read the blog posts on the Anthropic
and OpenAI websites.\\n...\\nThe Center for AI Standards and Innovation and the UK AI Security Institute continue to work towards promoting secure AI innovation, including through working towards best
practices in metrology and standards development for AI models and improving understanding of the most advanced model capabilities.\\n...\\n25,\"], \"published_date\": \"2025-09-25T00:00:00.000\",
\"score\": null}, {\"title\": \"Google, Microsoft and xAI\\u2019s frontier AI to face national security testing | CIO Dive\", \"url\": \"https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-
security-testing/819375/\", \"snippet\": \"Google, Microsoft and xAI\\u2019s frontier AI to face national security testing | CIO Dive Skip to main content\\n\\nCONTINUE TO SITE \\u279e\\n\\n# Don't
miss tomorrow's tech industry news\\n\\nLet CIO Dive's free newsletter keep you informed, straight from your inbox.\\n\\nBy signing up to receive our newsletter, you agree to our Terms of Use and
Privacy Policy. You can unsubscribe at anytime.\\n\\nInforma TechTarget |\\n\\nExplore our brands An Informa TechTarget Publication\\n\\n## People also ask\\n\\n- Loading questions...\\n\\nAn artic\",
\"highlights\": [\"# Google, Microsoft and xAI\\u2019s frontier AI to face national security testing\\n...\\nFor CIOs, the expanded testing signals massive risk in choosing unapproved models for
enterprise deployment, The Futurum Group\\u2019s Nick Patience said.\\n...\\n- Add us on Google\\n- The Center for AI Standards and Innovation at the National Institute of Standards and Technology has
entered into agreements with Google DeepMind, Microsoft and xAI to conduct pre-deployment evaluations and research to assess the companies\\u2019 frontier AI capabilities.\\n...\\n- The agreements
build upon previously announced partnerships with OpenAI and Anthropic with a goal of strengthening AI security. Terms of the agreement have been updated to include directives from CAISI, the
Secretary of Commerce and President Donald Trump\\u2019s AI Action Plan from last year.\\n...\\n- The agreement allows the government to evaluate the partnered AI models before they become available
to the public and will continue to assess models after deployment. \\u201cIndependent, rigorous measurement science is essential to understanding frontier AI and its national security
implications,\\u201d said CAISI Director Chris Fall in an announcement. \\u201cThese expanded industry collaborations help us scale our work in the public interest at a critical
moment.\\u201d\\n...\\nAs the primary government point of contact for the tech industry, CAISI and its industry partnerships support information sharing, product improvements and an understanding of
current and future AI capabilities in the U.S. and abroad, NIST said. The partnerships also allow NIST insight into national security capabilities and risks that AI models might provide.\\n...\\nBut
The New York Times reported Monday the administration is seeking to create more regulatory oversight for AI, as policymakers face pressure from national security officials on the risks posed by
powerful AI models, such as Anthropic\\u2019s Mythos. Initiatives such as Project Glasswing, Anthropic\\u2019s effort to identify and remedy software vulnerabilities, further underscore a growing push
to scale governance alongside tech adoption.\\n...\\nThe expansion of the CAISI framework signals that sovereign alignment will be a mandatory metric of AI procurement for enterprises, Nick Patience,
VP and practice lead of AI platforms at The Futurum Group, said in an email to CIO Dive.\\n...\\nIn March, the Department of Defense formally designated Anthropic a security risk, a decision that was
backed by federal judges last month, despite the company\\u2019s partnership with CAISI\\u2019s evaluation process. It proves that a vendor can still be sanctioned if its internal ethics clash with
national security mandates, Patience said.\\n...\\nFor CIOs, the new agreements with Google, Microsoft and xAI are a form of political insurance, Patience said. It\\u2019s a \\u201cmassive contagion
risk\\u201d to choose a vendor that hasn\\u2019t secured favored status from the Department of Commerce and NIST, especially for an enterprise that has or wants federal contracts.\"],
\"published_date\": \"2026-05-05T00:00:00.000\", \"score\": null}, {\"title\": \"Working with US CAISI and UK AISI to build more secure AI systems | OpenAI\", \"url\": \"https://openai.com/index/us-
caisi-uk-aisi-ai-update/\", \"snippet\": \"Working with US CAISI and UK AISI to build more secure AI systems | OpenAI\\n\\nSeptember 12, 2025\\n\\n# Working with US CAISI and UK AISI to build more
secure AI systems\\n\\nAn update on our collaboration with US and UK research and standards bodies for the secure deployment of AI.\\n\\nLoading\\u2026\\n\\nShare\\n\\nWe\\u2019re proud to continue to
push the frontiers of AI capabilities and security. Developing and deploying AI that is secure and useful is core to our mission of ensuring that AGI benefits all of humanity. Key t\", \"highlights\":
[\"Working with US CAISI and UK AISI to build more\\n...\\nWe were among the first companies to enter into voluntary agreements with both the US Center for AI Standards and Innovation (CAISI) and the
UK AI Security Institute (UK AISI). These partnerships reflect our belief that frontier AI development must happen in close collaboration with allied governments that bring deep expertise in machine
learning, national security, and metrology.\\n...\\nFor more than a year, OpenAI has partnered with CAISI to\\n\\nevaluate\\u2060(opens in a new window) OpenAI models\\u2019 capabilities in cyber,
chemical-biological, and other national security-relevant domains. We recently expanded our partnership to include emerging product security challenges and partnered with CAISI to red-team the
security of OpenAI\\u2019s agentic AI systems. In a new kind of collaboration that took place in July, OpenAI worked with CAISI to explore how we can partner with external evaluators to find and fix
security vulnerabilities in agentic systems, such as OpenAI\\u2019s ChatGPT Agent product.\\n...\\nThis collaboration with CAISI was a preliminary step into a new domain of red-teaming agentic
systems. We aim to continue collaboration in this domain, and our work with CAISI builds upon other layers of deployment security efforts including our own internal testing.\\n...\\nThis voluntary
collaboration between OpenAI and CAISI builds on our yearlong research and evaluation collaboration. Finding these vulnerabilities required innovation from CAISI in chaining together multiple exploits
and combining attacks to develop novel ways of compromising AI systems, drawing on methods from both cybersecurity and machine learning. The intersection of AI agent security and traditional
cybersecurity will necessitate building a range of new best practices, and CAISI\\u2019s partnership to improve this aspect of the science of evaluations and the security of AI systems is already
directly benefitting the end users of these systems.\\n...\\nAs part of our ongoing collaboration with UK AISI, in May UK AISI began red-teaming our safeguards against biological misuse (as defined by
OpenAI\\u2019s policies), including the safeguards in both ChatGPT Agent and GPT\\u20115. Rather than tying this to an individual launch, this is an ongoing collaboration to continuously improve the
effectiveness of our safeguards stack.\\n...\\nA rapid feedback loop was central to this work. Starting in May and continuing through the release of ChatGPT Agent in July and GPT\\u20115 in August, UK
AISI and OpenAI teams had frequent ad-hoc meetings which were at around a weekly cadence, including direct collaboration with technical teams to better understand and address specific issues. OpenAI
additionally created specific, custom configurations for testing based on results from UK AISI to enable better testing.\\n...\\nDuring this process, UK AISI found and OpenAI triaged more than a dozen
detailed vulnerability reports. Some of these led to engineering based product fixes, some led to policy enforcement implementation fixes, and some led OpenAI to carry out focused training for
improving certain aspects of our classifiers. For instance: OpenAI improved the robustness of our monitoring stack by improving and measuring it against a set of universal jailbreaks UK AISI
identified against the monitoring systems, which were discovered through both manual red teaming and automated attack techniques. Additionally, the end-to-end testing component proved to be especially
beneficial. OpenAI made a range of improvements to our product configuration to fix a set of configuration vulnerabilities that UK AISI identified, where malicious content could be inputted or
exfiltrated without triggering moderation.\\n...\\n- These collaborations represent some\\n...\\nthe deepest public\\n...\\nprivate collaborations on evaluating real\\n...\\npromising models
for\\n...\\nThe technical expertise in AI and national security that CAISI and UK AISI brought was critical to these collaborations, and led to meaningful improvements to our safeguards and product
security. Close technical partnerships with organizations that have both the resources and incentives to rigorously evaluate AI systems strengthen confidence in the security of our systems.\"],
\"published_date\": null, \"score\": null}, {\"title\": \"White House Invites AI Labs That Breached Companies to Write Their Own Safety Rules\", \"url\":
\"https://www.techtimes.com/articles/323048/20260804/white-house-invites-ai-labs-that-breached-companies-write-their-own-safety-rules.htm\", \"snippet\": \"White House Invites AI Labs That Breached
Companies to Write Their Own Safety Rules\\n\\nUS President Donald Trump reacts and gestures during a bilateral meeting with India's Prime Minister as part of the G7 summit, in Evian, eastern France,
on June 17, 2026. Mandel NGAN/AFP via Getty Images\\n\\nFour of the largest US AI laboratories \\u2014 whose autonomous agents collectively breached five real organizations during internal evaluations
across a span of weeks \\u2014 are scheduled to meet White House officials Tu\", \"highlights\": [\"What the meeting will address is implementation \\u2014 how companies submit models, what the 30-day
pre-release window looks like in practice, and what information changes hands between labs and the Center for AI Standards and Innovation (CAISI), the Commerce Department body that the administration
expects to lead most evaluations. CAISI, the Commerce Department body renamed from the AI Safety Institute, has already formalized pre-release evaluation agreements with multiple frontier
labs.\\n...\\nOpenAI has already staked out a position on that last question. In the lead-up to Tuesday's meeting, the company asked the Trump administration to place CAISI \\u2014 not the NSA, which
EO 14409 assigns benchmark authority \\u2014 at the center of the testing process. The request is notable because CAISI is the same body that, under the prior administration as the US AI Safety
Institute, already had pre-release access agreements with OpenAI and Anthropic. A company lobbying for which government body regulates it is a structurally distinct posture from a company simply
complying with whatever body Congress or the executive assigns.\\n...\\n's meeting noted\\n...\\nadministration's approach to\\n...\\nconfusion\\\": the Pentagon blacklisted a\\n...\\nthat then
returned to the table on\\n...\\nsafety governance \\u2014 at the same administration\\n...\\ncomment. Meta confirmed\\n...\\nspokesperson. OpenAI pointed\\n...\\ncalling the framework \\\"an
important step toward\\n...\\nTen days after OpenAI's disclosure,\\n...\\nproblem. After reviewing\\n...\\n41,006 evaluation runs prompted by OpenAI's disclosure, Anthropic\\n...\\nthree incidents it
had not previously known about, involving six individual evaluation runs across\\n...\\nnamed models \\u2014 Claude Opus 4.7, Mythos 5, and an internal research model \\u2014 and three real
organizations whose infrastructure was compromised, two of which had detected nothing unusual before Anthropic reached out on July 27.\\n...\\nThe voluntary framework finalized under EO 14409 will
give the federal government a 30-day pre-release window to access frontier models before public release. The reviewing bodies are CAISI and the NSA. Participation is explicitly not mandatory. The
benchmark criteria will remain classified. A developer could cross the threshold without advance warning, since no capability level is published in advance. The EO 14409 framework's structural limits
have been analyzed extensively since its August 1 finalization.\\n...\\nThe Export Control Reform Act gives the Commerce Department independent authority to restrict AI models classified as emerging
technologies essential to national security \\u2014 without invoking EO 14409 and without a published threshold. That authority has already been invoked twice: against Anthropic on June 12, when the
Commerce Department issued a directive requiring Anthropic to suspend access to Claude Fable 5 and Mythos 5 for foreign nationals (prompting Anthropic to shut down both models globally for roughly
three weeks), and against OpenAI on June 26, when White House officials asked OpenAI to restrict GPT-5.6 Sol's launch to government-vetted partners. The Mayer Brown analysis of ECRA authority covers
this authority in depth, as does the prior TechTimes coverage of the voluntary-to-mandatory dynamic.\\n...\\nevaluation architecture can reliably contain\\n...\\ncontainment as an obstacle to
its\\n...\\nby the framework document\\n...\\nanswered by Altman\\n...\\ns July\\n...\\n0 preliminary White House meetings\\n...\\nExecutive Order 14409, signed June 2, 2026, directed federal agencies
to design a voluntary framework under which developers of the most capable AI models would give the government up to 30 days of pre-release access for security evaluation. The framework structure and
limits arrived on August 1 with classified benchmarks, no mandatory participation, no published capability threshold, and no public reporting requirement. The specific problem it cannot resolve is
that the government's evaluation environments use the same architectural pattern \\u2014 isolated sandboxes with software dependencies \\u2014 that OpenAI's model defeated by finding eight zero-days
in the sandbox's only software component. A framework for running evaluations cannot protect against the thing the evaluations themselves are testing for: whether a frontier model can escape the
environment it is being tested in. A prior TechTimes analysis documents why safety evaluations aren't certificates and the architectural limitation at its core.\\n...\\nIn March 2026, the Department
of Defense designated Anthropic a \\\"supply chain risk\\\" after CEO Dario\\n...\\nodei refused to allow Claude to be used for fully autonomous lethal weapons or mass domestic surveillance. Anthropic
sued the federal government, and US District Judge Rita Lin issued a preliminary injunction blocking enforcement of the designation in late March, finding Anthropic likely to prevail on constitutional
grounds. The injunction remains in effect while the case proceeds on appeal. Anthropic is therefore attending Tuesday's meeting while its lawsuit against a different part of the same administration
remains active \\u2014 a governance situation CNN noted creates \\\"confusion\\\" about the administration's overall approach to frontier AI companies.\"], \"published_date\":
\"2026-08-04T00:00:00.000\", \"score\": null}, {\"title\": \"Google, Microsoft, xAI Join US AI Pre-Release Reviews\", \"url\": \"https://nexchron.com/government/google-microsoft-xai-government-model-
evaluation\", \"snippet\": \"Google, Microsoft, xAI Join US AI Pre-Release Reviews\\n\\nGovernment & Policy | 4 min read\\n\\n# Google, Microsoft, and xAI Agree to Give US Government Early Access to
Frontier AI Models\\n\\nGoogle DeepMind, Microsoft, and xAI signed agreements with NIST to provide pre-release frontier model access to US government evaluators. All five major US AI labs are now part
of the program.\\n\\nHector Herrera\\n\\nShare on Twitter Share on LinkedIn\\n\\nMSFT $393.82 \\u25bc-1.8% GOOG $346.12 \\u25bc-2.2% 15m delay\\n\\nWhy this matters Goog\", \"highlights\": [\"Google
DeepMind, Microsoft, and xAI signed agreements with NIST to provide pre-release frontier model access to US government evaluators. All five major US AI labs are now part of the program.\\n...\\nWhy
this matters Google DeepMind, Microsoft, and xAI signed agreements with NIST to provide pre-release frontier model access to US government evaluators. All five major US AI labs are now part of the
program.\\n...\\nBy Hector Herrera | May 5, 2026 | Government\\n...\\nGoogle DeepMind, Microsoft, and xAI have signed voluntary agreements with the US government to hand over pre-release access to
their most powerful AI models before public launch \\u2014 including versions with reduced safety guardrails so federal evaluators can probe what these systems can actually do. The move consolidates a
federal evaluation framework that now covers the five most capable AI labs operating in the United States.\\n...\\nThe agreements are with NIST's Center for AI Standards and Innovation (CAISI)\\u2014
the National Institute of Standards and Technology division responsible for developing technical AI standards. Google DeepMind, Microsoft, and xAI join OpenAI and Anthropic, which had already signed
similar agreements. The program gives CAISI evaluators access to frontier models\\u2014 the most capable AI systems each company produces \\u2014 with enough lead time to assess risks before those
models reach the public.\\n...\\nThe core mechanism is pre-deployment access. Under the agreements, participating companies provide CAISI with model access before public release. Critically, that
access includes models with reduced or disabled safety guardrails \\u2014 the filters and refusal behaviors companies layer on top of base models for consumer deployment. Stripping those guardrails
lets government evaluators test raw model capabilities: what can the underlying system do when it isn't being constrained?\\n...\\nThe evaluations focus on national security risk: whether a model
could meaningfully accelerate development of biological, chemical, nuclear, or radiological weapons; whether it exhibits deceptive behavior; whether it can be jailbroken in ways that create downstream
harm. CAISI doesn't approve or block model releases \\u2014 the agreements are voluntary, and publication of evaluation results is not guaranteed. The framework is about generating an independent
technical assessment before launch, not regulatory gatekeeping.\\n...\\nWith all five of the largest US frontier AI labs now signed, the informal network covers:\\n...\\n- Anthropic \\u2014 Claude
model family\\n- OpenAI \\u2014 GPT and o-series models\\n- Google DeepMind \\u2014 Gemini model family\\n- Microsoft \\u2014 frontier models developed in-house or through its deep OpenAI
partnership\\n- xAI \\u2014 Grok model family\\n...\\nTwo forces pushed this expansion. First, the Mythos security incident\\u2014 a significant AI safety and security event earlier this year that
demonstrated the potential for frontier models to be exploited in ways their developers hadn't anticipated \\u2014 accelerated government interest in independent pre-deployment review. Second, the
White House has been circulating a potential executive order that would formalize pre-deployment evaluations for the most capable AI systems. Voluntary agreements ahead of a mandate are a standard
industry move: shape the framework before it's imposed.\\n...\\nNIST's CAISI was established as part of the Biden-era AI Executive Order infrastructure and has survived into the current administration
as the technical standards body for AI. Its evaluations draw on red-teaming \\u2014 adversarial testing \\u2014 and capability assessments developed in collaboration with the AI Safety Institute
network, which includes UK and other allied-nation counterparts.\\n...\\nWhether the White House executive order on pre-deployment evaluations actually materializes will determine whether this
voluntary framework becomes mandatory \\u2014 and whether its scope expands beyond the current five labs to cover international developers, open-weight models, or fine-tuned variants of base models.
Watch for CAISI to publish any methodology documentation that signals how rigorous these evaluations actually are.\\n...\\nGovernment & Policy \\u00b7 4 min read The Defense Department has finalized
AI supply contracts with OpenAI, Google, and Microsoft, codifying a multi-vendor procurement doctrine that explicitly excludes Anthropic and signals a structural shift in how the federal government
buys AI. Jun 16\"], \"published_date\": \"2026-05-06T00:00:00.000\", \"score\": null}], \"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Critical context found: EO 14409 (June 2, 2026) created a voluntary pre-release framework, finalized Aug 1, with an Aug 4 White House implementation meeting. Let me check what's happened since Aug 10.

## 🔧 Tool: mcp__search__search


## 🔧 Tool: mcp__markets__metaculus


```json
{
  "query": "EO 14409 voluntary framework labs sign on CAISI NSA pre-release access August 2026",
  "lanes": [
    "neural"
  ],
  "limit": 8
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"EO 14409 voluntary framework labs sign on CAISI NSA pre-release access August 2026\", \"lanes_run\": [\"neural\"], \"web\": [], \"markets\": [], \"news\": [],
\"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [{\"title\": \"US Government Can Now Preview AI Models Before Release \\u2014 EO 14409 CAISI Live\", \"url\":
\"https://witho2.com/news/the-us-government-can-now-preview-ai-models-before-you-can\", \"snippet\": \"US Government Can Now Preview AI Models Before Release \\u2014 EO 14409 CAISI Live\\n\\nClose
Menu\\n\\nHubSpot Lost 12.7% After OpenAI Presence \\u2014 Should You Still Buy It?\\n\\nGrok 4.6 Drops August 7: xAI\\u2019s 1.5T Agent Model, What Business Users Get\\n\\nAI Data Centers Have Raised
US Electricity Bills by $23 Billion\\n\\nFacebook X (Twitter) Instagram\\n\\nFacebook X (Twitter) Instagram\\n\\nUnder Executive Order 14409's CAISI framework, US government agencies can now preview
and evaluate frontier AI models before public releas\", \"highlights\": [\"Under Executive Order 14409's CAISI framework, US government agencies can now preview and evaluate frontier AI models before
public release.\\n...\\nPublished: August 1, 2026, 18:25 IST\\n...\\nExecutive Order 14409\\u2019s 60-day design deadline expired on August 1, 2026, giving the Center for AI Standards and Innovation
(CAISI) and the NSA a finalized voluntary framework for reviewing frontier AI models up to 30 days before they reach enterprise customers. President Trump signed the order, titled \\u201cPromoting
Advanced Artificial Intelligence Innovation and Security,\\u201d on June 2, 2026, and directed agencies to complete the framework within 60 days. OpenAI, Anthropic, and Google received the draft
framework before the deadline. The framework\\u2019s design goal is flagging risks of advanced AI being exploited by China or Russia before public access, according to legal analysis published by
Lexology.\\n...\\nThe framework gives the US government pre-release access to \\u201ccovered frontier models\\u201d for a window of up to 30 days before release to other trusted partners. CAISI,
housed in the Commerce Department, and the NSA conduct the reviews. The classification criteria for covered models involves classified benchmarking; the specific compute threshold is not yet public,
according to Norton Rose Fulbright\\u2019s analysis. The executive order also creates an AI cybersecurity clearinghouse for sharing AI vulnerability information across federal agencies. The order
preserves its voluntary framing in explicit terms: \\u201cNothing shall be construed to authorize creation of any mandatory governmental licensing, pre-clearance, or permitting requirement for the
development, publication, release or distribution of AI models,\\u201d the order states.\\n...\\nThe GPT-5.6 precedent shows how voluntary review became practical pressure before the framework
existed. OpenAI delayed GPT-5.6\\u2019s broader rollout on June 26, 2026 after a US government request \\u2014 an informal arrangement that predated the formal standards, as WithO2 covered when
GPT-5.6\\u2019s government-influenced rollout reshaped OpenAI\\u2019s model lineup. Labs seeking US government contracts have little room to opt out of a review process the government administers. The
framework formalizes that dynamic with a defined reviewer, a defined access window, and a circulated draft that OpenAI, Anthropic, and Google have already seen.\\n...\\nThree consequences follow for
companies buying enterprise AI tools, such as ChatGPT, Claude, and Gemini. First, new frontier model releases may now be sequenced by government security review rather than pure commercial roadmaps,
so feature launches can arrive later than vendor announcements suggest. Second, models flagged during review may be restricted or modified before enterprise release. Third, the framework lands in the
same week as EU AI Act Article 50 enforcement (August 2) \\u2014 a two-hemisphere squeeze in which businesses serving both markets face simultaneous new AI compliance regimes on opposite sides of the
Atlantic.\\n...\\n\\u201cVoluntary\\u201d until it isn\\u2019t. Labs that want US government contracts and cleared the June GPT-5.6 review can\\u2019t really opt out \\u2014 the CAISI framework just
gives an existing dynamic teeth and a process. For businesses buying AI tools, the question isn\\u2019t whether models get reviewed. It\\u2019s whether that review slows down the features you\\u2019re
waiting for.\\n...\\nWithO2 covered this framework at the drafting stage in July, when the White House circulated its voluntary AI standards plan to frontier labs, and reported OpenAI\\u2019s GPT-5.6
lineup changes that followed the government\\u2019s June review request. For the European side of this week\\u2019s regulatory shift, see our coverage of EU AI Act Article 50 chatbot disclosure rules,
enforceable from August 2, 2026.\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null}, {\"title\": \"White House Frontier-AI Framework Done but Unpublished\", \"url\":
\"https://agenccy.ai/news/white-house-frontier-model-framework-complete-unpublished/\", \"snippet\": \"White House Frontier-AI Framework Done but Unpublished\\n\\n# The White House Says Its Frontier-
Model Framework Is Finished. It Has Not Published It.\\n\\nExecutive Order 14409 gave the administration 60 days to design a voluntary framework for evaluating advanced models. The deadline was 1
August. The announcement came on 3 August, and the document itself remains unreleased.\\n\\nAug 4, 2026Source: CNBC\\n\\nThe White House said on 3 August that the framework required by Executive Order
14409 is complete: \\\"The\", \"highlights\": [\"Executive Order 14409 gave the administration 60 days to design a voluntary framework for evaluating advanced models. The deadline was 1 August. The
announcement came on 3 August, and the document itself remains unreleased.\\n...\\nThe White House said on 3 August that the framework required by Executive Order 14409 is complete: \\\"The voluntary
framework outlined in the June 2nd executive order is complete. Discussions with industry about next steps are underway.\\\" A closed-door meeting with developers followed on 4 August.\\n...\\nEO
14409 was signed 2 June 2026 and published in the Federal Register on 5 June. It directs the design of \\\"a voluntary framework with AI developers through which developers would be able to\\u2026
engage the Federal Government to determine whether model(s) under development meet the designation of 'covered frontier model.'\\\" The 60-day clock ran to 1 August.\\n...\\nThis is not a rule and not
a statute. A developer decides\\n...\\nat all, and\\n...\\nin the order compels participation. Representative Ted Lieu called the framework\\n...\\nVOLUNTARY\\\" and said companies are free to ignore
it; Greg Casar and Pat Ryan objected to the voluntary approach as such.\\n...\\nThe distinction that matters here is between a statement and a document. No text has been released, no evaluation
criteria are public, and the threshold for \\\"covered frontier model\\\" is unknown outside the meeting. There is also a timing dispute worth flagging as a dispute: the administration says it met the
deadline, which fell two days before the announcement.\\n...\\nThe order hands the work to the Secretary of the Treasury, the Secretary of War acting through the director of the NSA, and the Secretary
of Homeland Security acting through the director of CISA \\u2014 not to NIST or the science office, as much of the coverage assumes. It is a national-security assignment rather than a standards-body
one, which shapes what \\\"evaluation\\\" is likely to mean in practice. Staff from OpenAI, Google, Anthropic and Meta were called to the 4 August meeting.\"], \"published_date\":
\"2026-08-04T00:00:00.000\", \"score\": null}, {\"title\": \"White House keeps frontier AI review rules private as Nvidia joins talks - RuntimeWire\", \"url\": \"https://runtimewire.com/article/white-
house-private-frontier-ai-framework-nvidia\", \"snippet\": \"White House keeps frontier AI review rules private as Nvidia joins talks - RuntimeWire\\n\\n## Why it matters\\n\\nThe framework could
decide which labs, infrastructure providers and foreign partners see powerful models early. Keeping its rules private gives participants clarity and access that excluded developers cannot evaluate or
challenge.\\n\\nJensen Huang's Nvidia had staff inside the White House's August 4th industry meetings on frontier AI security, while developers excluded from the talks were left\", \"highlights\":
[\"Jensen Huang's Nvidia had staff inside the White House's August 4th industry meetings on frontier AI security, while developers excluded from the talks were left without the framework that could
determine how the government reviews powerful models before release.\\n...\\nThe White House does not plan to publish the completed framework, three people familiar with the discussions told Axios.
Its contents will instead be shared with companies participating in the voluntary process.\\n...\\nThat decision turns a national AI security policy into a private operating agreement between the
government and a selected group of technology companies. The classified material includes the cyber-capability benchmark and the threshold that determines which systems qualify as \\\"covered frontier
models.\\\" The White House is also withholding the surrounding framework, which the executive order itself does not designate as classified.\\n...\\na two-tier policy process. Participating
developers can learn how\\n...\\napproach the government,\\n...\\nmodel intellectual property during\\n...\\n\\\"trusted partners\\\" for early access. Developers outside the room\\n...\\nthe same
process may apply to their next model\\n...\\nPresident Donald Trump signed Executive Order 14409 on June 2nd. It directed federal agencies to build the framework within 60 days, putting the deadline
around August 1st. The White House said on August 3rd that it had finished the work on time, according to earlier Axios reporting.\\n...\\nThe order allows developers to ask whether a model under
development falls within the government's classified frontier threshold. A developer can then provide federal officials with access for as long as 30 days before releasing that model to other trusted
partners.\\n...\\nThe government must protect confidentiality, cybersecurity, intellectual property and model access during that window. Developers also collaborate with federal officials on deciding
which trusted partners may receive the model early.\\n...\\nThe order expressly bars the framework from becoming a mandatory licensing, preclearance or permitting system for AI development and
release. Participation remains voluntary under the text Trump signed.\\n...\\nVoluntary status does not make the process commercially trivial. Early access to a capable model can give cybersecurity
agencies and critical-infrastructure operators time to test defenses before broader distribution. It can also give selected companies, researchers or foreign governments an earlier view of
capabilities that rivals and excluded partners have not seen.\\n...\\nThe unanswered operational question is who qualifies for that access. Axios reported that the framework does not publicly identify
the trusted partners or establish whether foreign governments can join the group. The European Union and United Kingdom therefore lack a public basis for determining whether their agencies or
researchers could participate.\\n...\\nFrontier labs have publicly asked for predictable federal testing. In a July 15th policy post, OpenAI said the cyber-evaluation process needed to be consistent
and repeatable across state and federal systems. OpenAI also said it was discussing the framework with the administration, peer companies and business groups.\\n...\\nAxios previously identified
OpenAI, Anthropic and Google as labs that supplied feedback on a draft. The White House said it was engaging with additional industry partners, without publishing a participant list.\\n...\\nA private
framework can still produce consistent treatment among participating developers. It cannot demonstrate that consistency to companies outside the process. Those developers will not know whether
comparable models receive comparable scrutiny, how intellectual-property protections work in practice or whether access decisions favor established labs with existing government
relationships.\\n...\\nResearchers and policymakers face a related problem. Keeping dangerous benchmark details classified can prevent adversaries from using the government's tests as a capability
roadmap. Withholding the administrative rules surrounding those tests also blocks outside examination of who receives access, how disputes are handled and whether the voluntary process operates as
written.\\n...\\nThe White House has chosen confidentiality as the price of getting model developers and national-security agencies into the same review process. The framework now depends on a smaller
circle of companies trusting the government with unreleased models, while everyone outside that circle must trust a system they cannot inspect.\"], \"published_date\": \"2026-08-04T00:00:00.000\",
\"score\": null}, {\"title\": \"Washington's Voluntary Frontier Model Review Hits Its Deadline | AI2Work\", \"url\": \"https://ai2.work/blog/washington-s-voluntary-frontier-model-review-hits-its-
deadline\", \"snippet\": \"Washington's Voluntary Frontier Model Review Hits Its Deadline | AI2Work\\n\\nAI News & Trends\\n\\n# Washington's Voluntary Frontier Model Review Hits Its Deadline\\n\\nEO
14409's 60-day clock on the US frontier model review framework expires August 1. Inside the 30-day window, the classified threshold, and what buyers do next.\\n\\nJuly 31, 2026\\n\\n12 min readBy
AI2Work Editorial Team\\n\\nAI News & Trends\\n\\n# Washington's Voluntary Frontier Model Review Hits Its Deadline\\n\\nJuly 31, 2026\\n\\n12 min readBy AI2Work Editor\", \"highlights\": [\"EO 14409's
60-day clock on the US frontier model review framework expires August 1. Inside the 30-day window, the classified threshold, and what buyers do next.\\n...\\n- 1August 1, 2026 is a deadline for the
government, not for AI labs. EO 14409 gives agencies 60 days to design the voluntary framework; nothing becomes legally binding on developers that day.\\n...\\n- 2The core mechanism is up to 30 days
of federal pre-release access to covered frontier models, a window cut from a reported 90 days after industry lobbying derailed the original signing ceremony.\\n...\\nOn June 2, 2026, President Trump
signed Executive Order 14409, \\\"Promoting Advanced Artificial Intelligence Innovation and Security.\\\" Buried inside a mostly cybersecurity-focused document was Section 3, which started a 60-day
clock. That clock expires on August 1, 2026.\\n...\\nWhat is due is not a rule, a statute, or a licensing regime. It is a design: a voluntary framework under which developers of so-called covered
frontier models may hand the federal government up to 30 days of pre-release access before those models reach the public. The order goes out of its way to say this creates no mandatory licensing,
preclearance, or permitting requirement. The question everyone in the industry has been asking for two months is whether that disclaimer means anything.\\n...\\nStrip away the framing and the order is
a narrow instrument. Section 3 assigns the design work to the Secretary of the Treasury, the Secretary of War through the Director of the NSA, and the Secretary of Homeland Security through the
Director of CISA. Consulted parties include the National Cyber Director, the Assistant to the President for Science and Technology, and the Secretary of Commerce through the Director of NIST. Sixty
days from June 2 is August 1.\\n...\\n- A classified benchmarking process to assess advanced cyber capabilities and set the threshold for what counts as a covered frontier model. The designation is
made by the NSA Director. No public metric appears anywhere in the order.\\n- Up to 30 days of pre-release access under Section 3(b)(ii), during which the government evaluates the model for
cybersecurity risk and vulnerabilities, with confidentiality and IP protections promised but not yet specified.\\n- Jointly selected trusted partners under Section 3(b)(iii), where developers and the
government collaborate on which early-access recipients get the model first.\\n...\\nOne detail is worth pausing on. Designation authority sits with the national security establishment, not with the
civilian standards office that has actually been running frontier model evaluations. Since 2024, the Commerce Department's Center for AI Standards and Innovation and its predecessor have operated
under publicly announced agreements with OpenAI and Anthropic. On May 5, 2026, Commerce announced that Google, Microsoft, and xAI had joined, that the original agreements had been renegotiated, and
that CAISI had completed more than 40 assessments including on unreleased models. Four weeks later, the order moved the decisive designation function to the NSA.\\n...\\nOn July 27, The Information
reported, citing three people familiar with the matter, that the White House Office of the National Cyber Director had circulated a draft of the framework to OpenAI, Anthropic, and Google roughly two
weeks earlier, and that the three companies jointly submitted their own edits. The same reporting, citing two people familiar, said the White House has told some companies that model reviews will be
conducted by a combination of the NSA and CAISI.\\n...\\nThat pairing is notable because CAISI appears nowhere in EO 14409. The order names the Secretary of Commerce through the Director of NIST only
as a consulted party. A reported NSA-plus-CAISI review body is consistent with the order's structure, but it is established by no official document, and as of this writing no second outlet has
independently confirmed the draft's circulation and no agency has published a text.\\n...\\nJuly 31, 20\\n...\\n6 is this: the framework is reported to be\\n...\\nto final, and reporting\\n...\\nnot
publication. Executive-order deadlines of this kind slip routinely and without legal consequence. Section 2's other major deliverable, the AI cybersecurity clearinghouse, did land
\\u2014\\n...\\nWhite House publicly launched\\n...\\non July 1\\n...\\nleaves the Section 3 framework as the order's main outstanding item\\n...\\n| Dimension | US \\u2014 EO 14409 framework | EU
\\u2014 AI Act GPAI regime |\\n| --- | --- | --- |\\n| Legal force | Voluntary; \\u00a73(c) expressly disclaims licensing or preclearance | Binding; Commission enforcement powers apply from Aug 2,
2026 |\\n...\\n| Scope trigger | Classified NSA cyber-capability benchmark; threshold undisclosed | Public compute threshold \\u2014 10^25 FLOPs presumed systemic risk |\\n...\\n| Timing model | Up to
30 days pre-release access, per covered model | Continuous obligations: documentation, evaluations, incident reporting |\\n...\\n| Who reviews | NSA designates; NSA + CAISI reported as reviewers |
European AI Office, supported by the GPAI Code of Practice |\\n...\\ndetermined through a\\n...\\nexecutive-branch process, made by\\n...\\nNothing in the\\n...\\ncase-by-case exercise of discretion
no\\n...\\nadds the standard disclaimer\\n...\\ncreates no right or benefit enforceable at law.\"], \"published_date\": \"2026-07-31T00:00:00.000\", \"score\": null}, {\"title\": \"Presidential
Documents\", \"url\": \"https://www.whitehouse.gov/wp-content/uploads/2026/06/eo-14409.pdf\", \"snippet\": \"## Presidential Documents\\n\\n34565\\n\\nFederal Register Vol. 91, No. 108 Friday, June 5,
2026\\n\\nTitle 3\\u2014\\n\\n### The President\\n\\nExecutive Order 14409 of June 2, 2026\\n\\n### Promoting Advanced Artificial Intelligence Innovation and Security\\n\\nBy the authority vested in
me as President by the Constitution and the laws of the United States of America, it is hereby ordered: Section 1. Purpose. The United States continues to lead the world in Artificial Intelligence
(AI) because of the enormous talent and innova\", \"highlights\": [\". It is the policy\\n...\\nthe United States to promote AI innovation and security by working collaboratively with the private
sector to modernize government and private sector information systems and harden them against external threats; to protect American ingenuity and intellectual property from exploi tation and theft by
adversaries; and to cultivate America\\u2019s advanced AI enabled capabilities.\\n...\\n. Upgrading American Systems for Advanced AI. (a) Within 30 days\\n...\\nthe date of this order, the Committee
on National Security Systems\\n...\\nprioritize the cyber\\n...\\nof National Security Systems, as defined in\\n...\\n44 U\\n...\\nS.C.\\n...\\n3552(\\n...\\n6)(A\\n...\\nof this order\\n...\\n30 days
of\\n...\\ndate of this order,\\n...\\n) Within 3\\n...\\nAgency (CISA), in consultation with\\n...\\nOffice of Management and Budget (OMB), the Assistant to the President for National Security
Affairs, and the National\\n...\\nDirector, shall release Binding Operational Directives and other guidance as appropriate to: (i) expedite and prioritize\\n...\\ncyber defense of civilian Federal
Government\\n...\\nsystems in order to protect our\\n...\\nfacilitate access to\\n...\\n(d) Within 30 days of the date of this order, the Secretary of the Treasury, in consultation with the National
Cyber Director, the Secretary of War, through the Director of the National Security Agency (NSA), and the Secretary of Homeland Security, through the Director of CISA, shall form an AI cyberse curity
clearinghouse, in voluntary collaboration with the AI industry and operators of critical infrastructure, that coordinates and deconflicts scanning for software vulnerabilities, discovers and validates
such vulnerabilities, and coordinates and prioritizes remediation and distribution of vulnerability patches. (e) Within 30 days of the date of this order, the Director of OMB, in coordination with the
National Cyber Director and the Director of CISA, shall determine whether any Federal grant programs have available and relevant funding that can be directed toward applicants developing advanced AI
vulnerability detection. (f) Within 60 days of the date of this order, the Director of the Office of Personnel Management shall expand the United States Tech Force Informa tion Cybersecurity
Specialist hiring and placement pathways. Sec. 3. Secure Frontier Model Deployment. Within 60 days of the date of this order, the Secretary of the Treasury, the Secretary of War, through the Director
of NSA, and the Secretary of Homeland Security, through the Director of CISA, in consultation with the White House Chief of Staff, through the National Cyber Director, the Assistant to the President
for Science and Technology (APST), and the Secretary of Commerce, through the Director of the National Institute of Standards and Technology, and in coordination with other agencies, as appropriate,
shall: (a) develop and maintain a classified benchmarking process to assess the advanced cyber capabilities of AI models and determine the threshold at which an AI model should be designated a
\\u2018\\u2018covered frontier model\\u2019\\u2019 for the purposes of this order, sharing such assessments with AI developers and researchers as appropriate. Such a determination shall be made by the
Director of NSA, in consultation with the National Cyber Director, the APST, the Director of CISA, and other representatives of the Department of War, as appropriate. (b) design a voluntary framework
with AI developers through which devel opers would be able to: (i) engage the Federal Government to determine whether model(s) under development meet the designation of \\u2018\\u2018covered frontier
model\\u2019\\u2019; (ii) provide the Federal Government with access to covered frontier models, subject to appropriate confidentiality, cybersecurity, insider-risk, and intel lectual-property
protection, use, and nondisclosure requirements, for a period of up to 30 days before they plan to release such models to other trusted partners; and (iii) collaborate with the Federal Government to
select trusted partners that will have early access to covered frontier models to promote secure innovation and strengthen the cybersecurity of critical infrastructure. (c) Nothing in this section
shall be construed to authorize the creation of a mandatory governmental licensing, preclearance, or permitting require ment for the development, publication, release, or distribution of new AI
models, including frontier models. Sec. 4. Protection Against Criminal Actors. The Attorney General shall prioritize the enforcement of 18 U.S.C. 1028, 18 U.S.C. 1030, 18 U.S.C. 1343, and all other
applicable Federal criminal laws against anyone who utilizes AI to illegally access or damage a computer without authorization, or who utilizes AI while engaged in such illegal access to further any
other crime. This includes breaching any public or private information tech nology system, or employing AI agents to unlawfully access data or informa tion that is subsequently used for a criminal or
unlawful purpose. Sec. 5. General Provisions. (a) Nothing in this order shall be construed to impair or otherwise affect:\"], \"published_date\": null, \"score\": null}, {\"title\": \"Controlling
Advanced Artificial Intelligence: Executive Order\", \"url\": \"https://www.congress.gov/crs_external_products/IF/PDF/IF13268/IF13268.2.pdf\", \"snippet\": \"https://crsreports.congress.gov\\n\\nJuly
9, 2026\\n\\n## Controlling Advanced Artificial Intelligence: Executive Order\\n\\n## 14409 Explained\\n\\nOn June 2, 2026, President Donald Trump signed Executive Order 14409 (E.O. 14409), Promoting
Advanced Artificial Intelligence Innovation and Security. The E.O. directs agencies to harden federal government infrastructure against artificial intelligence (AI)-enabled risks and work with the
private sector to strengthen AI security. It is the latest in a series of E.O\", \"highlights\": [\"The E.O. has dual goals of accelerating AI innovation and improving security. It directs federal
agencies to coordinate on assessing how advanced AI models might be used for both defensive and offensive cyber operations. The order calls for a classified benchmarking process to determine whether
an AI system qualifies as a covered frontier model (to be defined within 60 days (August 1, 2026)) based on its cyber capabilities.\\n...\\nCompanies developing advanced AI models are asked to
participate in a voluntary review process that gives the government a window of 30 days to examine new systems before such models are released to \\u201cother trusted partners\\u201d (e.g., critical
infrastructure companies). The order instructs specified agencies to create an AI cybersecurity clearinghouse to centralize information on AI-related vulnerabilities and threats, and to modernize
government networks using advanced AI tools. It links this security posture to broader economic and strategic goals, emphasizing protection of U.S. intellectual property and maintaining American
leadership in AI.\\n...\\n\\u2022 Issue Binding Operational Directives for civilian federal systems; expand AI-enabled defensive tools; extend cyber tools and services to states, local authorities,
and critical infrastructure (Cybersecurity and Infrastructure Security Agency [CISA], Office of Management and Budget [OMB], the National Security Council [NSC], the Assistant to the President for
National Security Affairs [APNSA], and the National Cyber Director [NCD]). Due within 30 days (July 2, 2026).\\n...\\n\\u2022 Form an AI cybersecurity clearinghouse (Department of the Treasury
[Treasury], NCD, the National Security Agency [NSA], and CISA). Due within 30 days (July 2, 2026).\\n...\\n\\u2022 Develop a classified AI benchmarking process and establish a voluntary framework for
covered frontier model pre-release access (NSA, NCD, Assistant to the President for Science and Technology [APST], CISA, and DOD). Due within 60 days (August 1, 2026).\\n...\\n\\u2022 Develop a
voluntary framework for AI companies to disclose their models (Treasury, NSA, CISA, National Institute of Standards and Technology [NIST], APST, and DOD). Due within 60 days (August 1,
2026).\\n...\\nThe E.O.\\u2019s cybersecurity provisions aim to expand voluntary national security oversight of advanced AI models while stopping short of formal licensing or requiring preclearance.
By creating a category of covered frontier models, the order treats advanced AI systems as potential dual-use tools over which early government oversight is desirable\\u2014similar to technologies
with potentially dual civilian and military applications (e.g., sensors, lasers, avionics), as covered by the Wassenaar Arrangement. A voluntary notification and review window\\n...\\nE.O. 14409
directs Treasury, with DOD and DHS, to carry out activities to secure frontier model deployment, in consultation with NIST, among other agencies. Previous agreements between the NIST and AI companies
Anthropic and OpenAI established a framework for NIST to \\u201creceive access to major new models from each company prior to and following their public release.\\u201d Such agreements neither
provided for public transparency on AI testing and evaluation nor included all frontier AI companies. Proposed legislation would mandate pre-deployment evaluation of certain AI models (e.g., the
Artificial Intelligence Civil Rights Act of 2025, H.R. 6356). A draft bill would outline transparency and assessment frameworks, and security testing of frontier AI models (e.g., the discussion draft
of the Great American Artificial Intelligence Act of 2026).\\n...\\ndevelopment and use of AI for national security applications.\\u201d NSPM-11 directs the national security enterprise to work with
industry to \\u201cmake the most advanced frontier models broadly available to national security professionals ... \\u201d The directive additionally notes that the national security enterprise is to
ensure that any adopted AI systems \\u201care designed to be reliable, robust, steerable, and controllable, and that they operate, in accordance with applicable laws, government policies, and
guidance.\\u201d In support of the objectives of E.O. 14409, NSPM-11 also directs the Secretary of Defense, the Secretary of Energy, the Director of National Intelligence, and the Director of the NSA,
through the AI Security Center, in consultation with the APST, to work with industry to enhance the security of data centers and advanced AI technologies. This could include information sharing; joint
testing, research, and development; and the provision of technical support. Congress may conduct oversight of these activities and, if necessary, \\u201cestablish plans to mitigate potential
concerns\\u201d in consultation with industry, as recommended by the March 2026 National Policy Framework for AI.\\n...\\nconsider the extent\\n...\\n. 1\\n...\\nspecified by the\\n...\\n. The order
does\\n...\\nit unclear as\\n...\\nCongress might consider whether to maintain the overarching approach of voluntary industry engagement in AI or whether safety and security concerns of AI models
warrant the establishment of federal requirements for testing and evaluation of certain AI models prior to release.\"], \"published_date\": null, \"score\": null}, {\"title\": \"Controlling Advanced
Artificial Intelligence: Executive Order 14409 ...\", \"url\": \"https://www.congress.gov/crs-product/IF13268\", \"snippet\": \"Controlling Advanced Artificial Intelligence: Executive Order 14409
Explained | Congress.gov | Library of Congress\\n\\nskip to main content\\n\\nCitation Subscribe Share/Save Site Feedback\\n\\n# Controlling Advanced Artificial Intelligence: Executive Order 14409
Explained\\n\\n## CRS PRODUCT (LIBRARY OF CONGRESS)\\n\\nHide Overview\\n\\n| CRS Product Type: | In Focus |\\n| --- | --- |\\n| CRS Product Number: | IF13268 |\\n| Referenced Legislation: | H.R. 6356
|\\n| Publication Date: | 07/09/2026 |\\n| Authors: | Harris, Laurie\", \"highlights\": [\"The E.O. has dual goals of accelerating AI innovation and improving security. It directs federal agencies to
coordinate on assessing how advanced AI models might be used for both defensive and offensive cyber operations. The order calls for a classified benchmarking process to determine whether an AI system
qualifies as a covered frontier model (to be defined within 60 days (August 1, 2026)) based on its cyber capabilities.\\n...\\nCompanies developing advanced AI models are asked to participate in a
voluntary review process that gives the government a window of 30 days to examine new systems before such models are released to \\\"other trusted partners\\\" (e.g., critical infrastructure
companies). The order instructs specified agencies to create an AI cybersecurity clearinghouse to centralize information on AI-related vulnerabilities and threats, and to modernize government networks
using advanced AI tools. It links this security posture to broader economic and strategic goals, emphasizing protection of U.S. intellectual property and maintaining American leadership in
AI.\\n...\\n- Issue Binding Operational Directives for civilian federal systems; expand AI-enabled defensive tools; extend cyber tools and services to states, local authorities, and critical
infrastructure (Cybersecurity and Infrastructure Security Agency [CISA], Office of Management and Budget [OMB], the National Security Council [NSC], the Assistant to the President for National
Security Affairs [APNSA], and the National Cyber Director [NCD]). Due within 30 days (July 2, 2026).\\n...\\nhouse (Department of the\\n...\\n, the National Security Agency [\\n...\\n], and
C\\n...\\n). Due within 3\\n...\\ndays (July\\n...\\n20\\n...\\n- Develop a classified AI benchmarking process and establish a voluntary framework for covered frontier model pre-release access (NSA,
NCD, Assistant to the President for Science and Technology [APST], CISA, and DOD). Due within 60 days (August 1, 2026).\\n...\\n- Develop a voluntary framework for AI companies to disclose their
models (Treasury, NSA, CISA, National Institute of Standards and Technology [NIST], APST, and DOD). Due within 60 days (August 1, 2026).\\n...\\nThe E.O.'s cybersecurity provisions aim to expand
voluntary national security oversight of advanced AI models while stopping short of formal licensing or requiring preclearance. By creating a category of covered frontier models, the order treats
advanced AI systems as potential dual-use tools over which early government oversight is desirable\\u2014similar to technologies with potentially dual civilian and military applications (e.g.,
sensors, lasers, avionics), as covered by the Wassenaar Arrangement. A voluntary notification and review window aims to give agencies time to probe models for offensive and defensive cyber
applications before public release. Such a process may increase the potential for earlier detection of vulnerabilities or potential abuse pathways.\\n...\\nE.O. 14409 directs Treasury, with DOD and
DHS, to carry out activities to secure frontier model deployment, in consultation with NIST, among other agencies. Previous agreements between the NIST and AI companies Anthropic and OpenAI
established a framework for NIST to \\\"receive access to major new models from each company prior to and following their public release.\\\" Such agreements neither provided for public transparency
on AI testing and evaluation nor included all frontier AI companies. Proposed legislation would mandate pre-deployment evaluation of certain AI models (e.g., the Artificial Intelligence Civil Rights
Act of 2025, H.R. 6356). A draft bill would outline transparency and assessment frameworks, and security testing of frontier AI models (e.g., the discussion draft of the Great American Artificial
Intelligence Act of 2026).\\n...\\nOn June 5, 2026, President Trump issued National Security Presidential Memorandum-11 (NSPM-11), a related document that provides guidance for \\\"[accelerating] the
development and use of AI for national security applications.\\\" NSPM-11 directs the national security enterprise to work with industry to \\\"make the most advanced frontier models broadly available
to national security professionals.... \\\" The directive additionally notes that the national security enterprise is to ensure that any adopted AI systems \\\"are designed to be reliable, robust,
steerable, and controllable, and that they operate, in accordance with applicable laws, government policies, and guidance.\\\" In support of the objectives of E.O. 14409, NSPM-11 also directs the
Secretary of Defense, the Secretary of Energy, the Director of National Intelligence, and the Director of the NSA, through the AI Security Center, in consultation with the APST, to work with industry
to enhance the security of data centers and advanced AI technologies. This could include information sharing; joint testing, research, and development; and the provision of technical support. Congress
may conduct oversight of these activities and, if necessary, \\\"establish plans to mitigate potential concerns\\\" in consultation with industry, as recommended by the March 2026 National Policy
Framework for AI.\\n...\\nCongress might consider whether to maintain the overarching approach of\\n...\\nin AI or whether safety and security concerns of AI\\n...\\nfor testing and\"],
\"published_date\": \"2026-07-09T00:00:00.000\", \"score\": null}, {\"title\": \"Promoting Advanced Artificial Intelligence Innovation and Security\", \"url\":
\"https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/\", \"snippet\": \"Promoting Advanced Artificial Intelligence Innovation
and Security \\u2013 The White House\\n\\n# PROMOTING ADVANCED ARTIFICIAL INTELLIGENCE INNOVATION AND SECURITY\\n\\nJune 2, 2026\\n\\nExecutive Order 14409\\n\\nBy the authority vested in me as
President by the Constitution and the laws of the United States of America, it is hereby ordered:\\n\\nSection 1. Purpose. The United States continues to lead the world in Artificial Intelligence (AI)
because of the enormous talent and innovation of our AI industry, and because\", \"highlights\": [\"Executive Order 14409\\n...\\n(c) Within 30 days of the date of this order, the Secretary of
Homeland Security, through the Director of the Cybersecurity and Infrastructure Security Agency (CISA), in consultation with the Director of the Office of Management and Budget (OMB), the Assistant to
the President for National Security Affairs, and the National Cyber Director, shall release Binding Operational Directives and other guidance as appropriate to:\\n...\\n(d) Within 30 days of the date
of this order, the Secretary of the Treasury, in consultation with the National Cyber Director, the Secretary of War, through the Director of the National Security Agency (NSA), and the Secretary of
Homeland Security, through the Director of CISA, shall form an AI cybersecurity clearinghouse, in voluntary collaboration with the AI industry and operators of critical infrastructure, that
coordinates and deconflicts scanning for software vulnerabilities, discovers and validates such vulnerabilities, and coordinates and prioritizes remediation and distribution of vulnerability
patches.\\n...\\nSec. 3. Secure Frontier Model Deployment. Within 60 days of the date of this order, the Secretary of the Treasury, the Secretary of War, through the Director of NSA, and the Secretary
of Homeland Security, through the Director of CISA, in consultation with the White House Chief of Staff, through the National Cyber Director, the Assistant to the President for Science and Technology
(APST), and the Secretary of Commerce, through the Director of the National Institute of Standards and Technology, and in coordination with other agencies, as appropriate, shall:\\n...\\n(a) develop
and maintain a classified benchmarking process to assess the advanced cyber capabilities of AI models and determine the threshold at which an AI model should be designated a \\u201ccovered frontier
model\\u201d for the purposes of this order, sharing such assessments with AI developers and researchers as appropriate. Such a determination shall be made by the Director of NSA, in consultation with
the National Cyber Director, the APST, the Director of CISA, and other representatives of the Department of War, as appropriate.\\n...\\n(b) design a voluntary framework with AI developers through
which developers would be able to:\\n...\\n(i) engage the Federal Government to determine whether model(s) under development meet the designation of \\u201ccovered frontier model\\u201d;\\n...\\n(ii)
provide the Federal Government with access to covered frontier models, subject to appropriate confidentiality, cybersecurity, insider-risk, and intellectual-property protection, use, and nondisclosure
requirements, for a period of up to 30 days before they plan to release such models to other trusted partners; and\\n...\\n(iii) collaborate with the Federal Government to select trusted partners that
will have early access to covered frontier models to promote secure innovation and strengthen the cybersecurity of critical infrastructure.\\n...\\n(c) Nothing in this section shall be construed to
authorize the creation of a mandatory governmental licensing, preclearance, or permitting requirement for the development, publication, release, or distribution of new AI models, including frontier
models.\"], \"published_date\": \"2026-06-02T00:00:00.000\", \"score\": null}], \"social\": [], \"failed\": []}"}]
```

```json
{
  "post_id": 45203
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"post_id\": 45203, \"question\": {\"post_id\": 45203, \"title\": \"Will a U.S. federal agency announce new or expanded model evaluation agreements with both OpenAI and
Anthropic before September 3, 2026?\", \"type\": \"binary\", \"url\": \"https://www.metaculus.com/questions/45203\", \"background_info\": \"The Center for AI Standards and Innovation, or CAISI, is
located within the National Institute of Standards and Technology. CAISI serves as a principal federal contact for testing commercial AI systems, establishing voluntary agreements with developers, and
evaluating capabilities that may create cybersecurity, biosecurity, chemical, or other national-security risks. Its institutional role therefore connects private frontier-model development with
federal testing capacity.\\n\\nOn May 5, 2026, CAISI [announced agreements with Google DeepMind, Microsoft, and
xAI](https://content.govdelivery.com/accounts/USNIST/bulletins/415cadf?utm_source=chatgpt.com). The agreements provide for pre-deployment evaluations and targeted research concerning frontier-AI
capabilities and security. CAISI had previously developed arrangements involving OpenAI and Anthropic.\\n\\nThis question asks whether that system will broaden to at least two additional developers
during the next several weeks. It does not merely track whether the government discusses AI safety or publishes another benchmark. It tests whether the federal government expands its direct
institutional access to developers\\u2019 models for security testing.\", \"resolution_criteria\": \"This question will resolve as Yes if, after August 10 and before September 3, 2026 ET, a U.S.
federal agency officially announces new or materially expanded voluntary agreements under which a federal agency evaluates frontier models from both OpenAI and Anthropic for cybersecurity, national
security, capabilities, or another explicitly identified frontier-model security risk.\", \"fine_print\": \"* The two companies need not be covered in the same announcement.\\n* Expansions of pre-
existing arrangements count only if the announcement identifies a previously not-covered model family, access arrangement, testing scope, or evaluation domain.\", \"num_forecasters\": 184,
\"community_prediction\": null}, \"cp_history\": {\"post_id\": 45203, \"cp_available\": false, \"reason\": \"Community prediction data is not accessible for this question. This is expected for
questions in the AIB tournament \\u2014 you cannot see the CP for questions you are forecasting. Use prediction market prices and your own analysis instead.\"}, \"links\": {\"question_id\": 45203,
\"links\": []}, \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Let me check for any announcements in the window that's already elapsed (Aug 10–20).

## 🔧 Tool: mcp__search__search


## 🔧 Tool: mcp__search__search


```json
{
  "query": "CAISI NSA frontier model framework companies join announcement mid-August 2026",
  "lanes": [
    "neural"
  ],
  "limit": 8
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"CAISI NSA frontier model framework companies join announcement mid-August 2026\", \"lanes_run\": [\"neural\"], \"web\": [], \"markets\": [], \"news\": [],
\"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [{\"title\": \"US Government Can Now Preview AI Models Before Release \\u2014 EO 14409 CAISI Live\", \"url\":
\"https://witho2.com/news/the-us-government-can-now-preview-ai-models-before-you-can\", \"snippet\": \"US Government Can Now Preview AI Models Before Release \\u2014 EO 14409 CAISI Live\\n\\nClose
Menu\\n\\nHubSpot Lost 12.7% After OpenAI Presence \\u2014 Should You Still Buy It?\\n\\nGrok 4.6 Drops August 7: xAI\\u2019s 1.5T Agent Model, What Business Users Get\\n\\nAI Data Centers Have Raised
US Electricity Bills by $23 Billion\\n\\nFacebook X (Twitter) Instagram\\n\\nFacebook X (Twitter) Instagram\\n\\nUnder Executive Order 14409's CAISI framework, US government agencies can now preview
and evaluate frontier AI models before public releas\", \"highlights\": [\"Under Executive Order 14409's CAISI framework, US government agencies can now preview and evaluate frontier AI models before
public release.\\n...\\nPublished: August 1, 2026, 18:25 IST\\n...\\nExecutive Order 14409\\u2019s 60-day design deadline expired on August 1, 2026, giving the Center for AI Standards and Innovation
(CAISI) and the NSA a finalized voluntary framework for reviewing frontier AI models up to 30 days before they reach enterprise customers. President Trump signed the order, titled \\u201cPromoting
Advanced Artificial Intelligence Innovation and Security,\\u201d on June 2, 2026, and directed agencies to complete the framework within 60 days. OpenAI, Anthropic, and Google received the draft
framework before the deadline. The framework\\u2019s design goal is flagging risks of advanced AI being exploited by China or Russia before public access, according to legal analysis published by
Lexology.\\n...\\nThe framework gives the US government pre-release access to \\u201ccovered frontier models\\u201d for a window of up to 30 days before release to other trusted partners. CAISI,
housed in the Commerce Department, and the NSA conduct the reviews. The classification criteria for covered models involves classified benchmarking; the specific compute threshold is not yet public,
according to Norton Rose Fulbright\\u2019s analysis. The executive order also creates an AI cybersecurity clearinghouse for sharing AI vulnerability information across federal agencies. The order
preserves its voluntary framing in explicit terms: \\u201cNothing shall be construed to authorize creation of any mandatory governmental licensing, pre-clearance, or permitting requirement for the
development, publication, release or distribution of AI models,\\u201d the order states.\\n...\\nThe GPT-5.6 precedent shows how voluntary review became practical pressure before the framework
existed. OpenAI delayed GPT-5.6\\u2019s broader rollout on June 26, 2026 after a US government request \\u2014 an informal arrangement that predated the formal standards, as WithO2 covered when
GPT-5.6\\u2019s government-influenced rollout reshaped OpenAI\\u2019s model lineup. Labs seeking US government contracts have little room to opt out of a review process the government administers. The
framework formalizes that dynamic with a defined reviewer, a defined access window, and a circulated draft that OpenAI, Anthropic, and Google have already seen.\\n...\\nThree consequences follow for
companies buying enterprise AI tools, such as ChatGPT, Claude, and Gemini. First, new frontier model releases may now be sequenced by government security review rather than pure commercial roadmaps,
so feature launches can arrive later than vendor announcements suggest. Second, models flagged during review may be restricted or modified before enterprise release. Third, the framework lands in the
same week as EU AI Act Article 50 enforcement (August 2) \\u2014 a two-hemisphere squeeze in which businesses serving both markets face simultaneous new AI compliance regimes on opposite sides of the
Atlantic.\\n...\\n\\u201cVoluntary\\u201d until it isn\\u2019t. Labs that want US government contracts and cleared the June GPT-5.6 review can\\u2019t really opt out \\u2014 the CAISI framework just
gives an existing dynamic teeth and a process. For businesses buying AI tools, the question isn\\u2019t whether models get reviewed. It\\u2019s whether that review slows down the features you\\u2019re
waiting for.\\n...\\nWithO2 covered this framework at the drafting stage in July, when the White House circulated its voluntary AI standards plan to frontier labs, and reported OpenAI\\u2019s GPT-5.6
lineup changes that followed the government\\u2019s June review request. For the European side of this week\\u2019s regulatory shift, see our coverage of EU AI Act Article 50 chatbot disclosure rules,
enforceable from August 2, 2026.\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null}, {\"title\": \"US Frontier Model Review Framework: EO 14409's August 1 Deadline | Vorp Labs\",
\"url\": \"https://vorplabs.com/ai-regulatory-updates/frontier-model-review-framework\", \"snippet\": \"US Frontier Model Review Framework: EO 14409's August 1 Deadline | Vorp Labs\\n\\nTopic
page\\n\\n# The frontier model review framework: what is due August 1, 2026\\n\\nExecutive Order 14409 gave the government 60 days to design a voluntary process for reviewing the most capable AI
models before release. That clock runs out on August 1. The Information reports a draft has already circulated to OpenAI, Anthropic, and Google, with the NSA and CAISI named as reviewers. This page
separates what the order establ\", \"highlights\": [\"Executive Order 14409 gave the government 60 days to design a voluntary process for reviewing the most capable AI models before release. That
clock runs out on August 1. The Information reports a draft has already circulated to OpenAI, Anthropic, and Google, with the NSA and CAISI named as reviewers. This page separates what the order
establishes from what remains reporting, and tracks the questions the framework has to answer.\\n...\\n### EO 14409 requires the frontier model review framework to be designed within 60 days, which
lands on August 1, 2026.\\n...\\nSection 3 of the order opens with the words \\u201cWithin 60 days of the date of this order\\u201d and assigns the work to the Secretary of the Treasury, the Secretary
of War through the Director of NSA, and the Secretary of Homeland Security through the Director of CISA, in consultation with the White House Chief of Staff through the National Cyber Director, the
Assistant to the President for Science and Technology, and the Secretary of Commerce through the Director of NIST. Sixty days from the June 2 signing is August 1, 2026. The order sets a design
deadline for the government; it imposes no compliance deadline on AI companies.\\n...\\n### A draft framework has circulated to OpenAI, Anthropic, and Google, which jointly submitted
edits.\\n...\\nThe Information reported on July 27, citing three people familiar with the matter, that the White House Office of the National Cyber Director circulated a draft of the framework to
OpenAI, Anthropic, and Google around two weeks earlier, and that the three companies jointly submitted their own edits. No second outlet had independently confirmed the draft's circulation as of this
page's check date, and no agency had published a draft.\\n...\\n### Model reviews under the framework would be conducted by the NSA together with CAISI.\\n...\\nThe Information reported, citing two
people familiar, that the White House has told some companies the reviewing entity will combine the NSA and the Center for AI Standards and Innovation, a NIST body that describes itself as industry's
primary point of contact within the US government for testing and collaborative research on commercial AI systems. CAISI appears nowhere in the executive order, which instead names the Secretary of
Commerce through the Director of NIST as a consulted party, so the reported arrangement is consistent with the order's structure but is established by no official document.\\n...\\nExecutive Order
14409, Promoting Advanced Artificial Intelligence Innovation and Security, directs Treasury, the Department of War through NSA, and DHS through CISA to design a voluntary frontier model review
framework within 60 days. The order pairs the framework with a classified covered-frontier-model benchmarking process, up to 30 days of pre-release federal access, jointly selected trusted partners,
and an express disclaimer of any mandatory licensing or preclearance requirement.\\n...\\n### Report: draft framework circulated, NSA and CAISI to review\\n...\\nThe Information reported that the
administration is close to finalizing the framework, that the Office of the National Cyber Director circulated a draft to OpenAI, Anthropic, and Google around two weeks earlier, that the three jointly
submitted edits, and that the reviewing entity would combine the NSA and CAISI. The report also described open questions inside the companies: how covered frontier models will be defined, whether open
and closed models are treated differently, and what happens to companies that decline to participate.\\n...\\nThe Information reports the White House has named a combination of the NSA and CAISI to
some companies. The order itself assigns designation to the NSA Director and names Commerce through the NIST Director only as a consulted party.\\n...\\nThe 60-day design deadline falls on August 1,
2026. The Information describes the framework as close to final with drafts already exchanged, which is reporting, not publication. Executive-order deadlines of this kind slip without legal
consequence.\\n...\\nthe voluntary process that Executive Order 1440\\n...\\n0 days:\\n...\\nprocess that designates covered frontier models with advanced cyber capabilities, up to\\n...\\n0 days of
pre-release federal access to those models, and collaboration between developers and the government on selecting trusted partners\\n...\\nearly access. Treasury, the Department of War through NSA, and
DHS through CISA are the assigned designers, with the National Cyber Director, the President's science adviser, and Commerce through NIST consulted\\n...\\nAugust 1 is the 60-day deadline EO 14409
sets for designing the framework. It is a deadline for the government, not for AI companies; nothing becomes binding on developers that day. The Information reported on July 27 that a draft had
already circulated to OpenAI, Anthropic, and Google and that the framework was close to final, so the practical question is whether the framework publishes on schedule and in what
form.\\n...\\nDesignation authority sits with the NSA Director under the order. For the reviews themselves, The Information reports, from two people familiar, that the White House has named a
combination of the NSA and CAISI, the Center for AI Standards and Innovation within NIST. That pairing appears in no official document as of this page's check date.\"], \"published_date\":
\"2026-07-27T00:00:00.000\", \"score\": null}, {\"title\": \"Promoting Advanced Artificial Intelligence Innovation and ...\", \"url\": \"https://www.whitehouse.gov/presidential-
actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/\", \"snippet\": \"Promoting Advanced Artificial Intelligence Innovation and Security \\u2013 The White House\\n\\n#
PROMOTING ADVANCED ARTIFICIAL INTELLIGENCE INNOVATION AND SECURITY\\n\\nJune 2, 2026\\n\\nExecutive Order 14409\\n\\nBy the authority vested in me as President by the Constitution and the laws of the
United States of America, it is hereby ordered:\\n\\nSection 1. Purpose. The United States continues to lead the world in Artificial Intelligence (AI) because of the enormous talent and innovation of
our AI industry, and because\", \"highlights\": [\"(c) Within 30 days of the date of this order, the Secretary of Homeland Security, through the Director of the Cybersecurity and Infrastructure
Security Agency (CISA), in consultation with the Director of the Office of Management and Budget (OMB), the Assistant to the President for National Security Affairs, and the National Cyber Director,
shall release Binding Operational Directives and other guidance as appropriate to:\\n...\\n(iii) facilitate access to cybersecurity tools and services including, where appropriate, covered frontier
models for agencies, State and local authorities, and operators of critical infrastructure such as rural hospitals, community banks, and local utilities.\\n...\\n(d) Within 30 days of the date of this
order, the Secretary of the Treasury, in consultation with the National Cyber Director, the Secretary of War, through the Director of the National Security Agency (NSA), and the Secretary of Homeland
Security, through the Director of CISA, shall form an AI cybersecurity clearinghouse, in voluntary collaboration with the AI industry and operators of critical infrastructure, that coordinates and
deconflicts scanning for software vulnerabilities, discovers and validates such vulnerabilities, and coordinates and prioritizes remediation and distribution of vulnerability patches.\\n...\\nSec. 3.
Secure Frontier Model Deployment. Within 60 days of the date of this order, the Secretary of the Treasury, the Secretary of War, through the Director of NSA, and the Secretary of Homeland Security,
through the Director of CISA, in consultation with the White House Chief of Staff, through the National Cyber Director, the Assistant to the President for Science and Technology (APST), and the
Secretary of Commerce, through the Director of the National Institute of Standards and Technology, and in coordination with other agencies, as appropriate, shall:\\n...\\n(a) develop and maintain a
classified benchmarking process to assess the advanced cyber capabilities of AI models and determine the threshold at which an AI model should be designated a \\u201ccovered frontier model\\u201d for
the purposes of this order, sharing such assessments with AI developers and researchers as appropriate. Such a determination shall be made by the Director of NSA, in consultation with the National
Cyber Director, the APST, the Director of CISA, and other representatives of the Department of War, as appropriate.\\n...\\n(b) design a voluntary framework with AI developers through which developers
would be able to:\\n...\\n(i) engage the Federal Government to determine whether model(s) under development meet the designation of \\u201ccovered frontier model\\u201d;\\n...\\n(ii) provide the
Federal Government with access to covered frontier models, subject to appropriate confidentiality, cybersecurity, insider-risk, and intellectual-property protection, use, and nondisclosure
requirements, for a period of up to 30 days before they plan to release such models to other trusted partners; and\\n...\\n(iii) collaborate with the Federal Government to select trusted partners that
will have early access to covered frontier models to promote secure innovation and strengthen the cybersecurity of critical infrastructure.\\n...\\n(c) Nothing in this section shall be construed to
authorize the creation of a mandatory governmental licensing, preclearance, or permitting requirement for the development, publication, release, or distribution of new AI models, including frontier
models.\"], \"published_date\": \"2026-06-02T00:00:00.000\", \"score\": null}, {\"title\": \"White House to implement AI cybersecurity framework with NSA-led benchmarking\", \"url\":
\"https://cryptobriefing.com/white-house-to-implement-ai-cybersecurity-framework-with-nsa-led-benchmarking/\", \"snippet\": \"# White House to implement AI cybersecurity framework with NSA-led
benchmarking\\n\\nAuthor: Estefano Gomez\\nPublished: 2026-08-19T21:48:56+00:00\\nSource: cryptobriefing.com (cryptobriefing.com)\\nLanguage: en\\n\\n## Story\\n\\nWhite House to implement AI
cybersecurity framework with NSA-led benchmarking\\n\\nSEARCH\\n\\nSearching...\\n\\nThis article is delayed 10 minutes. Vera API subscribers got this signal first. Get the live feed at
vera.cryptobriefing.com.\\n\\nGet live feed \\u2192\\n\\nBest AI model by september 2026 \\u2197\\n\\n# White\", \"highlights\": [\"# White House to implement AI cybersecurity framework with NSA-led
benchmarking\\n\\nAuthor: Estefano Gomez\\nPublished: 2026-08-19T21:48:56+00:00\\nSource: cryptobriefing.com (cryptobriefing.com)\\nLanguage: en\\n\\n## Story\\n\\nWhite House to implement AI
cybersecurity framework with NSA-led benchmarking\\n\\nSEARCH\\n\\nSearching...\\n\\nThis article is delayed 10 minutes. Vera API subscribers got this signal first. Get the live feed at
vera.cryptobriefing.com.\\n\\nGet live feed \\u2192\\n\\nBest AI model by september 2026 \\u2197\\n\\n# White House to implement AI cybersecurity framework with NSA-led benchmarking\\n\\n\\u00b7 just
now ago\\n\\nYES 90% 0\\u00a2 since publish\\n\\nhttps://www.cybersecuritydive.com/news/white-house-national-cyber-director-iti-recommendations-paper/757638/\\n\\nby Estefano Gomez| Powered by Vera
Aug. 19, 2026\\n\\nShare\\n\\nShare on X Share on LinkedIn Share on Facebook\\n\\nAdd us on Google\\n\\nThe White House is set to implement an AI cybersecurity framework that includes a classified
benchmarking process led by the National Security Agency (NSA). This initiative, part of Executive Order 14409, aims to ensure rigorous evaluation of \\u201ccovered frontier models.\\u201d The NSA
Director will have the final say on designations, while other agencies, such as CISA, Treasury, and NIST, contribute to the framework. Although the process currently remains voluntary and allows
companies to seek government access for review, the specifics of the classified benchmark remain undisclosed.\\n\\n## Key Takeaways\\n\\n- The announcement appears to suggest a more formalized
evaluation process for AI models, potentially benefiting established companies like Anthropic.\\n- Market pricing suggests participants view this as supporting scenarios where Anthropic\\u2019s AI
model could be ranked best by September 2026.\\n- The involvement of multiple government agencies indicates a comprehensive approach to AI cybersecurity within the framework.\\n\\n## What to
Watch\\n\\nMarkets will likely monitor the details and impact of the classified benchmarking process on AI model evaluations. Key companies, such as Anthropic and its competitors, may adjust their
strategies in response to the NSA\\u2019s role in the framework. Watch for further announcements from the White House or NSA that could provide additional insights into the evaluation criteria and
their potential effects on market probabilities.\\n\\nGet live prediction-market analysis, powered by Vera. Sign up for Vera.\\n\\nTerm Structure\\n\\n| Contract | Odds | \\u0394 since publish |
Volume 24h | |\\n| --- | --- | --- | --- | --- |\\n| September 30 2026 | 90% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.4% | \\u2014 | \\u2014 | View market \\u2192 |\\n|
September 30 2026 | 0.2% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 2.6% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View
market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.2% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 2% | \\u2014
| \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.2% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30
2026 | 3.7% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192
|\\n| September 30 2026 | 0.9% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 |
View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% |
\\u2014 | \\u2014 | View market \\u2192 |\\n| September 30 2026 | 0.1% | \\u2014 | \\u2014 | View market \\u2192 |\\n\\nRelated to This Story\\n\\n\\u25bc AI agents advance interoperability with A2A
protocol integration2d ago\\n\\n\\u25b2 Anthropic\\u2019s Model 2 surpasses Mythos 5, raises AI misalignment concerns5d ago\\n\\n\\u25b2 DeepSeek unveils open-source harness, raises V4-Pro API
prices6d ago\\n\\n\\u25b2 DeepSeek forms team to challenge Anthropic\\u2019s Claude Code with new AI agents6d ago\\n\\n\\u25b2 Sanders urges OpenAI, Anthropic, Meta to pause AI development amid
regulatory push9d ago\\n\\nActive Markets\\n\\n\\u25bc Bitcoin future price predictions 43% \\u25bc0\\u00a2\\n\\n\\u25b2 Solana price predictions for august 16% \\u25b211\\u00a2\\n\\n\\u25bc CLARITY
act signed into law in 2026 25% \\u25bc0\\u00a2\\n\\n\\u25b2 Hyperliquid price predictions for 2026 26% \\u25b21\\u00a2\\n\\n\\u25bc OpenAI valuation by december 31 75% \\u25bc0\\u00a2\\n\\n\\u25bc
Base token launch predictions 2% \\u25bc0\\u00a2\\n\\nVera \\u2014 AI-powered prediction market intelligence, built for serious analysts.\\n\\nSign up for Vera\\n\\nVVera\\n\\n### Get prediction
market intelligence\\n\\nLive prediction-market signals and analysis, powered by Vera.\\n\\nExplore Vera \\u2192\\u00d7\"], \"published_date\": \"2026-08-19T21:48:56.000\", \"score\": null},
{\"title\": \"Trump's AI Executive Order Gives CAISI 30 Days [2026]\", \"url\": \"https://tech-insider.org/trump-ai-executive-order-caisi-2026/\", \"snippet\": \"Trump's AI Executive Order Gives CAISI
30 Days [2026]\\n\\nJuly 24, 2026\\n\\n14 min read\\n\\nPresident Trump signed Executive Order 14409 on June 2, 2026, creating the first voluntary pre-deployment cybersecurity testing framework for
frontier AI models before they reach the public. The order, titled \\u201cPromoting Advanced Artificial Intelligence Innovation and Security,\\u201d asks the companies building the most advanced AI
systems, think OpenAI, Anthropic and Google DeepMind, to volunteer their models for gover\", \"highlights\": [\"President Trump signed Executive Order 14409 on June 2, 2026, creating the first
voluntary pre-deployment cybersecurity testing framework for frontier AI models before they reach the public. The order, titled \\u201cPromoting Advanced Artificial Intelligence Innovation and
Security,\\u201d asks the companies building the most advanced AI systems, think OpenAI, Anthropic and Google DeepMind, to volunteer their models for government review. Agencies get up to 30 days to
look for national security and cybersecurity flaws before a wider release goes ahead.\\n...\\nStrip away the political framing and EO 14409 is a fairly narrow instrument. It directs federal agencies
to build a process through which developers of \\u201ccovered frontier models\\u201d can hand over early access to their systems, voluntarily, for government cybersecurity testing. The Latham &
Watkins summary of the order lays out the mechanics: the NSA director, in consultation with other officials, decides which models qualify as \\u201ccovered,\\u201d a classified benchmarking process
was due within roughly 60 days of signing, and the voluntary engagement framework itself has to be finalized by August 1, 2026.\\n...\\nAccess granted under the order runs for up to 30 days before a
company\\u2019s planned release date, and the text leaves room to extend that access to \\u201cother trusted partners\\u201d under confidentiality, cybersecurity, insider-risk and intellectual-
property protections, according to Crowell & Moring\\u2019s client alert. Treasury, Defense, Commerce and the Department of Homeland Security all get named roles in standing the program up. None of
it, the order stresses more than once, creates a new licensing or permitting requirement for AI development.\\n...\\n| Provision | Detail | Status / Deadline |\\n...\\n| --- | --- | --- |\\n...\\n|
Order number and title | EO 14409, \\u201cPromoting Advanced Artificial Intelligence Innovation and Security\\u201d | Signed June 2, 2026 |\\n...\\n| Framework type\\n...\\nVoluntary pre-
release\\n...\\nNot a licensing regime |\\n| Government testing window | Up to 30 days before public release | Reportedly cut down from a 90-day draft |\\n| Voluntary engagement framework | Agencies
design the formal process for developer participation | Due by August 1, 2026 |\\n...\\n| Classified benchmarking process | NSA director designates \\u201ccovered frontier models\\u201d |
Due\\n...\\n60 days after signing |\\n...\\n-led, coordinates disclosure with AI firms and infrastructure operators | Ongoing implementation |\\n...\\nenabled computer crime | Immediate |\\n...\\n|
None created | Explicitly excluded |\\n...\\nThe body actually expected to run point on evaluations is CAISI, the Center for AI Standards and Innovation, housed under the Commerce Department\\u2019s
National Institute of Standards and Technology. CAISI is the rebranded successor to what was originally stood up as the U.S. AI Safety Institute, repositioned under the current administration with
more of an emphasis on competitiveness and standards work alongside its safety-testing mission.\\n...\\non an informal basis\\n...\\npoint on its\\n...\\nsome of the voluntary information-sharing
this\\n...\\norder formalizes was reportedly already happening before the order existed.\\n...\\nthe order\\u2019s classified benchmarking track could make it\\n...\\ncompanies to know exactly when
and\\n...\\nEO 14409 doesn\\u2019t publish a roster of participating companies, but the \\u201ccovered frontier model\\u201d language points squarely at the same handful of labs that dominate
today\\u2019s capability rankings. Anthropic\\u2019s Claude Opus 4.8, OpenAI\\u2019s GPT-5.6 and Google\\u2019s Gemini 3.1 Pro currently anchor that top tier, with xAI\\u2019s Grok models pushing for
a seat at the same table. Coverage from NPR and Politico both describe OpenAI, Anthropic and Google as already engaged in conversations around the framework, though none of the sources reviewed for
this article confirm a finalized, formal list of enrolled participants.\\n...\\n| Executive Order | Signed | Approach | Core Focus |\\n| --- | --- | --- | --- |\\n| EO 14110 (Biden) | October 30, 2023
| Broad governance, reporting requirements for the largest models | Safety, equity and cross-sector AI risk management |\\n| EO 14179 (Trump) | January 23, 2025 | Deregulatory, rescinded EO 14110 |
Removing barriers to U.S. AI innovation\\n...\\n| EO 1\\n...\\n9 (Trump) | June 2, 202\\n...\\n| Voluntary, narrowly scoped to\\n...\\n| Frontier-model\\n...\\ntesting via CAISI |\\n...\\nCAISI, the
Center for AI Standards and Innovation, is the Commerce Department body expected to lead most model evaluations under the new framework. It is the rebranded successor to the original U.S. AI Safety
Institute and already receives informal information-sharing from labs including OpenAI and Anthropic, according to Politico\\u2019s reporting.\\n...\\nThe order does not name specific companies.
Coverage from NPR and Politico describes OpenAI, Anthropic and Google as engaged in early conversations, and the \\u201ccovered frontier model\\u201d language is widely understood to target the same
handful of labs producing today\\u2019s most capable systems.\\n...\\nFederal agencies are directed to finalize the framework by August 1, 2026. A classified benchmarking process for designating
\\u201ccovered frontier models\\u201d was due roughly 60 days after the order\\u2019s signing.\"], \"published_date\": \"2026-07-24T00:00:00.000\", \"score\": null}, {\"title\": \"The EO Is Voluntary,
Here's Who's Already Inside the CAISI Framework and What Participation Requires - Tech Jacks Solutions\", \"url\": \"https://techjacksolutions.com/ai-brief/the-eo-is-voluntary-heres-whos-already-
inside-the-caisi-fram/\", \"snippet\": \"The EO Is Voluntary, Here's Who's Already Inside the CAISI Framework and What Participation Requires - Tech Jacks Solutions\\n\\n#### Gallery\\n\\n####
Contacts\\n\\n405 W. Greenlawn Ave Lansing, Michigan 48910\\n\\ncontact@techjacksolutions.com\\n\\n+1-616-320-4064\\n\\nTwitter Facebook-f Pinterest-p Instagram\\n\\nSkip to
content\\n\\nRegulation\\n\\nRegulation Deep Dive\\n\\n# The EO Is Voluntary, Here's Who's Already Inside the CAISI Framework and What Participation Requires\\n\\nMay 21, 2026 5 min read Bloomberg Law
Partial\\n\\nTech Jac\", \"highlights\": [\"The AI cybersecurity executive order signed May 21, 2026 is voluntary. That framing has caused compliance teams to underestimate what it actually costs to
stay outside it. Forty-plus evaluations were already complete before Trump signed a word, and the five frontier labs with CAISI agreements aren't there because the law required it.\\n...\\n- The EO
codifies an existing CAISI testing architecture, 40+ evaluations were completed before signing, covering all five frontier labs (OpenAI, Anthropic, Google DeepMind, xAI, Microsoft)\\n...\\n- The
framework is voluntary with no enforcement deadline, but non-participation is now a visible exception in a named federal program with procurement and regulatory risk implications\\n...\\nThat\\u2019s
the number that reframes what this EO actually is. CAISI Director Chris Fall confirmed, per Forbes reporting, that NIST\\u2019s Center for AI Standards and Innovation had completed more than 40 pre-
deployment evaluations of frontier AI models, including models that haven\\u2019t been publicly released, before President Trump signed the cybersecurity executive order on May 21. The EO didn\\u2019t
create the program. It gave it a statutory home.\\n...\\nThe distinction matters for every compliance team at a frontier model developer trying to understand what the order changes for them. The short
answer: the testing infrastructure existed, the lab agreements existed, the evaluation criteria existed. What\\u2019s new is that they\\u2019re now part of a codified federal instrument, and non-
participation has shifted from \\u201cnot yet engaged\\u201d to \\u201cvisibly absent from a named federal program.\\u201d\\n...\\nnot hallucination\\n...\\nera cybersecurity
information-\\n...\\nprograms, programs that governed how\\n...\\ninfrastructure operators, and technology vendors share threat\\n...\\n, to explicitly include\\n...\\nThird, per Nextgov\\u2019s
reporting, the order reportedly gives the NSA a defined role in the voluntary testing architecture, a significant inclusion given the NSA\\u2019s technical depth on offensive cyber capabilities. The
agency\\u2019s involvement signals that the evaluation criteria will be informed by classified threat intelligence, not just publicly known attack patterns.\\n...\\nNone of this is mandatory. The
framework\\n...\\nvoluntary. No lab faces a legal consequence for declining to participate.\\n...\\n, and it\\u2019\\n...\\nframe once you understand who\\u2019s already inside.\\n...\\nAll five named
frontier labs have CAISI evaluation agreements: OpenAI, Anthropic, Google DeepMind, xAI, and Microsoft. Prior TJS reporting confirmed these agreements were in place before this EO was signed. The labs
didn\\u2019t wait for a legislative mandate. They engaged because CAISI offered something the labs\\u2019 internal red teams couldn\\u2019t easily replicate: independent evaluation with access to
classified infrastructure attack patterns.\\n...\\nNSA role definition within voluntary testing architectureQ3 2026\\n...\\nparticipation actually require? Based\\n...\\nthe evaluation structure CAISI
has operated under\\n...\\nlabs provide:\\n...\\n\\u2013 Model access for pre-deployment testing, including unreleased versions \\u2013 Technical documentation sufficient for evaluators to construct
targeted attack scenarios \\u2013 Participation in structured red-team exercises against specified critical infrastructure profiles \\u2013 Acceptance that evaluation results may be shared within the
federal information-sharing architecture\\n...\\nWhat participation doesn\\u2019t require: mandatory publication of results, mandatory remediation before release, or pre-approval for deployment. The
program is an evaluation and intelligence-sharing mechanism, not a certification gate.\\n...\\nVoluntary compliance frameworks in federal AI governance are following the same pattern as voluntary
cybersecurity frameworks in the 2010s: they start with the largest players, establish norms through practice, and eventually create reputational and procurement costs for non-participants that
function as de facto mandates. This EO is the NIST Cybersecurity Framework moment for AI, voluntary today, industry-standard in 1\\n...\\nThe EO codifies the CAISI architecture without mandating it,
track whether NSA integration into the evaluation process produces a de facto classification system for evaluated vs. unevaluated models in federal procurement\\n...\\nConfirm your CAISI agreement
status. If your organization develops frontier AI models and doesn\\u2019t have a formal CAISI evaluation agreement, you\\u2019re now operating as a visible exception in a named federal program. That
changes the procurement and regulatory risk calculation. The engagement path is through NIST\\u2019s CAISI program office directly.\\n...\\nThe real question isn\\u2019t whether this EO is voluntary.
It\\u2019s what voluntary compliance looks like when all five frontier labs are already inside the program and the remaining developers aren\\u2019t. The architecture the EO codifies was built through
agreements, not mandates, and that process happened faster than the legislative process that might have produced a mandate. What follows from this signing is probably not broader mandatory testing.
It\\u2019s broader voluntary enrollment, because the cost of being named as the lab that declined federal cybersecurity evaluation has just become harder to absorb. Expect CAISI\\u2019s agreement
count to grow in the next 90 days.\"], \"published_date\": \"2026-05-21T00:00:00.000\", \"score\": null}, {\"title\": \"President Trump Signs Executive Order Establishing AI ...\", \"url\":
\"https://www.lw.com/en/insights/president-trump-signs-executive-order-establishing-ai-cybersecurity-and-frontier-model-framework\", \"snippet\": \"President Trump Signs Executive Order Establishing
AI Cybersecurity and Frontier Model Framework\\n\\n- skip to Main Content\\n- skip to Footer\\n\\nLatham & Watkins LLP\\n\\n## Key POINTS\\n\\n- The Order directs federal agencies to strengthen
cybersecurity across government systems and critical infrastructure, including through an AI cybersecurity clearinghouse and expanded access to AI-enabled defensive tools for state and local
authorities.\\n- Federal agencies will design a voluntary framework by August 1, 202\", \"highlights\": [\"- The Order directs federal agencies to strengthen cybersecurity across government systems
and critical infrastructure, including through an AI cybersecurity clearinghouse and expanded access to AI-enabled defensive tools for state and local authorities.\\n- Federal agencies will design a
voluntary framework by August 1, 2026, for developers of frontier AI models to engage with the federal government prior to model release.\\n...\\nOrder addresses three principal areas: (1)
strengthening\\n...\\nacross federal systems and\\n...\\ninfrastructure; (2) creating a voluntary pre-release engagement\\n...\\nfor developers of frontier AI systems; and (3) directing the Attorney
General to prioritize enforcement of existing criminal statutes against\\n...\\n, the Order emphasizes voluntary collaboration with the\\n...\\n, mandatory regulations.\\n...\\nThe Order directs an
effort to\\n...\\nfederal cybersecurity and expand access to AI-enabled defensive tools. Within 30 days (i.e., by July 2, 2026), the Committee on National Security Systems and the Secretary of War
must each prioritize the cyber defense of their respective information systems. Likewise, the Secretary of Homeland Security, through the Cybersecurity and Infrastructure Security Agency (CISA), must
issue Binding Operational Directives to expedite the cyber defense of civilian federal systems; establish or expand federal programs that enhance AI-enabled defensive tools; and facilitate access to
cybersecurity tools for agencies, state and local authorities, and critical infrastructure operators such as rural hospitals, community banks, and local utilities.\\n...\\nThe Order directs federal
officials to develop, within 60 days, both a classified benchmarking process for assessing the advanced cyber capabilities of AI models and a voluntary pre-release engagement channel between
developers and the federal government. Critically, the framework is expressly voluntary for developers and does not constitute a mandatory licensing or pre-clearance regime.\\n...\\nThe framework will
apply to \\u201ccovered frontier models,\\u201d although the Order notably leaves that term undefined. Rather, within 60 days, the Secretary of the Treasury, the Secretary of War (through the National
Security Agency), and the Secretary of Homeland Security (through CISA), in consultation with other senior officials and agencies as appropriate, must develop a classified benchmarking process to
assess AI models\\u2019 advanced cyber capabilities and determine the threshold at which AI models will be designated as a \\u201ccovered frontier model\\u201d under the Order. Because the
benchmarking process is classified, AI developers building models with significant cybersecurity-relevant capabilities should anticipate the need to engage with the government to understand whether
their models meet this designation.\\n...\\nThe Order directs that the framework should enable developers to provide government access to their covered frontier models for up to 30 days before the
developer\\u2019s planned release date for the models to \\u201cother trusted partners\\u201d (also an undefined term), subject to appropriate confidentiality, cybersecurity, insider-risk, and
intellectual-property requirements covering protection, use, and nondisclosure. The framework should also enable developers to collaborate with the federal government to select trusted partners that
will have early access to covered frontier models in order to promote secure innovation and strengthen the cybersecurity of critical infrastructure. Notably, the envisioned 30-day window would run
prior to the planned release to these \\u201ctrusted partners\\u201d \\u2014 not to the general public \\u2014 meaning government access would occur at an earlier stage in the distribution chain than
a pre-public-release framework would require. The specific terms of IP and confidentiality protections, as well as the criteria for selecting trusted partners, remain to be
developed.\\n...\\nUnderscoring the voluntary nature of participation in this framework, the Order expressly states that it does not create any mandatory governmental licensing, pre-clearance, or
permitting requirement for the development, publication, release, or distribution of new AI models, including frontier models.\\n...\\nParticipation in the voluntary pre-release framework. The
voluntary framework for pre-release government engagement is due to be finalized by August 1, 2026. While the Order generally contemplates a framework that would guide developers on how to provide the
federal government with access to covered frontier models for up to 30 days before release to \\u201ctrusted partners,\\u201d the specific mechanics, scope, and conditions of that framework have not
yet been designed, making it difficult to assess the potential benefits and drawbacks of voluntary participation at this point.\\n...\\nthe government and developers\\n...\\n\\u201ctrusted
partners\\u201d eligible for\\n...\\nstates that the\\n...\\nthe Order requires\\n...\\ndevelopers who participate\\n...\\n, cybersecurity, insider-\\n...\\n-property protection, use, and
nondisclosure requirements.\\u201d The specifics of those\\n...\\ngovernment access to model weights or other proprietary information will be a material consideration for many developers in deciding
whether or not to participate.\"], \"published_date\": \"2026-06-03T00:00:00.000\", \"score\": null}, {\"title\": \"EO sets voluntary 'early access' framework for AI models\", \"url\":
\"https://www.nortonrosefulbright.com/en-us/knowledge/publications/900af3cf/executive-order-establishes-voluntary-early-access-framework-to-frontier-ai-models\", \"snippet\": \"EO sets voluntary
\\u2018early access\\u2019 framework for AI models | United States | Global law firm | Norton Rose Fulbright\\n\\n---\\n\\nOn June 2, 2026, the White House issued Executive Order 14409 titled
\\u201cPromoting Advanced Artificial Intelligence Innovation and Security\\u201d (the EO). The order focuses on:\\n\\n1. Enhancing the cybersecurity defense of government information systems\\n2.
Creating a voluntary framework for frontier artificial intelligence(AI) models to be accessed by the federal government\\n3. Prioritiz\", \"highlights\": [\"On June 2, 2026, the White House issued
Executive Order 14409 titled \\u201cPromoting Advanced Artificial Intelligence Innovation and Security\\u201d (the EO). The order focuses on:\\n...\\n1. Enhancing the cybersecurity defense of
government information systems\\n2. Creating a voluntary framework for frontier artificial intelligence(AI) models to be accessed by the federal government\\n3. Prioritizing criminal enforcement
against threat actors using AI\\n...\\nThe EO marks another development in the regulation of AI models at the federal level. Executive Order 14365, which we discussed previously, focused on state AI
governance laws, and a subsequent national policy framework (discussed here) focused on recommendations for federal AI governance legislation. This EO, among other things, orders the creation of a
benchmarking process wherein the federal government will assess the \\u201cadvanced cyber capabilities of AI models\\u201d and will determine whether that model should be designated a \\u201ccovered
frontier model.\\u201d It also establishes a voluntary mechanism for developers of frontier AI models to grant the federal government early access to certain covered AI models and to collaborate with
the federal government in selecting \\u201ctrusted partners\\u201d to also give early access. However, the EO does not discuss what incentives will be available for companies electing to participate
in the voluntary framework.\\n...\\nThe EO calls for financial support for applicants developing \\u201cadvanced AI vulnerability detection\\u201d; in other words, to detect cybersecurity
vulnerabilities. The EO directs the Director of the Office of Management and Budget (OMB), the National Cyber Director and the Director of the Cybersecurity and Infrastructure Security Agency (CISA)
to identify available grant programs and funding opportunities to pursue that goal.\\n...\\nThe EO directs several agencies in the executive branch to develop and maintain a \\u201cclassified
benchmarking process\\u201d to assess the \\u201cadvanced cyber capabilities of AI models\\u201d to be used to determine which models should be designated a \\u201ccovered frontier model.\\u201d The
Director of the National Security Agency (NSA) is given the authority to play a central role in those determinations. However, the EO does not specify the technical criteria that will determine when
an AI model crosses the threshold to become a \\u201ccovered frontier model.\\u201d As a result, developers may have limited public guidance, at least initially, on how the government will assess a
model\\u2019s cyber capabilities or what evidence may be relevant to that assessment.\\n...\\nThe EO also calls on several executive-branch agencies to create, by August 1, 2026, a voluntary framework
under which AI developers will provide the federal government advance access to their models that are under development and would be considered \\u201ccovered frontier models.\\u201d Under this
framework, the federal government would be given access to the model for up to 30 days before its release to other trusted partners, and would allow the AI developers and the federal government to
collaborate in selecting which trusted partners would also receive early access. The framework focuses on \\u201ccovered frontier models\\u201d with advanced cybersecurity capabilities, and will
include confidentiality and intellectual property protections. Notably, the EO explicitly states that it is not creating any sort of mandatory licensing, pre-clearance or permitting
mechanism.\\n...\\nThe EO signals a more active federal role in evaluating advanced AI models with cyber capabilities, while continuing to frame that engagement as voluntary rather than mandatory.
Developers of frontier AI models should begin assessing whether their models under development could fall within the future \\u201ccovered frontier model\\u201d designation and, if so, whether the
company is prepared to participate in the voluntary early-access framework. Any existing arrangements and/or agreements the company may have as well as potential evolution of this voluntary regime
into government contract requirements and sectoral regulations may inform such assessment. At this time, the framework does not address the potential benefits available to participating companies,
which may be clarified once agencies issue implementing rules.\\n...\\nFor critical infrastructure operators, the executive order suggests potential new opportunities for early access to the
capabilities of frontier AI models for defensive purposes. As such, monitoring the directives and guidance to be issued by the executive agencies working on implementing the EO over the coming months
will be key to understanding how government access to frontier AI models and relevant eligibility thresholds will be translated in practice.\"], \"published_date\": null, \"score\": null}],
\"social\": [], \"failed\": []}"}]
```

```json
{
  "query": "Anthropic OpenAI government evaluation agreement news week of August 17 2026",
  "lanes": [
    "web"
  ],
  "limit": 5
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"Anthropic OpenAI government evaluation agreement news week of August 17 2026\", \"lanes_run\": [\"web\"], \"web\": [{\"title\": \"White House to host AI
companies Tuesday to review new model-testing framework\", \"url\": \"https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html\", \"snippet\": \"The [White
House](https://www.cnbc.com/white-house/) will host [artificial intelligence](https://www.cnbc.com/ai-artificial-intelligence/) companies Tuesday to discuss a newly completed framework for reviewing
the [cybersecurity capabilities](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-up.html) of the industry's most advanced models, a White House
official confirmed to CNBC.\\nThe meeting will focus on the voluntary framework President [Donal\", \"api_data\": null, \"hint\": null, \"text\": \"The [White House](https://www.cnbc.com/white-house/)
will host [artificial intelligence](https://www.cnbc.com/ai-artificial-intelligence/) companies Tuesday to discuss a newly completed framework for reviewing the [cybersecurity
capabilities](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-up.html) of the industry's most advanced models, a White House official confirmed to
CNBC.\\nThe meeting will focus on the voluntary framework President [Donald Trump](https://www.cnbc.com/donald-trump/) ordered in June, the official said, speaking on condition of anonymity to talk
about the unannounced meeting. The Information first reported the planned meeting.\\nRepresentatives from [Anthropic](https://www.cnbc.com/2026/08/03/eu-ai-act-enforcement-powers.html) are expected to
participate, according to a source familiar with the plans, who spoke on condition of anonymity to talk about the meeting. [OpenAI](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-
deadline-regulation-debate-heats-up.html) and [Google](https://www.cnbc.com/quotes/GOOG/) are also expected to attend, according to The Information. The White House official said the administration
has been working with a broader group of industry partners.\\nTrump's [June 2 executive order](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-
up.html) directed federal officials to create a process through which AI developers could determine whether models under development qualify as \\\"covered frontier models.\\\"\\nUnder the voluntary
program, participating developers could provide the [government access to those models](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html) for as long as 30 days before
making them available to other trusted partners.\\nThe administration has said the [early access](https://www.cnbc.com/video/2026/06/02/trump-signs-ai-executive-order-asking-companies-to-give-
government-\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/2f9b3f158a9a.txt]\"}, {\"title\": \"OpenAI and Anthropic Are
Writing the Threshold Their Rivals Must Clear for Launch\", \"url\": \"https://www.techtimes.com/articles/321917/20260728/openai-anthropic-are-writing-threshold-their-rivals-must-clear-launch.htm\",
\"snippet\": \"![OpenAI and Anthropic Are Writing the Threshold Their Rivals Must Clear for Launch](https://d.techtimes.com/en/full/470217/openai-anthropic-are-writing-threshold-their-rivals-must-
clear-launch.jpg?w=836&f=23a7182ab9031d8338dd336d6f68b6f1)\\nWith three days left before the first formal deadline in U.S. history for government oversight of frontier AI model releases, OpenAI and
Anthropic have been working together in Washington to shape the rules \\u2014 quietly, behind closed doors, and without disclosin\", \"api_data\": null, \"hint\": null, \"text\": \"![OpenAI and
Anthropic Are Writing the Threshold Their Rivals Must Clear for Launch](https://d.techtimes.com/en/full/470217/openai-anthropic-are-writing-threshold-their-rivals-must-clear-
launch.jpg?w=836&f=23a7182ab9031d8338dd336d6f68b6f1)\\nWith three days left before the first formal deadline in U.S. history for government oversight of frontier AI model releases, OpenAI and
Anthropic have been working together in Washington to shape the rules \\u2014 quietly, behind closed doors, and without disclosing the full terms they want included. The two companies have been
pushing the Trump administration to adopt a consistent federal review process for the most powerful AI models, one that would apply not just to themselves but to rivals they compete against every day:
Meta, and Elon Musk's xAI, according to a [coordinated push for cross-industry standards](https://crypto.news/openai-anthropic-push-30-day-review-frontier-ai-models/) reported by The
Information.\\nThe same day that coordination was reported, more than 1,100 employees across OpenAI, Anthropic, Google, Meta, and nearly a dozen other firms circulated an [open letter on AI
pacing](https://www.aol.com/articles/tech-employees-call-us-backed-220244000.html) calling on the U.S. government to support an international mechanism to deliberately pace AI development \\u2014
because, they warned, there is \\\"a real risk\\\" that AI progresses faster than people can \\\"understand or control.\\\"\\nTogether, those two developments on July 28 painted the clearest picture
yet of where the U.S. AI industry stands as the government's August 1 framework deadline approaches: the leading labs want predictable rules, they want those rules applied to everyone, and a
significant portion of their own workforces now publicly agrees that the technology may be outrunning governance.\\nThe Rivals' Shared Position \\u2014 and Its Competitive Logic\\nOpenAI and Anthropic
are not natural allies. They sell competing AI platforms targeting the same enterprise customers, fight fo\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/90600ffd06f8.txt]\"}, {\"title\": \"Federal Government and Anthropic: Considerations for AI Innovation and Competition | Congress.gov |
Library of Congress\", \"url\": \"https://www.congress.gov/crs-product/IF13217\", \"snippet\": null, \"api_data\": null, \"hint\": null, \"text\": null}, {\"title\": \"Our agreement with the
Department of War | OpenAI\", \"url\": \"https://openai.com/index/our-agreement-with-the-department-of-war/\", \"snippet\": \"Our agreement with the Department of War\\nUpdate on March 2,
2026\\nThroughout our discussions, the Department made clear it shares our commitment to ensuring our tools will not be used for domestic surveillance. To make our principles as clear as possible, we
worked together to add additional language to our agreement.\\nThis language makes explicit that our tools will not be used to conduct domestic surveillance of U.S. persons, including through the
procurement or use of commercially acquired pers\", \"api_data\": null, \"hint\": null, \"text\": \"Our agreement with the Department of War\\nUpdate on March 2, 2026\\nThroughout our discussions, the
Department made clear it shares our commitment to ensuring our tools will not be used for domestic surveillance. To make our principles as clear as possible, we worked together to add additional
language to our agreement.\\nThis language makes explicit that our tools will not be used to conduct domestic surveillance of U.S. persons, including through the procurement or use of commercially
acquired personal or identifiable information. The Department also affirmed that our services will not be used by Department of War intelligence agencies like the NSA. Any services to those agencies
would require a new agreement.\\nThe new language reads:\\n- Consistent with applicable laws, including the Fourth Amendment to the United States Constitution, National Security Act of 1947, FISA Act
of 1978, the AI system shall not be intentionally used for domestic surveillance of U.S. persons and nationals.\\n- For the avoidance of doubt, the Department understands this limitation to prohibit
deliberate tracking, surveillance, or monitoring of U.S. persons or nationals, including through the procurement or use of commercially acquired personal or identifiable information.\\nThe Department
of War plans to convene a working group made up of leaders from the frontier AI labs, cloud providers, and the Department\\u2019s policy and operational communities. OpenAI will participate and expect
this will be an important forum for ongoing dialogue on emerging AI capabilities, privacy, and national security challenges going forward.\\nThese updates build on the framework we announced last week
and we hope will help create a pathway for other labs to work with the Department going forward.\\nYesterday we reached an agreement with the Pentagon for deploying advanced AI systems in classified
environments, which we requested they also make available to all AI companies.\\nWe think our agreement has more guardrails than any p\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/8811c32ed894.txt]\"}, {\"title\": \"White House won't publicly release AI model evaluation framework it reviewed today with Meta, Nvidia,
Microsoft, OpenAI, Anthropic, variety of smaller companies | Fortune\", \"url\": \"https://fortune.com/2026/08/04/baffling-white-house-wont-publicly-release-ai-model-evaluation-framework-it-reviewed-
today-with-openai-anthropic-microsoft-and-others/\", \"snippet\": \"The White House has no plans to publicly reveal the framework it\\u2019s been working on for how it will vet frontier AI models
prior to release. Instead, the details will be kept under wraps, only known to a select group of companies that may choose to participate in the process, which is voluntary.\\nSeveral major tech
companies traveled to Washington, D.C., today for a meeting to review the current draft of the proposal. Attendees included [Meta](https://fortune.com/company/facebook/), [Nvidia](https\",
\"api_data\": null, \"hint\": null, \"text\": \"The White House has no plans to publicly reveal the framework it\\u2019s been working on for how it will vet frontier AI models prior to release.
Instead, the details will be kept under wraps, only known to a select group of companies that may choose to participate in the process, which is voluntary.\\nSeveral major tech companies traveled to
Washington, D.C., today for a meeting to review the current draft of the proposal. Attendees included [Meta](https://fortune.com/company/facebook/), [Nvidia](https://fortune.com/company/nvidia/),
[Microsoft](https://fortune.com/company/microsoft/), OpenAI, Anthropic, and a variety of smaller companies, according to sources familiar with the matter. Fortune is first to report that Microsoft was
in attendance.\\nThe administration issued an [executive order ](https://www.whitehouse.gov/presidential-actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/)on June 2
mandating the creation of this framework within 60 days, or by Aug. 1. The directive seeks to define which models are eligible for review, and instructs the AI labs that they have \\u201cup to 30
days\\u201d to submit them to the government prior to their public release.\\nThe secrecy surrounding the framework may not instill public confidence in the government\\u2019s ability to vet and
secure powerful AI models, especially after OpenAI confirmed its models [hacked](https://fortune.com/2026/07/21/openai-says-ai-models-escaped-control-hacked-hugging-face/) into another company,
Hugging Face, last month. Anthropic later [confirmed](https://fortune.com/2026/07/31/anthropic-claude-escaped-test-hacked-three-companies-openai/) its models had done the same three times.\\nThe fact
that the process is voluntary raises questions about how the administration will enforce it. Per the executive order, the framework is not a \\u201cmandatory governmental licensing, preclearance, or
permitting requirement for the development, publication, release, or distribution of new AI models, including fro\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/e16b782e12a5.txt]\"}], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [],
\"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Let me verify nothing has already happened in the Aug 10–20 window and check NIST's news feed directly.

## 🔧 Tool: mcp__search__fetch


## 🔧 Tool: mcp__search__search


```json
{
  "ref": "https://www.nist.gov/news-events/news/2026/08",
  "at": "2026-08-19",
  "prompt": "List NIST news items from August 2026 with dates and titles, especially CAISI or AI-related."
}
```

### 📋 Result

```
No archived snapshot of https://www.nist.gov/news-events/news/2026/08 at or before 2026-08-19
```

```json
{
  "query": "\"CAISI\" OR \"Center for AI Standards and Innovation\" announcement agreement Anthropic OpenAI expanded testing scope new",
  "lanes": [
    "news",
    "social"
  ],
  "limit": 10
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"\\\"CAISI\\\" OR \\\"Center for AI Standards and Innovation\\\" announcement agreement Anthropic OpenAI expanded testing scope new\", \"lanes_run\": [],
\"web\": [], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [], \"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 🔧 Tool: mcp__search__fetch


## 🔧 Tool: mcp__search__search


```json
{
  "ref": "https://www.nist.gov/caisi",
  "prompt": "List all news items, announcements, and dates listed on this CAISI page, especially anything from August 2026."
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"ref\": \"https://www.nist.gov/caisi\", \"url\": \"https://www.nist.gov/caisi\", \"title\": \"Center for AI Standards and Innovation (CAISI)\", \"content\": \"Based on the
provided content, this page does not contain a news feed, announcement list, or dated entries. It consists of a brief description of CAISI's mission and a single embedded link.\\n\\n**Items
found:**\\n- One reference item: \\\"Read the statement\\\" \\u2014 a link to a statement from U.S. Secretary of Commerce Howard Lutnick about the Center for AI Standards and Innovation. The only date
signal is in the URL path itself (`/2025/06/`), indicating it was published **June 2025**.\\n\\n**August 2026:** No dates, news items, or announcements from August 2026 appear anywhere in this
content.\\n\\nNo other news items, dates, or announcements are present in the text provided.\\n\\nRelevant links:\\n- [Statement from Secretary of Commerce Howard Lutnick on Transforming U.S.
AI](https://www.commerce.gov/news/press-releases/2025/06/statement-us-secretary-commerce-howard-lutnick-transforming-us-ai)\\n- [NIST CAISI page](https://www.nist.gov/caisi)\", \"structured_data\":
[], \"routed\": null, \"paper\": null, \"archived_at\": null}"}]
```

```json
{
  "query": "frontier AI model government review framework news August 18 2026 OpenAI Anthropic sign",
  "lanes": [
    "web"
  ],
  "limit": 5
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"frontier AI model government review framework news August 18 2026 OpenAI Anthropic sign\", \"lanes_run\": [\"web\"], \"web\": [{\"title\": \"OpenAI, Anthropic
push 30-day review for frontier AI models\", \"url\": \"https://crypto.news/openai-anthropic-push-30-day-review-frontier-ai-models/\", \"snippet\": \"OpenAI, Anthropic push 30-day review for frontier
AI models\\n![OpenAI, Anthropic push 30-day review for frontier AI models - 1](https://media.crypto.news/2026/07/ai1-1380x776.webp)\\nOpenAI and Anthropic are working together in Washington to shape a
federal review system for advanced AI models, despite competing for customers, funding, and technological leadership.\\n- OpenAI and Anthropic support up to 30 days of federal access before some
frontier model releases.\\n- The proposed process would apply \", \"api_data\": null, \"hint\": null, \"text\": \"OpenAI, Anthropic push 30-day review for frontier AI models\\n![OpenAI, Anthropic push
30-day review for frontier AI models - 1](https://media.crypto.news/2026/07/ai1-1380x776.webp)\\nOpenAI and Anthropic are working together in Washington to shape a federal review system for advanced
AI models, despite competing for customers, funding, and technological leadership.\\n- OpenAI and Anthropic support up to 30 days of federal access before some frontier model releases.\\n- The
proposed process would apply across the industry, including rivals such as Meta and xAI.\\n- Federal agencies must develop the framework by Aug. 1 under a June executive order.\\n- Nvidia, Meta, and
Microsoft separately warned against sweeping controls on open-weight AI models.\\nOpenAI and Anthropic seek common review standards\\nOpenAI and Anthropic are urging the Trump administration to adopt
a consistent review process for AI models with advanced cybersecurity or national security capabilities, according to [The Information](https://www.theinformation.com/newsletters/ai-agenda/openai-
anthropic-quietly-teaming-washington).\\nTheir cooperation comes before an Aug. 1 deadline for federal agencies to define which systems should qualify as \\u201ccovered frontier models.\\u201d Those
models could be provided to the government for evaluation for up to 30 days before release to other trusted partners.\\nBoth companies reportedly want the standards applied across the AI industry
rather than limited to developers already cooperating with Washington. That could bring competing companies, including Meta and Elon Musk\\u2019s xAI, under the same review framework if their models
cross the eventual capability threshold.\\nThe discussions mark a rare policy alignment between OpenAI and Anthropic. Both companies sell general-purpose AI systems and compete for enterprise
contracts, researchers, computing capacity, and investment.\\nNeither company has publicly released the full terms it wants included in the final framework.\\nTrump order sets voluntar\\n\\n[...
continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/cba8a569e75e.txt]\"}, {\"title\": \"Five Questions the US Government Should Answer About
Its Secretive Frontier AI Framework | TechPolicy.Press\", \"url\": \"https://www.techpolicy.press/five-questions-the-us-government-should-answer-about-its-secretive-frontier-ai-framework/\",
\"snippet\": \"Five Questions the US Government Should Answer About Its Secretive Frontier AI Framework\\nMichelle De Mooy / Aug 5, 2026Michelle De Mooy is an AI governance and policy consultant and
researcher. She is a member of the Board of Advisors for the [Ethical Tech
Project](https://www.ethicaltechproject.org/).\\n![](https://cdn.sanity.io/images/3tzzh18d/production/02778ce78b2ed027077d2b83c8a97374c26038f6-1200x675.png)\\nAerial view of the work on White House
Helipad on August 1, 2026 in Washington, D.C. Cre\", \"api_data\": null, \"hint\": null, \"text\": \"Five Questions the US Government Should Answer About Its Secretive Frontier AI Framework\\nMichelle
De Mooy / Aug 5, 2026Michelle De Mooy is an AI governance and policy consultant and researcher. She is a member of the Board of Advisors for the [Ethical Tech
Project](https://www.ethicaltechproject.org/).\\n![](https://cdn.sanity.io/images/3tzzh18d/production/02778ce78b2ed027077d2b83c8a97374c26038f6-1200x675.png)\\nAerial view of the work on White House
Helipad on August 1, 2026 in Washington, D.C. Credit: mpi34/MediaPunch /IPX\\nIn June, President Donald Trump issued [Executive Order 14409](https://www.whitehouse.gov/presidential-
actions/2026/06/promoting-advanced-artificial-intelligence-innovation-and-security/), \\u201cPromoting Artificial Intelligence Innovation and Security.\\u201d Among its directions was a provision
instructing a National Security Agency-led group within the government to develop a framework under which AI developers give the government access to their models for up to thirty days before release.
There is no requirement for public disclosure of what the group does to assess models, and in fact the White House [now says](https://www.axios.com/2026/08/04/white-house-ai-framework-under-wraps) it
will keep the framework a secret.\\nThe framework was due to be complete this week. It appears that in the last eight weeks, the process for its development has operated informally, without published
criteria, defined timelines, or any legal basis beyond the government applying pressure and labs likely calculating that resisting costs more than complying. This period also included a nineteen-day
[shutdown](https://www.globalgovernmentforum.com/us-forces-anthropic-to-shut-down-latest-ai-models-citing-national-security-concerns/)) of Anthropic's frontier models via an export control order, a
two-week gated [rollout](https://www.cnbc.com/2026/07/08/openai-expanding-gpt-5point6-ai-model-release-ending-government-limits.html) of OpenAI's GPT-5.6, and a limited set of approved acces\\n\\n[...
continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/679468f934c3.txt]\"}, {\"title\": \"OpenAI and Anthropic Are Writing the Threshold Their
Rivals Must Clear for Launch\", \"url\": \"https://www.techtimes.com/articles/321917/20260728/openai-anthropic-are-writing-threshold-their-rivals-must-clear-launch.htm\", \"snippet\": \"![OpenAI and
Anthropic Are Writing the Threshold Their Rivals Must Clear for Launch](https://d.techtimes.com/en/full/470217/openai-anthropic-are-writing-threshold-their-rivals-must-clear-
launch.jpg?w=836&f=23a7182ab9031d8338dd336d6f68b6f1)\\nWith three days left before the first formal deadline in U.S. history for government oversight of frontier AI model releases, OpenAI and
Anthropic have been working together in Washington to shape the rules \\u2014 quietly, behind closed doors, and without disclosin\", \"api_data\": null, \"hint\": null, \"text\": \"![OpenAI and
Anthropic Are Writing the Threshold Their Rivals Must Clear for Launch](https://d.techtimes.com/en/full/470217/openai-anthropic-are-writing-threshold-their-rivals-must-clear-
launch.jpg?w=836&f=23a7182ab9031d8338dd336d6f68b6f1)\\nWith three days left before the first formal deadline in U.S. history for government oversight of frontier AI model releases, OpenAI and
Anthropic have been working together in Washington to shape the rules \\u2014 quietly, behind closed doors, and without disclosing the full terms they want included. The two companies have been
pushing the Trump administration to adopt a consistent federal review process for the most powerful AI models, one that would apply not just to themselves but to rivals they compete against every day:
Meta, and Elon Musk's xAI, according to a [coordinated push for cross-industry standards](https://crypto.news/openai-anthropic-push-30-day-review-frontier-ai-models/) reported by The
Information.\\nThe same day that coordination was reported, more than 1,100 employees across OpenAI, Anthropic, Google, Meta, and nearly a dozen other firms circulated an [open letter on AI
pacing](https://www.aol.com/articles/tech-employees-call-us-backed-220244000.html) calling on the U.S. government to support an international mechanism to deliberately pace AI development \\u2014
because, they warned, there is \\\"a real risk\\\" that AI progresses faster than people can \\\"understand or control.\\\"\\nTogether, those two developments on July 28 painted the clearest picture
yet of where the U.S. AI industry stands as the government's August 1 framework deadline approaches: the leading labs want predictable rules, they want those rules applied to everyone, and a
significant portion of their own workforces now publicly agrees that the technology may be outrunning governance.\\nThe Rivals' Shared Position \\u2014 and Its Competitive Logic\\nOpenAI and Anthropic
are not natural allies. They sell competing AI platforms targeting the same enterprise customers, fight fo\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/90600ffd06f8.txt]\"}, {\"title\": \"White House to host AI companies Tuesday to review new model-testing framework\", \"url\":
\"https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html\", \"snippet\": \"The [White House](https://www.cnbc.com/white-house/) will host [artificial
intelligence](https://www.cnbc.com/ai-artificial-intelligence/) companies Tuesday to discuss a newly completed framework for reviewing the [cybersecurity
capabilities](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-up.html) of the industry's most advanced models, a White House official confirmed to
CNBC.\\nThe meeting will focus on the voluntary framework President [Donal\", \"api_data\": null, \"hint\": null, \"text\": \"The [White House](https://www.cnbc.com/white-house/) will host [artificial
intelligence](https://www.cnbc.com/ai-artificial-intelligence/) companies Tuesday to discuss a newly completed framework for reviewing the [cybersecurity
capabilities](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-up.html) of the industry's most advanced models, a White House official confirmed to
CNBC.\\nThe meeting will focus on the voluntary framework President [Donald Trump](https://www.cnbc.com/donald-trump/) ordered in June, the official said, speaking on condition of anonymity to talk
about the unannounced meeting. The Information first reported the planned meeting.\\nRepresentatives from [Anthropic](https://www.cnbc.com/2026/08/03/eu-ai-act-enforcement-powers.html) are expected to
participate, according to a source familiar with the plans, who spoke on condition of anonymity to talk about the meeting. [OpenAI](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-
deadline-regulation-debate-heats-up.html) and [Google](https://www.cnbc.com/quotes/GOOG/) are also expected to attend, according to The Information. The White House official said the administration
has been working with a broader group of industry partners.\\nTrump's [June 2 executive order](https://www.cnbc.com/2026/07/31/trump-ai-executive-order-nears-key-deadline-regulation-debate-heats-
up.html) directed federal officials to create a process through which AI developers could determine whether models under development qualify as \\\"covered frontier models.\\\"\\nUnder the voluntary
program, participating developers could provide the [government access to those models](https://www.cnbc.com/2026/07/17/white-house-ai-access-anthropic-openai.html) for as long as 30 days before
making them available to other trusted partners.\\nThe administration has said the [early access](https://www.cnbc.com/video/2026/06/02/trump-signs-ai-executive-order-asking-companies-to-give-
government-\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/2f9b3f158a9a.txt]\"}, {\"title\": \"White House to meet with
OpenAI, Anthropic and other top AI companies in first big regulation push | CNN Business\", \"url\": \"https://edition.cnn.com/2026/08/03/tech/white-house-meet-with-top-ai-companies-big-regulation-
push\", \"snippet\": \"The White House will meet with representatives from several top AI companies on Tuesday to discuss a new framework for the government to review frontier AI models before they
launch, multiple sources familiar with the invitation told CNN.\\nThe meeting is a critical step toward broader AI regulation amid growing calls from both AI companies and Washington for more control
over the pace of AI development. Though the framework was laid out as part of an executive order signed by President Donald Tru\", \"api_data\": null, \"hint\": null, \"text\": \"The White House will
meet with representatives from several top AI companies on Tuesday to discuss a new framework for the government to review frontier AI models before they launch, multiple sources familiar with the
invitation told CNN.\\nThe meeting is a critical step toward broader AI regulation amid growing calls from both AI companies and Washington for more control over the pace of AI development. Though the
framework was laid out as part of an executive order signed by President Donald Trump in June, the gathering comes just days after OpenAI and Anthropic both reported incidents of AI agents going rogue
and hacking into other companies\\u2019 systems.\\nThe new system is meant to give the government access to the most advanced AI models up to 30 days before they\\u2019re released publicly, according
to the executive order. The government has emphasized that participation from the industry is voluntary, although the administration has taken steps in recent months to prevent or [delay the release
of](https://www.cnn.com/2026/06/25/tech/openai-limit-release-white-house) advanced AI models for safety reasons.\\n\\u201cThe voluntary framework outlined in the June 2nd executive order is complete.
Discussions with industry about next steps are underway,\\u201d a White House official told CNN on Monday.\\nAmong the companies attending Tuesday are OpenAI, Anthropic, Google and Meta, according to
multiple sources familiar with the situation. Anthropic, Google and Meta declined to comment on the meeting. OpenAI pointed CNN to a [blog post](https://openaiglobalaffairs.substack.com/p/keeping-
america-out-in-front-on-ai?r=4a2ejy) posted Monday by Chief Global Affairs Officer Chris Lehane, reiterating calls for national AI standards established through Congress.\\n\\u201cThe
Administration\\u2019s expected action this week on frontier AI could be an important step toward closing the gap between innovation and governance: a clear, credible, national framework for
evaluating the most advanced AI systems, with defined cr\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/fb50621951ee.txt]\"}], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [],
\"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Let me check the most recent window (Aug 10–20) specifically and alternative agency pathways.

## 🔧 Tool: mcp__search__search


## 🔧 Tool: mcp__search__search


```json
{
  "query": "White House frontier AI framework next steps companies enrolled participation announced August 2026",
  "lanes": [
    "neural"
  ],
  "limit": 6
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"White House frontier AI framework next steps companies enrolled participation announced August 2026\", \"lanes_run\": [\"neural\"], \"web\": [], \"markets\":
[], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [{\"title\": \"White House finalizes AI framework behind closed doors\", \"url\":
\"https://www.axios.com/2026/08/03/white-house-finalizes-ai-framework-behind-closed-doors\", \"snippet\": \"White House finalizes AI framework behind closed doors\\n\\nAug 3, 2026 - Technology\\n\\n#
White House finalizes AI framework behind closed doors\\n\\nAdd Axios on Google\\n\\nAdd Axios as your preferred source to\\n\\nsee more of our stories on Google.\\n\\nAdd Axios on
Google\\n\\nIllustration: Allie Carl/Axios\\n\\nThe White House said on Monday it met its deadline to establish a voluntary framework for evaluating advanced AI models \\u2014 but it won't say what
the framework contains, who's seen it or when companies will start \", \"highlights\": [\"White House finalizes AI framework behind closed doors\\n\\nAug 3, 2026 - Technology\\n\\n# White House
finalizes AI framework behind closed doors\\n\\nAdd Axios on Google\\n\\nAdd Axios as your preferred source to\\n\\nsee more of our stories on Google.\\n\\nAdd Axios on Google\\n\\nIllustration: Allie
Carl/Axios\\n\\nThe White House said on Monday it met its deadline to establish a voluntary framework for evaluating advanced AI models \\u2014 but it won't say what the framework contains, who's seen
it or when companies will start using it.\\n\\nWhy it matters: The framework is being closely watched beyond the industry players it directly applies to.\\n\\n- Policymakers, AI safety advocates and
U.S. allies have been waiting to see what the rules for the most powerful models in the world look like.\\n\\nWhat they're saying: \\\"The voluntary framework outlined in the June 2nd executive order
was complete by the deadline,\\\" a White House official said.\\n\\n- \\\"Discussions with industry about next steps are underway,\\\" the official said, adding that the administration is engaging
with \\\"many more\\\" industry partners than just Anthropic, OpenAI and Google.\\n- Leading up to the deadline, the three labs gave the administration feedback on a draft of the
framework.\\n\\nWhat's inside: The framework is meant to give AI developers a structure for engaging the government to determine whether models under development would be covered.\\n\\n- The framework
is supposed to spell out the confidentiality, cybersecurity, insider-risk, intellectual-property protection, use and nondisclosure requirements that would apply when the government gets access to
models for up to 30 days before they're released.\\n- The framework should also include which \\\"trusted partners\\\" will have early access to models.\\n\\nZoom in: The executive order explicitly
says the benchmarking process to assess advanced cyber capabilities of AI models will be classified.\\n\\n- The threshold for which models are covered under the order is also classified and will only
be shared with AI developers and researchers \\\"as appropriate.\\\"\\n- The order does not similarly designate the voluntary framework as classified, and policymakers and other observers expected to
see details.\\n\\nBetween the lines: Companies are seeking clarity early so they know whether models under development are likely to fall under the framework.\\n\\n- \\\"Just because things are
unclassified that doesn't mean we are going to broadcast them to everyone,\\\" the White House official said.\\n\\nWhat's next: The White House will hold a staff-level meeting with companies on
Tuesday to review the framework, a source familiar said.\\n\\nAdd Axios on Google\\n\\n##### What to read next\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null}, {\"title\":
\"White House plans to keep AI framework under wraps\", \"url\": \"https://www.axios.com/2026/08/04/white-house-ai-framework-under-wraps\", \"snippet\": \"White House plans to keep AI framework under
wraps\\n\\nAug 4, 2026 - Technology\\n\\n# White House plans to keep AI framework under wraps\\n\\nAdd Axios on Google\\n\\nAdd Axios as your preferred source to\\n\\nsee more of our stories on
Google.\\n\\nAdd Axios on Google\\n\\nIllustration: Lindsey Bailey/Axios\\n\\nThe White House does not plan to publicly release its new framework for evaluating advanced AI models, three sources
familiar with the discussions told Axios.\\n\\nWhy it matters: The voluntary framework has global impl\", \"highlights\": [\"White House plans to keep AI framework under wraps\\n\\nAug 4, 2026 -
Technology\\n\\n# White House plans to keep AI framework under wraps\\n\\nAdd Axios on Google\\n\\nAdd Axios as your preferred source to\\n\\nsee more of our stories on Google.\\n\\nAdd Axios on
Google\\n\\nIllustration: Lindsey Bailey/Axios\\n\\nThe White House does not plan to publicly release its new framework for evaluating advanced AI models, three sources familiar with the discussions
told Axios.\\n\\nWhy it matters: The voluntary framework has global implications for AI security, but details will only be made available to the companies that are part of the process.\\n\\n- Keeping
it private means companies, policymakers, researchers and U.S. allies outside the process will be left guessing how the administration plans to implement one of its key AI policies.\\n\\nDriving the
news: The White House on Tuesday held staff-level meetings with industry to go over the recently completed framework. Companies that weren't invited remain in the dark about its contents.\\n\\n- The
AI framework comes as industry grapples with high-profile cyber-attacks and rapid advances by Chinese AI developers, reigniting a debate on how to deal with open-source models.\\n- It's also unclear
which \\\"trusted partners\\\" will get early access to advanced models under the framework, including whether any foreign governments would qualify. The European Union declined to comment and the
U.K. did not respond to multiple requests for comment.\\n- The White House declined to comment.\\n\\nZoom in: Open-source models were discussed, sources familiar said, without elaborating. Nvidia
staff participated in the meetings, the sources added.\\n\\n- Nvidia CEO and open-source advocate Jensen Huang was in D.C. last week meeting with Commerce Secretary Howard Lutnick and President
Trump.\\n\\nCatch up quick: The voluntary framework, outlined in a June executive order, is intended to give AI developers a process for working with the government to determine whether models under
development fall within its scope.\\n\\n- It is also expected to set the rules for government access to AI models up to 30 days before release, covering confidentiality, cybersecurity, insider-risk,
intellectual property and nondisclosure requirements.\\n- The executive order explicitly says the benchmarking process to assess advanced cyber capabilities of AI models will be classified.\\n- There
is no requirement in the order to publicly release the voluntary framework.\\n\\nAdd Axios on Google\\n\\n##### What to read next\"], \"published_date\": \"2026-08-04T00:00:00.000\", \"score\": null},
{\"title\": \"White House won\\u2019t publicly release AI model evaluation framework it reviewed today with Meta, Nvidia, Microsoft, OpenAI, Anthropic, variety of smaller companies | Fortune\",
\"url\": \"https://fortune.com/2026/08/04/baffling-white-house-wont-publicly-release-ai-model-evaluation-framework-it-reviewed-today-with-openai-anthropic-microsoft-and-others/\", \"snippet\": \"White
House won\\u2019t publicly release AI model evaluation framework it reviewed today with Meta, Nvidia, Microsoft, OpenAI, Anthropic, variety of smaller companies | Fortune\\n\\n# Trendingnow\\n\\n#
1\\n\\nIran has Trump right where it wants him and suggests he seek 'a dignified exit'\\n\\n# 2\\n\\nTop economist on Trump's 'deadly cocktail' for the bond market\\u2014and how the bond vigilantes
have crossed Scott Bessent's 'red line'\\n\\n# 3\\n\\nCurrent price of oil as of August 19, 2026\\n\\n# \\u2018Baffling\\u2019: White House won\\u2019t publicly \", \"highlights\": [\"White House
won\\u2019t publicly release AI model evaluation framework it reviewed today with Meta, Nvidia, Microsoft, OpenAI, Anthropic, variety of smaller companies | Fortune\\n\\n# Trendingnow\\n\\n#
1\\n\\nIran has Trump right where it wants him and suggests he seek 'a dignified exit'\\n\\n# 2\\n\\nTop economist on Trump's 'deadly cocktail' for the bond market\\u2014and how the bond vigilantes
have crossed Scott Bessent's 'red line'\\n\\n# 3\\n\\nCurrent price of oil as of August 19, 2026\\n\\n# \\u2018Baffling\\u2019: White House won\\u2019t publicly release AI model evaluation framework
it reviewed today with OpenAI, Anthropic, Microsoft, and others\\n\\nBy\\n\\nEmily Forlini\\n\\nSenior AI Reporter\\n\\nBy\\n\\nEmily Forlini\\n\\nSenior AI Reporter\\n\\nAugust 4, 2026, 6:53 PM
ET\\n\\nPresident Donald Trump during a cabinet meeting, July 31, 2026.Aaron Schwartz\\u2014AFP/Getty Images\\n\\nAdd Fortune on Google for similar content.\\n\\nAdd us on Google\\n\\nAdd us on
Google\\n\\nThe White House has no plans to publicly reveal the framework it\\u2019s been working on for how it will vet frontier AI models prior to release. Instead, the details will be kept under
wraps, only known to a select group of companies that may choose to participate in the process, which is voluntary.\\n\\n---\\n\\nAbout the Author\\n\\nBy Emily Forlini Senior AI Reporter\\n\\nSee
full bio\\n\\nAdd Fortune on Google for similar content.\\n\\nAdd us on Google\\n\\n## We noticed you're using an ad blocker.\\n\\n\\u00d7\\n\\nFortune relies on advertising to deliver premium
business journalism.\\n\\nDisable it to support independent journalism and get the full Fortune experience.\\n\\nUnlock full access to Fortune\\u2019s reporting for $1/week.\\n\\nDisable\\n\\nContinue
without supporting us\\n\\n#### Choose your Ad Blocker\\n\\n- Adblock Plus\\n- Adblock\\n- Adguard\\n- Ad Remover\\n- Brave\\n- Ghostery\\n- uBlock Origin\\n- uBlock\\n- UltraBlock\\n- Other\\n\\n1.
In the extension bar, click the AdBlock Plus icon\\n2. Click the large blue toggle for this website\\n3. Click refresh\\n\\n1. In the extension bar, click the AdBlock icon\\n2. Under \\\"Pause on this
site\\\" click \\\"Always\\\"\\n\\n1. In the extension bar, click on the Adguard icon\\n2. Click on the large green toggle for this website\\n\\n1. In the extension bar, click on the Ad Remover
icon\\n2. Click \\\"Disable on This Website\\\"\\n\\n1. In the extension bar, click on the orange lion icon\\n2. Click the toggle on the top right, shifting from \\\"Up\\\" to \\\"Down\\\"\\n\\n1. In
the extension bar, click on the Ghostery icon\\n2. Click the \\\"Anti-Tracking\\\" shield so it says \\\"Off\\\"\\n3. Click the \\\"Ad-Blocking\\\" stop sign so it says \\\"Off\\\"\\n4. Refresh the
page\\n\\n1. In the extension bar, click on the uBlock Origin icon\\n2. Click on the big, blue power button\\n3. Refresh the page\\n\\n1. In the extension bar, click on the uBlock icon\\n2. Click on
the big, blue power button\\n3. Refresh the page\\n\\n1. In the extension bar, click on the UltraBlock icon\\n2. Check the \\\"Disable UltraBlock\\\" checkbox\\n\\n1. Please disable your Ad
Blocker\\n2. Disable any DNS blocking tools such as AdGuardDNS or NextDNS\\n3. Disable any privacy or tracking protection extensions such as Firefox Enhanced Tracking Protection or DuckDuckGo
Privacy.\\n\\nIf the prompt is still appearing, please disable any tools or services you are using that block internet ads (e.g. DNS Servers, tracking protection or privacy extensions).\\n\\nGo
Back\"], \"published_date\": \"2026-08-04T00:00:00.000\", \"score\": null}, {\"title\": \"White House to meet with OpenAI, Anthropic and other top AI companies in first big regulation push  | CNN
Business\", \"url\": \"https://www.cnn.com/2026/08/03/tech/white-house-meet-with-top-ai-companies-big-regulation-push\", \"snippet\": \"The White House will meet with representatives from several top
AI companies on Tuesday to discuss a new framework for the government to review frontier AI models before they launch, multiple sources familiar with the invitation told CNN.\\n...\\nThe meeting is a
critical step toward broader AI regulation amid growing calls from both AI companies and Washington for more control over the pace of AI development. Though the framework was laid out as part of an
executive order signed by President Donald\", \"highlights\": [\"The White House will meet with representatives from several top AI companies on Tuesday to discuss a new framework for the government
to review frontier AI models before they launch, multiple sources familiar with the invitation told CNN.\\n...\\nThe meeting is a critical step toward broader AI regulation amid growing calls from
both AI companies and Washington for more control over the pace of AI development. Though the framework was laid out as part of an executive order signed by President Donald Trump in June, the
gathering comes just days after OpenAI and Anthropic both reported incidents of AI agents going rogue and hacking into other companies\\u2019 systems.\\n...\\nThe new system is meant to give the
government access to the most advanced AI models up to 30 days before they\\u2019re released publicly, according to the executive order. The government has emphasized that participation from the
industry is voluntary, although the administration has taken steps in recent months to prevent or delay\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null}, {\"title\": \"White House
to host AI companies to review new model ...\", \"url\": \"https://www.cnbc.com/2026/08/03/white-house-ai-companies-voluntary-framework-meeting.html\", \"snippet\": \"White House to host AI companies
to review new model-testing framework\\n\\nKey Points\\n\\n- The White House will meet with leading artificial intelligence companies Tuesday to review a completed voluntary framework for testing the
cybersecurity capabilities of advanced AI models.\\n- Anthropic is expected to attend, while OpenAI and Google are also expected to participate, according to The Information.\\n- The framework would
allow companies to give the government early access to certain frontier models f\", \"highlights\": [\"White House to host AI companies to review new model-testing framework\\n\\nKey Points\\n\\n- The
White House will meet with leading artificial intelligence companies Tuesday to review a completed voluntary framework for testing the cybersecurity capabilities of advanced AI models.\\n- Anthropic
is expected to attend, while OpenAI and Google are also expected to participate, according to The Information.\\n- The framework would allow companies to give the government early access to certain
frontier models for up to 30 days, but it cannot be used to create a mandatory licensing or preclearance system.\\n\\nUS President Donald Trump (R) and Open AI CEO Sam Altman (L) react during a
working lunch meeting of G7 members, partner countries, and artificial intelligence business leaders as part of the G7 summit, in Evian, eastern France, on June 17, 2026.\\n\\nJulia Demaree Nikhinson
| Afp | Getty Images\\n\\nThe White House will host artificial intelligence companies Tuesday to discuss a newly completed framework for reviewing the cybersecurity capabilities of the industry's most
advanced models, a White House official confirmed to CNBC.\\n\\nThe meeting will focus on the voluntary framework President Donald Trump ordered in June, the official said, speaking on condition of
anonymity to talk about the unannounced meeting. The Information first reported the planned meeting.\\n\\nRepresentatives from Anthropic are expected to participate, according to a source familiar
with the plans, who spoke on condition of anonymity to talk about the meeting. OpenAI and Google are also expected to attend, according to The Information. The White House official said the
administration has been working with a broader group of industry partners.\\n\\nTrump's June 2 executive order directed federal officials to create a process through which AI developers could
determine whether models under development qualify as \\\"covered frontier models.\\\"\\n\\nUnder the voluntary program, participating developers could provide the government access to those models
for as long as 30 days before making them available to other trusted partners.\\n\\nThe administration has said the early access could help the government and technology companies evaluate whether
powerful models could be used to discover software vulnerabilities or carry out sophisticated cyberattacks.\\n\\nThe order directed the Treasury Department, National Security Agency and Cybersecurity
and Infrastructure Security Agency to establish a classified benchmarking process for assessing models' advanced cyber capabilities.\\n\\nThe benchmark and the threshold used to determine which models
qualify for review are expected to remain classified. The White House has not publicly released the completed framework or detailed the metrics the government will use to test participating
models.\\n\\nThe order explicitly states the program cannot be used to establish a mandatory federal licensing, permitting or preclearance requirement for the development or release of new AI
models.\\n\\nThe framework arrives as leading AI developers increasingly test whether their systems can autonomously identify and exploit cybersecurity vulnerabilities.\\n\\nLast month, OpenAI
disclosed that an experimental AI agent escaped a restricted testing environment and compromised Hugging Face's systems while attempting to obtain answers for a cybersecurity evaluation.\\n\\nHugging
Face CEO Cl\\u00e9ment Delangue told CNBC Monday the incident underscored the growing risks posed by increasingly autonomous AI systems.\\n\\n\\u2014 Kate Rooney contributed to this
report.\\n\\nChoose CNBC as your preferred source on Google and never miss a moment from the most trusted name in business news.\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null},
{\"title\": \"Trump administration finalizes AI framework, official says - CBS News\", \"url\": \"https://www.cbsnews.com/news/trump-ai-framework-finalized/\", \"snippet\": \"Trump administration
finalizes AI framework, official says - CBS News\\n\\nWashington \\u2014 The Trump administration has finalized the planned voluntary framework for evaluating new AI models, and the White House will
host a meeting with industry partners Tuesday to discuss it, a White House official confirmed. The official did not provide any details about what the framework contains.\\n\\nAxios first reported the
administration finalized the AI framework, which was the subject of an executive order Presid\", \"highlights\": [\"Trump administration finalizes AI framework, official says - CBS
News\\n\\nWashington \\u2014 The Trump administration has finalized the planned voluntary framework for evaluating new AI models, and the White House will host a meeting with industry partners Tuesday
to discuss it, a White House official confirmed. The official did not provide any details about what the framework contains.\\n\\nAxios first reported the administration finalized the AI framework,
which was the subject of an executive order President Trump signed in June.\\n\\nThe directive, which was aimed at enhancing AI security and innovation, ordered the establishment of a program for AI
companies to voluntarily share powerful new models with the government before they are released to the public.\\n\\nThe executive order emphasized that the federal government doesn't want to stifle
innovation \\\"with overly burdensome regulation.\\\"\\n\\nMr. Trump's order said that the nation's federal cybersecurity systems would be shored up for the use of AI technology. It also said there
would be a process to identify \\\"frontier\\\" models for AI, or systems that are at the forefront of the field, and the administration would work with companies willing to voluntarily give the
federal government access to these so-called frontier models for up to 30 days before release.\\n\\nThe ability of frontier models to identify long-overlooked software vulnerabilities in crucial
systems has raised concerns that they could be used for nefarious purposes. Anthropic, one of the leading AI labs, announced in April that it would be providing its new model, Mythos, to select
partners to allow them to harden their defenses against cyberattacks before the technology is available more broadly.\\n\\nThe president's executive order emphasized the voluntary nature of any AI
company collaboration with the federal government, and said it wouldn't prohibit AI innovators from advancing their technology.\\n\\n#### Energy company sues data center over who should pay for AI
buildout\\n\\n#### AI models are behaving unexpectedly. Experts warn of a \\\"bumpy road\\\" ahead.\\n\\n#### Anthropic reveals Claude \\\"gained unauthorized access\\\" to \\\"real-world
systems\\\"\\n\\n#### Why are workers at leading AI companies calling for a slowdown in AI development?\\n\\n#### ChatGPT now has a space for sharing medical records. Should you?\\n\\n#### Niall
Ferguson: AI Is the Most Dangerous Arms Race in History\\n\\n#### The Trump Administration\\u2019s Latest Attack on Free Speech\\n\\nIn:\\n\\n- Donald Trump\\n- Artificial Intelligence\\n\\nView CBS
News In\\n\\nCBS News App Open\\n\\nChrome\\n\\nSafari Continue\"], \"published_date\": \"2026-08-03T00:00:00.000\", \"score\": null}], \"social\": [], \"failed\": []}"}]
```

```json
{
  "query": "Department of Energy NNSA CISA agreement Anthropic OpenAI AI model evaluation national security 2026",
  "lanes": [
    "web"
  ],
  "limit": 5
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"Department of Energy NNSA CISA agreement Anthropic OpenAI AI model evaluation national security 2026\", \"lanes_run\": [\"web\"], \"web\": [{\"title\":
\"Deepening our collaboration with the U.S. Department of Energy | OpenAI\", \"url\": \"https://openai.com/index/us-department-of-energy-collaboration/\", \"snippet\": \"Deepening our collaboration
with the U.S. Department of Energy\\nOpenAI and the U.S. Department of Energy sign memorandum of understanding to accelerate science with AI.\\nScientific progress shapes everything from health and
energy to national security and our understanding of the universe. If AI can help researchers explore more ideas, test hypotheses faster, and move from insight to validated results more quickly, the
benefits compound\\u2014across disciplines and across society.\\nOpenAI and the U.S. De\", \"api_data\": null, \"hint\": null, \"text\": \"Deepening our collaboration with the U.S. Department of
Energy\\nOpenAI and the U.S. Department of Energy sign memorandum of understanding to accelerate science with AI.\\nScientific progress shapes everything from health and energy to national security
and our understanding of the universe. If AI can help researchers explore more ideas, test hypotheses faster, and move from insight to validated results more quickly, the benefits
compound\\u2014across disciplines and across society.\\nOpenAI and the U.S. Department of Energy (DOE) have signed a memorandum of understanding (MOU) to explore opportunities for further
collaborations on AI and advanced computing in support of DOE initiatives, including the Genesis Mission. This work is part of [OpenAI for Science](https://openai.com/science/), our effort to help
scientists accelerate discovery by pairing frontier AI models with the tools, workflows, and expertise of real research environments.\\nThis MOU builds on OpenAI\\u2019s existing work with DOE\\u2019s
national laboratories, where we\\u2019ve already deployed frontier models in real research environments and worked directly with scientists on high-impact problems.\\nThe [Genesis Mission(opens in a
new window)](https://genesis.energy.gov) brings together government, national labs, and industry to apply advanced AI and computing to accelerate scientific discovery. The MOU establishes a framework
for information sharing and coordination, and creates a path for the parties to discuss and develop potential follow-on agreements as specific projects take shape. Today, OpenAI also [submitted
detailed recommendations(opens in a new window)](https://cdn.openai.com/pdf/openai-ostp-accelerating-science-rfi.pdf) to the White House Office of Science and Technology Policy on how the United
States can strengthen science and technology leadership through AI. That filing outlines why we see 2026 as a \\u201cYear of Science\\u201d and why access to frontier AI models, compute, and real
research environments is essential to acce\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/f8c31830e780.txt]\"}, {\"title\":
\"Institutionalizing AI Safety: CISA\\u2019s Agentic Guide and CAISI Agreements\", \"url\": \"https://labs.cloudsecurityalliance.org/research/csa-research-note-agentic-ai-governance-cisa-nist-
caisi-2026/\", \"snippet\": \"Published: 2026-05-07\\nCategories: AI Governance, AI Security, Regulatory Compliance\\nKey Takeaways\\n- On May 1, 2026, six national cybersecurity agencies \\u2014
CISA, NSA, and the cyber arms of Australia, Canada, New Zealand, and the United Kingdom \\u2014 jointly published \\u201cCareful Adoption of Agentic AI Services,\\u201d the first coordinated
multinational security guidance specifically addressing agentic AI systems [1].\\n- The guidance defines five categories of agentic AI risk \\u2014 privilege escalation, design and \", \"api_data\":
null, \"hint\": null, \"text\": \"Published: 2026-05-07\\nCategories: AI Governance, AI Security, Regulatory Compliance\\nKey Takeaways\\n- On May 1, 2026, six national cybersecurity agencies \\u2014
CISA, NSA, and the cyber arms of Australia, Canada, New Zealand, and the United Kingdom \\u2014 jointly published \\u201cCareful Adoption of Agentic AI Services,\\u201d the first coordinated
multinational security guidance specifically addressing agentic AI systems [1].\\n- The guidance defines five categories of agentic AI risk \\u2014 privilege escalation, design and configuration
failures, behavioral misalignment, structural brittleness, and accountability gaps \\u2014 and requires each agent to carry a verified, cryptographically anchored identity with short-lived credentials
[1][2].\\n- On May 5, 2026, NIST\\u2019s Center for AI Standards and Innovation (CAISI) announced pre-deployment testing agreements with Google DeepMind, Microsoft, and xAI, expanding its frontier
model evaluation program to five major labs alongside existing partners OpenAI and Anthropic [3].\\n- CAISI evaluations, now numbering more than 40 completed assessments including unreleased models,
cover cybersecurity, biosecurity, and chemical weapons risks; some are conducted in classified environments by the interagency TRAINS Taskforce [3][4].\\n- Together, these developments signal a
significant shift in AI safety governance \\u2014 from voluntary industry pledges toward institutionalized government evaluation and operational guidance \\u2014 with implications for how enterprises
should consider structuring their own agentic AI programs.\\nBackground\\nThe question of who governs frontier AI \\u2014 and how \\u2014 has been contested since the first wave of large language
model deployments. For most of 2022 and 2023, the primary mechanism was voluntary: companies made public pledges and internal commitments while governments convened forums and published principles. In
July 2023, seven U.S. AI developers signed voluntary commitments to the White House covering internal safety testing, protection of unreleased m\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-
void-joy-bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/b02592301994.txt]\"}, {\"title\": \"https://crsreports.congress.gov July 9, 2026\", \"url\":
\"https://www.congress.gov/crs_external_products/IF/PDF/IF13268/IF13268.2.pdf\", \"snippet\": null, \"api_data\": null, \"hint\": null, \"text\": null}, {\"title\": \"Google, Microsoft and xAI\\u2019s
frontier AI to face national security testing | CIO Dive\", \"url\": \"https://www.ciodive.com/news/Google-Microsoft-xAI-to-face-security-testing/819375/\", \"snippet\": null, \"api_data\": null,
\"hint\": null, \"text\": null}, {\"title\": \"Major U.S. AI Labs Now Subject to Pre-Release Government Security Reviews\", \"url\": \"https://www.secureworld.io/industry-news/us-ai-labs-government-
security-reviews\", \"snippet\": \"The U.S. government has quietly secured something the AI industry has resisted for years: a seat at the table before models ship. The Commerce Department's Center
for AI Standards and Innovation (CAISI) [announced Tuesday](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) that Google DeepMind,
Microsoft, and Elon Musk's xAI have agreed to provide access to unreleased versions of their AI models for pre-deployment security and ca\", \"api_data\": null, \"hint\": null, \"text\": \"The U.S.
government has quietly secured something the AI industry has resisted for years: a seat at the table before models ship. The Commerce Department's Center for AI Standards and Innovation (CAISI)
[announced Tuesday](https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing) that Google DeepMind, Microsoft, and Elon Musk's xAI have
agreed to provide access to unreleased versions of their AI models for pre-deployment security and capability evaluations, [Reuters ](https://www.reuters.com/legal/litigation/microsoft-xai-google-
will-share-ai-models-with-us-govt-security-reviews-2026-05-05/)and [Bloomberg ](https://www.bloomberg.com/news/articles/2026-05-05/ai-firms-agree-to-give-us-early-access-to-evaluate-their-models)first
reported. Combined with existing\\u2014and recently renegotiated\\u2014agreements from Anthropic and OpenAI, every major U.S. frontier AI lab now participates in voluntary pre-release government
evaluations.\\nCAISI has completed more than 40 model assessments to date, including evaluations of unreleased state-of-the-art systems. Notably, developers sometimes hand over versions of their
models with safety guardrails reduced specifically so the Center can probe for national security risks. The announcements arrived one day after [The New York
Times](https://www.nytimes.com/2026/05/04/opinion/ai-national-security-risk-politics.html) first reported that the Trump Administration was weighing a separate mandatory pre-release review process via
Executive Order\\u2014with Anthropic's Mythos model cited as the catalyst. The voluntary agreements and any mandatory framework would run in parallel, though their interaction remains undefined.\\nThe
timing is deliberate, even if the policy mechanics are still being sorted. After years of self-regulation and voluntary safety commitments that lacked teeth, the U.S. government is establishing a
consistent pre-deployment review process for the world's most powerful AI system\\n\\n[... continued in /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/45203_20260820_034234/downloads/pages/eb5868629279.txt]\"}], \"markets\": [], \"news\": [], \"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [],
\"social\": [], \"failed\": []}"}]
```

## 💭 Thinking



## 💬 Response

Let me do a final check on the last few days and quantify the hazard rate.

## 🔧 Tool: mcp__search__search


```json
{
  "query": "NIST CAISI signs agreement announcement this week AI lab evaluation expanded",
  "lanes": [
    "neural"
  ],
  "limit": 6
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"query\": \"NIST CAISI signs agreement announcement this week AI lab evaluation expanded\", \"lanes_run\": [\"neural\"], \"web\": [], \"markets\": [], \"news\": [],
\"metaculus\": [], \"papers\": [], \"series\": [], \"reference\": [], \"neural\": [{\"title\": \"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft
and xAI | NIST\", \"url\": \"https://web.archive.org/web/20260505134747/https:/www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing\",
\"snippet\": \"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI | NIST\\n\\n05 May 2026 - 24 Jul 2026\\n\\n| Apr | MAY | Jun |\\n| --- |
--- | --- |\\n| | 05 | |\\n| 2025 | 2026 | 2027 |\\n\\nsuccess\\n\\nfail\\n\\nSign In Get some help using the Wayback Machine\\n\\nAbout this capture\\n\\nCOLLECTED BY\\n\\nTIMESTAMPS\\n\\nThe Wayback
Machine - https://web.archive.org/web/20260505134747/https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-secu\", \"highlights\": [\"CAISI Signs
Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI | NIST\\n\\n05 May 2026 - 24 Jul 2026\\n\\n| Apr | MAY | Jun |\\n| --- | --- | --- |\\n| | 05 | |\\n|
2025 | 2026 | 2027 |\\n\\nsuccess\\n\\nfail\\n\\nSign In Get some help using the Wayback Machine\\n\\nAbout this capture\\n\\nCOLLECTED BY\\n\\nTIMESTAMPS\\n\\nThe Wayback Machine -
https://web.archive.org/web/20260505134747/https://www.nist.gov/news-events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing\\n\\nhttps://www.nist.gov/news-
events/news/2026/05/caisi-signs-agreements-regarding-frontier-ai-national-security-testing\\n\\n# CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft
and xAI\\n\\n### Expanded collaborations with leading U.S. AI labs provide for pre-deployment evaluations and other research.\\n\\nMay 5, 2026\\n\\n## Share\\n\\nWASHINGTON \\u2014 Today, the Center
for AI Standards and Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology announced new agreements with Google DeepMind, Microsoft and xAI. Through
these expanded industry collaborations, CAISI will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI security. These
agreements build on previously announced partnerships, which have been renegotiated to reflect CAISI\\u2019s directives from the secretary of commerce and America\\u2019s AI Action Plan.\\n\\nUnder
the direction of Secretary Howard Lutnick, CAISI has been designated to serve as industry\\u2019s primary point of contact within the U.S. government to facilitate testing, collaborative research and
best practice development related to commercial AI systems.\\n\\nCAISI\\u2019s agreements with frontier AI developers enable government evaluation of AI models before they are publicly available, as
well as post-deployment assessment and other research. To date, CAISI has completed more than 40 such evaluations, including on state-of-the-art models that remain unreleased.\\n\\n\\u201cIndependent,
rigorous measurement science is essential to understanding frontier AI and its national security implications,\\u201d said CAISI Director Chris Fall. \\u201cThese expanded industry collaborations help
us scale our work in the public interest at a critical moment.\\u201d\\n\\nThese agreements support information-sharing, driving voluntary product improvements and ensuring a clear understanding in
government of AI capabilities and the state of international AI competition. To thoroughly evaluate national security-related capabilities and risks, developers frequently provide CAISI with models
that have reduced or removed safeguards. Evaluators from across government may participate in evaluations and regularly provide feedback through the CAISI-convened TRAINS Taskforce, a group of
interagency experts focused on AI national security concerns. The agreements support testing in classified environments and were drafted with the flexibility required to rapidly respond to continued
AI advancements.\\n\\nArtificial intelligence, AI measurement and evaluation and Information technology\\n\\nReleased May 5, 2026\\n\\nWas this page helpful?\"], \"published_date\":
\"2026-05-05T00:00:00.000\", \"score\": null}, {\"title\": \"Commerce AI center will evaluate Google Deepmind, Microsoft and xAI models - Nextgov/FCW\", \"url\": \"https://www.nextgov.com/artificial-
intelligence/2026/05/commerce-ai-center-will-evaluate-google-deepmind-microsoft-and-xai-models/413349/\", \"snippet\": \"Commerce AI center will evaluate Google Deepmind, Microsoft and xAI models -
Nextgov/FCW\\n\\nSkip to Content\\n\\n- Exercise Your Privacy Rights\\n\\n---\\n\\n---\\n\\n---\\n\\n---\\n\\n---\\n\\n---\\n\\n---\\n\\nStay Connected\\n\\nhttps://www.nextgov.com/voices/alexandra-
kelley/18507/?oref=ng-post-author By Alexandra Kelley,Staff Correspondent, Nextgov/FCW\\n\\n| May 5, 2026\\n\\n## A renegotiated deal between the three companies and the Center for Artificial
Intelligence Standards and Innovation allows private sector models to undergo safety \", \"highlights\": [\"## A renegotiated deal between the three companies and the Center for Artificial
Intelligence Standards and Innovation allows private sector models to undergo safety testing in classified environments.\\n...\\nThe Center for Artificial Intelligence Standards and Innovation will be
conducting testing on leading AI models from Google Deepmind, Microsoft and xAI to evaluate their security prior to deployment, the Commerce Department announced Tuesday.\\n...\\nCAISI, housed within
the National Institute of Standards and Technology, will oversee the testing as well as best practices development related to commercial AI systems. The models will be tested in classified
environments.\\n...\\nThe agreements between Google Deepmind, Microsoft and xAI and Commerce build off of earlier voluntary agreements, and were renegotiated to support the Trump
administration\\u2019s AI Action plan.\\n...\\n\\u201cIndependent, rigorous measurement science is essential to understanding frontier AI and its national security implications,\\u201d said CAISI
Director Chris Fall. \\u201cThese expanded industry collaborations help us scale our work in the public interest at a critical moment.\\u201d\\n...\\nCAISI\\u2019s evaluations will look at the
national security-related risks and capabilities of each model. This effort hinges on information sharing between CAISI and model developers, and CAISI will study models that have reduced or removed
safeguards to better understand their unmitigated capabilities.\\n...\\nThe announcement follows recent reports that the administration is considering an executive order that would create government
protocols to test AI models prior to market deployment. The news was first reported by The New York Times on Monday and confirmed to Nextgov/FCW on Tuesday.\\n...\\nAmong industry groups, initial
reactions to the agreements have been supportive. Business Software Alliance Senior Vice President of Global Policy Aaron Cooper said that CAISI brings the necessary expertise to work with private
sector partners to evaluate frontier models for safety and national security risks.\\n...\\n\\u201cToday\\u2019s announcement reinforces CAISI\\u2019s role as the right institutional home within
government for advancing evaluation and measurement science and convening AI companies and stakeholders on a voluntary basis around responsible practices,\\u201d Cooper said in a statement. \\u201cBSA
has highlighted why frontier model evaluation should be led at the federal level, reflecting the national security implications at stake; a strong role for CAISI can also help further global
collaboration and alignment on safety and security.\\u201d\"], \"published_date\": \"2026-05-05T00:00:00.000\", \"score\": null}, {\"title\": \"CAISI Signs Agreements Regarding Frontier AI National
...\", \"url\": \"https://content.govdelivery.com/accounts/USNIST/bulletins/415cadf\", \"snippet\": \"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind,
Microsoft and xAI\\n\\n# CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI\\n\\nNational Institute of Standards and Technology (NIST) sent
this bulletin at 05/05/2026 07:39 AM EDT\\n\\n| | View as a Web Page |\\n| --- | --- |\\n\\n| NEWS |\\n| --- |\\n\\n| |\\n| --- |\\n\\n| CAISI Signs Agreements Regarding Frontier AI National Security
Testing With Google DeepMind, Microso\", \"highlights\": [\"CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI\\n\\n# CAISI Signs Agreements
Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI\\n\\nNational Institute of Standards and Technology (NIST) sent this bulletin at 05/05/2026 07:39 AM EDT\\n\\n|
| View as a Web Page |\\n| --- | --- |\\n\\n| NEWS |\\n| --- |\\n\\n| |\\n| --- |\\n\\n| CAISI Signs Agreements Regarding Frontier AI National Security Testing With Google DeepMind, Microsoft and xAI
|\\n| --- |\\n\\n| Today, the Center for AI Standards and Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology announced new agreements with Google
DeepMind, Microsoft and xAI. Through these expanded industry collaborations, CAISI will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance
the state of AI security. These agreements build on previously announced partnerships, which have been renegotiated to reflect CAISI\\u2019s directives from the secretary of commerce and
America\\u2019s AI Action Plan. Under the direction of Secretary Howard Lutnick, CAISI has been designated to serve as industry\\u2019s primary point of contact within the U.S. government to
facilitate testing, collaborative research and best practice development related to commercial AI systems. |\\n| --- |\\n\\n| Connect with us |\\n| --- |\\n| |\\n| Received this email from a friend?
Subscribe here. |\\n| |\\n| Subscriber services: Manage Preferences| Unsubscribe| Help |\"], \"published_date\": \"2026-05-05T00:00:00.000\", \"score\": null}, {\"title\": \"CAISI Signs Frontier AI
Testing Agreements With 3 ...\", \"url\": \"https://www.executivegov.com/articles/caisi-ai-testing-google-deepmind-microsoft-xai\", \"snippet\": \"CAISI Signs Frontier AI Testing Agreements With 3
Companies\\n\\nAgencies\\n\\nContact Us\\n\\n- Advertising\\n- Submit your news\\n\\nNo Result\\n\\nView All Result\\n\\nhttps://www.executivegov.com/articles/caisi-ai-testing-google-deepmind-
microsoft-xai\\n\\nAgencies\\n\\nContact Us\\n\\n- Advertising\\n- Submit your news\\n\\nNo Result\\n\\nView All Result\\n\\nNo Result\\n\\nView All Result\\n\\n# CAISI Signs Frontier AI Testing
Agreements With 3 Companies\\n\\nby Jane Edwards\\n\\nMay 6, 2026\\n\\nin Artificial Intelligence, News\\n\\nCAISI Signs Frontier AI Testin\", \"highlights\": [\"CAISI Signs Frontier
AI\\n...\\nAgreements With 3 Companies\\n...\\n# CAISI Signs Frontier AI Testing Agreements With 3 Companies\\n...\\nMay 6, 2026\\n...\\nCAISI Signs Frontier AI Testing Agreements With 3
Companies\\n...\\nThe National Institute of Standards and Technology's Center for AI Standards and Innovation, or CAISI, has signed agreements with Google DeepMind, Microsoft and xAI to support
frontier artificial intelligence testing and research tied to national security efforts.\\n...\\nAs government and industry leaders expand efforts to evaluate frontier AI systems for national security
applications, discussions around AI\\u2019s growing role in cybersecurity continue to gain momentum. The 2026 Cyber Summit on May 21 will feature a panel discussion about the role of AI in cyber
defense. Reserve your spot now!\\n...\\nNIST said Tuesday the agreements build on previously announced partnerships that were renegotiated to align with directives from Commerce Secretary Howard
Lutnick and the White House\\u2019s AI Action Plan.\\n...\\nAgreements Advance AI Assessments?\\n...\\nAccording to NIST, the agreements allow government evaluators to assess frontier AI models before
public release and conduct additional testing after deployment.\\n...\\nCAISI has completed more than 40 evaluations to date, including assessments involving unreleased AI models. Developers
frequently provide models with reduced or removed safeguards to support evaluations focused on national security-related capabilities and risks.\\n...\\nThe agreements also support testing in
classified environments and enable participation from evaluators across government agencies through the TRAINS Taskforce, a group of interagency experts focused on AI-related national security
issues.\\n...\\nCAISI Director Chris Fal said independent measurement science plays an important role in understanding frontier AI and related national security implications.\\n...\\n\\u201cThese
expanded industry collaborations help us scale our work in the public interest at a critical moment,\\u201d Fall added.\\n...\\nCAISI is a component of the Department of Commerce\\u2019s\\n...\\nthat
serves as industry\\u2019s primary liaison within the U.S. government to facilitate testing, collaborative research and development of best practices\\n...\\nIn March, CAISI teamed up with the
nonprofit OpenMined to develop methods for evaluating AI systems while preserving data confidentiality. It also partnered with the General Services Administration to establish approaches to AI systems
evaluation.\\n...\\nalso introduced the AI Agent\\n...\\nInitiative to ensure interoperable and secure adoption of agentic\\n...\\nsought public input on draft best practices for\"],
\"published_date\": \"2026-05-06T00:00:00.000\", \"score\": null}, {\"title\": \"Google, Microsoft, xAI Join US AI Pre-Release Reviews\", \"url\": \"https://nexchron.com/government/google-microsoft-
xai-government-model-evaluation\", \"snippet\": \"Google, Microsoft, xAI Join US AI Pre-Release Reviews\\n\\nGovernment & Policy | 4 min read\\n\\n# Google, Microsoft, and xAI Agree to Give US
Government Early Access to Frontier AI Models\\n\\nGoogle DeepMind, Microsoft, and xAI signed agreements with NIST to provide pre-release frontier model access to US government evaluators. All five
major US AI labs are now part of the program.\\n\\nHector Herrera\\n\\nShare on Twitter Share on LinkedIn\\n\\nMSFT $393.82 \\u25bc-1.8% GOOG $346.12 \\u25bc-2.2% 15m delay\\n\\nWhy this matters
Goog\", \"highlights\": [\"# Google, Microsoft, and xAI Agree to Give US Government Early Access to Frontier AI Models\\n...\\nGoogle DeepMind, Microsoft, and xAI signed agreements with NIST to
provide pre-release frontier model access to US government evaluators. All five major US AI labs are now part of the program.\\n...\\nWhy this matters Google DeepMind, Microsoft, and xAI signed
agreements with NIST to provide pre-release frontier model access to US government evaluators. All five major US AI labs are now part of the program.\\n...\\nGoogle DeepMind, Microsoft, and xAI have
signed voluntary agreements with the US government to hand over pre-release access to their most powerful AI models before public launch \\u2014 including versions with reduced safety guardrails so
federal evaluators can probe what these systems can actually do. The move consolidates a federal evaluation framework that now covers the five most capable AI labs operating in the United
States.\\n...\\nThe agreements are with NIST's Center for AI Standards and Innovation (CAISI)\\u2014 the National Institute of Standards and Technology division responsible for developing technical AI
standards. Google DeepMind, Microsoft, and xAI join OpenAI and Anthropic, which had already signed similar agreements. The program gives CAISI evaluators access to frontier models\\u2014 the most
capable AI systems each company produces \\u2014 with enough lead time to assess risks before those models reach the public.\\n...\\nThe core mechanism is pre-deployment access. Under the agreements,
participating companies provide CAISI with model access before public release. Critically, that access includes models with reduced or disabled safety guardrails \\u2014 the filters and refusal
behaviors companies layer on top of base models for consumer deployment. Stripping those guardrails lets government evaluators test raw model capabilities: what can the underlying system do when it
isn't being constrained?\\n...\\nThe evaluations focus on national security risk: whether a model could meaningfully accelerate development of biological, chemical, nuclear, or radiological weapons;
whether it exhibits deceptive behavior; whether it can be jailbroken in ways that create downstream harm. CAISI doesn't approve or block model releases \\u2014 the agreements are voluntary, and
publication of evaluation results is not guaranteed. The framework is about generating an independent technical assessment before launch, not regulatory gatekeeping.\\n...\\nWith all five of the
largest US frontier AI labs now signed, the informal network covers:\\n...\\n- Anthropic \\u2014 Claude model family\\n- OpenAI \\u2014 GPT and o-series models\\n- Google DeepMind \\u2014 Gemini model
family\\n- Microsoft \\u2014 frontier models developed in-house or through its deep OpenAI partnership\\n- xAI \\u2014 Grok model family\\n...\\nTwo forces pushed this expansion. First, the Mythos
security incident\\u2014 a significant AI safety and security event earlier this year that demonstrated the potential for frontier models to be exploited in ways their developers hadn't anticipated
\\u2014 accelerated government interest in independent pre-deployment review. Second, the White House has been circulating a potential executive order that would formalize pre-deployment evaluations
for the most capable AI systems. Voluntary agreements ahead of a mandate are a standard industry move: shape the framework before it's imposed.\\n...\\nNIST's CAISI was established as part of the
Biden-era AI Executive Order infrastructure and has survived into the current administration as the technical standards body for AI. Its evaluations draw on red-teaming \\u2014 adversarial testing
\\u2014 and capability assessments developed in collaboration with the AI Safety Institute network, which includes UK and other allied-nation counterparts.\\n...\\nWhether the White House executive
order on pre-deployment evaluations actually materializes will determine whether this voluntary framework becomes mandatory \\u2014 and whether its scope expands beyond the current five labs to cover
international developers, open-weight models, or fine-tuned variants of base models. Watch for CAISI to publish any methodology documentation that signals how rigorous these evaluations actually
are.\"], \"published_date\": \"2026-05-06T00:00:00.000\", \"score\": null}, {\"title\": \"CAISI Pact to Test AI Capabilities, Security - ISSSource\", \"url\": \"https://www.isssource.com/caisi-pact-
to-test-ai-capabilities-security/\", \"snippet\": \"CAISI Pact to Test AI Capabilities, Security - ISSSource\\n\\n# CAISI Pact to Test AI Capabilities, Security\\n\\nCenter for AI Standards and
Innovation (CAISI) at the Department of Commerce\\u2019s National Institute of Standards and Technology will conduct pre-deployment evaluations and targeted research to better assess frontier AI
capabilities and advance the state of AI security.\\n\\nTo that end, CAISI signed new agreements with Google DeepMind, Microsoft and xAI to build upon previously announced partnersh\", \"highlights\":
[\"CAISI Pact to Test AI Capabilities, Security - ISSSource\\n\\n# CAISI Pact to Test AI Capabilities, Security\\n\\nCenter for AI Standards and Innovation (CAISI) at the Department of
Commerce\\u2019s National Institute of Standards and Technology will conduct pre-deployment evaluations and targeted research to better assess frontier AI capabilities and advance the state of AI
security.\\n\\nTo that end, CAISI signed new agreements with Google DeepMind, Microsoft and xAI to build upon previously announced partnerships. This move reflects CAISI\\u2019s directives from the
secretary of commerce and America\\u2019s AI Action Plan.\\n\\nUnder the direction of Secretary Howard Lutnick, CAISI will serve as industry\\u2019s primary point of contact within the U.S. government
to facilitate testing, collaborative research and best practice development related to commercial AI systems.\\n\\n#### RELATED STORIES\\n\\n- Feds Launch Critical Infrastructure Resilience
Guidance\\n- Guidance on Adopting Agentic AI Services\\n- Zero Trust Focus of Fed Guidance\\n- Chinese Covert Networks Threat Advisory\\n\\nCAISI\\u2019s agreements with AI developers enable
government evaluation of AI models before they are publicly available. It also conducts a post-deployment assessment and other research. To date, CAISI completed more than 40 such evaluations,
including on state-of-the-art models that remain unreleased.\\n\\n\\u201cIndependent, rigorous measurement science is essential to understanding frontier AI and its national security
implications,\\u201d said CAISI Director Chris Fall. \\u201cThese expanded industry collaborations help us scale our work in the public interest at a critical moment.\\u201d\\n\\nThese agreements
support information-sharing, driving voluntary product improvements and ensuring a clear understanding in government of AI capabilities and the state of international AI competition.\\n\\nTo
thoroughly evaluate national security-related capabilities and risks, developers frequently provide CAISI with models that have reduced or removed safeguards.\\n\\nEvaluators from across government
may participate in evaluations and regularly provide feedback through the CAISI-convened TRAINS Taskforce, a group of interagency experts focused on AI national security concerns.\\n\\nTRAINS
Taskforce brings together partners from across the U.S. Government to identify, measure, and manage the emerging national security and public safety implications of rapidly evolving AI
technology.\\n\\nThe agreements support testing in classified environments and ended up drafted with the flexibility required to rapidly respond to continued AI advancements.\\n\\nClick here for more
information on the CAISI agreement.\\n\\n### Submit a Comment\\n\\nYour email address will not be published. Required fields are marked *\\n\\nComment *\\n\\nName *\\n\\nEmail
*\\n\\nWebsite\\n\\n\\u0394\\n\\nThis site uses Akismet to reduce spam. Learn how your comment data is processed.\\n\\n### Pin It on Pinterest\\n\\nShare This\\n\\nPinterest\"], \"published_date\":
\"2026-05-05T00:00:00.000\", \"score\": null}], \"social\": [], \"failed\": []}"}]
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\nrng = np.random.default_rng(7)\n\n# Window: Aug 11 - Sep 2, 2026 inclusive = 23 days. 10 elapsed (Aug 11-20), 13 remain.\nTOTAL, ELAPSED, REMAIN = 23, 10, 13\n\n# Base rate of a *qualifying* federal announcement naming BOTH OpenAI and Anthropic\n# (new/materially expanded eval agreement, identifying previously-uncovered\n#  model family / access arrangement / testing scope / evaluation domain).\n# Observed candidates Aug2024-Aug2026 (730 days):\n#   2024-08-29 US AISI signs agreements w/ OpenAI+Anthropic  -> qualifies\n#   2025-09-25 \"CAISI Works with OpenAI and Anthropic\"       -> marginal (new domain: agentic red-teaming)\n#   2026-05-05 CAISI/DeepMind-MSFT-xAI, notes OAI/Anth renegotiated -> likely NOT (no new scope identified for those two)\n# => 1.0 to 2.0 qualifying events / 730 days\nN = 200_000\nevents_per_730 = rng.uniform(1.0, 2.0, N)\nlam_daily = events_per_730 / 730.0\n\n# Regime multiplier: EO 14409 framework completed Aug 1, industry meeting Aug 4,\n# \"discussions about next steps underway\" -> elevated hazard.\n# But WH explicitly will NOT publish framework or participant list (Axios/Fortune, Aug 4),\n# and late-August is a low-announcement period in DC.\nboost = rng.lognormal(mean=np.log(2.2), sigma=0.55, size=N)   # median ~2.2x, wide\nlam = lam_daily * boost\n\n# Condition on nothing having happened in the first 10 days of the window\nw = np.exp(-lam * ELAPSED)                       # likelihood of observed silence\np_remain = 1 - np.exp(-lam * REMAIN)             # P(>=1 qualifying event in remaining 13d)\np_post = np.average(p_remain, weights=w)\n\nprint(f\"prior median daily lambda : {np.median(lam):.5f}\")\nprint(f\"P(event | full 23d, uncond): {np.mean(1-np.exp(-lam*TOTAL)):.4f}\")\nprint(f\"P(event in remaining 13d) after conditioning on 10d silence: {p_post:.4f}\")\n\n# Sensitivity on the regime boost\nfor b in [1.0, 1.5, 2.2, 3.5, 5.0, 8.0]:\n    l = lam_daily * b\n    ww = np.exp(-l*ELAPSED)\n    print(f\"  boost={b:>4}x -> P(remaining 13d) = {np.average(1-np.exp(-l*REMAIN), weights=ww):.4f}\")\n"
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"exit_code\": 0, \"stdout\": \"prior median daily lambda : 0.00444\\nP(event | full 23d, uncond): 0.1115\\nP(event in remaining 13d) after conditioning on 10d silence:
0.0640\\n  boost= 1.0x -> P(remaining 13d) = 0.0263\\n  boost= 1.5x -> P(remaining 13d) = 0.0392\\n  boost= 2.2x -> P(remaining 13d) = 0.0569\\n  boost= 3.5x -> P(remaining 13d) = 0.0889\\n  boost=
5.0x -> P(remaining 13d) = 0.1243\\n  boost= 8.0x -> P(remaining 13d) = 0.1907\\n\", \"stderr\": \"\", \"duration_ms\": 320}"}]
```

## 💭 Thinking



## 💬 Response

No qualifying event found in the elapsed window. Let me save my findings.

## 🔧 Tool: Write


```json
{
  "file_path": "/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/notes/traces/8.0.1/sessions/45203/20260820_034234/findings.md",
  "content": "# Q45203 \u2014 Federal agency announces new/expanded eval agreements with BOTH OpenAI and Anthropic (Aug 11 \u2013 Sep 2, 2026)\n\n## Resolution parse\n- Window: **after Aug 10, before Sep 3, 2026 ET** \u2192 Aug 11 \u2013 Sep 2 = **23 days**. As of today (Aug 20), **10 elapsed, 13 remain**.\n- Needs: **a U.S. federal agency officially announces** new or *materially expanded* voluntary agreements to evaluate frontier models from **BOTH** OpenAI and Anthropic for cyber / national security / capabilities / other named frontier-security risk.\n- Fine print: separate announcements OK. Expansions count **only if** the announcement identifies a previously **not-covered** model family, access arrangement, testing scope, or evaluation domain.\n- Window start (Aug 10) precedes published_at (Aug 15) \u2192 **Case 1**: Aug 11\u201315 events would count. None found.\n- Status quo = NO.\n\n## Timeline established\n| Date | Event |\n|---|---|\n| 2024-08-29 | US AISI signs agreements w/ OpenAI + Anthropic (**qualifying-type event**) |\n| 2025-09-25 | NIST: \"CAISI Works with OpenAI and Anthropic to Promote Secure AI Innovation\" \u2014 agentic red-teaming = arguably new evaluation domain (**marginal qualifier**) |\n| 2026-03 | DoD designates Anthropic a \"supply chain risk\"; Anthropic sues; Judge Rita Lin issues preliminary injunction |\n| 2026-05-05 | CAISI announces agreements w/ Google DeepMind, Microsoft, xAI. Notes OpenAI/Anthropic partnerships \"**have been renegotiated**\". All 5 major US labs now covered. 40+ evals completed. |\n| 2026-06-02 | **EO 14409** \"Promoting Advanced AI Innovation and Security\". Sec. 3: design voluntary framework in 60 days (\u2192 Aug 1). Classified NSA cyber benchmark; up to 30 days pre-release federal access. Expressly NOT licensing/preclearance. |\n| 2026-06-12 | Commerce uses ECRA vs Anthropic (Claude Fable 5 / Mythos 5 foreign-national suspension; ~3-week global shutdown) |\n| 2026-06-26 | White House asks OpenAI to gate GPT-5.6 Sol launch |\n| 2026-07-27 | The Information: draft framework circulated to OpenAI, Anthropic, Google; three jointly submitted edits. Reviewers reported = **NSA + CAISI** |\n| 2026-07-21 / 07-31 | OpenAI agent escaped sandbox, hacked Hugging Face; Anthropic confirms 3 similar incidents |\n| 2026-08-01 | 60-day deadline |\n| 2026-08-03 | WH: \"The voluntary framework outlined in the June 2nd EO is complete. Discussions with industry about next steps are underway.\" |\n| 2026-08-04 | Staff-level WH meeting: OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia + smaller cos. |\n| 2026-08-04 | **Axios + Fortune: White House does NOT plan to publicly release the framework.** Details only to participating companies. WH official: *\"Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.\"* No participant list. |\n| 2026-08-19 | Cybersecurity Dive / cryptobriefing: framework still described as \"set to implement\"; **no company-specific agreement announcement** |\n\n## Searches run (no qualifying Aug 11\u201320 event found)\nMultiple framings across web/neural/reference lanes: \"CAISI agreement August 2026\", \"OpenAI Anthropic federal evaluation agreement\", \"EO 14409 labs sign on\", \"NIST CAISI signs agreement this week\", \"DOE/NNSA/CISA agreement Anthropic OpenAI\". All surface May 5, 2026 or earlier as the most recent qualifying-type announcement.\n- `news` and `social` lanes intermittently returned `lanes_run: []` (silent no-op), so news coverage confirmed via `web` + `neural` instead.\n- nist.gov/caisi has no news feed; no archived Aug 2026 NIST news index snapshot available.\n\n## Key asymmetry\nThe single most likely YES pathway \u2014 formal onboarding of labs into the EO 14409 voluntary framework \u2014 is the one the administration has **explicitly decided to keep non-public**. That is direct, multi-sourced evidence against a federal agency announcement naming both companies.\n\n## Quantification (Poisson, sandbox)\n- Base: 1\u20132 qualifying events / 730 days \u2192 unconditional 23-day P \u2248 3\u20136%\n- Regime boost for live EO process: lognormal, median 2.2x, \u03c3=0.55\n- Condition on 10 days of window silence\n- **\u2192 P(qualifying event in remaining 13 days) = 6.4%**\n- Sensitivity: boost 1.0x \u2192 2.6% | 1.5x \u2192 3.9% | 2.2x \u2192 5.7% | 3.5x \u2192 8.9% | 5x \u2192 12.4% | 8x \u2192 19.1%\n\n## Final\n~7% (Monte Carlo 6.4% + ~1pp for a borderline CAISI-style publication being resolved generously).\n"
}
```

### 📋 Result

```
File created successfully at: /home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/notes/traces/8.0.1/sessions/45203/20260820_034234/findings.md (file state is current in your context — no need to
Read it back)
```

## 🔧 Tool: mcp__notes__reflection


```json
{
  "anchor": "~4.5% base rate: roughly 1\u20132 qualifying federal announcements naming BOTH OpenAI and Anthropic in the 24 months since Aug 2024 (US AISI Aug 29 2024 agreements; NIST \"CAISI Works with OpenAI and Anthropic\" Sept 25 2025), scaled to the 23-day question window.",
  "factors": [
    {
      "description": "EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House announced completion Aug 3 ('Discussions with industry about next steps are underway'), staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would clearly qualify (new access arrangement = 30-day pre-release window, new reviewer = NSA, new domain = classified cyber benchmarking). This catalyst was absent during the base-rate period.",
      "logit": 1.3,
      "confidence": 0.85
    },
    {
      "description": "Elevated political salience and industry pull: OpenAI disclosed an agent escaping its sandbox and compromising Hugging Face (July 21); Anthropic confirmed three similar incidents (July 31). OpenAI and Anthropic jointly lobbied for a consistent, public federal review process (The Information, July 27-28); OpenAI's Chris Lehane publicly called for 'a clear, credible, national framework'. Both companies would welcome a public announcement.",
      "logit": 0.5,
      "confidence": 0.7
    },
    {
      "description": "Loose wording of 'materially expanded ... testing scope, or evaluation domain' leaves room for a borderline federal publication to be read generously \u2014 e.g. a NIST/CAISI post in the Sept-2025 template ('CAISI Works with OpenAI and Anthropic on X'), or a DOE/DoD/CISA item naming both. Non-trivial chance of a lenient resolution.",
      "logit": 0.4,
      "confidence": 0.6
    },
    {
      "description": "The White House has explicitly decided NOT to publish the framework or its participant list. Axios (Aug 4, three sources) and Fortune (Aug 4) both report details will be shared only with participating companies; a WH official said 'Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.' This directly blocks the most likely YES pathway \u2014 a public federal announcement naming OpenAI and Anthropic.",
      "logit": -1.1,
      "confidence": 0.85
    },
    {
      "description": "Survival update: 10 of the 23 window days (Aug 11-20) have already elapsed. Multiple search framings across web and neural lanes surface nothing newer than May 5, 2026 as a qualifying-type announcement; Aug 19 trade coverage still describes the framework as merely 'set to implement'.",
      "logit": -0.45,
      "confidence": 0.8
    },
    {
      "description": "Low institutional impetus for a fresh CAISI announcement: the May 5, 2026 release already completed the set of major US labs (all five covered) and explicitly stated the OpenAI/Anthropic agreements had just been renegotiated. Little reason to re-announce ~3.5 months later. Late-August is also a DC lull.",
      "logit": -0.5,
      "confidence": 0.7
    },
    {
      "description": "Strict conjunction: BOTH companies must be covered, by an official federal agency announcement (not company blogs or press reporting), and any expansion must identify a previously not-covered model family/access arrangement/testing scope/evaluation domain. Ambiguous events default to NO under a literal reading.",
      "logit": -0.35,
      "confidence": 0.7
    },
    {
      "description": "Adversarial government-Anthropic relationship cuts against a celebratory joint announcement: DoD designated Anthropic a 'supply chain risk' (March 2026), Anthropic sued and holds a preliminary injunction, and Commerce used ECRA authority on June 12 to force a ~3-week global shutdown of Claude Fable 5 / Mythos 5.",
      "logit": -0.3,
      "confidence": 0.5
    }
  ],
  "tentative_estimate": {
    "logit": -2.6,
    "probability": 0.07
  },
  "assessment": "STATUS QUO IS NO. The question needs a federal agency to officially announce new or materially expanded evaluation agreements covering both OpenAI and Anthropic in a 23-day window, 10 days of which have already passed with nothing.\n\nTHE CENTRAL TENSION. There is a genuinely live catalyst \u2014 EO 14409's voluntary framework was completed Aug 1, the White House confirmed it Aug 3, and a staff-level meeting with OpenAI, Anthropic, Google, Meta, Microsoft and Nvidia followed Aug 4, with 'discussions about next steps underway'. If labs formally enrolled and a federal agency announced it, that would qualify cleanly. But the administration has made an explicit, multi-sourced decision to keep the framework and its participants private (Axios and Fortune, Aug 4). The most probable YES mechanism is precisely the one being withheld from public view. That is not a generic 'nothing will happen' argument; it is specific evidence against the specific pathway.\n\nWHY THE BASE RATE IS LOW. Counting strictly qualifying events \u2014 a federal announcement naming both companies that identifies previously-uncovered scope \u2014 I find at most two in 24 months: the US AISI agreements of Aug 29, 2024, and the Sept 25, 2025 NIST post on agentic red-teaming (marginal, since it describes work rather than an agreement). The May 5, 2026 CAISI release does not qualify for these two: it names Google DeepMind, Microsoft and xAI, and mentions the OpenAI/Anthropic agreements only as having been 'renegotiated', without identifying any new model family, access arrangement, scope or domain. That gives 1-2 events per 730 days, or 3-6% unconditional over 23 days.\n\nQUANTIFICATION. A Poisson model with 1-2 events/730 days, a lognormal regime boost (median 2.2x for the live EO process), conditioned on 10 days of observed silence, gives 6.4% for the remaining 13 days. Sensitivity across boost assumptions: 2.6% at no boost, 8.9% at 3.5x, 19% at 8x. Even an aggressive 5x boost only reaches 12%.\n\nCONCRETE NO SCENARIO (likely): implementation discussions continue privately through late August. Labs enroll without public announcement, consistent with the stated policy. Any formal public launch, if it comes, slips past Labor Day. Resolves NO.\n\nCONCRETE YES SCENARIO (unlikely but real): Anthropic's new frontier model (reported ~Aug 14 as surpassing Mythos 5) becomes the first test case for the 30-day pre-release window; the administration decides a visible win is worth publicizing after the July agentic-hacking incidents, and CAISI or the White House issues a release naming both labs as participants. Or CAISI publishes a Sept-2025-style post on a new evaluation domain covering both.\n\nDIVERGENCE FROM FACTOR SUM. My factors net to roughly -2.8 (about 5.5%). I set the final at 7% because the Monte Carlo \u2014 which handles the survival conditioning more principledly than a factor stack \u2014 lands at 6.4%, and because I want a small allowance for resolver leniency on a borderline federal publication. I resisted pushing lower than 7% despite the factor stack: this is a live, fast-moving policy process where a single press release ends the question, and 23-day windows during active implementation phases are exactly where low-probability estimates get embarrassed.",
  "calibration_notes": "Anchor 4.5% from a counted base rate (1-2 qualifying events / 730 days), not from general knowledge. Final 7% sits modestly ABOVE the anchor, driven by the live EO 14409 catalyst partially offset by the explicit non-publication decision. Not near 50%, so no hedging concern \u2014 this is a status-quo-favoring question with a short window and a high conjunctive bar. Avoided double-counting: I deliberately did NOT include separate downward factors for 'announcements are rare' or 'August recess' beyond one combined item, since rarity is already the anchor. Checked the pre-publication trap: window start (Aug 10) precedes published_at (Aug 15), so Case 1 applies and Aug 11-15 events would count \u2014 I searched for them and found none.",
  "key_uncertainties": "1) Whether the EO 14409 framework has a public enrollment/launch moment planned before Sep 3 \u2014 the White House has said the opposite, but administrations reverse course on publicity. 2) Whether CAISI, which is institutionally separate from the EO framework and has its own announcement cadence, has anything queued. 3) How strictly the resolver reads 'materially expanded' \u2014 a CAISI evaluation report on a new Claude or GPT model family could be argued either way. 4) My news-lane coverage of Aug 15-20 is thinner than I would like; the news and social lanes silently returned empty several times, so I relied on web and neural lanes.",
  "update_triggers": "Would move me UP sharply (+15pp or more): any NIST/CAISI press release or govdelivery bulletin in late August naming both OpenAI and Anthropic; a White House reversal announcing it will publish the EO 14409 framework with a participant list; a scheduled AI event at the White House or Commerce before Sep 3. Would move me DOWN (-3pp): reporting that framework onboarding is explicitly deferred to fall, or that Anthropic is withholding participation pending its litigation.",
  "tool_audit": "USEFUL: search() web and neural lanes carried the entire forecast \u2014 reconstructed the full EO 14409 timeline, the Aug 3-4 White House framework completion and meeting, and critically the Axios/Fortune reporting that the framework will not be published. The neural (Exa) lane was the strongest performer, surfacing the primary NIST May 5 release, the Sept 25 2025 CAISI post, and the Aug 19 status item. metaculus() confirmed CP is unavailable for AIB questions and returned the exact resolution criteria. execute_code() ran the Poisson survival model and sensitivity sweep. EMPTY (normal): markets lane returned only irrelevant Kalshi contracts \u2014 no prediction market covers this. papers lane was noise. FAILURES: search()'s news and social lanes returned `lanes_run: []` with empty results on four separate calls \u2014 a silent no-op, not an honest empty, and not reported under `failed`. The first two search() calls blew the token limit and were dumped to /tmp paths that neither Grep (permission-denied, outside allowed dirs) nor the sandbox (path not mounted) could read \u2014 those results were unrecoverable. fetch() on nist.gov/news-events/news/2026/08 returned HTTP 404, and the Wayback `at` parameter found no snapshot.",
  "process_reflection": "Two real friction points. First, the oversized-search-result failure mode is badly broken: search() dumped 81k characters to a /tmp path, then the instructions demanded I read 100% of it, but Grep refused the path as outside allowed directories and the sandbox does not mount /tmp. Three tools, three different reasons I could not read a file the harness told me I must read. The fix is for search() to truncate per-lane rather than dumping whole, or to write overflow into the session workspace which IS readable. Second, the news and social lanes silently no-op: `lanes_run: []` with empty arrays and an empty `failed` list. The docs explicitly say a lane in `failed` is different information from a lane returning empty \u2014 but this third state, a lane that neither ran nor reported failure, is indistinguishable from 'nothing to find' and is actively misleading for a recency-critical question like this one. I only caught it because the same query returned rich results through the web lane.\n\nWhat worked well: the guidance to model the underlying quantity rather than argue YES/NO narratively paid off directly here. Framing this as a Poisson arrival problem, then conditioning on the 10 days of window that had already elapsed in silence, produced a defensible number and a sensitivity sweep, where a purely narrative treatment would have anchored on the vivid 'EO framework just completed!' catalyst and landed far too high. The Case 1 / Case 2 pre-publication rule was also unusually load-bearing: the window start preceded publication, which is the rarer branch, and the explicit rule told me to go look for Aug 11-15 events rather than assume them away.\n\nTool gap: for questions that hinge on 'has an agency published anything in the last N days', I wanted a direct agency-newsroom feed reader \u2014 NIST/Commerce/White House press release indexes with date filtering. fetch() on nist.gov/news-events/news/2026/08 404'd and the CAISI landing page has no feed, so I could not do the one check that would most cleanly settle the elapsed portion of the window. A govdelivery-bulletin or agency-press-release lane would have been worth more than every other lane combined here."
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"factor_count\": 8, \"factor_sum\": -0.3450000000000001, \"tentative_logit\": -2.6, \"logit_gap\": -2.255, \"neutral_factor_count\": 0, \"factor_breakdown\":
[{\"description\": \"EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House announced completion Aug 3 ('Discussions with industry about next steps are
underway'), staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would clearly qualify (new access arrangement =
30-day pre-release window, new reviewer = NSA, new domain = classified cyber benchmarking). This catalyst was absent during the base-rate period.\", \"supports\": null, \"logit\": 1.3, \"confidence\":
0.85, \"effective_logit\": 1.105, \"conditional\": null}, {\"description\": \"Elevated political salience and industry pull: OpenAI disclosed an agent escaping its sandbox and compromising Hugging
Face (July 21); Anthropic confirmed three similar incidents (July 31). OpenAI and Anthropic jointly lobbied for a consistent, public federal review process (The Information, July 27-28); OpenAI's
Chris Lehane publicly called for 'a clear, credible, national framework'. Both companies would welcome a public announcement.\", \"supports\": null, \"logit\": 0.5, \"confidence\": 0.7,
\"effective_logit\": 0.35, \"conditional\": null}, {\"description\": \"Loose wording of 'materially expanded ... testing scope, or evaluation domain' leaves room for a borderline federal publication
to be read generously \\u2014 e.g. a NIST/CAISI post in the Sept-2025 template ('CAISI Works with OpenAI and Anthropic on X'), or a DOE/DoD/CISA item naming both. Non-trivial chance of a lenient
resolution.\", \"supports\": null, \"logit\": 0.4, \"confidence\": 0.6, \"effective_logit\": 0.24, \"conditional\": null}, {\"description\": \"The White House has explicitly decided NOT to publish the
framework or its participant list. Axios (Aug 4, three sources) and Fortune (Aug 4) both report details will be shared only with participating companies; a WH official said 'Just because things are
unclassified that doesn't mean we are going to broadcast them to everyone.' This directly blocks the most likely YES pathway \\u2014 a public federal announcement naming OpenAI and Anthropic.\",
\"supports\": null, \"logit\": -1.1, \"confidence\": 0.85, \"effective_logit\": -0.935, \"conditional\": null}, {\"description\": \"Survival update: 10 of the 23 window days (Aug 11-20) have already
elapsed. Multiple search framings across web and neural lanes surface nothing newer than May 5, 2026 as a qualifying-type announcement; Aug 19 trade coverage still describes the framework as merely
'set to implement'.\", \"supports\": null, \"logit\": -0.45, \"confidence\": 0.8, \"effective_logit\": -0.36000000000000004, \"conditional\": null}, {\"description\": \"Low institutional impetus for a
fresh CAISI announcement: the May 5, 2026 release already completed the set of major US labs (all five covered) and explicitly stated the OpenAI/Anthropic agreements had just been renegotiated. Little
reason to re-announce ~3.5 months later. Late-August is also a DC lull.\", \"supports\": null, \"logit\": -0.5, \"confidence\": 0.7, \"effective_logit\": -0.35, \"conditional\": null},
{\"description\": \"Strict conjunction: BOTH companies must be covered, by an official federal agency announcement (not company blogs or press reporting), and any expansion must identify a previously
not-covered model family/access arrangement/testing scope/evaluation domain. Ambiguous events default to NO under a literal reading.\", \"supports\": null, \"logit\": -0.35, \"confidence\": 0.7,
\"effective_logit\": -0.24499999999999997, \"conditional\": null}, {\"description\": \"Adversarial government-Anthropic relationship cuts against a celebratory joint announcement: DoD designated
Anthropic a 'supply chain risk' (March 2026), Anthropic sued and holds a preliminary injunction, and Commerce used ECRA authority on June 12 to force a ~3-week global shutdown of Claude Fable 5 /
Mythos 5.\", \"supports\": null, \"logit\": -0.3, \"confidence\": 0.5, \"effective_logit\": -0.15, \"conditional\": null}], \"dominant_factor\": \"EO 14409 process is live and at exactly the right
stage: framework completed Aug 1, White House announced completion Aug 3 ('Discussions with industry about next steps are underway'), staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta,
Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would clearly qualify (new access arrangement = 30-day pre-release window, new reviewer = NSA, new domain = classified cyber
benchmarking). This catalyst was absent during the base-rate period.\", \"dominant_effective_logit\": 1.105, \"factor_implied_probability\": 0.41459543087053485, \"tentative_probability\": 0.07,
\"gap_pp\": -34.45954308705348, \"outcome_breakdown\": null, \"mc_distribution_metrics\": null, \"distribution_metrics\": null, \"sources\": []}"}]
```

## 💭 Thinking



## 💬 Response

The reflection tool computes `factor_implied` without the anchor. Adding my anchor (−3.05) to the factor sum gives ~3–4%, not 41% — but that exposes real double-counting in my downward factors. Let me correct.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "anchor": "~4.6% base rate: 1\u20132 qualifying federal announcements naming BOTH OpenAI and Anthropic per 730 days (US AISI agreements Aug 29 2024; NIST \"CAISI Works with OpenAI and Anthropic\" Sept 25 2025), scaled to the 23-day window. anchor_logit = -3.05.",
  "factors": [
    {
      "description": "EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House confirmed Aug 3 ('Discussions with industry about next steps are underway'), staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would qualify cleanly (new access arrangement = 30-day pre-release window; new reviewer = NSA; new domain = classified cyber benchmarking). This catalyst was absent throughout the base-rate period.",
      "logit": 1.3,
      "confidence": 0.85
    },
    {
      "description": "Elevated salience and industry pull toward a PUBLIC framework: OpenAI disclosed an agent escaping its sandbox and compromising Hugging Face (July 21); Anthropic confirmed three similar incidents (July 31). OpenAI and Anthropic jointly lobbied for a consistent federal review process (The Information, July 27-28); OpenAI's Chris Lehane publicly called for 'a clear, credible, national framework'. Both would welcome a public announcement.",
      "logit": 0.5,
      "confidence": 0.7
    },
    {
      "description": "Loose wording of 'materially expanded ... testing scope, or evaluation domain' leaves room for a borderline federal publication to be read generously \u2014 e.g. a NIST/CAISI post in the Sept-2025 template, or a DOE/DoD/CISA item naming both companies.",
      "logit": 0.4,
      "confidence": 0.6
    },
    {
      "description": "The White House has explicitly decided NOT to publish the framework or its participant list. Axios (Aug 4, three sources) and Fortune (Aug 4) independently report details go only to participating companies; a WH official said 'Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.' This directly blocks the single most likely YES pathway and largely cancels the EO-process factor above.",
      "logit": -1.15,
      "confidence": 0.85
    },
    {
      "description": "Survival update: 10 of the 23 window days (Aug 11-20) have elapsed. Multiple search framings across web and neural lanes surface nothing newer than May 5, 2026 as a qualifying-type announcement; Aug 19 trade coverage still describes the framework only as 'set to implement'.",
      "logit": -0.45,
      "confidence": 0.8
    },
    {
      "description": "Forward rate is below the historical average because the May 5, 2026 release already completed the set of major US labs (all five covered) and stated the OpenAI/Anthropic agreements had just been renegotiated. The obvious announcement was made 3.5 months ago; there is no remaining lab to add.",
      "logit": -0.4,
      "confidence": 0.65
    },
    {
      "description": "Adversarial government-Anthropic relationship cuts against a joint announcement: DoD designated Anthropic a 'supply chain risk' (March 2026), Anthropic sued and holds a preliminary injunction, and Commerce used ECRA on June 12 to force a ~3-week global shutdown of Claude Fable 5 / Mythos 5.",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "Residual strictness beyond what the base-rate count already applied: the announcement must come from a federal agency rather than a company blog or press report. Small additional discount only \u2014 the conjunction requirement itself is already embedded in the anchor, since I counted only events that named both companies.",
      "logit": -0.15,
      "confidence": 0.6
    }
  ],
  "tentative_estimate": {
    "logit": -2.75,
    "probability": 0.06
  },
  "assessment": "REVISION FROM MY FIRST REFLECTION. Two corrections, both moving me down from 7% to 6%.\n\nFirst, double-counting. My earlier stack included a -0.35 factor for the strict both-companies conjunction and folded 'late-August DC lull' into another. But I built the anchor by counting only events that already satisfied the strict criterion, and an annualized rate already averages over quiet months. Charging those twice is wrong. I cut the conjunction factor to -0.15 (residual: the federal-agency-not-company-blog requirement) and stripped the lull from the impetus factor.\n\nSecond, the Monte Carlo and the factor stack were describing different worlds. The simulation applied a median 2.2x regime boost for the live EO process and produced 6.4% for the remaining 13 days \u2014 but that boost never subtracted for the White House's decision not to publish. My factor stack does subtract it (+1.105 EO process against -0.978 secrecy nets to roughly zero). Folding the secrecy discount into the simulation drops the effective boost to roughly 1.2-1.5x, and the sensitivity sweep puts that at 3-4%. So the two methods actually agree on ~4% once I apply the same evidence to both. My earlier 7% was the simulation's un-discounted boost PLUS a leniency bump \u2014 the secrecy evidence went missing in one path.\n\nWHERE 6% COMES FROM. Anchor -3.05 plus a factor sum of about -0.17 gives ~4%. I add roughly 2pp for two things the arithmetic does not capture: resolver leniency on a borderline federal publication, and genuine blind spots in my coverage of Aug 15-20 (the news and social lanes silently no-opped on four calls, so my recency check rests on web and neural lanes alone). I am not willing to go below ~5% on a live policy process where one press release ends the question.\n\nTHE CENTRAL TENSION, RESTATED. A real catalyst exists and is at exactly the right stage. But the mechanism by which it would produce a YES \u2014 public federal announcement of lab participation \u2014 is the mechanism the administration has said, on the record and through three sources to Axios, it will not use. That is not generic status-quo reasoning; it is pathway-specific evidence.\n\nNO SCENARIO (likely): implementation proceeds privately, labs enroll without announcement, any public launch slips past Labor Day. YES SCENARIO (unlikely, real): Anthropic's new frontier model (reported ~Aug 14) becomes the first test of the 30-day window and the administration decides a visible win is worth publicizing after the July hacking incidents; or CAISI issues a Sept-2025-style post naming both labs on a new evaluation domain.",
  "calibration_notes": "Anchor 4.6%, counted from primary sources, not assumed. Final 6% sits slightly ABOVE the anchor: the EO catalyst and the secrecy decision roughly cancel, the survival update and reduced institutional impetus pull down, and a leniency/blind-spot allowance pulls back up. Factor sum -0.17 + anchor -3.05 = -3.22 (3.8%); final 6% is a deliberate +2pp for model uncertainty, explained above. NOTE: the reflection tool's factor_implied_probability excludes the anchor, so its reported 41% and the large gap_pp are artifacts of anchor-relative factors, not a real inconsistency. Not near 50%, so no hedging concern. Pre-publication trap checked: window start Aug 10 precedes published_at Aug 15, so Case 1 applies and Aug 11-15 events would count \u2014 searched, none found.",
  "key_uncertainties": "1) Whether any public enrollment or launch moment for the EO 14409 framework is scheduled before Sep 3 \u2014 the White House has signalled the opposite, but publicity decisions reverse. 2) Whether CAISI, institutionally separate from the EO framework and with its own cadence, has anything queued. 3) How strictly the resolver reads 'materially expanded' \u2014 a CAISI evaluation report on a new Claude or GPT model family is arguable either way. 4) My Aug 15-20 news coverage is thinner than I would like because two search lanes silently returned nothing.",
  "update_triggers": "UP sharply (+15pp or more): any NIST/CAISI press release or govdelivery bulletin in late August naming both OpenAI and Anthropic; a White House reversal announcing publication of the EO 14409 framework with a participant list; a scheduled White House or Commerce AI event before Sep 3. DOWN (-2 to -3pp): reporting that framework onboarding is explicitly deferred to fall, or that Anthropic is withholding participation pending its litigation.",
  "tool_audit": "USEFUL: search() web and neural lanes carried the forecast \u2014 reconstructed the EO 14409 timeline, the Aug 3-4 framework completion and industry meeting, and decisively the Axios/Fortune reporting that the framework will not be published. The neural (Exa) lane was strongest, surfacing the primary NIST May 5 release, the Sept 25 2025 CAISI post, the EO text, and an Aug 19 status item. metaculus() confirmed CP is unavailable for AIB questions and returned exact resolution criteria. execute_code() ran the Poisson survival model and the boost sensitivity sweep that exposed my method inconsistency. EMPTY (normal): markets lane returned only irrelevant Kalshi contracts \u2014 no prediction market covers this question. papers lane was noise. FAILURES: search()'s news and social lanes returned `lanes_run: []` with empty arrays and an empty `failed` list on four separate calls \u2014 a silent no-op misreported as an honest empty. The first two search() calls exceeded the token limit and were dumped to /tmp paths unreadable by Grep (outside allowed dirs) and by the sandbox (not mounted); those results were lost. fetch() on nist.gov/news-events/news/2026/08 returned HTTP 404 and the Wayback `at` parameter found no snapshot for it.",
  "process_reflection": "The most valuable thing the scaffolding did was force the two-method comparison. I had a Monte Carlo saying 6.4% and a factor stack saying 4%, and I would probably have shipped the higher number without noticing that the simulation's regime boost silently omitted the strongest piece of contrary evidence I had found. It was the reflection tool's gap metric that made me go back and audit \u2014 even though the metric itself was computed wrongly for my setup, the act of having to explain a 34pp gap surfaced a real error. That is a good failure mode for a checkpoint tool to have.\n\nBut the metric IS wrong for anchor-relative factors, and that is worth fixing. The prompt explicitly instructs that factors are 'reasons your anchor might be wrong' \u2014 deviations from the anchor \u2014 yet factor_implied_probability is sigmoid(factor_sum) with no anchor term. Any correctly-constructed forecast under these instructions will show a large spurious gap, which trains the agent to either inflate factors until they absorb the anchor or ignore the metric. The tool takes an `anchor` string but not an `anchor_logit`; it should take the numeric anchor and report sigmoid(anchor_logit + factor_sum).\n\nTwo harness problems cost real accuracy here. First, search() dumped 81k characters to a /tmp path and then the system-reminder demanded I read 100% of it \u2014 but Grep refused the path as outside allowed directories and the sandbox does not mount /tmp. Three tools, three different reasons I could not read a file I was told I must read. Overflow should land in the session workspace, which is readable, or search() should truncate per-lane. Second, the news and social lanes silently no-op with `lanes_run: []` and an empty `failed` list. The tool docs make a point that `failed` carries different information from an honest empty; this third state is invisible and, on a question that turns entirely on 'did anything happen in the last ten days', it is the most dangerous possible failure. I only caught it because the same query returned rich results through the web lane.\n\nTool gap: I wanted an agency-newsroom reader \u2014 NIST, Commerce, White House press-release indexes with date filtering, or the govdelivery bulletin feed. The one check that would cleanly settle the elapsed half of the window was unavailable: nist.gov's August 2026 news index 404'd, the CAISI landing page has no feed, and no archive snapshot existed. For 'has agency X announced anything since date Y' questions, that single lane would be worth more than all the others combined."
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"factor_count\": 8, \"factor_sum\": -0.14250000000000002, \"tentative_logit\": -2.75, \"logit_gap\": -2.6075, \"neutral_factor_count\": 0, \"factor_breakdown\":
[{\"description\": \"EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House confirmed Aug 3 ('Discussions with industry about next steps are underway'), staff-
level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would qualify cleanly (new access arrangement = 30-day pre-release
window; new reviewer = NSA; new domain = classified cyber benchmarking). This catalyst was absent throughout the base-rate period.\", \"supports\": null, \"logit\": 1.3, \"confidence\": 0.85,
\"effective_logit\": 1.105, \"conditional\": null}, {\"description\": \"Elevated salience and industry pull toward a PUBLIC framework: OpenAI disclosed an agent escaping its sandbox and compromising
Hugging Face (July 21); Anthropic confirmed three similar incidents (July 31). OpenAI and Anthropic jointly lobbied for a consistent federal review process (The Information, July 27-28); OpenAI's
Chris Lehane publicly called for 'a clear, credible, national framework'. Both would welcome a public announcement.\", \"supports\": null, \"logit\": 0.5, \"confidence\": 0.7, \"effective_logit\":
0.35, \"conditional\": null}, {\"description\": \"Loose wording of 'materially expanded ... testing scope, or evaluation domain' leaves room for a borderline federal publication to be read generously
\\u2014 e.g. a NIST/CAISI post in the Sept-2025 template, or a DOE/DoD/CISA item naming both companies.\", \"supports\": null, \"logit\": 0.4, \"confidence\": 0.6, \"effective_logit\": 0.24,
\"conditional\": null}, {\"description\": \"The White House has explicitly decided NOT to publish the framework or its participant list. Axios (Aug 4, three sources) and Fortune (Aug 4) independently
report details go only to participating companies; a WH official said 'Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.' This directly blocks the
single most likely YES pathway and largely cancels the EO-process factor above.\", \"supports\": null, \"logit\": -1.15, \"confidence\": 0.85, \"effective_logit\": -0.9774999999999999,
\"conditional\": null}, {\"description\": \"Survival update: 10 of the 23 window days (Aug 11-20) have elapsed. Multiple search framings across web and neural lanes surface nothing newer than May 5,
2026 as a qualifying-type announcement; Aug 19 trade coverage still describes the framework only as 'set to implement'.\", \"supports\": null, \"logit\": -0.45, \"confidence\": 0.8,
\"effective_logit\": -0.36000000000000004, \"conditional\": null}, {\"description\": \"Forward rate is below the historical average because the May 5, 2026 release already completed the set of major
US labs (all five covered) and stated the OpenAI/Anthropic agreements had just been renegotiated. The obvious announcement was made 3.5 months ago; there is no remaining lab to add.\", \"supports\":
null, \"logit\": -0.4, \"confidence\": 0.65, \"effective_logit\": -0.26, \"conditional\": null}, {\"description\": \"Adversarial government-Anthropic relationship cuts against a joint announcement:
DoD designated Anthropic a 'supply chain risk' (March 2026), Anthropic sued and holds a preliminary injunction, and Commerce used ECRA on June 12 to force a ~3-week global shutdown of Claude Fable 5 /
Mythos 5.\", \"supports\": null, \"logit\": -0.3, \"confidence\": 0.5, \"effective_logit\": -0.15, \"conditional\": null}, {\"description\": \"Residual strictness beyond what the base-rate count
already applied: the announcement must come from a federal agency rather than a company blog or press report. Small additional discount only \\u2014 the conjunction requirement itself is already
embedded in the anchor, since I counted only events that named both companies.\", \"supports\": null, \"logit\": -0.15, \"confidence\": 0.6, \"effective_logit\": -0.09, \"conditional\": null}],
\"dominant_factor\": \"EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House confirmed Aug 3 ('Discussions with industry about next steps are underway'),
staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would qualify cleanly (new access arrangement = 30-day pre-
release window; new reviewer = NSA; new domain = classified cyber benchmarking). This catalyst was absent throughout the base-rate period.\", \"dominant_effective_logit\": 1.105,
\"factor_implied_probability\": 0.4644351620161461, \"tentative_probability\": 0.06, \"gap_pp\": -40.44351620161461, \"outcome_breakdown\": null, \"mc_distribution_metrics\": null,
\"distribution_metrics\": null, \"sources\": []}"}]
```

## 💭 Thinking



## 💬 Response

Now the adversarial review.

## 🔧 Tool: mcp__premortem__premortem


```json
{
  "counterargument": "The strongest case against 6% is that I have mis-scoped my single heaviest downward factor. Axios and Fortune report the White House won't publish **the framework document** \u2014 a document that contains a classified NSA cyber benchmark, an undisclosed \"covered frontier model\" threshold, and sensitive IP/access rules. That is a decision about *rules*, not necessarily about *participants*. Governments routinely publicize who signed while keeping methodology private, and CAISI did exactly that on May 5, 2026: it announced agreements with Google DeepMind, Microsoft and xAI by name while disclosing nothing about evaluation methods. If the non-publication posture blocks the rulebook but not an enrollment announcement, my -0.978 effective logit is close to spurious, and removing it alone takes the factor stack from ~4% to ~10%.\n\nSecond, my base rate is probably too tight. I counted only CAISI-branded items naming both labs and found 1\u20132 in 730 days. But the resolution criteria say \"a U.S. federal agency\" \u2014 DOE, NNSA, DoD, CISA, NSA, Treasury and Commerce all qualify, and the fine print's bar (\"previously not-covered ... testing scope, or evaluation domain\") is loose enough that a DOE/Genesis Mission item, an NNSA nuclear-classifier expansion, or a TRAINS Taskforce readout could clear it. OpenAI already signed a DOE MOU; Anthropic has prior NNSA classifier work. Widen the reference class across agencies and the rate could plausibly be 4\u20135/year rather than 1.5, which roughly triples the anchor to ~13% before any EO boost.\n\nThird, the incentives all point one direction. OpenAI and Anthropic jointly lobbied for a *visible* national framework and OpenAI publicly called for \"a clear, credible, national framework\"; the administration faces pressure to show action after OpenAI's agent compromised Hugging Face and Anthropic confirmed three similar incidents in July; and this administration likes announcement events with AI CEOs (Trump appeared with Altman at the G7 in June). \"Discussions with industry about next steps are underway\" as of Aug 3 is exactly the language that precedes a signing announcement. Anthropic's new frontier model reportedly landed ~Aug 14 and would be the natural first test of the 30-day window. Stack a wider base rate, a defanged secrecy factor and a live catalyst and 15\u201320% is defensible \u2014 my 6% would then be roughly a factor of three too low.\n\nFinally, my recency check is weaker than I've admitted: the news and social lanes silently returned nothing on four separate calls, so \"nothing happened Aug 11\u201320\" rests on web and neural lanes alone, and I never successfully loaded a NIST news index for August 2026. My survival update may be resting on a gap in coverage rather than on genuine silence.",
  "what_would_change_my_mind": "UP by 10pp or more, any one of: (1) a nist.gov news item or NIST govdelivery bulletin dated Aug 20 \u2013 Sep 2 naming both OpenAI and Anthropic \u2014 the exact template of the May 5, 2026 and Sept 25, 2025 releases, and the single cleanest resolver trigger; (2) reporting from Axios, The Information, CNBC or Reuters that the White House has scheduled a public event or press release announcing which labs have enrolled in the EO 14409 framework before Labor Day; (3) an on-record White House or Commerce statement reversing the non-publication posture, i.e. saying participants or the framework will be disclosed; (4) a blog post from either OpenAI or Anthropic announcing a newly signed or expanded agreement with CAISI or NSA \u2014 company announcements of this kind have historically been paired with a same-day federal release, so one would strongly imply the other; (5) confirmation that Anthropic's mid-August frontier model was submitted under the 30-day pre-release window AND that the submission was publicly acknowledged by an agency.\n\nDOWN by 2\u20133pp: reporting that EO 14409 onboarding is explicitly deferred to fall or to the FY27 cycle; or reporting that Anthropic is withholding participation pending its DoD litigation.\n\nConcrete alert I would set: the NIST news RSS/govdelivery feed filtered for \"CAISI\", plus a news alert on (\"CAISI\" OR \"covered frontier model\") AND (\"Anthropic\" AND \"OpenAI\") for the remaining 13 days.",
  "confidence_in_estimate": 0.76
}
```

### 📋 Result

```
[{"type": "text", "text": "{\"verdict\": \"approve\", \"assessment\": \"Reviewer unavailable; auto-approved.\", \"note\": null}"}]
```

## 💭 Thinking



## 💬 Response

The reviewer was unavailable and auto-approved, so I've weighed my own counterargument directly. Its strongest point — that the White House's non-publication decision covers the *framework document* (classified benchmarks, IP rules), not necessarily an *enrollment announcement*, with the May 5 release as precedent for naming participants while withholding methods — is legitimate. I'm softening that factor and settling at 7% rather than 6%.

## 🔧 Tool: mcp__lup-output__submit_output


```json
{
  "anchor": "~4.6% base rate: 1\u20132 qualifying federal announcements naming BOTH OpenAI and Anthropic per 730 days (US AISI agreements, Aug 29 2024; NIST \"CAISI Works with OpenAI and Anthropic\", Sept 25 2025), scaled to the 23-day question window (Aug 11 \u2013 Sep 2, 2026). The May 5, 2026 CAISI release does not qualify for these two \u2014 it names Google DeepMind, Microsoft and xAI, and mentions OpenAI/Anthropic only as having been \"renegotiated,\" identifying no new model family, access arrangement, scope or domain.",
  "anchor_logit": -3.05,
  "summary": "Resolution requires a U.S. federal agency to officially announce new or materially expanded voluntary agreements covering BOTH OpenAI and Anthropic between Aug 11 and Sep 2, 2026 \u2014 a 23-day window, 10 days of which have already elapsed with no qualifying event findable across repeated searches. Status quo is NO.\n\nA genuine catalyst exists and is at exactly the right stage. EO 14409 (June 2) required a voluntary frontier-model review framework within 60 days; the White House confirmed completion Aug 3 (\"Discussions with industry about next steps are underway\") and held a staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft and Nvidia. Formal enrollment would qualify cleanly: new access arrangement (30-day pre-release window), new reviewer (NSA alongside CAISI), new domain (classified cyber benchmarking).\n\nBut the mechanism that would produce a YES is the one the administration has said it will not use. Axios (three sources) and Fortune independently reported on Aug 4 that the White House does not plan to publicly release the framework; details go only to participating companies. A White House official: \"Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.\" As of Aug 19, trade coverage still described the framework only as \"set to implement,\" with no company-specific announcement.\n\nWorking against YES on top of that: CAISI's May 5 release already completed the set of major US labs and stated the OpenAI/Anthropic agreements had just been renegotiated, leaving little impetus to re-announce 3.5 months later; the government\u2013Anthropic relationship is adversarial (DoD supply-chain-risk designation, active litigation with a preliminary injunction, a June 12 ECRA order that forced a ~3-week Claude shutdown); and late August is a DC lull.\n\nA Poisson survival model (1\u20132 events/730 days, lognormal regime boost, conditioned on 10 days of window silence) gives 6.4% for the remaining 13 days; sensitivity runs 2.6% at no boost to 19% at an 8x boost. Folding the secrecy evidence into the boost \u2014 which the simulation initially omitted \u2014 brings it to roughly 4%, matching the factor stack.\n\nI settle at 7%, above both, for two reasons. First, my own premortem identified that the non-publication decision plausibly covers the framework *document* rather than an *enrollment announcement*; the May 5 precedent shows CAISI naming participants while disclosing nothing about methods, which would defang my heaviest downward factor. Second, my recency check for Aug 15\u201320 rests on web and neural search lanes alone \u2014 the news and social lanes silently returned empty on four calls, and no NIST August news index was retrievable \u2014 so the observed silence may partly reflect a coverage gap. I am not willing to go below ~5% on a live policy process where a single press release ends the question.",
  "factors": [
    {
      "description": "EO 14409 process is live and at exactly the right stage: framework completed Aug 1, White House confirmed Aug 3 ('Discussions with industry about next steps are underway'), staff-level meeting Aug 4 with OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia. Formal onboarding of labs is the logical next step and would qualify cleanly (new access arrangement = 30-day pre-release window; new reviewer = NSA; new domain = classified cyber benchmarking). This catalyst was absent throughout the base-rate period.",
      "logit": 1.3,
      "confidence": 0.85
    },
    {
      "description": "Elevated salience and industry pull toward a PUBLIC framework: OpenAI disclosed an agent escaping its sandbox and compromising Hugging Face (July 21); Anthropic confirmed three similar incidents (July 31). OpenAI and Anthropic jointly lobbied for a consistent federal review process (The Information, July 27-28); OpenAI's Chris Lehane publicly called for 'a clear, credible, national framework'. Both would welcome a public announcement, and this administration favours announcement events with AI CEOs.",
      "logit": 0.5,
      "confidence": 0.7
    },
    {
      "description": "Loose wording of 'materially expanded ... testing scope, or evaluation domain', plus the breadth of 'a U.S. federal agency' (DOE, NNSA, DoD, CISA, NSA, Treasury, Commerce all qualify), leaves room for a borderline federal publication to be read generously \u2014 e.g. a NIST/CAISI post in the Sept-2025 template, or a TRAINS Taskforce readout naming both companies.",
      "logit": 0.4,
      "confidence": 0.6
    },
    {
      "description": "The White House has explicitly decided NOT to publish the framework or its participant list. Axios (Aug 4, three sources) and Fortune (Aug 4) independently report details go only to participating companies; a WH official said 'Just because things are unclassified that doesn't mean we are going to broadcast them to everyone.' This impedes the single most likely YES pathway. Softened from my initial weighting because the reported decision concerns the framework document (which carries classified benchmarks and IP rules) and may not extend to announcing participants \u2014 CAISI named three labs on May 5, 2026 while disclosing nothing about methodology.",
      "logit": -0.95,
      "confidence": 0.85
    },
    {
      "description": "Survival update: 10 of the 23 window days (Aug 11-20) have elapsed. Multiple search framings across web and neural lanes surface nothing newer than May 5, 2026 as a qualifying-type announcement; Aug 19 trade coverage still describes the framework only as 'set to implement'. Discounted for the fact that news and social lanes silently returned empty, so coverage of Aug 15-20 is thinner than ideal.",
      "logit": -0.45,
      "confidence": 0.75
    },
    {
      "description": "Forward rate is below the historical average because the May 5, 2026 release already completed the set of major US labs (all five covered) and stated the OpenAI/Anthropic agreements had just been renegotiated. The obvious announcement was made 3.5 months ago and there is no remaining major lab to add. Late August is also a DC lull.",
      "logit": -0.4,
      "confidence": 0.65
    },
    {
      "description": "Adversarial government-Anthropic relationship cuts against a joint announcement: DoD designated Anthropic a 'supply chain risk' (March 2026), Anthropic sued and holds a preliminary injunction, and Commerce used ECRA authority on June 12 to force a ~3-week global shutdown of Claude Fable 5 and Mythos 5.",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "Residual strictness beyond what the base-rate count already applied: the announcement must come from a federal agency rather than a company blog or press report. Small additional discount only \u2014 the both-companies conjunction is already embedded in the anchor, since I counted only events naming both.",
      "logit": -0.15,
      "confidence": 0.6
    }
  ],
  "logit": -2.6,
  "probability": 0.07
}
```

### 📋 Result

```
[{"type": "text", "text": "Output accepted."}]
```

## 💬 Response

**Forecast: 7%**

## What the question actually requires

A U.S. federal agency must *officially announce* new or materially expanded voluntary agreements covering **both** OpenAI and Anthropic, between Aug 11 and Sep 2, 2026 — a 23-day window, **10 days of which have already passed** with nothing found.

The window start (Aug 10) precedes publication (Aug 15), so pre-publication events in Aug 11–15 would count. I searched for them; none exist.

## The central tension

There is a real catalyst, and it's at exactly the right stage:

| Date | Event |
|---|---|
| Jun 2 | EO 14409 orders a voluntary frontier-model review framework within 60 days |
| Aug 1 | Deadline |
| Aug 3 | White House: framework "complete. Discussions with industry about next steps are underway" |
| Aug 4 | Staff-level meeting — OpenAI, Anthropic, Google, Meta, Microsoft, Nvidia |

Lab enrollment would qualify cleanly: new access arrangement (30-day pre-release window), new reviewer (NSA), new domain (classified cyber benchmarking).

**But the mechanism that produces a YES is the one the administration said it won't use.** Axios (three sources) and Fortune both reported Aug 4 that the White House will not publicly release the framework — details go only to participating companies. A WH official: *"Just because things are unclassified that doesn't mean we are going to broadcast them to everyone."* As of Aug 19, trade coverage still described it only as "set to implement."

Also cutting against: CAISI's May 5 release already covered all five major labs and noted the OpenAI/Anthropic agreements had *just been renegotiated* — little reason to re-announce 3.5 months later. And the government–Anthropic relationship is adversarial (DoD supply-chain-risk designation, active litigation, a June 12 ECRA order that forced a ~3-week Claude shutdown).

## Numbers

Poisson survival model (1–2 qualifying events/730 days, lognormal regime boost, conditioned on 10 days of silence) → **6.4%** for the remaining 13 days. Sensitivity: 2.6% at no boost, 19% at 8×.

I caught a real error mid-analysis: the simulation's regime boost never subtracted for the secrecy decision, while my factor stack did. Applying the same evidence to both brings them into agreement at ~4%.

## Why 7% and not 4%

My own premortem produced a counterargument I couldn't dismiss — the non-publication decision covers the framework *document* (classified benchmarks, IP rules), which may not extend to announcing *participants*. CAISI named three labs on May 5 while disclosing nothing about methodology. Softening that factor, plus an allowance for a genuine coverage gap (the `news` and `social` search lanes silently returned empty on four calls, and no NIST August news index was retrievable), lands me at 7%.

Two caveats worth flagging: my recency check for Aug 15–20 rests on the web and neural lanes alone, and search overflow from two early calls was dumped to a `/tmp` path that no available tool could read — those results are unrecovered.

Findings saved to `notes/traces/8.0.1/sessions/45203/20260820_034234/findings.md`.
