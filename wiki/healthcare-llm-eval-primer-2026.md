# Healthcare LLM Eval Primer (arXiv 2609.14819, 2026)

- **Source:** McKinney et al., submitted 2026-09-13 — [arXiv:2609.14819](https://arxiv.org/abs/2609.14819) (digest 2026-09-15, abstract verified)
- **Structure (4 blocks):** (1) principles of study design; (2) statistical methods; (3) capability evaluation — MCQ, agentic, multi-turn benchmarks + operational metrics (token usage); (4) clinical context evaluation — free-text accuracy via human review, LLM-as-a-judge, clinical trial approaches.
- **Key rule:** align evaluation method with the research question; pitfalls in every block (probabilistic open-ended outputs, prompt/context shift).
- **Why it matters here:** кросс-доменное подтверждение per-risk-tier логики — клиника = наш B0 (strict gate, human review обязателен); MCQ-бенчи = B2 (trend). Разделение "capability vs context eval" ложится на mutation matrix: heal-check (capability) vs ambiguity-flag (context). LLM-as-a-judge с питфоллами — аргумент за independent oracle вместо self-grading (ср. Klain Confidently Incorrect: checker trusted the thing it checked).
- **Routing:** per-risk-tier framework + VerdictGate methodology (`ai-qa-wiki/outputs/product-concept-mutation-verifier-mvp.md`); ссылка-кандидат в first comment Article 27 (evals-слой).
- **Status:** abstract-level. Full PDF not reviewed.
