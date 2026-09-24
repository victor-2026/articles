**Format:** LinkedIn feed post (standalone methodology note, NOT series-numbered)
**Status:** DRAFT 24.09 (rev 2: user inline review applied). Product anonymized (no Vadim approval needed).
**Numbers lock (W3 Day-3 benchmark + qa-cube):** 5× campaign (168/35, honest rounding) = variants + swap. 50× verdicts = Jev 0.30s/100% vs Pi-fallback ~15s/33% — claim ONLY with comparator disclosed. "~3 hours" is conditional (would-take estimate for rebuild-each-time, not a measured run).
**Links:** NONE in body (reach) — discussions #2 + articles go in first comment.

---

120 validation runs in 35 minutes. Rebuilt-each-time, the same campaign would take ~3 hours.

5× from two boring moves: pre-built variants (4 conditions built once) + ~300ms swap. Run → swap → run, no rebuilds in the loop.

Verdicts: a lightweight judgment model at ~350ms each, no human in the scoring loop — battle-tested on 2 pilots, 3rd running. Same judgments via general-model fallback: ~15s per call at 33% success (two of three calls die on rate limits) — ~50× slower when it works at all.

The expensive part was never the runs — it was the rebuilds.

What does your mutation campaign spend most time on — running or rebuilding?

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #AIEvals
