# VerdictGate launch video V1 — 60-90s narrated terminal demo

Status: V1 RENDERED (verify content vs script below) → deployment: SEPARATE TRIAL POST, decoupled from 23.09 launch 19.09 (LI axiom: article feed = cover only). Voice: Daniel (en_GB). Style: dark #0d1117 + amber (article palette). Format: 1920×1080 mp4 (LinkedIn native video).

## Narration (~150 words, ~60s)

1. "Your vendor says: one hundred percent confidence, zero percent risk. [pause] The suite is green."
2. "We break two payments on purpose, and record what the suite does."
3. "One command. VerdictGate reads the recording — it never runs your code."
4. "B-zero: FAIL. One survivor. Payment submits successfully — and nobody caught it."
5. "That row has a name, an operator, and an empty decision field. Fix this first."
6. "Same CSV, same scorer version — byte-identical verdict. Attach it to the release."
7. "Green report? Or safe release? Now you can tell the difference."

## Shot list (terminal, typed live)

1. `$ cat results.csv` (3 rows visible) → 2. `$ python3 verdictgate.py results.csv` → 3. verdict table output scroll (B0 FAIL red) → 4. freeze on "Fix first" block (amber highlight) → 5. end card: repo URL + "v0.2.2 · 3 reviews · 0 P0".

## Build (all local, $0)

asciinema rec (scripted run on examples/payment-critical-fail) → PIL frames 1920×1080 dark/amber → ffmpeg mp4 + say Daniel narration mux. No stock footage, no talking head — terminal IS the visual (matches article aesthetic).

## Open
- Approve script wording (above) → render.
- End-card URL needs PUBLIC repo (gating: Fri 19.09).
- Optional V2 later: faceless explainer in the style of the C# series (script + stock/code visuals) — bigger lift, post-launch.

## RU dub v1 (rendered, pending tune — NOT now)
- File: /tmp/vg-video/verdictgate-launch-v1-ru.mp4 (35s, Milena). Verdict: ok with tweaks.
- TODO later: word-level script polish + slightly slower pace (longer holds).
