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

## 2026-09-05 13:05 - чекпоинт и пуш 9a7c9b1
- Коммит+пуш: article 22 final + brandbook v1 + digest guard/routing (13 files, +416/-54). В mult-window окружении: 23-26 и прочее чужое НЕ стейджил; 27 и digest-config частично смешанные (мой rogue-блок + чужой P0-реворк; мой routes + чужой kiro-source) — упомянуто.
- Не закоммичено (оставлено): digests/*.md (как раньше, в репо не трекаются), 22-pic-cover-v2/v3/v4/v6 (промежуточные генерации ~3MB), .DS_Store/obsidian/логи, чужие правки 23-26 (там же чужой дабл-параграф в 23 — не трогал).
- Открыто на завтра: мутации ствол-2; Feed Image остался в метадатах 23-27 и старых статей (убрано только 21/22); гард digest-cover openrouter ~$0.19 потрачено.
> Checkpoint saved 2026-09-05 13:05 MSK.

## 2026-09-06 01:39 - вечерняя сессия: инверсия графика + финалка-22 в ЛИ
- **Инверсия:** note-анонс убит (мост из 21/95 imp — ложная посылка). Пн 07.09 — статья-22, Чт 11.09 — discussion вдогонку (22-note-0709.md → 22-discussion-1109.md, анонс → PS про Monday's article).
- **Данные:** W36 агрегат (1241 imp/791, 523→14 затухание, +32 фолловера) в performance-log.csv; воронка 82K→451 views = 0.55% (не 2-3%); медианы по дням 300-500, Пн лучший (508); топы — баттлы.
- **Статья-22 в ЛИ:** +2 предложения (метрика 99.5%, empowerment), can never be, явный вопрос, split-владение external, The bottom line, серийный блок (3 темы без дат), cover v5 зачищен юзером. Пост сверен (фикс ** → Unicode).
- **Авторская строка везде:** OpenCode Go → Independent practice (статья+пост+коммент+discussion, скилл, pre-publish ×2, брендбук, gamma-сценарий). Старые посты не трогаем.
- **Консервы:** Seam Register + Checklist от Perplexity в Seam/ (фиксы N×M, e.g.-имена), роль — лид-магнит к Чт + приложение к 23.
- **Открыто:** мутации ствол-2 (завтра); Feed Image в 23-27; cron 9:00 дважды не сработал (ручной прогон).
> Checkpoint saved 2026-09-06 01:39 MSK.

## 2026-09-07 18:05 - TG-бот: каталог моделей Zen обновлен
- Факт: `deepseek-v4-flash-free` (старый fallback) удален с Zen; `qwen3.6-plus` стал платным; `north-mini-code-free` исчез. Free осталось 7: spark 1.3/1.2, pickle, nemotron ultra/lightning, mimo, ling.
- `~/bot/bot.py`: таблица MODELS 18 шт (7 free + 11 go), номера + алиасы в одно слово + полные id; FALLBACK и default = spark 1.3 free; защита от мертвых моделей; /models с номерами. Бот перезапущен через launchd (polling 200 OK).
- Осторожно: импорт bot.py в тестах стартует второй инстанс (409 Conflict) — тестировать только resolve-функции изолированно.
> Checkpoint saved 2026-09-07 18:05 MSK.

## 2026-09-09 03:55 - ночь 26-й: текст, 3-й кейс, визуалы, карусель, график

**26 текст финал (до кейса-3):** заголовок `How to Evaluate Any AI-QA Vendor in 5 Scenarios`; тело буллетами (Google-правки: `your app`, silent FALSE NEGATIVE вместо FP-ошибки гугла); testRigor M3-провал первым; InfoQ simulation-eval ссылка (дайджест-роут закрыт); серийный блок с Previous-URL на 22. Именность решена: без анонимизации (таблица A/B), оба вендора со шрамами. TODO: п.1 playbook+2 кейса ✅, п.3 после 22 ✅, п.2 карусель при 6-9 слайдах ✅ (7 есть).
**Фид-тексты ×2:** `26-carousel-post.md` (standalone, article drops Monday) + first-comment (серия+22-URL); Pulse-пост обновлен (компакт-список, буллеты, real wording warnings seen 3/3 confirmed).
**3-й кейс = Agentiqa (пилот 08.09, каталог Positions-CV-CL/company/pilots/Agentiqa):** baseline 3/3 + M1-M6, 0/6 survived, паттерн «verifies FLOWS not UI» (M3 silence + M4 misattribution); evidence/ 20 логов + 5 скринов (row 43). Решения: (b) notify Ради́ка с дедлайном Вс вечер (молчание = имя), слать ТОЛЬКО секцию; соло-пост убит (SUPERSEDED, ибо advertorial); рамка «независимый аудит по неопубликованной методике» (v0.3 не течет в статью — проверено). DM-текст готов, отправляет юзер.
**Правила (SKILL + pre-publish checklist):** (1) no `#`/`##` в публикуемом теле (секции = bold-линии, `# Title` в поле заголовка); 26 конвертирована (6 заголовков). (2) Working-notes только ПОД хештегами (`## 🛠 Служебные заметки редактора`), ревьюверы зону игнорят; 26 перестроена. SKILL-дубль DELETE-блоков убран.
**Визуалы 26:** `26-mutation-matrix.png` (мой HTML-мокап 62K); pic-26-0 cover (Gemini чист); pic-26-1/2 сравнение (реген False Negative нативно; мой PIL-патч удален как стейл); `26-report-after-warning.png` (реал 07.09, Warnings & Observations, seen 3/3 confirmed) + маркер в loop-closed; loop-текст на дословный баннер (старый `WARNING ui-structure|CONFIRMED` выкинут). Карусель Gemini 7 слайдов (S3-патч THE METHOD, S4-редизайн принят, S5 апскейл 431→1080) → `26-carousel-gemini.pdf` 862K; мой `26-carousel.pdf` запасной; `26-carousel-gemini-scenario.md` для будущих сравнений.
**Discussion-22:** гибрид собран (хук 2-го + мем-строка + пример + CTA pick-3), image → 22-pic3.jpeg, дата Fri 11.09. Luis Cavalheiro ветка: правило «макс 2 ответа автора в ветке, дальше лайки».
**График (вариант B→утро Ср):** Ср 09.09 10:00 UK карусель-26 → Пт 11.09 discussion-22 → Пн 14.09 статья-26. publication-plan.md обновлен. Шрифт для конвертера: sans (брендбук §2/§4).
**Открыто на утро:** 1) публикация карусели 10:00 UK; 2) DM Радику; 3) Вс вечер — вставка кейса-3 в 26; 4) aiinqa issue #26 подтянется дайджестом сам.
> Checkpoint saved 2026-09-09 03:55 MSK.

## 2026-09-09 day - карусель вышла, discussion готов, модели-детектив, дайджест закрыт

**Карусель-26 ВЫШЛА (утро):** https://www.linkedin.com/feed/update/urn:li:ugcPost:7503248261701455872/ — day-0: 64 imp, 49 reached, 38% in / 62% out (сильный внешний старт). Workflow: performance-log строка + 3 хука в hooks-library + статус в плане.
**Discussion-22 (Пт 11.09):** гибрид финал (0× "Monday", титул 1× в P.S. + 1× в комменте, P.S. "Checklist attached"), +2 примера-инварианта (idempotency, schema version), CTA `soon`. Картинка: Gemini-реген 1376×768, Detect Defects нативно, метадата на нее. Пакет: пост + картинка + first comment.
**График финал:** Ср карусель ✅ → Пт discussion → Пн 14.09 статья-26. Даты-баги вычищены (11.09=пт, 12.09=сб были).
**Ради́к:** DM отправлен (notify+deadline Вс вечер), ждем. Кейс-3 в 26 только после.
**Модели-детектив (окно Рупеш+Мутации):** 10× invalid_request_error = opencode-слаг в OpenRouter-провайдере. Правильно: OpenRouter → `meta/muse-spark-1.3-contributor` (но требует 18+ attest + разрешение на training — contributor-тир учится на промптах!); opencode-сессия → `opencode/...-free` (Zen, без гейтов). `zen/`-префикса не существует нигде. bot.py НЕ трогать (там Zen-неймспейс, корректен). Итог окна: спарк заработал, recalibration-нарратив отозван везде, reply-draft-08 готов. Рупеш≠Амир (два разных человека/папки!). Архив к контроферте: emails/counter-proposal-pack-2026-09-09.zip (490K, 7 файлов: контроферта + v0.3×3 + evidence + 2 exec-отчета 07.09). Холдинг уже был SENT (mv лишний).
**Дайджест 09.09 (11/11):** wiki/muse-meta-personal-ai-agent-2026.md NEW (Sentinel=supervisor-паттерн, 4 QA-угла); 27: swarm=дубль эп.1, GitLab=Эпизод 4; 26: GitLab PARKED в working notes; остальное распределено (ai-qa-wiki / pilot-кандидаты / skip с причиной).
**Открыто:** Пт discussion-пост; Вс дедлайн Ради́ка → вставка кейса-3; Пн статья-26.
> Checkpoint saved 2026-09-09 (day).

## 2026-09-11 ~05:00 - handover из соседнего окна: 2 внешние цитаты для статьи 26 (п.1, обработать агенту)

**Источник:** LifeMichael "Develop with AI Monthly Review" (Aug 15, 2026): https://www.linkedin.com/pulse/develop-ai-monthly-review-lifemichael-rwcif/ — ingested: ai-qa-wiki `raw/lifemichael-develop-with-ai-monthly-review-2026-08.md` + wiki-саммари `wiki/lifemichael-develop-with-ai-monthly-review-2026-08.md` (topics 332). Решение юзера: в черновик 26 НЕ вплетать сейчас, обработать здесь.
**Цитата А (orchestration):** софтдев сдвигается от одиночных код-агентов к платформам оркестрации (Kiro Crew AWS open-source, Devin): декомпозиция, параллельность, persistent context, validation + human review как фичи. Применение в 26: внешнее подтверждение тезиса "verification layer мейнстримится, вендоры сами признают". Первоисточник: https://lifemichael.com/en/software-development-with-ai-moves-toward-agent-orchestration/
**Цитата Б (swarm economics):** Cursor, пересборка SQLite роями: лучшая координация = тот же/лучший результат при радикально другой цене. Применение в 26: эмпирика под harness>model. Первоисточник: https://cursor.com/blog/agent-swarm-model-economics
**Дополнительно (если место):** JetBrains Context (repo-intelligence для агентов) + Claude cyber-evals (3 кейса неавторизованного доступа к реал-системам) — guardrails-угол; XtremeAI conf 24.11 — следить за proceedings; Kiro Crew — кандидат в пилоты (open-source).
**Уже сделано в соседнем окне:** Desplenter 2026 AI Readiness Report проверен (79/55/42/64 подтверждены из его постов) + sources-блок уже лежит в `26-first-comment.md`. Не дублировать, только А+Б.
> Handover saved 2026-09-11 ~05:00 MSK (окно "Статьи+Мутации": взять А+Б в статью 26 до пн 14.09).

## 2026-09-11 ~05:10 - routing от юзера агенту окна (прочитать первым)

**Файл-контракт:** `/Users/victor/Projects/Articles/WORKING-NOTES.md`
```bash
code /Users/victor/Projects/Articles/WORKING-NOTES.md
```
**Контекст:** корневых `/AGENTS.md` и `~/AGENTS.md` нет и не будет — контракт живет в репо Articles (AGENTS.md + WORKING-NOTES.md рядом). Порядок чтения: сначала WORKING-NOTES.md (§4 mutex + §3 токены), потом Articles AGENTS.md при нужде.
**Честная оговорка:** контракт покрывает файлы Articles. Пилоты/аутрич в Positions-CV-CL живут по своим правилам (pilot-log) — кросс-репная часть контракта (§5 карта) на них ссылается, но не управляет.
> Relayed 2026-09-11 ~05:10 MSK.

## 2026-09-11 - discussion-22 вышел + контракт обкатывается
- **Discussion-22 опубликован** (Пт, hybrid-текст, checklist-картинка): day-0 2h = 58 imp / 42 reached / 78% out, 1 reaction, 0 комментов. Первый коммент со ссылкой posted. Performance-log + 2 хука + статус плана ✅.
- **WORKING-NOTES.md** создан (контракт: размещение, маркер, токены, mutex 30 мин, карта) + п.7 в AGENTS.md. 26-я — эталон (токены ⏳/✅, маркер). Релей соседнему окну отправлен.
- **26-я ждет:** Вс дедлайн Ради́ка/Адама → вставка/финал кейса-3; 10x + cold-M3 у соседнего окна; Пн 14.09 публикация (пост уже на 3 vendors).
> Checkpoint saved 2026-09-11.

## 2026-09-11 (eve) - digest 11.09 + правила из ошибок
- **Digest 11.09 закрыт 12/12:** 27 → Эпизод 5 (Mythos 5 CAPTCHA-ад + PyPI-заливка); Muse wiki +traction (No.2, 83K, Instinct $2.5B) +hands-on (API>UI, location leak, галлюцинации); 26 → Testμ/Ghaib/Klain припаркованы (тело заморожено); остальное skip/transfer с причиной.
- **26-я дозаполнена заранее:** author line возвращена, Desplenter-статистика вшита в 🔍 (коммент требовал), ссылка на карусель в first comment, пост на 3 vendors + Agentiqa-строка. Аудит зоны чист.
- **Правила:** gotcha #4 в глобальной памяти (bulk edit ate lines) + WORKING-NOTES.md §7 Edit discipline (exact-match, assert-before-bulk, re-read-after).
- **10x:** 3/10 PASSED. Cold M3 + learning-клауза ждут Вс/Пн.
> Checkpoint saved 2026-09-11 (eve).

## 2026-09-11/12 night - cold finding, naming closed, wiki batch
- **Cold M3: FAIL vs warm 3/3 PASS** — память несет вердикт, не ускоряет. Тело 26-й: M3-строка warm/cold + клауза повторов с caveat; learning-эффект (M3/M6 времена) — кандидат, не утверждение. 0 survived стоит (fail=killed).
- **Naming Agentiqa CONFIRMED** (pilot-log rows 74–75, спор closed); Sunday-гейт по Радику снят, остался Адам. Radik-message оценено: (a)→уведомление не вопрос, +дедлайн-строка, канал email.
- **Megi follow-up SENT 11.09** (reply 29.08 был отправлен — stale-pending зачищен в index).
- **Wiki batch:** muse +traction/hands-on; ai-guardrail-layers-gupta (memory=наш кейс); testkube-evals-as-gates (prompt-мутации, per-tier convergence); spotify-portal (advisory→enforceable). YES Group: в дайджест нет (no RSS + 2/3 мимо), MCP-story припаркована в 25.
- **WORKING-NOTES.md + §7 + gotcha #4** (bulk-edit discipline); 26-я — эталон токенов; релей соседям отправлен.
- **10x:** 6/10, 7/10 летит (пачками). **Пн 14.09 статья-26** — осталось: Вс дедлайн Адама, финал-аудит, публикация.
> Checkpoint saved 2026-09-12 night.

## 2026-09-12 (day) - 26 scheduled Mon 9:00, threads closed
- **Article 26 в расписании LI на Пн 9:00** (текст + cover + 3 скрина + фид-пост). First comment — вручную в 9:05 Пн (не шедулится). Остаток мне после: performance-log + hooks.
- **Типографика решена:** EN-статьи/посты — em dash (M5 только для RU); конвертированы пост + тело 26-й (цитата баннера нетронута). Unicode-сага: смешанные стили — источник в буфере/конвертере, не в редакторе; фикс — набирать руками.
- **Megi:** follow-up + ack SENT, ответ 9:30 PM (дизайн-цепочка 5 стадий, прогонов нет, ждет Пн как бенчмарк). Тред спит до ее ранов.
- **Bolton:** не комментируем до Пн (холодный коммент растворится; после статьи — предметно).
- **Digest 12.09:** сгенерирован (3.12 явно; крон уже на 3.12 — ок), разобран 8/8 (wiki traces; парк 26; остальное skip/transfer).
- **Naming closed:** Agentiqa confirmed (rows 74-75), Adam/Radik молчание=согласие (дедлайн Вс), Rupesh confirmed письменно. OrangePro/Аамир — 0 упоминаний во всем репо, трек изолирован.
- **Cold M3: FAIL vs warm 3/3** — память несет вердикт; тело отражает (warm/cold). 10x: 6-7/10.
- **Wiki batch:** muse(+traction/hands-on), guardrails-gupta, testkube-gates, spotify-portal, session-traces. YES Group: не подписываемся (no RSS + мимо), MCP-story в парк 25-й.
> Checkpoint saved 2026-09-12 (day).

## 2026-09-14 (day) - Article 26 published, quadruple validation, weekly reports
- **Article 26 published LI Пн 14.09 09:00 UK.** Carousel Sep 9 (513 imp), Pulse article Sep 14 (157 imp day-1). Rupesh CEO first comment confirming method + product fix live.
- **Comments made:** Martin Miceli article (his article), Estefania Miceli post, Gururaj Hm post. All 3 posted.
- **Martin Miceli (CTO Parser) direct reply to comment:** "blank scores zero = green report with no ambiguity flag" + "mutation matrix sounds like very interesting empirical validation." "Uncertainty itself is valuable information." CEO publicly validated method.
- **Quadruple validation thread live:** Estefania (QA lead) + Martin (CTO Parser) + Gururaj (AI Eng Leader) + Rupesh (CEO QAEverest) — 4 industry leaders confirming silent false negative thesis.
- **Weekly reports generated:** W36 (Aug 25-31, 2,256 imp, Article 21 Conway launch 67%), W37 (Sep 1-7, 681 imp, dead week), W38 (Sep 8-14, 1,442 imp, Article 26 carousel 513 imp). 5 charts + 3 markdown reports in `linkedin-posts/weekly/`.
- **Digest 13.09:** 6/131 items, broken down (Playwright feed, visual regression, AI agents lying, rogue AI hack). Sep 12 gap confirmed NOT missing (data present).
- **Analytics verified:** 90-day (164,155 imp, 0 gaps) and 7-day (1,442 imp, 0 gaps) files — complete, no missing dates.
- **Jason Arbon "Testing AI" book:** Found complete library in `ai-qa-wiki/wiki/testing-ai-book-index.md` (21 chapters, 194 concept briefs). Created wiki page in Articles, then deleted as duplicate. Amodei wiki updated with book reference. Task-catalog updated.
- **Wiki updates:** `amodei-pace-the-frontier-2026.md` + items 6,7,8 (Rahul Parwal quote, Arbon book, Martin direct endorsement). `task-catalog.md` + P2 entry for Arbon book.
- **Rupesh recommendation (Draft 2):** ready to send, relationship warm (he just publicly endorsed work). Not sent yet.
> Checkpoint saved 2026-09-14 (day).

## 2026-09-15 (evening) - VerdictGate: продукт запущен (приватно)
- **Neiming saga:** MutGate мертв - коллизия PyPI (mutgate v0.1.1, JimGalasyn, активный с 08.09, named mutations as contracts) + mutation-gate (GitHub) + mutago (Go) = вся mut+gate окрестность занята. Перебор по глоссарию (7 стратегий, 15+ кандидатов) -> **verdictgate** (PyPI/npm/GitHub свободны): вердикт = coined term серии + артефакт verdict.md + ниша из концепта; полный выход из mut-окрестности = фича (мы не исполнитель). Plan B: tiergate.
- **Продукт:** victor-2026/verdictgate (PRIVATE до публикации Article 27). Phase 0-4 done за одну сессию: CLI (verdictgate.py, stdlib, 340 строк), templates (lite/full/methodology + results.csv + requirements.csv + evidence-pack), 4 примера (web-login PASS-with-signals / demo-math clean / payment-critical-fail exit 1 / noop-row exit 2), golden files, selfcheck CI (success 9s: golden diff + exit codes + determinism).
- **Ключевые решения зафиксированы в концепте** (ai-qa-wiki/outputs/product-concept-mutation-verifier-mvp.md, 9 правок с ассертами): статус ПРИНЯТ, oracle-gate в Why-not-X, B2 = Позиция C (дефолт строгий + vendor profiles в v0.2), override правила репо-сигнала (приватно сейчас, публично после 27-й), все 5 вопросов §12 закрыты.
- **Hard rules продукта:** детерминизм (no timestamps/random), SCORER_VERSION bump + golden update при любом изменении правил (урок 0.2.34->0.2.40), exit-code contract 0/1/2, zero-tolerance B0/B1 неконфигурируем, no-op refuse-pre-seed на входе.
- **Phase 5 (запуск) ждет Article 27:** публичность репо + follow-up пост на 26-ю ("method, codified") + DM вендорам (Rupesh/Adam/Radik могут прогнать свой CSV).
## 2026-09-15 (afternoon/evening) - VerdictGate v0.1.0 shipped + Article 27 edits
- **VerdictGate:** repo `victor-2026/verdictgate` pushed to GitHub (PRIVATE), CI selfcheck SUCCESS (9s: golden diff + exit 0/1/2 + determinism). 17 files committed. Author line fixed on 5 published articles (OpenCode Go → Independent practice).
- **Article 27:** rogue-line Episodes 4-5 inserted as one-line ladder in Result section ("swarm → backchannel → 3700 agents → GitLab proxy → Mythos 5 UI-gate"). Author line fixed. Ready for review.
- **All published articles:** author line normalized to `Victor Ematin · AI Quality Engineering Lead · Independent practice`.

## 2026-09-15 (late) - Article 27 body finalized for Fri 19.09 publication
- **Headline locked:** "QA Didn't Get Replaced. It Got Promoted." + sub-headline "The Guided QA Engineer: Why AI Promotes the Tester Instead of Replacing Them"
- **Hook fixed:** "their team writes 80% of the code" (not "an agent")
- **Problem:** question form — "who steers the quality criteria?"
- **Implementation:** Megi ProCredit mention removed; added B0 payment/auth example (idempotency, validator mutation)
- **Result:** rogue-line ladder compressed to 1 sentence (GitLab proxy + German wiki + Mythos 5 UI-gate)
- **Evidence:** 4 key links in body (Ng, Bolton, Article 26, Zalando); rest moved to first comment draft
- **Cleaned:** removed all working-notes sections (What to develop further, Raw threads, Open questions, Примечание, Rogue-линия)
- **Added:** "## Драфт 15.09" section with full 4-section body + visual assets checklist + first comment draft + cross-links
- **Author line:** confirmed "Independent practice" everywhere
- **Publication:** Fri 19.09 10:00 UK; carousel decision tomorrow by visual readiness

> Checkpoint saved 2026-09-15 (evening).

## 2026-09-15 (night) - 27 ready (text+visuals), link saga closed, digest done, Luxoft declined
- **Article 27 FINAL (Variant A):** body ~850 words (worked example: QAEverest sign-off 07/09, 0/4→3/3 relevance-gated, B0 100% x2, 10/10, c3d7) + 3 visuals generated HTML→PNG via Playwright (dark #0d1117+amber, 2x): 27-cover-guided.png (2400×1288), 27-gate-card.png, 27-before-after.png (+HTML sources alongside). Carousel CANCELLED for 19.09 (review: 4 theses ≠ 6-9 slides) → 5-slide derivative later. External review #1 (8→9/10: 4-vs-3 clarified, 90/80 dropped as sourceless, CCN expanded) + visual review accepted; rebuttals verified (Bolton quote verbatim from his 28.08 post; rogue ladder digest-sourced, links in 1st comment). Tech-writer skill pass: 10 fixes applied (lead ≤106ch, B-tier plain line, 5 hashtags, section emojis), blockers left for LI input per user. Open to Fri: gyn5e URL, Megi line in 1st comment, publish click.
- **Link saga CLOSED:** Article 26 long URL alive (webfetch "not found" was guest-view block, lnkd.in/eRTHUX3K was cache). Gotcha #8 in global memory: verify all external links pre-publish via browser/incognito, long URLs only. Konstantin/Adam/Megi DMs need correct-URL resend.
- **15-flashback (Wed 16.09) DONE:** post published, dashboard 100/100 screenshot captured, Badri/Divya email sent (audit proposal), Article 15 comment posted. All 4 steps complete.
- **Digest 15.09 parsed 6/6:** Applitools Validation Gap → wiki + 26-follow-up/VerdictGate; healthcare eval primer → wiki + per-risk-tier; Klain dup (PARKED 11.09); MoT/Cappy-stale/SeqMaestro skipped. Cappy-2024 → stale-date guard fixed in daily-digest.py (year-fallback, tested 5/5).
- **Slavnov:** methodology question answered (Article 26 link sent).
- **Rupesh — CLOSED:** commercial engagement declined by Rupesh. Per-risk-tier methodology exchange complete; attestation methodology documented; no commercial deal. Status updated across all trackers.
- **Luxoft Senior AI Developer (Anna Koroleva, Remote Serbia) DECLINED:** 40% fit (triage taxonomy, CBT, evals) vs hard gaps (Java 3y+, Appium/ADB, Bedrock) + Senior IC vs leadership-only filter. Reply draft ready (decline + keep-warm for Lead roles); tracker logging pending user OK.
> Checkpoint saved 2026-09-15 (night).

## 2026-09-15 (night) - Article 27 final edits + quotes bank
- **Body:** senior hook 2nd sentence restored ("their team writes 80% of the code", from skeleton 2fb2255); repetition trimmed (21); units unified to % survival (30); B1 glossed "core flows" (15); Klain moved body→first comment (lean ending: rogue + Zalando + CTA).
- **Rules set with user:** `###` headers + `[SCREENSHOT:]` markers stay as authoring markup — NOT flagged in reviews (user lays out at LI paste). Feed carries cover ONLY, never extra visuals (standing rule, recorded in post file).
- **Feed V2 (conflict):** CTA → "Full article below👇", 5 hashtags, visual section removed. V1 moved to `27-guided-qa-engineer-post-week.md` (standalone discussion post, tail rewrite pending).
- **gyn5e closed:** URL lived in Article 26 notes all along, copied to 27 (97, 122, comment).
- **Open:** Megi numbers (Review Effort min per tier — check thread; fallback: drop by 19.09) · V1 tail rewrite.

## 2026-09-17 (day) - Wiki building + digest + quotes bank + ContextQA + Adam Tornhill
- **ContextQA assessed:** LinkedIn 1 month, ~30 posts. AI Agent Testing Platform (enterprise, no-code, self-healing, Agentic Quality Tour). NOT for pilots (proprietary SaaS, no mutation testing, marketing-heavy). Saved to raw as market reference. Tatyana Arbouzova connection noted.
- **BeeCommerce blog checked:** e-commerce focused (headless, Magento, Shopify). 1 article already saved (12 agents, 5 layers). Rest = domain-specific, NOT for digest. Skip.
- **Adam Tornhill article saved:** "Practices I Abandoned with Agents" — after 25 years TDD, abandoned for agentic coding. E2e tests = human/agent boundary. Code for machine consumption. Double-entry bookkeeping (don't let AI change tests). Tooling enforces what you don't inspect. Strong connection to Article 27 + Tornhill's own CodeScene work.
- **Digest 16.09 parsed:** 12 items from 429 sources. 3 saved to raw:
  - TestMu AI: LLM Eval vs E2E Agent Testing (eval≠gate, Green/Yellow/Red)
  - TestMu AI: Finance AI Agent Compliance (FINRA, attestation pattern)
  - Anton Gulin: Save clues from failed Playwright test (retain-on-failure, evidence chain)
- **Bach vs Jensen debate:** "Safety is an engineering problem" (Jensen, Dreamforce) vs "Market forces do NOT optimize for safety" (Bach). Saved to raw as debate framing for Article 27.
- **Quotes bank:** 15 quotes in `quotes.md`. 13 added today across 5 sections: Displacement (1), Evals vs Tests (3), Agent Coding (4), AI Safety (3), Independence/Attestation (4). Key: "The author can't be the examiner" (Pettersson), "Harness configuration is a file" (Bansal/Bansal), "$5 PR = how much verification?" (Pettersson).
- **QA.tech researched:** Daniel Mauno Pettersson, CEO. Stockholm, $4.3M funding, 10-20 employees. Autonomous QA agents. Two key insights: (1) author≠examiner, (2) verification ratio depends on what PR touches.
- **wiki-topics.json:** 357 → 363 (+6: Tornhill, TestMu×2, Anton Gulin, Bach-Jensen, ContextQA).
- **Article 27 status:** body+visuals ready. Blocked on: gyn5e URL (in file now), Megi numbers (if available by Fri). Publication Fri 19.09 10:00 UK.
- **Next:** Megi numbers check, Article 27 publish, follow-ups (Radik, Adam).
- **quotes.md created:** quotes bank with source+use rule; first entry Lew (QA reshuffled faster than any SWE part).

## 2026-09-17 — Article 27 pre-publish + rules + 28 draft
- 27: inline links on first mentions (Bolton/Ng/26/Zalando; 20 skipped — no URL), 2 screenshot markers spread (gate table → Solution, before-after → Implementation end), all 3 visuals verified by eye.
- Link fix: 26-slag lost `-in` (404) → corrected in 4 files (15, performance-log, 27, 28), verified 200.
- Feed V2: caps reverted (a11y), H1 rule noted (27 grandfathered — cover baked).
- New standing rules (tech-writer SKILL 13/14 + emphasis budget): no "Article N", no periods in headlines, feed bold first+last only, body emphasis budget.
- 28 draft (launch, Tue 23.09): H1 undecided (#1 vs #2), body trimmed, quotes.md bank started.
- Open: H1 call, Megi numbers, repo public Fri, cover confirm, hashtags line.

## 2026-09-17 (evening) - Article 27 LI ready, Boris Cherny, digest 16-17, push
- **Article 27 published to LinkedIn draft** — ready for Fri 19.09 09:00 publication. All blockers resolved (gyn5e URL, Megi line dropped).
- **Boris Cherny transcript saved:** Claude Code practical tips (Anthropic). Key: CLAUDE.md = AGENTS.md pattern; "give it self-check tools" = Article 27 thesis; tiered bash permissions = B0-B3 gates; SDK = Unix utility; 80% Anthropic staff use daily; "IDEs may disappear by end of year."
- **Digest 16.09:** 3/12 already processed (Playwright, TestMu×2). Rest skip.
- **Digest 17.09:** 2 strong saved:
  - Keith Klain "Death by a Thousand Prompts" — "5 No's", Amodei critique, "more tests ≠ better testing"
  - Michaela Greiler SCOPE model — "agent tests signal safety where there is none", code review exploitation/surrender
- **Quotes bank:** 18 total (+3 today: Klain ×2, Greiler ×1).
- **wiki-topics.json:** 357 → 366 (+9 today).
- **Raw files today:** 6 (Tornhill, TestMu×2, Bach-Jensen, Boris Cherny, Klain, Greiler, ContextQA = 8 total).
- **Push:** Articles repo committed + pushed. Session checkpoint updated.

## 2026-09-17 (late) - Jason Arbon book comment + outreach
- **Jason Arbon post commented:** "How AI Tests Software" free book draft (first 100 readers). Comment sent: referenced "Testing AI" as key research source, expressed interest in eval vs behavioral testing boundary. URL: https://www.linkedin.com/feed/update/urn:li:activity:7482931369593946112/
- **Arbon already tracked** in task-catalog as P2 (Testing AI book, Chapter 11 = Article 27). This comment = Prong C engagement + free book access.

## 2026-09-17 (night) - Agentics Foundation Serbia wiki + Radik Action Ontology + Ukkuru quotes

**Agentics Foundation Serbia YouTube — full catalog:**
- RSS feed `UCp0JEOqglATIewFo17HSJpg` parsed — 14 videos (#1-#15, #3 missing)
- `wiki/agentics-foundation-serbia-youtube-2025-2026.md` — 14 meetup summaries, cross-links, 10 key quotes
- Dragan Spiridonov: Head of Agentic QE, Cognitum One; Agentics Foundation Secretary & Ambassador for Serbia
- Key for articles: "Two bugs in 10 min agent missed" (#15), "Agents say done ≠ works" (#11), "Autonomy scope creep 20-30 repos" (#15)
- **Digest config** updated: YouTube RSS + Dragan Spiridonov added to tracked sources + brands (AQE Fleet, Nagual-QE, RuFlo, Vibium, Agentics Foundation)

**Radik Zagirov (Agentiqa) — Action Ontology Runtimes:**
- Raw: `raw/radik-zagirov-action-ontology-runtimes-2026.md`
- Wiki: `wiki/action-ontology-runtimes-agent-execution-2026.md` — 3 architectural shifts
- Key: "hallucinations cannot mutate state" = our harness-as-state-machine; "SubmitOrder physically doesn't exist if not approved" = dynamic action spaces
- Cross-links: Articles 22/27, Greiler SCOPE, Tornhill tooling, Bansal harness config
- Quotes +3: "LM ≠ OS", "hallucinations cannot mutate state", "dynamic action spaces"

**George Ukkuru — Nobody Owning the Quality:**
- Quotes +3: Ukkuru "nobody owns", Cook "eval = shape not correctness", Hudekar "blind spot — why separated dev/QA"

**Quotes bank:** 18 → 27 (+9 today).
**wiki-topics.json:** 366 → 375 (+9).
**Repos pushed:** ai-qa-wiki `4f0a00a` → `1bc025f`, Articles `c777b85` → `d47dad4`.

## 2026-09-17/18 — Oleg letter pivot + Virto recon + 26/27/28 publishing flow
- Radik corrected: IS in published 26 (Worked example 3, Agentiqa 0/6); saw text pre-publish, no approval, set limits. My SUPERSEDED memory was stale — checked file, owned error.
- Strategy pivot: hiring lane stalled (month silence) → letter gets formal NO + pivot to Oleg substance (verify Radik pilots + attest Virto packs). Split letters: Larisa closure, Oleg proposal. 26 URL fixed (dropped -in, 404→200, 4 files).
- Oleg draft written (peer, price-principle, 30-min ask). Aamir resume parked post-27.
- Virto recon: vc-mcp-testing-module mapped (CSV suites + CI twins + P0 042/078/039/044/049) + local glossary found (was interview prep). No deploy before Oleg signal.
- 27 publishing Fri: cover+2 visuals verified, feed V2 (no caps), hashtags kept, no-numbers rule (skill 13), no-periods rule (skill 14), emphasis budget.
- 28 draft: H1 locked #1-colon, Perplexity 7/10 review applied (5 fixes), Pettersson selected, test-editing failure mode to wiki.
- Videos: V1 terminal (35s, Daniel, user-approved) + 26 Ken Burns (33s, fit-within rule) pipelines proven.

## 2026-09-18 (Fri) — Article 27 published, repo public, Oleg letter ready
- 27 live 9:00 (Pulse qa-didnt-get-replaced-got-promoted + lnkd.in + activity URN). 30 articles in profile.
- Repo PUBLIC (gh edit, README 200). AGENTS.md status updated.
- 26 URL fixed (-in dropped, 404→200, 4 files). 28 draft: Perplexity 7/10 applied, Pettersson in, H1 undecided→#1-colon, video V1 EN+RU rendered.
- Rules added (tech-writer 13/14 + emphasis budget): no Article N, no headline periods, feed bold first+last, body budget.
- Larisa+Oleg letter FINAL (split decided, then joint To: both; hire-closure + pilot + benefits + 2 links; send Fri). **SENT.**
- 1.0 exit criteria public (README). Investment ledger split (product 427m + methodology 60+h).
- Kanban sync Notion → local: тема закрыта (Notion dropped).
- Perplexity R2: DONE (conditional pass, findings → 0.2.1, triage in `reviews/perplexity-round2-triage-2026-09-17.md`). 0.2.2 (requirements guard) covered by Kimi (clean). Perplexity не трогаем.
- Open next: 28 launch Tue 23.09 · Radik follow-up ~20.09 · Megi reply · Oct 17 recheck.

## 2026-09-19 (Sat) — VerdictGate comments + Kristel transcript + Matt Graham + quotes

**VerdictGate comments (organic, zero-budget):**
- Article 20 ✅ — "The mutation matrix from this article now has a CLI" → https://github.com/victor-2026/verdictgate (feed: urn:li:ugcPost:7498171172069511169)
- Article 26 ✅ — "The method above is now code" (posted by user this morning, confirmed). Feed URL fixed: broken `urn:li:activity-...` → correct `urn:li:ugcPost:7504628732557459456/`
- Article 27 — postponed (user decision)
- LinkedIn boost: Article 26 eligible (feed post), Articles 13/12 (carousels) NOT boostable (document type). User = zero-budget, no boost.

**Kristel Kruustuk (Testlio founder):**
- Post + video transcript saved: `raw/kristel-kruustuk-video-transcript-2026.md` + `raw/kristel-kruustuk-ceos-testing-matters-2026.md`
- Quotes +7: Chamath "improvement engineering" (via Kristel), Amodei "independent testers", Nadella "third-party testers", Kristel "gap nobody's measuring", "silent failure", "improvement engineering", "test it like it matters"
- Key insight: Chamath coined "improvement engineering" — Kristel's video confirms

**Matt Graham (CEO RapidDev, 53K followers):**
- Comment posted on "last few 9s" post (UNBOUND conference): mutation testing = measuring last 9s in QA
- Post URL: https://www.linkedin.com/posts/matt-graham-nocode_training-the-next-generation-of-ai-models-activity-7497652207232913408-Vpa4
- Quotes +5: "last 9s brutally hard", "output cheap judgment expensive", "data problem nobody talks about", "automate 80% = shrink headcount", "high bar ≠ difficult"

**Aston Cook (AssertHired) + Leonardo Lanni (QA Roots):**
- Aston Cook comment reply — **SENT ✅** (11h ago, "confidence scales with suite size, evidence doesn't")
- Leonardo Lanni connection accepted + reply drafted (AI evaluation peer exchange)

**Status updates (user-confirmed):**
- Oleg letter — **SENT**
- Megi — request sent, awaiting reply
- Kanban sync Notion → local — **closed** (Notion dropped)
- Perplexity R2 — **DONE** (conditional pass, 0.2.1, Kimi 0.2.2 clean). Perplexity не трогаем.

**Performance log:** Article 26 feed URL fixed (broken → correct). Pushed `78f4cdd`.

**Quotes bank:** 27 → 34 (+7 Kristel +5 Matt Graham -1 overlap = net +11). Total: 34 quotes, 7 sections.
**Repos pushed:** Articles `5234337`, ai-qa-wiki `158e817`.

## 2026-09-19 eve — Kanaris reply SENT
- Paul Kanaris (QACE) pushback on 27 (QA owning AI-validation). Reply SENT: examiner≠author, tiers = release owner states bar, relevance gate = customer-needs layer stays QA. Thread: 1 reply used of 2.

## 2026-09-19 eve — Jan Moehlmann (stealth/YC/vex.sc→Composal) DRAFT, NOT SENT
- Discovery-miner (growth operator, ex-GM 11x.ai). No call offered. Draft locked (correction + one-liner + repo link): "our verdict was red (0/4), their dashboard green... green measured absence of red, not presence of detection." DRAFT SENT (final wording: "their dashboard was green, but our verdict was red (0/4 detected, unverified)... absence of red, not presence of detection... deciding what the sensor suite *should* capture"). No call offered.

## 2026-09-19 eve — W4 handover verified (28 batch 2735483)
- P0 5/5 closed (repo+MIT, cover spec, real CSV block, gotcha #8, 6th hashtag). P1 decided (lede, bridge, feed file, Pettersson kept). 0 placeholders/TBD in article. Verified by main.
- OWNER backlog: cover shoot · browser link check · approve R3 P0 #2 (Pettersson split) + P1 #5 (exit code).

## 2026-09-19 night — 28 review cascade closed (R1/R2/R3/Perplexity/Gemini) + outreach warmth

**Article 28 (W4, commits → `da3130b`):**
- R1 top-3 applied (repo inline, zero-P0-left-open, strict-schema entry cost) + R3 P0 #2 (Pettersson verbatim split) + P1 #5 (exit code) — all staged then applied on user go
- R3 P1 #6 slug claim REFUTED (reviewer wrong; no-"in" slug = fixed 404→200)
- Real CSV block byte-exact from `payment-critical-fail` run (exit 1); reviewer 5-col snippet refuted (missing operator → exit 2)
- Perplexity click-max: T1/T2/T4/T5/T6 applied, T8 staged; Conflict A resolved = SERIES (lede links stay)
- Feed: click-revision (goal article, 5 tags) → video line removed (LI axiom: feed = cover only) → URL line removed by user (cover-click mechanics + Gemini 10/10)
- Video V1 decoupled to separate trial post (plan file updated)
- T9 Gemini lede hybrid APPLIED; 427 scope clarified ("measured minutes on hardening + review cycle")
- Scores: Perplexity 9.5/8.5/8 → article; Gemini 9.5/10 article, 10/10 feed
- Open to 23.09: T3 (user facts) · cover shoot · browser link check · mobile-indent QA

**Outreach:**
- Leonardo Lanni: user sent mutation-matrix + VerdictGate link; Leonardo WARM (RMT compatibility check) — reply drafted (per-tier gates vs RMT thresholds, call/async)
- Jason Arbon DM (free book): user SENT reply (eval vs behavioral boundary, mutation verification offer)
- Matt Graham comment SENT ("last few 9s" → mutation measures last 9s in QA)
- Rupesh DM SENT 19.09 (VerdictGate launch peer ping, no ask) — awaiting reply; commercial stays CLOSED

**Quotes bank:** 34 total (7 sections). No new adds this block.
**Articles repo:** `84a0dc4` → `da3130b` (8 commits this session).
