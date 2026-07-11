# Google Ads Audit Checklist

<!-- Grounded: 2026-07-11 | source IDs: google-ads-api-official, google-ads-conversion-goals-official, google-ads-enhanced-conversions-official -->
<!-- Total Checks: 95 | Categories: 8 | See scoring-system.md for weights and algorithm -->

## Runtime evaluation contract

- Treat every row as an applicability-first evidence question. Return `not_applicable` when the campaign type, objective, geography, feature access, or required data is absent; return `unknown` when evidence is missing.
- A number in this legacy catalog is a practitioner investigation prompt, not a universal pass/fail boundary. It may affect health only when objective, conversion lag, sample size, date window, and a relevant account baseline justify it.
- Feature adoption, beta access, vendor-reported lift, and announcement awareness are opportunities, never account-health failures. The G81-G95 launch-discovery rows are unscored.
- Use current account/API evidence for settings and eligibility. Do not infer availability from an announcement date or recommend a feature the account cannot enable.

## Official evidence

- `google-ads-api-official`: [Google Ads API documentation](https://developers.google.com/google-ads/api/docs/start)
- `google-ads-conversion-goals-official`: [About conversion goals](https://support.google.com/google-ads/answer/10995103)
- `google-ads-enhanced-conversions-official`: [About enhanced conversions](https://support.google.com/google-ads/answer/9888656)

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Conversion Tracking | 25% | G42-G49 (8) + G-CT1 through G-CT3 (3) + G-CTV1 (1) = 12 |
| Wasted Spend / Negatives | 20% | G13-G19 (7) + G-WS1 (1) = 8 |
| Account Structure | 15% | G01-G12 (12) |
| Keywords & Quality Score | 15% | G20-G25 (6) + G-KW1, G-KW2 (2) = 8 |
| Ads & Assets | 15% | G26-G35 (10) + G-AD1, G-AD2 (2) = 12 |
| Settings & Targeting | 10% | G50-G61 (12) |
| Performance Max | N/A | G-PM1 through G-PM6 (6, scored within Ads & Assets) |
| AI & Demand Gen | N/A | G-AI1 (1) + G-DG1 through G-DG3 (3, scored within Ads & Assets) |
| Product-launch discovery | Unscored | G81-G95 (15 opportunity or governance questions) |

---

## Conversion Tracking (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G42 | Conversion actions defined | Critical | ≥1 primary conversion action configured | N/A | No active conversion actions |
| G43 | Enhanced conversions applicability and status | High | Eligible primary conversion actions use enhanced conversions and diagnostics are healthy | Eligible but diagnostics need review | Eligible, material first-party data is collected with valid consent, and enhanced conversions were rejected without documented reason |
| G44 | Server-side tracking | High | Server-side GTM or Google Ads API conversion import active | Planned but not deployed | No server-side tracking |
| G45 | Consent signals and regional requirements | Critical | Consent signals and tag behavior are verified against the account's geography, consent platform, and current Google requirements | Implementation exists but evidence or regional mapping is incomplete | Applicable traffic is sent without the required consent behavior |
| G46 | Conversion window appropriate | Medium | Window is justified by observed conversion lag and the business sales cycle | Default window without validation | Window demonstrably excludes material conversions or obscures the decision window |
| G47 | Micro vs macro separation | High | Only macro conversions (Purchase, Lead) set as "Primary" for bidding | Some micro events as Primary | All events including micro (AddToCart, TimeOnSite) as Primary |
| G48 | Attribution model | Medium | Data-driven attribution (DDA) selected | Last Click (intentional, document reasoning) | Rule-based model active (first click, linear, time decay, position-based were ALL auto-upgraded to DDA. Any remaining rule-based is a legacy misconfiguration) |

**G48/CT-FL5 accuracy notes:** Exclude Smart Campaign system-managed conversions (e.g., 'Smart campaign map clicks to call') from DDA and counting-type checks. Their attribution model and counting type are locked by Google; advertisers cannot change them. Only evaluate advertiser-controlled conversion actions.
| G49 | Conversion value assignment | High | Dynamic values for ecom; value rules for lead gen | Static values assigned | No conversion values |
| G-CT1 | No duplicate counting | Critical | GA4 + Google Ads not double-counting same conversion | N/A | Both GA4 import and native tag counting same action |

**G-CT1 accuracy notes:** Only check ENABLED conversion actions for duplicates. Exclude HIDDEN and REMOVED conversion actions; these are already disabled and cannot cause double-counting. When reporting duplicates, include the conversion action ID, type, origin, category, status, primary/secondary flag, counting type, and attribution model for easy resolution.
| G-CT2 | GA4 linked and flowing | High | GA4 property linked, data flowing correctly | Linked but data discrepancies | Not linked |
| G-CT3 | Google Tag firing | Critical | gtag.js or GTM firing correctly on all pages | Firing on most pages (>90%) | Tag missing or broken on key pages |

---

## Wasted Spend / Negatives (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G13 | Search term audit recency | Critical | Search terms reviewed within last 14 days | Reviewed within 30 days | Not reviewed in >30 days |
| G14 | Negative-keyword governance | High | Search-term evidence supports maintained negative controls with documented exceptions | Controls exist but review ownership or recency is unclear | Material irrelevant queries recur without a reviewed control |
| G15 | Account-level negatives applied | High | Negative lists applied at account or all-campaign level | Applied to some campaigns only | Not applied |

**G14/G15 accuracy notes:** Count both campaign-level negatives AND Shared Negative Keyword Lists when evaluating coverage. Campaigns covered by shared lists should NOT be flagged as "missing negatives." Report per-campaign breakdown showing direct negatives vs. shared list assignments for clear remediation paths.
| G16 | Material irrelevant search-term spend | Critical | No material spend on terms independently classified as irrelevant to the offer | Borderline terms require owner review | Material irrelevant spend is confirmed from complete search-term evidence |

**G16/G-WS1 accuracy notes:** Only flag search terms as "wasted" if they have >$10 spend AND 0 conversions. Long-tail terms with minimal spend (<$10) are normal exploration, not waste. When reporting, show top 10 wasters with spend and click details.
| G17 | Broad-match control | High | Broad match use is intentional, query quality is reviewed, and bidding/negative controls match the objective | Intent or evidence is incomplete | Broad match creates confirmed irrelevant spend without effective controls |

**G17 evidence note:** Do not infer historical Broad Match Modified behavior or advertiser intent from the current `BROAD` enum. Inspect search terms, campaign history, bidding, negatives, and owner intent.
| G18 | Close variant pollution | High | Exact/Phrase match not triggering irrelevant close variants | Minor close variant issues | Significant irrelevant close variant spend |
| G19 | Search term visibility | Medium | >60% of search term spend is visible (not hidden) | 40-60% visible | <40% visible |

**G19 accuracy notes:** When computing `totalVisibleSpend`, use ALL fetched search terms before any truncation or top-N limiting. A common error is summing cost from a truncated subset (e.g., top 500 of 2000 terms) which understates visibility. Fetch terms ordered by cost descending to ensure the highest-spend terms are captured first.
| G-WS1 | Zero-conversion keyword investigation | High | No keyword has material spend beyond the account's evidence threshold with zero lag-adjusted conversions | Sample or conversion lag is inconclusive | Material zero-conversion spend persists after lag, value, and search-term review |

---

## Account Structure (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G01 | Campaign naming convention | Medium | Consistent pattern (e.g., [Brand]_[Type]_[Geo]_[Target]) | Partially consistent | No naming convention |
| G02 | Ad group naming convention | Medium | Matches campaign naming pattern | Partially consistent | No naming convention |
| G03 | Ad-group theme coherence | High | Enabled, serving keywords and ads express a coherent intent | Mixed intent needs review | Unrelated serving intents share ads or landing pages and performance evidence shows harm |

**G03 accuracy notes:** When evaluating theme coherence: (1) Only count keywords with impressions > 0; dormant zero-impression keywords don't affect ad serving and shouldn't inflate counts. (2) Exclude paused ad groups: `ENABLED` ad groups only (paused groups can have enabled keywords at criterion level but aren't visible in UI). (3) Deduplicate keywords by text per ad group; the same keyword with BROAD + PHRASE match types is one keyword, not two. (4) Exclude stopword-only keywords (e.g., 'attorney', 'lawyers') from coherence scoring; they carry no thematic signal and dilute coherence scores.
| G04 | Campaign fragmentation | High | Structure preserves needed controls without starving learning or duplicating intent | Possible duplication or thin data | Confirmed overlap or data fragmentation harms control or learning |

**G04 accuracy notes:** For multi-location businesses, strip geographic identifiers (city names, state abbreviations, zip codes, metro areas, directional qualifiers like "North"/"South") from campaign names before counting unique objectives. A firm running "Divorce - Chicago", "Divorce - Schaumburg", "Divorce - Naperville" has 1 objective across 3 geos, not 3 separate objectives. Preserve PPC-meaningful terms (brand, nonbrand, pmax, remarketing, etc.).
| G05 | Brand vs Non-Brand separation | Critical | Brand and non-brand in separate campaigns | N/A | Brand and non-brand mixed in same campaign |

**G05/G07/G-PM3 brand detection:** Don't rely solely on campaign naming conventions. Derive brand tokens from the account/business name and scan actual keyword text for brand terms. Classify campaigns by keyword composition: >50% brand keywords = brand campaign. This catches mislabeled campaigns and provides accurate brand vs. non-brand separation.
| G06 | Performance Max applicability | Low | PMax was evaluated against objective, feed/asset readiness, measurement, and control needs | Evaluation is incomplete | N/A; absence is not a health failure |
| G07 | Search + PMax overlap | High | Brand exclusions configured in PMax when Search brand campaign exists | Partial brand exclusions | No brand exclusions in PMax alongside brand Search |
| G08 | Budget allocation matches priority | High | Top-performing campaigns not budget-limited | Minor budget constraints on top performers | Top performers severely budget-limited |
| G09 | Budget pacing | Medium | Pacing matches timezone, demand pattern, objective, and budget period | Isolated or unexplained pacing constraint | Repeated constraint prevents the approved objective or creates runaway spend |
| G10 | Ad schedule configured | Low | Ad schedule set if business has operating hours | N/A | No schedule despite clear business hours |
| G11 | Geographic targeting accuracy | High | "People in" (not "People in or interested in") for local | N/A | "People in or interested in" for local business |
| G12 | Network settings | High | Search Partners and Display inventory are each configured intentionally and evaluated separately | Setting or evidence is unreviewed | Mixed inventory causes confirmed quality or budget-control harm |

**G12 note:** Search Partners typically provides incremental reach at comparable CPA. Flag Search Partners OFF as a missed opportunity (Warning), not ON. Display Network on Search campaigns remains a Fail.

---

## Keywords & Quality Score (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G20 | Average Quality Score | High | Account-wide impression-weighted QS ≥7 | QS 5-6 | QS ≤4 |
| G21 | Critical QS keywords | Critical | <10% of keywords with QS ≤3 | 10-25% with QS ≤3 | >25% with QS ≤4 |
| G22 | Expected CTR component | High | <20% of keywords with "Below Average" expected CTR | 20-35% Below Average | >35% Below Average |
| G23 | Ad relevance component | High | <20% of keywords with "Below Average" ad relevance | 20-35% Below Average | >35% Below Average |
| G24 | Landing page experience | High | <15% of keywords with "Below Average" landing page exp. | 15-30% Below Average | >30% Below Average |
| G25 | Top keyword QS | Medium | Top 20 spend keywords all have QS ≥7 | Some top keywords at QS 5-6 | Top keywords with QS ≤4 |
| G-KW1 | Zero-impression keywords | Medium | No keywords with 0 impressions in last 30 days | <10% zero-impression | >10% of keywords with 0 impressions |
| G-KW2 | Keyword-to-ad relevance | High | Headlines contain primary keyword variants | Partial keyword inclusion | No keyword variants in ad headlines |

---

## Ads & Assets (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G26 | RSA per ad group | High | ≥1 RSA per ad group (≥2 recommended) | 1 RSA per ad group | Ad groups without any RSA |
| G27 | RSA headline count | High | ≥8 unique headlines per RSA (ideal: 12-15) | 3-7 headlines | <3 headlines |
| G28 | RSA description count | Medium | ≥3 descriptions per RSA (ideal: 4) | 2 descriptions | <2 descriptions |
| G29 | RSA Ad Strength | High | All RSAs "Good" or "Excellent" | Some "Average" | Any RSA with "Poor" Ad Strength |
| G30 | RSA pinning strategy | Medium | Strategic pinning (1-2 positions, 2-3 variants each) | Over-pinned (all positions) | N/A |
| G31 | PMax asset coverage | High | Eligible asset groups cover the required asset types and meaningful creative concepts for their inventory | Coverage or creative diversity is partial | Required assets are missing or policy/disapproval state prevents intended delivery |
| G32 | PMax video assets present | High | Native video in all formats (16:9, 1:1, 9:16) | 1-2 formats only | No native video (auto-generated only) |
| G33 | PMax asset group count | Medium | ≥2 asset groups per PMax (intent-segmented) | 1 asset group | N/A |
| G34 | PMax final URL expansion | High | Configured intentionally (ON for discovery, OFF for control) | N/A | Default ON without review |
| G35 | Ad copy relevance to keywords | High | Headlines contain primary keyword variants | Partial keyword inclusion | No keyword relevance in headlines |
| G-AD1 | Ad freshness | Medium | New ad copy tested within last 90 days | N/A | No new ads in >90 days |
| G-AD2 | CTR context | Medium | CTR is interpreted against same-format, same-network, same-objective account cohorts | Only a broad external benchmark is available | A statistically credible account-relative decline is unexplained |

---

## Settings & Targeting (10% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G50 | Sitelink extensions | High | ≥4 sitelinks per campaign | 1-3 sitelinks | No sitelinks |
| G51 | Callout extensions | Medium | ≥4 callouts per campaign | 1-3 callouts | No callouts |
| G52 | Structured snippets | Medium | ≥1 structured snippet set | N/A | No structured snippets |
| G53 | Image extensions | Medium | Image extensions active for search campaigns | N/A | No image extensions |
| G54 | Call extensions (if applicable) | Medium | Call extensions with call tracking for phone-based businesses | Call extension without tracking | No call extension for phone-based business |
| G55 | Lead form extensions | Low | Lead form tested for lead gen accounts | N/A | Not tested |
| G56 | Audience segments applied | High | Remarketing + in-market audiences in Observation mode | Some audiences applied | No audience signals |
| G57 | Customer Match lists | High | Customer Match list uploaded, refreshed <30 days | List >30 days old | No Customer Match lists |
| G58 | Placement exclusions | High | Account-level placement exclusions (games, apps, MFA sites) | Campaign-level only | No placement exclusions |
| G59 | Landing page mobile speed | High | Mobile LCP <2.5s (ideal <2.0s) | LCP 2.5-4.0s | LCP >4.0s |
| G60 | Landing page relevance | High | Landing page H1/title matches ad group theme | Partial relevance | No relevance to ad group |
| G61 | Landing page schema markup | Medium | Product/FAQ/Service schema present | N/A | No schema markup |

---

## Performance Max Extended (scored within Ads & Assets)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G-PM1 | Audience signals configured | High | Custom audience signals per asset group | Generic signals only | No audience signals |
| G-PM2 | PMax Ad Strength | High | "Good" or "Excellent" | "Average" | "Poor" |
| G-PM3 | Brand incrementality review | High | Brand contribution and incrementality are measured with query, experiment, or holdout evidence | Brand share is known but incrementality is not | Confirmed cannibalization conflicts with the campaign objective |
| G-PM4 | Search themes | Medium | Search themes configured (up to 50 per asset group) | <5 search themes | No search themes |
| G-PM5 | Negative keywords | High | Brand + irrelevant negatives applied (up to 10,000) | Some negatives applied | No negative keywords in PMax |
| G-PM6 | PMax negative-keyword applicability | Medium | Campaign- or account-level negatives are used only where search-term evidence justifies them | Evidence exists but scope needs review | Confirmed irrelevant queries persist without appropriate controls |

---

## AI Max & Demand Gen (v1.5, scored within Ads & Assets)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G-AI1 | AI Max for Search evaluation | Low | Availability and fit were evaluated with measurement and query guardrails | Eligible but evaluation is incomplete | N/A; non-adoption is an opportunity, not a health failure |
| G-DG1 | Demand Gen image assets | High | Demand Gen campaigns include BOTH video AND image assets (20% more conversions at same CPA vs video-only). DoorDash case study: 15x higher CVR, 50% lower CPA | Video assets only (missing image uplift) | No Demand Gen campaigns despite eligible account |
| G-DG2 | VAC migration status | Critical | All Video Action Campaigns migrated to Demand Gen (auto-upgraded April 2026) | Migration in progress | VAC campaigns still active (deprecated and will be force-migrated) |
| G-DG3 | Demand Gen frequency capping loss | High | Former VAC campaigns with frequency caps: alternative measurement strategy in place (Video Frequency Groups alpha, or manual frequency monitoring) | Frequency not monitored post-migration | Former VAC campaigns relied on frequency caps now lost in DG with no replacement strategy |

## CTV & Video Tracking (v1.5, scored within Conversion Tracking)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G-CTV1 | CTV Floodlight tracking limitation | High | CTV campaigns use non-Floodlight measurement (Google Ads conversion tracking, GA4). Note: Floodlight conversion measurement DOES NOT work on CTV devices | CTV campaigns active but measurement not verified | CTV campaigns relying on Floodlight for conversion measurement (will not capture CTV conversions) |

---

## Context Notes

- **ECPC deprecation (March 2025)**: Fully deprecated. Flag any remaining ECPC campaigns as FAIL with immediate migration to tCPA, tROAS, or Maximize Conversions.
- **Call Campaigns sunset (Feb 2026)**: Google stopped allowing creation of new Call campaigns in February 2026; existing Call campaigns continue serving until February 2027. Migrate to Search campaigns with call assets before the serving deadline.
- **Power Pack framework**: Google recommends running PMax + Demand Gen + AI Max for Search as a unified campaign stack for maximum coverage across all inventory.
- **AI Max for Search (2025)**: Layers broad match tech and keywordless targeting onto existing Search campaigns. Averages 14% lift in conversions at similar CPA. DSA is likely to be consolidated into AI Max (possible Q2 2026). Requires strong negative keyword lists before adoption.
- **Video Action Campaigns → Demand Gen (April 2026)**: All VACs auto-upgraded to Demand Gen by April 2026. Flag any remaining VAC campaigns as deprecated.
- **Demand Gen limitations**: Frequency capping is NOT supported in Demand Gen (significant loss from VAC). Only workaround: Video Frequency Groups (alpha). Multi-format (video + image) delivers 20% more conversions at same CPA vs video-only.
- **Smart Bidding Exploration (2025)**: Allows flexible ROAS targets to discover new traffic. Delivers 18% more unique search query categories + 19% more conversions.
- **Meridian (2025)**: Google's open-source Marketing Mix Model for incrementality measurement. Useful for advanced accounts evaluating cross-channel contribution.
- **Ads in AI Overviews**: Now showing globally. Requires high ad relevance to appear.

---

## Bidding & Budget (scored within Settings & Targeting)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G36 | Smart bidding strategy active | High | All campaigns with ≥15 conv/30d use automated bidding. ECPC fully deprecated March 2025. Flag any ECPC campaigns for immediate migration to tCPA/tROAS/Max Conversions. Consider Smart Bidding Exploration: allows flexible ROAS targets to discover new traffic, delivering 18% more unique search query categories with conversions and 19% more total conversions | Partially automated, or ECPC campaigns still present (migrate immediately) | Manual CPC on campaigns with sufficient data |
| G37 | Target CPA/ROAS reasonableness | Critical | Targets within 20% of historical performance | Targets 20-50% off historical | Target CPA <50% of actual CPA |
| G38 | Learning phase status | High | <25% of campaigns in "Learning" or "Learning Limited" | 25-40% in learning | >40% in learning |
| G39 | Budget constrained campaigns | High | Top performers show "Eligible" not "Limited by Budget" | Minor budget limitation | Top performers severely budget-limited |
| G40 | Manual CPC justification | Medium | Manual CPC only on campaigns with <15 conv/month | Manual CPC with 15-30 conv/month | Manual CPC with >30 conv/month |
| G41 | Portfolio bid strategies | Medium | Low-volume campaigns grouped into portfolios | N/A | Multiple <15 conv campaigns running independently |

---

## Product-launch discovery (G81-G95, unscored)

These IDs are retained for catalog compatibility. Use them only to discover eligibility,
governance risk, or an experiment opportunity. A missing, announced, beta, future, or
inaccessible feature is `not_applicable`, never a failed health control. Vendor lift figures
must not determine a recommendation.

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| G81 | Ask Advisor governance | High | Ask Advisor (unified Gemini agent across Ads + Analytics + GMP + Merchant Center) used read/insights-only; no unattended write actions | Adopted but write scope unreviewed | Running autonomous write actions without human approval gate |
| G82 | Business Agent for Leads eligibility | Medium | Evaluated for education / automotive / real-estate verticals where AI Max or PMax is active | Eligible vertical but not evaluated | N/A |
| G83 | Direct Offers expansion | Low | Promotion bundling / native checkout evaluated for UCP-eligible merchants | UCP-eligible merchant not yet testing native checkout / bundled offers | Driving promo traffic to slow off-site checkout while UCP Direct Offers sit unused |
| G84 | AI Mode ad-format readiness | Medium | Assets ready for Conversational Discovery / Highlighted Answers / AI-powered Shopping (AI Mode 1B MAU, AI Overviews 2.5B MAU) | Partial asset readiness | No AI-surface asset coverage despite eligibility |
| G85 | Journey-aware bidding | Medium | Biddable + non-biddable goals (calls, forms, newsletter signups) feeding Smart Bidding | Only biddable goals configured | No secondary goals defined for journey signal |
| G86 | Smart Bidding Exploration on PMax + Shopping | High | Enabled where eligible (+27% unique converting users per Google; was Search-only) | Search-only, not expanded to PMax/Shopping | Not evaluated despite eligible conversion volume |
| G87 | Campaign total budgets | Low | Total (vs daily) budgets used where pacing benefits (66% fewer manual adjustments per Google) | Daily budgets only; total budgets not evaluated for flighted/seasonal campaigns | Manual budget babysitting on flighted campaigns that would benefit from total budgets |
| G88 | Demand-led pacing | Low | Demand-led pacing enabled within monthly budget where appropriate | Eligible but still on flat daily pacing through demand spikes | Capping spend on high-demand days while leaving monthly budget unspent on low-demand days |
| G89 | Meridian in GA360 | Low | Meridian MMM (GeoX / Studio / Data Manager Map View) evaluated for incrementality on advanced accounts | GA360 account with budget scale but Meridian incrementality not yet evaluated | Allocating large multi-channel budgets on last-click attribution while Meridian MMM is available and ignored |
| G90 | Qualified Future Conversions (QFCs) | Medium | QFC predictive signal (Gemini, 6-month) evaluated for long-cycle accounts | Long sales-cycle account not yet testing QFCs | Optimizing only to last-click conversions on a 90+ day cycle, ignoring predictive signal |
| G91 | Attributed Branded Searches | Low | New Attributed Branded Searches metric tracked where brand-lift matters | Metric available but not yet added to brand/upper-funnel reporting | Judging brand-building campaigns on last-click ROAS while Attributed Branded Searches goes untracked |
| G92 | Asset Studio Gemini Omni readiness | Low | Creative pipeline ready for Asset Studio (Flash, summer 2026 GA: Veo + Nano Banana, 1-Click Creative Testing, Adobe/Canva pull-through) | Aware of summer 2026 GA but no creative-pipeline prep or Adobe/Canva connection | No Asset Studio adoption plan despite creative-bottlenecked account that would benefit from generative testing |
| G93 | Demand Gen feature stack | Medium | Multimodal video + product feeds (automotive +33% conversions), Campaign Type Attribution, Uplift Experiments adopted where eligible | Demand Gen active but missing feeds/experiments | No Demand Gen despite eligible account |
| G94 | Ads Advisor 3 safety features | Medium | Agentic safety surface (real-time policy reviews, security monitoring, instant certifications) understood and monitored | N/A | Agentic automation in use without safety-feature awareness |
| G95 | DSA migration-readiness evidence | Medium | A current in-account or official notice confirms applicability and the account has a reversible migration plan | Notice exists but readiness evidence is incomplete | Confirmed mandatory migration applies and no owner or rollback plan exists; otherwise `not_applicable` |

---

## Quick Wins (Google)

Items flagged as Quick Win when severity is Critical or High AND fix takes <15 minutes:

| Check | Fix | Time |
|-------|-----|------|
| G43: Enhanced conversions | Enable in Google Ads conversion settings | 5 min |
| G11: Location targeting | Switch to "People in" your targeted locations | 2 min |
| G14: Negative keyword lists | Create initial themed negative lists | 10 min |
| G17: Broad match + Manual CPC | Switch to Smart Bidding or Exact Match | 5 min |
| G12: Network settings | Disable Display Network on Search campaigns | 2 min |
| G05: Brand separation | Split brand keywords into separate campaign | 10 min |
| G50: Sitelink extensions | Add 4+ sitelinks to campaigns | 10 min |
| G-PM6: PMax negative keywords | Add campaign-level negatives to PMax | 10 min |
