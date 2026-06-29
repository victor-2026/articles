---
type: linkedin-post
title: "Removing 4,000 Lines of AI Tests Boosted My QA"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

 🚀 How Removing 4,000 Lines of AI Tests Boosted My QA. Best thing I've done all year.
  
277 unique tests running across 4 browsers — 1,108 Playwright runs, plus Python helpers and k6 load. All on a $0 AI budget.  
📊 API coverage hit 94%. PBT hit 100%.  
  
The stack: Playwright E2E suite hitting two environments — Docker (local full stack) and Render (backend-only, free tier).  
🔧 CI/CD runs smoke tests on every push via GitHub Actions — 12 endpoints, 3 minutes.  
⚙️ Backend had to be stabilised first: exception handlers, connection pooling, uptime monitor. The usual production hardening nobody talks about.  
Then I looked at the test code.  
🗑️ Two monolithic files — 3,908 lines of AI-generated spaghetti with 15 duplicated API blocks and no shared fixtures.  
✨ One sprint later: 23 clean modules, shared fixtures.ts, CI in 3 minutes.  
The refactoring also found what testing missed:  
🐛 A race condition that lived in production for a month. Sequential tests couldn't catch it — same microsecond, same JWT, unique_violation in PostgreSQL. Only parallel execution across 4 browser projects exposed the collision.  
🔑 One line fix: jti: uuid.uuid4().  
  
What the numbers say:  
🔄 → 2 monoliths → 23 modules, ~4,000 lines deleted  
▶️ → 1,108 runs across 4 browsers (277 unique)  
🌐 → 2 environments: Docker (local) + Render (cloud)  
🎯 → 1 race found, 1 line fix  
🔁 → 15 AI models cycled — 6 already gone  
  
Free AI is a treadmill. Keep moving or get left behind.  
  
📈 Phase 1 recap: [**https://lnkd.in/dbsecZfm**](https://www.linkedin.com/safety/go/?url=https%3A%2F%2Flnkd%2Ein%2FdbsecZfm&urlhash=ZngU&mt=O94EM1GvHgDdcULiKNzv_FhiFeHMctEiFCikf2bKw9aO4_ykxAimrV2G7nl5TAO8Jf1O8-83KtnowcTCZJt8OlNzgmcZ7DpZeXFDAFKklzXUh2EkwJtkfA&isSdui=true)  
  
🔥 Phase 3 is cooking — Go, C#, mutation testing, Render frontend. Next carousel.  
  
❓ What's the messiest test suite AI has helped you create?  
  
Victor Ematin · as AI Quality Engineering Lead · OpenCode Go  
[**#TestAutomation**](https://www.linkedin.com/search/results/all/?keywords=%23testautomation&origin=HASH_TAG_FROM_FEED) [**#ZeroBudgetQA**](https://www.linkedin.com/search/results/all/?keywords=%23zerobudgetqa&origin=HASH_TAG_FROM_FEED) [**#GenAItesting**](https://www.linkedin.com/search/results/all/?keywords=%23genaitesting&origin=HASH_TAG_FROM_FEED) [**#Playwright**](https://www.linkedin.com/search/results/all/?keywords=%23playwright&origin=HASH_TAG_FROM_FEED) [**#Render**](https://www.linkedin.com/search/results/all/?keywords=%23render&origin=HASH_TAG_FROM_FEED) [**#QATips**](https://www.linkedin.com/search/results/all/?keywords=%23qatips&origin=HASH_TAG_FROM_FEED)
Article published: https://www.linkedin.com/feed/update/urn:li:ugcPost:7466120792578121729/
Article includes: pdf carousel Phase2 - The refactoring sprint![[phase2-carousel 1.pdf]]