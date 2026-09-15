**Format:** Pulse Article/Post (follow-up to Article 15)
**Series:** AI Agents
**Feed Image:** Terminal screenshot showing O2 finding the injected bug + clean-PR control 100/100
**Hook:** DevAssure O2 re-test: 100/100, 0 FP. The hallucination issue from Article 15 is resolved.

---

# DevAssure O2 Re-Test: They Fixed It

**DevAssure O2 re-test: 100/100, 0 FP. The hallucination issue from Article 15 is resolved.**

## What Changed

**Original run (Article 15, Aug 2026):** Injected a 2-line bug (removed `.trim()` → whitespace-only posts submit). O2 caught the real bug — then invented 4 hallucinations from its own tooling artifact (typed literal `"A".repeat(2000)"` as 17 chars, blamed the app for the count mismatch). Score: 22/100. Precision 20%.

**Re-test (Sep 2026, via dashboard cloud agent on Render URL):** Same branch `test/devassure-o2` (commit 5bc0ad8, `.trim()` restored), same injected bug now fixed by code change. O2 ran 5 validations — all passed. **Score 100/100, 0 FP, 13 actions, 2m 3s.** The agent now correctly identifies when its own input becomes evidence. No more "I typed X, saw Y, blamed the app."

## Clean-PR Control (Pure FP Isolation)

Behavior-preserving refactor-only PR on the same composer area (no logic change). **Result: 100/100, 8 validations, 0 FP, 10 actions, 2m 24s.** No false positives on valid post creation. This isolates the FP problem: it was the artifact-awareness bug, not a general tendency to hallucinate.

## Verdict

**Human review gate still recommended** for production gating — but the FP blocker is resolved. The execution layer (diff → blast radius → real browser) was always solid. Now the finding validity matches.

**Clean-PR control: 100/100, no false positives on clean code.**

## Full Methodology

We've formalised a **mutation matrix methodology** ([Article 26](https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-in-5-scenarios-victor-ematin-lqdhe/) — testing AI-QA tools by injecting known defects and checking if they're caught). The same framework applies to any AI-QA vendor: M1-M6 scenarios (locator drift, weak/strong decoy, product regression, clean-PR, reliability probe).

---

Victor Ematin · AI Quality Engineering Lead · Independent practice

#AITesting #QAAgents #DevAssure #MutationTesting #AIAuditing #ZeroBudgetQA #Article15Followup

==== линкедин ушло так
T𝗛𝗘𝗬 𝗖𝗟𝗔𝗜𝗠𝗘𝗗 𝗜𝗧 𝗪𝗔𝗦 𝗙𝗜𝗫𝗘𝗗 — 𝗩𝗘𝗥𝗗𝗜𝗖𝗧: 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗

DevAssure O2 re-test: 100/100, 0 FP. The hallucination issue from previous pilot is resolved (https://www.linkedin.com/pulse/i-broke-my-app-purpose-ai-test-agent-found-bug-invented-victor-ematin-lguse/ ).

What Changed

Original run (Aug 2026): Injected a 2-line bug (removed .𝘵𝘳𝘪𝘮() → whitespace-only posts submit). O2 caught the real bug — then invented 4 hallucinations from its own tooling artifact (typed literal "𝘈".𝘳𝘦𝘱𝘦𝘢𝘵(2000)" as 17 chars, blamed the app for the count mismatch). Score: 22/100. Precision 20%.

Re-test (Sep 2026, via dashboard cloud agent on Render URL): Same branch 𝘵𝘦𝘴𝘵/𝘥𝘦𝘷𝘢𝘴𝘴𝘶𝘳𝘦-𝘰2 (commit 5bc0ad8, .𝘵𝘳𝘪𝘮() restored), same injected bug now fixed by code change. O2 ran 5 validations — all passed. Score 100/100, 0 FP, 13 actions, 2m 3s. The agent now correctly identifies when its own input becomes evidence. No more "I typed X, saw Y, blamed the app."

Clean-PR Control (Pure FP Isolation)

Behavior-preserving refactor-only PR on the same composer area (no logic change). Result: 100/100, 8 validations, 0 FP, 10 actions, 2m 24s. No false positives on valid post creation. This isolates the FP problem: it was the artifact-awareness bug, not a general tendency to hallucinate.

Verdict

Human review gate still recommended for production gating — but the FP blocker is resolved. The execution layer (diff → blast radius → real browser) was always solid. Now the finding validity matches.

𝗖𝗹𝗲𝗮𝗻-𝗣𝗥 𝗰𝗼𝗻𝘁𝗿𝗼𝗹: 𝟭𝟬𝟬/𝟭𝟬𝟬, 𝗻𝗼 𝗳𝗮𝗹𝘀𝗲 𝗽𝗼𝘀𝗶𝘁𝗶𝘃𝗲𝘀 𝗼𝗻 𝗰𝗹𝗲𝗮𝗻 𝗰𝗼𝗱𝗲.

Full Methodology

We've formalised a mutation matrix methodology https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-in-5-scenarios-victor-ematin-lqdhe/ — testing AI-QA tools by injecting known defects and checking if they're caught. The same framework applies to any AI-QA vendor: M1-M6 scenarios (locator drift, weak/strong decoy, product regression, clean-PR, reliability probe).

Victor Ematin · AI Quality Engineering Lead · Independent practice

#AITesting #QAAgents #DevAssure #MutationTesting #AIAuditing