---
type: linkedin-post
title: "3-webwright-strategy-post"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

I ran 30 sessions of AI agents writing Playwright tests — 600+ API calls, 5 models, 2 bugs patched in the framework itself.

1 working test to show for it 🧪

What the numbers say:
→ Workspace mode: 300 tok/step vs 2500 for browser (8x cheaper)
→ Format errors: 33% → 10% with custom Modelfile (temp 0.1)
→ deepseek-coder: 1% errors but generated Selenium instead of Playwright 🔄
→ GPU offload <50%: structured JSON breaks on every local model

The framework needs maturing — but the real bottleneck for local AI testing is GPU capacity for structured output.

Would I use this in production today? Not yet.
Would I bet on agent-generated tests for next year's CI? Yes — if the ecosystem keeps maturing 📈

What's your experience with AI-generated test code? Works or too fragile?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#Webwright #AITesting #TestAutomation #Playwright #QA
