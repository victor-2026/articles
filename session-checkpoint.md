# Session Checkpoint — 2026-06-30

## Session — Maestro vs Appium + LinkedIn Analytics

- **Новый каталог:** `linkedin-posts/Tools/` — статья + фид-пост + сценарий карусели
- **Статья:** `maestro-vs-appium-frontrow.md` — полный разбор (35 flows, 8 modules, 0 flaky)
- **Фид-пост:** `maestro-vs-appium-post.md` — улучшен (цифры в ритме, живой баг из лога)
- **Карусель:** `maestro-vs-appium-carousel-prompt.md` — 8 слайдов для NotebookLM (код в полутоне)
- **AI Fluency приостановлен** — carousel 49 imp (в 12x ниже среднего). Аудитория не откликается
- **План публикации:** Maestro vs Appium 1 июля 9:00, NextDay interview 2 июля (mobile AI apps)
- **Avito кейс перенесён** на 08.07
- **Appium код найден:** wdio.ios.conf.ts + login.spec.ts + smoke.spec.ts + helpers.ts — 4 файла реального проекта
- **Wiki:** `ai-qa-wiki/wiki/maestro-vs-appium-2026.md` — дополнен кейсом FrontRow
- **90-day analytics:** записаны в `wiki/follower-engagement-analysis-2026.md`

# Session Checkpoint — 2026-06-29

## Session — Follower/Engagement 90-day analysis

## Session — AI Fluency Article (scheduled Jun 25)

- **New directory:** `linkedin-posts/AI-Fluency/`
- **Article:** `interview-format-change.md` — "Google Now Tests AI Fluency, Not Code"
- **Feed post:** `ai-fluency-post.md` — ~400 chars
- **Sources:** Entrepreneur, Business Insider, Briefs Finance, Asia Business Daily, MockIF, YouTube
- **Tags:** #AIInterview #QAEngineer #TestAutomation #HiringTrends #AIInTech
- **Needs before publish:** [SCREENSHOT] images (2 tables), [COVER] image

**Hook:** "75% of Google's code is now AI-generated. So Google replaced its coding interviews with something else: an AI Fluency test."

**Money paragraph:** "I wasn't being tested on syntax. I was being tested on how well I could validate AI-generated code."

---

# Session Checkpoint — 2026-06-20 → 2026-06-21

## Session — Article 7 Final Polish + Buzzhive Replication

### Article 7: "You're Measuring the Wrong Thing"
- **Scheduled:** 2026-06-22 9:15
- **Cover:** 7-cover-linkedin.png (1200x644, LinkedIn-safe)
- **Screenshots (6 PNGs):** results-table, stack-comparison, high-lift-targets, artifacts-tree, cover-linkedin, appendix
- **Buzzhive replication added:** 36 runs total (18 OrangeHRM + 18 Buzzhive), 0% lift on both stacks
- **Model fixed:** Nemotron 3 Ultra Free (was big-pickle)
- **Disclaimer moved:** from under hook to methodological note
- **Hashtags:** 5 (#QAAutomation removed)
- **Feed post:** 3 emoji (test-tube, chart, dart), ~550 chars
- **GitHub link:** restored (experiments committed + pushed: cdb1769)
- **OrangeHRM link:** local only (no GitHub remote)
- **Russian summary:** 7-summary-rus.md saved
- **Discord post sent to autotesting channel**

### Article 8: "Skills Are Not npm Packages"
- Content ready, awaiting renumber as Part 2
- Russian summary: 8-summary-rus.md saved
- Needs: cross-link to Article 7, renumber, verify images

### Skills Experiment
- 18/18 Buzzhive runs completed — confirms OrangeHRM findings (0% lift)
- Generated: experiments/skill-reliability/generated/ (6 files), runs/ (18 outputs)
- Commit: cdb1769 feat(experiment): skill reliability experiment

### CoreStar
- QA Team Lead — Applied 2026-06-20 via LinkedIn
- BI QA Engineer (#105 on BambooHR) — adjacent vacancy at same company

## Key Decisions
- Article 7 + 8 are 2-part series: 0% lift proof → 3-layer architecture explanation
- Keep [COVER] marker only at top (bottom removed by user in LinkedIn UI)
- Experiment files not on GitHub for OrangeHRM — local path only

## Session 57b (2026-06-22) — Article 7 Published + Performance Log Updated

**Article 7 "You're Measuring the Wrong Thing" published 2026-06-22 ~9:00 CET:**
- 0% lift experiment, 36 runs, 2 projects, 3 skills
- 4h after publish: **200 impressions** on both article + feed post
- Feed post: https://www.linkedin.com/posts/victor-ematin_aiagents-testing-playwright-activity-7474706516189581312-e00i
- Performance log updated (md + csv)

## Next Actions
1. Prepare Article 8: renumber as Part 2, add cross-link to Article 7, verify images
2. Evening ritual 21:00 — retro, analytics, weekly report, lint AGENTS.md/checkpoints
