---
type: linkedin-post
title: "0-phase0-review"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# Phase 0 Review — Propositions

## From: Big Pickle + DeepSeek (OpenCode)
## Date: 2026-05-31

Сводка ревью Phase 0 документации. Источники: Big Pickle (анализ файлов проекта) + DeepSeek (технический аудит кода).

### Unified Propositions

| # | Предложение | Файл | Автор | Приоритет |
|---|-------------|------|-------|-----------|
| 1 | AUTH-007/008 помечены `Type: API`, но OrangeHRM demo не имеет публичного REST API — убрать кейсы или пометить N/A | TEST_CASES.md | BP | 🔴 High |
| 2 | `page: any` во всех POM — заменить на `Page` из `@playwright/test` | pom/*.ts | DS | 🔴 High |
| 3 | Нет `@smoke` тэгов в тестах, но `npm run test:smoke` задокументирован в package.json — убрать скрипт или добавить тэги | package.json | DS | 🔴 High |
| 4 | Leave POM (LeavePage.ts) существует, но таблица Module Coverage ставит ❌ — исправить на ✅ | TEST_ARCHITECTURE.md | BP | 🔴 High |
| 5 | CI/CD YAML есть в TEST_ARCHITECTURE.md, но `.github/workflows/` не существует — убрать из документа или создать файл | TEST_ARCHITECTURE.md | DS | 🟡 Medium |
| 6 | Все URL hardcoded в POM, `baseURL` из `playwright.config.ts` не используется — вынести в конфиг | pom/*.ts | DS | 🟡 Medium |
| 7 | `auth.spec.ts` использует `dashboardPage` + `loggedInPage` fixtures, хотя loggedInPage уже на Dashboard — упростить (один fixture) | e2e/auth.spec.ts | DS | 🟡 Medium |
| 8 | MAINT-001 не учитывает access screen (требует ввод Admin password) — дополнить шаги | TEST_CASES.md | BP | 🟡 Medium |
| 9 | Data-Driven pattern в TEST_ARCHITECTURE.md вызывает `addUser()` — такого метода нет. Заменить на `fillUserForm()` | TEST_ARCHITECTURE.md | BP | 🟡 Medium |
| 10 | AUTH-006 (Session expires) нереализуем на demo-стенде — понизить приоритет или удалить | TEST_CASES.md | BP | 🟡 Medium |
| 11 | `pim.spec.ts` смешивает `page.goto()` и `pimPage` методы — унифицировать через POM | e2e/pim.spec.ts | DS | 🟢 Low |
| 12 | Карусель Slide 5: "8 modules planned" — не сходится с 13 секциями в TEST_CASES.md (там 13, не 12) | outputs/linkedin-carousel-orangehrm.md | DS | 🟢 Low |
| 13 | `waitForTimeout`: фактически 11 в коде, пост LinkedIn говорит "10", ранее BP сказал "~14" — уточнить цифру (14 с explore.js) | e2e/, pom/, explore.js | BP/DS | 🟢 Low |
| 14 | Нет negative-сценариев (SQL injection, XSS, спецсимволы) — добавить low-priority backlog | TEST_CASES.md | BP | 🟢 Low |
| 15 | README не описывает процесс добавления нового модуля (POM → fixture → spec → test case) | README.md | BP | 🟢 Low |

### Итого

| Приоритет | Всего | Big Pickle | DeepSeek |
|-----------|:-----:|:----------:|:--------:|
| 🔴 High | 4 | 2 | 2 |
| 🟡 Medium | 6 | 4 | 2 |
| 🟢 Low | 5 | 3 | 2 |
| **Total** | **15** | **9** | **6** |

### Что требует действий до Phase 1

1. **High:** AUTH-007/008 → N/A или удалить
2. **High:** `page: any` → `Page`
3. **High:** `@smoke` тэги — добавить или убрать скрипт
4. **High:** Leave POM в таблице → ✅
5. **Medium:** Hardcoded URLs → baseURL
6. **Medium:** Data-Driven example → `fillUserForm()`

---

## Conclusions

### Решения по каждому предложению

| # | Предложение | Решение | Действие в Phase 1 |
|---|-------------|---------|---------------------|
| 1 | AUTH-007/008 — API тесты | **N/A** — demo не имеет REST API | Удалить из TEST_CASES.md или пометить `⚠️ N/A (no API)` |
| 2 | `page: any` → `Page` | **Принять** — TypeScript strictness | Заменить во всех POM файлах |
| 3 | `@smoke` тэги отсутствуют | **Добавить тэги** — npm run test:smoke полезен | Добавить `@smoke` в auth.spec.ts, dashboard.spec.ts; оставить скрипт |
| 4 | Leave POM таблица ≠ код | **Исправить** — LeavePage.ts существует | В TEST_ARCHITECTURE.md → ✅ |
| 5 | Hardcoded URLs | **Принять** — baseURL из playwright.config.ts | Все `page.goto('https://...')` → `page.goto('/')` |
| 6 | Data-Driven `addUser()` | **Исправить** — метода нет | Заменить на `fillUserForm()` в документации |
| 7 | auth.spec.ts fixtures | **Упростить** — один fixture | `loggedInPage` → `dashboardPage` (или наоборот) |
| 8 | MAINT-001 password step | **Дополнить** — access screen требует ввода | Добавить шаг в TEST_CASES.md |
| 9 | pim.spec.ts hybrid | **Унифицировать** — всё через POM | `page.goto()` → `pimPage.navigateTo()` |
| 10 | AUTH-006 Session expires | **Понизить** — нереализуемо на demo | P3 (backlog) |
| 11 | Carousel Slide 5 | **Исправить** — 13 секций ≠ 8 planned | "8 modules" → "13 test modules" |
| 12 | waitForTimeout count | **Уточнить** — 11 в коде, не 10 и не 14 | Исправить в посте и документации |
| 13 | Negative scenarios | **Backlog** — низкий приоритет | Добавить в TEST_CASES.md как P3 |
| 14 | README module process | **Backlog** — низкий приоритет | Добавить секцию "Adding a Module" |

### Phase 1 Refactor Plan

**Что делаем (High + Medium):**
1. `page: any` → `Page` во всех POM файлах (~5 файлов)
2. Hardcoded URLs → `page.goto('/')` (baseURL из config)
3. AUTH-007/008 → пометить N/A в TEST_CASES.md
4. Leave POM → ✅ в TEST_ARCHITECTURE.md
5. Data-Driven `addUser()` → `fillUserForm()`
6. `@smoke` тэги в auth + dashboard spec файлах
7. auth.spec.ts fixtures → упростить (один fixture)
8. MAINT-001 → дополнить шагами (password screen)

**Что откладываем (Low):**
- pim.spec.ts unified POM (после стабилизации основных)
- Carousel.slide 5 fix (документация, не код)
- Negative scenarios backlog (P3)
- README module process (P3)

**Оценка времени:** ~45 мин на High+Medium, ~20 мин на Low
