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
7. `WORKING-NOTES.md` — multi-window contract (notes placement, locks, owners)

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
- Author line: `Victor Ematin · AI Quality Engineering Lead · OpenCode Go` (no `$0 budget` — recruiters = 12% of profile viewers, reinforces R&D perception; budget numbers stay in article content, hashtag #ZeroBudgetQA stays for practitioner audience)
- Max 9 emoji per post
- Author line and hashtags always on separate lines at the bottom
- `raw/` never modified by AI (read-only source)

## Publication Workflow

1. User publishes post manually on LinkedIn
2. User shares post URL + confirms publication in chat
3. After confirmation, AI updates:
   - `hooks-library.md` — add hook(s) from published post
   - `performance-log.csv` — add row with date, topic, format, metrics (use `?` for unknown)


## Quotes Bank (`quotes.md`) — ОБЯЗАТЕЛЬНОЕ

- **Когда:** при КАЖДОЙ сессии, где юзер показывает посты/статьи/материалы (LinkedIn-посты, деки, подкасты, чужие статьи) — агент обязан отобрать сильные цитаты и занести в `quotes.md`.
- **Что:** формулировки, которые можно процитировать в будущих статьях (автор, метафора, тезис, цифра-контраст). Подбирать по принципу «одна строка смысла на цитату».
- **Формат (из header quotes.md, соблюдать всегда):** только с URL первоисточника + пометкой предлагаемого использования. Не свалка: абзац → до 1-2 сильных строк.
- **Секции:** добавлять/поддерживать тематические секции (`## Evals vs Tests`, `## AI Safety`, `## Independence / Attestation` и т.п.) — новые источники идут в существующую секцию или создают новую.
- **Покрытие для этого правила:** любые материалы, которые юзер сегодня дал (прямо в сообщении, репостом, ссылкой, PDF, профилем) — включая, но не ограничиваясь: LinkedIn-посты, презентации/деки, книги, статьи, комментарии, репосты.
- **Исключение:** конфиденциальная переписка (например, email от вендора) — заносить только с пометкой «private channel - public use requires consent».
- **Завершение:** в конце сессии упомянуть в session-checkpoint: сколько цитат добавлено и в какие секции.


## Subagents & OpenRouter — Free First (Global)

- Pi via `pi-subagents` (scout, researcher, worker, reviewer, oracle, delegate) — global `~/.pi/agent/settings.json`: `defaultProvider: openrouter`, `defaultModel: openrouter/free`, `enabledModels: [openrouter/*:free, openrouter/*, groq/*]`
- Free limits: 20 RPM, 1000/day (≥$10 lifetime credits, else 50/day) — shared across all `:free`, 429 = hit cap or provider pool busy
- Rule: try `:free` / `openrouter/free` first, on 429 fallback to paid variant (same slug without `:free`), concurrency 1-2, exponential backoff, Retry-After
- OpenCode delegates via bash: `pi --provider openrouter --model openrouter/free --print "Use reviewer to review this diff." -- @diff.txt`
- Интенсивность платного режима: `maxSubagentSpawnsPerRun=3` (было 64), `thinking medium=4096` (было 10240), `compaction 8192/10000` — лимит длительности/интенсивности если не free (0.5$/сессию)
- Also works headless in CI: `pi --mode json` or via `opencode` bash tool


### OpenRouter — Лимит и отчет (платный режим)

- Лимит зафиксирован: **1$/день**, **0.5$/сессию агента** (в дашборде https://openrouter.ai/keys → Edit → Limit 1 / daily, сейчас там 3 — поменяй вручную)
- Проверка: `~/.pi/agent/scripts/openrouter-guard.sh` (проверяет daily + сессию 0.5$ — ` --check-session 0.5`) (выводит `daily / 2.0`, остаток; пишет в `~/.pi/agent/openrouter-guard.log`)
- Уведомление оперативное: при ≥0.75$ (75%) — macOS notification `Glass`, при ≤0.1$ остатка — `Sosumi` + лог
- Отчетик по завершении платной работы: `~/.pi/agent/scripts/openrouter-guard.sh --report` → `~/Backups/ai-qa-wiki/openrouter-report-YYYY-MM-DD.md` + notification `Pop`
- LaunchAgent: `com.openrouter.guard` каждые 10 мин (`StartInterval 600`) + при загрузке
- Перед платной сессией: `openrouter-guard.sh` (проверка), после: `openrouter-guard.sh --report` (отчет)

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
