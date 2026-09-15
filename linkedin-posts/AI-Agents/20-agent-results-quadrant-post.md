**Format:** Feed Post for Article 20
**Hook:** Агент нашёл 5 багов. 4 были выдуманы. А в прошлую пятницу платформа вернула 0 находок — зелёный отчёт "no risk detected".

---

Our AI test agent found a real bug — whitespace-only posts could be submitted. Then 4 more findings, all hallucinations: it injected test data, then "discovered" the injection as a bug.

1 real bug, 4 artifacts.
20% confirmation rate, 80% false-discovery rate.

The agent is still worth running. The problem is trusting its report without measuring it.

Last week I ran the same test against a commercial AI-QA platform. I imported 5 Playwright tests, then added a second, identical sign-in form to the page — same style, same type, same label.

Three runs came back 5/5 green, each report stating "0% business risk". The step "Verify the Sign in button is visible" passed anyway. Its visual diff showed the change (2.20% → 3.19%) but never flagged it as ambiguity.

A red build forces a decision. A green report from a black box does not.


Do you track the confirmation rate for agent-reported bugs — or just count how many it found?
👇 Full article: Your Agent Found 5 Bugs. 4 Were Imaginary. — link in comments.

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#AIAgents #GenAITesting #MutationTesting