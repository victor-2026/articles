---
type: linkedin-post
title: "webwright-strategy-slides-rus"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# Webwright Strategy — Carousel Text

## Slide 1 — Title
**Как мы оцениваем AI-инструменты для тестирования**

30 сессий × 5 моделей × 600+ вызовов = 1 стратегия

## Slide 2 — The Framework
**5 измерений оценки AI-агента для QA**

1. **Поколение кода** — Playwright или Selenium?
2. **Потребление токенов** — сколько стоит шаг?
3. **Стабильность** — падает? Теряет контекст?
4. **Model-agnostic** — работает с разными LLM?
5. **Real project fit** — POM? Selectors? Timeouts?

Webwright проверен по всем пяти.

## Slide 3 — Architecture Win
**Workspace mode — меньше, но лучше**

Browser mode: screenshot + DOM = ~2500 tok/step
Workspace mode: read files + write code = ~300 tok/step

→ **8x дешевле**
→ Нет race condition с DOM
→ Агент работает как junior dev, не как пользователь

Это правильная архитектура для генерации тестов.

## Slide 4 — Model Zoo
**5 моделей — 5 результатов**

| Модель | Format err | Playwright? | Rate limit |
|--------|:----------:|:-----------:|:----------:|
| deepseek-coder-v2 | 1% | ❌ (Selenium) | Нет |
| qwen2.5 (temp=0.7) | 33% | ✅ | Нет |
| qwen2.5 (temp=0.1) | 10% | ✅ | Нет |
| Groq llama-3.3-70b | 0% | ✅ | 12K TPM |
| qwen2.5-coder:14b | 10% | ✅ | 5 tok/s |

Вывод: качество модели → качество результата. Webwright — прослойка.

## Slide 5 — Bugs Found
**2 core patches за 30 сессий**

**Bug 1:** `_compact_history()` → `'list' object has no attribute 'strip'`
Multimodal ответы = список, код ждёт строку.
Фикс: одна проверка типа.

**Bug 2:** `_prune_old_observation_aria_snapshots` → не чистит command_output
Workspace mode → context растёт бесконечно.
Фикс: расширенная обрезка + `keep_last_n_observations: 3`

## Slide 6 — Strategic Takeaway
**Research prototype ≠ production tool**

Webwright на WebArena: **86.67% success rate**
Webwright на OrangeHRM (POM, TypeScript, 12 модулей): **1 тест за 30 сессий**

Разрыв между бенчмарком и реальным проектом — порядок величины.

**Стратегия:**
- Следить за развитием
- Не внедрять в CI сегодня
- Использовать уроки: workspace mode, custom Modelfile, явные промпты

## Slide 7 — What's Next
**От evaluation к внедрению — план**

**Краткосрочно:** докинуть contract testing + chaos в Buzzhive, чтобы зафиксировать real work

**Среднесрочно:** переоценить Webwright через 6 месяцев (версия 0.2+, фиксы core bug)

**Долгосрочно:** строить internal agent поверх стабильной LLM, заимствуя Webwright architecture patterns

## Slide 8 — Resources
**Assets**

Chart 1: `/tmp/webwright_model_comparison.png`
Chart 2: `/tmp/webwright_token_cost.png`
Chart 3: `/tmp/webwright_bugs.png`

**Full report:** `OrangeHRM/outputs/session24-webwright-report.md`
**Carousel spec:** `OrangeHRM/outputs/webwright-carousel-spec.md`
