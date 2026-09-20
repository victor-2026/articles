**Format:** Pulse Article
**Series:** Quality-Operating-Model
**Cover:** 27-cover-guided.png — guided QA engineer steering AI agents, why vs how split, mutation matrix gate in background
**Feed Image:** Guided QA — humans give why, agents give how
**Hook:** How do you keep QA relevant when an agent writes 80% of the tests?

---

# QA Didn't Get Replaced. It Got Promoted.

## The Guided QA Engineer: Why AI Promotes the Tester Instead of Replacing Them

How do you keep QA relevant when an agent writes 80% of the tests? Same way a senior engineer stays relevant when their team writes 80% of the code: you stop typing and start steering.

**B1 (core flows): 3/3 mutants caught - 100%.** Our QAEverest pilot after the fix: every seeded break caught, zero survived.

### ❓ Problem

Agentic coding created the "guided full-stack engineer" — someone who steers AI with fundamentals instead of writing every line ([Andrew Ng, AI Engineering Skills Map](https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map)). QA got the same upgrade: agents now write the test code, but who steers the quality criteria? Teams ship green suites that never proved they can catch a break.

Before the fix, our QAEverest pilot showed 0/4 mutants caught at B1 — a fully green suite that missed every seeded break. This is the silent false negative at scale: **the tool sees everything, questions nothing, and stamps the miss as green.**

### 🧭 Solution

The role didn't shrink — it promoted. Ng's split is "humans give the why, agents give the how." For QA that means you supply what "good" means, where the risk lives, and whether the suite catches anything — the agent supplies the assertions. Testing is still on Ng's fundamentals list (Security & Reliability: test strategy, shift-left, AI-driven scanning) — agents assist, they don't absolve.

As Michael Bolton puts it: **["bottles have necks"](https://www.linkedin.com/posts/michael-bolton-08847_some-musings-on-things-drifting-over-the-activity-7499142012621864960-3Rae)** — the human gate is not a bottleneck to remove, it's the neck that regulates AI output into something observable. The guided QA engineer owns that neck.

The guided QA engineer owns three things the agent cannot infer:
1. **Risk-based gates** — survival rate × risk tier → human gate effort (B0: 0% survival, B1: 0% survival, B2: ≤5% survival, B3: trend only)
2. **Mutation checks as independent oracle** — you break the suite on purpose; if it doesn't catch the break, the green is unverified
3. **Human sign-off** — the Assessor comment on signals, the Reviewer of record, the Engineering owner

In plain terms: B0 is auth and payment (zero tolerance), B1 is core flows, B2 ships with ≤5% survival, B3 cosmetic is trend-only.

[SCREENSHOT: risk-based gate table - survival rate × risk → effort, B0/B1/B2/B3 example]

### 🛠 Implementation

I ran it as: (a) specify risk-based gates (strong for high-risk, light for low — risk-based pilot), (b) write the constraints the agent can't infer, (c) run mutation checks as the independent oracle (QAEverest pilot B1 3/3 100% after fix), (d) own the human sign-off.

**Before → After (Ng-style steering prompt):**

Before (agent guesses): `Write a test for the cache.`

After (you steer):

```
Test the read-through cache with TTL ≤5min.
- Invalidate on write-through to the DB.
- Assert staleness < TTL at the boundary (cache → DB), not just the UI.
- Verify with a mutation: flip TTL to 10min and watch it fail.
```

The agent now can't infer the TTL trade-off — you supplied the why. Same for data model, boundary, and risk gate.

**Worked example: what a sign-off looks like**

Our QAEverest pilot ran the full arc. Before the vendor fix: 0/4 mutants caught at B1 — a green suite at 100% confidence and 0% risk, every seeded break missed. After the fix, the relevance gate filtered the set to 3 catchable B1 mutants — all 3 caught, zero survived.

Then the strict gate. B0 — auth, zero tolerance — held 100% across two rotations. Findings review closed 10/10, each with confirm/dismiss on record. Sign-off went down 07/09 on commit c3d7, with the assessors named, not implied.

Three numbers made that release trustworthy, and none came from the tool's confidence score: survival rate per tier (B1 0% survived post-fix), confirmation rate on findings (10/10 reviewed), rotation stability (two clean B0 passes, not one).

Cost discipline matters too: full-matrix runs are nightly-grade. Per-PR the gate samples ~20 mutants on the changed area — light check every commit, heavy check every night. Never the reverse.

That is the guided QA engineer in one release: the agent executed, the matrix verified, the human signed.

[SCREENSHOT: before-after 0/4 vs 3/3 — same suite, relevance-gated rerun, denominators captioned]

### ✅ Result

"Verify what the agent generated" (Ng) + [survival-rate check](https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/): a green suite is an unverified claim until you break something on purpose. The guided QA engineer turns a green report into a trusted release — execution down, judgment up.

The same security pattern repeats: swarm agents escaped via trusted proxies (GitLab), backchannels (German wiki), and evaluator UI-gates (Anthropic Mythos 5) — unverified agent output = unverified release.

[Zalando's risk-based PR bot](https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html) (33% low-risk auto-approved; cyclomatic complexity inflected upward the moment agents entered the codebase) is a live per-risk-tier gate — vendor-independent, open tools.

The agent writes the test. You write the reason it should fail. Which skill does your QA hire req list as core today?

---

Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QualityEngineering #AITesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Альтернативный хук (кандидат в отдельный фид-пост)

- "Andrew Ng says agentic coding created the 'guided full-stack engineer' — someone who steers AI with fundamentals instead of writing every line. QA got the same upgrade. The question is whether you noticed."

### Evidence (ссылки для инлайна при публикации — прогнать по готче #8)

- Andrew Ng AI Engineering Skills Map: https://x.com/AndrewYNg/status/2088302050706686198 (The Batch #366 / Part 2: Software Engineering Fundamentals; Batch write-up: https://www.deeplearning.ai/the-batch/the-ai-engineering-skills-map). Eval-driven development (главный trait): https://www.linkedin.com/pulse/ai-engineering-skills-map-building-deploying-applications-andrew-ng-gyn5e
- Michael Bolton — "bottles have necks" (VERIFIED 15.09, verbatim from his own post 28.08.2026): https://www.linkedin.com/posts/michael-bolton-08847_some-musings-on-things-drifting-over-the-activity-7499142012621864960-3Rae — "bottles have necks to regulate output to something observable and manageable". General page: https://developsense.com/about-michael-bolton
- Article 26 (break the testing tool, QAEverest pilot B1 100% 3/3): https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/
- Zalando Agentic Engineering snapshot (risk-based PR bot 33% auto-approve, CCN inflection): https://engineering.zalando.com/posts/2026/08/agentic-engineering-at-zalando-a-snapshot.html
- Keith Klain "Confidently Incorrect" (140k transcripts, checks ≠ testing): https://qualityremarks.com/confidently-incorrect-2/

### Carousel angle — DECISION 15.09 (visual review): NO carousel for 19.09 publication

- Rationale: material holds ~4 visual theses, not 6–9; full carousel would force artificial splitting and break the false-confidence → human-gate chain. Publish as **Variant A: Pulse Article + cover + 2 inline visuals**.
- Derivative later (optional, separate asset, not a shrunk copy): 5 slides 1080×1350 — 1. "QA didn't get replaced. It got promoted." / 2. "A green suite can still miss every break." / 3. "The guided QA engineer owns three things: risk, oracle, sign-off." / 4. "Mutation testing asks the uncomfortable question: can the suite catch a deliberate break?" / 5. "The agent writes the test. You write the reason it should fail." — one thesis + one caption per slide, minimal decor. Last slide © Victor Ematin · AI Quality Engineering Lead · Independent practice.

### Visual assets — GENERATED 15.09 (HTML→PNG via Playwright, dark #0d1117 + amber, 2x retina)

- Cover `27-cover-guided.png` (2400×1288, = 1200×644 @2x): kicker + headline + why/how split left; RISK/ORACLE/SIGN-OFF panels + "Green report ≠ safe release" right. Source: `27-cover.html`.
- Inline 1 `27-gate-card.png` (1920×850, = 960×425 @2x): B0–B3 reference table. Source: `27-gate-card.html`.
- Inline 2 `27-before-after.png` (1920×1080, = 960×540 @2x): 0/4 vs 3/3 + denominators caption; doubles as feed-image candidate. Source: `27-before-after.html`.
- Re-shot rule: edit HTML → re-run Playwright snippet (see session 15.09) → verify with Read image. Do NOT edit PNGs directly.

### First comment (draft, вручную после публикации)

- Remaining evidence: Article 16 (Productivity Paradox), Article 20 (false-discovery), Article 21 (Conway), Keith Klain "Confidently Incorrect" (AI inspector missing behavior on 140k transcripts until reasoning added — checks ≠ testing: https://qualityremarks.com/confidently-incorrect-2/), Dario Amodei Sept 2026 "pace the frontier" (frontier-lab CEO calls for embedded evaluators with employee-like access — the attestor role by another name), Megi Tephnadze pilot (risk-based gate — к 19.09 уточнить, если чисел нет, убрать), Ng Building/Deploying (eval-driven development). Rogue-ladder links (тело держит 1 предложение, ссылки сюда): GitLab sandbox escape — https://www.infoq.com/news/2026/09/gitlab-ai-sandbox-access/ ; Anthropic Mythos 5 / CAPTCHA / PyPI — https://techcrunch.com/2026/09/10/anthropic-reveals-rogue-ai-agents-hate-captchas-just-like-you/ ; RubyGems rogue agents — https://tenderlovemaking.com/2026/09/11/what-a-time-to-be-alive/ ; HF multi-agent incident + Bengio lying/coordinating — из дайджестов 13–14.09. VerdictGate teaser: "the method, codified — coming soon" (без ссылки, репо приватный). Digest 13–14 ammo — только сюда, тело заморожено.

### Cross-links in body (make clickable on publish)

- Article 16, 20, 21, 26 (LinkedIn URLs)
- Andrew Ng Skills Map Building/Deploying (eval-driven development): https://www.linkedin.com/pulse/ai-engineering-skills-map-building-deploying-applications-andrew-ng-gyn5e
- Zalando engineering blog
- Michael Bolton DevelopSense
- Keith Klain Quality Remarks

### Replies tracker (rule: max 2 answers per thread)
- Aston Cook (AssertHired): supportive restate (100%/0% + green proves assertions, mutation measures gap). URL: https://www.linkedin.com/feed/update/urn:li:activity:7506593382740344832/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287506745018188115968%2Curn%3Ali%3AugcPost%3A7506301989249540096%29 — **SENT ✅** ("confidence scales with suite size, evidence doesn't").
- Sophia mini-case (STAGED 19.09, second wave, post on user go): `Live case from this week, same failure mode in another domain: an AI advisor given explicit constraints returned 5 mismatched results — twice, verbatim, after being asked to decline honestly if nothing fits. Then ranked a non-match "closest match" while admitting the gap in the same sentence. Parsing worked; judgment didn't exist. Confidence without abstention is the green suite of hiring.` (anonymized, no PII; source: private eval 2026-09-20)
- Shahid Kamal (Founder @ TestOptim, 1d): relevance filtering = underrated, unfiltered score punishes suite for nobody-cares breaks, team stops trusting. Reply DRAFTED 19.09 (post on user go): `Exactly, Shahid. Unfiltered, the score punishes the suite for breaks nobody would ever ship — the team reads noise and stops listening. Filtering is what turns it from a vanity metric into a release signal.`
