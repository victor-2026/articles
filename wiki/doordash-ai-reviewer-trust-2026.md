# DoorDash AI Reviewer Engineers Trust (May 2026, via Nielsen Sep 2026)

**Source:** [DoorDash eng blog](https://careersatdoordash.com/blog/doordash-built-an-ai-code-reviewer-engineers-actually-listen-to/) (Adam Yarger / Adam Rogal, 11.05.2026; fetched via Wayback — direct 403) via [Daniel Nielsen post](https://www.linkedin.com/) 12.09
**Digest:** ручной заход 12.09

## Numbers (production, not demo)

- 10,000+ PRs/week, 56 repos (Go, iOS, Android, web, infra, data). Auto-fires on PR open, ~7 min after open, usually before first human look.
- **60.2% acceptance on settled high/critical** (n=2,256), up from 46% with previous third-party agent. Webhook-triggered (non-cherry-picked): 59.0%.
- **~$3/review** (vs $5–20 public pricing for deep agentic review). Tunable: cheap models for simple steps, strong for verification-heavy, skip low-risk PRs.
- Metric that matters: *"Do engineers actually change their code?"* + *"Do teams keep it enabled?"* Trust = acceptance + retention.

## Architecture: v1 → v2 → v3

- **v1 specialists** (security/tests/perf/quality checklists): caught mechanical bugs, **missed architectural issues** (contract changed quietly, abstraction mismatch, 3-repos-away deletion). Nobody looked at the big picture.
- **v2 generalists** (whole change, parallel): caught cross-boundary issues but attention spread thin — real findings lost. *"Leaving critical issues on the table not because reviewers couldn't catch them, but because the system had not decided what deserved deep investigation."*
- **v3: lead scout + deep reviewers.** Scout notices but doesn't verify ("this deletion looks suspicious", "enum unhandled in sibling") → reviewers dig in, verify or drop. **Splitting noticing from verifying** = the change that mattered. Mirrors senior-engineer behavior (hunch → dig).

## Design principles

- **Precision over recall + disprove-it pass.** Every finding must survive explicit falsification before posting. *"We'd rather miss some issues than become noise. A reviewer that's muted catches nothing."*
- **Focused context (review profiles).** AGENTS.md is written for authoring, not reviewing → mined per-domain profiles from 4 sources (AGENTS.md review-relevant subset, historical senior PR comments, Slack decisions/post-mortems, incident history). Evidence filter: no concrete file-and-line → dropped. Routing: PSP PR loads PSP+payments+monetary rules, nothing else.
- **Good at (systematically hard for humans):** deletions (*"who depended on this?"*), **cross-boundary drift** (one side updated, siblings not — invisible in CI, each side compiles), silent behavior changes (signature same, semantics shifted).
- **Cost per successful review**, not token price (weak models retry invalid JSON; strong nails it first try).
- **Stuck-loop protection:** turn counter ≠ progress detector → soft timeout (return verified-only) + hard kill.
- **Reporting guardrails:** prevent **false-clean reviews**, reconcile stale findings, collapse outdated comments on re-review.
- **Fixer loop:** tag agent in PR thread → fix in isolated worktree with reviewer context carried over → normal PR commit (CI + human review still apply).

## Evals as development loop

- Acceptance = production signal (lagging). Day-to-day: **small eval set from real misses + incidents** (not synthetic puzzles) — PRs where a strong reviewer should have caught it.
- Eval set tests prompts/retrieval/models/profiles pre-production. Building **continuous eval harness**: every change measured against growing corpus of past incidents, *"provably gets better over time, not hoped"*.

## Why it matters for us

1. **Disprove-it pass = falsification gate.** Our mutation matrix falsifies the TOOL's claims; their scout-reviewer falsifies its OWN findings pre-post. Same epistemics, mirrored direction. Candidate shared principle for framework: no claim posts without surviving its negation.
2. **Cross-boundary drift = decoy/seam language from review side.** "One side updated, siblings not" is Article 22's seam defect + Article 26's decoy blindness, found independently. Third convergence point (with Amodei checkpoints, Testkube gates).
3. **Scout/verifier split = supervisor pattern again** (Agentiqa supervisor, Muse Sentinel, now DoorDash scout). Industry is converging on split cognition: notice cheap, verify dear. Feeds 27 directly.
4. **Evals-from-incidents = our evidence trail industrialized.** Pilot-log rows + 10x probe are the manual version; their continuous harness is the target state. Quote for 27: *"provably gets better, not hoped"*.
5. **False-clean prevention** is a named guardrail class we lacked: report MUST NOT say clean when analysis found issues. Directly maps to silent-green (our false negative) — add to 26-follow-up ammo + red-flags list on revision.
6. **Cost-per-successful-review** metric > token price — strengthens Spotify wiki + our $0-budget framing (measure outcomes per dollar, not tokens per dollar).

## Open (from wiki v1 — resolved by full text)

- ~~Full article (bot-blocked)~~ — retrieved via Wayback 12.09, page rewritten.

## Cross-links

- Article 22 (seams; cross-boundary drift) — link on next revision.
- Article 26 follow-up: disprove-it, false-clean guardrail, cost-per-success.
- Article 27: scout/verifier split, evals-from-incidents harness, fixer loop (supervised autonomy done right).
- Per-risk-tier framework: acceptance % as gate metric; routing profiles ≈ tier scoping.
- Spotify Portal wiki (cost tuning); Gupta guardrails (runtime + output layers).
