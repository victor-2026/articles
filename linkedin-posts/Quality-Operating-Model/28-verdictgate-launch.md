**Format:** Pulse Article (follow-up on Article 26)
**Series:** Quality-Operating-Model
**Cover:** TBD (gate-card reuse or new: verdict table B0 FAIL/B1 PASS)
**Feed Image:** TBD (cover doubles as feed preview)
**Hook:** Article 26 told you to break the testing tool. We broke our own first — then codified the method.

---

# Your Vendor's Green Report Is a Claim: Here's the Calculator That Checks It

*Follow-up on the vendor-gates series: break the tool, then the guided engineer.*

The last piece asked you to break the testing tool on purpose. We did — to ours first. Then we fixed every break, measured the rest, and shipped the method as code. It is called VerdictGate, and as of today it is open source.

Three independent reviews, **zero P0 findings**. A correctness-and-gaming audit, an adversarial red-team, and an interaction-effects pass — three different models, three different lenses. Every bypass they found is either fixed in code or documented as a human-owned trust boundary. The flip points below are measured, not asserted.

### ❓ Problem

A vendor's green report is self-graded homework. Our QAEverest pilot showed the shape: 100% confidence, 0% risk, every seeded break missed. The tool saw everything, questioned nothing, and stamped the miss as green.

Then we found the same shape in our own backyard. Twelve route mocks in our 49-test mutation suite never matched anything — `*` doesn't cross `/`, so the mutants never applied and the tests passed on real data, green and meaningless. Nobody verified the harness. That is the moment a green suite stops being evidence and becomes a story.

### 🧭 Solution

A verdict layer, not another executor. VerdictGate never generates or runs mutants — vendors run, you record, it judges: per risk tier, ship or no-ship, with the evidence pack to prove it. Static (Python stdlib, zero dependencies), deterministic (same CSV → byte-identical verdict), per-tier never blended (B0/B1 zero-tolerance, B2 band, B3 trend-only).

What it refuses is as important as what it computes: no-op mutants rejected at input, unassessed equivalents rejected, bare observed flags rejected, tier mismatches against requirements rejected. A verdict you cannot game by re-labeling is the whole point.

### 🛠 Implementation

How it was built is the trust story. Three reviews across two weeks: a gaming audit found 20+ issues (all closed or bounded), an adversarial pass found tier laundering and decision-theater (one fixed by a requirements guard, one documented), an interaction pass confirmed the controls compose without defeating each other. Zero P0 in the final round.

Then measurement replaced opinion. We swept relabeled mutants through the gates and found every proposed percentage threshold missed the real flip points (**5–17.6%**) — so zero-tolerance tiers got presence signals instead of percentages, and the B2 band got its numbers from a live 20-row boundary run (**5.0% PASS, 10.0% FAIL**, exact edge). A 17-row live roster closed the loop: genuine stale-feed survivor failed B1, mass signals fired, exclusions stayed visible.

**427 minutes** of build and review. **60+ hours** of field pilots behind the methodology. The ledger is public, in the repo.

### ✅ Result

The break-the-tool method, codified: break something on purpose, record it honestly, let the gate decide. Try it in 30 seconds on the included failing example — exit 1, with the exact row to fix first. Then run it on your suite. If your green survives, it is evidence. If it doesn't, you just saved a release.

The agent writes the test. The vendor writes the report. You write the verdict — now with a calculator.

---

Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QualityEngineering #AITesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Headlines (locked: article #2, feed #1, discussion #3)
1. Feed post: "Your Vendor's Green Report Is a Claim. Here's the Calculator That Checks It."
2. Article (this file): "We Tried to Cheat Our Own Test-Gate. Three Reviewers Watched." — WAIT, mismatch: title above uses #1. DECISION NEEDED: title = #2 ("We Tried to Cheat...") or keep #1? Draft written with #1 as H1. User picked all three; assignment was mine. Confirm before publish.
3. Discussion follow-up: "Stop Trusting Test Scores. Start Verdicting Them."

### Evidence (ссылки для инлайна — прогнать по готче #8)
- Repo: https://github.com/victor-2026/verdictgate (PRIVATE until Article 27 publication 19.09 — VERIFY PUBLIC before publishing this article!)
- Article 26: https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/
- Article 27: URL after 19.09 publication
- Amodei embedded evaluators · Osmani 80%/25x · Bach metamorphic (1 max in comment)

### Open (к публикации 23.09)
- H1 decision (see above)
- Cover (new vs gate-card reuse) + feed image
- Feed post text (hook #1, CTA "Full article below")
- First comment (repo link + method links + 1 external max)
- Repo MUST be public before this goes live (gating item)
