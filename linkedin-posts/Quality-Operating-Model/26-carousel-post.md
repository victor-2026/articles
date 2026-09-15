Your AI-QA platform just shipped you a green report. 0% risk. The page had two identical login forms - and the tool picked one silently.

How do you test a testing tool? You break it on purpose. I ran two AI-QA vendors through a 5-scenario mutation matrix:
🔹 **Baseline** - calibrate the oracle (confirm green)
🔹 **Locator drift** - heals or fails loudly?
🔹 **Weak + strong decoys** - ambiguity flagged or silent green?
🔹 **Product regression** - caught as a bug, or healed silently?
**What came out:**
• One vendor went 5/5 at 100% confidence and never flagged the ambiguity. Silent green.
• The other broke honestly on a duplicate label - and told us why. Honest death.
• The first vendor got the report, shipped a passive observation layer. Now passed runs flag their own warnings.

Swipe the carousel for the matrix, the two failure shapes, and the 4-step playbook. Full method with numbers drops as an article on Monday.

When did you last break your testing tool on purpose?

*Part of the Quality Operating Model series.*

Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QAEverest #QualityEngineering
