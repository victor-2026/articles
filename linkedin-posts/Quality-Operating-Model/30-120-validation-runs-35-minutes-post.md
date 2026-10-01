**120 validation runs in 35 minutes — and our first probe was wrong.**

The scariest false PASS in the campaign came from our own measuring instrument. Probe v1 detected that *some* validation occurred. It did not prove the deliberately broken field was validated. It could have certified a fix that fixed nothing.

Probe v2 made the verdict field-specific: the username break on **Username** only, the password break on **Password** and **Confirm Password**.

We also ran an automated Jev verdict hook: 358ms on average. Useful — but not the speed story. A ~45× faster verdict step touched only a single-digit share of total time. Rebuilds were the real bottleneck.

Full method + numbers in the article below👇

**When did your own probe last lie to you?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting
