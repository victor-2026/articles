---
type: linkedin-post
title: "2-autonoma-deploy"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# I put Autonoma on a PHP app. I chose a Node.js proxy — here's the 4-step fix and the 3 traps I found.

**Format:** Article / LinkedIn Pulse
**Series:** AI Agents for QA (Part 2a)
**Cover:** Autonoma adapter selection — 15 options, PHP (Laravel) highlighted
**Feed Image:** admin users page — 5 seeded users visible in OrangeHRM
**Hook:** "Autonoma's pipeline ran in 10 minutes. The proxy took 30."

---

[COVER: Autonoma adapter selection — 15 backend options, PHP (Laravel) selected, but OrangeHRM uses Symfony]

Autonoma (YC W22, codebase-first AI testing) ran through 7 pipeline steps in 10 minutes: discovered 13 modules, mapped 14 sub-features, proposed seed data for 6 database entities. Then I hit a wall.

The Environment Factory SDK offered 15 adapters — including PHP (Laravel). My app runs on PHP/Symfony, not Laravel. Different ecosystem. I chose TypeScript + Node instead: the test suite is already in TypeScript, Playwright fixtures use the same language, and OrangeHRM's REST API needs nothing more than `fetch`. Pragmatic, not perfect.

You build a standalone server that translates the Autonoma protocol into REST API calls for any stack.

I spent 30 minutes building one. Here's the 4-step playbook.

**🔍 Step 1: Discovery (15 min)**

Curl each endpoint. Test the response. Document the schema. I needed 6 entities: employee (`POST /api/v2/pim/employees`), systemUser (`POST /api/v2/admin/users`), candidate (`POST /api/v2/recruitment/candidates`), leaveRequest (`POST /api/v2/leave/leave-requests`), buzzPost (`POST /api/v2/buzz/posts`), buzzLike. Five worked on the first try. One didn't.

**⚠️ Step 2: Testing — Trap 1 (environment mismatch)**

Autonoma started on the online demo and cached `admin123` as a working credential. When I switched to local mid-pipeline, the same password returned 422 — the local instance enforces password policy (min 7 chars, upper + lower + digit + special). The fix is simple: I added a two-line validator that overrides weak passwords with `Orangehrm@2026`. Lesson: don't let Autonoma discover credentials in one environment and expect them to work in another.

**❌ Trap 2: DELETE format**

OrangeHRM doesn't accept `DELETE /endpoint/{id}`. Returns 405. It expects `DELETE /endpoint` with `{"ids": [id]}` in the request body. Every teardown function needed this pattern. Three entities I initially wrote with URL-path DELETE failed on the first verification cycle.

**🔎 Trap 3: Buzz like endpoint**

Not `/api/v2/buzz/likes` (404). Not `/api/v2/buzz/posts/{id}/likes` (404). Found in minified JavaScript: `/api/v2/buzz/shares/{shareId}/likes`. POST to like, DELETE to unlike. Both return 200.

**🔗 Step 3: Wiring (10 min)**

Connect the proxy to the Autonoma agent. Match the Environment Factory protocol fields. Handle session expiry (OrangeHRM cookies expire after 20 minutes of inactivity — auto-re-login required).

[SCREENSHOT: OrangeHRM admin users page — 5 seeded users across Admin and ESS roles, created in ~30 seconds by the factory]

**✅ Step 4: Verify (5 min)**

UP request creates all 6 entities: 5 employees, 2 users, 3 candidates, 2 buzz posts, 2 likes. ~30 seconds. DOWN request deletes everything in reverse order. 0 orphan records. All 200.

[SCREENSHOT: terminal — factory UP log: employees 88-92 created, users 19-20 created]

**💡 The lesson**

The Environment Factory SDK covers 15+ adapters across 7 languages — but matching your actual stack matters. Laravel adapters won't help a Symfony app. Budget 30-60 minutes for the proxy if your framework isn't on the list. Here's the breakdown: ~15 min endpoint discovery (curl + browser DevTools), ~15 min API edge cases (DELETE format, auth), ~10 min proxy wiring, ~5 min UP/DOWN verification.

Most of that time isn't coding — it's endpoint discovery. Run `curl -I` against each endpoint before writing a single line of proxy code.

And check the minified JavaScript for hidden API routes. The CSS class names won't help you. The compiled JS will.

---

Have you run a testing pipeline on a non-standard stack? Which endpoint tripped you up?

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#Autonoma #TestAutomation #Playwright #AIAgents #OrangeHRM #DevOps
