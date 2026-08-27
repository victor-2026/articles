Every company that "scaled QA" hired more testers into the same structure. That is not scaling - that is inflating.

The final-gate QA is a queue: releases wait, and the gate keeps finding the same defect classes, because nothing upstream changed.

Central QA should stop being the last step and become the quality system:

1. Standards and guardrails - what "done" means for a module, written down and measurable.
2. Test infrastructure - environments, data, CI, observability: conditions that make testing cheap enough to run continuously.
3. Quality evidence - observable proof instead of "QA passed."
4. Risk governance - metrics, error budgets, decision frameworks. In my DORA implementation, four core metrics plus QS weighting turned quality from a feeling into a number teams could manage.
5. Independent challenge - someone who asks what this change breaks that we are not testing.

Case: a client's QA function, three manual testers, regression cycle of three days. We moved them onto automation with an on-demand test bench and CI/CD checks. Same regression: four hours. The people did not disappear - their job changed from executing checks to owning the conditions that make checks possible.

The gate scales by hiring. The system scales by design.

Full article in comments.

#QualityEngineering #QAStrategy #QualityOps #DORAMetrics #OrgDesign #TestAutomation