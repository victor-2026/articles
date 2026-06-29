---
type: linkedin-post
title: "3-autonoma-vs-sorcar"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# I ran two AI agents on the same Playwright project. One discovered 13 modules and seeded the database. The other wrote executable code. They're not competitors — they're two halves of a workflow.

**Format:** Article / LinkedIn Pulse
**Series:** AI Agents for QA (Part 2b)
**Cover:** KISS Sorcar vs Autonoma — comparison table
**Feed Image:** 3-table.png
**Hook:** "28 specs vs 1 working test. 10 minutes vs 2. Autonoma on trial credits. KISS Sorcar on BYO key."

---

[COVER: KISS Sorcar vs Autonoma — comparison table]

Yesterday I tested two AI agents on the same OrangeHRM project. KISS Sorcar (Berkeley, Terminal Bench 2.0 leader at 62.2%) generated a working Playwright POM + test in 16 steps. Autonoma (YC W22, codebase-first testing platform) ran a 7-step pipeline: discovered 13 modules, verified 6 database entities, and generated 28 test specs plus 5 cross-module journeys.

28 specs across 13 modules in 10 minutes — $0.02. One working test in 16 steps — $0.01. Same OrangeHRM project, two different categories. They're not competitors. They're two halves of a workflow.

**What each agent does**

KISS Sorcar is a coding agent. It reads your project conventions from a single `SORCAR.md` file, writes code, runs tests, fixes failures, and repeats until everything passes. Output: production-ready Playwright `.ts` files. It competes with Cursor (61.7%) and Claude Code (58%) on Terminal Bench 2.0.

Autonoma is a testing pipeline platform. It runs 7 steps: page discovery → knowledge base → entity audit → scenario definition → factory verification → test generation → review. Output: `.md` spec files with plain English step descriptions plus an Environment Factory that seeds test data on demand. It competes with Mabl, Testim, and QA Wolf — not with coding agents.

**The comparison**

| | KISS Sorcar | Autonoma |
|---|---|---|
| **Category** | Coding agent | Testing pipeline platform |
| **Output format** | `.ts` (runnable) | `.md` (specs) |
| **Coverage depth** | 1 module (executable) | 13 modules (spec) |
| **Run-ready** | ✅ `npm test` | ❌ Manual `.ts` conversion needed |
| **Data seeding** | ❌ None | ✅ 6 entities via REST API |
| **Review model** | Human: mandatory | AI auto-review (optional manual) |
| **Stack detection** | Reads `SORCAR.md` | Defaults to Node.js (needs proxy for PHP/Python/Go) |
| **Priority tuning** | N/A | 5 critical / 14 high / 9 mid |
| **Backend integration** | N/A (no backend needed) | ⚠️ Node.js proxy required for non-Node projects |
| **Benchmark** | **62.2%** Terminal Bench 2.0 [arXiv:2604.23822](https://arxiv.org/abs/2604.23822) | N/A (compared vs Mabl/Testim, not coding agents) |
| **Cost per run** | ~$0.01 (DeepSeek) | ~$0.02 (GPT-4 mini, ~2K tokens) |

**Where Autonoma wins**

Autonoma discovered the full app structure without any exploration script. It identified 14 sub-features, mapped API endpoints, and proposed seed data for 6 database entities — including cross-references between employees, users, leave requests, and buzz posts. The Environment Factory created all 6 entities via REST API in ~30 seconds total.

The review pipeline caught 3 spec issues on the first cycle and auto-fixed them. The second cycle passed 30/30. This matters for teams that maintain test suites — automated spec review catches inconsistencies before they reach production.

Autonoma also generates journey tests spanning multiple modules: onboard employee → create user, hire candidate → directory entry, update profile → buzz post. These cross-module scenarios are expensive to design manually.

Autonoma's test prioritization: 5 critical, 14 high, 9 mid, 0 low. The auto-prioritization saved me from deciding which modules to cover — it ranked 14 tests as high or critical without human input.

**Where KISS Sorcar wins**

KISS Sorcar wrote code that runs. No translation step. No manual .ts conversion. The test passed on the first execution, with correct selectors, proper POM patterns, and matching assertions.

The fix-run-verify loop is the key architectural difference. KISS Sorcar writes code, runs it, sees the failure, fixes it, and re-runs. This feedback loop catches selector mismatches and assertion bugs before a human reviews the diff.

**Where KISS Sorcar loses**

KISS Sorcar doesn't explore the app. It needs you to tell it what to do — which module, which page, which test. No discovery, no API mapping, no data seeding. You get one test per prompt, not a coverage plan.

It also can't generate journey tests spanning multiple modules. The hire-candidate-to-directory flow (5 steps across PIM, Admin, Recruitment) is impossible in a single KISS Sorcar session without manual chaining.

And it has zero opinion about priority. Every test is equally important until a human says otherwise.

**Where Autonoma loses**

Autonoma's stack detection is its weakest link. It generated factory scaffolding for Node.js/Next.js — but OrangeHRM runs on PHP/Symfony. I had to build a standalone Node.js proxy server to bridge the Environment Factory protocol with the PHP REST API. This added ~30 minutes of manual setup that KISS Sorcar doesn't require.

[SCREENSHOT: Autonoma adapter selection — 15 backend options, PHP (Laravel) highlighted, but OrangeHRM uses Symfony]

Test priorities need human override. Autonoma assigned 9 of 28 tests to `mid` priority — some of these should be `high` for a production suite. The auto-prioritization is a good start but not production-ready.

And the biggest gap: Autonoma's output is `.md` spec files, not executable tests. You still need a coding agent — or a human — to translate them into runnable Playwright code.

**The combined workflow**

The real insight is that these agents are complementary, not competitive:

1. **Autonoma explores** the app — discovers modules, maps API endpoints, seeds test data
2. **Autonoma generates** `.md` specs — 28 tests covering 13 modules
3. **A human reviews** the specs — decides which are critical, which to combine, which to skip
4. **KISS Sorcar converts** selected specs into runnable `.ts` tests — following project conventions from `SORCAR.md`

This turns a 40-hour manual effort into a 30-minute collaborative workflow. Autonoma handles the discovery and coverage planning. KISS Sorcar handles the code generation. The human stays in the loop as reviewer and decision-maker.

**The takeaway**

The question isn't "which AI agent is better?" It's "what problem are you solving?"

Need to onboard a new project and map its complete module structure? Autonoma's pipeline delivers 13-module coverage in 10 minutes.

Need to write a specific test for a module you already understand? KISS Sorcar cuts 40 hours of manual POM writing to 16 steps.

The winning strategy isn't choosing one agent. It's knowing when to use which.

---

Have you used both a coding agent and a testing pipeline? Which one do you reach for first?

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIAgents #Playwright #TestAutomation #KISSSorcar #Autonoma
