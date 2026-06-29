**Status:** 🎨 Hand off to designer

**Format:** LinkedIn Carousel PDF (10 pages in one PDF)
**Canvas:** 1920×1080 px per slide
**Audience:** Senior QA Engineers, Test Managers, SDETs
**Tone:** Positive — "I want to be ready for this change"
**Angle:** Data-driven, practical checklist, not fear-mongering

---

## Visual Specs

| Attribute | Value |
|-----------|-------|
| Canvas | 1920×1080 px (LinkedIn carousel standard) |
| Heading font | Inter Bold, 48pt |
| Body font | Inter Regular, 28pt |
| Background | Dark navy `#0F172A` |
| Accent color | Cyan `#06B6D4` |
| Highlight | Amber `#FBBF24` |
| Text | White `#F8FAFC` |
| UI mockups (Google/Meta) | Light `#E2E8F0` panels with brand colors |
| Branding | Bottom right: "Victor Ematin · $0 budget" on every slide |

---

## Slide 1 — Cover

**Visual:** Google + Meta logos side by side. Headline in bold. Subtitle below.
**Text:**
75% of Google's code is AI-generated.
So Google changed how it hires.

And Meta, Stripe, Amazon, Coinbase followed.

*The 6 markers every QA engineer needs in 2026*

---

## Slide 2 — Timeline: Who Started When

**Visual:** Horizontal line with dot markers. Company logos on dots. Dates below.
**Text:**
Jun '25 — Canva
Oct '25 — Meta
Late '25 — Shopify · LinkedIn · Rippling
Apr '26 — Google · DoorDash
2026 — Stripe · Amazon · Microsoft · Coinbase

**Takeaway:** If you haven't started preparing, 2026 is the year.

---

## Slide 3 — What Google Tests Now

**Visual:** 3-panel CoderPad mockup (file browser | code editor | Gemini chat). Each panel has a label.
**Text:**
Code Comprehension — analysis + debug, not write from scratch
Prompt Engineering — can you instruct AI precisely?
Validation — can you catch AI mistakes?

**Roles:** L3–L4 + QA explicitly included

---

## Slide 4 — What Meta Tests Now

**Visual:** Flow diagram with 3 arrows: Bug Fix → Logic (~120 lines) → Optimization.
**Text:**
60-min session. GPT / Claude / Gemini / Llama in CoderPad.
3 stages: fix bug → implement logic → optimize performance
4 competencies: Problem Solving, Code Quality, Verification, Communication

⚠️ Blind copy-paste of AI code = instant fail

---

## Slide 5 — Stripe, Amazon, Microsoft, Coinbase

**Visual:** 4-column comparison. Each has logo + 1-line description.
**Text:**
Stripe — HackerRank + AI chat. Tasks unsolvable without AI in 40 min.
Amazon — OA with Amazon Q. Work with existing repo, not blank slate.
Microsoft — 45-min live Copilot round (CoreAI / Bing teams).
Coinbase — AI in all sessions. Focus: verbal reasoning on data structures.

---

## Slide 6 — The 6 Markers of AI Fluency

**Visual:** Hexagon diagram with 6 labeled nodes. Center text: "What companies screen for."
**Text:**
1. Output Validation — catch plausible-but-wrong code
2. Prompt Granularity — small slices, not one-shot
3. Technical Ownership — you drive, AI executes
4. Debugging AI — recognize hallucinations
5. Strategic Delegation — mechanics to AI, logic to you
6. Narration — explain why you prompt this way

---

## Slide 7 — The #1 Rule: 3-5 Minutes Without AI

**Visual:** Timer icon showing "3:00". Stop hand before AI chat icon. Arrow shows sequence: Read → Think → Plan → *then* Open AI.
**Text:**
"The 3-5 Minute Rule" — first minutes = no AI
Think → Plan → State approach → THEN open AI

Proves you're the architect, not the passenger.
Trap: "Answer Machine" — pasting problem into AI immediately

**Narrate:** "I'm taking 3 minutes to understand requirements."

---

## Slide 8 — The #1 Trap: Passive Agreement

**Visual:** Red X over copy-paste icon. Green checkmark checklist beside it.
**Text:**
"Looks correct" = instant fail at *every* company

**AI Bugs Checklist:**
☐ Off-by-one errors (most common AI mistake)
☐ Hallucinated APIs (libraries that don't exist)
☐ `time.time()` instead of `time.monotonic()`
☐ O(n²) when O(n log n) needed
☐ Missing null checks on empty inputs

**Workflow:** Prompt → Review → Run → Confirm

---

## Slide 9 — Why This Hits QA Hardest

**Visual:** 4 visual blocks. Each block shows "Old → New" with an icon.
**Block 1 (Test):** Write test from scratch → Prompt AI to generate
**Block 2 (Assert):** Recall assert syntax → Find edge cases in AI output
**Block 3 (SQL):** Write SQL manually → Validate AI-generated queries
**Block 4 (Agent):** Solve alone → Manage AI agents

**Bottom text:** QA is literally about verification. This plays to your strength.

---

## Slide 10 — Ready? 3 Practices for This Week

**Visual:** Phone wallpaper mockup with 3 checklist items. Each has a small icon.
**Text:**
15 minutes each. Pick one to start Monday:

1. **3-5 Minute Rule** — pick a problem, plan architecture, state approach, *then* open AI
2. **Prompt Granularity** — break one task into 3 small prompts vs 1 giant one
3. **Audit Mindset** — review AI code for 5 min. Look for plausible-but-wrong patterns

**CTA:** Comment 1, 2, or 3 — which one starts your Monday?

---

## Notes for Designer

- All text in English (LinkedIn International)
- Branding ("Victor Ematin · $0 budget") bottom right on every slide, opacity 70%
- Slide 1 cover headline = largest text on the deck
- Timeline (slide 2) — use simple dots + lines, no complex illustration needed
- Google/Meta panels (slides 3-4) — use generic CoderPad-colored UI, not real screenshots
- Hexagon (slide 6) — center text small, 6 nodes evenly spaced
- Export as single multi-page PDF (LinkedIn carousel format)
