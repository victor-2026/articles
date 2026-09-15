Your AI-QA platform just shipped you a green report. 0% risk. The page had two identical login forms — and the tool picked one silently.

I break testing tools on purpose. 5 scenarios, 3 vendors, 1 playbook:
🔹 **Baseline** — calibrate the oracle (confirm green)
🔹 **Locator drift** — heals or fails loudly?
🔹 **Weak + strong decoys** — ambiguity flagged or silent green?
🔹 **Product regression** — caught, not healed silently?
**What the pilots showed:**
• **QAEverest:** 5/5 at 100% confidence. Saw the diffs (2.20% → 3.19%), never flagged the ambiguity.
• **testRigor:** label rename healed 3/3; duplicate label broke honestly.
• **Agentiqa:** 0/6 survived; verifies flows, not UI — adapted silently, flagged blockers honestly.
**The loop closed:** I reported the gap — the vendor shipped a passive observation layer. Now a passed run flags its own warnings: duplicate form sections, seen 3/3, confirmed.

*Green is the default output. The question is whether your probes can make it non-green.*

When did you last break your testing tool on purpose?

Full article below👇

*Part of the Quality Operating Model series.*

Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QAEverest #QualityEngineering
