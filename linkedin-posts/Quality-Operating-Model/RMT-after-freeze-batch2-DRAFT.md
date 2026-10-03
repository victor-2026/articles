**Format:** LinkedIn Pulse Article (follow-up)
**Series:** Quality Operating Model (earliest Mon 05.10 — 48h after Friday 30)
**Status:** draft v1 (W4, 02.10 — from fully-reviewed skeleton; needs W1 fact-check of full draft → R1)
**Cover:** TODO (proposal: "frozen engine vs living results" — padlock + growth curve, dark + amber series style)
**Feed Image:** cover doubles as feed preview
**Hook:** We froze the engine. It kept teaching: 95 seeded mutants across 98 run-records, a crash that proved the mapping, and one honest limit we never published.
**Links back:** 29 (Leonardo union) + 30 (120 runs) via first comment (no bare URLs in body — series rule)

---

# What Changed After the Freeze: Batch #2, a Stamp Saga, and the Limit We Didn't Publish

We froze the engine. It kept teaching. Since the freeze: 95 seeded mutants across 98 run-records, a second batch that closed everything the first left open, three survivors re-run nine times, a crash that proved the exit-code mapping — and one honest limit of our own method that lived in a draft until today.

Last week set the stage: a joint piece with Leonardo Lanni on reverse mutation meets verdict policy, then a 120-run campaign proving our own probe lied before it measured. This note is what happened after — the news, the numbers, and the limit we should have published sooner.

### ❓ Problem

A freeze stops the code, not the learning. Three things kept moving after we stopped touching the engine: new mutant batches ran against old blind spots, confirmations reclassified survivors, and two gaps in our own honesty stayed open — our method's mapping limit lived only in a draft, and nobody had answered where seeded evidence lives in an outsider's lifecycle. A frozen engine with unpublished limits is a paused story, not a finished one.

### 🔬 Batch #2: the chains v1 never saw

Batch #2 hunted one scope: `expect.element()` chains — twenty-nine of them across unit specs in eleven files — that the v1 scanner saw as matcher="element" and walked straight past. Eleven files scouted, nine yielding, twenty-four seeded mutants. Twenty-seven run-records: twenty-two killed outright plus error-rerun rows on three mutants.

The closeout reads like a control experiment passing: twenty-two killed means the suite works. Two inconclusives went to resolution — a tooltip crash and a wa-controls kill — and zero inconclusive remain. Batch #2 closed exactly what batch #1 left open: survivors went to confirmation, everything else went green for a reason.

### 🧬 After the freeze: guards, softness, stamps

The engine evolved in four moves, one line each. A NO-OP guard skips `mutated == original` — seeder defects like `toHaveLength(0)` onto itself, which the scorer rejects with exit 2. Softness treats `expect.soft(...)` as a hop inside chain-unwrap, not a separate pattern (the OpenClaw spec uses it three hundred twenty times). Chains are batch #2 above — a scope, not an engine feature. And the stamp: every mutant carries its engine version, one batch, one version.

Then the confirmations. Three batch-#1 survivors re-ran three times each with reverts between runs — nine records, console log kept. Two survived all three runs and became genuine coverage gaps, promoted into gold as P2. The third died all three times once its branch executed: the original survival was vacuous, a switched-off environment branch, demoted to noise.

And the stamp saga, told honestly: batch #1's fifty-eight rows are unstamped — a pre-stamp engine, now the discipline's cautionary tale about versioning evidence. The batch #2 closeout carries stamp 0.1.0. The confirmation runs carry nothing, correctly unstated — pre-stamp seeds, no retroactive labeling. Never let anyone tell you both packs carry the version. Precision about provenance is the whole game.

### 📊 40% vs 91%: different layers, different denominators

Ten hand-set toggles of runtime behavior — streams, computer tools, oauth flows — each run six times, plus twenty-one green baselines: eighty-one records. Four of ten killed; the survivors split into honest gaps with no covering suite and blind spots the assertions never watched. Kill rate forty percent, zero crashes, zero flakes — unanimous six-of-six everywhere.

Against batch #1's ninety-one percent this looks like collapse. It isn't — it's a different layer. Ninety-one percent measures unit operators with the suite staring straight at the mutant. Forty percent measures behavior, where half the mutants fall past the assertions. Operator kill-rate does not extrapolate to behavioral: different layers, different denominators, separate packs. Mix them and you manufacture a number that means nothing.

### 💥 The crash that proved the mapping

One mutant earned the lead. Baseline: exit zero, thirty seconds, twenty-four passed. Mutant: exit -9, six hundred thirty-two seconds — the third consecutive hang — CPU pinned between thirty and two hundred percent across all twenty samples, output empty. The suite went red through the crash, via the pre-registered exit-code mapping: no human judgment in the loop between the hang and the verdict.

The mechanism is a hypothesis — negated visibility deadlocking the fixture — and this note says so plainly. That caveat is the point: a crash class is a universal fear, the arc is clean (three hangs in a row), and the honesty about what isn't established is what makes the established part believable.

### 🪞 The limit we didn't publish

Here is the honest limitation, first time in public: our profiles encode numbers, not gate shapes. Their B2 gate is an AND of cap and floor — at most one survivor at any N, score above sixty. Ours is a band: five percent at N above twenty, small-N floor below. Same letter, different machinery. We verified this limit never reached the published piece — it lived in a draft, and unpublished honesty doesn't count. So here it is, with its table.

[SCREENSHOT: Mapping Limit table — B2 Cap / B2 Score / Decision logic, QAEverest vs VerdictGate]

Publishing the limit strengthens the gate it bounds. A method that names where it stops is a method you can place.

### 🧭 Where seeded evidence lives

Not in the testing lane — at the governance gate every outsider lifecycle already has. Testing produces claims, green suites among them. The gate is where someone outside testing asks why this particular green should be trusted: release boards, procurement evidence requirements, regulated validation packages — same slot, different names. A seeded verdict plugs into that slot as a fact (defects planted, caught or not) rather than another claim, which is why it travels across governance, commerce, enterprise, and regulated worlds without translation. The gate exists everywhere; only its name changes.

Our campaign lifecycle — seed, inject, run, classify, attest, close — answers how the evidence is produced. Gate placement answers where it is consumed. The commercial hole was the missing second half. Now it isn't.

### ✅ Result

A skeptic of this caliber attacked the premise directly: a probe tests known fault classes, and detecting a created problem doesn't prove recognizing an unimagined one. The answer is built into the matrix, in writing: report gaps first, then the verdict — unknowns are why the verdict is per-tier with explicit scope, never a blanket zero. Seeded checks prove the gate holds on knowns; discovery of the unimagined lives where evidence gets stitched across the enterprise. Different instruments, same verdict meeting.

Terms, once: **seeded mutant** = an intentionally planted break; **kill rate** = caught divided by seeded; **closeout** = the verdict pack that resolves every inconclusive to zero; **stamp** = the engine version each mutant carries; **gold** = human-confirmed labels a judge is scored against.

Don't copy our ninety-five mutants — one engine is depth, not breadth. Copy the habits instead: version every mutant, resolve every inconclusive, publish every limit, and place the evidence where someone outside testing already asks for it. Same rule as everywhere in this series: machines count, humans decide.

The freeze held. The engine didn't.

**Where does seeded evidence live in your lifecycle — testing lane, governance gate, or nowhere yet?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Source
- Skeleton: `RMT-followup-what-changed-after-freeze-SKELETON.md` (all 9 sections CERTIFIED, W1 §§6-7 + W2 §2 + W3 §§2,4 + §3 verbatim)
- §3 English rendering: W3's Russian verbatim translated by W4 (meaning preserved; W3 to confirm rendering at draft review)
- Altman-style numbers spelled out in body per readability (digits in markers/ledger stay)

### Facts (ledger refs — see skeleton for full ledger)
- 95 seeded mutants / 98 run-records (units labeled, W2 ruling); B5 11/9/24; 22 killed + 2 resolved, zero inconclusive (closeout :16-17)
- S4/S5 3/3 genuine P2 (E4/E5), S1 vacuous NOISE (E1); batch1 UNSTAMPED, closeout stamped 0.1.0 (:5), confirmation unstamped
- appmut 81 rows, 21/21 green, M2/M4/M5/M9 killed, 4/10 = 40%, 0 flakes; 91% = 53/58 batch #1 (assertion level)
- tooltip:213 EQ_NEGATION: exit 0/30s/24 passed vs exit -9/632s 3rd hang, CPU 30–200% × 20 samples, empty output (closeout :11); mechanism = hypothesis NOT established
- Mapping Limit: QAEverest B2 AND-cap/floor vs VerdictGate band 5% + small-N floor (29-DRAFT L205-217; absent from live public per W1 1fc7c59)
- Lifecycle thesis: W1 e3f4943 verbatim core (gate, not lane; fact-not-claim travels untranslated)
- Kanaris pushback quotes ×3 (banked; reply = W1 track — doctrine only, no DM content)

### Open
- H1: v1 drafted (v2/v3 one-line swaps on user word)
- Cover: proposal in metadata — user picks style, Gemini generates (EN spec → fact-check)
- Inline visuals: Mapping Limit table image (mandatory) + candidates (B5 scope strip, stamp timeline, 40-vs-91 layers) — propose after text lock
- Feed post text + first comment: TODO (draft after text lock; links: verdictgate root — verify 200 at publish, 29 URL, 30 URL)
- Reviews: W1 fact-check of THIS draft → R1 (user) → earliest Mon 05.10
