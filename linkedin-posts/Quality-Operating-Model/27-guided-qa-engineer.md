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
- **Evidence:** Andrew Ng AI Engineering Skills Map (ingested 2026-08-28); Michael Bolton systems-thinking post (2026-08-28 - "bottles have necks", perturb-the-system); Article 16 (Productivity Paradox / verification layer); Article 20 (5 bugs / 4 imaginary - false-discovery); Article 26 (break the testing tool on purpose - QAEverest pilot); Megi Tephnadze pilot (risk-based human gate, ProCredit Bank Georgia).
- **CTA:** «The agent writes the test. You write the reason it should fail. Which one of those did your last hire req list as the core skill?»
- **Carousel angle (optional):** 6 slides - "Full-stack engineer → guided full-stack engineer" / "QA → guided QA engineer" / "Humans: why / Agents: how" / "Testing stayed on the fundamentals list" / "Verify, don't trust" / "The role promoted, not deleted".

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
