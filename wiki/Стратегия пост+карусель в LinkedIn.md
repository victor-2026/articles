# Стратегия: Пост + Карусель = две разные функции

**Связанные страницы:** [LinkedIn форматы и стратегии](./LinkedIn%20форматы%20и%20стратегии%20использования.md) (overview) · [Emojis 🚀 ✨❓](./Emojis%20🚀%20✨❓.md) (система эмодзи)

---

## 1. Почему Post ≠ Carousel

Пост и карусель — не дубли, а **два слоя одной истории**:

| | Post | Carousel |
|---|---|---|
| **Цель** | Hook + data + engagement trigger | Deep dive + visual proof |
| **Время чтения** | 3 секунды | 15-30 секунд |
| **Формат** | Plain text + emoji | PDF (LinkedIn конвертирует) |
| **Текст** | Плотный, короткие блоки | Минимум текста, макс визуала |
| **Эмодзи** | Да — визуальные якоря | Нет — чистый визуал |

**Золотое правило:** пост работает без карусели. Карусель без поста — нет.

Связь: **post = first layer, carousel = second layer**. Пост даёт все факты сжато, карусель раскрывает каждый факт визуально.

---

## 2. Format Templates

### Pattern A: Data Hook → List → Bridge → CTA
*Использовано в: Webwright, Future of QA Engineer*

```
🧠 Hook with key number
⚠️ Signal / context sentence

**Point 1 with data.** Number + context.
**Point 2 with data.** Number + context.
... (6-8 points)

📄 Bridge to carousel 👇

❓ CTA question

Author · Role · OpenCode Go
```

### Pattern B: Story → Problem → Fix → Grid → CTA
*Использовано в: Phase 2 Refactoring*

```
🚀 Hook with achievement + number

Result data (coverage, stack)
Context (CI/CD, backend)
Problem (4,000 lines spaghetti)
Fix (23 modules, 1 line)
Key insight

What the numbers say:
→ 2 monoliths → 23 modules, ~4,000 lines deleted
→ 1,108 runs across 4 browsers (277 unique)
→ 2 environments: Docker (local) + Render (cloud)
→ 1 race found, 1 line fix 🎯
→ 15 AI models cycled — 6 already gone

🐛 Story moment (race, insight)
🔑 Key takeaway

❓ CTA question

Author · Role · OpenCode Go
```

### Pattern C: Question → Evidence → Carousel → CTA
*Резерв — ещё не использован*

```
❓ Provocative question

Data point 1
Data point 2
...

So what? (conclusion + carousel bridge)

❓ CTA
```

---

## 3. Emoji System —→ [Emojis 🚀 ✨❓.md](./Emojis%20🚀%20✨❓.md)

Категории эмодзи, density rules, bold vs квадраты, visual anchors — вынесено в отдельную страницу.

---

## 4. Post Structure Patterns

### Hook типы

| Тип | Формула | Пример |
|-----|---------|--------|
| **Data hook** | 🧠/📊 + число + statement | "86.67% SOTA with ~1K lines of code." |
| **Achievement hook** | 🚀 + что сделал + результат | "How Removing 4,000 Lines Boosted My QA" |
| **Question hook** | ❓ + provocative question | "Which limitation hits your stack hardest?" |
| **Controversy hook** | Common belief vs reality | "AI isn't replacing QA engineers" |

### Data formatting

- **Большие числа** первыми — hook
- **Проценты** с визуальным контрастом (54.5% vs 44.1%)
- **Дробные** → округлять до 1 знака ($2.37, 60.1%)
- **Сравнения** — всегда с базой (+35% over previous, $2.37 vs $6.09)
- **Длинные списки** → **bold topic** + `.` + data (не квадраты, не цифры 1-8)

### Bridge к карусели

Всегда последняя строка перед CTA:
```
📄 Each [concept] visualized in the carousel below 👇
```

Или для конкретного формата:
```
📄 Full analysis in the carousel →
```

---

## 5. Carousel Structure

### 10 slides (оптимально)

| Slide | Content |
|-------|---------|
| 1 | **Title** — hook + author (same as post) |
| 2 | **Context** — проблема/прорыв |
| 3-9 | **One concept per slide** — title + 1 data point + visual |
| 10 | **CTA** — question + link/next steps |

### Carousel правила

- **Текст на слайде:** ≤1 предложение + 1-2 числа
- **Визуал:** CSS-only bars, grids, boxes, arrows. Никаких внешних картинок.
- **Тема:** тёмная (как Phase 2 template)
- **Шрифт:** крупный — читаем с мобильного
- **Логотип/автор:** на каждом слайде (bottom-right)
- **Никаких эмодзи** на слайдах — только в посте

### LinkedIn PDF → Carousel

LinkedIn автоматически конвертирует PDF в карусель при загрузке через Document upload. 

**Требования к PDF:**
- 1 слайд = 1 страница PDF
- Формат: 1920×1080 px (16:9)
- Шрифты: embedded (Noto Sans или system)
- Размер: ≤ 10 MB, ≤ 100 страниц
- Не использовать GIF/видео

---

## 6. Engagement Mechanics

- **❓ Всегда вопрос в конце** — самый важный элемент
- **Авторская строка:** "Имя · Role · OpenCode Go" — личный бренд
- **Хэштеги:** 5-6, только релевантные, в конце
- **Время публикации:** Вт/Ср/Чт 10:00-12:00 CET
- **Ссылки:** одна на предыдущий пост, одна на статью (в карусели)

---

## 7. Proven Patterns (Case Studies)

### 🟢 Future of QA Engineer — самый просматриваемый
- **Hook:** "AI isn't replacing you — it's leveling you up."
- **Формат:** Pattern A (Data Hook → List → CTA)
- **Визуал:** 🟢🔴🟪 colored squares
- **Структура:** короткие блоки, много воздуха
- **Итог:** 1,060 followers, 116 posts

### 🚀 Phase 2 Refactoring — визуальная эволюция
- **Hook:** "How Removing 4,000 Lines of AI Tests Boosted My QA"
- **Формат:** Pattern B (Story → Grid → CTA)
- **Аудитория:** leads, managers — эмодзи процессов ❌ шумят
- **Фишка:** number grid без эмодзи (→), эмодзи только hook 🚀 + story 🐛🔑 + CTA ❓
- **Пост БЫЛ** без эмодзи → переделан под визуал → ещё раз переделан (16→6 эмодзи)

### 🧠 Webwright — data-heavy, 8 limitations
- **Hook:** "86.67% SOTA with ~1K lines of code"
- **Формат:** Pattern A c **bold topic** (🟢 squares rejected — 8×🟢 = noise)
- **Визуал:** bold anchor + 4 emoji (🧠⚠️📄❓)
- **Фишка:** 8 points, каждая с числом, минимум шума

---

## 8. Checklist перед публикацией

- [ ] Hook с числом/эмодзи
- [ ] Signal (⚠️/📍/💡) если список
- [ ] Visual anchor: **bold topic** для списков / 🟢🔴 для контраста / → для ритма
- [ ] Каждый пункт с числом
- [ ] Bridge к карусели 📄 👇
- [ ] ❓ CTA вопрос
- [ ] Author line
- [ ] ≤9 эмодзи (data-heavy ≤4)
- [ ] Нет повторяющихся эмодзи в списке (8×🟢 = шум)
- [ ] ≤6 хэштегов
- [ ] PDF готов (10 стр, 16:9, тёмная тема)
