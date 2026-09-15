🔍 I tested the same OrangeHRM page with three AI tools.

Two coding agents (Aider + Devin) → fragile CSS selectors that break on DOM changes.
One free VLM (Nemotron Nano Omni) → 4/4 correct Playwright ARIA locators on the first try.

The difference? The VLM actually saw the page.

Every AI test generation pipeline works blind:

```
Spec (text) → LLM → Code → Run → Error → Fix
```

The agent never sees your UI. It guesses selectors from context, runs the test, reads the error, tries again.

I added one step — a screenshot → free VLM — and scaled it to 6 pages:

Login form → 7 elements
Maintenance screen → 8 elements
Admin users table → 10+ elements
Dashboard → 35+ elements
Claim assign form → 40+ elements
Buzz feed → 10 elements

**110 UI elements. Zero missed. Zero hallucinated. $0 spent.**🎯"

The locator problem isn't a model quality issue. It's a modality issue.

If you're evaluating AI testing tools, ask: **does it see your page, or guess it?**

Full breakdown with comparison table and caveats ↓

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

#AITesting #Playwright #VLM #TestAutomation #QualityEngineering

=====
**Статья + Feed Post** (без карусели).

Почему:
- **Статья** — глубина есть (сравнительная таблица, 6 страниц, caveats, 4-step fix). SEO работает, ссылка живёт долго.
- **Feed Post** — сильный hook: *"I tested the same page with two AI agents and a free VLM. The VLM got 4/4 correct — and it costs $0."* + скриншот таблицы сравнения (PNG) + ссылка на статью.
- **Карусель не нужна** — твой опыт показывает: Article 9 carousel = 49 imp vs feed 733 imp. Разрыв 15x. Эта тема тоже technical — карусель проиграет.

Формат feed поста — Pattern B (Story → Problem → Fix → Number Grid → CTA):
1. Hook: личный эксперимент
2. Problem: AI agents are blind
3. Fix: добавить VLM step
4. Number Grid: 110 elements, 0 errors, $0
5. CTA: "does it see the page or guess it?"

========

```

**Ключевые изменения:**
- Hook: личный эксперимент вместо описания
- Number Grid: 6 страниц как сканируемый список
- CTA: вопрос вместо стандартной ссылки
- +2 хештега
- Visual breaks для ритма

Теперь можно публиковать — статья уже готова, feed post усилен.