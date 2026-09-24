**Format:** LinkedIn Pulse Article (methodology) + cross-post Dev.to/blog (per W3 plan)
**Series:** Quality Operating Model (number TBD — slot in Tue/Fri rhythm)
**Cover:** TODO (timing bars: 3h rebuild vs 35min swap)
**Feed Image:** TODO (cover doubles as feed preview)
**Hook:** 120 validation runs in 35 minutes — across 2 seeded mutations, 5 probes each, zero product defects in the tool under test.
**Terminology lock (W3):** validation runs, NOT mutation tests. 4 conditions × 5 probes × 6 runs = 120. Mutations: 2 seeded (username-required removed, password bypass).

---

# How We Ran 120 Validation Runs in 35 Minutes (Instead of 3 Hours)

Traditional mutation campaigns rebuild the app per mutant. Hours of CI for a question that should take minutes. We stopped rebuilding and started swapping: pre-built variants, ~300ms swap, automated verdicts. 120 runs in 35 minutes — 5× faster than rebuild-each-time.

The target was a 4-role QA agent plugin (Manager/Analyst/Manual/Automator). The verdict first: no product defects found across all 120 runs. What we validated was the infrastructure around it — the retro loop, the verdict pipeline, the statistics.

### ❓ Problem

A mutation campaign has two clocks: the run clock and the rebuild clock. The run clock is seconds per test. The rebuild clock is minutes per mutant — frontend rebuild, container restart, reseeding. At 120 runs, rebuild dominates: ~2.8 hours of waiting for ~35 minutes of testing. CI pipelines kill campaigns on cost alone, long before anyone asks whether the results mean anything.

### 🧭 Solution

Three moves, each boring, compounding together:

- **Pre-built variants** — all four conditions (baseline, break, fix, drift) built once, ~65 seconds each. No rebuilds during the campaign.
- **Fast swap** — ~300ms switch between variants. The campaign loop becomes run → swap → run.
- **Automated verdicts** — Playwright executes, a verdict model classifies (regression or not) in ~350ms. No human in the scoring loop.

### 🛠 Implementation

Two seeded mutations, five probes each, six runs per probe: username-required removed, password-required bypassed, plus baseline and fix conditions. The retro loop ran the full cycle — break, FAIL, retro-edit, PASS — with drift measured via git diff on the engine's instruction paths. Drift scope came back clean.

The honest caveat: our probe v1 detects any validation, not field-specific errors — the target returns generic messages for all fields. Probe v2 will extract field-level errors. The campaign conclusions stand (breaks were caught at form level), but field attribution needs v2.

### ✅ Result

120 runs, 35 minutes wall time, 5× speedup over rebuild-each-time. Both seeded mutations behaved as designed across all probes. The retro loop is verified infrastructure now, not a hypothesis: break → FAIL → retro-edit → PASS, with an empty drift diff to prove the engine didn't silently change shape.

Total cost: ~9 hours wall time across three phases (4 design + 2 plan + 3 campaign), free tier throughout. The expensive part was never the runs — it was building the variants once and calibrating the probes.

Next: probe v2 with field-specific extraction, a local-LLM verdict alternative (cost/latency), and a full campaign at n=30 per condition with statistical power. The 120-run pilot was the shakedown; the measurement campaign comes next.

Running mutation campaigns? Let's compare notes.

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Facts (W3 checkpoint 2026-09-23/24, truth-locked)
- 120 runs = 4 conditions × 5 probes × 6 runs; 35 min wall; ~2.8h rebuild baseline (3h = rounding, approved)
- 2 mutations: username-required removed (SaveEmployee.vue:235, SaveSystemUser.vue:93), password bypass (PasswordInput.vue:100)
- Retro loop verified; drift diff clean; no product defects in qa-cube (infrastructure tested, not test generation)
- Probe v1 limitation: form-level only (honest caveat in body ✅)
- Terminology: validation runs, never "mutation tests" (W3 verdict)

### Open
- Vadim naming approval for LI article (discussions-ok ≠ article-ok?) — ask explicitly
- Code/Infra links: qa-cube repo public (codecube01/qa-cube ✅ linkable); swap_variant.py + Jev client live in PRIVATE pilots dir — NO public link, describe in words only
- Cover + feed + 3 inline (timing bars, swap architecture, results table): TODO
- Feed post text + first comment: TODO
- Slot: Tue/Fri rhythm, priority vs 29-Wed undecided
- Reviews: W3 facts ✅ (their checkpoint) → R1 (user) → publish
