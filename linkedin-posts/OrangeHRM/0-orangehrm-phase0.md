---
type: linkedin-post
title: "0-orangehrm-phase0"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# LinkedIn Post — OrangeHRM System Testing

## Post Text (~1100 chars)

🧠 OrangeHRM: 12 modules, 51 tests, 20% coverage. The math that matters.

20% coverage with a traceability matrix beats 80% without one.

I started building an E2E test suite for OrangeHRM — one of the most popular open-source HRMS systems.

12 modules. 51 test cases defined. Only 10 implemented (20% coverage).

The gap isn't about "writing more tests" — it's about structure:
📊 Traceability matrix: every test → module → page → POM
- Test cases with priorities: Critical / High / Medium
- Page Object Model from day 1 (not refactoring later)
- Exploration data: 12 modules mapped with screenshots

Stack: Playwright + TypeScript + POM — zero dependencies beyond that.

What I learned from Buzzhive (292 unique tests, 96% mutation score — repo in comments):
- Start with POM, not raw selectors
- Traceability matrix saves hours during reviews
- Playwright MCP found 12 untested critical paths in 15 minutes

Next: 8/12 modules with full traceability — confidence to deploy, not just coverage numbers.

🎯 What's your coverage threshold for "confidence to deploy"? 60%? 80%? Or is it something else entirely?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#TestAutomation #Playwright #OrangeHRM #E2E #QAEngineering
