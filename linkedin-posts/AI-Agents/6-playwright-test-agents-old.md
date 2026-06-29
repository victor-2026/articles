# 30 Minutes with Playwright Agents: The Healer Is Not an Agent — It's You

**Format:** Article / LinkedIn Pulse + Carousel
**Series:** AI Agents for QA (Part 4)
**Cover:** Allure dashboard — 86 passed, 0 failed, 1 flaky, 2 skipped
**Feed Image:** 3-way comparison table (KISS vs Autonoma vs Agents)
**Hook:** "Playwright Test Agents fix your tests automatically — until they don't. Then you become the Healer."

---

[COVER: 6-allure-overview.png — Allure dashboard: 86 passed, 0 failed, 1 flaky, 2 skipped]

Three weeks ago, I ran KISS Sorcar on OrangeHRM 5.8.1 and paid $0.19 for 4 tests. Last week, Autonoma cost $4.99 but never finished the pipeline. This week, I tried Playwright Test Agents — the three agents built into `@playwright/test` — and the result surprised me.

The Planner generated a 419-line test plan with 25 scenarios across 7 modules in under 5 minutes. The Generator was ready to code. And the Healer? It fixed 2 visual regression snapshots and improved a test — but 3 data-level bugs? I had to fix those myself.

**🎭 What the Healer could and couldn't fix**

The Healer agent has a debug loop: run tests, identify failures, fix code, rerun. On visual regression tests it worked: 2 stale snapshots updated, 1 test improved (removed `fullPage: true` on admin table — page height varies between runs). The Healer can handle interface drift.

But 3 failures on OrangeHRM 5.8.1 were deeper — data, not selectors:
- **My Info edit:** Employee ID "0001" was duplicated across 3 users. The save API rejected every change with "Employee Id already exists". No selector mismatch — the data was corrupt.
- **PIM edit:** The row locator `.oxd-table-row:has-text("Admin")` matched 3 rows (Admin User, Alice Administrator x2). Not a broken locator — a data-quality issue that caused strict-mode violation.
- **PIM delete:** The employee search returned an empty table because @local tests ran twice in parallel (chromium + local projects) and clobbered each other's data.

The Healer's remediation strategies are: update selectors, fix assertions, improve timing. None of these help when the root cause is data corruption and test parallelism.

**🛠 What I actually fixed (in 30 minutes)**

[SCREENSHOT: 6-what-i-fixed.png — 4 issues with root cause, fix, lines changed (8 total)]

Total: 8 lines changed. Zero selector fixes.

**🎭 The Planner — actually useful**

The Planner agent navigated the Claim module, documented 5 navigation tabs, 7 search fields, 9 table columns, and 4 form fields. It produced a plan with 25 scenarios including happy path, edge cases, and configuration pages. The file is `specs/claim-plan.md` and it's genuinely good — I used it to write 3 new Claim E2E tests.

What the Planner can't do: understand that "Tech Conference" is the only event available, or that the currency dropdown has 100+ options. It documented what it saw, not what was significant.

**📊 The three-way comparison (updated)**

[SCREENSHOT: 6-comparison.png — KISS vs Autonoma vs Playwright Agents on OrangeHRM 5.8.1]

**🔍 Key insight: three tools, three layers**

KISS generates executable tests with auto-repair (the code layer). Autonoma plans tests from the codebase (the architecture layer). Playwright Agents explore and document the UI (the interface layer). They don't compete — I now use all three:

1. Autonoma → discover module structure (if context fits)
2. Playwright Agents Planner → explore and document specific pages
3. KISS Sorcar → generate executable tests from specs
4. Human → fix the data-level issues no agent can see

**✅ Final numbers**

- 86 tests pass, 0 fail, 1 flaky, 2 skipped (pre-existing MAINT-003)
- 3 pre-existing regressions fixed (8 lines changed)
- 3 new Claim E2E tests added: UI-based assign, search by status, validation
- Healer fixed 2 stale snapshots + improved 1 test (visual regression)
- `playwright.config.ts` fixed: @local tests no longer run twice
- Total cost: $0 (Playwright is free, OrangeHRM runs on Docker)

The Healer is a great idea. But the hardest bugs in test automation aren't selector drift — they're data corruption, configuration errors, and parallelism. No agent fixes those. Yet. What data-level bug did your AI testing tool miss?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#Playwright #TestAutomation #AITesting #ZeroBudgetQA #AIAgents
