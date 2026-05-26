# Research Notes — May 2026 Platform Landscape

**For:** claude-ads v1.8.0
**Baseline:** v1.7.1 (released May 18, 2026)
**Compiled:** May 26, 2026
**Author:** research synthesis, primary-source cited

---

## Purpose

This file captures the May 2026 paid-advertising landscape deltas that post-date the v1.7.0 cut (May 17, 2026) and the v1.7.1 polish release (May 18, 2026). It is the input dossier for the v1.8.0 check additions, reference-doc rewrites, and CHANGELOG entry.

Every claim in this file cites a primary source (vendor blog, official press release, regulatory body, or earnings call). Where a number is contested or only available via practitioner reporting, it is flagged inline.

---

## Audit observation flagged before we go further

**The CHANGELOG.md on `main` is stale.** As of May 26, 2026 the file ends at v1.5.1 (April 14, 2026). v1.6.x and v1.7.x entries exist only via GitHub Releases tab. The `[Full changelog]` link inside the v1.7.0 release notes points to a `#170---2026-05-17` anchor that does not exist in the published file. **v1.8.0 should backfill v1.6.0, v1.7.0, v1.7.1 entries into CHANGELOG.md** so the file matches the release tags. See the proposed CHANGELOG.md entry produced alongside this file.

---

## What's already in v1.7.1 (do NOT re-add)

These items were already shipped in v1.7.0 (May 17, 2026) per the official release notes, and are not new audit gaps:

- `/ads amazon` sub-skill (Sponsored Products / Brands / Display, ACOS / TACOS, search-term harvesting)
- `/ads attribution` sub-skill (AdAttributionKit + GA4 + Consent Mode V2 + MMP health)
- `/ads server-side-tracking` sub-skill (sGTM, CAPI Gateway, event_id dedup, PII hashing discipline)
- `/ads google` AI Max era rewrite (`ai_max_setting.enable_ai_max`, AI Brief, FUE, brand exclusions) — needs **GML 2026 addendum** since GML happened 3 days after v1.7.0 shipped
- `/ads meta` Andromeda + GEM + Lattice era rewrite — needs **Q1 2026 metric refresh** and **ARM (Adaptive Ranking Model) addition**
- Cross-runtime install matrix (claude / codex / cursor / windsurf / gemini / goose)
- 41-test pytest eval harness with bidirectional 209-check catalog coverage
- 10-Principle Thinking Framework (OBSERVE × 2 / LISTEN / THINK / CONNECT × 2 / FEEL / ACCEPT / CREATE / GROW)

Verified check counts in `tests/fixtures/check-catalog.yaml` (per repo description): Google 80, Meta 50, LinkedIn 27, TikTok 28, Microsoft 24 = 209 verified. Apple, Amazon, Cross-platform, Attribution + Server-side use inline SKILL.md thresholds (Wave 3 will catalog these).

v1.7.1 itself (May 18, 2026) was a polish release: animated SVG banner, branding kit, SSS+ tier README rewrite, 10 factual citations fixed against primary sources in `ads-meta` / `ads-apple` / `ads-budget` / `ads-google` / `ads-microsoft` / `ads-creative`. No new sub-skills, no new agents, no script behavior changes.

---

## Genuinely new — what v1.8.0 should add

### 1. Google — Google Marketing Live 2026 (May 20, 2026)

**Source:** [blog.google/products/ads-commerce/google-marketing-live-2026-collection/](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/) (Vidhya Srinivasan, May 20, 2026)

GML happened 3 days **after** v1.7.0 cut and 2 days **after** v1.7.1 cut. None of these are reflected yet in the skill.

| Check ID | Status | Item |
|---|---|---|
| G81 | GA (beta, English globally) | **Ask Advisor** — unified Gemini agent spanning Google Ads + Google Analytics + Google Marketing Platform + Merchant Center. Absorbs Ads Advisor, Analytics Advisor, and the forthcoming Merchant Center agent. Audit check: detect adoption + verify it's not running unattended write actions. |
| G82 | Announced (pilot in education, automotive, real estate) | **Business Agent for Leads** in AI Mode — verticalized lead-gen agent inside AI Mode chat surfaces. Requires AI Max or Performance Max. |
| G83 | Announced | **Direct Offers expansion** with promotion bundling + native checkout for UCP merchants + travel expansion (Booking, Expedia) |
| G84 | Announced | **AI Mode ad formats** — Conversational Discovery ads, Highlighted Answers, AI-powered Shopping ads. AI Mode 1B MAU, AI Overviews 2.5B MAU per Google I/O May 19, 2026. |
| G85 | Beta May 7, 2026 | **Journey-aware bidding** — learns from both biddable AND non-biddable conversion goals (phone calls, form submissions, newsletter signups) |
| G86 | Expanding to PMax + Shopping | **Smart Bidding Exploration** — was Search-only, now expanding to Performance Max + Shopping. +27% unique converting users per Google. |
| G87 | GA | **Campaign total budgets** — 66% reduction in manual budget adjustments per Google |
| G88 | GA | **Demand-led pacing** — Google AI optimizes spend to follow consumer demand within monthly budget |
| G89 | Integrated GA360 | **Meridian in Google Analytics 360** — open-source MMM brought inside GA360; Meridian GeoX + Meridian Studio + Data Manager Map View |
| G90 | Announced | **Qualified Future Conversions (QFCs)** — Gemini-powered, predicts up to 6 months ahead |
| G91 | New metric | **Attributed Branded Searches** |
| G92 | Summer 2026 GA | **Asset Studio Gemini Omni (Flash)** — any-input-any-output (text/image/video); 1-Click Creative Testing; Veo + Nano Banana; Adobe + Canva pull-through; Asset Studio API |
| G93 | Live | **Demand Gen** — multimodal video creation, creator partnership boost in asset picker, Merchant Center video distribution, Google Maps inventory, checkout links to 9 new markets, product feeds expanded to automotive (+33% conversions per Google), one-click Demand Gen from PMax, Campaign Type Attribution, Uplift Experiments, TransUnion integration |
| G94 | April 21, 2026 | **Ads Advisor 3 agentic safety features** — real-time policy reviews, security monitoring, instant certifications |
| G95 | **HARD GATE — Sept 2026** | **DSA → AI Max forced migration** — Google's April 15, 2026 announcement: "Starting in September, remaining eligible Search campaigns with legacy settings will automatically upgrade to AI Max, and advertisers will no longer be able to create new campaigns with DSA via Google Ads, Google Ads Editor, or the Google Ads API." No opt-out. Practitioner Black Friday risk flagged (Digital Applied, NateCue, ALM Corp), not in Google's announcement. |

**Cases to update benchmarks.md:** Lufthansa +24% AI Max ROAS, IKEA +65% non-brand / +28% incremental ROAS, AI Max users +15% conversions at similar ROAS, Crew Clothing +70% long-term conversions, Doc Martens +16% revenue from first-party data, Demand Gen +33% conversions with feeds. **Flag as Google-supplied case studies, not independently audited** — JumpFly's April 2026 analysis and 84% advertiser survey show neutral-to-negative results.

### 2. Meta — official MCP + March 3 attribution rebuild

#### 2a. Meta Ads AI Connectors (Official MCP) — April 29, 2026

**Source:** [facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors); Search Engine Land coverage (Anu Adegbola)

| Check ID | Status | Item |
|---|---|---|
| M51 | GA (open beta global) | **Meta Ads MCP server live at `mcp.facebook.com/ads`** — 29 tools across 5 categories (campaign management, product catalog, accounts/assets, datasets/tracking, insights/benchmarks). Supports Claude, ChatGPT, Perplexity (added May 2026), Codex, Claude Code. Meta Business OAuth — no Developer App, no App Review required. Rate limit ~200 calls/hour per ad account. |
| M52 | Default behavior | **Paused-by-default safety** — all MCP-created campaigns launch in PAUSED state. Audit check: enforce this is honored and write-action governance is in place. |
| M53 | **CRITICAL warning** | **SurfaceLabs cautionary tale** (April 2026) — account permanently banned after one week of running autonomous campaigns via unofficial connector. Aggressive rapid API calls + frequent budget adjustments triggered Meta fraud detection. No appeal. Audit policy: **read-only (`ads_read`) scope first; write actions (`ads_management`) only after human approval gate**. |

#### 2b. March 3, 2026 attribution rebuild

**Source:** [facebook.com/business/news/click-attribution](https://www.facebook.com/business/news/click-attribution) (March 3, 2026); Search Engine Land coverage by Anu Adegbola

Verbatim from Meta's blog:
> "We are shifting conversions that came from a share, save, or other non-link click actions to be included in engaged-view attribution… we are also renaming engaged-view attribution, and going forward, it will be known as engage-through attribution."
> "46% of online purchase conversions with Reels now happen within the first 2 seconds of attention on our video ads… we have updated the definition for an engaged view for a video ad from 10 seconds to 5 seconds."
> "We also are starting to partner with third party analytics providers, such as Northbeam and Triple Whale, to incorporate both clicks and views into their attribution model."

| Check ID | Status | Item |
|---|---|---|
| M54 | Live March 3, 2026 | Click-through now counts ONLY link clicks (websites, apps, lead forms, destinations) |
| M55 | Live March 3, 2026 | **Engage-through attribution** new column — likes, expansions, video views, shares, saves, comments |
| M56 | Live March 3, 2026 | Engaged-view threshold dropped 10s → **5s** |
| M57 | Live March 3, 2026 | Default attribution: 7-day click, 1-day engage-through, 1-day view |
| M58 | **YoY warning** | YoY data not comparable to pre-March-3-2026 baselines — audit must flag this in any reporting view |
| M59 | Live | Northbeam + Triple Whale partnerships for view-through integration |

#### 2c. Meta AI stack — Q1 2026 refresh + ARM addition

**Source:** [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/); Meta Performance Marketing Summit (San Jose, 2026); Meta Q1 2026 earnings call

The v1.7.0 `/ads meta` rewrite covers Andromeda + GEM + Lattice. **Updates needed:**

| Check ID | Status | Item |
|---|---|---|
| M60 | Q1 2026 update | **GEM Q1 2026:** +13% CTR / +16% CVR on tested accounts; "4× more efficient" than prior ranking models per Meta |
| M61 | Q1 2026 update | **Lattice Q1 2026:** +6% landing-page-view ad CVR (in addition to original +12% ad quality / +6% conversions); 20% infrastructure capacity savings; rolling Lattice to app ads drove ~3% gain in conversions (Q3 2025 earnings) |
| M62 | Q1 2026 update | **Andromeda compute tripled** per Meta's January 2026 disclosure |
| M63 | **NEW — newest layer** | **ARM (Adaptive Ranking Model)** — newest layer in Meta's AI stack. Targets users with long interaction histories. +3% CVR, +5% CTR in early testing per Meta Performance Marketing Summit. Removes the truncation ceiling for high-value users. Audit check: detect ARM eligibility (broad audiences with deep history). |
| M64 | Q4 2025 model | **Incremental Attribution Q4 2025 model: +24% incremental conversions vs. standard attribution** per Meta about.fb.com January 2026 post |

#### 2d. Other Meta May 2026

| Check ID | Status | Item |
|---|---|---|
| M65 | Mid-rollout May 2026 | Ad-level placement control (was ad-set level only) |
| M66 | Mid-rollout | AI-generated Instant Forms from URL/prompt |
| M67 | **Privacy/governance** | **730-day purchase audience retention** — up from 180 days with auto-expansion. Audit flag: detect, surface to user, recommend explicit review |
| M68 | **Privacy/governance** | **New Pixel "auto-include detailed page/product info" setting** — often default ON; sends product/page metadata to Meta. Audit flag: detect setting, recommend explicit governance review |
| M69 | Live | Advantage+ Creative Image Generation Categories: "Refined product look", "Popular in your niche", "High ROAS" |
| M70 | **HARD GATE — June 22, 2026** | **Comscore Markets® replacing Nielsen DMA for automotive model ads — cutoff June 22, 2026**. Per Meta for Developers blog (Patrick Opoosun, March 13, 2026): "Beginning on June 22, 2026, we will discontinue the use of Nielsen's Designated Market Area (DMA) for automotive model ads. Comscore Markets®, which we introduced in August 2025, will serve as the replacement solution. After this date, campaigns still using Nielsen's DMA for automotive model ads targeting will be paused and require an update to Comscore Markets® to resume delivery." The `dma_code` field is replaced by `comscore_market_codes`. Automotive industry template must add a P0 check. |
| M71 | Mid-2026 | **DST pass-through fees up to 5%** in Austria, France, Italy, Spain, Turkey, UK |
| M72 | One-click setup April 2026 | **CAPI one-click setup** — already covered in `/ads server-side-tracking`; audit check: verify it's been enabled and EMQ ≥ 7 |

### 3. TikTok — TikTok World 2026 (May 13–15, 2026)

**Source:** [newsroom.tiktok.com](https://newsroom.tiktok.com/) TikTok World 2026 announcements; Adweek + AdExchanger coverage

Happened 4–2 days before v1.7.0 cut, so likely not in `/ads tiktok` yet.

| Check ID | Status | Item |
|---|---|---|
| T29 | Announced | **TikTok Ads MCP Server (official)** — third-party AI agents (Claude / ChatGPT) plan, launch, optimize campaigns autonomously. Last of the four majors to ship MCP. |
| T30 | Announced | **TikTok Ads Skills** — developer building blocks for campaign creation, performance insights, creative analysis, audience discovery, budget optimization |
| T31 | Q2 2026 global | **Smart+ One Buying Experience** — module-level automation control: turn automation on or off per module (targeting / budget / placements). Smart+ label appears on each module in UI. Audit must recognize module-level granularity. |
| T32 | Live | Smart+ **Music Autofix** (licensing) |
| T33 | Live | Smart+ creative reporting, multi-URL support, higher asset group limit |
| T34 | Live | Smart+ available for app install / app-event optimization (new objectives) |
| T35 | Announced | **TopReach + Creative Sequencing** — TopView + TopFeed unified buy with narrative sequencing |
| T36 | Announced | **Branded Buzz** — large-scale creator collaboration format |
| T37 | Announced | **Search Hubs** — brand-owned sponsored pages prioritized at top of TikTok search results |
| T38 | Announced | **Symphony AI updates**: Dreamina Seedance 2.0 (ByteDance video gen) integrated; Reference to Video for prompt-driven moment-specific generation |
| T39 | Announced | **TikTok GO** — full holiday booking (partners: Booking.com, Expedia, Viator, GetYourGuide, Tiqets, Trip.com) |
| T40 | Announced | **Mini Series & Mini Games**, Growth Max for Mini Games |
| T41 | US Q2 2026 | **Collage Carousel** — hero + 3 product visuals |
| T42 | Announced | **One Asset Manager** — unified asset management across formats |
| T43 | Announced | **View+ for Pulse Core Max** — premium reach upgrade |
| T44 | Announced | **TikTok Market Scope** — competitive intelligence tool |
| T45 | Live | **TikTok Real** (counterfeit / IP protection) + UK Ad-Free Subscription £3.99/month (opts users out of advertising data use) |
| T46 | Live | **GMV Max expansion** to more markets |

**TikTok divestiture status:** TikTok USDS Joint Venture LLC closed January 22, 2026. Oracle 15% / Silver Lake 15% / MGX 15% / ByteDance 19.9% / other US investors ~30.1%. 80.1% non-Chinese ownership. Oracle hosts US data in Oracle US cloud. Algorithm retrained on US data only. CEO Adam Presser; CSO Will Farrell. **No measurable disruption to advertiser operations** — audit should note this for any user worried about TikTok exit risk.

**Revenue benchmarks (for benchmarks.md):** TikTok 2025 global ad revenue ≈ $33.1B (Business of Apps, January 2026); eMarketer 2026 projection ≈ $34.8B. **Higher figures circulating in secondary compilations ($43.5B+) are not confirmed by a primary source** — flag as practitioner speculation.

### 4. LinkedIn — Off-Platform Event Ads + Campaign Manager rename

**Source:** [linkedin.com/help/lms/answer/a10264811](https://www.linkedin.com/help/lms/answer/a10264811); Danielle Webb LinkedIn Marketing Solutions blog (April 28, 2026)

| Check ID | Status | Item |
|---|---|---|
| L28 | Full rollout May 6, 2026 | **Off-Platform Event Ads** — Event-format ad without requiring a LinkedIn Event Page. Supports webinars, field events, hybrid. Lead Gen Objective syncs directly to Salesforce / HubSpot / Marketo. Event clipping for post-event nurture. First-party integrations: Cvent (LinkedIn Audience Connector), ON24, Integrate. B2B/SaaS industry templates need this. |
| L29 | Rolling 2025→2026 | **Campaign Manager terminology rename**: "Campaign Group" → "Campaign"; "Campaigns" → "Ad sets". **API kept old terminology** (`adCampaignGroups`, `campaignGroup`, `campaign`). UI/API mismatch is a UTM tag mapping trap. Audit must check for and warn about. |
| L30 | Live | Accelerate auto-campaign creation |
| L31 | Live | AI Ad Variants from one input |
| L32 | Live | Career Journey targeting — recent promotions, new job placements |
| L33 | Live | Reserved Ads (premium guaranteed inventory) |
| L34 | Live | First Impression Ads (premium first-position) |
| L35 | Live | BrandLink expansion |
| L36 | Live | Wire — short-form B2B video |
| L37 | Live | Thought Leader Event Ads |
| L38 | Live | CTV expansion |
| L39 | Live | Company Attribution in Revenue Attribution Report |
| L40 | Pursuing | MRC accreditation for video metrics |
| L41 | May 2026 | **Company Intelligence API** |
| L42 | Arriving 2026 | Flexible Ad Creation |
| L43 | SMB April 2026 | Auto-targeting and Draft with AI |
| L44 | Live | Real-time CRM data in Campaign Manager |
| L45 | May 6, 2026 | **Ads Agency Certification** global credential — requires Business Manager, invoicing, Marketing Academy completions |
| L46 | Algorithm 2026 | **Depth Score algorithm** — weighs time-on-content; engagement pods penalized; AI-written posts filtered; external links reduce organic reach 30–50% |

**Benchmarks (Dreamdata LinkedIn Ads Benchmarks Report 2026):** 121% ROAS, 272-day average B2B customer journey. LinkedIn ad costs $5–15 CPC vs. other platforms $1–3 CPC.

### 5. Microsoft — Activate 2026 + AI Max for Search pilot

**Source:** [about.ads.microsoft.com](https://about.ads.microsoft.com/) (April 22, 2026); Activate 2026 (May 19, 2026)

| Check ID | Status | Item |
|---|---|---|
| MS25 | Pilot May 2026 | **Microsoft AI Max for Search** — pilot opens May 2026. Distinct from Google's AI Max. Expands query matching across Copilot Search, Copilot Answers, Bing. Guardrails: brand inclusions/exclusions, term exclusions, messaging constraints. Search term + asset reporting at launch. Early adopters +5% CTR; PMax users see +8% incremental conversions. |
| MS26 | Live | **Offer Highlights** — product details (free shipping, in-store pickup) inside Copilot conversations. Best Buy launch partner. English-speaking retail. |
| MS27 | Closed pilot US + Canada | **Audience Generation** — plain-language → targeting (demographics, locations, in-market signals) |
| MS28 | April 2026 | **Performance Max transparency** — Final URL reporting; spend / impressions / clicks / ROAS by Final URL |
| MS29 | Live | **Clarity AI Visibility** — reports how brands appear in AI interfaces (citations, presence) |
| MS30 | Live | **Brand Agents** — embed on Shopify / WooCommerce |
| MS31 | Live April 22, 2026 | **UCP support in Merchant Center** (US live April 22, 2026); Shopify Catalog real-time sync |
| MS32 | Live | **Copilot Checkout** — 500,000+ US merchants; Target Circle loyalty linking launch partner |
| MS33 | Live | **Rewarded Portals** — in-game ad format with opt-in engagement |
| MS34 | New | **Import Center** (consolidated import workflow) |
| MS35 | Updates | Automated bidding updates + custom columns |
| MS36 | Diagnostic | **Performance Shift Root Cause Analysis** (Copilot-driven) |
| MS37 | Diagnostic | Conversion Tracking Diagnostics |
| MS38 | Live | Data-Driven Attribution |
| MS39 | Live | Conversion API (CAPI) server-to-server |
| MS40 | Brand Kit | Ad Studio Brand Kit |
| MS41 | API deprecation | **SOAP API deprecation** in favor of REST |

### 6. Apple — Multiple Search Ad Placements + iOS 26

**Source:** 9to5Mac (Jan 22, 2026); Apple Ads documentation (Dec 18, 2025); WWDC 2025 [developer.apple.com/videos/play/wwdc2025/221/](https://developer.apple.com/videos/play/wwdc2025/221/)

| Check ID | Status | Item |
|---|---|---|
| A36 | Rollout March 3, 2026 | **Multiple Search Ad Placements** — UK and Japan first; global rollout by end of March 2026 to all 91 Apple Ads markets. Up to 2 ads per single search query. Existing campaigns auto-enrolled. iOS 26.2 / iPadOS 26.2+ required. **No position-level reporting initially in AdAttributionKit** — audit must caveat any TAP placement-coverage report. |
| A37 | Live April 10, 2025 | App Store registered with AdAttributionKit |
| A38 | WWDC 2025 / iOS 18.4+ | **AdAttributionKit features** (already in `/ads attribution`, refresh): configurable attribution windows per ad network / interaction / global; configurable cooldowns to prevent install/re-engagement cannibalization; country codes in postbacks (subject to crowd anonymity); overlapping re-engagement conversion windows via Conversion Tags; Development Postbacks test tool |
| A39 | iOS 18.4+ | **Custom Product Pages replace Creative Sets** — up to 35 per app |
| A40 | iOS 26 (Sept 15, 2025) | **Advanced Fingerprinting Protection (ATFP)** default ON in **all** Safari browsing (was Private only). Per WebProNews early tests: up to 90% reduction in fingerprinting effectiveness. **Affects ALL iOS attribution pipelines, not just Apple Ads.** |
| A41 | iOS 26 | **Expanded Link Tracking Protection** strips gclid / fbclid / msclkid in **all** Safari browsing (was Private + Mail only). Server-side tracking now mandatory for iOS Safari conversion measurement. |
| A42 | June 2026 (forecast) | **WWDC 2026 watch list** — likely AdAttributionKit evolution (further window/cooldown granularity); possible SKAN sunset roadmap; iOS 27; possible Apple News ad expansion. Schedule v1.8.x addendum within 14 days of keynote. |

### 7. Amazon — already in v1.7.0; deltas to add

**Source:** [advertising.amazon.com/resources/whats-new](https://advertising.amazon.com/resources/whats-new); unBoxed 2025 (Nashville, Nov 11–12, 2025); unBoxed Toronto (Feb 25, 2026)

`/ads amazon` shipped in v1.7.0 with Sponsored Products / Brands / Display / ACOS / TACOS / search-term harvesting. The following items should be added or updated:

| Check ID | Status | Item |
|---|---|---|
| AMZ-new-1 | Live early 2026 | **Unified Campaign Manager** — Sponsored Ads + Amazon DSP in single platform (announced Nov 11, 2025). **15 months daily data + 6 years monthly data.** |
| AMZ-new-2 | Live | **Ads Agent** — conversational chat assistant for campaign creation, targeting, AMC analytics |
| AMZ-new-3 | Expanded Nov 11, 2025 | **Creative Agent** — agentic AI ad creation; expanded to support Streaming TV and Sponsored TV |
| AMZ-new-4 | Announced 2026 | **Full-Funnel Campaigns** — new AI campaign type across Sponsored Products, Sponsored Brands, display, streaming TV |
| AMZ-new-5 | Early 2026 | **MTA (Multi-Touch Attribution)** deployed across Campaign Manager |
| AMZ-new-6 | Live | **Sponsored Products Video in search results** |
| AMZ-new-7 | Live | **Reimagined homepage hero placement** + **Top-of-search pre-purchase** |
| AMZ-new-8 | Closed Nov 13, 2025 / Public Feb 2, 2026 | **Amazon Ads MCP Server** — supports Claude, ChatGPT, Gemini, Amazon Q, Bedrock |
| AMZ-new-9 | Live Jan 28, 2026 | **Sponsored Brands Collections** — minimum 3 ASINs, max 10. Auto (AI) + Manual modes. Up to 1,000 ASIN exclusions in Auto mode. Removes custom headlines, lifestyle images, branded creative. **US only.** Per [advertising.amazon.com/resources/whats-new/sponsored-brands-collections](https://advertising.amazon.com/resources/whats-new/sponsored-brands-collections). |
| AMZ-new-10 | GA March 25, 2026 | **Sponsored Products Prompts & Sponsored Brands Prompts** — moved beta → GA; CPC billing began; dedicated Prompts report (impressions, clicks, orders). Per [advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts](https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts). |
| AMZ-new-11 | Live | **Brand+ prospecting AI** — +71% PDP views, +42% brand discovery, +64% purchases vs. non-Brand+ tactics |
| AMZ-new-12 | Live | **Performance+ conversion AI** — +34% ROAS in-store, +68% CPA improvement off-Amazon |
| AMZ-new-13 | Live | **H&R Block combined Brand+/Performance+ case** — 144% full-funnel CVR lift, 35% CPA improvement |
| AMZ-new-14 | 2026 expansion | **Prime Video ads** — live in 16 countries; 2026 expansion: Belgium, Denmark, Norway, Turkey |
| AMZ-new-15 | Live | **Direct Netflix and Spotify integrations** via Amazon DSP |
| AMZ-new-16 | Live | **NBA on Prime Video** — started October 2025; expanded packages from May 2026 |
| AMZ-new-17 | Live | **Complete TV** — manage streaming TV across Prime Video + premium publishers with linear TV data integration |

**Citation correction for benchmarks.md:** The "+143% click-attributed sales" figure circulating in coverage belongs to **Sponsored Brands Reserve Share of Voice**, NOT Sponsored Brands Collections. Amazon's official Reserve Share of Voice page: "Increased Sponsored Brands top-of-search impression share from 62.7% to 99.3%; Increased click-attributed sales by 143%; Reduced lost top-of-search sales from 10.3% to 0.3%." The "2.5× more unique products purchased with AI version vs. manual" figure is in third-party guides (sentrykit.com) citing beta tests, **not** on Amazon's official launch page. Flag as not-yet-corroborated by primary source.

**Amazon Q3 2025 advertising services revenue: $17.7B (+24% YoY)** per Amazon Q3 2025 10-Q SEC filing (filed October 30, 2025).

### 8. Cross-platform — Reddit, Pinterest, Snap, CTV/OTT

| Check ID | Status | Item |
|---|---|---|
| X01 | Launched January 5, 2026 (CES) | **Reddit Max campaigns** — AI media-buying tool. Brooks Running case: 17% lower CPA, 27% more conversions per Reddit. |
| X02 | Beta May 20, 2026 | **Reddit Dual Attribution** — combines Reddit first-party + MMP + SKAdNetwork last-touch in single Ads Manager view ("industry-first" per Reddit). |
| X03 | GA May 20, 2026 | **Reddit App Event Optimization** — 22% average CPA improvement |
| X04 | Live | **Reddit app installs +129% YoY** Q1 2025 → Q1 2026 |
| X05 | Live | **Reddit Top Audience Personas** — AI-clustered behavioral segments from 23B+ posts and comments |
| X06 | Announced Dec 11, 2025; closed Feb 2026 | **Pinterest acquires tvScientific** — CTV performance advertising; 95% of AVOD audience reach |
| X07 | Launched April 27, 2026 | **Pinterest CTV Audiences** — combines Pinterest 600M MAU intent with tvScientific CTV reach |
| X08 | Live | **Snap Smart Campaign Solutions** — Smart Bidding (CPA target), Smart Budget (alpha), Smart Targeting (+8.8% conversions), Smart Ads (early test) |
| X09 | Live globally | **Snap Sponsored Snaps** — 22% more conversions, ~20% lower CPA vs. other inventories; +7% CTR / +17% click-through purchases Q3→Q4 2025 |
| X10 | April 28, 2026 alpha | **Snap AI Sponsored Snaps** — brand AI agents in Chat (Experian alpha partner). 950B+ Q1 2026 chats; 500M+ My AI users. |
| X11 | Live | **Snap Q4 2025: 946M MAU; 28% YoY advertiser growth; +89% YoY app ad revenue Q4** |
| X12 | Forecast 2026 | **CTV growth 14.5% to $37.95B** per eMarketer December 2025 |
| X13 | Live | **YouTube ~12% CTV market share, ~$9.21B net CTV ad sales** per eMarketer |
| X14 | Live | **Streaming captured 47.5% of US TV viewing in December 2025** per Nielsen The Gauge™ (January 20, 2026) |
| X15 | 2026 | **Disney+/Hulu integration** combining two of the largest ad-supported streaming audiences |
| X16 | 2026 doubling | **Netflix ad revenue $1.5B 2025, doubling 2026** per Netflix Q4 2025 earnings (co-CEO Greg Peters) and SEC Form 8-K |
| X17 | Live | **2026 US midterms** driving political CTV spend |

### 9. Universal Commerce Protocol + agentic commerce

**Source:** [blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/](https://blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/) (Sundar Pichai, January 11, 2026)

| Check ID | Status | Item |
|---|---|---|
| X18 | Launched NRF Jan 11, 2026 | **Universal Commerce Protocol (UCP)** — co-developers Shopify, Etsy, Wayfair, Target, Walmart. 20+ endorsers including Visa, Mastercard, American Express, Stripe, Adyen, PayPal, Home Depot, Best Buy, Macy's. Joined later: Amazon, Meta, Microsoft, Salesforce. |
| X19 | Rolling out May 19, 2026 (Google I/O) | **Universal Cart** in US; expanding to Canada, Australia, UK and into food delivery, travel |
| X20 | Merchant Center | `native_commerce` Merchant Center attribute is the eligibility field |
| X21 | Donated April 28, 2026 | **Agent Payments Protocol (AP2)** donated to FIDO Alliance |
| X22 | Spec 2026-04-08 | Compatible with A2A, MCP. Discovery via `/.well-known/ucp` JSON manifest. RS256/ES256 signing keys. Webhook endpoints for order lifecycle. |
| X23 | Live | **Shopping Graph 60B+ listings** per Google |

### 10. IAB Tech Lab — AAMP + Agent Registry

**Source:** [iabtechlab.com/introducing-the-iab-tech-lab-agent-registry/](https://iabtechlab.com/introducing-the-iab-tech-lab-agent-registry/)

| Check ID | Status | Item |
|---|---|---|
| X24 | Named February 26, 2026 | **AAMP (Agentic Advertising Management Protocols)** — IAB Tech Lab umbrella framework. Three pillars: execution, protocols, Agent Registry. Built on OpenRTB, AdCOM, OpenDirect, VAST, GPP, TCF wrapped in MCP / A2A. Named by CEO Anthony Katsur. |
| X25 | Launched ~March 1, 2026 | **IAB Tech Lab Agent Registry** — 10 active MCP entries by March 11, 2026: Amazon Ads MCP, Burt Intelligence (EU + US), HyperMindZ Campaign Orchestrator, Mixpeek, Optable, IAB Tech Lab Agent Registry MCP, Dstillery, PubMatic, Equativ. Zero A2A entries. Each company validated against GPP & TCF ID. Numbers increasing — re-verify at ship time. |

---

## Compliance / regulatory — the five hard clocks

### 11. EU AI Act Article 50 — August 2, 2026 (or December 2, 2026 for watermarking)

**Source:** [artificialintelligenceact.eu/article/50/](https://artificialintelligenceact.eu/article/50/); European Commission digital-strategy.ec.europa.eu Code of Practice page; Latham & Watkins client alert May 2026

| Check ID | Status | Item |
|---|---|---|
| C01 | Effective August 2, 2026 | **Article 50 transparency obligations**: providers must mark generative AI outputs in machine-readable format (audio, image, video, text) and detectable as artificially generated; deployers must disclose deepfakes and AI-generated text on matters of public interest; heightened standard for deepfakes (Article 50(4)); chatbots must disclose at first interaction |
| C02 | Political agreement May 7, 2026 | **AI Act Omnibus grandfathering**: generative AI systems placed on market before August 2, 2026 must comply with watermarking requirements only as of **December 2, 2026**. Subject to formal adoption (expected by July 2026). |
| C03 | Penalties | **Up to €15M or 3% global annual turnover**, whichever is higher |
| C04 | Code of Practice | First draft Dec 17, 2025; second draft March 2026; **final expected June 2026**. Multi-layered watermarking required (metadata + imperceptible + logging/fingerprinting); no single technique sufficient. |
| C05 | Audit gates for advertisers | Providers (Adobe Firefly, DALL·E, Midjourney) must embed watermarks at generation; **deployers** (marketing teams using AI visuals) must preserve them, disclose AI-generated visuals, implement internal governance |

### 12. US state privacy laws

**Sources:** [iapp.org](https://iapp.org/); [multistate.us](https://www.multistate.us/); Greenberg Traurig, Nelson Mullins, Hunton, Consenteo client alerts

| Check ID | Status | Item |
|---|---|---|
| C06 | March 2026 | **20 states with comprehensive privacy laws**: CA, CO, CT, DE, IN, IA, KY, MD, MN, MT, NE, NH, NJ, OR, RI, TN, TX, UT, VA, WA |
| C07 | May 2026 | **22 states by May 2026**: Oklahoma added (signed March 20, 2026, effective January 1, 2027); Alabama added (signed April 17, 2026, effective May 1, 2027) |
| C08 | Effective dates | New 2026 effective dates: Indiana, Kentucky, Rhode Island (January 1, 2026); Connecticut amendments + Arkansas + Utah amendments (July 1, 2026); California data broker registration updates (August 1, 2026) |
| C09 | 12 states by January 1, 2026 | **GPC honoring required**: CA, CO, CT, MT, NE, NH, NJ, MN, MD, DE, OR, TX |
| C10 | October 2025 → January 1, 2027 | **California Opt Me Out Act** — all web browsers must send GPC by January 1, 2027 |
| C11 | **Effective Jan 1, 2026** | **CCPA §7025(c)(6) visible-confirmation rule** — "A business must display whether it has processed the consumer's opt-out preference signal as a valid request to opt-out of sale/sharing on its website" |
| C12 | September 9, 2025 | **Joint CA + CO + CT AG enforcement sweep** targeting GPC compliance |
| C13 | **Effective July 1, 2026** | **Connecticut neural data** (SB 1295, signed June 24, 2025): "Neural data means any information that is generated by measuring the activity of an individual's central nervous system." Sensitive data category triggers law applicability with **no volume threshold**. Other additions: transgender/nonbinary status, financial account data, government ID numbers. |
| C14 | Sensitive data expansion | Across states: precise geolocation (within 1,750 feet), health inferences, neural data |
| C15 | "Sharing" redefinition | Some states: lookalike audience data transfers count as "sharing" even when no money changes hands |
| C16 | Effective April 2026 (newly collected data) | **Maryland Online Data Privacy Act (MODPA)** — strictest data minimization in US; "reasonably necessary" standard; bans selling sensitive data regardless of consent; bans targeting under-18s |
| C17 | January 1, 2026 | **California Delete Act DROP platform** launched; $200/day compounding fines per unfulfilled deletion request from January 31, 2026 |

**Enforcement track record (for `audit-compliance` agent):**

| Case | Amount | Date | Reason |
|---|---|---|---|
| Sephora | $1.2M | August 2022 | Earliest CCPA enforcement |
| Healthline Media | $1.55M | July 2025 | Failure to honor GPC + misuse of health data for advertising |
| Tractor Supply | $1.35M | September 2025 | Largest CPPA fine to date |
| Jam City | $1.4M | November 2025 | Children's data |
| **Disney** | **$2.75M** | **February 2026** | **Largest CCPA AG settlement to date — §7025(c)(2) cross-account propagation violation** |
| **Ford** | **$375,703** | **March 2026** | **CPPA — remedial obligation: audit every tracking technology** |
| Texas (major tech co.) | $1B+ | 2025–2026 | Texas Data Privacy and Security Act |

### 13. Privacy Sandbox shutdown

**Source:** [privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies) (Anthony Chavez, October 17, 2025)

| Check ID | Status | Item |
|---|---|---|
| C18 | Retired October 17, 2025 | **APIs retired**: Attribution Reporting API (Chrome + Android), IP Protection, On-Device Personalization, Private Aggregation (incl. Shared Storage), Protected Audience (Chrome + Android), Protected App Signals, Related Website Sets, SelectURL, SDK Runtime, Topics (Chrome + Android) |
| C19 | Remaining | **CHIPS (Cookies Having Independent Partitioned State), FedCM, Private State Tokens** |
| C20 | Live | Third-party cookies remain in Chrome via user-choice model — reliability declining (Safari, Firefox, Brave block by default) |
| C21 | UK CMA | Released Google from Sandbox commitments same day. CMA testing cited 85% attribution inaccuracy and 30% publisher revenue decline during trials. |

### 14. Other regulatory

| Check ID | Status | Item |
|---|---|---|
| C22 | DSA enforcement accelerating 2026 | Ad transparency reporting; targeting prohibitions for minors and sensitive categories; recommender system transparency; VLOP extra obligations. French authorities' Grok deepfake investigation Q1 2026. |
| C23 | HIPAA continued | Healthline Media + Blue Shield California investigations indicate continued health-data enforcement |
| C24 | LegitScript | Required for telehealth, pharmacy, addiction-treatment ads on Google/Meta |
| C25 | Special Ad Categories | Housing, credit, finance, employment, social issues — targeting limitations + disclosures continue 2026 |
| C26 | China PIPL | Cross-border data transfer rules; security assessment for large transfers |
| C27 | Brazil LGPD | ANPD enforcement increasing |
| C28 | India DPDPA | Phased rollout continuing; consent management |
| C29 | TCF v2.3 + GPP | Continue as primary EU consent signaling frameworks; GPP adopted in IAB Agent Registry validation |

---

## Caveats

These are practitioner / analyst figures that should be flagged as not directly corroborated by primary sources:

- **Amazon "+143% click-attributed sales"** for Sponsored Brands Collections — actually Reserve Share of Voice statistic, not Collections.
- **Amazon "2.5× more unique products purchased with AI version vs. manual"** — third-party (sentrykit.com) only; not in Amazon's official launch page.
- **TikTok 2026 global ad revenue projections >$34.8B** — Business of Apps + eMarketer give $33.1B 2025 / $34.8B 2026; higher numbers (MediaMister, SQ Magazine) lack primary source.
- **Google AI Max performance claims** (Lufthansa, IKEA, "15% more conversions") — Google-supplied case studies; JumpFly April 2026 independent analysis + 84% advertiser survey show neutral-to-negative.
- **Meta "year-over-year data not comparable"** — practitioner consensus (Lucid Media, Marketing Code, Leaf Signal); cite as analyst interpretation, not Meta's own language.
- **"Black Friday risk"** of September 2026 Google AI Max forced DSA migration — practitioner concern (Digital Applied, ALM Corp, NateCue), not in Google's announcement.
- **Andromeda performance figures vary widely** across third-party blogs. Primary source: about.fb.com January 2026 + Meta Q3/Q4 2025 earnings transcripts.
- **IAB "10 active MCP entries"** is current as of March 11, 2026; re-verify at ship time.

---

## v1.8.0 release plan (summary)

**Scope:** Substantive Wave 3 release — net-new check additions and reference-doc creation.

**Sub-skills to update:**

| Sub-skill | New checks | Update type |
|---|---|---|
| `/ads google` | G81–G95 (15 checks) | GML 2026 addendum |
| `/ads meta` | M51–M72 (22 checks) | MCP, attribution rebuild, AI-stack Q1 2026 refresh, ARM, automotive cutoff |
| `/ads tiktok` | T29–T46 (18 checks) | TikTok World 2026 |
| `/ads linkedin` | L28–L46 (19 checks) | Off-Platform Event Ads, rename, agency cert |
| `/ads microsoft` | MS25–MS41 (17 checks) | AI Max for Search, Activate 2026 |
| `/ads apple` | A36–A42 (7 checks) | Multi-placement + iOS 26 |
| `/ads amazon` | AMZ-new-1 through 17 | Already in v1.7.0, but UCM / Collections / Prompts / Brand+ / Performance+ adds |
| `/ads attribution` | iOS 26 + Reddit Dual Attribution + Meta March 3 rebuild | Existing in v1.7.0; refresh |
| `/ads server-side-tracking` | UCP / AP2 / IAB Agent Registry | Existing; refresh |
| `/ads compliance` agent (new in audit category) | C01–C29 (29 checks) | **NEW — EU AI Act + US state privacy + Privacy Sandbox + DSA + global** |

**New reference docs:**

- `mcp-integration.md` — rewrite for agentic era
- `compliance-requirements.md` — refactor for the 22-state US + EU AI Act landscape
- `meta-ai-stack.md` — consolidate Andromeda + GEM + Lattice + ARM with Q1 2026 metrics
- `notes-google.md`, `notes-meta.md`, `notes-tiktok.md`, `notes-linkedin.md`, `notes-microsoft.md`, `notes-apple.md`, `notes-amazon.md` — per-platform research notes

**CHANGELOG.md backfill** — restore v1.6.0, v1.7.0, v1.7.1 entries from GitHub Releases (currently missing from `main`).

**Catalog work:** Apple, Amazon, Cross-platform, Attribution + Server-side check counts to land in `tests/fixtures/check-catalog.yaml` (currently inline thresholds in their SKILL.md files).

**Watch list for v1.8.x patches:**

- **WWDC 2026** (June 2026) — AdAttributionKit evolution / SKAN sunset roadmap / iOS 27
- **EU AI Act Omnibus formal adoption** (expected July 2026) — may shift watermarking deadline
- **Meta Comscore Markets cutoff** (June 22, 2026) — automotive industry template P0
- **IAB Agent Registry** count increase — re-verify at ship time
- **OpenAI / Anthropic agent-runtime announcements** that could supersede MCP

---

*End of research notes.*
