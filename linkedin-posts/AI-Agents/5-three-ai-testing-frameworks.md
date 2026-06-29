# Four AI Testing Frameworks That Don't Compete: MAS, Playwright Agents, KISS Sorcar, Gulin's 3-Layer

**Format:** Article / LinkedIn Pulse
**Series:** AI Agents for QA (Part 3)
**Cover:** Four-layer stacked diagram — MAS (roles) → Playwright Agents (tools) → KISS Sorcar (execution bridge) → Anton Gulin (architecture)
**Feed Image:** Summary comparison table (PNG)
**Hook:** "Four frameworks from four places: my own codebase, Microsoft's Playwright team, a Berkeley Terminal Bench leader, and the first AI QA Architect. Each solves a different problem. Each is incomplete alone."

---

[COVER: Four-layer stacked diagram — MAS (roles) → Playwright Agents (tools) → KISS Sorcar (execution bridge) → Anton Gulin (architecture)]

Over the last 2 months, I evaluated four AI testing approaches: my own MAS, Microsoft's Playwright Agents, Berkeley's KISS Sorcar, and Anton Gulin's 3-layer model.

Each framework solves one layer — MAS: role memory (8 patterns). Playwright Agents: native auto-healing. KISS Sorcar: executable tests ($0.19/module). Anton Gulin: production gates (6 gates, 570 artifacts/run). You need all four — here's how they stack.

As I showed in Part 2 (published yesterday), KISS produces executable .ts tests with an auto-fix loop, while Autonoma generates .md specs via a 6-step pipeline.

Each one works. Each one is incomplete on its own. They don't compete — they stack.

## 🧩 Layer 1: MAS — Who does the work

MAS (Multi-Agent System) is role separation. Generator writes code, Critic validates assertions, Fixer patches failures, Executor runs the suite. The critical piece isn't the agents — it's the feedback loop.

After each cycle, patterns accumulate in `known_patterns.json`:

```json
{
  "id": "7",
  "error_type": "SelectorNotFound",
  "keywords": ["selector.*not found", "locator.*not found"],
  "fix": "Check data-testid attributes in DOM"
}
```

[SCREENSHOT: known_patterns.json showing 8 patterns with id, error_type, fix fields]

Our implementation currently holds 8 patterns across connection errors, timeouts, import issues, assertion mismatches, fixture problems, network failures, selector changes, and authentication errors. Each one eliminates a class of test failures.

MAS answers one question: **who** — which agent does what, and how does knowledge compound between sessions, not just within them?

## 🎭 Layer 2: Playwright Agents — How the work gets done
[SCREENSHOT: Playwright Agents architecture — Planner, Generator, Healer in sequence]

Microsoft shipped three agents directly inside `@playwright/test`:

- **Planner**: explores the app, produces a Markdown test plan
- **Generator**: transforms the plan into executable Playwright `.ts` tests
- **Healer**: runs the suite, auto-fixes locators and waits on failure

Integration is one command:
```bash
npx playwright init-agents --loop=opencode
```

I've mapped the Playwright Agents architecture to my OrangeHRM stack. The key insight: Healer closes the gap that KISS Sorcar fills — auto-fix of locators and waits — but natively inside `@playwright/test`, without a CLI agent fee (~$0.19/module with KISS). The trade-off: Playwright Agents only work inside a Playwright project. KISS works with any framework.

Playwright Agents answer: **how** — what tool chain turns exploration into executable tests and auto-recovers from failures?

## 🔧 Layer 3: KISS Sorcar — The execution bridge
[SCREENSHOT: 4-kiss-terminal.png — 3/3 passed, auto-fix loop]

Between Playwright Agents (free, Playwright-only) and Autonoma (pipeline, non-executable output), KISS Sorcar fills the execution gap. It's a CLI coding agent that reads existing POMs, generates `.ts` Playwright tests, and runs `npx playwright test` to verify them. When 2 of 3 generated tests failed on first run, it auto-fixed hallucinated selectors and re-ran until green.

In my OrangeHRM test, KISS produced 3 passing @smoke tests for $0.19 on deepseek-v3.2 — covering the Maintenance module (password gate, purge records). The Fix-Run-Verify loop is the key architectural difference: it cares about the exit code, not subjective review.

KISS answers: **how do I get executable tests today, on any framework, without writing them myself?**

### Spec-driven pipeline (multi-step) vs Fix-Run-Verify loop (one tool, one exit code)

## 🏛️ Layer 4: Anton Gulin 3-Layer — Why and what proves it
[SCREENSHOT: Allure dashboard showing 37 OrangeHRM tests with pass/fail and trace evidence]

Anton Gulin (former Apple SDET, now AI QA Architect) published a model that separates AI testing into three mandatory layers ([original post](https://anton.qa/blog/posts/ai-test-automation-architecture-3-layer-system)):

[SCREENSHOT: 5-Table-Layer-4-1-2.png — Anton Gulin 3-layer model + 6 quality gates]

Plus 6 gates before an AI-generated test ships:

I mapped every layer to my OrangeHRM stack:

- **Orchestration**: AGENTS.md boundaries map risk questions to each of 37 tests across 13 modules (33 pass, 3 pre-existing regressions on 5.8.1, 1 skip)
- **Execution**: GitHub Actions runs 26 @smoke tests in CI, with retries for flaky requests
- **Evidence**: Each CI run produces 570 Allure artifacts — traces, screenshots, and logs

The 6 gates are documented in my project's AGENTS.md. Not all are automated yet — Scope and Review still require human judgment. But Data, State, Run, and Evidence are enforced by the CI pipeline.

Anton Gulin answers: **why** — what risk are we covering, and how do we prove the test worked?

## 📊 The comparison table

[SCREENSHOT: 5-Table-Layer-4-3.png — 4-column comparison: MAS, Playwright Agents, KISS Sorcar, Anton Gulin across 10 dimensions]

## 🔗 Why you need all four

Here's what happens when you skip a layer:

- **MAS only**: you have role separation and pattern memory but no auto-recovery when selectors change
- **Playwright Agents only**: you have auto-healing but zero organizational memory between sessions — every selector change resets your knowledge
- **KISS Sorcar only**: you can generate tests fast, but with no role structure or architecture, they don't survive a framework upgrade
- **Anton Gulin only**: you have a perfect policy framework but no tools to execute or compound knowledge — policy alone doesn't write tests

My OrangeHRM stack is building toward all four. MAS provides the structure. Playwright Agents and KISS Sorcar provide the automation and execution layers. Anton Gulin's gates provide the production guardrails.

## 💡 The rule

Anton Gulin wrote the sentence that stuck with me:

> Generation is cheap. Evidence is the architecture.

I'd add two more:

> Tools without architecture produce flaky tests.
> Roles without tools produce theory.

Each of the four frameworks solves one part of the puzzle. The winning strategy isn't choosing one — it's knowing which layer you're missing and filling that gap first.

## ❓ Which layer is missing in your stack?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIAgents #Playwright #TestAutomation #AutonomaAI #KISSSorcar
