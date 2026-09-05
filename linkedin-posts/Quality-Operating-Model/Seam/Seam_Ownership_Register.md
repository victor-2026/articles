# Seam Ownership Register

## Purpose
Track ownership, contracts, metrics, and gates for every critical seam (boundary) in the system.

## How to use
- One row per seam.
- Fill all fields before release.
- Review in design/review meetings and retrospectives.

## Seam Register (template)

| # | Seam name | Boundary type | Services/teams involved | Owner (named) | Backup owner | Contract repo/link | Contract version | End-to-end metric | Metric threshold | Alert rule | Certification gate | Evidence required | Last reviewed | Risk level |
|---|-----------|---------------|-------------------------|---------------|--------------|--------------------|------------------|-------------------|------------------|------------|--------------------|-------------------|---------------|------------|
| 1 | e.g., Auth ↔ User Profile | Technical / Organizational | Auth team, Profile team | Alice Chen | Bob Kim | github.com/org/auth-contracts | v2.3 | Login→Profile load success rate | ≥ 99.5% (7d) | PagerDuty: success_rate < 99% for 5m | Schema drift test + 4-worker race test | Test logs, trace IDs, contract test results | 2026-09-01 | Medium |
| 2 | e.g., Payment gateway ↔ Order service | External | Payments vendor, Order team | e.g., Victor Ematin | e.g., Maria Lopez | vendor.com/docs/payment-api | v1.8 | Payment completion rate | ≥ 99.0% (7d) | Slack alert on error_rate > 1% | Certification suite + sandbox replay | Evidence pack: logs, replay results, SLA report | 2026-08-28 | High |
| 3 | e.g., Recommendation engine ↔ Frontend | Technical / AI | Recs team, Web team | John Doe | Jane Smith | github.com/org/recs-contract | v3.1 | Recs render latency p95 | ≤ 300ms | Grafana alert on p95 > 300ms | A/B gate + fallback test | Trace samples, fallback coverage report | 2026-09-05 | Low |

## Boundary types
- **Technical**: contracts, schemas, events, version compatibility.
- **Organizational**: cross-team user journeys, shared flows.
- **External**: vendors, partners, customer-specific extensions.

## Definitions
- **Owner**: named accountable human for the seam (not a team).
- **Backup owner**: secondary accountable human.
- **Contract repo/link**: source of truth for API/event/schema contract.
- **End-to-end metric**: business-aligned metric for the flow crossing the seam.
- **Certification gate**: mandatory test/verification before release.
- **Evidence required**: artifacts proving the gate passed (logs, traces, reports).
- **Risk level**: Low / Medium / High based on impact and likelihood.

## Review cadence
- High-risk seams: weekly review.
- Medium-risk seams: bi-weekly review.
- Low-risk seams: monthly review.

## Notes
- If owner cannot be named in 10 seconds, the seam is unowned — escalate.
- Add new seams during design reviews, not after incidents.
