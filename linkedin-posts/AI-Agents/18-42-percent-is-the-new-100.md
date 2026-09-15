**Format:** Pulse Article
**Series:** AI Engineering
**Cover:** 18-cover-42-percent.png ✅
**Feed Image:** 18-gaia2-table.png ✅
**Hook:** The best agent in the world passes 42% of real-world tasks. The best open-source one: 21%. Everything else is a verification problem.
**Based on:** Gaia2 (Meta, ICLR 2026 oral, arXiv 2602.11964) + SOP-Bench (Amazon, KDD 2026, github.com/amazon-science/sop-bench). Кросс-ссылка на статью 16 (verification layer) и 17 (UI agents).
**Wiki:** ai-qa-wiki/wiki/iclr-2026-agent-benchmarking-self-improvement.md

---

<!-- COVER: 18-cover-42-percent.png - 42% pass@1, GPT-5 vs Kimi-K2 21%, "write-action verifier" -->

# 42% Is the New 100%: What Agent Benchmarks Actually Measure Now

The strongest agent in the world passes 42% of real-world tasks. The strongest open-source agent: 21%. And the most interesting part is not the score - it is what the benchmark measures to get it.

## Gaia2: benchmarks grew up

Meta's Gaia2 (ICLR 2026 oral) abandoned the static benchmark model. Its environments evolve independently of the agent: temporal constraints, noisy events, ambiguity, other agents acting in the same world.

Results across frontier models:

| Model | Score |
|-------|-------|
| GPT-5 (high) | 42% pass@1 - strongest overall, fails time-sensitive tasks |
| Claude-4 Sonnet | trades accuracy and speed for cost |
| Kimi-K2 | 21% pass@1 - best open-source |

## The measurement is the story

Gaia2 pairs every scenario with a write-action verifier: it checks intermediate actions, not just the final answer. GAIA (2023) used exact match on the output. Gaia2 evaluates what the agent did at each step.

That is the same shift QA made years ago: assertions on behavior, not on strings.

## SOP-Bench: agents on business processes

Amazon's SOP-Bench (2,000+ tasks, 12 domains) takes the other direction - real Standard Operating Procedures: healthcare, logistics, finance, content moderation. 10-50+ decision points per procedure. Metrics: ECR (execution completion), TSR (task success), outcome-aware.

Both benchmarks share a thesis:

1. Real environments, not clones
2. Complex multi-step business processes
3. Verification of full interaction with tools, not dialogue-level checks

## What QA takes from this

- **Action-level verification is the design target.** If you evaluate agents, check what they did at each step - not just the final output. This is assertion design for agentic systems.
- **42% is not a failure of models, it is a budget for verification.** If the best agent is wrong 58% of the time, the harness is not a nice-to-have. It is the product.
- **Domain SOPs are test cases.** Amazon encodes business procedures as executable tasks with ground truth. Your QA suite can do the same: turn your own SOPs into agent evaluation scenarios.
- **Cross-check with the UI layer.** OpenApps showed UI agents collapse under interface drift (63% to 4%). Gaia2 shows even the best models cap at 42% in dynamic environments. Combine both: variation-aware, action-level verification - and you have a modern agent QA strategy.

## The takeaway

The industry spent five years chasing benchmark scores. The new benchmarks measure whether an agent survives reality - and nobody does. That gap is not a model problem. It is a harness problem: write-action verifiers, domain SOPs, UI variation testing. The QA leader who builds that harness owns the only thing that makes agents shippable.

What does your agent evaluation check - the output, or the actions?

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #ZeroBudgetQA #GenAITesting #AgentBenchmarks