**Format:** Pulse Article
**Series:** AI-Agents (Article 10)
**Cover:** A split screenshot — left side: Antigravity login_test.go with the "admni123" typo highlighted, right side: Go test tree showing 8 files. Title reads "Antigravity vs OpenCode Go"
**Feed Image:** Same image, 1200×644 crop
**Screenshots:**
  - Cover: `10-cover.png`
  - Code typo (section 6): `10-code-typo.png`
  - Race bugs table (section 7): `10-race-bugs-table.png`
  - Comparison table (section 10): `10-comparison-table.png`
  - Go test tree (section 11): `10-go-tree.png`
**Hook:** "I gave two unknown AI agents the same prompt — one wrote 5 tests and found a race bug in 2 hours"

---

# I Let Antigravity vs OpenCode Go Write Tests for the Same API — One Found a Bug in 2 Hours

[COVER: Split screenshot — Antigravity login_test.go with admni123 typo on left / OpenCode Go test tree on right]

It started with a typo.

I was setting up an experiment: give a fresh AI agent unlimited access to a codebase and see what it produces. The prompt was simple — "write all possible login tests for the admin user." The model was unknown, the context was clean, the budget was zero.

What happened next revealed more about AI testing than I expected.

**Antigravity (unknown model, clean sheet, 2 days): 5 Go tests + race bug + Docker fix in 48 hours. OpenCode Go (gpt-4o-mini, 40+ sessions, $10 flat): 49 tests across 8 files with infrastructure layer. Same target. Different depth. Both found race bugs the other missed.**

Here is the full breakdown of what each agent delivered, what broke, and what that taught me about AI-generated test suites.

## The Setup

The target was Buzzhive — a FastAPI + React sandbox with 2,917 lines of TypeScript API tests as the source of truth. The goal was to migrate those tests to Go, using either Playwright Go or net/http.

Two agents received the same task:

- **Antigravity** — unknown model, brand-new macOS profile, cloned repo into `/Users/Shared/`, 48-hour free trial
- **OpenCode Go** — gpt-4o-mini, $10 flat rate, 40+ sessions of context in the same project, worked in `/Users/victor/`

The setup was asymmetrical by design. One agent had zero context. The other had months of history. I wanted to see which mattered more: fresh eyes or institutional knowledge.

## What Antigravity Delivered in 48 Hours

One file. Five test functions. Ten test cases.

`login_test.go` (188 lines) covered the critical login paths:
- Valid credentials → dashboard redirect + localStorage token
- Wrong password → 401 + error message
- Invalid email → 401
- HTML5 email validation — browser-level rejection
- SQL injection — 4 payloads table-driven (`' OR '1'='1`, `admin'--`, `' OR 1=1--`, `'; DROP TABLE users;--`)

The code quality was solid: a reusable `runTestWithPage` helper, HTTP response logging, `networkidle` waits, proper `assert` vs `require` usage, nil-safety checks. For a clean-sheet agent with no prior context, this was impressive.

But the real discovery was non-functional. Antigravity found a race condition — a separate bug from the known refresh token race (which OpenCode had documented weeks earlier). The details are lost because the 48-hour trial expired without a trace.

And then there was the Docker fix. Antigravity read the nginx.conf, spotted a duplicate `location "/api"` block, and corrected it — something no human had flagged in weeks of development.

## What OpenCode Go Built Over 40 Sessions

Eight files. Forty-nine tests. Infrastructure.

OpenCode Go produced:
- `auth_test.go` (8 tests) — login, register, refresh, me endpoints
- `auth_security_test.go` (19 tests) — refresh token validation, invalid tokens, empty body, edge cases
- `posts_test.go` (4 tests), `users_test.go` (6 tests), `follows_test.go` (5 tests) — CRUD + relationships
- `race_test.go` (2 tests) — 10 goroutines parallel login + 5+5 follow/unfollow
- `client.go` — base URL config, retry logic, auth header injection
- `helpers.go` — random data generation, cleanup, assertions

The key difference was **infrastructure**. OpenCode Go built a test framework, not just test cases. `client.go` meant every new API test started with 30 lines of working setup. `helpers.go` meant cleanup was automated. `warmup_test.go` meant CI failures would surface connection issues before the test suite ran.

## The Bug That Shouldn't Have Existed: "admni123"

This is my favourite part — and the most embarrassing.

When I typed the admin password during the Antigravity experiment, I made a typo: `admni123` instead of `admin123`. Antigravity used my input verbatim. The test still passed.

Why? Because the frontend proxied API calls to Render (http://buzzhive-test.onrender.com), which redirected http to https with a **307 status code**. Playwright's `ExpectResponse` intercepted the 307 **before** the backend ever checked the credentials. The test asserted `status in [200, 307]` — green across the board.

**I made a typo. Antigravity trusted my input. The 307 masked the 401. Both of us missed it.**

The lesson: HTTP status code assertions are not enough. Every login test should verify:
- URL redirects to the dashboard (or stays on `/login` on failure)
- localStorage contains `access_token` (or is empty)
- UI elements are visible (nav-profile or error message)

[SCREENSHOT: 10-code-typo.png — The admni123 typo in login_test.go with the 307/401 callout]

## Race Bugs — Independent Validation

Diversity in testing approaches finds bugs a single perspective misses.

[SCREENSHOT: 10-race-bugs-table.png — 4 race bugs with Found By and Status columns]

Two different AI tools, working independently, found different race bugs in the same codebase. Antigravity found one I still cannot reproduce (trial expired). OpenCode Go found two I now have on record. Neither set of findings invalidates the other — they validate the methodology.

## Context > Model

The most practical takeaway from this experiment:

**Antigravity (clean sheet) found the Docker bug in 2 minutes** — because it read nginx.conf without assumptions. It had no history, no habits, no "this is how we always do it." It just read the config and spotted the duplicate.

**OpenCode Go (40 sessions) found 4 race conditions** — because it knew what had broken before. It had documented the refresh token race, understood the concurrency patterns, and wrote `race_test.go` targeting the same weak points.

Fresh eyes catch what familiarity misses. Experience catches what first impressions overlook. The optimal setup is both — but most teams only have one.

## The Numbers

[SCREENSHOT: 10-comparison-table.png — Antigravity vs OpenCode Go, 7 metrics]

## What This Means for AI-Generated Tests

1. **Never trust the first green run.** If a test passes but the credentials are wrong — your assertion layer is too shallow
2. **Diversity in AI tooling beats consistency.** Two agents found different bugs in the same API. Use more than one approach
3. **Infrastructure wins over test count.** 49 tests with `client.go` are worth more than 49 standalone tests. The framework is the asset
4. **Context is a double-edged sword.** Experience prevents rookie mistakes but also breeds blind spots. Rotate tools, not just people

[SCREENSHOT: 10-go-tree.png — Full Go test infrastructure tree: api/, cmd/, client.go, helpers.go]

## Try It Yourself

The code is open source at github.com/victor-2026/qa-automation-playwright. The Go tests live in `go-backend/api/`. The Antigravity `login_test.go` is in `go-backend/cmd/api-tests/`.

Have you compared two AI tools on the same testing task? What did each find that the other missed?

---

Victor Ematin · QA Automation Engineer · $0 budget · OpenCode Go

#TestAutomation #GoLang #AITesting #GenAItesting #ZeroBudgetQA
