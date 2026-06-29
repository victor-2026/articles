# Startup Programs — Credits, Tokens & Special Pricing

---
type: reference
domain: ai
created: 2026-06-20
updated: 2026-06-20
tags: [startup-credits, grants, agent-reference]
---

# AI Startup Resource Grants - agent reference

Программы, которые дают стартапам/компаниям кредиты, токены, GPU-компьют, хостинг или перки. Это справочный файл для ИИ-агента (knowledge/tool-file): фильтруй по `category`, `status`, `filters`; канонические требования - в поле **provide** (free text). Перед действием перепроверяй `url` - суммы и окна приема меняются.

Поля: **status** = active | waitlist | closed (циклический/пауза) | unclear (программа реальна, цифра/страница не подтверждены). **filters** - грубые эвристики для машинной фильтрации (`?` = не указано); канонично поле provide. Проверено веб-поиском по офиц. страницам, июнь 2026.

Всего программ: 61.


## Inference / токены

### Baseten for Startups (AI Startup Program)
- **id:** `baseten-for-startups-ai-startup-program`
- **url:** https://www.baseten.co/startup-program/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $25,000 in credits for Dedicated Inference or Training; up to $2,500 in credits for Model APIs. Plus priority support (response within a few business hours), shared Slack/Zoom, networking and GTM/exclusive events.
- **provide:** Must be an AI-first startup (AI core to the primary product). Funding stage Seed to Series A AND founded less than 5 years ago. Net-new customer only: 'Only net new customers can be enrolled' = you have never received any Baseten credits before. No explicit employee cap, work-email, website/pitch, VC-referral or region requirement stated on the page.
- **apply:** Apply via the form behind the 'Submit your application' / 'Join the program' button on baseten.co/startup-program/ (target: https://www.baseten.co/talk-to-us/startup-program/). No alternative email listed.
- **filters:** stage=seed to series a; max_age_y=5; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Fireworks AI for Startups (Fireworks for Startups)
- **id:** `fireworks-ai-for-startups-fireworks-for-`
- **url:** https://fireworks.ai/startups
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Offers 'Build Credits' (credits + higher rate limits) plus direct access to Fireworks applied-AI engineers, day-0/day-1 SOTA OSS model access, startup community/events, product collaboration and marketing visibility. NO specific dollar credit amount is published on the official page. Third-party listings cite figures like ~$5K (some via Google Cloud / partner packs), but these are unconfirmed against the official page.
- **provide:** AI-native startups building generative-AI apps that need fast/reliable inference. Third parties list funding stages Pre-seed through Series B and global availability, but the official page does NOT publish explicit funding caps, company-age caps, work-email, website/pitch, VC-referral, or net-new requirements.
- **apply:** Apply via the 'Join Program' / 'Register Today' button at fireworks.ai/startups -> fireworks.ai/startup-program (registration form).
- **filters:** stage=pre-seed through series b; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Mistral for Startups (Mistralship)
- **id:** `mistral-for-startups-mistralship`
- **url:** https://mistral.ai/startups
- **status:** unclear  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Approximately €30,000 (~$30K) in credits for Mistral's La Plateforme, plus cohort mentorship: 1:1 support from Mistral's Solutions & Science team and early access to new models/products. Equity-free.
- **provide:** Early-stage AI startups building with Mistral models; cohort-based (~10 startups per 6-month cohort), highly selective, application mandatory. Third-party sources indicate: company under ~7 years old, has an online presence (website), and has NOT raised Series B or later (Series A or earlier). Must prepare a company overview + implementation plan for using Mistral's models. No equity taken; global. Exact official caps not directly confirmed from the page.
- **apply:** Apply directly via Mistral's website (mistral.ai/startups) during open cohort application windows announced on Mistral's channels. Cohort/selection-based, not a rolling self-serve form.
- **filters:** stage=series b; max_age_y=7; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Perplexity for Startups
- **id:** `perplexity-for-startups`
- **url:** https://www.perplexity.ai/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $5,000 in Perplexity API credits + 6 months of free Perplexity Enterprise Pro for up to 50 seats.
- **provide:** Per Perplexity's official announcement (X/Threads): startup must have raised LESS THAN $20M in equity funding, be LESS THAN 5 years old, AND be associated with one of Perplexity's approved Startup Partners (accelerator/VC/partner referral effectively required). Some third-party listings state '<$10M' but the official Perplexity post says <$20M. No explicit employee cap or work-email rule published; global.
- **apply:** Apply via the form on perplexity.ai/startups (must show association with an approved Startup Partner). Eligible applicants receive an activation email after verification. Partner-referral route via the partner's perk portal where applicable.
- **filters:** stage=?; max_age_y=5; max_funding_$m=20; net_new=?; referral=True; self_serve=False

### Replicate Startup Program
- **id:** `replicate-startup-program`
- **url:** https://replicate.com/startups
- **status:** unclear  ·  **confidence:** low  ·  **verified:** 2026-06
- **amount:** Credits reported in the ~$1K-$10K range (figures vary by source; not confirmed on an official Replicate page). Third-party paths cited: ~$2.5K via Ramp, ~$1K via Researcher Access, and invitation-only/VC-partner credit paths. Use of Replicate's open-source ML model hosting / inference.
- **provide:** Pre-seed, Seed, or Series A; global; building with open-source ML models. Practical gating noted by third parties: must use a company-domain email (personal Gmail/Outlook commonly rejected), have a real (non-placeholder) website, and application details must match Crunchbase/PitchBook. No official figure for employee/age caps confirmed.
- **apply:** Reported via 'Claim Offer' links to replicate.com and via partner channels (Ramp perks portal, researcher-access program, VC introductions). No confirmed open application form on an official Replicate startups page at time of check.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Together AI Startup Accelerator
- **id:** `together-ai-startup-accelerator`
- **url:** https://www.together.ai/startup-accelerator
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Tiered free platform credits by funding raised: Build (up to $5M raised) = up to $15K credits + 3 hrs engineering support; Scale ($5M-$10M) = up to $30K + 6 hrs; Grow (over $10M) = up to $50K + 10 hrs. All tiers: forward-deployed engineering support, GTM amplification to 800K+ developers, community/events, VC network connections. Credits do NOT apply to Reserved GPU Clusters.
- **provide:** AI-native startups building on Together AI's platform; selection-based. The differentiating eligibility factor is funding raised (which determines tier, e.g. <$5M / $5-10M / >$10M). The page asks applicants to 'share all the details' (company/funding details). No explicit employee cap, age cap, work-email, or net-new rule published; covers training/fine-tuning/inference use.
- **apply:** Apply via the on-page application form at together.ai/startup-accelerator (fill out the details fields and submit). No separate email listed.
- **filters:** stage=?; max_age_y=?; max_funding_$m=5; net_new=?; referral=?; self_serve=False


## Облако и БД

### Akamai (Linode) Rise Start-Up Program
- **id:** `akamai-linode-rise-start-up-program`
- **url:** https://www.akamai.com/cloud/start-ups/rise
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Between US$500 and US$120,000 in Akamai Cloud (Linode) credits during the FIRST year, allocated by stage/needs (a range, not a flat $120k for everyone). Three-year program: years two and three offer continued discounts on cloud services (specific discount % not published). Also includes solutions-engineer guidance, dedicated account management, and community/networking.
- **provide:** For-profit company fewer than 7 years old, new to Rise. Must show at least ONE traction signal: paid employees beyond founders, active non-friends/family/investor users, initial revenue, OR VC funding (any one suffices; no formal funding-proof doc or employee cap beyond the 7-year age limit). Must have a defined plan to scale infrastructure with Akamai Cloud as one of the PRIMARY providers. Account prerequisites: a corporate email matching your company domain, a working company website on that same domain (required for security verification), and a valid credit card on file. Net-new credit rule: existing Akamai customers qualify only if they have NOT received more than US$3,000 in prior infrastructure credits. Industry: SaaS, media, and gaming prioritized; managed hosting providers, MSPs, system integrators, and resellers NOT eligible. No explicit region/country limit or required VC/accelerator referral on the official page.
- **apply:** No standalone form URL or application email published. Steps: (1) create an Akamai Cloud account at https://login.linode.com/signup with a corporate email + valid credit card; (2) submit the intake application via the "Apply to the Rise start-up program" CTA on https://www.akamai.com/cloud/start-ups/rise; (3) team reviews, status within ~2 weeks; (4) qualified applicants take a discovery call; (5) onboarding and credits added. A separate partner-referral track exists at linode.com/start-ups/partner/ (VCs/accelerators/incubators can refer portfolio companies), but a referral is not required for direct application.
- **filters:** stage=?; max_age_y=7; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Alibaba Cloud AI Catalyst
- **id:** `alibaba-cloud-ai-catalyst`
- **url:** https://www.alibabacloud.com/en/startup/ai
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Up to 2 billion free Model Studio tokens; up to $120,000 in cloud credits; 12 months access to Alibaba Cloud Academy (learning/certification); 1:1 office hours with AI experts; access to Alibaba Cloud global events and partnership opportunities.
- **provide:** Official page does NOT spell out funding-stage, employee/age caps, prior-credits, incorporation, or region requirements. It prioritizes AI-focused startups, especially those in AI video/image generation and deepfake detection, AI model-aggregation platforms, and content-moderation solutions. (No VC/partner referral stated as required.)
- **apply:** Submit the online application form on the program page. Four steps: application submission, possible request for more info, email notification of acceptance/rejection, then onboarding.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Cloudflare for Startups
- **id:** `cloudflare-for-startups`
- **url:** https://www.cloudflare.com/startups/
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Cloudflare credits in tiers, plus free core security/networking features for all tiers. Current product page indicates roughly: Tier 3 = $10k (credits + community/dev resources); Tier 2 = $100k (credits + account manager + technical sessions); Tier 1 = $350k (max credits + account manager + priority support + bi-weekly office hours). NOTE: Cloudflare's own April 2025 blog described a different 4-tier structure of $5k / $25k / $100k / $250k. The figures vary by source/date - the $10k/$100k/$350k set is what the current /startups/ page returned. Credits valid ~1 year.
- **provide:** For-profit company founded within the last 10 years (some sources say ≤5 years), actively developing a technology/software product, with a live publicly accessible website, a domain-matching business email, and a public presence on LinkedIn/X/GitHub. FIRST-TIME applicants only (no prior Cloudflare startup credits). Higher tiers are funding-gated: roughly 'funded up to Series B within the last 12 months', with the ~$100k tier needing $1M+ raised from an affiliated partner and the top tier needing $5M+ raised from an affiliated partner (one of 250+ approved VC/accelerator partners). Direct applications are accepted; partner affiliation strengthens higher-tier eligibility but a referral code is not mandatory for the base tier.
- **apply:** Apply via the 'Apply now' link on https://www.cloudflare.com/startups/, which goes to https://www.cloudflare.com/lp/startups/ (application form). Partner/accelerator affiliation can be indicated to qualify for higher tiers.
- **filters:** stage=series b; max_age_y=10; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Databricks for Startups
- **id:** `databricks-for-startups`
- **url:** https://www.databricks.com/product/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $200,000 in credits, spanning both Databricks and Neon (the serverless Postgres DB Databricks acquired). This is the consolidated app-backend + data + AI stack. (Note: older third-party directories still cite a stale $50,000 figure from the previous program; the current official figure is $200k.)
- **provide:** Purpose-built for early-stage, venture-backed startups. Target profile: recently raised institutional funding, pre-seed through Series A, building the company on data/AI. No public hard cap on employees/revenue stated. Databricks explicitly says 'Not sure if you qualify? Apply or ask your investor' and will review borderline applications. Investor/VC association is a strong signal but a direct apply path exists. Detailed eligibility (incorporation, prior-credits rule) is gated behind the application form, not published.
- **apply:** Apply via the 'Apply now' button on https://www.databricks.com/product/startups, which opens a Qualtrics application form. Can also be routed through an investor/VC partner.
- **filters:** stage=pre-seed through series a; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### DigitalOcean Hatch
- **id:** `digitalocean-hatch`
- **url:** https://www.digitalocean.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $100,000 in compute credits with a $10,000/month spend limit (usage above the monthly limit is billed), valid ~12 months. Plus up to ~3 months of free GPU Droplet usage and discounted ongoing GPU access (~$1.90/GPU/hour for H100-class), 15 months of free Standard-tier support, 1:1 sessions with DigitalOcean staff, marketplace exposure, and partner discounts (Stripe, Notion, HubSpot, etc.). Exact credit amount is determined after review and is higher for partner-referred startups.
- **provide:** Must have raised $10 million or less. Must have a company website with a MATCHING corporate/business email (no personal email). Must register a DigitalOcean team account using that business email. Must NOT have previously received DigitalOcean credits (net-new). AI-native startups are prioritized; pure service-based/consulting startups are ineligible. A VC/accelerator/incubator partner referral is not strictly required (you can select 'Other'), but partner-referred applicants typically receive larger credit awards than direct applicants.
- **apply:** Apply via the Typeform linked from https://www.digitalocean.com/startups (select 'Other' if not backed by a recognized VC/accelerator/partner). Approved DigitalOcean Startups partners (VCs, accelerators) can also refer startups directly.
- **filters:** stage=?; max_age_y=?; max_funding_$m=10; net_new=True; referral=False; self_serve=False

### IBM for Startups (watsonx)
- **id:** `ibm-for-startups-watsonx`
- **url:** https://www.ibm.com/startups
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** IBM Cloud credits usable across watsonx (AI), data/analytics, security and infrastructure (130+ services). Two tiers: Builder = $1,000/month in credits; Premium = $10,000/month, up to a total of $120,000 (typically over 12 months).
- **provide:** Company under 5 years old; under ~$1M annual revenue; maximum ~$5M total funding raised. Must be actively developing a software-based product/service that is OWNED (not licensed) by the startup and is core to the business. Must operate your own public website on your own domain and provide a contact email on that domain. Premium ($10k/mo) tier requires sponsorship/referral from an approved IBM venture partner; Builder tier is more openly accessible. Zero equity taken.
- **apply:** Apply via the IBM application form at https://orders.cloud.ibm.com/IBMGEP-application/ (linked from ibm.com/startups). Premium tier requires going through an approved venture/accelerator partner.
- **filters:** stage=?; max_age_y=5; max_funding_$m=1; net_new=?; referral=?; self_serve=False

### MongoDB for Startups (Atlas)
- **id:** `mongodb-for-startups-atlas`
- **url:** https://www.mongodb.com/solutions/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Atlas credits (amount varies by tier/funding stage; widely cited up to $5,000, larger for VC-backed tiers - exact per-tier dollar figures not published on page), plus Voyage AI tokens (AI embedding/reranking), Developer Support plan (first 30 days free then $49/mo, payable with credits), 1:1 expert sessions, and matching partner credits from Fireworks AI and Temporal. 12 months to activate, 12 months to use.
- **provide:** Series A or earlier; company less than 7 years old; a single scalable software product/service; active company website + LinkedIn page; must NOT have been previously accepted into the program. Dev shops, consultancies, and marketing agencies are ineligible. New MongoDB users not required (existing users may apply). VC/accelerator referral NOT required (direct application available, or referral via partner).
- **apply:** Direct application form embedded on the page (#startups section). Alternatively, a VC/accelerator can refer you; partners not yet enrolled email startups@mongodb.com. Contact: startups@mongodb.com.
- **filters:** stage=series a or earlier; max_age_y=7; max_funding_$m=?; net_new=?; referral=False; self_serve=False

### Neon Startup Program
- **id:** `neon-startup-program`
- **url:** https://neon.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $100,000 in Neon credits distributed over time, plus engineering support during onboarding and beyond, early product access, and co-marketing opportunities.
- **provide:** Must have raised a minimum of $1M in total venture funding; be at early-stage product or MVP stage; and be backed by verifiable venture capital. Application form asks for company email, company website, and major investor/accelerator. No stated incorporation/employee/age cap or no-prior-credits clause.
- **apply:** Apply via the form embedded on neon.com/startups ('Apply now' / #contact-form). Requires first/last name, company email, company website, and major investor/accelerator name.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Oracle for Startups
- **id:** `oracle-for-startups`
- **url:** https://www.oracle.com/startup/
- **status:** unclear  ·  **confidence:** low  ·  **verified:** 2026-06
- **amount:** Baseline: Oracle Cloud Free Tier access plus a stated ~70% discount on Oracle Cloud services and a small starter credit (~$500 cited by directories). Higher allocations 'up to $100,000' in OCI credits are cited historically, but are now primarily available via VC/accelerator partners and could not be confirmed on the official page. Non-dilutive (no equity). Figures NOT confirmed from Oracle directly - do not rely on them as current.
- **provide:** Generally: less than 10 years old; have a minimum viable product / scalable technology solution; commonly 'not a current Oracle Cloud customer' for the credit grant; enterprise-oriented solution favored. The larger credit tiers in practice require association with a qualified accelerator or VC partner. Open globally and to any stage per Oracle's own framing ('open to all startups'). Exact current requirements unverified due to 403 on official pages.
- **apply:** Apply through the Oracle for Startups site (oracle.com/startup/ → oracle.com/cloud/oracle-for-startups/): check eligibility, prepare company/website/product details, submit, await approval. Larger credit allocations route through an approved VC/accelerator partner.
- **filters:** stage=?; max_age_y=10; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### OVHcloud Startup Program
- **id:** `ovhcloud-startup-program`
- **url:** https://startup.ovhcloud.com/en/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Two tiers, 12-month credit window. EU site: START = up to EUR 10,000 in free public cloud credits + 6h 1-on-1 engineer time; SCALE = up to EUR 100,000 + up to 20h engineer time. US site quotes the same tiers in USD: START = up to USD 12,000; SCALE = up to USD 120,000. Also includes mentoring, support, visibility, and access to networking/funding events. No equity taken, no fee.
- **provide:** Stage-based, not hard metric caps. Official FAQ requires: a genuine startup / professional commercial activity with at least a POC or MVP that can run on OVHcloud cloud, plus a near-term need for cloud infrastructure. Tiering by funding stage: START = pre-seed/seed; SCALE = Series A and above. Apply via and associate with an OVHcloud customer account (once associated you cannot switch accounts). Excluded: non-startup projects (NGOs, associations, hobby projects), companies that previously participated in the program, incomplete applications, and contentious activities (crypto mining, Black Hat SEO). Region: choose the correct country/regional OVHcloud site; program runs across OVHcloud markets (EU, US, etc.) with credits in local currency. CAUTION: a third-party aggregator (Granted AI) claims hard caps of under 5 years old, under 50 employees, revenue below EUR 10M plus a Series-A/monthly-spend gate for SCALE; these numeric thresholds are NOT stated on OVHcloud official FAQ/eligibility pages and should be treated as unverified. No explicit net-new-customer rule found, but prior participants are barred.
- **apply:** Apply via the official portal: click Apply at https://startup.ovhcloud.com/en/ (login/signup at https://startup.ovhcloud.com/en/login/). Pick the correct country site, sign in to or create an OVHcloud account, answer the business questions, submit; decision within ~7 days by email. US incubators/accelerators/VCs can contact the team at startup@us.ovhcloud.com for partner/referral inquiries.
- **filters:** stage=pre-seed; max_age_y=5; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Redis Startup Program (Redis for Startups)
- **id:** `redis-startup-program-redis-for-startups`
- **url:** https://redis.io/startups/
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Per third-party listings: $10,000 in Redis credits. Free Redis Cloud (official page states 6 months free with usage limits; some aggregators say 12 months - inconsistent, so duration is not firmly confirmed). Plus early access to new features, dedicated support with monthly office hours / basic support plan, applied-AI team mentorship, and go-to-market/co-marketing benefits.
- **provide:** Per third-party listings: privately-held venture-backed startups, pre-seed/seed stage, with less than $5M total funding, building on Redis for real-time data / AI-ML applications. Application asks for technical architecture, growth roadmap, and may request financials/pitch deck. Prior-credits and region restrictions not stated. Official redis.io/startups page does not itself spell out these thresholds.
- **apply:** Apply via the form linked from redis.io/startups/ ('Apply now'). Third-party sources cite a partner/application portal. Alternatively speak to Redis via redis.io/meeting/.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=5; net_new=?; referral=?; self_serve=False

### Scaleway Startup Program
- **id:** `scaleway-startup-program`
- **url:** https://www.scaleway.com/en/startup-program/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Tiered EUR cloud credits, no equity. Founders up to EUR 1,000 over 1 year. Early Stage up to EUR 9,000 (EUR 1,500/mo x 6). Growth Stage up to EUR 36,000 (EUR 3,000/mo x 12), about USD 39,000. Includes GPU compute (H100) for AI startups plus engineer guidance.
- **provide:** Official criteria: under 5 years old, under 50 employees, not yet a Scaleway client (net-new). Any vertical; no funding proof, founder-age cap, work-email, website, or VC referral required per official text. Third-party listings add EU/associated-country incorporation (likely but not verbatim on official page). Entry via Founders tier, then Early/Growth by monthly spend; cannot jump Early to Growth.
- **apply:** Email startup-program@scaleway.com via official page https://www.scaleway.com/en/startup-program/. No standalone form URL; team assists by email. Rolling weekly review. Also reachable via partner perk portals like Founderpass.
- **filters:** stage=?; max_age_y=5; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Snowflake for Startups
- **id:** `snowflake-for-startups`
- **url:** https://www.snowflake.com/en/why-snowflake/startup-program/
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Snowflake Startup Accelerator: 6-month program giving free Snowflake usage credits (exact dollar amount NOT published on the official page), access to technical experts, dedicated go-to-market support, and visibility in Snowflake's ecosystem. Snowflake also announced investing up to $200M into next-gen startups. (The $250k figure floating around is a third-party tiered-credit reference, NOT a confirmed flat Snowflake grant.)
- **provide:** Startup Accelerator: designed for startups developing customer-facing applications on top of Snowflake's AI Data Cloud; evaluated on potential to drive value for Snowflake customers. Official page does NOT publish funding-stage, employee/age caps, net-new-customer, incorporation, or referral requirements. (The Startup Challenge competition, a separate track, requires <$5M cash funding, no priced equity round / pre-Series A, legal incorporation, app built on Snowflake, demo video - do not conflate with the standing program.)
- **apply:** 'Register your interest' / fill out the form on the Startup Program and Startup Accelerator pages; a Snowflake team member follows up to discuss. Admitted on a rolling basis.
- **filters:** stage=series a; max_age_y=?; max_funding_$m=5; net_new=?; referral=?; self_serve=?

### Supabase Startup Program
- **id:** `supabase-startup-program`
- **url:** https://supabase.com/solutions/startups
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Direct program (third-party-reported): 6 months of Team plan free, ~$3,600 value (database, auth, storage, edge functions, realtime, vector). Via partner ecosystems (e.g., AWS Activate, Vercel, YC, Mercury Perks) credit values vary widely - reported figures range from $300 to up to $25,000 depending on partner; none confirmed on supabase.com directly.
- **provide:** Direct program (third-party-reported): less than $5M total funding; founded within last 5 years; fewer than 10 employees; an active or prospective Supabase project; bootstrapped/pre-seed/seed accepted; NO VC referral required. Agencies/consultancies ineligible. Common rejection causes: personal (Gmail/Outlook) email instead of company-domain work email, thin/placeholder website, info mismatched vs Crunchbase/PitchBook. Partner-route eligibility depends on the specific partner program.
- **apply:** Direct: create a Supabase organization, then complete the startup program form (reported at supabase.com/partners), submit funding/team/founding/product info; review ~3-14 business days. Alternatively apply via partner accelerators/VCs (YC, Techstars, AWS Activate, Vercel, Mercury Perks).
- **filters:** stage=pre-seed; max_age_y=5; max_funding_$m=5; net_new=?; referral=False; self_serve=False

### Tencent Cloud Startup Program
- **id:** `tencent-cloud-startup-program`
- **url:** https://www.tencentcloud.com/campaign/startupprogram
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Up to $100,000 USD in Tencent Cloud service vouchers (tiered, "starting from $0" up to the $100k cap), plus exclusive product discounts, complimentary access to 100+ products for prototyping/free tier, technical workshops, dedicated customer/solution-engineering support, and co-marketing through Tencent's partner network. The $100k figure is corroborated by multiple secondary sources (cloudcredits.io, StartmeupHK, HackerNoon) but is NOT confirmed as readable text on the official campaign page itself - treat the exact ceiling as not officially verified.
- **provide:** Per secondary sources (not verbatim from the official page): must be an operational startup, either VC-backed (ideally by a Tencent VC partner) OR self-funded with operational viability; founded within the last 5 years (extended to 10 years for Web3 startups); must NOT have previously received substantial Tencent Cloud credits (net-new to the program); a registered company with funding/registration details to submit on the form. A verified Tencent Cloud account is mandatory. Regional focus is Asia/global-international (intl.cloud.tencent.com); some partner-channel variants are region/affiliation-gated (e.g. Tencent-NUS = NUS-affiliated startups, ~$7,500 credits; HKUST channel for HK). No explicit employee cap, work-email requirement, or mandatory VC/accelerator referral could be confirmed; self-funded startups are explicitly eligible, so a referral is not strictly required for the main program.
- **apply:** Apply directly via the official campaign page https://www.tencentcloud.com/campaign/startupprogram - click "Sign Up", create and identity-verify a Tencent Cloud account at intl.cloud.tencent.com, then fill out the in-flow application form (company + funding details). Approval is by email within ~2 weeks. No standalone form URL or contact email is published on the page itself. Partner/accelerator channels offer alternate entry points with their own forms (e.g. Tencent-NUS via a Microsoft Forms link, HKUST Entrepreneurship Center), but these are affiliation-specific and often smaller credit tiers.
- **filters:** stage=?; max_age_y=5; max_funding_$m=?; net_new=True; referral=False; self_serve=False

### Vultr Startup Program (Vultr Digital Start-up Program)
- **id:** `vultr-startup-program-vultr-digital-star`
- **url:** https://discover.vultr.com/startup-program
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $100,000 in cloud credits (valid ~12 months) PLUS up to 35% long-term service discounts. Credits cover CPU, GPU, and other Vultr cloud services. Also bundled: executive sponsorship, technical architecture reviews, dedicated account management, and priority support. (No fixed per-startup figure published - $100K is the stated maximum/"up to" amount, allocated case-by-case.)
- **provide:** Stage/funding: MUST have secured recent Series A, B, C, D, or E financing (institutional venture funding is the hard gate - no pre-seed/seed/bootstrapped tier offered). Applicant must PROVIDE: (1) name + contact of senior-most technical executive (e.g. CTO); (2) name + contact of senior-most cloud infrastructure leader; (3) last 6 months of cloud compute invoices (so applicant needs existing measurable cloud spend - this is a migration program, effectively net-new-to-Vultr customers); (4) agreement to be publicly referenceable as a program member. No published employee-count cap, company-age cap, work-email requirement, website requirement, or explicit region restriction (program runs events e.g. in Mexico City but does not state geographic exclusions). No VC/accelerator referral required - startups apply directly.
- **apply:** Apply directly via the official page https://discover.vultr.com/startup-program using the "Apply Now" / "Join Now" button. There is NO public self-serve form URL or dedicated application email - the CTA routes the application through Vultr's sales/partnerships channel for review. No partner portal or third-party referral mechanism is involved; submit the required documents (executive contacts + 6 months of invoices) when contacted.
- **filters:** stage=series a; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False


## GPU-компьют

### AMD Developer Cloud
- **id:** `amd-developer-cloud`
- **url:** https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Two paths: (1) $100 in credits (~50 hours on a single MI300X) automatically for signing up to the AMD AI Developer Program, no approval. (2) An additional initial 25 complimentary credit hours on MI300X via the GPU Droplet credit-request form, subject to approval, usable within 10 days of approval. Some partner bundles also add $50 Fireworks AI API credits and a free month of DeepLearning.AI Pro. On-demand pricing is ~$1.99/hr single MI300X.
- **provide:** Create an AMD account / enroll in the AMD AI Developer Program (the $100 has no approval gate). The 25 extra hours require submitting the credit request form and approval. A valid payment method (card) must be on file before launching a GPU Droplet even if credits cover usage. No funding stage, incorporation, employee cap, or VC referral required; open to individual developers. (Separate, larger 100k-hour allocations exist for specific cohorts like Indian/Malaysian researchers and startups - not the general grant.)
- **apply:** Sign up / claim via the AMD AI Developer Program and the AMD Developer Cloud at https://www.amd.com/en/developer/resources/cloud-access/amd-developer-cloud.html; for the extra 25 hours, create the account, go to the GPU Droplet page, and fill out the credit request form (DigitalOcean-hosted environment).
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### CoreWeave Startup Accelerator
- **id:** `coreweave-startup-accelerator`
- **url:** https://www.coreweave.com/
- **status:** unclear  ·  **confidence:** low  ·  **verified:** 2026-06
- **amount:** Cannot confirm a specific figure. 2022 announcement said accepted companies get 'CoreWeave Cloud credits plus additional discounts' but gave no dollar amount. Current Ventures page lists no fixed free-credit amount (it is investment / compute-for-equity, not a published credit grant). Do not cite a number.
- **provide:** Per 2022 program: AI/ML-focused companies solving complex problems with high-performance compute; open-ended (no deadlines). Current Ventures path: founders pre-seed through later stage; terms negotiated (investment or compute-for-equity). No published employee/age/email/funding-proof requirements; effectively a selective, relationship/equity-based process rather than a self-serve credit form.
- **apply:** No live dedicated accelerator form confirmed. Closest current route is the CoreWeave Ventures application form/contact at https://www.coreweave.com/ventures (apply via form or email the Ventures team). General contact via coreweave.com.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Modal for Startups
- **id:** `modal-for-startups`
- **url:** https://modal.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 'Thousands of free GPU credits.' No single exact dollar figure published on the page; amount is tiered by funding stage. Do not treat as a fixed number.
- **provide:** Must be new to Modal and not have previously received credits in that tier (non-renewable per tier). VC-funding gated: Seed-Series A = raised any amount from a Modal VC partner OR raised >$1M from any fund; Series B+ = raised >$30M / post-Series B with a VC from their partner network. Effectively requires VC backing; partner-network referral strengthens eligibility. No employee/age cap, incorporation, or work-email requirement stated.
- **apply:** Apply via the form/'Apply Now' button on https://modal.com/startups (the #apply section of the same page).
- **filters:** stage=seed-series a; max_age_y=?; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Nebius AI Lift (startups)
- **id:** `nebius-ai-lift-startups`
- **url:** https://nebius.com/startups
- **status:** waitlist  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $5,000 introductory credits (stated as up to ~1,600 H100-equivalent GPU hours) plus up to $100,000 in savings via discounted compute for production workloads. The $100k is a discount, not free credit.
- **provide:** Must meet ALL: VC- or accelerator-backed; minimum $5M USD raised; building/scaling an AI-enabled product; maintain a working company website; apply with a company email address; officially incorporated business less than 7 years old. Currently effectively requires application through a Nebius venture partner. Excluded: consulting firms, resellers, cloud providers, crypto-only businesses, public companies.
- **apply:** Application form on https://nebius.com/startups (the #form section); a separate community signup exists to be notified of availability; questions to startups@nebius.com. Preferred route is via a Nebius venture partner.
- **filters:** stage=?; max_age_y=7; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### RunPod Startup Program
- **id:** `runpod-startup-program`
- **url:** https://www.runpod.io/startup-program
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Two tiers. Growth: deposit up to $50,000 and get +$25,000 bonus credits (=$75,000 total) under a 12-month agreement. Starter: $1,000 in credits. Credits usable across Pods, Serverless, Clusters, Storage with no product restrictions. Note: Growth tier is deposit-matched, not pure free credit.
- **provide:** Venture-backed (Seed through Series B+) strongly preferred but reviewed holistically. Must have a real workload (production inference, training/fine-tuning, or compute-intensive R&D with a production path) and be ready to onboard now. Primarily for NEW customers (net-new, not existing/prior). No explicit employee/age cap, region limit, work-email, or referral requirement stated.
- **apply:** Apply via the 'Apply now' button / application form on https://www.runpod.io/startup-program.
- **filters:** stage=seed through series b; max_age_y=?; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Vast.ai Startup Program
- **id:** `vast-ai-startup-program`
- **url:** https://vast.ai/startup
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Spend-matching, not upfront free credits: Vast matches your verified compute spend dollar-for-dollar in credits (e.g., spend $500 -> get $500 back in credits). No fixed maximum published on the page.
- **provide:** Targeted at companies that are 'shipping' - actively training models, running inference, or scaling a production workload. The page does NOT publish specific eligibility gates: no stated funding-stage requirement, employee/age cap, incorporation proof, prior-credits rule, work-email requirement, referral, or region limit. Practical gate is that you must actually spend (verified compute spend) to earn matching credits.
- **apply:** Apply via the 'Apply Now' / 'Apply to the startup program' button on https://vast.ai/startup; team follows up to finalize the offer.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False


## AI-тулинг и поиск

### Datadog for Startups
- **id:** `datadog-for-startups`
- **url:** https://www.datadoghq.com/partner/datadog-for-startups/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $100,000 in credits for one year of access to the full Datadog platform (no restricted/watered-down tiers). Includes optional Technical Engagement Manager onboarding and a customer success rep.
- **provide:** Series A or earlier. Must be NET-NEW to Datadog: cannot be a current or prior Datadog customer and cannot have previously received DDFS credits. CRITICAL: all applicants must come through one of Datadog's official referral partners (VCs, accelerators, hyperscalers/other vendor startup programs) - a referral is mandatory. Credits must be activated within 30 days of acceptance; ~3 months of no usage triggers an inactivity notice. No explicit employee-count or company-age cap published.
- **apply:** Apply via the 'Apply Now' form on https://www.datadoghq.com/partner/datadog-for-startups/ (must indicate/come via a referral partner); create a trial account while under review. Questions to startups@datadoghq.com.
- **filters:** stage=series a or earlier; max_age_y=?; max_funding_$m=?; net_new=True; referral=True; self_serve=False

### Exa free searches (Free tier)
- **id:** `exa-free-searches-free-tier`
- **url:** https://exa.ai/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to 20,000 requests per month for free (per official pricing page), covering web search tool calls for agents, webpage text and highlights. Beyond that you upgrade to Core ($49/mo) or Pro ($449/mo). (Older sources mention a $10 signup credit / 1,000 requ- not on the current page.)
- **provide:** Sign up for an account / API key. Credit-card requirement not explicitly stated on the pricing page. No funding/incorporation/employee requirements for the free tier.
- **apply:** Self-serve: sign up at https://dashboard.exa.ai to get an API key; 'Try API for free' / API Playground links on https://exa.ai.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True

### Firecrawl free tier (Free plan)
- **id:** `firecrawl-free-tier-free-plan`
- **url:** https://www.firecrawl.dev/pricing
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 1,000 credits per month (~1,000 pages scraped/month), with 2 concurrent requests and low rate limits.
- **provide:** No credit card required. Just sign up for an account. No funding/incorporation/employee requirements for the standard free plan. (The separate Student Program requires student verification; a startup-credits deal is referenced only in third-party directories, not confirmed on the official pricing page.)
- **apply:** Self-serve: sign up at https://www.firecrawl.dev/signin?view=signup. (Student Program: apply at https://www.firecrawl.dev/student-program.)
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True

### LangChain / LangSmith for Startups
- **id:** `langchain-langsmith-for-startups`
- **url:** https://www.langchain.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Two tiers. BUILD tier: discounted LangSmith seat pricing (no credits figure). SCALE tier: $10K in LangSmith credits, valid for 1 year (2 years for Y Combinator participants), plus VIP event invites, office hours with the LangChain team, exclusive Slack networking channel, and a startup spotlight.
- **provide:** BUILD: first-time/new customer; less than $10M total funding; minimum $25K seed funding raised ('additional eligibility criteria may apply'). SCALE: first-time/new customer; Series A or earlier (up to $50M funding); must be backed by a LangChain premier VC partner (e.g. Sequoia, Y Combinator, Amplify, South Park Commons, Mayfield, NEA, Bessemer, First Round, Basis Set, Lux, Kleiner Perkins, Afore, Accel, Khosla, Audacious, Union). If your VC isn't a partner you can still qualify for the Build tier on the funding criteria alone.
- **apply:** Submit the tier-specific Airtable application linked from https://www.langchain.com/startups; confirmation email contains activation instructions.
- **filters:** stage=seed; max_age_y=?; max_funding_$m=10; net_new=True; referral=?; self_serve=False

### LlamaIndex / LlamaCloud (LlamaParse) Startup Program
- **id:** `llamaindex-llamacloud-llamaparse-startup`
- **url:** https://www.llamaindex.cloud/startups
- **status:** unclear  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Reported by secondary sources as ~$2,000 in free LlamaCloud/LlamaParse credits (about one year), plus a dedicated AI-engineer Slack support channel, bulk-credit discounts, an alignment call with founder Jerry Liu, and a community spotlight. Figure NOT confirmed on the official page (cert expired). Separately, the standard free plan gives 10,000 credits/month automatically.
- **provide:** Secondary sources indicate it targets startups, with at least some references to VC-backed startups. Exact, official eligibility (incorporation, funding stage + proof, employee cap, no-prior-credits, referral) could NOT be verified because the official page was unreachable (expired certificate). The plain free tier (10k credits/mo) has no startup/funding requirement - just account registration.
- **apply:** Apply via the form at https://www.llamaindex.cloud/startups (page currently throws an expired-certificate error). The free 10k-credit plan needs no application - just sign up at https://cloud.llamaindex.ai.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Pinecone for Startups
- **id:** `pinecone-for-startups`
- **url:** https://www.pinecone.io/startup-program/
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Free access to Pinecone's Standard Tier plus Pro Support (any cloud/region deployment, RBAC, Backups, Import, Prometheus Metrics, dedicated Slack channel), plus 'usage credits and discounts.' NO specific dollar figure or duration is published on the official page - do not assume a number. No equity taken.
- **provide:** Series A or earlier funding stage; fewer than 100 employees. Available globally. Page does not state a 'net-new customer' / no-prior-credits rule or require a VC referral, though a partner track exists (via Google Form).
- **apply:** Apply via the 'Join the Program' link on https://www.pinecone.io/startup-program/, or email startups@pinecone.io. Partners/VCs can become referral partners via a Google Form linked on the page.
- **filters:** stage=series a or earlier; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Qdrant for Startups
- **id:** `qdrant-for-startups`
- **url:** https://qdrant.tech/qdrant-for-startups/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 20% discount on Qdrant Cloud, valid for 12 months from the date of acceptance. This is a discount, not free credits.
- **provide:** Pre-seed, Seed, or Series A; company under five years old; less than $5M raised; building an AI-driven product or service (agencies/devshops NOT eligible); new to Qdrant Cloud (existing accounts created within last 30 days OK); must NOT have previously participated in the program; must provide a link to a live, functional website; billing must be direct with Qdrant (not via a cloud marketplace). No VC referral required.
- **apply:** Submit the online application form on https://qdrant.tech/qdrant-for-startups/ ('Apply Now'). Questions to startups@qdrant.com.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=5; net_new=True; referral=False; self_serve=False

### Serper free tier
- **id:** `serper-free-tier`
- **url:** https://serper.dev/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 2,500 free search queries (one-time free allotment for new accounts via the Google Search API).
- **provide:** No credit card required. Just create an account. No funding/incorporation/employee requirements stated.
- **apply:** Self-serve: click 'Sign up' on https://serper.dev to create an account and get an API key.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True

### Tavily free research plan (Researcher tier)
- **id:** `tavily-free-research-plan-researcher-tie`
- **url:** https://docs.tavily.com/documentation/api-credits
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 1,000 API credits per month (resets monthly). Roughly ~1,000 basic searches (1 credit each) or ~500 advanced searches (2 credits each); includes Search and Extract endpoints plus community support.
- **provide:** No credit card required. Just sign up for an account and get an API key. No funding/incorporation/employee requirements stated.
- **apply:** Self-serve: sign up at https://app.tavily.com to create an account and retrieve a free API key.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True

### Unstructured free tier
- **id:** `unstructured-free-tier`
- **url:** https://unstructured.io/pricing
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 15,000 free pages of document processing, no expiration, with full access to every feature in the platform. No minimums, completely free.
- **provide:** None beyond creating an account / signing up. No funding stage, no incorporation, no employee cap, no credit card stated. Open to any developer.
- **apply:** Self-serve: click 'Get Started' / 'Try for free' on https://unstructured.io/pricing (modal at https://unstructured.io/pricing?modal=try-for-free) or https://unstructured.io/letsgo and create an account.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True

### Zilliz Cloud free credits / free tier
- **id:** `zilliz-cloud-free-credits-free-tier`
- **url:** https://zilliz.com/zilliz-cloud-free-tier
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Permanent Free tier cluster: 5 GB storage (~1M 768-dim vectors), 2.5M vCUs/month, up to 5 collections, no credit card. Plus promo: $100 in free credits on work-email signup (expire in 30 days), +$100 more for adding a payment method (extends expiry to 1 year) = up to $200, usable on Serverless and Dedicated clusters. A 30-day enterprise trial with up to $200 credits is also referenced.
- **provide:** Self-serve sign-up; work email recommended (gives the $100 credit). No funding stage, employee cap, incorporation proof, pitch, or referral required. Adding a payment method unlocks the extra $100 and 1-year credit expiry.
- **apply:** Self-serve: create an account at zilliz.com / cloud.zilliz.com (no application form). No partner portal needed.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=True


## Голос и видео

### AssemblyAI Startup Program
- **id:** `assemblyai-startup-program`
- **url:** https://www.assemblyai.com/contact/startup-program
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to 200,000 hours in free speech-to-text credits, plus access to all latest features, co-marketing opportunities, and community.
- **provide:** Application form collects: company incorporation year, company size, team commitment (full-time vs side project), funding stage (bootstrapped through Series C+), current customer status (pre-launch to 50+ paying customers), monthly STT usage, and total funding raised (USD). No explicit hard caps published (no stated employee/age cap, no work-email or referral requirement, no region limit, no 'no prior credits' clause) - selection is at AssemblyAI's discretion.
- **apply:** Web form at assemblyai.com/contact/startup-program. Support: support@assemblyai.com.
- **filters:** stage=series c+; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Cartesia Startup Grants
- **id:** `cartesia-startup-grants`
- **url:** https://www.cartesia.ai/startups
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** 12 months free on the Scale tier: 88M characters/year (8M/month) plus $300/month in agent credits, ~$7,200 total value, with 2 months of credit rollover plus high concurrency limits and improved support. (Google-for-Startups variant differs: 12 months Startup Tier, 1.25M credits/month, up to 5 concurrent, Pro Voice Cloning.)
- **provide:** For 'eligible startups' building voice experiences (prototype to scale). Specific gating not published on the rendered pages I could access; the AWS-channel offer effectively requires being an eligible startup in AWS's ecosystem, and the Google variant requires Google for Startups Cloud Program Scale Tier membership. Direct (non-partner) eligibility details for cartesia.ai/startups could not be confirmed - treat funding-stage/region caps as unverified.
- **apply:** Apply at cartesia.ai/startups, or claim via partner portals: AWS Startups (startups.aws.com/offers/cartesia-ai) or Google for Startups Cloud Program (cartesia.ai/google-startups).
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Deepgram Startup Program
- **id:** `deepgram-startup-program`
- **url:** https://deepgram.com/startup-program
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $100,000 in Deepgram credits for STT, TTS and Voice Agent APIs. Credits must be used within 12 months. (Separately, a Deepgram-on-AWS variant also offers up to $100k for 12 months.)
- **provide:** Be an AI builder or early-stage startup; the FAQ gates on funding - cross-sources confirm 'less than $10M raised' (page itself asks 'What if I've raised more than $10M?'). Must be in production or planning to launch within the next 6 months, and committed to actively building/engaging with the community. No fee, no equity. Need a free Deepgram account with a Project ID ready.
- **apply:** Create a Deepgram account (console.deepgram.com/signup), then submit the application form via deepgram.com/startup-program describing your startup and how you'll use voice AI.
- **filters:** stage=?; max_age_y=?; max_funding_$m=10; net_new=?; referral=?; self_serve=False

### ElevenLabs Startup Grants
- **id:** `elevenlabs-startup-grants`
- **url:** https://elevenlabs.io/startup-grants
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** 33 million characters of audio-generation credits (equiv. to 680+ hours of Conversational AI audio), free for 12 months across the platform.
- **provide:** Startups/small companies with fewer than 25 employees, anywhere in the world. Must have a clear business/monetization strategy and intend to take a product to market long-term (one-off projects/campaigns rejected). Agencies and consulting firms NOT eligible. Existing ElevenLabs enterprise customers NOT eligible. One application per company (multiple companies = one app each). If awarded, must display the 'ElevenLabs Grants' logo + link at the bottom of your website for at least 12 months.
- **apply:** Apply via the form at elevenlabs.io/startup-grants (describe the startup, team, growth plans). Decision within ~1 week.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Hume AI EVI Startup Grant
- **id:** `hume-ai-evi-startup-grant`
- **url:** https://www.hume.ai/grant-program
- **status:** unclear  ·  **confidence:** low  ·  **verified:** 2026-06
- **amount:** 3 months of free / unlimited EVI (Empathic Voice Interface) API usage, plus access to the technical-support Discord channel and co-marketing opportunities. After the 3 months, eligible for highly discounted enterprise plans.
- **provide:** Early-stage startups, pre-seed to Series B; must have a clear use case for empathic voice AI; must not have previously received a Hume AI grant; must commit to integrating EVI within 3 months and provide feedback.
- **apply:** Apply via the application form at hume.ai/grant-program-application (linked from hume.ai/grant-program). Decision within ~2 weeks. (Live status of the form not confirmed.)
- **filters:** stage=pre-seed to series b; max_age_y=?; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Speechmatics Startup Program
- **id:** `speechmatics-startup-program`
- **url:** https://www.speechmatics.com/startup-program
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $50,000+ in credits across batch, real-time, text-to-speech and on-prem products. Plus monthly engineer office hours, priority developer support + Slack channel, beta feature access, and co-marketing. Graduates get heavily discounted enterprise pricing.
- **provide:** Raised less than $10M total; have a functional MVP in production OR a committed launch within 1-2 months; NOT currently on a paid Speechmatics enterprise plan; active development team with a defined ASR use case. A 30-minute qualification call is required. Bonus consideration for regulated industries, underrepresented languages, or accessibility focus. Work email recommended over personal.
- **apply:** Form on speechmatics.com/startup-program (sections: About you / Your company / Use case; collects name, work email, job title, phone, LinkedIn), followed by a qualification call.
- **filters:** stage=?; max_age_y=?; max_funding_$m=10; net_new=?; referral=?; self_serve=?

### Tavus Startups & Grants
- **id:** `tavus-startups-grants`
- **url:** https://www.tavus.io/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** 15,000 conversational video minutes, 25 replicas, and 3 months of full platform access (CVI - real-time conversational video pipeline, 30ms RAG + Memories, 42 languages, SOC2/HIPAA/GDPR/BAA).
- **provide:** Aimed at 'early-stage builders' prototyping a product, embedding Tavus APIs, or building conversational-video features. No formal eligibility criteria published on the page (no stated funding-stage, incorporation, employee/age cap, region limit, or referral requirement). Form requires only First Name, Last Name, Email, Phone.
- **apply:** Embedded form at tavus.io/startups (First/Last name, Email, Phone).
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Vapi for Startups
- **id:** `vapi-for-startups`
- **url:** https://vapi.ai/startups
- **status:** closed  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** When open: 7,500 free minutes per month for 12 months (90,000 minutes/year), vs 100 free minutes/month for regular users. Plus private Slack channel with forward-deployed engineers, early feature access, and community membership.
- **provide:** Startups building voice AI products/features; pre-seed to Series A with $250k+ in funding; projects focused on innovative voice applications; launching to customers within 6 months. Note: meeting criteria does not guarantee acceptance. (Currently moot - applications on hold.)
- **apply:** Normally via the page at vapi.ai/startups, but applications are on hold; no active form/email is presented while paused.
- **filters:** stage=pre-seed to series a; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?


## Перк-стеки

### Brex Startup Perks
- **id:** `brex-startup-perks`
- **url:** https://www.brex.com/support/brex-partner-perks
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Confirmed: AWS up to $5,000 (depending on Activate eligibility); OpenAI $2,500 in API credits for 1 year; Google Cloud up to $200,000 over 2 years; Retool $25,000 (new customers); Carta 20% off year one + waived implementation + 10,000 Brex points; Deel up to $5,000 credits or 50% off year one; Gusto 50% off year one; Slack 30% off Pro/Business+ for 12 months (companies <200 employees); QuickBooks 30% off 12 months; Framer 1 year free. No Azure or Anthropic credits listed.
- **provide:** Must be a Brex customer (open a Brex account) - perks unlock from the Brex dashboard. Some sources note Brex onboarding effectively favors funded startups (commonly cited ~$50k+ in bank for full account access, not stated on the perks page itself). Individual perks add their own conditions: AWS subject to Activate eligibility; Retool new-customers-only; Slack <200 employees. Many require new-customer status with the partner.
- **apply:** In the Brex dashboard, go to Rewards > Perks and discounts and select the partner tiles; each tile shows its own eligibility and redemption instructions.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### HubSpot for Startups
- **id:** `hubspot-for-startups`
- **url:** https://www.hubspot.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Tiered software discount on net-new Professional or Enterprise products only. Funded tier: 90% off year one, 50% off year two, 25% off year three. Partner/organization tier: 30% off year one, 15% off year two. (No cloud/compute credits - this is a discount on HubSpot subscriptions.)
- **provide:** Must qualify via ONE of: (1) Funding - raised Pre-seed, Seed, or Series A but NOT Series B or later, verifiable in Crunchbase or PitchBook (gets the 90% tier); OR (2) Partner - affiliation with an approved HubSpot for Startups partner / approved entrepreneurial organization / accelerator/incubator/VC (gets the 30% tier). Discount applies only to net-new Professional or Enterprise purchases (must not already own those products).
- **apply:** Click 'Check your eligibility' on hubspot.com/startups, answer qualification questions, then create the account and onboard. Partner-affiliated applicants apply through their partner/accelerator.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Mercury Perks (Raise)
- **id:** `mercury-perks-raise`
- **url:** https://mercury.com/perks
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Confirmed: AWS up to $5,000 Activate credits; Microsoft for Startups $5,000+ credits; Google Cloud startup credits; Notion 6 months free; GitHub 1 year free; Stripe Atlas 20% off; Supabase $300; Slack 25% off; Gusto 3 months free; QuickBooks 30% off; Xero 3 months free; plus many 20-80%-off SaaS discounts across dev/AI/HR/sales tools.
- **provide:** Must have (or open) a Mercury business banking account to access the perks marketplace. Per-partner conditions apply: AWS requires business name + email to match the Mercury account, and you are rejected if you have already redeemed $5k+ AWS credits elsewhere (if you redeemed <$5k, you only get the difference up to $5k). Notion/other perks require new-customer status. No explicit funding-stage gate stated for the perks marketplace itself.
- **apply:** Sign up for / log into the Mercury dashboard and redeem each perk from the Perks section; AWS and others have individual redemption flows requiring matching company info.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=?

### Notion for Startups
- **id:** `notion-for-startups`
- **url:** https://www.notion.com/startups
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Free access to the Notion Business plan (normally $20/member/mo) including Notion AI. Tiers: 6 months free (partner-affiliated, <100 employees) - stated up to ~$12,000 value for 100 employees; 3 months free (non-partner, valid business website + company-domain email); 1 month free (SMBs / <10 employees / incomplete business info).
- **provide:** Must be a NEW, non-paying Notion customer (not on a paid plan) and not have received a prior Notion promotion. Work/company-domain email required (no Gmail/Outlook) plus a valid Notion workspace domain and public company website. For the 6-month tier: a partner referral code from Notion's network (VCs, accelerators, AWS Activate, Stripe Atlas, etc.) and <100 employees. Excludes service-based businesses/agencies/consultancies from the longer tiers. Cannot combine offers or use multiple partner codes.
- **apply:** Submit the application at notion.com/startups (notion.so/startups-apply); enter the partner referral code if you have one for the 6-month tier. Processing ~3-5 business days.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=True; referral=?; self_serve=False

### Ramp Partner Perks
- **id:** `ramp-partner-perks`
- **url:** https://ramp.com/rewards
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** $350,000+ total in partner rewards. Confirmed: OpenAI up to $2,500 in API credits; AWS up to $5,000; Datadog up to $100,000; Segment $50,000; Amplitude up to $40,000; Retool $25,000; Google Cloud $350; Stripe $25,000 fee-free processing; HubSpot 30% off year one; QuickBooks 30% off 12 months; Asana 50% off 1 year; Vanta up to 40% off (<25 employees).
- **provide:** Must sign up for Ramp ('Get Ramp today and redeem within the product dashboard'); perks redeemed after account creation. Marketed as available to bootstrapped/pre-seed/seed startups with no VC referral required. The page does not state an explicit funding/employee cap; individual partner perks carry their own conditions (e.g. new-customer status, employee caps like Vanta <25). Account review cited as ~1-2 business days.
- **apply:** Create a Ramp account, then redeem each reward from the Rewards section of the Ramp product dashboard. Individual reward landing pages (e.g. ramp.com/rewards/openai) capture email to start.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=False; self_serve=?

### Stripe Atlas Perks
- **id:** `stripe-atlas-perks`
- **url:** https://support.stripe.com/questions/stripe-atlas-perks-partners
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $50k+ aggregate perks. Confirmed figures: $2,500 Stripe processing credits; AWS Activate $5,000 (new users only); Google Cloud $2,000+ first year; Microsoft Azure $5,000+ (via Microsoft for Startups); Cloudflare $100k; PostHog $50k; Airtable $42k; Notion ~6 months free; Xero 6 months free; Mercury/Brex $1,000+ banking cashback. Partner roster now includes Perplexity. No OpenAI/Anthropic API credits listed here.
- **provide:** Must incorporate a company through Stripe Atlas and have the Atlas application approved. Each partner may impose its own eligibility/compliance rules - e.g. AWS, Google Cloud, Replit require new-customer status. No VC referral needed; the trigger is Atlas incorporation itself.
- **apply:** Redeem from the Perks tab of the Stripe Atlas Dashboard after Atlas application approval. Each perk tile has its own redemption flow. No separate application form.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=False; self_serve=False


## Акселераторы с кредитами

### AI Grant (Friedman & Gross)
- **id:** `ai-grant-friedman-gross`
- **url:** https://aigrant.com/
- **status:** closed  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $250,000 via uncapped SAFE + ~$632K in vendor credits: $350,000 Azure/Microsoft credits plus ~$282,500 in partner credits (Anthropic, OpenAI, Replicate, Modal, PostHog, Vercel, ElevenLabs, etc.). Total package commonly cited at ~$850K.
- **provide:** Pre-seed/seed-stage building anything that meaningfully leverages AI models. No credentials required; solo founders welcome; prior fundraising is OK. Incorporation not required to apply but required if accepted. Open globally.
- **apply:** Application form on aigrant.com when a batch is open (currently closed). Contact: support@aigrant.org (general), sponsorship@aigrant.org (partners). A SparkXYZ-hosted application portal has also been used for prior batches.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### AI2 Incubator
- **id:** `ai2-incubator`
- **url:** https://www.ai2incubator.com/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Pre-seed capital: up to $600K on a SAFE at a $10M cap. Early allocation typically $100K (solo founder) or $200K (cofounding team), topped up to $600K as you hit early traction; mature teams can get the full $600K upfront. Plus up to $1M+ in non-dilutive cloud credits.
- **provide:** Applied-AI founders, earliest stages ('from day one of your idea'); Seattle/Pacific Northwest focus ('doubling down on Seattle'). Technical depth implied but not stated as a hard requirement. Pre-seed stage.
- **apply:** Apply via the form at https://apply.ai2incubator.com/ (linked from aihouse.vc). Rolling admissions.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Berkeley SkyDeck
- **id:** `berkeley-skydeck`
- **url:** https://skydeck.berkeley.edu/apply/
- **status:** closed  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Cohort track: ~20 startups selected per 6-month batch receive a $200,000 investment from the Berkeley SkyDeck Fund, plus 900+ in-kind legal/financial/tech resources from Resource Partners. Pad-13 track: 60-80 teams get resources/access but NO guaranteed investment.
- **provide:** Open globally ('startups from all over the world'); industry-agnostic; Berkeley affiliation NOT required, though UC-affiliated and international startups are a stated priority. Specific stage not mandated. Equity/SAFE terms for the $200K not disclosed on the page.
- **apply:** Apply via the Airtable application form linked from the 'CONNECT'/apply button on skydeck.berkeley.edu/apply; Batch 23 form opens July 20, 2026.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Conviction Embed
- **id:** `conviction-embed`
- **url:** https://embed.conviction.com/
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $250K investment via uncapped, no-discount MFN SAFE + $350K AWS credits + $350K Azure credits + $500K+ other compute/inference/hosting credits (OpenAI, Anthropic, Baseten, Pinecone, Vercel, Weights & Biases) + early access to Mistral models. Class size 10-12 companies.
- **provide:** Very early-stage AI founders (pre-idea through pre-seed). Solo founders welcome (cofounder matching offered); not-yet-incorporated teams encouraged; prior fundraising not disqualifying. No formal credential/experience bar; highly selective (<1% in early batches). Requires attending the in-person SF retreat.
- **apply:** Apply via the form at embed.conviction.com/apply. Questions / cofounder matching: embed@conviction.com.
- **filters:** stage=pre-seed; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Google AI Futures Fund
- **id:** `google-ai-futures-fund`
- **url:** https://labs.google/aifuturesfund
- **status:** active  ·  **confidence:** medium  ·  **verified:** 2026-06
- **amount:** Bundle (no single fixed figure published on the official page): early access to Google DeepMind models (Gemini, Veo, Imagen); hands-on support from DeepMind/Google Labs researchers and engineers; Google Cloud credits + dedicated technical support; and optional direct equity investment from Google 'when you're ready.' Regional co-invest deals cited up to ~$2M (e.g. Google + Accel, India). Google Cloud credits via the broader startup program scale up to $350K but the AFF page itself does not state a credit dollar amount.
- **provide:** Early-to-mid-stage AI startups building products that leverage frontier AI. Global eligibility. Cloud benefits are 'subject to Google Cloud eligibility requirements' (the standard Google for Startups AI tier typically requires seed-Series A funding, founded within ~10 years, use/plan to use Vertex AI or Gemini, and not having received more than a small amount of prior Google Cloud credits) - but the AFF page itself lists no explicit stage/region/incorporation criteria.
- **apply:** Apply via the Google Form linked from the 'Apply now' button on labs.google/aifuturesfund.
- **filters:** stage=seed-series a; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### South Park Commons Founder Fellowship
- **id:** `south-park-commons-founder-fellowship`
- **url:** https://www.southparkcommons.com/founder-fellowship/
- **status:** closed  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** $400K upfront for 7% equity, plus an additional $600K guaranteed in your next external round (so up to $1M of capital). Plus up to $1M in credits and perks from partners (Anthropic, OpenAI, Azure, GCP, AWS, and others).
- **provide:** Pre-revenue, pre-product, even pre-idea founders; selection emphasizes founder-market fit over traction. In-person bootcamp in San Francisco or NYC (residency-based). Equity terms (7%) fixed. No funding-stage proof needed since it targets pre-idea stage.
- **apply:** Apply via the form linked on the southparkcommons.com/founder-fellowship page; Fall 2026 application window opens 'this summer' 2026.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### STATION F F/ai Program
- **id:** `station-f-f-ai-program`
- **url:** https://stationf.co/news/f-ai
- **status:** closed  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Not quantified on the official announcement. Provides selected startups direct access to partners' advanced tools, internal expertise, senior leadership, and global networks (and the Station F campus environment). No specific compute-credit, GPU, or cash figures published.
- **provide:** Early-stage AI-native startups with strong technical/research foundations and a clear path to commercialization; expected to reach meaningful revenue milestones (incl. the ~EUR 1M mark within six months). Selection weighted to team + technology, favoring repeat founders and PhDs. Cohort of 20.
- **apply:** No open application form - admission is by recommendation/referral only (invitation-based). No public apply URL.
- **filters:** stage=?; max_age_y=?; max_funding_$m=?; net_new=?; referral=?; self_serve=False

### Vercel for Startups
- **id:** `vercel-for-startups`
- **url:** https://vercel.com/startups/credits
- **status:** active  ·  **confidence:** high  ·  **verified:** 2026-06
- **amount:** Up to $30,000 in Vercel platform credits, per the official credits page. (Third-party aggregators cite higher 'up to $200K' figures, but that is unverified and not stated on Vercel's own page - treat $30K as the confirmed amount; exact credit/Pro duration not specified on the page.)
- **provide:** Must be BACKED BY one of Vercel's 100+ approved venture/accelerator partners (Y Combinator and many VC firms). Partner verification is MANDATORY: applicant must upload a screenshot of the full browser window showing the Vercel Credit offer from their partner's dashboard. The page does not explicitly state employee caps, company-age caps, funding-stage minimums, or a net-new/no-prior-credits rule; third-party sources describe it as pre-seed through Series A, global.
- **apply:** Apply directly via the form on vercel.com/startups/credits (requires a logged-in Vercel account; submit email, team, partner selection, country, and the partner-offer screenshot). Alternatively claim through your accelerator/VC's partner perk portal.
- **filters:** stage=pre-seed through series a; max_age_y=?; max_funding_$m=?; net_new=?; referral=True; self_serve=?
