# Article 8: Skills Are Not npm Packages — They're Validators in the Evidence Layer

## Hook

**"Skills are not npm packages. They're not generators. They're validators in the Evidence layer."**

Part 1 showed 36 runs across 2 projects: 0% lift. The experiment failed because we tested skills as *generators*. Anton Gulin's 3-layer architecture explains why — and where skills actually belong.

---

## The 3-Layer Architecture (Anton Gulin)

| Layer | Responsibility | What It Does |
|-------|----------------|--------------|
| **Orchestration** | Risk questions | What to test, what risks matter, what questions to answer |
| **Execution** | CI pipeline | Runs tests, gates deployments, produces artifacts |
| **Evidence** | Traces, screenshots, logs, videos | **Proves** tests are right, not just runnable |

> **"Generation is cheap. Evidence is the architecture."** — Anton Gulin

---

## Where Skills Fit (And Where They Don't)

| Layer | Skills Role | Why |
|-------|-------------|-----|
| **Orchestration** | ❌ No | Risk assessment, strategy — human judgment |
| **Execution** | ⚠️ Partial | Can generate tests, but not the gate itself |
| **Evidence** | ✅ **YES** | Skills = **validators** in the Evidence layer |

**The experiment failed because we tested skills as generators (Execution layer). They belong in Evidence layer as validators.**

---

## What This Means for Skill Design

### ❌ Wrong: Skill as Generator
```
Input: "Write a test for login"
Output: test.spec.ts (code)
Metric: Lines of code / test count
```

### ✅ Right: Skill as Validator
```
Input: test.spec.ts + execution trace + failure mode
Output: PASS/FAIL + specific failure mode explanation
Metric: False positive rate / mutation score / evidence quality
```

---

## The 6 Quality Gates (Evidence Layer)

| Gate | Pass Condition | Skill as Validator |
|------|---------------|-------------------|
| **Scope** | Test maps to one named risk | Skill validates risk coverage |
| **Data** | Test data setup is explicit | Skill validates data isolation |
| **State** | Browser state is controlled | Skill validates state isolation |
| **Run** | Test passes in CI | Skill validates stability |
| **Evidence** | Trace/screenshot/log exists | Skill validates evidence completeness |
| **Review** | Human can explain failure mode | Skill provides failure mode analysis |

**Skills as validators** check these gates automatically. They don't generate tests — they validate that generated tests *pass the gates*.

---

## What Our Experiment Revealed

| Skill | Tested As | Result | Correct Role |
|-------|-----------|--------|--------------|
| fault-injection | Generator | 0% lift | **Validator** (checks mutation score) |
| rest-api-qa | Generator | 0% lift | **Validator** (checks contract/validation coverage) |
| bdd-gherkin | Generator | 0% lift | **Validator** (checks syntax/structure compliance) |

**The 0% lift is not a skill failure. It's a category error.**

---

## How to Redesign Skills (Evidence Layer)

### 1. Input: Test + Execution Context
```typescript
// Instead of: "generate test"
// Skill receives:
{
  testCode: "...",
  trace: "...",
  screenshots: [...],
  failureMode: "...",
  mutationScore: 0.94
}
```

### 2. Output: Validation Result
```typescript
// Skill returns:
{
  scopePass: true,
  dataPass: false,        // ← missing data isolation
  statePass: true,
  runPass: true,
  evidencePass: false,    // ← missing trace
  reviewPass: true,
  failureMode: "Test shares state with previous test — violates isolation gate"
}
```

### 3. Metrics That Matter
- **False positive rate** (not test count)
- **Mutation score** (not lines of code) — Autonoma confirms: AI-generated suites average 20-40% mutation score vs 60-80% human-written. Green means consistency, not correctness.[[1]](#ref1)
- **False negative detection** (not pass rate)
- **Evidence completeness** (traces, screenshots, logs per test)

---

## The Architecture Shift

```
OLD:  Human → Skill (generator) → Test → CI → Deploy
      ↑                                ↑
   Generator                          Gate

NEW:  Human → Generator → Test → CI → Skill (validator) → Evidence → Deploy
                                      ↑              ↑
                                  Validator      Evidence Layer
```

**Skills move from left of CI to right of CI.**

---

## What This Means for You

| If you're... | Do this |
|--------------|---------|
| **Building skills** | Design as validators, not generators. Input = test + evidence. Output = gate pass/fail + failure mode. |
| **Using skills** | Run skills *after* CI, not before. Skills = quality gates, not test generators. |
| **Measuring skills** | Track false positive rate, mutation score, evidence completeness. Not test count. |
| **Designing agents** | Agent = Orchestrator + Generator + Validator. Three roles, not one. |

---

## The Hard Truth

**Your skill library is probably in the wrong layer.**

If your skills output `test.spec.ts` files → they're generators (Execution layer).
If your skills output `gate: PASS/FAIL + failure_mode` → they're validators (Evidence layer).

**The 0% lift in our experiment wasn't a skill failure. It was a layer error.**

---

## Next Steps

1. **Audit your skills**: Which layer is each in?
2. **Redesign as validators**: Input = test + evidence, Output = gate result
3. **Add evidence checks**: Traces, screenshots, mutation score, failure mode
4. **Measure differently**: False positive rate > test count

---

## Tags

#AIAgents #Testing #Playwright #SkillEngineering #QAArchitecture #EvidenceLayer #QualityGates

---

---
## References

<a name="ref1"></a>[1] Tom Piaggio, "Mutation Testing vs Code Coverage: The Real Test-Quality Metric", Autonoma Blog, June 2026. https://getautonoma.com/blog/mutation-testing-vs-code-coverage

Victor Ematin · AI Quality Engineering Lead · OpenCode Go