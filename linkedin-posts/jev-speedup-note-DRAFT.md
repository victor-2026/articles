**Format:** LinkedIn feed post (standalone methodology note, NOT series-numbered)
**Status:** DRAFT 24.09. Product anonymized (no Vadim approval needed). Numbers: W3 checkpoint (168/35 = 4.8× → "5×" honest rounding; Jev ~350ms avg).
**Do NOT claim:** 50× (no basis — fabrication). Speedup = variants + swap, NOT Jev alone.

---

120 validation runs in 35 minutes. Same campaign rebuilt-each-time: ~3 hours.

5× from two boring moves: pre-built variants (built once, ~65s each) + ~300ms swap. Run → swap → run, no rebuilds in the loop.

Verdicts: sub-second each (~350ms), no human in the scoring loop. Same judgments via model-fallback judging: ~15s at 33% success — ~50× slower when it works at all. Battle-tested on 2 pilots (FlowScout enrichment, qa-cube campaign), 3rd running. The expensive part was never the runs — it was the rebuilds.

What does your mutation campaign spend most time on — running or rebuilding?

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA
