**Format:** LinkedIn feed post (standalone methodology note, NOT series-numbered)
**Status:** DRAFT 24.09. Product anonymized (no Vadim approval needed). Numbers: W3 checkpoint (168/35 = 4.8× → "5×" honest rounding; Jev ~350ms avg).
**Numbers lock (W3 Day-3 benchmark + qa-cube):** 5× campaign (168/35, honest rounding) = variants + swap. 50× verdicts = Jev 0.30s/100% vs Pi-fallback ~15s/33% — claim ONLY with comparator disclosed (as in body line 11).

---

120 validation runs in 35 minutes. Same campaign rebuilt-each-time: ~3 hours.

5× from two boring moves: pre-built variants (built once, ~65s each) + ~300ms swap. Run → swap → run, no rebuilds in the loop.

Verdicts: sub-second each (~350ms), no human in the scoring loop. Same judgments via model-fallback judging: ~15s at 33% success — ~50× slower when it works at all. Battle-tested on 2 pilots (FlowScout enrichment, qa-cube campaign), 3rd running. The expensive part was never the runs — it was the rebuilds.

What does your mutation campaign spend most time on — running or rebuilding?

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA
