# VLM vs Blind AI Agents — Experiment Data

**Дата:** 2026-07-13
**Модель:** Nemotron 3 Nano Omni (nvidia/nemotron-3-nano-omni-30b-a3b-reasoning:free)
**Приложение:** OrangeHRM 5.8.1 (Docker)
**Стоимость:** $0 (free tier OpenRouter)

## Методология

- 6 скриншотов из `e2e/visual/snapshots/visual/`
- Каждый отправлен в VLM как base64 PNG
- Вопрос: "List ALL visible UI elements" + "Write Playwright locators for key elements"
- Результаты сверены с реальным DOM и существующими тестами

## Результаты

### 1. Login (login-visual.png)
- Heading: "Login"
- Username input (label: "Username")
- Password input (label: "Password")
- Login button
- Forgot your password? link
- OrangeHRM logo
- Footer: OrangeHRM OS 5.8.1
- **Итого: 7/7**

### 2. Maintenance Password (maintenance-password-visual.png)
- Heading: "Administrator Access"
- Instructional text
- Username: "Admin" (disabled)
- Password input (empty)
- Cancel button
- Confirm button
- Footer + copyright
- **Итого: 8/8**
- **Selectors: 4/4 ARIA correct**

### 3. Admin Users (admin-users-visual.png)
- Search: Username, User Role dropdown, Employee Name, Status dropdown
- Table: Username, User Role, Employee Name, Status, Actions
- Buttons: Reset, Search, + Add
- Row actions: Trash, Pencil
- Pagination: (28) Records Found
- **Итого: 10+/10+**

### 4. Dashboard (dashboard-visual.png)
- 12 sidebar nav links (Dashboard highlighted)
- Top bar: Upgrade button, Admin User dropdown
- Time at Work card: "Not Punched In", "0h 0m Today", Mon-Sun labels
- Quick Launch card: "Not Available"
- Employee Distribution by Sub Unit card: "100.0%", "Unassigned"
- My Actions card: "No Pending Actions to Perform"
- Buzz Latest Posts: 3 posts (author + timestamp + content)
- Employee Distribution by Location card: "100.0%", "Unassigned"
- Footer
- **Итого: 35+/35+**

### 5. Claim Assign (claim-assign-visual.png)
- 7 tabs (Configuration, Submit, My Claims, Employee Claims active, Assign Claim)
- 7 filter fields (Employee Name, Reference Id, Event Name, Status, From Date, To Date, Include)
- Reset + Search buttons
- + Assign Claim button
- Table: Reference Id, Employee Name, Event Name, Description, Currency, Submitted Date, Status, Amount, Actions
- View Details action buttons
- (87) Records Found
- **Итого: 40+/40+**

### 6. Buzz Feed (buzz-feed-visual.png)
- 10 posts, each with author "Admin User", timestamp "24-06-2026 03:0X AM", content "Load test post 178225968xxxx"
- **Итого: 10/10 (dynamic content read correctly)**

## Сводка

| Страница | Элементов | Найдено | Пропущено | Галлюцинации |
|----------|-----------|---------|-----------|--------------|
| Login | 7 | 7 | 0 | 0 |
| Maintenance | 8 | 8 | 0 | 0 |
| Admin Users | 10+ | 10+ | 0 | 0 |
| Dashboard | 35+ | 35+ | 0 | 0 |
| Claim Assign | 40+ | 40+ | 0 | 0 |
| Buzz Feed | 10 | 10 | 0 | 0 |
| **Total** | **~110** | **110** | **0** | **0** |

**Accuracy: 100%**
**Correct ARIA selectors: 4/4**
**Стоимость: $0**

## Сравнение с Aider/Devin (тот же экран maintenance)

| Элемент | VLM | Aider | Devin |
|---------|-----|-------|-------|
| Heading | `getByRole('heading', { name: 'Administrator Access' })` ✅ | `h6:has-text(...)` ⚠️ fragile | `h6` ⚠️ strict mode |
| Password | `getByRole('textbox', { name: 'Password' })` ✅ | `input[name="password"]` ⚠️ fragile | `input[type="password"]` ⚠️ fragile |
| Confirm | `getByRole('button', { name: 'Confirm' })` ✅ | `button:has-text(...), button[type="submit"]` ⚠️ fragile | `button[type="submit"]` ⚠️ fragile |
| Cancel | `getByRole('button', { name: 'Cancel' })` ✅ | not generated ❌ | not generated ❌ |
