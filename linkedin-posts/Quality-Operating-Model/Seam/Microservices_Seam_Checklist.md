# Microservices Seam Checklist

Use this checklist for every critical seam in a microservices architecture.

## Before design / implementation

- [ ] **Seam identified**: boundary between services/teams/vendors is explicitly named.
- [ ] **Owner assigned**: named owner + backup owner (not "shared responsibility").
- [ ] **Contract defined**: API/event/schema contract exists in a versioned repo.
- [ ] **Version strategy**: versioning scheme and deprecation policy are documented.
- [ ] **Failure modes**: timeout, retry, circuit-breaker, fallback behavior are specified.
- [ ] **Observability plan**: logs, metrics, traces for the seam are defined.

## Test strategy for the seam

- [ ] **Contract tests**: automated tests for schema/event compatibility (drift detection).
- [ ] **Integration tests**: end-to-end tests crossing the seam with realistic data.
- [ ] **Race/timing tests**: parallel workers, delayed responses, token refresh scenarios.
- [ ] **Version matrix**: test N×M version combinations (producer/consumer).
- [ ] **Chaos tests**: network latency, packet loss, service restarts at the seam.
- [ ] **Property-based tests**: generate edge-case payloads for schema boundaries.
- [ ] **Fallback tests**: verify graceful degradation when the seam fails.

## Metrics and thresholds

- [ ] **End-to-end metric**: business-aligned metric for the flow (e.g., success rate, latency p95).
- [ ] **Thresholds defined**: SLO/SLA thresholds are set and documented.
- [ ] **Alert rules**: alerts configured for threshold breaches (PagerDuty, Slack, Grafana).
- [ ] **Dashboard**: seam metrics visible on a shared dashboard.

## Release gate

- [ ] **Certification suite**: mandatory tests must pass before release.
- [ ] **Evidence pack**: logs, traces, test results collected for each release.
- [ ] **Rollback plan**: rollback procedure documented and tested.
- [ ] **Canary/feature flag**: gradual rollout mechanism for seam changes.
- [ ] **Sign-off**: owner + backup owner approve the release.

## Post-release

- [ ] **Monitoring**: seam metrics monitored for 7 days post-release.
- [ ] **Incident playbook**: steps for seam-related incidents documented.
- [ ] **Retrospective**: seam incidents reviewed, ownership/metrics updated.
- [ ] **Register updated**: Seam Ownership Register updated with lessons learned.

## External seams (vendors/partners)

- [ ] **Partner contract**: external API contract and SLA documented.
- [ ] **Shared test environment**: sandbox/staging environment available.
- [ ] **Evidence from partner**: test results, SLA reports, change notifications.
- [ ] **Customer risk assessment**: impact on customers evaluated and documented.

## AI/ML seams (if applicable)

- [ ] **Golden dataset**: evaluation dataset for model outputs at the seam.
- [ ] **Drift detection**: model/data drift monitoring in place.
- [ ] **Fallback to rules**: deterministic fallback when model confidence is low.
- [ ] **Human-in-the-loop**: escalation path for edge cases.

## 10-Second Test

- [ ] **Owner named**: can you name the seam owner in 10 seconds?
- [ ] **Metric named**: can you name the end-to-end metric in 10 seconds?
- [ ] **Gate named**: can you name the certification gate in 10 seconds?

If any answer is "no" or takes >10 seconds, the seam is unowned — escalate.
