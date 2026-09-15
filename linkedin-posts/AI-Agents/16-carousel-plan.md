# NotebookLM Scenario: AI Productivity Paradox Carousel

## Instructions for NotebookLM

Generate a 7-slide HTML presentation (1080×1350 px, 4:5 portrait, dark theme) for LinkedIn carousel. Use the source data below.

## Format Spec

- Dimensions: **1080×1350 px per slide (4:5 portrait — LinkedIn mobile standard, +30-40% usable area on smartphones vs 16:9)**
- Background: Dark (#0d1117) — GitHub Dark theme
- Palette: background #0d1117, text #f0f6fc, accent/number #58a6ff, green #3fb950, red #f85149, border/cards #30363d
- Font: system sans-serif, white text, large sizes
- No emoji on slides
- Each slide is a full-width div with flexbox centering (`flex-direction: column`), `page-break-after: always` (PDF export: one slide per page, no breaks)
- Big numbers visually separated from body text, high contrast accent color (#58a6ff / #3fb950)

## Source Data

### Slide 1 — Cover
Headline: Agents Write 7x More Code. Releases Grew 20%.
Subheadline: The AI Productivity Paradox Is a QA Problem
Big numbers: 7x code vs +20% releases
Footer: Verification layer · middle loop · the gap is verification

### Slide 2 — The Paradox
Headline: The Feeling of Speed Is Deceiving
List:
- 82% of engineers spend less time writing code (Annie Vella study, 28 countries)
- 84% report higher productivity — yet experience got worse: 14% -> 27%
- GitLab: 78% code faster, 79% say delivery hasn't sped up
- METR: felt +20% faster, measured 19% slower
Big number: +20% felt, -19% measured
Bottom: "We do more and enjoy it less."

### Slide 3 — The Middle Loop
Headline: Where the Time Went: the Middle Loop
Diagram: [ Inner Loop ] -> (( MIDDLE LOOP )) -> [ Outer Loop ]
- Inner loop: write · build · run · fix (IDE, TDD)
- MIDDLE LOOP: Direct · Evaluate · Correct
- Outer loop: commit · review · deploy · monitor (DevOps)
Bottom: "Supervising an agent is the new QA territory."

### Slide 4 — The Case: Block
Headline: What Breaks First? The Review Pipeline
Before/After contrast:
- Before: 90% engineers used AI → CEO saw 0 value (stuck at Stage 1-2)
- After: AI-code +69%, PRs 21x → Human review pipeline broke
Big number: 21x automated PRs
Bottom: "The fix was a QA design decision: one agent finds, another repairs."

### Slide 5 — The Solution: 4 QA Moves
Headline: Where QA Earns Its Keep Now
List:
1. AI reviewer + auto-fix loop — find, repair, then human
2. Regression advice on every PR — checklists from git diff
3. Mutation testing as anti-overfit guardrail — 34/34 caught
4. Comprehension debt control — specs are the new code
Bottom: "Verification scales with PR volume. Trust is measured, not assumed."

### Slide 6 — The Hard Truth
Headline: Writing Got Cheap. Verifying Did Not.
- Understanding, verifying, shipping, maintaining — all more expensive
- AI code is dangerous because it is plausible: compiles, runs, logic error three commits deep
- When verification capacity shrinks, risk does not disappear - it becomes less visible
Bottom: "Teams that invest in the verification layer ship."

### Slide 7 — CTA
Headline: Which Stage Is Your Team on the 0-5 Scale?
Subheadline: What breaks first when you hit 4?
CTA: Full analysis in the article — link in comments
Footer: © Victor Ematin · AI Quality Engineering Lead · OpenCode Go (копирайт — PDF скачиваемый, последняя страница = подпись)