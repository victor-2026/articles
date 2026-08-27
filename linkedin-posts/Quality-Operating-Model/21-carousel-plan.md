# Carousel 21 - Plan

**Title:** When Product Architecture Outgrows QA
**Subtitle:** A Conway's Law lens for Quality Engineering transformation
**Format:** 1080x1350 (4:5), 8 slides, PDF
**Sequence:** После связки статьи 16 → ждать 3-7 дней → карусель 21 → ещё 5-8 дней → Pulse Article 21

## Публикационная траектория (из рецензии)
1. **Сегодня утро:** карусель 16 (9:00) + Pulse Article 16 (11:00) + комментарий со ссылкой на статью под фид-постом
2. **Через 4-6 дней:** карусель 21 «When Product Architecture Outgrows QA»
3. **Ещё через 5-8 дней:** Pulse Article 21 «Conway's Law Is a Quality Engineering Problem Too»

Логика дуги: AI увеличивает объём изменений быстрее, чем растёт человеческая верификация → verification становится операционной проблемой QA-leadership → распределённая архитектура требует распределённого ownership качества → Central QE из релизного gate превращается в quality system

## Bridge sentence для карусели 21 (связь с 16)
> AI made verification a bottleneck. Distributed architecture determines where that bottleneck appears.

Или в подписи:
> AI increases the volume of change. Conway's Law helps us design the ownership model that can verify change safely across teams, services and partners.

## Слайды
1. When product architecture outgrows QA (тогда: one team→one app; сейчас: domains/APIs/partners + one QA bottleneck)
2. The gap appears quietly (teams split / APIs multiply / integrations critical / releases independent; QA как one team)
3. Conway's Law explains why (systems mirror orgs; architecture outpaces ownership → quality drifts)
4. Use the Inverse Conway Maneuver (design boundaries → evolve teams/communication/ownership; NOT one team per service)
5. Shift 1: ownership follows capability (correctness, contracts, regression safety, operational readiness)
6. Shift 2: accountability follows outcome (E2E journey, one accountable owner)
7. Shift 3: central QA becomes a quality system (standards, test infra, evidence, risk governance - not final gate)
8. Start with one critical flow (3 вопроса: prevents/proves/alerted) + formula + дискуссионный вопрос

## Файлы
- 21-carousel.html (источник)
- 21-carousel.pdf (для LinkedIn)
- /tmp/wiki/21-carousel-pages/slide-01..08.png (PNG-страницы)
- 21-carousel-post.md (сопровождающий пост: дискуссия, без «Full article» - статья позже)

## Правила
- Не копировать визуальный язык Virto (таблица/периодическая система)
- Footer на каждом слайде: Quality Operating Model · X/8
- 1 идея на слайд, 20-35 слов, крупный заголовок
- Alt text для слайдов при загрузке
- Gotcha #4: не PIL-собирать PDF - печать браузера (Playwright page.pdf) ✅

## После карусели
- Pulse Article 21 (уже готова: 21-conways-law-qa.md) - с учётом комментариев, со ссылкой «This expands on a question I raised recently...»
- Возможна вторая карусель: "Who owns quality when delivery crosses company boundaries?" (AI/partners)