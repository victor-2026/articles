# NotebookLM / Gemini — Сценарии генерации картинок для статей 12 и 14

Загрузите эти два сценария в NotebookLM (или Gemini) как источник данных → попросите сгенерировать HTML → откройте в браузере → скриншот.

Сравните результат с PNG из Playwright (HTML→PNG) и выберите лучший.

---

## Сценарий 1: 12-prod-table.png — «What Actually Runs in Production Today»

### Цель
Тёмная таблица для Pulse Article «AI Testing Agents in 2026: A 3-Month Field Report». Показывает 6 инструментов, которые реально работают в production после 3 месяцев тестов.

### Формат
- Размер: 1200×700 px (inline в статье, после секции «What Actually Runs in Production Today»)
- Стиль: тёмная тема (фон #0d1117, как GitHub dark), моноширинный шрифт, аккуратная таблица
- Заголовок таблицы: «What Actually Runs in Production Today»

### Данные (строго из статьи — не выдумывать)

| Tool | What We Use It For | Production Since |
|------|-------------------|-----------------|
| Kiro | Nightly security audit | Day 1 |
| Playwright Planner | New module exploration | Day 1 |
| Playwright Generator | Test generation from plans | Week 2 |
| Playwright Healer | Stale snapshot auto-fix | Week 2 |
| Claude Code | CI/CD + MCP pipeline | Week 4 |
| MAS patterns | Reusable learned_patterns | Week 6 |

### Блок под таблицей (красная плашка)
**What we don't use:**
Autonoma (context overflow) · Devin (blind on selectors) · Sorcar (superseded — its auto-fix loop is now native in Playwright Healer and Aider's --test-cmd)

### Стилевые требования
- Названия инструментов — синим (#79c0ff)
- Колонка «Production Since» — зелёным (#3fb950)
- «Что не используем» — красная плашка (#f85149 на тёмно-красном фоне)
- Чисто, без лишних украшений. Это данные, не реклама

---

## Сценарий 2: 14-cover-maturity.png — обложка статьи «AI Engineering Maturity Model»

### Цель
Обложка (cover) для Pulse Article про модель зрелости AI-инженерии по 9 концепциям Alex Barády. Визуал должен передавать: лестница L1-L5 + слоган + авторство.

### Формат
- Размер: 1200×644 px (стандартный cover для LinkedIn Pulse)
- Стиль: тёмный градиент (#0f172a → #1e293b), светлый текст, современный tech-вид

### Композиция (сверху вниз)
1. **Заголовок:** «AI User or AI Builder?»
2. **Подзаголовок:** «The 9-Concept Maturity Test · no dedicated test budget · 4 real codebases»
3. **Лестница из 5 уровней** (горизонтальная шкала, каждый следующий чуть выше/ярче):

| Уровень | Название | Подпись | Цвет |
|---------|----------|---------|------|
| L1 | Prompting | Copy-paste results. No tools. | серый |
| L2 | Tool User | One agent + MCP + scripts | синий |
| L3 | Builder | Loops, subagents, CI/CD | зелёный |
| L4 | +Infra target | Gateway, rate limits, cost | жёлтый |
| L5 | Production target | Evals, guardrails, telemetry | красный |

4. **Подпись внизу:** «Based on Alex Barády (ENDGAME) — 9 concepts separating AI user from AI builder»

### Стилевые требования
- Лестница должна визуально «расти» (L5 выше/крупнее L1)
- Цвета уровней от холодного к горячему (серый → красный) — символизирует прогресс
- Минимум украшений — чистая типографика
- Шрифт: system sans-serif (Segoe UI / SF Pro)

---

## Как использовать в NotebookLM

1. Откройте NotebookLM → новый Notebook → загрузите этот файл как источник
2. В чате попросите: «Сгенерируй HTML-страницу для Сценария 1 (или 2). Воспроизведи все данные и стилевые требования точно.»
3. Откройте полученный HTML в браузере
4. Сделайте скриншот (Cmd+Shift+4, выделите область картинки)
5. Сохраните в `linkedin-posts/AI-Agents/` под нужным именем (12-prod-table.png / 14-cover-maturity.png)

## Сравнение с Playwright

| Критерий | Playwright HTML→PNG (готово) | NotebookLM/Gemini |
|----------|------------------------------|-------------------|
| Контроль layout | ✅ точный (я задаю HTML/CSS) | ⚠️ зависит от генерации |
| Шрифты | ⚠️ system fonts | ⚠️ зависит от среды |
| Скорость | ✅ 10 секунд | ~2-5 мин вручную |
| Эстетика | функциональная | может быть стильнее |
