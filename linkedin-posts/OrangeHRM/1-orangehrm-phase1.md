---
type: linkedin-post
title: "1-orangehrm-phase1"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# LinkedIn Post — OrangeHRM Phase 1

## Post Text (~1200 chars)

5 POMs. 11 tests. 2 expected fails. Building the test skeleton for OrangeHRM taught me more than 1000 passing tests on a project I already know.

**What I built**
5 Page Objects (Login, Dashboard, Admin, PIM, Leave). 11 tests across 4 modules. Fixtures with pre-logged-in state. Plus an exploration script that mapped all 12 OrangeHRM modules in 15 seconds using Playwright MCP.

The skeleton works. But the muscle isn't there yet.

**Code review found 6 issues in 11 tests**
page:any → Page, hardcoded URLs → baseURL, waitForTimeout → explicit waits, no @smoke tags, CI/CD in docs not YAML. All fixable. All blockers for scale.

**The real difficulty**
Shared demo — no API, no Docker, no control. Data changes between sessions. Tests interfere with each other.

**What I fixed**
One refactor session: 7/8 issues (1 N/A — no API). 7/7 smoke tests now pass ✅

**What's next**
Next sprint: 8 modules, local Docker, explicit waits.

The goal isn't 100% coverage. It's a skeleton that stays solid as I add muscle.

What's your Phase 1 checklist for new test suites?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#OrangeHRM #Playwright #TestAutomation #QAEngineering
