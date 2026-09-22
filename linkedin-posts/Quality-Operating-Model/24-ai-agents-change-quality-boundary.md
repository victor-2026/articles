**Format:** Pulse Article
**Series:** Quality Operating Model
**Cover:** 24-cover-agents-boundary.png ✅ (1920×1080, HTML source alongside)
**Feed Image:** 24-agent-policy.png ✅ (triad, 1920×1080, HTML source alongside)
**Hook:** An agent can cross more boundaries in one session than a human tester in a week — and amplify a mistake at the same speed. Who is accountable for the outcome it produced?

---

# Agents Cross Boundaries at Machine Speed: Accountability Still Moves at Human Speed

*Same decoy as before, new question: not whether the tool fails, but who answers for what it did.*

If your mutation report is 100% green and nobody can name who is accountable for each green line, you have automation without ownership.

We imported 5 Playwright tests into an AI-QA platform and injected a second identical sign-in form — same style, same submit, same label. Three runs came back **5/5 green, 0% business risk, Low severity**. The step "Verify the Sign in button is visible" passed every time. The visual diff grew from 2.20% to 3.19% and was never flagged as ambiguity. The tool silently picked the first matching target and reported success.

### ❓ Problem

Decompose that green run and you get an uncomfortable split. **Authorization worked**: the agent did only what the tests allowed — no forbidden action, no scope escape. **Auditability failed**: the report is indistinguishable from an honest one. Not forged, just blind — and blindness leaves no trace.

Same style, same submit type, same label — identical by every attribute a matcher should care about. Which principle picked the first form over the second? The exported report doesn't say. That silence is the finding: we judge the tool as a black box, by its observable report — and even a target log would only be traceability, not an ambiguity flag.

This is the mirror image of [an earlier agent run](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/), where the agent caught a real bug and then hallucinated four more findings from its own injections. Same blind spot, both directions: the agent cannot tell the difference between discovering evidence and manufacturing it. A testing tool with no ambiguity signal is a boundary-crosser you cannot audit — it crosses from "checked" to "claimed" without leaving a mark.

### 🧭 Solution

An agent quality boundary has four parts, and most teams only built the first:

- **Authorization** — what the agent is allowed to do (roles, scopes, environments).
- **Traceability** — what the agent actually did (step log, target log, decision log).
- **Policy testing** — can you make it do the forbidden, and does it stop? Run the agent against decoy, mutant and duplicate targets and require an ambiguity flag: a stop, a confidence drop, or a suggestion. If the tool ships a green report instead, the policy fails. This is negative testing applied to the testing tool itself.
- **Auditability** — a report a third party can verify. "3 relevant mutants caught, 0 survived" is falsifiable. "100% confidence, 0% risk" is marketing copy: it tells you nothing to check.

### 🛠 Implementation

Start with one imported suite and one injected duplicate — a form, a button, or an API endpoint, the way we did. Demand the flag before you demand the coverage. Then close the echo chamber: when the same generator writes the code, the tests and the review, verification must live outside the loop (mutation checks, contract tests, golden datasets). Regulated readers will recognize the shape: model-risk management (SR 11-7-style) demands the same independence for any model whose output moves money or access. And remember Conway's revenge: agent structure mirrors org structure. If ownership is blurry among humans, it will be blurrier among agents — every unnamed boundary becomes an unaudited one.

Our oracle stayed outside the whole time: 34 deliberately seeded faults, all caught, zero survivors on the reference backend. The decoy case never touched the quadrant math — it tested the boundary, not the score.

### ✅ Result

We reported the gap instead of writing the tool off — and the vendor shipped a passive observation layer: ambiguous matches get flagged even when all steps pass. Breaking the tool on purpose made it harder to fool. Accountability, it turns out, is a feature you can request.

The checklist for your org is four questions: is there a written policy for what an agent may do in production? Is every agent action traceable to a target? Do you run decoys that must trigger an ambiguity flag? Can an outsider verify your green report? If any answer is no, the boundary is still "whatever the agent asks for" — and the bill for that arrives as an incident, not a warning.

Does your QA org have a policy for what an agent is allowed to do in production — or is the boundary still "whatever the agent asks for"?

Victor Ematin · AI Quality Engineering Lead · Independent practice

#QualityEngineering #QAStrategy #AIAgents #TestAutomation #QualityOps

## 🛠 Служебные заметки редактора (не публиковать)

<!-- REVIEWERS: IGNORE BELOW THIS LINE -->

*Все ниже — рабочие материалы. Копипаст в LinkedIn заканчивается на хештегах.*

### Angle lock (24 = accountability, NOT quadrant/method)
- Статья 20 = FP/FN-квадрант того же кейса; Статья 26 = методология + loop-closed; 24-я = accountability/auditability. Дублирования нет: 20 спрашивает "что случилось", 26 — "как ломать", 24 — "кто отвечает".
- QAEverest naming: покрыт fair-notice трейлом 26-й (naming OK). Новых клеймов о вендоре нет — только факты Aug-26 пилота + loop-closed из 26-й.

### Evidence (ссылки для инлайна — прогнать по готче #8)
- Article 20 (квадрант): https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/
- Article 26 (метод + loop-closed): https://www.linkedin.com/pulse/how-evaluate-any-ai-qa-vendor-5-scenarios-victor-ematin-lqdhe/
- Article 28 (verdict): Pulse URL on publication (scheduled Tue Sep 22 09:00)
- Article 19 (echo chamber) + Article 21 (Conway): ссылки при сборке
- Wiki mutation matrix: методология B

### QA-is-dead (JDAQA x Testkube, 17.09) — ammo для accountability-угла
- Источник: `ai-qa-wiki/raw/qa-is-dead-orchestrating-quality-2026.md` (442 стр., OCR 21.09) + wiki-статья `wiki/qa-is-dead-orchestrating-quality-2026.md`.
- **Цитата для тезиса 24 (own the risk):** «Own the risk — Accepting accountability for the release. Someone signs their name. AI cannot.» — slide 07, вошла в цитатник (quotes.md, секция QA is Dead).
- **Цитата-мост (face the unknown → 24 decoy/unknown edge):** «AI runs the known path; humans imagine the one nobody wrote down.» — slide 07.
- **Концепт-таблица:** Human Footprint (Product/Engineering/Validation, slides 16-18) — «AI does surface area, human owns truth» = визуальная поддержка AI-vs-human ownership-границы; двенадцать строк Validation (test strategy, the oracle, release go/no-go, quality governance) — готовый противовес "agent crossed boundary" в 24.
- **Вставка:** не в тело (24-я self-contained), а в first comment при публикации как внешняя авторизация тезиса (cite JDAQA x Testkube). Проверить URL/доступность ручк-ссылки по gotcha #8 перед использованием.

### Open
- Visuals SHOT 21.09 ✅ (cover + feed triad + 24-decoy-diff mock, all 1920×1080, HTML sources alongside)
- Feed post text: TODO (hook из шапки, CTA)
- First comment: TODO (repo? нет — 24-я не про VerdictGate; method links 20/26 + 1 external max)
- Inline cross-links 19/20/21/26: вставить при сборке + gotcha #8
- Reviews: R1 (человек) → publish; Perplexity/Gemini опционально (тело уже в голосе серии)
