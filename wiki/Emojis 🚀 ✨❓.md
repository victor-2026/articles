# Emoji System for LinkedIn Posts

**Связанные страницы:** [LinkedIn форматы и стратегии](./LinkedIn%20форматы%20и%20стратегии%20использования.md) (overview) · [Стратегия пост+карусель](./Стратегия%20пост+карусель%20в%20LinkedIn.md) (шаблоны A/B/C)

---

## Категории

| Категория | Эмодзи | Назначение |
|-----------|--------|------------|
| **Visual anchors** | 🟢🔴🟣🟡🟠🟤 | Структурные разделители — визуально лёгкие |
| **Achievement** | 🚀🎯📈🏆🧠 | Результат, прорыв, инсайт |
| **Process** | ⚙️🔧🔑✨🗑️🐛 | Действие, фикс, проблема |
| **Engagement** | ❓💬👀🔥📄 | Вовлечение, CTA |
| **Structure** | 📊📄🔄▶️🌐 | Метрики, контекст, прогресс |
| **Warning** | ⚠️📍 | Сигнал внимания |

---

## Emoji Density Rules

- **≤1 эмодзи на 5 строк текста** — baseline
- **≤9 эмодзи на пост** — никогда не превышать
- **0 эмодзи в карусели** — карусель только визуал
- **Pattern A (data-heavy):** эмодзи только для hook/signal/bridge/CTA = ≤4
- **Pattern B (story-heavy):** эмодзи на ключевые моменты — ≤9, только achievement/result/engagement

---

## Цветные квадраты vs эмодзи

| | 🟢🔴🟣 Квадраты | 🚀🐛🔑 Эмодзи |
|---|---|---|
| **Вес** | Лёгкий, структурный | Тяжёлый, эмоциональный |
| **Когда** | Редкие якоря, контраст | Story-driven, achievements |
| **Пример** | `🟢 54.5%` vs `🔴 44.1%` (контраст) | "🐛 Race found, 🔑 1 line fix" |
| **Риск** | Одинаковые ×8 = шум | >9 = перегруз |

**Правило:** квадраты только для контраста (разные цвета). Повтор одного квадрата ×8 = визуальный шум. Для списков → **bold topic** вместо квадрата.

### Альтернативы для списков (без квадратов)

| Вариант | Формат | Когда |
|---------|--------|-------|
| **Bold topic** | `**Title.** Data.` | Data-heavy, проф аудитория |
| **→** | `→ Title. Data.` | Лёгкий ритм, general |
| **Воздух** | Просто абзацы с пустыми строками | Макс readability |

---

## Выравнивание в LinkedIn Editor

Эмодзи разной ширины не выровнять в столбец:
```
🚀 Hook — text starts here
🐛 Bug — text starts HERE (правее)
```

### Решения

**A — → для списка** (рекомендовано для data-heavy)
```
→ 2 monoliths → 23 modules
→ 1,108 runs across 4 browsers
→ 1 race found, 1 line fix 🎯
```

**B — Bold + эмодзи сверху**
```
🚀 Results
**Coverage.** 94% API, 100% PBT
**Speed.** CI in 3 minutes
```

**C — Эмодзи в конец строки**
```
2 monoliths → 23 modules 🗑️
1,108 runs across 4 browsers 📊
1 race found, 1 line fix 🎯
```

---

## Number Grid Format

Что the numbers say:
→ 2 monoliths → 23 modules, ~4,000 lines deleted
→ 1,108 runs across 4 browsers (277 unique)
→ 2 environments: Docker (local) + Render (cloud)
→ 1 race found, 1 line fix 🎯
→ 15 AI models cycled — 6 already gone

**Правила:**
- `→` в начале строки (без пробелов перед)
- Эмодзи только в конце последней/ключевой строки 🎯
- Однотипные строки без эмодзи — не шумят

---

## Case study: Phase 2 Refactoring

**Было** (агент написал): 16 эмодзи, 5 в grid, process-эмодзи.

**Стало** (после ревью для lead/manager аудитории): 6 эмодзи, grid clean →, process-эмодзи убраны.

**Вывод:** аудитория лидов/менеджеров ≠ process-эмодзи (🔧⚙️🗑️). Оставлять только achievement 🚀🎯 + story 🐛🔑 + engagement ❓.
