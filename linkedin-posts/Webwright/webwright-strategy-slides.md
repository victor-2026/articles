---
type: linkedin-post
title: "webwright-strategy-slides"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# Webwright Strategy — Carousel Text

## Slide 1 — Title
**How We Evaluate AI Tools for Test Automation**

30 sessions × 5 models × 600+ calls = 1 strategy

## Slide 2 — The Framework
**5 Dimensions of AI Agent Evaluation for QA**

1. **Code generation** — Playwright or Selenium?
2. **Token consumption** — how much does a step cost?
3. **Stability** — crashes? Loses context?
4. **Model-agnostic** — works with different LLMs?
5. **Real project fit** — POM? Selectors? Timeouts?

Webwright tested across all five.

## Slide 3 — Architecture Win
**Workspace mode — less is more**

Browser mode: screenshot + DOM = ~2500 tok/step
Workspace mode: read files + write code = ~300 tok/step

→ **8x cheaper**
→ No DOM race conditions
→ Agent works like a junior dev, not a user

This is the right architecture for test generation.

## Slide 4 — Model Zoo
**5 models — 5 outcomes**

| Model | Format err | Playwright? | Rate limit |
|-------|:----------:|:-----------:|:----------:|
| deepseek-coder-v2 | 1% | ❌ (Selenium) | No |
| qwen2.5 (temp=0.7) | 33% | ✅ | No |
| qwen2.5 (temp=0.1) | 10% | ✅ | No |
| Groq llama-3.3-70b | 0% | ✅ | 12K TPM |
| qwen2.5-coder:14b | 10% | ✅ | 5 tok/s |

Takeaway: model quality determines output quality. Webwright is a wrapper.

## Slide 5 — Bugs Found
**2 core patches in 30 sessions**

**Bug 1:** `_compact_history()` → `'list' object has no attribute 'strip'`
Multimodal responses = list, code expects a string.
Fix: one type check.

**Bug 2:** `_prune_old_observation_aria_snapshots` → never cleans command_output
Workspace mode → context grows unbounded.
Fix: extended pruning + `keep_last_n_observations: 3`

## Slide 6 — Strategic Takeaway
**Research prototype ≠ production tool**

Webwright on WebArena: **86.67% success rate**
Webwright on OrangeHRM (POM, TypeScript, 12 modules): **1 test in 30 sessions**

The gap between benchmark and real project is an order of magnitude.

**Strategy:**
- Monitor development
- Don't deploy in CI today
- Apply the lessons: workspace mode, custom Modelfile, explicit prompts

## Slide 7 — What's Next
**From evaluation to adoption — roadmap**

**Short-term:** complete contract testing + chaos in Buzzhive to solidify real-world work

**Medium-term:** reassess Webwright in 6 months (v0.2+, core bug fixes)

**Long-term:** build internal agent on stable LLM, borrowing Webwright architecture patterns

## Slide 8 — Resources
**Assets**

Chart 1: `/tmp/webwright_model_comparison.png`
Chart 2: `/tmp/webwright_token_cost.png`
Chart 3: `/tmp/webwright_bugs.png`

**Full report:** `OrangeHRM/outputs/session24-webwright-report.md`
**Carousel spec:** `OrangeHRM/outputs/webwright-carousel-spec.md`
