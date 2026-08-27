**Format:** Pulse Article
**Series:** Quality Operating Model
**Cover:** 22-cover-boundaries.png (TODO)
**Feed Image:** 22-boundary-map.png (TODO)
**Hook:** «Каждый дефект, который дорого обошёлся, жил на стыке: между командами, между системами, между vendor и продуктом. Quality at the boundary - самая недооценённая работа в QA.»
**Based on:** Perplexity discussion (Aug 2026); собственный опыт: Buzzhive (refresh token race condition между 4 workers, contract tests 28/28, API 94% покрытие), distributed teams
**Wiki:** ai-qa-wiki (TODO)

---

<!-- COVER: 22-cover-boundaries.png — org chart with boundary lines highlighted, defect markers on the lines -->

# Who Owns Quality at the Boundaries?

The most expensive defect you ever shipped lived on a boundary.

Between two teams. Between two systems. Between a vendor and your product. Between the platform and the customer-specific implementation.

Nobody disputes the module is owned. The seam between modules is where ownership goes quiet.

## Why boundaries break

Each team proves its own slice works. Each team's tests pass. The seam - the contract, the timing, the failure mode, the version skew - has no owner, no test and no accountable human.

In my modular suite this showed up exactly there: a refresh token race between parallel workers, contract mismatches between API modules, integration drift no UI test ever saw. The modules were healthy. The boundaries were not.

## The three boundary layers

1. **Technical boundaries.** Contracts, events, schemas, version compatibility. This is where contract testing, consumer-driven contracts and schema validation live. My contract suite (28/28 passing) caught more real integration issues than the entire UI suite - because it targeted the seam, not the surface.

2. **Organizational boundaries.** Two teams, one journey. The answer is never "shared responsibility" - it is a named accountable owner for the end-to-end flow, with explicit business invariants and observable evidence.

3. **External boundaries.** Partners, vendors, customer-specific extensions. Delegating implementation does not delegate product risk. Extension contracts, compatibility rules, certification gates and shared test environments make the risk visible before it ships.

## The question that finds the gap

For every critical journey, ask: **who can name the owner of the seam?** If the answer takes longer than ten seconds, the defect is already scheduled - it just hasn't shipped yet.

## The closing line

Quality at the boundary is the difference between a platform and a pile of modules.

<!-- REMINDER после публикации 21: вставить ссылку на 21 (Conway's Law, обратный манёвр). Кросс-связь: 20 (Your Agent Found 5 Bugs) https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/ - границы важны потому, что ложный зелёный отчёт маскирует ответственность -->

---

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#QualityEngineering #QAStrategy #ContractTesting #IntegrationTesting #OrgDesign #QualityOps