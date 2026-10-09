**Format:** LinkedIn Pulse Article (methodology)
**Series:** Quality Operating Model (slot FRI 09.10 LOCKED)
**Status:** draft v1 (W4, 30.09 — from W2 session record; needs W2 public/internal pass before publish)
**Cover:** DONE (`31-cover.png` + `.jpeg`, 1920×1080 — 68% green vs 0.242 red split, same-25-labels footer)
**Feed Image:** cover doubles as feed preview
**Hook:** 68% agreement with the expert — sounds respectable, until kappa 0.242. Same 25 labels, same sitting, failing grade.
**Constraints (W2, binding):** aggregates only (no W3 per-item labels without consent), no timings (unmeasured — omit), no private correspondence, no commercial/vendor strategy.

---

# How to Calibrate an AI Judge With 30 Human Labels and One Failing Grade

Seventeen out of twenty-five - 68% agreement with the expert — sounds respectable, until the statistician in the room says kappa is 0.242. Same labels, same sitting, failing grade — and that failing grade was the whole point.

I asked whether a free local judge could replace a cloud one. It called all 30 findings defects, with total conviction. Zero exact matches. Without human labels, that looks like diligence. A good judge is indistinguishable from a confident liar. So I built the ruler first: 25 blind labels, 68% agreement, kappa 0.242. Failing grade — and that failure was the whole point. What the ruler taught me fits in six rakes — step on them in advance, not in production.

### ❓ Problem

A judge outputs verdicts in words. Words are cheap, confidence is free, and nothing in the output tells you whether the judgment tracked reality. Our local judge proved it: every item is (?) a defect, zero exact matches, total conviction. Without gold labels, you cannot tell diligence from theater.

Before this track, we never needed labeling at all. Mutation testing carries its own oracle — we break the system ourselves, and killed-or-survived is observed through exit codes, not judged. Gold becomes mandatory if and only if an AI judgment stands between evidence and conclusion with no executable check in between. The rule for the future writes itself: no judgment, no labeling tax.

### 🧭 Solution

Thirty items, three worlds, one protocol. Gold-30 splits into three strata of ten: E (end-to-end survivors from our own mutation campaign — negated assertions the suite never caught), H (historical findings — crawler outputs, one real live-site bug, two public issue reports), U (unit-spec quirks — validation rules, retry helpers, parsers). Three different worlds, so the judge gets attacked from three angles.

Calibration came first: five worked examples, walked through jointly with the arbiter, excluded from scoring. Then twenty-five items labeled independently and blind. Labeling for the first time, you will ask these six questions — here are the answers that became protocol, so you don't pay for them twice:

- **What goes in the pointer field?** A reproducible trace — path plus lines. Pointers mandatory only for diverged items, at arbitration — nowhere else.
- **Can I submit without pointers?** Yes: labels and notes now feed the score; pointers get written only where arbitration demands them.
- **Where does the effort go?** Into severity calls, not into twenty-five pointers. Flag the unsure items, move on.
- **Do I assess the test or the system?** The system, by default — a test observation counts only if it reveals specified behavior nobody enforces. Never rate test code quality. (I asked this before the arbiter ruled it — first-timers find the hardest question free of charge.)
- **These mutant items confuse me — do we redo if we diverge?** Yes. A mutant is intentional breakage, survived means the suite stayed green, and the only question is whether a real bug of that shape would matter. Iteration guaranteed, no penalty for first-pass divergence.
- **Which items, and where do I stand?** Track state visibly from day one — status amnesia is real, checkpoints aren't a dashboard.

### 🛠 Replicate it

Three rakes will find you no matter how careful the protocol. Mutant confusion: in a deliberately broken assertion, "what even *is* the finding here" is a legitimate question, not a stupid one. Test-vs-system ambiguity (see rake four above — decide it before labeling starts, not mid-set). And the systematic +1 bias: six of eight divergences rated higher than the second assessor — you will over-call the planted controls, because that's what traps are for. Expect it, discount it, move on.

Copy the protocol, not the numbers: stratify the gold across worlds, calibrate jointly on a handful, label blind, demand pointers only at arbitration, default to system-over-test, gate on kappa — and publish the arbitration reasoning, because the rulings *are* the gold. Two precedent rules fell out of ours for all future sets: survived plus no adjacent enforcement means P2; survived plus adjacent coverage means NOISE.

Terms, once, for readers outside the craft: **gold** = human labels the judge is scored against; **kappa** = agreement corrected for chance (both raters saying NOISE a lot is not agreement); **arbitration** = a third ruling with published reasoning that closes each divergence.

### ✅ Result

Agreement 17/25 (68%). Cohen's kappa **0.242** against a 0.6 gate — FAIL. By design, that routes to arbitration, not to relabeling: eight divergences, eight published rulings, final gold of 24 NOISE / 4 P2 / 1 P1 / 1 P0. The low kappa is a result, not a failure — it measured exactly what it was built to measure.

If this sounds familiar, it should. Strip the domain and this is RLHF annotation: guideline, calibration, independent labeling, kappa, arbitration. The industry's known hard problems showed up on schedule — annotator disagreement is alignment's number-one bottleneck. Two differences: thousands of click-workers versus thirty expert labels (domain expertise beats clicks), and purpose — RLHF labels train weights, ours measure judges. Same craft, opposite end of the pipeline: a ruler, not a lesson.

Don't copy our kappa — thirty labels on one pipeline is depth, not breadth. Copy the habit instead: no judgment without a ruler, no ruler without a gate, no gate without published arbitration. Same rule as everywhere in this series: machines count, humans decide.

Assume your judge is lying until the ruler says otherwise.

**What happens in your pipeline when the judge fails its own calibration?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Source
- W2 session record: `31-first-time-assessor-0242-DRAFT.md` (7 sections → compressed to 4 Pulse sections; six questions kept full — the article's meat)
- Local-only memo NOT quoted: `verdictgate/reviews/slot-labeling-experience-memo-2026-09-26.md`

### Facts (from W2 record, aggregates only)
- Local judge 0/30 exact (all-defect); gold-30 = E/H/U × 10; 5 joint calibration (excluded); 25 blind
- Agreement 17/25 (68%), kappa 0.242, gate <0.6 → arbitration (not relabel)
- 8 divergences arbitrated; final gold 24 NOISE / 4 P2 / 1 P1 / 1 P0; fp⇔NOISE biconditional on all 30
- +1 bias: 6/8 higher than second assessor; E5/H10 teaching cases (anonymized, no per-item labels)
- Precedents R1 (survived + no adjacent enforcement → P2) / R2 (survived + adjacent coverage → NOISE)

### Constraints check (W2 binding)
- W3 per-item labels: NOT used (aggregates + anonymized E5/H10 only) — still needs W3 consent check? No: no labels published. W2 public/internal pass still required pre-publish.
- Timings: omitted entirely (unmeasured)
- No correspondence, no commercial content ✅

### Open
- Cover: proposal in metadata (68% vs 0.242 split) — user picks style, Gemini generates
- Inline visuals: TBD (candidate: strata diagram E/H/U; kappa-explained strip; protocol flowchart) — propose after text lock
- Provenance CORRECTED (W2 gold-30 record, owner "все не так" 08.10 — my open-weight-cloud correction was WRONG, not applied): local judge = mini-jev (qwen2.5:3b, Phase A, company/pilots/Jev/); 0/30-exact all-defect caller = mini-jev; cloud incumbent = Jev TypeSafe (Phase B x1 on gold-30, endpoint/model verified); gpt-oss-120b/Groq = DIFFERENT eval (attempt-3 D2-C), must NOT leak into this article. Labelers W3+Victor (Victor first-timer), arbiter W2. Calibration five: H3, H7, E2, U10, E5 (no IDs in body). Sources: labeling-guideline-v1.md + plan-local-judge-2026-09-25.md + phaseb-report-2026-09-26.md.
- Feed post v2 stands (JEV hook, goal-first, 25 kept / 30 dropped; "paid" removed billing-blind; version never present) — JEV-side now double-confirmed (owner goal + W2 Phase B).
- Reviews: R0 owner-tightening ✅ → W2 public/internal PASS ✅ → W1 NUMBERS-TRUTH PASS b895309 (verbatim vs source, arithmetic converges; kappa as reported, same-sitting per W2) ✅ → R1 (user) → publish Fri 09.10
- Package ready: cover (`31-cover.png`/`.jpeg`) · feed post (`31-calibrate-ai-judge-post.md`) · first comment (`31-first-comment.md`)
