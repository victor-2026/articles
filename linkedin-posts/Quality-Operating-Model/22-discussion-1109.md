**Format:** LinkedIn Discussion Post
**Series:** Quality Operating Model
**Date:** Fri 11.09 10:00 UK
**Purpose:** Follow-up discussion after Article 22 (published Mon 07.09) - engagement on the 10-second test
**Cover:** none (regular feed post, not Pulse — no cover, no carousel)
**Feed Image:** 22-discussion-Gemini_new.jpeg (1376x768) — Gemini-реген checklist-карточки (Detect Defects нативно, опечаток нет)

---

**Your architecture changed. Your ownership didn't.**

The argument: the components are green. The business flow is broken.

Why? Because nobody owns the seam — the contract between two teams, the event that has to arrive on time, the failure mode when the vendor is slow.

**Can you name the owner of the seam in under ten seconds?**

If the answer takes longer than ten seconds, the defect is already scheduled. It just hasn't shipped yet.

My example: every token refresh under parallel workers must be serialized — the loser retries, never overwrites. One line, checkable, owned.

Two more from recent reviews:
— Who owns duplicate charges when the user double-clicks Pay? Every order carries an idempotency key; duplicates are rejected, never re-charged.
— Who owns the event contract when Team A ships v2? Every event carries a schema version; consumers reject unknown versions loudly, never silently.

**Which seam in your system would fail the 10-second test?**

Drop it below 👇 — I'll pick 3 and dissect them soon.

P.S. Checklist attached. "Who Owns Quality at the Boundaries?" → first comment.

Victor Ematin · AI Quality Engineering Lead · Independent practice

#QualityEngineering #ConwaysLaw #TestAutomation #QAStrategy #IntegrationTesting
