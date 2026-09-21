**Format:** JOINT Pulse Article (Victor × Leonardo Lanni) — INCOMING DRAFT, NOT voiced, NOT reviewed
**Series:** Quality Operating Model (candidate 29/30)
**Source:** W1/W2 window handover, 2026-09-21/22. Verbatim below.
**Status:** PARKED for W4 triage. Do NOT publish. Leonardo review pending (his side).
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

| Layer | Question | Tool | Output |
|-------|----------|------|--------|
| **1. Sensitivity** | "Can the test detect a broken assertion?" | **RMT** | Killed/Survived per assertion + risk tier |
| **2. Evidence** | "What exactly survived?" | Evidence Contract | `behaviour + tier + killed/survived + decision` |
| **3. Policy** | "Is this green acceptable?" | VerdictGate | B0/B1 zero-tolerance, B2 band, B3 trend |

**Pipeline:** Code Change → RMT (mutate assertions) → Run Tests → Evidence Contract → VerdictGate → PASS/FAIL + Evidence Pack
**Key claim (VERIFY):** RMT output feeds VerdictGate as first-class input. Provenance tagged for diagnostics.

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

### 5b. Case Study: OrangeHRM 122 Behaviors (200 words)
Autonoma/KISS/Kiro mapped 122 behaviors; RMT mutates assertions; VerdictGate gates per tier. Key finding: functional failures caught, structural fragility missed (B2 5/5 survived); re-test after fix 100/100, 0 FP.

### 6. The "Outside the Product" Checklist (150 words)
Mutation Backlog / Engineer / Tier assignment / Review Board / Attestation template / Dispute resolution / Lifecycle / Metrics — checkboxes.

### 7. Call to Action / Closing (150 words)
> The mutation is not the test. The mutant is the question. The survivor is the answer. The gate is the judgment.
> RMT makes sure your assertions can die. VerdictGate decides if the survivors matter.

**Try it:** RMT [Leonardo's repo/link TBD] · VerdictGate: repo link + 30s example.

### 8. Author Bios (50 words each)
Leonardo Lanni (QA Roots, RMT) / Victor Ematin (VerdictGate) — links TBD.

---

## W4 TRIAJE (added on filing, 2026-09-22)

**P0 — factual/structural, must resolve before voicing:**
1. **pip install is FALSE.** Draft says `pip install verdictgate → python -m verdictgate`. Repo reality: static script, `python3 verdictgate.py results.csv`, zero dependencies, NOT on pip. Fix to repo + 30s example (same as 28).
2. **Duplicate section numbers:** two "5" (Mechanics + Case Study) and two "7" (CTA + Bios). Renumber on voicing.
3. **Placeholders:** RMT repo/link TBD, author links TBD, Truth of "first-class input" claim (RMT→VerdictGate integration) UNVERIFIED — has the pipeline actually run end-to-end, or is it architecture on paper? Do not publish as fact until proven (own medicine: break it first).
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

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

- Status: INCOMING, filed verbatim 2026-09-22. No voice pass. No reviews.
- Next: user scope (file-only vs start voicing) + P0 answers from W1/W2 window.
