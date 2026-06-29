---
type: linkedin-post
title: "2-webwright-limitations-post"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

Webwright: 86.67% state-of-the-art with ~1K lines of code. 8 limitations that decide viability for your stack.

⚠️ Microsoft's "terminal-first" agent hits state-of-the-art on Online-Mind2Web and Odysseys (+35% over previous). But real adoption blockers matter more than benchmarks:

🔴 Premature "done." Self-reflection gate is mandatory — agent must verify in fresh directory before emitting done:true.

🔴 Context ceiling. 20-step compaction loses cross-page reasoning. On Odysseys (100-step tasks): GPT-5.4 reaches 60.1%.

🔴 Script debt. Generated scripts are reusable RPA-style. UI changes kill them silently — requires dedicated validation cycles.

🔴 Granularity dilemma. Micro-routines (reliable, hard to manage) vs monoliths (comprehensive, fragile). No winner yet.

🔴 Model ceiling. GPT-5.4 dominates easy tasks (96.2%). Claude Opus wins hard tasks (80.5% vs 76.6%). Your ceiling = your model choice.

🔴 Environment limits. Canvas, legacy frames, obfuscated UIs force pixel fallback — losing 10x DOM-based speed.

🔴 TCO amortization. One-time AI generation ($2.37 for GPT or $6.09 for Claude per script) → near-zero per run after validation. The more regression passes, the lower the cost per test.

🔴 Predictability vs resilience. Traditional automation is brittle but deterministic. Webwright is resilient but harder to audit.

📄 Each limitation visualized in the carousel below 👇

❓ Which one hits your stack hardest?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#Webwright #AITesting #TestAutomation #Playwright #QA
