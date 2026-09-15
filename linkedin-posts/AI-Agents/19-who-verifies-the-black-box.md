**Format:** Pulse Article
**Series:** AI Engineering
**Cover:** 19-cover-blackbox.png ✅
**Feed Image:** 19-blackbox-loop.png ✅
**Hook:** «Не коммить то, что не понимаешь» vs «понимать код - навык, который тянет назад». Оба правы. Ответ QA - поведение, а не строки.
**Based on:** Pavel Shcherbinin (CTO Yandex) vs Zabrodin дискуссия, TG ~Jul 2026 (`raw/shcherbinin-tg-understand-code-debate-2026.md`); DevAssure O2 (Session 87); 34/34 mutations; Meta ACH (arXiv 2501.12862); Denys Chaban echo chamber (Virto, Sasha Siniouguine post thread)
**Wiki:** ai-qa-wiki/wiki/shcherbinin-tg-understand-code-debate-2026.md

---

<!-- COVER: 19-cover-blackbox.png — black box with agents inside, verification outside -->

# Who Verifies the Black Box?

Two CTOs are arguing in my feed. One says: *never commit code you don't understand.* The other: *understanding code line by line is a skill that holds you back when agents write 80% of it.*

Both are right. Both are wrong. And the resolution is not philosophical - it is a QA design decision.

## The black box is here to stay

Agents write **7x more code** (MIT/Wharton). GitLab: **78%** code faster, **79%** say delivery didn't speed up. Nobody is going back to hand-written code - not even the CTO who said "don't commit what you don't understand."

The uncomfortable part: he is also right. AI code is dangerous because it is **plausible**. It compiles, it runs, it produces output - the logic error sits three commits deep, and the diff review that should catch it is now a rubber stamp for 10x more PRs.

So the real question is not "should we understand everything?" It is: **when understanding is impossible, what is the control?**

## The QA answer: behavior, not lines

Tests do not require understanding every line. They require understanding **behavior** - and then verifying the black box from the outside, the way you verify any closed system:

1. **Behavioral specs, not implementation specs.** The spec says what must happen, not how. A bad spec produces wrong code faster - precise specs are the new code.
2. **Verification independent of the generator.** The same agent that wrote the code must not be the only one checking it. One agent finds, another repairs - or a human gate with evidence.
3. **Tests that can still fail on purpose.** In my Playwright suite, **34/34 injected faults were caught** - 0 survivors. A surviving mutant means the test asserts a string, not behavior. That is the anti-overfit guardrail: the test's job is to be *able* to catch a lie, not just to pass.

## The echo chamber warning

An engineer on a CEO's post put it better than I can: if a flawed assumption enters the shared context, the entire autonomous cycle will seamlessly build, test, and merge that error with perfect internal consistency. The agents create a **high-velocity echo chamber** - code, tests, and review all generated from the same wrong premise, all passing.

Our DevAssure O2 run was a miniature version: the agent caught a real injected bug - and also produced 5 findings, most of them artifacts of its own actions. Same generator, same blind spot, both directions.

That is why the control must be outside the loop: mutation testing, contract tests, golden datasets, a human gate that demands evidence. Verification wins only when it does not share the generator's assumptions.

## What this means for QA leaders

The "understanding" debate is a trap. Nobody can understand 7x code. What you can do is build the layer that makes understanding unnecessary: behavior-based tests, independent review, and faults that still kill the suite.

Sasha Siniouguine (CEO, Virto Commerce) said it exactly: *"I feel more like a QA engineer than a developer these days - I spend more time reading specs and reviewing what got generated than typing code."* The black box is not the problem. The missing verification layer is.

Which is your control when the code is a black box - the diff review that stopped scaling, or tests that can fail on purpose? If it's the first, the second is where the value moved. I wrote up the full pattern in The AI Productivity Paradox Is a QA Problem [Pulse-URL статьи 16 - вставить при публикации].

And because the verification layer itself can lie, I measured the trust problem from both sides in [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/) - the four failure modes of an agent's report and how to probe each one.

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #ZeroBudgetQA #GenAITesting #Verification