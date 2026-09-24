**Format:** LinkedIn feed post (standalone methodology note, NOT series-numbered)
**Status:** DRAFT 24.09 (rev 2: user inline review applied). Product anonymized (no Vadim approval needed).
**Numbers lock (W3 Day-3 benchmark + qa-cube):** 5× campaign (168/35, honest rounding) = variants + swap. 50× verdicts = Jev 0.30s/100% vs Pi-fallback ~15s/33% — claim ONLY with comparator disclosed. "~3 hours" is conditional (would-take estimate for rebuild-each-time, not a measured run); "2.5 hours saved" pairs with it (rounded pair).
**Links:** NONE in body (reach) — discussions #2 + articles go in first comment.
**Second comment SENT ✅ 25.09 (mini-jev merge):** `Follow-up: same 7 findings through local mini-jev (Ollama CPU, $0) — ~0.1s vs Jev ~0.3s, severity 2/7 exact match. Cheap judges converge; the 50× stays a different comparator (Jev vs fallback).`

---

120 validation runs in 35 minutes. Rebuilt-each-time, the same campaign would take ~3 hours — 2.5 hours saved.

One operation got ~50× faster (verdict calls: 0.3s vs ~15s fallback at 33% success). But verdicts were never the bottleneck — rebuilds were. The campaign-level 5× came from a human question, not a faster model: where does the time actually go?

Answer: variants pre-built once (each Vue regen costs ~65s — skipped 120×) + ~300ms swap. Run → swap → run, no rebuilds in the loop.

Verdicts came from Jev, a lightweight judgment model (~350ms each, battle-tested on two pilots, third running). No human in the scoring loop. Same judgments via general-model fallback: ~15s per call at 33% success (two of three calls die on rate limits) — ~50× slower when it works at all.

The expensive part was never the runs — it was the rebuilds.

For us this meant: feedback in one coffee break instead of half a day.

What does your mutation campaign spend most time on — running or rebuilding?

Full numbers (GitHub discussion) in the comments👇

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #AIEvals
