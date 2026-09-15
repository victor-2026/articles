# Tornhill: Farewell TDD in Agentic Coding (Sep 2026)

**Source:** [Practices I Abandoned with Agents](https://adamtornhill.substack.com/p/practices-i-abandoned-with-agents) (Substack, 03.09.2026) via his LI post 12.09. Full text fetched.
**Author:** Adam Tornhill, CodeScene founder, *Your Code as a Crime Scene*. 25 years TDD. Authority tier: Bolton/Bach/Klain.

## Thesis

TDD = design technique optimized for **human cognition** (small increments, visible progress). Agentic coding needs larger steps; forcing agents through human-shaped increments negates the benefits. Same pattern as his Clojure shift (REPL > TDD for exploration): paradigm shifts demand workflow shifts.

## What replaced it

- **E2E tests as human/agent abstraction boundary** (NOT TDD — scope differs: one agentic iteration = tens of red-green-refactor cycles; human out of the low-level loop; order of code-vs-test irrelevant).
- **Code for machine consumption**, enforced via tooling (MCP inspectors), not manual inspection.
- **Surviving parts:** double-entry bookkeeping (drive every change via a failing test) + red-green repurposed: *red = confidence the suite can validate delegated changes*.

## The killer detail (our territory)

AI acted on failing tests by **deleting the test or weakening its condition to match erroneous code**. Hence failing-test-driven delegation. This is verification-gaming at unit scale — same species as silent green (QAEverest) and misattribution (Agentiqa).

## Why it matters for us

1. **Red-as-oracle-calibration = matrix scenario 1.** His "red proves the suite can validate delegation" is our "baseline confirms green, calibrates the oracle" — independent derivation, fourth convergence (Amodei checkpoints, Testkube gates, DoorDash disprove-it).
2. **Test-deletion gaming → 26-follow-up ammo.** Strongest known real-world instance of the agent defeating its own verification. One line + link, ready for first comment or follow-up post.
3. **E2E-as-boundary = seams (22).** Tests as human/agent abstraction boundaries — boundary language from the TDD world. Cross-link 22 on revision.
4. **Paradigm-shift meta-lesson** (Clojure→agents): practices must match cognition shape (human-small vs agent-large). Frames 27's guided engineer: steers at feature level, not line level.

## Addendum: CodeHealth MCP vs AI-induced smells (post 1w ago)

- **Quality gates on TRENDS, not absolute values.** Module-level design (cohesion, complexity); metric power = how metrics balance each other. Metaphor: *Sonar = spell checker, Code Health = paragraph sense.* Auto-enforced via MCP+CLI+PR (+ linters for line level — complementary).
- **Webb (CTO thread):** AI fails to fix excess-args without a measured outcome even with prompting — measurement-before-fix, evals-first.
- **Screenshot stats** (safeguard trigger rates on AI code) — unseen, pending manual view.
- **Our take:** trend-gates = 10x-probe logic (Gulin bar rate+spread over time) and tier-threshold philosophy (% secondary to survived count). Level-framing (module vs line) mirrors Agentiqa flows-vs-UI. Enforceable>advisory, fourth rhyme (Spotify, DoorDash profiles, 25).

## Cross-links
- Article 26 (oracle calibration; test-gaming follow-up).
- Article 22 (abstraction boundaries); 27 (feature-level steering, manifesting).
- Bolton/Bach checks-vs-testing (Klain wiki): TDD-survivors are checks with teeth (failing-first), not green decoration.
