# Session Checkpoint — 2026-08-29 (Session 109)

## Статья 21 «Conway's Law Is a Quality Engineering Problem Too» — ПУБЛИКАЦИЯ ЗАПЛАНИРОВАНА
- **Дата публикации: 2026-08-31 (Пн) 10:00**
- Текст финализирован (9.5/10), 2 раунда рецензии пройдено
- Картинки: `21-cover-conways.png` (hero, есть `<!-- COVER -->` маркер), `21-org-drift.png` (добавлен inline-маркер `<!-- FEED IMAGE -->` в секцию «What organizational drift looks like»)
- Карусель: `21-carousel.pdf` (9 слайдов)
- Фид-пост: `21-conways-law-qa-post.md`
- Bolton-цитату НЕ добавляли (решено не перегружать финализированную статью)
- Ритм запуска (если держим 48ч): пост-31.08 10:00 → карусель ~02.09 → discussion ~04.09

## Next
- Опубликовать статью 21 + фид-пост 31.08 в 10:00
- После публикации: добавить URL в hooks-library.md + performance-log.csv
- Заполнить реальные URL статей 22/23 при их публикации
- Article 27 (Guided QA Engineer): скелет готов, дописать тело (ждём CARBON?)

---

# Session Checkpoint — 2026-08-26 (Session 106)

## Статья 20 «Your Agent Found 5 Bugs. 4 Were Imaginary.» — ОПУБЛИКОВАНА
- Карусель (9:00) + статья (13:00) + фид-пост опубликованы 2026-08-26
- Карусель: https://www.linkedin.com/feed/update/urn:li:ugcPost:7498171172069511169/
- Статья: https://www.linkedin.com/pulse/your-agent-found-5-bugs-4-were-imaginary-victor-ematin-zqcte/
- performance-log.csv: 3 строки (carousel/post/article) добавлены, метрики `?`
- hooks-library.md: 5 хуков добавлены

## Статья 21 «Conway's Law Is a Quality Engineering Problem Too» — ГОТОВА (9.5/10)
- Текст финализирован по 2 раундам рецензии (federated quality ownership, boundary definition, таблица+evidence, em dash, AI через quality attributes, delegation chain)
- Картинки: `21-cover-conways.png` (one team → domains → one business flow, «across»), `21-org-drift.png` (green blocks + ORDER FAILED)
- Карусель: `21-carousel.pdf` (9 слайдов, пересобрана)
- Фид-пост: `21-conways-law-qa-post.md` (standalone)
- План: `publication-plan.md` (ритм Вт/Чт, 10:00-11:00 UK)
- **Пост-21 публикуется 9:00**

## График запуска статьи 21
| День | Формат | Тема |
|------|--------|------|
| Сегодня (Чт) | Feed image `21-org-drift.png` + problem post | "The architecture changed. Ownership didn't." |
| Четверг (след.) | Carousel `21-carousel.pdf` | "Every component is green..." |
| Вторник (след.) | Pulse article | полная система |
| Четверг (след.) | Discussion post | "Who owns the business outcome?" |

## Cross-links прописаны в 19/21/22/23/24/25/26
- 19 → ссылка на 20 (реальный URL)
- 21 → 20 (URL) + 22/23 (курсивом)
- 22/23/24/25/26 → REMINDER + cross-links на 20

## Next
- Опубликовать пост-21 (feed image + problem post) в 9:00
- Через 48ч - карусель 21
- След. вторник - статья 21
- Заполнить реальные URL статей 22/23 при их публикации

---

# Session Checkpoint — 2026-08-29 (Session 110)

## Article 27 «Guided QA Engineer» — скелет + анкоры
- `Quality-Operating-Model/27-guided-qa-engineer.md` — threads: QA-as-gatekeeper, QA-as-supervisor, Karpathy «manifesting», Bolton «bottles have necks», Bach Testing-vs-Checking
- Cross-links добавлены: Andrew Ng Loop Engineering (developer moves up = promoted role), Krivitsky nested loops (outer loop = human-owned)
- Ng + Krivitsky + Bolton + Bach = 4 внешних авторитета для тезиса «role promoted, not deleted»

## Article 21 (Conway) — статус
- Запланирована 31.08 10:00 (из Session 109)
- Feed image marker `<!-- FEED IMAGE: 21-org-drift.png -->` добавлен
- Bolton-цитату НЕ добавляли (решено не перегружать)

## Wiki ингесты (см. ai-qa-wiki checkpoint) — питают статьи 21/24/26/27
- Ng loop engineering, OpenWorker security agents, Krivitsky nested loops

## Next
- Article 27: дописать тело (после/параллельно CARBON)
- Article 21: опубликовать 31.08 10:00 (+ hooks-library, performance-log)
- Article 26 (break the tool): OpenWorker open-source harness = контраст к QAEverest closed

---

# Session Checkpoint — 2026-09-05 01:44 UTC (night of 04.09)

## 22: badge fix + 3 картинки + привязки
- **22-cover-boundaries.png:** бейдж расширен 190→270px, `DEFECT LIVES ON THE SEAM` виден целиком; бейдж приподнят; скругленные углы боксов восстановлены попиксельно (r=12), зачисток не осталось (проверено попиксельно + zoom ×3).
- **22-boundary-map.png (fixed):** маркеры дефектов стоят на швах между блоками (Service A/B, Team A/B с `?`, Our system/Vendor API); у каждого слоя своя подпись и свой owner; глиф `→` заменен на `>` (был tofu `☐`); пустого низа нет; вопрос-плашка сохранена.
- **22-coverage-vs-reality.png (new, 66K):** сплит `28/28 PASSED` зеленая панель vs таймлайн 4 воркеров (звезда-вспышка, `token overwritten`, бейдж `401 x3`) + вердикт `The contract was owned. The timing boundary was not.`
- **22-ten-second-checklist.png (new, 70K):** 3 вопроса с тегами TECHNICAL/TIMING/EXTERNAL + баннер `>10 seconds — the defect is already scheduled.`
- **Привязки:** в `22-who-owns-quality-at-boundaries.md` +2 маркера `[SCREENSHOT:]` (сплит после money paragraph, чеклист у CTA); в `22-note-0809.md` feed image → checklist.
- Палитра везде темная #0d1117 + янтарь вместо красного (по решению юзера).

## Next
- 08.09 заметка + checklist; 11.09 22 Pulse; 16.09 26 Pulse (после Rupesh).

> Checkpoint saved 2026-09-05 01:44 UTC.

## 2026-09-05 01:52 - 22 финал + брендбук + дайджест + мутации next
- **22 финалка:** правки по 2 рецензиям (самоповтор кейса убран, UI-тезис починен, Owner-буллиты, 10-Second Test, финал курсивом); хештеги 6→5; пост отполирован (3 слоя 🔹, bold 28/28, CTA Full article below👇); note-0809 (дата Tue 08.09, money paragraph, CTA, хештеги 5); first-comment WeatherNext drafted (22-first-comment.md).
- **Pulse-правила в скилле:** cover = feed-превью автоматом, отдельного Feed Image нет (метадата, Part 1/2, Workflow); фид-пост делается ПОСЛЕ обложки+статьи, приложить больше ничего нельзя. То же в wiki/pre-publish-and-monitoring.md. Из метадат 21/22 Feed Image убран; 23-27 почистить (найдено 32 матча, исторические 2-20 не трогать).
- **Cover v5:** image-gen gemini-2.5-flash-image ~$0.19 (v2-v6, опечатки TIMOUT/OWNORSHIP, отказ модели, победа v5); юзер почистил дубль BOUNDARIES в редакторе; прописана в метадату + [COVER:]; :19 снят; инлайны → pic2/pic3.
- **brandbook.md v1:** палитра, шрифты, 3 формата, bottom-line/battle/footer-правила, 3 школы, пайплайн без VPN, §8 ротация форматов; гепы (фото, единый формат, пруф-линейка).
- **21 vs брендбук:** переделок нет (~90% compliant); провал-95 — тема без чисел, не визуал.
- **График:** note Пн 08.09 + статья Чт 11.09 (данные: день недели не решает, медианы 300-500, топы — баттлы); H4 daily отложена; консервы-банк заведен (≥3 готовых).
- **Дайджест 04.09:** сгенерен + TG + блок «Нам полезно» (rogue-агенты→27, Tensor Completion→framework, Klarent→пилот, WeatherNext→коммент-22).
- **Next:** мутации ствол-2 (операторы вглубь: Delta placeholder/label/class + assertion-kind logging + candidate set под fragility layer), потом Full v2.
> Checkpoint saved 2026-09-05 01:52 MSK.
