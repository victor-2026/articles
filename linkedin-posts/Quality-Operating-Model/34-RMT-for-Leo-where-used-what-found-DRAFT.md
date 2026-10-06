**Format:** LinkedIn Pulse Article (short note — 1 idea + 1 case + 1 number)
**Series:** Quality Operating Model (slot 08.10 TBD — after consent ping + W1 agreement)
**Status:** draft v1 (#34) (W4, 03.10 — owner order: draft now, W1 agreement next; consent ping still must go BEFORE publish)
**Cover:** DONE 03.10 v2 — `RMT-Leo-cover-v2.png` + `.jpeg` (1920×1080, concept #1: broken assert in red on IDE + green BUILD PASSED badge; v1 typographic kept as fallback; NO Leonardo name — consent pending)
**Feed Image:** cover doubles as feed preview
**Hook:** We break tests on purpose. Fifty-three of fifty-eight broken assertions died — and the five survivors taught us more than the fifty-three kills.
**Links:** first comment (29th URL, 30 URL, verdictgate root — verify 200 at publish)

---

# We Break Tests on Purpose: RMT, Where We Used It, and What It Found

Reverse Mutation Testing mutates test verifications, not app code: seed a broken assertion and check the suite goes red — surviving mutants expose weak verifications, not app defects. It differs from classic mutation testing in seeding direction only; the verdict machinery is shared. The formulation is Leonardo Lanni's: "MT challenges the application, RMT challenges the test." The method is his gift to the commons — this note is where we used it and what it found.

Terms, once: **RMT** = break the check, not the code; **survived** = the suite stayed green on a deliberately broken assertion; **gold** = survivors confirmed by humans, promoted into the judge's bench.

It started as a joint piece: our verdict-policy framework and Leonardo's RMT scanner were combined in one experiment on September 29th, one article, one method tested from both ends. Then we took RMT home and ran it through two full batches on an open-source agent runtime — in test code, never the app: fifty-eight seeded breaks, then twenty-four more chasing the chains the first scanner walked past.

Five survivors from batch one, plus five hard cases from batch two — two timeouts and three representative kills — became bench items E1 through E10: a judge's exam written by the mutations themselves. The breaks that escaped the suite now test the judges. That loop, from seeded break to gold label, is the quietest win in this story.

What it found, in absolutes (no comparisons — we ran no control, and we say so): fifty-three of fifty-eight killed in batch one, five survivors adjudicated down to two real verification gaps: the tests executed the behavior but did not assert it strongly enough. A survivor is not automatically a bad test — it can also mark an equivalent mutation, an unreachable branch, or a test watching the wrong layer. Batch two: twenty-two killed plus two resolved from inconclusive, zero left standing. The guards evolved from the gaps themselves — skip identical mutations, resolve chained or indirect assertions before judging a mutant, version-stamp every mutant so results stay reproducible across scanner releases. Ninety-one percent kill on assertions versus forty on behavioral toggles: assertions die easier because breaking one changes the expected outcome directly, while behavioral toggles need the surrounding scenario to propagate the change. Different layers, never blended, reported side by side.

Methods kept private compound; methods shared compound faster. RMT arrived as one researcher's idea and now runs inside an independent pipeline, writing exams for AI judges. That is what open methodology does — and why this note names its author.

Same rule as everywhere in this series: machines count, humans decide.

**What would your suite catch if someone broke its assertions tonight — and who would tell you?**

If useful, I can share the mutation taxonomy we used for assertions vs behavioral toggles.

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

### Source
- RMT paragraph: W2 b330adb verbatim core (W1 approved b78f5fc, W2 db01059 — quotable as-is; formulation attr. Leonardo Lanni)
- Where used: W2 eadb249 (OpenClaw #1 58 + #2 24; E1–E10 = RMT outputs; B2 as in 29th)
- What's good: W2 absolutes only (53/58, 1+2+2 genuine, 22 + resolved, guards evolution, 91.4 vs 40 layers)
- Metrics: our repost 182/3/1 (02.10); 29th Pulse analytics = Leonardo's side
- Attribution link (Perplexity 03.10 — answers "link his phrase" question): Leonardo on RMT (tests, not code; tests that don't fail when they should): https://testguild.com/podcast/a548-leonardo/ → FIRST COMMENT at publish (no bare URLs in body — series rule)

### Boundaries (BINDING until cleared)
- **Consent:** 24.09 covered name+numbers IN 29th only. New ping REQUIRED before publish (W1 draft exists; sending = owner). Drafting authorized by owner 03.10; publishing without explicit yes = forbidden.
- **Naming:** SUT anonymized ("open-source agent runtime", as in 29th) — default closed. Swap point marked: two batches sentence + E1–E10 sentence. Opening OpenClaw name = NEW W1/owner decision.
- **No MT comparisons** (W2 boundary — no control run). Draft contains none ✅ (check at every review).

### Open
- Cover: v2 built (concept #1, no Leonardo name — swap in after yes); v1 fallback kept
- Feed post text: DONE (variant A, file `RMT-for-Leo-post.md`)
- First comment: links ONLY to our properties — our 29th repost (ugcPost-7510633125073412096) + 30 + TestGuild (Leonardo formulation source) + verdictgate root. NO link to Leonardo's Pulse (owner decision 05.10 — traffic stays home; attribution in text unchanged, consent still required for the name).
- Reviews: W3 CONFIRM ✅ → W1 AGREEMENT 74c0237 ✅ → W2 FACT-CHECK 10c59af PASS ✅ → Perplexity applied ✅ → W1 RE-AGREEMENT a6bd422 (boundaries hold, E-mapping 5+2+3 closed; nits deferred: L7-vs-54 cosmetic, because-softener optional) ✅ → consent ping SENT 03.10 (awaiting yes — publishing BLOCKED) → R1 (user) → slot 12.10 (moves on yes)
