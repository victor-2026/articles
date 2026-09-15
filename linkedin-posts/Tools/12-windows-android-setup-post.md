I spent 8 hours setting up Appium + Maestro on a Windows machine with an AMD CPU that officially does not support Android virtualization.

17 out of 18 Android tests passed.

The most expensive mistake was not the emulator — it was a selector strategy. React Native's testID maps to different attributes on iOS and Android. One 15-line `byId()` helper fixed 99 selector calls across 6 spec files.

Everything else was stale state:

◦ No HAXM → `-gpu auto`, 2-min boot (physics, not a bug)
◦ Blank APK → missing JS bundle, one command order fix
◦ "UiAutomation not connected" → fresh uiautomator2 driver
◦ Maestro timeout → same root cause, no config change

The real comparison: 8 hours setup, $0/month — vs — BrowserStack at $200+/month.

Full breakdown in the article.

#TestAutomation #MobileTesting #Appium #Maestro #ZeroBudgetQA

Victor Ematin · QA Automation Engineer · $0 infrastructure budget · OpenCode Go
