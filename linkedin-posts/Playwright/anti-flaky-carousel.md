# NotebookLM Carousel Script: Anti-Flaky Patterns

## Slide 1 — Cover

**3 Anti-Flaky Patterns That Cut My Test Failures by 80%**

Zero waitForTimeout. Zero flaky. Zero excuses.

Victor Ematin · AI Quality Engineering Lead · $0 budget

---

## Slide 2 — The Problem

**Your test isn't flaky. Your timeout is.**

waitForTimeout(2000) works locally, breaks in CI. Sleeps are code smells.

My suite had 40+ waitForTimeout calls. Every CI run needed manual re-runs. Pass rate hovered around 78%.

The fix wasn't a better framework. It was removing the sleeps.

---

## Slide 3 — Pattern 1: Auto-waiting Assertions

**Playwright already waits. Let it.**

Playwright auto-waits on assertions: `expect(locator).toHaveText()`, `toBeVisible()`, `toBeEnabled()`.

BEFORE:
```
await page.waitForSelector('.toast');
expect(page.locator('.toast')).toBeVisible();
```

AFTER:
```
await expect(page.locator('.toast')).toBeVisible();
```

Don't wait THEN assert. Assert directly.

---

## Slide 4 — Pattern 2: API Mocking over UI Setup

**Why click 5 times when you can fake one API call?**

BEFORE: Log in, navigate 3 menus, fill 2 forms, submit, wait for redirect.

AFTER:
```
await page.route('**/api/posts',
  route => route.fulfill({ json: mockData })
);
```

Three levels of mocking:
- API: `page.route()` for network
- Clock: `page.clock.fastForward()` for time
- Component: mock child components

Deterministic data. 10x faster. Zero server timing flake.

---

## Slide 5 — Pattern 3: expect.poll()

**For state that lives outside the DOM.**

Async checks for DB, API response, Redux store, or any external state.

BEFORE:
```
await new Promise(r => setTimeout(r, 3000));
const count = await getDbCount();
expect(count).toBe(5);
```

AFTER:
```
await expect.poll(async () => getDbCount()).toBe(5);
```

Auto-retries with configurable interval + timeout. No magic numbers.

---

## Slide 6 — expect().toPass() for Race Conditions

**When one assertion isn't enough.**

Wraps any block of expectations:
```
await expect(async () => {
  await expect(price).toHaveText('$10');
  await expect(total).toHaveText('$10');
  await expect(badge).toBeVisible();
}).toPass();
```

Real use case: UI update + API response + DOM re-render all happening simultaneously. toPass() retries the whole block until everything stabilises.

---

## Slide 7 — The Framework Trap

**"Playwright is flaky" said the team with 40 sleeps.**

The real root cause:
- Plays nicely with Playwright ✅
- Retries on timeout instead of fixing the selector ❌
- waitForTimeout as a "quick fix" ❌
- Blaming the framework for test code debt ❌

Flaky tests are a code quality issue. Same as any other code.

Solution: code review gates for test code. No waitForTimeout. No sleep. No magic numbers.

---

## Slide 8 — Before/After Metrics

| Before | After |
|---|---|
| 40+ waitForTimeout | 0 waitForTimeout |
| ~78% pass rate | ~94% pass rate |
| Manual CI re-runs every morning | Green on first run |
| 3 hours debugging flaky failures | MTTR: immediate |
| [SCREENSHOT: Flaky dashboard before] | [SCREENSHOT: All green after] |

The only change was removing sleeps. Same app. Same framework. Same CI.

---

## Slide 9 — Summary

**3 patterns, 1 bonus, 1 rule.**

Patterns:
1. Auto-wait assertions — let Playwright wait
2. API mocking — deterministic setup, 10x faster
3. expect.poll() — async checks without timeouts

Bonus: expect().toPass() — stabilise race conditions

Rule: **NO waitForTimeout in production test code.**

Go check your test suite right now. Count the waitForTimeouts. Remove them.

---

## Slide 10 — About

**Victor Ematin** · AI Quality Engineering Lead · $0 budget

600+ E2E tests across 3 projects, zero flaky.

Allure TestOps · Playwright · Go · AI Testing

Follow for QA, Playwright, and AI-driven testing.
