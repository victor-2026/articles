# Working Notes Contract — multi-window orchestration

**Why:** chat evaporates, files persist. All cross-window state lives in files, not in chat history.

## 1. Where notes live

- Article drafts: `## 🛠 Служебные заметки редактора (не публиковать)` section at the END of the file, AFTER hashtags. Subsections = `###`.
- Pilot runs: `pilot-log.md` (Positions-CV-CL). Vendor comms: `outreach/`. No triple bookkeeping — see §5.
- Copy-paste into LinkedIn STOPS at hashtags. Reviewers (human, Pi, Google) evaluate ONLY above the marker.

## 2. Machine-readable marker

First line under the section header must be:
`<!-- REVIEWERS: IGNORE BELOW THIS LINE -->`
Humans read the header, agents grep the marker.

## 3. Status tokens (grep-able, owner + date mandatory)

- `⏳ PENDING (owner, since DATE)` — open item. No owner = doesn't exist.
- `✅ DONE (DATE)` — closed.
- `⛔ BLOCKED (on WHAT, since DATE)` — waiting.
- `🔒 HELD (owner, since HH:MM, task)` — file lock, see §4.

## 4. Single-writer lock (mutex)

- Before editing a file, check the top of its 🛠 section for 🔒.
- Fresh lock (< 30 min by file mtime — mtime IS the heartbeat): do NOT touch. Write `⏳ WAIT (owner, want)` below it and move on. No spinlocks.
- Stale lock (mtime > 30 min, no movement): do NOT break it yourself. Notify the USER in chat (`stale lock by X, take over?`). User decides in one line.
- Clinch (two windows want the same file): both report to the USER. Agents never negotiate peer-to-peer — the user is the bus.
- Silent holder = abandoned holder: no response in its window → same stale path after 30 min.
- Timeout: **30 min** (agreed 11.09; revisit if pace changes).

## 5. Canonical map (one home per fact)

| Fact | Lives in | Nowhere else |
|---|---|---|
| Article text | article file | — |
| Pilot runs | pilot-log.md | — |
| Vendor comms | outreach/ | — |
| Cross-window decisions | the artifact they gate (working notes) | — |
| Session history | session-checkpoint.md | — |

## 6. Stale sweep

- Pre-publish: no `##` in body, notes below hashtags, no rule contradicting a decided item.
- Decided items stay as `~~struck~~ + ✅ date`; never delete history, never leave live contradictions.

## 7. Edit discipline (gotcha #4, 2026-09-11)

- `oldString` must match EXACTLY (whitespace included). On mismatch error: STOP, re-read, never widen the guess.
- Bulk edits (replace-all, script rewrites): assert match identity + count BEFORE replacing (`grep -c`, `old in t`); abort on surprise. Re-read the region AFTER.
- "Success" without verification = silent content loss. Trust `grep`, not the tool's OK.

## 8. Freeze protocol (body freeze → deployment queue, 2026-09-12)

- Frozen body takes NO new material — freeze protects the review chain (vendor-verified facts), not the text.
- Fresh material deploys in order, never into the body:
  1. **First comment** — 1–2 external quotes backing the thesis (zero risk).
  2. **Follow-up post** (mid-week) — chorus angle + link back (second wave, no new facts needed).
  3. **Sequel backlog** — material big enough for its own article (parked, not inserted).
  4. **Other windows** (framework, sibling articles) — via working-notes parks.
- Rationale: insertions bloat tempo and force re-verification; the queue compounds reach instead.

## 9. Window reset protocol (new window + failed window disposal, 2026-09-24)

1. **Copy the failed window's name**, clarify export need — export transcript if it holds verbatim material, else delete outright (archived loops re-infect future sessions as "sources").
2. **Create new window in Plan mode** — grant project access (narrow dirs; read-only mounts where possible).
3. **Startup order (first message):** read root AGENTS.md + `verdictgate/docs/window-discipline.md` (own row = own zone) + session-checkpoint tail (50 lines). Rename window. Then micro-task #1 (one task → diff → stop).
