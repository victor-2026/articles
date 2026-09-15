# Spotify Portal: Token Routing That Cuts Claude Code Spend ~90% (Sep 2026)

**Sources:** [Stanislav Beliaev post](https://www.linkedin.com/) (via user share, 11.09) · [Spotify eng blog](https://engineering.atspotify.com/2026/9/portal-by-spotify-cut-my-claude-code-token-usage-by-90) · [plugin repo](https://github.com/spotify/portal-ai-plugins)
**Digest:** ручной заход 11.09 (не RSS)

## Facts

- **Problem:** 25% eng leaders spend $200–500/dev/mo on tokens, some past $2000; by 2028 AI coding costs expected to exceed avg dev salary. Most spend = I/O (open 5 files to answer about 1 method; test copying 20 neighbors) — thousands of tokens, ~zero reasoning.
- **Fix (2 parts):**
  1. **Two cheap workers** (1 YAML each: prompt + Gemini 2.5 Flash, temp 0.2): `bulk-reader` (files → structured bullets), `code-writer` (reference file → matching code).
  2. **`shunt` plugin, 3 layers:** Hooks (full Read >350 lines blocked, rerouted to bulk-reader; targeted reads pass) → Scripts (Portal CLI wrapper, ship files, write to disk) → Skills (invocation syntax md).
- **Key learning:** rules in CLAUDE.md were advisory → Claude ignored them. Hooks made behavior **enforceable**. Raw files + generated code never enter Claude's context.
- **Result:** ~90% avg token savings on bulk reads (Java monorepo).
- **Caveats:** editing/reasoning can't be delegated; each delegation +10–30s round trip → small files not worth routing.
- **Install:** open source, 3 commands, via Portal by Spotify.

## Why it matters for us

1. **Advisory → enforceable** = наш тезис про гейты (Articles 23/25, human gate в 26): проверка, которую можно проигнорировать, — не проверка. Spotify доказал это на токенах.
2. **Token economics питает ZeroBudgetQA:** наши лимиты (OpenRouter $1/день, free-first) — та же дисциплина снизу. Их цифры ($200–500/dev) — аргумент для статей про стоимость AI-QA.
3. **Применимо к нашим пайплайнам:** bulk-reader паттерн (дешевая модель для I/O, флагман для reasoning) — кандидат для ai-qa-wiki ingest и digest-саммари (сейчас все жрет флагманский контекст).

## Cross-links

- AGENTS.md Subagents & OpenRouter (free-first, лимиты) — та же экономика, другой масштаб.
- Article 25 (vendor gates): enforceable > advisory.
- Article 26 (human gate): гейт, который нельзя обойти.
