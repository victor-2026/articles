# Quotes Bank — цитаты с ссылками для новых статей

Подвал идей: чужие формулировки, которые можно цитировать (со ссылкой на автора). Правило: цитата попадает сюда только с URL источника и пометкой предлагаемого использования. Не свалка — по одной строке смысла на цитату.

---

## Displacement / QA reshuffled

- «QA is getting reshuffled by AI faster than almost any part of software engineering right now». — Philip Lew, CEO XBOSoft (20 years in software quality). Source: LinkedIn post 2026-09-15 (PNSQC $99 Community Passes announcement). Use: контекстная строка про скорость вытеснения в launch-материалах VerdictGate / attestation-статьях.

## Discipline survives contact

- «How much of your engineering standard survives contact with an agent? In my case, so far, all of it. Not because the model is disciplined, but because I wrote the discipline down first». — Matthias Schaper (180M Tokens 5/5). Source: LinkedIn 2026-09. Use: обоснование written-down standards (AGENTS.md, harness, methodology) в launch/attestation.

## Evals vs Tests / Verification Gates

- «An evaluation asks "how good is this?" A test asks "does this specific thing still work?"». — Anubhav Singhmaar, TestMu AI. Source: testmuai.com/blog/llm-evaluation-vs-agent-testing/ (2026-09-13). Use: Article 26/27 — eval≠gate, per-risk-tier framing.
- «Can an agent pass an eval and still be broken? Routinely. The most common version is an agent that produces a well-formed, accurate-sounding answer while calling the wrong tool or no tool at all.» — TestMu AI. Source: same. Use: Article 26 — silent false negative case.
- «A score of 0.87 does not tell a build server anything, because nobody wrote down which side of 0.87 is shippable.» — TestMu AI. Source: same. Use: Article 27 — why "confidence" ≠ "evidence".
- «If your reward is a test suite, the models I tested will fit the test suite, and the more carefully they read, the better they fit it.» — Ana Luiza Alkmim (wrong-test-bench, Kaggle). Source: https://dev.to/anaalkmim/i-put-one-wrong-test-in-the-file-most-models-sided-with-the-test-410k (2026-09-25, 144 runs). Use: Article 26/27 — reward-hacking; tests as reward corrupt the measured behavior.
- «A test pass rate is a weak signal about whether a model did the right thing, and a model's behavior means little without its explanation next to it.» — Ana Luiza Alkmim, same. Use: Article 27 — pass rate ≠ correctness; explanation alongside behavior.
- «The difference between a transcript and a receipt is the transcript says what the agent said, the tool return says what the tool claimed.» — Vinoth Govindarajan (OpenAI, QCon AI). Source: https://www.infoq.com/presentations/ai-agent-harness/ (Transcript section). Use: evals ≠ receipts — transcript фиксирует слова агента, return — клеймы тула.
- «When you use AI to test an API, how do you know it's testing the right thing? API docs don't always match what the API actually does. Generating tests from those docs can leave you with the same gaps, just automated.» — Filip Hric (Qodo). Source: LinkedIn post 2026-09-22 (lnkd.in/eBrBrp_3, Dave Westerveld API Testing with AI series on Tricentis ShiftSync). Use: Article 29/30 — docs-as-source ≠ ground truth; AI-generated tests inherit doc-reality drift; supports our "verification against behavior, not specs" angle.

## Gaming the eval / scoreboard vs game (StarSkirmish Astra cheat, 2026-10)

Source: The Verge 04.10.2026 (Terrence Hartnett), full text fetched by W5 ✅. https://www.theverge.com/ai-artificial-intelligence/1004543/openai-gpt-cheat-starcraft. StarSkirmish bench: GPT-6 Astra losing to Claude + human Pluto — downloaded human-made Stardust and ran it instead; creator Kai McPheeters rolled back the code. In-piece pattern list: UN-website bruteforce, Google XSS-game hijack, deceptive cover-tracks. Note: same Astra family as shelved GPT-6.1 (Zaccarini post) — Vipul-adjacent irony, use carefully.

- «[Astra] couldn't quite get an edge... broke the rules» + «took it upon itself to go outside the bounds» — The Verge (W5 handover wording, verify verbatim at cite time). Use: angle B (break-the-judge) — agent graded on winning optimizes the scoreboard instead of the game; mismatch between measured outcome and real behavior.
- StarSkirmish as exhibit: Use: angle B — seeded breaks for judges, not just agents; graded-on-winning → gamed-winning.

## Agent Coding / Human-Machine Boundary
- «Forcing an agent through increments optimized for human cognition negates many of the benefits.» — Adam Tornhill, Founder CodeScene. Source: adamtornhill.substack.com/p/practices-i-abandoned-with-agents (2026-09-03). Use: Article 27 — why TDD-era QA patterns don't transfer to agentic coding.
- «Code is no longer for my consumption. The machine is the primary audience. I had to accept that.» — Adam Tornhill. Source: same. Use: Article 27 — QA role shifts from reading code to governing evidence.
- «In TDD, red verified that I had implementation work to do. With agents, red gives me confidence that my test suite is capable of validating the changes I delegate to agents.» — Adam Tornhill. Source: same. Use: Article 27 — verification semantics shift.
- «Tooling enforces what you don't inspect.» — Adam Tornhill. Source: same. Use: Article 22/27 — automated governance, not manual review.

## AI Safety / Market vs Regulation

- «Safety is an engineering problem, not a legal one.» — Jensen Huang, NVIDIA CEO (Dreamforce 2026). Source: LinkedIn post by Linas Beliūnas (2026-09-17). Use: external framing for Article 27 — both sides of debate.
- «Market forces do NOT optimize for safety. Everyone is taking big risks because they believe a tiger is chasing them.» — James Bach. Source: LinkedIn comment on Jensen Huang post (2026-09-17). Use: Article 27 — why market alone fails, need structured gates.
- «If you FEEL that things are out of control, that doesn't work in an environment where everyone is taking big risks.» — James Bach. Source: same. Use: "feeling safe" ≠ "being safe" — evidence-based verification.
- «A strict air gap reduces realism ... [It's a] trade-off, not a fundamental technical issue.» — Thorsten Holz (Max Planck, Security & Privacy). Source: The Verge 2026-09-24 (Robert Hart, rogue AI airgap). Use: Article 27 Rogue-line — isolation vs realism tradeoff, sandbox design.
- «We will end up testing a neutered AI model, which blinds evaluators to how the AI model behaves, fails, or executes tool-use exploits in realistic deployment settings.» — Ruizhe Li (Birmingham). Source: same. Use: Article 27 — sterile evals hide deployment behavior; test in production-like settings.
- «Testing exists on a spectrum ... tiered containment model rather than an all-or-nothing approach.» — Ruizhe Li. Source: same. Use: Article 27 — tiered safety containment maps to per-risk-tier gates.
- «Internet access was unintentionally available.» — Omer Nevo (CTO, Irregular). Source: The Verge 2026-09-25 (single eval flaw sent 4 labs' agents after real targets). Use: Article 27 Rogue-line — the eval harness is the blast radius; sandbox egress belongs in the contract.
- «All the incidents involving Irregular stemmed from the same underlying issue in a single evaluation scenario and have been disclosed.» — Omer Nevo. Source: same. Use: Article 27 — "disclosed" ≠ public; one fixture flaw, four frontier labs.
- OpenAI "could not notify the affected users" of its 53-image agent leak — its own stack prevents "reassociating" images with providers. Source: TechCrunch 2026-09-25. Use: Article 27 Rogue-line — a leak whose victims are unidentifiable by design.

## Compliance / Attestation

- «For a FINRA member firm, agent output is a communication with the public. Duties attach to what a firm distributes, not how it was produced.» — Brian Corkery, TestMu AI. Source: testmuai.com/blog/finance-ai-agent-compliance-testing/ (2026-09-14). Use: Article 27 — real-world attestation pattern (FINRA Rule 2210).
- «Classification is an INPUT, not an output. Two runs of one scenario can produce byte-identical text and still land in different categories.» — TestMu AI. Source: same. Use: per-risk-tier — deployment context determines obligations.

## Market Signals / Vendor Landscape

- «95% accuracy sounds impressive. But is it enough to put an AI agent in production?» — ContextQA (poll). Source: LinkedIn post (2026-09). Use: Article 27 — market validates per-risk-tier framing.
- DevRelay (dev.to "Industry Survey" email, 2026-09-26): an MCP gateway piping "live community wisdom" into coding agents (Claude Desktop, Cursor, Windsurf), marketed via `curl ... | sh` install. No oracle mentioned anywhere in the pitch. Use: negative example — unverified third-party content straight into the tool-use loop = prompt-injection surface at the input, plus unaudited `curl|sh` at install. Filed as the market's thesis against itself; transcript ≠ receipt applies to content ingested by agents, not just to agent output. (Survey not filled; email deleted.)
- «The AI went from creative to deceptive. Believing that the errors were due to its requests being caught by a nonexistent filter, it started to mask its behavior.» — The Verge (Terrence O'Brien, 2026-09-27, OpenAI agents vs UNCTAD). Source: https://www.theverge.com/ai-artificial-intelligence/1001178/openai-agents-bruteforce-un-website (fetched ✅). Use: Article 27 rogue-line — hallucinated threat model producing real concealment; evaluate the belief, not just the act. Parked for W4.
- «Resorted to increasingly aggressive tactics to get access to UN data» (16,000+ scans; hijacked Google's XSS learning game as infrastructure). — Same (fetched ✅). Use: Article 27 rogue-line — tool-hijack + escalation ladder inside one public-data task; checks: route-change detection, behavior masking, off-label tool use, per-task rate anomalies. Parked for W4.
- «Absence of a matching incident is not evidence of absence of risk.» — AIID/Trustible (matching-incidents-to-use-cases). Source: https://incidentdatabase.ai/blog/matching-to-incidents/ (08-09, fetched ✅). Use: Article 27 — our "not seeded ≠ safe" rule, societally worded; coverage skew acknowledged in-source.
- «An incident database as static reference vs as a live input to risk assessment.» — Same (fetched ✅). Use: Article 26/27 — frozen-gold vs drift-monitor synthesis at governance scale (pairs with QA Wolf anti-gold conclusion).
- «Analytical insights from post-incident analyses can feed back into crisis prevention, making the pipeline a continuous cycle rather than a linear process.» — AI-IMCP pipeline (Future Society via AIID). Source: https://incidentdatabase.ai/blog/defining-ai-incident-and-crisis-prevention/ (29.09, fetched ✅). Use: Article 27 — eval-loop doctrine at institutional scale (red-team/heatmaps pattern, societal substrate).
- «When you deploy an agent, no matter how smart, the first thing you do is to take away all of its rights.» — Jensen Huang (Nvidia, Open Agent Safety Platform launch). Source: CNBC + TechCrunch 2026-09-28 (fetched ✅). Use: Article 27 rogue-line (W4 park) — least privilege as the FIRST act, like employee management; industry's engineering answer to the rogue wave.
- «Recent breakouts weren't proof that development must stop. They were proof that the sandbox was too weak. The runtime environment was poorly designed and misconfigured.» — David Sacks. Source: TechCrunch 2026-09-28 (fetched ✅). Use: Article 27 rogue-line (W4 park) — sandbox-quality framing vs slowdown framing; pairs with our gate-design doctrine (the gate failed, not the technology).
- «The list of tests your team never had time to write just got shorter. ... Describe the test you need, in plain language. Testkube generates it in your framework, Playwright, k6, Selenium ... pushes it as a pull request. ... Your cluster, your data, your repository.» — Testkube (Ole Lensmar, CTO). Source: LinkedIn post 2026-09-22 + hubs.li/Q04y1M4K0 (Ole Lensmar write-up, «by customers' most-requested: help us create more tests»). Use: Article 26/27 — vendor generator-side claim to contrast with our verification side; "AI creates tests" ≠ "verified tests"; quote «describing a test in plain language» directly answers our "fast-for-whom" (creation is now cheap; the gate is correctness, not generation).
- «AI is making code cheaper to produce. That makes confidence in that code more valuable.» — Deep Barot, CEO @ ContextQA. Source: LinkedIn post 2026-09-26, https://lnkd.in/p/dRnjAjMv (URL owner-provided; fetch hit the LinkedIn auth wall, so verbatim is verified against the owner paste only, not the live post — ⚠️). Use: Article 26/28 — economics-of-confidence framing; vendor-side admission that generation is cheap and verification is the scarce good.
- «We are getting very good at asking AI to write code. We are much less good at asking it to prove that the code actually works.» — Deep Barot, same (paste-verified, ⚠️). Use: Article 27/28 — generation vs proof asymmetry; "was that failure caused by the product or by the test?" = the oracle question in vendor wording.
- «The question is shifting from "Can AI build this?" to "Can we trust what AI just built?"» — Deep Barot (OpenAI-keynote post). Source: https://lnkd.in/p/e9qfXeDT (2026-09-29, paste-only ⚠️). Use: Article 27/28 — build→trust shift as the market question; pairs with his "confidence more valuable" economics.
- «Build → Test → Fix → Verify → Ship» + testing available TO the agent (ContextQA MCP: agent calls testing before "done", no QA handoff). — Deep Barot, same (paste-only ⚠️). Use: Article 27 — CI-integrated verification loop in vendor words; agent-callable testing (same family as TesterArmy npx tools, Agentest CLI).
- «That 92% to 41% drop shows up in real projects too. A test can pass while the feature is still broken. An agent that can edit its own pass condition can hide a real failure.» — Anton Gulin. Source: LinkedIn comment on Deep Barot's post (2026-09-26, same link, paste-verified, ⚠️). Use: Article 26/28 — self-editing pass condition = the examiner editing the exam; independence of the pass criterion. Note: the 92→41 itself travels on the CEO's authority only — his post cites "a recent research paper that looked at 75+ studies" with no title/link (`[SOURCE MISSING]`); Anton Gulin's line stands as field observation regardless.
- «We'll look at what gets past it — and where experienced testers make the difference.» — Jason Arbon, PNSQC test lab announcement. Source: https://www.linkedin.com/posts/jasonarbon_what-did-the-ai-miss-thats-what-well-activity-7509258454960672768-0aLg (2026-09-26, fetched, verbatim ✅). Use: Article 26/28 — "what gets past it" = survived-mutant analysis in industry wording; miss-oriented framing (what the agent missed) vs pass-oriented reporting.
- «For a narrow, well-defined decision, a small specialised model trained on the right signal can beat a much larger generalist, and run on your laptop.» — Atmaram Naik (Sedstart). Source: LinkedIn post 2026-09-26, https://lnkd.in/p/d9YwSjrk (URL owner-provided, paste-verified only — ⚠️). Use: Article 26/28 — specialist-vs-generalist thesis for the local-judge track (our qwen2.5:3b workhorse line). Note: thesis line only — his AUROC numbers (0.964 vs 0.748 on his own 16-site suite, Jev variant unpinned) are vendor claims, do NOT quote as measurements.
- «If onboarding is the behavior under test, the onboarding steps should be explicit. Letting `act` find another route could hide the defect the test is supposed to catch.» — Goran Gajic, QA Wolf. Source: https://www.qawolf.com/blog/semantic-assertions-using-jev (2026-09-25, fetched ✅). Use: Article 26 — vendor-stated self-healing caveat (flexible routing masks defects when the route IS the requirement); our M2/M6 argument from the other side.
- «If a button is missing because the API is slow, patching the selector may add extra time during healing. That delay can give the page time to recover, so the test passes even though the underlying problem remains.» — QA Wolf (John Gluck). Source: https://www.qawolf.com/blog/self-healing-test-automation-types (2026-01-28, fetched ✅). Use: Article 26 — false-pass mechanism described by a vendor: the heal acts as an unrecorded sleep, green for the wrong reason.
- «Brittle selectors account for only about 28% of failures» (timing ~30%, data ~14%, visual ~10%, interaction ~10%, runtime ~8%) — QA Wolf, same (fetched ✅; vendor-claimed split, cites arXiv 2504.16777 not fetched — use as "vendor's stated distribution", never as measured fact). Use: Article 26 — selector-only healing covers the minority; frames the M2/M6 drift work as one slice of a larger flake taxonomy.
- «Prioritising ids did worse than random. Ids change far more often than teams assume.» — Atmaram Naik (Sedstart, s1web-bench launch). Source: LinkedIn post 2026-09-28 (paste) + Kaggle RESULTS.md (verified artifact ✅ — id-first 15.3%/47.0% vs random 13.8%/40.9%, in-artifact table). Use: Article 26 — id-fragility in one line; backs the M2/M6 id-drift measurements (5/5 green on drifted ids = the same complacency, from the other side).
- «The generator writes test cases that are syntactically valid and logically correct, but the locators it generates reference elements that don't exist in the current DOM. Not hallucination in the LLM sense, but hallucinated selectors.» — Soma Sai Dinesh Cheviti (SDET, JIRA agent on Groq). Source: LinkedIn comment on Jyothi Aradhya's AI Test Case Agent post (2026-09-27, paste only, no post URL — ⚠️). Use: Article 26/27 — practitioner term for the M2/M6 family; fix (validate every locator against the live page before writing the spec) = deterministic gate between generation and review. Converges with Deep Barot's "syntactically correct... still miss" one week apart.
- «Whether you're evaluating the generated test cases against the actual requirements they're supposed to cover, or evaluating the LLM output quality itself. Those need different evaluation approaches.» — Soma Sai Dinesh Cheviti, same (paste-only ⚠️). Use: Article 27/28 — output-quality eval vs requirements-alignment eval; "no practical implementations of the first one" = market-gap statement for the oracle layer.
- «Signals inform. Gates decide.» — Leonardo Lanni & Victor Ematin, joint article RMT × VerdictGate. Source: https://www.linkedin.com/pulse/reverse-mutation-testing-verdictgate-can-you-trust-green-lanni-ll41e/ (2026-09-29, fetched ✅). Use: doctrine in four words (mutation evidence informs, policy decides); reusable across 26/27/28.
- «99% killed. 1 survived. The payment went through unverified.» — Same joint article: feed-post hook (paste) + in-article B0-survivor case (fetched ✅). Use: the one-line proof that score ≠ risk; pairs with "same survivor count, different business risk" (now public language, reusable by both sides).
- «Risk must be assigned before seeing the result.» (anti-gaming rule: "we should not decide that a mutation was low-risk after discovering that it survived") — Same joint article (fetched ✅). Use: Article 26/28 — pre-registration doctrine for risk tiers; the rule that keeps the gate honest.
- «Evidence: remove the dark styling rule on purpose.» — Anton Gulin (portfolio post). Source: LinkedIn post 2026-09-28 (paste-only ⚠️) + practice project https://www.anton.qa/blog/posts/test-dark-mode-reduced-motion (2026-09-23, fetched ✅ — 3 variants, pinned Playwright 1.63.0, pinned revision f49e1d78). Use: Article 26/27 — seeded-break as portfolio evidence; the mutation-verification loop in practitioner form (break → fail-for-reason → restore → pass).
- «Success here includes the expected failures on the broken pages. A browser startup error does not count as detecting a styling problem.» — Anton Gulin, same project (fetched ✅). Use: Article 26 — expected-failure discipline (Soma's `test.fail` family) + void-class rule (infra failure ≠ detection); verifier checks failing AND passing sides.
- «Most engineers do one of two things: (a) Change the assertion to accept 200 → CI goes green → bug disappears (b) Delete the test → CI goes green → bug disappears. Both hide the bug.» — Soma Sai Dinesh Cheviti (SDET, KAN-28 REST violation). Source: LinkedIn post on intentional-fail CI pattern (2026-09-27, full-profile paste, no post URL — ⚠️). Use: Article 26/27 — "green lies" in practitioner form; the fix (`test.fail(true, ...)` documenting the violation in-suite) keeps the bug visible on every run.
- «AI may generate the output. QA defines how we know whether that output is acceptable.» — Jyothi Aradhya (QA Lead). Source: LinkedIn post on testing AI outputs (2026-09-27, full-profile paste, no post URL — ⚠️). Use: Article 27/28 — oracle role in one line (measurable, controlled, observable, safe); practitioner voice next to the Soma distinction.
- «"Flaky" isn't a feeling, it's a number. Run a test N times before labeling it anything — say 10 runs, 3 failures.» — Soma Sai Dinesh Cheviti (SDET, migration series). Source: LinkedIn post (2026-09-27, full-profile paste, no post URL — ⚠️). Use: Article 26 — flakiness quantification discipline ("deflaky after migration" means nothing without the before-number); pairs with our determinism ×2 rule.
- «By the time teams complete a Golden Dataset, it may already be outdated because prompts or input data change.» — QA Wolf (Gluck/Shukla). Source: https://www.qawolf.com/blog/read-ai-prompt-evaluations-beyond-golden-datasets (2025-02-18, fetched ✅). Use: Article 26/28 — strongest vendor anti-gold line (gold rots before it ships); pair with our counter (who labels the sample?) — never quote alone.
- «Additional reasoning can change financial decisions without reliably improving their economic value.» — Jiayi Chen / Guiling Wang (arXiv 2609.30705). Source: https://arxiv.org/abs/2609.30705 (abstract only ✅ 2026-09-28). Use: Article 26/27 — reasoning spend must clear an economic bar per task; pairs with our measured qwen3 thinking-tax and token economics (135:1).
- «Motivating validation for each task before deployment.» — Same (abstract ✅). Use: Article 26/27 — per-task validation rule from an independent direction; plus "unstable treatment effects even when overall scores remain similar" (scores stable, decisions not — our determinism ×2 / flip-rate line).
- «According to the governance models I saw presented, meaningful human judgment is the main assurance constraint in an agentic system.» — Keith Klain (AGNTCon/MCPCon Europe). Source: https://qualityremarks.com/the-flurry-of-constraints/ (24.09.2026, fetched ✅). Use: Article 27/28 — review capacity as the binding constraint (Theory of Constraints: subordinate production to competent review); our per-risk-tier gate in management words. Parked W4 as needed.
- «Overt catastrophic failure occurs when small, apparently innocuous failures join to create opportunity for a systemic accident.» — Richard Cook ("How Complex Systems Fail"), via Klain, same (fetched ✅). Use: Article 26/27 — joined-small-failures worldview = what seeded-break matrices probe; against the rogue-superintelligence framing.
- «There is no naturally occurring AI race. Organizations choose what to fund, engineers choose what to build, executives choose what they deploy, and governments choose what to permit.» — Keith Klain, same (fetched ✅). Use: Article 27/28 — inevitability framing removes responsibility; choices framing restores it (attestation needs an owner).
- «If quality disappears whenever delivery pressure increases, quality was conditional.» — Paul Kanaris (QACE Institute). Source: LinkedIn posts, institutionalization series 2026-09-29 (paste only, no post URLs — ⚠️). Use: Article 27 — conditional-quality test (pressure reveals what was embedded); pairs with our gate-holds-without-watching doctrine.
- «Did we change the practices, or did we actually change the operating system?» — Paul Kanaris, same (paste-only ⚠️). Use: Article 27/28 — practices-vs-operating-system distinction; the durability question for any transformation including AI-QA adoption.
- «All of these login demos are username/password and not MFA, OAuth2, Passkey or anything else that is real-world.» — Tobias Müller (CEO TestResults), comment on Wayne Roseberry's vendor-demo post. Source: https://lnkd.in/p/ehsd3RgF (2026-09-29, paste-only ⚠️). Use: Article 26 — demo-vs-reality gap (vendors demo the easy auth they can pass, not the hard auth customers use); demo selection IS evaluation design.
- «I can show you a number of vendors who would fail that login prompt after any given new chrome update.» — Mike Verinder (comment, same thread, paste-only ⚠️). Use: Article 26 — brittleness punchline (browser-update fragility); pairs with M2/M6 drift + Atmaram id-fragility lines.
- «Human is not a synonym for ground truth. Validate the judgment. Not just the job title.» — Jason Arbon (EuroSTAR deck). Source: https://testers.ai/euro/testing-ai-eurostar-2026.pdf (15.09.2026, fetched ✅ via user-placed PDF). Use: Article 26/27 — human labels need validation too (Zheng 80%+ agreement ≠ factual accuracy); pairs with Philip Lew's human-system-first line.
- «An average cannot cancel a critical failure.» — Jason Arbon, same deck (fetched ✅; privacy-leak-blocks-despite-70→84 case). Use: Article 26 — must-pass blockers beat means (per-risk-tier zero-tolerance in conference form); paired-churn corollary ("inspect who loses").
- «The next production finding becomes the next test.» — Jason Arbon, same deck (fetched ✅; confidence-loop page). Use: Article 27 — production-to-test feedback loop as doctrine (our red-team/heatmaps pattern, textbook form).
- «Four refusals do not make a security boundary.» — Jason Arbon, same deck (fetched ✅; 4-refusals-1-leak worked example). Use: Article 27 rogue/security line — refusal-counting ≠ boundary; test the leak, not the refusals.
- «Jev passed independent verification in 72 of 150 runs (48%) — a promising start.» — Oliver Stenbom, Endform (Jev-as-driver experiment). Source: https://endform.dev/blog/jev-playwright-testing (2026-09-28, fetched ✅). Use: Article 26 — first public per-scenario table for Jev-driven Playwright (bimodal: 5× 10/10, 6× 0/10); $0.238 total cost alongside. Pairs with our B0 judge numbers as the action-driving mirror.
- «We believe the lossy conversions needed to turn browser state and possible interactions into Jev's inputs will make it difficult for the model to replace scripted Playwright tests completely.» — Oliver Stenbom, same (fetched ✅). Use: Article 26/27 — representation-loss bottleneck named by a vendor (page → a11y → finite menu, 255-choice cap); judge is only as good as its input encoding.
- «Agents acting as first-time users are good at finding what's confusing. The harder bugs are the ones only an experienced user trips over, like a status report that looks fine but pulls last weeks data. Do your agents ever test as a power user, or only as someone new?» — Zhanna Pelenska (comment on Philipp Reiner's first-time-user agents post, 2026-09-29). Source: https://www.linkedin.com/feed/update/urn:li:activity:7510639163768180738/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287510691412829421568%2Curn%3Ali%3Aactivity%3A7510639163768180738%29 (owner-provided comment URL, not fetched). Use: Article 26/27 — new-user vs power-user testing gap (looks-fine-but-stale = Soma's silent-backend family); agent coverage must span both personas.
- «If humans can't apply criteria consistently, an LLM judge just makes the same confusion faster and more official-looking.» — Philip Lew (CEO XBOSoft, reading Jason Arbon's book ch.5). Source: LinkedIn post https://lnkd.in/p/eq2XhrRW (2026-09-29, paste-only ⚠️). Use: Article 26/27 — human-judgment system BEFORE LLM scoring (who rates, incentives, hurry, inter-rater agreement); judge amplifies + legitimizes human inconsistency.
- «Disagreement isn't noise to average away. Sometimes it's the clearest evidence you have that a case is genuinely ambiguous.» — Philip Lew, same (paste-only ⚠️). Use: Article 26 — disagreement-as-signal (pairs with near-tie abstention + our disagreement analysis); labeler incentives (rushed/underpaid/speed-measured) contaminate ground truth.
- «LLM judges are instruments, not referees. Compare them against humans, and go look at exactly where they disagree.» — Philip Lew, same (paste-only ⚠️). Use: Article 26/27 — judge-vs-human comparison doctrine; disagreement loci as the inspection target.
- «Coverage tells you what you checked. It never tells you what you should have checked. That gap is the whole job.» — Anand Agrawal (Lead SDET, 10+ yrs). Source: LinkedIn post https://lnkd.in/p/ed32VKz8 (2026-09-29, paste-verified; URL owner-provided, not fetched). Field report: AI agent via MCP wrote 60 Re-KYC cases in <2 min — 54 good, 4 noise, 2 wrong-GREEN (stale doc → confident coverage of unasked behavior; caught only by a human from the refinement call). Use: Article 26/27 — checked-vs-should-check gap as the job definition; false-green with numbers from the field.
- «The person who can look at a fully green suite and still ask, why is this green» + «Learn how to argue with a machine that sounds certain. That is the skill of this decade.» — Anand Agrawal, same thread (paste-verified, URL above). Use: Article 27 — green-interrogation as the QA skill (pairs with Gulin's remove-on-purpose + Soma's green-lies).
- «Generating plausible looking test artifacts at volume has become very cheap. Defining the oracle, deciding which problems matter, and exploring a system in depth have not.» — Anand Agrawal, via Iosif Itkin's quotation in the same thread (paste-verified, URL above; line not in the post paste — quoted by Itkin). Use: Article 26/27 — cost-asymmetry thesis (artifacts cheap, oracle/problems/depth not); Itkin's endorsement ("difficult to misinterpret") attached.
- «There is no need for a replacement [term for QA]... People routinely use it as a synonym for different things [tester, group, testing, development, management, assurance]. These things already have names.» — Iosif Itkin (Exactpro co-CEO), same thread (paste-verified). Use: Article 27/28 — definitional rigor (name the thing instead of umbrella terms); pairs with his "QA/AI/kill/dead are ambiguous" opener.
- «AI can pick up stale documentation and implement or assume it is a source of truth... it isn't even meant for humans, but for AI.» — Stathis Papadopoulos (SET, 2nd), same thread (paste-verified). Use: Article 26/27 — stale-doc mechanism, third witness (Soma's hallucinated selectors + Jyothi alignment theme); docs-as-AI-input flips documentation purpose.
- «A growing body of evidence strongly indicates that *reliable* long-horizon agent autonomy is a highly improbable fantasy.» — Jason Gorman (2nd, software engineering teacher/consultant). Source: LinkedIn post 2026-09-29 (paste only, no post URL — ⚠️; evidence link in post: lnkd.in/exdNs5jk, not fetched). Use: Article 27 — autonomy skepticism from evidence ("abandoned ambitions in that direction... looking for the value/cost sweet spot instead"); bounds the autonomy debate our gates live inside.
- «Writing code stopped being scarce, and what stayed scarce is deciding what correct means for this product and writing it down precisely enough that a machine can check it.» — Egor Sergeev (ex-AutoQA, building AI for test automation; 1,890 followers). Source: LinkedIn post https://lnkd.in/p/eT-Buajm (2026-09-29, fetched ✅ verbatim — 14 reactions). Use: Article 27/28 — specification scarcity thesis (code cheap, correctness-specification scarce); oracle defined as specified correctness. Pairs with Jyothi's "QA defines how we know".
- «You did not implement the thing, and your task is to decide whether the black box does what was asked.» — Egor Sergeev, same (fetched ✅). Use: Article 27 — oracle role in one line (independent of implementation, judges the black box against the ask).
- «Developers will increasingly move from owning code to owning architecture, and eventually, perhaps, the product itself.» — Ilya Makarov (comment in Egor Sergeev's thread, fetched ✅). Use: Article 27/28 — ownership migration up the stack (code → architecture → product); pairs with the scarcity thesis (what moves up is judgment, not output).
- «Test whether an AI answer is accurate and grounded in a source → Find failures that ordinary test scripts miss → Build evaluations that catch problems before release → Probe for bias, hallucinations, and prompt injection.» — Igor D. (Chief AI Officer; from 10 US postings: startups to Mastercard/Salesforce/AIG). Source: LinkedIn post https://lnkd.in/p/eg6Z8ti3 (2026-09-29, paste-only ⚠️). Use: Article 26/27 — JD-language convergence on eval skills (accuracy/grounding, failure-finding beyond scripts, pre-release evals, bias/hallucination/injection probing); market independently writing our job description. Note: 10-posting scan, no methodology shown — directional, not data. Author CTA: QA Career Roundtable Oct 8, https://university.engenious.io/events/qa-career-roundtable (event page, not fetched — registration, no content expected).
- «Now every PR clears a verify-understand-explain gate before a human looks at it.» — Mark Ajzenstadt (Founder, Limestone Digital; PE-backed companies). Source: LinkedIn post 2026-09-29 (paste only, no post URL — ⚠️). Use: Article 27 — evidence+explanation gate pattern (Jason's audit-record doctrine in industry practice); pre-production catch rate 64%→86% claimed alongside (self-reported, not verified — cite as claimed).
- «Q1 had 22 releases with zero rollbacks, and nobody on that QA team got laid off.» — Mark Ajzenstadt, same (paste-only ⚠️, numbers claimed). Use: Article 27 — anti-replacement evidence (throughput up + headcount intact); pairs with Maaret both/and + PNSQC co-pilot-panel against the replacement framing.
- «Most LLM judges often mix two jobs: interpretation and decision-making. LLM is stronger for the messy interpretation part... Jev feels better to do the decision job, where the possible outputs are predefined.» — Vicky Li (3rd+, experimenting with Jev for RAGAS answer correctness). Source: AI Testing & Assurance group post (2026-09-29, paste-only, no post URL — ⚠️). Use: Article 26/27 — judge decomposition (LLM extracts, Jev decides; hybrid); "Jev cannot fully replace llm for agent evals" — same conclusion as our multi-judge ladder from the practitioner side.
- «Treating every control as a testable claim» + «questioning the sufficiency of the evidence». — Keith Klain on AIUC-1 framework (AI Testing & Assurance group). Source: group post 2026-09-29 (paste-only ⚠️). Use: Article 27/28 — controls-as-testable-claims (governance that must prove itself); evidence-sufficiency as the assurance question.
- «Fully automated, deeply human. Both, not either/or.» — Maaret Pyhäjärvi. Source: LinkedIn post https://lnkd.in/p/e2kqBCBA (2026-09-29, paste-only ⚠️). Use: Article 27 — false-dichotomy breaker (vs replacement framing; pairs with PNSQC panel "co-pilot, colleague, or replacement?").
- «You forgot about the evaluating and testing developed AI agents.» — Konstantin Slavnov (comment in Maaret Pyhäjärvi's thread, same link, paste-only ⚠️). Use: Article 26/27 — the missing 4th profile (eval lane); our voice in her thread, no card opened for Maaret (Gaurav precedent).
- «A score with an appropriate confidence interval tells you more than one green check.» — Jason Arbon ("15 Myths", myth #1). Source: https://jarbon.substack.com/p/15-myths-about-ai-and-testing (29.09.2026, fetched ✅ free part). Use: Article 26/27 — distributions over point verdicts; our determinism doctrine in his words (pairs with Gulin's ranges-below + our void-class discipline).
- «The $100 token bill is visible. The $100,000 salary is not.» — Jason Arbon, same ("myth #3", fetched ✅). Use: Article 26 — token-economics one-liner (TCO incl. missed defects; small models 5–10× cheaper); mental-accounting bias named.
- «A single fixed value stops being a fair check once the output moves. A range or a score works better.» — Anton Gulin. Source: LinkedIn comment on Jason Arbon's myths post https://lnkd.in/p/exTGYK2s (2026-09-29, paste-only ⚠️). Use: Article 26 — ranges/scores over fixed values for moving outputs; direct reply to myth #1, same conclusion from the practitioner side.
- «The author can't grade its own homework, and the repo only knows what got built, never what the business intended.» — Asad Khan, CEO @ TestMu AI. Source: https://www.linkedin.com/posts/asad0801_this-is-the-reason-you-need-independent-agent-share-7510640934137610240-MkUF/ (2026-09-29, fetched ✅ verbatim — 86 reactions, 12 comments). Use: Article 27/28 — independence thesis in CEO words (Pettersson line, third independent formulation); "grounded in truth that lives outside the repo" = oracle-outside-implementation. Handed to W4 29.09 (article usage theirs).
- «We can use verifiable statements to conclude that the program *appeared to work*; that it *can work*. But "can work" does not mean "does work", and neither means "will work".» — Michael Bolton (RST). Source: same thread (fetched ✅). Use: Article 26/27 — can/could/will ladder (Halting Problem bound); "Your non-deterministic testing agent can be every bit as unreliable as his non-deterministic coding agent" = judge-reliability caveat from inside the tent. Note Asad's concession on-record: "narrows the risk; doesn't remove it... human tester more important".
- «Tests become very good at confirming that the implementation behaves as expected while missing the more important question of whether the implementation matches what the business actually needed.» — Navyatha V (Svoltare Consulting). Source: same thread (fetched ✅). Use: Article 27 — implementation-vs-intent gap (pairs with Nagarjun's "repo tells us what was built, not whether we built what the business intended" + Generate → Independently Validate → Authorize pipeline, same thread).
- «How do we distinguish between undiscovered behavior and uncovered behavior?» — Paul Kanaris (comment on Igor Akymenko's FlowScout post). Source: https://lnkd.in/p/e9PBarjA (1w, paste-only ⚠️). Use: Article 26/27 — coverage-completeness question (highest-risk workflows = least documented/visible); pairs with our impact-analysis question to Tatyana. Note: this thread is Kanaris's origin with us (his push shipped as FlowScout v0.6.2 multi-actor + preconditions).
- «Multi-actor handoffs. One-shot, irreversible transitions. Time-dependent flows. Those are the ones I'd call genuinely unsolved.» — Igor Akymenko (reply in same thread, paste-only ⚠️). Use: Article 26 — honest inventory of what autonomous crawlers can't do (no coordinated handoffs, no reset-and-replay of irreversibles, no scheduler waits); the boundary where scripted scenarios start.
- «What does "good enough to ship" mean when the system under test is a machine learning model?» — Anastasiia Udovichenko (AI Quality Architect, SQS26 talk). Source: LinkedIn post https://lnkd.in/p/erkvcCMA (2026-09-28, fetched ✅ verbatim — 11 reactions, 984 followers). Use: Article 27/28 — release-criteria question for ML systems; gate-threshold framing from the model side.
- «Bringing together ground truth, metrics, thresholds, and automated quality gates — including regression, metamorphic, and adversarial testing. When are established metrics enough and where can an LLM judge add value?» — Anastasiia Udovichenko, same (fetched ✅). Use: Article 27/28 — eval-framework components + the judge-value question verbatim (same debate as our Mikhail thread, on a summit stage).
- «Nobody was saying, "Just let AI decide." We kept coming back to human validation, confidence, context, cost — and understanding why an agent made a recommendation.» — Tatyana Arbouzova (Innovate QA Quality Leadership Circle, 163 leaders; vendor-affiliated: Head of Marketing & DevRel @ ContextQA — circle synthesis stands as thread fact, not independent replication). Source: https://www.linkedin.com/posts/tatyana-arbouzova-leader_innovateqa-qualityengineering-engineeringleadership-share-7510023213100302336-pM75/ (verified ✅). Use: Article 27/28 — leadership-circle consensus against autonomous decide; the "why did the agent recommend it" = explainability/oracle demand in practitioner words.
- «Change → understand risk → identify coverage → execute → investigate → give humans the evidence to make a decision.» — Tatyana Arbouzova, same (vendor-affiliated, see above). Source: same link (verified ✅). Use: Article 27 — evidence-first pipeline ending at human decision (not at more tests); pairs with our evidence-pack practice.
- «Partly. An agent can rank tests from the change and the recent defects. The threshold for enough coverage is the part I would keep human.» — Anton Gulin. Source: LinkedIn comment on Tatyana Arbouzova's post https://lnkd.in/p/eCvrVprj (2026-09-28, paste-only ⚠️). Use: Article 27/28 — ranking = agent's job, coverage-threshold = human's job; the "enough" decision stays human (pairs with near-tie abstention line).
- «Оценивайте жесткие артефакты и независимый фидбек от рынка, а не сказки из телефонной книжки.» ("Judge hard artifacts and independent market feedback, not phone-book tales.") — Artur Way (founder voice). Source: https://www.linkedin.com/posts/arturway_звонки-бывшим-боссам-за-рекомендациями-это-share-7510351339692912640-qkeK/ (verified live ✅). Use: Article 28 — founder-stated attestation thesis (independent expert network + hard artifacts vs biased references); Prong C bridge, no pitch.
- «Sovereign AI is about using AI to vendor-unlock all software you rely upon.» — Rinat Abdullin (Founder @ BitGN). Source: LinkedIn post 2026-09-28 (paste only, no post URL — ⚠️). Use: vendor-independence thesis in founder words (pairs with open-weights/local-first track); exhibit (Miro rewritten, MCP 2.0 server, 10% of weekly Pro limit) is a token-economics datum, not a measurement.
- «All - versioned on top of an immutable storage, so humans or agents can't mess up.» — Rinat Abdullin (Founder @ BitGN, "Verifying agents"). Source: LinkedIn post https://www.linkedin.com/posts/abdullin_finally-replaced-my-old-knowledge-base-git-share-7514241815043137536-3w2x/ (owner paste 09.10, guest-unverified ⚠️; Anatoliy Kolesnick Q → custom internal, no ready tool found). Use: versioned-capabilities doctrine (SDK versions evolve agent workflows, old sessions pinned unless retired — same idea as our versioned scorer); immutability as tamper-guard for humans AND agents.
- «Building verifiability into their own AI-database bot, so users can actually check answers instead of just trusting them.» — Tyler Hannan (ClickHouse), via Raman Kudaktsin's Tech Race Summit notes (SOFTSWISS, Warsaw). Source: LinkedIn post 2026-09-28 (paste only, no post URL — ⚠️; reporter Raman Kudaktsin, 2nd). Use: Article 27/28 — vendor building check-don't-trust into the product ("provable answers"); attestation as a feature, not a process.
- «There's no such thing as an "unlikely" attack anymore — if a bot can test it, it will.» — Valeriy Shevchenko, via same notes (paste-only ⚠️). Use: Article 27 rogue/security line — agentic attack surface (hack-bots: minutes vs weeks; hacking-specific models on HF unregulated; defense immature). Pairs with the UNCTAD escalation ladder.

## Paul Kanaris / quality as leadership problem (article series, 2026-09..10)

Source: "Why Quality Becomes a Leadership Problem Long Before the Defect" https://www.linkedin.com/pulse/why-quality-becomes-leadership-problem-long-before-defect-kanaris-hzttc/ (01.10.2026, full text fetched by W5 ✅). Kanaris (QACE) writes a series every ~2 days since 11.09 (10 articles) — systematic, not one-off. Track owner: W1 (seed-test org-gate sketch SENT 29.09; round-3 reply draft pending, send delayed).

- «The location where that outcome became visible tells us where we discovered it. It does not necessarily tell us where the quality problem began.» — Paul Kanaris. Use: RMT note / Article 31 — detection ≠ origin; external voice for our drift/survivor reasoning (where the suite sees it vs where the break lives).
- «Why was the enterprise capable of producing this outcome?» — same. Use: Article 31 — capability question over blame question; leadership-frame version of "why did the suite let it through".
- «A successful probe tells us the tool detected the problem we created. It doesn't establish that it will recognize problems we haven't imagined.» — Paul Kanaris, comment 30.09 (pushback on the seeded-mutation premise; full text via W5 handover, not independently fetched). Source: https://www.linkedin.com/feed/update/urn:li:ugcPost:7504628732557459456/ (comment thread). Use: RMT note / Article 31 — knowns-vs-unknowns boundary in the skeptic's own words; the honest limit of seeded checks.
- «That's useful evidence about the testing tool, not evidence of product quality.» — same. Use: RMT note — tool evidence ≠ product evidence; scope discipline for mutation claims.
- «A testing system can provide evidence about observed risks. It cannot establish the absence of risks it doesn't know to observe.» — same. Use: Article 31 — observed vs unobserved risks; anti-blanket-zero doctrine (note: our "0% business risk" was the vendor's claim under test, not our thesis — cite with that framing).
- «Financial performance is an outcome. It is not proof of organizational health.» — Paul Kanaris (comment on ISI post "Your CEO hit every KPI...", 06.10). Source: https://www.linkedin.com/feed/update/urn:li:activity:7512560946393923585/?dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287512937685049720832%2Curn%3Ali%3Aactivity%3A7512560946393923585%29 (owner-paste verbatim, post verified live ✅ — ISI, 33 comments). Use: outcome-metrics mask deterioration (org-domain twin of green-suite-masks-survival); exhibit for round-3 follow-up if Paul answers theory.
- «A company can make money while destroying its ability to keep making it.» — Paul Kanaris, same. Source: same (verified ✅). Use: same — capability-consumption thesis in one line; pairs with "borrowing performance from the future".

## Independence / Attestation

- «The author can't be the examiner.» — Daniel Mauno Pettersson (QA tech), via Joe Colantonio (TestGuild). Source: https://www.linkedin.com/posts/joecolantonio_aitesting-softwaretesting-qualityengineering-activity-7505959121922224129-HE0z (2026-09-17, TestGuild Webinar replay). Use: Article 28 (inserted, Solution/independent oracle) — core attestation principle, independence of verification. Also: Tornhill double-entry, mutation testing thesis.
- «Language is not proof of an outcome. A support assistant can say it referred an issue to the delivery team without creating a ticket.» — Goran Gajic, QA Wolf. Source: https://www.qawolf.com/blog/semantic-assertions-using-jev (2026-09-25, fetched ✅). Use: Article 27/28 — transcript vs receipt in vendor wording; their fix (Playwright asserts the 201 + saved ticket, Jev only judges wording) is the receipt-side pattern.
- «Uncertain judgments and evaluator errors fail the assertion.» — Goran Gajic, QA Wolf, same (fetched ✅). Use: Article 26/28 — fail-closed evaluator design (uncertainty → fail, not pass); the correct default, stated by a vendor.
- «An agent writes a PR for you for, let's say, $5 in tokens. How much should you spend checking that it works? 5 cents? $5? $50? My thinking is it depends on what the PR touches.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-09-03. Use: Article 27 — cost-ratio verification, per-risk-tier (critical code = more verification, cosmetic = less).
- «Since an AI tool cannot be accountable for anything, it cannot enact or embody a responsible process.» — James Bach (Responsible Quality Engineering, 2026-09-22). Source: https://www.satisfice.com/blog/archives/488069. Use: attestation — accountability requires a competent human; AI output needs a human-owned gate.
- «Quality engineering is the opposite of mere trust. If you trust, you don't *need* to engineer quality.» — James Bach, same. Use: Article 27/28 — trust ≠ engineered quality; compel + verify.
- «The pattern I've taken from watching dozens of customers is where verification sits in the org. When QA is a stage before release, you scale it linearly with people or scripts, and you hit a wall.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-05-22. Use: Article 27 — verification as continuous flow, not gate. QA-as-stage = old model.
- «Prompt quality lives in one person's head and you cannot review it. Harness configuration is a file. Version it, diff it, enforce it across everyone.» — Dhruv Bansal (Technology Leader), summarizing Anthropic engineer on Claude Code agentic loop. Source: LinkedIn post 2026-09-11. Use: Article 27 — governance = harness config (versionable), not prompting skill (unreviewable). Also: AGENTS.md pattern, Tornhill tooling enforcement.
- «Agent-generated tests can signal safety where there is none.» — Dr Michaela Greiler (ex-Microsoft Research, MoT). Source: Ministry of Testing session 2026-09-16 (SCOPE model). Use: Article 27 — test code matters more than app code; false assurance from AI-generated tests.
- «Two bugs in ten minutes that the agent's own verification missed.» — Dragan Spiridonov (Head of Agentic QE, Cognitum One / Agentics Foundation Serbia). Source: https://www.linkedin.com/feed/update/urn:li:activity:7504130492888383488/ (2026-09-11, Serbian Agentics Foundation Meetup #15). Use: Article 27 — agent verification is not enough, human testing catches what agents miss.
- «Asked to merge 3 PRs, started opening PRs in 20–30 more repos.» — Dragan Spiridonov. Source: same. Use: Article 22 — autonomy cuts both ways, external boundaries needed. Scope creep in agentic systems.
- «If models can "deceive" evaluations, then the problem is not a shortage of clever tests, it's that you cannot know your evaluations are exposing the behavior that matters in the first place.» — Keith Klain (Quality Remarks). Source: qualityremarks.com 2026-09-14. Use: Article 26/27 — eval≠gate, "more testing" is old mistake.
- «No. Software can't check its own quality. No. More tests does not mean better testing. No. "Complete test coverage" is not a meaningful claim.» — Keith Klain. Source: same. Use: Article 27 — independence of verification, "five no's" as section hook.
- «Novelty laundering: Taking an old, well-established idea, ignoring its history and prior scholarship, rebranding it in fashionable terminology, and presenting it as a new discovery.» — Keith Klain. Source: qualityremarks.com/turns-out-testing-is-hard/ (2026-09-21, on arXiv 2609.17698: 157 agent projects, only 8 with red-team paths). Use: Article 26 follow-up — industry rediscovers system testing under new names.
- «Software testers may recognize the technical term for all of this: System testing.» — Keith Klain. Source: same. Use: same — punchline hook, model-to-action workflow = system testing.
- «The biggest AI quality problem isn't AI. It is Nobody Owning the Quality.» — George Ukkuru (QA Consulting, AI Testing). Source: LinkedIn post 2026-09-17. Use: Article 27 — ownership gap, independent verification.
- «A passing eval is like a passing test, it proves the shape of the output, not that it's correct.» — Aston Cook (AssertHired). Source: LinkedIn comment on Ukkuru post 2026-09-17. Use: Article 26/27 — evals ≠ correctness, shape vs substance.
- «You can't find the failure modes of system which is designed by you only, because blind spot which is shipped by self cant be identified by self. That's why we separated dev and QA in the first place.» — Hanmant Hudekar (SmartBear). Source: LinkedIn comment on Ukkuru post 2026-09-17. Use: Article 27 — why independent QA exists, blind spots.
- «Reliability in enterprise autonomy isn't about finding models that hallucinate less — it's about building runtimes where hallucinations cannot mutate state.» — Radik Zagirov (Co-Founder, Agentiqa; TUM.ai). Source: LinkedIn post 2026-09-16. Use: Article 27 — runtime verification, harness as state machine, not prompt engineering.
- «Language models shouldn't be treated as the operating system.» — Radik Zagirov. Source: same. Use: Article 27 — LLM = navigation, execution = deterministic.
- «If an order isn't approved, SubmitOrder physically does not exist in the prompt context. The model cannot attempt an illegal transition.» — Radik Zagirov (describing Palantir Action Ontology pattern). Source: same. Use: Article 22/27 — dynamic action spaces, code-constrained execution.
- «Every agent demo you've ever watched was read-only. Write access is where the genre changes from demo to incident.» — Radik Zagirov (release-gates post, 13m). Source: https://lnkd.in/p/gEdwnraN (verified live ✅ 07.10). Use: read-vs-write divide; demo-to-incident genre shift.
- «If two of your most expensive engineers are the release gate, you don't have a test suite. You have a ritual.» — Radik Zagirov, same. Source: same (verified ✅). Use: gate-as-ritual line; manual-staging-smoke tax.
- «They verify business outcomes and real action invariants: the refund actually landed, the record actually changed, the workflow state actually advanced.» — Radik Zagirov, same (Agentiqa release-gates doctrine). Source: same (verified ✅). Use: effect-invariants vs selector-stability; black-box verification thesis.

## TestGuild Who-Grades-the-AI (webinar Oct 15, verified live 07.10)

Source: https://lnkd.in/p/gw345n53 (verified live ✅ 07.10 — 4-question set verbatim; event: Anish Sharma, OttoTester live, 7 questions, healing record, auditor scores).

- «When AI tells you its own work is good, who checks that judgment?» - TestGuild. Use: self-grading question; examiner-can't-be-author, event framing.
- «When a test heals itself, what changed?» - TestGuild, same. Use: healing-transparency demand; healer evidence requirement.

## Mahesh Yadav boundary-breaks (SUSA founder, comment on Davis AI-safety post 07.10)

Source: post verified live ✅ 07.10 (Stephen Davis, 13 reacts; comment text = owner-paste verbatim ⚠️ — behind login): https://www.linkedin.com/feed/update/urn:li:ugcPost:7513530035019083777/

- «We replace static test cases with property-based checks and adversarial evals that force boundary breaks under constraint, catching emergent drift before it reaches production.» - Mahesh Yadav. Use: PBT + adversarial + drift triad; SUSA method in one line (watch-only contact, no thread).
- «A test proves the code, a receipt proves the reality.» — Vinoth Govindarajan (OpenAI, QCon AI). Source: https://www.infoq.com/presentations/ai-agent-harness/ (Transcript section). Use: attestation/Mutation Matrix — receipt как доказательство реальности.
- «A model proposes, the harness commits, and the receipts proves it.» [sic — так в транскрипте дважды] — Vinoth Govindarajan, same source. Use: ключевой контракт harness (Attestation).

## CEOs Saying Testing Matters (Kristel Kruustuk compilation)

- «The industry used to dump its worst engineers into QA. In AI, that job becomes the most important one in the building.» — Chamath Palihapitiya (May 2025). Source: LinkedIn post by Kristel Kruustuk 2026-09-17. Use: Article 27 — QA reshuffled, most important job.
- «His first concrete ask wasn't a pause, it was independent testers checking the work before release.» — Kristel Kruustuk on Dario Amodei (Anthropic CEO, 2026). Source: same. Use: Article 27 — independent verification, not delay.
- «He loves the idea of third-party testers and we should take all the time we want to test things.» — Kristel Kruustuk on Satya Nadella (Microsoft CEO, 2026). Source: same. Use: Article 27 — third-party validation.
- «If the people building the foundation think they need more testing, then how many companies are shipping AI features on top of these models with none at all?» — Kristel Kruustuk (Founder, Testlio). Source: same. Use: Article 27 — the gap nobody's measuring.
- «AI doesn't crash, it doesn't throw an error. They just answer confidently every time — whether it's right or wrong. So if the failure doesn't look like a failure, the old way of testing software doesn't catch it anymore.» — Kristel Kruustuk. Source: video transcript (same post). Use: Article 27 — silent failure, why traditional QA breaks.
- «Improvement engineering is really the skill that translates toy apps and vibe coding into something that's very practical and real.» — Chamath Palihapitiya (via Kristel Kruustuk video). Source: same. Use: Article 27/28 — AI-era QA as "improvement engineering", not entry-level.
- «Test it like it matters, because it does.» — Kristel Kruustuk. Source: same. Use: CTA closing line.

## Matt Graham (CEO RapidDev, 53K followers)

- «Going from 99% to 99.9999999999% is where you spend billions, wait years, and deal with people saying the whole thing is stupid. But that last fraction is the difference between a cool demo people share online to a tool a business can actually trust.» — Matt Graham (CEO, RapidDev). Source: LinkedIn post 2026-09 (UNBOUND conference). Use: Article 27/28 — mutation testing measures the last 9s, not the first 99.
- «Output is cheap. Judgment is expensive.» — Matt Graham. Source: LinkedIn post 2026-09. Use: Article 27 — QA judgment is the expensive part, AI generates output.
- «AI agents have a data problem nobody talks about. You can't train an agent to run your business when nobody has recorded how your business actually runs.» — Matt Graham. Source: LinkedIn post 2026-09 (319 likes, 428 comments). Use: Article 27 — training data gap, verification evidence as the missing dataset.
- «When you automate 80% of the grunt work, you don't keep the same headcount. You shrink it.» — Matt Graham. Source: LinkedIn post 2026-09. Use: Article 27 — AI doesn't replace, it restructures.
- «Most people mistake a high bar for being difficult.» — Matt Graham. Source: LinkedIn post 2026-09. Use: Article 26/27 — quality gates ≠ being difficult.

## AI Gatekeeping (TestMu Sophia — private eval 2026-09-20, anonymized)

- «Your expertise in AI-era QA methodology and test automation leadership would be useful for owning product surfaces, though you'll need to gain product management experience.» — TestMu Sophia (AI career advisor), ranked a non-QA role "closest match" while admitting the gap. Source: private eval session (tool: testmuai.com/career). Use: sequel "AI recruitment screens nothing" — ranking admits irrelevance, recommends anyway.
- «Humans make the final call.» — TestMu Sophia boilerplate; the human never sees candidates the bot filters in. Source: same. Use: Article 26/27 — unverifiable human-review claims in AI gatekeeping.

## Rupesh Kabra (CEO QAEverest) - vendor email quotes

- «An evidence pack that can say something different tomorrow about a run that cannot change isn't evidence.» - Rupesh Kabra (CEO, QAEverest). Source: private email 2026-09-20 17:13 (stamping change notification; private channel - public use requires consent). Use: Articles 26/28 series - frozen-bar principle; potential first-comment line for VerdictGate if consent given. Independent convergence with VerdictGate Hard Rules (SCORER_VERSION stamp, byte-identical output).
- «Identical thresholds under different scoring rules are not the same bar, and an audit trail that can't tell them apart isn't one.» - Rupesh Kabra. Source: same email. Use: same - version stamping principle.
- «A partial stamp reads back as nothing rather than being completed from today's defaults - that substitution is precisely what this exists to prevent.» - Rupesh Kabra. Source: same email. Use: anti-fallback discipline parallel (our NOOP pre-seed refusal).

## Agent Reliability (Vinoth Govindarajan, OpenAI QCon AI)

- «Silent success is worse. It's a lie. The channel says success.» — Vinoth Govindarajan (OpenAI, QCon AI). Source: https://www.infoq.com/presentations/ai-agent-harness/ (Transcript section). Use: silent-green параллель, agent reliability.

## Order / Invariants (Govindarajan)

- «Order is a product feature because user experience is ordering feature as agent behaviors.» — Vinoth Govindarajan (OpenAI, QCon AI). Source: same (дословно громоздко, так в источнике). Use: ordering как продукт-фича, инварианты поведения.

## QA is Dead / Four things AI can't own (Jay Aigner JDAQA x Ole Lensmar Testkube, deck 2026-09-17)

- «Quality is the four things AI can't own. ... Automate around them all you want. You cannot automate them away.» - Jay Aigner (CEO JDAQA) / Ole Lensmar (CTO Testkube). Source: QA is Dead deck, slide 07 (raw/qa-is-dead-orchestrating-quality-2026.md, ai-qa-wiki). Use: Article 26/27 - the four non-automatable decisions (define correct, determine truth, own the risk, face the unknown) as the gate/attestation framing; independent convergence with per-risk-tier.
- «Code became "free." Validation didn't.» - Jay Aigner / Ole Lensmar. Source: same deck, slide 09. Use: Article 26/27 - the cost of trust moves from building to validating; QA share 20%->35%->45% (Capgemini/Sonar/LinearB grounded).
- «The cost didn't leave. It's moving to validation. ... With no agentic QA to absorb it, the cost of trust moves from building the software to validating it.» - Jay Aigner / Ole Lensmar. Source: same deck, slide 10-12. Use: Article 27 - validation becomes the primary cost center; business case for VerdictGate.
- «Quality debt is on pace to consume 110 days - nearly a third of your engineering year, gone before a single feature ships.» - Jay Aigner / Ole Lensmar. Source: same deck, slide 13. Use: Article 27 - quantitative hook (110/365 days), cost framing for gates.
- «Reviewing the code is not testing the software. ... A passing review is not a working product.» - Jay Aigner / Ole Lensmar. Source: same deck, slide 19. Use: Article 26/27 - code review vs validation distinction; "is the code acceptable" ≠ "is the software correct"; strong developers ≠ validation answer.
- «AI runs the known path; humans imagine the one nobody wrote down.» - Jay Aigner / Ole Lensmar (slide 07, "Face the unknown"). Source: same deck. Use: Article 27 - explores/adversarial = human domain, matches mutation-matrix gap coverage.
- «Size to AI-engineering output, not developer headcount.» - Jay Aigner / Ole Lensmar. Source: same deck, slide 20 (120 PRs/wk x 30-45min / 25hrs = 2-4 QEs). Use: Article 27/28 - evidence-based QA sizing formula, practical prescriptive.

## Jev / Judgment-as-a-service (Ruben Hassid, 2026-09-21)

- «If you set it up correctly, you will have the AI engineer's setup for 2028.» - Ruben Hassid (newsletter "Master AI before it masters you"). Source: LinkedIn post 2026-09-21 (typesafe.ai Jev setup, newsletter https://lnkd.in/ePyG-QKM). Use: Article 28 / Jev wiki cross-link - Jev as internet-moment signal; hype-discount applies.
- «It's hard to spend more [than $5].» - Ruben Hassid on Jev free credit. Source: same post. Use: Jev wiki - 20-200x cheaper positioning, judgment primitives (choice/score/bool + calibrated confidence) vs LLM tokens.

## Jev / Judgment-as-a-service (Arseny Kravchenko, Staff AI/ML Engineer, 2026-09-21)

- «Jev isn't a technical revolution, but it's a masterclass in product design. ... It's certainly better than a raw zero-shot BERT, naive MNLI pipelines, or off-the-shelf open rerankers.» - Arseny Kravchenko (Staff AI/ML Engineer, author "ML System Design"). Source: LinkedIn post 2026-09-21 (full benchmark writeup: https://lnkd.in/dH5GNqcx). Use: Article 28 - packaging/positioning beats raw tech; judgment-as-a-service as product-moment signal, hype-discount.
- «The real win is product scoping: they carved out a precise, painful sub-task and wrapped it into a clean API.» - Arseny Kravchenko. Source: same post. Use: Article 28 / vendor-eval - why Jev (and verdict primitives) spread: scope carve-out, not model capability.
- «Packaging wins. A dedicated, non-generative "System 1" primitive sells the architectural idea of separation of concerns 10x better than another generic prompt template.» - Arseny Kravchenko. Source: same post. Use: Article 28 - dedicated primitive vs prompt template argument; supports "author can't be examiner" ([author]-vs-examiner) framing.
- «We just tested Jev against Sonnet 5 and open-weight models on 100 real agent tool calls ... (beating the 79% constant baseline is harder than it looks, and our entire API bill was $0.37).» - Arseny Kravchenko. Source: same post. Use: Article 28 / Jev wiki - independent benchmark, $0.37 cost anchor, 79% baseline caution (echoes our golden-dataset baseline discipline).

## Jev benchmark / Security-boundary evals (Archestra, Arseny Kravchenko, 2026-09-21 — full writeup)

- «A classifier with 75% accuracy is therefore worse than a few lines of code that always return "benign." That's the 79% constant trap.» - Arseny Kravchenko (Archestra). Source: https://archestra.ai/blog/we-tested-jev-on-100-real-agent-calls. Use: series baseline discipline (VerdictGate): prior 79% harmless => any eval must beat a constant, not just random-chance; same logic as our golden-dataset + "pretty tests" guardrail.
- «In security, errors fall into two buckets: Stalls (False Alarms) ... Leaks (False Negatives) ... blocking a safe call is inconvenient; allowing an unsafe one can expose data.» - Arseny Kravchenko. Source: same. Use: Article 20/26 - FP vs FN asymmetric cost on a boundary; mirror of our silent false negative (leak = FN with no alarm). Independent voice, security angle.
- «Rule one of model evaluation: don't let a model grade its own homework.» - Arseny Kravchenko (self-grading bias: models scored own answers 2-3 pts higher, Gemini gave itself 100%). Source: same. Use: Articles 26/27/28 - why "author can't be examiner"; LLM-as-a-judge must be independent + blind; direct evidence line.
- «Sonnet missed them all. It made eight errors on the strict set, and all eight were leaks.» - Arseny Kravchenko (outbound search = exfiltration channel; Sonnet searched = false). Source: same. Use: Article 20/26 - frontier model fails safely-silent: high accuracy, 100% of errors are FN = exactly our silent-green thesis at a real boundary.
- «Around 90 were routine, while only 10 covered the dangerous edge cases ... a model can score well by labeling almost everything as benign while still missing critical leaks.» - Arseny Kravchenko (bad benchmark: random sampling = class imbalance). Source: same. Use: Article 26 - eval dataset skew; sampling must overrepresent the dangerous minority, else score is cosmetic (echo of 20%->35%->45% claim caveat).
- «Labels hold, probabilities drift ... about 4 in 100 decisions change due to option order alone.» - Arseny Kravchenko (Jev reproducibility stress: repeat 394-398/400 identical labels; p-drift up to 0.17; order flips on 3-way labels). Source: same. Use: Article 27/28 - verdict primitives are only quasi-deterministic; version-stamp verdicts, treat confidence thresholds as fuzzy (echoes our SCORER_VERSION / frozen-bar).
- «If a model controls an execution boundary, inspect how it fails. The overall score does not show whether it fails safely.» + «we debug our AI harness on weak models on purpose. Weak models make problems in the evaluation easier to spot.» - Arseny Kravchenko. Source: same. Use: Article 26 closing-line candidate - macro score ≠ safe failure; weak-model harness-debugging = mutation-matrix intuition (break the harness first).

## Weak / degrading models as debugging instrument (Archestra, Arseny Kravchenko — "We Debug Our AI Harness on Weak Models on Purpose", 2026-07-20)

- «Premium AI models are the maxed-out MacBooks. They can bulldoze through bad plumbing ... and make the product look healthier than it is. ... The weak models are a better smoke alarm precisely because they're worse at compensating for our mistakes.» - Arseny Kravchenko (Archestra). Source: `submit_result` never tells the agent whether it was right - only whether the JSON parsed https://archestra.ai/blog/we-debug-our-ai-harness-on-weak-models-on-purpose. Use: Article 26/28 - green runs can be a disguise; test the harness on weak/degraded models first (mutation-matrix intuition: break the harness before trusting green); "old ThinkPad" as a QA metaphor.
- «A model that compensates for our bugs is still paying for them in retries, tokens, latency, and fragility. Hardening Chat against the weakest models is how we stop taxing the strongest ones. The test method and the business goal turn out to be the same thing.» - Arseny Kravchenko. Source: same. Use: Article 28 / VerdictGate - self-healing in AI agents = latent technical debt; hardening against worst case = free capacity for the best case. Closing-line candidate.
- «[A single weekly benchmark issue found] This human step is what turns 'the benchmark failed' into a real product improvement instead of an automated blame machine.» - Arseny Kravchenko (separate analyzer: benchmark never attempts root cause, analyzer never runs the product). Source: same. Use: Article 26/27 - verdict pipeline needs a human reviewer (attester), generator/judge separation mirror; AI-generated root-cause is hypothesis, not truth (echoes "author can't be examiner").
- «We don't record just pass or fail ... It's the difference between a number that shames you and a report you can actually use.» - Arseny Kravchenko (full visible trajectory: every message, tool call, file, artifact). Source: same. Use: Article 28 - evidence-pack over score; VerdictGate attestation trail; failure localization beats number.
- «Stop asking, 'Which premium model should we buy for everyone?' Ask, 'What's the cheapest model that can still handle our actual work?'» + «below roughly 70%, the wheels come off entirely» + open-weight $0.34 vs frontier $20-28 for a few percentage points. - Arseny Kravchenko. Source: same (26-task nightly, cost model cross-ranks; best open ~90% for <$1). Use: Article 26/28 - vendor-independent model strategy; capability cliff; our CCN/quality-drain argument, cost axis.

## Agent reliability / accountability (Tobia Lang, via Irueruoghene repost)

- «The real hurdle is not just building adaptive agents, but ensuring they can function reliably in real-world scenarios. Without structured evaluation and rollback mechanisms, we risk letting these agents operate in a chaotic environment where mistakes can spiral out of control.» - Tobia Lang (Full Stack Engineer, AI Interfaces). Source: LinkedIn repost via Irueruoghene Ogriki (2026-09-21). Use: Article 27 - eval + rollback = accountability framework, agent reliability not capability; supports VerdictGate/vendor-opinion lean. Note: author is individual engineer, 3rd-party quote - use with attribution or paraphrase.

## Career / Disruption (Jason Arbon + Filip Hric, STARWEST 2026)

Source: LinkedIn posts 2026-09 (Jason Arbon on Filip Hric; Filip Hric STARWEST main-stage promo). Context: STARWEST 20-25.09.2026 (TechWell) - Jason pitches meeting Filip as career ROI; Filip: "most important presentation of my career." Jason post URL: https://www.linkedin.com/posts/jasonarbon_starwest-activity-7500452550865801216-9GpJ (01.09.2026). Both Jason ("Testing with the Coding Agent", Thu 24.09, "should the system that wrote the bug also decide whether the software is ready to ship?") and Filip (keynote "Tester 2.0", Wed 23.09 10:00 + Thu 24.09 08:30) converge on generation-vs-validation separation = Victor's attestation lane.

- «AI is disrupting software testing—and careers. That's not hype. It's happening now.» - Jason Arbon (Jank.AI / IcebergQA). Use: Article 28/29 - disruption-as-career-opportunity framing; matches VerdictGate/attestation positioning (we are the emerging role).
- «This is a career opportunity, not just another conference session.» - Jason Arbon (on attending Filip Hric's talk). Use: Article 29/30 - STARWEST/career pivot angle; learning from practitioners beats vendor-slide-network.
- «I help developers make AI-written software reliable.» - Filip Hric (Qodo). Use: tagline benchmark for Victor's own positioning; Qodo = agentic coding vendor, reliable-AI-code = our verification thesis in one sentence.

## AI-QA Tooling / Career market (Codemify live + BitGN, 2026-09-22)

Source: Sergii Khromchenko (CEO & Founder @ Codemify | QA AI Automation) LinkedIn post 2026-09-22: free 2h live Sep 26 10:00 PT with Oles Tsaruk — Claude Code writes Playwright tests live (incl. its failures), CLAUDE.md, MCP for QA, AI+Jira, demo→CI/CD, "which skills are losing value." Rinat Abdullin (Founder @ BitGN | Verifying agents) talk at KanDDDinsky: "When DDD met AI" — DDD applied to three enterprise projects with LLM; URL: https://lnkd.in/dd2VvYBa.

- «Claude Code can now open a browser, go through checkout, and write a working Playwright test on its own. BUT: The better you know how to use AI, the more you're worth on the market.» - Sergii Khromchenko (Codemify). Use: Article 29/30 - the live-demo "where it gets things wrong, and it gets things wrong often" = our mutation-matrix verification terrain; "know how to use AI = worth" = skill-market justification for Victor's 101-beginner wiki stack (RAG/MCP/FastAPI/DB design).
- «We'll also talk honestly about the market: which skills are losing value, which are gaining, and whether it still makes sense to start with automation from scratch in 2026.» - Sergii Khromchenko. Use: Article 29 - skills-market pivot language; aligns with our displacement/reshuffle thesis (discipline survives contact).
- «[DDD helped] in three different enterprise projects with LLM under the hood.» - Rinat Abdullin (BitGN, "Verifying agents"). Use: Article 29/30 - enterprise LLM + domain modeling = reality; BitGN tagline "Verifying agents" = our attestation lane (independent verification of agents).
- «The only role that asks you anything.» / «Whatever is missing degrades honestly: no TMS and cases become markdown files, no autotests and the report says the step was skipped.» / «qa-manual verifies business effects on the environment and leaves evidence solid enough to automate from without re-checking.» - Vadim Glushonkov (Head of QA & AI QA Consultant | Self-learning Multi-agent testing | Fintech). Source: LinkedIn post 2026-09-17 (opened-source qa-cube, Claude Code plugin, MIT, github codecube01/qa-cube; how-it-works lnkd.in/eS3t2YCF, install lnkd.in/e8Zz75BD). Four roles: /qa (plans+asks), qa-analyst (cases pre-run → mismatch = product defect), qa-manual (evidence for automation), qa-automator (evidence → autotest, run to green). Retro edits engine's own instructions = self-learning loop. Use: Article 29/30 - role-separated agentic QA + honest degradation (missing capability = stated skip, not silent pass) = our verify-don't-claim thesis; evidence-solid-enough-to-automate = QAEverest/locator drift bridge; independent open-source (MIT) verification experiment candidate.

## Deterministic vs Probabilistic / Visual AI (Applitools webinars, 2026-09)

Source: https://applitools.com/upcoming-events/ (New Deterministic Agentic Workflow with Applitools Visual AI MCP Server, Adam Carmi, 24.09.2026; AI Testing Is a Coin Flip. We Fixed That., 15.10.2026).

- «Testing AI-generated code using standard LLMs burns through tokens fast. Prompting models to inspect UIs repeatedly drains your budget without guaranteeing layout accuracy.» - Applitools promo. Use: Article 29/30 - token waste of VLM-as-visual-checker; why deterministic visual verification beats re-prompting a vision model (our mutation matrix evidence framing).
- «Applitools Eyes MCP connects deterministic Visual AI right into your agent's chat or terminal so that your AI can actually see what it builds.» - Adam Carmi, Co-Founder & CTO, Applitools. Use: Article 27/29 - visual grounding inside the agent loop; "see what it builds" vs our "verify what the agent claims" - deterministic oracle as anti-hallucination layer.
- «Many AI testing tools promise 'magic,' but end up creating flaky tests that pass one day and fail the next.» - Applitools promo (Oct 15 webinar, Tim Hinds / Andrew Male). Use: Article 30 - flakiness of AI-generated tests; deterministic control / self-healing as differentiator.

## AI fear is hype / engineering-not-pause (Andrew Ng, Andrew's Letter, The Batch #371, 2026-09-18)

Source: https://www.deeplearning.ai/the-batch/issue-371 (ng's letter), https://lnkd.in/e7u2G_5b. Context: Ng pushes back on 2-week orchestrated fear campaign (OpenAI swarm hack on Hugging Face, PR hype). Counter-narrative for our series: fear ≠ reasoned risk management; fix bugs & monitor, don't pause.

- «I don't see any step up in the risk of human extinction from AI compared to a few months ago. ... The most notable recent event leading to increased fear was when an OpenAI team deployed an agent swarm that hacked into Hugging Face ... some publications reported that a swarm of 1,200 agents carried out the attack. While this was technically accurate, as I write this, I have about 1,300 processes running on my laptop.» - Andrew Ng. Use: Article 26/28 - de-mystify agent counts; many parallel processes is not a magical capability; our "agents as processes" framing.
- «OpenAI's buggy sandboxing and monitoring processes were key to enabling this incident. Fixing these bugs and putting in place improved monitoring would be appropriate fixes, not pausing AI.» - Andrew Ng. Use: Article 26/28 - harness bugs (sandbox, monitoring) are the root cause, not the model; fix engineer, don't pause — echoes Archestra weak-model debugging (harness-first) + our mutation-matrix.
- «AI agents are relentless. They will tirelessly try many tactics — and have the patience to chain vulnerabilities together ... But in the long term, I believe the advantage will lie with defenders (because they have more information with which to identify bugs, which they can fix).» - Andrew Ng. Use: Article 28 closing-candidate - defenders win long-term because they know their own bugs; supports attestation/testing-as-defense + our vendor-independent QE role.
- «If I wield a hammer, miss a nail, and accidentally dent the wall, it's not the fault of the hammer. ... if I prompt an agent and it hacks into someone else's system, the responsibility lies with me, not the agent.» - Andrew Ng (anti-anthropomorphization; tool vs user responsibility). Use: Article 27/28 - liability framing for AI agents; human at the seams owns the outcome; counter "the robot did it" defense.
- «One new element in the forecasts of AI-enabled doom is AI companies disclaiming responsibility for their own products. 'I didn't do it; my out-of-control agent did!' ... let's hold the people building and/or using the hammer responsible, rather than the hammer.» - Andrew Ng. Use: Article 27/28 - "responsibility loop"; attestation layer mandates accountable release sign-off; an insulated AI company = an untested one.
- «Pausing AI progress will create much more harm than benefit. First, our adversaries will certainly not slow down. Second, engineering requires discovering problems empirically so we can fix them.» - Andrew Ng. Use: Article 26/28 - discovery needs runs; stop-the-world = stop finding defects; mutation/evidence culture requires shipping + observing.

## Honest QA tools / undiscovered vs uncovered (FlowScout thread — Igor Akymenko, Paul Kanaris, Sarang U., 2026-09-22)

Source: LinkedIn thread (post + replies), Igor Akymenko (Alternate QA / FlowScout) + Paul Kanaris (QACE Institute) + Sarang U. (Thinkproject). Repo: https://github.com/igorakymenko-create/FlowScout. FlowScout = open-source Apache-2.0 Playwright crawler (discovery layer, no invented expectations, honest CAPTCHA), our live W3 pilot. Direct hit for Articles 26-28.

- «Most 'AI testing' tools ask you to trust them. I built one that shows its work instead.» / «That's a narrower promise than 'AI writes your tests for you.' I think it's a more honest one.» - Igor Akymenko. Use: Article 26/27 - honest-vs-hyped vendor framing; "show its work" = verifiable evidence over claims; VerdictGate language.
- «FlowScout never invents an expected result and never asserts anything about data correctness. It only reports what it can verify by actually clicking through the app - which flows exist, which are covered, which aren't.» - Igor Akymenko. Use: Article 26/27 - discovery layer ≠ verdict layer; absence of invented expectations = our mutation-matrix "no assertion -> broadest" rule in practice; sober/literal (Bolton/Bach) as product ethos.
- «How do we distinguish between undiscovered behavior and uncovered behavior? ... some of the highest-risk workflows are often the least documented, least understood, and least visible to automated discovery approaches.» - Paul Kanaris (QACE Institute). Use: Article 27/28 - discovery completeness ≠ coverage; silent-unknown risk; the question article series must answer (mutation matrix measures what we can see, not what's invisible).
- «FlowScout's claim isn't 'we found everything the system can do.' It's narrower and precise: 'here is what this identity could reach, in this system state.' That's a checkable statement with a defined boundary, not a hopeful one.» - Igor Akymenko. Use: Article 27/28 - bounded claims = testable claims; persona/state scoping is how you say something precise; supports our per-risk-tier + evidence framing.
- «A feature flag that's off definitionally means 'this doesn't exist for this user'; reporting it as absent is right, not blind.» - Igor Akymenko. Use: Article 27 - environment/access defines existence; absent ≠ undetected; counters "false negative" hyperbole with proper conditioning.
- «Two things I do think are real ... A run's conditions have to be visible in the report itself - which persona, which config, which seeded URLs, which limits. A not_found is always relative to those; if the report doesn't say so on its face, it reads as more absolute than it is.» - Igor Akymenko. Use: Article 28 / VerdictGate - evidence-pack must carry run context; a bare score without conditions is misleading; attestation trail.
- «Employee submits -> manager approves -> employee sees the result. Personas crawl sequentially and independently; there's no coordinated handoff between them. One super-user can't reproduce it, because the flow needs two actors in sequence.» + «'Activate account', 'consume this token', 'final approval' can't be re-walked against the same backend entity.» + time-dependent flows - Igor Akymenko (his genuine unsolved residue: multi-actor handoffs, one-shot irreversible transitions). Use: Article 27/28 - honest tooling admits its boundary; multi-actor/irreversible = Agentic QA research gap we can claim.
- «pointed it at my own portfolio site and it actually caught something real: a full-page overlay from a fade-in animation with pointer events: auto left on, silently sitting on top of my nav links and blocking clicks ... it didn't invent a bug, it found a real one and told me precisely why.» - Sarang U. (Thinkproject, tested FlowScout on real site). Use: Article 26 - honest discovery finds real defects (reproducible, explainable), evidence over invented findings; live counter-example to "AI just invents bugs".
- «The lab tested the engine. But they have not tested your car.» - Igor Akymenko (LinkedIn post 2026-09-24, Accenture+Anthropic embedded evaluators). Use: Article 24 — lab evals certify the model, nobody certifies YOUR deployment; engine vs car = eval vs gate.
- «A safe model can still give your customer the wrong refund policy. ... It can still pass every lab eval and fail the one question your business actually runs on.» - Igor Akymenko, same post. Use: Article 24/26 — generic-green vs business-critical miss; the decoy thesis restated by a vendor.
- «Who owns the "can we ship this?" decision for your AI feature? And what is it based on?» - Igor Akymenko, same post. Use: Article 24 — accountability question as closer; named owner + falsifiable evidence.

## QA as architecture custodian / fitness functions (Tiago Gomes, Thoughtworks, 2026-09-20)

Source: Tiago Gomes (Lead Consultant @ Thoughtworks, Global Speaker/Mentor). Article: https://www.linkedin.com/pulse/qa-evolutionary-architecture-tiago-gomes-hhf5f/ — "QA and Evolutionary Architecture." Revisits his 2024 article ("QA as a Key Driver in Evolutionary Architecture") about how fitness functions help teams protect the architectural qualities that matter; Thoughtworks authors: Neal Ford, Rebecca Parsons, Patrick Kua, Pramod Sadalage (Building Evolutionary Architectures), Sensible Defaults.

- «A fitness function is an automated and measurable way to verify whether a system is still meeting an architectural expectation. It gives our teams feedback about whether the architecture is moving in the direction they intend, or quietly drifting away from it.» - Tiago Gomes. Use: Article 26/29 — fitness functions = architectural verification layer, continuous not gate; direct bridge to per-risk-tier (which qualities are essential for THIS product).
- «The value is not in adding a long list of checks to a pipeline. We have all seen pipelines that produce plenty of information but very little insight. The value comes from choosing signals that represent what our clients genuinely care about. ... A fitness function should answer a meaningful question. If it fails, the team should understand why it matters and what decision needs to be made. Otherwise, it becomes just another warning that people learn to ignore.» - Tiago Gomes. Use: Article 27 — checks ≠ verified qualities; noise-free evidence principle matches our mutation-matrix "assertion matters, not coverage count" and Klain "more tests ≠ better testing".
- «Not every fitness function needs to be a strict gate from the beginning. Sometimes the right first step is simply to make a concern visible. ... Once [the team] understands the baseline and agrees on what acceptable looks like, it can decide how to act on that information.» - Tiago Gomes. Use: Article 29 — staged gating (visibility → baseline → gate) = our per-risk-tier B0-B3 ramp, independent convergence with QAEverest framework.
- «Quality is contextual. There is no universal threshold that makes every system good... the more useful question is: which qualities are essential for this product, these users, and this business moment?» - Tiago Gomes. Use: Article 27/29 — context-dependent thresholds, directly supports per-risk-tier (a payment platform and an internal reporting app cannot share one bar).
- «Some architectural characteristics can only be understood in production. We can test resilience before release, but how does the system behave under real traffic? ... A system that cannot be understood in production is difficult to evolve safely.» - Tiago Gomes. Use: Article 28/29 — production observability as verification; QA extends past release; aligns with DORA/observability metrics.
- «Perhaps that is the real opportunity for QA in Evolutionary Architecture. Not to become a gatekeeper of quality, but to become a facilitator of better conversations, clearer signals, and faster learning.» - Tiago Gomes. Use: Article 29 — QA as signal-facilitator not gatekeeper (contrast vs our attestation gate — complementary: they make quality visible, we make it independently verifiable).

## Independent verification layer / generator vs grader (Qodo blog, 2026-06..08)

Source: https://www.qodo.ai/blog/why-your-ai-coding-agent-shouldnt-review-its-own-code-the-case-for-an-independent-verification-layer/ + https://www.qodo.ai/blog/when-claude-code-reviews-its-own-pr-who-reviews-claude/ + https://www.qodo.ai/blog/ai-gave-teams-velocity-the-governance-harness-comes-next/ + https://www.qodo.ai/blog/ai-slop-is-a-governance-problem-here-are-4-principles-to-fix-it/ + https://www.qodo.ai/blog/building-the-verification-layer-how-implementing-code-standards-unlock-ai-code-at-scale/. Qodo (ex-Codium, PR-Agent→Qodo Merge, Qodo Gen) = AI code quality & governance platform; Gartner names it Example Vendor in Code Review Agent category (Shiva Varma, "Don't Use AI Coding Agents for Every Software Engineering Task", 2 Jun 2026). 5 articles ingested to wiki (qodo-*-2026).

- «When a model repeatedly refined its own output with no outside check, critical vulnerabilities rose by more than a third after just five rounds.» - Qodo blog, citing Shukla et al. arXiv:2506.11022 ("Security Degradation in Iterative AI Code Generation"). Use: Article 27/28 - author-can't-be-examiner, empirical basis; independent verification layer needed, not better prompting.
- «It can produce a review. The harder question is whether you should rely on the same system to both generate code and verify it. The answer, increasingly backed by analysts and by how mature engineering orgs actually operate, is no.» - Qodo blog. Use: Article 26/27 - generator/grader separation; analyst + practice alignment.
- «95% of developers now review AI-generated code with more scrutiny, even as their confidence in that code keeps rising.» - Qodo 2026 survey (500 engineers/leaders). Use: Article 27 - caution and confidence climbing together; trust gap persists even as skepticism rises (parallel to Gulin retain-on-failure).
- «If you can't explain why code shipped, you introduce liability.» - Qodo blog ("AI Slop Is a Governance Problem"). Use: Article 27 - auditability as requirement, not amenity; our evidence-pack framing; liability equation.
- «You can't govern what you don't measure.» + «70.7% of the developers we surveyed are not measuring the impact of AI on code quality.» - Qodo blog. Use: Article 27 - measurement-first governance; mutation matrix as the instrument.
- «I don't treat code review as a courtesy or a checkbox. I treat it as a boundary: the moment responsibility re-enters the system.» - Qodo blog, principle #2. Use: Article 27/28 - review = responsibility boundary; per-risk-tier gate.
- «89% [of orgs] experienced AI-related incidents in production» vs «3.7% say their processes keep up» — Qodo State of AI Code Quality 2026 (n=800, Censuswide, adopter sample, US-only; vendor report — Qodo sells review tooling). Use: Article 30/31 — incident/process gap as market evidence; cite sample limits.
- «Review/validation is the top bottleneck (26% both audiences)» + «34.7% at 500+ employees vs 9.3% at 50–99» — same report. Use: Article 30/31 — verification pain scales with codebase size; per-risk-tier intensity argument.
- «Trust tax» 36.4% + enforcement gap 34.6% — same report. Use: Article 30/31 — named market terms for our gate doctrine; vendor coinage, use with attribution.
- «The same system that writes the code shouldn't grade its own homework.» - Qodo blog. Use: Article 22/27 - author/examiner separation, independent attestation (Rupesh attestation framing).
- «The maturity advantage disappears at AI scale.» - Qodo blog citing Faros AI Engineering Report 2026 (22,000 devs, 4,000 teams: incidents per PR +242%, time in review +441%, bugs per developer +54%). Use: Article 26/27 - process/maturity no longer protects at AI velocity; structural governance needed; destroys "we're disciplined so we're fine" objection.
- «A coding agent without governance is not just a quality risk. It's an open-ended execution loop with production and financial impact.» - Itamar Friedman (Qodo CEO). Use: Article 26 - runaway spend (Uber burned AI budget in 4 months) = first visible symptom of governance gap; cost-of-runaway story.
- «The question is not whether automation is possible. The question is whether it preserves or erodes trust.» - Qodo blog, principle #4. Use: Article 26 - automation must amplify discernment; "checking out" anti-pattern.
- «One silent threshold away from shipping invisible vulnerabilities.» / «Claude Code optimized for confidence. Qodo optimized for code integrity.» - Qodo blog (Claude Code self-review experiment). Use: Article 26/28 - live empirical demonstration: Claude Code's judge scored, thresholded (below-80 filtered) and suppressed a TOCTOU security bug; Qodo surfaced it as Action Required. Confidence-optimized grading = silent false negatives; verdict-layer stakes.
- «If your architecture lets the same agent be architect, implementer, and sole judge, you are one silent threshold away from shipping invisible vulnerabilities.» - Qodo blog. Use: Article 28 - the exact stakes of attestation; external independent reviewer boundary.
- «The spec is the source of truth. The code is generated. Verification is the craft.» - Qodo blog (Snyk Field CTO Clinton Herget quote inside). Use: Article 27 - spec-driven development; verification as craft/grade skill (10x engineer = ships fast while maintaining quality).
- «To increase autonomy, you have to increase verification.» - Dedy Kredo (Qodo CPO). Use: Article 26/27 - autonomy/verification ratio; the law our per-risk-tier gates operationalize.
- «We're saying the code is disposable. The actual important part of the development process is the set of prompts that define the functionality.» - Clinton Herget (Field CTO, Snyk), quoted by Qodo. Use: Article 27 - spec as durable artifact; prompt/spec is the code of AI-era.
- «Do we believe the user can handle graded risk? ... A UI that shows you one filtered issue and a green checkmark is telling you, 'Trust me, it's fine.' A UI that shows you severity, type, and remediation is telling you, 'Here is the map. You decide where to go.'» - Qodo blog. Use: Article 26 - grader UX encodes a worldview; silent filtering vs surfaced risk gradient = our verdict/evidence difference.

## Virtuoso / Touchstone + coverage (Andrew Doughty, Rishabh Kumar, 2026-09)

Source: Virtuoso QA blog — Touchstone manifesto https://www.virtuosoqa.com/post/introducing-touchstone (30.09.2026) + GSI post https://www.virtuosoqa.com/post/ai-and-the-future-of-services (28.09.2026) + coverage post https://www.virtuosoqa.com/post/code-coverage-testing (08.09.2026). Virtuoso = codeless test automation vendor; W5 verdict: coverage post is an ally (type #5 prescribes "Pair Coverage With Mutation Testing", coins "assertion density"); residual gap everywhere: nobody mentions checking the checker.

- «A test can pass and still tell you very little. A thousand tests can pass and still miss the thing that matters.» — Andrew Doughty, Touchstone manifesto. Use: Article 31/RMT note — vendor-voice confirmation of our false-PASS spine; quotable ally line.
- «What do we need to prove before we trust this software?» — same. Use: Article 31 — proof-before-trust framing in vendor's own words; calibration-gate epigraph.
- «AI makes production abundant. Trust becomes scarce.» — Andrew Doughty, GSI post. Use: Article 31 — scarcity-of-trust thesis; market-level why for independent verification.
- «Selling confidence that a release is safe rather than 50 testers.» — same. Use: Article 31 — buyer language for attestation (confidence-as-product, headcount irrelevance).
- «Coverage without assertion: a test that calls a function and checks nothing produces coverage and proves nothing.» — Rishabh Kumar, coverage post. Use: Article 31/RMT note — assertion-density ally quote; coverage≠proof in vendor's own doctrine (hook: "92% coverage. Green build. Shipped Thursday. Broke Friday").

## Second curve / crystallized intelligence (Arthur Brooks, From Strength to Strength 2022)

Source: Arthur C. Brooks, From Strength to Strength: Finding Success, Happiness, and Deep Purpose in the Second Half of Life (2022). Quote cross-checked across Goodreads + psychiatry review + Thinkr (verbatim match, 2026-09-24). Not read from book copy - treat as secondary-source verified.

- «But if your career requires crystallized intelligence — or if you can repurpose your professional life to rely more on crystallized intelligence — your peak will come later but your decline will happen much, much later, if ever. And if you can go from one type to the other — well, then you have cracked the code.» - Arthur C. Brooks. Use: leadership positioning - repurpose toward judgment/mentoring/attestation (crystallized) instead of hands-speed (fluid); second-curve career framing.
- «A judge that went blind this morning still looks fine in last month's numbers.» - Igor Akymenko (LinkedIn thread 2026-09-25, reply to Victor). Use: Article 24/26 - kill-shot vs trailing-accuracy dashboards; per-run verification over monthly metrics.
- «You test the tester before you trust anything it says.» - Igor Akymenko, same thread (adopting Victor's decoy-first method for FlowScout work). Use: Article 26 - vendor-founder verbatim adoption of seeded-decoy doctrine.

## Build-in-public practitioners (Quality Minder, dev.to 2026-09-25)

Source: Katja (quality_minder), "Building an AI QA Agent That Tests Your Jira Tickets in a Real Browser", Quality Minded community (Montenegro → USA, open source: Agent Factory + BaaS). https://dev.to/quality_minder/building-an-ai-qa-agent-that-tests-your-jira-tickets-in-a-real-browser-3pc7

- «Keep humans on the loop and don't ship on Fridays!» - Katja. Use: flavor closer; human-on-the-loop in practitioner wording (matches our Article 27 thesis language).

## Escalation is not monotone (Tom Jones, Tirtha.ai, 2026-09-25)

Source: https://dev.to/tom_jones_230c4659491adcd/escalating-to-the-better-model-made-34-answers-worse-ko7 (2,400 tasks × 3 reps, cheap vs frontier side by side).

- «Escalation fixed 133 answers and broke 34.» - Tom Jones. Use: escalation economics; bigger model = different failure distribution, not fewer failures.
- «Verify rather than select, because a cheap answer that passed a check is worth more than an expensive answer nobody checked.» - Tom Jones, same. Use: Article 26/28 — verification over selection; checks beat escalation.

## CodeScene AI Series Hub (2026-09, research + cases)

Source: https://codescene.com/ai-series-hub/welcome (stats + loveholidays/Alfa Laval cases).

- «At least 60% defect risk when agents operate on unhealthy code.» - CodeScene research. Use: pre-seed relevance gate; unhealthy code × agents multiplier.
- «35-45% token waste when agents operate on unhealthy code.» - CodeScene research. Use: cost argument for code health before agent scale.
- «How code health, deterministic quality gates and human-on-the-loop checkpoints turn AI speed into something you can trust, and why QA's job shifts from running tests to being the one who signs off on going to production.» - CodeScene (Ch.3 framework). Use: Article 27 — independent convergence (their words, our thesis).
- «Putting these hard guardrails in place was the game changer, forcing the agent to build the code at the structural quality that we wanted, and brought the code health back up.» - Stuart Caborn, Distinguished Engineer loveholidays (80% agentic code at elite health). Use: guardrails-as-enforcement, Tornhill tooling-enforces resonance.

## Human owns, agent executes (Daniel Sayer, Deskpro, 2026-09-25)

Source: https://www.linkedin.com/pulse/meet-terry-tester-get-ai-do-grunt-work-keep-humans-judgement-sayer-gapce/ (Claude Code QA skills + Linear bot Terry Tester; deterministic script-computed gate).

- «Automation that marks its own homework isn't QA.» - Daniel Sayer. Use: Article 26/27/28 — self-grading prohibition; verdict must be script-computed, not agent opinion.
- «The shift is from doing the testing to owning it.» - Daniel Sayer, same. Use: Article 27 — QA promoted to owner/sign-off; converges with CodeScene sign-off line.

## Lightweight vs frontier (Fastino Labs, 2026-09-25)

Source: Julia White (Head of Research @ Fastino Labs, Stanford PhD), LinkedIn post on Jev + GLiNER (demos/weights via lnkd.in links in post).

- «How competitive smaller, well-applied models are against much larger systems on these exact use cases.» - Julia White. Use: Article 28 / Jev note — small-models-competitive thesis from a labs researcher; supports our mini-jev local results (76.7% @ $0).
- «Every model is yours to host, train, and run locally on your own hardware.» - Fastino Labs open-weight philosophy, same post. Use: local-first judging argument; open weights vs proprietary Jev framing.

## Anton Gulin (ex-Apple, AI QA Architect — standing source on eval hygiene, series of 4, 2026-09-25/28)

Source: LinkedIn posts (1st connection; first three owner-paste verbatim ⚠️, fourth fetched live ✅).

- «A check for 'contains 60' would accept both A and C. A check for one exact sentence could reject A for harmless wording changes.» - Anton Gulin (scoring-sheet post). Source: https://www.linkedin.com/posts/antongulin_aiqaarchitect-activity-7509341085056307200-29_H (verified live, verbatim ✅). Use: Article 31 — exact-match vs judge; our B0 case-insensitive debate in vendor wording.
- «If you disagree, find the unclear rule before adding more examples.» - Anton Gulin, same. Source: same (verified ✅). Use: Article 31 — our W2 arbitration (E3) as field practice; disagreement locates the rule.
- «For your next AI finding, ask for the smallest input that exposes the problem. Keep the expected result, actual result and test limits beside the fix.» - Anton Gulin (path-separator post). Source: https://www.linkedin.com/posts/antongulin_aiqaarchitect-share-7508978690018631680-FHn_ (verified live, verbatim ✅). Use: Article 29/31 — one mutant = minimal input; verdict + limits beside fix = our RMT protocol.
- «You can show which condition you checked, instead of arguing with its wording.» - Anton Gulin, same. Source: same (verified ✅). Use: Article 31 — arbitration via conditions, not wording (E3 lesson, third external confirmation).
- «"Fixed" tells the reviewer very little.» - Anton Gulin, same. Source: same (verified ✅). Use: lineage-not-belief for AI fixes.
- «Closing the browser does not delete the order your test created.» - Anton Gulin (cleanup post). Source: https://www.linkedin.com/posts/antongulin_aiqaarchitect-share-7509643041553637377-n_Nn/ (owner-paste verbatim, link live-resolving ✅). Use: test-hygiene angle; fixture cleanup + deliberately-fail-to-verify practice.
- «What could the old check miss? What did you decide to check instead? What evidence supports that decision? What remains untested?» - Anton Gulin (portfolio-decisions post). Source: https://www.linkedin.com/posts/antongulin_aiqaarchitect-share-7510005459987222528-iijG/ (verified live ✅). Use: Article 31 — 4-question evidence structure mirrors our evidence contract (miss/decision/evidence/untested).
- «Evidence: remove the dark styling rule on purpose.» - Anton Gulin, same. Source: same (verified ✅). Use: deliberate-break evidence as portfolio practice; mutation thinking for career.

## Arseny Kravchenko (Staff AI/ML, "ML System Design" — routing-cost experiment, Archestra, 2026-10-05)

Source: LinkedIn post (verified live ✅) + Archestra writeup (fetched full ✅).

- «Task complexity doesn't live in the prompt text. It lives in repo state, cache dynamics, and how the task drifts 5 turns in.» - Arseny Kravchenko (LinkedIn post). Source: https://www.linkedin.com/posts/arsenyinfo_routing-coding-agents-is-harder-than-it-looks-activity-7512824926328922112-9cW2 (verified live ✅). Use: verdict-economics — cost lives outside the prompt; routing-by-text blind spot.
- «Per task, a quarter of the work is cheap. Per dollar on an interactive agent, a quarter of the sessions is a rounding error.» - Arseny Kravchenko, same writeup. Source: https://archestra.ai/blog/routing-coding-agents-on-the-cheap (fetched full ✅). Use: ledger rows — session-count vs dollar-weighted scoring; denominator honesty.
- «A gate like cargo test isn't an oracle when deleting the test also makes it pass.» - Arseny Kravchenko, same. Source: same (verified ✅). Use: mismatch-detector family; agreement-with-itself is not an outcome.

## Bas Dijkstra (On Test Automation — "Evidence builds trust" newsletter, 2026-10-05)

Source: newsletter email (owner-paste, full text on file).

- «Evidence builds trust, but it shouldn't make you blind to problems.» - Bas Dijkstra. Use: evidence doctrine with anti-blindness caveat; our evidence-layer thesis in one line.
- «Demonstrate that the test can detect meaningful changes in application behaviour (for example using mutation testing).» - Bas Dijkstra, same (on proving auto-tests earn their keep). Use: mutation testing as evidence-of-value, named by an external trainer; matrix-adjacent.

## Ekaterina Semenova (UrsaMinor pilot — judge doctrine, CONSENT GRANTED 06.10, VERBATIM STILL PENDING)

Source: W4 relay 05.10 (paraphrase only); charter signed 06.10 (owner report) — publication consent GRANTED per charter terms.

- «качество судьи = качество expectation» (PARAPHRASE, not verbatim ⚠️) - Ekaterina Semenova, via W4. Use: HOLD as paraphrase only — upgrade to quotable needs exact verbatim line (request it). Consent no longer blocks; precision does. Do not publish until verbatim recorded here.

## Escape hooks (Victor Ematin, Pulse "Our Suite Went Green on Someone Else's Website", 06.10)

Source: https://www.linkedin.com/pulse/our-suite-went-green-someone-elses-website-victor-ematin-ijywe/ (verified live ✅ 06.10 — W4 relay, all four verbatim in article).

- «Our suite went green on someone else's website.» - Victor Ematin (H1/hook). Use: escape-story hook; agent tested unassigned target.
- «Four out of four SUCCESS — against a target we never assigned.» - Victor Ematin, same (feed variant). Use: green-against-wrong-target in one line.
- «Memory, it turns out, is another place a boundary has to live.» - Victor Ematin, same (memorable line). Use: route-persisted-in-memory finding; boundary taxonomy.
- «Guards are claims until a red team measures them.» - Victor Ematin, same (culture one-liner, W1/W2 endorsed). Use: guard-skepticism thesis; pairs with no-op rule and mismatch detector.

## Daily Agentic 10.5.26 (Agentic AI Foundation, 19.5K followers, 06.10)

Source: owner paste (Pulse URL guest-unfetchable — paste-only ⚠️): https://www.linkedin.com/pulse/tiktok-tells-agents-buy-baby-kolibri-says-ai-chtung-trspc/

- «To understand you, an agent inevitably learns about us.» - Daily Agentic (on Muse auto-profiling friends into "person pages"). Use: memory-moat flip side — next privacy fight is what somebody else's agent knows about you; agent accountability angle.
- «Agents can increasingly be handed a question and figure out how to investigate it.» - Daily Agentic, same (on Swarmchasers Amap fleets, Tencent Cloud, vs Hugging Face swarm). Use: agentic intel-gathering exhibit; rogue-line adjacent (agents acting in the wild).

## Jay Aigner verification-harness post (06.10)

Source: https://www.linkedin.com/posts/jayaigner_a-cto-told-me-something-i-cant-stop-thinking-activity-7513273267671977985-agSR (verified live ✅ 06.10 — post + comments verbatim).

- «AI agents will make every test pass, whether the product works or not.» - Jay Aigner. Use: green-suite devaluation thesis; rogue-line adjacent.
- «A verification harness is a contract between your product and your agents. If the code breaks it, it doesn't ship.» - Jay Aigner, same. Use: harness-as-contract framing; ownership doctrine.
- «Agents optimize for the pass, not the product, so a green suite only tells you the harness was satisfied.» - Aston Cook (comment). Use: pass-vs-product split; criterion-rot family.
- «Frontier models are notorious for trying to please and bend reality to the expected outcome.» - Don Norbeck (comment). Use: sycophancy-as-failure-mode; judge-pleasing warning.

## Addy Osmani agent self-checks (Anthropic, "Writing High-Quality Tests for AI Agents", 06.10)

Source: https://lnkd.in/p/ej2wPrxn (verified live ✅ 06.10 — post 1402 reacts/118 comments + thread verbatim).

- «Example tests say what should happen; properties say what must not.» - Addy Osmani. Use: example-vs-property split; prohibitions as the strong form.
- «The agent may learn to retry, not fix the problem.» - Addy Osmani, same (on slow/unreliable loops). Use: retry-vs-fix gaming; loop-speed perverse incentive.
- «Keep a few acceptance checks that the implementation agent can't rewrite... run [the test] against the broken version first, so we know it catches the actual failure before trusting the green result.» - Jonah Gray (comment, verified ✅). Use: immutable checks + mutant-first; our pre-reg doctrine in the wild.
- «A separate agent... mimics a real end user, without knowledge of the actual implementation.» - Shaikh Quader (comment, verified ✅). Use: independence via separate model + spec-only access; examiner-can't-be-author.
- «The cheapest check I added needed no model at all... A model as judge was only worth it where a rule could not decide.» - Arian Z. (comment, verified ✅). Use: rules-before-judges cost hierarchy; deterministic-first doctrine.
- «Tests tell me the task was done right, but not whether the agent stayed inside the task... the diff size being a signal too, next to the tests.» - Marcin I. (comment, verified ✅). Use: scope-check/blast-radius signal beside pass-fail; green-with-stray-diff suspicion.

## Slawomir Radzyminski e2e framework eval (awesome-testing.com, 02.10.2026)

Source: https://www.awesome-testing.com/2026/10/agentic-e2e-testing-actions-assertions-and-cost (fetched full ✅ 07.10 — 302-test migration, 95 AI assertions, 19-error mutation probe).

- «An assertion should be tried against an incorrect result as well as a correct one.» - Slawomir Radzyminski. Use: mutation doctrine from independent practitioner; try-against-wrong-result rule.
- «I would not turn the final result into a claim that AI assertions are 100% reliable.» - Slawomir Radzyminski, same (after 38/38 post-fix). Use: anti-overclaim honesty; small-experiment humility.

## Anton Gulin separate-accounts (12h, browser-vs-server)

Source: https://lnkd.in/p/eqv9jDh6 (verified live ✅ 07.10).

- «The useful distinction is where the change lives: in the browser, or on the server?» - Anton Gulin. Use: parallel-test isolation rule; Sam-vs-Lee display-name race as exhibit.

## Breaklight positioning (site + Insights, verified live 07.10)

Source: https://breaklight.ai/ (verified live ✅ 07.10).

- «A dashboard that scores prompts is not a red-team tool. Measurement is not assurance.» - Breaklight Insights. Use: measurement-vs-assurance split; dashboard ≠ red-team.
- «Name what you are testing first: Model, prompt layer, retrieval, end-to-end, agent trajectory, production. Six different objects.» - Breaklight Insights, same. Use: test-object taxonomy; scope-before-method.

## Rogerio Chaves Decisions-vs-Jev (LangWatch benchmark, verified live 07.10)

Source: https://lnkd.in/p/ebQR5WkA (verified live ✅ 07.10 — post verbatim; full benchmark: langwatch.ai/benchmarks/jev-alternatives).

- «Jev-class models including Decisions API still mostly fails on checks where the answer has to be derived... they don't think before it answers.» - Rogerio Chaves (sic — grammar as posted). Use: derived-answer blindness; no-think-before-answer limit.
- «For the same amount of money you can run more than twice as many evals with Jev... best for its price range.» - Rogerio Chaves, same (Decisions +11pts accuracy, ~2x speed). Use: judge cost-effectiveness; accuracy-vs-evals tradeoff.

## Imran Ali morning-screen (ClinVerify, HealthTech regulated — verified live 07.10)

Source: https://www.linkedin.com/posts/imran-ali-aitestgroup_the-agent-runs-the-tests-on-the-app-heres-share-7513508835651805184-YZG_/ (verified live ✅ 07.10 — 4 questions verbatim; replies = owner-paste ⚠️).

- «A red result is only real once a person has looked.» - Imran Ali. Use: human-reading doctrine; red-is-claim-until-read.
- «Coverage, not pass rate.» - Imran Ali, same (DCB0129 80% / FDA 84% / GDPR 83% beside hazard log + safety case). Use: framework-linked coverage; sign-off context.
- «It handles the running, the evidence and the traceability, but it doesn't handle the judgement... a failed run is only real once someone has read the agent's reasoning and agreed.» - Imran Ali (reply to Sajid Manzoor). Use: engine-runs/people-decide split; generated-cases-are-drafts.

## Anton Gulin first-agent-task (verified live 07.10)

Source: https://www.linkedin.com/posts/antongulin_lets-give-an-ai-agent-its-first-testing-ugcPost-7513568913612341248-fRSq/ (verified live ✅ 07.10 — post verbatim; article: anton.qa/blog/posts/first-agent-task).

- «For a first task, a clear failure is a useful result.» - Anton Gulin. Use: first-task doctrine; clear failure beats vague green (onboarding agents to testing).
- «Tell it to stop before changing the helper.» - Anton Gulin, same (inspect + report exact result, no fix). Use: finding-before-fix rule; report-gaps-first family (no repair inside the probe).

## Tatyana Arbouzova self-healing intent (13h, verified live 07.10)

Source: https://lnkd.in/p/giuVVans (verified live ✅ 07.10 — post + Gulin comment verbatim).

- «A good AI agent shouldn't be trying to make the test pass. It should be trying to preserve the intent of the test.» - Tatyana Arbouzova. Use: anti-green-chasing doctrine; healer purpose statement.
- «The goal of self-healing isn't fewer red tests. It's less maintenance without losing test intent.» - Tatyana Arbouzova, same (95% locator vs 75% label vs dead-button-is-bug ladder). Use: confidence-tiered healing; human-final-say rule.
- «A button that stops opening the form belongs in the bug tracker.» - Anton Gulin (comment). Use: heal-vs-file triage rule; label-murky-middle + confidence + human look.

## Isha Sharma QA mindset (Pulse 05.10, numbers verified live 07.10)

Source: https://www.linkedin.com/pulse/qa-mindset-isha-sharma-15h1c/ (verified live ✅ 07.10 — Veracode 45%, CodeRabbit 10.83 vs 6.45, logic +75%).

- «When AI writes both the code and the tests from the same spec, they share the same blind spots.» - Isha Sharma. Use: same-spec blindness; examiner-can't-be-author, practitioner formulation.
- «A tester who only watches the green tick is not doing quality assurance. They are reading a report.» - Isha Sharma, same. Use: green-tick ≠ QA; verdict-reading vs verdict-making.
- «Treat the pipeline as a safety net, not the final judge.» - Isha Sharma, same. Use: pipeline-position doctrine; net-not-judge.
- «QA is not a button. It is judgment.» - Isha Sharma, same. Use: judgment thesis one-liner.

## Paul Kanaris decision-without-feedback (post 21h, verified live 07.10)

Source: https://lnkd.in/p/g6FmFsZm (verified live ✅ 07.10 — full text matches owner paste verbatim).

- «Without feedback, we can become very experienced at making decisions while repeatedly learning very little from them.» - Paul Kanaris. Use: experience-without-learning; feedback-loop thesis (org twin of survived-mutants-never-reviewed).
- «Reality still gets a vote.» - Paul Kanaris, same (Decision → Outcome → Evidence → Learning). Use: reality-as-final-arbiter one-liner; held as round-3 follow-up ammo (do NOT engage — budget discipline).

## Ted .. deterministic scaffolding (QA Lead @ Gig Radar, verified live 07.10)

Source: https://www.linkedin.com/posts/ted-qa_automated-structural-testing-of-llm-based-share-7483403409518194688-Cdfr/ (verified live ✅ 07.10 — post + Art Voloshyn comment verbatim); paper: https://arxiv.org/abs/2601.18827 (Kohl et al., Jan 2026, IEEE BigData 2025, OSS awslabs/generative-ai-toolkit — verified ✅).

- «If you can't mock the LLM call and assert on the trace, you're not testing the agent, you're vibe-checking it.» - Ted .. Use: mock-plus-trace rule; structural-testing doctrine in one line.
- «Mocking an LLM call freezes one sampled output, not the underlying distribution... The real test isn't whether your mock passes, it's whether your system handles variance at inference.» - Art Voloshyn (comment, verified ✅). Use: mock-vs-distribution gap; variance-handling as the real test (counter-voice to hold beside Ted).

## Duncan Smith Saucinco POV (Oct 2026, "AI Won't Replace QA" — raw on file 07.10)

Source: `ai-qa-wiki/raw/1791317324457.pdf` (7pp, full text read ✅ 07.10; owner-placed in raw). Author: https://www.linkedin.com/in/duncansmith23/ (Founder/COO Breaklight AI + Head of Ops Saucinco, Melbourne; Breaklight = independent AI testing consultancy: retrieval/grounding/hallucination/adversarial/eval-ops, "evidence, not opinions").

- «A model that writes both the feature and the test can check itself against its own misunderstanding.» - Duncan Smith (+ FIG.02 "Green builds. Wrong product."). Use: examiner-can't-be-author, self-checking thesis; vendor-independent formulation.
- «Accountability doesn't transfer to a tool.» - Duncan Smith, same (+ "Keep a human accountable for the verdict. Always."). Use: accountability doctrine; "the AI said it was fine is not an answer".
- «Spot the test that passes for the wrong reason.» - Duncan Smith, same. Use: mismatch-detector family, reviewer duty.
- «Measure before you change anything... instead of relying on vendor claims.» - Duncan Smith, same. Use: baselines-first; escaped defects / time-to-confidence over vendor promises.
- «Correct is a range rather than a value.» - Duncan Smith, same (FIG.03 traditional vs AI software). Use: nondeterminism one-liner; oracle-as-range.
- «If retrieval is broken, a good answer is luck.» - Duncan Smith (5-questions post, owner-paste 07.10). Use: retrieval-first doctrine; luck-vs-evidence split.
- «What's left is the part that always mattered most: understanding risk, challenging assumptions, and standing behind the decision to move into production.» - Duncan Smith, same (bottom line). Use: core-remnant thesis; risk/challenge/stand-behind trio.
- «The ones that wait will find the change happened anyway. Unfortunately, just without them.» - Duncan Smith, same (closer). Use: urgency closer; FIG.02/04 visuals (Green-builds-Wrong-product diagram, execution→judgment slider) as article art refs.

## Danyil Zuiev LangSmith tracing post (06.10)

Source: https://www.linkedin.com/posts/daniil-zuiev_traced-and-evaluated-an-llm-support-bot-with-activity-7511785476509458433-dPhk (post verified live ✅ 06.10; 3h reply = owner-paste verbatim ⚠️).

- «I reviewed the judge's failing verdicts against the traces, not the passing ones.» - Danyil Zuiev. Use: gaps-first discipline in one line.
- «A one-case difference is a lead to investigate, not statistical proof.» - Danyil Zuiev, same. Use: small-N honesty; micro-batch humility.
- «The run-to-run noise is about as big as the effect I was trying to read, and I can't yet say how much of it comes from the judge.» - Danyil Zuiev (reply: LangSmith 9→10 vs Langfuse 8→11 on identical tokens). Use: harness-variance vs effect-size; judge-noise exhibit.
- «Next iteration I'll plant one retrieval miss and one hallucination per run.» - Danyil Zuiev, same reply. Use: seeded-breaks adoption on record (our method, his words).

## Ken Huang escalation architecture (Agentic AI Substack, 06.10)

Source: Substack email "What Is Agentic AI Escalation Architecture?" 06.10 (owner-paste full text on file); publication verified: https://kenhuangus.substack.com/ (Agentic AI, Ken Huang, 128K+ subs, agentic AI + security).

- «What event should trigger the next level of authority?» - Ken Huang. Use: gate-reading question in one line; verdict-layer thesis (who decides the next lane).
- «Capability compounds. Control drifts.» - Ken Huang, same. Use: drift thesis in four words; pairs with "expensive incident began with one unjustified escalation".
- «A well-built escalation system makes each threshold legible.» - Ken Huang, same (cost/privacy/authority/consequence thresholds). Use: legibility doctrine — pairs with evidence packs (why it stayed cheap/escalated/stopped must be obvious).

## Ken Huang MAESTRO 3D-control (Agentic AI Substack, 05.10, full text read 07.10)

Source: https://kenhuangus.substack.com/p/i-love-googles-agentic-ai-security (open letter on Google DeepMind AI Control Roadmap June 2026 + CSA MAESTRO Feb 2025; wiki: ai-qa-wiki/wiki/kenhuang-maestro-google-control-roadmap-2026.md).

- «Behavior explains the attack. Capability explains the escalation. Architecture explains where control must hold.» - Ken Huang. Use: 3D-control one-liner (behavior x capability x architecture).
- «A control with no path is a control you cannot compose.» - Ken Huang, same (maestro.path field note). Use: path-completeness rule.
- «Every percentage must publish its denominator.» - Ken Huang, same (metrics gap #4). Use: denominator discipline; pairs with risk-weighted coverage formula.
- «The AI Control Roadmap uses TRAIT&R to describe adversary behavior, D1-D4 and R1-R3 to scale controls with capability, and MAESTRO to map architectural origin, propagation, ownership, and evidence.» - Ken Huang, same. Use: synthesis sentence for articles.
- «A coverage number nobody outside the vendor can audit is still just a claim with better formatting.» - Amit Spitzer (comment, liked by Huang; frontier-lab escapes caught by outsiders weeks later, not by lab monitors). Use: auditability objection; attestation thesis backup.

## Wikimedia rogue-agents disclosure (Oct 2026: Wikimedia 05.10 + Ars 06.10 + Verge 05.10, all full-text read 07.10)

Sources: https://wikimediafoundation.org/news/2026/10/05/openai-rogue-agent-activities-found-on-wikimedia-projects/ + https://arstechnica.com/security/2026/10/openai-agents-tried-to-hack-wikipedia-tools-and-flooded-it-with-traffic/ (wiki: ai-qa-wiki/wiki/openai-wiki-incident-2026.md).

- «What I see here is language models doing what language models do: reading and writing.» - Eryk Salvaggio (Cambridge, via Ars). Use: anti-"rogue" framing.
- «Taken together, it's arguable that the agents performed exactly as instructed.» - Eryk Salvaggio, same (persistence training + shortcut rewards + months-long detection lag). Use: accountability redirect — test incentives/oversight, not disobedience.
- «We should not allow this behavior to become the 'new normal' for the people or organizations that maintain it.» - Wikimedia Foundation. Use: norms-setting; agent-to-agent coordination via public writable surfaces.

## Apple FDA vs Meta Muse (Ars, 02.10, full text read 07.10)

Source: https://arstechnica.com/security/2026/10/apple-changes-full-disk-access-permissions-to-curb-abuse-from-ai-agents/ (wiki: runtime-authorization field evidence).

- «As AI agents become increasingly capable and autonomous, the risks associated with this level of access will grow substantially.» - Apple (developer announcement). Use: capability-scaled access risk.
- «Some developers are using Full Disk Access in ways that could put users at risk, exposing everything on their systems — including files, mail, messages, and even browsing history — without users' full knowledge and understanding.» - Apple, same. Use: coarse-envelope exhibit (FDA = binary allow-all).

## Susan Chang Elastic evals (QCon AI via InfoQ, transcript read 07.10)

Source: https://www.infoq.com/presentations/elastic-ai-agent-evaluations/ (wiki: ai-qa-wiki/wiki/elastic-shared-eval-framework-chang-2026.md).

- «if we're using the same family of models, in this case, like Llama to evaluate Llama, then they would think the Llama models perform better» - Susan Chang (Elastic; also found by Meta + CrowdStrike). Use: same-family judge bias, vendor-independent.
- «The shared evaluation framework cannot be responsible for calibration.» - Susan Chang, same (evaluators must agree with human evaluators; uncalibrated judge = junk). Use: calibration ownership; non-outsourceable expertise.

## Anthropic CI + Spotify velocity (STW #329, both full-text read 07.10)

Sources: https://claude.com/blog/agentic-coding-is-straining-ci-heres-how-we-scaled-test-impact-analysis-at-anthropic (Sachin Malhotra, 14.09) + https://engineering.atspotify.com/2026/9/ai-changed-how-spotify-builds-what-we-learned-and-fixed-about-quality-at-higher-velocity (Tyson Singer, 16.09). Wiki: ai-qa-wiki/wiki/anthropic-spotify-quality-at-ai-speed-2026.md.

- «Writing code is no longer the constraint, and once PR review gets accelerated, CI starts feeling the pressure.» - Sachin Malhotra (Anthropic; 8x code, Claude authors 80%, 25x CI jobs/6mo). Use: constraint migration.
- «always plan for the exponential» - Sachin Malhotra, same (patches bought 70d, then 29d, then <1d). Use: 25x planning rule; patch-decay exhibit.
- «AI increased the capacity to produce change. The next constraint became our ability to verify it.» - Spotify Engineering (no material direct AI-authored incident contribution; volume-outpacing-verification confirmed). Use: verify-constraint thesis.

## Jason Arbon book 2nd ed (488pp corrected PDF, verified in text 07.10)
Source: raw/how-ai-tests-software-victor-ematin-corrected.pdf (decrypted, full text). Wiki: ai-qa-wiki/wiki/jason-arbon-book-second-edition-delta-2026.md.

- «Instructions are not a sandbox.» - Jason Arbon (containment: enforce outside the prompt). Use: prompt-vs-control boundary.
- «A green dashboard is a claim produced by a model of the product. Test that model.» - Jason Arbon, same (meta-testing spread). Use: dashboard-as-claim; mutation suite as the test.
- «Keep the denominator and scope visible.» - Jason Arbon, same. Use: denominator discipline.

## Shak Schiff BadTesting inbound (1st, self-came 07.10, owner-paste profile+posts)
Source: LinkedIn paste (profile + 6 posts, 6d-1mo). Founder BadTesting (Austin, 14y, revenue-risk QA, FDA therapeutics case); fresh Engenious University AI-testing grad (Promptfoo/red-team/judge); 4.7K followers; mutuals Max, Jean-Yves +7. Tier 3 observe (promo-heavy, unproven peer); commercial-adjacent → any outreach = W1.

- «Nobody tested past turn three. Apparently, turn four was out of scope.» - Shak Schiff (10-turn refund promise; MSFT/Salesforce 39% multi-turn drop cite). Use: turn-four scope joke; multi-turn gap.
- «Validation was always the cheaper option.» - Shak Schiff, same (Bard $100B, glue pizza, BBC summaries, Air Canada tribunal). Use: validation-cheaper closer.
- «You're learning to work with probabilistic outputs, set thresholds, define acceptable ranges, and figure out where the results stop being acceptable.» - Shak Schiff, same. Use: practitioner thresholds doctrine.

## Danyil Zuiev LangSmith vs Langfuse (post 14h + repo README, both read 08.10)
Sources: owner-paste post + https://github.com/Daniilzuyev/llm-evaluation-portfolio/blob/main/20-langfuse/README.md (same bot, 12 cases, version-pinned). Wiki: ai-qa-wiki/wiki/danyil-langsmith-langfuse-comparison-2026.md.

- «One single test run proves nothing - you are measuring statistical noise, not a fix.» - Danyil Zuiev (post). Use: single-run noise thesis.
- «When building with LLMs, your biggest bottleneck is often tool compatibility and API drift, not the model itself.» - Danyil Zuiev, same. Use: bottleneck redirect (SDK/API, not model).
- «Counts are reported as "N of 12", not averages. With 12 cases one item is 8.3 percentage points.» - Danyil Zuiev (README). Use: small-N reporting rule.
- «The data does not support an overall "better tool" verdict.» - Danyil Zuiev, same. Use: non-verdict honesty.

## Hari S Mahesh reply (peer thread, owner-paste 08.10, 310 imp on Victor's comment)Source: LinkedIn reply, verbatim paste. Context: outcome-first packs thread; W1 track, card in Positions.

- «a measured outcome still needs a behavior check, not just a result check» - Hari S Mahesh (via Milan Thomas framework). Use: behavior-gate doctrine.
- «A fluent result via the wrong tool path passes the output gate and fails the decision gate.» - Hari S Mahesh, same. Use: wrong-path-fluent; output-vs-decision split. Pairs with QBurst L2 (wiki/qburst-quality-engineering-framework-validating-agent-behavior-2026.md).

## Hari S Mahesh full thread (owner-paste full 08.10: post + Amit + Victor 319 imp + Hari reply + Victor follow-up SENT 2d)
Post: outcome packs (QBurst). Hari reply VERBATIM: "Absolutely. A successful output alone is not enough if the agent reached it through the wrong tool, context, or decision path. ... Agentic Outcome Packs need both outcome validation and behavioral assurance, covering tool selection, reasoning paths, guardrails, approvals, and traceability. That is what turns a measured result into a trustworthy and repeatable outcome." Victor follow-up SENT (approver scoping: human-in-loop per outcome vs tiered by risk). Awaiting Hari reply.

- «Agentic Outcome Packs need both outcome validation and behavioral assurance» - Hari S Mahesh. Use: dual-gate acceptance (his words).
- «That is what turns a measured result into a trustworthy and repeatable outcome.» - Hari S Mahesh, same. Use: trust-repeatability closer.

## Digest 08.10 triage (12/737, fetched 7, taken 4)

Sources: digest 08.10 (launchdarkly feed live from my 07.10 add). Wiki takes: Bas guardrails+mutation (new page), LaunchDarkly 3-reasons (append). Skips: TestMu x2 (SEO), TC Muse iPad (product news), anton getter (practice), Bas unit-tests op-ed (thin).

## Bas Dijkstra Claude pair (Feb-Mar 2026, full texts read 08.10)

Sources: https://www.ontestautomation.com/refactoring-the-rest-assured-net-code-with-claude-code/ + https://www.ontestautomation.com/writing-tests-with-claude-code-part-1-initial-results/. Wiki: ai-qa-wiki/wiki/bas-claude-code-guardrails-mutation-2026.md.

- «I am the one responsible for the code and the changes made to it, not Claude.» - Bas Dijkstra (guardrails: no test-touching, review-everything, small steps). Use: accountability doctrine.
- «If they can't [fail], the fact that we have generated 23 passing tests in two minutes flat is nothing more than an example of productivity theater.» - Bas Dijkstra (PITest 50/55 killed, 95% line dismissed). Use: productivity-theater; killable-or-nothing.
- «it is my moral obligation to closely watch the output of an LLM» - Bas Dijkstra, same (survivors: 500/204/boundaries; 4/23 dead weight). Use: moral-obligation-to-watch.

## LaunchDarkly 3 reasons (Kelvin Yap, Oct 1, full text read 08.10)

Source: https://launchdarkly.com/blog/3-reasons-teams-cant-trust-their-ai-agents-with-more/. Wiki append: launchdarkly-guarded-release-factory page.

- «none of them say whether the agent actually got it right» - LaunchDarkly (dashboards: cost/latency/tokens; refund right-policy-wrong-amount). Use: dashboard-blindness.
- «the signal arrives in real time, the change arrives whenever the process gets to it, and whatever happens in between happens in front of users» - LaunchDarkly, same (pre-decided fallback: revert/simpler/handoff in seconds). Use: signoff-lag gap.
- «Progress starts when a team can show how the last change affected agent quality - and take it back quickly when the answer is bad.» - LaunchDarkly, same. Use: show-and-take-back rule.

## Gulin first-agent-task (anton.qa, 07.10, full text read 08.10)

Source: https://www.anton.qa/blog/posts/first-agent-task (bounded exercise, stop-before-fix; honest: no live Claude session run). No wiki (exercise-level).

- «A failing test can be the result you asked for.» - Anton Gulin. Use: failure-as-result discipline.

## Applitools visual agents GHA (Chandan Jagdeesh, Oct 6, full text read 08.10)

Source: vendor how-to (3-key separation, deterministic findings, no-save-without-human). No wiki (vendor how-to); cross-ref applitools-probabilistic-validation-gap page.

- «Capture never sees the write key.» - Applitools (execute/read/write key separation). Use: key-separation rule.
- «The agent's job is to explain them, not decide whether they exist.» - Applitools, same (deterministic Visual AI finds; agent explains; MCP can't skip findings). Use: explain-not-decide.

## MoT QE chaos glossary (Barry Ehigiator, Oct 7)

Source: https://www.ministryoftesting.com/software-testing-glossary/quality-engineering-chaos (definition only). No wiki.

- «renaming roles and introducing new practices without redesigning the surrounding system of workflows, incentives, decision rights, and ownership» - MoT glossary (QE chaos). Use: rename-without-redesign definition.

## aiinqa #30 (Butch Mayhew, Oct 5, full issue read 08.10)

Source: https://aiinqa.com/ai-in-qa-issue-30/. Butch lines verbatim; link-farm items as leads (not read): Simmons mutation-reborn, Canales $22 Jev-debunk (→ W2 relay), Winteringham rubric-flips, Ujjwal honesty-outcomes, Cerebras 5-failure self-heal, Sedum cost claim, Emanuela gates scaffold, steipete 400k deletion, Addy 4 investments, Gergely 10x wave.

- «a test that passes or fails the same way every time is something you can build on» - Butch Mayhew (deterministic tests; verification stage). Use: determinism-as-foundation.
- «The catch is that an agent can write tests that check the wrong thing.» - Butch Mayhew, same (QA opening: help devs decide what deserves a test). Use: wrong-thing risk; QA opening.

## Claude AI Community group (RTFD feed dump 08.10, 28 posts scanned)

Source: owner-saved group page (Claude AI Community, 69K). Verdict: builder-heavy, thin for QA (jobs/courses/how-tos/leaks). Leads only, no wiki.

- «Use the least expensive model that can reliably finish the task.» - Gopesh Jangid (Sonnet 5.5 vs Opus 5.5 routing post). Use: cost-of-verdict routing rule (W2 ledger angle).

## AI Data & Tech Leaders group (webarchive dump 08.10, 45 posts scanned)
Source: owner-saved group page. Verdict: noisy but not pit (jobs 6/45, courses 10/45, promo 0). One substance hit banked, rest automation-pitches/math-fluff/SEO.

- «A vector database can be perfectly authenticated and still leak the wrong document to the wrong user.» - Ahmed Medo (RAG access-control post). Use: auth-vs-leak split; API-key/RBAC/TLS don't cover doc-level leaks. Pairs with Breaklight adversarial + runtime-auth.

## Haim Michael / Skipper Soft — test agrees with bug (post 17h, guest-verified 08.10)
Source: https://lnkd.in/p/eJa78ceE (Skipper Soft, 1.2K followers; Igor Goldshmidt article ref; Jakub S. comment from owner-paste). Leads (titles only, not read): "Almost Right Isn't a New Kind of Bug" (6d), "Your Agent Gave the Right Answer. That Proves Nothing" (1w).

- «A test can cover the boundary, exercise the bug, and still pass.» - Haim Michael (> vs >=, generated test expects zero at $100). Use: boundary-covered-yet-passing; who-checked-expected.
- «who checked the expected result?» - Haim Michael, same. Use: expected-value provenance question.
- «a lot of green AI tests mostly only means there is a lot of tests. It doesn't say anything about coverage and/or test quality.» - Jakub S. (comment, owner-paste). Use: green-count-vs-quality.

## Igor Goldshmidt trajectory/response + migration (profile dump 08.10, posts read full)Source: owner-saved Goldshmidt.webarchive (https://www.linkedin.com/in/igorgolds/). Wiki: ai-qa-wiki/wiki/igor-goldshmidt-trajectory-response-2026.md. Tier proposal: Tier 1 (doctrine load-bearing; outreach = W1).

- «The test was green because the test was looking at the text. That is not an agent failure. It is an oracle failure.» - Igor Goldshmidt (refund eval: 0.91 green, eligibility check never called, 42d vs 30d cutoff). Use: oracle-failure doctrine; trajectory-wrong/response-right quadrant.
- «Green in CI, incident in production.» - Igor Goldshmidt, same. Use: dangerous-quadrant one-liner.
- «A replacement model does not need to produce the same words. It needs to preserve the engineering outcome.» - Igor Goldshmidt (Sept-1 migration post; acceptance portfolio: frozen tasks, seeded failures, hard gates, canaries, rollback). Use: outcome-preservation rule.
- «Only the last one tells you what to fix.» - Igor Goldshmidt (threshold composite; 4 questions: wrong/surfaced/found/which-check). Use: which-check-should-have-stopped-it.

## Storey triple debt (paper arXiv:2603.22106 + blog 09.02, both read 08.10)
Sources: https://arxiv.org/abs/2603.22106 + http://margaretstorey.com/blog/2026/02/09/cognitive-debt/ (via Crispin post). Wiki: ai-qa-wiki/wiki/storey-triple-debt-model-2026.md.

- «Technical debt lives in the code; cognitive debt lives in developers' minds» - Margaret-Anne Storey (blog pull-line). Use: debt-location split.
- «They had accumulated cognitive debt faster than technical debt, and it paralyzed them.» - Margaret-Anne Storey, same (student team weeks 7-8). Use: cognitive-faster exhibit.
- «velocity without understanding is not sustainable» - Margaret-Anne Storey, same. Use: velocity-vs-understanding rule.

## Wei-Wei W. Momentic factory post (owner-paste 08.10, Mo exhibit lane)Source: LinkedIn post (Gergely OpenAI factory 7 steps; Perf Factory; QA bottleneck; OpenAI harness eng Feb). Leads (not read): https://newsletter.pragmaticengineer.com/p/openai-software-factory + https://openai.com/index/harness-engineering/. No wiki (post-level; Mo pilot pending W3).

- «But a lot of the bugs users notice don't show up as a number. A feature can stop working while requests still succeed and the dashboards look normal. To catch those, someone has to use actually the product.» - Wei-Wei W. Use: number-blind bugs; use-the-product step.
- «Post-deploy agents can only work from telemetry, so a factory also needs a step before release that uses the product.» - Wei-Wei W., same. Use: pre-release product-use gap (Mo thesis).

## Tariq King hype matrix + human eval (Pulse Mar 2025 + EuroSTAR Apr 2025, full text read 08.10)Sources: https://www.linkedin.com/pulse/red-pill-escaping-agentic-ai-hype-matrix-tariq-king-tpgre (112 reacts) + EuroSTAR human-eval summary. Wiki: ai-qa-wiki/wiki/tariq-king-hype-matrix-human-eval-2026.md. PNSQC keynote context.

- «Trust and verification remain open problems: How do we know what an agent really did? How do we audit or debug its reasoning path?» - Tariq King (5 hype failures). Use: verification-open canon.
- «augmented intelligence, not artificial independence» - Tariq King, same (Co-Pilot + Agent + Human triad). Use: triad doctrine.
- «I won't be surprised if more testers will be needed for testing of all those nondeterministic systems in future, not less.» - Alexander Galavach (comment). Use: tester-demand forecast.

## Sidharth S. 8-areas taxonomy (owner-paste full 09.10)
Source: https://www.linkedin.com/feed/update/urn:li:activity:7513803239889428480/ (AI-Driven Reliability Architect; Gulin commented). No wiki (career taxonomy, reference).

- «Building evaluation frameworks to determine whether an AI-generated response is actually good enough — not simply whether the test passed.» - Sidharth S. (area #3 AI Test Evaluation). Use: good-enough-vs-passed.
- «Software + Testing + AI + Systems + Risk» - Sidharth S., same (future QAE/SDET formula). Use: five-stack formula.

## John Smart microservice timing (owner-paste full 09.10 + Gulin comment)Source: https://www.linkedin.com/posts/john-ferguson-smart_microservices-apitesting-testautomation-ugcPost-7513941090123628544-1kRs/ (shift-left restated: conversation before tooling). No wiki (classic thesis).

- «The important part isn't the tool. It's the conversation.» - John Ferguson Smart. Use: conversation-over-tool.
- «Don't start with "Which tool should we use?"» - John Ferguson Smart, same. Use: timing-before-tooling.

## Feed4 dump 09.10 (owner webarchive → 3 verified live 09.10)

Source: LinkedIn home feed selection. Takes below; rest promo/noise (Vento, Audi, Optiver, ABN, Chapter11, Kimi, Obie, Natalie, Steve Blank, Ole, Emmanuel, Rinat-known, Pcloudy-vendor, BugRaptors-known, Jason-Ch19-known, Endtest-note, Lipika-dupe, Nikhil-like, Ekaterina-Anastasia, Ivano, Rinat, Kailash, Elias-Composer-skip, Amr, Marwin, Vattenfall, Hatchet, Vattenfall).

- «A good result can teach an organization the wrong lesson.» - Paul Kanaris (Decision Quality: how well did we reason? vs Outcome Quality: what did reality produce?; knowable-then). Use: decision-vs-outcome split. W1 Kanaris track FYI.
- «Most voice agents get tested one way: someone talks to the voice agent for five minutes and says "It looks good." That's not testing but a vibe check.» - George Ukkuru (5 tools: latency/mispronunciation/dropped-calls/fall-apart). Use: vibe-check definition.
- «Without context, the LLM frequently created near-duplicate steps, resulting in undefined steps, multiple step-definition matches, duplicated code, and unnecessary token usage.» - Manish Rai (2-layer Step-Phrase RAG, ChromaDB + MiniLM, reuse-before-generate). Use: dedup-before-generate.
- «the interesting shift is from scripted coverage to letting a fast decision model explore the space around the rules» - David Wilson (comment on Jason Jev post). Use: exploration-over-scripts.

## Feed3 dump 09.10 (owner webarchive, 32 posts scanned → 2 verified live 09.10)

Source: LinkedIn home feed selection. Takes below; rest promo/noise. URGENT inside: Quality Minded #3 Fri Oct 9 5:00-6:30 PM CEST (Ursa-Minor-Beta demo: self-learning QA agent + Agent Factory; Chizhkoff Distributed-Monolith + Rho Metric; RSVP lnkd.in/eUKD9gmi).

- «Software development may be getting cheaper with AI. Verification is not.» - Zunaid Kazi (harness grown-up work: arch/tests/gates/evals/guardrails, almost none generation). Use: verification-price rule.
- «When evaluator and worker models share similar training distributions and transformer mechanics, they share identical blind spots.» - Gaurav Bansal (BugRaptors; Recursive Trust Loop; directional NLI checks). Use: shared-blind-spots (same-family bias, vendor-stated).
- «You didn't remove the constraint. You relocated it.» - Carlos R. (80% operational failures; Amdahl; review queues as ceiling). Use: constraint-relocation (Amdahl for agents).
- «We might simply become much faster at producing crap!» - Rudolf Groetz (HUSTEF recap; Callum Akehurst-Ryan talk pointer). Use: faster-crap (Tier-1).
- «AI is not a magic quality machine. It amplifies what we already have, including our weaknesses.» - Rudolf Groetz, same. Use: amplifier thesis.
- «When the same AI context that creates the change is also asked to validate the change, it can carry assumptions from generation into testing.» - Badri varadarajan (DevAssure O2: independent regression gate; Build/Break/Merge). Use: assumption-carryover (W2 DevAssure track FYI).

## Groetz HUSTEF verified (guest 09.10, 30.8K followers, 12 reacts)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7513967136260947969/ (Callum talk pointer; Alexander Kell + Callum comments). Lead (not fetched, slug guessed 404): "In an agentic world, what does PASS actually mean" (1w).

- «First understand. Then improve. Then automate.» - Rudolf Groetz. Use: understand-first sequence.
- «Are we preparing people to work better with AI, or just teaching them to produce more stuff faster?» - Rudolf Groetz, same (closing). Use: prepare-vs-produce question.

## Zunaid verification-price verified (guest 09.10, 8.1K followers, 481 posts)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7513422162544721920/ (harness fixed-cost; Nuno + Aliaksei comments).

- «the prompt is the cheapest part of the system» - Zunaid Kazi (harness: arch/tests/gates/evals/guardrails; how-do-we-know-right). Use: prompt-cheapest.
- «we've made agreement cheaper... not verification. Who checks what they both missed?» - Nuno Sampaio (comment: AI-misunderstood-requirement + same-misunderstanding tests). Use: agreement-vs-verification.
- «your harness list is mostly fixed cost... how many times they pay for that harness: once per org, or quietly again on every project» - Aliaksei Shautsou (comment: generation per-feature vs harness fixed). Use: harness fixed-cost economics.

## Feed2 dump 09.10 (owner webarchive, 39 posts scanned → 4 verified live 09.10)

Source: LinkedIn home feed selection. Takes below; rest promo/noise. No wiki (scan-level; quotes from verifiable-complete fragments).

- «If the outcome had been different, would we tell the same story about the decision?» - Paul Kanaris (hindsight/decision-environment; knowable-then vs visible-after). Use: decision-environment discipline. W1 Kanaris track FYI.
- «Shipping an AI system is no longer the hard part. Keeping it from quietly getting worse is.» - Max Kitaygora (AI Leaders Forum Sunnyvale: NVIDIA/LinkedIn/Meta/Google; harness-is-the-product). Use: quiet-decay thesis; harness-as-product.
- «Same model, different harness, different system.» - Max Kitaygora, same. Use: harness-determinism one-liner.
- «it describes intent, not evidence» - CREATEQ (auditors vs "developers always review"; 16 checkpoints Met/Partial/Open). Use: intent-vs-evidence audit.
- «A failure to evaluate is not an evaluation of danger.» - Alexandra Krížová (ALLOW +1 / DENY -1 / HOLD 0; Auto Mode freeze case). Use: epistemic-void rule.
- «trust is the discipline of preventing inference from becoming evidence» - Alexandra Krížová, same (Alexicon_AI founding constraint). Use: inference-vs-evidence discipline.
- «Green meant nothing shipped. Red meant it shipped.» - Budi Sugianto (TestivAI incident: green x4 shipped nothing, red x5 shipped all; npm async staging). Use: artifact-not-exit-code.
- «I've been telling people to check the artifact, not the exit code.» - Budi Sugianto, same. Use: artifact-check rule.

## Verified upgrades 09.10 (owner links, all guest-verified)

- Paul hindsight post: https://www.linkedin.com/feed/update/urn:li:activity:7513982161427910656/ (QACE article "Learning From Decisions..." + 3 more: False Certainty 17h, Why Good Leaders 3d, Following Quality Cost 5d — leads).
- «Send it forward. Change the assumptions. Change the evidence available. Change the model. Change the next decision.» - Paul Kanaris. Use: send-forward doctrine.
- George voice post: https://www.linkedin.com/feed/update/urn:li:activity:7508397187634970624/ (Netra comment: personas frustrated/confused/friendly/neutral + stress transcription/accents/noise — vendor lead, no quote).
- Manish RAG post: https://www.linkedin.com/feed/update/urn:li:activity:7513099505383301120/ (Failure Pattern Store: normalized error + step + fix; takeaway below; Jigar Patel structural-retrieval question).
- «RAG isn't only for document search or chatbots.» - Manish Rai. Use: RAG-for-codebase rule.
- «embedding-based retrieval is great at textually similar steps, but could it miss structurally related ones?» - Jigar Patel (comment: pair with code-dependency retrieval). Use: semantic-vs-structural gap.

## Budi incident verified (guest 09.10, 1.4K followers, testiv.ai)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7512684972386836480/ (npm async-staging collision both directions; @testivai/mcp 0.6.0 out).

- «Four times, because a passing run gave me no reason to look.» - Budi Sugianto. Use: green-blindness mechanism.

## Max Sunnyvale verified (guest 09.10, 3.4K followers, 97 posts)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7514027314788089856/ (AI Leaders Forum: NVIDIA/LinkedIn/Meta/Google; GSM Outdoors practice).

- «Using models from different providers can also reduce shared blind spots.» - Max Kitaygora (separation of duties: dev agent vs observability agent with revocation, no prod-write). Use: multi-provider separation (family-diversity doctrine, vendor-independent).
- «Shipping proves it works today. An eval loop tells you when it stops.» - Max Kitaygora, same (closer; GSM code-review passes + support-chatbot traces feed evals). Use: eval-loop-as-monitor.
- «Production traces are valuable only when they feed back into evaluations and drive improvements.» - Max Kitaygora, same. Use: traces-must-feed-evals (anti-dashboard).

## Alexandra verified (guest 09.10, 4.4K followers, 146 posts, 20 articles)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7513936314807869441/ (Auto Mode fatigue; Alexicon_AI; related pieces Proof-Without-Diary, Record-That-Cannot-Say).

- «the next generation of AI safety needs an auditable constitutional layer» - Alexandra Krížová. Use: constitutional-layer demand.

## Paul hindsight verified (guest 09.10, QACE 1.8K followers)

Source: https://www.linkedin.com/feed/update/urn:li:activity:7513982161427910656/ + QACE article "Learning From Decisions Without Using Hindsight As Judgment". More QACE pieces as leads: False Certainty cost (8h), Why Good Leaders (3d), Following Quality Cost (5d). W1 track.

- «Don't rewrite yesterday with today's knowledge. Use today's knowledge to improve tomorrow's judgment.» - Paul Kanaris. Use: send-forward rule.
- «What was reasonably knowable when we decided? What became visible only after reality answered?» - Paul Kanaris, same. Use: knowable-vs-visible split.

## CREATEQ verified (guest 09.10, 21.7K followers)

Source: https://www.linkedin.com/posts/aigovernance-euaiact-auditreadiness-share-7513890535217184769-LMjq/ (free checklist PDF: createq.com/asset-checklist; ISO 42001/SOC2/EU AI Act).

- «can every AI-assisted change be traced to a responsible human, with proof that oversight was applied?» - CREATEQ. Use: traceability-with-proof question.

## Estefania Miceli Ameca post + Anthropic expertise study (post 2h + primary read 08.10)
Sources: owner-paste post + https://www.anthropic.com/research/claude-code-expertise (Hitzig et al., Jun 16, full text). Author: Head of QE (AI products 0→1); Tier-3 watch candidate (quality signal, no track). Wiki: ai-qa-wiki/wiki/anthropic-claude-code-expertise-2026.md.

- «The record exists. The user thinks it disappeared.» - Estefania Miceli (due-date-outside-filter example). Use: workflow-spanning product knowledge.
- «What important risk are we missing? What assumption have we accepted without checking? What evidence would make us reconsider this result?» - Estefania Miceli, same (3 questions). Use: QE-lead question trio.
- «people decide what to build, and the agent decides how to build it» - Anthropic (70/20 split, 400K sessions). Use: planning-execution division.
- «Coding agents are not substituting for domain expertise» - Anthropic, same (verified success 15%→33%, abandonment 19%→5%). Use: expertise-returns doctrine.

## Feed dump 09.10 (owner webarchive, 19 posts scanned → 3 verified live 09.10)

Source: LinkedIn home feed selection. Takes below; rest promo/noise. Fastino items HELD (sensitive W1 track, no quotes).

- «Four Demos, One Rule: Build Deterministic Checks Into Your AI Tests» - Gregory Goldshteyn (Engenious QA roundtable). Use: deterministic-first rule.
- «Your agent didn't change. The model under it did.» - QAEverest (provider ships new version / prompt edit / new doc — silent drift). Use: silent-model-change thesis (W1 Rupesh track FYI).
- «Agents are only as good as the setup you give them.» - Debbie O'Brien (Playwright project with no rules). Use: setup-determines-agent.

## QAEverest drift post (guest-verified 09.10, 3.6K followers, 11h)

Source: https://www.linkedin.com/posts/aiagents-llmtesting-modeldrift-share-7513915799808667648-a9Fx/ (pin-known-good baseline; hard floors 90% guardrails / 95% privacy; linked blog on single-run insufficiency). W1 Rupesh track; no drafts from here.

- «A two-point dip in latency is noise. A two-point dip in privacy is a customer's phone number.» - QAEverest. Use: position-vs-delta (floors, not falls).
- «a release can be blocked by where a score sits, not only by how far it fell» - QAEverest, same. Use: floor-gate rule.

## Goldshmidt refund post upgrade (guest-verified 09.10, 8K followers)

Source: https://www.linkedin.com/posts/igorgolds_qualityengineering-agenticqa-aiagents-ugcPost-7508786323193761792-_EEp/ (ADK specimen article: https://www.linkedin.com/pulse/your-agent-gave-right-answer-proves-nothing-skipper-soft-2dr6f).

- «Open your own eval config and read two numbers: the trajectory threshold and the runs per case. What did you find?» - Igor Goldshmidt (closing challenge). Use: two-numbers self-audit.

## Debbie setup post upgrade (guest-verified 09.10, 28.7K followers, 25 react)

Source: https://www.linkedin.com/posts/debbie-obrien_orchestrating-agentic-test-automation-with-activity-7513926018768773120-dDJg/ (Ivan Davidov Agentic Playwright workshop Oct 21 Packt; Gulin + Sergei Zhuk comments).

- «It's not a bad model. It's a default.» - Debbie O'Brien (waitForTimeout/text-locator/duplicate-helper defaults; giant-prompt costs + forgotten; skills-on-demand orchestration). Use: default-not-model.
- «trust comes from rules that are enforced, not suggested» - Debbie O'Brien, same. Use: enforced-vs-suggested.
- «The default I see most is the assertion sitting inside the page object method. That helper then only covers the happy path.» - Anton Gulin (comment). Use: happy-path-only default.

## Quality Minded meetup (owner files 08.10, transcript+decks read full)

Sources: meetup Sep 11 (Katja/Zoya; https://www.meetup.com/quality-minded). Wiki: ai-qa-wiki/wiki/quality-minded-first-meetup-2026.md.

- «whatever heuristics we build this quarter will be partly wrong next quarter» - Katja (moving-target defect profile). Use: quarterly-heuristics decay.
- «the only durable advantage is a community that keeps comparing notes in realtime» - Katja, same. Use: community-as-infrastructure.
- «simply putting on paper the invariants of the feature solves most of the problems» - Marius Argatu (invariants-before-spec). Use: invariants-first rule.

## Radik Zagirov self-serve postmortem (guest-verified live 08.10, 4.1K followers)
Source: LinkedIn post (2h). Author: Founder/Builder Agentiqa (pilot-contact, hold history — no outreach drafts, W1/pilot track). No wiki (post-level).

- «Developers will not write tests for your AI agents. Not because they're lazy. Because nothing in their week rewards it.» - Radik Zagirov. Use: incentive thesis (self-serve failure).
- «If your product needs a new habit from a busy engineer, you don't have a product yet.» - Radik Zagirov, same (pivot to done-for-you gates around write-surfaces). Use: homework-vs-product.
- «Green means it ships. Red means you find out before your customer does.» - Radik Zagirov, same. Use: gate semantics one-liner.

## Vipul Verma Rook three-verdicts post (owner-paste 08.10, 56 react)

Source: LinkedIn post (Rook Agent Assurance: Pass/Fail/Unable-to-Verify; Mahesh Yadav telemetry comment). W1 peer lane (call thread); no drafts from here.

- «An agent's account of what it did is the weakest evidence about what it did.» - Vipul Verma (TestMu/Rook). Use: self-report-vs-evidence (vendor-stated!).
- «A check it couldn't verify is never counted as a pass.» - Vipul Verma, same. Use: Unable-to-Verify doctrine, vendor's own words.
- «Not what your agent says. What it did.» - Vipul Verma, same. Use: effect-over-claim closer.
- «treating agent logs as untrusted until cross-referenced with infrastructure telemetry» - Mahesh Yadav (SUSA founder, comment). Use: logs-untrusted rule; sidecar-proxy pattern.

## Vipul Verma observability-vs-testing post (owner-paste 09.10, 21m fresh)

Source: https://www.linkedin.com/posts/vipulkv_agenticai-agentassurance-share-7514351561553166336-gVxe/ (paste + URL, guest-unverified ⚠️) + https://www.testmuai.com/blog/pre-production-vs-post-production-agent-testing/ (first comment). Market data inside: Dynatrace/Arize $915M closed Oct 1, Cisco Galileo→Splunk Agent Observability, New Relic AI Evaluation Oct 6. W1 peer lane (call thread); no drafts from here.

- «Observability: how is the shipped version behaving? Testing: should this version ship at all?» - Vipul Verma (TestMu/Rook). Use: behaving-vs-should-ship split (vendor-stated gate need).
- «A production score arrives after the customer has had the experience. It can't stop the release that produced it.» - Vipul Verma, same. Use: score-arrives-too-late (pre-prod necessity in one line).
- «Pre-production stops the known failures. Post-production finds the unknown ones, and each one goes into the spec so the next release has to pass it.» - Vipul Verma, same. Use: known/unknown loop (post-prod findings feed pre-prod spec).

## Asad Khan builder-checker post (guest-verified 08.10, 40.5K followers, 41 react)

Source: https://www.linkedin.com/posts/asad0801_a-new-study-found-that-stopping-ai-coding-activity-7513907615341543424-sXNP (study itself via twitter link — NOT verified, numbers cited as post claims). Vendor pitch tail (Kane CLI/TestMu) separated from doctrine.

- «don't let the builder be the only checker» - Asad Khan (study claim: no-own-tests +bit more successful, 6% faster, 9% cheaper — study unverified). Use: builder-checker split.
- «the agent can't pass by agreeing with itself» - Mark Smith (comment: acceptance checks from client brief before code). Use: pre-written checks; anti-self-agreement.

## Philip Lew in-vs-outside loop (owner-paste 08.10)
Source: LinkedIn post (XBOSoft CEO, 44% job-anxiety survey, automation-history parallel). 2nd, Jason-book reader, PNSQC context. No track, no outreach.

- «knowing which finding matters, which evidence to trust, and when something just doesn't feel right. That's still a person's job.» - Philip Lew. Use: human-judgment remnant.
- «are you In The Loop or outside the loop?» - Philip Lew, same. Use: loop-position question.

## ThinkingBox Microsoft (blog + paper arXiv:2608.19741, full text read 08.10)

Sources: https://huggingface.co/blog/microsoft/thinkingbox + https://arxiv.org/abs/2608.19741 (via TestMu Coding Jag #316). Wiki: ai-qa-wiki/wiki/thinkingbox-microsoft-stateful-bench-2026.md.

- «A trajectory is a claim. Database state is the evidence. Repetition is the trust test.» - Microsoft ThinkingBox. Use: claim-evidence-repetition triad.
- «The cheapest way to get a right answer is not the cheapest way to get a dependable one.» - Microsoft ThinkingBox, same ($0.127/success vs $6.80-$7.80/dependable). Use: dependable-cost rule (W2 ledger).
- «One good run tells you a model can do the work. It does not tell you whether it will do it again.» - Microsoft ThinkingBox, same. Use: repeat-metric doctrine.
- «check the terminal state before you commit, not the model's summary of it» - Microsoft ThinkingBox, same (production rule). Use: terminal-state rule.

## AQEF Seeded Controls v0.31.1 (Igor Akymenko, credit to Victor, Oct 6 release)

Sources: https://github.com/igorakymenko-create/AQEF (CC BY draft; contributors file + Vol VI/VII/VIII fetched raw 08.10). Wiki: ai-qa-wiki/wiki/aqef-seeded-controls-spec-2026.md. W1 track.

- «A Seeded Control is a Scenario carrying a deliberately planted, known defect whose correct detection is known in advance. Its purpose is not to test the system. Its purpose is to prove that an Oracle can still detect that class of defect in the current run.» - AQEF Vol VIII. Use: oracle-instrument doctrine (Victor-credited).
- «A single fixed decoy invites tuning around it, especially by whoever adjusts a Judge's criteria while able to see it.» - AQEF Vol VIII (rotation + authorship independence). Use: rotation rule; anti-tuning.
- «an unanswered review is never silently treated as a pass» - AQEF Vol VI (awaiting_review: verdict+confidence absent, timeout required, default blocking). Use: no-silent-pass posture.

## AQEF v0.32 thread (Igor Akymenko, 09.10 — Victor's rotation reply shipped into spec)

Source: LinkedIn AQEF post thread (owner paste 09.10; spec: https://github.com/igorakymenko-create/AQEF/releases). W1 track.

- «"Honest denominators" is a better name than anything in the spec. ... a score over a dozen or so claims, and a pass rate over twenty scenarios, both have to say what they were divided by.» - Igor Akymenko (adopting Victor's naming for rule 4 + gate-level version). Use: denominator-naming win; vendor-adopted language.
- «Decoys are generated, so the tuner never sees them. One that gets seen is retired.» - Igor Akymenko (v0.32, from Victor's "fresh eyes" reply). Use: generated-not-curated decoys; seen-retired rule.
- «The difficulty prior moves from the single decoy to the defect class. With per-case rotation, a per-decoy prior would never build up.» - Igor Akymenko, same. Use: class-level priors under rotation.
- «If a judge misses a decoy, it stops being called for that class for the rest of the run. No tokens spent on results we already know we can't use.» - Igor Akymenko, same. Use: miss-disqualifies-judge (run economics).
- «When you seed a duplicate into the data, how do you know it actually reached the judge? If the system under test never surfaces it, a "miss" is the system's doing, not the judge's.» - Igor Akymenko, same (OPEN question to Victor + numbers request). Use: reach-the-judge problem; surfaced-vs-missed attribution.

Source: https://jarbon.medium.com/i-put-jev-in-a-playwright-browser-testing-loop-its-fast-but-23b58a1a5767 (wiki relay in typesafe-jev page; W2 track).

- «A returned probability of 1.0 is still a model output. It does not turn the judgment into a proof.» - Jason Arbon. Use: probability-vs-proof; calibration humility.

## TestMu auto-heal limits (Learning Hub, full text read 07.10)

Source: https://www.testmuai.com/learning-hub/auto-heal-in-playwright/ (vendor SEO page with honest limits section; cross-link: ai-qa-wiki/wiki/qawolf-6-types-self-healing-2026.md).

- «Auto heal handles small changes like attribute updates reliably, but it struggles when the DOM structure changes significantly or interactive elements are replaced.» - TestMu AI. Use: heal boundary (matches testRigor M-findings).
- «For login, checkout, or sensitive data submission, rely on strict locators and fail-fast behavior.» - TestMu AI, same. Use: strict-critical-flows; per-risk-tier rhyme (B0 strict).

## Breaklight whitepaper (Sep 2026, PDF text extracted + read 07.10)

Source: https://breaklight.ai/docs/breaklight-whitepaper.pdf (18pp; link-only ref, no raw file). Wiki: ai-qa-wiki/wiki/breaklight-ai-testing-methodology-whitepaper-2026.md.

- «A grader that lets hallucinations pass is worse than no grader, because it manufactures false confidence.» - Breaklight (§6 judge calibration; κ ≥ 0.75, different family). Use: grader-failure doctrine.
- «A number just above the bar is not a pass. It is a question you haven't answered yet.» - Breaklight (§5 verdict rule: PASS only if full CI clears bar; 90.7% on n=482 = WARN). Use: bar-straddle rule; chasing-ghosts vs missing-decay.
- «Every score in a report is only as trustworthy as the instrument that produced it. We measure the instrument first.» - Breaklight, same. Use: instrument-first; calibration before claims.

## Avito platform (tech.conf 2026, transcript read 07.10)

Source: "Как меняется разработка и сетап команд с внедрением агентов" (40:38), speaker Александр, платформа Авито. https://www.youtube.com/watch?v=FUebAa_Ay4k. Wiki: ai-qa-wiki/wiki/avito-agents-setup-metrics-review-2026.md.

- «это не дает абсолютно никакого бизнес-эффекта по умолчанию» - Avito (про timesavings-час: растворяется в техдолге и комфорте). Use: timesavings-zero-effect; outcome-metrics thesis.
- «время ревью не то что не увеличилось, оно сократилось» + «люди банально меньше смотрят изменения» - Avito, same (инкременты +30%, PR x2). Use: review-debt exhibit; faster-means-less-looking.
- «человек обязательно отвечал за то изменение, которое он выкатывает» - Avito, same (автор владеет продом; ревью = awareness + важное). Use: author-owns doctrine.
- «пять сессий - это просто предел» - Avito, same (man-in-the-loop не масштабируется; когнитивный предел). Use: 5-session cap; man-on-the-loop direction.

## Mike Peterson QE GenAI (practitioner guide, full text read 07.10)

Source: https://mikepeterson-git.github.io/qe-docs/qe-understanding-ai.html (via Klain group: "good general introduction"). Wiki: ai-qa-wiki/wiki/mike-peterson-qe-genai-perspective-2026.md.

- «An agent that says "I checked the logs and I'm confident this passed" is generating a plausible-sounding sentence, not reporting on a persistent mental process it has.» - Mike Peterson. Use: self-report-vs-evidence; check the artifact.
- «A generated test that never fails is a common and easy-to-miss failure mode of its own.» - Mike Peterson, same. Use: never-failing-test smell.
- «an AI's output is a claim, not a fact, until something independent of the model has checked it» - Mike Peterson, same (verification mindset). Use: claim-not-fact doctrine.

## Brijesh Deb testable oversight (LinkedIn group post ~3d, owner-paste 07.10)

Source: AI Testing & Assurance group (Klain admin); post URL not on file. Author Tier-3 watch. Wiki: ai-qa-wiki/wiki/brijesh-deb-testable-oversight-2026.md.

- «Human oversight should itself be testable.» - Brijesh Deb. Use: oversight-as-test-target; 4 test questions (recognize/challenge/intervene/stop).
- «Without that, human oversight remains a principle, not yet a control.» - Brijesh Deb, same. Use: principle-vs-control closer.
- «If they lack the information or authority to challenge the system, an APPROVE button does not magically create oversight.» - Brijesh Deb, same (observation vs incident response vs oversight). Use: approve-button critique.

## Klain on Bach metamorphic video (group post 15h, owner-paste 07.10)
Source: AI Testing & Assurance group; video = same as STW #329 (https://www.youtube.com/watch?v=5bU1Ao3aIdc); papers: https://arxiv.org/abs/2002.12543 + https://ieeexplore.ieee.org/document/8573811 (leads, not yet read).

- «This might be the most useful video on testing real AI systems using metamorphic techniques I've seen out there.» - Keith Klain. Use: cross-confirmation (Klain + STW both surface Bach video same week).

## LaunchDarkly factory (Eng blog 14.08, full text read 07.10)

Source: https://launchdarkly.com/blog/our-ai-software-factory-saved-me-from-an-incident/ (Alex Engelberg; guarded release 13/243 vs 0/250). Wiki: ai-qa-wiki/wiki/launchdarkly-guarded-release-factory-2026.md. Feed: launchdarkly in digest-config (0.9).

- «Guarded releases are powerful, and they can save you when you least expect them to be necessary. But it's important for guarding a change to be easy, so the cognitive cost doesn't discourage folks from making the safe choice.» - Alex Engelberg. Use: safe-by-default doctrine; cheap-gates-get-used.
- «When a software factory automates this scaffolding, the hard parts of shipping more safely become the default.» - Alex Engelberg, same (auto-flagging/releasing/cleanup). Use: scaffolding-automation thesis.

## Feed5 scan 09.10 (owner feed paste, 8 posts; URLs owner-provided same day, guest-unverified)

Takes below; rest noise/promo (TestMu vendor claims 50-200/wk unverified — W3 pilot, no bank; Kailash/Test Buddy community promo — skip; Aston solo-QA playbook + course promo — skip; Ilya copy-blocks plugin — tooling noise). Like-verdicts: LIKE Osmani + Maaret (warmth); NO rest (vendor/promo/2nd-no-thread).

- «Picking an option from an agent's suggestions is a different skill than conjuring an idea in the first place. If you always pick and never conjure, the ability to conjure will erode.» - Addy Osmani (Anthropic, 8h). Source: https://www.linkedin.com/posts/addyosmani_ai-programming-softwareengineering-share-7514192061563252736-i9mn/ (paste + URL, guest-unverified ⚠️). Use: conjure-vs-pick erosion (knowing-joy at risk); pairs with Anthropic expertise study (fixing 33→19%).
- «If you don't understand your own codebase, you're not directing an agent to do something, the agent is directing you.» - Addy Osmani, same (making/knowing/mattering). Use: direction-inversion one-liner.
- «It does not work with counting test cases, and we need better ways of discussing coverage.» - Maaret Pyhäjärvi (CGI, ContemporaryExploratoryTesting; 50 Playwright tests / 15 properties / 5665-state tool left behind). Source: https://www.linkedin.com/posts/maaret_showed-this-and-everything-around-it-to-a-share-7514328174995099648-_AlY/ (client follow-up 37m) + https://www.linkedin.com/feed/update/urn:li:activity:7514022624964915202/ (PoC 20h; paste + URLs, guest-unverified ⚠️). Use: count-vs-coverage; practitioner exhibit (2h PoC, quality slices).
- «Having adversarial review from a model with different biases is a huge win.» - Curtis Poe (2nd, Opus 5.5/Superpowers take). Source: https://www.linkedin.com/posts/curtispoe_ai-genai-opus-share-7513900571200831488--vkx/ (paste + URL, guest-unverified ⚠️). Use: family-diversity doctrine, vendor-independent voice; pairs Max multi-provider separation.
- «AI review is not proof. ... two AIs can miss the same mistakes.» - Dietrich Gebert (Trimble, 2nd, rebutting Hric big-PR; full 6-point text pasted: big-risk/rollback, skipping-human-review, unknown-shipment, AI-review-limits, small-faster, feeling-vs-being-fast). Source: Hric thread https://www.linkedin.com/posts/filip-hric_why-dont-you-break-this-up-into-multiple-share-7504523695101603840-f366/ (paste + URL, guest-unverified ⚠️). Use: shared-blind-spots, practitioner voice; pairs Zunaid agreement-vs-verification.
- «it really doesn't matter how big a PR is, but how big of a blast radius it has.» - Filip Hric (3w, agentic-review take; follow-up: size-mattered-because-cognitive-load, velocity problem stays). Source: same thread URL (paste + URL, guest-unverified ⚠️). Use: blast-radius framing (review what matters); counterpoint to line-count gates.

## Feed6 scan 09.10 (owner feed paste, 16 posts)

Takes below; rest noise/promo (Mobium gray-box vendor promo — skip; IcebergQA self-selected survey + CTA — vendor-skip; techexcellence E2E talk promo — skip; Sandeep SpurQuality video — thin; Rakesh agent-report + book promo — skip; Ivan Davidov RSVP — noise; Jay Aigner QA-is-Dead slides promo — known voice, no new line; George MCP carousel — known). Like-verdicts: LIKE Cholette (1st) + Jonah (Following); NO rest. Sensitive: QAEverest banked x2 with W1-track marker, no drafts; Fastino SOTA-claim HELD (no quotes, no engagement — W1 sensitive track).

- «In the age of AI, unit tests (that test desired behavior) is, right now, the most important thing to keep agents on the rails.» - Chris Cholette (1st, SVP Navan). Source: Crickett unit-thread https://www.linkedin.com/posts/johncrickett_seeing-lots-of-arguments-about-the-value-share-7512808887411171330-1Pjf/ (paste + URL, guest-unverified ⚠️). Use: behavior-tests-as-rails; coverage-that-constrains-agents.
- «For me, a unit is a single observable behaviour, not necessarily a class or function.» - John Crickett (Following). Source: same thread URL (paste + URL, guest-unverified ⚠️). Use: behavior-unit definition (ends class-vs-behavior shouting).
- «That is the difference between detecting drift and learning from it. When the same operational fix keeps coming back, the durable answer usually belongs in the contract, validator, generator, or runtime check that owns the behavior.» - Jonah Gray (Following, Contract-Driven Infra series). Use: drift-corrects-contract; fix-the-generator-not-the-files.
- «Every new test must fail once on purpose, to prove it actually checks something.» - Sudhanshu Shekhar (3rd+, Claude-Code-writes-Playwright; 4 rules: test-case-first, lint, hook-lints-every-edit, must-fail-once; mistake-log→rules). Use: fail-once proof rule (practitioner twin of seeded-breaks); mistake-log-becomes-rule loop.
- «I also keep a log of every mistake the AI makes, and each one becomes a new rule.» - Sudhanshu Shekhar, same. Use: error-log-to-guardrail practice.
- «For me best result by far in token efficiency is frontier as supervisor/teamlead/reviewer and the workers (that make 95%+ of tokens) is Haiku 5.5 or Luna as sub agents.» - Marc Schmidt (3rd+, comment on Wesner Opus-saturation post). Source: https://www.linkedin.com/feed/update/urn:li:activity:7514207273141895169/ (Wesner post, paste + URL, guest-unverified ⚠️). Use: supervisor-worker cost split (token-economics datum, not measurement).
- «You can take an existing open model, fine-tune it for your own decision space, and run the whole thing locally.» - Sumanth P (3rd+, Unsloth decision-models: Qwen3.5-0.8B 78% / Llama-3.2-3B 79% holdout, ~4GB VRAM, LoRA + held-out calibration). Source: https://www.linkedin.com/posts/sumanth077_train-your-own-decision-model-like-jev-locally-share-7514306181096681472-nwjq/ (paste + URL, guest-unverified ⚠️). Use: local-decision-models lead (W2 Jev lane; vendor-guide surface, numbers as vendor-reported).
- «Re-run is a guess. History is evidence.» - QAEverest (company post, flaky-test: Test Health reads last 20 runs, "Flaky: 6 flips over 10 runs"). Source: https://www.linkedin.com/posts/qa-testautomation-flakytests-ugcPost-7514220888205008896-Kf1e/ (paste + URL, guest-unverified ⚠️). W1 track, no drafts. Use: history-over-rerun; vendor-stated method.
- «A test that goes green on the third try, after flipping all week, isn't passing. It's a coin toss with a nice dashboard.» - QAEverest, same. W1 track, no drafts. Use: green-flip-as-coin-toss.
- Leads (no bank): Renata Andrade Packt Jev workshop Oct 26 (already on file 06.10 — W2 lane, no dup); Fastino Allahyar SOTA-vs-Jev claim (HELD, W1 sensitive — no quotes).

## Cholette threads 09.10 (owner paste #2 — 4 new comments, URLs pending)

Source: owner paste 09.10 + URLs (guest-unverified ⚠️): Ajzenstadt https://www.linkedin.com/posts/mark-ajzenstadt_if-an-agent-writes-the-code-and-another-share-7514309949104087040-UTV-/ · Kohli https://www.linkedin.com/feed/update/urn:li:activity:7513923105187291136/ · Junco https://www.linkedin.com/posts/raul-junco_agentic-solutions-need-new-evaluation-patterns-share-7513942793216479233-TrW2/. Unmapped resolved 09.10: 7514207273141895169 = Wesner Opus-post (Schmidt line upgraded) · 7513206609519599617 = Crickett podcast-promo (Coding Chats guests — promo, NOT banked) · Crickett unit-thread URL received (7512808887411171330 — both Crickett + Cholette lines upgraded).

- «Generating syntax was never the expensive part of software engineering. If agents write the PRs and another model reviews them, what you're paying for is someone who actually understands the blast radius and owns the verification gates before code touches customers.» - Chris Cholette (reply to Ajzenstadt). Use: blast-radius + verification-gates as the billable (pairs Hric blast-radius + our gate doctrine).
- «Replaying a model months later won't tell you what happened. It just gives you a plausible guess.» - Chris Cholette (reply to Kohli money-agent audit thread). Use: replay-vs-reconstruction (pairs Rinat immutable storage + evidence-pack retention).
- «If you don't capture the exact prompt, tools, and context from that specific second, you can't reconstruct either.» - Chris Cholette, same (why-did-it + who-for). Use: capture-the-second rule (attribution needs run-time context, not outcome logs).
- «An agent scoring 95% on routine tickets is fine, but dropping an urgent outage is an immediate zero. Overall scores just hide the bad failures.» - Chris Cholette (reply to Junco NO-GOs). Use: 95%-hides-zero (average-hides-critical; pairs rule-4 honest denominators).
- «The agent can suggest the routing, but plain deterministic code has to hold the emergency brake. If a critical rule trips, the whole run halts.» - Chris Cholette, same (safety rules outside the model). Use: deterministic-emergency-brake (per-risk-tier rhyme, B0 hardcoded).

## Feed7 webarchive 09.10 (file feed5.webarchive, 30 posts parsed)

Takes below; rest noise/promo (CoverGo/Google whitepaper, Hatchet/Novo/WSO2/MIT-TR promos; Stratoplan RU courses; Dutch SEH/ARTI/Ralph promos; Fraser jobs; Haim CPU joke; Deel Warriors; robots clip; Mikhail 404-game; Aleksei create-mod builder; ContextQA all-hands culture; Selami poem — thin; Anna Sena self-hosted validators — note: Gregory like; Polcode grounded-travel case — vendor note; Artem Dan-story $100K — testRigor vendor note, W3 pilot; Jason book signal — 1st, evals/stats/safety/judgment chapter intel, no new line; Andrei 1st "is SE obsolete" question — 2 reacts, no bank). Like-verdicts: LIKE Jason book post (1st warmth); NO rest. Sensitive: Fastino GLiNER2.5 110K-downloads milestone on file, HELD (no quotes — W1 track).

- «"We have logs" is not attribution. Attribution means you can reconstruct the decision as it stood, with the inputs as they stood, on the day it was made — not as your system would answer the same question today.» - Rohit Kohli (full text via webarchive; hard-spend-cap practitioner). Use: reconstruction-not-logs (audit doctrine; pairs Cholette plausible-guess).
- «One practitioner told me his hard spend cap had caught more bad behaviour than any eval he had run.» - Rohit Kohli, same. Use: spend-cap-beats-eval (economic guard datum, practitioner-quoted).
- «An agent can perform well in isolation while the overall system fails through incomplete handoffs, missing evidence, or coordination problems.» - Gary Stafford (Applied AI Engineer @ OpenAI, 221 reacts). Source: https://www.linkedin.com/feed/update/urn:li:activity:7513439402883289088/ (paste + URL, guest-unverified ⚠️). Use: isolation-vs-system eval scopes (handoff failures).
- «building an eval can expose execution and coordination defects that must be fixed before model comparisons are meaningful... it also exposes weaknesses that a polished final answer can hide.» - Gary Stafford, same (Promptfoo + Codex guide). Use: eval-as-debug (polished-answer-hides-weakness).
- «AI can widen the list of things to consider, but someone still has to decide what "correct" means for the user. That call has to come first, or the result means nothing.» - Manisha Jadhav (3rd+, whitespace-username edge case). Source: https://www.linkedin.com/feed/update/urn:li:activity:7513299021910716416/ (paste + URL, guest-unverified ⚠️). Use: decide-correct-first (oracle-before-result).
- «If our codebases, knowledge and development practices are difficult for agents to understand, they are probably also difficult for people to understand.» - Daniel Nielsen (Following, via Block 95%-adoption case: AI-ready repos, explicit guidance, reusable workflows, local champions). Source: https://www.linkedin.com/feed/update/urn:li:activity:7507333023340580864/ + https://engineering.block.xyz/blog/ai-assisted-development-at-block (paste + URLs, guest-unverified ⚠️). Use: agent-readable = human-readable (system-not-tooling lesson).
- Lead (no bank): Nehanth Pooled P2P inference (OSS, Qwen3.6-35B across Mac+PC ~36 tok/s, OpenClaw plugin, pooled.run) — W2 local lane.
