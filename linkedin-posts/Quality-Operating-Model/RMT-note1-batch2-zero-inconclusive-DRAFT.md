**Format:** LinkedIn Pulse Article (short note — 1 idea + 1 case + 1 number)
**Series:** Quality Operating Model (slot Mon 05.10 — earliest, 48h after Friday 30)
**Status:** PUBLISHED Mon 05.10 (#32) (~09:00, carousel PDF + feed post + first comment live; ugcPost:7512589821614288896, 200-verified)
**Cover:** TODO (proposal: red crash screen vs green suite — "zero inconclusive", dark + amber)
**Feed Image:** cover doubles as feed preview
**Hook:** Twenty-four mutants walked into the suite. Twenty-two died on sight. Two went to resolution. Zero walked out unanswered.
**Links:** first comment carries repo links + full fact ledger (skeleton blob on GitHub — W1 condition: trust not diluted by the split)

---

# Batch #2: Zero Inconclusive Remain

Twenty-four mutants walked into the suite. Twenty-two died on sight. Two went to resolution — a tooltip crash and a controls kill. Zero walked out unanswered. That sentence is the whole note; the rest is how we earned it.

Last week set the stage: a joint piece with Leonardo Lanni on September 29th on reverse mutation meets verdict policy, then last week's 120-run campaign proving our own probe lied before it measured. Both established the machinery. This is the first field report from it: batch #2, hunting exactly what batch #1 left open.

The target was narrow on purpose: `expect.element()` chains across unit specs that our first scanner saw as matcher="element" and walked straight past. Eleven files scouted, nine yielding, twenty-four seeded breaks. Twenty-seven run-records came back: twenty-two killed outright, plus error-rerun rows on three stubborn mutants.

Then the closeout, which reads like a control experiment passing. Twenty-two killed means the suite works — these are the controls, and controls firing is the sound of a healthy rig. The two inconclusives each got a name and a ruling instead of a shrug: one died through a crash, one through the kill mapping. The ledger now says zero inconclusive remain, and zero is a complete sentence.

The crash deserves its minute. Baseline: exit zero, thirty seconds, twenty-four passed. Mutant: exit -9, six hundred thirty-two seconds — the third consecutive hang — CPU pinned between thirty and two hundred percent across all twenty samples, output empty. The suite went red through the crash via a pre-registered exit-code mapping: nobody decided anything in between. The mechanism is a hypothesis, stated as one — negated visibility deadlocking the fixture — and that caveat is what makes the rest believable.

Scoreboard, with units labeled because bare numbers lie: ninety-five seeded mutants across ninety-eight run-records. Every inconclusive resolved. Full ledger — every claim with its file and line — linked in the first comment, because a short note must not mean a thin evidence trail.

Don't copy our twenty-four mutants — one scope is depth, not breadth. Copy the closeout discipline instead: every batch ends at zero inconclusive, or it doesn't end. Same rule as everywhere in this series: machines count, humans decide.

**When did your last campaign end with zero unanswered — by resolution, not by exhaustion?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

### Source
- Skeleton §§1–2,4 (CERTIFIED; W2 §2 eba3d66, W3 §§2,4 confirm; rmt.py lines = W2 768511b)
- Headline: newsats variant of skeleton H2 (units labeled per W2 ruling)

### Facts (ledger refs)
- B5: 11 files scouted, 9 yielding, 24 mutants (run script :22); 27 rows = 22 killed + error-reruns
- Closeout :16-17: 22 killed = controls, 2 resolved (tooltip Caught-by-crash + wa-controls Killed), zero inconclusive remain
- tooltip:213: exit 0/30s/24 passed vs exit -9/632s 3rd hang, CPU 30–200% × 20, empty output (closeout :11); mechanism = hypothesis NOT established
- 95 seeded mutants / 98 run-records (units labeled, bare 95/98 banned)

### Open
- Cover: proposal in metadata — user picks style, Gemini generates
- Feed post text: TODO (after text lock — hook = H1 variant)
- First comment: TODO — repo links (verify 200 at publish) + LEDGER LINK (skeleton blob URL on github.com/victor-2026/articles — W1 condition, mandatory)
- Reviews: W1 fact-check f33106c PASS (2 flags fixed: 29-count removed, date anchors precise) ✅ → W2 4e37764 4×PASS + Q answered (120-run = 30-campaign track, phrasing "last week's" applied) ✅ → W3 explicit CONFIRM (zero deviations) ✅ → R1 (user) → Mon 05.10
- FORMAT CHANGE (owner, 02.10): Pulse cancelled → carousel (scenario + feed post files alongside); this draft = fact base, not publishable text
