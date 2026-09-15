# 26-carousel — Gemini generation scenario (для сравнения с HTML-вариантом)

**Формат:** 7 слайдов, portrait 1080×1350, темная тема #0d1117 + янтарь #f0b429.
**Правило:** весь текст — только из промптов ниже, дословно. Ничего не перефразировать (проверять орфографию: CONFIDENCE, AMBIGUOUS, IDENTICAL).
**Запрет:** термин только `False Negative`, никогда `False Positive`.

## S1 — Cover
Robot on minefield (pic-26-0 уже есть — использовать как фон). Текст поверх:
`QUALITY OPERATING MODEL / How to Evaluate Any AI-QA Vendor in 5 Scenarios / Break the testing tool on purpose. / Victor Ematin`

## S2 — Problem
Типографика, без картинок. Текст:
`THE PROBLEM / A tool that fails red costs you an hour. A tool that lies green costs you the release. / 5/5 green at 100% confidence, 0% risk — with two identical login forms on the page.`

## S3 — Method
Перерисовать матрицу (26-mutation-matrix.png как референс): 5 узлов Baseline / Locator drift / Weak decoy / Strong decoy / Product regression; две строки EXPECTED (GREEN, GREEN/heal, FLAG, FLAG, CATCH) vs ACTUAL (все GREEN). Подпись: `When every row is green, green means nothing.`

## S4 — Cases
Сплит Vendor A Silent Green (False Negative) vs Vendor B Honest Death (Correct Diagnosis) — pic-26-2 как референс композиции. Подпись: `Silent green vs honest death.`

## S5 — Loop closed
Скрин 26-report-warnings-crop.png как референс. Панель `Warnings & Observations`, бейдж `WARNING ui-structure`, строка `Duplicate login form sections on the page`, `seen in 3 of last 3 runs`, `confirmed`. Подпись: `Green stayed green — it stopped being silent.`

## S6 — Playbook
Типографика, 4 строки:
`1. Import a small suite you fully understand. / 2. Run the 5 scenarios; demand per-scenario outputs. / 3. Red flags: silent green, heal-without-review, confidence without methodology. / 4. Report gaps first.`

## S7 — CTA
Типографика: `When did you last break your testing tool on purpose? / Full method in the article. / Victor Ematin · AI Quality Engineering Lead`
