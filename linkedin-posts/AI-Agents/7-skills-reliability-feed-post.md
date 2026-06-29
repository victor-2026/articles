I ran 36 controlled tests across 2 projects with AI. Result: 0% lift. 🧪

3 skills × 2 conditions × 3 runs × 2 projects = 36 runs. 0% lift.

Projects:
- OrangeHRM (PHP/jQuery, form-based, legacy)
- Buzzhive (React/TypeScript, REST API, modern)

Skills tested:
1. fault-injection (null injection via page.route)
2. rest-api-qa (API testing best practices)
3. bdd-gherkin (Gherkin syntax/structure)

Result: 36 runs, 36 passes, 0% lift. 📊

The mutation wasn't a bug on either stack:
- OrangeHRM (PHP) handles null gracefully
- Buzzhive (React) handles null gracefully
Both systems are resilient by design.

rest-api-qa and bdd-gherkin: base model already knows these patterns cold.

Skills ≠ correctness boost on known patterns.
They give: consistency, vocabulary, hygiene, onboarding.
But if model knows the pattern, skill = style guide, not capability unlock.

Next experiment: test skills where model fails (contract testing, mutation infra, OAuth, financial rules, chaos).

Don't ask "does skill help?" — ask "where does model fail without skill?" 🎯

Part 2 coming: Anton Gulin's 3-layer architecture — skills as validators, not generators.

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIAgents #Testing #Playwright #SkillEngineering #Experiment

