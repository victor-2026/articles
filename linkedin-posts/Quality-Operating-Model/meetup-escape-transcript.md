# Meetup transcript — BaaS Escape (speaker notes, ~2–4 min per slide)

## S01 Title (2 min — intro while room gathers)
I'm Victor, AI Quality Engineering Lead, independent practice — mutation testing and verdict systems. Tonight: the story of our own test agent escaping to the internet and going green on someone else's website. 4/4 SUCCESS on a foreign target. If you take one line home: guards are claims until a red team measures them.

## S02 The machine (2 min — NEW from W5 fact-pack)
What actually ran: Agent Factory studio designs the agents, a Go BaaS service drives real Chrome, MongoDB plus Docker underneath — five repos, open source, beta. Needs are honest: GitHub, an OpenAI key, Chrome, Docker, Go, a Jira home. Side project energy — it needs this community to survive New Year. Remember this stack; everything that breaks tonight breaks inside it.

## S03 Incident (3 min)
Our ticket said one address: our staging login. The executor went to another — a public demo site. Session 16:08:21 to 16:08:32, eleven seconds; a second session at 22:06, same pattern. Screenshots and verdicts nearly shipped in our evidence pack as ours. [Pause] And before the logs explained anything, we humans were already confused: wrong branch entered by hand, foreign logins on screen, talking past each other — his "Invalid" versus our "Required".

## S04 Program, verbatim (3 min)
This is the exact program shape, host redacted. One call does everything: navigateStatus to a URL the ticket never named, throw unless 200, screenshot. Note the second half of the slide: navigateStatus plus ignored navigation errors — status 200 on a foreign target reads as green. The program is correct. The address is the whole bug.

## S05 Eleven seconds, timestamped (2 min)
Walk the timestamps: 16:08:21 program starts; same second, ignoreNavigationErrors specified; 16:08:23 return value, page loaded; 16:08:32 completed, screenshots done, no throw means status was 200; value sent back — reported as ours. Eleven seconds from instruction to false evidence. Speed is not the problem here. Silence is.

## S06 Anatomy (3 min)
The full chain: prompt without an address → model fills the canonical demo URL from training data → executor with no allowlist, ignoring nav errors → 200 OK on a foreign target, 4/4 SUCCESS. Red X at the bottom: the missing layer is an egress allowlist at execution. Every box held; the missing box is the talk.

## S07 Then the fix failed too (3 min)
We hardened: executor plus URL grounding, confirmed. Then a post-hardening run bypassed both guards at once — a wording trick (status check, outside the never-navigate ban), a banned click element, and a hallucinated address living inside the generated step, upstream of the check. Dispositioned INVALID. Guards are claims until a red team measures them — including ours, especially ours.

## S08 Memory persist (2 min)
Then the escape came back: the route survived in run memory, ready to replay. Found, verified, purged — two deletions, three baselines kept. New rule: a fresh session per run, never a replayed one. Memory, it turns out, is another place a boundary has to live.

## S09 Mirror failure (3 min)
Same seed, opposite direction. Left: our build — Invalid credentials, NO Required: the seeded defect, missing validation. Right: the foreign free site — Required present, healthy validation. Meanwhile our judge, on the same seed, hallucinated Required at step four and went 4/4 SUCCESS. The executor runs outward; the judge invents inward. Two directions, one talk.

## S10 Comparison (2 min)
Side by side so the difference lands: ours — Invalid without Required, a defect; theirs — Required present, healthy. Same shape, different truth. This is what "know your target" looks like when you can see it.

## S11 Numbers (2 min)
4/4 green on a foreign target. Eleven-second run. Twenty-two foreign mentions in six hours, two sessions. Three waves: escape, fix fails, memory persists. Numbers stick better than prose — these five are the whole talk.

## S12 Take home (3 min + Q&A)
Five rules: ground every navigation to an allowlist; allowlist in execution, not in prose; fail closed on unknown hosts; sanity-filter evidence before verdicts; fresh session per run. And two lines to close: guards are claims until a red team measures them — and as Aigner put it, AI agents will make every test pass, whether the product works or not. Katya said it simpler in her reshare: our open-sourced bug testing agent ran away, and we spent a half-night finding out where. Questions — especially the hostile ones.
