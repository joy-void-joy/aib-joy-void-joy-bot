# CAISI / OpenAI+Anthropic evaluation agreements — Q45203

**Question**: Will a U.S. federal agency officially announce new or materially expanded voluntary
agreements under which a federal agency evaluates frontier models from BOTH OpenAI and Anthropic,
after Aug 10 and before Sep 3, 2026 ET?

**Today**: 2026-08-20. Window Aug 11 – Sep 2. ~10 days elapsed, ~13 remain.

## Step 1 — resolution parse
- Resolver: Metaculus/AIB (CP hidden, 184 forecasters; twin question 44708 w/ 61).
- Needs: (1) a **U.S. federal agency** official announcement — company blog posts do NOT count;
  (2) coverage of **both** OpenAI and Anthropic (may be separate announcements);
  (3) if an expansion of a pre-existing arrangement, must identify a previously-not-covered
  model family / access arrangement / testing scope / evaluation domain.
- **"Already happened" check**: criteria give an explicit start date (Aug 10) BEFORE published_at
  (Aug 15) → Case 1. Events Aug 10–15 would count. Verified: none occurred.
  The Aug 4 White House framework briefing predates Aug 10 and does not count.
- Status quo = NO.

## Timeline
- Aug 29, 2024: AISI/NIST announces agreements with **both** Anthropic and OpenAI (MOUs, pre- and
  post-release access). ← the clearest historical instance of a qualifying announcement.
- Sep 25, 2025: CAISI "Works with OpenAI and Anthropic" — reports completed joint security work.
- Feb 27, 2026: Trump orders agencies to drop Anthropic; DoD designates it a supply-chain risk.
- Mar 2026: Anthropic sues; Mar 26 preliminary injunction. D.C. Circuit denied the second request.
- May 5, 2026: **CAISI announces agreements with Google DeepMind, Microsoft, xAI.** Release notes
  prior OpenAI/Anthropic partnerships "have been renegotiated"; Axios: spokesperson said those are
  "ongoing and reflect updated MOUs." 40+ evals completed; classified-environment testing; TRAINS
  Taskforce. → OpenAI/Anthropic MOU renegotiation was already announced BEFORE the window.
  *Note: the nist.gov press-release URL now 404s (Cybersecurity Dive editor's note confirms NIST
  removed it).*
- Jun 2, 2026: **EO 14409**. Sec. 3 (due Aug 1): classified benchmarking for "covered frontier
  model" + **design a voluntary framework** for up-to-30-day pre-release federal access.
  Explicitly not a licensing/preclearance regime.
- Jun 12–30, 2026: export-control ultimatum; Anthropic pulls Mythos 5 / Fable 5; lifted Jun 30.
- Jun 26, 2026: OpenAI gates GPT-5.6 Sol to admin-approved customers.
- Jul 17, 2026: CNBC — admin dictating frontier-model access; "Gold Eagle" clearinghouse launched.
- **Aug 3–4, 2026: framework FINALIZED; White House briefs OpenAI, Anthropic, Google, Meta, Nvidia,
  Microsoft.** Open-weight models excluded for now.
- **Aug 4, 2026: White House will NOT publicly release the framework** (Axios ×3 sources, WIRED,
  Fortune, CNBC, Reuters). Benchmarks classified. No requirement in the EO to publish.
- Aug 4, 2026: five Democratic senators ask Trump to work with Congress on statutory testing.
- Aug 7, 2026 (Nextgov): "No one is saying, officially, what was decided."
- Aug 17, 2026 (WIRED, via AI Weekly): unnamed WH official says framework "right now deals only
  with the closed models developed by the likes of Anthropic and OpenAI"; expected to extend to
  open models "in the coming months." ← in-window but an anonymous quote in a magazine, not an
  official agency announcement of a new/expanded agreement.
- **Aug 19, 2026 (The Information): "more than two weeks later, much of the AI sector remains in
  the dark... The White House has yet to share details of the framework publicly."**

## Assessment
YES requires a *government* announcement. Everything in the record says the government has
deliberately chosen not to make one, and has held that line for 15 days past the briefing.
Remaining window (~13 days) spans the deadest part of the DC calendar (August recess; Labor Day
Sep 7). Anthropic's litigation with DoD is unresolved, making a celebratory joint naming awkward.

Against that: a genuine live process where company sign-ons are the operative next step; a May 5
precedent of Commerce publicizing exactly this; political incentive to answer Senate pressure.

## Quantification (scenario mixture, 200k draws)
- Posture weights: secrecy holds 0.72 / partial pivot 0.20 / independent CAISI release 0.08
- P(announcement) 0.04 / 0.45 / 0.75; P(both cos | ann) 0.55 / 0.70 / 0.60; P(new scope) 0.80/0.88/0.85
- Core path 9.8%; + loose-resolution path (3.5%) → **12.9%**
- Sensitivity on pivot weight 0.10→0.40: 10.5% → 18.0%
- Pure frequency anchor (2.5 qualifying announcements / 24 months, 13-day window): **4.4%**

**Final: ~0.10** — the model's 13% leans on a pivot weight I think is generous given 15 days of
confirmed silence and an explicit non-publication decision; I weight the frequency anchor and the
secrecy evidence more heavily than the mechanical mixture does.

## Tool notes
- `news` lane DEAD all session (403: AskNews tier). `web` lane returned empty on every query.
  `neural` lane carried the entire research load — worked very well.
- Persisted large tool outputs land in a path the Read tool is not permitted to open, and the
  sandbox is a separate container, so oversized `search()` results were unrecoverable. Worked
  around by narrowing lanes to keep outputs inline.
- Metaculus CP hidden (expected for AIB). No relevant prediction markets exist.
