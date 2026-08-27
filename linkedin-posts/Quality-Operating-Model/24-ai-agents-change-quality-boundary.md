AI agents are a new kind of boundary-crosser - and the org chart does not know how to hold them accountable.

## Skeleton

- **Hook:** «An agent can cross more boundaries in one session than a human tester in a week - and amplify a mistake at the same speed. Who is accountable for the outcome it produced?»
- **Body:**
  1. Agents как новый client (MCP/UCP, agent-driven flows) - не UI-пользователь, не API-клиент, а автономный исполнитель
  2. Quality boundary для агентов: authorization (что агент может сделать), traceability (что он сделал), policy testing (можно ли заставить сделать запрещённое), auditability (отчёт, который нельзя подделать)
  3. Эхо-камера (мост к статье 19): same generator writes code + tests + review - verification must be outside the loop (mutation testing, contract tests, golden datasets)
  4. Conway для агентов: структура агентов повторяет оргструктуру - если ownership размыт у людей, у агентов он будет размыт ещё сильнее
- **Evidence:** DevAssure O2 (agent caught real bug + 5 false findings - same blind spot both directions); 34/34 mutation; **QAEverest decoy pilot (Aug 26): 3 green runs 5/5 + 0% business risk with two identical sign-in forms on the page - duplicate-target ambiguity not detected, visual diff 2.20%->3.19% seen but not classified**
- **CTA:** «Does your QA org have a policy for what an agent is allowed to do in production - or is the boundary still "whatever the agent asks for"?»

## Fresh angle (Aug 26): policy testing = negative testing for the tool itself

The QAEverest decoy pilot is a live case for point 2 (policy testing) that does NOT reuse the DevAssure O2 story:

- Imported 5 Playwright tests, injected a second identical sign-in form (same style, same `type="submit"`, same label). All three exported reports came back **5/5 green, 0% business risk, Low severity**. The step "Verify the Sign in button is visible" passed; visual diff grew 2.20%->3.19% but was never flagged as ambiguity.
- **Why this belongs in the accountability article:** a tool that silently picks the first matching target is a boundary-crosser you cannot audit. Authorization works (agent only did what tests allowed) - but **auditability fails**: the green report is undetectable as a lie without an independent oracle. This is the "отчёт, который нельзя подделать" requirement violated from the other side - not forged, just blind.
- **Actionable rule (answers TODO 2):** "agent policy testing" is real and concrete - run the agent against decoy/mutant/duplicate targets and require an ambiguity flag (stop, confidence drop, or suggestion). If the tool ships a green report instead, policy fails. This is negative testing applied to the testing tool itself.

## TODO questions to user
1. ~~ОК ли повторить DevAssure O2 кейс (уже был в статье 19) или нужен свежий угол?~~ ✅ Решено: свежий угол = QAEverest decoy pilot (добавлен выше)
2. ~~Вводить ли термин "agent policy testing" как новый вид тестирования?~~ ✅ Обосновано: negative testing для самого инструмента (decoy/mutant/duplicate -> required ambiguity flag)
3. Карусель для этой статьи или текст?

## Cross-links (прописать при публикации)
- **Статья 20** [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/) - тот же QAEverest decoy кейс с угла FP/FN-квадранта и 4 failure modes. 24-я берёт его с угла accountability/auditability.
- **Статья 19** (Who verifies the black box?) - эхо-камера, verification outside the loop (мост уже в Body п.3)
- **Статья 21** (Conway's Law) - п.4 Body (Conway для агентов) ссылается на обратный манёвр
- **Wiki:** [AI QA Tool Evaluation: Mutation Matrix](wiki/ai-qa-tool-evaluation-mutation-matrix.md) - метод оценки платформ, включая policy testing