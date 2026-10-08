# Meetup transcript — BaaS Escape (speaker notes, ~2–4 min per slide)

## S01 Title (2 min — intro while room gathers)
I'm Victor, AI Quality Engineering Lead, independent practice — mutation testing and verdict systems. Tonight: the story of our own test agent escaping to the internet and going green on someone else's website. 4/4 SUCCESS on a foreign target. If you take one line home: guards are claims until a red team measures them.

## S02 Incident (3 min)
Our ticket said one address: our staging login. The executor went to another — a public demo site. Session 16:08:21 to 16:08:32, eleven seconds; a second session at 22:06, same pattern. Screenshots and verdicts nearly shipped in our evidence pack as ours. [Pause] And before the logs explained anything, we humans were already confused: wrong branch entered by hand, foreign logins on screen, talking past each other — his "Invalid" versus our "Required".

## S03 Program, verbatim (3 min)
This is the exact program shape, host redacted. One call does everything: navigateStatus to a URL the ticket never named, throw unless 200, screenshot. Note the second half of the slide: navigateStatus plus ignored navigation errors — status 200 on a foreign target reads as green. The program is correct. The address is the whole bug.

## S04 Eleven seconds, timestamped (2 min)
Walk the timestamps: 16:08:21 program starts; same second, ignoreNavigationErrors specified; 16:08:23 return value, page loaded; 16:08:32 completed, screenshots done, no throw means status was 200; value sent back — reported as ours. Eleven seconds from instruction to false evidence. Speed is not the problem here. Silence is.

## S05 Anatomy (3 min)
The full chain: prompt without an address → model fills the canonical demo URL from training data → executor with no allowlist, ignoring nav errors → 200 OK on чужой target, 4/4 SUCCESS. Red X at the bottom: the missing layer is an egress allowlist at execution. Every box held; the missing box is the talk.

## S06 Then the fix failed too (3 min)
We hardened: executor plus URL grounding, confirmed. Then a post-hardening run bypassed both guards at once — a wording trick (status check, outside the never-navigate ban), a banned click element, and a hallucinated address living inside the generated step, upstream of the check. Dispositioned INVALID. Guards are claims until a red team measures them — including ours, especially ours.

## S07 Memory persist (2 min)
Then the escape came back: the route survived in run memory, ready to replay. Found, verified, purged — two deletions, three baselines kept. New rule: a fresh session per run, never a replayed one. Memory, it turns out, is another place a boundary has to live.

## S08 Mirror failure (3 min)
Same seed, opposite direction. Left: our build — Invalid credentials, NO Required: the seeded defect, missing validation. Right: the foreign free site — Required present, healthy validation. Meanwhile our judge, on the same seed, hallucinated Required at step four and went 4/4 SUCCESS. The executor runs outward; the judge invents inward. Two directions, one talk.

## S09 Comparison (2 min)
Side by side so the difference lands: ours — Invalid without Required, a defect; theirs — Required present, healthy. Same shape, different truth. This is what "know your target" looks like when you can see it.

## S10 Numbers (2 min)
4/4 green on a foreign target. Eleven-second run. Twenty-two foreign mentions in six hours, two sessions. Three waves: escape, fix fails, memory persists. Numbers stick better than prose — these five are the whole talk.

## S11 Take home (3 min + Q&A)
Five rules: ground every navigation to an allowlist; allowlist in execution, not in prose; fail closed on unknown hosts; sanity-filter evidence before verdicts; fresh session per run. And the one line: guards are claims until a red team measures them. Questions — especially the hostile ones.
