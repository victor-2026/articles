**Format:** Pulse Article
**Series:** AI-Agents (Article 11)
**Cover:** Coverage gap comparison — 49 uncovered methods across 2 projects (OrangeHRM + Buzzhive). Title: "Kiro.dev coverage gap analysis — cross-project"
**Feed Image:** `11-kiro-coverage-comparison.png`
**Screenshots:**
  - OrangeHRM coverage table: `11-kiro-coverage-table.png`
  - Buzzhive coverage table: `11-kiro-buzzhive-table.png`
  - Comparison summary: `11-kiro-coverage-comparison.png`
**Hook:** "I ran an AI IDE against two production test frameworks — it found 49 methods I never tested. Across two completely different codebases."

---

# Your Test Framework Has Blind Spots. I Found 49 in 2 Projects.

[COVER: Comparison table — OrangeHRM: 14 gaps, Buzzhive: 35 gaps, Total: 49 gaps, 164 tests generated]

**49 methods and endpoints with zero test coverage. Across two production applications. Found in under an hour by an AI IDE with $0 budget.**

I spent weeks building Page Object Models for OrangeHRM (13 Page Objects) and [Buzzhive](https://github.com/victor-2026/qa-automation-playwright) (52 API endpoints). Then I gave [Kiro.dev](https://kiro.dev) access to both codebases. **14 uncovered methods in OrangeHRM. 35 uncovered endpoints in Buzzhive. Including `approveClaim`, `rejectClaim`, and critical API flows I wrote but never tested.**

Here is what happened across two completely different architectures, and what it says about the limits of human test planning.

## The Setup

**OrangeHRM** has ~200 tests across 16 modules. The POM layer is mature — 13 Page Objects, each with dedicated methods for every user-facing action.

**Buzzhive** has 330 tests across 5 testing layers (E2E, API, contract, mutation, PBT). The API coverage was 94% — or so I thought.

Both frameworks had the same blind spot. You write tests during development, use them in CI, but who audits the test suite itself for untested methods?

The breakdown:

| Project | Methods/Endpoints | Tested | Uncovered | Tests Generated |
|---------|-------------------|--------|-----------|-----------------|
| OrangeHRM | 69 POM methods | 55 | **14** | 42 |
| Buzzhive | 52 endpoints | 17 | **35** | 122 |
| **Total** | **121** | **72** | **49** | **164** |

## What the AI Actually Found

[SCREENSHOT: OrangeHRM coverage gap table — Claim: 3 gaps, Admin: 11 gaps]

In Buzzhive, the picture was even more dramatic — 35 endpoints across auth, posts, users, and admin with zero direct coverage:

[SCREENSHOT: Buzzhive coverage gap table — 35 uncovered endpoints across auth, posts, users, admin]

Three categories of gaps emerged across both projects:

**Category 1 — Forgot to test (human error).** `approveClaim` and `rejectClaim` are core business logic in OrangeHRM. I simply never wrote a spec for the approval workflow. The POM had the methods. The test file had assertions for list view, filters, data entry — but not the actual decision flow.

Same pattern in Buzzhive: 12 admin endpoints for user management, role assignment, and system configuration — completely untested. Core API flows that should have been covered in week one.

**Category 2 — Tested indirectly, never directly.** Several OrangeHRM methods like `isUserFormVisible` and `editUserStatus` were exercised by other tests but never had their own assertion. The POM worked. The coverage was an illusion.

In Buzzhive, 8 API endpoints were called by other tests as setup steps but never validated directly. The API worked. The assertions were missing.

**Category 3 — Edge cases and error paths.** 15 Buzzhive endpoints handled error scenarios (401 unauthorized, 403 forbidden, 404 not found, 422 validation errors). I tested the happy paths. I never tested what happens when things break.

## The Self-Healing Moment

Kiro generated spec files for both projects: 42 tests for OrangeHRM, 122 for Buzzhive. **164 tests generated. 144 passed on first run. 20 failed — the AI fixed 8 (OrangeHRM UI timing); 12 exposed a real test environment gap (Buzzhive shared state).**

**OrangeHRM:** The first run failed in 8 places. The AI read the Playwright error output, identified the root causes (toast notifications closing before assertions, strict mode violations on shared selectors), and fixed them. Two null-safety issues. One unused helper. All automated.

**Buzzhive:** 110 tests passed on the first run. 12 failed — all in a group conversation endpoint that required specific database state. These failures exposed a real gap: the spec assumed clean state that did not exist in a shared test environment. A human would have hit the same issue.

The difference tells its own story. OrangeHRM (custom CSS, complex UI timing) triggered flaky-test patterns a human would recognise. Buzzhive (REST API) failed on environment assumptions, not code quality. The AI self-healed UI timing issues but could not fix missing test data — that is still a human responsibility.

## Cross-Project Validation

This is not a one-off result. The same AI IDE, the same approach, applied to two completely different codebases:

- **OrangeHRM:** PHP backend, custom CSS, [Playwright](https://playwright.dev) UI tests, Page Object Model
- **Buzzhive:** Node.js backend, REST API, Playwright E2E + API tests, modular architecture

Different languages. Different frameworks. Different testing strategies. Same blind spot. Same AI solution.

If this were one project, I could dismiss it as a special case. Two projects with the same pattern? That is a systemic gap in how test engineers plan coverage.

## How Critical Were the Gaps?

Not all 49 gaps were equal. Here is the breakdown across both projects:

| Severity | OrangeHRM | Buzzhive | Total | Examples |
|----------|-----------|----------|-------|----------|
| **🔴 Real hole** | 2 | 4 | **6** | `approveClaim`, Search API (0% coverage), admin ban testing non-existent endpoint |
| **🟡 Important** | 3 | 8 | **11** | `openFirstClaimDetails`, Messages send/read, Comments edit/delete |
| **🟢 Incremental** | 8 | 22 | **30** | `isUserFormVisible`, avatar upload, pin/unpin, comment likes |
| **⚪ Noise** | 1 | 1 | **2** | Unused helper `loginAs()`, duplicate assertions |

**Key finding:** 6 real holes across both projects — including Search with 0% coverage and an admin ban test that validates an endpoint that does not exist in the backend. The rest is healthy CI/CD appetite, not critical gaps.

## Why Traditional Metrics Missed This

Simple reason: **we measured coverage at the endpoint level** (94% = 49/52 base URLs). Kiro measured at the **method + sub-endpoint level** — there coverage was ~60%. Different metric. Search API did not appear in the 52 because `search/` counted as one endpoint.

Second reason: **human — we tested what we considered important** (auth, posts, profile, admin). We never did a full inventory of all routes × methods.

## What Other Tools Would Have Found

| Tool | Would Find | Would Miss |
|------|------------|------------|
| **OpenAPI diff** (export spec → compare with tests) | Search (0% — immediately visible), all method-level gaps | Admin ban mismatch (spec may be outdated) |
| **Code coverage (Istanbul)** on backend | Search routes — 0 hits | UI gaps |
| **Pact contract testing** | Messages, Comments (consumer not covered → contract not generated) | Search (if search is not consumed by anyone, Pact stays silent) |
| **Mutation testing** | Admin ban test — mutation survives (test does not validate logic) | Search gaps |
| **Playwright trace viewer** | Dead code `loginAs()` | API gaps |

**Bottom line:** Kiro did in 7 minutes what the combination of OpenAPI diff + code coverage + mutation testing takes 3-4 hours to set up. The value is not in the uniqueness of findings, but in **speed**: 7 minutes → 35 gaps without infrastructure setup.

## What This Means

A $0 AI IDE with 50 free credits found 49 coverage gaps across two production frameworks. The gaps were not edge cases — they were core business flows and critical API endpoints.

The lesson is not "AI replaces test engineers." It is "AI audits what test engineers miss." Code review catches logic errors. AI catches coverage gaps.

I still wrote both POMs. I still know what every method and endpoint does. But I no longer trust my own memory to know which ones are tested.

**If you have a test framework — POM, API, or both — run an AI audit. You might be surprised what you missed. Across two projects, I found 49 gaps. How many are in yours?**

---

*Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go*
#TestAutomation #ZeroBudgetQA #GenAItesting #Playwright #CoverageGaps
