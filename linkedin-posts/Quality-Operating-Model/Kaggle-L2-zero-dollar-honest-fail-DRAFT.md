**Format:** LinkedIn Pulse Article (short note — 1 idea + 1 case + 1 number)
**Series:** Quality Operating Model (slot TBD — slate #1)
**Status:** draft v1.1 (W4, 05.10 — W3 sign-off applied: bench 8.08/8.69 + AUROC, sensitivity 11.72/0.5000 robust, LoRA 7.93M/1.6%, pins in notes; assembled from W3 run facts + W2 plain-words/parked/terms 5599720)
**Cover:** TODO (proposal: "$0" receipt vs GPU chip — free hardware, honest result, dark + amber)
**Feed Image:** cover doubles as feed preview
**Hook:** Zero dollars, eleven minutes, best loss 6.9470 — and we parked the track. Free hardware, honest failure.
**Links:** first comment (repo/protocol links TBD at publish)

---

# $0, 11 Minutes, 6.9470: Tuning on Free GPUs and Parking It Honestly

Zero dollars. Eleven minutes of wall time. Best eval loss 6.9470 — and we parked the track instead of shipping a story. This note is about free hardware, an honest negative result, and why the combination is rarer than either part alone.

Three reasons the work lived on Kaggle, plainly. First, free GPUs: two T4s at zero cost, thirty hours a week of quota, about two and a half spent across the day's sessions. The same tune locally would have eaten hours of CPU for a 340M model over three epochs; on Kaggle it took six hundred fifty-four seconds at three to six samples a second. Second, privacy: a private kernel plus a private dataset, locked data never exposed, terms closed — shared infrastructure that sees nothing it shouldn't. Third, reproducibility: everything pinned, then saved under versions, so the weights survive the session instead of burning with it. A lesson previously learned the hard way.

What got done: two thousand of nine thousand steps, evaluation every five hundred (forty-two batches, seconds each), early stop with patience three, best eval loss 6.9470 at step five hundred. The bundle came home whole — a thirty-two megabyte adapter (seven-point-nine million trainable parameters, one-point-six percent) plus configs, saves stepping from running to stable to final, kernel log pulled locally. SHAs matched both directions, Kaggle to local and back.

Then the bench, on the same T4s: four hundred ninety-five elements, fourteen hundred queries, two hands, minutes of compute. Base 8.08% vs best 8.69% — plus zero-point-six points on three elements, AUROC 0.5295 to 0.5302: noise in both directions. A sensitivity check on final (11.72%, AUROC exactly 0.5000) confirmed the fail is robust, not marginal. A tuned 340M changed nothing measurable on the locked test. So the track is parked explicitly, not failed forward: the question stays open for fine-tune stories with locked tests, the answer on this one is closed.

The terms framing matters more than the numbers. A public dataset under eval terms went into a private kernel with a private dataset and private weights; only aggregates with citation come out. That is the whole privacy story in one sentence, and it held.

No new tune is planned — everything scheduled is done. The platform and the protocol stand ready for the next training run: any model, same pins, same privacy, same saves. Free-tier limits — GPU quotas, session ephemerality — are known quantities now, handled by discipline rather than discovered by accident.

And the story travels: free hardware plus an honest negative result, told to a vendor as peer exchange rather than a pitch. Negative results nobody publishes are how everyone pays for the same lesson twice.

Don't copy our 6.9470 — one tune is depth, not breadth. Copy the habits instead: pin everything, save versions, bench on locked tests, and park explicitly when the answer is no. Same rule as everywhere in this series: machines count, humans decide.

**When did you last publish a negative result — and what did it save someone else?**

Victor Ematin · AI Quality Engineering Lead · Independent practice

#MutationTesting #QAAutomation #Playwright #AIQA #SoftwareTesting

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

### Source
- W3 run facts 02.10 (hardware/tune/bundle/bench/result — "все цифры мои, из логов")
- W2 5599720: plain-words + parked-рационал + terms-фрейминг (вставлены почти дословно, перевод W4)

### Facts (W3, из логов)
- Kaggle T4x2 free, квота 30ч/нед, потрачено ~2.5ч; 2000/9447 степов, 654с стенки, 3.5–6.1 samples/s; eval каждые 500 (42 батча, ~6с); early stop patience-3
- Bundle: адаптер 31.77MB + конфиги; сейвы training-running → s1web-stability-lora → s1web-stability-final; kernel log локально
- Bench: eval-kernel (тот же T4), 495 els / 1444 qids × 2 руки, минуты счета
- Итог: $0, best eval_loss 6.9470@500, bench base 8.08% / best 8.69% (Δ+0.6pp, 3 els), AUROC 0.5295/0.5302 → FAIL; sensitivity final 11.72% / AUROC 0.5000 (FAIL robust); track parked. Pins: base 7ee5da4c… / best 1899e036… / locked ea675b59… (W3 sign-off 05.10, бит-в-бит).
- W2: локально те же 6300×3 были бы часами; 340M; SHA сошлись обеими руками

### Open
- Slot: TBD (slate #1; предложить после слотов RMT-notes + 31)
- Cover: proposal in metadata — Gemini EN-spec → fact-check
- Feed post text + first comment: TODO (after text lock)
- Reviews: W3 numbers confirm (его цифры — быстрый signe-off?) → W1 fact-check → R1 (user)
