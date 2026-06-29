---
type: linkedin-post
title: "4-orangehrm-dual-target"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# OrangeHRM Phase 3 — Same test suite, two environments, one flag

**Format:** Post / LinkedIn Feed
**Series:** OrangeHRM Phase 3
**Note:** Bridge to Part 3 (Deployment carousel, published Jun 5)

---

29 tests. 2 environments. 1 flag.

After 4 hours of Docker hell (previous post), this is the end state.

I built a Playwright test suite for OrangeHRM that runs on a shared demo (read-only, 23 tests) and on local Docker (read-write, 29 tests with 6 @local-only). Same code, same assertions. The only difference? `LOCAL=true/false`.

**The invariant:** 22 smoke tests passed on both environments — shared demo and local Docker — with zero flakiness. That's what dual-target gives you.

**How it works:** `playwright.config.ts` has 3 projects — smoke (CI), chromium (demo), local (Docker) — gated by `LOCAL=true` and Playwright grep tags. 4 tests skipped by design (Claim module missing, no candidates on fresh instance).

**Why this matters:** You can't trust demo data. But you can still validate 80% of your smoke suite on the demo — and the @local tests pick up the rest on a real server.

**Numbers:**
→ 29 unique (23 demo / 29 local)
→ 22 smoke on both ✅
→ 6 @local. 4 skipped. 0 waitForTimeout in either config.

What's your strategy for testing across environments — same suite with tags, or separate configs entirely?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#OrangeHRM #Playwright #TestAutomation #QAEngineering #CICD
