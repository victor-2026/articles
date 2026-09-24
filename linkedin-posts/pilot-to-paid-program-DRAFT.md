**Format:** Program plan (cross-window) — DRAFT, owner-of-record TBD (recommend verdictgate/docs/pilot-program/, W2 places per rule 26)
**Status:** DRAFT 24.09 (W4). qa-cube = first clean big pilot → machine needs productizing for paid orders (Rupesh-type).
**Source:** user program review 24.09.

---

# Pilot-to-Paid Program

## Stream 1 — Methodology & speed (owner W2, runs W3)

- Bottleneck analysis of the 9h (what ate time besides 35min runs)
- openjev vs jev comparison pilots (W3, Jev free till 25.09 🔥)
- Probe v3 backlog; local-LLM verdict alternative
- RMT engine: scope decision OPEN (full vs module vs minimal — W4 recommends minimal-for-pilot, see below)

## Stream 2 — External pack (paid-order readiness)

| Artifact | Owner | Status |
|----------|-------|--------|
| A-post (GitHub discussions, peer) | W4 (+W3 facts) | POSTED (discussions #2) ✅ |
| B-article / 30 (methodology) | W4 | drafted, Vadim ok ✅, slot pending |
| Carousel derivative | W4 | after B publish |
| **Pilot Report PDF** (outline below) | **W1 lead, W2 method, W3 evidence** | outline approved, assembly pending |
| Badge/certificate ("Mutation-attested") | W1 (+W2 criteria) | design + issuance rules OPEN |
| Evidence-pack spec (supply standard) | W2 | OPEN |

## Stream 3 — Internal archive & activation

- Raw artifacts (CSV, verdict packs, logs): W3 indexes locations
- Records (checkpoints, perf-log, cross-links): W4 maintains
- Activation SOP (new version / paid request → reopen dir + rerun matrix): W3 to write

---

## Pilot Report outline (for W1/W2 assembly)

1. **Cover:** pilot, product+version, dates, parties (independent evaluator / vendor contact), verdict per tier
2. **Scope & method:** matrix version, scenarios, tools (VerdictGate + scorer version), environment
3. **Results per tier:** B0–B3 tables (seeded/caught/survived/score/gate) + fix-first list
4. **Caveats & limits:** probe versions, blind spots, free-tier constraints, what was NOT tested
5. **Evidence pack index:** CSVs, verdict packs, logs (+ hashes/paths)
6. **Sign-off:** reviewer, vendor acknowledgment line, date; reproducibility statement (same CSV + scorer = byte-identical)
7. **Commercial annex (W1):** engagement terms, paid-tier contents, contact

---

## Attestation model (decided 24.09 — registry, not certificate-alone)

- **Source of truth = registry (append-only):** product + version, scope, verdict per tier, evidence links (CSV + scorer version → byte-identical), date, sign-off. Certificate PDF = rendered VIEW of a registry entry. Badge/figure = pointer to entry.
- **Obligations per entry:** pinned versions (what was tested), reproducibility window (same CSV + scorer = same verdict), re-attestation trigger (new product version = new entry, old stays), support = methodology questions, not product support.
- **Two lanes (already emerged in practice):**
  - *Open-source lane (free, public):* Vadim/qa-cube, Igor/FlowScout. Peer feedback, published with consent. Serves R&D + marketing.
  - *Commercial lane (paid, private-first):* DevAssure, QAEverest-pattern. Report private by default; public only with consent + fair notice. Fail = consulting lead (fix-first list), pass = trust signal for THEIR enterprise buyers (SOC2 logic).
- **Answer to "why come to us":** fail privately → free consulting that improves the product (Rupesh: 0/4 → fix shipped; Igor: 3 bugs → 0.4.0). Pass publicly → independent trust signal + badge + article. Both outcomes have value; the asymmetry dissolves.
- **Vadim case = template showcase** for lane 1 (passed → public attestation + badge).

## 🛠 Служебные заметки (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

- Placement: recommend `verdictgate/docs/pilot-program/` (W2 decides per rule 26); this file = W4 working copy.
- W2 answers for RMT scope (24.09, W4 recommendation): Option C (minimal for pilot) + 3 matchers (toBeVisible/toHaveText/toHaveLength) + pilot-this-week priority.
