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