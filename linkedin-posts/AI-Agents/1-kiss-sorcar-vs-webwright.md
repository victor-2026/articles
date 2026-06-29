---
type: linkedin-post
title: "1-kiss-sorcar-vs-webwright"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# I tested 2 AI agents on the same Playwright task. One took 50+ runs. The other got it right on the first try.

**Format:** Article / LinkedIn Pulse
**Series:** AI Agents for QA
**Hook:** "50+ runs vs 1 run. $2.37 vs $0."

---

A month ago I spent 40+ hours trying to make Microsoft's Webwright generate a working Playwright test. 50+ attempts. 5 different models. 1,000+ API calls. The result: one barely working test and a lot of format errors.

Yesterday I ran the same type of task with KISS Sorcar — an open-source agent from Berkeley. 16 steps. 1 test. 0 failures. Cost: $0.

**What is KISS Sorcar**

KISS Sorcar is an open-source AI coding agent that beats Cursor and Claude Code on Terminal Bench 2.0 (62.2% vs 61.7% vs 58%, run on Claude Opus 4.6). Built by Koushik Sen at Berkeley. 500+ GitHub stars. 3,270 lines of Python. Free. Local. Bring your own API key.

Unlike Webwright — which struggled with JSON formatting, absolute paths, and "cd" commands — KISS Sorcar runs as a VS Code extension. You give it a task in natural language. It reads your project conventions from a single `SORCAR.md` file. Then it writes code, runs tests, fixes failures, and repeats until everything passes.

**The experiment**

I gave both agents the same task: create a Playwright Page Object and test for the 12th module of my OrangeHRM test suite. Maintenance module. No tests existed. The agent had to read existing code patterns, write the POM, register it in fixtures, and run the test.

Webwright took multiple sessions. Format errors. Wrong selectors. Missing imports. It generated Selenium code when I asked for Playwright. After 50+ attempts across 5 models, I got one test that passed — but the POM was broken.

KISS Sorcar read my `SORCAR.md`, studied existing POMs and spec files, matched the patterns, and wrote correct code in 16 steps. The test passed on the first run.

**What makes the difference**

| | Webwright | KISS Sorcar |
|---|:---:|:---:|
| Terminal Bench 2.0 | Unknown | **62.2%** (#1 vs Cursor + Claude Code) |
| Playwright built-in | ❌ Separate browser | ✅ Chromium + Playwright |
| Git safety | ❌ Edits files directly | ✅ Git Worktree isolation |
| fix-run-verify loop | ❌ Generates only | ✅ Writes → tests → fixes → repeats |
| Format errors | >30% | 0% (1 run, 1 pass) |
| Cost | $2.37/asset | $0 (BYO key) |
| Models | Anthropic only | Model-agnostic (OpenRouter, Groq, Ollama) |

The key difference isn't model quality. Both used similar-tier LLMs. The difference is **agent architecture**. Webwright was designed as research — it proved that agents *can* generate browser tests. KISS Sorcar was designed as a tool — it proves that agents *should*.

**The architecture that matters**

KISS Sorcar runs on 5 layers, each exactly one concern:

1. **KISS Agent** — budget-tracked ReAct loop (483 lines)
2. **Relentless Agent** — auto-continuation, never gives up (514)
3. **Sorcar Agent** — coding tools + browser + parallel sub-agents (912)
4. **Chat Agent** — multi-turn history (443)
5. **Worktree Agent** — Git isolation per task (916)

Webwright's architecture: one monolithic Runner that spawns browser sessions. No Git isolation. No built-in Playwright — you install it separately. No fix-run-verify loop — it stops after generating code.

**What this means for QA**

I've now tested three approaches to AI-generated tests in the past 30 days:

1. **Manual** — I write tests. 100% control. Slow.
2. **Webwright** — research-grade. Impressive demos. Not production-ready.
3. **KISS Sorcar** — open-source. Free. Works today.

The cost trajectory is clear: $0 per automated test, 16 steps, first-try success. For teams maintaining growing test suites like my OrangeHRM project, that's the difference between AI as a science project and AI as a daily tool.

**The SORCAR.md pattern**

KISS Sorcar reads one file at the start of every task: `SORCAR.md`. This is where you define project conventions — imports, selectors, no-go zones, test commands. It's like `AGENTS.md` for code generation, but lighter: 60 lines, pure convention, no fluff.

[SCREENSHOT: SORCAR.md content with POM template, test commands, and no-go zones]

I've published the full guide in my OrangeHRM repo.

**What I'm testing next**

Can KISS Sorcar refactor 40+ `waitForTimeout` calls into explicit waits across a 29-test suite? Can it generate mutation tests for API endpoints? If it handles those, the dream of a QA engineer who *reviews* AI-generated tests instead of *writing* them — becomes real.

What AI agent have you tried for test generation — and did it actually work?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#KISSSorcar #AIAgents #TestAutomation #Playwright #ZeroBudgetQA
