# Maestro vs Appium Carousel — NotebookLM Script

## Slide 1 — Cover

**Visual:** Dark background. FrontRow logo (small, top-left). Your photo bottom-left.

**Title (large, bold):** I chose Maestro over Appium for a test assignment.

**Subtitle:** Here is what I learned in 7 days on FrontRow (iOS + Android)

**Bottom:** Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

---

## Slide 2 — The Assignment

**Visual:** Skeleton UI of a mobile events app (Feed, Search, Tickets tabs). Checklist icon top-right.

**Title:** 7 days, 1 app, open tooling

**Body:**
FrontRow — live events app with auth, events feed, ticketing, billing, push notifications.

Goal: build an E2E test suite. Any open-source framework.

Deadline: 7 days.

---

## Slide 3 — Day 1: Appium

**Visual background (halftone ~15% opacity):** wdio.ios.conf.ts + login.spec.ts code (actual code from the project)

```
// wdio.ios.conf.ts — 23 lines config
export const config: Options.Testrunner = {
  ...sharedConfig,
  capabilities: [{
    platformName: 'iOS',
    'appium:automationName': 'XCUITest',
    'appium:deviceName': 'iPhone 15',
    'appium:platformVersion': '17.5',
    'appium:app': APP_PATH,
    'appium:noReset': false,
  }],
};

// login.spec.ts — imports + helpers + test
import { browser } from '@wdio/globals';
import { waitForId, tapId, typeIntoId } from './helpers';

describe('Login', () => {
  it('signs in with the demo account', async () => {
    await waitForId('screen.events');
    await browser.$('~Profile').click();
    await tapId('profile.signInButton');
    await typeIntoId('login.emailInput', 'demo@frontrow.app');
    await typeIntoId('login.passwordInput', 'demo1234');
    await tapId('profile.signInButton');
    await waitForId('profile.signOutButton');
  });
});
```

**Foreground text:**
Setup: config + capabilities + helpers + imports = 4 files before first test

First test: 4 hours

Third run: flaky — `no such element` (see log)

Even with WebdriverIO abstractions — still needs config file, helper module, import chain.

---

## Slide 4 — Day 2: Maestro

**Visual background (halftone ~15% opacity):** `smoke/launch.yaml` — 11 lines, no imports, no helpers, no config

```yaml
appId: app.frontrow.qa
---
- launchApp:
    clearState: true
- extendedWaitUntil:
    visible:
      id: 'screen.events'
    timeout: 20000
- assertVisible: 'Events'
```

```
auth/login.yaml — 32 lines, full login flow
events/browse.yaml — 55 lines, search + filter + detail + back
tickets/buy.yaml — 27 lines, runFlow + navigate + purchase
```

**Foreground text:**
brew install maestro → 90 seconds

First working test → 15 minutes

35 flows by day 7. Zero flaky.

---

## Slide 5 — Comparison Table

**Visual:** Two columns, dark background. Maestro = green accent, Appium = subtle grey

| | Appium | Maestro |
|---|---|---|
| Setup time | ~4 hours | ~10 minutes |
| First test | 4 hours | 15 minutes |
| Test syntax | Java/Python (80+ lines) | YAML (11 lines) |
| Flaky rate | ~30% (built-in) | ~0% (auto-retry) |
| iOS real device | Supported | Simulator only |
| Complex logic | Full control | YAML ceiling |

---

## Slide 6 — What Maestro CANNOT Do

**Visual:** Three cards with icons

**Card 1** | Real iOS devices — Appium still required for physical iPhone testing

**Card 2** | Complex flows — 2FA codes, conditional branching, data-driven tests push past YAML limits

**Card 3** | Enterprise device farms — Appium's BrowserStack/Sauce Labs integration is deeper

---

## Slide 7 — The 80/20 Rule

**Visual:** Horizontal bar chart, 80% green "Maestro", 20% grey "Appium"

**Title:** Use both, but differently

**Body:**
Maestro for the 80% — smoke, critical paths, CI: fast, stable, readable.

Appium for the 20% — real devices, complex interactions, platform-level edge cases.

---

## Slide 8 — CTA

**Visual:** Clean, minimal. Your photo bottom-left.

**Title:** Maestro won my test assignment. But I keep Appium in my toolbox.

**Body:**
Fast and reliable beat flexible but fragile on a 7-day deadline.

What is your mobile E2E stack?

**Hashtags:** #MobileTesting #Maestro #Appium #QA #TestAutomation

---

## Notes for AI image generation

- Slide 3 code background: use TypeScript code (wdio.conf.ts + login.spec.ts concatenated), syntax highlighting, blurred/transparent
- Slide 4 code background: use YAML code with Maestro's blue-green accent theme, blurred/transparent
- Slide 5 table: 2-column, high contrast, numbers as the hero (4h vs 10min, 80 vs 11 lines)
- Slide 6 cards: rounded rectangles, subtle shadows, icon + 1 line of text
- Slide 7 bar: 80/20 split, green/grey, clean sans-serif numbers
- Colour palette: dark navy/charcoal background (#1a1a2e or similar), accent green (#00c853 or similar), text white
- Font: sans-serif throughout
