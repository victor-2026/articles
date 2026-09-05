**Format:** Pulse Article
**Series:** Quality-Operating-Model
**Cover:** [COVER: Guided QA engineer - risk-based gate table + CCN inflection at agent adoption, guided vs typing split]
**Feed Image:** [SCREENSHOT: Guided QA - humans give why, agents give how]
**Hook:** How do you keep QA relevant when an agent writes 80% of the tests?

---

# 27 — The Guided QA Engineer: Why AI Promotes the Tester Instead of Replacing Them

**Headline options:**
1. **Curiosity Gap:** The Agent Writes the Tests. You Write Why They Should Fail.
2. **Direct Benefit:** The Guided QA Engineer: How to Stay Relevant When AI Writes 80% of Your Tests
3. **Contrarian:** QA Didn't Get Replaced. It Got Promoted.

How do you keep QA relevant when an agent writes 80% of the tests? Same way a senior engineer stays relevant when an agent writes 80% of the code: you stop doing the typing and start doing the steering.

**B1: 3/3 mutants caught - 100%** - our QAEverest pilot after the fix. A green AI-generated suite is an unverified claim until you break something on purpose.

[SCREENSHOT: risk-based gate - survival rate × risk → human gate effort (High 0 / Medium 5% / Low trend)]

<!-- COVER: 27-cover-guided.png — guided QA engineer steering AI agents, why vs how split, mutation matrix gate in background -->

## Skeleton → 4-Section Draft (Problem → Solution → Implementation → Result)

### Problem
Agentic coding created the "guided full-stack engineer" - someone who steers AI with fundamentals instead of writing every line (Andrew Ng, AI Engineering Skills Map). QA got the same upgrade: agents now write the test code, but no one steers the quality criteria. Teams ship green suites that never proved they can catch a break.

### Solution
The role didn't shrink - it promoted. Ng's split is "humans give the why, agents give the how." For QA that means you supply what "good" means, where the risk lives, and whether the suite catches anything - the agent supplies the assertions. Testing is still on Ng's fundamentals list (Security & Reliability: test strategy, shift-left, AI-driven scanning) - agents assist, they don't absolve.

### Implementation
I ran it as: (a) specify risk-based gates (strong for high-risk, light for low - Megi's ProCredit pilot), (b) write the constraints the agent can't infer, (c) run mutation checks as the independent oracle (QAEverest pilot B1 3/3 100% after fix), (d) own the human sign-off.

**Before → After (Ng-style steering prompt):**

Before (agent guesses): `Write a test for the cache.`

After (you steer):

```
Test the read-through cache with TTL ≤5min.
- Invalidate on write-through to the DB.
- Assert staleness < TTL at the boundary (cache → DB), not just the UI.
- Verify with a mutation: flip TTL to 10min and watch it fail.
```

The agent now can't infer the TTL trade-off - you supplied the why. Same for data model, boundary, and risk gate.

[SCREENSHOT: risk-based gate table - survival rate × risk → effort, Megi example]

### Result
"Verify what the agent generated" (Ng) + survival-rate check (Article 20/26): a green suite is an unverified claim until you break something on purpose. The guided QA engineer turns a green report into a trusted release - execution down, judgment up.

- **Hook (kept):** "Andrew Ng says agentic coding created the 'guided full-stack engineer' - someone who steers AI with fundamentals instead of writing every line. QA got the same upgrade. The question is whether you noticed."
- **Evidence:** [Andrew Ng AI Engineering Skills Map](https://x.com/AndrewYNg/status/2088302050706686198) ([The Batch #366](https://www.deeplearning.ai/the-batch/issue-366) / [Part 2: Software Engineering Fundamentals](https://www.explainx.ai/blog/andrew-ng-software-engineering-fundamentals-agentic-coding-august-2026)) (ingested 2026-08-28); [Michael Bolton](https://developsense.com/about-michael-bolton) systems-thinking (Rapid Software Testing co-creator) - "bottles have necks" as gatekeeper metaphor, perturb-the-system ([DevelopSense](https://developsense.com)); Article 16 (Productivity Paradox / verification layer); Article 20 (5 bugs / 4 imaginary - false-discovery); Article 26 (break the testing tool on purpose - QAEverest pilot B1 100% 3/3); [Zalando Agentic Engineering snapshot 2026-08-14](https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html) (risk-based PR bot 33% auto-approve, CCN inflection); Megi Tephnadze pilot (risk-based human gate, ProCredit Bank Georgia).
- **CTA (one, actionable):** The agent writes the test. You write the reason it should fail. Which one did your last hire req list as the core skill?
- **Carousel angle (optional):** 6 slides 1080x1350 4:5 - "Full-stack engineer → guided full-stack engineer" / "QA → guided QA engineer" / "Humans: why / Agents: how" / "Testing stayed on the fundamentals list" / "Verify, don't trust" / "The role promoted, not deleted" - last slide © Victor Ematin · AI Quality Engineering Lead · OpenCode Go

---
Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#TestAutomation #ZeroBudgetQA #GenAItesting #Playwright #QATips #QualityEngineering #AITesting

## What to develop further

- **Concrete before/after:** a real test-spec written as constraints (Ng-style prompt: "use read-through cache TTL ≤ 5 min") vs the same test hand-authored. Shows the steering skill is new, not gone.
  - **Tie to Article 21 (Conway):** quality ownership delegates the same way - the guided QA engineer delegates execution but keeps the boundary and theevidence.
  - **Tie to Zalando (2026 snapshot):** their risk-based PR approval bot is a live per-risk-tier gate, and the CCN inflection at agent adoption is empirical evidence for the "verify, don't trust" thesis. Wiki: `wiki/zalando-agentic-engineering-snapshot-2026.md`.
- **Risk-based gate table** from the mutation matrix Full template: map survival rate × risk → human gate effort. This is the operational "guided" part.
- **Bolton metaphor - "bottles have necks":** the human gate is not a bottleneck to remove, it is the neck that regulates AI output into something observable and manageable. Quote-ready: "This is why wine doesn't come to your table in a bucket." Use as the lead visual/anchor for the QA-as-gatekeeper section.
- **Counter-argument to pre-empt:** "but the agent also writes the constraints via SKILL.md / context" - answer: the agent encodes your stated intent, it doesn't discover the trade-off you forgot to state. That gap is the job.

## Raw threads to fold in (draft later)

- **QA-as-quality-gatekeeper.** The operational layer is concrete: the risk-based gate table from Mutation Matrix Full (survival rate × risk → human gate effort). This IS the "guided" part - you don't author the tests, you set the gates. The gatekeeper owns the threshold, not the test code. Tie to Megi's pilot (strong gate high-risk / light low-risk) as the worked example. Anchor metaphor: Bolton's "bottles have necks" - the gate is regulation, not obstruction.
- **QA-as-supervisor (recent framing).** The "supervisor" angle: the QA engineer orchestrates multiple AI agents (test-gen, exec, review) the way a supervisor orchestrates a team - assigns, checks, escalates. Distinct from "gatekeeper" (decision authority) vs "supervisor" (orchestration). Pick one as the headline, use the other as supporting.
- **Karpathy "manifesting" verb.** Karpathy used "manifesting" as a verb - developing manifests/specs for AI agents (the explicit intent the agent executes against). Maps directly to the QA role: the QA engineer "manifests" the quality criteria, the agent "implements" them. Good linguistic hook - "you don't write the test, you manifest the spec." Note: verify exact Karpathy quote/source before publishing.
- **Bach / RST "Testing vs Checking" (Prachi Dahibhate profile, 2026).** Cleanest one-liner for the gatekeeper thread: "The agent performs the checks. The QA engineer performs the testing." Bach's "magic testing box" + "What's not here?" + The James Bach Test (7 questions before trusting an AI report) = the evaluation rubric behind the gate. Directly supports Article 20/26 and the Mutation Matrix verdict column.
- **Andrew Ng "Loop Engineering" (2026).** Highest-authority proof of the promoted-role thesis: Ng states developers "were acting as the QA function... now make higher-level product decisions." The three loops (agentic coding / engineering / developer-feedback) = the nested verification layers; the human owns the outer loop. Pair with Krivitsky's nested Agentic Factory (Coding→Feature→Impact) as the visual scaffold. Ng's "evals" = the mutation matrix, stated by an AI founder.

## Open questions before writing the body

- Headline role word: guided QA engineer / QA-as-gatekeeper / QA-as-supervisor - which leads?
- Do we need Karpathy source citation, or keep it as a cultural nod?
- Does this replace or extend Article 24 (Quality Operating Model)?

## Примечание (обсудить)
- Добавить ссылку: Eval-driven development как главный trait (Ng, gyn5e, 21.08) — прямо mutation matrix + evidence layer; цитата для Article 26/27: https://www.linkedin.com/pulse/ai-engineering-skills-map-building-deploying-applications-andrew-ng-gyn5e

## Rogue-линия 04-05.09 — тройной кейс verify-don't-trust (обсудить включение)
- Эпизод 1 (04.09): swarm OpenAI-агентов вышел в открытый интернет без ведома лаборатории — https://techcrunch.com/2026/09/04/another-swarm-of-openai-agents-reached-the-open-internet-without-the-frontier-labs-knowledge/
- Эпизод 2 (04.09): rogue-агенты используют немецкую wiki как message board — https://www.theverge.com/ai-artificial-intelligence/990149/openai-rogue-agents-german-wiki + https://collusion.wiki/
- Эпизод 3 (05.09): 3 700 агентов обсудили 18 000 сообщений о способах обхода ограничений — https://arstechnica.com/security/2026/09/openai-agents-discussed-ways-to-escape-their-sandbox-on-public-wiki/
- Тезис для Result: неконтролируемый агент пишет код/тесты, которых никто не верифицировал, — guided-инженер и есть тот, кто ставит gate между генерацией и релизом.
- Вопрос дозировки: тройка целиком раздует тело — вариант: в body лестница одной строкой (swarm → backchannel → escape talk), детали в карусель/первый коммент. Решить до финализации body.
