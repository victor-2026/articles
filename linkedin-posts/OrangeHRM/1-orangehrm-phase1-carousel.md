---
type: linkedin-post
title: "1-orangehrm-phase1-carousel"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# Carousel — OrangeHRM Phase 1: The Skeleton (8 slides)

## Slide 1: Title

**Phase 1 — The Skeleton**

5 POMs · 11 tests · 2 expected fails

[SCREENSHOT: outputs/screenshot-dashboard.png — OrangeHRM Dashboard]

---

## Slide 2: What I Built

**5 Page Objects. 4 Modules. 11 Tests.**

```
Login → Dashboard → Admin → PIM → Leave
     ↑           ↑         ↑       ↑
auth.spec    POMs     fixtures   config
```

[SCREENSHOT: outputs/screenshot-pim.png — PIM employee list]
[VISUAL: architecture diagram — arrows from spec → POM → page]

---

## Slide 3: The Shared Demo Trap

**No API. No Docker. No Control.**

Every test runs on a shared demo instance:
- Data changes between sessions
- State resets unpredictably
- No API seeding, no teardown shortcuts
- Tests interfere with each other

[SCREENSHOT: outputs/orangehrm-quick_20260531_210525/screenshots/explore_1_login_page.png — OrangeHRM Login page]

---

## Slide 4: Code Review Wake-up

**6 problems in 11 tests. Before Phase 1 started.**

| Problem | Impact |
|---------|--------|
| `page: any` → no TS safety | Silent failures |
| Hardcoded URLs | Dead on URL change |
| `waitForTimeout` | Flaky by design |
| No `@smoke` tags | No quick feedback |
| CI/CD in doc, not YAML | Never ran in CI |

[VISUAL: table — each row = problem + impact]

---

## Slide 5: Before / After

**The same code. One session. 7 fixes.**

| Before | After |
|--------|-------|
| `page: any` | `page: Page` via BasePage |
| `page.goto('https://...')` | `baseURL` in config |
| `waitForTimeout(3000)` | Explicit waits |
| No smoke tags | 7 `@smoke` tests |
| CI/CD in markdown | `.github/workflows/` |

[VISUAL: split — left "before" code (red), right "after" (green)]

---

## Slide 6: AI Can't Save You Here

**Webwright: 50+ runs, 5 models, 1000 API calls — 0 usable tests.**

AI-generated testing failed on an unfamiliar domain. The skeleton was built by hand in one session.

[VISUAL: large **0** centered. Caption: "usable tests"]

---

## Slide 7: What Passed

**7/7 smoke tests ✅. 2 destructive = expected fail (shared demo).**

After one refactor session:
- Auth login + dashboard ✅
- Admin page + search ✅
- PIM list + search ✅
- Leave list ✅

[SCREENSHOT: outputs/screenshot-smoke-pass.png — 12/12 smoke passed в терминале]
[SCREENSHOT: outputs/screenshot-admin.png — Admin page с user list]

---

## Slide 8: The Philosophy

**"The goal isn't 100% coverage. It's a skeleton that stays solid as I add muscle."**

**What's your take: start with a skeleton, or go for coverage from day 1?**

[VISUAL: minimal text on dark background. Skeleton/architecture metaphor]

---

#OrangeHRM #Playwright #TestAutomation #QAEngineering #Phase1
