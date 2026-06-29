# Playwright Test Agents — Implementation Tasks

## Project: Playwright Agents

### PWA-001: Install + init agents
Description: Run `npx playwright init-agents --loop=opencode` in qa-automation-sandbox. Verify agent definitions created in `.github/`. Regenerate after Playwright update.
Priority: P0
Tags: #setup #opencode

### PWA-002: Pilot Planner → Generator на OrangeHRM
Description: Run Planner на одном модуле (Login → Dashboard flow). Проверить качество .md плана. Запустить Generator. Сравнить с рукописными тестами.
Priority: P1
Tags: #pilot #orangehrm

### PWA-003: Healer experiment
Description: Взять рабочий тест, intentional поломать locator. Запустить Healer. Оценить: находит ли элемент, чинит ли, сколько итераций.
Priority: P1
Tags: #pilot #healer

### PWA-004: Seed test integration
Description: Написать seed.spec.ts для OrangeHRM — авторизация, базовые фикстуры. Проверить что Planner использует контекст из seed для навигации по залогиненным страницам.
Priority: P1
Tags: #orangehrm #seed

### PWA-005: Autonoma vs Playwright Agents — comparison
Description: Один модуль (Admin → Add User) прогнать через оба пайплайна. Сравнить: время, качество тестов, количество правок, процент проходящих.
Priority: P2
Tags: #comparison #autonoma

### PWA-006: CI/CD investigation
Description: Могут ли Playwright Agents работать в CI/CD (без IDE)? Проверить: запуск Planner через CLI, запуск Generator, запуск Healer. Документировать ограничения.
Priority: P2
Tags: #cicd #research

### PWA-007: Combined pipeline: Autonoma seed → Playwright Planner/Generator
Description: Autonoma Environment Factory генерирует данные → seed test → Playwright Planner → Generator → Healer. Протестировать полный конвейер.
Priority: P2
Tags: #integration #pipeline

### PWA-008: Документация + AGENTS.md
Description: Обновить AGENTS.md в sandbox и OrangeHRM — добавить секцию Playwright Test Agents, команды init, как запускать.
Priority: P2
Tags: #docs

### PWA-010: Quality Gates automation
Description: Gate 6 conditions (Scope, Data, State, Run, Evidence, Review) — implement as pre-commit CI check or PR checklist. Create check script that validates trace exists, CI passed, test maps to risk.
Priority: P2
Tags: #qa-gates #cicd

### PWA-009: Mutation tests comparison
Description: Сгенерировать mutation-тесты через Playwright Generator (из Mutation test plan). Сравнить с рукописными mutation тестами (34/34 pass). Оценить покрытие мутаций.
Priority: P2
Tags: #mutation #comparison

---

## Quick Start

```bash
# init agents
cd qa-automation-sandbox
npx playwright init-agents --loop=opencode

# planner
# В OpenCode загрузить skill Playwright Planner (появится в .github/)
# → task: "Generate a plan for OrangeHRM Admin module"

# generator
# → task: "Generate tests from specs/admin.md"

# healer
# → task: "Heal tests/tests/admin/add-user-failing.spec.ts"
```
