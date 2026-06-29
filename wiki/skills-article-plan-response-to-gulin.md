# Plan: Article "Skills Are Not npm Packages"

**Format:** LinkedIn Pulse Article  
**Series:** AI Agents  
**Response to:** Anton Gulin's skill-creator (eval-driven skill development as npm packages)

---

## The Gap

Gulin's model: skill-creator → eval → optimize → deploy. Skills as npm packages with external evaluation.

What it misses:
- No fallback for **lean judgement** — when the model is its own judge (big-pickle evaluating big-pickle)
- No **AGENTS.md + boundaries** — skills need project-level rules, not just SKILL.md
- No **stop-rules** (from Hack'n'Vibe's RULES.md) — what NOT to do is more valuable than what to do
- No **self-evaluation embedded in the skill** — 4 axes: correctness, relevance, stability, coverage
- No **BDD harness** (from Rinat) — skills should produce executable specs, not just suggestions

## Thesis

**A skill that can't self-evaluate is a guess.** Gulin's eval-driven approach assumes an external judge. Most teams don't have one. Skills need built-in reliability measurement.

---

## Outline

### Hook (personal)
"I used Anton Gulin's skill-creator. It works — until you need to evaluate with the only model you have. Same model evaluating same skill. That's when I had to flip the problem."

### Money paragraph (2nd)
9 stop-rules, 4 reliability axes, 8 skills with embedded self-evaluation, and one uncomfortable finding: skills help most where you thought you didn't need them.

### Section 1 — What Gulin Gets Right
- Eval-driven development is the right idea
- skill-creator pipeline (create → eval → optimize → deploy) is solid
- Skills as shareable packages is the right ecosystem vision
- Credit: his 3-Layer Architecture (Orchestration → Execution → Evidence) is our foundation too

### Section 2 — Where the Model Breaks
**The lean judgement problem:**
- Gulin's eval assumes an external judge (another LLM, human, test suite)
- In practice: you're using the same model (big-pickle) to evaluate its own skill output
- `[SCREENSHOT: example of model praising its own output]`
- Result: inflated scores, false confidence

**The structure gap:**
- Gulin's skill-creator generates SKILL.md only
- We found skills need: AGENTS.md (project rules) + boundaries table + stop-rules
- Hack'n'Vibe's RULES.md: 9 stop-rules prevent 4 classes of failures that do-rules couldn't catch
- `[TABLE: SKILL.md vs AGENTS.md + boundaries + stop-rules]`

### Section 3 — 4-Axis Self-Evaluation
Instead of external judge, embed reliability measurement inside the skill:

| Axis | What It Measures | Pass/Fail |
|------|-----------------|-----------|
| **Correctness** | Does the output compile/pass? | Compiler, test run |
| **Relevance** | Does it address the actual task? | Checklist match |
| **Stability** | Same output given same input? | 3-run variance |
| **Coverage** | Does it handle edge cases? | Required patterns |

- Each skill evaluates itself after generation
- No external judge needed
- Works with any model, including the one running it

### Section 4 — BDD Harness as the Validation Layer
**From Rinat:** BDD with Given-When-Then is the natural validation layer for skills.

- A skill shouldn't just tell you the answer — it should produce an **executable spec**
- Our `bdd-gherkin` skill generates feature files that can be run as tests
- If the spec contradicts the code → build fails, not "let's audit"
- `[SCREENSHOT: failing build because BDD spec detected drift]`

### Section 5 — The Real Delta: Skills as Agent Behavior Design
**From Proka4:** "QA мышление — это проектирование поведения агентов. Та же мышца, с другой стороны."

- Gulin treats skills as **code generation packages**
- We treat skills as **agent behavior blueprints**
- A skill defines: what decisions the agent makes, what it asks, when it stops
- Example: `fault-injection` skill doesn't just generate a mutation test — it tells the agent when to intercept API vs UI vs DB
- `[TABLE: Gulin's model (code-output) vs our model (behavior-output)]`

### Section 6 — Results from 8 Skills
| Skill | Axes | Stop-rules | Self-eval pass | Without skill | With skill |
|-------|------|-----------|----------------|---------------|------------|
| fault-injection | 4/4 | 3 | ✅ | .2 | .5 |
| bdd-gherkin | 4/4 | 2 | ✅ | .3 | .6 |
| rest-api-qa | 4/4 | 1 | ✅ | .6 | .7 |

*(Estimated — pending skill-lift experiment)*

### CTA
"Which evaluation model works for your team? External judge, or built-in self-evaluation? Try both and tell me what breaks."

---

## Headline Options

1. **Contrarian:** "Skills Are Not npm Packages — 8 Skills Later, I Learned What Anton Gulin's Model Misses"
2. **Curiosity Gap:** "Anton Gulin Said Skills Should Be Eval-Driven. I Tried It With No External Judge."
3. **Direct Benefit:** "How to Build Skills That Measure Their Own Reliability (Without Expensive LLM Judges)"

---

## Visuals Needed
- `[COVER: Two paths diagram — Gulin's eval-driven pipeline vs our self-evaluating skill structure]`
- `[SCREENSHOT: self-evaluation output from bdd-gherkin skill — 4 axes pass/fail]`
- `[SCREENSHOT: failing build because BDD harness detected spec drift]`
- `[TABLE: SKILL.md vs AGENTS.md + boundaries + stop-rules]`
- `[TABLE: Gulin's code-output model vs our behavior-output model]`

---

## Key Numbers
- 8 skills with embedded self-evaluation
- 4 reliability axes (correctness, relevance, stability, coverage)
- 9 stop-rules from RULES.md pattern
- Estimated lift: +0.2 to +0.6 per skill
- Gulin's 3-Layer model → foundation
- Our delta: self-evaluation + stop-rules + BDD harness

---

## References
- Anton Gulin: [opencode-skill-creator](https://github.com/antongulin/opencode-skill-creator)
- Hack'n'Vibe: RULES.md — stop-rules pattern
- Rinat Abdullin: BDD > SDD as AI-Native Harness
- Alexey Proka4: "QA мышление = проектирование поведения агентов"
- Our skills: `~/.config/opencode/skills/` (8 skills)
