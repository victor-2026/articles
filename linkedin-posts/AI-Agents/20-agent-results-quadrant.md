**Format:** Pulse Article
**Series:** AI Engineering
**Cover:** 20-cover-quadrant.png ✅ (also used as Feed Image for the post)
**Feed Image:** 20-cover-quadrant.png ✅
**Hook:** Агент нашёл 5 багов. 4 были выдуманы. Как измерить доверие к агенту - квадрант результатов.
**Based on:** DevAssure O2 run (Session 87, 5 findings: 1 real + 4 artifacts); Manjunath k comment (Aug 19): "How are you measuring false confidence — a healed test that masks a real product regression?"; 34/34 mutations (Playwright API + DB, social-app backend); Meta ACH (arXiv:2501.12862); commercial AI-QA platform decoy pilot (Aug 26, 3 green runs 5/5 with two identical sign-in forms, reported "0% business risk", visual diff 2.20%→3.19% not flagged as ambiguity)
**Wiki:** ai-qa-wiki/wiki/ai-qa-tool-evaluation-mutation-matrix.md

---

<!-- COVER: 20-cover-quadrant.png — 2x2 quadrant: TP/FP/TN/FN, agent results vs reality -->

# Your Agent Found 5 Bugs. 4 Were Imaginary.

Our DevAssure O2 run found a real bug — whitespace-only posts could be submitted. Then it produced 4 more findings. All artifacts of its own actions: it injected data, then "discovered" the injection as a bug.

**1 of 5 findings survived review: 20% confirmation rate, 80% false-discovery rate.**

The agent was genuinely useful — and if you auto-trusted its report, you'd chase up to four false investigations per confirmed bug. This is the question every team adopting AI testing agents needs to answer: **how do you measure false confidence?**

## The quadrant

Agent results have four cells, and only two of them get attention:

<!-- SCREENSHOT: 20-cover-quadrant.png — 2x2 quadrant: TP/FP/TN/FN; FP (hallucinated) and FN (missed) are the quiet cells; green ≠ true -->

```
            Bug is real          No bug
Agent       TP — true positive   FP — false positive
reported                          (hallucinated bug)
Agent       FN — false negative  TN — true negative
silent      (missed bug)
```

The metrics that matter are the quiet ones: FP rate and FN rate. A demo shows TP. The other three cells are what demos usually hide.

## Four failure modes, one quadrant

What teams call "loss of trust" is usually four different failures. Each has its own cell and its own probe:

**1. The hallucination (FP)** — reports a bug that isn't there. Its own actions look like bugs to it: it injects data, then "discovers" the injection.
*Probe:* review gate — 1 of 5 survived: 20% confirmation rate, 80% false-discovery rate (a point estimate for this sample, not the classic FP rate, which needs TN counts we didn't collect).

**2. The miss (FN)** — silent on a bug that is real. The quiet cell: nothing fails, so nobody looks.
*Probe:* fault injection — 34/34 injected faults caught, 0 survivors (Playwright API + DB mutations on a social-app backend).

**3. The healed test (FN)** — green, but checks a string, not behavior; the regression is masked by green. `#pay-now` → `#checkout-pay` is a legit heal; `#pay-now` → `button:has-text("Pay")` silently weakens the assertion to "some element with Pay in it", so the test passes against a modal overlay instead of the checkout element.
*Probe:* mutation testing + diff review on every heal.

**4. The blind first-match (FN)** — picks the first matching target; ambiguity unseen.
*Probe:* decoy targets (duplicate elements).

Mutation-style injection is the engine behind 3 and 4 — a decoy is just a fault injected into the DOM instead of the code. If a mutant survives, the test checks a string, not behavior. Meta runs the same pattern at scale — ACH ("Mutation-Guided LLM-based Test Generation at Meta", arXiv:2501.12862): it generates a few targeted, currently-undetected mutants, filters out equivalent ones with an LLM-based equivalence-detector agent (LLM-as-judge), and runs JIT on changed code only.

## Second experiment: a commercial AI-QA platform

To see how these failure modes show up in practice, I ran the same probes through a commercial AI-QA platform. I imported a 5-test Playwright suite, then injected mutations into the app it tests. Three runs — baseline, then two decoy injections — came back 5/5 green; all three exported reports stated **"0% business risk, Low severity"** and "no risk detected" (their risk wording, quoted as reported).

<!-- SCREENSHOT: 20-quadrant-validate.png — three runs: baseline 5/5 green, weak decoy green 2.20%, strong decoy green 3.19%; "Green ≠ true" -->

The decoy was a second, visually identical sign-in form: same style, same `type="submit"`, same "Sign in" label. The step "Verify the Sign in button is visible" passed anyway. The platform's visual diff showed the change (2.20% → 3.19% as I strengthened the decoy) but never flagged it as ambiguity — from the outside, the assertion resolved to the first matching "Sign in" on the page.

This is failure mode 4 — the blind first-match — and it's the most dangerous kind of miss: an ambiguity was present — the kind a human would flag in seconds — yet the platform reported green.

> A red build forces a decision; a green report from a black box does not.

## The measure is the same for all four

You don't learn trust from demos. You learn it from injections — fault injection for the miss, review gates for the hallucination rate, diff review for every heal, decoy targets for the blind first-match. Each mode needs its own probe; one green run never validates the other three. Two cells still matter as baselines: **TP** is a real bug correctly reported — injected faults are just the controlled way to measure how often that happens. **TN** — run the agent against clean code and count false alarms; high noise makes real signals easier to miss.

## What to do Monday

1. **Review a sample of agent findings against source before trusting the report** — confirmation rate, not raw count.
2. **Seed known defects (mutation testing)** — measure FN, not just TP.
3. **Run the agent against clean code** — baseline your FP.
4. **Diff every healer change** — if the fix only silences the signal, it lies.
5. **Track confirmation rate over time** — a rising false-discovery rate is the first sign of drift.

The agent that finds 5 bugs and gets 1 right is still worth running — once you know the ratio, and once the 4 ghosts can't reach your backlog. Your agent will tell you what it found. Your probes tell you which of the four failure modes it has.

Do you track confirmation rate for agent-reported bugs — or just count how many it found?

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #ZeroBudgetQA #GenAITesting #MutationTesting