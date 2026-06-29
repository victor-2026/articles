# Articles — AGENTS.md

## Boundaries

| Area | AI can | AI ask | AI cannot |
|------|--------|--------|-----------|
| `wiki/*.md` | ✅ edit | | |
| `linkedin-posts/*.md` (except `Old/`) | ✅ edit | | |
| `linkedin-posts/Old/*` | | | ❌ never |
| `linkedin-posts/performance-log.csv` | ✅ append rows | | |
| `raw/*` | | | ❌ never |
| `_Тезисы.md` | | ✅ ask before edit | |
| `md2linkedin.py`, `pbcopy-html.swift` | | ✅ ask | |
| `README.md` | ✅ edit | | |
| `AGENTS.md` | ✅ edit | | |

## Architecture

```
raw/  ──→  wiki/  +  linkedin-posts/  +  performance-log.md
Notion  ──→  kanban/  (sync: bot/notion-sync-kanban.py)
```

- **raw/** — human-only source input (analytics exports, reference links, ideas). AI reads but never modifies.
- **wiki/** — AI-owned knowledge base: post formats, emoji rules, strategies, guides.
- **linkedin-posts/** — post drafts organized by project or theme. Each subdirectory = one series.
- **linkedin-posts/Old/** — archive. Immutable by AI.
- **linkedin-posts/performance-log.md** — published post metrics (markdown table for Obsidian). Source file is `.csv` — AI edits CSV, regenerates MD.
- **linkedin-posts/weekly/** — auto-generated weekly reports from CSV.
- **kanban/** — auto-generated from Notion Tasks DB. Edit in Notion only.
- **md2linkedin.py**, **pbcopy-html.swift** — tooling scripts. Edit only with human approval.

## Sources of Truth

1. **Notion Tasks DB** — tasks kanban (source of all kanban/*.md files)
2. `AGENTS.md` — this file
3. `wiki/LinkedIn форматы и стратегии использования.md` — format rules
4. `wiki/Emojis 🚀 ✨❓.md` — emoji conventions
5. `_Тезисы.md` — content ideas pipeline
6. `.opencode-memory.md` — global memory

## Kanban Sync

- Source of truth: Notion Tasks DB (`37da5ab6-666f-8028-a641-fdc8bfa0574b`)
- Local mirror: `kanban/*.md` — auto-generated, DO NOT EDIT manually
- Sync command: `python3 ~/bot/notion-sync-kanban.py`
- Sync method: Polling via Telegram bot (every 60s, in progress items) + manual on request
- To add/edit tasks: use Notion board directly

## Anti-Patterns

1. **No secrets** — no tokens, passwords, or PATs
2. **No dated facts** — avoid "as of May 2026"; use "as of last update"
3. **No model-specific instructions** — must work with any LLM
4. **≤ 32 KiB** — keep files small; split when exceeded

## Post Conventions

- Format: **hook** → body → CTA → **author line** → hashtags
- Author line: `Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go` (use both by default if within char limit; skip `$0 budget` only if article clearly uses paid tools or Go for execution)
- Max 9 emoji per post
- Author line and hashtags always on separate lines at the bottom
- `raw/` never modified by AI (read-only source)

## Publication Workflow

1. User publishes post manually on LinkedIn
2. User shares post URL + confirms publication in chat
3. After confirmation, AI updates:
   - `hooks-library.md` — add hook(s) from published post
   - `performance-log.csv` — add row with date, topic, format, metrics (use `?` for unknown)

## Communication — Full File Paths (MANDATORY)

In opencode-desktop TUI (macOS): **only `mailto:` is clickable**. file://, /Users/.../path, markdown links = NOT clickable.

**Always provide: full absolute path + bash code block with `code` command.**

```
File: /Users/victor/.../file.md
```bash
code /Users/victor/.../file.md
```
```

For multiple files: one bash code block with multiple `code` lines.
For email: use `mailto:user@domain` (clickable!).

Full rule + examples: `~/.opencode-memory.md` → "Communication Style — File Paths"
