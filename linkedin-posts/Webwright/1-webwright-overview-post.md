---
type: linkedin-post
title: "1-webwright-overview-post"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

🧠 5 takeaways from Webwright — Microsoft Research's minimal browser agent (~1,000 lines total) — that changed how I think about browser automation.

$2.37 per automation asset. GPT-5.4 authors a reusable CLI tool for $2.37. Pay the reasoning tax once. Run at near-zero cost forever. That number changed what I thought "expensive" automation meant.

The common thread? Less is more — fewer lines, fewer clicks, fewer dependencies.

**1,000 lines is enough.** Runner (150), Model bridge (550), Terminal sandbox (300). The harness stops being the bottleneck.

**Stop clicking, start coding.** Stateless DOM-clickers guess coordinates. Webwright writes Python scripts. The browser is a disposable workspace — the script is the artifact.

**Self-reflection beats retries.** Before emitting done:true, the agent runs the script, catches the traceback, fixes imports, then retries in a fresh directory. Terminal stack traces > blind retries.

**Less framework = better results.** 86.67% SOTA on Online-Mind2Web. 60.1% on Odysseys (+35%). Claude Opus wins hard tasks (80.5% vs 76.6%).

📄 Full breakdown in the carousel below 👇

Testing Webwright this week. The next post covers what breaks — and what surprised me. Want a reality check? Like 👍 and I'll share what I find.

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIAgents #Webwright #MicrosoftResearch #TestAutomation #SoftwareEngineering
