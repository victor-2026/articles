**Format:** LinkedIn Pulse Article
**Series:** AI & QA
**Cover:** Google/Meta logos + interview whiteboard with AI
**Feed Image:** Google Code Comprehension round — Gemini interface during interview
**Hook:** "75% of Google's code is now AI-generated. So Google replaced its coding interviews with something else: an AI Fluency test."

---

[COVER: Google + Meta logos side by side, headline "AI Fluency Is the New Interview Standard"]

# Google Now Tests AI Fluency, Not Code — Here's What Changed Overnight

Last week I almost applied for a role I knew I'd nail on paper — until I read the interview format. Instead of "write a sorting algorithm," the new process said: "use Gemini to solve this problem and explain why you trust its output."

I wasn't being tested on syntax. I was being tested on how well I could **validate AI-generated code**.

This is not an experiment. It's an official pilot, and it's already running at Google, Meta, Canva, and Cognition (the team behind Devin).

## What Google Changed

Sundar Pichai confirmed what many suspected: **75% of all new code at Google is now AI-generated**. Writing code from scratch is no longer the bottleneck — verifying, debugging, and improving AI output is.

The new interview format replaces one algorithmic round with a **Code Comprehension** session:

- You have access to **Gemini** throughout
- You're given a problem and AI-generated code
- You're evaluated on: prompt quality, output validation, edge case coverage, debugging skill
- QA/Automation roles are explicitly included

The old question: "Can you write this from memory?"
The new question: "Can you tell me why this AI-generated answer is wrong?"

[SCREENSHOT: Google interview format table — Old vs New]

## Meta Followed Within Weeks

Meta's pilot goes further. One full algorithmic round is replaced by a **60-minute AI-Enabled Coding session** with models from OpenAI, Anthropic, and Google connected to the IDE.

The evaluation criteria:

| What They Don't Test | What They Test |
|----------------------|----------------|
| Syntax recall | Prompt engineering |
| Algorithm memorization | Output validation |
| Writing from blank slate | Debugging AI mistakes |
| Solo problem-solving | AI agent orchestration |

[SCREENSHOT: Table — Old vs New interview criteria]

## Cognition's HR Director Put It Best

> "Interviewing without AI is like a math test without a calculator."

Emily Cohen, HR Director at Cognition (makers of Devin), says they removed algorithm memorisation entirely. Candidates are evaluated on how they manage AI agents on real product tasks.

Canva did the same. The consensus across all four companies: **passive acceptance of AI output is an instant fail**.

## What This Means for QA Engineers

This shift hits QA harder than most roles — because our entire workflow is about **verification**.

The skills that now matter in interviews:

- **Prompt engineering** — generating test cases, assertions, data setups via AI
- **Output validation** — spotting hallucinations, missing edge cases, security holes in AI-generated tests
- **Debugging AI code** — fixing what the model got wrong
- **AI agent orchestration** — managing a pipeline of Planner → Generator → Healer agents (yes, that's a real Playwright feature now)

The red flag recruiters are trained to catch: **copy-paste without thinking**.

## The Takeaway

If you're preparing for interviews this year, don't spend another week memorising LeetCode patterns. Spend it learning how to **read AI-generated code critically**, how to write prompts that produce reliable output, and how to explain *why* you trust — or don't trust — what the model gave you.

Because the interview format changed. And the candidates who adapt first will be the ones who pass.

---

**Victor Ematin** · AI Quality Engineering Lead · OpenCode Go

#AIInterview #AIInTech #QAEngineer #TestAutomation #HiringTrends
