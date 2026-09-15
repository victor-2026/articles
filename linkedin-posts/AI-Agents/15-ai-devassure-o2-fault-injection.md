**Format:** Pulse Article
**Series:** AI Testing
**Cover:** DevAssure O2 agent + injected bug + browser window, dark theme, "1 bug injected · 5 found" banner
**Feed Image:** Terminal screenshot showing O2 finding the injected whitespace-submit bug
**Hook:** I injected a bug into my own app on purpose. DevAssure O2 found it in minutes — then invented 4 more that didn't exist.

---

[COVER: 15-devassure-cover.png — O2 agent, injected bug flow, browser window, "1 real · 4 hallucinated"]

# I Broke My App on Purpose. The AI Test Agent Found the Bug — Then Invented 4 More

There's a new generation of testing agents that don't write tests you maintain. They read your pull request diff, map the blast radius, and test the change themselves in a real browser.

I decided to stress-test the most hyped one — **DevAssure O2**. But I didn't hand it a clean PR. I did the opposite: **I injected a real bug into my own app first.**

The agent found it. Then it did something far more interesting.

## The Experiment

Repo: my Playwright test bed (Buzzhive — a social app with posts, likes, comments). Stack: React frontend, FastAPI backend, Docker Compose.

**The injected bug** — 2 lines in `PostComposer.tsx`:
```diff
-  if (!content.trim()) return
-  disabled={!content.trim() || loading}
+  if (!content) return
+  disabled={!content || loading}
```

That's it. The submit button now stays enabled when the user types only whitespace. Backend accepts it (whitespace is ≥1 char). A regression that ships silently — no compile error, no crash, just wrong behavior that a human would have to notice.

Committed to branch `test/devassure-o2`, rebuilt the frontend, pointed O2 at the diff.

## What O2 Did

Command:
```
devassure test --base main --head test/devassure-o2 --url http://localhost:3000
```

**Score: 22/100. 5 scenarios run.** Here's what happened:

1. **Logged in as a real user** (alice@buzzhive.com) — full browser, no scripted selectors
2. Created a post, verified the composer clears after submission
3. Verified char count at 0, 50, and 2000 characters
4. Checked submit button states

And it **found the injected bug**:

> 🐞 **critical** — "Submit button remains enabled when post composer contains only whitespace characters, violating content validation rules"

That's the exact regression I planted. Real finding. Correct severity. **This part is genuinely impressive.**

[SCREENSHOT: 15-o2-terminal.png — O2 terminal output, caught whitespace-submit bug, Score 22/100]

## The Catch: 4 False Positives

Then O2 started inventing bugs. Here's what happened, step by step:

> **What O2 intended:** Execute `"A".repeat(2000)` as JavaScript to fill the field with 2,000 characters.
> **What O2 actually did:** Typed the literal 17-character string `"A".repeat(2000)"` into the textarea.
> **Where the logic broke:** Saw "17" in the character count, expected 2,000, and concluded the app corrupted the input.

The agent blamed the app for its own artifact. All 5 findings at a glance:

| # | Type | Finding | Status |
|---|------|---------|--------|
| 1 | Validation | Submit button enabled with whitespace-only content | ✅ **Real** (injected) |
| 2 | Functionality | App accepted literal JS code as post content | ❌ Hallucination |
| 3 | Functionality | Input field value differs from typed text | ❌ Hallucination |
| 4 | Validation | Char count unreliable with malformed input | ❌ Hallucination |
| 5 | Security | App fails to validate and sanitize content | ❌ Hallucination |

**O2 created the artifact itself, then blamed the app for it.**

[SCREENSHOT: 15-findings-table.png — 5 findings: 1 real critical + 4 hallucinations from its own tooling]

That's the pattern that matters. 5 findings total: **1 real critical, 4 hallucinations caused by its own tooling.** If you merge PRs on this output, you'll waste hours triaging phantom bugs — and eventually start ignoring the real ones.

## Why This Is the Real Story

A testing agent that finds 100% of injected bugs but reports 80% false positives is **net-negative for trust**. And trust is the thing that decides whether anyone runs it in production.

The agentic loop actually self-heals — O2 tried to use an unavailable `evaluate` tool, noticed, and switched to `input` without failing. That's real engineering. But self-healing tool use ≠ correct assertions. The gap is in **validation of its own actions**, not in execution.

## What I'd Fix First

1. **A human review gate** — every finding before merge. Non-negotiable today.
2. **Agent-artifact awareness** — O2 should distinguish "I typed garbage into the field" from "the app corrupted input". Its own input should never become evidence.
3. **Diff-to-assertion grounding** — the agent generated char-count tests because the diff touched the composer, but the *rule* (whitespace must not submit) came from my `app.yaml` config:
```yaml
rules:
  - "Post content must be non-empty after trimming whitespace"
  - "Post content must not exceed 2000 characters"
  - "Submit button disabled when content is empty or whitespace-only"
```
   The rules file is the single highest-leverage config change for reducing hallucinations. **It's a lever we control.**

## The ROI Question

O2 run time: **~7 min**. Time triaging 4 false positives: **~40 min**. Total for 1 real finding: **~47 min**. A skilled tester doing exploratory testing catches the same whitespace regression in ~15 min.

So O2 isn't faster today. But it runs unattended, on every PR, at 3 AM. The math flips when false-positive rates drop below 30% — and that's a config problem, not an architecture problem.

## Verdict

DevAssure O2 is real. It runs a browser, logs in as a user, reads diffs, and caught a genuinely sneaky 2-line regression in minutes. **The agentic execution layer works.**

But out of the box it's not PR-gate ready. 4 of 5 findings were its own artifacts. Budget for the triage cost, add a human gate, and treat every "critical" as "unverified until a human says so."

📌 **More from the AI Agents series:**

1. [You're Measuring the Wrong Thing](https://www.linkedin.com/pulse/youre-measuring-wrong-thing-victor-ematin-y4jkf/) — 36 runs, 2 projects, 0% lift: why agent architecture matters more than model choice
2. [Skills Are Not npm Packages](https://www.linkedin.com/pulse/skills-npm-packages-what-i-learned-building-8-agent-victor-ematin-by2qf/) — What I learned building 8 agent skills
3. [Your Test Framework Has Blind Spots — I Found 49% Across 2 Projects](https://www.linkedin.com/pulse/your-test-framework-has-blind-spots-i-found-49-2-projects-ematin-dkxgf/) — Kiro coverage gap analysis
4. [I Spent $15 to Test 7 AI Agents](https://www.linkedin.com/pulse/i-spent-15-test-7-ai-agents-0-tool-beat-200mo-tier-victor-ematin-bxcvf/) — 7 agents, 3 projects, $15 in API credits
5. [AI Testing Agents: 3-Month Field Report](https://www.linkedin.com/pulse/ai-testing-agents-2026-3-month-field-report-victor-ematin-s2abe/) — 10 agents, 4 real codebases, the wider picture
6. [AI User or AI Builder](https://www.linkedin.com/pulse/you-ai-user-builder-9-concept-maturity-test-victor-ematin-polhe/) — 9 concepts mapped to L1-L5: where the field report leads organizationally

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AITesting #QAAgents #Playwright #ZeroBudgetQA #AgenticTesting
