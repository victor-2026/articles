The strongest agent in the world passes 42% of real-world tasks. The best open-source one: 21%.

Meta's Gaia2 (ICLR 2026): environments that evolve independently of the agent - temporal constraints, noise, ambiguity.

GPT-5 (high): 42% pass@1 - fails time-sensitive tasks
Kimi-K2: 21% - best open-source

The measurement is the story: Gaia2 checks intermediate actions with a write-action verifier, not just the final output. The same shift QA made years ago - assertions on behavior, not on strings.

Amazon's SOP-Bench adds the other dimension: 2,000+ tasks from real Standard Operating Procedures across 12 domains (healthcare, logistics, finance). Metrics: execution completion, task success, outcome-aware.

42% is not a model failure. It is a verification budget. If the best agent is wrong 58% of the time, the harness is the product.

Action-level verification. Domain SOPs as test cases. UI variation testing. That is modern agent QA - and the QA leader who builds the harness owns what makes agents shippable.

What does your agent evaluation check - the output, or the actions?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #GenAITesting #AgentBenchmarks