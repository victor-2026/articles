Microsoft shipped 3 AI agents for Playwright.
🎭 One wrote 25 scenarios in 5 minutes. 
🎭 One explored but never coded. 
🔧 The third fixed 3 visual regressions — but failed at 3 data-level bugs.

Here's what the agents could and couldn't do:

🎭 Planner — explored the Claim module, documented 5 tabs, 7 search fields, 9 columns. Generated a 419-line test plan.

🎭 Generator — works via browser recording, but our tests are POM-based.

🔧 Healer — fixed 2 stale snapshots and improved 1 test layout. But 3 failures went deeper:

• Duplicate employee ID #0001 blocking saves (data corruption)
• .has-text("Admin") matching 3 rows (data quality)
• @local tests running twice in parallel (config error)

8 lines changed. Zero selector fixes.

The real Healer is you. No AI agent understands your data. Yet.

[Image: 6-comparison.png]
[Image: 6-what-i-fixed.png]

What data-level bugs has your test automation missed?

Victor Ematin · AI Quality Engineering Lead · OpenCode Go

#Playwright #TestAutomation #AITesting #ZeroBudgetQA #AIAgents
