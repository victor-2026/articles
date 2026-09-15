**Format:** Pulse Article
**Series:** DS/ML for QA (Article 1)
**Hook:** "Everyone tests ML models in Python. I used Go. Here's what I found — including a NaN bug in the first 30 lines."

<!-- COVER: 11-cover.png — Go test tree: 4 test levels + terminal output with 11 tests PASS in 0.03s -->

# Everyone Tests ML in Python. I Used Go. Here's What I Found.

I was preparing for a Test Lead role at Avito — Russia's largest classifieds platform. Their systems run on ML models that allocate liquidity across millions of listings. I needed to understand how to test those models.

The default choice would be Python: pandas, scikit-learn, pytest. Everyone in DS/ML uses Python.

I chose Go instead.

**377 lines of Go code, 11 test functions across 4 testing levels. And a NaN bug caught by the very first invariant — before it ever reached production.**

Here is the four-layer framework I built, why Go worked better than Python for this specific problem, and the bug I would have missed without PBT.

<!-- Money Paragraph -->

1. The Problem: Testing a Non-Deterministic System

Traditional QA works with deterministic assertions. Click button, expect 200. Submit form, expect redirect.

ML models don't work that way. The same input can produce slightly different outputs after retraining. A "bug" in ML is not a crash — it's a gradual degradation in quality that might go unnoticed for weeks.

Testing a liquidity allocation algorithm requires four levels of validation, not one.

2. Level 1: Property-Based Tests — The Invariants

Before testing what the model does, test what it must never violate.

I wrote four invariants for the allocation algorithm:

- **All shares sum to 1.0** — you cannot allocate more or less than 100% of liquidity
- **No negative shares** — a listing cannot receive negative allocation
- **Total allocation = total liquidity** — no money disappears
- **Higher rating = higher share** — the model must respect its own ranking

These ran in under a millisecond. They caught the NaN bug immediately.

3. Level 2: The A/B Gate

Before releasing a new model version, you need statistical evidence that it's better than the current one, not just different.

The A/B gate simulates two models competing over N iterations:

better, pValue := SimulateABTest(currentModel, experimentModel, 1000)
if !better {
    // Block deployment — new model isn't proven better
}

The rule: if the experiment doesn't win at least 55% of simulated comparisons, it doesn't ship. This prevents releasing changes that are "different but not better."

4. Level 3: Drift Detection

Models degrade in production. Data drift (input distributions change), concept drift (the relationship between inputs and outputs changes), upstream drift (the data pipeline breaks silently).

The implementation uses PSI (Population Stability Index) — a statistical measure of distribution shift:

psi, drifted := DetectDrift(baselineDist, currentDist)
if drifted {
    // Trigger alert, initiate rollback
}

PSI greater than 0.1 signals significant drift. The test validates both directions: same distributions pass, shifted distributions fail.

<!-- SCREENSHOT: 11-drift-test.png — ВСТАВИТЬ PNG: PSI comparison, same distribution PSI≈0.01 (PASS green), shifted PSI≈0.5 (FAIL red) -->

5. Level 4: The Golden Dataset

The final safety net. A fixed set of hand-verified examples with expected outputs.

This runs as a nightly CI job. If the model's output on the golden dataset deviates beyond a threshold, deployment is blocked. No exceptions.

6. The NaN Bug

The first PBT test failed immediately.

score := ad.Rating * (1 + ad.History) / float64(ad.Priority)

When all weights are zero — zero rating, zero history, zero priority — Go's float64 division produces NaN (Not a Number). NaN is not less than or equal to zero, so the totalWeight less-than-or-equal-to-zero fallback guard doesn't trigger. NaN propagates silently into every allocation.

Traditional unit tests with hand-picked inputs would miss this. Property-based tests with invariants catch it every time.

The fix was a single line:

if math.IsNaN(totalWeight) || totalWeight <= 0 {
    // Equal distribution fallback
}

One invariant. One bug. Zero production incidents.

<!-- SCREENSHOT: 11-nan-diff.png — ВСТАВИТЬ PNG: Before (red) / After (green) NaN fix code comparison -->

7. Why Go Instead of Python?

Three reasons:

- **Same stack as integration tests** — the Go allocator sits alongside API tests in the same CI pipeline. No context switching.
- **Compiled = fast CI** — 11 tests in 0.03 seconds. No dependency installation, no virtualenv.
- **Type system catches interface bugs** — structs make invalid states unrepresentable. Python dataclasses don't enforce this at compile time.

This doesn't mean "Python is bad for ML testing." It means: if your infrastructure is in Go, test your ML components in Go.

The Numbers

<!-- SCREENSHOT: 11-level-table.png — ВСТАВИТЬ PNG: таблица 4 уровней тестирования (PBT, A/B Gate, Drift, Golden Dataset) -->

Total: 377 lines of Go, 11 tests, 0.03 seconds.

What a Test Lead Should Know

Every ML model needs four layers of protection:

1. **Invariants** — what must never be true
2. **Gates** — proof that new is better than current
3. **Drift detection** — automatic alert when production changes
4. **Golden dataset** — regression baseline that never changes

Build these before the first model ships. Backport them to existing models. Your DS team will thank you.

---

The code is open-source: [github.com/victor-2026/ai-qa-wiki/tree/main/code/ds-ml-testing-go](https://github.com/victor-2026/ai-qa-wiki/tree/main/code/ds-ml-testing-go)

Do you test ML models in your stack? What level are you missing?

Victor Ematin · QA Lead · $0 budget · OpenCode Go

#GoLang #MLTesting #DataScience #QAAutomation #PropertyBasedTesting