# 22 — Gamma Scenarios for Visual Assets

**Goal:** Recreate 22 visual assets in Gamma with a consistent dark theme (GitHub dark #0d1117), avoiding previous errors (red thin on blue, red on white). Use amber/white/blue palette from 21-carousel, not red-on-white.

**Base palette (from 21-carousel.html):**
- Background: `#0d1117` (dark)
- Card: `#161b22`
- Foreground: `#e6edf3`
- Muted: `#8b949e`
- Accent blue: `#58a6ff`
- Good green: `#3fb950`
- Amber (defect): `#F59E0B` (use for seam/defect, not pure red #f85149)
- No thin red lines on blue; use thick 4-6px amber or white.

---

## 1. Cover 1280×720 — `22-cover-boundaries.png`

**Gamma prompt:**

> Minimal dark tech cover, 1280×720, background #0d1117, title "Who Owns Quality at the Boundaries?" in large white #e6edf3, subtitle "The seam between teams has no owner, no test, no accountability." in muted #8b949e. Two rounded dark cards (#161b22) with blue #58a6ff border, left "TEAM A — Module + Tests GREEN", right "TEAM B — Module + Tests GREEN". Thick amber #F59E0B horizontal connector (6px) between cards with arrow. Above connector, amber rounded badge "DEFECT LIVES ON THE SEAM" in dark text on amber. Clean, no red, no thin lines, GitHub dark theme, vector flat, no photo.

**Do not:** red thin line on blue, red on white, glossy 3D.

**Export:** PNG 1280×720, 72dpi.

---

## 2. Feed Image 1080×1350 (4:5) — `22-boundary-map.png`

**Gamma prompt:**

> Dark feed image, 1080×1350 (4:5), background #0d1117, header dark card #161b22 with white title "QUALITY AT THE BOUNDARY" and muted subtitle "Most expensive defects live on the seam, not in the module". Three stacked dark cards (#161b22) with colored left border: 1) blue #58a6ff "1. Technical — Contracts • Events • Schemas • Version skew" 2) green #3fb950 "2. Organizational — Two teams, one journey • Named E2E owner" 3) amber #F59E0B "3. External — Vendors • Extensions • Delegated risk ≠ delegated ownership". Each card: white text for title, muted for "→ Contract test / Schema validation / Gate on PR". Small amber dot on seam line. Bottom: large blue #58a6ff card "THE QUESTION THAT FINDS THE GAP — Who can name the owner of the seam in under 10 seconds?" White text, plus small muted "If it takes longer, the defect is already scheduled." Minimal, flat, dark, no red on white.

**Do not:** white background, red text on white, thin red seam.

**Export:** PNG 1080×1350, 4:5, for LinkedIn feed.

---

## 3. Carousel 1080×1350 (6 slides) — optional, 22-carousel.pdf

**Slide 1 — Hook:**
> Dark slide, 1080×1350, background #0d1117, large white text "The most expensive defect you ever shipped lived on a boundary." Small muted subtitle "Between two teams. Between two systems. Between vendor and product." Dark card, no images, centered.

**Slide 2 — Why boundaries break:**
> Dark slide, two dark cards (#161b22) with blue border, left "Team A: All tests pass", right "Team B: All tests pass", amber thick connector "SEAM: contract • timing • failure mode" with amber badge "NO OWNER, NO TEST". White/blue text, no red.

**Slide 3 — Technical boundaries:**
> Dark slide, blue accent #58a6ff, title "1. Technical boundaries" white, bullet list in muted: "Contracts • Events • Schemas • Version compatibility". Small screenshot mock: "28/28 contract tests 94% API coverage — caught 3 drifts, UI 0". Dark card, code-style mono.

**Slide 4 — Organizational boundaries:**
> Dark slide, green #3fb950, title "2. Organizational boundaries" white, "Two teams, one journey → Named E2E owner + business invariant + observable evidence". Dark card with checklist "Owner: ___ / Invariant: ___ / Gate: contract test on PR". Green accent.

**Slide 5 — External boundaries:**
> Dark slide, amber #F59E0B, title "3. External boundaries" white, "Delegating implementation ≠ delegating product risk". Dark card with "Extension contracts • Compatibility rules • Certification gates". Amber accent, no red.

**Slide 6 — CTA:**
> Dark slide, blue #58a6ff full-bleed card, white text "Who can name the owner of your most critical seam in under 10 seconds? Comment with the seam — I'll reply with a one-line invariant you can gate tomorrow." Footer small muted "Victor Ematin · AI Quality Engineering Lead · Independent practice  •  Quality Operating Model #22 • © Victor Ematin" White/blue, centered.

**Carousel spec:** 1080×1350 per slide, 4:5, background #0d1117 throughout, consistent fonts (Helvetica/Arial), no red thin lines, no white feed, export as PDF 1080×1350.

---

**General Gamma settings:**
- Theme: Dark, minimal, GitHub dark
- Style: Flat vector, no photos, no gradients, no glossy
- Fonts: Sans, bold titles, muted subtitles
- Colors: Only #0d1117, #161b22, #e6edf3, #8b949e, #58a6ff, #3fb950, #F59E0B (no #f85149 thin red)
- Avoid: red on white, thin red on blue, light backgrounds for 22 series

**Source for 22 text:** `22-who-owns-quality-at-boundaries.md` (hook, three layers, question).
