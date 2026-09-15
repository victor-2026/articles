# Maestro vs Appium: The Test Assignment That Changed My Mobile Testing Stack

**TL;DR:** I had 7 days to build a mobile E2E suite for FrontRow (iOS/Android). I started with Appium — and switched to Maestro by day two. Here is why, and where each tool belongs in your stack.

## The assignment

FrontRow is a live events app: events feed, search, ticketing, auth, push notifications, billing. Standard mobile stack, standard E2E requirements.

I had one week. The brief was open tooling — any open-source framework.

## Day 1: Appium

I have used Appium before. I know its power. I also know its setup cost.

Getting Appium running locally:
- Node.js version dance
- Appium server install (npm -g appium)
- UiAutomator2 driver + XCUITest driver
- Android SDK paths, Xcode CLT
- Capabilities JSON boilerplate
- Inspector config for element discovery

Half a day later I had a running server. Four hours total to write my first working test. That test broke on the third run — timing issue, no built-in retry.

**22 lines of Java. One assertion. Already flaky.**

## Day 2: Maestro

I had heard about Maestro but never tried it. The claim: "brew install maestro" and you are done.

I ran brew install maestro. It took 90 seconds.

```yaml
# smoke/launch.yaml — 11 lines
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

My first test was running in 15 minutes. It did not flake. Not once.

Compare the same flow in Appium (Java):

```java
// ~80 lines of boilerplate
DesiredCapabilities caps = new DesiredCapabilities();
caps.setCapability("platformName", "Android");
caps.setCapability("deviceName", "emulator-5554");
caps.setCapability("app", "/path/to/app.apk");
caps.setCapability("automationName", "UiAutomator2");
URL serverUrl = new URL("http://localhost:4723");
AndroidDriver driver = new AndroidDriver(serverUrl, caps);
WebDriverWait wait = new WebDriverWait(driver, Duration.ofSeconds(20));
wait.until(ExpectedConditions.presenceOfElementLocated(
    MobileBy.id("screen.events")));
driver.findElement(MobileBy.id("screen.events")).isDisplayed();
```

Four hours of setup, 80 lines of code, still flaky. Or 15 minutes, 11 lines, zero flaky.

## 35 tests in 7 days

By the end of the week I had 35 Maestro flows across 8 modules:

| Module | Flows | What it covers |
|--------|-------|----------------|
| smoke | 3 | Launch, onboarding skip, onboarding complete |
| auth | 7 | Login, register, forgot password, recovery deeplinks, profile edit, language switch |
| events | 8 | Browse, search, genre filter, sort, pagination, reviews, favorites, follow artist |
| tickets | 4 | Buy, tier select, cancel, transfer |
| billing | 3 | Payment methods CRUD, buy success, buy decline |
| native | 1 | Native device interaction demo |
| debug | 1 | Failure trigger |
| capabilities | 1 | Haptic feedback |

Zero flaky runs. Each flow is self-contained: `clearState: true` on launch, no shared state.

## The RN `<Modal>` blind spot

FrontRow's cancel-ticket dialog uses React Native `<Modal>` — it renders in a separate UIWindow outside the main view hierarchy. Neither Appium (XCUITest) nor Detox can find elements inside it. Test automation stops at the overlay.

Maestro handles it in one line:

```yaml
- tapOn:
    id: ticketDetail.cancelConfirmYes
```

This was the moment I realised Maestro is not just "a simpler YAML wrapper." It operates at the accessibility service layer, which sees every window — not just the main view hierarchy. **Detox and Appium both have a `<Modal>` blind spot. Maestro does not.**

## Where Maestro works

- **Smoke tests** that must never flake
- **Critical path flows** (auth, purchase, checkout)
- **CI pipelines** — one binary, one YAML file, no build step
- **Teams without Java/Python in QA** — YAML is readable by anyone
- **Flutter and React Native** — accessibility layer works out of the box

## Where Maestro does not work

- **Real iOS devices** — only simulator. If you need physical iPhone testing, you still need Appium.
- **Complex logic** — YAML does not do loops well, conditional branching gets messy, 2FA code extraction is painful
- **Custom gestures** beyond tap/swipe/scroll — Appium's TouchAction gives more control
- **Enterprise scale** — Appium's ecosystem (BrowserStack, Sauce Labs, LambdaTest) is deeper

## The honest answer

You probably need both.

Maestro for the 80% — fast, stable, readable E2E flows that cover your core user journeys.

Appium for the 20% — real devices, complex interactions, edge cases that need platform-level access.

**Maestro won my test assignment because "fast and reliable" beat "flexible but fragile" on a 7-day deadline.** But I keep Appium in my toolbox for when the app pushes past what YAML can express.

---

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

#MobileTesting #Maestro #Appium #QA #TestAutomation #FrontRow
