One agent passed 63% of tasks. After a UI update - 4%. Nobody touched the code.

Meta's OpenApps benchmark (ICLR 2026): 10,000+ evaluations, 7 UI agents, 6 apps with configurable interfaces.

Findings:
→ Reliability within one app version: stable
→ Across app versions: fluctuates >50% for most agents
→ Kimi-VL-3B: 63% -> 4% average success

Interface drift is the new regression. Agent selectors and flows rot exactly like old locators - and teams treat them like a golden environment will hold forever.

If you ship a UI agent, your QA suite needs versioned UI variants, agent evals on every UI release, and failure-mode instrumentation.

The agents write. We verify. That's the verification layer again - from my stack: mutation testing against agent-written tests, regression checklists on every PR, now UI variation testing for agents.

Which of your flows would survive a UI redesign without re-testing?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #GenAITesting #UIAgents