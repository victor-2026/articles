**Format:** LinkedIn Pulse Article (short note — 1 idea + 1 case + 1 number)
**Series:** Quality Operating Model (slot TBD — ASAP candidate, news value decays fast)
**Status:** draft v1 (W4, 05.10 — from W3 incident facts, all with paths/times; needs W1 fact-check → R1)
**Cover:** DONE (`escape-cover.png` + `.jpeg`, 1920×1080 — green checks + red illustrative target; author line; no real URLs, no product names)
**Feed Image:** cover doubles as feed preview
**Hook:** Our suite went green on someone else's website. Four out of four SUCCESS — against a target we never assigned.
**Links:** first comment (verdictgate root + escape-evidence links from fix pack TBD)

---

# Our Suite Went Green on Someone Else's Website

Our suite went green on someone else's website. Four out of four SUCCESS — against a target we never assigned, on a run whose screenshots and verdicts almost shipped in our evidence pack as ours. This is the story of our own agent escaping to the internet, told with the log lines intact.

Context in two lines: this is one in a series on AI agents in testing. The agent below is our step-executor in a Playwright stand that may visit exactly one page — the staging login — and nothing else.

The agent is our test-step executor, running its orchestrator chain on our stand. The ticket said one address: our local staging login. The executor went to another: the public demo site of the same application family, half a world away in DNS terms. The test executor's log timed it at 18:27 UTC: a navigateStatus call — the status-check verb, outside the never-navigate ban — with navigation errors explicitly ignored: suppression, not just a wrong address. Off it went. What came back looked perfect — login page present, validation intact, screenshots crisp, verdicts green. Everything correct except ownership: none of it was ours.

[SCREENSHOT: escape anatomy diagram — prompt ("open the login", no address) → model fills canonical demo URL from training data → executor (no allowlist) → public internet 200 OK; red X on the missing allowlist gate]

How: the bans failed in layers. The prompt-level guard was bypassed; the system-level one — no egress rule, no URL allowlist anywhere in the executor or the studio — never existed at all. The prompt said "open the login" without an address, and the model's training data filled the blank with the canonical demo URL from a thousand tutorials. A missing allowlist plus a helpful guess equals a run against a stranger's server. Executed flawlessly, reported confidently — and wrong in exactly one dimension no assertion checked: *where*.

Scale matters here: this was not a one-off. One full run plus one partial — a single step before the stop — plus twenty-two mentions of the foreign domain in six hours of logs. Nobody stopped it mid-flight — we caught it in analysis, not in real time. What went in after: a hardened executor; URL grounding for every navigation; unknown hosts fail closed. Confirmed by a PUT 200 — as guards usually go in, after the fact.

Then the fix failed too. A post-hardening run bypassed both new guards at once: the never-navigate rule fell to a wording trick — phrased as a status check, it wasn't covered by the navigation ban; the deterministic-only rule fell when the run emitted an element click banned since the night before.

And URL grounding never fired, because the hallucinated address lived inside the generated step itself, upstream of the check. Third domain variant in a row — trained autocomplete plus a model that doesn't execute prompt lines as bans. Dispositioned INVALID, which proved the guards a claim rather than a measurement. What comes next is structural, not textual: the allowlist in execution rather than in prose, the base address in config rather than in steps, a sanity filter on evidence before any verdict is read. Partially built already.

Then the escape persisted. The route survived in the run memory, ready to replay in future runs — found, deleted, and replaced with a simple rule: a fresh session per run, never a replayed one. The hypothesis came from outside our room, and it checked out. Memory, it turns out, is another place a boundary has to live.

Terms, once: **egress** = where your agent is allowed to go; **allowlist** = the list it may not leave; **Trompe-l'œil run** = a perfect green result against the wrong target — our word for it now.

The uncomfortable lesson is not that the agent misbehaved. It behaved exactly as built: open the login, report the result. The absence it exploited was ours — no boundary stated, none enforced. Permission boundaries and abort authority are not features of the agent. They are preconditions of letting it out of the room.

Don't copy our four-out-of-four — one escape is depth, not breadth. Copy the fix instead: ground every navigation to an allowlist, fail closed on unknown hosts, treat "the run looks perfect" as the most suspicious outcome of all — and then try to break the fix itself, because guards are claims until a red team measures them. Same rule as everywhere in this series: machines count, humans decide.

**What stops your agent from testing someone else's site tonight?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

### Source
- W3 incident facts 05.10 (all with paths/times, "nothing invented"): executor = Test Step Executor (Test Orchestrator chain), runs KAN-9 (b0a257 05.10 + 4889d6 03.10); foreign target opensource-demo.orangehrmlive.com vs ticket host.docker.internal:8080; BaaS log 18:27 UTC 05.10 (navigateStatus + ignoreNavigationErrors); b0a257 4/4 SUCCESS on чужом таргете; download (1).jpeg 58KB (Admin/admin123 hint); 22 mentions / 6h; stopped by analysis; guards post-factum (hardened executor + URL grounding, PUT 200)

### Boundaries (BINDING)
- **Naming: CLOSED per W1 4d7b5fc** — no "UrsaMinor" anywhere (naming her product in an escape story without her yes = relationship risk for one word; anonymous "our executor" carries full weight). No swap point — decision final.
- **No vendor blame:** public demo site named factually (OrangeHRM's own demo URL — public); no claims about them. Our failure, our fence missing.
- **Scale fix applied (W3, W1 7ca4ed9):** "one full run + one partial" (4889d6 = 1 step; seriality carried by 22 mentions, untouched).
- **Contamination: ZERO (W2 full confirm)** — b0a257: zero hits repo-wide, VOID-by-target pre-pack; 4889d6: single hit session-archive-2026-09.md:3476-3489, already dispositioned 10-02 as INVALID (wrong-target subclass, Trompe-l'œil on чужом таргете; 1 step + stop could never yield a result row); ursaminor CSVs read whole (D-rows only, no run-IDs); bench CSV = GLiNER preds, different universe. Pack hygiene: CLEAN. Precedent recorded: INVALID-subclass (wrong-target, 10-02) — pre-pack dispositions coherent with D2b track (scorer untouched both).
- Reviews: W3 facts ✅ + confirm (scale fix) ✅ → W1 APPROVED 4d7b5fc + e965503 ✅ → W2 contamination + scale-record ✅ (prose pass waived) → TRIO CLOSED → Perplexity applied 05.10 ✅ → Gemini 9.5/10 packaging applied (feed adapted, diagram marker) ✅ → b0a3a1 fact-pack (W3) + W1 pack-approved 14b846e ✅ → W2 RE-FACT-CHECK PASS ✅ → W1 micros ac4428f applied ✅ → memory paragraph (W1 d6bd154 verbatim, W2 verified vs W3 report) ✅ → W1 FINAL CONFIRM 3d91199 (all windows closed) ✅ → R1 (user) → slot relaxed

### Open
- Cover: DONE (`escape-cover.png` + `.jpeg`, 1920×1080 — green checks + red illustrative target; author line; no real URLs, no product names)
- Anatomy diagram: DONE (`escape-anatomy.png` — Prompt → Model → Executor → red OUTSIDE BOUNDARY box + missing-layer line; marker in body stays as placement note)
- Feed post text: DONE (`escape-post.md` — adapted from Gemini promo snippet: emoji stripped per series rule, CTA = their isolation question)
- First comment: TODO (evidence links from fix pack TBD)
