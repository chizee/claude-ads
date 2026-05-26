---
name: ads-apple
description: "Apple Ads (formerly Apple Search Ads) deep analysis for mobile app advertisers. Evaluates campaign structure, bid health, Custom Product Pages (CPPs), AdAttributionKit (view-through attribution 24h post-impression), MMP attribution, budget pacing, TAP coverage (Today/Search/Product Pages), Maximize Conversions bidding, and goal CPA benchmarks by country. Use when user says Apple Ads, Apple Search Ads, ASA, App Store ads, Apple ads, Search Ads, AdAttributionKit, view-through attribution, or is advertising a mobile app on iOS."
user-invokable: false
tested_date: 2026-05-26
tested_with: claude-code v2.x
---

# Apple Ads (formerly Apple Search Ads) Deep Analysis

<!-- Updated: 2026-04-13 | v1.5: Maximize Conversions, CPP-only (Creative Sets deprecated), AdAttributionKit, rebrand -->
<!-- Note: Apple rebranded "Apple Search Ads" to "Apple Ads" in April 2025 -->

## Process

1. Collect Apple Ads account data (exports from Apple Ads dashboard or pasted metrics)
2. Identify active placement types (Search Results, Search Tab, Today Tab, Product Pages)
3. Evaluate all applicable checks as PASS, WARNING, or FAIL
4. Calculate ASA Health Score (0-100)
5. Generate findings report with action plan

## What to Analyze

### Campaign Structure (25% weight)

**BOFU; Bottom of Funnel (Search Results, Exact Match brand)**
- Brand keyword campaign present (own app name + misspellings)
- Competitor campaign present (competitor app names as keywords)
- Category campaigns targeting high-intent generic terms (e.g. "workout app", "budget tracker")

**MOFU; Middle of Funnel (Search Match / broad discovery)**
- Search Match campaigns active in at least one ad group for discovery
- Search Match ad groups isolated from Exact Match (separate ad groups; never mix)
- Search Terms Report reviewed to mine converting queries for Exact Match promotion

**Campaign Architecture Rules:**
- Brand / Category / Competitor should be separate campaigns (different CPT bids, budgets)
- Search Match ad groups isolated from manual keyword ad groups; NEVER mix in same ad group
- Goal: let Search Match discover, then promote winners to Exact Match campaigns

### Bid Health (20% weight)

**CPT (Cost Per Tap) vs Install Rate by Match Type:**
- CPT vs category benchmarks (see Benchmarks section below)
- TTR (Tap-Through Rate): benchmark >2.5% for Search Results, >1.5% for Search Tab
- Conversion Rate (tap → install): benchmark 50-65% for brand terms, 20-40% for category
- CPT/CPG (Cost Per Goal): compare against target CPI/CPA from MMP

**Bid Strategy:**
- Manual CPT bidding appropriate for small/new accounts
- **Maximize Conversions** (GA February 26, 2026): AI-powered auto-bidder using Search Match that sets optimal bids per search query in real time. Target CPA (weekly average target) replaces CPA Cap (being deprecated). Recommended daily budget: at least 5x target CPA. Two-week learning period minimum. **Current limitation**: only optimizes for installs, NOT post-install events (no trial, subscription, or ROAS optimization yet)
- CPA Goals available at campaign level; evaluate if conversion volume supports it (>100 installs/month per campaign)
- Are bids differentiated by match type? (Brand Exact > Category Exact > Search Match)
- Keyword-level CPT bids set, not just ad group default?

**Keyword Health:**
- Irrelevant Search Terms (from Search Match) identified and excluded via negative keywords
- Low-performing keywords paused or bid reduced (TTR <1% + high CPT)
- High-volume generic terms checked for intent quality (avoid "free apps" type queries)

### Custom Product Pages (15% weight)

> **Creative Sets fully deprecated.** CPPs are now the sole ad variation mechanism. CPP limit doubled to **70** in October 2025.

**Custom Product Pages (CPP):**
- CPPs created in App Store Connect? (up to 35 per app)
- At least 3 CPP variants tested per campaign type (different value props per audience)
- CPP assets aligned with ad group keyword themes (e.g. fitness keywords → fitness screenshots)
- CPPs increase conversion rates ~8% for games, ~6.6% for non-gaming apps (per [AppTweak CPP guide](https://www.apptweak.com/en/aso-blog/guide-to-custom-product-pages-cpp))
- SoundCloud case study: CPPs in competitor campaigns led to 58% CR increase, 39% CPI reduction ([AppTweak case study](https://www.apptweak.com/en/case-studies/soundcloud))
- **Critical**: 78% of App Store search volume comes from devices with Personalized Ads off (per Apple's Q1 2022 internal data, [9to5Mac](https://9to5mac.com/2022/05/11/ios-15-users-opt-out-of-personalized-ads/)). Use creative-based targeting (CPP asset alignment) rather than demographic audience filters

**Default (Store Listing) Creative:**
- App icon, subtitle, and first 3 screenshots optimized; these show in ads by default
- Short description (170 chars) compelling and keyword-rich
- Preview video present (strongly recommended for TTR improvement)

**Creative Testing:**
- CPP performance compared: which variant has highest TTR and lowest CPI?
- Deep links in CPPs available on iOS/iPadOS 18+ (test for re-engagement)
- CPPs can now be assigned organic keywords (WWDC 2025), bridging paid/organic optimization

### Attribution & MMP Health (15% weight)

**MMP Integration (Critical):**
- MMP (AppsFlyer / Adjust / Branch / Singular) integrated with Apple Ads via AdAttributionKit + ATT
- Apple Ads properly connected as a partner in MMP dashboard
- In-app events being sent back to Apple Ads (enables Maximize Conversions and ROAS optimization)
- Post-install event quality: are purchase, subscription_start, or other revenue events tracked?

**AdAttributionKit & Dual Attribution (April 10, 2025):**
- Apple Ads registered with AdAttributionKit (SKAN v1-3), creating dual attribution for the first time
- Installs now report through BOTH SKAN/AAK postbacks AND the AdServices API
- WWDC 2025: configurable attribution windows, overlapping re-engagement windows, attribution cooldowns, and country codes in postbacks ([Apple Developer, WWDC25 session 221](https://developer.apple.com/videos/play/wwdc2025/221/); [Singular recap](https://www.singular.net/blog/wwdc-2025-aak/))
- SKAdNetwork conversion values configured in MMP (maps user actions to conversion windows)
- ATT opt-in rate monitored (low ATT rate = less MMP data, more reliance on SKAN/AAK)
- Privacy threshold considerations: are campaigns getting postbacks or null reports?

**Attribution Windows:**
- Default Apple Ads attribution: 30-day click, 1-day view; appropriate for app install goals?
- WWDC 2025 added configurable windows and overlapping re-engagement windows (iOS 18.4+, requires `EligibleForAdAttributionKitOverlappingConversions=YES` in Info.plist; see [WWDC25 session 221](https://developer.apple.com/videos/play/wwdc2025/221/))
- For re-engagement or subscription goals: evaluate longer lookback windows

### Budget Pacing (10% weight)

- Daily cap set at campaign level (budget pacing in ASA is daily, not monthly)
- Actual daily spend vs daily cap ratio: flag if consistently hitting cap (could be missing volume)
- Conversely: flag if spend is <50% of daily cap (creative or bid issue, not budget)
- Budget split across placement types aligned with performance (don't over-invest in underperforming placements)
- Lifetime budget campaigns (if used): check end dates and pacing curves

### TAP Coverage: Placement Types (10% weight)

ASA offers 4 placement types; evaluate coverage and performance:

| Placement | Where | Best for | Benchmark CPT |
|-----------|-------|----------|----------------|
| Search Results | Below search results | High intent, bottom funnel | $0.50-$3.00 |
| Search Tab | Top of Search tab | Discovery, mid funnel | $0.30-$1.50 |
| Today Tab | App Store home | Brand awareness | $1.00-$5.00 |
| Product Pages | Competitor/related app pages | Competitor conquesting | $0.50-$2.00 |

**Evaluation:**
- Search Results: must be active (highest intent placement)
- Search Tab: active for scale? Evaluate CPT and TTR vs Search Results
- Today Tab: only if budget >$3k/month and brand awareness is a goal (high CPT, low intent)
- Product Pages: competitive opportunity; are competitor CPPs being targeted?

### Goal CPA / KPI Assessment (5% weight)

**Benchmarks by Category (2025-2026 ASA averages):**
| Category | Avg CPT | Avg TTR | Avg Install CVR | Target CPI |
|----------|---------|---------|-----------------|------------|
| Games | $0.50-$1.00 | 3-5% | 55-70% | $1.00-$3.00 |
| Health & Fitness | $1.50-$3.00 | 2-4% | 45-60% | $3.00-$8.00 |
| Productivity | $1.00-$2.50 | 2-3.5% | 50-65% | $2.00-$5.00 |
| Finance | $2.00-$5.00 | 1.5-3% | 40-55% | $5.00-$15.00 |
| Education | $1.00-$2.00 | 2-4% | 50-65% | $2.00-$6.00 |
| Shopping | $0.80-$2.00 | 2.5-4% | 45-60% | $2.00-$5.00 |
| Lifestyle | $0.80-$1.80 | 2-3.5% | 45-60% | $2.00-$5.00 |

**Country-level benchmarks:**
- Tier 1 (US, UK, AU, CA, JP): CPT 2-3× above global average; highest LTV
- Tier 2 (DE, FR, KR, SG, HK): CPT 1-1.5× above global average
- Tier 3 (BR, IN, MX): CPT 30-60% below Tier 1; high volume, lower LTV

**Checks:**
- Actual CPI vs target CPI (from MMP); flag if >2x target
- CPI trend over 30 days (improving or worsening?)
- Revenue events: is ROAS positive within MMP attribution window?

### Overall Benchmarks (2025 SplitMetrics data)

| Metric | Search Results Average |
|--------|-----------------------|
| TTR (Tap-Through Rate) | 9.7% |
| Conversion Rate | 66.2% |
| CPT (Cost Per Tap) | $2.25 |
| CPA (Cost Per Acquisition) | $3.76 |

- US is the highest-cost market
- AMEI (Africa/Middle East/India) is most cost-efficient and stable
- **International markets often deliver 3-5x better CPI than US** with comparable LTV for subscription apps

### Platform Changes (v1.5)

| ID | Check | Severity | Notes |
|----|-------|----------|-------|
| ASA-MA1 | Multiple ads per query readiness | Medium | Rolling out March 2026: up to 2 ads per search query (was 1). Changes competitive dynamics: more search results real estate available. Evaluate bid strategy for increased competition |

**Deprecated:**
- Creative Sets: fully deprecated. Only CPPs now (up to 35 per app)
- CPA Cap: being retired in favor of Target CPA via Maximize Conversions
- Demographic audience targeting as primary strategy: 78% of App Store search volume comes from devices with Personalized Ads off (Apple's Q1 2022 internal data; conversion rate is nearly identical between opted-in and opted-out users — 62.1% vs 62.5%)

## v1.8.0 — Multiple Search Ad Placements + iOS 26 (A36-A42)

Apple Ads updates from late 2025 through Q1 2026. The iOS 26 privacy items (A40, A41) affect every iOS attribution pipeline, not just Apple Ads, so they cross-reference `ads/references/compliance-requirements.md` (C-iOS-1) and the `/ads server-side-tracking` sub-skill.

| ID | Check | Severity | Notes |
|----|-------|----------|-------|
| A36 | Multiple Search Ad Placements live | High | Up to 2 ads per single search query. UK + Japan first on March 3, 2026; global rollout to all 91 Apple Ads markets by end of March 2026. Existing campaigns auto-enrolled (no opt-out, no separate setup); requires iOS/iPadOS 26.2+ (older OS still shows a single placement). CPT/CPI pricing unchanged; relevance-first auction applies to both positions. 65% of App Store downloads happen after a search, so this is high-leverage real estate. **CRITICAL CAVEAT:** no position-level reporting in AdAttributionKit initially. Audits cannot separate position 1 from position 2 — only aggregate. Any TAP (Today/Search/Product Pages) placement-coverage report must caveat that position-level breakdown is unavailable ([9to5Mac, Jan 22, 2026](https://9to5mac.com/); Apple Ads documentation, Dec 18, 2025) |
| A37 | App Store registered with AdAttributionKit | Medium | The App Store itself has been registered with AdAttributionKit since it went live April 10, 2025 — a precondition for postback / view-through attribution from App Store ad surfaces. Verify the user's app includes the AdAttributionKit framework in its App Store metadata |
| A38 | AdAttributionKit feature surface up to date | Medium | WWDC 2025 / iOS 18.4+ production features: configurable attribution windows (per ad network / interaction type / global); configurable cooldowns to prevent install vs re-engagement cannibalization; country codes in postbacks (subject to crowd anonymity threshold); overlapping re-engagement conversion windows via Conversion Tags; Development Postbacks settings test tool for QA. Refresh check thresholds and add postback-decoding examples for the country-code field. Core coverage lives in `/ads attribution` ([WWDC25 session 221](https://developer.apple.com/videos/play/wwdc2025/221/)) |
| A39 | Custom Product Pages within limit | Medium | CPPs replace the deprecated Creative Sets — up to 35 per app, each targetable with a distinct creative combination. Verify usage is within the 35-per-app limit; flag accounts using fewer than 5 CPPs for product-page testing (indicates underutilization) |
| A40 | iOS 26 Advanced Fingerprinting Protection (ATFP) | High | Default ON in ALL Safari browsing as of iOS 26 (was Private Browsing only). Up to ~90% reduction in fingerprinting effectiveness per early WebProNews testing. Breaks device-graph attribution, probabilistic match modeling, and server-side identity resolution across **all iOS attribution pipelines**, not just Apple Ads. Server-side conversion APIs become the only reliable signal pathway for iOS Safari conversion measurement. See `compliance-requirements.md` (C-iOS-1) ([WebProNews, iOS 26 Safari fingerprinting protection](https://www.webpronews.com/apple-enhances-safari-privacy-with-default-fingerprinting-protection-in-ios-26/)) |
| A41 | iOS 26 Expanded Link Tracking Protection | Critical | Strips gclid / fbclid / msclkid in ALL Safari browsing as of iOS 26 (was Private + Mail only) — affects every iOS Safari user, not just the privacy-conscious minority. For accounts with iOS Safari traffic share above 5%, server-side conversion APIs are mandatory for iOS Safari conversion measurement. Audit and remediate via `/ads server-side-tracking`; see `compliance-requirements.md` (C-iOS-1) ([WITHIN, iOS 26 Link Tracking Protection](https://www.within.co/blog/ios-26/)) |
| A42 | WWDC 2026 watch list | Low | WWDC 2026 keynote is in June 2026. Likely Apple Ads / AdAttributionKit announcements to monitor: further AdAttributionKit window / cooldown granularity; possible SKAN (SKAdNetwork) sunset roadmap; iOS 27; possible Apple News ad expansion. **Action:** schedule a v1.8.x addendum within 14 days of the keynote to fold in whatever ships |

**iOS 26 cross-reference:** A40 and A41 are platform-wide privacy changes. When either applies, route server-side remediation through `/ads server-side-tracking` and confirm the requirement is logged against `ads/references/compliance-requirements.md` (C-iOS-1) so the fix is tracked at the account level, not just in this Apple audit.

## Output Format

```
## Apple Ads Audit

**ASA Health Score: [X]/100**

### Critical Issues ([count])
- [Issue with specific impact and fix]

### High Priority ([count])
- [Issue]

### Campaign Structure
PASS/WARNING/FAIL for each check category

### Benchmark Comparison
[Metric] | Your Account | ASA Benchmark | Status

### Quick Wins (do this week)
1. [Most impactful fix with expected outcome]
2.
3.

### Recommended Next Steps
[Prioritized action plan]
```

## Scoring Weights

| Category | Weight |
|----------|--------|
| Campaign Structure | 25% |
| Bid Health | 20% |
| Custom Product Pages | 15% |
| Attribution & MMP | 15% |
| Budget Pacing | 10% |
| TAP Coverage | 10% |
| Goal KPI Assessment | 5% |

## Data to Request from User

If not provided, ask for:
- Campaign list with spend, installs, CPT, TTR, CVR (last 30 days)
- Active placement types
- MMP being used (AppsFlyer, Adjust, Branch, Singular, or none)
- Target CPI / CPA and app category
- Countries/regions active
- Whether Custom Product Pages are set up in App Store Connect
