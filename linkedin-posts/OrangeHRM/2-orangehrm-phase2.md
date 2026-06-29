---
type: linkedin-post
title: "2-orangehrm-phase2"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

I spent 2 weeks testing on a shared demo. Then I caught it lying.

OrangeHRM OS 5.4 — its search API doesn't filter data. It returns every record every time. My waitForTimeout calls were masking a no-op — tests passed because the first page "looked right."

I trusted the black box. It was lying.

The demo resets data between sessions, blocks destructive operations, and returns 0 employees in Directory search. You can't trust anything it shows you.

So what did I build despite that?

4 new modules with working tests:

▸ Recruitment — load, add candidate, search ✅ (3/3 — the only module that accepts new data on shared demo)
▸ Performance — load reviews ✅ (empty, but correct — no review data seeded)
▸ Buzz — load feed ✅ | create post ❌ (demo blocks creation)
▸ Directory — load ✅ (0 employees returned — expected on shared)

Where that gets us:

Phase 1 → Phase 2: 11→25 tests, 7→15 smoke, 5→11 POMs, 6→0 waitForTimeout, 22%→43% coverage, 4/12→8/12 modules.

I documented 4 API endpoints — Recruitment, Performance, Buzz, Directory — to make tests data-aware instead of guessing.

4 tests skipped by design: Claim module not available (2), admin autocomplete (1), no candidates on fresh instance (1). 3 more marked @local — they only run on local Docker.

Recruitment became the first module at 100% coverage — because I could actually test it end-to-end on shared demo.

What I learned:

Phase 1 gave me bones. Phase 2 added organs. But the demo taught me something no textbook could: test what's real, not what's comfortable.

A passing test on a broken environment is worse than a failing one — because you think you're covered when you're not.

Drop your demo horror story below.

Victor Ematin · AI Quality Engineering Lead + OpenCode Agents


#OrangeHRM #Playwright #TestAutomation #QAEngineering #E2E **#OpenCodeDesktopOneLove** 