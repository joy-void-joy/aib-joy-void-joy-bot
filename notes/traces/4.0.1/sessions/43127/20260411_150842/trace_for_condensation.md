# Reasoning Log: How many problems solved by AI will the official FrontierMath Open Problems index show on May 1, 2026?

*Generated: 2026-04-11T15:15:37.201115+00:00*


## 💭 Thinking

Let me analyze this forecasting question about the FrontierMath Open Problems index. I need to understand:

1. What the current state is (1 problem solved as of April 4, 2026)
2. What could change by May 1, 2026
3. The likelihood of additional problems being solved

Let me start by researching the current state of FrontierMath Open Problems.

## 🔧 Tool: mcp__markets__get_metaculus_questions


```json
{
  "post_id_list": [
    43127
  ]
}
```

### 📋 Result

```
{"post_id": 43127, "title": "How many problems solved by AI will the official FrontierMath Open Problems index show on May 1, 2026?", "type": "multiple_choice", "url":
"https://www.metaculus.com/questions/43127", "background_info": "Epoch\u2019s Open Problems index describes these as unsolved mathematics problems that have resisted serious attempts by professional
mathematicians, and says AI solutions would meaningfully advance human mathematical knowledge. As of April 4, 2026, the official index shows 1/4 solved in \u201cModerately interesting\u201d and 0
solved in \u201cSolid result,\u201d \u201cMajor advance,\u201d and \u201cBreakthrough,\u201d so the current counted total is 1. Another official problem page (Small Diophantine) reports partial
progress but not a full solution, which makes a second counted solve a live near-term
milestone.\n\n`{\"format\":\"bot_tournament_question\",\"info\":{\"hash_id\":\"a0680374ed4885be\",\"sheet_id\":538.0}}`", "resolution_criteria": "This question resolves as the total number of  AI-
solved problems shown by the official FrontierMath Open Problems index shows on May 1, 2026. https://epoch.ai/frontiermath/open-problems/", "fine_print": "", "num_forecasters": 11,
"community_prediction": null, "options": ["1 or fewer", "2", "Greater than 2"]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


```json
{
  "url": "https://epoch.ai/frontiermath/open-problems/",
  "prompt": "How many problems are solved? What is the current status of each open problem? List all problems and their solve status."
}
```

### 📋 Result

```
{"url": "https://epoch.ai/frontiermath/open-problems/", "content": "Based on the provided text content:\n\n**Problems Solved:** The text mentions that **1 problem was removed** from the benchmark on
2026-03-05, but this was not because it was solved by AI. Rather, it was removed because any solution would not meet their criteria of being a publishable result.\n\n**Current Status:** The text does
not provide:\n- The total number of problems in the collection\n- Individual problem names or identifiers\n- Solve status for specific problems\n- Whether any problems have been genuinely
solved\n\nThe content only describes this as \"a collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians\" and notes that one problem was removed
for quality threshold reasons, not because it was solved.\n\n**Relevant links:**\n- The text references a problem page with \"more info on an AI-generated solution and subsequent human elaboration,\"
but the specific URL is not provided in the excerpt\n- The base URL is https://epoch.ai/frontiermath/open-problems/ but this appears to be the page you already provided\n\nTo get the actual list of
problems and their current solve status, you would need to access the full webpage or additional pages on the Epoch AI FrontierMath site.", "title": "FrontierMath: Open Problems - Unsolved
Mathematical Challenges"}
```

```json
{
  "query": "FrontierMath Open Problems AI solved 2026"
}
```

### 📋 Result

```
{"query": "FrontierMath Open Problems AI solved 2026", "results": [{"title": "FrontierMath: Open Problems - Unsolved Mathematical Challenges | Epoch AI", "url": "https://epoch.ai/frontiermath/open-
problems/", "snippet": "A collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would meaningfully advance the state of human
mathematical knowledge.\n2026-03-05: We removed one problem from the benchmark, as we have determined that any solution would not meet our bar of being a publishable result in its own right. The
problem page remains up: see it for more info on an AI-generated solution and subsequent human elaboration.", "api_data": null, "hint": null}, {"title": "Introducing FrontierMath: Open Problems -
Epoch AI - Substack", "url": "https://epochai.substack.com/p/introducing-frontiermath-open-problems", "snippet": "Introducing FrontierMath: Open Problems\nBenchmarking AI on unsolved research problems
that have eluded mathematicians\nThis work was supported by a grant from Schmidt Sciences.\nAI math capabilities have come far and fast. In mid-2024, [high school
math](https://epoch.ai/benchmarks/math-level-5) was still a challenge. By the end of 2025, AI systems were solving [extremely hard problems](https://epoch.ai/frontiermath/about) designed to be
solvable only by top human experts. As we write this, it see", "api_data": null, "hint": null}, {"title": "Share of FrontierMath problems solved correctly by AI models - Our World in Data", "url":
"https://ourworldindata.org/grapher/ai-frontiermath-over-time", "snippet": "Share of FrontierMath problems solved correctly by AI models\n![](/grapher/ai-frontiermath-over-time.png)\nWhat you should
know about this indicator\n- This indicator shows the share of FrontierMath problems that AI models solve correctly, based on Epoch AI's evaluation.\n- FrontierMath is a set of 350 original math
problems written by experts, covering many areas of advanced mathematics. Many problems are difficult enough that human specialists might need hours or days to solve them.\n- The benchmar",
"api_data": null, "hint": null}, {"title": "Benchmarking AI on unsolved math problems | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/about/", "snippet": "FrontierMath: Open
Problems\nThis work was supported by a grant from Schmidt Sciences.\nAI math capabilities have come far and fast. In mid-2024, [high school math](https://epoch.ai/benchmarks/math-level-5) was still a
challenge. By the end of 2025, AI systems were solving [extremely hard problems](https://epoch.ai/frontiermath/tiers-1-4/about) designed to be solvable only by top human experts. As we write this, it
seems likely that AI systems will soon be able to solve problems that no human has ", "api_data": null, "hint": null}, {"title": "A Ramsey-style Problem on Hypergraphs | Epoch AI", "url":
"https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs/", "snippet": "Solution update\nThis problem has been solved! A solution was first elicited by Kevin Barreto and Liam Price, using
GPT-5.4 Pro. This solution was confirmed by problem contributor Will Brian, and will be written up for publication. A full transcript of the original conversation with GPT-5.4 Pro can be found
[here](https://epoch.ai/files/open-problems/gpt-5-4-pro-hypergraph-ramsey.txt) and GPT-5.4 Pro\u2019s write-up from the end of that transcript can be found [here](https://epoch.ai/files/open-proble",
"api_data": null, "hint": null}, {"title": "How many FrontierMath Open Problems solved in 2026? | Manifold", "url": "https://manifold.markets/bh/how-many-frontiermath-open-problems", "snippet": "How
many FrontierMath Open Problems solved in 2026?\n9\n\u1e40400\u1e40282Dec
31\n15%\n1\n15%\n2\n16%\n3\n14%\n4\n9%\n5\n3%\n6\n3%\n7\n3%\n8\n3%\n9\n3%\n10\n3%\n11\n3%\n12\n3%\n13\n3%\n14\n3%\n15\n3%\nResolves to the number of problems displayed as solved at
[https://epoch.ai/frontiermath/open-problems](https://epoch.ai/frontiermath/open-problems)\nI will not trade in this market.\nSee also this market for EOY2027: [https://manifold.markets/bh/how-many-
frontiermath-open-problems-SzcLglOOOs?r=Ymg](https://manifold.markets/bh/how-many-frontie", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."},
{"title": "'Breakthrough' Frontier Math Open Problem solved before 2028 | Manifold", "url": "https://manifold.markets/Jolliest/breakthrough-frontier-math-open-pro", "snippet": "'Breakthrough' Frontier
Math Open Problem solved before 2028\n7\n\u1e40100\u1e401432028\n54%\nchance\n1H\n6H\n1D\n1W\n1M\nALL\nContext: [https://epoch.ai/frontiermath/open-problems](https://epoch.ai/frontiermath/open-
problems)\nThere are currently 4 categories of Frontier Math Open Problems: Moderately Interesting, Solid Result, Major Advance, Breakthrough. This market will resolve yes if 1 of the 3 breakthrough
problems are solved by AI.\nIf more 'Breakthrough' questions are added, they are also considered for the re", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for
historical prices."}, {"title": "Epoch AI on X: \"Can AI solve math research problems that have eluded human mathematicians? Our new benchmark, FrontierMath: Open Problems, is designed to help find
out. AI hasn\u2019t solved any of these yet, but the game is young! https://t.co/6RbPXT0gzQ\" / X", "url": "https://x.com/EpochAIResearch/status/2016188014540816879", "snippet": "We\u2019ve detected
that JavaScript is disabled in this browser. Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp
Center\nTerms of Service Privacy Policy Cookie Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "From Erd\u0151s to Axiom: Open Problems AI Has Actually
Solved", "url": "https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/", "snippet": "AI has moved beyond acing math benchmarks and into something
more important: contributing to real open problems. Here\u2019s the verified list so far, the credible claims still under review, and why this changes how math research may get done.\nThere\u2019s a
new genre of AI headline that would\u2019ve sounded absurd 18 months ago: AI solved an open math problem.\nNow we\u2019ve got enough examples that the harder question isn\u2019t whether it\u2019s
happening. It\u2019s how to separate the real thing from the hype. Some of the sp", "api_data": null, "hint": null}, {"title": "AI Math Benchmarks: AI's Growing Capabilities", "url":
"https://spectrum.ieee.org/ai-math-benchmarks", "snippet": "[Mathematics](https://spectrum.ieee.org/tag/mathematics) is often regarded as the ideal domain for measuring AI progress effectively.
Math\u2019s step-by-step logic is easy to track, and its definitive, automatically verifiable answers remove any human or subjective factors. But AI systems are improving at such a pace that math
[benchmarks are struggling to keep up](https://spectrum.ieee.org/melanie-mitchell).\nWay back in November 2024, nonprofit research organization Epoch AI quietly released [Front", "api_data": null,
"hint": null}]}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__markets__manifold_price


```json
{
  "url": "https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs/",
  "prompt": "When was this problem solved? What is the current status? Is it marked as solved?"
}
```

### 📋 Result

```
{"url": "https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs/", "content": "Based on the content provided:\n\n**When was this problem solved?**\nThe problem was first solved by Kevin
Barreto and Liam Price using GPT-5.4 Pro. The exact date is not specified in the text.\n\n**Current status:**\n- The solution has been confirmed by problem contributor Will Brian\n- Brian plans to
write up the solution for publication, possibly including follow-on work\n- Barreto and Price have the option of being coauthors on any resulting papers\n- Multiple other AI models (Opus 4.6, Gemini
3.1 Pro, GPT-5.4 xhigh) have subsequently also solved the problem using a general testing scaffold\n\n**Is it marked as solved?**\nYes, the page has a \"Solution update\" section at the top explicitly
stating \"This problem has been solved!\"\n\n**Relevant links:**\n- [Full transcript of original conversation with GPT-5.4 Pro](https://epoch.ai/files/open-problems/gpt-5-4-pro-hypergraph-
ramsey.txt)\n- [GPT-5.4 Pro's write-up of the solution](https://epoch.ai/files/open-problems/hypergraph-ramsey-gpt-5-4-pro-solution.pdf)\n- [Opus 4.6 (max) solution
transcript](https://epoch.ai/files/open-problems/hypergraph_partition_ramsey-transcript-opus-4-6-max.txt)\n- [Gemini 3.1 Pro solution transcript](https://epoch.ai/files/open-
problems/hypergraph_partition_ramsey-transcript-gemini-3-1-pro.txt)\n- [GPT-5.4 (xhigh) solution transcript](https://epoch.ai/files/open-problems/hypergraph_partition_ramsey-transcript-
gpt-5-4-xhigh.txt)", "title": "A Ramsey-style Problem on Hypergraphs"}
```

```json
{
  "url": "https://epochai.substack.com/p/introducing-frontiermath-open-problems",
  "prompt": "How many open problems are there? What categories? What is the current status of each problem? When was this published?"
}
```

### 📋 Result

```
{"url": "https://epochai.substack.com/p/introducing-frontiermath-open-problems", "content": "Based on the content:\n\n**Number of problems:** 14 problems in the pilot release\n\n**Categories:** The
problems cover various mathematical topic areas, with a tilt toward:\n- Combinatorics\n- Number theory\nOther areas are mentioned but not specified. The goal is to maintain diversity as the benchmark
expands.\n\n**Current status:** At the time of release, none of these 14 problems have been solved by humans or AI systems. The content notes that GPT-5.2 Pro and Gemini 3 Deep Think were tested via
simple prompting in web apps but showed little promise on the actual open problems (though they could solve \"warm-up\" variants where solutions are known).\n\n**Publication date:** Not explicitly
stated in the content. The text references \"mid-2024\" and \"end of 2025\" as past events and says \"As we write this\" when discussing current capabilities, but no specific publication date is
given.\n\n**Relevant links:**\n- [FrontierMath: Open Problems website](https://epoch.ai/frontiermath/open-problems/about)\n- [Problem proposal
form](https://docs.google.com/forms/d/e/1FAIpQLSckGHMY4ofgKfvf39Ue8fDZAbXJqN9pTcf5oLP3f3y-chE0Bg/viewform)\n- [Inverse Galois problem example](https://epoch.ai/frontiermath/open-problems/inverse-
galois)\n- [Ramsey book graphs problem example](https://epoch.ai/frontiermath/open-problems/ramsey-book-graphs)\n- [FrontierMath benchmarks](https://epoch.ai/benchmarks/math-level-5)\n- [AI
contributions to Erd\u0151s problems](https://github.com/teorth/erdosproblems/wiki/AI-contributions-to-Erd%C5%91s-problems)", "title": "Introducing FrontierMath: Open Problems"}
```

```json
{
  "query": "FrontierMath \"open problems\" \"Small Diophantine\" solved partial progress April 2026"
}
```

### 📋 Result

```
{"query": "FrontierMath \"open problems\" \"Small Diophantine\" solved partial progress April 2026", "results": [{"title": "FrontierMath: Open Problems - Unsolved Mathematical Challenges | Epoch AI",
"url": "https://epoch.ai/frontiermath/open-problems/", "snippet": "A collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would
meaningfully advance the state of human mathematical knowledge.\n2026-03-05: We removed one problem from the benchmark, as we have determined that any solution would not meet our bar of being a
publishable result in its own right. The problem page remains up: see it for more info on an AI-generated solution and subsequent human elaboration.", "api_data": null, "hint": null}, {"title":
"Finiteness Problem for Diophantine Equations | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/small-diophantine", "snippet": "About the problem\nDefine a heuristic \u201csize\u201d of
a Diophantine equation by substituting \\(2\\) for all variables and absolute values of coefficients for all coefficients. For instance \\(x^2 - 2y^2 -1\\) has size \\(13\\).\nThe finiteness problem
for a Diophantine equation asks whether the equation has infinitely many solutions. This problem is about the nine equations with size \\(\\leq 24\\) where the finiteness problem is open. Numerical
evidence suggests that these equations all have infinitely many so", "api_data": null, "hint": null}, {"title": "Share of FrontierMath problems solved correctly by AI models - Our World in Data",
"url": "https://ourworldindata.org/grapher/ai-frontiermath-over-time", "snippet": "Share of FrontierMath problems solved correctly by AI models\n![](/grapher/ai-frontiermath-over-time.png)\nWhat you
should know about this indicator\n- This indicator shows the share of FrontierMath problems that AI models solve correctly, based on Epoch AI's evaluation.\n- FrontierMath is a set of 350 original
math problems written by experts, covering many areas of advanced mathematics. Many problems are difficult enough that human specialists might need hours or days to solve them.\n- The benchmar",
"api_data": null, "hint": null}, {"title": "How many FrontierMath Open Problems solved in 2026? | Manifold", "url": "https://manifold.markets/bh/how-many-frontiermath-open-problems", "snippet": "How
many FrontierMath Open Problems solved in 2026?\n9\n\u1e40400\u1e40282Dec
31\n15%\n1\n15%\n2\n16%\n3\n14%\n4\n9%\n5\n3%\n6\n3%\n7\n3%\n8\n3%\n9\n3%\n10\n3%\n11\n3%\n12\n3%\n13\n3%\n14\n3%\n15\n3%\nResolves to the number of problems displayed as solved at
[https://epoch.ai/frontiermath/open-problems](https://epoch.ai/frontiermath/open-problems)\nI will not trade in this market.\nSee also this market for EOY2027: [https://manifold.markets/bh/how-many-
frontiermath-open-problems-SzcLglOOOs?r=Ymg](https://manifold.markets/bh/how-many-frontie", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."},
{"title": "FRONTIERMATH: A BENCHMARK FOR EVALUATING ADVANCED MATHEMATICAL REASONING IN AI", "url": "https://arxiv.org/pdf/2411.04872", "snippet": "FrontierMath: A Benchmark for Evaluating Advanced
Mathematical Reasoning in AI\nAbstract\nWe introduce FrontierMath, a benchmark of hundreds of original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The
questions cover most major branches of modern mathematics\u2014from computationally intensive problems in number theory and real analysis to abstract questions in algebraic geometry and category
theory. Solving a typical problem requires multiple hours of e", "api_data": {"content": [{"type": "text", "text": "{\"paper_id\": \"2411.04872\", \"format\": \"html\", \"url\":
\"https://arxiv.org/html/2411.04872\", \"content\": \"FrontierMath: A Benchmark for Evaluating Advanced Mathematical Reasoning in AI\\nAbstract\\nWe introduce FrontierMath, a benchmark of hundreds of
original, exceptionally challenging mathematics problems crafted and vetted by expert mathematicians. The questions cover most major branches of modern mathematics\\u2014from computationally intensive
problems in number theory and real analysis to abstract questions in algebraic geometry and category theory. Solving a typical problem requires multiple hours of effort from a researcher in the
relevant branch of mathematics, and for the upper end questions, multiple days. FrontierMath uses new, unpublished problems and automated verification to reliably evaluate models while minimizing risk
of data contamination. Current state-of-the-art AI models solve under 2% of problems, revealing a vast gap between AI capabilities and the prowess of the mathematical community. As AI systems advance
toward expert-level mathematical abilities, FrontierMath offers a rigorous testbed that quantifies their progress.\\n1 Introduction\\nRecent AI systems have demonstrated remarkable proficiency in
tackling challenging mathematical tasks, from achieving olympiad-level performance in geometry [trinh2024solving] to improving upon existing research results in combinatorics [romera2024mathematical].
However, existing benchmarks face some limitations:\\nSaturation of existing benchmarks\\nCurrent standard mathematics benchmarks such as the MATH dataset [hendrycks2021measuring] and GSM8K
[cobbe2021training] primarily assess competency at the high-school and early undergraduate level. As state-of-the-art models achieve near-perfect performance on these benchmarks, we lack rigorous ways
to evaluate their capabilities in advanced mathematical domains that require deeper theoretical understanding, creative insight, and specialized expertise. Furthermore, to assess AI\\u2019s potential
contributions to mathematics research, we require benchmarks that better reflect the challenges faced by working mathematicians.\\nBenchmark contamination in training data\\nA significant challenge in
evaluating large language models (LLMs) is data contamination\\u2014the inadvertent inclusion of benchmark problems in training data. This issue leads to artificially inflated performance metrics that
mask models\\u2019 true reasoning capabilities [deng2023investigating, xu2024benchmark]. While competitions like the International Mathematics Olympiad (IMO) or American Invitational Mathematics
Examination (AIME) offer fresh test problems created after model training, making them immune to contamination, these sources provide only a small number of problems and often require substantial
manual effort to grade.\\nTo address these limitations, we introduce FrontierMath, a benchmark of original, exceptionally challenging mathematical problems created in collaboration with over 60
mathematicians from leading institutions. FrontierMath addresses data contamination concerns by featuring exclusively new, previously unpublished problems. It enables scalable evaluation through
automated verification that provides rapid, reproducible assessment. The benchmark spans the full spectrum of modern mathematics, from challenging competition-style problems to problems drawn directly
from contemporary research, covering most branches of mathematics in the 2020 Mathematics Subject Classification (MSC2020).222In particular, FrontierMath contains problems across 70% of the top-level
subjects in the MSC2020 classification excluding \\u201c00 General and overarching topics; collections\\u201d, \\u201c01 History and biography\\u201d, and \\u201c97 Mathematics education\\u201d.\\nThe
problems in FrontierMath demand deep theoretical understanding, creative insight, and specialized expertise, often requiring multiple hours of effort from expert mathematicians to solve. We provide a
set of representative example problems and their solutions (see Appendix B.3 and Figure\\u02dc1). Notably, current state-of-the-art AI models are unable to solve more than 2% of the problems in
FrontierMath, even with multiple attempts, highlighting a significant gap between human and AI capabilities in advanced mathematics (see Figure 2).\\nTo understand expert perspectives on
FrontierMath\\u2019s difficulty and relevance, we interviewed several prominent mathematicians, including Fields Medalists Terence Tao (2006), Timothy Gowers (1998), and Richard Borcherds (1998), and
IMO coach Evan Chen. They unanimously characterized the problems as exceptionally challenging, requiring deep domain expertise and significant time investment to solve. While they noted that the
requirement of numerical answers differs from typical mathematical research practice, these problems nonetheless demand substantial expertise and time even from experienced mathematicians.\\n2 Data
collection\\n2.1 The collection pipeline\\nWe developed the FrontierMath benchmark through collaboration with over 60 mathematicians from universities across more than a dozen countries. Our
contributors formed a diverse group spanning academic ranks from graduate students to faculty members. Many are distinguished participants in prestigious mathematical competitions, collectively
holding 14 IMO gold medals. One contributing mathematician also holds a Fields Medal.\\nTheir areas of expertise collectively span a vast expanse of modern mathematics\\u2014including but not limited
to algebraic geometry, number theory, point set and algebraic topology, combinatorics, category theory, representation theory, partial differential equations, probability theory, differential
geometry, logic, and theoretical computer science. Since many of our contributors are active researchers, the problems naturally incorporate sophisticated techniques and insights found in contemporary
mathematical research.\\nEach mathematician created new problems following guidelines designed to ensure clarity, verifiability, and definitive answers across various difficulty levels and
mathematical domains. Four requirements guided problem creation:\\n-\\n\\u2022\\nOriginality: While problems could build on existing mathematical ideas, they needed to do so in novel and non-obvious
ways\\u2014either through clever adaptations that substantially transform the original concepts, or through innovative combinations of multiple ideas that obscure their origins. This ensures that
solving them requires genuine mathematical insight rather than pattern matching against known problems.\\n-\\n\\u2022\\nAutomated verifiability: Problems had to possess definitive, computable answers
that could be automatically verified. To facilitate automated verification, we often structured problems to have integer solutions, which are straightforward to check programmatically. We also
included solutions that could be represented as arbitrary SymPy objects\\u2014including symbolic expressions, matrices, and more. By utilizing SymPy, we enabled a wide range of mathematical outputs to
be represented and verified programmatically, ensuring that even complex symbolic solutions could be efficiently and accurately checked. This approach allowed us to support diverse answer types while
maintaining verification standards.\\n-\\n\\u2022\\nGuessproofness: Problems were designed to avoid being susceptible to guessing; solving the problem had to be necessary to find the correct answer.
As can be seen from Figure\\u02dc1, problems often have numerical answers that are large and nonobvious, which reduces the vulnerability to guesswork. As a rule of thumb, we require that there should
not be a greater than 1% chance of guessing the correct answer without doing most of the work that one would need to do to \\u201ccorrectly\\\" find the solution. This is important to ensure that the
challenges assessed genuine mathematical understanding and reasoning.\\n-\\n\\u2022\\nComputational tractability: The solution of a computationally intensive problem must include scripts demonstrating
how to find the answer, starting only from standard knowledge of the field.333For example, if a problem requires factoring a large integer, this must be doable from a standard algorithm. These scripts
must cumulatively run less than a minute on standard hardware. This requirement ensures efficient and manageable evaluation times.\\nFor each contributed problem, mathematicians provided a detailed
solution and multiple forms of metadata. Each submission included both a verification script for automated answer checking (see Section\\u02dc2.2) and comprehensive metadata tags. These tags included
subject and technique classifications, indicating both the mathematical domains and specific methodologies required for solution. Each submission then underwent peer review by at least one
mathematician with relevant domain expertise, who evaluated all components: the problem statement, solution, verification code, difficulty ratings, and classification tags (see Section\\u02dc2.3).
Additionally, the problems were securely produced and handled to prevent data contamination, and reviewed for originality (see Section\\u02dc2.4). Finally, the submissions included structured
difficulty ratings that assessed three key dimensions: the required level of background knowledge, the estimated time needed to identify key insights, and the time required to work through technical
details (see Section\\u02dc2.5).\\n2.2 Automated verification\\nFrontierMath focuses exclusively on problems with automatically verifiable solutions\\u2014primarily numerical answers or mathematical
objects that can be expressed as SymPy objects (including symbolic expressions, matrices, sets, and other mathematical structures). For each problem, the evaluated model submits code that computes and
saves its answer as a Python object. A script then automatically verifies this answer. If the problem has a unique integer solution, it checks for an exact match. If the problem has a unique symbolic
real answer, it uses SymPy evaluation to check that the difference between the submitted answer and the actual answer simplifies to 0. In all other cases, a custom verification script is necessary to
check validity of a submitted answer (see Figure 3).\\nThis design choice enables rapid, objective evaluation of AI models without requiring them to output solutions in formal proof languages like
Lean or Coq. The automated verification framework substantially reduces the cost and complexity of evaluation, as verification can be performed programmatically without human intervention.
Furthermore, it eliminates potential human bias and inconsistency in the evaluation process, as the verification criteria are explicitly defined and uniformly applied.\\nWhile this approach enables
efficient and scalable evaluation, it does impose certain limitations. Most notably, we cannot include problems that require mathematical proofs or formal reasoning steps, as these would demand human
evaluation to assess correctness and clarity.444In theory, we could have accepted formalized proofs in Lean or other formal languages as a problem solution format. However, this presents two
challenges. Firstly, current AI models are often not trained to write formalized proofs in specialized languages. We wanted to ensure that the problems were measuring genuine reasoning skills, rather
than skill at writing formalized proofs. Secondly, Lean\\u2019s mathematical library, mathlib, doesn\\u2019t fully cover the undergraduate math curriculum [mathlib], let alone the scope of research
math, which limits the fields such a benchmark could measure. However, even without formal proofs, these problems span a substantial breadth of modern mathematics and include problems that eminent
mathematicians have characterized as exceptionally difficult (see Section\\u02dc6).\\n2.3 Validation and quality assurance\\nTo maintain high quality standards and minimize errors in the benchmark, we
established a rigorous multi-stage review process. Each submitted problem underwent blind peer review by at least one expert mathematician from our team, who evaluated the following
criteria:\\n-\\n\\u2022\\nVerifying the correctness of the problem statement and the provided solution.\\n-\\n\\u2022\\nChecking for ambiguities or potential misunderstandings in the problem
wording.\\n-\\n\\u2022\\nAssessing the problem for guessproofness, ensuring that solutions cannot be easily obtained without proper mathematical reasoning.\\n-\\n\\u2022\\nConfirming the
appropriateness of the assigned difficulty ratings and metadata.\\nVerifying correctness is the most important of these tasks. For problems with unique solutions\\u2014the majority of our
benchmark\\u2014verifying correctness requires checking the mathematical argumentation, computations, and, if applicable, programming scripts the writer provided to justify their answer. For problems
with non-unique solutions, e.g. those which ask for a solution to some system of Diophantine equations or for a Hamiltonian path in a given graph, the reviewer only checks that the provided
verification script matches the problem requirements and test it on the answer.\\nAll problems in the benchmark have undergone at least one blind peer review. Through this review process, we identify
problems with incorrect answers as well as those that fail to meet our guessproofness criterion. Such problems are only included in the benchmark after authors successfully address these issues
through revision.\\nDuring first reviews, our reviewers commonly identify several types of issues with submitted problems. These include answers that aren\\u2019t easily verifiable, problems where
guessing is easier than proving, and cases where simple brute-force methods circumvent the intended difficulty. Such issues occur predominantly with authors who are new to submitting questions to the
benchmark and have not yet fully internalized the guidelines. Beyond these concerns, straightforward errors in question statements or computational mistakes in solutions leading to incorrect answers
are also not uncommon.\\nWe commissioned blind reviews from second reviewers on 30 randomly chosen questions so far to get some idea about the noise threshold we might expect due to errors, and we
also randomly selected 5 questions to be removed from the dataset and serve as a public sample of problems (see Appendix\\u02dcA). In total, 35 of the accepted problems have received scrutiny beyond
the first round of peer review.\\nTwo out of 35 questions had an incorrect answer provided by the author, undetected in the first review. Assuming that a question being incorrect is a Bernoulli trial
with probability and that the second reviewers catch all errors, using a Jeffreys prior on yields a posterior error rate of for this benchmark. On one hand, the Jeffreys prior is conservative since
our prior belief about is likely lower due to the careful construction of the benchmark. On the other hand, we must account for potential undetected errors that even the second review might have
missed. Therefore, estimating a critical error rate of approximately is reasonable. This estimate aligns with error rates typical in machine learning benchmarks; for instance,
[northcutt2021pervasivelabelerrorstest] estimate a label error rate in the ImageNet validation set, while [gema2024we] find that over of questions in the MMLU benchmark contain errors based on expert
review of 3,000 randomly sampled questions.\\nThe second reviews also identified less critical errors. Six out of 35 questions had missing hypotheses in their statements which technically made them
not fully rigorous. While domain experts could reasonably impute this missing context, it might still pose difficulties for models attempting to solve these problems. For two of the 35 questions,
reviewers proposed strategies for guessing the solution with substantially less effort or computation than was necessary for a rigorous mathematical justification of the answer, violating the
guessproofness criterion. In all cases, they proposed adjustments to the problem which corrected the error while preserving the original mathematical intent of the writer.\\nAlthough the error rate
remains low, the mistakes we have spotted highlight the issues of a passive review system, in which the reviewer sees the full solution document and simply has to state their approval in order for a
problem to be accepted into the benchmark. Going forward, we are adopting a more active review process, and will henceforth require concrete confirmation of a problem\\u2019s soundness before it is
accepted. For problems which seek a solution with some easily verified characteristic, such as a tuple of integers satisfying a Diophantine equation, it is enough to test that criterion directly. If a
problem seeks a symbolic real number or some efficiently computed value, then it would be strong evidence if a heuristically determined guess approximates the given solution. For more abstract
problems, it may be necessary to have a reviewer solve the problem themselves, given only the key steps and ideas of the solution rather than the full write-up.\\nAdditionally, we observed
inconsistent difficulty ratings between first and second reviewers; due to the subjective nature of this task, ratings rarely matched and often showed substantial differences.555See Section 2.5 for
discussion on our ongoing effort to normalize these ratings. In several cases, second reviewers found no fundamental problems with the questions but suggested ways to increase their difficulty,
indicating potential room to improve the difficulty of the remaining questions if reviewers were to spend more time on refining them.\\n2.4 Originality and data contamination prevention\\nContributors
were explicitly instructed to develop novel mathematical problems. While they could build upon existing mathematical ideas, they were required to do so in non-obvious ways\\u2014either through clever
adaptations that substantially transformed the original concepts, or through novel and innovative combinations of multiple ideas. This approach ensured that solving the problems required genuine
mathematical insight rather than pattern matching against known problems.\\nTo minimize the risk of problems and solutions being disseminated online, we encouraged all submissions to be conducted
through secure, encrypted channels. We employed encrypted communication platforms to coordinate with contributors and requested that any written materials stored online be encrypted\\u2014for
instance, by placing documents in password-protected archives shared only via secure methods.666While we endeavored to adhere strictly to these protocols, we acknowledge that, in some cases, standard
email clients were used when communicating about a subset of the problems outside our immediate team.\\nOur primary method for validating originality relied on expert review by our core team of
mathematicians. Their extensive familiarity with competition and research-level problems enabled them to identify potential similarities with existing problems that automated systems might miss. The
team conducted thorough manual checks against popular mathematics websites, online repositories, and academic publications. This expert review process was supplemented by verification using plagiarism
detection software.\\nTo provide further confidence in our problems\\u2019 originality, we ran them through the plagiarism detection tools Quetext and Copyscape. Across the entire dataset, the
verification process revealed no significant matches to existing content, with minimal flags attributed only to standard mathematical terminology or software oversensitivity.777We limited our
plagiarism checking to problem statements only, excluding solutions to minimize online exposure. We specifically chose Quetext and Copyscape over more widely-used tools like Turnitin because they
posed the lowest risk of our problems being stored in databases that might later be used to train AI models.\\n2.5 Problem difficulty\\nEstimates of mathematical problem difficulty are useful for
FrontierMath\\u2019s goal of evaluating AI mathematical capabilities, as such estimates would provide more fine-grained information about the performance of AI models. To assess problem difficulty,
each problem author provided ratings along three key dimensions:\\n-\\n1.\\nBackground: This rating ranges from 1 to 5 and indicates the level of mathematical background required to approach the
problem. A rating of 1 corresponds to high school level, 2 to early undergraduate level, 3 to late undergraduate level, 4 to graduate level, and 5 to research level.\\n-\\n2.\\nCreativity: Estimated
as the number of hours an expert would need to identify the key ideas for solving the problem. This measure has no upper limit.\\n-\\n3.\\nExecution: Similarly estimated as the number of hours
required to compute the final answer once the key ideas are found, including time writing a script if applicable. This measure also has no upper limit.\\nTo verify and refine the initial difficulty
assessments, each difficulty assessment underwent a peer-review process. Reviewers assessed the accuracy of the initial difficulty ratings. Any discrepancies between the authors\\u2019 ratings and the
reviewers\\u2019 assessments were discussed, and adjustments were made as needed to ensure that the difficulty ratings accurately reflected the problem\\u2019s demands in terms of background,
creativity, and execution.\\nAccurately assessing the difficulty of mathematics problems presents significant challenges [Chen2024, Chen2024Mistake]. Problems that seem impossible may become trivial
after exposure to certain techniques, and multiple solution paths of varying complexity often exist. Moreover, while we designed our problems to require substantial mathematical work rather than allow
solutions through guessing or pattern matching, the possibility of models finding unexpected shortcuts could undermine such difficulty estimates.\\nGiven these challenges, we view our difficulty
ratings as providing rough guidance. More rigorous validation, such as through systematic data collection on human solution times, would be needed to make stronger claims about these difficulty
assessments.888In unpublished preliminary work, we found that problems rated as more difficult correlate with lower solution rates by GPT-4o, providing some support for our difficulty assessment
system. However, more systematic validation would be needed to make strong claims about the reliability of these ratings.\\n3 Dataset composition\\nThe FrontierMath benchmark covers a broad spectrum
of contemporary mathematics, spanning both foundational areas and specialized research domains. This comprehensive coverage is crucial for effectively evaluating AI systems\\u2019 mathematical
capabilities across the landscape of modern mathematics. Working with over 60 mathematicians across different specializations, we captured most top-level MSC 2020 classification codes, reflecting the
breadth of mathematics from foundational fields to emerging research areas.\\n| MSC Classification | Percentage | MSC Classification | Percentage |\\n| 11 Number theory | 17.8% | 57 Manifolds and cell
complexes | 2.1% |\\n| 05 Combinatorics | 15.8% | 13 Commutative algebra | 2.1% |\\n| 20 Group theory and generalizations | 8.9% | 54 General topology | 1.4% |\\n| 60 Probability theory and stochastic
processes | 5.1% | 35 Partial differential equations | 1.4% |\\n| 15 Linear and multilinear algebra; matrix theory | 4.8% | 53 Differential geometry | 1.4% |\\n| 14 Algebraic geometry | 4.8% | 42
Harmonic analysis on Euclidean spaces | 1.4% |\\n| 33 Special functions | 4.8% | 41 Approximations and expansions | 1.4% |\\n| 55 Algebraic topology | 3.1% | 52 Convex and discrete geometry | 1.4%
|\\n| 12 Field theory and polynomials | 2.4% | 82 Statistical mechanics, structure of matter | 1.0% |\\n| 30 Functions of a complex variable | 2.4% | 44 Integral transforms, operational calculus |
1.0% |\\n| 68 Computer science | 2.4% | 17 Nonassociative rings and algebras | 1.0% |\\n| 18 Category theory; homological algebra | 2.4% | Other (< 3 problems each) | 9.9% |\\nNumber theory and
combinatorics are most prominently represented, collectively accounting for approximately 34% of all MSC2020 tags. This prominence reflects both our contributing mathematicians\\u2019 expertise and
these domains\\u2019 natural amenability to problems with numerical solutions that can be automatically verified. The next most represented fields are algebraic geometry and group theory (together
about 14% of MSC tags), followed by algebraic topology (approximately 3%), linear algebra (5%), and special functions (5%). Problems involving probability theory and stochastic processes constitute
about 5% of the MSC tags, with additional significant representation in complex analysis, category theory, and partial differential equations, each comprising between 1-3% of the MSC tags.\\nThe
network visualization (Figure 4) reveals how mathematical subjects combine within individual problems. Number theory and combinatorics appear together most frequently, with 13% of problems requiring
both subjects, followed by combinatorics-group theory (9%) and number theory-group theory (8%). These three fields\\u2014number theory (44% of all problems), combinatorics (39%), and group theory
(22%)\\u2014form the core of the benchmark, each combining with more than a dozen other mathematical domains in novel ways.\\nThere is a wide range of techniques required to solve the problems in our
dataset. In particular, there are over 200 different techniques listed as being involved in the solutions of our problems. Although generating functions, recurrence relations, and special functions
emerge as common techniques, they each appear in less than 5% of problems, underscoring the benchmark\\u2019s methodological diversity. Even the most frequently co-occurring techniques appear together
in at most 3 problems, highlighting how problems typically require unique combinations of mathematical approaches.\\n4 Evaluation\\n4.1 Experiment-enabled evaluation framework\\nTo evaluate AI models
on FrontierMath problems, we developed a framework that allows models to explore and verify potential solution approaches through code execution, mirroring how mathematicians might experiment with
ideas when tackling challenging problems. This framework enables models to test hypotheses, receive feedback, and refine their approach based on experimental results, as illustrated in Figure 5.\\nThe
evaluation process follows an iterative cycle where the model analyzes the mathematical problem, proposes solution strategies, implements these strategies as executable Python code, receives feedback
from code execution results, and refines its approach based on the experimental outcomes. For each problem, the model interacts with a Python environment where it can write code blocks that are
automatically executed, with outputs and any error messages being fed back into the conversation. This allows the model to verify intermediate results, test conjectures, and catch potential errors in
its reasoning.\\nWhen submitting a final answer, models must follow a standardized format by including a specific marker comment (# This is the final answer\\n), saving the result using Python\\u2019s
pickle module, and ensuring the submission code is self-contained and independent of previous computations. The interaction continues until either the model submits a correctly formatted final answer
or reaches the token limit, which we set to 10,000 tokens in our experiments. If a model reaches this token limit without having submitted a final answer, it receives a final prompt requesting an
immediate final answer submission. If the model still fails to provide a properly formatted final answer after this prompt, the attempt is marked as incorrect.\\n4.2 Results\\n4.2.1 Accuracy on
FrontierMath\\nWe evaluated six leading language models on our existing subset of FrontierMath problems: o1-preview ([o1-preview]), o1-mini ([o1-mini]), and GPT-4o (2024-08-06 version) ([GPT-4o]),
Claude 3.5 Sonnet (2024-10-22 version) ([sonnet3-5]), Grok 2 Beta ([grokbeta]), and Google DeepMind\\u2019s Gemini 1.5 Pro 002 ([gemini15pro002]). All models had a very low performance on FrontierMath
problems, with no model achieving even a 2% success rate on the full benchmark (see Figure 6). This stands in stark contrast to other mathematics evaluations such as GSM8K ([cobbe2021training]), MATH
([hendrycks2021measuring]), AIME 2024 ([o1-learningtoreason]), or Omni-MATH ([gao2024omni]), which are closer to saturation (see Figure 2).\\nBased on a single evaluation of the full benchmark, we
found that models solved very few problems (less than 2% success rate). Given this low success rate and the fact that we ran only one evaluation, the precise ordering of model performance should be
interpreted with significant caution, as individual successes can have an outsized impact on rankings. To better understand model behavior on solved problems, we identified all problems that any model
solved at least once\\u2014a total of four problems\\u2014and conducted repeated trials with five runs per model per problem (see Appendix B.2). We observed high variability across runs: only in one
case did a model solve a question on all five runs (o1-preview for question 2). When re-evaluating these problems that were solved at least once, o1-preview demonstrated the strongest performance
across repeated trials (see Section B.2).\\nMoreover, even when a model obtained the correct answer, this does not mean that its reasoning was correct. For instance, on one of these problems running a
few simple simulations was sufficient to make accurate guesses without any deeper mathematical understanding. However, models\\u2019 low overall accuracy shows that such guessing strategies do not
work on the overwhelming majority of FrontierMath problems. We also ran each model five times per problem on our five public sample problems (see Appendix A), and made the transcripts publicly
available.999The transcripts can be downloaded at https://epochai.org/files/sample_question_transcripts.zip\\n4.2.2 Number of responses and token usage\\nOur evaluation framework allows models to run
experiments and reflect on their results multiple times before submitti\"}"}]}, "hint": null}, {"title": "Benchmarking AI on unsolved math problems | Epoch AI", "url":
"https://epoch.ai/frontiermath/open-problems/about/", "snippet": "FrontierMath: Open Problems\nThis work was supported by a grant from Schmidt Sciences.\nAI math capabilities have come far and fast.
In mid-2024, [high school math](https://epoch.ai/benchmarks/math-level-5) was still a challenge. By the end of 2025, AI systems were solving [extremely hard
problems](https://epoch.ai/frontiermath/tiers-1-4/about) designed to be solvable only by top human experts. As we write this, it seems likely that AI systems will soon be able to solve problems that
no human has ", "api_data": null, "hint": null}, {"title": "Introducing FrontierMath: Open Problems - Epoch AI - Substack", "url": "https://epochai.substack.com/p/introducing-frontiermath-open-
problems", "snippet": "Introducing FrontierMath: Open Problems\nBenchmarking AI on unsolved research problems that have eluded mathematicians\nThis work was supported by a grant from Schmidt
Sciences.\nAI math capabilities have come far and fast. In mid-2024, [high school math](https://epoch.ai/benchmarks/math-level-5) was still a challenge. By the end of 2025, AI systems were solving
[extremely hard problems](https://epoch.ai/frontiermath/about) designed to be solvable only by top human experts. As we write this, it see", "api_data": null, "hint": null}, {"title": "Epoch AI on X:
\"Can AI solve math research problems that have eluded human mathematicians? Our new benchmark, FrontierMath: Open Problems, is designed to help find out. AI hasn\u2019t solved any of these yet, but
the game is young! https://t.co/6RbPXT0gzQ\" / X", "url": "https://x.com/EpochAIResearch/status/2016188014540816879", "snippet": "We\u2019ve detected that JavaScript is disabled in this browser.
Please enable JavaScript or switch to a supported browser to continue using x.com. You can see a list of supported browsers in our Help Center.\nHelp Center\nTerms of Service Privacy Policy Cookie
Policy Imprint Ads info \u00a9 2026 X Corp.", "api_data": null, "hint": null}, {"title": "FrontierMath \u2014 Grokipedia", "url": "https://grokipedia.com/page/frontiermath", "snippet":
"FrontierMath\n[benchmark dataset](https://grokipedia.com/page/Benchmark_(computing))developed by Epoch AI to evaluate\n[advanced mathematical reasoning
capabilities](https://grokipedia.com/page/Automated_theorem_proving)in artificial intelligence models, featuring hundreds of original, exceptionally challenging problems crafted and vetted by expert
mathematicians.\n[Introduced via an](https://grokipedia.com#ref-1)\n[[1]](https://grokipedia.com#ref-1)[arXiv preprint](https://grokipedia.com/page/ArXiv", "api_data": null, "hint": null}, {"title":
"On the smallest open Diophantine equations", "url": "https://arxiv.org/pdf/2204.11624", "snippet": "{\"paper_id\": \"2204.11624\", \"format\": \"pdf\", \"url\": \"https://arxiv.org/pdf/2204.11624\",
\"pdf_path\": \"/home/pfftz/job/onit/aib-joy-void-joy-bot.git/tree/main/logs/43127_20260411_150842/downloads/arxiv/2204.11624.pdf\", \"hint\": \"PDF downloaded to /home/pfftz/job/onit/aib-joy-void-
joy-bot.git/tree/main/logs/43127_20260411_150842/downloads/arxiv/2204.11624.pdf. Use the Read tool to read the PDF content.\"}", "api_data": {"content": [{"type": "text", "text": "{\"paper_id\":
\"2204.11624\", \"format\": \"pdf\", \"url\": \"https://arxiv.org/pdf/2204.11624\", \"pdf_path\": \"/home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/43127_20260411_150842/downloads/arxiv/2204.11624.pdf\", \"hint\": \"PDF downloaded to /home/pfftz/job/onit/aib-joy-void-joy-
bot.git/tree/main/logs/43127_20260411_150842/downloads/arxiv/2204.11624.pdf. Use the Read tool to read the PDF content.\"}"}]}, "hint": null}]}
```

```json
{
  "query": "FrontierMath Open Problems solved 2026"
}
```

### 📋 Result

```
{"markets": [{"market_title": "How many FrontierMath Open Problems solved in 2026?", "probability": 0.5, "volume": 282.0, "url": "https://manifold.markets/bh/how-many-frontiermath-open-problems",
"source": "manifold", "description": null, "market_id": "55pCtZPZlS", "recent_history": [{"date": "2026-04-05", "probability": 0.152}, {"date": "2026-04-09", "probability": 0.173}]}, {"market_title":
"Will Moltbook solve any open FrontierMath problems in 2026?", "probability": 0.045128475014634455, "volume": 464.9602962783498, "url": "https://manifold.markets/ChaosIsALadder/will-moltbook-solve-
any-open-proble", "source": "manifold", "description": null, "market_id": "5Ru0yPsN9N", "recent_history": null}], "query": "FrontierMath Open Problems solved 2026"}
```

## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__search__fetch_url


## 🔧 Tool: mcp__asknews__search_news


## 🔧 Tool: mcp__search__fetch_url


```json
{
  "url": "https://epoch.ai/frontiermath/open-problems/small-diophantine",
  "prompt": "What is the current status of this problem? Has it been solved? Is there partial progress? What AI models have attempted it?"
}
```

### 📋 Result

```
{"url": "https://epoch.ai/frontiermath/open-problems/small-diophantine", "content": "## Current Status\n\n**Partially solved** (3 of 9 equations resolved):\n\n- **GPT-5.4 Pro** (March 2026) solved 2
equations via direct substitution:\n  - z\u00b2+y\u00b2z-z+x\u00b3+2=0\n  - z\u00b2+y\u00b2z+x\u00b3+x+1=0\n\n- **Problem authors** subsequently solved a 3rd equation (adapting GPT-5.4 Pro's
approach):\n  - z\u00b2+y\u00b2z+x\u00b3+x-1=0\n\n**Remaining**: 6 of 9 equations are still unsolved.\n\nThe problem authors anticipated some equations might have \"relatively uninteresting\"
solutions via direct substitution. They believe resolving all 9 equations will require a genuinely new mathematical approach.\n\n## AI Models Tested\n\nThe content mentions that AI models have been
evaluated but doesn't provide a complete list. Only **GPT-5.4 Pro** is explicitly named as having made progress.\n\n## Context\n\n- These are the smallest Diophantine equations (size \u226424) with
open finiteness problems\n- Numerical evidence suggests all have infinitely many solutions, but this remains unproven\n- Problem authors note high uncertainty about resolution timeframe\n- Solution
requires finding 3 distinct integer solutions (x,y,z) with |x| > 10^50 for each equation\n\n**Relevant links:**\n- [GPT-5.4 Pro's solutions to two equations](https://epoch.ai/files/open-
problems/small-diophantine-two-families.pdf)", "title": "Finiteness Problem for Diophantine Equations"}
```

```json
{
  "url": "https://epoch.ai/frontiermath/open-problems/about/",
  "prompt": "How many total open problems are there? What are all the problems listed? What is the current solve status? What categories exist and how many are in each?"
}
```

### 📋 Result

```
{"url": "https://epoch.ai/frontiermath/open-problems/about/", "content": "Based on the content provided:\n\n**Total Open Problems:** 14 problems in the pilot release\n\n**Problems Listed:** Only 4
example problems are explicitly detailed:\n\n1. **Ramsey number R(B_{n-1}, B_n)** - Combinatorics, Moderately interesting\n2. **KLT del Pezzo surfaces** - Combinatorics (likely Algebraic Geometry),
Solid result\n3. **Degree 23 polynomial with Galois group M_{23}** - Number theory, Major advance\n4. **Unknotting number algorithm** - Topology, Breakthrough\n\n**Current Solve Status:** At the time
of release, none of these problems have been solved by humans or AI systems. Initial attempts by GPT-5.2 Pro and Gemini 3 Deep Think showed no promise on the actual open problems.\n\n**Categories by
Significance:** The content describes problems distributed across tiers of meaningfulness:\n- Moderately interesting (within a subfield)\n- Solid result\n- Major advance\n- Breakthrough\n\nThe pilot
set has a tilt toward **combinatorics and number theory**. The content aims for even distribution across significance tiers but doesn't provide exact counts per category.\n\n**Note:** The content only
showcases 4 example problems out of the 14 total problems in the pilot release.\n\n---\n\n**Relevant links:**\n- [Problem proposal form](https://epoch.ai/frontiermath/open-problems/submissions)\n-
[Ramsey book graphs problem](https://epoch.ai/frontiermath/open-problems/ramsey-book-graphs)\n- [KLT del Pezzo surface problem](https://epoch.ai/frontiermath/open-problems/klt-del-pezzo-surface)\n-
[Inverse Galois problem](https://epoch.ai/frontiermath/open-problems/inverse-galois)\n- [Unknotting number problem](https://epoch.ai/frontiermath/open-problems/unknotting-number)\n- [Contact
email](mailto:[email protected])", "title": "Benchmarking AI on unsolved math problems"}
```

```json
{
  "query": "FrontierMath open problems AI solved",
  "hours_back": 336,
  "n_articles": 5
}
```

### 📋 Result

```
Error calling tool 'search_news': ForbiddenError: 403012 - Usage limit exceeded for 'requests', please upgrade your plan at https://my.asknews.app/plans to increase your limits.
```

```json
{
  "url": "https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/",
  "prompt": "What FrontierMath open problems has AI solved? List all solved problems and their dates."
}
```

### 📋 Result

```
{"url": "https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/", "content": "Based on the content, AI has solved the following FrontierMath open
problems:\n\n1. **Ramsey Hypergraphs** - Solved March 23, 2026\n   - Improved lower bounds on a hypergraph quantity H(n)\n   - Solved using OpenAI's GPT-5.4 Pro\n\n2. **Small Diophantine Equations** -
Solved March 5, 2026 (partial)\n   - GPT-5.4 Pro solved 2 out of 9 open equations in a finiteness problem for low-size Diophantine equations\n   - Overall problem still marked as unsolved,
representing partial progress\n   - Solved using OpenAI's GPT-5.4 Pro\n\nRelevant links:\n- [Ramsey Hypergraphs problem page](https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs)\n- [Small
Diophantine problem page](https://epoch.ai/frontiermath/open-problems/small-diophantine)", "title": "From Erd\u0151s to Axiom: 12 Open Problems AI Has Actually Solved"}
```

## 💭 Thinking

Let me now synthesize what I've learned and think about the forecast.

Key facts:
1. As of April 4, 2026, the official FrontierMath Open Problems index shows 1 problem solved (the Ramsey Hypergraphs problem, solved by GPT-5.4 Pro).
2. There are 14 problems in the pilot release.
3. The categories are: Moderately interesting, Solid result, Major advance, Breakthrough.
4. The question says "1/4 solved in 'Moderately interesting'" - so there are 4 problems in the "Moderately interesting" category, and 1 is solved.


5. The Small Diophantine problem has made some progress with 3 of 9 equations resolved, but hasn't been fully solved yet.
6. One problem was removed from the benchmark back on March 5, 2026.
7. The resolution date is May 1, 2026, so I need to figure out what the count will be by then.
8. The question was published and closes on April 11, 2026, which is before the resolution date.

So I'm trying to forecast how many problems will be solved by May 1, 2026, starting from the current count of just 1.

For the count to increase, either the Small Diophantine problem would need to be fully completed (all 9 equations, though the remaining 6 are described as requiring a genuinely new mathematical approach), or another problem would need to be solved by AI. The key thing is that the question resolves based on what the index actually shows on May 1, 2026, not on partial progress. With about 20 days left until that date, I'm weighing whether it's likely that either the Small Diophantine gets fully solved or another problem gets cracked.

Looking at the Manifold market data for the full year 2026, there's roughly equal probability spread across 1-4 problems solved, but that's for the entire year—by May 1st, I'd expect the probabilities to be weighted more heavily toward the lower end since we're only a third of the way through the year.

The Small Diophantine problem is the most realistic candidate for a second solve since it's already at 3 of 9 equations, though the remaining 6 would require a fundamentally different mathematical approach. With only about 20 days left and no indication that other problems are close to being solved, staying at 1 solved problem is by far the most likely outcome. A second solve is possible but would need either rapid progress on the Diophantine or an unexpected breakthrough elsewhere, while anything beyond 2 seems quite improbable in this timeframe. ~70%
- "2": ~20%
- "Greater than 2": ~5-10%

I'm reconsidering the Small Diophantine problem—it requires solving all 9 equations to count as fully solved, and with only 3 of 9 resolved and 6 remaining that need genuinely new approaches, completing it in 20 days seems unlikely. That said, there could be other problems being worked on behind the scenes, and AI capabilities are advancing rapidly with multiple frontier models now capable of tackling these challenges. Looking at the timeline, the Ramsey problem took about 2-3 months from the benchmark's launch in early 2026 to solve, so another solve in the next 20 days is possible but not highly probable given the difficulty curve.

I'll adjust my final estimates to be slightly more conservative on the higher end: "1 or fewer" at 72%, "2" at 20%, and "greater than 2" at 8%.

## 💬 Response

Now let me check for any very recent news about additional FrontierMath solves.

## 🔧 Tool: mcp__search__web_search


## 🔧 Tool: mcp__search__search_exa


```json
{
  "query": "FrontierMath open problem solved April 2026"
}
```

### 📋 Result

```
{"query": "FrontierMath open problem solved April 2026", "results": [{"title": "FrontierMath: Open Problems - Unsolved Mathematical Challenges | Epoch AI", "url": "https://epoch.ai/frontiermath/open-
problems/", "snippet": "A collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would meaningfully advance the state of human
mathematical knowledge.\n2026-03-05: We removed one problem from the benchmark, as we have determined that any solution would not meet our bar of being a publishable result in its own right. The
problem page remains up: see it for more info on an AI-generated solution and subsequent human elaboration.", "api_data": null, "hint": null}, {"title": "Share of FrontierMath problems solved
correctly by AI models - Our World in Data", "url": "https://ourworldindata.org/grapher/ai-frontiermath-over-time", "snippet": "Share of FrontierMath problems solved correctly by AI
models\n![](/grapher/ai-frontiermath-over-time.png)\nWhat you should know about this indicator\n- This indicator shows the share of FrontierMath problems that AI models solve correctly, based on Epoch
AI's evaluation.\n- FrontierMath is a set of 350 original math problems written by experts, covering many areas of advanced mathematics. Many problems are difficult enough that human specialists might
need hours or days to solve them.\n- The benchmar", "api_data": null, "hint": null}, {"title": "'Breakthrough' Frontier Math Open Problem solved before 2028 | Manifold", "url":
"https://manifold.markets/Jolliest/breakthrough-frontier-math-open-pro", "snippet": "'Breakthrough' Frontier Math Open Problem solved before
2028\n7\n\u1e40100\u1e401432028\n54%\nchance\n1H\n6H\n1D\n1W\n1M\nALL\nContext: [https://epoch.ai/frontiermath/open-problems](https://epoch.ai/frontiermath/open-problems)\nThere are currently 4
categories of Frontier Math Open Problems: Moderately Interesting, Solid Result, Major Advance, Breakthrough. This market will resolve yes if 1 of the 3 breakthrough problems are solved by AI.\nIf
more 'Breakthrough' questions are added, they are also considered for the re", "api_data": null, "hint": "Use manifold_price for market data, or manifold_history for historical prices."}, {"title":
"How many FrontierMath Open Problems solved in 2026? | Manifold", "url": "https://manifold.markets/bh/how-many-frontiermath-open-problems", "snippet": "How many FrontierMath Open Problems solved in
2026?\n9\n\u1e40400\u1e40282Dec 31\n15%\n1\n15%\n2\n16%\n3\n14%\n4\n9%\n5\n3%\n6\n3%\n7\n3%\n8\n3%\n9\n3%\n10\n3%\n11\n3%\n12\n3%\n13\n3%\n14\n3%\n15\n3%\nResolves to the number of problems displayed
as solved at [https://epoch.ai/frontiermath/open-problems](https://epoch.ai/frontiermath/open-problems)\nI will not trade in this market.\nSee also this market for EOY2027:
[https://manifold.markets/bh/how-many-frontiermath-open-problems-SzcLglOOOs?r=Ymg](https://manifold.markets/bh/how-many-frontie", "api_data": null, "hint": "Use manifold_price for market data, or
manifold_history for historical prices."}, {"title": "Benchmarking AI on unsolved math problems | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/about/", "snippet": "FrontierMath: Open
Problems\nThis work was supported by a grant from Schmidt Sciences.\nAI math capabilities have come far and fast. In mid-2024, [high school math](https://epoch.ai/benchmarks/math-level-5) was still a
challenge. By the end of 2025, AI systems were solving [extremely hard problems](https://epoch.ai/frontiermath/tiers-1-4/about) designed to be solvable only by top human experts. As we write this, it
seems likely that AI systems will soon be able to solve problems that no human has ", "api_data": null, "hint": null}, {"title": "A Ramsey-style Problem on Hypergraphs | Epoch AI", "url":
"https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs/", "snippet": "Solution update\nThis problem has been solved! A solution was first elicited by Kevin Barreto and Liam Price, using
GPT-5.4 Pro. This solution was confirmed by problem contributor Will Brian, and will be written up for publication. A full transcript of the original conversation with GPT-5.4 Pro can be found
[here](https://epoch.ai/files/open-problems/gpt-5-4-pro-hypergraph-ramsey.txt) and GPT-5.4 Pro\u2019s write-up from the end of that transcript can be found [here](https://epoch.ai/files/open-proble",
"api_data": null, "hint": null}, {"title": "What Is the Frontier Math Benchmark? Why Open Research Problems Expose True AI Reasoning | MindStudio", "url": "https://www.mindstudio.ai/blog/frontier-
math-benchmark-open-research-problems-ai-reasoning", "snippet": "What Is the Frontier Math Benchmark? Why Open Research Problems Expose True AI Reasoning\nFrontier Math uses unpublished problems that
take researchers days to solve. Models with full Python access still score under 3%. Here's why it matters.\n![What Is the Frontier Math Benchmark? Why Open Research Problems Expose True AI
Reasoning](https://i.mscdn.ai/70cbb1ad-08d7-4fdc-ab31-e343780966a6/generated-images/34713d9a-ba22-4eb7-a8f6-1bc9e9bd87a4.png?fm=auto&w=1200&fit=cover?fm=auto&w=1200&fit=cover)\nA", "api_data": null,
"hint": null}, {"title": "First AI solution on FrontierMath: Open Problems", "url": "https://epochai.substack.com/p/first-ai-solution-on-frontiermath", "snippet": "First AI solution on FrontierMath:
Open Problems\nAI has solved one of the problems in FrontierMath: Open Problems, our benchmark of real research problems that mathematicians have tried and failed to solve\nThe newly-solved problem
came from Will Brian, who had placed it in the Moderately Interesting category. It is a conjecture from a paper he wrote with Paul Larson in 2019. They were unable to solve it at the time, or in
several attempts since. Brian had this to say.\nBrian plans to write up the", "api_data": null, "hint": null}, {"title": "GPT-5.4 solves its first open math problem from FrontierMath benchmark",
"url": "https://www.remio.ai/post/gpt-5-4-solves-its-first-open-math-problem-from-frontiermath-benchmark", "snippet": "GPT-5.4 solves its first open math problem from FrontierMath benchmark\n[Olivia
Johnson](https://www.remio.ai/members-area/olivia/profile)- Mar 15\n- 5 min read\n![GPT-5.4 solves its first open math problem from FrontierMath benchmark](https://static.wixstatic.com/media/80334c_41
6521e934bc4e9e8b5bf99bf5490a88~mv2.png/v1/fill/w_49,h_29,al_c,q_85,usm_0.66_1.00_0.01,blur_2,enc_avif,quality_auto/80334c_416521e934bc4e9e8b5bf99bf5490a88~mv2.png)\n[Recent logs from the evaluation of
GPT-5.4 Pro](https://ww", "api_data": null, "hint": null}, {"title": "GPT-5.4 Pro Cracks Open Math Problem", "url": "https://winbuzzer.com/2026/03/24/gpt-54-pro-solves-open-math-problem-epoch-ai-
frontiermath-xcxwbn/", "snippet": "- Breakthrough: OpenAI\u2019s GPT-5.4 Pro solved an open mathematical problem that had resisted human efforts since 2019, verified independently by Epoch AI.\n-
Broader Capability: Three other frontier AI models from Anthropic, Google, and OpenAI also solved the same problem, suggesting shared mathematical reasoning capacity.\n- Benchmark Progress:
FrontierMath scores jumped from 5% under GPT-4 in 2024 to 50% under GPT-5.4 Pro in March 2026.\n- Expert Reaction: Mathematicians remain divided, with Terenc", "api_data": null, "hint": null}]}
```

```json
{
  "query": "FrontierMath open problems new AI solve 2026",
  "num_results": 5
}
```

### 📋 Result

```
[{"title": "First AI solution on FrontierMath: Open Problems", "url": "https://epochai.substack.com/p/first-ai-solution-on-frontiermath", "snippet": "First AI solution on FrontierMath: Open
Problems\n\n# Epoch AI\n\nSubscribeSign in\n\nUpdates\n\n# First AI solution on FrontierMath: Open Problems\n\n### AI has solved one of the problems in FrontierMath: Open Problems, our benchmark of
real research problems that mathematicians have tried and failed to solve\n\nEpoch AI\n\nMar 23, 2026\n\n33\n\n4\n\n5\n\nShare\n\nThe newly-solved problem came from Will Brian, who had placed it in
the Moderately Interesting category. It is a conjecture from a paper he wrote with Paul ", "highlights": ["First AI solution on FrontierMath: Open Problems\n\n# Epoch AI\n\nSubscribeSign in\n\nUpdates
# First AI solution on FrontierMath: Open Problems ### AI has solved one of the problems in FrontierMath: Open Problems, our benchmark of real research problems that mathematicians have tried and
failed to solve Epoch AI\n\nMar 23, 2026\n\n33\n\n4\n\n5\n\nShare The newly-solved problem came from Will Brian, who had placed it in the Moderately Interesting category. It is a conjecture from a
paper he wrote with Paul Larson in 2019. They were unable to solve it at the time, or in several attempts since. Brian had this to say. Brian plans to write up the solution for publication, possibly
including follow-on work spurred by the AI\u2019s ideas. This matches his prospective assessment: a solution would be publishable in a standard speciality journal, and would be fairly likely to
generate new questions. Congratulations to Kevin Barreto and Liam Price, who first elicited a solution from GPT-5.4 Pro! They have the option to be coauthors, with Brian, on any resulting paper.
Congratulations also to Geby Jaff who elicited a solution shortly thereafter. We have replicated this elicitation in our scaffold for testing models on the problems. In this scaffold, Gemini 3.1 Pro,
GPT-5.4 (xhigh), and Opus 4.6 (max) are all capable of solving the problem at least some of the time. For more about the problem, including a full chat transcript showing GPT-5.4 Pro\u2019s original
solution, and other models\u2019 solutions in our harness, see the problem page on our website. And check out the main FrontierMath: Open Problems page to learn more about the benchmark. So far one
Moderately Interesting problem has been solved. Which problem will be solved next, and when? ---\n\nThanks for reading! Subscribe to receive the latest from Epoch
AI.\n\nSubscribe\n\n33\n\n4\n\n5\n\nShare\n\nPrevious #### Discussion about this post\n\nCommentsRestacks\n\n2 more comments...\n\nNo posts\n\n### Ready for more?\n\nSubscribe \u00a9 2026 Epoch
Artificial Intelligence, Inc \u00b7 Publisher Privacy\n\nSubstack \u00b7 Privacy\u2219 Terms\u2219 Collection notice Start your Substack Get the app\n\nSubstack is the home for great culture"],
"published_date": "2026-03-23T17:58:04.000", "score": null}, {"title": "GPT-5.4 Pro solved a Ramsey hypergraph problem in FrontierMath for the first time, and also pushed Brian-Larson asymptotics |
lilting channel", "url": "https://lilting.ch/en/articles/gpt54-pro-frontiermath-ramsey-hypergraph", "snippet": "GPT-5.4 Pro solved a Ramsey hypergraph problem in FrontierMath for the first time, and
also pushed Brian-Larson asymptotics | lilting channel\n\nContents\n\nOf the 15 researcher-level open problems in Epoch AI\u2019s FrontierMath benchmark, the first one has now been solved. GPT-5.4 Pro
solved the Ramsey hypergraph partition problem in a free-form conversation, and Epoch AI formally confirmed the result. In a follow-up, the model even went beyond the prompt and established the
asymptotic sharpness of the", "highlights": ["GPT-5.4 Pro solved a Ramsey hypergraph problem in FrontierMath for the first time, and also pushed Brian-Larson   ...    Contents Of the 15 researcher-
level open problems in Epoch AI\u2019s FrontierMath benchmark, the first one has now been solved. GPT-5.4 Pro solved the Ramsey hypergraph partition problem in a free-form conversation, and Epoch AI
formally confirmed the result. In a follow-up, the model even went beyond the prompt and established the asymptotic sharpness of the Brian-Larson conjecture. Claude Opus 4.6 and Gemini 3.1 Pro later
solved the same problem inside Epoch\u2019s scaffold, which is a framework that   ...    ## What FrontierMath is FrontierMath is a benchmark made of open problems or nontrivial known problems written
by working mathematicians. Unlike ordinary benchmarks, every task is designed to be code-verifiable, so a model only counts as solving it if it can produce an algorithm that matches the expected
answer. The 15 problems are grouped into four tiers: | Tier | Count | Meaning |\n| --- | --- | --- | | Moderately interesting | 4 | Standard results suitable for a specialist journal | | Solid result
| 5 | Good enough for a major journal |\n| Major advance | 3 | Results with a large impact on the field | | Breakthrough | 3 | Serious problems that have been open for more than 10 years | The topics
are six number theory problems, six combinatorics problems, one algebraic geometry problem, and two topology/geometry problems. The Ramsey hypergraph problem that was solved here was in the
\u201cModerately interesting\u201d tier, with a human estimate of one to three months.   ...    Ramsey theory studies the idea that large enough structures inevitably contain regular patterns. Here
the setting is a hypergraph version of that problem, and the key quantity is a lower-bound improvement for a function called`H(n)`.   ...    divide a set into non-overlapping groups. In this
problem,`H(n)` asks how large a hypergraph can be if it has no   ...    Brian and Larson\u2019s 2019 paper gave a recursive lower bound:\n\n```\nk\u2081 = 1\nk\u2099 = \u230an/2\u230b +
k_{\u230an/2\u230b} + k_{\u2308n/2\u2309}\n``` They showed that`H(n)` is at least this large and conjectured that the true growth rate is essentially`n\u00b7ln n`. The problem statement asked for a
constant`c > 1` such that`H(n) \u2265 c\u00b7k_n`, with the result already holding at`n = 15`, and it also asked for code returning a witness hypergraph.   ...    GPT-5.4 Pro found the answer in a
free-form conversation with Kevin Barrett and Liam Price. That is important because   ...    The core idea was a \u201cframe replacement lemma.\u201d GPT-5.4 Pro introduced the idea of an`(n\u2081,
..., n\u209c)`-frame, which lets   ...    For`n = 15`, the improvement is already visible: ```\nA\u2081\u2085 \u2265 A\u2083 + 3\u00d7A\u2084 + e\u2083(3) = 5 + 3\u00d78 + 15 = 44\nk\u2081\u2085 =
43\n44/43 > 1\n``` So the requested constant`c > 1` exists. The smallest ratio in the paper\u2019s construction is`57/56` at`n = 32`.   ...    ```\nH(n) \u2265 ((H_t - 1) / ln t) \u00b7 n\u00b7ln n -
O_t(n)\n```\n\nSince`(H_t - 1) / ln t \u2192 1`, the lower bound approaches: ```\nH(n) \u2265 (1 - o(1)) \u00b7 n\u00b7ln n\n``` That matches the Brian-Larson upper bound asymptotically, so the
conjectured growth rate is essentially correct. ## Model status\n\nAfter GPT-5.4 Pro solved it first, Epoch AI evaluated several models inside its scaffold. | Model | Variant | Solved |\n| --- | --- |
--- |\n| GPT-5.2 Pro | all variants | No | | Gemini 3 Deep Think | all problems | No |\n| GPT-5.4 Pro | all problems | Yes, in free-form conversation | | GPT-5.4 (xhigh) | all problems | Yes, with
scaffold |\n| Claude Opus 4.6 (max) | all problems | Yes, with scaffold |   ...    Will Brian, one of the problem authors, called the solution exciting and said it strips away inefficiency from the
lower-bound construction while reflecting the upper-bound structure quite well. He also said he plans to write the result up as a paper and invite Kevin Barrett and Liam Price as coauthors. The
remaining 14 FrontierMath problems are still open.\n\nBack"], "published_date": "2026-03-24T09:41:00.000", "score": null}, {"title": "GPT-5.4 solves its first open math problem from FrontierMath
benchmark", "url": "https://www.remio.ai/post/gpt-5-4-solves-its-first-open-math-problem-from-frontiermath-benchmark", "snippet": "-- GPT-5.4 solves its first open math problem from FrontierMath
benchmark\n\ntop of page\n\n\u200b\n\nSpring Flash Sale \ud83c\udf81 Get 30% off in annual plan with code - SPRING2026\n\nRecent logs from the evaluation of GPT-5.4 Pro show a shift in how large
language models handle complex, unsolved mathematics. In a specific instance involving the FrontierMath benchmark\u2014a collection of hundreds of original, research-level problems\u2014the model
successfully addressed an open problem related to hypergraph construction. This", "highlights": ["-- GPT-5.4 solves its first open math problem from FrontierMath benchmark\n\ntop of page\n\n\u200b
Spring Flash Sale \ud83c\udf81 Get 30% off in annual plan with code - SPRING2026 Recent logs from the evaluation of GPT-5.4 Pro show a shift in how large language models handle complex, unsolved
mathematics. In a specific instance involving the FrontierMath benchmark\u2014a collection of hundreds of original, research-level problems\u2014the model successfully addressed an open problem
related to hypergraph construction. This result represents a transition from AI solving student-level competitions to contributing to the discovery of new mathematical bounds. FrontierMath, developed
by Epoch AI in collaboration with IMO gold medalists and Fields Medalists, was designed to be \"leak-proof.\" Unlike MATH or GSM8K datasets, where models often rely on pattern matching from training
data, FrontierMath problems are unpublished and require hours or days of computational reasoning. The problem GPT-5.4 solved involves the construction of a specific hypergraph and finding the lower
bound for a sequence denoted as H(n). ## Why FrontierMath Tier 4 challenges stopped previous models like o1 Earlier benchmarks like o1 or o3 showed high proficiency in traditional competitive math,
but their performance dropped significantly when faced with \"Tier 4\" problems in the FrontierMath set. These problems are categorized as being at the level of active mathematical research. In late
2024, models like OpenAI\u2019s o1 maintained an accuracy rate of roughly 2% on this dataset. By late 2025, o3 improved this to 25%, but solving a truly \"open\" problem\u2014one where the answer was
not known to the evaluators\u2014remained a gap. The difficulty lies in the complexity of the logical chain. Standard reasoning models often hallucinate intermediate steps when a proof requires more
than a few dozen transitions. FrontierMath demands thousands of logical steps, often requiring the model to bridge disparate fields such as combinatorics and algorithmic complexity. GPT-5.4 navigated
this   ...    The problem in question concerned a specific bound in hypergraph theory. Previously, mathematicians had established that nlog\u20612(n) was a lower bound, but many suspected that
nln\u2061(n) was the actual limit. GPT-5.4 identified a way to generalize an existing construction found in a 2022 research paper (NSF-PAR 10338368).   ...    This event changes the definition of
\"progress\" in AI. We are no longer measuring how well a model can repeat a   ...    The success of GPT-5.4 in this instance suggests that the bottleneck for AI in science was never just
\"intelligence,\"   ...    tool. If these results hold across the remaining 13 open problems in the FrontierMath subset, the timeline for AGI in specialized scientific domains may be shorter than
previously estimated. The focus for research institutions will likely shift toward creating more \"verifiable\" environments like FrontierMath, where the answer is unknown, but the criteria for a
correct answer are strictly defined. ### FAQ\n\nWhat is the FrontierMath benchmark? FrontierMath is a high-difficulty mathematics dataset created by Epoch AI. It consists of 350 original problems
designed to test AI on research-level mathematics that cannot be found in existing training sets. How did GPT-5.4 solve an open problem? The model used a combination of Python for generating
constructions and Lean for formal verification. It iteratively tested different algorithmic approaches until it found a hypergraph construction that met the requirements of the   ...    Is
GPT-5.4\u2019s math solution officially verified?   ...    How does GPT-5.4 differ from o1 in math performance? GPT-5.4 exhibits a higher accuracy rate on Tier 4 problems (research level) compared to
o1\u2019s 2% accuracy. It also shows   ...    sound. By using Lean, AI models can provide \"guaranteed\" proofs that do not suffer from the hallucinations common in natural language outputs. What
specific math problem did the model solve? The model solved a problem regarding hypergraph construction and the lower bound of a sequence H(n), successfully extending a known construction from a 2022
research paper to reach a new,"], "published_date": "2026-03-14T16:00:00.000", "score": null}, {"title": "First AI solution on FrontierMath: Open Problems", "url": "https://vuink.com/post/rcbpunv-d-
dfhofgnpx-d-dpbz/p/first-ai-solution-on-frontiermath", "snippet": "First AI solution on FrontierMath: Open Problems\n\nInvalid email/password combination.\n\nSubmit a link\n\nPlease enter
url.\n\nLoading ...\n\n\n\n# First AI solution on FrontierMath: Open Problems\n\nsubmited by\n\nStyle Pass\n\n2026-03-23 19:30:11\n\nThe newly-solved problem came from Will Brian, who had placed it in
the Moderately Interesting category. It is a conjecture from a paper he wrote with Paul Larson in 2019. They were unable to solve it at the time, or in several attempts since. Brian had this to say.",
"highlights": ["First AI solution on FrontierMath: Open Problems\n\nInvalid email/password combination.\n\nSubmit a link\n\nPlease enter url. Loading ...\n\n\n\n# First AI solution on FrontierMath:
Open Problems\n\nsubmited by\n\nStyle Pass\n\n2026-03-23 19:30:11 The newly-solved problem came from Will Brian, who had placed it in the Moderately Interesting category. It is a conjecture from a
paper he wrote with Paul Larson in 2019. They were unable to solve it at the time, or in several   ...    Brian plans to write up the solution for publication, possibly including follow-on work
spurred by the AI\u2019s ideas. This matches his prospective assessment: a solution would be publishable in a standard speciality journal, and would be fairly likely to generate new questions.
Congratulations to Kevin Barreto and Liam Price, who first elicited a solution from GPT-5.4 Pro! They have the option   ...    thereafter. We have replicated this elicitation in our scaffold for
testing models on the problems. In this scaffold, Gemini 3.1 Pro, GPT-5.4 (xhigh), and Opus 4.6 (max) are all capable of solving the problem at least some of the time. For more about the problem,
including a full chat transcript showing GPT-5.4 Pro\u2019s original solution, and other models\u2019 solutions in our harness, see the problem page on our website. Read more epochai.subs...\n\nShare
:  \n\nComment\n\n###### Related Posts\n\n## FrontierMath: Open Problems\n\nComment ## What I Wish I Knew About FrontierMath - by Greg Burnham\n\nComment\n\n## A Ramsey-style Problem on
Hypergraphs\n\nComment ## FrontierMath Competition: Setting Benchmarks for AI Evaluation\n\nComment ## Clarifying the Creation and Use of the FrontierMath Benchmark\n\nComment ## FrontierMath: A
Benchmark for Evaluating Advanced Mathematical Reasoning in AI\n\nComment ## FrontierMath Tier 4 | Epoch AI\n\nComment ## OpenAI\u2019s o3 AI model scores lower on a benchmark than the company
initially implied\n\nComment ## AI\u2019s math problem: FrontierMath benchmark shows how far technology still has to go\n\nComment\n\n###### Recent Posts   ...    ## Search code, repositories, users,
issues, pull requests...\n\nComment\n\n###### Related External Posts ###### Introducing FrontierMath: Open Problems - Epoch AI\n\n\n\n###### Introducing FrontierMath: Open Problems - Epoch AI ######
Which lab's AI will be the first to score over 10% on FrontierMath ... ###### First AI Erd\u0151s solve and now first AI FrontierMath open problem solve Cool ###### First AI Erd\u0151s solve and now
first AI FrontierMath open problem solve Cool ###### First AI Erd\u0151s solve and now first AI FrontierMath open problem solve Cool ###### OpenAI to Open First India Office in New Delhi: A New AI
Chapter for ... ###### Open AI's O3 Benchmarking: Redefining Standards in AI Performance ###### Epoch AI Unveils FrontierMath: A New Frontier in Testing AI's ... ###### Will an AI score over 10% on
FrontierMath Benchmark in 2025 | Manifold ###### FrontierMath: New AI Benchmark Exposes Limitations in Advanced ...   ...    ###### FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch
AI ###### OpenAI\u2019s new reasoning AI model achieves human level results on ... ###### What will be true of the SOTA AI on the FrontierMath benchmark, before ... ###### Gemini 3 Pro Hits 38% on
FrontierMath as Google Takes Lead in AI ... ###### Is AI already superhuman on FrontierMath? - by Anson Ho ###### We evaluated top AI models on FrontierMath, our challenging math ... ###### AI model
scores \u2265 90% on FrontierMath Benchmark before 2027? Odds ... ###### Here are the first Epoch AI Tier 4 results! | Ken Ono ###### FrontierMath: LL"], "published_date": null, "score": null},
{"title": "Benchmarking AI on unsolved math problems", "url": "https://epoch.ai/frontiermath/open-problems/about", "snippet": "Benchmarking AI on unsolved math problems | Epoch AI\n\n \n\n##
FrontierMath: Open Problems\n\nThis work was supported by a grant from Schmidt Sciences.\n\nAI math capabilities have come far and fast. In mid-2024, high school math was still a challenge. By the end
of 2025, AI systems were solving extremely hard problems designed to be solvable only by top human experts. As we write this, it seems likely that AI systems will soon be able to solve problems that
no human has solved before.\n\nIndeed, there a", "highlights": ["Benchmarking AI on unsolved math problems | Epoch AI\n\n \n\n## FrontierMath: Open Problems This work was supported by a grant from
Schmidt Sciences. AI math capabilities have come far and fast. In mid-2024, high school math was still a challenge. By the end of 2025, AI systems were solving extremely hard problems designed to be
solvable only by top human experts. As we write this, it seems likely that AI systems will soon be able to solve problems that no human has solved before.   ...    had humans previously tried to solve
them? Does this say anything new about AI capabilities? Today we are releasing a pilot version of a new benchmark, FrontierMath: Open Problems, which we hope will shed light on this topic. The
benchmark consists of open problems from research mathematics that professional mathematicians have tried and failed to solve. To facilitate evaluation at scale, we include only problems for which
proposed solutions can be verified programmatically. At the time of release, to the best of our knowledge, none of these problems have been solved by humans or AI systems. If an AI system solves any
problem, it will be a meaningful advance in the frontier of human knowledge. Moreover, we   ...    significance of the problems, ranging from moderately interesting results to major breakthroughs. The
pilot release consists of 14 problems with: - Write-ups explaining the problem\u2019s significance and difficulty - Precise prompts that can be given to AI systems \u2013 try them yourself! - Initial
attempts by AI systems to solve the problems We will add more problems in the coming months and are actively commissioning contributions. See our problem proposal   ...    As for the verifiers \u2014
the programs that evaluate candidate solutions \u2014 we offer access for a fee. We structure access   ...    with us to help fund further expansion. We commit to grant access uniformly, and not
exclusively to any entity. Inquire at [[email protected]]. ## Example problems\n\nField: Combinatorics\n\nModerately interesting Let \\(B_n\\) denote a triangular book graph on \\(n\\) vertices. For a
given \\(n\\), construct a graph showing that the Ramsey number \\(R(B_{n-1}, B_n)\\) is greater than \\(4n - 2\\). Finding a general construction for \\(R(B_{n-1}, B_n)\\) would be of interest to
computational graph theorists. Such a   ...    Construct a family of explicit normal projective KLT del Pezzo surfaces \\(X\\) over an algebraically closed field of   ...    Paolo Cascini Professor of
Math, University College London\n\nRead more about this problem\n\nField: Number theory Major advance Find a degree \\(23\\) polynomial in \\(\\mathbb{Z}[x]\\) whose splitting field over
\\(\\mathbb{Q}\\) has Galois group \\(M_{23}\\). The inverse Galois problem is one of the most basic open questions in number theory, asking for the construction of polynomials with prescribed
symmetries. This is the minimal case for which the problem is open; it is especially   ...    Daniel Litt Assistant Professor of Mathematics, University of Toronto\n\nRead more about this
problem\n\nField: Topology Breakthrough Give an algorithm that takes a knot as input and determines whether the unknotting number of the knot is equal to one. This problem is one of the fundamental
questions in low-dimensional topology. It asks a basic question about how hard   ...    Joel Hass Professor, Department of Mathematics, University of California, Davis\n\nRead more about this problem
## Problems are mathematically meaningful, diverse, and hard Problems are contributed by professional mathematicians. Contributors suggest problems they are familiar with from   ...    Our goal is to
find problems that are meaningful to mathematicians on their own terms. We do not select problems to be   ...    Problems cover a range of mathematical topic areas. The pilot set has a tilt toward
combinatorics and number theory,   ...    See the problem proposal form for more details on the problem sourcing process.   ...    ## Solved problems will be removed from the benchmark If a problem is
solved \u2014 whether by humans or AI \u2014 the result will be published.8 Thus, any future AI system attempting the same problem would simply be able to look up the solution. For this reason, we
will remove solved problems from the   ...    While this \u201cfirst-to-solve\u201d set-up is atypical, we don\u2019t think it undermines the value of the Open Problems benchmark   ...    Most
immediately, this benchmark asks whether AI can solve unsolved math problems. We think this also helps us track   ...    ## We hope to see strong attempts to get AI systems to solve these problems Our
primary goal is to understand the frontier of AI math capabilities. However, it is not clear how best to elicit AI capabilities on the benchmark problems. So far we have tried simply prompting GPT-5.2
Pro and Gemini 3 Deep Think in their web apps.10 The results of this are shown on the individual problem pages. In this setting the models are generally capable of solving \u201cwarm-up\u201d
problems:   ...    To paraphrase Douglas Adams: We love goalposts. We love the whooshing noise they make as they go by.\n\n \n\n"], "published_date": "2026-01-27T00:00:00.000", "score": null}]
```

## 💬 Response

Now I have a comprehensive picture. Let me synthesize the key information.

**Key facts:**
- 15 total open problems across 4 tiers: Moderately interesting (4), Solid result (5), Major advance (3), Breakthrough (3)
- Currently **1 problem solved**: Ramsey Hypergraphs (Moderately interesting tier), solved March 23, 2026 by GPT-5.4 Pro
- 1 problem removed (March 5) - not counted as solved
- Small Diophantine has **partial** progress (3/9 equations solved) but is NOT marked as solved; remaining 6 need "a genuinely new mathematical approach"
- Resolution date: May 1, 2026 (~20 days from now)
- Multiple frontier models can solve the one already-solved problem: GPT-5.4 Pro, Opus 4.6, Gemini 3.1 Pro
- The Manifold market for full-year 2026 gives ~15% each to 1, 2, 3, and 14% to 4

Let me check the X/Twitter for any breaking news on new solves.

## 🔧 Tool: mcp__asknews__search_x_twitter


```json
{
  "advanced_search_expression": "FrontierMath solved open problem since:2026-04-01_00:00:00_UTC"
}
```

### 📋 Result

```
{"as_string":"------Web Search Results Start------\n<web_doc>\nCitation key: [0]\nTitle: X post from Riko Suminoe 🏳️‍🌈🇵🇸\n\nKey Points: Content: @agstcptl93841 @nicbarkeragain Then how the hell it's
solved some Erdos problems, and Terrence Tao who was skeptical not while ago, now uses LLMs in his research?\nFrontierMath Open problem, solved by LLM.\nIt's not just math, it's math you can't even
imagine doing.\nRetweets: 0\nLikes: 1\nReplies: 2\nQuotes: 0\n\nPublished date: April 09 2026, 04:11\n\nURL: https://x.com/RikoSuminoe69/status/2042092991243022709\n\nSource: X (formerly
Twitter)\n</web_doc>\n------Web Search Results End------\n\n\n------Web Search Results Start------\n------Web Search Results End------\n\n\n","as_dicts":[],"offset":null}
```

## 🔧 Tool: mcp__search__web_search


```json
{
  "query": "site:epoch.ai frontiermath open-problems solved 2026"
}
```

### 📋 Result

```
{"query": "site:epoch.ai frontiermath open-problems solved 2026", "results": [{"title": "FrontierMath: Open Problems - Unsolved Mathematical Challenges | Epoch AI", "url":
"https://epoch.ai/frontiermath/open-problems/", "snippet": "A collection of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would
meaningfully advance the state of human mathematical knowledge.\n2026-03-05: We removed one problem from the benchmark, as we have determined that any solution would not meet our bar of being a
publishable result in its own right. The problem page remains up: see it for more info on an AI-generated solution and subsequent human elaboration.", "api_data": null, "hint": null}, {"title":
"Benchmarking AI on unsolved math problems | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/about/", "snippet": "FrontierMath: Open Problems\nThis work was supported by a grant from
Schmidt Sciences.\nAI math capabilities have come far and fast. In mid-2024, [high school math](https://epoch.ai/benchmarks/math-level-5) was still a challenge. By the end of 2025, AI systems were
solving [extremely hard problems](https://epoch.ai/frontiermath/tiers-1-4/about) designed to be solvable only by top human experts. As we write this, it seems likely that AI systems will soon be able
to solve problems that no human has ", "api_data": null, "hint": null}, {"title": "A Ramsey-style Problem on Hypergraphs | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/ramsey-
hypergraphs/", "snippet": "Solution update\nThis problem has been solved! A solution was first elicited by Kevin Barreto and Liam Price, using GPT-5.4 Pro. This solution was confirmed by problem
contributor Will Brian, and will be written up for publication. A full transcript of the original conversation with GPT-5.4 Pro can be found [here](https://epoch.ai/files/open-problems/gpt-5-4-pro-
hypergraph-ramsey.txt) and GPT-5.4 Pro\u2019s write-up from the end of that transcript can be found [here](https://epoch.ai/files/open-proble", "api_data": null, "hint": null}, {"title": "Finiteness
Problem for Diophantine Equations | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/small-diophantine", "snippet": "About the problem\nDefine a heuristic \u201csize\u201d of a
Diophantine equation by substituting \\(2\\) for all variables and absolute values of coefficients for all coefficients. For instance \\(x^2 - 2y^2 -1\\) has size \\(13\\).\nThe finiteness problem for
a Diophantine equation asks whether the equation has infinitely many solutions. This problem is about the nine equations with size \\(\\leq 24\\) where the finiteness problem is open. Numerical
evidence suggests that these equations all have infinitely many so", "api_data": null, "hint": null}, {"title": "Hadamard Matrices | Epoch AI", "url": "https://epoch.ai/frontiermath/open-
problems/hadamard/", "snippet": "About the problem\nA [Hadamard matrix](https://en.wikipedia.org/wiki/Hadamard_matrix) is a square matrix all of whose entries are \\(\\pm 1\\) and whose rows are
mutually orthogonal. Beyond trivial cases, the order of such a matrix must be a multiple of four. The Hadamard conjecture states that a Hadamard matrix exists for every such order. It remains
open.\nMathematicians have chipped away at finding examples of Hadamard matrices of larger and larger order. The smallest case for which no matrix is k", "api_data": null, "hint": null}, {"title":
"Explicit Deformations of Algebras | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/explicit-deformations", "snippet": "About the problem\nUpdate (2026-03-12): We have determined that
any solution to this problem would not meet our bar of being a publishable result in its own right. As a result, we have removed the problem from the benchmark.\nThe problem consists of finding an
explicit deformation from a specific curvilinear algebra to a specific monomial algebra. It is an instance of a more general problem, namely finding a general strategy for constructing such explicit
deformations. It is this more general prob", "api_data": null, "hint": null}, {"title": "FrontierMath: LLM Benchmark for Advanced AI Math Reasoning | Epoch AI", "url":
"https://epoch.ai/frontiermath/", "snippet": "FrontierMath includes both carefully crafted challenge problems and open research problems that remain unsolved by mathematicians.\nA benchmark of several
hundred unpublished, highly challenging mathematics problems. Difficulty Tiers 1-3 cover undergraduate through early postdoc level problems, while Tier 4 is research-level mathematics.\nA collection
of unsolved mathematics problems that have resisted serious attempts by professional mathematicians. AI solutions would meaningfully advance the sta", "api_data": null, "hint": null}, {"title": "Epoch
AI 2025 impact report | Epoch AI", "url": "https://epoch.ai/blog/epoch-impact-report-2025", "snippet": "In 2025, we saw AI continue to increase in scale and importance. AI companies reached [annual
revenues totalling tens of billions of dollars](https://epochai.substack.com/p/new-ai-companies-data-hub), and are building data centers that individually [cost comparable
amounts](https://epoch.ai/data/data-centers). Leading benchmarks show capabilities [accelerating](https://epoch.ai/data-insights/ai-capabilities-progress-has-sped-up), propped up by the establishment
of reasoning models, such as OpenA", "api_data": null, "hint": null}, {"title": "Ramsey Numbers for Book Graphs | Epoch AI", "url": "https://epoch.ai/frontiermath/open-problems/ramsey-book-graphs",
"snippet": "About the problem\nThis problem aims to determine the Ramsey numbers \\(R(B_{n-1}, B_n)\\), where \\(B_n\\) denotes a triangular [book
graph](https://en.wikipedia.org/wiki/Book_(graph_theory)) on \\(n\\) vertices. The upper bound \\(R(B_{n-1}, B_n) \\le 4n - 1\\) was established in 1978, and was more recently shown to be sharp for an
infinite family of \\(n\\) as well as for all \\(n \\le 21\\).\nGiven these results, it seems likely that the upper bound is sharp for all \\(n\\). The goal of this problem is to pro", "api_data":
null, "hint": null}, {"title": "FrontierMath Problems | Epoch AI", "url": "https://epoch.ai/frontiermath/benchmark-problems", "snippet": "Tier 4\nThis extreme tier consists of 50 problems crafted as
short-term research projects by professors and postdocs. They are designed to surpass Tier 3 in difficulty, with some potentially remaining unsolved by AI for decades.\nAn optimization problem in BMO
space\nLet\n\\[ c = \\sup_{f} \\int_{0}^{1} (f(t)^{3}+|f(t)|)dt\\]where supremum is taken over all integrable functions \\(f : [0,1] \\to \\mathbb{R}\\) such that \\(\\int_{0}^{1}f(t)dt=-10\\),
\\(\\int_{0}^{1} f^{2}(t)dt=100+\\frac{1}{12}\\), and\n\\[ \\sup_{J", "api_data": null, "hint": null}]}
```

## 💬 Response

Good. No new solves have been announced beyond the Ramsey Hypergraphs one. Now let me run my reflection.

## 🔧 Tool: mcp__notes__reflection


```json
{
  "factors": [
    {
      "description": "Status quo: Currently 1 problem solved (Ramsey Hypergraphs). If nothing changes, the count stays at 1.",
      "supports": "1 or fewer",
      "logit": 1.5,
      "confidence": 0.95
    },
    {
      "description": "Small Diophantine has partial progress (3/9 equations) but remaining 6 need 'genuinely new mathematical approach' - unlikely to be fully solved in 20 days",
      "supports": "1 or fewer",
      "logit": 0.7,
      "confidence": 0.8
    },
    {
      "description": "Multiple frontier AI models (GPT-5.4 Pro, Opus 4.6, Gemini 3.1 Pro) are actively being tested on these problems, and AI math capabilities are advancing rapidly (2% to 50% on FrontierMath Tiers 1-4 in ~18 months)",
      "supports": "2",
      "logit": 0.8,
      "confidence": 0.6
    },
    {
      "description": "Most remaining problems are in harder tiers (Solid result, Major advance, Breakthrough) - only 3 unsolved 'Moderately interesting' problems remain, and these already resisted GPT-5.4 Pro attempts",
      "supports": "1 or fewer",
      "logit": 0.8,
      "confidence": 0.75
    },
    {
      "description": "Short time window: only ~20 days until May 1 resolution. Even if a solution is found, verification by problem contributors and update to the website takes time.",
      "supports": "1 or fewer",
      "logit": 0.6,
      "confidence": 0.8
    },
    {
      "description": "No new model releases or breakthroughs announced in the last 2-3 weeks. The last solve (Ramsey Hypergraphs) was March 23, nearly 3 weeks ago with no additional solves since.",
      "supports": "1 or fewer",
      "logit": 0.5,
      "confidence": 0.7
    },
    {
      "description": "Manifold market for full-year 2026 gives ~15% to just 1 solve and ~15% to 2 solves, meaning cumulative P(<=1 by EOY) is only ~15%. But this question is only about May 1, meaning less time for solves.",
      "supports": "2",
      "logit": 0.3,
      "confidence": 0.5,
      "conditional": "If Manifold is well-calibrated for full year"
    },
    {
      "description": "Possibility of a new frontier model release (e.g., GPT-5.5, Claude 5, Gemini 4) in the next 20 days that could crack additional problems",
      "supports": "Greater than 2",
      "logit": 0.5,
      "confidence": 0.25
    }
  ],
  "tentative_estimate": {
    "probabilities": {
      "2": 0.22,
      "1 or fewer": 0.7,
      "Greater than 2": 0.08
    }
  },
  "assessment": "The current state is clear: 1 problem solved (Ramsey Hypergraphs), with partial progress on Small Diophantine (3/9 equations). The resolution is in ~20 days.\n\n**For \"1 or fewer\" (status quo):** This is strongly favored. The solved count has been 1 since March 23. No new solves have been announced in the ~19 days since. The Small Diophantine needs 6 more equations solved with \"a genuinely new mathematical approach.\" Most other problems are in harder tiers. Verification and website updates add friction even if a solution is found.\n\n**For \"2\":** The main pathway is either: (a) Small Diophantine being fully completed (unlikely given 6/9 remaining equations needing new approaches), (b) another Moderately interesting problem being cracked, or (c) a lower-tier problem being surprisingly solved. Multiple strong AI models exist and are being tested. The question description itself flags the second solve as \"a live near-term milestone,\" suggesting it's plausible but not imminent.\n\n**For \">2\":** Would require at least 3 problems solved. Given only 1 has been solved in ~3 months of the benchmark existing, solving 2+ more in 20 days would be extraordinary. The main risk is a step-change in AI capability (new model release) that simultaneously cracks multiple problems, but this is speculative.\n\n**Counterargument against my estimate:** AI capabilities are advancing extremely rapidly. The Ramsey solve showed that once models cross a capability threshold, multiple models can solve the same problem. A new model could potentially solve several problems at once. But: these problems were designed to resist exactly this, and the harder tiers have successfully resisted all attempts so far.\n\n**Base rate check:** 1 problem solved in ~10 weeks of the benchmark existing = ~0.1 solves/week. In 3 weeks, expected value is ~0.3, suggesting P(any new solve) \u2248 25-30%, which aligns with my ~30% for 2+.",
  "calibration_notes": "Base rate: ~1 solve in 10 weeks \u2248 0.1/week. In 3 weeks: Poisson \u03bb=0.3 gives P(0 new)=74%, P(1 new)=22%, P(2+ new)=4%. My estimates are slightly more bullish on >2 (8% vs 4%) to account for the possibility of discontinuous AI progress.",
  "key_uncertainties": "1. Whether a new frontier AI model will be released before May 1 that significantly exceeds current capabilities. 2. Whether the Small Diophantine problem's remaining equations will yield to current approaches or require genuinely new mathematics. 3. Whether solutions found but not yet verified/announced exist in the pipeline.",
  "update_triggers": "- Announcement of a new frontier model (GPT-5.5, Claude 5, etc.) would shift probability toward 2 and >2. - Epoch AI announcing another solve would obviously change the count. - Small Diophantine progress announcement (additional equations solved) would increase P(2).",
  "tool_audit": "Useful: web_search returned comprehensive results on the state of FrontierMath. fetch_url successfully extracted problem status details from Epoch AI pages. search_exa provided good supplementary articles. manifold_price confirmed market pricing. Failed: search_news hit rate limits (403). search_x_twitter returned minimal results but no new solve announcements. The fetch_url of the main open problems page didn't render the full problem list (likely JavaScript-rendered), but individual problem pages worked well.",
  "process_reflection": "The research phase went smoothly for this question. The combination of web_search and fetch_url gave me a clear picture of the current state. The main gap was the inability to see the full rendered page at epoch.ai/frontiermath/open-problems/ which likely requires JavaScript rendering - but I was able to piece together the status from individual problem pages and news articles. The Manifold market data for the full-year question was helpful as a calibration anchor, though I had to adjust for the shorter time window. The news search rate limit was a minor inconvenience but web_search compensated. Overall the scaffolding worked well for this type of question."
}
```

### 📋 Result

```
{"factor_count": 8, "factor_sum": 4.17, "neutral_factor_count": 0, "factor_breakdown": [{"description": "Status quo: Currently 1 problem solved (Ramsey Hypergraphs). If nothing changes, the count
stays at 1.", "supports": "1 or fewer", "logit": 1.5, "confidence": 0.95, "effective_logit": 1.4249999999999998}, {"description": "Small Diophantine has partial progress (3/9 equations) but remaining
6 need 'genuinely new mathematical approach' - unlikely to be fully solved in 20 days", "supports": "1 or fewer", "logit": 0.7, "confidence": 0.8, "effective_logit": 0.5599999999999999},
{"description": "Multiple frontier AI models (GPT-5.4 Pro, Opus 4.6, Gemini 3.1 Pro) are actively being tested on these problems, and AI math capabilities are advancing rapidly (2% to 50% on
FrontierMath Tiers 1-4 in ~18 months)", "supports": "2", "logit": 0.8, "confidence": 0.6, "effective_logit": 0.48}, {"description": "Most remaining problems are in harder tiers (Solid result, Major
advance, Breakthrough) - only 3 unsolved 'Moderately interesting' problems remain, and these already resisted GPT-5.4 Pro attempts", "supports": "1 or fewer", "logit": 0.8, "confidence": 0.75,
"effective_logit": 0.6000000000000001}, {"description": "Short time window: only ~20 days until May 1 resolution. Even if a solution is found, verification by problem contributors and update to the
website takes time.", "supports": "1 or fewer", "logit": 0.6, "confidence": 0.8, "effective_logit": 0.48}, {"description": "No new model releases or breakthroughs announced in the last 2-3 weeks. The
last solve (Ramsey Hypergraphs) was March 23, nearly 3 weeks ago with no additional solves since.", "supports": "1 or fewer", "logit": 0.5, "confidence": 0.7, "effective_logit": 0.35}, {"description":
"Manifold market for full-year 2026 gives ~15% to just 1 solve and ~15% to 2 solves, meaning cumulative P(<=1 by EOY) is only ~15%. But this question is only about May 1, meaning less time for
solves.", "supports": "2", "logit": 0.3, "confidence": 0.5, "effective_logit": 0.15, "conditional": "If Manifold is well-calibrated for full year"}, {"description": "Possibility of a new frontier
model release (e.g., GPT-5.5, Claude 5, Gemini 4) in the next 20 days that could crack additional problems", "supports": "Greater than 2", "logit": 0.5, "confidence": 0.25, "effective_logit": 0.125}],
"dominant_factor": "Status quo: Currently 1 problem solved (Ramsey Hypergraphs). If nothing changes, the count stays at 1.", "dominant_effective_logit": 1.4249999999999998, "outcome_breakdown":
[{"outcome": "1 or fewer", "factor_count": 5, "logit_sum": 3.415, "factors": [{"description": "Status quo: Currently 1 problem solved (Ramsey Hypergraphs). If nothing changes, the count stays at 1.",
"supports": "1 or fewer", "logit": 1.5, "confidence": 0.95, "effective_logit": 1.4249999999999998}, {"description": "Small Diophantine has partial progress (3/9 equations) but remaining 6 need
'genuinely new mathematical approach' - unlikely to be fully solved in 20 days", "supports": "1 or fewer", "logit": 0.7, "confidence": 0.8, "effective_logit": 0.5599999999999999}, {"description":
"Most remaining problems are in harder tiers (Solid result, Major advance, Breakthrough) - only 3 unsolved 'Moderately interesting' problems remain, and these already resisted GPT-5.4 Pro attempts",
"supports": "1 or fewer", "logit": 0.8, "confidence": 0.75, "effective_logit": 0.6000000000000001}, {"description": "Short time window: only ~20 days until May 1 resolution. Even if a solution is
found, verification by problem contributors and update to the website takes time.", "supports": "1 or fewer", "logit": 0.6, "confidence": 0.8, "effective_logit": 0.48}, {"description": "No new model
releases or breakthroughs announced in the last 2-3 weeks. The last solve (Ramsey Hypergraphs) was March 23, nearly 3 weeks ago with no additional solves since.", "supports": "1 or fewer", "logit":
0.5, "confidence": 0.7, "effective_logit": 0.35}]}, {"outcome": "2", "factor_count": 2, "logit_sum": 0.63, "factors": [{"description": "Multiple frontier AI models (GPT-5.4 Pro, Opus 4.6, Gemini 3.1
Pro) are actively being tested on these problems, and AI math capabilities are advancing rapidly (2% to 50% on FrontierMath Tiers 1-4 in ~18 months)", "supports": "2", "logit": 0.8, "confidence": 0.6,
"effective_logit": 0.48}, {"description": "Manifold market for full-year 2026 gives ~15% to just 1 solve and ~15% to 2 solves, meaning cumulative P(<=1 by EOY) is only ~15%. But this question is only
about May 1, meaning less time for solves.", "supports": "2", "logit": 0.3, "confidence": 0.5, "effective_logit": 0.15, "conditional": "If Manifold is well-calibrated for full year"}]}, {"outcome":
"Greater than 2", "factor_count": 1, "logit_sum": 0.125, "factors": [{"description": "Possibility of a new frontier model release (e.g., GPT-5.5, Claude 5, Gemini 4) in the next 20 days that could
crack additional problems", "supports": "Greater than 2", "logit": 0.5, "confidence": 0.25, "effective_logit": 0.125}]}], "mc_distribution_metrics": {"implied_probabilities": {"1 or fewer":
0.9099322337352794, "2": 0.05616928786838427, "Greater than 2": 0.03389847839633634}, "tentative_probabilities": {"2": 0.22, "1 or fewer": 0.7, "Greater than 2": 0.08}, "per_option_gap_pp": {"1 or
fewer": -20.993223373527947, "2": 16.383071213161575, "Greater than 2": 4.610152160366366}, "max_gap_pp": -20.993223373527947, "max_gap_option": "1 or fewer"}, "sources": ["[(Metaculus) How many
problems solved by AI will the official FrontierMath Open Problems index show on May 1, 2026?](https://www.metaculus.com/questions/43127)", "[FrontierMath: Open Problems - Unsolved Mathematical
Challenges](https://epoch.ai/frontiermath/open-problems/)", "[A Ramsey-style Problem on Hypergraphs](https://epoch.ai/frontiermath/open-problems/ramsey-hypergraphs/)", "[Introducing FrontierMath: Open
Problems](https://epochai.substack.com/p/introducing-frontiermath-open-problems)", "[FRONTIERMATH: A BENCHMARK FOR EVALUATING ADVANCED MATHEMATICAL REASONING IN AI](https://arxiv.org/pdf/2411.04872)",
"[On the smallest open Diophantine equations](https://arxiv.org/pdf/2204.11624)", "[(Manifold) How many FrontierMath Open Problems solved in 2026?](https://manifold.markets/bh/how-many-frontiermath-
open-problems)", "[(Manifold) Will Moltbook solve any open FrontierMath problems in 2026?](https://manifold.markets/ChaosIsALadder/will-moltbook-solve-any-open-proble)", "[Finiteness Problem for
Diophantine Equations](https://epoch.ai/frontiermath/open-problems/small-diophantine)", "[Benchmarking AI on unsolved math problems](https://epoch.ai/frontiermath/open-problems/about/)", "[From
Erd\u0151s to Axiom: 12 Open Problems AI Has Actually Solved](https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/)"], "reviewer_critique":
"**Evidence Verification:**\n\nAll core factual claims in the factors are grounded in the research trace:\n\n1. **Factor 1 (1 problem solved - Ramsey Hypergraphs)**: Verified. Trace confirms via The
Neuron article and Epoch AI pages: \"Ramsey Hypergraphs - Solved March 23, 2026\" by GPT-5.4 Pro.\n\n2. **Factor 2 (Small Diophantine 3/9, \"genuinely new approach\" needed)**: Verified. The fetch_url
result for the Small Diophantine page confirms \"Partially solved (3 of 9 equations resolved)\" and \"They believe resolving all 9 equations will require a genuinely new mathematical approach.\"\n\n3.
**Factor 3 (AI math capability advancement)**: Minor imprecision but directionally correct. Trace shows \"5% under GPT-4 in 2024 to 50% under GPT-5.4 Pro in March 2026\" (Winbuzzer article) and \"o1
maintained an accuracy rate of roughly 2%\" on Tier 4. The factor's \"2% to 50%\" conflates these slightly, but the underlying point about rapid capability growth is well-supported.\n\n4. **Factor 4
(3 unsolved Moderately interesting problems)**: Verified. Trace confirms 4 Moderately interesting total, 1 solved = 3 remaining.\n\n5. **Factor 5 (20 days until resolution)**: Verified. Published
April 11, resolves May 1.\n\n6. **Factor 6 (March 23 last solve)**: Verified directly from trace.\n\n7. **Factor 7 (Manifold market probabilities)**: Verified. Trace shows \"15% 1, 15% 2, 16% 3, 14%
4\" for the full-year market.\n\n8. **Factor 8 (New model possibility)**: Appropriately speculative with 0.25 confidence.\n\n**Resolution Criteria**: Present and correctly engaged. The agent fetched
and analyzed the official index (epoch.ai/frontiermath/open-problems/) that the resolution criteria specify.\n\n**No Double-Counting Issues**: Factors 1 and 6 both reference current state but serve
different analytical purposes (baseline vs. momentum).\n\n**No Wrong-Direction Factors**: All logit signs correctly correspond to their outcome labels.\n\n**Adversarial Reasoning Present**: Assessment
addresses the counterargument about rapid AI capability advancement.\n\n**Probability Assessment**: The 70/22/8 split is well-calibrated to the evidence. The base rate calculation (1 solve in ~10
weeks \u2192 ~25-30% chance of new solve in 3 weeks) supports ~70% for status quo. My independent estimate would be 65-75% for \"1 or fewer,\" consistent with the agent's 70%."}
```

## 💬 Response

The reflection reviewer approved my analysis. Let me finalize the forecast.

## 🔧 Tool: StructuredOutput


```json
{
  "summary": "Currently 1 FrontierMath Open Problem is solved (Ramsey Hypergraphs, solved March 23, 2026 by GPT-5.4 Pro). With only ~20 days until the May 1 resolution date, the status quo of 1 solved problem is heavily favored. The Small Diophantine problem has partial progress (3/9 equations) but the remaining 6 require \"a genuinely new mathematical approach.\" Most remaining problems are in harder tiers that have resisted all AI attempts. The Poisson base rate (~0.1 solves/week, \u03bb=0.3 for 3 weeks) gives ~74% chance of no new solve, consistent with my estimate. The main upside risk is a new frontier model release or an unexpected breakthrough on a Moderately interesting problem.",
  "probabilities": {
    "2": 0.22,
    "1 or fewer": 0.7,
    "Greater than 2": 0.08
  },
  "factors": [
    {
      "description": "Status quo: Currently 1 problem solved (Ramsey Hypergraphs). If nothing changes, the count stays at 1.",
      "supports": "1 or fewer",
      "logit": 1.5,
      "confidence": 0.95
    },
    {
      "description": "Small Diophantine has partial progress (3/9 equations) but remaining 6 need 'genuinely new mathematical approach' - unlikely to be fully solved in 20 days",
      "supports": "1 or fewer",
      "logit": 0.7,
      "confidence": 0.8
    },
    {
      "description": "Multiple frontier AI models (GPT-5.4 Pro, Opus 4.6, Gemini 3.1 Pro) are actively being tested on these problems, and AI math capabilities are advancing rapidly (2% to 50% on FrontierMath Tiers 1-4 in ~18 months)",
      "supports": "2",
      "logit": 0.8,
      "confidence": 0.6
    },
    {
      "description": "Most remaining problems are in harder tiers (Solid result, Major advance, Breakthrough) - only 3 unsolved 'Moderately interesting' problems remain, and these already resisted GPT-5.4 Pro attempts",
      "supports": "1 or fewer",
      "logit": 0.8,
      "confidence": 0.75
    },
    {
      "description": "Short time window: only ~20 days until May 1 resolution. Even if a solution is found, verification by problem contributors and update to the website takes time.",
      "supports": "1 or fewer",
      "logit": 0.6,
      "confidence": 0.8
    },
    {
      "description": "No new model releases or breakthroughs announced in the last 2-3 weeks. The last solve (Ramsey Hypergraphs) was March 23, nearly 3 weeks ago with no additional solves since.",
      "supports": "1 or fewer",
      "logit": 0.5,
      "confidence": 0.7
    },
    {
      "description": "Manifold market for full-year 2026 gives ~15% to just 1 solve, meaning most traders expect more than 1 by EOY. But May 1 is much sooner than EOY, limiting the window for additional solves.",
      "supports": "2",
      "logit": 0.3,
      "confidence": 0.5,
      "conditional": "If Manifold is well-calibrated for full year"
    },
    {
      "description": "Possibility of a new frontier model release (e.g., GPT-5.5, Claude 5, Gemini 4) in the next 20 days that could crack additional problems",
      "supports": "Greater than 2",
      "logit": 0.5,
      "confidence": 0.25
    }
  ]
}
```

### 📋 Result

```
Structured output provided successfully
```

## 💬 Response

## Forecast Summary

**Question:** How many FrontierMath Open Problems will be shown as AI-solved on May 1, 2026?

| Outcome | Probability |
|---------|------------|
| **1 or fewer** | **70%** |
| **2** | **22%** |
| **Greater than 2** | **8%** |

**Key reasoning:**

- **Current state:** 1 problem solved (Ramsey Hypergraphs, March 23 by GPT-5.4 Pro) out of 15 total problems across 4 difficulty tiers
- **Partial progress:** Small Diophantine has 3/9 equations solved but remaining 6 need "a genuinely new mathematical approach" — not close to a full solve
- **Time constraint:** Only ~20 days remain, and no new solves have occurred in the 19 days since the Ramsey solve
- **Difficulty gradient:** Most remaining problems are in harder tiers (Solid result, Major advance, Breakthrough) that have resisted all AI attempts
- **Base rate:** ~0.1 solves/week → Poisson λ=0.3 for 3 weeks gives ~74% chance of no new solve, aligning with the 70% estimate
- **Upside risk:** Rapid AI capability advancement and active testing by multiple labs create meaningful (~22%) probability of a second solve, but >2 solves would require extraordinary circumstances
