---
type: linkedin-post
title: "3-orangehrm-local-deployment-carousel"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

## Slide 1 — Title
[PHOTO: Server tower or desktop PC]

**Building a Local OrangeHRM: One Docker Saga**

My home server wasn't built for containers. I made it work anyway.

---

## Slide 2 — The Problem
[VISUAL: Split screen — left side shows shared demo login (opensource-demo.orangehrmlive.com), right side shows a failing test result with "Add user — FAILED"]

**25 unique tests, 15 smoke — but 3 destructive ones blocked:**

- Add user — data conflict with other sessions
- Add employee — same conflict
- Create buzz post — demo blocks creation

2 more skipped (Claim module missing). Not failing because my code is wrong.

---

## Slide 3 — The Hardware
[PHOTO: Desktop PC tower]

**A workstation, not a server:**

- AMD Threadripper X399
- 64 GB RAM
- Windows 10 Pro
- Never designed for containers

Docker Desktop — 19 minute engine timeout. WSL 2 backend can't initialize on this chipset.

---

## Slide 4 — Fix Chain
[VISUAL: 5-step flowchart as horizontal boxes with arrows]

BIOS SVM Mode → WSL 1 → WSL 2 → docker.io → OrangeHRM

**Step by step:**
1. `BIOS M.I.T. → Advanced CPU Settings → SVM Mode: Enabled`
2. Ubuntu WSL 1 → WSL 2 conversion
3. Docker Desktop uninstalled
4. `sudo apt install docker.io` (Moby engine, no Desktop)
5. `docker compose up` — OrangeHRM 5.4 + MariaDB 10.11.4

---

## Slide 5 — Architecture
[DETAILED DESCRIPTION: Connection flow — MacBook → SSH tunnel (port 8080) → Windows Server → WSL 2 Ubuntu → Docker containers]

**How it connects:**

MacBook → SSH tunnel (8080) → WSL 2 Ubuntu → Docker: OrangeHRM + MariaDB

SSH tunnel: `ssh -L 8080:xxx.xxx.xxx.xxx:8080 user@xxx.xxx.xxx.xxx`

---

## Slide 6 — Dual-Target Config
[VISUAL: Code snippet of playwright.config.ts with highlight on baseURL ternary, and a table of 3 projects]

```typescript
baseURL: process.env.LOCAL === 'true'
  ? 'http://localhost:8080'
  : 'https://opensource-demo.orangehrmlive.com'
```

| Project | Runs | Tests |
|---------|------|-------|
| smoke | everywhere | 15 smoke |
| chromium | CI / demo | all except @local |
| local | LOCAL=true | all 28 |

Just set `LOCAL=true` — one variable controls everything.

---

## Slide 7 — Before / After
[VISUAL: Table comparison — 3 tests listed with red ❌ before and green ✅ after]

| Test | Shared demo | Local |
|------|:-----------:|:-----:|
| Add user (ADMIN-002) | ❌ data conflict | ✅ isolated |
| Add employee (PIM-002) | ❌ data conflict | ✅ isolated |
| Create post (BUZZ-002) | ❌ demo blocks | ✅ passes |

Total: 25 tests on shared demo → 28 tests on local (3 destructive now pass).

---

## Slide 8 — The Cost

**4 hours of Docker troubleshooting**

**1 BIOS setting**

**1 SSH tunnel**

**20 lines of dual-target config**

**Destructive tests that actually pass.**

---

What's the weirdest infrastructure fix you've had to make?
