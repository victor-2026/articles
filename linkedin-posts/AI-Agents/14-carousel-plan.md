# NotebookLM Scenario: AI User vs AI Builder Carousel

## Instructions for NotebookLM

Generate a 10-slide HTML presentation (1920×1080, dark theme) for LinkedIn carousel. Use the source data below.

## Format Spec

- Dimensions: 1920×1080 px per slide
- Background: Dark (#0d1117) — GitHub Dark theme
- Font: system sans-serif, white text, large sizes
- No emoji on slides
- Each slide is a full-width div with flexbox centering
- Output as a single HTML file with slides stacked vertically (for screenshotting)

## Source Data

### Slide 1 — Cover
Headline: Are You an AI User or an AI Builder?
Subheadline: The 9-Concept Maturity Test
Footer: 10 tools · 4 real codebases · no dedicated test budget · 3 months

### Slide 2 — The Ladder
Headline: My QA Mapping: 9 Concepts, 5 Levels
List (two columns):
Left: L1 AI Consumer (prompts only) · L2 Tool User (MCP) · L3 Builder (agentic loops, subagents)
Right: L4 Target State (AI gateway, inference economics) · L5 Target State (evals, guardrails, observability)
Subheadline: Core skill at every level: Context Engineering
Bottom: "My L1-L5 interpretation — not Barády's original scoring model."

### Slide 3 — L2 · MCP (Tool User)
Headline: Concept 2 — MCP
Definition: One interface to tools: email, repos, DB, browser
Example: Claude Code is a paid CTO daily driver at a project I worked on. MCP connected it to CI/CD, Slack, and Jira without extra integration setup.
Bottom: "The tool was already there. The interface was the unlock."

### Slide 4 — L3 · Agentic Loops + Subagents (Builder)
Headline: Concept 1+3 — Agentic Loops & Subagents
Definition: AI plans → acts → observes → reflects (loops); break big task → parallel → merge (subagents)
Example: Autonoma reached scenarioRecipe (step 4/6) but did not reach the documented confirmation before testGenerator — $3.62 in run/API spend, 0 tests generated. Planner → Generator → Healer fixed two stale snapshots in one session.
Bottom: "The loop is the idea. The feedback loop is the product."

### Slide 5 — L4 Target · AI Gateway
Headline: Concept 4 — AI Gateway
Definition: One control plane: auth, routing, rate limits, logs
Example: No AI gateway was installed. The model switched itself 3 times in one session — 4 models.
Big number: 3 switches, 4 models, 1 session

### Slide 6 — L4 Target · Inference Economics (Infrastructure)
Headline: Concept 5 — Inference Economics
Definition: Every token costs money; caching cuts spend
Example: Same Maintenance task — $3.62 vs $0.19 in run/API cost. Subscription fees and engineering time excluded.
Big numbers: $3.62 vs $0.19
Bottom: "Know your cost per test or you're flying blind."

### Slide 7 — L5 Target · Evals + Guardrails (Quality)
Headline: Concept 6+7 — Evals & Guardrails
Definition: Test outputs against benchmarks before production; filter unsafe input/output
Example: 34/34 mutation checks passed in the covered scope. Mutation testing is an anti-overfit guardrail, not a full AI safety layer.
Big number: 34 / 34
Bottom: "Trust is measured, not assumed."

### Slide 8 — L5 Target · Observability (Operations)
Headline: Concept 8 — Observability
Definition: Traces, logs, metrics for production AI
Example: Allure provides test-run evidence and DORA provides delivery metrics. Model/tool telemetry is a separate layer.
Bottom: "Without it, 'passed' is a claim, not a fact."

### Slide 9 — Core · Context Engineering
Headline: Concept 9 — Context Engineering
Definition: Feed the right context from retrieval, memory, tools
Example: Fit the relevant codebase context into the window — not tokens into the codebase.
Bottom: "The window is fixed. Your context strategy isn't."

### Slide 10 — Verdict + CTA
Headline: The Tools Were Never the Bottleneck
Subheadline: The systems around them were.
CTA: Walk your stack against all 9 concepts → full article in comments
Footer: Which gate is missing: evals, cost controls, or context?
