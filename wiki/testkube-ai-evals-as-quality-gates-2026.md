# Testkube: AI Evals as Quality Gates (Aug 2026)

**Source:** [How to Integrate AI Testing in Delivery Pipelines](https://testkube.io/blog/how-to-integrate-ai-testing-delivery-pipelines) (Testkube blog, Sarvani Yallapragada, 18.08.2026) via Rudolf Groetz post 11.09
**Related:** [Using AI for Quality Gates](https://testkube.io/blog/) (26.08: reasonable prompt change tanks faithfulness, zero broken tests) · [Testing AI Systems Across All Four Layers](https://testkube.io/blog/) (28.08)

## Thesis

Deterministic CI/CD can't ship AI: same input ≠ same output. Passing unit tests no longer means shippable. Pipelines need an **eval layer** — faithfulness, recall, relevancy, safety, latency — with thresholds AS the gates: pre-merge evals, deployment gates, continuous post-deploy (shadow testing, scheduled benchmarks).

## Killer demo (their words, our logic)

Baseline vs candidate prompt on same 20 questions. Candidate adds *"Draw from your general knowledge in addition to the provided context"* → Faithfulness tanks (hallucination), Relevancy tanks (verbose, off-topic). Gate blocks; AI agent opens fix PR. **This is mutation matrix for prompts**: same probe set, one injected change, oracle = thresholds. Silent green for prompts, caught by gate.

## Gate stages

1. **Pre-merge:** prompt regression, RAG eval, response quality, safety, model comparison — on PR.
2. **Deployment:** thresholds must hold (their demo: Faithfulness ≥0.80, Recall ≥0.75, Relevancy ≥0.80) before staging/prod.
3. **Post-deploy:** shadow testing (prod traffic vs new prompt, no user impact) + scheduled benchmarks (catch model/embedding drift without releases).

## Tool landscape (pointer, not catalog)

- Eval frameworks: DeepEval (CI-oriented), Ragas (RAG), LangSmith (LangChain trace/compare), OpenAI Evals (custom benches).
- Observability: Langfuse, Arize Phoenix, W&B.
- Orchestration: GH Actions, Argo, Tekton; Testkube = K8s-native runner (TestWorkflows CRDs, Influx metrics via ai-metrics-parser, Insights dashboard, agent remediation).

## Why it matters for us

1. **Independent derivation of per-risk-tier gates.** Their "deployment progresses only if faithful/relevant/safe" = our B-gate shape (thresholds per tier, % secondary). Framework thesis validated from vendor side.
2. **Prompt-mutation precedent.** Candidate-prompt demo belongs in Article 26 follow-up ammo: decoys aren't just UI — same blindness in prompt space.
3. **Quote bank:** *"A reasonable-looking prompt change can tank faithfulness without breaking a single test"* (26.08 post) — prompt-world silent green, one line.
4. **Runtime validation argument** (models/embeddings drift without code changes) supports 27's continuous-verification line.

## Cross-links

- Article 26 (mutation matrix; parked follow-up, body frozen).
- Per-risk-tier framework (framework window): gate-shape convergence.
- Article 27 (guided QA): continuous post-deploy eval + agent-remediation loop (agent opens fix PR = supervised autonomy done right).
