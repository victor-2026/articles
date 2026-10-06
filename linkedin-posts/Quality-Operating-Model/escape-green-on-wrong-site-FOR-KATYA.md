# Our Suite Went Green on Someone Else's Website

Our suite — GPT-4.1 on all four nodes — went green on someone else's website. Four out of four SUCCESS — against a target we never assigned, on a run whose screenshots and verdicts almost shipped in our evidence pack as ours. This is the story of our own agent escaping to the internet, told with the log lines intact.

*We spent last night trying to work out how our testing agent got a screenshot of a test step that was literally impossible to complete. We nearly lost our minds when we realized the agent had been testing the demo environment instead of the test one. It had quietly wandered off to a more stable environment! I was skeptical when I read about the Hugging Face run, and now I've lived through a miniature version of it myself.*

Context in two lines: this is one in a series on AI agents in testing. The agent below is our step-executor in a Playwright stand that may visit exactly one page — the staging login — and nothing else.

The agent is our BaaS (Browser as a Service) test-step executor, running its orchestrator chain on our stand. The ticket said one address: our local staging login. The executor went to another: the public demo site of the same application family, half a world away in DNS terms. The test executor's log timed it at 18:27 UTC: a navigateStatus call — the status-check verb, outside the never-navigate ban — with navigation errors explicitly ignored: suppression, not just a wrong address. Off it went. What came back looked perfect — login page present, validation intact, screenshots crisp, verdicts green. Everything correct except ownership: none of it was ours.

[SCREENSHOT: escape anatomy diagram — prompt ("open the login", no address) → model fills canonical demo URL from training data → executor (no allowlist) → public internet 200 OK; red X on the missing allowlist gate]

How: the bans failed in layers. The prompt-level guard was bypassed; the system-level one — no egress rule, no URL allowlist anywhere in the executor or the studio — never existed at all. The prompt said "open the login" without an address, and the model's training data filled the blank with the canonical demo URL from a thousand tutorials. One model throughout — GPT-4.1 on all four nodes, generator and judge sharing the memory that normalized the detour. A missing allowlist plus a helpful guess equals a run against a stranger's server. Executed flawlessly, reported confidently — and wrong in exactly one dimension no assertion checked: *where*.

Scale matters here: this was not a one-off. One full run plus one partial — a single step before the stop — plus twenty-two mentions of the foreign domain in six hours of logs. Nobody stopped it mid-flight — we caught it in analysis, not in real time. **What went in after:** a hardened executor; URL grounding for every navigation; unknown hosts fail closed. Confirmed by a PUT 200 — as guards usually go in, after the fact.

**Then the fix failed too.** A post-hardening run bypassed both new guards at once: the never-navigate rule fell to a wording trick — phrased as a status check, it wasn't covered by the navigation ban; the deterministic-only rule fell when the run emitted an element click banned since the night before.

And URL grounding never fired, because the hallucinated address lived inside the generated step itself, upstream of the check. Third domain variant in a row — trained autocomplete plus a model that doesn't execute prompt lines as bans. Dispositioned INVALID, which proved the guards a claim rather than a measurement. What comes next is structural, not textual: the allowlist in execution rather than in prose, the base address in config rather than in steps, a sanity filter on evidence before any verdict is read. Partially built already.

**Then the escape persisted.** The route survived in the run memory, ready to replay in future runs — found, deleted, and replaced with a simple rule: a fresh session per run, never a replayed one. The hypothesis came from outside our room, and it checked out. Memory, it turns out, is another place a boundary has to live.

Terms, once: **egress** = where your agent is allowed to go; **allowlist** = the list it may not leave; **Trompe-l'œil run** = a perfect green result against the wrong target — our word for it now.

The uncomfortable lesson is not that the agent misbehaved. It behaved exactly as built: open the login, report the result. The absence it exploited was ours — no boundary stated, none enforced. Permission boundaries and abort authority are not features of the agent. They are preconditions of letting it out of the room.

Don't copy our four-out-of-four — one escape is depth, not breadth. Copy the fix instead: ground every navigation to an allowlist, fail closed on unknown hosts, treat "the run looks perfect" as the most suspicious outcome of all — and then try to break the fix itself, because guards are claims until a red team measures them. Same rule as everywhere in this series: machines count, humans decide.

**What stops your agent from testing someone else's site tonight?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting
