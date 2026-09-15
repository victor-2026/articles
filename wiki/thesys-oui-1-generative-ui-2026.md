# Thesys OUI-1: Generative UI Model Trained on Verified-Fixed Loops (Sep 2026)

**Source:** [Parikshit Deshmukh post](https://www.linkedin.com/) (Thesys co-founder, via user share, 12.09) · [tech breakdown](https://www.openui.com/blog/oui-1)
**Digest:** ручной заход 12.09

## Facts

- **OUI-1:** "world's first model built specifically for Generative UI". 4B params, runs locally, ~2x faster than their previous approach.
- **Training method (the interesting part):** not examples only — trained on UI *"actually generated, verified, and fixed"*. The verification-fix loop is the training signal.
- **Score:** 71.7% on their Generative UI benchmark vs 13% base model. Open weights + OpenUI Lang + open benchmark.
- **Thesis:** agents won't just generate text — they'll generate software in realtime.

## Why it matters for us

1. **Verify-fix-train = loop closed as ML.** Our Article 26 story (report gap → vendor ships passive layer) is the same loop at process level; Thesys bakes it into weights. Feedback-becomes-feature, but automated. Strong external rhyme for the loop-closed framing.
2. **Benchmark ownership caveat.** 71.7% on THEIR benchmark, graded by their yardstick — testing mind asks: who verifies the benchmark? Open weights/benchmark make it auditable (good), but independent replication is the real gate. Same oracle-scrutiny we apply to vendors.
3. **Generative-UI reliability = decoy-adjacent.** Generated UI that looks right but is wrong (cf. Muse hands-on hallucinating "Photos"/"Calender") is exactly the surface our decoy mutations probe: identical-looking forms, silently picked. OUI-1's 13%→71.7% jump measures this gap closing.
4. **Small-local economics.** 4B local + 2x faster rhymes with Spotify Portal (cheap models for bulk work) and our $0-budget thesis: small specialized beats big generic per task.

## Cross-links

- Article 26 (loop closed; decoy mutations vs generated UI).
- Muse wiki (label hallucinations hands-on).
- Spotify Portal wiki (small-model economics).
- Article 27 (guided QA): who verifies generated software in realtime — the open question OUI-1 sharpens.
