# Your AI Testing Agent Is Flying Blind. A Free VLM Fixes That.

[COVER: vlm-comparison.png — таблица Aider vs Devin vs VLM]

Two coding agents vs. one free VLM on the same page. **110 elements, 0 errors, $0.** The agents broke on every DOM change — the VLM didn't.

Every AI test generation tool follows the same pipeline:

```
Spec (text) → LLM → Test code → Run → Error → Fix
```

The agent never sees the page. It guesses selectors from context, runs the test, reads the error, and tries again.

This isn't a bug. It's the standard architecture.

## What We Tested

I ran two coding agents — [Aider](https://aider.chat/) and [Devin](https://devin.ai/) — against the same [OrangeHRM](https://www.orangehrm.com/) page. Neither claims to "see" the UI. Both use the text-only pipeline.

The result? Fragile selectors that work until the DOM changes:

```
Aider guessed:    input[name="password"], input[type="password"]
Devin guessed:    input[type="password"]
What actually works: page.getByRole('textbox', { name: 'Password' })
```

Then I added one step: **a screenshot → Vision-Language Model**.

I captured the same page as a PNG and sent it to **[Nemotron 3 Nano Omni](https://openrouter.ai/nvidia/nemotron-3-nano-omni-30b-a3b-reasoning)** — a free, open-weight VLM on [OpenRouter](https://openrouter.ai/). No DOM, no HTML, no XPath. Just the image.

```
Spec → Screenshot → VLM → ARIA selectors → Test code
```

**Result: 4/4 correct [Playwright](https://playwright.dev/) ARIA locators.** The VLM described every element and wrote the exact locator:

| Element  | Aider                    | Devin                    | VLM (free)                                               |
| -------- | ------------------------ | ------------------------ | -------------------------------------------------------- |
| Heading  | `h6:has-text(...)`       | `h6` (strict mode)       | `getByRole('heading', { name: 'Administrator Access' })` |
| Password | `input[name="password"]` | `input[type="password"]` | `getByRole('textbox', { name: 'Password' })`             |
| Confirm  | `button:has-text(...)`   | `button[type="submit"]`  | `getByRole('button', { name: 'Confirm' })`               |
| Cancel   | Not generated            | Not generated            | `getByRole('button', { name: 'Cancel' })`                |

## 110 Elements, 0 Errors

I scaled the test to 6 pages across OrangeHRM:

- Login form → 7 elements 
- Maintenance screen → 8 elements 
- Admin users table → 10+ elements 
- Dashboard (nav, cards, charts, Buzz posts) → 35+ elements 
- Claim assign form (tabs, filters, table) → 40+ elements 
- Buzz feed (dynamic timestamps, post IDs) → 10 elements 

**~110 UI elements across 6 pages. 0 missed. 0 hallucinated. $0 spent.**✅

The VLM even read dynamic content verbatim — timestamps like `"24-06-2026 03:08 AM"` and post IDs like `"Load test post 1782259683587"` — straight from the screenshot.

## Why This Matters

The locator problem isn't a model quality issue. **It's a modality issue.**

Aider and Devin work exactly as designed: text in, code out, iterate on errors. They're not bad at selectors — they simply never see what the page looks like.

The AI test generation pipeline has a blind spot: visual context. A free VLM fills it in one API call.

## The Fix

Add this step before test generation:

```
1. Playwright opens page
2. Take screenshot (page.screenshot())
3. Send to free VLM (Nemotron Nano Omni)
4. Use returned ARIA selectors
```

You get `getByRole('button', { name: 'Confirm' })` without parsing the DOM — more resilient than any CSS selector an agent can guess.

## Caveats

- Tested on OrangeHRM (PHP + custom CSS). Other frameworks may behave differently.
- The VLM identifies elements accurately, but branching logic and assertions still require a human.
- Dynamic content (toasts, live updates) needs a fresh screenshot each time.

## The Bottom Line

> The standard AI test generation pipeline is blind. A free VLM step fixes the single biggest source of flaky selectors — at zero cost.

If you're evaluating an AI testing tool, don't just ask "can it write tests?" Ask: **does it see the page, or guess it?**

---
**Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go**

#AITesting #Playwright #VLM #TestAutomation #QualityEngineering

---
===== конец статьи
**Key edits made by Qwen 3.7 Max:**
- Tightened opening sentences for rhythm
- Replaced "Practical Takeaway" → "The Fix" (shorter, more direct)
- Removed redundant phrasing ("the cheapest fix in your stack" — the $0 angle is already established)
- Cleaned up "Caveats" wording for consistency
- Sharpened the bottom line closing line
- Preserved all technical accuracy and data tables verbatim

 ====  =====
- **Статья + Feed Post** (без карусели).

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
