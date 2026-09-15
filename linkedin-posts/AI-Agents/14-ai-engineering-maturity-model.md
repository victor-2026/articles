**Format:** Pulse Article
**Series:** AI Engineering
**Cover:** L1–L5 maturity ladder graphic — 9 concepts mapped to 5 levels, dark theme, 1200×644
**Feed Image:** Table of 9 concepts × our mostly-free stack equivalent
**Hook:** One Autonoma run cost $3.62 in run/API spend and produced 0 tests. A simpler workflow cost $0.19.
**Based on:** Alex Barády (ENDGAME) — 9 concepts post, Jul 6, 2026. Link: https://www.linkedin.com/posts/alex-bardy_endgame-founder-ai-entrepreneur-executive-activity-7331500856319062016-HJx7

---

<!-- COVER: 14-cover-maturity.png — 9 concepts in 3 layers (Builder / Infrastructure / Quality+Ops), L1–L5 labels -->

# Are You an AI User or an AI Builder? The 9-Concept Maturity Test

One Autonoma run cost **$3.62 in run/API spend** and generated no tests. A simpler workflow completed the same Maintenance task for **$0.19 in run/API spend**. These are execution costs only; subscriptions and engineering time are excluded.

**[Alex Barády](https://www.linkedin.com/posts/alex-bardy_endgame-founder-ai-entrepreneur-executive-activity-7331500856319062016-HJx7), founder of ENDGAME, named 9 concepts that separate the two.** His post defines the concepts, not an L1–L5 scoring system. The ladder and level labels below are my QA-oriented interpretation based on hands-on experiments.

Here's the QA-oriented test.

## The 9 Concepts in One Table

<!-- SCREENSHOT: 14-concepts-table.png — 9 concepts, definitions, maturity levels -->

- **Agentic Loops** — AI plans → acts → observes → reflects, loops until done. **My mapping: Builder (L3).**
- **MCP** — One interface to tools: email, repos, DB, browser. **My mapping: Tool User (L2).**
- **Subagents** — Break a big task into parallel work and merge the results. **My mapping: Builder (L3).**
- **AI Gateway** — One control plane for authentication, routing, rate limits, and logs. **My mapping: Infrastructure target (L4).**
- **Inference Economics** — Every token costs money; caching and model selection reduce spend. **My mapping: Infrastructure target (L4).**
- **Evals** — Test outputs against benchmarks before production. **My mapping: Quality target (L5).**
- **Guardrails** — Constrain unsafe input, output, and actions. **My mapping: Quality target (L5).**
- **Observability** — Traces, logs, and metrics for production AI. **My mapping: Operations target (L5).**
- **Context Engineering** — Feed the right context from retrieval, memory, tools, and history. **My mapping: core skill across levels.**

**Barády's thesis:** "People spend months perfecting prompts and ignore the infrastructure, evaluation, and systems that power real AI products."

That thesis describes exactly where I went wrong for two months. My prompts got prettier. My run still stopped at step 4/6.

## From L1 to L5 — My Maturity Ladder

The nine concepts are not a universal certification. I use them as a gated ladder: claim the highest level for which you can demonstrate every required control.

### L1 — User: Prompting
You write prompts and copy-paste results. No state, tools, or feedback loop. This is a baseline, not one of Barády's nine concepts.

### L2 — Tool User: Single Tool + Scripts
One agent, basic MCP, and shell scripts. The output is useful, but there is no reliable execution-and-check loop yet.

### L3 — Builder: Loops + Subagents
Agentic loops, subagents, and CI/CD integration. The agent can act, observe a result, and revise the work.

### L4 — Builder + Infrastructure: Gateway + Economics
Central routing, rate limits, cost visibility, and caching. This is a target state for my stack, not a capability I currently claim to have reached.

### L5 — Quality + Operations: Evals, Guardrails, Observability
Every change is measured, gated, and traced, with permission boundaries and audit gates. This is the target state for production-grade AI.

## Where My Mostly-Free Stack Sits — and What It Cost to Learn

10 tools/agents, 4 real codebases, and 79 work sessions. The projects were OrangeHRM, Buzzhive, an NDA e-commerce codebase, and FrontRow. I had no dedicated test budget; actual run/API costs are stated per experiment below.

## Agentic Loops — Autonoma stopped at step 4/6

[Autonoma](https://getautonoma.com)'s six-stage pipeline is `pagesFinder → KB → entityAudit → scenarioRecipe → testGenerator → environmentFactory`. The documented workflow pauses before `testGenerator` so a human can confirm the data recipes and scenarios. My run reached `scenarioRecipe` (step 4/6), but I did not reach that confirmation or test generation. It also hit a 274K-token context overflow and timeouts, while the model switched three times across four models without asking. **Run/API spend: $3.62. Tests generated: 0.** The loop is the idea; the feedback loop is the product.

## MCP — Claude Code is a CTO's daily driver

A CTO I work with runs [Claude Code](https://www.anthropic.com/claude-code) every day. It connects CI/CD, Slack, and Jira through MCP and closes the loop: if it breaks something, it fixes it. Claude Code is paid; this workflow had no additional integration setup cost.

## Subagents — Playwright's Planner → Generator → Healer

The best built-in agent pipeline in my test set. [Planner](https://playwright.dev/docs/test-agents) explores and writes a `.md` plan. Generator turns it into `.ts` tests. Healer executes and auto-fixes — it fixed two stale snapshots and improved one test in a single session. Subagents work when each one has a narrow job and a clean handoff.

## AI Gateway — the auto-switch problem

I had no AI gateway installed. The model switched itself three times in one session across four models: `deepseek-v3.2 → moonshotai/kimi-k2.6 → deepseek/v4-pro → openai/gpt-5.4-nano`. **A gateway is a next-step control for routing, limits, and cost visibility — not a capability I claim to have reached.**

## Inference Economics — $3.62 vs $0.19

The same Maintenance task cost $3.62 with Autonoma's pipeline and **$0.19 with a manual KISS workflow**. These are run/API costs only; engineering time and subscriptions are excluded. [Kiro](https://kiro.dev)'s security audit was approximately $0.06 per run in a nightly workflow. Caching and model selection are not optimization details — they determine whether an experiment can become a habit.

## Evals — downstream QA validation is not a model eval

34/34 mutation checks passed in the covered scope. 28/28 contract tests passed. These are **downstream QA validation signals**: they show whether the generated or changed test assets detect selected faults and satisfy contracts. They are not a general model eval for correctness, relevance, or safety. **Evidence turns "I think this test works" into "I measured this behavior in scope."**

## Guardrails — mutation testing is one anti-overfit guardrail

Fault injection and mutation testing protect the test suite from overfit assertions: a surviving mutant is evidence that the test may be too weak. That is an **anti-overfit guardrail for QA**, not a complete AI safety guardrail. A risk-based AI safety layer also needs input and output policy checks, least-privilege tool permissions, sandboxing, secrets and PII controls, human approval for high-impact actions, rate/time/cost limits, audit logs, a kill switch, and adversarial safety evals. The anti-overfit validator I am building follows the [Meta ACH pattern](https://arxiv.org/abs/2501.12862); it is planned work, not current production evidence.

## Observability — Allure and DORA are evidence, not model telemetry

[Allure TestOps](https://qameta.io/allure-testops) provides test-run evidence: results, attachments, traces, and launch history. [DORA](https://dora.dev/) provides delivery metrics such as deployment frequency, lead time, change failure rate, and recovery time. Neither captures the full model/tool runtime.

Model/tool telemetry would include a correlation ID, model/provider/version, prompt-template or input hash, token usage, latency, retries, fallbacks, estimated run cost, tool name, redacted arguments, authorization decisions, tool results, errors, approvals, retrieval sources, and agent state transitions. My current stack has the test-evidence layer; this runtime telemetry is a next-step gap.

## Context Engineering — the skill that underpins everything

Session checkpoints, token budgets, retrieval, and deliberate file selection. My single biggest lever is fitting the relevant codebase context into the window instead of throwing more tokens at the problem. The Autonoma run showed why context engineering is a prerequisite for reliable agent handoffs.

## The 9-Point Test

Mark each item **Yes** only when you can show evidence, not when the capability exists only in a prompt or a plan:

- **Agentic Loops:** Does a failed run observe the failure and retry or escalate?
- **MCP:** Are external tools connected through an authorized interface?
- **Subagents:** Do specialist agents have narrow roles and explicit handoffs?
- **AI Gateway:** Can you route, cap, and audit model usage?
- **Inference Economics:** Can you calculate run/API cost per task or test?
- **Evals:** Do you benchmark model or agent output before shipping?
- **Guardrails:** Are inputs, outputs, tools, and high-impact actions bounded?
- **Observability:** Can you reconstruct model/tool calls, fallbacks, and side effects?
- **Context Engineering:** Can you explain what context entered the run and why?

Use the highest level for which you can demonstrate every gate: L2 means a usable tool and basic integrations; L3 adds a feedback loop and CI execution; L4 adds routing, limits, and cost visibility; L5 adds model/output evals, action guardrails, and runtime telemetry. This is a practical QA rubric, not a universal industry standard.

I started at L2 and moved toward L4 by building the controls in that checklist. The tools were never the bottleneck. The missing controls were.

## From L2 Toward L4 in 4 Moves

1. Add a feedback loop: one agent with `--test-cmd` ([Aider](https://aider.chat)) or a Healer — not the most hyped tool.
2. Gate CI on downstream validation: mutation and contract checks before merge, not after.
3. Install a gateway or equivalent control plane: routing, hard limits, and run/API cost visibility.
4. Add model/tool telemetry and correlate its IDs with Allure launches and DORA delivery events.

Where does your stack sit today — L1, L2, L3, L4, or L5? Tell me which gate is missing.

→ The numbers come from my field report on 10 tools/agents across 4 real codebases: [AI Testing Agents in 2026](https://www.linkedin.com/pulse/ai-testing-agents-2026-3-month-field-report-victor-ematin-s2abe/) and the 7-agent comparison in [I Spent $15 to Test 7 AI Agents](https://www.linkedin.com/pulse/i-spent-15-test-7-ai-agents-0-tool-beat-200mo-tier-victor-ematin-bxcvf/).

Victor Ematin · AI Quality Engineering Lead · No dedicated test budget · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #GenAITesting #ContextEngineering
