# NotebookLM — Visuals for Article 9

**Тема:** AI Test Tools Comparison — Playwright Agents vs KISS vs Autonoma
**Аудитория:** QA engineers, engineering managers
**Стиль:** Clean, modern, tech — no clipart, no gradients, dark mode optional
**Формат:** 1920×1080 PDF/PNG

---

## 1. COVER — Comparison Table (1200×644, LinkedIn card)

Заголовок: **3 AI Test Tools on OrangeHRM 5.9**

Таблица 3×8 столбцов:

| Metric | Playwright Agents | KISS/Sorcar | Autonoma |
|--------|:-:|:-:|:-:|
| Tests generated | 8 | 8 | 95 |
| Coverage | 1 page | 1 page | 14 modules |
| Format | `.spec.ts` | `.spec.ts` + POM | `.md` specs |
| Execution | Standard runner | Standard runner | AI agent + vision runtime |
| Auto-fixes | 2 | 0 | 28 → re-gen |
| POM created | No | Yes (187 lines) | No |
| Setup time | 10 min | 15 min | 3+ hours |

Цвета строк: PW = зелёный `#45ba4b`, KISS = синий `#2d7ff9`, Autonoma = оранжевый `#f97316`
Без emoji, без подвала, текст строго английский

---

## 2. LOGO BANNER — три иконки side by side

- **Слева:** Playwright маска (зелёная #45ba4b) + подпись "10 min • 8 tests"
- **Центр:** "KISS" текст (синий #2d7ff9, bold sans-serif) + подпись "15 min • 8 tests + POM"
- **Справа:** Autonoma буква "A" (фиолетовый #8b5cf6) + подпись "3+ hrs • 95 specs"

Фон тёмный #1a1a2e или белый #ffffff (выбрать что лучше смотрится)

---

## 3. COMPARISON — архитектурная схема

Три колонки, сверху вниз:

**Playwright Agents:**
Planner (explore page → 22 scenarios in .md)
  → Generator (write 8 Playwright tests)
  → Healer (detect + fix 2 failures)
  → **Output: 8 `.spec.ts` files**

**KISS/Sorcar:**
Prompt 1: "Create POM + 4 tests"
  → 187-line POM + 4 tests
  → Prompt 2: "3 advanced tests"
  → Manual fix (waitForResponse filter)
  → **Output: 8 `.spec.ts` + POM**

**Autonoma:**
Explore pages → KB → Entity audit (32 models)
  → Scenarios (68 records) → Factory setup (18)
  → Test generation → Review (28/43 fail → re-gen)
  → **Output: 95 `.md` specs**

**Нижняя строка (вывод):**
- PW / KISS: "Test code — runs anywhere (playwright test)"
- Autonoma: "Test intent — needs AI agent runtime"

---

## 4. FEED IMAGE — mock терминала (1080×1080, квадрат)

Чёрный фон (`#0d1117`), моноширинный шрифт (SF Mono / JetBrains Mono), зелёный `#00ff41`

```
$ autonoma run

◐ Exploring pages... done (32 pages)
◐ Building knowledge base... done
◐ Auditing entities... 32 models found
◐ Designing scenarios... 68 records written
◐ Wiring factories... 18/18 verified
◐ Generating tests... 95 specs written
◐ Reviewing specs... 43/43 checked
  ✓ 15 passed
  ✗ 28 failed → sending back to generator

▸ 25 nodes tested, 95 tests written, 0 in queue
▸ Pipeline: 3h 12m elapsed, still running
```

Пульсирующий курсор `▸` в последней строке для динамики

---

## Output

Save to: `/Users/victor/Projects/Articles/linkedin-posts/AI-Agents/`
Naming: `9-cover.png`, `9-logo-banner.png`, `9-architecture.png`, `9-terminal-feed.png`
