**99% killed. 1 survived. The payment went through unverified. ☠️**

A green test proves the shape of the output, not that it's correct.

Two ways to challenge it:
🔬 Mutation Testing — break the app, ask if the test notices.
🧪 Reverse Mutation Testing — break the verification, ask if the test can prove it wrong.

But one survivor ≠ one survivor. A dead "Thank you" banner and an unverified payment status both count as 1 — the business risk is not the same.

So we attach risk to the behaviour, not the operator — and gate per tier: B0/B1 zero tolerance, band rule below.

Our batch: 58 runs, 53 killed, 5 survived — with the full breakdown (1 vacuous, 2 dismissed, 2 real gaps). Decisions included, FAIL stands.

Co-authored with Victor Ematin (VerdictGate): mutation evidence in, risk-aware verdict out. Full method + tables in the article 👇

**What did your last surviving mutant actually represent?**

Leonardo Lanni · Quality Engineering Expert · Founder of QA Roots
Co-author: Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QualityEngineering #TestAutomation #AIQA #SoftwareTesting
