# Quotes Bank — цитаты с ссылками для новых статей

Подвал идей: чужие формулировки, которые можно цитировать (со ссылкой на автора). Правило: цитата попадает сюда только с URL источника и пометкой предлагаемого использования. Не свалка — по одной строке смысла на цитату.

---

## Displacement / QA reshuffled

- «QA is getting reshuffled by AI faster than almost any part of software engineering right now». — Philip Lew, CEO XBOSoft (20 years in software quality). Source: LinkedIn post 2026-09-15 (PNSQC $99 Community Passes announcement). Use: контекстная строка про скорость вытеснения в launch-материалах VerdictGate / attestation-статьях.

## Evals vs Tests / Verification Gates

- «An evaluation asks "how good is this?" A test asks "does this specific thing still work?"». — Anubhav Singhmaar, TestMu AI. Source: testmuai.com/blog/llm-evaluation-vs-agent-testing/ (2026-09-13). Use: Article 26/27 — eval≠gate, per-risk-tier framing.
- «Can an agent pass an eval and still be broken? Routinely. The most common version is an agent that produces a well-formed, accurate-sounding answer while calling the wrong tool or no tool at all.» — TestMu AI. Source: same. Use: Article 26 — silent false negative case.
- «A score of 0.87 does not tell a build server anything, because nobody wrote down which side of 0.87 is shippable.» — TestMu AI. Source: same. Use: Article 27 — why "confidence" ≠ "evidence".

## Agent Coding / Human-Machine Boundary

- «Forcing an agent through increments optimized for human cognition negates many of the benefits.» — Adam Tornhill, Founder CodeScene. Source: adamtornhill.substack.com/p/practices-i-abandoned-with-agents (2026-09-03). Use: Article 27 — why TDD-era QA patterns don't transfer to agentic coding.
- «Code is no longer for my consumption. The machine is the primary audience. I had to accept that.» — Adam Tornhill. Source: same. Use: Article 27 — QA role shifts from reading code to governing evidence.
- «In TDD, red verified that I had implementation work to do. With agents, red gives me confidence that my test suite is capable of validating the changes I delegate to agents.» — Adam Tornhill. Source: same. Use: Article 27 — verification semantics shift.
- «Tooling enforces what you don't inspect.» — Adam Tornhill. Source: same. Use: Article 22/27 — automated governance, not manual review.

## AI Safety / Market vs Regulation

- «Safety is an engineering problem, not a legal one.» — Jensen Huang, NVIDIA CEO (Dreamforce 2026). Source: LinkedIn post by Linas Beliūnas (2026-09-17). Use: external framing for Article 27 — both sides of debate.
- «Market forces do NOT optimize for safety. Everyone is taking big risks because they believe a tiger is chasing them.» — James Bach. Source: LinkedIn comment on Jensen Huang post (2026-09-17). Use: Article 27 — why market alone fails, need structured gates.
- «If you FEEL that things are out of control, that doesn't work in an environment where everyone is taking big risks.» — James Bach. Source: same. Use: "feeling safe" ≠ "being safe" — evidence-based verification.

## Compliance / Attestation

- «For a FINRA member firm, agent output is a communication with the public. Duties attach to what a firm distributes, not how it was produced.» — Brian Corkery, TestMu AI. Source: testmuai.com/blog/finance-ai-agent-compliance-testing/ (2026-09-14). Use: Article 27 — real-world attestation pattern (FINRA Rule 2210).
- «Classification is an INPUT, not an output. Two runs of one scenario can produce byte-identical text and still land in different categories.» — TestMu AI. Source: same. Use: per-risk-tier — deployment context determines obligations.

## Market Signals / Vendor Landscape

- «95% accuracy sounds impressive. But is it enough to put an AI agent in production?» — ContextQA (poll). Source: LinkedIn post (2026-09). Use: Article 27 — market validates per-risk-tier framing.

## Independence / Attestation

- «The author can't be the examiner.» — Daniel Mauno Pettersson (QA tech), via Joe Colantonio (TestGuild). Source: LinkedIn post 2026-09-17 (TestGuild Webinar replay). Use: Article 27 — core attestation principle, independence of verification. Also: Tornhill double-entry, mutation testing thesis.
- «An agent writes a PR for you for, let's say, $5 in tokens. How much should you spend checking that it works? 5 cents? $5? $50? My thinking is it depends on what the PR touches.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-09-03. Use: Article 27 — cost-ratio verification, per-risk-tier (critical code = more verification, cosmetic = less).
- «The pattern I've taken from watching dozens of customers is where verification sits in the org. When QA is a stage before release, you scale it linearly with people or scripts, and you hit a wall.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-05-22. Use: Article 27 — verification as continuous flow, not gate. QA-as-stage = old model.
- «Prompt quality lives in one person's head and you cannot review it. Harness configuration is a file. Version it, diff it, enforce it across everyone.» — Dhruv Bansal (Technology Leader), summarizing Anthropic engineer on Claude Code agentic loop. Source: LinkedIn post 2026-09-11. Use: Article 27 — governance = harness config (versionable), not prompting skill (unreviewable). Also: AGENTS.md pattern, Tornhill tooling enforcement.
