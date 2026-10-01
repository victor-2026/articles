**Format:** LinkedIn Pulse Article (methodology)
**Series:** Quality Operating Model (slot FRI 09.10 LOCKED)
**Status:** draft v1 (W4, 30.09 — from W2 session record; needs W2 public/internal pass before publish)
**Cover:** TODO (proposal: split visual "68% vs 0.242" — same labels, two readings, dark + amber series style)
**Feed Image:** cover doubles as feed preview
**Hook:** 68% agreement with the expert — sounds respectable, until kappa 0.242. Same 25 labels, same afternoon, failing grade.
**Constraints (W2, binding):** aggregates only (no W3 per-item labels without consent), no timings (unmeasured — omit), no private correspondence, no commercial/vendor strategy.

---

# How to Calibrate an AI Judge With 30 Human Labels and One Failing Grade

Seventeen out of twenty-five. 68% agreement with the expert — sounds respectable, until the statistician in the room says kappa 0.242. Same labels, same afternoon, failing grade — and that failing grade was the whole point.

I labeled 30 items to answer one question: can a free local AI judge replace a paid cloud one? Our local judge had called *everything* a defect (0/30 exact) with a straight face — and without a human ground truth, that looks like diligence. A good judge is indistinguishable from a confident liar. So before trusting any judge, I built the ruler: 30 expert labels, one failing grade, eight arbitrated disagreements.

The target was our own verdict pipeline — the infrastructure that classifies findings as defects or noise. What I calibrated was not the product. It was the act of judging itself.

### ❓ Problem

A judge outputs verdicts in words. Words are cheap, confidence is free, and nothing in the output tells you whether the judgment tracked reality. Our local judge proved it: every item a defect, zero exact matches, total conviction. Without gold labels, you cannot tell diligence from theater.

Before this track, we never needed labeling at all. Mutation testing carries its own oracle — we break the system ourselves, and killed-or-survived is observed through exit codes, not judged. Gold becomes mandatory if and only if an AI judgment stands between evidence and conclusion with no executable check in between. The rule for the future writes itself: no judgment, no labeling tax.

### 🧭 Solution

Thirty items, three worlds, one protocol. Gold-30 splits into three strata of ten: E (end-to-end survivors from our own mutation campaign — negated assertions the suite never caught), H (historical findings — crawler outputs, one real live-site bug, two public issue reports), U (unit-spec quirks — validation rules, retry helpers, parsers). Three different worlds, so the judge gets attacked from three angles.

Calibration came first: five worked examples, walked through jointly with the arbiter, excluded from scoring. Then twenty-five items labeled independently and blind. As a first-timer, I asked six questions — every one of them load-bearing, every answer now protocol:

- **What goes in the pointer field?** A reproducible inspection trace — file path plus lines. Later amended: pointers mandatory only for diverged items, at arbitration.
- **Can I submit without pointers?** Yes — two-phase protocol. Labels and notes now feed the agreement score; pointers get written only where arbitration demands them.
- **Where does the effort go?** Into severity calls, not into twenty-five pointers. Flag the unsure items, move on.
- **Do I assess the test or the system?** The system, by default. Bridge rule: a test observation counts if and only if it reveals specified behavior nobody enforces. Test code quality is never rated.
- **These mutant items confuse me — is this reverse mutation, and do we redo if we diverge?** Yes, and yes. Mental model: a mutant is intentional breakage, survived means the suite stayed green, and the only question is whether a real bug of that shape would matter. Iteration guaranteed, no penalty for first-pass divergence.
- **Which twenty-five, and where do I stand?** Status amnesia is real — a labeling track needs an owner-visible dashboard, not just checkpoints.

The beginner found the hardest question of the set before the arbiter ruled it. That is what first-timers are for.

### 🛠 Replicate it

Five difficulties surfaced — all observed, none inferred. Mutant confusion (what even *is* the finding in a deliberately broken assertion?). Test-vs-system ambiguity. JSON mechanics (one trailing comma broke parsing — hand-edited JSON needs a validator in the loop). A systematic +1 bias: six of eight divergences rated higher than the second assessor, over-calling the controls the set had planted as traps. And calibration items that teach: one P2 accepted over the arbiter's NOISE lean (asserted-but-unenforced specified behavior), one P1-vs-P0 split on silent misrepresentation — proof the judgments were never blanket.

Copy the protocol, not the numbers: stratify the gold across worlds, calibrate jointly on a handful, label blind, demand pointers only at arbitration, default to system-over-test, gate on kappa — and publish the arbitration reasoning, because the rulings *are* the gold. Two precedent rules fell out of ours for all future sets: survived plus no adjacent enforcement means P2; survived plus adjacent coverage means NOISE.

Terms, once, for readers outside the craft: **gold** = human labels the judge is scored against; **kappa** = agreement corrected for chance (both raters saying NOISE a lot is not agreement); **arbitration** = a third ruling with published reasoning that closes each divergence.

### ✅ Result

Agreement 17/25 (68%). Cohen's kappa **0.242** against a 0.6 gate — FAIL. By design, that routes to arbitration, not to relabeling: eight divergences, eight published rulings, final gold of 24 NOISE / 4 P2 / 1 P1 / 1 P0. The low kappa is a result, not a failure — it measured exactly what it was built to measure, and the arbitration trail is now reusable infrastructure for every judge we test next.

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
- Feed post text + first comment: TODO (draft next, after text lock)
- Reviews: W2 public/internal pass → W1 fact-check → W3 (out of scope? no product facts — decide) → R1 (user) → publish Fri 09.10
