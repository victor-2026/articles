# Test Carrying Cost & Inventory Discipline (Antoine R., Sep 2026)

**Source:** [Antoine R. post](https://www.linkedin.com/) (DevSecOps, via user share, 12.09)
**Digest:** ручной заход 12.09

## Thesis

Worst QA dashboard = counting number of tests. Every test case has a **carrying cost**: maintain, debug, trust, explain on failure. Fine when it protects an important risk; waste when it preserves an old assumption.

## Prescription (inventory discipline)

- Archive obsolete checks.
- Split slow suites.
- Move non-critical validation out of the commit path.
- Keep core signal under 10 minutes.
- Then measure delivery: lead time down, change failure rate down, fewer emergency fixes, fewer manual rituals.
- *"A good test suite should make the riskiest decisions safer. It should not turn every old requirement into permanent work."*

## Why it matters for us

1. **Carrying cost = economic leg of risk tiers.** Per-risk-tier framework prices gates by risk; Antoine prices tests by risk. Same coin: B0 gate is expensive because the risk is expensive. His "cost is fine when it protects important risk" is the one-line justification of tiered strictness.
2. **Non-prioritized suites 2x slower CI** — empirical cost of flat (unprioritized) quality models; supports 21/23 (federated ownership needs prioritization to work).
3. **Outcome metrics = DORA.** Lead time + change failure rate as the scoreboard (not test count) — aligns with Test-Dora-Plus; test-count dashboards are vanity metrics.
4. **"Permanent work" vs sonar:** obsolete checks that nobody archives = unmeasured survivors in mutation terms — tests that pass forever and prove nothing. Mutation score is the audit of his inventory.

## Cross-links

- Per-risk-tier framework (cost of gate ∝ risk).
- Articles 21/23 (ownership + system; prioritization as precondition).
- Test-Dora-Plus (lead time / CFR as scoreboard).
- Article 26 follow-up: mutation survival as obsolete-check detector.
