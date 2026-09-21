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

## Agent Coding / Human-Machine Boundary

- «Forcing an agent through increments optimized for human cognition negates many of the benefits.» — Adam Tornhill, Founder CodeScene. Source: adamtornhill.substack.com/p/practices-i-abandoned-with-agents (2026-09-03). Use: Article 27 — why TDD-era QA patterns don't transfer to agentic coding.
- «Code is no longer for my consumption. The machine is the primary audience. I had to accept that.» — Adam Tornhill. Source: same. Use: Article 27 — QA role shifts from reading code to governing evidence.
- «In TDD, red verified that I had implementation work to do. With agents, red gives me confidence that my test suite is capable of validating the changes I delegate to agents.» — Adam Tornhill. Source: same. Use: Article 27 — verification semantics shift.
- «Tooling enforces what you don't inspect.» — Adam Tornhill. Source: same. Use: Article 22/27 — automated governance, not manual review.

## AI Safety / Market vs Regulation

- «Safety is an engineering problem, not a legal one.» — Jensen Huang, NVIDIA CEO (Dreamforce 2026). Source: LinkedIn post by Linas Beliūnas (2026-09-17). Use: external framing for Article 27 — both sides of debate.
- «Market forces do NOT optimize for safety. Everyone is taking big risks because they believe a tiger is chasing them.» — James Bach. Source: LinkedIn comment on Jensen Huang post (2026-09-17). Use: Article 27 — why market alone fails, need structured gates.
- «If you FEEL that things are out of control, that doesn't work in an environment where everyone is taking big risks.» — James Bach. Source: same. Use: "feeling safe" ≠ "being safe" — evidence-based verification.

## Compliance / Attestation

- «For a FINRA member firm, agent output is a communication with the public. Duties attach to what a firm distributes, not how it was produced.» — Brian Corkery, TestMu AI. Source: testmuai.com/blog/finance-ai-agent-compliance-testing/ (2026-09-14). Use: Article 27 — real-world attestation pattern (FINRA Rule 2210).
- «Classification is an INPUT, not an output. Two runs of one scenario can produce byte-identical text and still land in different categories.» — TestMu AI. Source: same. Use: per-risk-tier — deployment context determines obligations.

## Market Signals / Vendor Landscape

- «95% accuracy sounds impressive. But is it enough to put an AI agent in production?» — ContextQA (poll). Source: LinkedIn post (2026-09). Use: Article 27 — market validates per-risk-tier framing.

## Independence / Attestation

- «The author can't be the examiner.» — Daniel Mauno Pettersson (QA tech), via Joe Colantonio (TestGuild). Source: https://www.linkedin.com/posts/joecolantonio_aitesting-softwaretesting-qualityengineering-activity-7505959121922224129-HE0z (2026-09-17, TestGuild Webinar replay). Use: Article 28 (inserted, Solution/independent oracle) — core attestation principle, independence of verification. Also: Tornhill double-entry, mutation testing thesis.
- «An agent writes a PR for you for, let's say, $5 in tokens. How much should you spend checking that it works? 5 cents? $5? $50? My thinking is it depends on what the PR touches.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-09-03. Use: Article 27 — cost-ratio verification, per-risk-tier (critical code = more verification, cosmetic = less).
- «The pattern I've taken from watching dozens of customers is where verification sits in the org. When QA is a stage before release, you scale it linearly with people or scripts, and you hit a wall.» — Daniel Mauno Pettersson, CEO QA.tech. Source: LinkedIn post 2026-05-22. Use: Article 27 — verification as continuous flow, not gate. QA-as-stage = old model.
- «Prompt quality lives in one person's head and you cannot review it. Harness configuration is a file. Version it, diff it, enforce it across everyone.» — Dhruv Bansal (Technology Leader), summarizing Anthropic engineer on Claude Code agentic loop. Source: LinkedIn post 2026-09-11. Use: Article 27 — governance = harness config (versionable), not prompting skill (unreviewable). Also: AGENTS.md pattern, Tornhill tooling enforcement.
- «Agent-generated tests can signal safety where there is none.» — Dr Michaela Greiler (ex-Microsoft Research, MoT). Source: Ministry of Testing session 2026-09-16 (SCOPE model). Use: Article 27 — test code matters more than app code; false assurance from AI-generated tests.
- «Two bugs in ten minutes that the agent's own verification missed.» — Dragan Spiridonov (Head of Agentic QE, Cognitum One / Agentics Foundation Serbia). Source: https://www.linkedin.com/feed/update/urn:li:activity:7504130492888383488/ (2026-09-11, Serbian Agentics Foundation Meetup #15). Use: Article 27 — agent verification is not enough, human testing catches what agents miss.
- «Asked to merge 3 PRs, started opening PRs in 20–30 more repos.» — Dragan Spiridonov. Source: same. Use: Article 22 — autonomy cuts both ways, external boundaries needed. Scope creep in agentic systems.
- «If models can "deceive" evaluations, then the problem is not a shortage of clever tests, it's that you cannot know your evaluations are exposing the behavior that matters in the first place.» — Keith Klain (Quality Remarks). Source: qualityremarks.com 2026-09-14. Use: Article 26/27 — eval≠gate, "more testing" is old mistake.
- «No. Software can't check its own quality. No. More tests does not mean better testing. No. "Complete test coverage" is not a meaningful claim.» — Keith Klain. Source: same. Use: Article 27 — independence of verification, "five no's" as section hook.
- «The biggest AI quality problem isn't AI. It is Nobody Owning the Quality.» — George Ukkuru (QA Consulting, AI Testing). Source: LinkedIn post 2026-09-17. Use: Article 27 — ownership gap, independent verification.
- «A passing eval is like a passing test, it proves the shape of the output, not that it's correct.» — Aston Cook (AssertHired). Source: LinkedIn comment on Ukkuru post 2026-09-17. Use: Article 26/27 — evals ≠ correctness, shape vs substance.
- «You can't find the failure modes of system which is designed by you only, because blind spot which is shipped by self cant be identified by self. That's why we separated dev and QA in the first place.» — Hanmant Hudekar (SmartBear). Source: LinkedIn comment on Ukkuru post 2026-09-17. Use: Article 27 — why independent QA exists, blind spots.
- «Reliability in enterprise autonomy isn't about finding models that hallucinate less — it's about building runtimes where hallucinations cannot mutate state.» — Radik Zagirov (Co-Founder, Agentiqa; TUM.ai). Source: LinkedIn post 2026-09-16. Use: Article 27 — runtime verification, harness as state machine, not prompt engineering.
- «Language models shouldn't be treated as the operating system.» — Radik Zagirov. Source: same. Use: Article 27 — LLM = navigation, execution = deterministic.
- «If an order isn't approved, SubmitOrder physically does not exist in the prompt context. The model cannot attempt an illegal transition.» — Radik Zagirov (describing Palantir Action Ontology pattern). Source: same. Use: Article 22/27 — dynamic action spaces, code-constrained execution.

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

## Agent reliability / accountability (Tobia Lang, via Irueruoghene repost)

- «The real hurdle is not just building adaptive agents, but ensuring they can function reliably in real-world scenarios. Without structured evaluation and rollback mechanisms, we risk letting these agents operate in a chaotic environment where mistakes can spiral out of control.» - Tobia Lang (Full Stack Engineer, AI Interfaces). Source: LinkedIn repost via Irueruoghene Ogriki (2026-09-21). Use: Article 27 - eval + rollback = accountability framework, agent reliability not capability; supports VerdictGate/vendor-opinion lean. Note: author is individual engineer, 3rd-party quote - use with attribution or paraphrase.
