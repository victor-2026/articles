# 27 — The Guided QA Engineer: Why AI Promotes the Tester Instead of Replacing Them

How do you keep QA relevant when an agent writes 80% of the tests? Same way a senior engineer stays relevant when an agent writes 80% of the code: you stop doing the typing and start doing the steering.

## Skeleton

- **Hook:** «Andrew Ng says agentic coding created the 'guided full-stack engineer' - someone who steers AI with fundamentals instead of writing every line. QA got the same upgrade. The question is whether you noticed.»
- **Body:**
  1. **Ng's split: humans give the 'why', agents give the 'how'.** In his AI Engineering Skills Map, core SE fundamentals (architecture, data, security, reliability, scaling) are what let you steer an agent toward the right trade-offs. For QA this is the same move: you supply the quality criteria, the agent supplies the test code.
  2. **The role didn't shrink - it promoted.** Ng's "guided full-stack engineer" maps cleanly to a "guided QA engineer": not the person who authors every assertion, but the person who specifies what 'good' means, where the risk lives, and whether the generated suite actually catches anything. Execution moved down; judgment moved up.
  3. **Testing is still on Ng's fundamentals list - agents assist, they don't absolve.** His Security & Reliability row lists test strategy (unit/integration/coverage), shift-left, AI-driven scanning. Agents can scaffold it, but you need a test-aware prompt. The QA engineer becomes the one who writes that prompt and verifies the output.
  4. **'You must verify what the agent generated' - Ng said it, the mutation matrix proves it.** Ng: agents help generate scripts but you must verify them. That is exactly the survival-rate argument from Article 20/26: a green AI-generated suite is an unverified claim until you break something on purpose and watch it catch the break.
  5. **What the guided QA engineer actually does now:** (a) specify risk-based gates (strong gate for high-risk, light for low - Megi's model), (b) write the constraints the agent can't infer (TTL, data model, boundary), (c) run mutation checks as the independent oracle, (d) own the human sign-off that turns a green report into a trusted release.
- **Evidence:** Andrew Ng AI Engineering Skills Map (ingested 2026-08-28); Article 16 (Productivity Paradox / verification layer); Article 20 (5 bugs / 4 imaginary - false-discovery); Article 26 (break the testing tool on purpose - QAEverest pilot); Megi Tephnadze pilot (risk-based human gate, ProCredit Bank Georgia).
- **CTA:** «The agent writes the test. You write the reason it should fail. Which one of those did your last hire req list as the core skill?»
- **Carousel angle (optional):** 6 slides - "Full-stack engineer → guided full-stack engineer" / "QA → guided QA engineer" / "Humans: why / Agents: how" / "Testing stayed on the fundamentals list" / "Verify, don't trust" / "The role promoted, not deleted".

## What to develop further

- **Concrete before/after:** a real test-spec written as constraints (Ng-style prompt: "use read-through cache TTL ≤ 5 min") vs the same test hand-authored. Shows the steering skill is new, not gone.
- **Tie to Article 21 (Conway):** quality ownership delegates the same way - the guided QA engineer delegates execution but keeps the boundary and theevidence.
- **Risk-based gate table** from the mutation matrix Full template: map survival rate × risk → human gate effort. This is the operational "guided" part.
- **Counter-argument to pre-empt:** "but the agent also writes the constraints via SKILL.md / context" - answer: the agent encodes your stated intent, it doesn't discover the trade-off you forgot to state. That gap is the job.
