# Reasoning Log: Will the community prediction be higher than 74.20% on 2026-03-28 for the Metaculus question "Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?"?

*Generated: 2026-03-16T03:52:56.730005+00:00*


## 💭 Thinking

Let me analyze this meta-prediction question carefully.

## Step 1: Parse the Resolution Criteria

This is a meta-prediction question asking: Will the community prediction (CP) on Metaculus question #41140 be **higher than 74.20%** on **2026-03-28 22:40:01**?

Key details:
- Current CP as of 2026-03-14: 74.20%
- The threshold is 74.20% (the current value)
- Resolution date: 2026-03-28 (about 12 days from now)
- The question closes on 2026-03-16 (today), so I need to make my forecast now


- The underlying question asks: "Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?"

## Step 2: This is a Meta-Prediction

I'm forecasting where the CP will be on March 28, not the underlying event itself. The real question is whether CP will move above 74.20% by then. Looking at the historical trend, the CP has been climbing steadily—from 55% in early February up to 70% by the end of the month, gaining roughly 5 percentage points per week.

Since the threshold is exactly at the current CP level of 74.20%, I'm essentially asking whether the trend will continue and push it higher over the next two weeks. The pattern has been consistent for over a month, so I should dig into what's driving the underlying question to see if that momentum is likely to hold.

## 🔧 Tool: mcp__markets__get_metaculus_questions


## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__markets__polymarket_price


```json
{
  "post_id_list": [
    41140
  ]
}
```

### 📋 Result

```
{"post_id": 41140, "title": "Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/41140", "background_info":
"[METR](https://metr.org/) is an AI model evaluation and threat research organisation that studies AI capabilities and their ability to conduct AI research and self-improve.\n\nMETR regularly tests
released models for their threat capacity, which includes measuring their ability to complete realistic software and research tasks reliably. For each task, they measure how long it takes humans with
relevant expertise to complete it, then see which tasks different models can solve. By fitting a curve of model success against human task duration, they define each model's \"[time
horizons](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)\": the longest task length (in human time) on which the model can succeed with around 50% or 80%
probability.\n\nTheir results show that these horizons have been growing exponentially over time. As of December 2025 the highest time horizon with an 80% chance of success is 31 minutes by
[GPT-5.1-Codex-Max](https://evaluations.metr.org/gpt-5-1-codex-max-report/), a 5x improvement from 2024's best performer GPT-o1.", "resolution_criteria": "This question will resolve as **Yes** if,
during 2026, [METR estimates](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) that an AI model has a time horizon of \u22653 hours at 80% reliability, i.e. the AI has an
estimated\u00a0\u226580% reliability on tasks requiring human experts\u00a0\u22653 hours to solve.", "fine_print": "* If METR substantially changes their dataset such that new estimates are not
comparable to old estimates, this question will use the closest available equivalent to the dataset used during December 2025.\n* If METR ceases estimating a model's time horizon at \u226580%
reliability, this question will be **annulled**.\n* Current estimated time horizons are presented as \"Task duration\" or \"Task length\" when mouseovering models in the \"Measuring AI Ability to
Complete Long Tasks\" graph.", "num_forecasters": 809, "community_prediction": null}
```

```json
{
  "query": "METR AI model time horizon 3 hours reliability 2026",
  "n_articles": 10,
  "hours_back": 720
}
```

### 📋 Result

```
{"as_dicts":null,"as_string":"------News Summaries Start------\n<doc>\nCitation key: [1]\nTitle: Singularity Update: You Have No Idea How Crazy Humanoid Robots Have Gotten\n\nSummary: \nAt Figure
headquarters in San Jose, CEO Brett Adcock and David Blundin demonstrated fully autonomous humanoid robots capable of 67 consecutive hours of work with only one error, marking a shift from traditional
coded robotics to 'Helix 2', a single neural network controlling the entire robot. This approach allows robots to learn from experience rather than instructions, enabling generalization to unseen
tasks and environments. Figure has vertically integrated its manufacturing, producing its own actuators, hands, and compute systems to ensure rapid iteration, with a facility in Baku designed for
50,000 units annually and plans to scale to millions. The company aims to deploy robots in unseen homes by 2026 for long-horizon tasks, followed by scaled pilots in 2027-2028. Figure's business model
involves leasing robots for approximately $300 per month ($10/day), positioning them as 50 times cheaper than human labor. The article projects that by 2030, developed households could lease robots
for household chores, and by 2035, 10 billion humanoid robots could exist globally, fundamentally altering the economy by removing labor as a constraint.\n\nPublished date: March 15 2026,
12:10\n\nURL: https://www.zerohedge.com/ai/singularity-update-you-have-no-idea-how-crazy-humanoid-robots-have-gotten\nSource: Zero Hedge\nClassification: Technology\nSentiment: positive\nReporting
voice: Narrative\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [2]\nTitle: The Three Reliability Modes I See in Production AI Agents\n\nSummary: \nFollowing months of running autonomous
AI agents in production, the author identifies three reliability modes for these systems. Mode 1 involves agents following strict decision trees, which are predictable but limited to repetitive tasks
with low variation. Mode 2 utilizes LLM prompts for decision-making, offering flexibility but resulting in unpredictability under edge cases; this is described as the mode where 'most teams operate.'
Mode 3 consists of agents that modify their own prompts and behavior based on feedback, making them the most powerful yet risky due to the potential to drift from intended behavior. The author notes
that most production systems mix all three modes and emphasizes the importance of knowing which mode each agent operates in to monitor accordingly. The article was published on March 15, 2026, on DEV
Community.\n\nPublished date: March 15 2026, 03:54\n\nURL: https://dev.to/the_bookmaster/the-three-reliability-modes-i-see-in-production-ai-agents-3h8n\nSource: DEV Community\nClassification:
Technology\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [3]\nTitle: Research Analysis\n\nSummary: \nMuhammad Abbas, a BS-CS student at
FAST NUCES Peshawar, analyzes two research papers that redefine AI from a passive prompt-responding model to an active 'agentic' system. The first paper, 'The Rise of Agentic AI' by Bandi et al.
(2025) from Northwest Missouri State University, reviewed 143 studies (90% from 2024-2025) and argues that agentic AI decomposes goals into sub-tasks, uses memory, reflects on errors, and utilizes
tools with minimal supervision. A 2025 MIT Sloan and Boston Consulting Group survey found 35% of organizations adopted AI agents by 2023, with 44% planning deployment, while Google Trends showed
search interest for 'agentic AI' peaked in July 2025. The second paper, 'A Survey of LLM-based Deep Search Agents' by Xi et al. (2025) from Shanghai Jiao Tong University, details three generations of
search, culminating in agents that plan multi-step retrieval strategies. Abbas notes that the DeepWideSearch benchmark (arXiv:2510.20168) revealed a critical failure mode: frontier models like GPT-5,
Gemini 2.5 Pro, and Claude Sonnet 4 achieved only a 2.39% average success rate on combined deep reasoning and wide-scale information gathering tasks. The analysis highlights that while these systems
map to course concepts like PEAS, BFS, DFS, and A* heuristics, they face significant challenges in reliability, error compounding, and long-horizon planning.\n\nPublished date: March 14 2026,
18:29\n\nURL: https://dev.to/abbas_c3296322e33f/research-analysis-1ep7\nSource: DEV Community\nClassification: Technology\nSentiment: neutral\nReporting voice: Analytical\nContinent:
Asia\n\n</doc>\n\n<doc>\nCitation key: [4]\nTitle: Observability for AI-Assisted Development\n\nSummary: \nA March 14, 2026 article published in DEV Community argues that the software development
industry lacks effective observability for AI-assisted development, leading to unreliable perceptions of productivity. The author cites a 2025 METR study where experienced open-source developers
estimated they were 24% faster using AI, while a randomized controlled trial measured them at 19% slower, revealing a self-assessment error of over 40 percentage points. The article contends that
without pre-existing baselines for metrics like cycle time, deployment frequency, and change failure rate, teams cannot accurately attribute improvements to AI. While cost visibility is described as
'reasonable' in tools like Claude Code and Cline, quality visibility is characterized as 'nearly zero' across the industry. The author details the fragmented tooling landscape: Claude Code offers
native OpenTelemetry support and commit tagging; OpenAI Codex CLI supports OTel export and enterprise dashboards; GitHub Copilot focuses on license value via acceptance rates; and Cursor offers
minimal data. The article identifies critical gaps in observability, including the inability to track effort distribution, detect failure patterns, correlate AI-generated commits with incident rates,
or provide an aggregate view of organizational maturity. The author proposes a vision for future tools that includes 'AI timesheets' for self-awareness, automated Root Cause Analysis (RCA) tagging,
context effectiveness scoring for configuration files like CLAUDE.md, and a stitched-together org-wide view combining git, ticket, CI, and AI usage data to determine if AI is delivering value or
merely degrading quality.\n\nPublished date: March 14 2026, 12:57\n\nURL: https://dev.to/javatarz/observability-for-ai-assisted-development-2m06\nSource: DEV Community\nClassification:
Technology\nSentiment: negative\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [5]\nTitle: You Can't Fix What You Can't See: The AI Agent Observability
Crisis\n\nSummary: \nThe article, published by DEV Community on March 14, 2026, addresses the 'AI agent observability crisis,' arguing that traditional monitoring metrics like uptime and latency are
insufficient for production-grade AI agents. It details a scenario where an agent operated for three weeks with 'near zero' error rates and 'nominal' latency, yet consistently recommended the wrong
API version because its outputs were syntactically correct but semantically wrong. The author identifies four distinct failure categories requiring specific detection strategies: 1) Semantic drift,
where outputs shift away from intended behavior over time; 2) Tool reliability failures, where agents propagate stale or incorrect data from external tools; 3) Context window saturation, causing
agents to 'forget' early constraints; and 4) Silent task incompletion, where agents return partial outputs formatted as complete answers. The article evaluates the 2026 tooling landscape, noting that
no single platform covers all failure modes equally. It highlights LangSmith as the default for LangChain users ($39/seat for the Plus plan), Arize Phoenix as a standout open-source option using
OpenTelemetry, Galileo for real-time evaluation using lightweight models, and Helicone as a lightweight gateway for cost tracking. The author recommends a two-tool approach combining a tracing
platform (like Phoenix or LangSmith) with an evaluation layer (like Galileo or Braintrust). A five-step instrumentation priority is proposed: 1) Span-level traces for tool calls, 2) Task completion
rate (aiming for >95%), 3) Token budget per session (alerting at ~70% of context window), 4) Output evaluation on a 5-10% sample, and 5) Memory freshness metrics (flagging data older than 7 days in
fast-moving domains). The piece concludes that the most dangerous period for deployments is 'week three,' when slow failures compound unnoticed, and emphasizes that the gap in agent operations is
cultural rather than technical.\n\nPublished date: March 14 2026, 12:39\n\nURL: https://dev.to/ai_agent_digest/you-cant-fix-what-you-cant-see-the-ai-agent-observability-crisis-2adl\nSource: DEV
Community\nClassification: Technology\nSentiment: negative\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [6]\nTitle: 谷歌：Genie
3能力已明显进步，AI生成游戏世界能保持一分钟稳定\n\nSummary: \nOn March 14, 2026, Google DeepMind updated its Genie 3 platform, demonstrating progress in AI-generated interactive worlds while acknowledging significant
limitations. According to reports from TechSpot and IT Home, the Genie 3 model can now maintain a stable 3D environment for approximately one minute, a notable improvement over early versions that
lasted only a few seconds. However, beyond this timeframe, the scene typically degrades into chaos. The system generates content frame-by-frame, functioning more like a text-driven video stream than a
traditional 3D game engine. Alexander Muffler, a DeepMind researcher, stated that Project Genie aims to assist, not replace, the game development industry. While the technology is viewed as a step
toward Artificial General Intelligence (AGI) by enabling 'world models' to predict environmental changes, Genie 3 is not yet ready for commercial game production.\n\nPublished date: March 14 2026,
12:37\n\nURL: https://finance.sina.com.cn/stock/t/2026-03-14/doc-inhqyhws0315413.shtml\nSource: 新浪财经\nClassification: Technology\nSentiment: neutral\nReporting voice: Objective\nContinent: North
America\n\n</doc>\n\n<doc>\nCitation key: [7]\nTitle: Assessing heterogeneity in METR's late 2025 developer productivity experiment -- LessWrong\n\nSummary: \nMaya Farber Brodsky analyzed data from
METR's late 2025 developer productivity experiment to assess heterogeneity in AI's effect on task completion time. While the sample-wide estimated speedup is 6%, the analysis reveals significant
variation: tasks predicted by developers to benefit substantially from AI saw a 13% speedup, and the individual developer with the highest estimated speedup achieved a 33% speedup. The article notes
that METR's original study found a speedup of -18% for returning developers and -4% for new recruits, with confidence intervals indicating uncertainty. Brodsky further estimated a 'synthetic' speedup
of approximately 25% by heuristically accounting for potential selection bias, assuming 50% of tasks were excluded because developers did not want to complete them without AI. The analysis focuses on
estimation rather than characterizing uncertainty, and the author explicitly states these figures are not personal best-guesses.\n\nPublished date: March 14 2026, 12:27\n\nURL:
https://www.lesswrong.com/posts/dFmQThALG8EdZFqgL/assessing-heterogeneity-in-metr-s-late-2025-developer\nSource: Maya Farber Brodsky\nClassification: Technology\nSentiment: neutral\nReporting voice:
Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [8]\nTitle: The AI Agent Bubble Is Starting to Leak\n\nSummary: \nAccording to an article published on March 14, 2026, in DEV
Community, the AI agent sector is experiencing a 'leak' in its hype bubble, with three companies the author knows personally quietly shelving AI agent projects after 18-month efforts. The author, who
identifies as a developer, argues that while AI models are 'incredible,' agents fail in production because they are 'non-deterministic systems operating in deterministic environments.' Specific
failures cited include an agent confidently lying to a customer about a shipped order after misinterpreting an API response, and the general inability of agents to handle rate limits (e.g., 429
errors) or ambiguous inputs gracefully. The article distinguishes between 'chains' (glorified, human-in-the-loop workflows) and true 'autonomy,' noting that real autonomy requires reliable judgment
under uncertainty, which current models struggle with due to compounding errors in multi-step workflows. The author predicts that reliable, genuinely autonomous agents for complex tasks are '18-24
months away,' not due to model intelligence, but because infrastructure, error recovery patterns, and observability tooling are still being developed. The summary notes that while use cases like code
generation and document processing with human review are working, 'set it and forget it' autonomy for tasks involving money or customer communication is not yet viable. The article concludes that the
industry is in a phase of 'boring, incremental reliability improvements' rather than a total collapse, with the bubble 'leaking' to reveal a smaller but 'still pretty interesting'
reality.\n\nPublished date: March 14 2026, 12:01\n\nURL: https://dev.to/taskconcierge/the-ai-agent-bubble-is-starting-to-leak-14e4\nSource: DEV Community\nClassification: Technology\nSentiment:
neutral\nReporting voice: Subjective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [9]\nTitle: How to Measure Whether Your AI Agent Actually Delivers\n\nSummary: \nThe article, published
on March 14 2026 by DEV Community, addresses the limitation of 'vouch-based trust' in AI agents, which measures relationships rather than actual performance. To close this gap, the AIP v0.5.42 release
introduces a 'Probabilistic Delegation Reliability' (PDR) score. This system requires agents to submit signed observations comparing what they promised versus what they delivered. According to the
text, over-delivery improves calibration, while under-delivery reduces the score. The PDR score combines social trust (vouches) with behavioral reliability; a high number of vouches combined with poor
delivery results in a low composite score, which the system automatically uses to quarantine unreliable agents. The development of PDR involved collaboration with Nanook, who proposed the integration
and contributed a scoring algorithm derived from a 28-day pilot involving 13 agents and real production data. The system features public scores, observation history with chain hashes for tamper
detection, and automated divergence alerts that trigger when an agent's social trust diverges from its actual delivery performance.\n\nPublished date: March 14 2026, 11:59\n\nURL:
https://dev.to/thenexusguard/how-to-measure-whether-your-ai-agent-actually-delivers-26fo\nSource: DEV Community\nClassification: Technology\nSentiment: neutral\nReporting voice: Objective\nContinent:
North America\n\n</doc>\n\n<doc>\nCitation key: [10]\nTitle: The Hidden Layer of AI Systems Nobody Talks About: Evaluation\n\nSummary: \nJaideep Parashar, presented by Rethynk AI, argues that
'Evaluation' is the overlooked yet critical layer of AI systems necessary to ensure reliability and trust. Unlike deterministic software where correctness is binary, AI models produce variable
outputs, requiring continuous evaluation to detect issues like hallucinations, bias, or performance drift that may otherwise go unnoticed until they harm users. According to the article, effective
evaluation measures multiple dimensions: consistency across repeated tasks, compliance with ethical and legal policies, and efficiency regarding cost and latency. The text states that a robust
strategy must combine automated tests with human judgment, as automation alone is insufficient for nuanced behavioral assessment. Parashar notes that while evaluation does not produce visible product
features, its absence creates hidden risks, and as AI systems mature, evaluation is becoming a standard architectural component similar to logging in cloud systems. The article was published on March
14, 2026, by DEV Community.\n\nPublished date: March 14 2026, 03:42\n\nURL: https://dev.to/jaideepparashar/the-hidden-layer-of-ai-systems-nobody-talks-about-evaluation-44c7\nSource: DEV
Community\nClassification: Technology\nSentiment: neutral\nReporting voice: Explanatory\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [11]\nTitle: Something Changed in AI Two Weeks Ago
And Almost Nobody Is Talking About It\n\nSummary: \nAccording to the article published on Medium.com on March 13, 2026, a significant shift in AI reliability occurred approximately two weeks prior,
enabling a 'quiet automation explosion' where tasks previously requiring weeks of engineering now take only afternoons. The author attributes this change to a drop in error rates for Large Language
Models (LLMs), specifically citing 'Claude / GPT-4o / Gemini' as the reasoning layers now capable of reliable tool use and memory. A specific example provided involves a financial research workflow
that previously required '3 analysts, 2 weeks, custom dashboards,' but can now be executed by an agent in '~40 seconds' by pulling data from the 'FRED API' and cross-referencing earnings calls. The
article notes that teams failing six months ago due to 'hallucinations, context limits, unreliable outputs' are now rebuilding these tools successfully in hours.\n\nPublished date: March 13 2026,
14:40\n\nURL: https://medium.com/@neerupujari5/something-changed-in-ai-two-weeks-ago-and-almost-nobody-is-talking-about-it-2a8ffe5fd60f\nSource: Medium.com\nClassification: Technology\nSentiment:
positive\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [12]\nTitle: \"Les agents IA prendront bientôt le contrôle de votre navigateur Web\" : les prédictions
d'Aymeric Roucher\n\nSummary: \nIn an interview with L'Express published on March 11, 2026, AI engineer Aymeric Roucher, author of the upcoming book 'Ultra-intelligence' (Odile Jacob, 2025) and former
HuggingFace employee, discusses the rapid evolution of AI agents. Roucher explains that the rise of platforms like Moltbook—which was recently acquired by Meta and described as a 'social network for
AI agents'—and OpenClaw (founded by Peter Steinberger, who recently joined OpenAI) marks a shift from simple chatbots to autonomous agents capable of planning and executing tasks. He notes that the
four major AI laboratories—xAI, Anthropic, OpenAI, and Google—are now closely matched in performance. According to data from the METR benchmark, the average autonomy horizon for AI agents has surged
from just a few minutes in 2023 with GPT-4 to nearly 15 hours with the latest Claude Opus. Roucher attributes this progress to 'scaling laws' and the adoption of reinforcement learning, which allows
models to learn from trial and error. However, he warns of risks, including 'hallucinations' and economic biases where agents stop prematurely to save costs; he personally spends 600 euros per month
on AI inference. Roucher predicts that by 2026, the next major leap will be 'Computer Use,' allowing agents to navigate the web using virtual keyboards and mice. He forecasts a significant drop in
demand for human software developers within a year, as agents can replicate projects that previously took teams of ten engineers a decade to build, and anticipates similar impacts on legal and medical
fields within two to three years.\n\nPublished date: March 11 2026, 15:14\n\nURL: https://www.lexpress.fr/economie/high-tech/les-agents-ia-prendront-bientot-le-controle-de-votre-navigateur-web-les-
predictions-daymeric-roucher-RCFQOY2ZVNDSBM2UV7C7H522IY/\nSource: LExpress.fr\nClassification: Technology\nSentiment: neutral\nReporting voice: Objective\nContinent:
Europe\n\n</doc>\n\n<doc>\nCitation key: [13]\nTitle: AI专家：对AI的质疑是对\"指数级增长趋势\"的\"自欺欺人\"\n\nSummary: \nJulian Schrittwieser, a researcher at the AI company Anthropic, argues in a blog post that
skepticism regarding an 'AI bubble' or 'plateau' is a 'self-deception' that misreads the technology's exponential growth trend. Schrittwieser compares this dismissal to the initial ignorance of the
exponential spread of the COVID-19 pandemic. His core argument relies on two key studies: METR's 'Measuring AI's Ability to Complete Long Tasks' and OpenAI's 'GDPval' assessment. According to METR
data, AI models' ability to autonomously complete software engineering tasks is doubling at an exponential rate; models from seven months ago (Sonnet 3.7) could complete one-hour tasks with 50%
success, while newer models including Grok 4, Opus 4.1, and GPT-5 now handle tasks exceeding two hours. In the GDPval assessment covering 44 professions across 9 industries, Schrittwieser notes that
the latest GPT-5 is 'surprisingly close' to human performance, while the earlier-released Claude Opus 4.1 performed 'almost matching' the industry experts who provided the tasks (average 14 years of
experience). Schrittwieser praised OpenAI for this evaluation, stating it showed 'integrity and care for beneficial AI outcomes' by revealing another lab's model outperforming their own. Based on
these trends, Schrittwieser projects that by mid-2026, models will be able to work autonomously for a full 8-hour day; by the end of 2026, at least one model will reach human expert levels in many
industries; and by the end of 2027, models will frequently surpass experts in many tasks. The article, published on March 09 2026, suggests that if these improvements were to stop suddenly, it would
be 'extremely surprising'.\n\nPublished date: March 09 2026, 19:16\n\nURL: https://k.sina.com.cn/article_7857201856_1d45362c0019030un0.html\nSource: k.sina.com.cn\nClassification:
Technology\nSentiment: positive\nReporting voice: Objective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [14]\nTitle: The End of the One-Model Era: Building Multi-AI Workflows in
2026\n\nSummary: \nAccording to January 2026 benchmark data, the 'one-model era' of AI is over, as no single model dominates all tasks. GPT-5.2 leads the Artificial Analysis Intelligence Index with 50
points, while Claude Opus 4.5 follows closely at 49 points; however, Gemini 3 Pro leads the LMArena user preference rankings for creative tasks. The author, a developer who rebuilt their workflow over
the last month, reports that specialization is now key: GPT-5.2 with extended reasoning is best for complex analysis, Claude Opus 4.5 is preferred for coding (with METR estimating it completes
software tasks taking humans nearly five hours with at least a 50% success rate), and Gemini 3 Pro is favored for natural-sounding writing. Additionally, Gemini 3 Flash and GPT-4o are noted for speed
and cost efficiency in quick tasks. Market share data indicates a shift away from ChatGPT, which dropped from 87% to 68% in one year, while Gemini rose from 5% to 18%. Currently, 81% of users employ
GPT, 43% use Claude, and 35% use Gemini. Despite these gains, the author notes practical challenges including context transfer issues, varying prompting styles, and the administrative burden of
managing four different subscriptions. The article concludes that while multi-model workflows introduce friction, the capability gains justify the effort, urging users to adopt a flexible, task-
specific approach rather than remaining loyal to a single provider.\n\nPublished date: March 08 2026, 21:27\n\nURL: https://dev.to/joozio/the-end-of-the-one-model-era-building-multi-ai-workflows-
in-2026-3pn1\nSource: DEV Community\nClassification: Technology\nSentiment: neutral\nReporting voice: Subjective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [15]\nTitle: Matt Shumer is
(mostly) wrong\n\nSummary: \nOn March 07, 2026, a Medium.com article titled 'Matt Shumer is (mostly) wrong' analyzes and rebuts claims made by Matt Shumer regarding the capabilities of AI in software
engineering. Shumer claimed that AI now produces finished, error-free code in four hours without human intervention, citing a 'bootstrap' strategy where AI labs prioritized coding to build smarter AI
versions. The article's AI analysis and author refute this, noting that Shumer ignores the 'Reliability Wall.' While Shumer cites METR data showing AI completing tasks in nearly five hours (a figure
doubling every four to seven months), the article clarifies this 50% accuracy metric applies only to simple tasks; the 80% accuracy window remains flat at 27-32 minutes. The author argues that a 20%
failure rate every 30 minutes leads to 'Stochastic Divergence,' where AI builds on hallucinated foundations. Regarding the claim that 'AI helped build itself,' the article distinguishes between
'Infrastructure Dogfooding' (AI writing boilerplate) and true 'Architectural Self-Correction,' asserting human researchers remain responsible for core innovations. Finally, while agreeing Shumer is
correct that fewer roles will exist for those who only write code, the article cites Benjamin Green to suggest a new profession will emerge focused on software architecture rather than coding,
potentially mirroring the low ratio of architects to architecture school graduates.\n\nPublished date: March 07 2026, 10:43\n\nURL: https://medium.com/@polyglot_factotum/matt-shumer-is-mostly-
wrong-3f0626ce9afd\nSource: Medium.com\nClassification: Technology\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [16]\nTitle: AI Coding
Benchmarks are Wrong\n\nSummary: \nThe article critiques the validity of recent AI coding benchmarks, specifically citing a claim that 'Claude Opus 4.5, released in November, can now solve complex
software engineering problems that take human experts nearly five hours with 50 percent reliability' (Source: How 2026 Could Decide the Future of Artificial Intelligence). While the source article
suggests this signals a 'phase transition' with Anthropic CEO Dario Amodei stating in September that the 'vast majority' of code for new Claude models is written by Claude itself, and a creator of
Claude Code claiming in December that '100 percent of his updates to Claude that month were written by Claude,' the author argues this data is misleading. The author, an experienced software engineer,
notes that while AI writes '100 percent' of their side project code, it requires reviewing every task due to 'outright bugs and conceptual mistakes.' The author contends that AI currently only excels
at 'grunt-like work' like translating libraries, failing at 'designing the conceptual structure of software.' An AI analysis within the text explains this discrepancy by distinguishing between
'Capability vs. Reliability.' It highlights that the '50% Horizon (~5 hours)' implies a 'coin-flip's chance' of success, while the '80% Horizon (~30 mins)' indicates a 'more than 20% chance the AI
will fail' on tasks longer than 30 minutes. The analysis attributes the benchmark success to 'METR tasks' involving 'Cybersecurity CTFs' or 'Data Science' with clear 'win conditions,' whereas real-
world coding requires 'Architectural Foresight' which current 'greedy' models lack. The text concludes that the current state of AI is akin to 'pair programming with a very fast, very brilliant, but
very drunk junior developer' rather than a 'coding singularity,' as the bottleneck remains ensuring code works as intended through 'conceptual thinking.'\n\nPublished date: March 01 2026,
12:35\n\nURL: https://medium.com/@polyglot_factotum/ai-coding-benchmarks-are-wrong-274596257413\nSource: Medium.com\nClassification: Technology\nSentiment: neutral\nReporting voice:
Subjective\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [17]\nTitle: METR's 14h 50% Horizon Impacts The Economy More Than ASI Timelines -- LessWrong\n\nSummary: \nMETR's latest update
on AI progress reports a 50% time horizon of approximately 14.5 hours (95% CI: 6 to 98 hours) for Claude Opus 4.6 on software tasks, the highest estimate to date, though the measurement is highly
uncertain due to a saturated task suite. Forecaster Peter Wildeford predicts 2-3.5 workweek time horizons by year-end, which could have 'significant implications for the economy.' Ajeya Cotra, a METR
researcher, now believes her prior predictions were too conservative, suggesting a 3-4 month doubling time with superexponential progress is more likely. Despite this, the author cautions against
alarm, noting that the 50% horizon may not fully capture economic transformation. The real focus, according to the author, is on achieving an 'Automated Coder'—a system capable of fully autonomous
coding—which depends on the 'coding time horizon required to achieve Automated Coder.' The model at aifuturesmodel.com estimates this at 3.3 work years, but varies widely: from one month (yielding
automation by August 2028) to 125 years (near-human lifespan). The author argues that full coding automation is critical because partial automation may still bottleneck progress due to human
limitations in research taste and compute allocation.\n\nPublished date: February 20 2026, 21:08\n\nURL: https://www.lesswrong.com/posts/gBwrmcY2uArZSoCtp/metr-s-14h-50-horizon-impacts-the-economy-
more-than-asi\nSource: Maya Farber Brodsky\nClassification: Technology\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [18]\nTitle: The
Hidden Skill of 2026: Knowing When to Ignore AI\n\nSummary: \nA study conducted by METR in July 2025 tracked experienced open-source developers using AI coding assistants over thousands of hours.
Despite the developers believing they were working 20% faster, the research found they were actually 19% slower. The study revealed a significant disconnect between perceived and actual productivity,
indicating that AI tools may be undermining performance despite users' belief in their efficiency. The article highlights the hidden skill of knowing when to ignore AI, suggesting that overreliance on
AI can reduce real output even when users feel more productive. Published on February 18, 2026, by Level Up Coding.\n\nPublished date: February 18 2026, 18:21\n\nURL:
https://levelup.gitconnected.com/the-hidden-skill-of-2026-knowing-when-to-ignore-ai-a3bcd5be6300\nSource: Level Up Coding\nClassification: Technology\nSentiment: neutral\nReporting voice:
Analytical\nContinent: North America\n\n</doc>\n\n<doc>\nCitation key: [19]\nTitle: Becoming reliable executors of complex tasks - The Times of India\n\nSummary: \nAccording to an article published in
The Times of India on February 18, 2026, AI systems are expected to evolve from being 'copilots' that require human oversight to becoming reliable executors of complex tasks. Currently, AI is
impressive in demonstrations and answering questions but remains 'brittle' outside of coding, lacking reliability, correctness, and integration in real-world workflows. The author envisions AI models
improving in general computer use, problem-solving in novel and unstructured domains, and on-the-job learning. The author outlines three key expectations: AI should act less as a creative writer and
more as a 'verifiable truth engine,' especially in high-stakes fields like public policy, health, and finance where hallucinations are intolerable; AI should provide proven reliability on structured
data, with capabilities to prove correctness, cite data lineage, and reason under constraints; and AI should achieve better long-horizon autonomy by proactively setting goals, breaking them into
tasks, executing them, and tracking progress over weeks. The ultimate goal is for AI to move beyond responding to prompts and instead act as a dependable, insight-driven executor.\n\nPublished date:
February 18 2026, 06:04\n\nURL: https://timesofindia.indiatimes.com/technology/times-techies/becoming-reliable-executors-of-complex-tasks/articleshow/128493396.cms\nSource: The Times of
India\nClassification: Technology\nSentiment: positive\nReporting voice: Analytical\nContinent: Asia\n\n</doc>\n\n<doc>\nCitation key: [20]\nTitle: Estimating METR Time Horizons for Claude Opus 4.6
and GPT 5.3 Codex (xhigh) -- LessWrong\n\nSummary: \nMaya Farber Brodsky estimates the METR time horizons for Claude Opus 4.6 and GPT 5.3 Codex using a weighted regression model based on the Epoch
Capabilities Index (ECI), which incorporates 10 agentic and reasoning benchmarks including SWE-Bench Pro, ARC-AGI-2, GDPval-AA, and Terminal-Bench 2.0. The model predicts a 50% pass rate time horizon
of 7.9 hours for Opus 4.6 and 8.7 hours for GPT 5.3 Codex, aligning with crowd-sourced predictions that favor OpenAI. However, the author expresses skepticism about the Opus 4.6 estimate due to its
exceptionally high performance on ARC-AGI-2, a benchmark likely cherry-picked by Anthropic. The author notes that OpenAI may have similarly cherry-picked benchmarks, especially given the model's
release timing in response to Opus 4.6. Based on these concerns, the author expects both models to perform slightly lower and closer together, estimating 8.25 hours for GPT 5.3 Codex and 8.7 hours for
Opus 4.6. The METR benchmark measures the interpolated task length at which a model has a 50% or 80% chance of solving a task in one shot, with results sensitive to the task suite used. The analysis
includes 8 post-o3 2025 models, and the model fits well for GPT 5.2 and Opus 4.5, though Anthropic models slightly underperformed and OpenAI models outperformed their predictions.\n\nPublished date:
February 16 2026, 18:29\n\nURL: https://www.lesswrong.com/posts/WacuyurbABwNv8ziq/estimating-metr-time-horizons-for-claude-opus-4-6-and-gpt-5\nSource: Maya Farber Brodsky\nClassification:
Technology\nSentiment: neutral\nReporting voice: Analytical\nContinent: North America\n\n</doc>\n\n------News Summaries End------\n","offset":10,"hit_cache":false}
```

```json
{
  "query": "AI model time horizon METR 2026",
  "limit": 5
}
```

### 📋 Result

```
{"markets": [], "query": "AI model time horizon METR 2026"}
```

## 💬 Response

This is very informative. Let me now check for the latest METR evaluations and search for recent developments that could move the CP.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "query": "METR AI time horizon 80% reliability latest update March 2026"
}
```

### 📋 Result

```
{"query": "METR AI time horizon 80% reliability latest update March 2026", "results": [{"title": "Task-Completion Time Horizons of Frontier AI Models - METR", "url": "https://metr.org/time-horizons/",
"snippet": "The task-completion time horizon is the task duration (measured by human expert completion time) at which an AI agent is predicted to succeed with a given level of reliability. For
example, the 50%-time horizon is the duration at which an agent is predicted to succeed half the time. The graph below shows the 50%- and 80%-time horizons for frontier AI agents, calculated using
their performance on over a hundred diverse software tasks.\nWe periodically [update this page](#updates) with new measurem", "api_data": null, "hint": null}, {"title": "Measuring AI Ability to
Complete Long Tasks - METR", "url": "https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/", "snippet": "This is our most up-to-date measurement of the task-completion time
horizons for public language models. For methodology details and FAQs, see our [dedicated time horizons page](/time-horizons/).\nSummary\nWe propose measuring AI performance in terms of the length of
tasks AI agents can complete. We show that this metric has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months. Extrapolating this trend predicts
that, in under a decade, we will s", "api_data": null, "hint": null}, {"title": "METR - Wikipedia", "url": "https://en.wikipedia.org/wiki/METR", "snippet": "Model Evaluation and Threat Research (METR)
(MEE-t\u0259r), is a nonprofit research institute, based in Berkeley, California, that evaluates frontier AI models' capabilities to carry out long-horizon, agentic tasks that some researchers argue
could pose catastrophic risks to society. They have worked with leading AI companies to conduct pre-deployment model evaluations and contribute to system cards, including OpenAI's o3, o4-mini, GPT-4o
and GPT-4.5, and Anthropic's Claude models.\nMETR's CEO and fou", "api_data": {"content": [{"type": "text", "text": "{\"title\": \"METR\", \"url\": \"https://en.wikipedia.org/wiki/METR\", \"extract\":
\"Model Evaluation and Threat Research (METR) (MEE-t\\u0259r), is a nonprofit research institute, based in Berkeley, California, that evaluates frontier AI models' capabilities to carry out long-
horizon, agentic tasks that some researchers argue could pose catastrophic risks to society. They have worked with leading AI companies to conduct pre-deployment model evaluations and contribute to
system cards, including OpenAI's o3, o4-mini, GPT-4o and GPT-4.5, and Anthropic's Claude models.\\nMETR's CEO and founder is Beth Barnes, a former alignment researcher at OpenAI who left in 2022 to
form ARC Evals, the evaluation division of Paul Christiano's Alignment Research Center. In December 2023, ARC Evals was then spun off into an independent 501(c)(3) nonprofit and renamed METR.\",
\"mode\": \"full\"}"}]}, "hint": null}, {"title": "METR", "url": "https://metr.org/", "snippet": "Featured research\nOur AI evaluations research focuses on assessing broad autonomous capabilities and
the ability of AI systems to accelerate AI R&D. We also study potential AI behavior that threatens the integrity of evaluations and mitigations for such behavior.\n[View all
research](/research)\n![GPT-5.1 Evaluation Results](/assets/images/gpt-5-1-research.jpg)\nGPT-5.1 Evaluation Results\nWe evaluate whether GPT-5.1 poses significant catastrophic risks via AI self-
improvement, rogue replication, or", "api_data": null, "hint": null}, {"title": "Time Horizon 1.1 - METR", "url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/", "snippet": "We\u2019re releasing
a new version of our time horizon estimates (TH1.1), using more tasks and a new eval infrastructure.\nOur estimates of time horizons for many models have been updated. The new estimates generally fall
within our existing confidence intervals, though the trend in time horizon growth looks a little different, discussed below. We expect to make more changes to our evaluation protocols so that we can
capture the continued rapid growth in capabilities.\nEarly in 2025 we published our [t", "api_data": null, "hint": null}, {"title": "Timelines Forecast \u2014 AI 2027", "url":
"https://ai-2027.com/research/timelines-forecast", "snippet": "Timelines Forecast\nForecasting time to automated superhuman coders\nEli Lifland, Nikola Jurkovic, FutureSearch | April
2025\n![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcombined-headline.4c72f6dd.png&w=3840&q=75)\nSummary\n2025 Dec 31 update: We've published a revamped timelines and takeoff model at
[aifuturesmodel.com](https://www.aifuturesmodel.com/).\n2025 May 7 update: Eli has, based on feedback, made a few updates to the model that he\u2019s described in [the appendix](#2025-may-7-update).
The u", "api_data": null, "hint": null}, {"title": "This is the most misunderstood graph in AI | MIT Technology Review", "url": "https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-
misunderstood-graph-in-ai/", "snippet": "This is the most misunderstood graph in AI\nTo some, METR\u2019s \u201ctime horizon plot\u201d indicates that AI utopia\u2014or apocalypse\u2014is close at
hand. The truth is more complicated.\n![\"\"](https://wp.technologyreview.com/wp-content/uploads/2026/02/ai-chart3.jpg)\nMIT Technology Review Explains: Let our writers untangle the complex, messy
world of technology to help you understand what\u2019s coming next. [You can read more from the series here](https://www.technologyreview.com/tag/tech-review-explains).\nEvery time Op", "api_data":
null, "hint": null}, {"title": "Details about METR\u2019s evaluation of OpenAI GPT-5", "url": "https://evaluations.metr.org/gpt-5-report/", "snippet": "Details about METR\u2019s evaluation of OpenAI
GPT-5\nNote on independence: This evaluation was conducted under a standard NDA. Due to the sensitive information shared with METR as part of this evaluation, OpenAI\u2019s comms and legal team
required review and approval of this post (the latter is not true of any other METR reports shared on our website).[1](https://evaluations.metr.org#fn:1)\nThroughout this report, \u201cGPT-5\u201d
refers to \u201cgpt-5-thinking\u201d.\nExecutive Summary\nAs described in OpenAI\u2019s GPT-5 System ", "api_data": null, "hint": null}, {"title": "METR Time Horizons | Epoch AI", "url":
"https://epoch.ai/benchmarks/metr-time-horizons", "snippet": "The tasks considered include\nThe models\u2019 final duration is assigned based on the longest task that the model can complete. The
duration of the task for that purpose is judged by the time it takes a human to complete that task.\nWe source time horizons directly from METR\u2019s own analysis.\nThe methodology to estimate a
model\u2019s time horizon is as follows:\nCollect performance data: For each of HCAST, RE-Bench, and SWAA, for each task, evaluate the model\u2019s performance. Each model was run around 8 times ",
"api_data": null, "hint": null}, {"title": "Interpreting the METR Time Horizons Post", "url": "https://www.lesswrong.com/posts/fRiqwFPiaasKxtJuZ/interpreting-the-metr-time-horizons-post", "snippet":
"[EDIT: initial publication did not have the link to the original post, and was missing the footnotes. Sorry about that! Fixed now.]\n[This has been lightly edited from the original post, eliminating
some introductory material that LW readers won't need. Thanks to [Stefan Schubert](https://stefanschubert.substack.com/) for suggesting I repost here. TL;DR for readers already familiar with the METR
[Measuring AI Ability to Complete Long Tasks](https://arxiv.org/abs/2503.14499) paper: this post highl", "api_data": null, "hint": null}]}
```

```json
{
  "query": "METR evaluations 2026 Claude Opus GPT time horizon hours"
}
```

### 📋 Result

```
{"query": "METR evaluations 2026 Claude Opus GPT time horizon hours", "results": [{"title": "Task-Completion Time Horizons of Frontier AI Models - METR", "url": "https://metr.org/time-horizons/",
"snippet": "The task-completion time horizon is the task duration (measured by human expert completion time) at which an AI agent is predicted to succeed with a given level of reliability. For
example, the 50%-time horizon is the duration at which an agent is predicted to succeed half the time. The graph below shows the 50%- and 80%-time horizons for frontier AI agents, calculated using
their performance on over a hundred diverse software tasks.\nWe periodically [update this page](#updates) with new measurem", "api_data": null, "hint": null}, {"title": "Measuring Time Horizon using
Claude Code and Codex - METR", "url": "https://metr.org/notes/2026-02-13-measuring-time-horizon-using-claude-code-and-codex/", "snippet": "Most of METR\u2019s time horizon measurements are done using
two scaffolds: [Triframe](https://github.com/METR/triframe_inspect) and [ReAct](https://github.com/METR/inspect-agents/blob/main/packages/agents/src/metr_agents/agents.py)[1](#fn:1).\nPeople sometimes
see that we use these two scaffolds and feel skeptical about the validity of our results. Shouldn\u2019t scaffolds like Claude Code and Codex do much better on time horizon given how much work has
gone into making those scaffolds better for software", "api_data": null, "hint": null}, {"title": "Estimating METR Time Horizons for Claude Opus 4.6 and GPT 5.3 Codex (xhigh) \u2014 EA Forum", "url":
"https://forum.effectivealtruism.org/posts/vxEWdn7ni4QEwEdE8/estimating-metr-time-horizons-for-claude-opus-4-6-and-gpt-5-1", "snippet": "Note: Appendix re-analysing with the addition of Gemini 3.1
data added 20/02/26 - this substantially changed the results\nOne of the most attended to benchmarks for any new model these days is the METR estimated time horizon for \u201ca diverse set of multi-
step software and reasoning tasks\u201d[[1]]. This comes in two variants - 50% pass rate and 80% pass rate.\nOstensibly, these represent the time it would take for a competent human expert to complete
a task which the model have a 50% or 80% chance of on", "api_data": null, "hint": null}, {"title": "METR", "url": "https://metr.org/", "snippet": "Featured research\nOur AI evaluations research
focuses on assessing broad autonomous capabilities and the ability of AI systems to accelerate AI R&D. We also study potential AI behavior that threatens the integrity of evaluations and mitigations
for such behavior.\n[View all research](/research)\n![GPT-5.1 Evaluation Results](/assets/images/gpt-5-1-research.jpg)\nGPT-5.1 Evaluation Results\nWe evaluate whether GPT-5.1 poses significant
catastrophic risks via AI self-improvement, rogue replication, or", "api_data": null, "hint": null}, {"title": "Time Horizon 1.1 - METR", "url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/",
"snippet": "We\u2019re releasing a new version of our time horizon estimates (TH1.1), using more tasks and a new eval infrastructure.\nOur estimates of time horizons for many models have been updated.
The new estimates generally fall within our existing confidence intervals, though the trend in time horizon growth looks a little different, discussed below. We expect to make more changes to our
evaluation protocols so that we can capture the continued rapid growth in capabilities.\nEarly in 2025 we published our [t", "api_data": null, "hint": null}, {"title": "Claude Opus 4.5 Achieves
50%-Time Horizon Of Around 4 ...", "url": "https://www.lesswrong.com/posts/q5ejXr4CRuPxkgzJD/claude-opus-4-5-achieves-50-time-horizon-of-around-4-hrs-49", "snippet": "We estimate that, on our tasks,
Claude Opus 4.5 has a 50%-time horizon of around 4 hrs 49 mins (95% confidence interval of 1 hr 49 mins to 20 hrs 25 mins). While we're still working through evaluations for other recent models, this
is our highest published time horizon to date.\nWe don\u2019t think the high upper CI bound reflects Opus\u2019s actual capabilities: our current task suite doesn\u2019t have enough long tasks to
confidently upper bound Opus 4.5\u2019s 50%-time horizon. We are working on updating our task", "api_data": null, "hint": null}, {"title": "Estimating METR Time Horizons for Claude Opus 4.6 and ...",
"url": "https://www.lesswrong.com/posts/WacuyurbABwNv8ziq/estimating-metr-time-horizons-for-claude-opus-4-6-and-gpt-5", "snippet": "Note: Appendix re-analysing with the addition of Gemini 3.1 data
added 20/02/26 - this substantially changed the results\nOne of the most attended to benchmarks for any new model these days is the METR estimated time horizon for \u201ca diverse set of multi-step
software and reasoning tasks\u201d[[1]](#fnbny286fxqrv). This comes in two variants - 50% pass rate and 80% pass rate.\nOstensibly, these represent the time it would take for a competent human expert
to complete a task which the model have a 50% or ", "api_data": null, "hint": null}, {"title": "This is the most misunderstood graph in AI | MIT Technology Review", "url":
"https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/", "snippet": "This is the most misunderstood graph in AI\nTo some, METR\u2019s \u201ctime horizon
plot\u201d indicates that AI utopia\u2014or apocalypse\u2014is close at hand. The truth is more complicated.\n![\"\"](https://wp.technologyreview.com/wp-content/uploads/2026/02/ai-chart3.jpg)\nMIT
Technology Review Explains: Let our writers untangle the complex, messy world of technology to help you understand what\u2019s coming next. [You can read more from the series
here](https://www.technologyreview.com/tag/tech-review-explains).\nEvery time Op", "api_data": null, "hint": null}, {"title": "Exponential Progress: Claude Opus 4.6 Has 50% Time Horizon Of 14.5 Hours
On METR Time Horizons Benchmark", "url": "https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark/", "snippet": "Elon Musk has
[said ](https://officechai.com/ai/we-have-entered-the-singularity-says-elon-musk/)we have entered the singularity, and Sam Altman has [said](https://officechai.com/ai/theres-going-to-be-a-faster-ai-
takeoff-than-i-originally-thought-openai-ceo-sam-altman/) that AI is progressing faster than he expected, and some of these observations are showing up in benchmark data.\nNew measurements from METR
\u2014 a nonprofit focused on evaluating AI capabilities \u2014 show that Claude Opus 4.6, Anthropic", "api_data": null, "hint": null}, {"title": "AI Model Benchmarks Mar 2026 | Compare GPT-5, Claude
4.5, Gemini 2.5, Grok 4 | LM Council", "url": "https://lmcouncil.ai/benchmarks", "snippet": "18 benchmarks - the world's most-followed benchmarks, curated by [AI
Explained](https://www.youtube.com/@aiexplained-official), author of [SimpleBench](https://simple-bench.com)\nIndependently-run benchmarks by Epoch, Scale and others, so may not match self-reported
scores by AI orgs.\n| Models (no tools) | Score | |\n|---|---|---|\n| 1 | Gemini 3 Pro Preview | 37.52% \u00b11.90 |\n| 2 | Claude Opus 4.6 (max) | 34.44% \u00b11.86 |\n| 3 | GPT-5 Pro | 31.64%
\u00b11.82 |\n| 4 | GPT-5.2 | 27.80% \u00b11.76 |\n| 5 | GPT-5 (Aug", "api_data": null, "hint": null}]}
```

```json
{
  "query": "AI model 3 hour time horizon METR 80% reliability 2026",
  "limit": 5
}
```

### 📋 Result

```
{"markets": [{"market_title": "[ACX 2026] Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?", "probability": 0.7883013185997726, "volume": 14535.465379622185, "url":
"https://manifold.markets/DaftPunkRock/acx-2026-will-an-ai-model-reach-a-3", "source": "manifold", "description": null, "market_id": "UdsLNSc2OE", "recent_history": null}], "query": "AI model 3 hour
time horizon METR 80% reliability 2026"}
```

## 💬 Response

Good data. Let me now fetch the METR time horizons page to get the latest actual data, and check the key news article about Claude Opus 4.6's time horizons.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://metr.org/time-horizons/",
  "prompt": "What are the latest 80% reliability time horizons for the most recent AI models? What is the current best 80% time horizon? Has any model reached 3 hours at 80% reliability?"
}
```

### 📋 Result

```
{"url": "https://metr.org/time-horizons/", "content": "Based on the content provided, I cannot give you the specific 80% time horizon values for the most recent AI models. \n\nThe webpage describes
the **methodology** for calculating time horizons and mentions that it is \"periodically updated\" with measurements for frontier AI models. It lists update dates through March 3rd, 2026, mentioning
models like:\n- Claude Opus 4.6 and GPT-5.3-Codex (Feb 20, 2026)\n- GPT-5.2 (Feb 4, 2026)\n- Gemini 3 Pro and GPT-5.1 Codex Max (Feb 3, 2026)\n- Claude Opus 4.5 (Dec 19, 2025)\n\nHowever, the actual
**numerical values** for the 80% time horizons are not included in the text content you provided. The page appears to have a graph showing these metrics, but graph data was not included in the text
extraction.\n\nThe content does not explicitly state whether any model has reached 3 hours at 80% reliability.\n\n**Relevant links:**\n- [Full paper on methodology and
results](https://arxiv.org/abs/2503.14499)\n- [Accompanying blog post](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)\n- [Follow-up work on time horizon variation
across domains](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)\n- [Research on holistic vs algorithmic scoring](https://metr.org/blog/2025-08-12-research-update-towards-
reconciling-slowdown-with-time-horizons/)", "title": "Task-Completion Time Horizons of Frontier AI Models"}
```

```json
{
  "url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/",
  "prompt": "What are the updated 80% reliability time horizons? What is the best 80% time horizon? Has any model reached 3 hours at 80%? What are the latest estimates?"
}
```

### 📋 Result

```
{"url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/", "content": "The content does **not** provide 80% reliability time horizons. All the time horizon estimates mentioned are for the **50%
(median) time horizon**, not 80%.\n\nThe data shown includes:\n- Point estimates (P50/median)\n- Confidence intervals (shown in brackets)\n\nFor example, the highest performing model is **Claude Opus
4.5** with a TH1.1 estimate of **320 minutes [170, 729]** at the 50% level, which is about 5.3 hours median time horizon.\n\n**No information about 80% time horizons or whether any model has reached 3
hours at 80% reliability** is contained in this content.\n\nThe latest TH1.1 estimates (50% time horizons) are:\n- Claude Opus 4.5: 320 mins (~5.3 hours)\n- GPT-5.1-codex-max: 173 mins (~2.9 hours)\n-
GPT-5: 214 mins (~3.6 hours)\n- Claude Sonnet 4.5: 122 mins (~2 hours)\n- o3: 121 mins (~2 hours)\n\nRelevant links:\n- [Time horizon methodology](https://metr.org/blog/2025-03-19-measuring-ai-
ability-to-complete-long-tasks/)\n- [Live dashboard](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)\n- [HCAST paper (Rein 2025)](https://metr.org/hcast.pdf)\n- [Public
data repository](https://github.com/METR/eval-analysis-public)\n- [Task bounty desiderata](https://taskdev.metr.org/desiderata/)\n- [Cross-domain time-horizon blog
post](https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-domains/)\n- [Time horizon paper (Kwa et al.)](https://arxiv.org/abs/2503.14499)", "title": "Time Horizon 1.1"}
```

## 💭 Thinking

Let me gather more data. I need to understand the current state of the 80% time horizon specifically, and what the latest models have achieved. The news articles mention that Claude Opus 4.6 has a 50% time horizon of ~14.5 hours, but I need to know about the 80% time horizon specifically.

Let me search for more specific information about the 80% time horizon.

## 💬 Response

Let me get more specific data on the 80% time horizon, which is what the question is actually about.

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "url": "https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark/",
  "prompt": "What is the 80% time horizon for Claude Opus 4.6 and other recent models? Has any model reached 3 hours at 80% reliability? What are the latest 80% time horizon numbers?"
}
```

### 📋 Result

```
{"url": "https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark/", "content": "The content does **not** provide 80% time
horizon data for Claude Opus 4.6 or any other models. \n\nThe article exclusively discusses **50% time horizons** (the task length at which a model succeeds roughly half the time). For Claude Opus
4.6, this is approximately 14.5 hours at the 50% success rate.\n\nNo information about 80% time horizons, 3-hour reliability thresholds, or any metrics beyond the 50% benchmark is included in this
text.\n\nRelevant links:\n- [METR's measurements and benchmark details](https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-
benchmark/) (the article itself)\n- [Elon Musk on the singularity](https://officechai.com/ai/we-have-entered-the-singularity-says-elon-musk/)\n- [Sam Altman on AI
progress](https://officechai.com/ai/theres-going-to-be-a-faster-ai-takeoff-than-i-originally-thought-openai-ceo-sam-altman/)", "title": "Exponential Progress: Claude Opus 4.6 Has 50% Time Horizon Of
14.5 Hours On METR Time Horizons Benchmark"}
```

```json
{
  "query": "METR 80% time horizon hours 2026 Claude Opus GPT latest estimate"
}
```

### 📋 Result

```
{"query": "METR 80% time horizon hours 2026 Claude Opus GPT latest estimate", "results": [{"title": "Task-Completion Time Horizons of Frontier AI Models - METR", "url": "https://metr.org/time-
horizons/", "snippet": "The task-completion time horizon is the task duration (measured by human expert completion time) at which an AI agent is predicted to succeed with a given level of reliability.
For example, the 50%-time horizon is the duration at which an agent is predicted to succeed half the time. The graph below shows the 50%- and 80%-time horizons for frontier AI agents, calculated using
their performance on over a hundred diverse software tasks.\nWe periodically [update this page](#updates) with new measurem", "api_data": null, "hint": null}, {"title": "METR Time Horizons | Epoch
AI", "url": "https://epoch.ai/benchmarks/metr-time-horizons", "snippet": "The tasks considered include\nThe models\u2019 final duration is assigned based on the longest task that the model can
complete. The duration of the task for that purpose is judged by the time it takes a human to complete that task.\nWe source time horizons directly from METR\u2019s own analysis.\nThe methodology to
estimate a model\u2019s time horizon is as follows:\nCollect performance data: For each of HCAST, RE-Bench, and SWAA, for each task, evaluate the model\u2019s performance. Each model was run around 8
times ", "api_data": null, "hint": null}, {"title": "Time Horizon 1.1 - METR", "url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/", "snippet": "We\u2019re releasing a new version of our time
horizon estimates (TH1.1), using more tasks and a new eval infrastructure.\nOur estimates of time horizons for many models have been updated. The new estimates generally fall within our existing
confidence intervals, though the trend in time horizon growth looks a little different, discussed below. We expect to make more changes to our evaluation protocols so that we can capture the continued
rapid growth in capabilities.\nEarly in 2025 we published our [t", "api_data": null, "hint": null}, {"title": "This is the most misunderstood graph in AI | MIT Technology Review", "url":
"https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/", "snippet": "This is the most misunderstood graph in AI\nTo some, METR\u2019s \u201ctime horizon
plot\u201d indicates that AI utopia\u2014or apocalypse\u2014is close at hand. The truth is more complicated.\n![\"\"](https://wp.technologyreview.com/wp-content/uploads/2026/02/ai-chart3.jpg)\nMIT
Technology Review Explains: Let our writers untangle the complex, messy world of technology to help you understand what\u2019s coming next. [You can read more from the series
here](https://www.technologyreview.com/tag/tech-review-explains).\nEvery time Op", "api_data": null, "hint": null}, {"title": "Details about METR\u2019s evaluation of OpenAI GPT-5.1-Codex-Max", "url":
"https://evaluations.metr.org/gpt-5-1-codex-max-report/", "snippet": "Details about METR\u2019s evaluation of OpenAI GPT-5.1-Codex-Max\nNote on independence: This evaluation was conducted under a
standard NDA. Due to the sensitive information shared with METR as part of this evaluation, OpenAI\u2019s comms and legal team required review and approval of this
post.[1](https://evaluations.metr.org#fn:1)\nSummary\nMETR [previously found](https://evaluations.metr.org/gpt-5-report/) that further incremental development[2](https://evaluations.metr.org#fn:2) of
models similar to GPT-5", "api_data": null, "hint": null}, {"title": "How Does Time Horizon Vary Across Domains? - METR", "url": "https://metr.org/blog/2025-07-14-how-does-time-horizon-vary-across-
domains/", "snippet": "![Chart of AI time horizons increasing in many domains](/assets/images/time-horizon-domains/time-horizons-increasing.png)\n[smoothed
spline](https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.make_splrep.html#scipy.interpolate.make_splrep)with s=0.2, k=1. Lines have a range on the y-axis equal to the range of
task lengths actually in the benchmark (2nd% to 98th% quantiles).\nSummary\nIn the paper [Measuring AI Ability to Complete Long Software Tasks](https://metr.org/blog/2025-0", "api_data": null, "hint":
null}, {"title": "Details about METR\u2019s evaluation of OpenAI GPT-5", "url": "https://evaluations.metr.org/gpt-5-report/", "snippet": "Details about METR\u2019s evaluation of OpenAI GPT-5\nNote on
independence: This evaluation was conducted under a standard NDA. Due to the sensitive information shared with METR as part of this evaluation, OpenAI\u2019s comms and legal team required review and
approval of this post (the latter is not true of any other METR reports shared on our website).[1](https://evaluations.metr.org#fn:1)\nThroughout this report, \u201cGPT-5\u201d refers to
\u201cgpt-5-thinking\u201d.\nExecutive Summary\nAs described in OpenAI\u2019s GPT-5 System ", "api_data": null, "hint": null}, {"title": "Interpreting the METR Time Horizons Post", "url":
"https://www.lesswrong.com/posts/fRiqwFPiaasKxtJuZ/interpreting-the-metr-time-horizons-post", "snippet": "[EDIT: initial publication did not have the link to the original post, and was missing the
footnotes. Sorry about that! Fixed now.]\n[This has been lightly edited from the original post, eliminating some introductory material that LW readers won't need. Thanks to [Stefan
Schubert](https://stefanschubert.substack.com/) for suggesting I repost here. TL;DR for readers already familiar with the METR [Measuring AI Ability to Complete Long
Tasks](https://arxiv.org/abs/2503.14499) paper: this post highl", "api_data": null, "hint": null}, {"title": "Timelines Forecast \u2014 AI 2027", "url": "https://ai-2027.com/research/timelines-
forecast", "snippet": "Timelines Forecast\nForecasting time to automated superhuman coders\nEli Lifland, Nikola Jurkovic, FutureSearch | April
2025\n![](/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fcombined-headline.4c72f6dd.png&w=3840&q=75)\nSummary\n2025 Dec 31 update: We've published a revamped timelines and takeoff model at
[aifuturesmodel.com](https://www.aifuturesmodel.com/).\n2025 May 7 update: Eli has, based on feedback, made a few updates to the model that he\u2019s described in [the appendix](#2025-may-7-update).
The u", "api_data": null, "hint": null}, {"title": "METR's 14h 50% Horizon Impacts The Economy More ...", "url": "https://www.lesswrong.com/posts/gBwrmcY2uArZSoCtp/metr-s-14h-50-horizon-impacts-the-
economy-more-than-asi", "snippet": "Another day, another METR graph update.\nMETR [said](https://x.com/METR_Evals/status/2024923422867030027?s=20) on X:\nWe estimate that Claude Opus 4.6 has a
50%-time-horizon of around 14.5 hours (95% CI of 6 hrs to 98 hrs) on software tasks. While this is the highest point estimate we\u2019ve reported, this measurement is extremely noisy because our
current task suite is nearly saturated.\n[Some](https://x.com/nikolaj2030/status/2024925581146722806?s=20) [people](https://x.com/GarrisonLovely/status/2024", "api_data": null, "hint": null}]}
```

```json
{
  "query": "METR 80% reliability time horizon 3 hours AI model 2026",
  "num_results": 10
}
```

### 📋 Result

```
[{"title": "AI 3 hour time horizon METR 80%? - Metaculus", "url": "https://www.metaculus.com/questions/41140/", "snippet": "AI 3 hour time horizon METR 80%?\n**The Bridgewater x Metaculus Forecasting
Contest**returns for year three. $30,000 in prizes across Open and Undergraduate competitions, plus recruiting opportunities for top forecasters. Past contests have led to internship offers and full-
time hires at Bridgewater.\n**Register here**and compete for prizes starting January 12.\n# \n* Questions\n* Tournaments\n* Services\n* News\n* Questions\n* Tournaments\n* Questions\n* Questions\n*
More\n* Log inSign Up\n* a/\u6587\n* Log inSign", "highlights": ["water.  ...    * Tournaments\n* Services\n* News\n* Questions\n* Tournaments * Questions\n* Questions\n* More\n* Log inSign Up\n*
a/\u6587\n* Log inSign Up\n**6**comments **562**forecasters\n# Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?\nCurrent estimate Revealednext week\nShare\nPredict\nTop
Key Factors\nView all (1)\nModels improve exponentially over time\nImpact Increases Likelihood\nStrength\n8 votes\nCommentsTimelineIn the NewsKey FactorsQuestion Info\nTimeline\nRevealednext week
1d1w2mall\n0%25%50%75%100%\nResolution Criteria This question will resolve as**Yes**if, during 2026,METR estimatesthat an AI model has a time horizon of \u22653 hours at 80% reliability, i.e. the AI
has an estimated \u226580% reliability on tasks requiring human experts \u22653 hours to solve. ### Fine Print * If METR substantially changes their dataset such that new estimates are not comparable
to old estimates, this question will use the closest available equivalent to the dataset used during December 2025. * If METR ceases estimating a model's time horizon at \u226580% reliability, this
question will be**annulled**. * Current estimated time horizons are presented as \"Task duration\" or \"Task length\" when mouseovering models in the  ...    Show Less\nKey
Factors\nDriver\nby\n@lubossaloky\nModels improve exponentially over time\nImpact\nIncreases Likelihood  ...    METRis an AI model evaluation and threat research organisation that studies AI
capabilities and their ability to conduct AI research and self-improve. METR regularly tests released models for their threat capacity, which includes measuring their ability to complete realistic
software and research tasks reliably. For each task, they measure how long it takes humans with relevant expertise to complete it, then see which tasks different models can solve. By fitting a curve
of model success against human task duration, they define each model's \"time horizons\": the longest task length (in human time) on which the model can succeed with around 50% or 80% probability.
Their results show that these horizons have been growing exponentially over time. As of December 2025 the highest time horizon with an 80% chance of success is 31 minutes byGPT-5.1-Codex-Max, a 5x
improvement from 2024's best  ...    Show Less\n## Comments\nLog in\n6 comments\nrecent\n#### lubossaloky\n\u00b7Dec 28, 2025 lubossaloky'sPrediction\n55%\nDec 28, 2025\nModels improve exponentially.
Simplified graph for 80% success: * End of 2022 - 10 seconds.\n* End of 2023 - 1 minute (x6).\n* End of 2024 - 6 minutes (x6).  ...    Reply(0)Changed my mind (0)Mind (0)(0)\nhide 1 replies\n####
blednotik\n\u00b7Jan 7, 2026 @lubossalokybased on your data:\n2023 - x6 improvement\n2024 - x6 improvement\n2025 - x5.33 improvement 2026 - we need x5.625 improvement to resolve the question as
yes.\nMy prediction: 40%\n2  ...    Today Claude Opus 4.5's time horizon is estimated as 4.5 hours (first graph athttps://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)). Does
it mean that the  ...    @blednotikYou have to look at the \"80% Success\" graph (see the resolution criteria). The highest is currently GPT-5.1-Codex-Max with a time of 32 mins.  ...    It's
important to distinguish between AI services/systems that can run for a long time vs actual agentic execution. Many current systems use retries, replanning, fallbacks, etc. and can go for hours, but
it's not the same as working on  ...    If we're talking about passing METR, it must be true agentic performance with long-horizon coherence. Currently,  ...    benchmarked coherence. I really don't
see how we can have true planning coherence for 3 hours in 2026 - within the next  ...    @durstidoClaude Opus 4.5 is at about 5 hours at 50% success so the capability is there but just not the
reliability. However these two metrics are doubling about every 4 months so I\u2019d say it\u2019s pretty likely we\u2019ll get to 3 hours at 80%. We\u2018re at 30 minutes now and have about 3
doublings to go. Reply(0)Changed my mind (0)Mind (0)(0)\nFollowembed\nAuthors:\nADQ\nOpened:Dec 19, 2025\nCloses:Dec 31, 2026 Scheduled resolution:Jan 1, 2027\nSpot Scoring Time:Jan 18, 2026\nACX 2026
Prediction Contest Artificial Intelligence\n\ud83c\udfc6 2025-2026 Leaderboard\nNews Match\n Leading AI expert delays timeline for its possible destruction of humanity\nGuardian\u2022Jan 6, 2026\n\n
World \u2018may not have time\u2019 to prepare for AI safety risks, says leading researcher\nGuardian\u2022Jan 4, 2026\n  ...    2026? 85%chance\n31\n][\n####"], "published_date": null, "score":
null}, {"title": "Task-Completion Time Horizons of Frontier AI Models - METR", "url": "https://metr.org/time-horizons/", "snippet": "Task-Completion Time Horizons of Frontier AI Models - METR\n\nTask-
Completion Time Horizons of Frontier AI Models\n\nThese are our most up-to-date measurements of the task-completion time horizons for public frontier language models. We intend to update this page
periodically whenever we have new measurements to share.\n\n##### LAST UPDATED\n\n##### SHARE\n\nCopy Link arXiv Citation\n\nThe task-completion time horizon is the task duration (measured by human
expert completion time) at which an AI agent is pr", "highlights": [" task-completion time horizon is the task duration (measured by human expert completion time) at which an AI agent is predicted to
succeed with a given level of reliability. For example, the 50%-time horizon is the duration at which an agent is predicted to succeed half the time. The graph below shows the 50%- and 80%-time
horizons for frontier AI agents, calculated using their performance on over a hundred diverse software tasks. Time Horizon 1.1 (Current)TH 1.1\n\nTime Horizon 1.1 (Current) Follows the same
methodology described in the initial paper, but with a larger task suite. See release announcement. Time Horizon 1.0 (Mar 2025) Original time horizon computations. Calculated for models from 2019
through Nov 2025, following the methods described in the original time horizon paper. Log Scale Linear Scale\n\n50% Success 80% Success Analysis code is available on GitHub. Raw data available here We
periodically update this page with new measurements of the time horizons for public frontier AI models. Due to our  ...    What does running a time horizon evaluation involve? and Why has METR
reported time horizons for some models but not  ...    To estimate the time horizons of frontier AI agents, we first estimate the duration it takes a human expert to complete each of our tasks. For
each agent, we fit a logistic curve to predict the probability it successfully completes tasks as a function of human task duration. To get the 50%-time horizon (or 80%-time horizon), we find the task
duration where the fitted curve intersects with 50% (or 80%) success probability. Example of the logistic curve fit to each of three models' performance on tasks of varying duration. The 50%-time
horizon is the task duration where the fitted curve intersects with 50% success probability.  ...    ### Does \u201ctime horizon\u201d mean the length of time that current AI agents can act
autonomously? No. The 50%-time horizon is the length of task (measured by how long it takes a human expert) that an AI agent can complete with 50% reliability. It\u2019s a measure of the difficulty of
a task, rather than the time an AI spends to  ...    ### How long do AI agents take to complete a 2-hour task?  ...    ### Why not report the time horizon at a higher reliability level (e.g. time
horizon at 99% success rate)? Accurately measuring the 99%-time horizon would require many more tasks. These tasks would also need to be very short, making them harder to design and harder to get
reliable human baselines for. In addition, our results would be much  ...    Since the trends for 50%- and 80%-time horizons are very similar, we expect the (true) time horizon at higher  ...    ###
When you say that a model has a 2-hour time horizon, does that mean it can do 50% of all 2-hour tasks, or that each  ...    The answer is somewhere in between. For example, on tasks that take a human
expert 90 minutes to 3 hours, a GPT-5 agent (with time horizon of around 2 hours and 17 minutes) succeeds 100% of the time for around one-third of the tasks, fails  ...    ### Have you considered
alternative curve fits? Why does METR fit an exponential trend to the time horizon data, as  ...    In our March 2025 paper introducing time horizon, we investigated the quality of linear and
hyperbolic fits for models  ...    - March 6th, 2025: Added DeepSeek-R1.\n- April 4th, 2025: Added Claude 3.7 Sonnet. - April 16th, 2025: Added o3 and o4-mini.\n- June 27th, 2025: Added DeepSeek-V3
and Qwen models.  ...    - December 19th, 2025: Added Claude Opus 4.5.\n- February 3rd, 2026: Added Gemini 3 Pro and GPT-5.1 Codex Max. - February 4th, 2026: Added GPT-5.2.\n- February 6th, 2026: This
page is now live! - February 20th, 2026: Added Claude Opus 4."], "published_date": "2026-03-03T00:00:00.000", "score": null}, {"title": "Is METR Underestimating LLM Time Horizons? - LessWrong", "url":
"https://www.lesswrong.com/posts/kNHxuusznCR3rhqkf/is-metr-underestimating-llm-time-horizons", "snippet": "# Is METR Underestimating LLM Time Horizons?\n\n- Post URL (Markdown, compact): /api/post/is-
metr-underestimating-llm-time-horizons?compact=1\n- Comments URL (Markdown): /api/post/is-metr-underestimating-llm-time-horizons/comments\n- Post URL (Markdown): /api/post/is-metr-underestimating-llm-
time-horizons\n- Post URL (HTML): /posts/kNHxuusznCR3rhqkf/is-metr-underestimating-llm-time-horizons\n- Comments: 6\n- Frontpage\n- Tag: AI\n- Tag: METR (org)\n- Tag: Language Models (LLMs)\n- Tag:
Forecasting & Predic", "highlights": [". - *AI-2027 has argued controversially that the METR trends may actually be more accurately modeled as super-exponential, with finite-time blowup; this post
argues that while this claim does not seem to be very well  ...    - Using METR human-baseline data, I define an alternate LLM time-horizon measure, i.e. the longest time horizon over which an LLM
exceeds human baseline reliability (or equivalently the intersection point of the human and LLM logistic curves), and this measure shows a much faster growth-trend than METR's fixed-threshold trends:
doubling every 1.9 months, versus 6.8 months for the 50% METR-trend over the same time period. \u00a0Also, since this metric is directly  ...    principled way to assess time to human-level horizons,
which suggests roughly 2026-2027, with substantial uncertainty.  ...    The METR time-horizon metric provides estimates for the longest software tasks that a given AI is capable of
completing\u00a0[^wmn0epeokb]. \u00a0This estimate is based on human baseline measurements for how long a set of software tasks took human engineers, with the (geometric) average time based on the
subset of humans who succeeded at each task. \u00a0METR  ...    typically reported LLM time horizons at fixed reliabilities independent of task length (e.g. 50% or 80%). The METR estimates have
featured prominently in efforts to estimate the timeline to human level long-horizon agency, e.g. per the AI-2027 forecasts[^skwoix772i]. \u00a0The following bullets describe potential downsides of
this METR horizon approach  ...    - Potentially unattainable bar for human-level: A related issue is that if we require AI to exceed a fixed 50% horizon  ...    doing is not comparing to fixed target
reliabilities at each horizon length (e.g. METR's 50% and 80% targets), but  ...    below) and instead focus on absolute reliability targets. \u00a0One issue is that current LLMs e.g. gpt-5 already
exceed the METR human baseline time horizons at both the 50% and 80% targets; however, humans do still have fatter tailed  ...    4.5, since this claim is less clear now). \u00a0For instance,
\u00a0gpt-5 has worse reliability than the human baselines once the METR task length gets longer than 4.5 hr, but note its 50% horizon is only 2.3 hr. \u00a0Using these human-reliability baselines, we
can estimate LLM time horizons, as the longest task duration over which the LLM is more reliable than the  ...    The trend in this human-relative time horizon metric is increasing much faster than
the existing METR trends, and assuming an exponential fit, the LLM time horizons at human-reliability are doubling every 1.9 months, versus every 7 months over the same time period for the METR
(50%-reliability) time horizon trend (see Table 1 and Figure 2). \u00a0In other words, every 1.9 months there is a doubling in the longest time horizon that LLMs can handle at METR's human  ...
super-exponential finite-time blowup for projecting the METR fixed-reliability (80%) time horizons; per above, this  ...    ## 1.5 Projections to Reach Human Level (hyperbolic fit) Per above, with an
exponential fit, LLMs would never catch up with humans, but with a hyperbolic fit the current trend suggests human level by around mid 2026, relative to the (weak) METR human baselines (see Table 2).
\u00a0That table also  ...    level into 2027. \u00a0These stronger baselines have flatter slope, with human reliability dropping more slowly with longer  ...    connection to actual human
performance; for instance, based on METR's human-baseline logistic fit, we should expect humans to get about 3% reliability for tasks at 1-month horizon (along the METR difficulty trend line), so it's
not clear why we would require \"human-level\" AI to get 50% (or 80%). \u00a0That said, in so far as the human baselines are weak  ...    | time horizon (50% reliability) | 6.8 months | 11 / 2030 | |
time horizon (human-level reliability) | 1.9 months | 12 / 2026 | Table 1: Estimated doubling rates for the proposed human-reliability LLM time-horizon metric versus the METR 50%-reliability metric.
\u00a0Note that the METR horizons are doubling at a much slower rate, and if we assume status quo  ...    | human reliability (at 16 hr) | LLMs-to-exceed-human-level (date) |\n| --- | --- | | 22%
(measured human baseline) | 2026-09-02 |\n| 50% | 2026-12-28 |\n| 80% | 2027-04-16 | Table 2: *Projections for when LLMs will exceed human reliability over all time horizons, based on hyperbolic fit.
The  ...    with an exponential trend the 50% horizon will"], "published_date": "2026-01-17T00:00:00.000", "score": null}, {"title": "What will be the METR time horizon doubling time in 2026? |
Manifold", "url": "https://manifold.markets/Bayesian/what-will-be-the-metr-time-horizon", "snippet": "What will be the METR time horizon doubling time in 2026? | Manifold\n\nMANIFOLD Sign up\n\nWhat
will be the METR time horizon doubling time in 2026?\n\nBayesian\n\n56\n\n\u1e4010k\u1e4032k\n\n2027\n\nOldest\n\n16%\n\n<3 months\n\nYesNo\n\n8%\n\n3-3.5 months\n\nYesNo\n\n12%\n\n3.5-4
months\n\nYesNo\n\n15%\n\n4-4.5 months\n\nYesNo\n\n13%\n\n4.5-5 months\n\nYesNo\n\n10%\n\n5-5.5 months\n\nYesNo\n\n7%\n\n5.5-6 months\n\nYesNo\n\n4%\n\n6-6.5 months\n\nYesNo\n\n4%\n\n6.5-7
months\n\nYesNo\n\n11%\n\n>7 months\n\nYesNo\n\nThis market matches Software Engineering: METR Time Horizon Doubl", "highlights": ["\n\u1e4010k\u1e4032k\n\n2027\n\nOldest\n\n16% <3
months\n\nYesNo\n\n8%\n\n3-3.5 months\n\nYesNo\n\n12%\n\n3.5-4 months\n\nYesNo\n\n15%\n\n4-4.5 months\n\nYesNo\n\n13%\n\n4.5-5 months YesNo\n\n10%\n\n5-5.5 months\n\nYesNo\n\n7%\n\n5.5-6
months\n\nYesNo\n\n4%\n\n6-6.5 months\n\nYesNo\n\n4%\n\n6.5-7 months\n\nYesNo\n\n11%  ...    This market matches Software Engineering: METR Time Horizon Doubling Time [from the AI 2026 Forecasting
...    Resolves to the best-fit doubling time for METR-HRS frontier models as of December 31, 2026, computed using the methodology described in the More Info section of the survey (see here). If METR
releases an updated METR-HRS suite that is a clear successor with comparable difficulty for questions at the  ...    Buckets are left-inclusive: e.g., 4-4.5 months includes 4.0 but not 4.5.\n\nMarket
contextGenerate Technology\n\nAI\n\n2026 AI Forecasting Survey by AI Digest\n\nFollow\n\nSign upGet\n\n1,000  ...    Claude Sonnet 4.6 METR 50% time horizonBayesian\n\nGrok 4.20 METR 50% time
horizonBayesian Will the METR 50% Time Horizon be \"ambiguous\" at the end of 2026?Bayesian39% chance What will the frontier METR time horizon be on January 1, 2027?Benthamite  ...    Model with METR
time horizon \u22658 hours released in 2026?Ben96% chance  ...    The 2026 doubling time is very sensitive to the highest value from 2025 (and its timing). Time horizon 1.1 revises late 2025 numbers
upward, which means the doubling time will look longer than it is. A 3 month doubling time would require something getting to ~43 hours by late November, or longer if it's released later. A full work
week without human intervention.Edit: ha no my math sucks, it would actually be 85 hours.Arbitrage opportunity: https://manifold.markets/Bayesian/best-metr-time-horizons-in-2026  ...    @bh The new
graph has made think that by the end of the year we will see a SOTA model that has a time horizon length of somewhere between 24 to 30 hours. Bayesian  ...    @bens jan 25 anywhere on earth\n\njim
opened a \u1e401,000 YES at 7% order order up ('yes' for <3 months)\n\n23 replies\n\nBayesian\n\n@jim I'm tempted tbh but Bayesian\n\nthat would be 4 doublings in 2026, roughly 80 hours at EOY
Bayesian filled a \u1e4012,000 NO at 7% order\n\nok i filled it\n\njim(edited) @Bayesian my best guess for current doubling-times is 2.86 months, so this market should hopefully resolve in my favour.
The measurement itself of model horizons this long is the main thing I'd be worried about (and I haven't  ...    So current expected time horizons are 5 x 2^461 hours? That\u2019s a lot of hours. But
anyway 2.86 months doubling time is  ...    @Bayesian I am confused by how doubling time are determined. How would I determine the METR doubling time  ...    @MaxLennartson it isn't a function of only
the time at the end of the year, it's the line of best fit across all the frontier datapoints across the entire year. so if it's 5 hours til september and then 20 hours in  ...    @Bayesian Assuming
19-24 hours by end of the year. It seems unlikely that the doubling time would be less than three months but it could be 4.5, 5 or even 6 months. Does it come down to guessing or is there a strategy
to  ...    @MaxLennartson the quickest estimate is to do 19-24hours divided by the current best score of 4h49min,  ...    @Bayesian I am still a bit confused. Maybe I am doing my math wrong. I did 19
hours divided by 4 hours 49 minutes. I got 3.94463668 (3 hours 56 minutes 41 seconds). 3."], "published_date": null, "score": null}, {"title": "Are AI time-horizons (still) doubling every 7 months? -
Medium", "url": "https://medium.com/@AIchats/are-ai-time-horizons-still-doubling-every-7-months-6262ed2bcc6a", "snippet": "Are AI time-horizons (still) doubling every 7 months? | by Anatol Wegner |
Mar, 2026 | Medium\n\nSitemap\n\nOpen in app\n\nSign up\n\nSign in\n\nMedium Logo\n\nGet app\n\nWrite\n\nSearch\n\nSign up\n\nSign in\n\n# Are AI time-horizons (still) doubling every 7
months?\n\nAnatol Wegner\n\n14 min read\n\n1 day ago\n\n--\n\nListen\n\nShare\n\n## A critical review of METR\u2019s \u2018Task-Completion Time Horizons of Frontier AI Models\u2019 benchmark with the
assistance of Gemini.\n\nPress enter or click to view image in full size\n\nThis is a continuat", "highlights": [" ## A critical review of METR\u2019s \u2018Task-Completion Time Horizons of Frontier
AI Models\u2019 benchmark with the assistance of Gemini.  ...    This is a continuation of a previous conversation about METR time horizon benchmark paper which can be found  ...    The conversation
starts with me providing Gemini with the data file of the latest benchmark results which can be  ...    Q: Hi again. So METR have released an updated set of results that includes newer models \u2014
the results are in the  ...    Gemini: Based on the updated dataset you provided, which includes models released through early February 2026, we can  ...    - More starkly, the from_2023_on doubling
time is estimated at 128.7 days (just over 4 months), with a confidence interval of [105, 157]. - The updated all_time_stitched point estimate is now 187.8 days. - The original paper claimed a
doubling time of roughly 212 days (approx. 7 months) for the 2019\u20132025 period. In the roughly one year between the original paper\u2019s cutoff (Claude 3.7 Sonnet at ~60 minutes) and the latest
model in this dataset (Claude Opus 4.6 at ~718 minutes), the estimated p50 time horizon has increased by a factor of 12.  ...    - Claude Opus 4.6 (Feb 2026): Estimate 718 mins. CI: [319, 3949]  ...
3. Implications for the \u201cScaling Law\u201d and ExtrapolationThe original paper extrapolated a 7-month doubling time to predict that AI would reach a 1-month horizon (167 hours, or 10,020 minutes)
between late 2028 and early 2031. If one were to apply the updated 128-day doubling time to the latest 718-minute baseline, that 1-month horizon would be reached vastly sooner \u2014 likely within
late 2026 or early 2027. Furthermore, the upper bound of Claude Opus 4.6\u2019s  ...    4. Model DiversityThe updated dataset does introduce one non-Anthropic/OpenAI data point (gemini_3_pro, with a
224-minute horizon). While this marginally improves the diversity of the sample, the dataset remains overwhelmingly  ...    - The updated benchmark results show an aggressive acceleration (128-day
doubling time) precisely as models enter the multi-hour, economically valuable domain. - Their mission assumes \u201cfast and drastic\u201d change and warns against waiting to \u201csee whether things
seem to be going  ...    functions as an alarm bell. By generating estimates that show a 12-fold increase in capability horizons in a single  ...    In summary, the new data does not resolve the
methodological critiques of the original paper; it magnifies them. It  ...    When the authors fit a logistic curve to these binned data points, the exact spot where the curve crosses the 50%
threshold \u2014 the heralded \u201ctime horizon\u201d \u2014 is highly sensitive to the success rate within just one or two of these  ...    The statistical model is screaming that it has no data. It
is trying to find a 50% success threshold for models that  ...    Q: So let\u2019s see what factors play into the estimated time scales given the logistic fit to the data. Now we can reasonably assume
that the latest models can solve tasks with length less than one hour with high success probability, that is something like 80\u201390% of the time (as per METR\u2019s own p80 estimates). In this case
the time horizon estimate is essentially determined by 4 data points i.e. the 2\u20134, 4\u20138, 8\u201316 and 16h+ bins. Crucially even slight changes in the success rate of the latter two will
significantly increase the estimate i.e. even a few percentage point increases in the average success rate will dramatically push up the estimated time scale due to the logarithmic scale of the time
...    Gemini: This is an incredibly sharp mathematical critique. You have essentially reverse-engineered the vulnerability in  ...    This perfectly explains the explosive jump in the 2026 data.
Claude Opus 4.6\u2019s estimated horizon of 718 minutes (approx. 12 hours) is almost certainly not the result of it reliably completing a wide, robust distribution of 12-hour  ...    stretch the p50
point deep into the >10-hour territory to make the curve fit. Conclusion: Measuring Noise, Not a Scaling LawYour deduction reveals that at the frontier edge of this benchmark, the \u201ctask
completion time horizon\u201d is no longer a continuous measure of general AI capability. It is a mathematical artifact highly leveraged by discrete events. If a model gets lucky on a single 8-hour
task (perhaps because that specific coding problem happened to be  ...    When you plot these highly volatile, single-task-dependent intercepts against time, you are not plotting a fundamental  ...
renders the \u201c128-day doubling time\u201d and the extrapolations to a \u201c1-month AGI\u201d mathematically unsubstantiated.  ...    whether a model gets a time horizon of 10 minutes or 10 hours
\u2014 relies almost entirely on the 7 tasks in RE-Bench  ...    the 128-day or 212-"], "published_date": "2026-03-11T03:45:51.610", "score": null}, {"title": "This is the most misunderstood graph in
AI - MIT Technology Review", "url": "https://www.technologyreview.com/2026/02/05/1132254/this-is-the-most-misunderstood-graph-in-ai/", "snippet": "This is the most misunderstood graph in AI | MIT
Technology Review\nSkip to Content\n\nMIT Technology Review\n\n* Featured\n* Topics\n* Newsletters\n* Events\n* Audio\n\nMIT Technology Review\n\n* Featured\n* Topics\n* Newsletters\n* Events\n*
Audio\nArtificial intelligence\n# This is the most misunderstood graph in AI\nTo some, METR\u2019s \u201ctime horizon plot\u201d indicates that AI utopia\u2014or apocalypse\u2014is close at hand. The
truth is more complicated.\nBy\n* Grace Huckinsarchive page\nFebruary 5, 2026\n&amp;quot;&amp;quot;Stepha", "highlights": [" AI To some, METR\u2019s \u201ctime horizon plot\u201d indicates that AI
utopia\u2014or apocalypse\u2014is close at hand. The truth is more complicated. By\n* Grace Huckinsarchive page\nFebruary 5, 2026&quot;&quot;Stephanie Arnett/MIT Technology Review | Public domain
(ship)  ...    Every time OpenAI, Google, or Anthropic drops a new frontier large language model, the AI community holds its breath. It doesn\u2019t exhale until METR, an AI research nonprofit whose
name stands for \u201cModel Evaluation & Threat Research,\u201d updates a now-iconic graph that has played a major role in the AI discourse since it was first released in March of last year. The graph
suggests that certain AI capabilities are developing at an exponential rate, and more  ...    That was certainly the case for Claude Opus 4.5, the latest version of Anthropic\u2019s most powerful
model, which was released in late November. In December, METR announced that Opus 4.5 appeared to be capable of independently completing a task that would have taken a human about five hours\u2014a
vast improvement over what even the exponential trend would  ...    More fundamentally, the METR plot does not measure AI abilities writ large, nor does it claim to. In order to build the graph, METR
tests the models primarily on coding tasks, evaluating the difficulty of each by measuring or estimating how long it takes humans to complete it\u2014a metric that not everyone accepts. Claude Opus
4.5 might be able to complete  ...    METR was founded to assess the risks posed by frontier AI systems. Though it is best known for the exponential trend plot, it has also worked with AI companies to
evaluate their systems in greater detail and published several other independent research projects, including a widely covered July 2025 study suggesting that AI coding  ...    with that graph\u2019s
often breathless reception. In January, Thomas Kwa, one of the lead authors on the paper that  ...    Part of the trouble with the METR plot is that it\u2019s quite a bit more complicated than it
looks. The x-axis is simple enough: It tracks the date when each model was released. But the y-axis is where things get tricky. It records each model\u2019s \u201ctime horizon,\u201d an unusual metric
that METR created\u2014and that, according to Kwa and Von Arx, is frequently  ...    To understand exactly what model time horizons are, it helps to know all the work that METR put into calculating
them. First, the METR team assembled a collection of tasks ranging from quick multiple-choice questions to detailed coding  ...    to fall off. From a model\u2019s performance, the researchers
calculated the point on the time scale of human tasks at which the model would complete about 50% of the tasks successfully. That point is the model\u2019s time horizon. All that detail is in the blog
post and the academic paper that METR released along with the original time horizon  ...    the time horizon metric can get lost in the shuffle. One common misapprehension is that the numbers on the
plot\u2019s y-axis\u2014around five hours for Claude Opus 4.5, for example\u2014represent the length of time that the models can operate  ...    perform. Kwa has seen this error so frequently that he
made a point of correcting it at the very top of his recent blog  ...    As complex and widely misinterpreted as the time horizon concept might be, it does make some basic sense: A model with a one-
hour time horizon could automate some modest portions of a software engineer\u2019s job, whereas a model with a 40-hour horizon could potentially complete days of work on its own. But some experts
question whether the amount of  ...    ]Read next Von Arx says that she, too, was originally skeptical that time horizon was the right measure to use. What convinced her was seeing the results of her
and her colleagues\u2019 analysis. When they calculated the 50% time horizon for all the major models available in early 2025 and then plotted each of them on the graph, they saw that the time
horizons for the top-tier models were increasing over time\u2014and, moreover, that the rate of advancement was speeding up. Every seven-ish months, the time horizon doubled, which means that the most
advanced models could complete tasks that took humans nine seconds in mid 2020, 4 minutes in early 2023, and 40 minutes in late 2024. \u201cI can do all the theorizing I want about whether or not it
makes sense, but the trend is there,\u201d Von Arx says. It\u2019s this dramatic pattern that made the METR plot such a blockbuster. Many people learned about it when they read AI 2027, a viral sci-fi
story cum quantitative forecast positing that superintelligent AI could wipe out  ...    boosters, the exponential trend indicates that AI will soon usher in an era of radical economic growth. The
venture capital firm Sequoia Capital, for example, recently put out a post titled \u201c2026: This is AGI,\u201d which used the METR plot to argue that AI that can act as an employee or contractor
will soon arrive. \u201cThe provocation really was  ...    Just because a model achieves a one-hour time horizon on the METR plot, however, doesn\u2019t mean that it can replace one hour of human work
in the real world. For one thing, the tasks on which the models are evaluated don\u2019t reflect the complexities and confusion of real-world work. In their original study, Kwa, Von Arx, and their
colleagues quantify  ...    Despite these limitations, many people"], "published_date": "2026-02-05T00:00:00.000", "score": null}, {"title": "[ACX 2026] Will an AI model reach a 3 hour time horizon
with 80% reliability during 2026? | Manifold", "url": "https://manifold.markets/WalterMartin/acx-2026-will-an-ai-model-reach-a-3", "snippet": "[ACX 2026] Will an AI model reach a 3 hour time horizon
with 80% reliability during 2026? | Manifold\nOpen options\n[ACX 2026] Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?\nWalterMartin
avatar\nwalmart\n55\n5.1k\u1e407347\nDec 31\n57%\nchance\n5\n1H\n6H\n1D\n1W\n1M\nALL\nBetYESBetNO\nResolves according to Metaculus resolution.\nMetaculus high-level description:\nThis question will
resolve as**Yes**if, during 2026,METR estimatesthat an AI model has a time horizon of \u22653 hours at 80% relia", "highlights": ["walmart\n55\n5.1k\u1e407347\nDec
31\n57%\nchance\n5\n1H\n6H\n1D\n1W\n1M\nALL\nBetYESBetNO Resolves according to Metaculus resolution.\nMetaculus high-level description: This question will resolve as**Yes**if, during 2026,METR
estimatesthat an AI model has a time horizon of \u22653 hours at 80% reliability, i.e. the AI has an estimated \u226580% reliability on tasks requiring human experts \u22653 hours to solve. This
question is managed and resolved by Manifold.\nMarket contextGenerate\nTechnology\nAI Technical AI Timelines\nACX 2026 Prediction Contest\nFollow\nSign upGet\n\u1e401,000 to start
trading!\n\nComments\n\n54 Holders\n\n83 Trades\n\nOpen options  ...   MatthewBarnett avatar\nMatthew Barnett\n-3% 1d59%chance\n] AI time horizon of 20 hours by January 1st 2027?\njim
avatar\njim\n80%chance\n Which \"AI 2027\" predictions will be right by Late 2026?\nBayesianTom avatar\nBayesianTom  Will a publicly known AI model achieve an 80% time horizon that is an 1 hour and 30
minutes by September 2026?Blocksterpen3 avatar\nBlocksterpen3\n82%chance\n Will models be able to do the work of an AI researcher/engineer before 2027?\nTossup avatar\nTossup 25%chance\n\nAI time
horizon of 10 hours by September 1st 2026?\njim avatar\njim\n80%chance \nBest AI time horizon by August 2026, per METR?\nJoshYou avatar\nJosh\n Will an AI achieve >80% performance on the FrontierMath
benchmark before 2027?\nBayesian avatar Bayesian\n48%chance\n Before 2027, will a frontier AI model achieve an AA-Omniscience hallucination rate below 5%?JaundicedBaboon avatar\nJaundiced
Baboon\n32%chance\n Will an AI achieve >85% performance on the FrontierMath benchmark before 2027?\nBayesian avatar  ...    Will an AI achieve >85% performance on the FrontierMath benchmark before
2028?\nMatthewBarnett avatar Matthew Barnett\n59%chance\n\nAI time horizon of 20 hours by January 1st 2027?\njim avatar\njim 80%chance\n\nWhich \"AI 2027\" predictions will be right by Late
2026?BayesianTom avatar\nBayesianTom\n Will a publicly known AI model achieve an 80% time horizon that is an 1 hour and 30 minutes by September 2026?Blocksterpen3 avatar\nBlocksterpen3\n82%chance\n
Will models be able to do the work of an AI researcher/engineer before 2027?\nTossup avatar\nTossup 25%chance\n\nAI time horizon of 10 hours by September 1st 2026?\njim avatar\njim\n80%chance \nBest
AI time horizon by August 2026, per METR?\nJoshYou avatar\nJosh\n Will an AI achieve >80% performance on the FrontierMath benchmark before 2027?\nBayesian avatar Bayesian\n48%chance\n Before 2027,
will a frontier AI model achieve an AA-Omniscience hallucination rate below 5%?JaundicedBaboon avatar\nJaundiced Baboon\n32%chance\n[ Will an AI achieve"], "published_date": null, "score": null},
{"title": "Is METR Underestimating LLM Time Horizons", "url": "https://andreasrobinson.substack.com/p/is-metr-underestimating-llm-time", "snippet": "Is METR Underestimating LLM Time Horizons\n\n#
Andreas Robinson\nSubscribeSign in\n# Is METR Underestimating LLM Time Horizons\n\nAndreas Robinson's avatar\n\nAndreas Robinson\nJan 22, 2026\n1\nShare\n**TL;DR**\n* *Using METR human-baseline data,
I define an alternate LLM time-horizon measure, i.e. the longest time horizon over which an LLM exceeds human baseline reliability (or equivalently the intersection point of the human and LLM logistic
curves), and this measure shows a much faster growth-trend than M", "highlights": [", 2026\n1\nShare\n**TL;DR** * *Using METR human-baseline data, I define an alternate LLM time-horizon measure, i.e.
the longest time horizon over which an LLM exceeds human baseline reliability (or equivalently the intersection point of the human and LLM logistic curves), and this measure shows a much faster
growth-trend than METR\u2019s fixed-threshold trends: doubling every 1.9 months, versus 6.8 months for the 50% METR-trend over the same time period. Also, since this metric is directly  ...
principled way to assess time to human-level horizons, which suggests roughly 2026-2027, with substantial uncertainty.*  ...    The METR time-horizon metric provides estimates for the longest software
tasks that a given AI is capable of completing [[2]]. This estimate is based on human baseline measurements for how long a set of software tasks took human engineers, with the (geometric) average time
based on the subset of humans who succeeded at each task. METR also measured human reliability at each task, but rather than compare the AIs to those human levels, they have typically reported LLM
time horizons at fixed reliabilities independent of task length (e.g. 50% or 80%). The METR estimates have featured prominently in efforts to estimate the timeline to human level long-horizon agency,
e.g. per the AI-2027 forecasts[[3]]. The following bullets describe potential downsides of this METR horizon approach and  ...    doing is not comparing to fixed target reliabilities at each horizon
length (e.g. METR\u2019s 50% and 80% targets), but  ...    * *Potentially unattainable bar for human-level:* A related issue is that if we require AI to exceed a fixed 50% horizon at every time
horizon in order to be considered human level, then it\u2019s not clear that this will ever occur,  ...    *below) and instead focus on absolute reliability targets. One issue is that current LLMs
e.g. gpt-5 already exceed the METR human baseline time horizons at both the 50% and 80% targets; however, humans do still have fatter tailed  ...    4.5, since this claim is less clear now*). For
instance, gpt-5 has worse reliability than the human baselines once the METR task length gets longer than 4.5 hr, but note its 50% horizon is only 2.3 hr. Using these human-reliability baselines, we
can estimate LLM time horizons, as the longest task duration over which the LLM is more reliable than the  ...    ## 1.3 **Trends in Human-Relative Metric (exponential fit)** The trend in this human-
relative time horizon metric is increasing much faster than the existing METR trends, and assuming an exponential fit, the LLM time horizons at human-reliability are doubling every 1.9 months, versus
every 7 months over the same time period for the METR (50%-reliability) time horizon trend (see *Table 1 *and* Figure 2*). In other words, every 1.9 months there is a doubling in the longest time
horizon that LLMs can handle at METR\u2019s human  ...    * *AI-2027 super-exponential projection:* The AI-2027 project has argued, with some controversy, for using a super-exponential finite-time
blowup for projecting the METR fixed-reliability (80%) time horizons; per above, this seems poorly supported in that fixed reliability case, but it is much better supported for this alternative  ...
## 1.5 **Projections to Reach Human Level (hyperbolic fit)** Per above, with an exponential fit, LLMs would never catch up with humans, but with a hyperbolic fit the current trend suggests human level
by around mid 2026, relative to the (weak) METR human baselines (see *Table 2*). That table also  ...    level into 2027. These stronger baselines have flatter slope, with human reliability dropping
more slowly with longer  ...    connection to actual human performance; for instance, based on METR\u2019s human-baseline logistic fit, we should expect humans to get about 3% reliability for tasks at
1-month horizon (along the METR difficulty trend line), so it\u2019s not clear why we would require \u201chuman-level\u201d AI to get 50% (or 80%). That said, in so"], "published_date":
"2026-01-22T00:00:00.000", "score": null}, {"title": "Time Horizon 1.1 - METR", "url": "https://metr.org/blog/2026-1-29-time-horizon-1-1/", "snippet": "Time Horizon 1.1 - METR\n* Research\n* Notes\n*
Updates\n* About\n* Donate\n* Careers\n* \nSearch\n\n\nMETR Logo\n\n* Research\n* Notes\n* Updates\n* About\n* Donate\n* Careers\n*\n\nMenu\nTime Horizon 1.1\n##### DATE\nJanuary 29, 2026\n#####
SHARE\n** Copy Link\n** Citation\nBibTeX Citation\n&times;\n```bibtex\n<span class=\"nc\">@misc</span><span class=\"p\">{</span><span class=\"p\">time-horizon-1-1</span><span class=\"p\">,</span>\n
<span class=\"na\">title</span> <span class=\"p\">=</span> <span class=\"s\">{Time Horizon 1.1}</span>", "highlights": [" Updates\n* About\n* Donate * Careers\n*\n\nMenu\nTime Horizon 1.1\n#####
DATE\nJanuary 29, 2026\n##### SHARE\n** Copy Link  ...    <span class=\"nc\">@misc</span><span class=\"p\">{</span><span class=\"p\">time-horizon-1-1</span><span class=\"p\">,</span>  ...
class=\"s\">{\\url{https://metr.org/blog/2026-1-29-time-horizon-1-1/}}</span><span class=\"p\">,</span> <span class=\"na\">year</span> <span class=\"p\">=</span> <span class=\"s\">{2026}</span><span
class=\"p\">,</span>  ...    **We\u2019re releasing a new version of our time horizon estimates (TH1.1), using more tasks and a new eval infrastructure.** Our estimates of time horizons for many
models have been updated. The new estimates generally fall within our existing confidence intervals, though the trend in time horizon growth looks a little different, discussed below. We expect to
...    **Early in 2025 we published our time-horizon methodology for measuring the autonomous capabilities of AI models.** We found a steady exponential increase in models\u2019 human-equivalent
\u201ctime horizon.\u201d Over the course of 2025 we applied  ...    **We are rolling out two significant changes to our time-horizon evaluation setup:** 1. Improvements to our task suite. We
increased our suite from 170 to 228 tasks. We added 73 tasks (all are from HCAST,  ...    We have re-estimated the effective time horizons for 14 models, using performance on our new TH1.1 task suite
and evaluation infrastructure. The new estimates generally lie within the confidence intervals from the TH1 time horizons.  ...    We increased the tasks in our suite by 34% (228/170) and doubled the
number of tasks that are 8 hours or longer  ...    Our original time horizon dataset, released in March 2025, showed a smooth trend with the frontier time-horizon doubling around every 7 months over
the period 2019 to 2025.  ...    Measurements of the 50%-time-horizon of different models across different task suites and evaluation infrastructures.  ...    identical. The post-2023 doubling-time is
131 days under TH1.1, compared to 165 days under TH1, meaning progress is  ...    As discussed above, even our Time Horizon 1.1 suite has relatively few tasks that the latest generation of models  ...
## Appendices\n### Data  ...    ### Comparison of Old and New Estimates\n| |TH1.0|TH1.1| |P50 doubling time|195.8 days [162, 223]|196.5 days3| |P50 doubling time, >=2023|165.3 days [129, 211]|130.8
days [107, 161]| |P50 doubling time, >=2024|108.9 days|88.6 days|\n| | | |\n|Tasks|170|228|\n|Tasks 8h+|14|31|  ...    ### Changes to Model Horizon Estimates\n| |TH1|TH1.1|Change|\n|Claude Opus
4.5|289 [110,1268]|320 [170,729]|+11%| |GPT-5.1-codex-max|173 [81,411]| | |\n|Claude Sonnet 4.5|122 [59,252]| | |\n|GPT-5|138 [68,281]|214 [117,480]|+55%| |Claude Opus 4.1|114 [56,215]| | |\n|Claude
Opus 4|86 [44,144]|101 [58,170]|+18%|\n|Grok 4|109 [48,235]| | |  ...    The TH1.1 time horizons all fell within the TH1 bootstrapped confidence intervals, however those bootstraps represent  ...
<span class=\"nc\">@misc</span><span class=\"p\">{</span><span class=\"p\">time-horizon-1-1</span><span class=\"p\">,</span> <span class=\"na\">title</span> <span class=\"p\">=</span> <span
class=\"s\">{Time Horizon 1.1}</span><span  ...    <span class=\"na\">author</span> <span class=\"p\">=</span> <span class=\"s\">{METR}</span><span class=\"p\">,</span>  ...
class=\"s\">{\\url{https://metr.org/blog/2026-1-29-time-horizon-1-1/}}</span><span class=\"p\">,</span> <span class=\"na\">year</span> <span class=\"p\">=</span> <span class=\"s\">{2026}</span><span
class=\"p\">,</span> <span class=\"na\">month</span> <span class=\"p\">=</span> <span class=\"s\">{01}</span><span class=\"p\">,</span> <span class=\"p\">}</span>\n```\n**\nMETR Logo **METR**
researches, develops, and evaluates frontier AI systems to measure how well they can perform complex tasks autonomously. Subscribe to our newsletter for updates. Want to contribute to this work? METR
is hiring: View open roles\n## Featured research METR researches, develops and runs cutting-edge tests of AI capabilities, including"], "published_date": "2026-01-29T00:00:00.000", "score": null},
{"title": "METR: Measuring AI Ability to Complete Long Tasks - LessWrong 2.0 viewer", "url": "https://www.greaterwrong.com/posts/deesrjitvXM4xYGZd/metr-measuring-ai-ability-to-complete-long-tasks",
"snippet": "METR: Measuring AI Ability to Complete Long Tasks - LessWrong 2.0 viewer\n\n# METR: Measuring AI Ability to Complete Long Tasks\n\nLink post\n\nSummary: We propose measuring AI performance
in terms of the length of tasks AI agents can complete. We show that this metric has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months.
Extrapolating this trend predicts that, in under five years, we will see AI agents that can independently complete a large fr", "highlights": [" We propose measuring AI performance in terms of the
length of tasks AI agents can complete. We show that this metric has been consistently exponentially increasing over the past 6 years, with a doubling time of around 7 months. Extrapolating this trend
predicts that, in under five years, we will see AI agents that can independently complete a large fraction of software tasks that currently take humans days or weeks. The length of tasks (measured by
how long they take human professionals) that generalist frontier model agents can complete autonomously with 50% reliability has been doubling approximately every 7 months for the last 6 years. The
shaded region represents 95% CI calculated by hierarchical bootstrap over task families, tasks, and task attempts.  ...    We think that forecasting the capabilities of future AI systems is important
for understanding and preparing for the  ...    Current frontier AIs are vastly better than humans at text prediction and knowledge tasks. They outperform experts on  ...    We find that measuring the
length of tasks that models can complete is a helpful lens for understanding current AI  ...    On a diverse set of multi-step software and reasoning tasks, we record the time needed to complete the
task for humans with appropriate expertise. We find that the time taken by human experts is strongly predictive of model success on a given task: current models have almost 100% success rate on tasks
taking humans less than 4 minutes, but succeed <10% of the time on tasks taking more than around 4 hours. This allows us to characterize the abilities of a given model by \u201cthe length (for humans)
of tasks that the model can successfully complete with x% probability\u201d. For each model, we can fit a logistic curve to predict model success probability using human task length. After fixing a
success probability, we can then convert each model\u2019s predicted success curve into a time duration, by looking at the length of task where the predicted success curve intersects with that
probability. For example, here are fitted success curves for several models, as well as the lengths of tasks where we predict a 50% success rate: Depiction of the process of computing the time
horizon. For example, Claude 3.7 Sonnet (the right-most model, represented in the darkest green) has a time horizon of approximately one hour, as this is where its fitted logistic curve intersects the
50% success probability threshold. We think these results help resolve the apparent contradiction between superhuman performance on many benchmarks and the common empirical observations that models do
not seem to be robustly helpful in automating parts of people\u2019s  ...    That being said, by looking at historical data, we see that the length of tasks that state-of-the-art models can complete
(with 50% probability) has increased dramatically over the last 6 years. If we plot this on a logarithmic scale, we can see that the length of tasks models can complete is well predicted by an
exponential trend, with a doubling time of around 7 months. Our estimate of the length of tasks that an agent can complete depends on methodological choices like the tasks used  ...    correct, at
around 1-4 doublings per year. If the measured trend from the past 6 years continues for 2-4 more years, generalist autonomous agents will be capable of performing a wide range of week-long tasks. The
steepness of the trend means that our forecasts about when different capabilities will arrive are relatively robust  ...    estimates rather than baselines. This shows an even faster doubling time, of
under 3 months.[2] We replicate our results on SWE-bench Verified and observe a similar exponential trend  ...    A sensitivity analysis of the extrapolated date at which frontier AI systems will have
a horizon of 1 month. In each row, we apply 10,000 random perturbations to our data and find the distribution over the date of 1-month AI implied by the perturbed data. Box endpoints represent the
25th and 75th percentiles, and whiskers the 10th and 90th percentiles,  ...    trends in AI are more predictive of future performance than pre-2024 trends. As shown above, when we fit a similar trend
to just the 2024 and 2025 data, this shortens the estimate of when AI can complete month-long tasks with 50% reliability by about 2.5 years.  ...    First, our work demonstrates an approach to making
benchmarks more useful for forecasting: measuring AI performance in terms of the length of tasks the system can complete (as measured by how long the tasks take humans). This allows us to measure how
models have improved over a wide range of capability levels and diverse domains.[3] At the same time, the  ...    Second, we find a fairly robust exponential trend over years of AI progress on a
metric which matters for real-world  ...    code]. As mentioned above, this direction could be highly relevant to the design of future evaluations, so  ...    In addition, METR is hiring! This project
involved most staff at METR in some way, and we\u2019re currently  ...    ---\n\nSee also: tweet thread.\n\n^  ...    - Noosphere89's comment on Why Cor\u00adrigi\u00adbil\u00adity is Hard and
Im\u00adpor\u00adtant (i.e. \u201cWhence the high MIRI con\u00adfi\u00addence in al\u00adign\u00adment difficulty?\u201d) by Raemon (30 Sep 2025 14:40 UTC; 1 point)  ...    - [How far along
Metr\u2019"], "published_date": null, "score": null}]
```

## 💬 Response

Now I have rich data. Let me synthesize the key findings and compute the forecast.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Key data points for the CP trend\ndates = ['2026-02-07', '2026-02-14', '2026-02-21', '2026-02-28', '2026-03-07', '2026-03-14']\ncp_values = [55.0, 62.0, 65.0, 70.0, 72.0, 74.2]\n\n# Weekly changes\nchanges = [cp_values[i] - cp_values[i-1] for i in range(1, len(cp_values))]\nprint(\"Weekly CP changes:\", changes)\nprint(\"Average weekly change:\", np.mean(changes))\nprint(\"Recent weekly changes (last 3):\", changes[-3:])\nprint(\"Average of last 3:\", np.mean(changes[-3:]))\n\n# The threshold is 74.20% (current value)\n# Time remaining: from ~March 14 to March 28 = ~14 days = ~2 weeks\n# Question: will CP be STRICTLY above 74.20% on March 28?\n\n# The trend is clearly upward but decelerating\n# Weekly changes: 7.0, 3.0, 5.0, 2.0, 2.2\n# The rate of increase has slowed from ~7/week to ~2/week\n\n# Let's model this as a random walk with drift\n# Using recent data (last 3 weeks) for drift estimate\nrecent_drift_per_week = np.mean(changes[-3:])\nprint(f\"\\nRecent drift per week: {recent_drift_per_week:.2f}%\")\n\n# Volatility estimate from changes\nvolatility_per_week = np.std(changes[-3:])\nprint(f\"Volatility per week (last 3): {volatility_per_week:.2f}%\")\n\n# Full sample volatility\nfull_vol = np.std(changes)\nprint(f\"Full sample volatility: {full_vol:.2f}%\")\n\n# Monte Carlo simulation\nnp.random.seed(42)\nn_sims = 100000\nweeks_ahead = 2  # ~14 days\ncurrent_cp = 74.2\nthreshold = 74.2\n\n# Use recent drift and full-sample volatility \ndrift = recent_drift_per_week  # ~3.07% per week\nvol = full_vol  # ~1.89% per week\n\n# Simulate 2 weeks of random walk\nfinal_cps = np.zeros(n_sims)\nfor i in range(n_sims):\n    cp = current_cp\n    for w in range(weeks_ahead):\n        cp += np.random.normal(drift, vol)\n        # CP bounded between 1 and 99\n        cp = max(1, min(99, cp))\n    final_cps[i] = cp\n\nprob_above = np.mean(final_cps > threshold)\nprint(f\"\\nMonte Carlo results:\")\nprint(f\"P(CP > {threshold}%) on March 28: {prob_above:.3f}\")\nprint(f\"Median final CP: {np.median(final_cps):.1f}%\")\nprint(f\"25th-75th percentile: {np.percentile(final_cps, 25):.1f}% - {np.percentile(final_cps, 75):.1f}%\")\nprint(f\"10th-90th percentile: {np.percentile(final_cps, 10):.1f}% - {np.percentile(final_cps, 90):.1f}%\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Weekly CP changes: [7.0, 3.0, 5.0, 2.0, 2.200000000000003]\nAverage weekly change: 3.8400000000000007\nRecent weekly changes (last 3): [5.0, 2.0,
2.200000000000003]\nAverage of last 3: 3.0666666666666678\n\nRecent drift per week: 3.07%\nVolatility per week (last 3): 1.37%\nFull sample volatility: 1.90%\n\nMonte Carlo results:\nP(CP > 74.2%) on
March 28: 0.989\nMedian final CP: 80.3%\n25th-75th percentile: 78.5% - 82.2%\n10th-90th percentile: 76.9% - 83.8%\n", "stderr": "", "duration_ms": 370}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me also run a more conservative scenario\n# The drift is clearly decelerating - let me model potential deceleration\n\n# Weekly changes: 7.0, 3.0, 5.0, 2.0, 2.2\n# There's a clear deceleration trend\n# Let me also consider that the CP might stall or even decline\n\n# More conservative model: use only the last 2 weeks of drift\nrecent_2_drift = np.mean([2.0, 2.2])\nprint(f\"Last 2 weeks drift: {recent_2_drift:.2f}%/week\")\n\n# Even more conservative: assume drift slows further\n# As CP approaches higher levels, new information needed to push it higher\n\n# Run scenarios with different drift assumptions\nscenarios = {\n    \"Optimistic (full drift)\": (3.07, 1.90),\n    \"Moderate (last 2 weeks)\": (2.1, 1.90),\n    \"Conservative (drift halves)\": (1.0, 2.0),\n    \"Very conservative (no drift)\": (0.0, 2.5),\n    \"Pessimistic (slight downward)\": (-0.5, 2.5),\n}\n\nnp.random.seed(42)\nn_sims = 100000\nweeks_ahead = 2\ncurrent_cp = 74.2\nthreshold = 74.2\n\nfor name, (drift, vol) in scenarios.items():\n    final_cps = current_cp + np.random.normal(drift * weeks_ahead, vol * np.sqrt(weeks_ahead), n_sims)\n    prob = np.mean(final_cps > threshold)\n    print(f\"{name}: P(above) = {prob:.3f}, median = {np.median(final_cps):.1f}%\")\n\n# Key considerations:\n# 1. The underlying question is about AI reaching 3hr at 80% reliability\n# 2. Current best 80% time horizon is ~31 minutes (GPT-5.1-Codex-Max as of Dec 2025)\n# 3. But the 50% horizon is already ~14.5 hours for Claude Opus 4.6\n# 4. The gap between 50% and 80% horizons has been closing\n# 5. Manifold market for the same question is at ~57-79%\n# 6. The CP has been steadily rising, suggesting forecasters are increasingly optimistic\n# 7. New model releases (Claude Opus 4.6, GPT-5.3, Gemini 3) could trigger further upward movement\n\n# The question is specifically whether CP will be STRICTLY above 74.2%\n# Given the strong upward trend and the threshold being exactly the current value,\n# the probability is quite high\n\nprint(\"\\n--- Analysis ---\")\nprint(\"The CP has risen every single week for 5+ weeks\")\nprint(\"The minimum weekly increase was 2.0%\")\nprint(\"Even with zero drift, there's about a 50% chance of being above threshold\")\nprint(\"With any positive drift (which all evidence supports), probability is high\")\nprint(\"The trend shows consistent upward pressure from AI capability improvements\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Last 2 weeks drift: 2.10%/week\nOptimistic (full drift): P(above) = 0.989, median = 80.3%\nModerate (last 2 weeks): P(above) = 0.941, median = 78.4%\nConservative (drift
halves): P(above) = 0.761, median = 76.2%\nVery conservative (no drift): P(above) = 0.501, median = 74.2%\nPessimistic (slight downward): P(above) = 0.386, median = 73.2%\n\n--- Analysis ---\nThe CP
has risen every single week for 5+ weeks\nThe minimum weekly increase was 2.0%\nEven with zero drift, there's about a 50% chance of being above threshold\nWith any positive drift (which all evidence
supports), probability is high\nThe trend shows consistent upward pressure from AI capability improvements\n", "stderr": "", "duration_ms": 10}
```

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\nimport numpy as np\n\n# Let me think carefully about what could push CP DOWN:\n# 1. A major negative news event about AI capabilities (unlikely in 2 weeks)\n# 2. METR publishing updated numbers that show LESS progress than expected\n# 3. General pessimism/reassessment about whether 80% threshold is achievable\n\n# What could push CP UP:\n# 1. New model releases with better benchmarks\n# 2. METR publishing new evaluations showing progress\n# 3. Continued exponential trend in capabilities\n# 4. New analysis posts on LessWrong/EA Forum\n# 5. The existing strong upward momentum\n\n# Key data points supporting continued upward trend:\n# - Claude Opus 4.6 has 50% horizon of ~14.5 hours\n# - 80% horizon was ~31 min as of Dec 2025 (GPT-5.1-Codex-Max)\n# - Doubling time for 80% horizon is ~4-7 months\n# - Need to go from ~31 min to 3 hours (180 min) = ~2.5 doublings\n# - At 4-month doubling: ~10 months needed from Dec 2025 = Oct 2026\n# - At 7-month doubling: ~17.5 months needed from Dec 2025 = May 2027\n# - The 50% horizon is ALREADY well above 3 hours for multiple models\n# - Gap between 50% and 80% has been narrowing\n\n# The Manifold market for the underlying question is at 57% (one version) and 79% (another)\n# The Metaculus CP has been rising steadily\n# The news search revealed Anthropic researcher projecting mid-2026 for 8-hour workday capability\n\n# Weight the scenarios:\n# - Zero or negative drift: very unlikely given fundamentals (10-15% weight)\n# - Drift of ~1%/week (decelerating): moderate probability (30% weight)\n# - Drift of ~2%/week (recent pace): most likely (40% weight)\n# - Drift of ~3%/week (continued strong pace): possible (20% weight)\n\nweights = [0.05, 0.10, 0.30, 0.35, 0.20]\nprobs = [0.386, 0.501, 0.761, 0.941, 0.989]\n\nweighted_prob = sum(w * p for w, p in zip(weights, probs))\nprint(f\"Weighted probability: {weighted_prob:.3f}\")\n\n# Let me also consider that the question is whether CP will be HIGHER than 74.20%\n# Not higher or equal. So even 74.21% counts.\n# The current CP is exactly 74.20%\n\n# Given the extremely strong upward trend (5 consecutive weeks of increases)\n# and the fact that we only need ANY increase at all, \n# the probability is quite high\n\n# Also check: what is the Manifold market at for this specific meta-question?\n# The Manifold market for the underlying event is at 57-79%\n# This suggests continued positive sentiment\n\n# My estimate: ~80-85% probability that CP will be above 74.20% on March 28\n\n# Factors:\n# + Strong upward trend (5 consecutive weeks)\n# + Fundamental AI progress continues rapidly\n# + New model evaluations expected in next 2 weeks\n# + Multiple new models being evaluated by METR\n# - CP could stall as it approaches high levels\n# - 80% horizon still significantly below target\n# - Some contrarian analyses question METR methodology\n\nprint(f\"\\nFinal assessment: ~82% probability\")\nprint(f\"The strong monotonic upward trend is the dominant factor\")\nprint(f\"The threshold being exactly the current value means we only need ANY upward movement\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Weighted probability: 0.825\n\nFinal assessment: ~82% probability\nThe strong monotonic upward trend is the dominant factor\nThe threshold being exactly the current value
means we only need ANY upward movement\n", "stderr": "", "duration_ms": 0}
```

## 💬 Response

Now let me run my reflection checkpoint.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Strong monotonic upward trend in CP: 5 consecutive weekly increases from 55% to 74.2%, never declining",
      "logit": 1.5,
      "confidence": 0.9
    },
    {
      "description": "Threshold equals current CP (74.20%), meaning only marginal upward movement is needed for YES",
      "logit": 1,
      "confidence": 0.95
    },
    {
      "description": "Fundamental AI capability progress supports continued optimism: Claude Opus 4.6 50% horizon at 14.5 hours, doubling time accelerating to ~4 months",
      "logit": 0.8,
      "confidence": 0.7
    },
    {
      "description": "Manifold market for underlying question at 57-79%, showing broad optimism about AI reaching 3hr/80% target",
      "logit": 0.5,
      "confidence": 0.6
    },
    {
      "description": "Deceleration in weekly CP increases (7.0 \u2192 3.0 \u2192 5.0 \u2192 2.0 \u2192 2.2) suggests momentum may be slowing as CP approaches 75%+",
      "logit": -0.5,
      "confidence": 0.7
    },
    {
      "description": "Current best 80% time horizon is only ~31 minutes vs 3-hour target; some analyses question METR methodology and extrapolation reliability",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "Possible negative catalyst: critical analyses of METR methodology (MIT Tech Review, Medium posts) could dampen enthusiasm",
      "logit": -0.3,
      "confidence": 0.4
    }
  ],
  "tentative_estimate": {
    "logit": 1.5,
    "probability": 0.82
  },
  "assessment": "This is a meta-prediction about whether the Metaculus community prediction for 'Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?' will be above 74.20% on March 28. The current CP is exactly 74.20% as of March 14, so we need only marginal upward movement.\n\nKey evidence for YES:\n- CP has risen monotonically for 5+ weeks: 55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%\n- The underlying AI capability trend is strongly positive (METR time horizons doubling every ~4 months recently)\n- New model evaluations continue to come in (Claude Opus 4.6, GPT-5.3 Codex, Gemini 3 Pro)\n- The threshold is exactly the current value, meaning ANY upward movement resolves YES\n\nKey evidence for NO:\n- CP growth has decelerated from ~7%/week to ~2%/week\n- The 80% time horizon is still far from the 3-hour target (current best ~31 minutes)\n- Methodological critiques of METR could dampen enthusiasm\n- CPs can sometimes reverse, especially when approaching high levels\n\nMonte Carlo simulation with weighted scenarios gives ~82% probability. The dominant factor is the strong monotonic trend combined with the threshold being exactly the current value.",
  "tool_audit": "Useful: get_metaculus_questions (got question details but no CP), search_news (rich context on METR progress), web_search (found key METR pages), search_exa (excellent detailed content from LessWrong and METR), manifold_price (found related market at 79%), fetch_url (got METR TH1.1 data). Empty: polymarket_price (no matching markets). The METR time horizons page couldn't extract the graph data which would have been ideal.",
  "calibration_notes": "Base rate for a monotonically rising CP to continue rising over 2 more weeks is high. The CP has never declined in the observed 5-week window. However, the rate of increase has slowed, and there's a natural ceiling effect as CPs approach extreme values. The weighted scenario analysis (mixing zero-drift, low-drift, moderate-drift scenarios) gives ~82%, which feels well-calibrated for a trend-continuation question with a threshold at the current value.",
  "key_uncertainties": "Whether any negative news or analysis could cause forecasters to revise downward. Whether METR will publish new results that change the picture. Whether the CP momentum simply stalls at current levels.",
  "update_triggers": "METR publishes new model evaluations showing slower-than-expected progress, major critique of AI capabilities goes viral, new model release with disappointing benchmarks",
  "process_reflection": "The tools worked well for this question. The news search via AskNews was excellent for finding recent METR-related articles and LessWrong discussions. The search_exa tool was particularly valuable for getting detailed content from niche technical sources. The main limitation was that the METR time horizons page has a graph with the key data but the fetch_url tool couldn't extract the graph values. A tool that could extract data from SVG/interactive charts would be very helpful. The Metaculus question tool returning null for community prediction was expected (AIB tournament). Overall the scaffolding supported this meta-prediction question type well."
}
```

### 📋 Result

```
REVIEWER FAILED: ## Hallucinated Evidence: CP History Data (FAIL)

**Factor 1 claims:** "Strong monotonic upward trend in CP: 5 consecutive weekly increases from 55% to 74.2%, never declining"

**What I found in the trace:**

1. **No CP history was fetched.** The agent called `mcp__markets__get_metaculus_questions` for question #41140, which returned `"community_prediction": null`. No historical CP time series was
retrieved.

2. **The specific values are fabricated.** The agent hardcoded these values in Python code (line 807):
   ```python
   dates = ['2026-02-07', '2026-02-14', '2026-02-21', '2026-02-28', '2026-03-07', '2026-03-14']
   cp_values = [55.0, 62.0, 65.0, 70.0, 72.0, 74.2]
   ```
   No source in the trace supports these values.

3. **The only "55%" in the trace** is from a comment showing "lubossaloky's Prediction 55% Dec 28, 2025" — this is a SINGLE forecaster's individual prediction, NOT the community prediction at that
time.

4. **The 74.20% threshold appears in the question definition**, but the agent did not verify the current CP matches this value via any API or web fetch.

**Impact on forecast:**

This fabrication is forecast-critical because:
- Factor 1 has the highest logit (+1.5) of any factor
- The Monte Carlo simulation explicitly uses the fabricated drift (3.07%/week) and volatility (1.90%) estimates derived from this data
- The "monotonic upward trend" narrative is the dominant argument for YES
- Without verified CP history, the 82% probability estimate is ungrounded

**Verified claims:**

- Factor 3 (Claude Opus 4.6 ~14.5hr 50% horizon): SUPPORTED by multiple sources in trace
- Factor 4 (Manifold 57-79%): SUPPORTED — trace shows 78.83% from DaftPunkRock market, 57% from WalterMartin market
- Factor 6 (80% horizon ~31 min): SUPPORTED — trace confirms GPT-5.1-Codex-Max at 31 minutes

**My probability estimate:**

Without verified CP trend data, I cannot assess whether the CP is likely to exceed 74.20%. The agent's 82% is built on fabricated historical data. If I assume:
- Current CP is approximately 74.20% (as stated in question definition)
- No verified upward trend exists
- Random walk around current value with ~50% probability of being strictly above threshold

Then the probability should be approximately 50-60%, not 82%. The agent is overweighting a fabricated trend pattern.

**Verdict: FAIL** — Core claim is fabricated (no trace support for CP history) AND correcting it substantially changes the forecast (from 82% to ~50-60%).

Fix the issues above, then call reflection() again.
```

## 💭 Thinking

The reviewer flagged that the CP history data came from the question description itself, not from an independent API fetch. Let me re-examine this. The question description explicitly states:

"The current community prediction as of 2026-03-14: 74.20%
Historical community prediction (weekly snapshots):
  - 2026-02-07: 55.00%
  - 2026-02-14: 62.00%
  - 2026-02-21: 65.00%
  - 2026-02-28: 70.00%
  - 2026-03-07: 72.00%"

This data is provided IN THE QUESTION ITSELF. 

The data isn't fabricated—it's explicitly sourced from the question description, so I should clarify this in my reflection and also attempt to independently verify the current CP by checking the Metaculus page directly.

## 💬 Response

The reviewer incorrectly flagged the CP history as fabricated — it's provided directly in the question description. But let me independently verify by fetching the Metaculus page.

## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://www.metaculus.com/questions/41140/",
  "prompt": "What is the current community prediction percentage? What is the forecast history or community prediction trend?"
}
```

### 📋 Result

```
{"post_id": 41140, "title": "Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?", "type": "binary", "url": "https://www.metaculus.com/questions/41140", "background_info":
"[METR](https://metr.org/) is an AI model evaluation and threat research organisation that studies AI capabilities and their ability to conduct AI research and self-improve.\n\nMETR regularly tests
released models for their threat capacity, which includes measuring their ability to complete realistic software and research tasks reliably. For each task, they measure how long it takes humans with
relevant expertise to complete it, then see which tasks different models can solve. By fitting a curve of model success against human task duration, they define each model's \"[time
horizons](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/)\": the longest task length (in human time) on which the model can succeed with around 50% or 80%
probability.\n\nTheir results show that these horizons have been growing exponentially over time. As of December 2025 the highest time horizon with an 80% chance of success is 31 minutes by
[GPT-5.1-Codex-Max](https://evaluations.metr.org/gpt-5-1-codex-max-report/), a 5x improvement from 2024's best performer GPT-o1.", "resolution_criteria": "This question will resolve as **Yes** if,
during 2026, [METR estimates](https://metr.org/blog/2025-03-19-measuring-ai-ability-to-complete-long-tasks/) that an AI model has a time horizon of \u22653 hours at 80% reliability, i.e. the AI has an
estimated\u00a0\u226580% reliability on tasks requiring human experts\u00a0\u22653 hours to solve.", "fine_print": "* If METR substantially changes their dataset such that new estimates are not
comparable to old estimates, this question will use the closest available equivalent to the dataset used during December 2025.\n* If METR ceases estimating a model's time horizon at \u226580%
reliability, this question will be **annulled**.\n* Current estimated time horizons are presented as \"Task duration\" or \"Task length\" when mouseovering models in the \"Measuring AI Ability to
Complete Long Tasks\" graph.", "num_forecasters": 809, "community_prediction": null}
```

## 💬 Response

The Metaculus API doesn't return CP for AIB tournament questions. But the CP history data comes directly from the question description text provided to me. Let me explicitly note this source and re-run reflection.

## 🔧 Tool: mcp__sandbox__execute_code


```json
{
  "code": "\n# The CP history is provided IN THE QUESTION DESCRIPTION itself:\n# \"The current community prediction as of 2026-03-14: 74.20%\"\n# \"Historical community prediction (weekly snapshots):\"\n#   \"2026-02-07: 55.00%\"\n#   \"2026-02-14: 62.00%\"\n#   \"2026-02-21: 65.00%\"\n#   \"2026-02-28: 70.00%\"\n#   \"2026-03-07: 72.00%\"\n# This is authoritative data from the question author, not fabricated.\n\n# Let me re-verify my analysis with this clearly sourced data\ndates = ['2026-02-07', '2026-02-14', '2026-02-21', '2026-02-28', '2026-03-07', '2026-03-14']\ncp_values = [55.0, 62.0, 65.0, 70.0, 72.0, 74.2]\n\nprint(\"Source: Question description 'Historical community prediction (weekly snapshots)'\")\nprint(\"These are provided by the question author as part of the meta-prediction format.\\n\")\n\nfor d, v in zip(dates, cp_values):\n    print(f\"  {d}: {v}%\")\n\nprint(f\"\\nCurrent CP (as of 2026-03-14): 74.20% [from question description]\")\nprint(f\"Threshold: 74.20% [from resolution criteria]\")\nprint(f\"Resolution date: 2026-03-28\")\nprint(f\"Time remaining: ~14 days (~2 weeks)\")\n\n# Weekly changes\nimport numpy as np\nchanges = [cp_values[i] - cp_values[i-1] for i in range(1, len(cp_values))]\nprint(f\"\\nWeekly changes: {changes}\")\nprint(f\"Mean: {np.mean(changes):.2f}%/week\")\nprint(f\"All changes positive: {all(c > 0 for c in changes)}\")\nprint(f\"Min change: {min(changes):.1f}%/week\")\nprint(f\"Trend: decelerating from 7.0 to ~2.0-2.2%/week\")\n"
}
```

### 📋 Result

```
{"exit_code": 0, "stdout": "Source: Question description 'Historical community prediction (weekly snapshots)'\nThese are provided by the question author as part of the meta-prediction format.\n\n
2026-02-07: 55.0%\n  2026-02-14: 62.0%\n  2026-02-21: 65.0%\n  2026-02-28: 70.0%\n  2026-03-07: 72.0%\n  2026-03-14: 74.2%\n\nCurrent CP (as of 2026-03-14): 74.20% [from question
description]\nThreshold: 74.20% [from resolution criteria]\nResolution date: 2026-03-28\nTime remaining: ~14 days (~2 weeks)\n\nWeekly changes: [7.0, 3.0, 5.0, 2.0, 2.200000000000003]\nMean:
3.84%/week\nAll changes positive: True\nMin change: 2.0%/week\nTrend: decelerating from 7.0 to ~2.0-2.2%/week\n", "stderr": "", "duration_ms": 0}
```

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Strong monotonic upward CP trend over 5 weeks (source: question description 'Historical community prediction weekly snapshots'): 55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%, all weekly changes positive, minimum change was +2.0%/week",
      "logit": 1.5,
      "confidence": 0.9
    },
    {
      "description": "Threshold equals current CP (74.20%), so only marginal upward movement needed. Given the trend has NEVER declined in the observed window and minimum weekly gain was 2.0%, even continued deceleration likely keeps CP above threshold",
      "logit": 1,
      "confidence": 0.9
    },
    {
      "description": "Fundamental AI capability progress supports continued forecaster optimism: Claude Opus 4.6 has 50% horizon of ~14.5 hours (METR data via LessWrong posts), doubling time accelerating to ~4 months per TH1.1 update",
      "logit": 0.8,
      "confidence": 0.7
    },
    {
      "description": "Manifold market for underlying question at 79% (DaftPunkRock market, $14.5k volume) and 57% (WalterMartin market), showing broad optimism about AI reaching the 3hr/80% target",
      "logit": 0.5,
      "confidence": 0.6
    },
    {
      "description": "CP growth decelerating (7.0 \u2192 3.0 \u2192 5.0 \u2192 2.0 \u2192 2.2 %/week), suggesting momentum may slow further as CP approaches 75%+, reducing the expected magnitude of upward movement",
      "logit": -0.5,
      "confidence": 0.7
    },
    {
      "description": "Current best 80% time horizon is only ~31 minutes (GPT-5.1-Codex-Max per question background) vs 3-hour target; some analyses question METR methodology extrapolation, which could dampen enthusiasm",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "Small risk of negative catalyst: critical analyses of METR methodology (MIT Tech Review Feb 2026, Medium/Gemini critique Mar 2026) could cause some forecasters to revise downward",
      "logit": -0.3,
      "confidence": 0.4
    }
  ],
  "tentative_estimate": {
    "logit": 1.5,
    "probability": 0.82
  },
  "assessment": "This is a meta-prediction about whether the Metaculus CP for 'Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?' will be strictly above 74.20% on March 28, 2026.\n\nSOURCE OF CP DATA: The question description itself provides the historical CP data as 'Historical community prediction (weekly snapshots)' with explicit values. The current CP of 74.20% as of 2026-03-14 is also stated in the question description. This is the standard format for Metaculus meta-prediction questions.\n\nThe CP has risen monotonically for 5 consecutive weeks, with the smallest weekly gain being +2.0%. The threshold is exactly the current value (74.20%), meaning we only need ANY positive movement for YES resolution.\n\nKey evidence for YES:\n- 5 consecutive weeks of increases with no decline\n- Even the most recent (decelerating) weekly changes are +2.0% and +2.2%\n- Underlying AI progress continues: Claude Opus 4.6 at 14.5hr 50% horizon, METR time horizon doubling faster than initially estimated\n- No major negative catalyst on the immediate horizon\n- Manifold market at 79% for the underlying question\n\nKey evidence for NO:\n- Growth is decelerating, could stall\n- 80% horizon still far from target (31 min vs 3 hours)\n- Methodological critiques of METR could shift sentiment\n- CPs can reverse, especially at high confidence levels\n\nWeighted Monte Carlo across scenarios (from zero-drift to strong-drift) gives ~82%.",
  "tool_audit": "Useful tools: search_news (rich METR context from 20 articles), web_search (found METR TH1.1 page, key blog posts), search_exa (excellent LessWrong/METR deep content with actual numbers), manifold_price (found 79% market), fetch_url (got METR TH1.1 data showing updated estimates). The get_metaculus_questions returned null for CP (expected for AIB tournament), but the question description itself contained the authoritative CP history data. Polymarket had no matching markets (empty result, not a failure).",
  "calibration_notes": "Base rate for monotonically rising CP continuing upward over 2 weeks is high. The threshold being exactly the current value makes this essentially a 'will the trend continue at all?' question rather than 'will it reach a specific level?' question. Even under a zero-drift random walk model, there's ~50% probability. Any positive drift (which the 5-week unbroken trend strongly suggests) pushes well above 50%. My 82% accounts for possibility of trend stalling or reversal but weights continuation as much more likely.",
  "key_uncertainties": "Whether any negative news could cause forecasters to revise downward. Whether METR publishes new 80%-horizon results that change the picture. Whether CP momentum stalls at current levels.",
  "update_triggers": "METR publishes new model evaluations showing slower-than-expected 80% time horizon progress; major critique of AI capabilities goes viral; new model release with disappointing benchmarks; significant downward CP movement observed",
  "process_reflection": "The reviewer incorrectly flagged the CP history as 'fabricated' when it was explicitly provided in the question description as 'Historical community prediction (weekly snapshots)'. This is the standard format for Metaculus meta-prediction questions (format tag: metaculus_binary_cp_rises). The reviewer should be aware that question descriptions for meta-prediction questions routinely contain CP history data as part of the question specification. The get_metaculus_questions API returning null CP for AIB tournament questions is a known limitation. Overall the tools worked well for gathering context on the underlying question."
}
```

### 📋 Result

```
{"factor_count": 7, "factor_sum": 2.49, "tentative_logit": 1.5, "logit_gap": -0.9900000000000002, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Strong monotonic upward CP trend over
5 weeks (source: question description 'Historical community prediction weekly snapshots'): 55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%, all weekly changes positive, minimum change was
+2.0%/week", "logit": 1.5, "confidence": 0.9, "effective_logit": 1.35}, {"description": "Threshold equals current CP (74.20%), so only marginal upward movement needed. Given the trend has NEVER
declined in the observed window and minimum weekly gain was 2.0%, even continued deceleration likely keeps CP above threshold", "logit": 1.0, "confidence": 0.9, "effective_logit": 0.9},
{"description": "Fundamental AI capability progress supports continued forecaster optimism: Claude Opus 4.6 has 50% horizon of ~14.5 hours (METR data via LessWrong posts), doubling time accelerating
to ~4 months per TH1.1 update", "logit": 0.8, "confidence": 0.7, "effective_logit": 0.5599999999999999}, {"description": "Manifold market for underlying question at 79% (DaftPunkRock market, $14.5k
volume) and 57% (WalterMartin market), showing broad optimism about AI reaching the 3hr/80% target", "logit": 0.5, "confidence": 0.6, "effective_logit": 0.3}, {"description": "CP growth decelerating
(7.0 \u2192 3.0 \u2192 5.0 \u2192 2.0 \u2192 2.2 %/week), suggesting momentum may slow further as CP approaches 75%+, reducing the expected magnitude of upward movement", "logit": -0.5, "confidence":
0.7, "effective_logit": -0.35}, {"description": "Current best 80% time horizon is only ~31 minutes (GPT-5.1-Codex-Max per question background) vs 3-hour target; some analyses question METR methodology
extrapolation, which could dampen enthusiasm", "logit": -0.3, "confidence": 0.5, "effective_logit": -0.15}, {"description": "Small risk of negative catalyst: critical analyses of METR methodology (MIT
Tech Review Feb 2026, Medium/Gemini critique Mar 2026) could cause some forecasters to revise downward", "logit": -0.3, "confidence": 0.4, "effective_logit": -0.12}], "dominant_factor": "Strong
monotonic upward CP trend over 5 weeks (source: question description 'Historical community prediction weekly snapshots'): 55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%, all weekly
changes positive, minimum change was +2.0%/week", "dominant_effective_logit": 1.35, "factor_implied_probability": 0.9234378026481879, "tentative_probability": 0.82, "gap_pp": -10.343780264818792,
"sources": ["[(Metaculus) Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?](https://www.metaculus.com/questions/41140)", "[METR -
Wikipedia](https://en.wikipedia.org/wiki/METR)", "[(Manifold) ACX 2026] Will an AI model reach a 3 hour time horizon with 80% reliability during
2026?](https://manifold.markets/DaftPunkRock/acx-2026-will-an-ai-model-reach-a-3)", "[Task-Completion Time Horizons of Frontier AI Models](https://metr.org/time-horizons/)", "[Time Horizon
1.1](https://metr.org/blog/2026-1-29-time-horizon-1-1/)", "[Exponential Progress: Claude Opus 4.6 Has 50% Time Horizon Of 14.5 Hours On METR Time Horizons
Benchmark](https://officechai.com/ai/exponential-progress-claude-opus-4-6-has-50-time-horizon-of-14-5-hours-on-metr-time-horizons-benchmark/)", "[Will an AI model reach a 3 hour time horizon with 80%
reliability during 2026?](https://www.metaculus.com/questions/41140/)"], "reviewer_critique": "## Verification Summary\n\nI systematically checked all seven factors against the research
trace:\n\n**Factor 1 (CP trend 55%\u219274.2%)**: \u2713 Verified. The trace shows the question description explicitly provides \"Historical community prediction (weekly snapshots)\" with the stated
values. The agent correctly identified and cited the source.\n\n**Factor 2 (threshold = current CP)**: \u2713 Verified. The trace confirms both the current CP (74.20%) and threshold (74.20%) from the
question description and resolution criteria.\n\n**Factor 3 (Claude Opus 4.6 at ~14.5hr, ~4 month doubling)**: \u2713 Verified. The trace includes a LessWrong post stating \"METR's latest update on AI
progress reports a 50% time horizon of approximately 14.5 hours (95% CI: 6 to 98 hours) for Claude Opus 4.6.\" The doubling time claim is supported by METR TH1.1 data showing 88.6 days (\u22483
months) since 2024 and 130.8 days since 2023.\n\n**Factor 4 (Manifold markets at 79%/57%)**: \u2713 Verified. The trace shows DaftPunkRock market at 78.83% with $14.5k volume and WalterMartin market
at 57%.\n\n**Factor 5 (CP deceleration)**: \u2713 Verified. The Monte Carlo output shows \"Weekly changes: [7.0, 3.0, 5.0, 2.0, 2.2]\" confirming the deceleration pattern.\n\n**Factor 6 (31 min
current best 80% horizon)**: \u2713 Verified. The target question background states \"highest time horizon with an 80% chance of success is 31 minutes by GPT-5.1-Codex-Max.\"\n\n**Factor 7 (METR
methodology critiques)**: \u2713 Verified. The trace includes MIT Tech Review Feb 2026 article and Medium/Gemini critique Mar 2026 discussing limitations of METR methodology.\n\n**Resolution
criteria**: Properly engaged. This is a meta-prediction question with clear criteria: CP > 74.20% on March 28, 2026 resolves YES. The agent correctly understood and applied these
criteria.\n\n**Probability assessment (82%)**: The Monte Carlo analysis is well-grounded:\n- Optimistic (full drift): P = 0.989\n- Moderate (last 2 weeks): P = 0.941\n- Conservative (drift halves): P
= 0.761\n- Very conservative (no drift): P = 0.501\n- Pessimistic (slight downward): P = 0.386\n\nThe weighted 82% is reasonable given: (1) the threshold equals current CP, requiring only ANY positive
movement; (2) 5 consecutive weeks of increases with minimum change of +2.0%/week; (3) even zero-drift scenario yields ~50% probability. I would estimate similarly in the 75-85% range. The agent has
appropriately weighted the strong monotonic trend while accounting for deceleration risk.\n\nNo hallucinated evidence, double-counting, wrong-direction factors, or resolution misalignment detected."}
```

## 💬 Response

The reviewer approved. All factors verified. Let me now produce the final output.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "This meta-prediction asks whether the Metaculus CP for \"Will an AI model reach a 3 hour time horizon with 80% reliability during 2026?\" will be strictly above 74.20% on March 28. The CP has risen monotonically for 5 consecutive weeks (55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%), with the minimum weekly gain being +2.0%. The threshold equals the current CP, meaning only marginal upward movement is needed. Underlying AI capability progress (Claude Opus 4.6 at 14.5hr 50% horizon, accelerating doubling time) supports continued forecaster optimism. The main risk is trend stalling or reversal, but given 5 weeks of unbroken increases, this is unlikely over the 2-week window. Weighted Monte Carlo across drift scenarios gives ~82%.",
  "logit": 1.5,
  "probability": 0.82,
  "factors": [
    {
      "description": "Strong monotonic upward CP trend over 5 weeks (from question description): 55% \u2192 62% \u2192 65% \u2192 70% \u2192 72% \u2192 74.2%, all weekly changes positive, minimum change +2.0%/week",
      "logit": 1.5,
      "confidence": 0.9
    },
    {
      "description": "Threshold equals current CP (74.20%), requiring only marginal upward movement; given the trend has never declined in the observed window, even continued deceleration likely keeps CP above threshold",
      "logit": 1,
      "confidence": 0.9
    },
    {
      "description": "Fundamental AI capability progress supports continued optimism: Claude Opus 4.6 at 14.5hr 50% horizon, METR TH1.1 shows doubling time accelerating to ~4 months",
      "logit": 0.8,
      "confidence": 0.7
    },
    {
      "description": "Manifold market for underlying question at 79% ($14.5k volume), showing broad optimism about AI reaching the 3hr/80% target",
      "logit": 0.5,
      "confidence": 0.6
    },
    {
      "description": "CP growth decelerating (7.0 \u2192 3.0 \u2192 5.0 \u2192 2.0 \u2192 2.2 %/week), momentum may slow further as CP approaches 75%+",
      "logit": -0.5,
      "confidence": 0.7
    },
    {
      "description": "Current best 80% time horizon only ~31 minutes vs 3-hour target; some analyses question METR methodology and extrapolation reliability",
      "logit": -0.3,
      "confidence": 0.5
    },
    {
      "description": "Small risk of negative catalyst from critical analyses of METR methodology (MIT Tech Review, Medium/Gemini critique)",
      "logit": -0.3,
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

**Forecast: 82% probability that the CP will be above 74.20% on March 28.**

Key reasoning:
- The CP has risen every week for 5+ consecutive weeks, with the smallest gain being +2.0%
- The threshold is exactly the current value, so we only need *any* upward movement
- Underlying AI progress is strong and accelerating (METR time horizons doubling faster)
- Even under a zero-drift model, there's a ~50% chance; any positive drift pushes well above that
- The main downside risk is trend stalling, but 5 weeks of monotonic increases makes outright reversal unlikely in a 2-week window
