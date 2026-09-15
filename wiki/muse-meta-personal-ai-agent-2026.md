# Muse — Meta Personal AI Agent (Sep 2026)

**Sources:** [ai.meta.com/muse](https://ai.meta.com/muse/) (product) · [TechCrunch 08.09.2026](https://techcrunch.com/2026/09/08/meta-debuts-its-muse-ai-agent-will-consumers-trust-it/) (trust angle, Sarah Perez) · [The Verge 08.09.2026](https://www.theverge.com/ai-artificial-intelligence/991216/meta-bets-on-ai-agent-muse-to-catch-up-in-ai-race) (race context, Robert Hart)
**Digest:** 2026-09-09 (3 items merged into this page)

## Facts

- **Launch:** Sep 8, 2026, US only. Web (muse.ai) + iOS/Android + WhatsApp chats; Meta AI glasses "coming soon".
- **Model:** powered by in-house **Muse Spark** (same family as `meta/muse-spark-1.3` / contributor tier on OpenRouter).
- **What it does:** email, travel booking, bill lowering, forms, grocery lists from reels, invitations, purchases (Stripe Link checkout; Shop Pay + 1Password coming). No-API services → **browser fallback** with user credentials. Works in background after app close; learns from conversations for unprompted suggestions.
- **Pricing:** free (usage meter + card required upfront) → Power $20/mo → Maximum $100/mo.
- **Competitors named:** Gemini Spark, Claude Cowork, ChatGPT Work, Copilot Tasks, Grok Bot, open-source Moltbot.
- **Trust baggage:** $18B multistate settlement (Aug 2026), Cambridge Analytica, FTC 2011/2019/2023, $942M New Mexico child-safety order. Training opt-out exists (default unknown); "forget" instruction supported.

## Sentinel — the supervisor pattern

Muse runs in **Muse Secure VM** (dedicated virtual computer, own browser). A separate **Sentinel agent** patrols the same VM at system level: no visibility into passwords/payment methods, nothing reaches the internet without approval, no data to ads systems. Confidential VM (even Meta can't access) promised later this year.

**Why it matters for us:** Sentinel = the **independent supervisor** pattern — same architecture as Agentiqa's supervisor model ("AI-written code should not grade itself"). Verifier separated from actor at system level, not by prompt.

## QA angles

1. **Trust as testable claim.** "Doesn't share with ads", "no password visibility", "forget works" — each is a verifiable assertion, not a vibe. Mutation-matrix instinct applies: probe the claim, don't read the whitepaper.
2. **Browser fallback = seam.** No-API access via real browser with user creds is the widest attack surface in the design (credentials + autonomy + background execution).
3. **Supervisor needs its own audit.** Who verifies Sentinel? Same regress as Article 26's "who verifies the verifier" — a supervisor is a second agent with its own failure modes (approval fatigue, over-permissive defaults).
4. **Background execution + learning loop** = non-determinism by design; unprompted suggestions are untestable by script, only by behavior sampling.

## Traction + hands-on (10.09)

- **No.2 US App Store** (from No.4 day before; 83K+ iOS US downloads, Sensor Tower via TC/Perez). Context: Threads did 4.3M day-one, ChatGPT 500K first week, Meta AI app 108K debut. Android: No.338 Productivity (weak). Web/WhatsApp uncounted.
- **Rival to watch: Instinct** ($2.5B valuation, $350M raised): text-message agent, user email addresses, Stripe + 1Password integrations, agent-to-agent social graph ("more valuable than Meta's friend graph" per TC).
- **Hands-on verdict (Verge/Roth 10.09): "works and creeps me out".** Works: Gmail cleanup (thousands), Amazon purchase with cart check. Creeps: shipping address → local news injection; Instagram API read deeper than UI shows (ad topics vague vs API detail); hallucinated app names ("Photos" for App Store, "Calender").
- **QA read:** API-surfaces-more-than-UI (observation gap = testability gap); location leakage via order data (seam: commerce → profile); label hallucinations in generated UI (exact-text matcher would PASS wrong names — decoy-adjacent).

## Cross-links
- Article 27 (guided QA): Sentinel as live industry instance of supervisor pattern; trust-deficit as Verify-don't-trust case.
- Article 26: "who verifies the verifier" — Sentinel/Agentiqa parallel.
- Agentiqa pilot catalog: independent-layer analogy (Positions-CV-CL/company/pilots/Agentiqa/index.md).
- GitLab sandbox escape (InfoQ 08.09.2026): what happens when the supervisor/allowlist model fails — trust handoff via approved proxy.
