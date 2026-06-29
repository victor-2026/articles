# Carousel: 30 Minutes with Playwright Agents

**Format:** 1920×1080 PDF (LinkedIn auto-converts to slides)  
**Design:** Dark theme (like Allure dashboard), minimal text per slide

---

## Slide 1 — Cover
**Title:** 30 Minutes with Playwright Agents  
**Subtitle:** The Healer Is Not an Agent — It's You  
**Background:** Allure dashboard — **86 passed, 0 failed, 1 flaky, 2 skipped**  
**Author:** Victor Ematin · AI Quality Engineering Lead · OpenCode Go

---

## Slide 2 — What Healer Fixed
**Title:** Healer Handled Interface Drift  
**Two cards:**
- ✅ **2 stale snapshots** — regenerated (pixel diff 0.05)
- ✅ **1 test improved** — removed `fullPage: true` on admin table (unstable height)

**Key insight:** Healer fixes selectors, timing, assertions — and visual regression.

---

## Slide 3 — What Healer Missed
**Title:** But 3 Bugs Were Deeper  
**Three cards:**
1. Employee ID "0001" — 3 users share it → API rejects every save
2. `Admin` matches 3 rows → strict-mode violation (data quality, not locators)
3. @local tests run twice in parallel → empty table on delete

**None of these are selector issues. All are data-level.**

---

## Slide 4 — What I Fixed
**Image:** `6-what-i-fixed.png`  
**Caption:** 8 lines changed. Zero selector fixes.

---

## Slide 5 — Planner Actually Helps
**Title:** Planner — The Useful Agent  
**Flow:**
```
Planner explore → 419-line plan → 25 scenarios
  → Generator → 3 E2E tests (all pass)
  → Healer → fixes visual (not data-level)
```
**Result:** New module written in 30 minutes.

---

## Slide 6 — Comparison: 3 Tools, 3 Layers
**Image:** `6-comparison.png`

---

## Slide 7 — Takeaway
**Three numbers:**
- **86** tests passing
- **8** lines changed
- **$0** spent

**Bottom line:** All 3 tools are needed — each covers one layer. None fixes data-level bugs.

**CTA:** What data-level bug did your AI testing tool miss?
