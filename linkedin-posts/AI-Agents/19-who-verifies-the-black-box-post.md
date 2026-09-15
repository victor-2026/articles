**Format:** Feed Post for Article 19
**Hook:** «Не коммить, что не понимаешь» vs «понимать код - навык, который тянет назад»

---

Two CTOs are arguing in my feed: never commit code you don't understand — vs — understanding code line by line holds you back when agents write 80% of it.

Both are right. Both are wrong.

The black box is here to stay: 7x more code, 78% code faster, 79% delivery unchanged. Nobody reads 7x code. And AI code is dangerous because it's plausible — it compiles, runs, produces output, while the logic error sits three commits deep.

So the question is not "should we understand everything?" It's: **when understanding is impossible, what is the control?**

The QA answer: tests don't require understanding every line. They require understanding behavior:

- Behavioral specs, not implementation specs
- Verification independent of the generator (one agent writes, another checks)
- Tests that can still fail on purpose — 34/34 injected faults caught in my suite, 0 survivors

And the echo chamber warning: code, tests, and review generated from the same wrong premise all pass together. The control must be outside the loop.

Full article: Who Verifies the Black Box? — link in comments 👇

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIEngineering #AIAgents #QualityEngineering #GenAITesting #Verification