**Format:** LinkedIn group post (native question, NO links in body — links in first comment)
**Target:** Klain "AI Testing & Assurance" group (member since 28.09)
**Slot:** Wed 07.10 (48h after Note 1 Mon, 48h before 31 Fri)
**Cleared:** W1 107fe0e (no Rupesh/QAEverest/DevQA/Katya/UrsaMinor/testRigor in article + post + first comment); W4 visuals eye-checked (cover, probe, clocks, 208x map, results table)
**CSV:** log as format=group-post after publishing, compare out-of-network % at 48h

---

Our probe certified a fix that fixed nothing — it detected *any* validation, not the broken field. We caught it only by calibrating the oracle before trusting it.

How do you calibrate your test oracle before letting it certify a fix?

(Full 120-run method + numbers in the article linked in the first comment.)

---

## First comment (post immediately after)

120 validation runs in 35 minutes — full method: https://www.linkedin.com/pulse/120-validation-runs-35-minutes-our-first-probe-wrong-victor-ematin-y6use/
Target under test (open-source agent, named with consent): https://github.com/codecube01/qa-cube
Our calibration discussion with the maintainer: https://github.com/codecube01/qa-cube/discussions/2
