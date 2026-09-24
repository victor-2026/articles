**Format:** GitHub Discussions post (qa-cube repo, Vadim's turf) — NOT LinkedIn
**Status:** DRAFT approved, to post by user. Sequence: (1) DM text to Vadim for approval → (2) enable-Discussions ask → (3) post publicly. On article-B publish: EDIT post body (add link), not comments.
**Source facts:** W3 pilot checkpoint 2026-09-23/24 (Phase 1-3, 120 runs).

---

**Mutation-attestation pilot: 120 validation runs (5 probes × 6 runs × 4 conditions) against 2 seeded mutations, zero qa-cube product defects**

Phase 1–3 done on free tier (OpenRouter + Pi subagents). Verdict first: no product defects found in qa-cube across 120 validation runs (~35 min wall time, 4 conditions × 5 probes × 6 runs, 2 seeded mutations).

What held up:
- 4-role separation operational (Manager/Analyst/Manual/Automator)
- Honest degradation confirmed — Automator refuses without evidence instead of inventing results
- Retro loop verified end-to-end (break → FAIL → retro-edit → PASS, drift measured via git diff)
- Spec-vs-reality fires: Analyst marks assumptions correctly

Honest caveat (our side, not yours): probe v1 detects any validation, not field-specific — OrangeHRM returns generic errors for all fields. Probe v2 will extract field-level errors.

Thanks for the MIT release — the architecture made this pilot possible. Full methodology write-up coming as a separate article; will link it here.

---

## 🛠 Служебные заметки (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

- Numbers to verify before posting: 120 runs / 35 min / 2 mutations (W3 checkpoint).
- Tone: peer feedback, no ask, no trial talk (Vadim burned twice on "trial").
- Follow-up: on article-B publish, edit body (append link section).
