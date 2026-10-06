# Slate — короткие тематические заметки (формат: 1 идея + 1 кейс + 1 цифра)

 pivot от heavy-статей (решение owner, 02.10). Порядок — предложение W4, слоты уточняются.

## 1. Kaggle L2: честное бесплатное железо [DRAFT v1 готов]
- Идея: бесплатное железо + честный отрицательный результат.
- Кейс: L2-тюн complete, bench locked → FAIL ±3, трек parked explicitly.
- Цифра: $0 / 6.9470 / ±3.
- Файл: `Kaggle-L2-zero-dollar-honest-fail-DRAFT.md` (~550 слов). W3 цифры + W2 смыслы вшиты. Slot TBD. Next: W3 signe-off цифр → W1 → R1.
- Закрыто: terms-фрейминг (приватность на shared-инфре одной строкой).

## 2. RMT Note 1: Batch #2 + crash (кандидат на Пн 05.10)
- Идея: сьют работает — 22 killed, zero inconclusive.
- Кейс: tooltip exit -9/632s, третий ханг подряд.
- Цифра: 95 mutants / 98 records.
- Статус: факты CERTIFIED, reviews W1+W2+W3 closed. Ждёт решения owner (b-распил).

## 3. RMT Note 2: лимит, который мы не опубликовали
- Идея: unpublished honesty doesn't count.
- Кейс: Mapping Limit таблица (QAEverest AND vs наш band).
- Цифра: band 5% vs absolute cap.
- Статус: §6 W1 confirm. Ждёт b-решения.

## 4. RMT Note 3: где живут seeded evidence
- Идея: gate, not lane (тезис W1 e3f4943 готов).
- Кейс: четыре мира аутсайдеров (governance/commerce/enterprise/regulated).
- Цифра: не нужна — тезис сам цифра.
- Статус: §7 W1 confirm. Ждёт b-решения.

## 5. Leo-RMT good: где использовали + что хорошего [W2 DELIVERED eadb249, BLOCKED на 3 пунктах]
- Идея: метод как щедрость (поделились, не захомячили).
- RMT абзацем (W2 b330adb, standalone, цитировать как есть; W1 APPROVED b78f5fc — атрибуция Лео, юниты с подписью, слои не смешаны): Reverse Mutation Testing mutates test verifications, not app code: seed a broken assertion (e.g. expect(x).not.toBe(y) where y holds) and check the suite goes red — surviving mutants expose weak verifications, not app defects. It differs from classic mutation testing in seeding direction only (verification vs system); the verdict machinery (per-tier gates, evidence packs) is shared. Formulation to cite: Leonardo Lanni ("MT challenges the application, RMT challenges the test"). Our engine (rmt 0.1.0, deterministic, 2 operators + chain-unwrap + NO-OP guard + stamps): 95 seeded mutants across 98 run-records (OpenClaw batches #1–2), 91.4% kill on assertions vs 40% on behavioral app mutants (different layers, never blended).
- Где использовали (наша сторона): OpenClaw #1 (58) + #2 (24); E1–E10 gold = RMT-выходы; B2 как в 29-й.
- Что хорошего (только абсолюты, БЕЗ MT-сравнений — контрольного MT-прогона не было): 53/58 + 1+2+2 (S4/S5 genuine), batch#2 22 + resolved, guards из измеренных гэпов.
- Цифра: наши — репост 182/3/1 (02.10); Pulse 29-й — у Leonardo.
- BLOCKERS (драфт без них = риск): (a) сторона Лео (его кейсы + цитата) — outreach/сам Лео; (b) нейминг OpenClaw — НОВОЕ решение W1/owner (default closed: в 29-й SUT анонимизирован); (c) consent ping отправлен? (драфт W1 готов, отправка за owner).
- Дедлайн фактуры: Ср 07.10 (слот заметки 08.10). ДРАФТ v1 готов (~490 слов + Perplexity-правки) + фид-пост (вариант A) + обложка v2 (концепт #1). Reviews: W3/W1/W2 closed ✅. CONSENT PING SENT 03.10 — awaiting yes (публикация BLOCKED до yes). Осталось: метрики 29-й (опц.), R1.

## 6. FlowScout: итерации → методология → 0.6
- Идея: тул растёт через seeded controls.
- Кейс: 3 замечания приняты, Volume VIII, заход на методологию с нашим разделом.
- Цифра: TBD (v0.6.2 multi-actor?).
- Статус: замысел, детали у W1.

## 7. qa-cube: первый продукт без ошибок
- Идея: похвала (редкий жанр, работает на отношения).
- Кейс: zero-bug + документация + сайт + оформление.
- Цифра: 0 defects (careful: инфраструктуру тестировали, не генерацию — честная рамка из 30-й).
- Статус: замысел, consent Вадима на имя есть (24.09).

## 8. Jev: аналоги + планы (night race уже описан в 30-й)
- Идея: что дальше после первого пилота.
- Кейс: Stenbom 72/150? аналоги судьи (цитата уже в банке).
- Цифра: TBD.
- Статус: замысел.

## 9. Salvage: testRigor + OpenClaw — найти угол в «скучных»
- Идея: TBD (угол не найден — главный риск слейта).
- Кейс: testRigor-пилот (M1-M4), OpenClaw-инвентарь.
- Цифра: TBD.
- Статус: нужен угол, иначе дроп.

## 10–12. Углы от W5 (фактура готова, в вики за неделю) — кандидаты после слейта 1–9
- A «Зелёный врёт системно»: 5/5 green при дубликате (наш) + 91% PITest с дырами 500/204 (Бас) + green check на выдуманном телефоне (Данил) + кворум vs self-rating (Грётц). Тезис: зелёный без seeded proof — декор.
- B «Судью тоже надо ломать»: Pretext бьёт LLM-судью 97%/77% + AgentDojo (judge hijacking) + drift 0.25→1.0 (Данил) + 8/100 при excellent (Aston) + StarSkirmish (Astra читерит проигрыш: Stardust вместо своей игры — graded-on-winning → gamed-winning, quotes в банке 05.10). Тезис: seeded breaks для судей. Помечен W1 (b480891): обогатить нашими D-данными судьи позже (2 галлюцинации + слепота — exhibit когда созреет).
- C «Агент с правами»: 48K junction-инцидент + OpenClaw/Gmail + HF-swarm (permission boundaries, abort authority) + НАШ ПОБЕГ (лучший документированный экспонат серии: лог + промпт + скрин + дыра + фикс — evidence-ссылки из фикс-пакета TBD). Самый виральный, самый лёгкий. (W1 ee3a324)
