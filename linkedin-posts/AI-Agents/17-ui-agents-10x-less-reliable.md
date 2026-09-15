**Format:** Pulse Article
**Series:** AI Engineering
**Cover:** 17-cover-ui-agents.png ✅
**Feed Image:** 17-openapps-drop.png ✅
**Hook:** Один агент проходил 63% задач. После обновления интерфейса - 4%. Никто не трогал код.
**Based on:** OpenApps (Ullrich et al., Meta, ICLR 2026) - 10,000+ эвалюаций, 7 мультимодальных агентов, 6 приложений с конфигурируемым UI. Кросс-ссылка на статью 16 (verification layer).
**Wiki:** ai-qa-wiki/wiki/iclr-2026-agent-benchmarking-self-improvement.md

---

<!-- COVER: 17-cover-ui-agents.png - 63% -> 4% drop, "UI drift kills UI agents" -->

# Your UI Agent Is 10x Less Reliable Than You Think

One agent passed 63% of tasks. After an interface update - 4%. Nobody touched the code.

That is not a bug report. That is the headline finding of OpenApps, a Meta benchmark from ICLR 2026 that asked a question QA has been asking for years: what happens to an autonomous UI agent when the interface changes?

## The experiment

Meta built six configurable apps (messenger, calendar, maps, and others) that can change appearance and content. Then they ran 10,000+ independent evaluations across seven leading multimodal agents - and compared reliability within a fixed app version against reliability across versions.

## What the numbers say:

| Metric | Value |
|--------|-------|
| Reliability within one app version | Relatively stable |
| Reliability across app versions | Fluctuates >50% for most agents |
| Worst case (Kimi-VL-3B) | 63% -> 4% average success |

The 63% to 4% collapse was not an outlier. Most agents swung by more than half their success rate purely because the environment configuration changed.

## Why this is a QA problem

Three findings that map directly to testing:

1. **Interface drift is the new regression.** Your agent's selectors, flows, and screens are test assets - and they rot exactly like old locators rot. The UI agents community has no equivalent of visual regression testing, and OpenApps shows why they need one.
2. **Loops and hallucinated actions are environment-dependent.** The same agent loops or invents actions in one config and behaves in another. You cannot certify an agent against one environment snapshot and expect it to hold.
3. **"Stable" is a lie without variation.** Fixed-environment benchmarks overstate reliability. OpenApps measured the difference: it is not 5%. It is often more than 50%.

## What this means for teams shipping UI agents

- **Test across variations, not just happy paths.** If you ship an agent that clicks through your product, your QA suite needs versioned UI variants, not one golden environment.
- **Re-run agent evals on every UI release.** Treat the agent as a first-class consumer of your UI changes - exactly like an end user, but with a much larger blast radius.
- **Instrument failure modes.** Track where the agent loops or hallucinates an action. Those are your flaky tests in agent form - and they are far more expensive.
- **This is the verification layer again.** From my stack: mutation testing against agent-written tests, LLM-generated regression checklists on every PR, and now - UI variation testing for agents. The pattern is always the same: the agents write, we verify.

## The uncomfortable question

If a 5% interface change drops a 63% agent to 4%, what happens when your agent meets your users' devices, browsers, and screen sizes? The answer is not "train a better model". It is "build a better verification harness" - and that is a QA design decision.

Which of your flows would survive a UI redesign without re-testing?

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #ZeroBudgetQA #GenAITesting #UIAgents