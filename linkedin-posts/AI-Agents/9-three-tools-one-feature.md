**Format:** LinkedIn Pulse Article
**Series:** AI Agents #9
**Cover:** Comparison table — PW Agents vs KISS vs Autonoma across 8 metrics
**Feed Image:** Autonoma terminal: "136 tests, 14 modules, 6/6 mutations caught"
**Hook:** "I pointed 3 AI test tools at OrangeHRM — one gave me 8 tests in 10 minutes, another gave me 136 in 3.5 hours."

---

[COVER: Three logos side by side — Playwright mask, KISS icon, Autonoma A]

# I Ran 3 AI Test Tools on the Same OrangeHRM App — Here's What Each Produced

I took the same Workspace Notification Configuration page and let three AI tools compete: Microsoft's Playwright Agents (3-agent pipeline), KISS/Sorcar (prompt-driven), and Autonoma (entity-aware platform). Same app. Same page. Same admin credentials.

The results surprised me.

Playwright Agents generated 8 tests in 10 minutes — automated pipeline, zero edits. KISS produced 8 tests across two prompts plus a reusable 187-line POM. Autonoma ran for 3.5 hours and produced 136 test variations across 14 modules — but only 2 covered the page I asked about.

This is not a "which AI is best" contest. It's a map. Each tool trades off one strength against another — and knowing that trade-off before you start saves hours.

## The Feature

OrangeHRM 5.9's Workspace Notification Configuration page — a settings panel where admins configure Slack/Google Chat webhooks for birthday and anniversary alerts. The form has 7 fields, validation logic, API-backed enable/disable toggle, and a registration table.

This is OrangeHRM's first new feature in 2 years. Releases 5.8 and 5.8.1 shipped only security improvements. When a vendor ships nothing but security patches for 18 months, the next feature is worth testing well.

A realistic mid-complexity feature. Not a login form. Not a 10-tab dashboard.

## Playwright Agents — 8 Tests, 2 Auto-Fixes

Microsoft's [Playwright Agents](https://playwright.dev/docs/test-agents) (shipped May 2026) use a Planner → Generator → Healer chain. I ran `npx playwright init-agents --loop=opencode` and let it work.

**Planner** explored the page, documented 7 form fields, the Enable toggle, platform switching, and the registration table. Output: a 22-scenario test plan in Markdown.

**Generator** wrote 8 Playwright tests: 1 `@smoke` (page loads) and 7 `@local` (checkbox toggle, platform switching, webhook validation, registration CRUD).

**Healer** caught and fixed 2 failures in the first run:
- A Vue race condition in the Enable checkbox toggle — fixed by adding `page.goto()` reload after each toggle
- A duplicate registration API conflict — fixed by adding pre-cleanup via `DELETE` before the create flow

**Result:** 8/8 tests pass. One pipeline run. No manual editing.

## KISS/Sorcar — 8 Tests + POM, 2 Prompts

	[KISS/Sorcar](https://github.com/ksenxx/kiss_ai) generates test code by feeding a prompt to an LLM (I used Nemotron 3 Ultra Free on OpenRouter).
	
	Prompt 1: "Create a POM and 4 tests for workspace notifications." → 187-line `WorkspaceNotificationPage.ts` (POM) + 4 tests: smoke check, platform switching, empty validation, webhook URL validation. All passed.
	
	Prompt 2: "Create 3 advanced tests — registration, duplicate prevention, disable feature." → 3 more tests, one manual fix (POM's `waitForResponse` filter required HTTP 200, but duplicate POSTs return 400).
	
	**Result:** 8/8 tests pass. Two prompts, one code fix. The POM is reusable across test files.

## Autonoma — 136 Tests, 14 Modules, 3.5 Hours Total

[Autonoma](https://github.com/autonoma-ai/autonoma) (Apache 2.0, open-source April 2026) takes a codebase-first approach through 7 stages: explore pages → build knowledge base → audit entities → design scenarios → wire factories → generate tests → review.

The first run in Session 48 (June 2026) stopped at factory wiring. This time I added all 18 factories. The pipeline ran to completion.

**Total: 3.5 hours** from start to finish.

**What Autonoma generated:** 40 unique Markdown specification files — each describing user flows in natural language with frontmatter (title, intent, criticality) and step-by-step instructions. The INDEX.md lists 136 test variations because one spec file generates multiple parameterized variants (different roles, statuses, data values).

But here's the critical difference: these are NOT executable Playwright tests. Autonoma's architecture runs them through an AI agent loop — take a screenshot, ask an LLM what to do next, use vision to locate the element, execute via Playwright, repeat. The `.md` file describes intent, not selectors.

Of the 136 variations, only 2 covered the Workspace Notification page. The other 134 spread across Admin (29), PIM (15), Journeys (15), and 11 more modules. Autonoma optimizes for breadth, not depth.

Yet those 2 specs are fully traceable: every step in configure-slack-notification and validate-webhook-url maps to tests in both PW Agents and KISS. Specs describe intent — tests assert behavior. The same coverage, expressed at different abstraction levels.

**Result:** 136 test variations (40 unique `.md` files) across 14 modules. 3.5 hours total. No executable test files — requires Autonoma's AI agent runtime to execute.

[SCREENSHOT: Comparison table (PNG) — PW Agents vs KISS vs Autonoma across metrics]

## Mutation Testing — Do These Tests Actually Catch Bugs?

I injected 6 real-world fault simulations using Playwright's `page.route()` — the tests run against a mutated backend without touching Docker (mutation testing = page.route() intercepts API responses, no Docker restart). Each fault mimics a plausible production bug.

| # | Fault | PW Agents | KISS |
|---|-------|:---------:|:----:|
| 1 | API returns 404 on PUT toggle | ✅ Caught | ✅ Caught |
| 2 | API crashes with 500 on POST | ✅ Caught | ✅ Caught |
| 3 | Toggle state reverts after reload (PUT succeeds, GET returns old state) | ✅ Caught | ✅ Caught |
| 4 | Validation text "Required" rewritten to "Mandatory" in API responses | ✅ Caught | ✅ Caught |
| 5 | API response delayed by 10s | ✅ Caught | ✅ Caught |
| 6 | Page heading mutated in HTML | ✅ Caught | ✅ Caught |

**Both caught 6/6.** Not a single blind spot across any fault type — API failure, state corruption, text drift, or timeout. Each suite also has unique blind spots (PW Agents skips Google Chat validation, KISS skips Send Test button), but mutation testing proved them equally resilient where they overlap.

(The Autonoma `.md` specs can't participate here: they're natural language executed by an AI agent's vision loop, not test code that runs in a standard CI pipeline.)

## The Trade-Offs

| Metric | Playwright Agents | KISS/Sorcar | Autonoma |
|--------|:-:|:-:|:-:|
| Tests generated | 8 | 8 | 136 (40 unique) |
| Coverage | 1 page | 1 page | 14 modules |
| Format | Playwright `.spec.ts` | Playwright `.spec.ts` | Natural language `.md` |
| Execution | Standard runner | Standard runner | AI agent + vision runtime |
| Auto-fixes | 2 | 0 | 28 → re-gen (done) |
| POM created | No | Yes (187 lines) | No |
| Setup time | 10 min | 15 min | 3.5 hours |

Playwright Agents wins on **speed-to-value** — one pipeline, 8 tests, 2 auto-fixes. Ten minutes from config to green run.

KISS wins on **maintainability** — the POM is production-grade and reusable across test files. You pay two prompts and one manual fix, but you get real code.

Autonoma wins on **scope** — it explored the entire app, not one page. 136 test variations across 14 modules is unmatched. But the 3.5-hour runtime, 18 factories, and the review loop reveal the cost of breadth. And those 136 specs can't run in CI without Autonoma's AI agent runtime.

## What I'd Ship Tomorrow

For a single feature: **Playwright Agents**. 8 tests in 10 minutes with auto-healing is unbeatable for velocity.

For a full module: **KISS + Playwright Agents**. Use KISS for the POM skeleton, Playwright Agents for test scenarios. Best of both worlds.

For app-wide exploration: **Autonoma**. 136 test variations across 14 modules justify the 3.5-hour commitment. But plan for factory wiring (18 entities) and accept that the output is natural language specs — you'll need Autonoma's runtime to run them.

The key insight: these tools don't compete on the same axis. PW Agents and KISS generate **test code** that runs anywhere. Autonoma generates **test intent** that runs on its own platform. Your choice depends on whether you need portable assertions or broad coverage.

No single tool fits every context. The question isn't "which AI is best." It's "what problem are you solving right now?"

---

What trade-off matters most in your stack — and which tool surprised you most when you actually ran it?

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

#TestAutomation #Playwright #AIAgents #ZeroBudgetQA #GenAItesting
