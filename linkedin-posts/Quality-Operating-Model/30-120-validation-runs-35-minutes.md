**Format:** LinkedIn Pulse Article (methodology) + cross-post Dev.to/blog (per W3 plan)
**Series:** Quality Operating Model (number TBD — slot in Tue/Fri rhythm)
**Status:** SCHEDULED Fri 02.10 09:00 GMT+3 (Pulse + feed post loaded in LI; Vadim ok; 29 published Mon 29.09)
**Cover:** 30-cover-campaign.png ✅ (1920×1080, timing bars 3h vs 35min + 5×, HTML source alongside)
**Feed Image:** cover doubles as feed preview
**Hook:** Our first probe would have certified a fix that fixed nothing — 120 validation runs in 35 minutes, and the scariest false PASS we found was our own.
**Terminology lock (W3):** validation runs, NOT mutation tests. 4 conditions × 5 probes × 6 runs = 120. Mutations: 2 seeded (username-required removed, password bypass).

---

# 120 Validation Runs in 35 Minutes — and Our First Probe Was Wrong

120 validation runs in 35 minutes — 5× faster than rebuild-each-time. But speed isn't the story. The story is that our own measuring instrument lied to us first, in a campaign whose whole point was catching lies.

[SCREENSHOT: two-clocks diagram — run clock (seconds) vs rebuild clock (minutes), 2.8h vs 35min bars, 30-clocks.jpeg ✅]

The target was a 4-role QA agent plugin (Manager/Analyst/Manual/Automator). The product was not the defect. Our first probe was. What we validated was the infrastructure around it — the retro loop, the verdict pipeline, the statistics.

### ❓ Problem

A mutation campaign has two clocks: the run clock and the rebuild clock. The run clock is seconds per test. The rebuild clock is minutes per mutant — frontend rebuild, container restart, reseeding.

At this scale, rebuild dominates: ~2.8 hours of full traditional iterations (65s rebuild + ~20s test-and-verdict overhead each) for ~35 minutes of campaign testing. CI pipelines kill campaigns on cost alone, long before anyone asks whether the results mean anything.

### 🔬 Our own instrument lied

Our probe v1 detected *any* validation, not field-specific errors — the target returns generic messages for all fields, so v1 would have certified a fix that fixed nothing. To be explicit: qa-cube (the open-source agent under test) itself had zero defects; the bug was in our measuring instrument.

[SCREENSHOT: probe v1 vs v2 diagram — blind PASS on generic toast vs field-specific FAIL on Username, 30-pic-probe.jpeg ✅]

Calibration, in miniature, is also the `is_regression` story: our verdict hook's own field proved unreliable, so the true metric became `validation_detected == "no"` — we measured around their field instead of through it. Trust the instrument, but build the workaround measurement.

Second case: a min-length rule that passes empty strings (`!value` → true) — emptiness held only by a separate required check. A trap for rule authors, caught by calibration, not by the suite.

One blemish on the Jev record, honestly disclosed: OrangeHRM (the target app) toasts are uninformative ("ErrorInvalid Parameter" for min-length, policy, and empty alike). Detection catches the fact, never the cause — the verdict is fast, the *why* still needs a human.

### 🧭 Solution

Three moves, each boring, compounding together. The point isn't any single trick — it's that every trick was found by measurement, not guessed:

**Move 0 — prove the rig honest, before trusting it:**

- **Honest controls** — failure-simulation correctly FAILS, valid input correctly PASSes. The rig measures what it claims: break manifests, validity passes.

**Move 1 — kill the scoring bottleneck:**

- **First Jev use in campaign** — TypeSafe cloud verdict hook, 358ms avg (~45× vs 16s Playwright run), ~130–150 calls, all sub-second, all free tier. Op-level win, system-level percents — honest proportions beat miracle factors.
- **Automated verdicts** — Playwright executes (14.6–17.4s), the Jev verdict hook classifies (regression or not) in 358ms avg (306–487ms, std 52ms). No human in the scoring loop.
- **General model as fallback: measured, scoped** — in an internal 50-finding benchmark, the general-model fallback (Pi/openrouter) produced a usable correct verdict in 33% of cases at ~15s vs 100% for the structured Jev path at ~0.3s — a narrow operational benchmark, not a claim about LLMs generally. The fast path above is battle-tested on two pilots, third running.

**Move 2 — kill the rebuild:**

- **Pre-built variants** — all four conditions (baseline, break, fix, drift) built once, ~65 seconds each. No rebuilds during the campaign. Trivial in hindsight — invisible beforehand. It surfaced only after we profiled the slow spots instead of optimizing by feel.
- **Fast swap** — 312ms avg switch between variants (190–799ms range, **208×** vs ~65s rebuild). The campaign loop becomes run → swap → run.

[SCREENSHOT: swap architecture — 4 pre-built variants, 300ms loop run→swap→run, no rebuilds, 30-swap.jpeg ✅]

The order mattered more than the tricks: add Jev → profile slow spots (human+agent) → fix by measurement.

### 🛠 Replicate it

Two seeded mutations across four conditions (baseline, break, fix, drift), five probes each, six runs per probe: username-required removed (`SaveEmployee.vue:235`, `SaveSystemUser.vue:93`), password bypass (`PasswordInput.vue:100`), plus baseline and fix conditions.

Breaks flip in via a toggle harness (`required` false→true, all-false assert at the end) — no rebuilds, no hand-editing between runs. After each break: FAIL → retro-edit → PASS, with drift measured via git diff on the engine's instruction paths — its operating instructions (clean diff = engine didn't silently change shape).

Probe v2 extracts per-field errors (Playwright) with per-field validation/regression in a structured schema; variant swap runs ~300ms instead of a 65s rebuild. Concrete outcomes: break manifests on Username only, drift on Password + Confirm.

Terms, once, for readers outside automation: **mutation** = an intentionally planted validation break; **probe** = the check that must prove the break is visible; **oracle / verdict hook** = the logic classifying evidence as regression or not; **calibration** = proving the probe watches the right field for the right reason; **drift** = the agent's instruction paths changing shape unannounced.

### ✅ Result

120 runs, 35 minutes wall time, 5× speedup over rebuild-each-time (4.8× exact — 168/35, ~80% less campaign time). Both seeded mutations behaved as designed across all probes. The retro loop is verified infrastructure now, not a hypothesis: break → FAIL → retro-edit → PASS, with an empty drift diff to prove the engine didn't silently change shape.

[SCREENSHOT: results table — 4 conditions × 5 probes with legend (mutation_score = caught/seeded; native_rate = native hits, transparency only) + Username-only / Password+Confirm outcomes, 30-results.jpeg ✅]

None of this happens without the vendor who said yes: Vadim gave access, opened Discussions on the repo, consented to the name and the numbers. Against vendors who hide behind "proprietary", measurement needs cooperation — this one had it.

Total cost: one setup evening for the variant scheme, then ~35 minutes per campaign — repeat cost near-zero (the night run 01:04–01:39 beat the free-tier expiry the next day — deadlines clarify the mind). The expensive part was never the runs — it was building the variants once and calibrating the probes.

Don't copy our numbers — 120 runs on one build is depth, not breadth. Copy the habit instead: the loop assembles evidence automatically, but the judgment of what a survivor means stays human. Same rule as everywhere in this series: machines count, humans decide.

Assume your first probe lies.

**How do you calibrate your test oracle before trusting it to certify a fix?**

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
- Vadim naming approval for LI article: GRANTED 24.09 ("Yes why not" + 🤯😀🤝) ✅
- Verdict model identity: RESOLVED 28.09 (Jev verdict hook, GLiNER2 family cloud). Jev call count: range ~130–150 (W3, honest range). Wave-ID: CLOSED 29.09 (W3 dig + W1 recount 7a45195: 12 cumulative snapshots 010919→013947 = 10→120 rows, header 01:04–01:39 matches to the minute; setup + evening rerun correctly excluded).
- Code/Infra links: qa-cube repo public (codecube01/qa-cube ✅ linkable); swap_variant.py + Jev client live in PRIVATE pilots dir — NO public link, describe in words only
- Cover + feed + 4 inline (probe v1-vs-v2, timing bars, swap architecture, results table): ALL ✅ 30.09 (probe fact-checked; clocks/swap/results cut from Gemini combo, fact-checked, white edges trimmed; old blue clocks superseded, preserved in git f241818)
- Feed post text ✅ + first comment ✅ (30-first-comment.md, links verified 200 30.09, LI-26 URL matches 28-first-comment)
- Slot: FRI 02.10 LOCKED (29 out Mon)
- Reviews: W3 facts ✅ → W1 fact-check PASS 58d2133 → R1 (user, in-LI paste review 30.09) ✅ → tech-writer review (P0/P1 applied, P1.3 dashes left to user eye) → W1 preflight PASS 7238e51 → W3 preflight PASS 30.09 (2 notes parked per user: unnamed pilots, 168-vs-170 — no fix) → SCHEDULED Fri 02.10 09:00
