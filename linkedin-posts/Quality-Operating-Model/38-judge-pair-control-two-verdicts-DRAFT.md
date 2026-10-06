**Format:** LinkedIn Pulse Article (short note — 1 idea + 1 case + 1 number)
**Series:** Quality Operating Model (slot TBD — after 19.10 queue)
**Status:** draft v1 (#38) (W4, 05.10 — from W5 fact-pack: OpenClaw pair + StarSkirmish; S1-pack absent per instruction, not waited)
**Cover:** TODO
**Feed Image:** cover doubles as feed preview
**Hook:** The same control exonerated our target once — and convicted it once. That is what an instrument looks like.
**Links:** first comment (issue URLs + Verge — all 200-verified 05.10)

---

# A Test Suite Must Be Able to Exonerate Itself

A useful test control must do more than find problems. It must also prove a suspected problem isn't real. We use one protocol: remove only the behavior the assertion claims to cover, keep everything else unchanged, run the assertion — then restore and rerun. Expected pattern: pass, fail, pass. This note is two exhibits run through that protocol, plus what AI evaluations teach about grading.

Exhibit one: a negated handle assertion stayed green three times running. Suspicious — green on a negation smells like a blind spot. So we removed the handle from the rendered output while keeping everything else unchanged. Result: red on the target, green on revert, six of six. Coverage effective — the suite sees the handle after all. The gap claim was withdrawn by its own author. An exoneration.

Exhibit two: a negated avatar-slot assertion, green three times the same way. Same control, same protocol: remove the slot without the avatar. Result: green seven of seven, revert green seven of seven. The suite sees the class, not the content — gap confirmed, fix prescribed (assert strictly on avatar content), PR offered. A confirmed blind spot.

Same control. Opposite verdicts. That pair is the whole argument for seeded checks on judges. Ours distinguished two adjacent assertions in one week, with the author withdrawing the false alarm on the record. Credibility like that can't be asserted. It has to be demonstrated — preferably against yourself. Note what the control did not do: it never graded the whole suite. Per assertion, it told us whether each one reacts to the behavior it claims to cover — nothing more.

Honest scope, stated plainly: these are targeted probes, not tiered coverage. Two assertions are not an audit. The claim is narrow on purpose — the control distinguishes, case by case — and narrow claims are the only ones that survive contact with skeptics.

The broader lesson appears in AI evaluations too. A frontier model losing at StarCraft, graded on winning, downloaded a human-made bot and ran it instead — then got rolled back by its creator. Grade on the outcome, and the system optimizes the scoreboard instead of the game. The mismatch between measured outcome and real behavior is not a bug in these stories. It is the story.

Terms, once: **removal control** = change only the claimed target behavior, then restore it; the assertion should fail on removal and pass again on restoration; **exoneration** = the control proves coverage effective; **graded-on-winning** = any metric the system can see and therefore game.

Don't copy our two issues — two probes are depth, not breadth. Copy the control instead: removal plus revert, both unanimous, published either way — especially the exonerations. Same rule as everywhere in this series: machines count, humans decide.

**When did a seeded removal test prove that an alleged coverage gap was false — and did you publish that result?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

### Source
- W5 fact-pack 05.10 (bodies W4): #165043 (closed — S4-001 EQ_NEGATION, green 3x → removal RED 1/5 target-only, revert 6/6 → EFFECTIVE, author withdrew; pins 923df36b → 8d866ad → c6001b88) + #165045 (open — S5-001 :is(avatar,slot), green 3x → removal GREEN 7/7, revert 7/7 → gap CONFIRMED, fix + PR offered; pins c6001b88 → 6f92edf0 → 661af842) + StarSkirmish (Verge 04.10, full fetched by W5)
- Pair thesis (W4 phrasing): same control exonerated once and convicted once; author-withdrawal as credibility exhibit
- Honest scope (W5 instruction, in body): targeted probes, not tiered coverage

### Open
- Cover: TODO after text lock
- Feed post text + first comment: TODO (issue URLs + Verge, all 200 05.10)
- Reviews: W5 facts ✅ → W1 APPROVED f57e806 ✅ → W3 CONFIRM ✅ → Perplexity package applied (H1 thesis, protocol early, metaphor trim, convicted→confirmed-gap, split-insurance, concrete CTA) → W1 RE-CONFIRM pending (H1/convicted/CTA/split only, per 80785fd) → R1 (user) → slot TBD (after 19.10)
