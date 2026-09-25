**Format:** JOINT Pulse Article (Victor × Leonardo Lanni) — INCOMING DRAFT, NOT voiced, NOT reviewed
**Series:** Quality Operating Model (candidate 29/30)
**Source:** W1/W2 window handover, 2026-09-21/22. Verbatim below.
**Status:** VARIANT C CONFIRMED 24.09 — Leonardo said YES ("absolutely, I'm in"). He writes RMT half, timeline accepted. Policy half SEND file ready: `29-policy-half-to-leonardo.md` (+.docx, send tomorrow). Review Wed → publish Fri next week.
**Queue (W1 25.09):** 30 goes next Tue slot (Vadim "next week" promise); 29 follows on Leonardo delivery even if after 30 (numbers need not dictate order — rule 13: readers don't know kanban).
**Deadlines (shifted 24.09, Thu):** ~~policy half → Leonardo Fri → his half/review by Wed → publish Fri next week.~~ VOID — replan after W2 implementation lands.
**W4 scope:** policy half + shared table + voice pass on join. RMT half = Leonardo's text (quote, don't rewrite).
**Collisions:** 28 launches Tue Sep 22 09:00 — independent stream, no body changes from this draft.

---

# Article Draft: "RMT × VerdictGate: When Sensitivity Meets Policy — A Mutation Testing Union"

**Target:** QA Roots (Leonardo's 15K audience) + Article 29/30 (Victor's channels)
**Format:** Joint article / cross-post
**Length:** ~1500-2000 words
**Timeline:** Draft → Leonardo review → cross-post both channels

---

## Working Title Options
1. **"RMT × VerdictGate: When Sensitivity Meets Policy — A Mutation Testing Union"**
2. **"RMT × VerdictGate: Sensitivity × Policy — The Complete Mutation Lifecycle"**
3. **"Two Sides of the Mutation Coin: RMT Sensitivity × VerdictGate Policy"**

---

## Article Structure

### 1. Hook (150 words)
**The Problem:** Everyone runs mutation testing. Few ask: *what does a green result actually mean?*
Traditional MT asks: "Can tests detect code defects?"
RMT asks: "Can tests detect *wrong verifications*?"
VerdictGate asks: "Given surviving mutants, is this green trustworthy for *this risk tier*?"
**Three layers, one question:** *Can you trust your green?*

### 2. The Two Halves (400 words)

#### **RMT — "Is the Verifier Alive?"** (Leonardo)
- **Core idea:** Mutate the *assertion*, not the code. `expect(x).toBe(true)` → `expect(x).toBe(false)`. If test still passes → assertion is dead.
- **Output:** Killed/Survived per assertion + risk tier (behaviour-level, not operator-level)
- **Key insight:** Risk lives on the *verification point*, not the operator. `payment.status == PAID` = B0. `successMessage == "Thank you"` = B3. Same `EQ_NEGATION` operator, different risk.

#### **VerdictGate — "Is the Verdict Trustworthy?"** (Victor)
- **Core idea:** Mutation results → per-risk-tier verdict (B0/B1 zero-tolerance, B2 band, B3 trend)
- **Policy layer:** B0/B1 zero-tolerance, B2 ≤5% survival, B3 trend-only. Observed-only budget. Mass-E signals.
- **Evidence pack:** RACI sign-off, machine-reproducible verdict, fix-first list.

#### **The Union** (shared diagram)
```
RMT (sensitivity)  →  Evidence Contract (behaviour + tier + killed/survived)  →  VerdictGate (policy)
```

### 3. The Critical Insight: Risk Lives on the Verification Point (300 words)
**The Aha Moment** (from Leonardo's message): risk tier belongs to the verification point, not the mutation operator. Same `EQ_NEGATION` → B0 on `payment.status`, B3 on `successMessage`. The operator carries zero risk; the verification point carries all risk.

### 4. The Three-Layer Architecture (300 words)

| Layer | Question | Tool | Output | Failure mode (if this layer fails) |
|-------|----------|------|--------|-------------------------------------|
| **1. Sensitivity** | "Can the test detect a broken assertion?" | **RMT** | Killed/Survived per assertion + risk tier | dead assertions pass silently — green means nothing |
| **2. Evidence** | "What exactly survived?" | Evidence Contract | `behaviour + tier + killed/survived + decision` | survivors unverifiable — nothing to gate on |
| **3. Policy** | "Is this green acceptable?" | VerdictGate | B0/B1 zero-tolerance, B2 band, B3 trend | untrusted green ships — nobody stops the release |

**Pipeline:** Code Change → RMT (mutate assertions) → Run Tests → Evidence Contract → VerdictGate → PASS/FAIL + Evidence Pack
**Design (roadmap, NOT fact — W2 22.09):** RMT output is designed to feed VerdictGate as first-class input. Joint RMT×VerdictGate pilot on 122 behaviors planned post-Leonardo review. Provenance tagged for diagnostics.

### 5. The "Outside the Product" Mechanics (250 words)

| Role | Responsibility |
|------|----------------|
| **Mutation Engineer** | Seeds mutants, runs pipeline, maintains operator sets |
| **QA Analyst / Product Owner** | Assigns risk tiers to verification points |
| **Mutation Review Board** | Attests verdicts, signs off evidence packs |
| **VerdictGate (automated)** | Applies per-tier gates, emits evidence pack |

**Mutation Lifecycle:** Seed → Inject → Run → Classify → Attest → Close
**Metrics:** MTTR, Escape Rate, Survival Rate by tier.
**Risk-Steering Mutation Depth:** B0/B1 full operator set; B2/B3 sampled subset.
**Pre-seed Relevance Filter:** drop verification points outside the change boundary.

### 6. Verified runs (sidebar on voicing: move after Three-Layer table)
- QAEverest 7-mut pilot (CSV, exit codes, verdict packs — verified)
- DevAssure 15-answer (FP 4→0, re-check passed — verified)
- Rupesh stamping change (email, spec update — verified)
- Roadmap: joint RMT×VerdictGate pilot on 122 behaviors planned post-Leonardo review.

### 7. The "Outside the Product" Checklist (150 words)
Mutation Backlog / Engineer / Tier assignment / Review Board / Attestation template / Dispute resolution / Lifecycle / Metrics — checkboxes.

### 8. Call to Action / Closing (150 words)
Staged actionable close (W3): "This week: run RMT on one PR. Next week: feed results to VerdictGate. Share the evidence pack."
> The mutation is not the test. The mutant is the question. The survivor is the answer. The gate is the judgment.
> RMT makes sure your assertions can die. VerdictGate decides if the survivors matter.

**Try it:** RMT [INSERT: leonardo-rmt-repo — real URL from Leonardo; do NOT use `github.com/leonardo-lanni/reverse-mutation-testing` (W3 guess, UNVERIFIED)] · VerdictGate: `git clone https://github.com/victor-2026/verdictgate && python3 verdictgate.py results.csv` — verdict in 30 seconds.

### 9. Author Bios (50 words each, W3 credentials REJECTED where false — see triage)
Leonardo Lanni (QA Roots, RMT) / Victor Ematin (VerdictGate) — full bios + links TBD (Leonardo confirms his own facts).
⛔ W3 suggested Victor bio "ex-EPAM/SoftServe" — FALSE, REJECTED. Never use (cf. global memory gotcha #1: fabricated EPAM entry).
Cross-post mechanics (W3): Leonardo posts 09:00 CEST, Victor reposts 09:30 with "Building on Leonardo's RMT…" + link. Confirm with Leonardo.

---

## W4 TRIAJE (added on filing, 2026-09-22)

**P0 — factual/structural, must resolve before voicing:**
1. ~~**pip install is FALSE.** Draft says `pip install verdictgate → python -m verdictgate`. Repo reality: static script, `python3 verdictgate.py results.csv`, zero dependencies, NOT on pip. Fix to repo + 30s example (same as 28).~~ ✅ RESOLVED 22.09 (W2 decision: variant (a) — clone + python3, truth embedded in policy half; PyPI → backlog post-v1.0; gotcha filed as wiki rule 16)
2. **Duplicate section numbers:** two "5" (Mechanics + Case Study) and two "7" (CTA + Bios). Renumber on voicing.
3. ~~**Placeholders:** RMT repo/link TBD, author links TBD, Truth of "first-class input" claim (RMT→VerdictGate integration) UNVERIFIED — has the pipeline actually run end-to-end, or is it architecture on paper? Do not publish as fact until proven (own medicine: break it first).~~ ✅ RESOLVED 22.09 (W2: 122-claim removed, verified-only list + roadmap item)
4. **Length:** 1500-2000 words vs series 800-1000. Either split (two-parter) or cut on voicing.

**P1 — decisions for W1/user:**
5. Leonardo agreed to co-author? Review loop defined, but joint IP / split / whose channel first = open.
6. RMT evidence-contract spec: quoted or paraphrased? (provenance rule: cite, don't copy).
7. Timing vs 28 launch (Tue 09:00): independent streams, but two launches in one week compete. Recommend 29 slot ≥7 days after 28.

## W4 DRAFTED BLOCK (not approved, 2026-09-22) — Tier decision matrix
| Case | Who assigns tier | When | Artifact | Verdict owner |
|------|-----------------|------|----------|---------------|
| Own suite (VerdictGate solo) | QA engineer (author) | pre-seed | requirements.csv risk levels | author + reviewer sign-off |
| Vendor eval (26-style) | evaluator | at matrix design | 5-scenario matrix tiers | evaluator |
| Joint RMT pilot | Leonardo proposes P-tier per verification point → Victor maps P→B | pre-seed relevance filter | Evidence Contract (behaviour + tier) | Mutation Review Board (joint) |

Default mapping 1:1 (P0→B0 … P3→B3); disputes → board. Tiers are set BEFORE the run — otherwise the gate is gameable (tier laundering, own adversarial finding).

## Routed in (W5 handover 23.09, no ingest)

- **JevBench** (Show HN reproducible benchmark for typed decision models, 23.09 digest): external reference candidate — cheap decision-benchmarking vs our mutation approach. NO wiki file (JEV covered ×7, page 5MB, no transcript). Slot: 29 (measurement economics) or 26-follow-up comment. Verdict: routing enough, W5 recommendation accepted.

## Appendix A: Policy Half (W2 source, verbatim 22.09 — cleaned of opencode dup-loop, RTF→TXT)

# Policy Half: VerdictGate — The Verdict Layer

*The mutation is not the test. The mutant is the question. The survivor is the answer. The gate is the judgment.*

---

## The Verdict Layer: Policy on Green

RMT tells you **whether the check can die**. VerdictGate tells you **whether the green means go**.

Traditional mutation testing gives you a kill rate. A single number. "87% killed — good job." But a 13% survival rate means something radically different if the survivors are in payment processing vs. the "Thank you" banner.

VerdictGate adds the **policy layer** on top of mutation evidence:

| Tier | Scope | Gate Rule | Signal Threshold |
|------|-------|-----------|------------------|
| **B0 Critical** | Payment, auth, credentials, data integrity | **Zero tolerance** — 0 survivors | Score < 90% → mandatory signed comment |
| **B1 High** | Core journeys, primary CRUD, search | **Zero tolerance** — 0 survivors | Score < 80% → mandatory signed comment |
| **B2 Medium** | Secondary flows, edge cases | **Band** — ≤5% survivors (N≥20) or max 1 (N<20) | Score < 90% → mandatory signed comment |
| **B3 Low** | Cosmetic, copy, layout | Trend-only vs rolling 3-run baseline | — |

**No global percentage.** No "87% killed = good." Each tier has its own gate, its own signal budget, its own escalation path.

---

## The Evidence Contract: Mutation → Verdict

RMT (or traditional MT, or any mutation source) produces rows. VerdictGate consumes them.

| mutation_id | behavior | operator | risk_tier | expected | suite_result | observed | decision |
|-------------|----------|----------|-----------|----------|--------------|----------|----------|
| M1 | Payment submits | element_remove | B0 | Y | pass | | |
| M2 | Login rejects wrong pwd | validation_removed | B0 | Y | fail | | |
| M3 | Login button visible | element_remove | B1 | Y | fail | | |

**The contract is simple:** each row = one seeded defect + observed outcome. No hidden state. No hidden logic. Same CSV → same verdict, byte-identical, forever.

---

## The Gate Is Not the Score

A common mistake: "mutation score 87% = pass."

VerdictGate separates **signal** from **gate**:

| Signal | Gate |
|--------|------|
| Mutation score (per tier) | Hard gate (B0/B1 zero-tolerance, B2 band, B3 trend) |
| Observed-only rate | Signal only (budget: B0 10%, B1 20%) |
| Mass-equivalent rate | Signal only (B2: >5% = review) |
| Mass-observed rate | Signal only (B2: >10% = review) |
| Missing decisions (B2 survivors) | Hard gate (fail) |

**Signals inform. Gates decide.** A low score triggers a mandatory signed Assessor comment — not an auto-fail. A human decides, with evidence.

---

## The Evidence Pack: Audit-Ready by Default

Every verdict emits three artifacts:

1. **`results.verdict.md`** — human-readable evidence pack with per-tier tables, signals, fix-first list, sign-off table (Reviewer / Independent Assessor / Engineering Owner)
2. **`results.verdict.json`** — machine-readable, version-stamped, byte-identical reproducible
3. **Raw CSV + run logs** — lineage, not belief

> *Anyone with the same CSV + same scorer version + same CLI flags gets the same verdict, byte-identical, forever.*

No hidden state. No "trust me." Reproducible verdicts.

---

## The Mapping Limit: Profile ≠ Engine

Here's the honest limitation: **VerdictGate profiles encode numbers, not gate shapes.**

QAEverest's B2 gate = `survived <= 1 AND score >= 60` (AND of cap + floor, absolute cap at ANY N).
VerdictGate B2 = band ≤5% at N≥20, small-N floor max 1 at N<20.

| Aspect | QAEverest | VerdictGate |
|--------|-----------|-------------|
| B2 Cap | Absolute (max 1 at ANY N) | Band 5% at N≥20, small-N floor |
| B2 Score | ≥60% floor | ≥90% signal target |
| Decision logic | AND (cap AND floor) | Band + small-N floor |

**The profile carries THEIR numbers. Our engine applies OUR gate shape.** Cross-check validates numbers (90/80/60), not gate shape. Divergence documented in `MAPPING LIMIT`.

---

## The Honesty Rule: Provisional Until Cross-Checked

Every vendor profile ships with `"provisional": true`.

> *Vendor numbers are THEIR claim until cross-checked on a live run.*

We don't hide this. The flag means: "Semantics locked, live verification pending." After a cross-check run + W2 verification → `provisional: false`.

---

## W3 review applied 22.09 (structural; voice items staged)

- Renumber applied: 5 Mechanics, 6 Verified runs (sidebar after Three-Layer table on voicing), 7 Checklist, 8 CTA (+ staged actionable close), 9 Bios.
- Three-Layer table: Failure-mode column ADDED.
- INSERT markers: RMT repo = real URL from Leonardo only (W3-guessed github URL banned).
- Hook staged (concrete pain, W3): "Your CI says 92% killed. A payment mutation survived. You shipped anyway. That night, payment failed."
- Mechanics reframe staged: "Who does what when the gate fails?" (actionable, not corporate).
- Leonardo ask staged: 1 vivid RMT example from a real PR (his text).
- Length (1500-2000 vs 800-1000): DECISION OPEN — split two-parter vs 40% cut.
- Title: W3 prefers option 1; option 3 more clickable — DECISION OPEN (user).
- Appendix A labeled: Policy Half = Victor's voice only; RMT half = Leonardo's text quoted verbatim per provenance.

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

- Status: INCOMING, filed verbatim 2026-09-22. No voice pass. No reviews.
- Next: user scope (file-only vs start voicing) + P0 answers from W1/W2 window.
