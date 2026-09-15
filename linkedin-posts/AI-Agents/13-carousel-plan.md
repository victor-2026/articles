# NotebookLM Scenario: Desktop AI Agents Comparison Carousel

## Instructions for NotebookLM

Generate a 7-slide HTML presentation (1920×1080, dark theme) for LinkedIn carousel. Use the source data below.

## Format Spec

- Dimensions: 1920×1080 px per slide
- Background: Dark (#0d1117) — GitHub Dark theme
- Font: system sans-serif, white text, large sizes
- No emoji on slides
- Each slide is a full-width div with flexbox centering
- Output as a single HTML file with slides stacked vertically (for screenshotting)

## Source Data

### Slide 1 — Cover
Headline: I Tested 7 AI Agents Against a $500/mo Tool
Subheadline: The $0 tool won on every metric
Footer: 3 projects · Same POM spec · Total spend: $15/mo

### Slide 2 — The Contenders
Headline: 7 Agents, 3 Projects
List in two columns:
Left: OpenCode ($10/mo) · Aider ($0) · Kiro ($0) · Devin ($500/mo)
Right: Autonoma ($5/run) · Antigravity (free→$20) · Claude Code ($20-200/mo)
Subheadline: Same tasks: POM generation, E2E tests, codebase analysis

### Slide 3 — Devin vs Aider
Headline: Same Spec, Two Results
Table:
| Metric | Devin ($500/mo) | Aider ($0) |
| POM methods | 4 | 10 |
| Tests | 7 (unverified) | 1 (auto-fixed via CI) |
| First green run | ❌ | ✅ 15.4s |
Bottom line: "$500/mo vs $0 — the cheaper tool was more reliable."

### Slide 4 — Kiro's 30-Minute Audit
Big number: 89 / 109
Label: endpoints untested (81.65%)
Second number: 36 security files with zero auth tests
Subheadline: Detected a breaking change CI would miss.
Bottom: "$0, 30 minutes of analysis."

### Slide 5 — The Cost Breakdown
Headline: Cost Per Agent
List (no table):
- OpenCode: ~$10/mo → 600+ tests, 13 POMs, 10 workflows
- Aider: $0 → auto-fix loop, deeper POM
- Kiro: $0 → 89 endpoints, 36 security files
- Devin: $500/mo → unverified output
- Autonoma: $5/run → crashed at step 4/6

### Slide 6 — The Verdict
Headline: Open Source Won on Every Metric
Four cards in a row:
1. OpenCode — Top Value — 600+ tests at $10/mo
2. Aider — Best Quality — auto-fix via --test-cmd
3. Kiro — Must-have — audit blind spots for free
4. Devin — Overpriced — unverified at $500/mo

### Slide 7 — Quick Setup + CTA
Headline: $10/mo QA Stack
Bullet list:
1. Daily generator: OpenCode + gpt-4o-mini
2. Spec & auto-fix: Aider with --test-cmd
3. Security audit: Kiro (once per sprint)
4. Cost guardrail: Hard billing limits
CTA: Full article with code and screenshots — link in comments
Footer: Drop your cost-per-test below 👇
