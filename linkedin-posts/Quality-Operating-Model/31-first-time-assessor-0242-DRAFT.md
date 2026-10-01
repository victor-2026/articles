# First-time assessor: what labeling 30 items for an AI judge taught me (DRAFT)

**Status:** slot FRI 09.10 LOCKED. Language: EN (series norm, W4 decision 30.09). Headlines + outline in progress (W4).
**Forbidden in this draft:** W3's per-item labels (need W3 consent for publication), unverified timings (solo wall-clock unmeasured — marked as such everywhere), private correspondence, commercial/vendor strategy.
**Sources:** frozen gold-30 file (W3 tree), guideline v1, W2 session checkpoints (public), labeling memo `verdictgate/reviews/slot-labeling-experience-memo-2026-09-26.md` (local-only).

---

## 1. Why a human had to label at all

We needed to decide whether a free local AI judge could replace a paid cloud one. A judge outputs verdicts in words — and without a human ground truth, a good judge is indistinguishable from a confident liar. Our local judge called *everything* a defect (0/30 exact) with a straight face; without gold that looks like diligence.

Before this track, no labeling was ever needed: mutation testing carries its own oracle (we break it ourselves — killed/survived is observed via exit codes, not judged). Gold becomes mandatory if and only if an AI judgment stands between evidence and conclusion with no executable check. Rule for the future: no judgment — no labeling tax.

## 2. The setup: 30 items, three worlds

Gold-30, three strata of 10: E (e2e survivors from our own mutation campaign — negated assertions the suite didn't catch), H (historical findings: crawler outputs, a real live-site bug, two public issue reports), U (unit-spec quirks: validation rules, retry helpers, parsers). Three different worlds so the judge gets tested from three angles. Calibration: 5 worked examples walked jointly (excluded from agreement scoring), then 25 labeled independently and blind.

## 3. Six questions from a first-timer (all load-bearing)

In order asked, with the answers that became protocol:
1. *What goes in `my_pointer`?* — reproducible inspection trace (path+lines). Later amended: pointers mandatory only for diverged items at arbitration.
2. *Submit without pointers?* — Yes (two-phase protocol): labels+notes now → kappa; pointers only where arbitrated.
3. *Spend time justifying?* — effort into severity calls, not 25 pointers; flag unsure items.
4. *Assess the test or the system?* — SYSTEM by default (taxonomy leaves no room); bridge rule: test observation counts iff it reveals unenforced specified behavior. Never rate test code quality.
5. *These mutant items confuse me (is this RMT?) — if we don't converge, redo?* — Yes, RMT; mental model (mutant = intentional breakage; survived = suite green; job = would a REAL bug of that shape matter?); iteration guaranteed, no penalty for first-pass divergence.
6. *Which 25, where?* — status amnesia is real; track state needs an owner-visible dashboard, not just checkpoints.

## 4. Difficulties (observed, not inferred)

- **D1. Mutant confusion.** E-items describe deliberately broken assertions the suite didn't catch; the beginner question "what even IS the finding here" is legitimate.
- **D2. Test-vs-system ambiguity.** The hardest question of the set, found by the beginner before the arbiter ruled it.
- **D3. JSON mechanics.** One trailing comma broke parsing; fixed by arbiter without touching values. Lesson: hand-edited JSON needs a validator in the loop.
- **D4. Systematic +1 bias.** 6 of 8 divergences higher than the second assessor — over-calling controls (the set's traps firing as designed) + file-it liberality. Calibration lesson, not failure.
- **D5. Calibration items that teach.** E5 (P2 accepted over the arbiter's NOISE lean — asserted-but-unenforced specified behavior) and H10 (P1 vs P0 on silent misrepresentation, proving non-blanket judgment).

## 5. Numbers: kappa 0.242 and why that's a result, not a failure

Agreement 17/25 (68%), both raters NOISE-heavy → Cohen's kappa **0.242**, gate (<0.6) FAIL — by design this routes to arbitration, not to relabeling. Eight divergences arbitrated with published reasoning; rulings ARE gold. Final gold: 24 NOISE / 4 P2 / 1 P1 / 1 P0, fp⇔NOISE biconditional holding on all 30. Precedent rules established for future sets: R1 (survived + no adjacent enforcement → P2) / R2 (survived + adjacent coverage → NOISE).

## 6. This was RLHF annotation (just expert-grade and for measurement, not training)

RLHF in one paragraph: LLMs become useful at stage 3, when human labelers rank outputs and a reward model learns "what humans want." Labelers there do exactly this work: guideline → calibration → independent labeling → kappa → arbitration. The pain points are the industry's known hard problems — annotator disagreement is alignment's #1 bottleneck. Two differences: (a) scale — thousands of click-workers vs 30 expert labels (domain expertise beats clicks); (b) purpose — RLHF labels train weights, ours measure judges (a ruler, not a lesson). Same craft, opposite end of the pipeline.

## 7. What goes public vs stays inside (for this article)

PUBLIC: process, aggregates (kappa, counts, divergence pattern), R1/R2 precedents, the six questions, D1–D5, RLHF parallel. INTERNAL without separate decisions: W3's per-item labels (needs W3 consent — new use beyond the comparison), unverified timings (mark unmeasured or omit), private correspondence, commercial/vendor strategy. Rule: methodology + aggregates out; others' labels + unverified out only with consent. Before publishing: one public/internal pass over the draft (W2 can check: what is quote, aggregate, or consent-gated).
