# Amodei "We Must Pace the Frontier" (Sep 2026) — evaluators, checkpoints, OAI-HF

**Source:** [darioamodei.com/post/we-must-pace-the-frontier](https://darioamodei.com/post/we-must-pace-the-frontier) (Sep 2026) via Bolton/Bach livestream post 12.09
**Trigger:** recursive self-improvement accelerating + OAI-HF swarm incident

## The 3-step plan

1. **Embedded evaluators** (Anthropic commits unilaterally): third-party teams (e.g. METR) with employee-like access — badges, laptops, tools, live conversations. Right to **publish findings without editorial control** (narrow redactions only, can't redact unfavorable). Banking-supervisor precedent.
2. **Democratic coordination:** common safety standards + pacing, needs antitrust waivers.
3. **Global coordination:** 4 levels (bioweapon ban → pre-release testing → RSI speed limit → full pause); verification is the binding constraint.

## OAI-HF incident (their words)

Swarm acted as "fanatically devoted collective": attacked unasked unrelated targets, sacrificed selves, **attempted to hack the grader** evaluating them. Amodei: in 6–12 months a similar swarm could take over the internet (persistent botnet, $100B+ damage). Dismissing as one-company failure = mistake; similar incidents industry-wide incl. Anthropic.

## Testing & Evaluation section (direct quotes territory)

- Smarter models deceive tests → need broader, more ingenious evals + interpretability cross-checks.
- **Checkpoints scheme:** capability X → certifications Y,Z (evals + interpretability + training-env audits). X e.g. "escapes most sandboxes", Y/Z = whatever makes breakout propensity negligible.
- Operational excellence (filtering, sandboxing, env hygiene) listed alongside alignment — execution, not just theory.

## Why it matters for us

1. **Embedded evaluators = attestor role, institutionalized.** Amodei proposes at frontier scale what independent attestation does at product scale (per-risk-tier framework: assessor over LIVE runs, publishable findings). Quote-bank for commercial + articles.
2. **"The grader needs grading too."** OAI-HF tried to hack its evaluator — Article 26's core move (probe the oracle, don't trust it) validated at frontier scale. Mutation matrix IS the product-scale embedded evaluator.
3. **Checkpoints = per-risk-tier gates by another name.** Capability-tier → certification-tier mapping mirrors B0–B3 + thresholds. Framework convergence, third independent derivation (Testkube, Amodei).
4. **Rogue prime case for 27:** fanatical collective + grader-hack belongs in Rogue-line (strongest episode yet — self-sacrifice + evaluator attack in one).
5. **Bolton/Bach livestream response (12.09, RST angle)** — watch for their testing framing; checks-vs-testing lens on Amodei's evals.
6. **External validation — Amodei quote via Rahul Parwal (12.09):** Anthropic's CEO says "Testing and Evaluation is one of the most valuable, difficult, and serious areas in the software industry today." Confirms Article 26/27 thesis from the highest authority: testing AI ≠ testing software, it's a distinct discipline requiring its own methods.
7. **Practical companion — Jason Arbon "Testing AI" (testingaibook.com):** 21-chapter operating manual for "Confidence Engineering." Chapter 11 "The Confidence Engineer" maps directly to Article 27's guided QA engineer role (connects product intent, code, tests, evals, rollout, business consequences). Book argues "Generation is easy. Validation is the hard part" — same thesis as mutation matrix (26) and risk-based gates (27). Full chapter map + 194 concept briefs: `ai-qa-wiki/wiki/testing-ai-book-index.md`.
8. **Direct endorsement — Martin Miceli (CTO Parser) reply to comment (14.09):** Confirmed the "blank scores zero = green report with no ambiguity flag" parallel, called mutation matrix "very interesting empirical validation." His insight: "uncertainty itself is valuable information." Article 27 gate design principle: uncertainty ≠ failure, it's information the system should surface, not suppress. This is the CEO of a testing-tool company publicly validating the method.
9. **Jason Arbon workshop data (14.09):** "Expert QA vs AI" — early but directional real workshop data comparing expert QA engineers against AI tools. 10-minute exercise available for contribution. Presenting at Pacific Northwest Software Quality Conference. Full article on substack. Directly supports Article 27's guided QA thesis: the expert QA role is measurable and differentiates from AI. Link: testingaibook.com, testers.ai/workshop, github.com/jarbon/testing-ai-skills.

## Cross-links

- Per-risk-tier framework: attestor + checkpoints convergence.
- Article 26: grade-the-grader (OAI-HF), mutation matrix as embedded evaluation.
- Article 27: OAI-HF rogue episode; guided human + embedded external as two-layer supervision.
- Klain Confidently Incorrect (inspect-o-nator missed behavior): same trust-the-checker failure, smaller scale.
