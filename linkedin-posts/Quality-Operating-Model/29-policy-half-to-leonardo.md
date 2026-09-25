**Format:** DM attachment for Leonardo Lanni (joint article 29, variant C) — SEND tomorrow
**Status:** READY 24.09. Substance = Appendix A (W2 source) + tier matrix. Voice pass happens at merge, not before sending.
**Do NOT include:** internal triage, P0 notes, Leonardo-bio details (his facts, his confirmation).

---

Hi Leonardo — as promised, my policy half. Full text below, review whenever ready.

# Policy Half: VerdictGate — The Verdict Layer

*The mutation is not the test. The mutant is the question. The survivor is the answer. The gate is the judgment.*

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

**No global percentage.** Each tier has its own gate, its own signal budget, its own escalation path.

## The Evidence Contract: Mutation → Verdict

RMT (or traditional MT, or any mutation source) produces rows. VerdictGate consumes them: behaviour + tier + killed/survived + decision per row. No hidden state. Same CSV → same verdict, byte-identical, forever.

## The Gate Is Not the Score

VerdictGate separates **signal** from **gate**. Mutation score per tier is a hard gate (B0/B1 zero-tolerance, B2 band, B3 trend); observed-only and mass rates are signals with budgets. **Signals inform. Gates decide.** A low score triggers a mandatory signed comment — not an auto-fail. A human decides, with evidence.

## Tier Decision Rule (who sets tiers, when)

| Case | Who assigns | When |
|------|-------------|------|
| Own suite | QA engineer (author) | pre-seed (requirements file) |
| Vendor eval | evaluator | at matrix design |
| Joint pilot (us) | You propose P-tier per verification point → I map P→B | pre-seed relevance filter |

Tiers are set BEFORE the run — otherwise the gate is gameable. Default mapping 1:1 (P0→B0 … P3→B3); disputes go to a joint review.

---

*Repo (open source, MIT): https://github.com/victor-2026/verdictgate — 30-second failing example included. Looking forward to your RMT half!*
