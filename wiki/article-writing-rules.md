# Правила написания статьи (tech-writer)

Детальные правила написания LinkedIn-статей и постов. Ядро процесса - в скилле `tech-writer` (`~/.config/opencode/skills/tech-writer/SKILL.md`), здесь - развёрнутые правила с примерами.

**Связанные страницы:** [Стратегия пост+карусель](./Стратегия%20пост+карусель%20в%20LinkedIn.md) · [LinkedIn форматы и стратегии](./LinkedIn%20форматы%20и%20стратегии%20использования.md) · [Публикация и мониторинг](./pre-publish-and-monitoring.md)

---

## 1. Структура статьи: Problem → Solution → Implementation → Result

Логический поток каждой статьи. Без отклонений.

## 2. Data-First Writing

Каждое утверждение должно иметь число:
- ❌ «Tests got faster»
- ✅ «Execution time dropped 19% — from 2.6 min to 2.1 min»

## 3. Contrast-Driven Hook

Первые 2-3 строки (видимы в мобильной ленте) должны содержать **конфликт или контраст**.

Паттерн: «$X vs $Y — the cheaper/faster/smaller won.»
- ❌ «I tested 7 agents and here's what happened»
- ✅ «I spent $15 to test 7 agents against a $500/mo tool — the $0 tool won»

**~150 chars preview** — это всё, что увидит большинство читателей. Нет контраста в превью → пролистывают.

## 4. Запрет клише

Нет: «In today's world...», «As we all know...», «It goes without saying...»
Начинать с проблемы, не с погоды.

## 5. First-Person Voice

Для аудитории Senior+: «I built», не «the team implemented». Личный опыт = доверие. CTO читают между строк.

## 6. Oxford Comma

Да. Для технической аудитории сигнализирует внимание к деталям.

## 7. Paragraph Length

Один абзац = одна мысль. **2-4 предложения, 40-60 слов.**
LinkedIn Pulse читают в основном с мобильных. Абзац длиннее 5 строк на экране телефона — разделить.

## 8. The Money Paragraph

**Второй абзац — самый важный во всей статье.**

LinkedIn-лента показывает первые ~150 символов статьи в превью:
- Клише/пустота → пролистывают
- Смелое заявление или число → кликают

**CRITICAL: ключевое число ДОЛЖНО быть в первых ~150 символах.** Если лид-абзац длиннее ~140 символов — число не попадёт в превью. Реструктурировать так, чтобы сильнейшее число оказалось в видимой зоне.

Правило: лид = хук (эмоция/личное). Money paragraph = самое смелое число/утверждение. Лучшую метрику — туда.

Анти-паттерн: число за ~150 символами («I tested X with Y. One approach did Z. The other? **100 elements, 0 errors**» — число на ~170-м символе).
Паттерн: число первым («Two agents vs. one VLM. **110 elements, 0 errors, $0.** The agents broke — the VLM didn't.» — число на ~55-м символе).

## 9. Tables & Visuals

**Два правила для таблиц в статьях:**
1. **Таблицы = скриншоты** — LinkedIn не рендерит Markdown-таблицы. Маркер `[SCREENSHOT: description]`.
2. **Дублировать ключевые таблицы текстом** сразу после маркера скриншота — ловит читателей на медленном соединении/без картинок, полезно для копирования данных.

Инфографики: `[INFOGRAPHIC]`. Скриншоты: `[SCREENSHOT: description]`. Типы графиков: bar charts для before/after, line charts для трендов.

**3 варианта генерации изображений (предлагать все, пользователь выбирает):**
1. **HTML→PNG** — HTML с таблицей → скриншот через Playwright. Быстро, AI контролирует layout. (1200×644 cover, 960×425 inline)
2. **Image generation** — canvas/HTML2PNG/AI image model. Для кастомных визуалов.
3. **NotebookLM / Gemini scenario** — структурированный сценарий (source data + формат-спецификация) → пользователь генерирует HTML → скриншотит сам. Пользователь выбирает визуальный стиль.

**Carousel scenario format** (для NotebookLM):
- Количество слайдов и размеры (**1080×1350 px, 4:5 портрет — LinkedIn мобильный стандарт, +30-40% площади vs 16:9. Квадрат 1080×1080 допустим. 16:9 альбомный НЕ использовать — мелко на мобильных**)
- Точный текст каждого слайда (headline, body, footer)
- Формат-спек: цвета, шрифты, layout
- Source data структурировано для прямого использования

## 10. Hashtags

3-5 внизу. Примеры: `#TestAutomation #ZeroBudgetQA #GenAItesting #Playwright #QATips`

## 11. Call to Action (опционально)

Предложить один, решает пользователь: вопрос аудитории, приглашение комментировать, ссылка на GitHub, «Subscribe and follow».

## 12. Narrative Style

Живо, но профессионально. Лёгкий сторителлинг. Без кликбейта и корпоративного жаргона.

---

## 13. Headline Formulas (по одной на вариант)

| Formula | Pattern | Example |
|---------|---------|---------|
| **Curiosity Gap** | «I replaced [X] with [Y] — here's what happened» | *«I replaced 40 waitForTimeout with expect() — execution dropped 19%»* |
| **Direct Benefit** | «How to [achieve X] without [pain Y]» | *«How to scale 2,000+ tests without breaking your CI pipeline»* |
| **Contrarian** | «Why [common practice] is wrong for [context]» | *«Why monolithic test files are an anti-pattern (and how to escape)»* |

## 14. Article Depth Patterns

Паттерны, поднимающие статью от «хорошего поста» до «industry reference». Применять для технических статей (архитектура, сравнение инструментов, результаты экспериментов).

### 14.1 Severity Stratification

Не все находки равны. Разбить по серьёзности — честность и точность:

| Severity | Count | Examples |
|----------|-------|----------|
| 🔴 Real hole | N | Core feature, 0% coverage |
| 🟡 Important, not critical | N | Adjacent tests exist, no direct coverage |
| 🟢 Incremental | N | Low risk, shared logic |

**Правило:** всегда отделять критичные находки от шума. Читатели доверяют авторам, которые не бьют тревогу зря.

### 14.2 Cost/Time Stratification

Тяжёлые проверки (mutation testing, глубокий trace analysis) дорогие. Показать стратификацию:

| Check Type | When | Cost |
|------------|------|------|
| **Lightweight** | Every PR (< 2 min) | ~$0 |
| **Heavyweight** | Nightly / Staging (40+ min) | ~$5-20/run |

**Правило:** никогда не предлагать дорогие проверки на каждый коммит. Показать сдвиг.

### 14.3 Architecture Completeness — Feedback Loops

Описываешь пайплайн/архитектуру — **замкни цикл**:
- Компонент выдал FAIL → что дальше?
- Есть auto-fix цикл? Ручная эскалация?
- Есть guardrails (flakiness check, anti-gaming)?

**Анти-паттерн:** линейный пайплайн с тупиковыми компонентами.
**Паттерн:** замкнутые циклы обратной связи с явными guardrails.

### 14.4 Multi-Project Validation

Один проект = анекдот. Два+ проекта = паттерн.

По возможности валидировать находки на: разных архитектурах (POM vs API, PHP vs Node.js), размерах команд, стратегиях тестирования.

**Правило:** «I found X in project A» < «I found X in projects A and B — same pattern, different codebase.»

### 14.5 Depth Checklist (для технических статей)

- [ ] **Root cause explained** — почему проблема существует? (не просто «она есть»)
- [ ] **Alternative comparison** — какие ещё инструменты/подходы могли бы найти то же?
- [ ] **Efficiency metrics** — насколько быстро/дёшево vs альтернативы? (time, cost)
- [ ] **Business impact** — что будет, если НЕ починить? (SOC2, data breach, regression)
- [ ] **Terminology disambiguation** — похожие названия → одна строка разъяснения различия
- [ ] **No false dichotomies** — избегать «X useless», когда точнее «X without Y is insufficient»
- [ ] **Guardrails documented** — edge cases, flakiness, gaming prevention

## 15. Content Hooks Library

После каждой публикации извлекать 3-5 сильных хуков/фраз в `linkedin-posts/hooks-library.md`.

**Формат:**

| Hook | Source Post | Reuse For |
|------|-------------|-----------|
| «20% coverage with a traceability matrix beats 80% without one» | 0-orangehrm-phase0 | Coverage discussions |
| «taught me more than 1000 passing tests on a project I already know» | 1-orangehrm-phase1 | Learning/contrast |

*Обновлено: 2026-08-20*