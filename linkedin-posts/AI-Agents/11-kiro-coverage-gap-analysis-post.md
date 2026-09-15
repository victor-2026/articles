I ran [Kiro.dev](https://kiro.dev) — a free AI IDE — against two production test frameworks.

It found 49 methods and endpoints I never tested across two completely different codebases.

**OrangeHRM (POM):**
→ 14 uncovered methods (including `approveClaim` and `rejectClaim` — core business flows)
→ 42 tests generated

**Buzzhive (API):**
→ 35 uncovered endpoints (auth, posts, users, admin, error paths)
→ 122 tests generated

**Total: 49 gaps. 164 tests generated. 144 passed on first run — AI fixed 8 more. 🔧**

The uncomfortable truth: I wrote every one of those methods and endpoints myself. They're the core of both applications. And I never tested them.

Same AI IDE. Same approach. Two different architectures (PHP + Playwright POM, Node.js + REST API). Same blind spot.

A $0 AI IDE with 50 free credits found what my human planning missed — twice.

Full breakdown (with coverage gap tables from both projects and self-healing details) ↓

Victor Ematin · AI Quality Engineering Lead · $0 budget · OpenCode Go
#TestAutomation #ZeroBudgetQA #GenAItesting #Playwright
