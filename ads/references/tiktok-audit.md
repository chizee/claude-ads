# TikTok Ads Audit Checklist

<!-- Updated: 2026-05-26 | v1.8.0 -->
<!-- Sources: Google Research PDF 1 (T01-T25), Claude Research, Gemini Research -->
<!-- Total Checks: 46 | v1.8.0: TikTok World 2026 (T29-T46) -->

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Creative Quality | 30% | T05-T10 + T20-T25 (12 checks) |
| Technical Setup | 25% | T01-T02 (2 checks) |
| Bidding & Learning | 20% | T11-T13 (3 checks) |
| Structure & Settings | 15% | T03-T04 + T14-T16 (5 checks) |
| Performance | 10% | T17-T19 (3 checks) |
| Search, Commerce & Tracking | N/A | T-SR1, T-GM1, T-EA1 (3 checks, v1.5) |
| TikTok World 2026 (v1.8.0) | N/A | T29-T46 (18, scored within existing categories) |

---

## Creative Quality (30% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T05 | Creative volume | Critical | ≥6 creative assets per ad group | 3-5 creatives | <3 creatives per ad group |
| T06 | Vertical video format | Critical | All video assets 9:16 (1080x1920) | Mixed ratios with some vertical | No vertical video (landscape only) |
| T07 | Native-looking content | High | Ads look organic / creator-style (not polished corporate) | Semi-native style | Clearly corporate/polished ads |
| T08 | Hook strategy | High | First 1-2 seconds have attention-grabbing hook | Decent hook but not optimized | No clear hook in opening |
| T09 | Creative lifespan | High | No creative active >7 days with declining CTR (7-10 day avg lifespan). Frequency <2.5x. Campaigns with 10+ unique creatives achieve 1.3x higher ad recall, 3.0x purchase intent, 1.5x higher awareness vs <5 | 7-14 days with minor decline; frequency approaching 2.5x | >14 days with significant CTR decline. Frequency >2.5x causes 30-40% CVR drops |
| T10 | Spark Ads utilization | High | Spark Ads tested and active (+30% completion rate, +142% engagement rate, +43% CVR, -4% CPM vs non-Spark). Profile landing page = 69% higher CVR and 37% lower CPA. Strategy: test with dark ads first, identify top performers, convert winners to Spark | Tested but paused | No Spark Ads tested (~3% CTR vs ~2% standard) |
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
| T12 | Budget sufficiency | High | Daily budget ≥50x target CPA per ad group. GMV Max mandatory for all Shop Ads (July 2025). For first-time VSA campaigns, budget ≥50x target CPA. Evaluate holistically: Shop total GMV / (Ads cost + affiliate commission) | 20-49x CPA | <20x CPA per ad group |
| T13 | Learning phase | High | Ad groups achieving ≥50 conversions/week | 25-50 conversions/week | <25 conversions/week (stuck in learning) |

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
| T04 | Smart+ utilization | Medium | Smart+ campaigns tested with modular control. Advertisers can lock specific modules (targeting, creative, budget, placement) while automating others. Supports up to 30 ad groups/campaign, 30 asset groups/ad group, 50 creatives/asset group | N/A | Not tested (42% adoption, 1.41-1.67 median ROAS; modular control since 2025) |
| T14 | Search Ads Toggle | High | Search Ads Toggle enabled for all campaigns (20% increase in conversions when combined with In-Feed; 18% of in-feed non-converters convert via Search Ad; 2x higher purchase lift; 57% of TikTok users use search). Max 1,000 keywords per ad group | N/A | Search Ads Toggle OFF (missing significant incremental conversions) |
| T15 | Placement selection | Medium | Appropriate placements selected (TikTok, Pangle, etc.) | Default placements without review | N/A |
| T16 | Dayparting | Low | Ad schedule aligned with target audience activity | N/A | No schedule despite clear patterns |

---

## Performance (10% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T17 | CTR benchmark | High | CTR ≥1.0% for in-feed ads | CTR 0.5-1.0% | CTR <0.5% |
| T18 | CPA target | High | CPA within target range | CPA 1.5-3x target | CPA >3x target (trigger 3x Kill Rule) |
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

## TikTok World 2026 (v1.8.0, T29-T46, scored within existing categories)

TikTok World 2026 ran May 13-15, 2026, two days before the v1.7.0 cut. Source: `research/notes-tiktok.md`. These checks fold into the existing six categories (creative, structure, tracking, commerce, performance) rather than forming a new weighted bucket. Separately, the TikTok USDS divestiture closed January 22, 2026 (80.1% non-Chinese ownership); it produced no measurable disruption to advertiser operations, so no migration or continuity check is warranted.

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| T29 | TikTok Ads MCP Server | Medium | TikTok Ads MCP Server (official, announced May 13 2026; last of the four majors) connection detected and inventoried | MCP Server known but not yet connected | No MCP Server usage despite agentic workflow opportunity |
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
| T41 | Collage Carousel | Low | Collage Carousel (hero + 3 product visuals; US Q2 2026) tested for product storytelling | US product advertiser eligible but Collage Carousel not tested | Multi-product US catalog ignores Collage Carousel despite market eligibility |
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
