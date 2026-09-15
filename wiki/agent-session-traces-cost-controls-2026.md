# Session Traces + Cost Controls for Agent Failures (StackGen/InfoQ, Sep 2026)

**Source:** [InfoQ 11.09.2026](https://www.infoq.com/news/2026/09/observability-ai-agents/) (Mark Silvester, via StackGen/Sabith K Soopy CNCF post 04.08)
**Digest:** 2026-09-12

## Core claim

*"The hardest part isn't building them; it's understanding what they're doing when they go wrong."* Standard monitoring says whether a service responds; it can't explain why an autonomous workflow loops, calls invalid endpoints, or claims completed work it skipped. An agent can repeatedly call the wrong tool **without triggering an availability alert**.

## The apparatus

- **Nested session traces** (Langfuse): every LLM call, tool exec, sub-agent delegation = span with latency + token cost; child spans under parents = full delegation chain. Async batch exporter (telemetry outage drops data, never blocks agents).
- **Cost controls as primary safeguard:** hard iteration caps + per-tool call limits BEFORE execution; pre-execution checks blocking identical consecutive tool requests; rolling-average cost anomaly detection (routing errors, hallucinations, context expansion). Reactive alerts arrive too late for parallel agents.
- **Append-only searchable log** (tool calls, governance decisions, memory ops; creds/PII redacted) + CLI diagnostic (API access, vector DB, approvals, memory counts, trace backend, integrations in one run).
- **Automated analysers → human review:** duration, tool failures, retries, token efficiency flagged; bounded Prometheus metrics (tool error rates, approval histograms). **No dynamic session IDs in metric labels** (cardinality crash) — *"Traces are for debugging, metrics are for alerting."*
- **Ecosystem:** OTel GenAI semantic conventions (standard attrs); LangSmith converts anomalous traces → regression test datasets; Arize Phoenix (OTel tracing + self-hosted LLM-judge + prompt experiments).

## Why it matters for us

1. **Traces = evidence trail, generalized.** Our mutation matrix + evidence/ logs + pilot-log rows are the manual version of this apparatus. Their span-per-tool-call with token cost is exactly the granularity our audit trail wants.
2. **Cost controls = token economics enforced.** Iteration caps + consecutive-call blocking are runtime guardrails (Gupta layer 6) made concrete — pairs with Spotify Portal (route cheap) and our OpenRouter $1/day (cap spend).
3. **Anomalous-traces → test datasets (LangSmith)** = production behavior feeding the eval set. Same loop as our 10x probe (Gulin bar) + shadow-testing (Testkube): measured reliability over time, not point verdicts.
4. **Quote bank:** *"Traces are for debugging, metrics are for alerting"* — one line that settles dashboards-vs-traces debates; usable in 25/27.
5. **Pre-execution identical-call blocking** is a mini-mutation-gate: the harness refuses to repeat itself — mechanical skepticism, no LLM needed.

## Cross-links

- Spotify Portal wiki (route cheap + cap spend); Gupta guardrails wiki (runtime layer).
- Article 26 follow-up: traces as the evidence layer behind green reports.
- Article 27: CLI diagnostic + analysers→human as supervised-autonomy pattern.
- Per-risk-tier framework: rolling-average anomaly detection ≈ fragility signal.
