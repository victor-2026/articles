I gave two AI agents the same testing prompt. One had 2 days of context. The other had 40 sessions.

The difference wasn't just in test count (5 vs 49).

It was in what they noticed — and what both missed.

Antigravity (unknown model, $0) spotted a duplicate nginx config that had been there for weeks. Then its trial expired and the code vanished.

OpenCode Go (gpt-4o-mini, $10 flat) built an entire test infrastructure — client.go, helpers.go, race conditions on goroutines. But it never looked at the Docker config.

And both missed the real bug: **admni123**.

I had typed the wrong password. Antigravity used it verbatim. The test passed because a 307 redirect intercepted before the 401. Neither agent flagged it.

Full breakdown in the article — what each produced, what broke, and why I now run two AI tools on every project.

Victor Ematin · QA Automation Engineer · $0 budget · OpenCode Go

#TestAutomation #GoLang #AITesting #GenAItesting #ZeroBudgetQA
