# Maestro vs Appium: feed post

I had 7 days to build a mobile E2E suite for 📱FrontRow (iOS + Android). Open tooling.

Day 1: Appium. Half a day of setup — Node version dance, XCUITest driver, SDK paths, capabilities JSON. Four hours to first working test. Third run — no such element. The test found nothing. Twice.

Day 2: Maestro. brew install maestro. One binary. 90 seconds. First flow running in 15 minutes. 35 flows by day 7. Zero flaky.

The numbers:

Appium: 4h setup, 4h to first test, ~30% flaky, 80+ lines of code
Maestro: 10min setup, 15min to first test, 0% flaky, 11 lines of YAML 

Four hours of setup, 80 lines of code, still flaky. Or 15 minutes, 11 lines, zero flaky.

Maestro won the sprint. But I keep Appium for real iOS devices and complex flows.  
  
Plus: RN <Modal> dialogs — invisible to Appium. Maestro sees them.

What is your mobile E2E stack?

---

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go

#MobileTesting #Maestro #Appium #QA #TestAutomation
