**Format:** TBD (skeleton suggests Pulse Article — scope outgrew a note; user decides)
**Series:** Quality Operating Model (RMT follow-up, earliest Mon 05.10 — 48h after Friday 30)
**Status:** SKELETON v1 (W4, 30.09 — structure + certified facts only; engine facts await W2/W3)
**Links back:** 29 (Leonardo union) + 30 (120 runs) — URLs at publish time
**Spec sources:** W3 inventory 29.09, W2 reframe + count f945e1f, W1 spec b4bc3c9 + mandates 1fc7c59, W5 Kanaris bridge

---

# HEADLINE OPTIONS (news angle, pick one)

1. What Changed After the Freeze: Batch #2, a Stamp Saga, and the Limit We Didn't Publish
2. 95 Mutants, 98 Records: What the Engine Learned After We Stopped Touching It
3. The Honest Limit of Our Mutation Method (Plus Everything New Since September)

---

## 1. ANCHOR (certified — links to 29, one paragraph)

- 29 established: RMT × VerdictGate union, live on Leonardo's Pulse 29.09. One-line recap + link.
- 30 established: infrastructure trust (120 runs, probe calibration). One-line recap + link.
- This note: what happened AFTER the freeze — engine kept evolving, new batches ran, and one honest limit stayed in the draft. Now published here.

## 2. NEWS: WHAT CHANGED AFTER FREEZE (W2+W3 facts, W4-verified 02.10 — all 9 artifacts exist, load-bearing lines spot-checked)

- Batch #2 = B5 scope: `expect.element()` chains the v1 scanner skipped (it saw matcher="element" and walked past). 11 files scouted, 9 yielding, 24 seeded mutants (`scripts/run-rmt-campaign-batch2.py:22`). Result (`results/rmt-campaign-batch2-20260924_232138.jsonl`, 27 rows): 22 killed outright + error-rerun rows on three mutants. Closeout (`results/batch2-verdict-closeout-2026-09-26.md:16-17`): 22 killed = controls (the suite works), 2 inconclusive resolved — tooltip Caught-by-crash + wa-controls Killed. Zero inconclusive remain. Batch #2 closed exactly what batch #1 left open.
- Engine evolution, one line each (W2 side — Jev engine; W3 scope boundary respected): NO-OP guard (`rmt.py:160`) skips `mutated == original` (e.g. `toHaveLength(0)` onto itself) — seeder defects the scorer rejects with exit 2. soft (`rmt.py:32,92,113`) treats `expect.soft(...)` as a hop in chain-unwrap, not a separate regex (OpenClaw spec: 320 usages). chains = B5 above (W3 scope, not an engine feature — do not mix). stamp (`rmt.py:23` + `:171`): `RMT_VERSION = "0.1.0"`, every mutant carries `rmt_version` — one batch, one engine version.
- S4-confirmation + stamp saga: three batch-#1 survivors re-run 3× with revert between runs (`results/confirmation-runs-20260925_004815.jsonl`, 9 rows; console `results/confirmation-console-20260925_034815.log`). S4 (auth:295) and S5 (sugg:255) survived 3/3 → genuine coverage gaps, gold E4/E5 = P2, closed (`results/confirmation-verdict-2026-09-26.md:10-11`). S1 (profile:677) killed 3/3 at PROOF=1 → original survival VACUOUS (env-gated branch was off), gold E1 = NOISE (`:12`). Stamp saga, corrected per W2: batch #1's 58 rows are UNSTAMPED (pre-0.1.0 engine — "run on a pre-stamp engine" is now the discipline's cautionary tale); batch #2 closeout stamped 0.1.0 (`:5`); confirmation runs unstamped (pre-stamp seeds, correctly unstated — never "both packs carry 0.1.0").
- Count, with units labeled (W2 ruling — bare 95/98 banned): **95 seeded mutants across 98 run-records** (58 + 24 + 4 + 9 mutants; 58 + 27 + 4 + 9 records, delta 3 = error-rerun rows).

## 3. ANCHOR CASE: appmut 4/10 (W3 narrative verbatim 02.10, W2 concur 768511b)

appmut — это 10 ручных тоглов поведения OpenClaw-рантайма (stream, computer-tool, oauth…), каждый прогнан 6× плюс 21 зеленый бейзлайн = 81 запись. Убиты 4 из 10 (M2/M4/M5/M9); выжившие — либо честные дыры (M6/M10 без покрывающей сюиты), либо слепые зоны ассершенов (M1/M3/M7/M8). 40% против 91% batch #1 — потому что 91% меряет операторы, на которые сюита смотрит в упор, а 40% меряет поведение, где половина мутантов падает мимо ассершенов. Вывод пака: операторный kill-rate не экстраполируется на behavioral — разные слои, отдельные знаменатели.

(W4-verified supplements, в драфт по месту: вердикт = локальный vitest exit, без Jev в петле; zero exit -9; zero flakes — все 6/6 единогласно. Refs: appmut-verdict :3/:8/:25.)

## 4. MEAT: A — Caught-by-crash (W2+W3 concur; B parked) (W3 facts, W4-verified 02.10)

tooltip:213 EQ_NEGATION. Baseline: exit 0, 30 seconds, 24 passed. Mutant: exit -9, 632 seconds — third consecutive hang — CPU sustained 30–200% across all 20 samples, empty output (`results/batch2-verdict-closeout-2026-09-26.md:11`). Suite red through crash, via the pre-registered exit-code mapping. Mechanism is a hypothesis (negated-visibility deadlocks the fixture — NOT established, and the note says so). Why it leads: a crash class is a universal fear, the arc is clean (three hangs in a row), and the mechanism caveat is model epistemics.

Parked: B — S1-vacuous in one line (killed 3/3 at PROOF=1; original survival was a switched-off env branch — a thin truth about env-gating, good for wave two, not for the hook).

## 5. GUARD: qa-cube H4 (binding, W1)

- H4 = MT-direction CONTRAST ("two ways to seed"), never "second RMT case". One paragraph max. Overstatement blocked.

## 6. MAPPING LIMIT (certified — from 29-DRAFT, now published here)

- Honest limitation: VerdictGate profiles encode numbers, not gate shapes. (W1 verified 1fc7c59: absent from live public — this note is its first publication.)
- QAEverest B2 = `survived <= 1 AND score >= 60` (AND of cap + floor, absolute cap at ANY N).
- VerdictGate B2 = band ≤5% at N≥20, small-N floor max 1 at N<20.
- Table (as image or text per length): B2 Cap / B2 Score / Decision logic rows.
- Frame: why publishing the limit strengthens the gate (unpublished honesty doesn't count).

## 7. LIFECYCLE PLACEMENT (thesis: W1 e3f4943 via owner 02.10 — fact-check on section draft by W1)

Seeded evidence doesn't live in the testing lane — it lives at the governance gate every outsider lifecycle already has. Testing produces claims (green suites); the gate is where someone outside testing asks "why should I trust this green?" — release boards, procurement evidence requirements, and regulated validation packages all have this slot, each under a different name. A seeded verdict plugs into that slot as a fact (planted defects, caught-or-not) rather than another claim, which is why it travels across governance, commerce, enterprise, and regulated worlds without translation: the gate exists everywhere, only its name changes. Campaign lifecycle (how we produce the evidence) answers our question; gate placement (where the evidence is consumed) answers theirs — the commercial hole is the missing second half.

## 8. KNOWNVS-UNKNOWN (Kanaris bridge, certified quotes)

- Kanaris pushback 30.09 (banked): probe tests known fault classes; recognition miss is unknowns-adjacent; tool evidence ≠ product evidence.
- Our answer (W5 structure, W1 owns reply — note carries the doctrine, not the DM): gaps-first matrix already claims the opposite of blanket-zero; QI discovers unknowns, seeded checks hold knowns. Different instruments, same verdict meeting.
- Frame: a skeptic of this caliber attacking the premise becomes part of the article's limit section, not a footnote.

## 9. CLOSE + CTA + LINKS

- Close line (draft): "The freeze held. The engine didn't. Here's everything it learned — and the one limit we should have published sooner."
- CTA (draft): "Where does seeded evidence live in your lifecycle — testing lane, governance gate, or nowhere yet?"
- First comment: repo links (verdictgate root — verify 200 at publish), 29 URL, 30 URL.

---

## 🛠 Служебные заметки (не публиковать)

### Fact ledger
| Claim | Source | Status |
|---|---|---|
| Mapping Limit numbers (B2 AND/band) | 29-DRAFT L205-217 | CERTIFIED (file) |
| Absent from live public | W1 guest-fetch 1fc7c59 | CERTIFIED (bus) |
| Count: 95 seeded mutants across 98 run-records (units labeled, W2 ruling — bare 95/98 banned) | W2 recount + W3 cross-check (27 rows = 24 unique + reruns) | CERTIFIED 02.10 (W4: 9/9 artifacts exist, counts match) |
| Batch #2 B5 (11 files, 9 yielding, 24 mutants; 22 killed + 2 resolved, zero inconclusive) | run script :22, batch2 jsonl (27 rows), closeout :16-17 | CERTIFIED 02.10 (W4 spot-checked) |
| Engine one-liners (NO-OP :160, soft :32/92/113, stamp :23/:171; chains = W3 B5 scope, not engine) | W2 facts, W3 scope boundary, W2 engine-split concur | CERTIFIED 02.10 (rmt.py lines match in checkout) |
| S4/S5 3/3 genuine P2 (E4/E5), S1 3/3 killed at PROOF=1 → vacuous (E1 NOISE) | confirmation jsonl (9 rows) + console log, confirmation-verdict :10-12 | CERTIFIED 02.10 (W4 spot-checked) |
| Stamp saga CORRECTED: batch1 UNSTAMPED, batch2 closeout stamped 0.1.0 (:5), confirmation unstamped (never "both carry 0.1.0") | W2 correction (same class as blocked letter) | CERTIFIED 02.10 |
| appmut 4/10 (81 rows, 21/21 green, M2/M4/M5/M9 killed, 0 flakes; 40% behavioral vs 91% assertion, layers don't extrapolate) | appmut-verdict :3/:8/:15-23/:25 | CERTIFIED 02.10 (W4 spot-checked) |
| Meat A (tooltip:213, exit -9/632s 3rd hang, CPU 30–200%, mechanism = hypothesis NOT established); B parked | closeout :11, W2+W3 concur | CERTIFIED 02.10 |
| §3 narrative verbatim (toggles/stream/oauth, 40-vs-91 via gaze distance) + W4 supplements (vitest exit, no Jev, 0 flakes) | W3 text, W2 concur 768511b | CERTIFIED 02.10 |
| Kanaris quotes ×3 | quotes.md (W5 handover) | CERTIFIED (banked) |
| Lifecycle thesis (gate, not lane) | W1 e3f4943 via owner 02.10 | CERTIFIED (bus; W1 fact-checks section draft) |

### Open
- Format: note vs Pulse Article (scope says article; user decides)
- Reviews: §6+§7 W1 CONFIRM 0bc2aee ✅ → §2 W2 CONFIRM eba3d66 ✅ → §§2,4+§3 W3 CONFIRM (rmt.py lines = W2 768511b, §3 verbatim inserted) ✅ → W1 fact-check of full draft → R1 (user) → earliest Mon 05.10
