# DORA Carousel — Visual Design Spec

**Style:** Clean, professional, tech.
**Font:** Inter (headings bold 36-48px, body 16-20px)
**Colors:** Dark navy (#1e3a5f) → teal (#0d9488) gradient for cover.
           White backgrounds for content slides.
           Green accent (#16a34a) for Elite/positive.
           Red accent (#dc2626) for problem/before states.

---

## Slide 1 — Cover
Text: "QA → DORA: 2 Metrics on Elite"
Subtitle: "How I mapped my test pipeline to 4 DORA metrics"
Bottom: Victor Ematin · AI Quality Engineering Lead
Visual: Dark navy-to-teal gradient background. Center: stylized 2x2
        dashboard icon with checkmarks (teal). White text.

## Slide 2 — Problem
Text: "QA metrics no one needs"
Visual: Split screen. Left: stack of papers (coverage reports,
        test cases) crossed out with red X. Right: empty space
        with "So what?" question mark. Dark navy header bar.
Bottom quote (bold): "DORA speaks business language."

## Slide 3 — Map: DORA ↔ QA
Text: "4 metrics = 4 QA artifacts"
Visual: Full-width table with 4 rows. Left column: DORA metric name
        (dark navy background, white text). Right column: QA equivalent
        (light gray background, dark text). Arrow icon between columns.
Rows:
  Change Failure Rate → Mutation score (34/34 caught)
  CI/CD Stability → Pass rate + flaky (40→0)
  Lead Time for Changes → Regression (3d→4h)
  MTTR → Fix time (1-line, immediate)

## Slide 4 — Dashboard
Text: "One Grafana, 4 DORA metrics"
Visual: Full-screen screenshot of dora-dashboard.png as background,
        slightly dimmed. Four overlay labels on the dashboard panels:
        CFR, Stability, Lead Time, MTTR (white text, semi-transparent
        dark background pill). Bottom bar: "Grafana + Infinity plugin.
        No Prometheus, no external DB. 3 hours setup."

## Slide 5 — CFR: Change Failure Rate
Text: "Elite. 0% failure rate."
Big number: "34/34" (green, centered)
Subtitle: "mutations caught = 0% CFR = Elite level"
Visual: Left side — scrollable list of mutation types with green
        checkmarks (SQL injection, missing auth, broken WHERE, wrong
        JOIN...). Right side — circular progress indicator 100% in green.
        White background.

## Slide 6 — Stability: CI/CD
Text: "High. From 78% to 94%."
Big number: "40+ → 0" (green)
Subtitle: "waitForTimeout eliminated"
Visual: Upward line chart with two dots: ~78% (red) → ~94% (green).
        Below chart: two columns — "Before: 40+ flaky tests" (red)
        vs "After: 0 flaky" (green). Playwright browser icon on right.
Bottom: "CI stability is not about speed. It's about predictability."

## Slide 7 — Lead Time: Regression
Text: "High → Elite. 3d → 4h."
Big number: "3 days → 4 hours"
Subtitle: "regression execution time"
Visual: Timeline. Left: large red block "3 days". Right: small green
        block "4 hours". Arrow between them labeled "Wimark project".
Bottom: "What took 3 days takes 4 hours. The difference is test
        architecture, not tools."

## Slide 8 — MTTR: Mean Time to Recover
Text: "Elite. Immediate."
Big number: "< 1 minute"
Subtitle: "time to fix a flaky test"
Visual: Timer/stopwatch icon on green background. Right side: dark
        code block showing "1-line fix". Below: "Root cause → fix →
        push. All in one CI session."

## Slide 9 — Results
Text: "5 dashboards, 2 projects, 1 Grafana"
Visual: Grid of 5 miniature dashboard screenshots (blurred/styled):
  🟡 DORA Core — 4 metrics
  🟠 OrangeHRM — 20%→65% coverage
  🔵 Buzzhive — 78%→94% pass rate
  🟢 Quality Gates — 34/34 mutations
  🔴 AI Agents — KISS $0.01 vs Webwright $2.37
Bottom: "All dashboards self-contained. No Prometheus, no external DBs."

## Slide 10 — CTA
Text: "Find your CFR."
Center: bold question — "What percentage of your changes fail in production?"
Three bullets below:
  • Start with mutation tests
  • Map each DORA metric to a QA artifact
  • Build your dashboard (3 hours, Infinity plugin, ready)
CTA line: "Comment your CFR. Or ask a question — I'll answer."
Bottom: Victor Ematin · AI Quality Engineering Lead · OpenCode Go
Hashtags: #DORA #TestAutomation #Grafana
