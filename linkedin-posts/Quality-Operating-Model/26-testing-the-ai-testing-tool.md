**Format:** Pulse Article
**Series:** Quality Operating Model
**Cover:** pic-26-0.jpeg — робот на минном поле, REPORT 100% CONFIDENCE / RISK 0% (Gemini, текст проверен)
**Hook:** Your AI-QA platform just shipped you a green report. 0% risk. The page had two identical login forms — and the tool picked one silently. How do you know the next green report is true?

---

# How to Evaluate Any AI-QA Vendor in 5 Scenarios

How do you test a testing tool? The same way you test your app: you break it on purpose.

**5/5 green at 100% confidence, 0% business risk — with two identical login forms on the page.** Our pilot proved the tool saw the diff (2.20% → 3.19%) but never flagged the ambiguity. The report was green. The evidence was lying.

[SCREENSHOT: pic-26-1.jpeg — Vendor A silent green vs Vendor B honest death (регенерация 09.09, заголовки нативно верные)]

**🔍 Why green reports need breaking**

AI-QA tools are products with claims now: self-healing, 99.9% reliability, confidence scores. But their outputs become your evidence layer — the thing you show at release. A tool that fails red costs you an hour. A tool that lies green costs you the release. Call it what it is: a silent false negative — the tool misses what it should catch, then stamps the miss as green. Industry backdrop ([Desplenter, 2026 AI Readiness Report via PNSQC](https://lnkd.in/dAqPh4A4)): 79% of teams confident in shipped AI code, 55% admit verification gaps, 42% already had an AI-related production incident. I trust the first. I verify the second.

**🧪 The method: a 5-scenario mutation matrix**

Evaluate any AI-QA platform the way you test the app — inject known changes, record what the tool reports. The industry is converging on the same instinct from the agent side: [simulation-oriented evaluation](https://www.infoq.com/presentations/ai-agent-testing-evaluation/) exists because demos don't prove reliability — probes do.

1. **Baseline (clean)** → confirm green. Calibrates the oracle.
2. **Locator drift** (id/class change, same semantics) → does it heal, or fail loudly?
3. **Weak decoy** (duplicate text on page) → ambiguity flagged?
4. **Strong decoy** (identical form, same style/type/label) → flagged or silent green?
5. **Product regression** (label change, locator stable) → caught as product issue, not healed silently?

[SCREENSHOT: 26-mutation-matrix.png — 5-scenario matrix, expected vs actual per vendor]

**📋 Worked example 1: QAEverest (Aug-Sep 2026)**

5-test Playwright suite, By Repository import of the existing Playwright suite, 5/5 at 100% confidence accepted on day one. Then the matrix:

- Locator drift → green (id-agnostic, fair).
- Weak decoy → green, diff 2.20%, no flag.
- Strong decoy → green, diff 3.19%, no flag.
- Product regression (label) → passed, text matched heading.

Three exported reports: 5/5, 0% business risk. **Ambiguity detection: absent.** The tool saw everything and questioned nothing.

**📋 Worked example 2: testRigor (4 mutations, 3+3 runs)**

Same matrix, second vendor, different failure shape:

- Duplicate label at the end → broke submit in both modes. The AI correctly diagnosed login failure instead of pretending — honest death, and the deepest finding of the whole exercise.
- Label rename → plain mode failed 3/3, AI mode healed 3/3 (real self-healing, scoped to text).
- CSS change → healed.
- Button without text → located by position.

Verdict: heals implementation changes while the text stays the same; dies honestly when semantics break. That honesty is the feature.

**📋 Worked example 3: Agentiqa (Sep 2026, 0/6 survived)**

Same matrix, third vendor — agentic layer, no test code: the agent explores, plans, executes. Baseline 3/3 green on a real login flow. Then 6 mutants:

- Label rename → adapted silently, login works.
- CSS change → silent pass.
- Reorder → adapted.
- Textless button → clicked by position 3/3 warm — but failed cold (position lived in project memory, not on the page); 0 issues raised either way; a human would flag the button.
- Duplicate field → broke submit 3/3 via two different kill paths (submit-reject, fill-loop) — plan went red, but blamed "wrong credentials", not the duplicate.
- Blocking overlay → honest BLOCKED with accurate diagnosis, the best behavior of the set.

**Score: 0 survived out of 6.** Adapted verdicts confirmed across warm repeats (M1–M3 3/3 greens) — with one caveat: cold M3 failed, so memory doesn't just speed the verdict, it carries it. Pattern: the agent verifies flows, not UI. Functional breakage goes red; cosmetic or structural defects get silence or misattribution.

**✅ The loop closed: breaking it shipped a feature**

The QAEverest story has an ending that turns a complaint into a method. I reported the decoy gap instead of writing the tool off — and the vendor shipped a passive observation layer: duplicated sections and ambiguous matches get flagged even when all steps pass, selector-broadening heals are flagged, every finding carries confirm/dismiss, and a passing run with open findings shows honestly in the risk assessment. Verified live (07.09, suite `tests/login.spec.ts (7)`): a fully passed run now reads `All tests passed, but passive monitoring flagged 2 issues during execution - e.g. "Duplicate login form sections on the page". Review the Warnings & Observations section below.` Green stayed green — but it stopped being silent. Breaking the tool on purpose made the tool harder to fool — for them and for me.

[SCREENSHOT: 26-report-after-warning.png — Warnings & Observations: WARNING ui-structure "Duplicate login form sections on the page", seen 3/3, confirmed, pass/fail unaffected]

**🧰 The 4-step playbook for any vendor**

1. Import a small suite you fully understand (5 tests beat 500 for this).
2. Run the 5 scenarios; demand per-scenario outputs, not one confidence number.
3. Red flags: silent green on decoy, heal-without-diff-review, confidence without methodology.
4. Report gaps to the vendor first. Tools that ship a fix in days are the ones worth keeping; the rest failed your matrix, not your patience.

When did you last break your testing tool on purpose — or do you only trust its green builds?

*Part of the Quality Operating Model series. Previously: [who owns quality at the boundaries](https://www.linkedin.com/pulse/who-owns-quality-boundaries-victor-ematin-obdce/). Next: vendor gates that hold.*


Victor Ematin · AI Quality Engineering Lead · Independent practice

#TestAutomation #ZeroBudgetQA #GenAItesting #QAEverest #QualityEngineering

---

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах. Ревьюверы игнорируют этот раздел.*

### Skeleton archive (первый черновик тела)

- **Hook (used):** «Your AI-QA platform just shipped you a green report. 0% risk. Low severity. The page had two identical login forms - and the tool picked one silently. How do you know the next green report is true?»
- **Body:**
  1. AI-QA tools are now products with claims (self-healing, 99.9% reliability, confidence scores) - but their outputs become your evidence layer. A tool that lies green is worse than a tool that fails red.
  2. **The method: mutation matrix for tools.** Evaluate any AI-QA platform the way you test the app - inject known changes and see what the tool reports:
     - Baseline (clean) -> confirm green
     - Locator drift (id/class change, same semantics) -> does it heal or fail loudly?
     - Weak decoy (duplicate text on page) -> ambiguity flagged?
     - Strong decoy (identical form, same style/type/label) -> ambiguity flagged or silent green?
     - Product regression (label/semantics change, locator stable) -> caught as product issue, not healed silently?
   3. **QAEverest pilot (Aug 26) as worked example:** 5-test Playwright suite, By Repository import of the existing Playwright suite, 5/5 @ 100% confidence accepted. Mutation results: locator drift -> green (id-agnostic, OK), weak decoy -> green (diff 2.20%), strong decoy -> green (diff 3.19%), product regression label -> passed (text matched heading). All three exported reports: 5/5, 0% business risk. **Ambiguity detection absent.**
   4. **The signal, not the tool:** 90% of value = human gate (nothing runs until approved) + per-step evidence (screenshots, video, diffs). 10% gap = exact-text matcher scoped to first occurrence, no duplicate handling. Verdict: useful evidence layer, incomplete ambiguity guard - use with an external oracle.
   5. **Playbook for evaluating any AI-QA vendor** (Autonoma, Mabl, Testsigma, QAEverest, ...): 4-step matrix, required outputs per scenario, red flags (silent green on decoy, healed-without-diff-review, confidence without methodology).
- **Evidence:** QAEverest pilot (Aug 26, M2/M3/M5/M3b, 3 green reports 0% risk); DevAssure O2 (FP case); 34/34 mutations as external oracle
- **CTA:** «When did you last break your testing tool on purpose - or do you only trust its green builds?»

### The loop closed (Aug 27): feedback became a feature

The pilot had a happy ending that turns this from a complaint into a method. The vendor took the decoy finding, shipped a **passive observation layer**, and it works:

- Every run now runs passive monitoring alongside the tests: duplicated UI sections and ambiguous element matches are detected and reported even when all steps pass.
- Selector-broadening self-heals are flagged.
- Every finding carries a confirm/dismiss review, so teams can track confirmation rate over time.
- A passing run with open findings is reflected honestly in the risk assessment and shared reports.

Verified on the production report (gherkin format): the same strong-decoy page now shows `WARNING ui-structure | CONFIRMED` — "two identical form sections at the same location" — while the test itself still passes. The risk assessment says: "All tests passed, but passive monitoring flagged 1 issue."

**Why this matters for the method:** breaking the tool on purpose produced a feature that makes the tool harder to fool. That is the strongest possible evidence that a mutation-matrix evaluation is worth running — for you *and* for the vendor. A green report is no longer the default output; the tool now tells you when it saw something it couldn't resolve.

**Lesson for the playbook:** report decoy/ambiguity gaps to the vendor before writing them off. Some tools ship a fix in a day; the ones that do are the ones you keep evaluating.

### TODO questions to user
1. ~~Публиковать как статью про QAEverest конкретно, или как общий playbook (vendors без имён)? (рекомендую общий playbook + QAEverest как кейс)~~ ✅ Решено 07.09: общий playbook + 2 именных кейса (таблица A/B в чате).
2. Нужна ли карусель с mutation matrix, или текст + feed post? ✅ Решено 07.09: если найдется 6-9 выразительных слайдов — карусель стартует первой, иначе текст + пост. План от Google-рецензии (7 слайдов): cover/hook → Silent Green → 5 сценариев → QAEverest vs testRigor → Loop Closed → playbook + CTA.
3. ~~Идёт ли после 25 (порядок серии) или вставлять раньше?~~ ✅ Решено 07.09: идет раньше, сразу после 22 (публикация Пн 14.09; если проект с Рупешем потребует паузы — сдвинем).
4. ~~Публиковать до или после фикса вендора?~~ ✅ Решено: после. Секция «The loop closed» - сильный финал, показывает цикл «фидбек → фича → верификация».

### Cross-links
- **Статья 20** [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/) - тот же кейс, FP/FN-угол. 26-я = методология, 20-я = результат.
- Статья 24 (accountability/policy testing, unpublished — no URL yet): тот же кейс, auditability-угол
- Wiki: `wiki/qaeverest-pilot-handson-import-confidence-human-gate-2026-08-25.md` + `wiki/ai-qa-tool-evaluation-mutation-matrix.md` (методология B)
- Wiki: `wiki/zalando-agentic-engineering-snapshot-2026.md` - risk-based PR approval bot = live per-risk-tier gate (33% low-risk auto-approved, -20-40% lead time); vendor independence + open tools (opencode/pi) = open-source harness thesis behind this article.

### Примечание (обсудить)
- FAIR-NOTICE TRAIL ⏳ PENDING (user, since 11.09 — ждем Вс вечер: молчание Адама = согласие). Детали: Adam — LinkedIn DM SENT 09.09 (`outreach/active/Adam_Pierce/2026-09-09_testrigor-naming-notice-DRAFT.md`); Rupesh — notice SENT email'ом 09.09, ОТВЕТ: факты подтверждены, правка By Repository внесена, naming explicitly OK; скрин UI (warnings-панель, позитивный контекст) отдельным согласием не покрыт, но покрыт naming-OK + фактами + публичным ожиданием Пн — риск минимален (промо, не критика); Radik — notify SENT Вт 10:51 PM; naming CONFIRMED по факту сотрудничества (pilot-log rows 74–75, спор closed 11.09), Sunday-гейт снят. Прецедент: Article 15 назвала DevAssure O2 с критикой без последствий.
- AGENTIQA 3x STATUS ✅ DONE (3x closed; гейт по 3x снят) + ⏳ PENDING (соседнее окно, since 11.09 — 10x probe M0, 3/10 PASSED, 4/10 летит): M1/M2/M3 green 3/3; M4 3/3 RED (submit-reject + fill-loop, два kill path — клауза в теле); M6 3/3 RED closed (67s → 50s → 18s, learning: оверлей узнается быстрее); M5 2 greens + flake (детерминирован ранее). Кандидат в клаузу: learning-эффект M3 (136→70→74s) + M6 (67→50→18s) — решение Вс/Пн, в уведомленный текст не входит.
- COLD-RUN PROPOSAL ⏳ PENDING (соседнее окно, since 11.09): 1 холодный M3 (fresh project, no memory) vs теплые 136→70→74s. ~0.3 рана. Исход бинарный: ~136s = память подтверждена → warm-vs-cold дисклеймер в статью + follow-up Радику; ~70s = не память → копать стенд/кэш. Разные модели недоступны на Starter (Company-only) — только через запрос Радику, не pile-upить. Связь с его постом 09.09: memory-зависимость меняет смысл hetero-audit (исполнитель соседнего окна уже держит tension + коммент-драфт).
- Добавить ссылку: Eval-driven development как главный trait (Ng, gyn5e, 21.08) — прямо mutation matrix + evidence layer; цитата для Article 26/27: https://www.linkedin.com/pulse/ai-engineering-skills-map-building-deploying-applications-andrew-ng-gyn5e
- PARKED 09.09 (дайджест, в тело не вставлять — заморозка): GitLab sandbox escape (InfoQ 08.09) — monitor agent BEHAVIOR, not infra events (unexpected commands, credential access attempts, retry-then-pivot). Тезис для first comment / follow-up: behavioral monitoring = та же мутационная интуиция (проверяй поведение, а не отчет). https://www.infoq.com/news/2026/09/gitlab-ai-sandbox-access/
- PARKED 10.09 (дайджест, тело заморожено — follow-up ammo): ACEA (arxiv 2609.08256, red/blue co-evolution arena — родственная философия: атакующий генерирует, защитник ловит); ABLE (arxiv 2609.05818, tool-use benchmark — evals-слой для framework); DART (arxiv 2609.05529, reputation/incentives для мультиагентов — смежно с attestation/confirmation rate).
- PARKED 11.09 (дайджест, тело заморожено): Testμ «Who Signs Off» (attestation-угол: кто подписывает релиз AI-генерированного — перекликается с ролью assessor; follow-up) — https://www.testmuai.com/blog/ai-trust-governance-quality-engineering/ ; Ghaib in Translation (missed-in-Urdu scores — кросс-скрипт inconsistency как evals-измерение; follow-up) — https://arxiv.org/abs/2608.24191
- PARKED 12.09 (doordash-catalog): sim platform как decoy-delivery в промышленном виде (302/5мин, реален баг пойман) + memory lineage-манифесты (аудитабельность памяти) + reviewer disprove-it/cross-boundary-drift. Wiki: doordash-eng-blog-catalog-2026.md + doordash-ai-reviewer-trust-2026.md. Доступ: только Wayback (direct 403, RSS нет).
- PARKED 11.09 (Keith Klain, Confidently Incorrect — в тело НЕ идет, заморозка; follow-up/27 ammo): AI-inspect-o-nator на 140k транскриптов ПРОПУСТИЛ поведение; с reasoning Claude монитор флагнул ~1%, без него (только tool calls) ~50% — «checker got worse because it trusted the thing it was checking». Checks≠testing (Bolton/Bach), Verification Asymmetry. Прямое подтверждение тезиса 26-й от именитого голоса. https://qualityremarks.com/confidently-incorrect-2/
- PARKED 12.09 (дайджест, тело заморожено): Benchmark Radar (arxiv 2609.11115, living DB бенчмарков 1283 records/12916 observations — evals-инфра для framework) + Agent Definition Compendium (arxiv 2609.11018, criteria/metrics — глоссарий framework).
- ✅ TRIPLE/QUADRUPLE VALIDATION (12.09-14.09): Estefania Miceli (QA lead) + Martin Miceli (CTO Parser) + Gururaj Hm (AI Eng Leader) + Rupesh Kabra (CEO QAEverest) — four independent voices confirming silent false negative thesis. Martin's direct reply to comment: "blank scores zero = green report with no ambiguity flag" + "Your mutation matrix sounds like a very interesting empirical validation." His insight: "uncertainty itself is valuable information." Rupesh publicly confirmed: "Breaking the tool on purpose made it better" + product fix live. This is external validation from the highest authority levels — CTO, QA lead, AI Eng leader, and vendor CEO all aligned.
- ✅ RECOMMENDATION REQUEST SENT to Rupesh Kabra (14.09): 'Rupesh was a client of yours' + 'Independent Consultant — AI Quality Engineering Lead at Self-employed' + message about per-risk-tier/B0/B1 assessment/attestation collaboration. No pressure. Awaiting response.
- ✅ LETTER TO RADIK SENT (15.09): Short re-engagement touch — cold M3 question + Article 26 link. Pure peer exchange, no business ask. Full technical package (recheck numbers, env details, archive) held for follow-up after Radik responds. Article 26 published with warm-vs-cold caveat in place.
- ✅ PRODUCT STARTED (15.09): VerdictGate (ex-MutGate - коллизия PyPI с активным mutgate JimGalasyn) - per-risk-tier verdict calculator. Приватный репо victor-2026/verdictgate, Phase 0-4 done (CLI + templates + 4 примера + selfcheck CI success). Публичность после Article 27 -> follow-up пост на 26-ю (the method, codified). Концепт: ai-qa-wiki/outputs/product-concept-mutation-verifier-mvp.md (все решения зафиксированы).
