# DoorDash Engineering Blog — QA/AI-relevant catalog (via Wayback, Jul 2026 snapshot)

**Source:** [engineering blog index](https://careersatdoordash.com/engineering-blog/) (direct 403 bot-block; fetched via Wayback 13.07.2026 snapshot). **RSS: none** (all /rss, /feed variants 403) → NOT addable to digest-config; access pattern = manual + Wayback.
**Digest:** ручной заход 12.09

## Deep dives (fetched full text)

### 1. Simulation + evaluation platform for support chatbots (Gong/Bamba, Jun 2026) — MUST READ

Closed loop Generate→simulate→evaluate→iterate. Production transcripts → structured replayable scenarios (1:1 traceability). Stateful LLM simulator (persona, progress judgment, push-back/escalate) + scripted deterministic mode. Mock-aware routing (header/gRPC-wrapper/MCP-metadata), 3 mocking strategies (tool-level, production-backed, mock downstream service). LLM-as-judge feature rubrics, binary pass/fail, SQL-queryable, regression tracking.
**Numbers:** 302 sim convos / 5 min vs 175 prod / 7h (escalation 46% vs 44% — representative, not just plausible); hallucinations in sim −90%. Arrange-Act-Assert at conversation level. Scripted example caught a REAL bug (credits instead of requested refund).
**Our take:** industrial InfoQ sim-eval (used in 26) with numbers attached; scenario-diversity + production-grounding = the two properties our decoy matrix lacks at scale. Feeds 26-follow-up (simulation as decoy delivery) + 27 (flywheel).

### 2. Unified consumer memory (Saboo et al, Jun 2026) — MUST READ for memory track

3 layers: long-term versioned blocks + manifests (model ID, prompt/model/response hashes, any-date reconstruction, A/B, rollback) / in-session high-recency overrides / explicit stable preferences. Graduation pipeline (validate/dedup/merge). Dense asymmetric + graph encodings. Lessons: extraction∥encoding decoupled, multiple encodings win, **lineage non-negotiable**. Future: memory-in-the-loop SLMs, parametric vs latent vs token memory, temporal graphs.
**Our take:** production answer to our warm-vs-cold finding — versioned manifests + lineage are exactly the auditability our 10x lacks; graduation pipeline ≈ supervised promotion (human-gateable). MAS + George-thread material. Feeds Gupta wiki + Agentiqa follow-up.

### 3. AI reviewer engineers trust (Yarger/Rogal, May 2026) — separate page

→ `doordash-ai-reviewer-trust-2026.md` (60.2% acceptance, scout/verifier, disprove-it, cross-boundary drift, evals-from-incidents).

## One-line pointers (not fetched — titles only, fetch on demand)

- **Food Metadata with LLM Juries** — LLM-as-judge panels; evals methodology candidate.
- **Ask DoorDash Part 3: Evaluation** (+ Part 2: Intelligence) — eval methodology for assistant; pair with sim platform.
- **Long-Running Agents journey** — supervision-at-scale narrative; 27 candidate.
- **Small LMs for search ads** — small-model economics (Spotify rhyme).
- **DoorDash Assistant overview** — product surface, weak standalone.
- **Offline LLMs, Online Personalization (carousels)** — experimentation/testing tag; marginal.
- Proxy cache / brand affinity — off-track (perf/marketing).

## Access method

Direct = 403. Pattern: `https://web.archive.org/web/2026/<article-url>`. Snapshots exist (Jul 2026). For digest purposes: manual pull only.
