---
type: linkedin-post
title: "3-orangehrm-local-deployment"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# 3 — OrangeHRM Local Deployment

---

Docker Desktop failed. BIOS had to be reconfigured. Here's how I deployed OrangeHRM locally.

While building Phase 2, I hit a wall: 25 tests passed on shared demo, but 3 destructive ones needed a real server — add user, add employee, create buzz post all failed on data conflicts. I needed a local instance.

What should have been "docker compose up" turned into a saga.

The hardware: Windows 10 Pro on a home server. AMD Threadripper X399, 64GB RAM. A workstation never designed for containers.

First attempt: Docker Desktop. Engine started timing out after 19 minutes. WSL 2 backend couldn't initialize — a known issue on this chipset.

The fix chain:

1. BIOS → SVM Mode enabled (M.I.T. → Frequency → Advanced CPU Settings → SVM)
2. Ubuntu WSL 1 → WSL 2 (required after BIOS change)
3. Docker Desktop uninstalled → sudo apt install docker.io directly in WSL 2
4. OrangeHRM 5.4 + MariaDB 10.11.4 via docker-compose
5. Installer: 6 green steps, but password policy needed Admin#123 → MoreSecure#123
6. wget the deployment-runbook from GitHub

The networking puzzle:

▸ localhost:8080 inside WSL — works
▸ localhost:8080 from Windows browser — doesn't (WSL 2 limitation)
▸ WSL direct IP 172.xxx.xxx.xxx:8080 — works
▸ 192.168.1.xxx:8080 via netsh portproxy — unstable

The SSH tunnel (from MacBook):

`ssh -L 8080:172.xxx.xxx.xxx:8080 User@10.xxx.xxx.xxx`

Now I can run Playwright tests from my MacBook against the Windows server. Then all destructive tests pass.

Dual-target configuration — three projects:

▸ smoke — /@smoke/ — runs everywhere
▸ chromium — excludes @local — CI and demo
▸ local — /@local/ — LOCAL=true only

The result:

▸ 3 destructive tests converted from "expected fail" to pass
▸ Full suite: 28 tests on local vs 25 on shared demo
▸ 15 smoke tests — every environment
▸ Zero config changes between environments — just LOCAL=true

What this cost me: 4 hours of Docker troubleshooting. 1 BIOS setting. 1 SSH tunnel. 20 lines of config.

What I gained: Destructive tests that actually pass. No more wondering if a failure is my code or the demo resetting at 3am.

Have you ever had to fight infrastructure just to run a docker compose up? What was the weirdest fix?

Victor Ematin + AI Quality Engineering Lead + OpenCode Agents
