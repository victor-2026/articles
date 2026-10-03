**Format:** LinkedIn carousel PDF (7 slides, 1080×1350 px, 4:5 portrait) + feed post
**Series:** Quality Operating Model (slot Mon 05.10 09:00)
**Status:** scenario v1 (W4, 02.10 — from Note 1 draft v1, facts CERTIFIED, W1 fact-check passed with fixes applied)
**Style:** dark #0d1117 + amber (series system); mono digits; last slide carries `© Victor Ematin · AI Quality Engineering Lead · Independent practice`
**Generation:** user picks — HTML→PNG (AI controls layout) or Gemini image-gen per slide spec below

---

## ЛОГИКА ОТБОРА: что из большой статьи ушло в карусель и почему

Большая статья (RMT-after-freeze, ~1100 слов, 9 секций) отвечает на три вопроса: что нового, где предел метода, где ему жить. В карусель идёт ТОЛЬКО первый вопрос (Note 1: batch #2 + crash) — по правилу «один носитель = одна идея». Остальное (Mapping Limit, lifecycle, appmut, S4-saga) — следующие носители, не этот.

Принцип нарезки: в карусель попадает то, что читается за 20 секунд скролла и бьёт числом. Объяснения, оговорки и контекст остаются в first comment (леджер) и будущих заметках.

Послайдно (суть + хук + что вырезано):
1. **Обложка (24 → 0).** Суть: весь выпуск одной строкой. Хук: контраст «зашли/не вышли». Вырезано всё остальное — обложка не объясняет, она останавливает скролл.
2. **Scope (11 → 9 → 24).** Суть: прицел был узким намеренно. Хук: «сканер прошёл мимо» — инструмент слеп, и это заявлено вслух. Вырезана механика CHAIN_HOPS/unwrap (ей место в леджере, не на слайде).
3. **Closeout (22/2/0).** Суть: зелень как звук здорового стенда. Хук: «ноль — полное предложение». Вырезаны имена резолвов в детали (tooltip + wa-controls упомянуты, без разбора).
4. **Crash I (0/30/24 vs -9/632).** Суть: две колонки, цифры говорят сами. Хук: визуальный шок зелёного против красного. Ноль прозы — только цифры и подпись мутанта.
5. **Crash II (ред + оговорка).** Суть: честность как приём доверия. Хук: «механизм — гипотеза» — признание, которое делает остальное believable. Вырезаны CPU-детали глубже 20 сэмплов.
6. **Discipline (zero + 95/98).** Суть: правило, которое можно украсть. Хук: «или не кончается» — угроза как мнемоника. Вырезана вся S4/appmut-фактура (другие выпуски).
7. **CTA + копирайт.** Суть: вопрос читателю + защита от кражи PDF. Хук: «разрешением, а не измором» — дистинкция, которую хочется репостить.

Проверка полноты: любой слайд понятен без остальных (скролл рвёт порядок), порядок даёт арку (заход → прицел → итог → драма → честность → правило → вопрос).

---

## Slide 1 (cover)
Headline: 24 MUTANTS WALKED IN.
Sub: Zero walked out unanswered.
Footer: 95 seeded mutants / 98 run-records · RMT field report #1

## Slide 2 (scope)
Headline: THE CHAINS v1 WALKED PAST
Body: expect.element() chains across unit specs. First scanner saw matcher="element" — and kept walking.
Strip: 11 files scouted → 9 yielding → 24 seeded breaks

## Slide 3 (closeout)
Headline: 22 KILLED. 2 RESOLVED. 0 INCONCLUSIVE.
Body: 22 killed = the suite works (controls firing). Two inconclusives got names and rulings: one crash, one kill mapping.
Strip: Zero inconclusive remain. Zero is a complete sentence.

## Slide 4 (the crash I)
Headline: BASELINE vs MUTANT
Two columns:
LEFT (green): exit 0 · 30s · 24 passed
RIGHT (red): exit -9 · 632s · 3rd consecutive hang
Footer: tooltip:213 EQ_NEGATION

## Slide 5 (the crash II)
Headline: RED THROUGH THE CRASH
Body: CPU 30–200% across all 20 samples. Output empty. Suite red via pre-registered exit-code mapping — nobody decided anything in between.
Caveat line: Mechanism = hypothesis (stated as one). The caveat is what makes the rest believable.

## Slide 6 (discipline)
Headline: EVERY BATCH ENDS AT ZERO
Body: …or it doesn't end. Resolution, not exhaustion.
Strip: 95 seeded mutants / 98 run-records (units labeled — bare numbers lie)

## Slide 7 (CTA + copyright)
Headline: WHEN DID YOUR LAST CAMPAIGN END AT ZERO?
Sub: Machines count. Humans decide.
Footer: © Victor Ematin · AI Quality Engineering Lead · Independent practice
