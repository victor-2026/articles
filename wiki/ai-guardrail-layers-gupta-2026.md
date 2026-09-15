# 7 Guardrail Layers for Production AI (Gupta, Sep 2026)

**Source:** [Antrixsh Gupta post](https://www.linkedin.com/) (via user share, 11.09) — taxonomy, 2 lines per layer, plus thread
**Digest:** ручной заход 11.09

## The 7 layers

1. **Input** — sanitize requests (injection, unsafe inputs).
2. **Prompt** — protect system instructions (jailbreaks, hijacking, leakage).
3. **Retrieval** — ACL-aware retrieval, source validation, grounding.
4. **Tool** — least privilege, allowlists, approval gates, transaction limits.
5. **Output** — validate responses (PII, unsafe content, unsupported claims).
6. **Runtime** — token budgets, rate limits, circuit breakers, loop detection.
7. **Memory** — session isolation, retention, TTLs, sensitive-memory controls, deletion.

## Thread signals

- Carlos Shoji: retained context as controlled asset (memory ≈ live inputs in importance) — автор согласился.
- QuantumEdgeX: risk follows the whole workflow, every handoff = control point — автор согласился. **Это seam-язык.**

## Why it matters for us

1. **Memory layer = наш warm-vs-cold кейс.** Agentiqa project memory ускоряет повторы (136→70s) — т.е. retained context меняет вердикты. По Гупте это не баг скорости, а неуправляемый guardrail: нет session isolation между оценочными прогонами, нет TTL. Наш cold-M3 — это буквально тест memory guardrail.
2. **Tool layer = vendor gates (25).** Approval gates + allowlists — та же механика, что требуем от AI-QA вендоров.
3. **Handoff language = seams (22).** «Every handoff creates another point worth controlling» — переформулировка seam ownership для AI-рантайма. Кандидат в кросс-ссылку при ревизии 22/23.
4. **Output layer (unsupported claims)** = silent-green детектор в терминах безопасности: unsupported claim, прошедший outward, — это наш false negative под другим именем.

## Cross-links

- Agentiqa pilot (warm-vs-cold, M3/M6 learning) — живой кейс отсутствующего memory guardrail.
- Article 22 (seams) / 25 (vendor gates) — та же структура, другой слой стека.
- Article 26 red flags: «confidence without methodology» ↔ output guardrail gap.
