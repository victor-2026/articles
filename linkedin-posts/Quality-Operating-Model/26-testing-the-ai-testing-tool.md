How do you test a testing tool? Same way you test the app: you break it on purpose.

## Skeleton

- **Hook:** «Your AI-QA platform just shipped you a green report. 0% risk. Low severity. The page had two identical login forms - and the tool picked one silently. How do you know the next green report is true?»
- **Body:**
  1. AI-QA tools are now products with claims (self-healing, 99.9% reliability, confidence scores) - but their outputs become your evidence layer. A tool that lies green is worse than a tool that fails red.
  2. **The method: mutation matrix for tools.** Evaluate any AI-QA platform the way you test the app - inject known changes and see what the tool reports:
     - Baseline (clean) -> confirm green
     - Locator drift (id/class change, same semantics) -> does it heal or fail loudly?
     - Weak decoy (duplicate text on page) -> ambiguity flagged?
     - Strong decoy (identical form, same style/type/label) -> ambiguity flagged or silent green?
     - Product regression (label/semantics change, locator stable) -> caught as product issue, not healed silently?
   3. **QAEverest pilot (Aug 26) as worked example:** 5-test Playwright suite, GitHub Actions import, 5/5 @ 100% confidence accepted. Mutation results: locator drift -> green (id-agnostic, OK), weak decoy -> green (diff 2.20%), strong decoy -> green (diff 3.19%), product regression label -> passed (text matched heading). All three exported reports: 5/5, 0% business risk. **Ambiguity detection absent.**
   4. **The signal, not the tool:** 90% of value = human gate (nothing runs until approved) + per-step evidence (screenshots, video, diffs). 10% gap = exact-text matcher scoped to first occurrence, no duplicate handling. Verdict: useful evidence layer, incomplete ambiguity guard - use with an external oracle.
   5. **Playbook for evaluating any AI-QA vendor** (Autonoma, Mabl, Testsigma, QAEverest, ...): 4-step matrix, required outputs per scenario, red flags (silent green on decoy, healed-without-diff-review, confidence without methodology).
- **Evidence:** QAEverest pilot (Aug 26, M2/M3/M5/M3b, 3 green reports 0% risk); DevAssure O2 (FP case); 34/34 mutations as external oracle
- **CTA:** «When did you last break your testing tool on purpose - or do you only trust its green builds?»

## The loop closed (Aug 27): feedback became a feature

The pilot had a happy ending that turns this from a complaint into a method. The vendor took the decoy finding, shipped a **passive observation layer**, and it works:

- Every run now runs passive monitoring alongside the tests: duplicated UI sections and ambiguous element matches are detected and reported even when all steps pass.
- Selector-broadening self-heals are flagged.
- Every finding carries a confirm/dismiss review, so teams can track confirmation rate over time.
- A passing run with open findings is reflected honestly in the risk assessment and shared reports.

Verified on the production report (gherkin format): the same strong-decoy page now shows `WARNING ui-structure | CONFIRMED` — "two identical form sections at the same location" — while the test itself still passes. The risk assessment says: "All tests passed, but passive monitoring flagged 1 issue."

**Why this matters for the method:** breaking the tool on purpose produced a feature that makes the tool harder to fool. That is the strongest possible evidence that a mutation-matrix evaluation is worth running — for you *and* for the vendor. A green report is no longer the default output; the tool now tells you when it saw something it couldn't resolve.

**Lesson for the playbook:** report decoy/ambiguity gaps to the vendor before writing them off. Some tools ship a fix in a day; the ones that do are the ones you keep evaluating.

## TODO questions to user
1. Публиковать как статью про QAEverest конкретно, или как общий playbook (vendors без имён)? (рекомендую общий playbook + QAEverest как кейс)
2. Нужна ли карусель с mutation matrix, или текст + feed post?
3. Идёт ли после 25 (порядок серии) или вставлять раньше?
4. ~~Публиковать до или после фикса вендора?~~ ✅ Решено: после. Секция «The loop closed» - сильный финал, показывает цикл «фидбек → фича → верификация».

## Cross-links
- **Статья 20** [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/) - тот же кейс, FP/FN-угол. 26-я = методология, 20-я = результат.
- Статья 24 (accountability/policy testing): тот же кейс, auditability-угол
- Wiki: `wiki/qaeverest-pilot-handson-import-confidence-human-gate-2026-08-25.md` + `wiki/ai-qa-tool-evaluation-mutation-matrix.md` (методология B)
- Wiki: `wiki/zalando-agentic-engineering-snapshot-2026.md` - risk-based PR approval bot = live per-risk-tier gate (33% low-risk auto-approved, -20-40% lead time); vendor independence + open tools (opencode/pi) = open-source harness thesis behind this article.