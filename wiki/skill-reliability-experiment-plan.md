# Skill Reliability Experiment — OrangeHRM

**Status:** Planned (postponed)  
**Methodology:** Anton Gulin's Agent Skill Reliability framework (3 runs per condition, programmatic pass/fail)  
**Model under test:** Nemotron 3 Ultra Free (opencode)  
**Target:** OrangeHRM 5.8.1 (Docker, port 8080)

---

## Hypothesis

A skill earns its keep where it teaches the model something it gets wrong on its own.

- `fault-injection` — specific domain patterns (`page.route()`, HOM, `transaction()`) → should show lift
- `rest-api-qa` — general API patterns → unknown (model may already know)
- `bdd-gherkin` — specific syntax + conventions → should show lift (model often breaks Gherkin formatting)

---

## Methodology

### Per-skill protocol

1. **Task** — one concrete, reproducible prompt
2. **Without skill** — general agent, no skill loaded (3 runs)
3. **With skill** — load skill via `skill()` tool, then same prompt (3 runs)
4. **Evaluation** — programmatic checks (compile, syntax validation, test execution)
5. **Score** — pass rate with skill − pass rate without skill

### Scoring

| Lift | Meaning |
|------|---------|
| > 0 | Skill adds measurable reliability |
| 0 | No difference (ceiling — model already knows it) |
| < 0 | Skill confuses the model |

---

## Experiment 1: `fault-injection`

### Task prompt
```
Write a Playwright test for OrangeHRM PIM Employee List.
Use page.route() to intercept the Employee List API response and set
emp_firstname to null for every employee.
Verify the test catches the mutation (expect the test to fail — the UI
should show an error or empty state).
OrangeHRM runs on http://localhost:8080
Credentials: Admin / Orangehrm@2026
Use helpers/credentials.ts for auth setup.
```

### Pass criteria
- [ ] Test is valid TypeScript (compiles with `npx tsc --noEmit`)
- [ ] Uses `page.route()` for API interception
- [ ] Injects `null` into a response field
- [ ] Test fails when run (the mutation is caught)

### Without skill — expected
Model writes generic `page.route()` test, may not understand OrangeHRM API structure.

### With skill — expected
Follows `fault-injection` API checklist: null injection, status code check, UI assertion after mutation.

---

## Experiment 2: `rest-api-qa`

### Task prompt
```
Write a Playwright API test for OrangeHRM auth endpoint.
Test: POST /auth/login with valid credentials returns 200 and a token.
Test: POST /auth/login with invalid password returns 401 and an error message.
OrangeHRM runs on http://localhost:8080
Use API_BASE from helpers/credentials.ts.
```

### Pass criteria
- [ ] Test is valid TypeScript
- [ ] Tests both positive (200) and negative (401) cases
- [ ] Validates response body structure, not just status code
- [ ] Tests pass when run

### Without skill — expected
Model writes basic status code assertions.

### With skill — expected
Follows Buzzhive patterns: token management, schema assertions, error message validation.

---

## Experiment 3: `bdd-gherkin`

### Task prompt
```
Write a Gherkin feature file for OrangeHRM Claim module.
Include:
- Feature with As a / I want / So that
- Background with login state
- Happy path: user submits an expense claim
- Edge case: claim with missing receipt is rejected
- Edge case: claim with amount exceeding limit shows warning
Use proper Gherkin syntax (2-space indent, Given/When/Then order).
```

### Pass criteria
- [ ] Valid Gherkin syntax (`npx gherkin-lint` pass)
- [ ] Feature + Background + Scenario + Scenario Outline
- [ ] Proper Given → When → Then order throughout
- [ ] Domain-level steps (no UI mechanics or SQL in step text)

### Without skill — expected
Model may produce invalid Gherkin, mixed indentation, wrong keyword order.

### With skill — expected
Clean Gherkin with 2-space indent, proper vocabulary, Scenario Outline with Examples table.

---

## Execution plan

### Prerequisites
- [ ] OrangeHRM Docker running (`docker-compose up -d`)
- [ ] `gherkin-lint` installed (`npm install -g gherkin-lint`)
- [ ] Playwright + TypeScript configured
- [ ] `helpers/credentials.ts` has valid credentials

### Run order
```
1. fault-injection — 3 runs no-skill → 3 runs with-skill → score
2. rest-api-qa     — 3 runs no-skill → 3 runs with-skill → score
3. bdd-gherkin     — 3 runs no-skill → 3 runs with-skill → score
```

### Estimated time
- ~12 min per run (Docker + Playwright warmup)
- 18 runs × 12 min = ~3.6 hours total
- ~4-5 hours with evaluation overhead

### Judge
TBD — LLM-as-a-judge (Nemotron 3 Ultra Free) or human review.

---

## Expected results

| Skill | Expected lift | Confidence |
|-------|--------------|------------|
| `fault-injection` | +0.2 to +0.5 | High — specific patterns model rarely uses |
| `rest-api-qa` | +0.0 to +0.2 | Medium — API testing is well-known, but Buzzhive specifics may help |
| `bdd-gherkin` | +0.3 to +0.6 | High — Gherkin formatting is a known LLM weak spot |

---

## Post-Publication

If lift is measurable, the results feed into:
- Article 7: "Do Agent Skills Actually Help? We Measured It"
- `~/.opencode-memory.md` — update skills section with lift data
- Skill files (`SKILL.md`) — add reliability score in metadata

---

**Created:** 2026-06-17  
**Author:** Victor Ematin  
**Status:** ✅ Complete (36 runs, 0% lift, Article 7 published)
