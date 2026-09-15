# Notes: "Everyone Tests ML in Python. I Used Go."

## To Improve (Jul 7 — plan for this week)

1. **Add section: "When Python still wins"** — balanced view. Python ecosystem (hypothesis PBT, scikit-learn, pandas fixtures) vs Go (same-stack, fast CI). Not Go > Python, but "right tool for your infra."

2. **Expand A/B Gate section** — add:
   - p-value threshold explanation (why 0.05?)
   - Why 55% win rate = pragmatic choice, not 95% confidence
   - Sample size requirements (1000 iterations — how was this chosen?)

3. **Comparison table: Go vs Python** — concrete metrics:
   - CI time (Go: 0.03s vs Python: ? with venv/deps)
   - Maintenance complexity
   - Ecosystem maturity for ML testing

4. **Consider:** add a "Level 0: Data Quality" before PBT — validate input data before it reaches the model (schema, nulls, ranges). DS teams spend 60% of time on data prep.

## Strong Points (keep as-is)
- NaN bug hook — best opener
- 4-level framework (memorable, quotable)
- Go choice creates narrative tension
- Direct relevance to Avito case
