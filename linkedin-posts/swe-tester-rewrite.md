---
type: linkedin-post
title: "swe-tester-rewrite"
date: 2026-06-14
format: post
series: ""
status: published
impressions: 0
engagement: 0
tags: []
---

# SWE-Tester: I tested an AI that reproduces GitHub issues — 41,000 examples, 3 models, surprising results

**Rewrite — replaces original (May 23, 0% engagement, 13d old)**
**Format:** Post / LinkedIn Feed

---

I tested SWE-Tester — an open-source framework that trains LLMs to reproduce GitHub issues from text. I ran it against 3 real bugs from my own projects.

41,000 training examples from real PRs, 2,600 repos. Qwen-2.5-Coder beat the baseline by 21% on change coverage, 10% on error reproduction.

The framework uses a two-stage workflow: first it localizes defective code, then edits test files.

**What worked:**
- 21% better change coverage vs baseline models
- 10% improvement in error reproduction
- Qwen-2.5-Coder performed best among open models

**What didn't:**
- Multi-file bugs still need human judgment
- Vague issue descriptions → vague tests

SWE-Tester is a triage tool, not a test engineering replacement. But 41K real-PR examples make me optimistic about AI-assisted debugging in 2026-2027.

Did you try SWE-Tester or similar frameworks? What model did you pair it with?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#SWETester #MASpipeline #TestingAI #AITesting #GenAItesting
