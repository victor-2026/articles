**Format:** Pulse Article
**Series:** Quality Operating Model
**Subtitle:** Using the Inverse Conway Maneuver to align architecture, teams, quality ownership and business outcomes
**Cover:** 21-cover-conways.png (TODO: слева one team → one application; справа domains/teams/integrations + один выделенный business flow; overlay «Tests follow boundaries. Accountability follows outcomes.»)
**Feed Image:** 21-org-drift.png (TODO: два состояния - architecture evolved/QA did not vs architecture and QE aligned; без мелкого текста)
**Hook:** «Продукт становится модульным раньше, чем модель качества. Teams split, APIs multiply, integrations become critical - а QA всё ещё организован как будто один app делала одна команда.»
**Based on:** professional experience with modular systems, distributed teams and contract testing (Conway's Law + Inverse Conway Maneuver)
**Wiki:** ai-qa-wiki (TODO: org structure topic)

---

<!-- COVER: 21-cover-conways.png — one team→one application (left) vs domains/teams/integrations + highlighted business flow (right) -->

# Conway's Law Is a Quality Engineering Problem Too

*Using the Inverse Conway Maneuver to align architecture, teams, quality ownership and business outcomes*

A product can become modular long before its quality model does.

Teams split. APIs multiply. Integrations become critical. Delivery partners build extensions. Releases become increasingly independent.

Yet QA is often still organized as if one application were delivered by one team.

The answer is neither fully centralized QA nor completely decentralized testing. It is federated quality ownership: teams own the quality of the capabilities they build, while a central Quality Engineering function provides shared standards, enablement, specialist expertise and independent oversight.

## The QA implication of Conway's Law

**Conway's Law states that organizations tend to design systems that mirror the communication structures through which they work.**

In practice, team boundaries, dependencies and communication paths often become architecture boundaries, dependencies and integration points.

The **Inverse Conway Maneuver** turns this observation into an organizational design choice: shape team boundaries and communication paths to support the architecture and product flow you want.

For QA leaders, the practical question is:

**If the architecture has evolved, has the quality operating model evolved with it?**

A boundary is any point where ownership, data, behavior, technology or operational responsibility moves from one context to another. It may be a team boundary, an API or event contract, a shared data store, a vendor handoff or a transition from development to operations.

This does not mean creating one team for every service, module or API. A capability is a stable product responsibility—such as pricing, checkout, identity or fulfillment—not necessarily a single microservice.

The goal is to align stable team boundaries with stable product capabilities while protecting business outcomes that span those boundaries.

## What changes for QA

Applied to QA and Quality Engineering, the maneuver changes the question from:

> "Which central team should test this?"

to:

> "Which capability owner can prevent this failure, which business-flow owner is accountable for the outcome, and what evidence proves that the boundary is safe?"

That is the shift from a testing function to a quality operating model.

## Three shifts in the quality operating model

### 1. Quality ownership follows the capability

Teams that own reusable services, modules or product domains should own their functional correctness, API and event contracts, regression safety, compatibility and operational readiness.

A reusable capability is not **ready** merely because its feature works in isolation. It is ready when consumers can integrate with it safely, upgrades are predictable and failures are diagnosable.

### 2. Accountability follows the business outcome

A customer journey crossing channels, integrations, delivery partners and enterprise systems cannot be left with "everyone" as its owner.

It needs one named accountable owner, while responsibility for verification remains distributed across the contributing teams.

That owner should define the business invariants and ensure that the end-to-end outcome is observable through reliable evidence.

For example, a successful order is not merely a successful checkout response. It is an order created once, priced correctly, accepted by downstream systems, recoverable after failure and traceable across the journey.

This distinction between accountable and responsible is developed further in *Who Owns Quality at Boundaries?*

### 3. Central QA becomes a quality enablement and governance function

Central QA should not become the final gate for every release. Its role is to help the organization build and govern a system of quality through:

- standards and engineering guidance;
- test infrastructure and environments;
- quality evidence models;
- specialist expertise;
- metrics and risk governance;
- independent assessment of systemic risk.

The goal is not to centralize all testing. It is to make quality ownership, risks and verification explicit wherever teams, systems, data or responsibilities cross a boundary.

The broader evolution from a QA function to a quality system is discussed in *QA Function → Quality System*.

## What organizational drift looks like

Organizational drift rarely arrives as a deliberate decision. Teams and delivery paths evolve incrementally, while the existing quality model remains familiar because it still appears to work.

<!-- FEED IMAGE: 21-org-drift.png — two states: architecture evolved / QA did not (left) vs architecture and QE aligned (right); no fine text -->

The gaps surface at boundaries: during an upgrade, a production incident, an integration failure or a partner release.

Typical signs include:

- A central QA team approves releases for components it neither owns nor understands deeply.
- API and event contracts change without evidence from consumers.
- Customer-specific integrations are tested late, with production-data assumptions hidden in middleware.
- All modules are green, but the end-to-end business flow fails.
- A partner owns custom code, but no one can show its compatibility, upgrade or support evidence.
- Production alerts identify a technical error, but not the affected business outcome, service impact or accountable responder.

In one modular platform I worked with, a suite covering 28 API contracts exposed regressions in schemas, version assumptions and data semantics before the corresponding UI scenarios failed.

UI testing remained valuable. The point was not to replace it, but to move detection closer to the boundary where those defects were introduced. The suite did not merely increase test coverage; it made consumer expectations visible and executable.

This is also why a green agent report at a system boundary can be especially dangerous: it may hide false positives, false negatives or a mismatch between technical checks and business reality. I explored this problem in [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/)

## A practical quality operating model

The model is distributed by ownership, but unified by shared standards and outcome accountability.

| Owner | Primary quality responsibility | Typical evidence |
| ----- | ------------------------------ | ---------------- |
| Product/platform team | Reusable capability, contracts, compatibility, regression, baseline non-functional quality and upgrade safety | Contract tests, compatibility matrix, upgrade tests and operational readiness evidence |
| Delivery/solution team | Customer configuration, integrations, data migration, end-to-end flows and go-live readiness | Integration tests, migration rehearsal, E2E evidence and release readiness review |
| Implementation partner | Custom code, extension tests, supported versions, security fixes and upgrade validation | Test results, support matrix, security evidence and upgrade certification |
| Central QE/QA function | Standards, enablement, test platforms, quality evidence, metrics, risk governance and independent assessment | Quality standards, dashboards, risk reviews and systemic assessments |
| Business-flow owner | Customer outcome, business invariants, cross-boundary escalation and end-to-end accountability | Journey monitoring, outcome metrics, incident ownership and recovery evidence |

Delegating a customer-specific extension does not delegate product risk.

Clear extension boundaries, compatibility rules, certification gates and shared evidence are essential to keep upgrades and support sustainable.

## AI makes boundary ownership more urgent

AI-driven clients make this model even more important.

Traditional clients often constrain intent through predefined screens, workflows and permissions. An autonomous client can invoke a technically valid capability in an invalid business context—at speed and at scale.

For agentic workflows, authorization, traceability, policy enforcement and auditability should be treated as quality attributes, not left exclusively to a separate security checklist.

When an agent acts with delegated authority on behalf of a customer or employee, the system should be able to show:

- who authorized the agent;
- which agent and version acted;
- what scope and limits were granted;
- which business context applied;
- what action was proposed and executed;
- what evidence was recorded;
- how the action could be stopped, reversed or escalated;
- how the delegation chain can be reconstructed.

## Where to start

Start with one critical business flow, not an org chart.

Map it from customer action to the final system of record. Identify the capabilities, APIs, events, data owners, teams, partners and operational handoffs involved.

Then define:

- one accountable owner for the outcome;
- owners for contributing capabilities;
- explicit contracts and business invariants;
- minimum test evidence at each boundary;
- production signals, escalation paths and recovery expectations.

If the map cannot answer **who fixes it, who proves it and who is alerted when it fails**, the boundary is not yet operationally owned.

> **Tests should follow architectural boundaries. Accountability should follow the business outcome.**

The goal is not to centralize all testing. It is to make quality ownership, risks and verification explicit wherever complexity crosses a boundary.

**Where does quality ownership disappear between teams in your organization—and what evidence would make that boundary operationally safe?**

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#QualityEngineering #QAStrategy #ConwaysLaw #EngineeringLeadership #SoftwareArchitecture
