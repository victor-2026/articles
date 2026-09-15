**Format:** Pulse Article
**Series:** Mobile Testing Tools
**Cover:** Terminal split — 11 lines Appium vs 4 lines Detox (1200×644)
**Hook:** I tested the same RN app with Appium (39 tests) and Detox (32 tests). Appium covers 36% of test IDs, Detox covers 35%. Maestro covers 80%. The gap is not capability — it is architecture. Every Appium test needs explicit waits. Detox does not wait. It synchronizes.
---

# I Tested the Same RN App with Appium and Detox — the Gap Is Architecture

The FrontRow project runs both Appium and Detox test suites. Not because we planned it — because each framework answers a different architectural question.

Appium arrived first. 39 tests across 7 spec files — promo codes, stepper, edit profile, inbox, my-tickets, event detail, auth. Every test needs explicit `waitForDisplayed({ timeout })` calls. Not because the app is slow. Because Appium does not know when the app has finished rendering — it can only check if an element is visible *right now*.

Detox came later, for the same screens. 32 tests covering the same flows. The same app, the same testIDs, the same simulator. **Zero timing-related failures**. Detox does not guess when rendering is done. It monitors the app's run loop and knows when the JS thread is idle.

[SCREENSHOT: side-by-side terminal — Appium flaky test vs Detox consistent pass]

The reason is architectural. And it is the only thing that matters when choosing between these two frameworks.

## The architecture gap

Appium sends HTTP commands through WebDriver to XCUITest (iOS) or UiAutomator (Android). The chain looks like this:

```
Test script → WebDriver → Appium Server → WDA/UI Automator → UI layer
```

Every command is a network round-trip. The framework does not know when your app has finished rendering. It only knows whether an element is visible *right now* — which is why every Appium test is littered with `waitForDisplayed({ timeout })` calls. You are guessing how long the app needs.

Detox 20.x takes a different route:

```
Test script → Detox → XCUITest → Idling Resources → App Run Loop
```

It uses XCUITest to inject itself into the iOS simulator process, then monitors the app's run loop and JavaScript dispatch queue directly. It does not guess when rendering is done. Detox knows when the JS thread is idle, when animations have settled, when network requests have completed. **It does not wait. It synchronizes.**

[SCREENSHOT: architecture comparison diagram — two data flows]

## The same test, two frameworks

Here is a promo-code test from the FrontRow suite. Appium version:

```typescript
// Appium (WebDriverIO)
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

Detox version:

```javascript
// Detox
await element(by.id('buyTicket.promoInput')).tap()
await element(by.id('buyTicket.promoInput')).typeText('FRONTROW50\n')
await element(by.id('buyTicket.promoApplyButton')).tap()
await expect(element(by.id('buyTicket.promoSuccess'))).toBeVisible()
```

The difference is not syntax. The difference is that a third of the Appium test is timeout guesses — 3 explicit waits in 9 lines. The Detox version has zero — 4 lines.

For auth flows (sign-in, forgot password, OTP), the code gap is the same — Appium needs `waitForDisplayed` before every interaction, Detox does not — but both produce stable, repeatable results.

## The stability numbers

The numbers tell a story about architecture, not capability:

[SCREENSHOT: coverage comparison table — Appium 36% (56/154 IDs), Detox 35% (54/154), Maestro 80% (124/154). 134 unique IDs covered across all three frameworks.]

On this project (iOS 26.3, XCUITest 11.0.0, RN 0.81.5), **both frameworks achieve consistent pass rates on the screens they target**. The difference is not failure rate — it is **cost per test**.

The Appium promo-code test above is 9 lines with 3 explicit `waitForDisplayed` calls. The Detox version is 4 lines with zero. Across 39 tests, that pattern multiplies.

Measured on Apple Silicon M4, frontrow.spec.ts (20 tests) completes in ~12 minutes — about 36 seconds per test including setup. Detox per-test time is comparable (~42s from an earlier 12-test run). The duration is not the differentiator.

What differs is maintenance: when animations or API response times change, Appium tests need timeout adjustments. Detox tests do not — they synchronize at the run-loop level.

The text-input gap often cited against Appium has a workaround: W3C keyDown/keyUp actions per character, with keyboard dismissed by tapping a safe element. After applying this pattern, Appium promo-code tests pass consistently. The fix is verbose but reliable — a pattern, not a blocker.

## Where Detox wins

Detox removes the most expensive category of flakiness — timing. On every RN screen, it synchronizes with the JS thread automatically. No `waitForDisplayed`, no timeout guesses, no "let me add 2 more seconds and try again." Auth flows (login, forgot password, OTP) are a single `expect().toBeVisible()` away from passing.

The cost of this is that Detox must occupy the main thread. In return, it gives you deterministic tests — the same output every run, regardless of machine load.

## Where Detox breaks down

Detox only works for React Native. That is its superpower and its prison.

FrontRow's native demo screen is a hand-rolled UIKit UIViewController — built as a tech demo for XCUITest training, not the product itself. For native screens like this, Detox's synchronization does not apply — it cannot hook into the native rendering loop. You fall back to `waitFor().toBeVisible().withTimeout(30000)` — exactly the same pattern you would use in Appium.

All product screens — event detail, buy ticket, ticket detail — are React Native and work with Detox's sync. The native demo exists only for training purposes.

Appium, by contrast, does not care what your app is made of. React Native, SwiftUI, UIKit, WebView — it goes through the same accessibility layer every time. The abstraction is universal but shallow.

## Where both break down

There is a subtler limitation that affects **both** frameworks: React Native `<Modal>` components render in a separate UIWindow that neither Detox nor Appium (XCUITest) can query. Cancel confirmations, bottom sheets, or any overlay using RN Modal are invisible to both. On FrontRow, the cancel-ticket confirmation dialog uses RN Modal — Maestro handled it in one line; Detox and Appium could not find it at all.

## Hardware matters

Appium's WebDriverAgent compiles from source the first time you run it on a new simulator OS version. On an Intel Mac, the build takes ~10 minutes. On Apple Silicon, it is significantly faster. Detox requires no WDA build step — it launches in seconds on any architecture.

If your team runs Intel Macs, the initial WDA setup is a one-time cost per simulator version. It is manageable but worth planning around.

## Which one should you use

The answer is not "Detox is better." The answer depends on your app's architecture.

- **Your app is 100% React Native?** Detox removes the most expensive category of flakiness. Use it for most screens.
- **Your app uses RN `<Modal>`?** Add Maestro for those flows. Detox and Appium both miss overlays in a separate UIWindow — Maestro handles them natively.
- **Your app is hybrid (RN + native)?** Both. Detox for JS-driven screens, Appium for native views. They share the same testID contract — no duplication needed.
- **Your app needs the widest coverage per test written?** Maestro covered 80% of test IDs on this project — the highest of any framework. YAML flows are faster to write than any code-based framework.
- **Your app is not React Native?** Appium. Detox will not help you.

The FrontRow project runs both. The choice was not ideological. Each test goes to the framework that fits the screen it tests.

[SCREENSHOT: decision flowchart — pure RN → Detox, hybrid → both, native → Appium]

---

The WebDriver abstraction is not bad. It is seventeen years old, battle-tested, and works on every platform ever made. But for React Native, it is the wrong layer. Detox drops one level deeper — into the runtime — and that one level makes all the difference.

Your app stack should drive your test stack. Not the other way.

What is your mobile stack — pure RN, hybrid, or native? Your answer determines the test framework, not the other way around.

---

*Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go*

*#ReactNative #MobileTesting #Detox #Appium #TestAutomation*
