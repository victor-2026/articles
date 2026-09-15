# Applitools — Probabilistic Validation Gap (2026)

- **Source:** Tim Hinds, Applitools blog, 2026-09-14 — [Bridging the "Probabilistic Validation Gap"](https://app14743.cloudwayssites.com/blog/probabilistic-validation-gap-agentic-sdlc/) (digest 2026-09-15, verified live)
- **Term:** **Probabilistic Validation Gap** — VLM-валидация UI галлюцинирует (no sub-pixel measurement, token overhead, zero baseline accountability); legacy-селекторы (CSS/XPath) ломаются при каждом рефакторе от агентов ("AI Blackhole", maintenance tax). Скорость генерации x10, уверенность в релизе падает — нет объективного воспроизводимого сигнала.
- **Answer (vendor):** deterministic governance layer — proprietary DLM + Visual AI; 3 новинки: (1) Eyes MCP (`@applitools/mcp`) — агент расследует visual diffs в IDE-чате; (2) Figma design baselines — прямое сравнение live vs Figma URL; (3) NLP test steps (`eyes.run`) — plain-English степы в Playwright, self-heal без публичных LLM.
- **Claim:** 80% lower maintenance tax (непроверено — кандидат под mutation matrix).
- **Why it matters here:** вендорское название нашей проблемы (silent false negative + verification gap, Article 26). "Детерминированный оракул" = то же, что VerdictGate делает правилом (exit-code contract, golden diff, determinism). Eyes MCP = агент как visual QA partner — родственно guided QA engineer (Article 27), но с другой стороны: агент расследует, человек гейтит.
- **Routing:** Article 26 follow-up ("the method, codified") + VerdictGate-позиционирование + конкурентный ландшафт (Applitools vs QAEverest / testRigor / Agentiqa). Термин берем, клеймы — только через независимый прогон.
- **Status:** candidate, not validated. No independent run.
