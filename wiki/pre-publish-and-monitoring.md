# Публикация и мониторинг LinkedIn-контента

Чек-листы, ограничения платформы и мониторинг после публикации. Ядро процесса - в скилле `tech-writer` (`~/.config/opencode/skills/tech-writer/SKILL.md`), здесь - развёрнутые правила.

**Связанные страницы:** [Правила написания статьи](./article-writing-rules.md) · [Стратегия пост+карусель](./Стратегия%20пост+карусель%20в%20LinkedIn.md) · [LinkedIn форматы и стратегии](./LinkedIn%20форматы%20и%20стратегии%20использования.md)

---

## 1. Pre-publish Audit (любой пост)

- [ ] Cross-links к статьям серии (и в Pulse Article, и в фид-посте, где уместно)
- [ ] Все числа source-backed
- [ ] Нет неподтверждённых утверждений
- [ ] Нет повторов из прошлых постов (допустимо в рамках серии)
- [ ] CTA присутствует
- [ ] ≤1200 chars
- [ ] Авторская строка внизу: `Name · Title · OpenCode Go`. **Без `$0 budget`** (рекрутеры = 12% зрителей профиля; «$0 budget» усиливает R&D/песочничное восприятие и подрывает enterprise-позиционирование). Цифры бюджета остаются в КОНТЕНТЕ статьи, где они и есть история ($3.62 Autonoma, $0.19 KISS); хэштег #ZeroBudgetQA остаётся (аудитория практиков)
- [ ] 3-5 хэштегов
- [ ] Нет клише («In today's world...», «As we all know...»)
- [ ] Эмодзи ≤9, data-heavy ≤4
- [ ] Таблицы → скриншоты (LinkedIn не поддерживает таблицы)
- [ ] Numbered lists проверены (LinkedIn их ломает)
- [ ] **External references all linked** — каждое упоминание человека/инструмента/статьи имеет кликабельный URL (credit авторам, источники, homepage проекта)
- [ ] **Нет внешних URL в теле фид-поста** — LinkedIn режет охват. Ссылки в первый комментарий или через кнопку Pulse Article. В теле: «link in comments 👇»
- [ ] **Изображение прикреплено к фид-посту** — посты с картинками получают 2-3x больше показов. Text-only = потерянный охват
- [ ] **Карусель/PDF упомянуты в фид-посте** — «👇 Check out the attached PDF slides» — явный указатель на визуальный актив увеличивает dwell time
- [ ] **Мобильная разметка** — без «стен текста»: абзац ≤2-3 строки, кейс выделен blockquote/📌/разделителем, списки с ↳/→ ритмом. Плотный блок между двумя списками — убийца читаемости
- [ ] **Кейс-стади как визуальный акцент** — сильнейший кейс (Block: +69% AI-код, 21x PRs, сломанный review pipeline) на отдельной строке (📌 или blockquote), не зарыт в середине списка

## 2. Article Review Checklist (рецензия перед публикацией)

**Narrative:**
- [ ] Hook — конкретный (числа, контраст)
- [ ] Money paragraph (2-й абзац) — сильнейшее утверждение в первых 150 chars
- [ ] CTA — вопрос аудитории (провокационный, приглашает к дискуссии)
- [ ] Первый комментарий спланирован — отдельно от CTA, сеет обсуждение
- [ ] «How to Replicate» секция есть (драйвит Saves) — практические шаги
- [ ] Авторская подпись

**Internal Consistency (MANDATORY — сканировать каждую статью):**
- [ ] **Нет дублирования результатов** — ключевое число появляется один раз, не в 3 секциях
- [ ] **Нет противоречий чисел** — одна метрика = одно значение во всех секциях (напр., количество [Authorize])
- [ ] **Суммы таблиц сходятся** — 5 строк в сумме = X, total row = X
- [ ] **Диаграммы соответствуют тексту** — ASCII/визуальные диаграммы отражают описанную архитектуру (включая циклы, ветвления)
- [ ] **Дисциплина эмодзи/символов** — не более 2-3 одинаковых символов подряд; data-heavy ≤4 эмодзи

**Format:**
- [ ] Длина ≤1200 chars (длиннее — карусель)
- [ ] Нет повторов из прошлых постов
- [ ] Нет generic filler

## 3. LinkedIn Platform Limitations

### 3.1 Таблицы — только скриншот

LinkedIn не поддерживает таблицы ни в постах, ни в Pulse Articles. Любая таблица = изображение.

**3 варианта генерации (предлагать все):**

1. **HTML→PNG (AI делает)** — HTML с таблицей → Playwright скриншот. Быстро, AI контролирует layout. (1200×644 для cover, 960×425 для inline)
2. **Image generation** — canvas или AI image model. Для визуально насыщенных картинок.
3. **NotebookLM / Gemini scenario** — AI пишет сценарий → пользователь генерирует HTML → скриншотит сам. Пользователь выбирает стиль.

**Формат:** 1920×1080 для article, 1200×900 для post. В `alt text` — ключевую метрику.

**Правило:** если в статье есть markdown-таблица → AI автоматически предупреждает («❌ LinkedIn не поддерживает таблицы»), предлагает 3 варианта, по выбору генерирует HTML или пишет сценарий.

### 3.2 Numbered Lists — ручная проверка

LinkedIn Pulse переформатирует нумерованные списки (сбрасывает номера 1,2,3 → 1,1,1, объединяет пункты, удаляет отступы).

**Правило:** предупредить перед публикацией: ⚠️ «LinkedIn ломает numbered lists — проверь вручную после вставки»

### 3.3 Pre-Publication Manual Checklist (в LinkedIn UI)

- [ ] **Numbered lists** — все номера корректны
- [ ] **Tables** — заменены скриншотом (PNG/PDF)
- [ ] **No Cyrillic** — пост только на английском
- [ ] **Encoding** — нет битых символов, кавычки «» → "", тире — → -
- [ ] **Emojis present** — ≥1 (визуальное разнообразие), но ≤9
- [ ] **Visual element** — есть хотя бы одно изображение (скриншот, схема, карусель)
- [ ] **Links** — URL не обрезан
- [ ] **Author line** — отдельная строка внизу
- [ ] **Hashtags** — отдельная строка, CamelCase (#TestAutomation)
- [ ] **Preview ~150 chars** — ключевое число в видимой зоне (скопировать первые 150 символов, убедиться что цифра там)
- [ ] **Mobile view** — нет нечитаемых переносов
- [ ] **Article cover image** — 1200×644 px

## 4. Post-Publication Monitoring

### 4.1 Performance Log

Вести `linkedin-posts/performance-log.csv`.

**Колонки:** `date,topic,format,impressions,likes,comments,saves,shares,yes_no_edit,notes`

**Однострочник (10 сек/неделю):**
```bash
echo "2026-06-04,Phase 2 OrangeHRM,post,1200,24,3,8,2,n,\"notes\"" >> path/to/performance-log.csv
```

### 4.2 Weekly Report Template

Создавать `linkedin-posts/weekly/YYYY-W##.md` каждый понедельник.

```markdown
# LinkedIn Performance — Week W, YYYY
**Published:** N posts
**Total engagement:** X likes, Y comments, Z saves

## Top Performer
- **Post:** [title]
- **Format:** [post/carousel/thread]
- **Engagement:** X%
- **Why worked:** [hook type, format, timing]
- **Action:** Extract hook → hooks library

## Bottom Performer
- **Post:** [title]
- **Engagement:** < 2% after 7d
- **Action:** Rewrite headline + lead paragraph

## Audience Signals
| Type | Count | Notes |
|------|-------|-------|
| 🟢 CTO / Head of QA | N | |
| 🟡 Peers | N | |
| 🔴 Recruiters | N | |
| 🔵 New followers | N | |

## Actions
- [ ] Extract top hooks
- [ ] Rewrite low-performer
- [ ] Plan next week
```

### 4.3 Thresholds

| Metric | Action |
|--------|--------|
| Engagement < 2% after 7 days | Rewrite headline + lead paragraph |
| Saves > 10 | Extract hook to hooks library |
| Comment from CTO/Head of QA | Highlight in weekly report, save for audience analysis |
| New followers > 2% of impressions | Note which post drove the growth |

### 4.4 Saves as Primary Metric

Лайки пассивны. Saves = «я вернусь к этому» — сильнее намерение.

При оценке: saves > likes. Приоритет контенту, который генерирует saves, а не likes.

## 5. Dual-Format Publishing Workflow

Когда публикуются и карусель, и Pulse Article:

### 5.1 Feed Post Differentiation — CRITICAL

Карусель-пост и артикл-пост ДОЛЖНЫ иметь **разные хуки и разный эмоциональный фокус.** Если оба поста видны в ленте одного читателя (День 1 карусель, День 2 статья), одинаковые хуки = читатель игнорирует второй.

| Parameter | Carousel Post | Article Post |
|-----------|---------------|--------------|
| **Emotion** | Provocation / Contrast | Analytics / Economics |
| **Key message** | «$X vs $Y — the cheaper won» | «How to build the stack for $Z» |
| **CTA** | «Swipe through» + battle question | «Read full article» + setup question |
| **Target action** | Shares (viral reach) | Saves (bookmark for later) |

**Анти-паттерн:** оба поста начинаются с «The $500 agent failed. The $0 agent passed.»
**Паттерн:** Карусель = «The $500 agent dropped unverified code and left.» / Статья = «Can you replace QA automation for $15/month?»

### 5.2 Publishing Sequence

1. **Подготовить оба ассета** — PDF карусель (≤7 слайдов) + текст статьи с cover
2. **Сначала карусель** в ленте (как document post)
3. **Первый комментарий карусели** — «Full deep-dive with all 7 agent results + screenshots → link here» (добавить ссылку после публикации статьи)
4. **Через 2 часа — Pulse Article**
5. **Первый комментарий статьи** — вовлекающий вопрос (отличается от комментария карусели)

**Carousel format:** PDF, 1080×1350 (4:5 портрет), тёмная тема, без эмодзи на слайдах, крупный шрифт для мобильных. Big numbers акцентным цветом (#58a6ff/#3fb950), отделены через flex column. `page-break-after: always` — один слайд на страницу. Кейсы: Before/After контрастные строки, не длинные списки.

**Копирайт на последней странице (обязательно):** LinkedIn позволяет скачивать PDF карусели («For accessibility purposes... download your document as a PDF»). Последняя страница = подпись: `© Victor Ematin · AI Quality Engineering Lead · OpenCode Go`. Не подпись-афоризм, не ссылку на следующую статью - именно копирайт с именем и ролью.

**Gotcha: LinkedIn отклоняет PDF, собранный через PIL/скрипт** («We encountered a problem sharing your post. Return to draft.»). Причина - структура/метаданные файла, НЕ пропорции (портрет 4:5 и квадрат 1:1 одинаково отвергались). **Фикс: пересохранить PDF через печать браузера** (Chrome/Edge: открыть HTML → Print → Save as PDF) - LinkedIn принимает такой файл без проблем. Опубликованная карусель 16 - квадрат 1080×1080, пересохранённый через печать.
**Article cover:** 1200×644, тёмный для статьи / светлый для фид-поста контраста.

### 5.3 Фид-пост для карусели (3 задачи)

1. **Цепляет хуком** в первых 2-3 строках (до «...see more») — парадокс/контраст
2. **Продаёт просмотр карусели** — анонс слайдов через `↳` («In the attached 7-slide breakdown (PDF) 📑: ↳ The Middle Loop... ↳ What broke at Block...») — байт на пролистывание, dwell time + просмотры PDF для алгоритмов. НЕ вываливать детали текстом
3. **Переправляет на статью** — «Full long-read article link is in the comments» (URL в теле режет охват)

**Структура (проверено на Article 16):**
```
Хук (2 строки, контраст + вопрос)
→ Позиционирование (сдвиг узкого места = QA leadership проблема)
→ Ставка/предупреждение (review pipeline ломается первым)
→ 📑 PDF-тизер: 3-5 пунктов с ↳ (анонс слайдов)
→ Ценностное утверждение («The value isn't in writing anymore — it's in verifying.»)
→ 👉 Swipe through the slides for the full framework.
→ 💬 Full long-read article link is in the comments.
→ ❓ CTA-вопрос (0-5 шкала)
→ Авторская строка + хэштеги
```

**Публикация:** PDF через иконку «Add a document» (LinkedIn оформляет как интерактивную карусель). Ссылку на статью — в ПЕРВОМ комментарии сразу после публикации + закрепить (pin).

## 6. Saves Strategy

Алгоритм LinkedIn весит Saves > Likes. Для драйва Saves:
- Добавить секцию **«How to Replicate»** или **«Quick Setup»** ближе к концу
- Сделать actionable: пронумерованные шаги, которые читатель может выполнить
- Практические гайды сохраняют; мнения пролистывают

*Обновлено: 2026-08-20*