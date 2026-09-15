# Image Generation Scenario — NotebookLM

## Image 1: Cover + Feed Image (1200×644 px) — Code Comparison

**Это одна картинка — LinkedIn Pulse Article использует Cover как Feed image.**

**Style:** Split terminal/IDE view, dark background (#0d1117 GitHub Dark)

**Layout:** Two panels, equal width.

### Left panel — APPIUM (9 lines)
Header: "Appium (WebDriverIO)" — red tint (#e94560)

```
const input = await $('~buyTicket.promoInput')
await input.waitForDisplayed({ timeout: 10000 })
await input.setValue('FRONTROW50')
const apply = await $('~buyTicket.promoApplyButton')
await apply.waitForDisplayed({ timeout: 5000 })
await apply.click()
const success = await $('~buyTicket.promoSuccess')
await success.waitForDisplayed({ timeout: 10000 })
expect(await success.isDisplayed()).toBe(true)
```

Highlight `waitForDisplayed` lines in yellow.

### Right panel — DETOX (4 lines)
Header: "Detox" — green tint (#00d4aa)

```
await element(by.id('buyTicket.promoInput')).tap()
await element(by.id('buyTicket.promoInput')).typeText('FRONTROW50\n')
await element(by.id('buyTicket.promoApplyButton')).tap()
await expect(element(by.id('buyTicket.promoSuccess'))).toBeVisible()
```

No highlights — all clean.

### Bottom caption
"9 lines · 3 explicit waits     vs     4 lines · 0 waits"
"Cost per test, not capability"

---

## Image 2: Architecture Diagram (1200×644 px) — Inline в статье

**Style:** Clean technical diagram, dark background (#1a1a2e), teal accent (#00d4aa for Detox, #e94560 for Appium)

**Layout:** Two columns side by side.

### Left column — APPIUM
Header: "Appium — HTTP Round-Trip"

Stack (top to bottom, connected by arrows):

```
Test Script        ← WDIO
    ↓ HTTP request → ← response
Appium Server
    ↓ HTTP request → ← response
WDA / UiAutomator
    ↓ HTTP request → ← response
UI Layer           ← black box
```

Bottom label: "Does not know when render completes"
Red indicator next to each connection.

### Right column — DETOX
Header: "Detox — In-Process Sync"

Stack (top to bottom, connected by arrows):

```
Test Script
    ↓
Detox              ← embedded in process
    ↓
RN Run Loop        ← idling resources
JS Dispatch Queue
Animation Loop
Network Requests
```

All layers inside a dashed box labeled "iOS Simulator Process"
Green indicator: "Synchronized — no wait guesses needed"

### Bottom bar
"39 tests | 7 specs" on left, "32 tests | 5 files" on right

---

## Image 3: Not needed — Maestro coverage исключена (сравнение 3х инструментов)

---

## Image 4: Decision Flowchart (1200×644 px) — Inline в статье

**Style:** Flowchart, same dark theme (#0d1117)

**Flow:**

```
                    ┌─────────────────────┐
                    │ Your app stack?      │
                    └──────────┬──────────┘
                               │
            ┌──────────────────┼──────────────────┐
            ▼                  ▼                  ▼
   ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
   │  100% RN        │ │  Hybrid      │ │  Not RN        │
   └────────┬───────┘ └──────┬───────┘ └───────┬────────┘
            ▼                ▼                  ▼
   ┌────────────────┐ ┌──────────────┐ ┌────────────────┐
   │ Detox          │ │ Detox +      │ │ Appium         │
   │ for most       │ │ Appium       │ │ (only option)  │
   │ screens        │ │ per screen   │ │                │
   └────────────────┘ └──────────────┘ └────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │ RN Modal?           │
                    │ Add Maestro         │
                    └─────────────────────┘
```

---

## Notes
- All images: 1200×644 px
- Font: monospace for code, sans-serif for labels
- Consistent dark theme across all images
- No emoji in images (clean technical style)
- Output as PNG
