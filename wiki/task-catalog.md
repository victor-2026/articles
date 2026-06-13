# Task Catalog

## Project: OrangeHRM

### Admin autocomplete fix
Description: Employee Name field in Admin → Add User shows "Invalid" on fresh OrangeHRM 5.4 instance. Root cause: autocomplete dropdown not selecting. Fix POM or skip gracefully.
Priority: P0

### Upgrade local Docker to OrangeHRM 5.8.1
Description: Current local instance runs OrangeHRM 5.4. Upgrade docker-compose to 5.8.1. Verify all existing tests still pass. Document breaking changes.
Priority: P1

### Performance reviews: add test data
Description: Performance module has zero seed data on local instance. Create employees + reviews via API or SQL so performance tests can run.
Priority: P1

### MAINT-003: Purge employee data
Description: Write test for Maintenance → Purge Records → search employee → purge. Destructive, runs only on local (@local tag).
Priority: P1

### Claim module investigation
Description: Claim module not installed in OrangeHRM 5.4. Check if available in 5.8.1, install, write basic test.
Priority: P2

### CI/CD: add Allure publish step
Description: GitHub Actions workflow should generate and publish Allure report as an artifact after test run.
Priority: P2

---

## Project: Buzzhive (qa-automation-sandbox)

### GitHub Variables: set BACKEND_URL + FRONTEND_URL ✅ DONE (Session 45, 2026-06-10)
Description: CI/CD workflows (uptime, nightly, contracts, mutation) need GitHub repo Variables set. BACKEND_URL = qa-automation-playwright-1.onrender.com, FRONTEND_URL = qa-automation-playwright-front.onrender.com.
Priority: P0

**Status:** Both variables set via `gh variable set` on 2026-06-10:
- `BACKEND_URL` = `https://buzzhive-test.onrender.com` (legacy, NOT the new `-1` URL — see note)
- `FRONTEND_URL` = `https://qa-automation-playwright-front.onrender.com`

**Note on BACKEND_URL divergence:** The task spec says `qa-automation-playwright-1.onrender.com` but the actual value is `buzzhive-test.onrender.com` (legacy FastAPI). Decision 2026-06-10: keep legacy because the new URL returns HTML for `/openapi.json` (likely a frontend reverse-proxy, not FastAPI). CI tests need OpenAPI export → need legacy. When/if the new service exposes OpenAPI docs, the var can be flipped.

### k6: expand load tests
Description: Existing k6 script test GET endpoints only. Add POST endpoints (posts, follows), scale to 100+ VUs on Windows Server.
Priority: P1

### render.yaml: decide legacy vs -1 backend
Description: Two backend services exist (buzzhive-test legacy, qa-automation-playwright-1 new). Decide: update render.yaml or deprecate one.
Priority: P1

### Pact consumer contracts Phase 2
Description: Phase 1 done (schema validation). Phase 2: Pact consumer-driven contracts for auth + posts endpoints.
Priority: P1

### Autonoma pipeline on Buzzhive API
Description: Run Autonoma on Buzzhive codebase. Create Environment Factory for Buzzhive entities (users, posts, follows). Compare Autonoma specs vs existing 2000+ Playwright tests.
Priority: P2

---

## Project: Articles & LinkedIn

### SWE-Tester rewrite
Description: Existing post has 309 imp, 0 engagement. Rewritten draft exists. Decision: edit in-place (keep URL) or delete + publish new as fresh post.
Priority: P1

### From Vibing rewrite
Description: Existing post has 252 imp, 1 like. Rewritten draft exists. Decision: edit in-place or delete + publish new.
Priority: P1

### Post: Anti-Flaky Patterns carousel
Description: Topic: expect() over waitForTimeout, 3 mock levels, expect.poll. Source material in raw/anti-flakiness-habr.md. Format: carousel.
Priority: P1

### Post: Role of QA in AI Era (5 theses)
Description: Quality Gap (54.5% deployed, 44.1% disabled), Knowledge Transfer Risk, New Skill Stack, Philosophy, Superpowers. Has Old draft to resurface.
Priority: P1

### Article: Why AI Agents Cheat in CI/CD
Description: Source: llm-agents-cicd-cheating-habr.md (11K views on Habr). LLM agents choose cheating over solving tasks. Strong hook.
Priority: P2

### Article: Hidden Costs of Vibe-Coded Apps
Description: Source: hidden-costs-vibe-coded-apps.md. 80/20 problem — demo-ready vs production-safe. Security, CI/CD, monitoring gaps.
Priority: P2

### Carousel: Desktop AI Agents 2026 Comparison
Description: Source: desktop-ai-agents-2026.md. 20+ AI coding tools compared across 5 tiers with pricing.
Priority: P2

### Article: Notion → Telegram → OpenCode architecture
Description: Document the orchestration model with architecture diagram. Explain layers: Notion (plan), Telegram (dispatch), OpenCode (execute).
Priority: P2

### Post: Comprehension Debt
Description: Source: comprehension-debt.md. Hidden cost of AI-generated code shipped without understanding.
Priority: P2

### Cross-link article series
Description: Провязать серии статей ссылками друг на друга. Сейчас статьи опубликованы изолированно — нет перекрёстных ссылок между связанными темами (QA Metrics DORA, AI Agents comparison, Autonoma vs Mabl vs Testsigma, Playwright Test Agents). Добавить backlinks в конец каждой статьи, сгруппировать по сериям.
Priority: P1

---

## Project: Career

### Precisely: Cover Letter
Description: CV sent (Principal Technology Architect – QA). CL ready in template CL_AI_QA_Lead.md. Customize and send.
Priority: P1

### Smartcat: follow-up after Jun 5 recruiter screen
Description: Vika Alimova interview done Jun 5. Need to check status, send thank-you, prepare for next round if any.
Priority: P1

### Ascendion: track response
Description: CV + CL sent. Track if any response received.
Priority: P2

---

## Project: Telegram Bot (@Victor435_bot)

### /task fetch from Notion API
Description: Currently /task reads local kanban/*.md. Replace with Notion API: get database ID, query Tasks database, return live data. Provides typed and detailed descriptions from Notion.
Priority: P1

### Notion webhook → auto-trigger on "In Progress"
Description: When user moves task to "In Progress" in Notion, Notion webhook → Telegram bot → auto-execute /task run. Requires public endpoint (ngrok / server tunnel).
Priority: P2

### Add GitHub Copilot models
Description: Copilot Free plan available (claude-haiku-4.5, gpt-5.4-nano, gpt-5.4-mini, gpt-5.2). Add to model list and route to correct prefix.
Priority: P2

### /batch command
Description: Accept list of tasks, run them sequentially with specified agents. Format: /batch orangehrm admin-fix --agent qa, articles post --agent writer
Priority: P2

---

## Project: QA Architecture (Cross-Project)

### Quality Gates: automate 3-layer checklist
Description: Anton Gulin 3-Layer gates (Scope, Data, State, Run, Evidence, Review) added to AGENTS.md for sandbox + OrangeHRM. Next: automate as CI check or pre-commit hook. Script validates trace exists, CI passed, test maps to a named risk.
Priority: P2

---

## Project: Notion Integration

### [W1] Import ai-qa-wiki into Notion
Description: Export ~50 .md files from ~/Projects/ai-qa-wiki/wiki/ as pages into Notion. Check formatting, backlinks, structure.
Priority: P1

### [W1] Test Notion Agent: search, Plan Mode
Description: Chat with Notion Agent. Try "find articles about mutation testing", "create a summary of all OrangeHRM tests". Evaluate response quality.
Priority: P2

### [W2] Create DB "Test Runs"
Description: Database with columns: date, module, pass count, fail count, status (PASS/FAIL). For tracking test execution history.
Priority: P2

### [W2] Custom Agent: Q&A from wiki
Description: Create Custom Agent that answers team questions from Notion knowledge base. Connect to Slack. Test with AI-QA-Wiki content.
Priority: P2

### [W2] Custom Agent: daily standup
Description: Custom Agent reads Tasks database, collects In Progress items, posts formatted standup to Slack channel on schedule.
Priority: P2

### [W3] Integrated orchestration: Notion queue → Telegram dispatch
Description: Full pipeline: Notion tasks flow to Telegram bot via webhook, bot dispatches to appropriate agent (qa/writer/reviewer/career), result posted back to Notion. Requires Notion API integration.
Priority: P1

### [W3] External Agents API: test OpenCode connection
Description: Register OpenCode as external agent in Notion. Try assigning a task from Notion to OpenCode. Evaluate if API is stable enough for regular use.
Priority: P2

### [W4] Workers: Allure/Playwright report → Notion
Description: Write Notion Worker that parses Allure JSON/XML results and creates a report page in Notion automatically after test run.
Priority: P2

### [W4] Workers: GitHub Actions webhook → Notion
Description: Capture GitHub Actions workflow completions via webhook. Create/update a "CI/CD Runs" database in Notion with results.
Priority: P2

### [W9] Vendor lock-in assessment
Description: After 2+ months of Notion use, evaluate: what would we lose if trial ends? Cost of migration back to local .md? Decision: hybrid or full Notion.
Priority: P2

## Infrastructure & Tools

### Verify wiki_llm.py script
Description: Script at `Positions-CV-CL/scripts/wiki_llm.py` uses Groq API. Verify it works with current API key. Check which other projects could benefit (ai-qa-wiki already has groq_qa.py, Articles could use for raw/ analysis, Test-Dora-Plus had it but file missing).
Priority: P2

### Bot: debug Groq 180s timeout
Description: 2597 errors today — Groq API calls exceed 180s. Bot returns "Timed out after 180s" for most messages. Fix: add retry, use faster model, or increase timeout+split long responses.
Priority: P1
