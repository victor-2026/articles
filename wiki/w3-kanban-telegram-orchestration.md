# W3: Kanban → Telegram → OpenCode orchestration

## Overview

Архитектура, при которой локальные kanban-файлы служат source of truth для очереди задач. Telegram-бот (@Victor435_bot) автоматически отслеживает изменения и диспатчит задачи в OpenCode без ручного вмешательства.

```
kanban/*.md ──(poll 60s)──> poll_kanban_sync()
               thread         │
                     dispatch_state.json
                              │
                    tg_send() ──> TG bot ──> user
                              │
                    subprocess.run() ──> opencode run ──> task output
```

## Компоненты

### 1. Source of truth: kanban/*.md

6 файлов в `/Users/victor/Projects/Articles/kanban/`:

| Файл | Проект |
|------|--------|
| `bot.md` | Telegram Bot (@Victor435_bot) |
| `notion.md` | Notion Integration |
| `articles.md` | Articles & LinkedIn |
| `orangehrm.md` | OrangeHRM Demo |
| `career.md` | Career Pipeline |
| `buzzhive.md` | Buzzhive (qa-automation-sandbox) |

Каждый файл имеет секции: `## Backlog`, `## This Iteration`, `## In Progress`, `## Done`.

Бот отслеживает только секцию `## In Progress`.

### 2. Poller: poll_kanban_sync()

- Запускается в отдельном daemon-треде при старте бота
- Первые 5 секунд — warmup
- Затем цикл с интервалом 60 секунд

Логика первого запуска (tracking mode):
- При первом запуске (dispatch_state.json не существовал) — все текущие In Progress задачи **трекаются**, но не диспатчатся
- После первого цикла tracking_mode отключается
- При последующих циклах новые In Progress задачи диспатчатся

### 3. State: dispatch_state.json

`~/bot/dispatch_state.json` — JSON-файл, где хранится статус каждой задачи:

```json
{
  "articles::Write phase 4 post": {"status": "dispatched", "time": "2026-06-17 21:27:00", "duration": 5.43, "result": "..."},
  "bot::Fix polling timeout": {"status": "failed", "time": "2026-06-17 21:28:00", "duration": 3.1, "result": "Session not found"}
}
```

Ключ: `{project}::{task_description}`.

Статусы:
- `tracked` — обнаружена при первом запуске, не диспатчилась
- `pending` — отправлена на выполнение
- `dispatched` — успешно выполнена
- `failed` — ошибка выполнения

### 4. Notifier: tg_send()

- HTTP POST на `api.telegram.org/bot{token}/sendMessage`
- Использует `urllib.request` (синхронный, без asyncio)
- SSL-сертификаты через certifi
- Markdown-экранирование через `tg_escape()` (экранирует `_`, `*`, `[`, `` ` ``)

### 5. Executor: OpenCode subprocess

- `subprocess.run([opencode, "run", "--dangerously-skip-permissions", "--model", model, prompt])`
- Timeout: 180 секунд
- Промпт: `"Project: {project}. Task: {task_desc}. Execute this task."`

## Поток выполнения

```
1. Пользователь редактирует kanban/*.md
   → Добавляет задачу в ## In Progress

2. Бот (через 0-60 сек):
   a. Читает все kanban/*.md
   b. Сравнивает In Progress с dispatch_state.json
   c. Находит новую задачу (нет в state)

3. Бот отправляет в Telegram:
   "🔄 Auto-dispatch: project → task"

4. Бот запускает OpenCode:
   opencode run --model default "Project: {project}. Task: {task}. Execute this task."

5. OpenCode выполняет задачу

6. Бот отправляет результат в Telegram:
   "✅ project → task\n<output>"

7. dispatch_state.json обновляется
```

## Как пользоваться

### Добавить задачу в очередь
1. Открыть нужный `kanban/*.md`
2. Переместить задачу в секцию `## In Progress`
3. Бот подхватит в течение 60 секунд

### Запустить вручную через Telegram
```
/task bot fix polling timeout run
/task bot fix polling timeout --agent qa run
```

### Посмотреть статус всех задач
```
/task list
```

### Посмотреть задачи проекта
```
/task bot
/task bot polling
```

### Отключить автодиспатч для конкретной задачи
Добавить задачу в `dispatch_state.json` со статусом `tracked` — бот пропустит.

## Граничные случаи

| Сценарий | Поведение |
|----------|-----------|
| dispatch_state.json не существует | Первый цикл трекает всё, второй — диспатчит |
| dispatch_state.json существует | Бот сразу в режиме диспатча |
| Задача уже в In Progress при рестарте | Не диспатчится повторно (уже в state) |
| OpenCode не запущен (нет сессии) | Статус `failed`, результат "Session not found" |
| Telegram API недоступен | Лог `TG send failed`, диспатч продолжается |
| Несколько задач в In Progress | Диспатчатся последовательно, по одной за цикл |

## Код

Основные функции в `/Users/victor/bot/bot.py`:

| Функция | Строка | Назначение |
|---------|--------|------------|
| `read_kanban()` | ~390 | Читает все kanban/*.md |
| `cmd_task()` | ~409 | Обработчик /task (ручной диспатч) |
| `poll_kanban_sync()` | ~570 | Фоновый poll-цикл |
| `tg_send()` | ~560 | Отправка сообщения в Telegram |
| `tg_escape()` | ~557 | Экранирование Markdown |
| `start_poll()` | ~630 | Запуск poll-треда |

## Версии

| Версия | Дата | Изменения |
|--------|------|-----------|
| 1.0 | 2026-06-17 | Первая реализация: threading + urllib + certifi + экранирование |
