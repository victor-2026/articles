**Format:** Pulse Article
**Series:** AI Testing
**Cover:** A collage of 10 tool entries (Kiro, Playwright Planner/Generator/Healer, Claude Code, MAS, Autonoma, Sorcar, Devin, Aider) with a "3 months, $0 budget" banner
**Feed Image:** Terminal screenshot showing all 10 tools with pass/fail status
**Hook:** I spent 3 months stress-testing 10 different AI testing agents on 4 real projects — here's what actually shipped to production.

---

[COVER: 12-ai-cover.png — 10 tools (Kiro, Playwright Planner/Generator/Healer, Claude Code, MAS, Autonoma, Sorcar, Devin, Aider), dark theme, "3 months · $0 budget", 6 prod / 2 retired / 2 experimental]

# AI Testing Agents in 2026: A 3-Month Field Report

**10 tools. 79 sessions. $0 budget. 6 still run in production today (5 at $0).** I spent 3 months stress-testing them on 4 real projects — OrangeHRM, Buzzhive, an NDA e-commerce codebase, and FrontRow.

Here's what survived contact with production — and what quietly died.

## Autonoma — The $4.99 Promise That Almost Worked

[Autonoma](https://getautonoma.com) builds a 6-step pipeline: pagesFinder → KB → entityAudit → scenarioRecipe → testGenerator. I ran it on OrangeHRM.

**What worked:** Steps 1-2 (pagesFinder, KB) are solid at 131K context. The agent builds a complete app map automatically.

**What didn't:** EntityAudit exploded to 274K tokens with POM files. ScenarioRecipe timed out at 191K. Worst of all — **the model auto-switched 3 times without asking**: deepseek → kimi → v4-pro → gpt-5.4-nano. The bill hit $3.62 instead of $0.50.

TestGenerator was never reached. Pipeline died at 4/6.

**Verdict:** Works for small apps (<50 pages). On real codebases with Page Objects, the context budget breaks. A manual KISS workflow ($0.19) produced the same tests with zero switching risk.

[SCREENSHOT: 12-ai-autonoma.png — pipeline 4/6, model auto-switch, $0.50→$3.62]

## Kiro — 36 Security Gaps in 2 Minutes

[Kiro](https://kiro.dev) is a security audit agent. It doesn't write tests — it finds vulnerabilities.

On **OrangeHRM** (PHP): 36 security-critical files with zero tests — auth, OAuth, permissions, SSO, certificates.

On an **NDA e-commerce codebase** (.NET): module-catalog — 14/16 controllers with zero tests (87.5%). 400 source files vs 48 test files. 5 test files with 0 test methods (files exist, tests don't).

Cost: ~$0.06 per run. Time: ~2 minutes.

**Verdict:** Instant value. Runs nightly in our CI now.

[SCREENSHOT: 12-kiro-audit.png — 36 security files, 7 critical/high, 0 tests]

## Devin — The 81.65% Blind Spot

[Devin](https://devin.ai) cloned both repos, analyzed the code, and found: 89/109 endpoints untested (81.65%). Of 110 `[Authorize]`-protected endpoints, 82 had zero test for 401/403.

Then I simulated a breaking change: removing `limited_permissions` from PermissionAuthorizationHandlerBase. **CI wouldn't catch it.** All 110 `[Authorize]` attributes would silently grant full access.

4 modules with zero coverage (127 files: 3 SQL providers + DistributedLock). Core module: 353 files, 4% coverage.

**The catch:** Devin — and [Aider](https://aider.chat) — are blind to the DOM. They guess selectors from Playwright error output. On Maintenance POM (OrangeHRM), Aider generated deeper POMs (10 methods vs 4) with its `--test-cmd` auto-fix loop — 2/2 tests green on the first run.

**Verdict:** Devin sees code structure; Aider sees test feedback. Neither sees the screen. Aider's auto-fix loop makes it more reliable for test generation.

[SCREENSHOT: 12-devin-coverage.png — 81.6% untested, 4 modules 0%, breaking change simulation]

## Playwright Test Agents — The Healer That Fixed 2 of 3

[Playwright's three agents](https://playwright.dev/docs/test-agents): **Planner** (explores → .md plan), **Generator** (.md → .ts tests), **Healer** (executes + auto-fixes).

The Healer is the real innovation. In one session, it fixed 2 stale snapshots and improved 1 test — autonomously. But it couldn't fix 3 data-level bugs, confirming the thesis: Healers fix UI, not data.

**Verdict:** Best built-in agent pipeline as of 2026. Combine with data seeding (not included) for full coverage.

[SCREENSHOT: 12-healer-report.png — 2/2 snapshots fixed, 0/3 data bugs, thesis confirmed]

## Claude Code — The CTO's Daily Driver

A CTO I work with uses [Claude Code](https://www.anthropic.com/claude-code) for tests every day. It integrates with CI/CD via MCP (Slack, Jira), and runs a closed-loop: if it breaks something, it fixes it.

No setup cost — but not a $0 tool: it needs a Claude Pro/Max subscription or API credits. No context budget drama. Just works.

**Verdict:** If you only pick one — pick this. It's the only paid tool on this list, so it stays in the CTO's stack, not my $0 one. The free equivalent: opencode with free models — same closed loop, zero cost.

## What Actually Runs in Production Today

[SCREENSHOT: 12-prod-table.png — 6 tools, what we use them for, production since]

| Tool | What We Use It For | Production Since |
|------|-------------------|-----------------|
| **Kiro** | Nightly security audit | Day 1 |
| **Playwright Planner** | New module exploration | Day 1 |
| **Playwright Generator** | Test generation from plans | Week 2 |
| **Playwright Healer** | Stale snapshot auto-fix | Week 2 |
| **Claude Code** | CI/CD + MCP pipeline | Week 4 |
| **MAS patterns** | Reusable learned_patterns | Week 6 |

**What we don't use:** Autonoma (context overflow — retired), Sorcar (superseded — retired), Devin (blind on selectors — experimental), Aider (experimental — blind on the DOM, but its `--test-cmd` feedback loop keeps it in the toolbox). 6 in production + 2 retired + 2 experimental = 10.

## The $0 Lesson

10 tools, 4 projects, 79 work sessions, **$0 budget** (free tiers + open source).

The winner isn't the most hyped tool. It's the one that:
- Fits your context budget
- Has a feedback loop (`--test-cmd`)
- Doesn't switch models behind your back
- Ships to production, not just to a demo

## How to Replicate This for $0

1. Pick one agent with a feedback loop (Aider's --test-cmd, Playwright's Healer) — not the most hyped one.
2. Run it on one real module, not a demo. Record cost per run from day one.
3. Gate it in CI: agent output is a suggestion until an eval or a human approves it.
4. Measure cost per test, not cost per month — and kill anything that switches models without asking.

📌 **More from the AI Agents series:**

1. [You're Measuring the Wrong Thing](https://www.linkedin.com/pulse/youre-measuring-wrong-thing-victor-ematin-y4jkf/) — 36 runs, 2 projects, 0% lift: why agent architecture matters more than model choice
2. [Skills Are Not npm Packages](https://www.linkedin.com/pulse/skills-npm-packages-what-i-learned-building-8-agent-victor-ematin-by2qf/) — What I learned building 8 agent skills — behavior blueprints, not code libraries
3. [Your Test Framework Has Blind Spots — I Found 49% Across 2 Projects](https://www.linkedin.com/pulse/your-test-framework-has-blind-spots-i-found-49-2-projects-ematin-dkxgf/) — Kiro coverage gap analysis
4. [I Spent $15 to Test 7 AI Agents](https://www.linkedin.com/pulse/i-spent-15-test-7-ai-agents-0-tool-beat-200mo-tier-victor-ematin-bxcvf/) — 7 agents, 3 projects, $15 in API credits
5. [AI User or AI Builder](https://www.linkedin.com/pulse/you-ai-user-builder-9-concept-maturity-test-victor-ematin-polhe/) — 9 concepts mapped to L1-L5: where the field report leads organizationally

Which AI testing agent actually runs in your CI today — and which one died quietly? Tell me in the comments.

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

#AITesting #QAAgents #Playwright #ZeroBudgetQA #GenAItesting #ClaudeCode
