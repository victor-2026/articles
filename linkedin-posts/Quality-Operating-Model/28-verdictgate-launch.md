**Format:** Pulse Article (follow-up on Article 26)
**Series:** Quality-Operating-Model
**Cover:** NEW verdict-screenshot (real terminal output: B0 FAIL + Fix-first M1 block, dark #0d1117 + amber, 1920×1080) — DECIDED 19.09, shoot pending (user)
**Feed Image:** cover doubles as feed preview
**Hook:** Article 26 told you to break the testing tool. We broke our own first — then codified the method.

---

# Your Vendor's Green Report Is a Claim: Here's the Calculator That Checks It

*Follow-up on [break the tool](https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/) and [the guided engineer](https://www.linkedin.com/pulse/qa-didnt-get-replaced-got-promoted-victor-ematin-9jzse/).*

The last piece asked you to break the testing tool on purpose. We did — to ours first. Then we fixed every break, measured the rest, and shipped the method as code. It is called VerdictGate, and as of today it is open source.

VerdictGate is a static Python script with zero dependencies: it takes the CSV from your mutation run (a strict, documented schema — garbage in is exit 2, not a verdict) and returns a deterministic verdict per risk tier, plus an evidence pack for audit. One exit code tells CI whether to ship.

Three independent reviews, **zero P0 left open**. A correctness-and-gaming audit, an adversarial red-team, and an interaction-effects pass — three different models, three different lenses. Every bypass they found is either fixed in code or documented as a human-owned trust boundary. The flip points below are measured, not asserted.

### ❓ Problem

A vendor's green report is self-graded homework. In one pilot with a vendor tool, the report showed the shape: 100% confidence, 0% risk, every seeded break missed. The tool saw everything, questioned nothing, and stamped the miss as green.

Then we found the same shape in our own backyard. Twelve route mocks in our 49-test mutation suite never matched anything — `*` doesn't cross `/`, so the mutants never applied and the tests passed on real data, green and meaningless. Nobody verified the harness. That is the moment a green suite stops being evidence and becomes a story.

### 🧭 Solution

A verdict layer, not another executor. VerdictGate never generates or runs mutants — vendors run, you record, it judges: per risk tier, ship or no-ship, with the evidence pack to prove it. Static (Python stdlib, zero dependencies), deterministic (same CSV → byte-identical verdict), per-tier never blended (B0/B1 zero-tolerance, B2 band, B3 trend-only).

What it refuses is as important as what it computes: no-op mutants rejected at input, unassessed equivalents rejected, bare observed flags rejected, tier mismatches against requirements rejected. As Daniel Mauno Pettersson puts it: the author can't be the examiner — the oracle must live outside the implementation it judges. A verdict you cannot game by re-labeling is the whole point.

### 🛠 Implementation

How it was built is the trust story. Three reviews across two weeks: a gaming audit found 20+ issues (all closed or bounded), an adversarial pass found tier laundering (re-labeling a critical mutant as low-risk to dodge the strict gate — fixed by a requirements guard) and decision-theater (marking survivors "dismissed" with no rationale — flagged for sign-off), an interaction pass confirmed the controls compose without defeating each other. Zero P0 in the final round.

Then measurement replaced opinion. We swept relabeled mutants through the gates and found every proposed percentage threshold missed the real flip points (**5–17.6%**) — so zero-tolerance tiers got presence signals instead of percentages, and the B2 band got its numbers from a live 20-row boundary run (**5.0% PASS, 10.0% FAIL**, exact edge). A 17-row live roster closed the loop: genuine stale-feed survivor failed B1, mass signals fired, exclusions stayed visible.

**427 minutes** of build and review. **60+ hours** of field pilots behind the methodology. The ledger is public, in the repo.

### ✅ Result

The break-the-tool method, codified: break something on purpose, record it honestly, let the gate decide. Try it in 30 seconds on the included failing example — exit 1, with the exact row to fix first. Then run it on your suite. If your green survives, it is evidence. If it doesn't, you just saved a release.

What the 30 seconds look like — a results file with six required columns, one command, one verdict:

```
mutation_id,behavior,operator,risk_tier,expected,suite_result
M1,Payment submits successfully,element_remove,B0,Y,pass
M2,Payment rejects invalid card,validation_removed,B0,Y,fail
$ python3 verdictgate.py results.csv
B0 FAIL · B1 PASS · B2 NOT EXERCISED · B3 NOT EXERCISED - FAIL (exit 1)
1. B0 · M1 · Payment submits successfully (element_remove) - SURVIVED, decision: NO RECORDED DECISION
```

In CI it is one step with three exit codes (0 pass, 1 gate failed, 2 bad input), and the evidence pack — verdict, machine-readable twin, raw CSV, sign-off table — attaches to the release record next to your defect escape rate. The gate doesn't replace your metrics; it decides whether they were earned.

The repo is open source (MIT) — [VerdictGate on GitHub](https://github.com/victor-2026/verdictgate). The failing example above runs in 30 seconds.

Methodology became a calculator; the calculator produces an evidence pack.

The agent writes the test. The vendor writes the report. You write the verdict — now with a calculator.

---

Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QualityEngineering #AITesting #MutationTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Headlines (locked 17.09: H1 #1 with colon per no-periods rule, feed #1 hook variant, discussion #3)
1. Feed post: "Your Vendor's Green Report Is a Claim. Here's the Calculator That Checks It."
2. Article (this file): H1 #1 as written above.
3. Discussion follow-up: "Stop Trusting Test Scores. Start Verdicting Them."

### Evidence (ссылки для инлайна — прогнать по готче #8)
- Repo: https://github.com/victor-2026/verdictgate (PUBLIC ✅)
- Article 26: https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/
- Article 27: https://www.linkedin.com/pulse/qa-didnt-get-replaced-got-promoted-victor-ematin-9jzse (published 18.09)
- Amodei embedded evaluators · Osmani 80%/25x · Bach metamorphic (1 max in comment)
- INVESTMENT.md (proof of work, for first comment): https://github.com/victor-2026/verdictgate/blob/main/INVESTMENT.md

### Open (к публикации 23.09)
- Cover: DECIDED 19.09 (new verdict-screenshot per spec) — shoot pending (user)
- Feed post text: DRAFTED 19.09 → `28-verdictgate-launch-post.md`
- First comment: DRAFTED 19.09 → `28-first-comment.md`
- ~~Repo MUST be public before this goes live (gating item)~~ ✅ PUBLIC
- Gotcha #8: string-check 19.09 ✅ (26/27 URLs = performance-log, repo live via gh, no lnkd.in in body) — browser/incognito check pending (user)

### Cover shoot spec (DECIDED 19.09 — new, not gate-card reuse)

- Base: run `examples/payment-critical-fail` in terminal, dark theme #0d1117 + amber (series palette)
- Frame: verdict table + "Fix first" block with M1 (same example as body — recognition)
- Overlay top: article H1; bottom strip: `v0.2.2 · static · zero dependencies`
- Format: 1920×1080 (cover doubles as feed preview)
- Rejected alternative: reuse 27 gate-card (visual repeat for 27 readers)

### 🛠 Служебные — обсудить (цитаты из quotes.md)

- [x] **Pettersson** — SELECTED 17.09, вставлен в Solution (independent oracle). URL найден в quotes.md:45 (TestGuild webinar replay) — использовать в first comment. ✅ DONE 19.09.
- [ ] Greiler / Klain — PARKED (перегруз секции отклонен).

### ⏳ Pending review texts (R3, apply on user go)

- **P0 #2 Pettersson split (L29)** — old: `As Daniel Mauno Pettersson puts it: the author can't be the examiner — the oracle must live outside the implementation it judges.` → new: `As Daniel Mauno Pettersson puts it: "the author can't be the examiner." That is why the oracle must live outside the implementation it judges.`
- **P1 #5 exit code (L15)** — old: `One exit code tells CI whether to ship.` → new: `An exit code tells CI whether to ship.`
