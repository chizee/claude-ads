# TikTok Ads Audit Checklist

<!-- Grounded: 2026-07-11 | source IDs: tiktok-business-api-official, tiktok-events-api-official, tiktok-pixel-official -->
<!-- Total Checks: 46 | v1.8.0: TikTok World 2026 (T29-T46) -->

## Runtime evaluation contract

- Establish objective, market, placement, commerce/app/web surface, attribution, conversion lag, spend, sample size, and feature access first. Missing evidence is `unknown`; ineligible surfaces are `not_applicable`.
- Creative counts, refresh days, frequency, budget-to-CPA ratios, learning volume, CTR, and watch-time bands are practitioner prompts. They affect health only when account-relative evidence and the selected optimization event justify them.
- T29-T46 are unscored launch discovery. MCP, Skills, Smart+, Symphony, commerce, travel, gaming, premium reach, and research-tool adoption are never health requirements.
- Vendor-reported lifts may motivate a measured experiment but must not be presented as an expected result.

## Official evidence

- `tiktok-business-api-official`: [TikTok API for Business](https://business-api.tiktok.com/portal)
- `tiktok-events-api-official`: [About Events API](https://ads.tiktok.com/help/article/events-api)
- `tiktok-pixel-official`: [About TikTok Pixel](https://ads.tiktok.com/help/article/tiktok-pixel)

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Creative Quality | 30% | T05-T10 + T20-T25 (12 checks) |
| Technical Setup | 25% | T01-T02 (2 checks) |
| Bidding & Learning | 20% | T11-T13 (3 checks) |
| Structure & Settings | 15% | T03-T04 + T14-T16 (5 checks) |
| Performance | 10% | T17-T19 (3 checks) |
| Search, Commerce & Tracking | N/A | T-SR1, T-GM1, T-EA1 (3 checks, v1.5) |
| Product-launch discovery | Unscored | T29-T46 (18 applicability or opportunity questions) |

---

## Creative Quality (30% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T05 | Creative test capacity | High | Distinct creative concepts are sufficient for the approved spend and experiment cadence | Capacity is thin or repetitive | Delivery concentration or exhausted tests confirm a material creative bottleneck |
| T06 | Vertical video format | Critical | All video assets 9:16 (1080x1920) | Mixed ratios with some vertical | No vertical video (landscape only) |
| T07 | Native-looking content | High | Ads look organic / creator-style (not polished corporate) | Semi-native style | Clearly corporate/polished ads |
| T08 | Hook strategy | High | First 1-2 seconds have attention-grabbing hook | Decent hook but not optimized | No clear hook in opening |
| T09 | Creative fatigue | High | Same-cohort performance, frequency, reach, and conversion quality show no credible fatigue | Directional decline lacks enough data | Sustained account-relative decline is confirmed after excluding auction, budget, audience, and tracking changes |
| T10 | Spark Ads applicability | Low | Authorization, brand risk, format fit, and account-relative experiment evidence were evaluated | Experiment is incomplete | N/A; absence is not a health failure |
| T20 | TikTok Shop integration | Medium | Shop catalog connected (for e-commerce) | N/A | Eligible but not connected |
| T21 | Video Shopping Ads (VSA) | Medium | VSA tested for product catalog accounts | N/A | Not tested despite eligible catalog |
| T22 | Caption SEO | High | Captions include high-intent keywords for search discovery | Some keywords in captions | No keyword optimization in captions |
| T23 | Sound/music usage | Medium | Trending or engaging audio used | Licensed audio but not trending | Silent ads (TikTok is sound-on platform) |
| T24 | CTA button | Medium | Appropriate CTA button selected (not default) | N/A | Default CTA without customization |
| T25 | Safe zone compliance | High | Key content within safe zone (X:40-940, Y:150-1470) | Minor elements outside safe zone | Key text/CTA in UI overlay zones |

---

## Technical Setup (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T01 | TikTok Pixel installed | Critical | Pixel firing on all relevant pages | Firing on most pages (>90%) | Pixel not installed or broken |
| T02 | Events API + ttclid | High | Server-side events via Events API with ttclid passback | Events API active but no ttclid passback | No server-side tracking |

### ttclid Critical Note
The TikTok Click ID (`ttclid`) comes in landing page URL parameters and MUST be:
1. Captured on first page load
2. Stored in session/cookie
3. Sent back with ALL conversion events

Without ttclid, attribution breaks for many conversions. This is TikTok's key technical difference from other platforms.

---

## Bidding & Learning (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T11 | Bid strategy | High | Lowest Cost for volume; Cost Cap for efficiency | N/A | Bid Cap set too aggressively (severe under-delivery) |
| T12 | Budget sufficiency | High | Budget is justified by target economics, conversion lag, expected event volume, and experiment duration | Delivery or sample is inconclusive | Budget makes the approved objective or test infeasible |
| T13 | Learning evidence | High | Delivery status and event volume are interpreted from the current account surface and selected optimization event | Learning status or cause is unclear | Repeated disruptive edits or preventable fragmentation blocks learning |

### Learning Phase Rules
- Exit criteria: ~50 conversions in 7 days per ad group
- Campaign minimum budget: $50/day
- Ad group minimum budget: $20/day
- Daily budget should be ≥50x target CPA for sufficient learning room
- Avoid changes during learning (resets the phase)

---

## Structure & Settings (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T03 | Campaign structure | High | Separate campaigns for prospecting vs retargeting | N/A | Prospecting and retargeting mixed |
| T04 | Smart+ applicability | Low | Available automation modules were evaluated against control, measurement, and experiment needs | Evaluation is incomplete | N/A; non-adoption is an opportunity |
| T14 | Search Ads applicability | Low | Search inventory was evaluated where market, objective, query demand, and feature access support it | Evaluation is incomplete | N/A; a disabled or unavailable toggle is not a health failure |
| T15 | Placement selection | Medium | Appropriate placements selected (TikTok, Pangle, etc.) | Default placements without review | N/A |
| T16 | Dayparting | Low | Ad schedule aligned with target audience activity | N/A | No schedule despite clear patterns |

---

## Performance (10% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T17 | CTR benchmark | Medium | CTR is compared with a same-objective, placement, format, geography, and date-window cohort | Only a broad benchmark is available | A statistically credible account-relative decline is unexplained |
| T18 | CPA target | High | Lag-adjusted CPA is within the owner-approved economic target at adequate sample | Sample or lag is inconclusive | Material target miss persists after quality, lag, and margin review; never apply a fixed kill multiple |
| T19 | Video completion rate | Medium | Average video watch time ≥6 seconds | 3-6 seconds | <3 seconds average watch time |

---

## Quick Wins (TikTok)

| Check | Fix | Time |
|-------|-----|------|
| T14: Search Ads Toggle | Enable Search Ads Toggle in campaign settings | 2 min |
| T06: Vertical video | Convert existing assets to 9:16 format | 10 min |
| T24: CTA button | Select appropriate CTA (not default) | 2 min |
| T10: Spark Ads | Whitelist top creator/organic content as Spark Ads | 10 min |
| T22: Caption SEO | Add high-intent keywords to ad captions | 5 min |
| T25: Safe zone | Verify key content within X:40-940, Y:150-1470 | 5 min |

---

## TikTok-Specific Context

| Fact | Value |
|------|-------|
| Smart+ adoption | 42% of US TikTok performance campaigns (surged from 9% in early 2025) |
| Smart+ capacity | 30 ad groups/campaign, 30 asset groups/ad group, 50 creatives/asset group |
| GMV Max | Default for TikTok Shop Ads (July 2025) |
| TikTok Shop CVR | >10% (vs 0.46-2.4% standard) |
| CPM advantage | 40-60% cheaper than Meta |
| Spark Ads CTR | ~3% vs ~2% standard In-Feed |
| Spark Ads CPA | ~$60 vs ~$100 standard |
| Engagement rate | 5-16% (far exceeds FB 0.09%, IG 1.22%) |
| Search Ads | Launched 2025; supports Sales, Traffic, Lead Generation objectives in 12 markets |
| Safe zone | X:40-940px, Y:150-1470px (900x1320px usable) |
| Available markets | 12 countries (US, UK, key Asian/European) |

---

## Search, Commerce & Tracking (v1.5)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T-SR1 | Search Ads alongside In-Feed | High | Search Ads enabled alongside In-Feed campaigns (20% conversion uplift when combined; 18% of non-converters from in-feed convert via Search; 2x purchase lift). Supports keyword targeting with exact/phrase/broad, negative keywords, search term reports | N/A | Search Ads not enabled despite available budget (missing 18-20% incremental conversions) |
| T-GM1 | GMV Max for Shop campaigns | Critical | All TikTok Shop campaigns use GMV Max (mandatory since July 2025). Three ad types: Video Shopping Ads, LIVE Shopping Ads, Product Shopping Ads | Non-GMV Max Shop campaigns still transitioning | Non-GMV Max Shop campaigns active (non-compliant with July 2025 mandate) |
| T-EA1 | Events API Gateway setup | High | Events API Gateway configured for simplified server-side tracking (recovers 13%+ of missed conversions vs pixel-only). SKAN 4 integration with coarse conversion values active for iOS | Events API planned but not deployed | No server-side tracking (pixel-only, missing 13%+ of conversions) |

---

## Product-launch discovery (T29-T46, unscored)

These IDs are retained for catalog compatibility. Re-verify feature existence, market,
account access, and eligibility through current official documentation or in-account evidence.
Missing access and non-adoption are `not_applicable` or opportunities, never health failures.

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T29 | TikTok Ads MCP Server | Medium | Any connected integration's endpoint, owner, tools, scopes, and mutation authority are inventoried from live evidence | Connection exists but inventory is incomplete | N/A; absence is not a health failure |
| T30 | TikTok Ads Skills | Low | TikTok Ads Skills developer building blocks adopted for custom automation | Aware but not yet building | Not adopted despite developer resources in account |
| T31 | Smart+ One Buying Experience module control | High | Audit recognizes module-level granularity: targeting, budget, and placements can each be toggled on/off PER MODULE (not all-or-nothing automation) | Smart+ One in use but module-level controls not reviewed | Treated as all-or-nothing; module-level levers ignored |
| T32 | Smart+ Music Autofix | Low | Smart+ Music Autofix enabled so flagged audio is auto-relicensed | N/A | Eligible Smart+ campaigns with Music Autofix off, risking takedowns |
| T33 | Smart+ creative reporting + multi-URL | Low | Smart+ creative reporting, multi-URL, and the higher asset-group limit in use | Partial adoption (e.g., single URL only) | N/A |
| T34 | Smart+ for app objectives | Low | Smart+ used for app-install / app-event objectives where applicable | N/A | App-objective campaigns not testing Smart+ despite eligibility |
| T35 | TopReach + Creative Sequencing | Low | TopReach with Creative Sequencing (unified TopView + TopFeed) used for sequenced reach plays | Running TopView/TopFeed separately, not as a sequenced buy | Large reach budget with no narrative sequencing despite eligibility |
| T36 | Branded Buzz | Low | Branded Buzz large-scale creator collaboration format evaluated for awareness pushes | Awareness objective live but Branded Buzz not evaluated | Awareness/reach push ignores Branded Buzz despite clear creator-collab fit |
| T37 | Search Hubs | Medium | Brand-owned sponsored Search Hubs pages evaluated where branded search demand exists | Branded demand present but Search Hubs not evaluated | N/A |
| T38 | Symphony AI creative stack | Low | Symphony AI / Dreamina Seedance 2.0 / Reference to Video used to scale creative variations | N/A | Manual-only creative refresh despite stack availability |
| T39 | TikTok GO booking integration | Low | TikTok GO booking integration live for travel partners (Booking.com, Expedia, Viator, GetYourGuide, Tiqets, Trip.com) | Travel advertiser not evaluating TikTok GO booking integration | Travel/booking account ignoring TikTok GO despite partner availability |
| T40 | Mini Series & Mini Games | Low | Mini Series and Mini Games formats evaluated; Growth Max used for Mini Games where relevant | Entertainment/gaming advertiser not evaluating Mini Series or Mini Games | Gaming/entertainment objective ignores Mini Games + Growth Max despite clear fit |
| T41 | Collage Carousel availability | Low | Current account evidence confirms access and an owner-approved test rationale | Availability or fit is unknown | N/A when unavailable; non-adoption is an opportunity |
| T42 | One Asset Manager | Low | One Asset Manager used for unified asset management across campaigns | N/A | Assets fragmented across tools despite One Asset Manager availability |
| T43 | View+ for Pulse Core Max | Low | View+ premium reach upgrade applied to Pulse Core Max placements where reach goals warrant | Pulse Core Max running but View+ upgrade not evaluated | Reach-goal campaigns on Pulse Core Max skip View+ despite eligibility |
| T44 | TikTok Market Scope | Low | TikTok Market Scope used for competitive intelligence and category benchmarking | Market Scope available but not used for benchmarking | Optimizing blind with no Market Scope competitive intelligence despite access |
| T45 | TikTok Real + UK Ad-Free Subscription | Medium | UK measurement plan accounts for users opted OUT of advertising data use via the UK Ad-Free Subscription (£3.99/mo); TikTok Real counterfeit/IP protections understood | UK audience present but opt-out measurement impact not modeled | UK campaigns ignore Ad-Free Subscription opt-outs, overstating measured conversions |
| T46 | GMV Max market expansion | Low | GMV Max market expansion adopted in newly eligible markets | N/A | Newly eligible markets not using GMV Max for Shop Ads |

---

## Context Notes

- **Smart+ modular control (2025)**: Lock targeting/creative/budget/placement independently
- **GMV Max (July 2025)**: Mandatory for all Shop Ads campaigns
- **Symphony Automation**: AI-powered creative variations from product URLs, which impacts creative refresh evaluation
- **Events API Gateway**: Simplified server-side setup for conversion recovery
- **Search Ads maturity**: Now supports Sales, Traffic, and Lead Generation objectives in 12 markets
- **Creative lifespan**: 7-10 days average. Refresh weekly minimum. High-spend ($1K+/day) needs variations every 3-4 days

---

## TikTok Safe Zone Diagram

```
┌──────────────────────────────┐
│  0-150px: Status bar, account│  ← TOP UNSAFE
├──────────────────────────────┤
│                         │    │
│    SAFE ZONE            │140 │  ← RIGHT: Like, comment,
│    X: 40-940px          │ px │     share, profile icons
│    Y: 150-1470px        │    │
│    (900×1320px)         │    │
│                         │    │
├──────────────────────────────┤
│  0-450px: Caption, music,    │  ← BOTTOM UNSAFE
│  CTA, navigation bar         │
└──────────────────────────────┘
```

All critical text, logos, and CTAs MUST be within the safe box.
