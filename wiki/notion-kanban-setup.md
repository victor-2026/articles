# Настройка Kanban в Notion

## Структура

Создай **5 database pages** в корне Notion (или в папке Projects):

### 1. OrangeHRM
**Свойства:**
- Name (title) — задача
- Status (select): Backlog, This Iteration, In Progress, Done, Cancelled
- Priority (select): P0, P1, P2
- Project (select): OrangeHRM
- Tags (multi-select): POM, Spec, Infra, Content, Bug

**View:** Kanban by Status

### 2. Buzzhive / qa-automation-sandbox
**Свойства:** те же + URL (text)

**View:** Kanban by Status

### 3. Articles & LinkedIn
**Свойства:** те же + Format (select: Post, Article, Carousel), Published (date)

**View:** Kanban by Status

### 4. Career
**Свойства:** те же + Company (text)

**View:** Kanban by Status

### 5. Telegram Bot
**Свойства:** те же

**View:** Kanban by Status

---

## Linked Database (опционально)

Создай **главную доску** — Linked database ко всем 5 проектам, сгруппированную по Project. Один экран видит всё.

---

## Резервная копия

Раз в неделю (перед Sunday ritual) копируй Done → в `Articles/kanban/*.md` или просто проверяй что AI актуализировал .md файлы.

---

## Если Notion закончится

Перенос в Obsidian:
1. Установи плагин Kanban
2. Конвертируй .md в формат Obsidian Kanban
3. Теряешь: drag-and-drop, фильтры, коллаборацию
4. Получаешь: локальные файлы, без привязки к вендору
