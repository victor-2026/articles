**Format:** Pulse Article
**Series:** Mobile Testing Infrastructure — Issue #1
**Published:** 2026-07-07
**Cover:** Split screen — left MacBook (Xcode), right Windows (CMD with adb devices + emulator)
**Feed Image:** Terminal with "adbd" on Windows + iPhone sim on Mac — the two-device setup
**Hook:** "17 out of 18 tests passed. The one that failed was a testID mismatch, not the infrastructure."
---
[COVER: Split screen left=Mac with iOS simulator, right=Windows CMD showing "adb devices" with emulator and "Maestro completed"]

# I Tried to Run Mobile Tests on a Windows Machine With No GPU — 17 Out of 18 Passed

**Setup:** MacBook (iOS) + Windows 10 Pro (Android) + AMD Threadripper (no HAXM). **Three test tools:** Appium, Maestro, Playwright. **17/18 Appium tests passing, 46 Maestro flow files ready, 0 budget for infrastructure.**

Here is the exact blueprint — every command, every failure, every fix.

---

## The Problem

Mobile testing has a blind spot. You build features on a Mac, run iOS tests locally, push to CI — and then someone asks "does this work on Android?"

You have options:
1. Buy a Mac Studio with Android emulator (slow, expensive)
2. Use a cloud device farm ($200+/mo)
3. Use the Windows tower under your desk

I chose option 3. It took 8 hours and taught me more than a year of cloud testing.

---

## The Core: One 15-Line Helper That Unlocked 2 Platforms

Before infrastructure, before drivers, before CI — the first thing I fixed was the selector strategy.

Every test worked on iOS. Every test failed on Android.

Root cause: React Native's `testID` maps to `resource-id` on Android but `accessibilityIdentifier` on iOS. Appium's `~` selector maps to `content-desc` (= `accessibilityLabel`). Two different attributes, same testID.

This is the single most expensive mistake in cross-platform mobile testing — and the cheapest to fix.

```typescript
const isAndroid = browser.capabilities.platformName === 'Android'

export function byId(id: string) {
  return isAndroid
    ? $(`//*[@resource-id="${id}"]`)
    : $(`~${id}`)
}

export async function tapId(id: string) {
  await byId(id).waitForDisplayed({ timeout: 10000 })
  await byId(id).click()
}
```

[SCREENSHOT: VS Code showing helpers.ts with byId, waitForId, tapId, typeIntoId functions]

**One file. Six spec files updated. 99 direct `$('~')` calls replaced.** Not a single platform branch in any test — just `byId('login.button')` on both OS.

This helper is now the foundation of the entire Mobile Testing Infrastructure series. Every future article references it.

---

## Everything Else That Broke Along the Way

Once the selectors worked, the real problems surfaced. Here is every infrastructure issue, condensed to what matters:

**No HAXM on AMD** → 2-minute emulator boot with `-gpu auto`. Cold boot + purge stale `.qcow2` files. Physics, not a bug.

**Blank APK after install** → missing JS bundle. `expo export:embed` must run before `./gradlew assembleDebug`. 1302 modules, 178 MB, one command order fix.

**"UiAutomation not connected"** → stale uiautomator2 server APK. `adb uninstall` then `appium driver install uiautomator2@8.1.0`. Fresh emulator + fresh driver.

**Maestro driver timeout** → same root cause: stale state. Production APK + fresh uiautomator2 8.1.0 fixed it without a single config change. Launch → clear state → assert — all under 30 seconds.

**Pattern across all four:** stale state from previous failed attempts. Solution: clean slate every time.

---

## Three More That Almost Broke the Build

### 1. JS Bundle Caching Hell

Metro bundler does not rebuild the JS bundle when you expect it to. `expo export:embed` caches aggressively — even after a clean gradle build, the injected bundle may be the stale one from last week.

The fix is not obvious — Metro caches independently of Gradle:

```bash
rm -rf node_modules/.cache
npx expo export:embed --platform android --dev false
cd android && ./gradlew assembleDebug
```

The fresh bundle lands at `app/build/generated/assets/react/debug/index.android.bundle` after the build. If you need to inject it into an existing APK, use `zip -g` and re-sign (see section 3).

Lost an hour on this. It is the single most common RN/Expo issue that no setup guide mentions. If your APK installs but shows a blank screen — this is the first thing to check.

[SCREENSHOT: Terminal showing `expo export:embed` output after `rm -rf node_modules/.cache` — 1302 modules bundled]

### 2. Disabled Button Is Invisible to UiAutomator

React Native hides `disabled` Pressable components from the accessibility tree entirely. UiAutomator cannot see them — not just "cannot interact," cannot even query.

```
disabled={false}   // ❌ button invisible to Appium
disabled={condition} // ❌ invisible when condition is true
```

The fix is architectural: keep the button enabled and remove `disabled` from `accessibilityState` entirely — even `disabled: false` can trigger hiding on some RN versions:

```tsx
<Pressable
  disabled={false}
  onPress={() => { if (isDisabled) return; handleSubmit() }}
  accessibilityState={{ busy: Boolean(loading) }}
>
```

The button is always visible to UiAutomator. Tapping when disabled is a no-op.

[SCREENSHOT: images/uiautomator-hierarchy.png — UiAutomator hierarchy before fix (saveButton missing) vs after fix (visible)]

### 3. APK Signature After Zip-Inject

You modified the APK (injected a fresh bundle). Now installation fails with `INSTALL_PARSE_FAILED_NO_CERTIFICATES`.

APK signatures are tied to the zip contents. Modify any file inside → signature breaks. For debug builds the fix is straightforward:

```bash
apksigner sign --ks ~/.android/debug.keystore \
  --ks-pass pass:android --ks-key-alias androiddebugkey \
  app-debug.apk
```

`jarsigner` applies only APK Signature Scheme v1, which Android 14+ rejects. Use `apksigner` from SDK `build-tools/` — it applies v2/v3 schemes. Debug keystore password is `android`, alias is `androiddebugkey`.

[SCREENSHOT: images/install-parse-failed.png — terminal: INSTALL_PARSE_FAILED → apksigner sign → Success]

---

## Cloud vs Windows — the Real Cost

After fixing everything, I ran the numbers. Here is how this setup compares to alternatives:

| Option | Setup Time | Cost/Month | Emulator Boot | Same-Stack CI |
|--------|-----------|------------|---------------|---------------|
| Windows (AMD) | 8 hours | $0 | 2 min | ✅ Same GHA runner |
| Mac Mini | 30 min | $99+electricity | 30 sec | ❌ Separate infra |
| BrowserStack/Sauce | 10 min | $200+ | instant | ❌ Remote debug |

The Windows setup cost 8 hours once. BrowserStack costs $200+ every month. After 3 months, the Windows machine has paid for itself in savings — and I am not sharing devices with 50 other engineers.

---

## The Result

[SCREENSHOT: WDIO terminal output showing "17 passing" in green]

| Tool | Tests | Pass | Run Time | Breakdown |
|------|-------|------|----------|-----------|
| Appium (Android) | 18 | 17 (94%) | ~12 min | 2 min boot + 3 min APK + 7 min suite |
| Maestro (Android) | 3 smoke | 3 (100%) | ~30 s | included above |
| Appium (iOS) | 18 | 17 (94%) | ~8 min | native, no boot overhead |
| Maestro (iOS) | 46 | 46 (100%) | ~5 min | flattened YAML, fast assertions |

The one failure: `settings.aboutRow` — an iOS-only testID that does not exist on Android. Not infrastructure. Test design.

**$0 infrastructure cost.** A Windows machine that was already there, running test infrastructure during the workday.

**One `byId()` helper.** Six spec files. 99 selectors replaced. Two platforms.

---

## The Catch

You need someone who can debug ADB over SSH, read a uiautomator hierarchy dump, write a 15-line cross-platform helper, and tolerate a 2-minute emulator boot.

If that person is you — the setup is free.

If you are paying a cloud provider $200/month because "Mac mini + Windows VM is too complex" — show them this article.

---

## One More Thing

The Maestro smoke suite runs the same YAML files on both platforms. No platform branches. No `if ios` blocks. The flows use `id:` selectors, and the `byId()` helper in Appium mirrors the same logic.

[SCREENSHOT: images/maestro-tree.png — Flattened directory tree of tests/maestro/ showing auth, billing, events, smoke, tickets — 46 files]

That is the real win. Not the 17 passing tests. The portable test layer that works on both OS with zero platform-specific code.

---

## Call to Action

Are you running Android tests on a non-Mac machine? What is your biggest bottleneck — infrastructure or test reliability?

I document every setup decision in my GitHub repo: [github.com/victor-2026/Mobile_1](https://github.com/victor-2026/Mobile_1)

Victor Ematin · QA Automation Engineer · Windows + Mac = full mobile coverage · OpenCode Go
