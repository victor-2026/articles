---
type: linkedin-post
title: "qa-metrics-dashboard"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# QA → DORA mapping: my pipeline hit Elite on 2 of 4. Dashboard inside.

**Format:** Article / LinkedIn Pulse
**Series:** Side Projects
**Cover:** dora-dashboard.png — Grafana DORA Core dashboard with 4 panels
**Hook:** "Mutation caught = Change Failure Rate. Flaky count = Reliability. 48h → 4h regression = Lead Time."

---

[COVER: Grafana DORA Core dashboard — 4 panels showing CFR, CI/CD stability, lead time, MTTR]

My QA pipeline hit Elite on 2 of 4 DORA metrics. Change Failure Rate: 0% (34/34 mutations caught). MTTR: immediate (1-line fixes). Here's the mapping and the Grafana dashboards.

I connected my two QA projects — Buzzhive (~300 tests, ~1,100 runs estimated) and OrangeHRM (29 tests, 33 of 51 planned) — to the DORA framework. The results put my pipeline at Elite level on two metrics. Here's what I mapped and how.

**The mapping**

[SCREENSHOT: DORA-to-QA mapping table — 4 metrics with QA equivalents, data, and Elite/High levels]
<!-- TODO: Replace with dora-mapping-table.png (1920x1080) -->

| DORA Metric | QA Equivalent | My Data | Level |
|------------|--------------|---------|:---:|
| **Change Failure Rate** | Mutations caught / total | 34/34 = 0% | **Elite** |
| **CI/CD Stability** | Pipeline pass rate + waitForTimeout | ~78%→~94% (estimated, per CV), 40+ → 0 flaky | **High** |
| **Lead Time for Changes** | Regression execution time | 3 days → 4 hours (Wimark, per my resume) | **High→Elite** |
| **MTTR** | Time to fix flaky test root cause | 1-line fix, immediate | **Elite** |

The trick: mutation testing IS change failure detection. When you inject 34 faults into your system and catch all 34, your failure rate is zero. Every mutation that escapes is a production bug you wouldn't have caught. This isn't theoretical — DORA's Change Failure Rate measures exactly this: what percentage of changes cause failure. Catching 100% of injected failures = 0% real failure rate.

This approach scales. The same DORA-for-QA mapping was proposed for a company with 4,500+ microservices and 300+ engineering teams. If it works at that scale, it works for a two-project portfolio.

**Five dashboards, one Grafana instance**

I built the visual layer in Grafana with the Infinity plugin — no external database, just JSON files. The setup cost 3 hours of debugging (CORS, Docker DNS, one missing `"type": "time"` column), but the result is five dashboards with embedded data:

[SCREENSHOT: Five Grafana dashboards — DORA Core, OrangeHRM Coverage, Buzzhive Test Health, Buzzhive Quality Gates, AI Agent Effectiveness]
<!-- TODO: Replace with grafana-dashboards-table.png (1920x1080) -->

| Dashboard | Signal |
|-----------|--------|
| 🟡 DORA Core | CFR, CI/CD stability, lead time — Elite audit |
| 🟠 OrangeHRM Coverage | 20%→65% over 1 week |
| 🔵 Buzzhive Test Health | ~78%→~94% pass rate (estimated), 40+ waitForTimeout → 0 flaky |
| 🟢 Buzzhive Quality Gates | Mutation 34/34, Contract 28/28 |
| 🔴 AI Agent Effectiveness | KISS Sorcar ($0.01) vs Webwright ($2.37) |

**Why this matters**

When a CTO or QA Director asks "how do you measure quality?" — most candidates list tools. Playwright. Selenium. Jira. A dashboard with DORA levels answers the question differently: "Here's my pipeline's Change Failure Rate. Here's my lead time. Here's how to read the levels."

The key insight from industry deployments: metrics must be actionable. Mutation score isn't just a number — when a mutation escapes, the team knows exactly which test to add. That's what makes DORA different from traditional QA scorecards that aggregate signals without giving teams a path to improve.

The configuration is in `qa-automation-sandbox/monitoring/`. All dashboards are self-contained in Grafana with inline JSON — no Prometheus, no external services.

How do you measure your test pipeline's effectiveness — CI/CD pass rate, or something closer to DORA?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#DORA #TestAutomation #Grafana #QAEngineering #AIAgents
