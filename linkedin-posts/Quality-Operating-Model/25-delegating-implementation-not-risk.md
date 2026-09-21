**Format:** Pulse Article
**Series:** Quality Operating Model
**Cover:** [COVER: 25-cover-delegation.png — partner vs product risk, logo stays on the box]
**Feed Image:** [SCREENSHOT: 25-partner-gate — extension contracts + compatibility rules + certification gates]
**Hook:** Your partner shipped the extension. Your logo is still on the box.

---

Delegating implementation does not delegate product risk.

**One vendor, three extensions, zero gates - that is where 80% of integration defects landed before we added certification.**

[SCREENSHOT: 25-extension-contracts — what partner may touch vs must prove]

Delegating implementation does not delegate product risk.

## Skeleton

- **Hook:** «Your partner shipped the extension. Your logo is still on the box.»
- **Body:**
  1. Распределённая разработка: partners, vendors, customer-specific implementations, outsourcing
  2. Три механизма контроля: extension contracts (что разрешено трогать), compatibility rules (версии, API, events), certification gates (доказательство до релиза)
  3. Shared test environments и evidence requirements - партнёр сдаёт не код, а доказательство качества
  4. Upgrade sustainability: как обновление платформы не ломает партнёрские расширения (regression на стыке)
- **Evidence:** [CASE: опыт пользователя с outsourcing/partners? Wimark? Virtual teams?]
- **CTA:** «What does your partner deliver: code, or evidence?»

## TODO questions to user
1. Есть ли реальный кейс с партнёрами/vendor из опыта (Virto-контекст, outsourcing, Wimark)?
2. Связывать ли с сертификацией (ISTQB-стиль) или только инженерные gates?
3. Нужен ли этот материал сейчас или лучше после 21-24 (порядок серии)?

## Cross-links (прописать при публикации)
- **Статья 21** (Conway's Law, обратный манёвр) - partner boundary в таблице quality operating model (Implementation partner row) - 25-я развивает этот ряд
- **Статья 23** (QA function -> quality system) - партнёр сдаёт evidence, а не код: связь с quality evidence model
- **Статья 24** (AI agents cross quality boundary) - агент как автономный партнёр: если человеческий партнёр сдаёт код без evidence, то агент - тем более
- **Статья 20** [Your Agent Found 5 Bugs. 4 Were Imaginary.](https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/) - партнёрский отчёт «всё зелёное» требует того же оракула, что и агент

### Parked evidence (11.09)
- Google Ads MCP-proxy ban (Aug 31): shared middle layer с одним токеном на 50 рекламодателей закрыт; каждому свой Cloud project. Vendor middle-layer trust = делегирование имплементации без делегирования границ. Цитата: «narrower than panic, wider than comfortable». Источник: YES Group newsletter via user share.

### QA-is-dead (JDAQA x Testkube, 17.09) — ammo для "passing review ≠ working product"
- Источник: `ai-qa-wiki/raw/qa-is-dead-orchestrating-quality-2026.md` (442 стр., OCR 21.09) + wiki-статья `wiki/qa-is-dead-orchestrating-quality-2026.md`. Вошла в цитатник: quotes.md, секция QA is Dead.
- **Цитата под тезис 25 (partner/dev дает артефакт, не proof):** «Reviewing the code is not testing the software. ... A passing review is not a working product.» — slide 19. Прямой аргумент: extension/dev/партнёр сдаёт "acceptable code" ≠ "correct software".
- **Вторая линия (слайд 20 mining формула):** «Size to AI-engineering output, not developer headcount» — если у партнёра scalability-аргумент (пришлём больше инженеров), отвечать формулой 120 PRs/week × 30-45 min ÷ 25 hrs = 2-4 QEs embedded.
- **Вставка:** в first comment при публикации (внешняя авторизация) — cite JDAQA x Testkube; либо 1 фраза в тело, если редактор удалит из-за лимита — нет, тело 25 заморожено, только first comment/perxlink. URL-проверка по gotcha #8.

Victor Ematin · AI Quality Engineering Lead · Independent practice

#QualityEngineering #QAStrategy #Outsourcing #QualityOps #ContractTesting
