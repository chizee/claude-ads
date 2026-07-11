# Meta Ads Audit Checklist

<!-- Grounded: 2026-07-11 | source IDs: meta-marketing-api-official, meta-conversions-api-official -->
<!-- Total Checks: 72 | v1.8.0: MCP + attribution rebuild + Q1 2026 AI-stack (M51-M72) -->
<!-- Categories: 5 | See scoring-system.md for weights and algorithm -->

## Runtime evaluation contract

- Establish objective, geography, attribution window, conversion lag, spend, sample size, and feature access before evaluating a row. Missing evidence is `unknown`; ineligible surfaces are `not_applicable`.
- Legacy numeric bands are investigation prompts. Use an account-relative cohort or a directly applicable dated benchmark before they affect health.
- Do not penalize an account for not adopting Advantage+, an AI feature, MCP, a placement, or a vendor integration. M51-M72 are unscored opportunity/governance discovery; only observed unsafe write authority, privacy exposure, or a confirmed mandatory migration may create a health finding.
- Do not repeat vendor lift figures as expected account outcomes.

## Official evidence

- `meta-marketing-api-official`: [Meta Marketing APIs documentation](https://developers.facebook.com/docs/marketing-apis/)
- `meta-conversions-api-official`: [About Conversions API](https://www.facebook.com/business/help/AboutConversionsAPI)

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Pixel / CAPI Health | 30% | M01-M10 (10 checks) |
| Creative (Diversity & Fatigue) | 30% | M25-M32 (8 checks) + M-CR1 through M-CR4 (4 extended) |
| Account Structure | 20% | M11-M18 + M33-M40 (16 checks) + M-ST1, M-ST2 (2 extended) |
| Audience & Targeting | 20% | M19-M24 (6 checks) |
| Product and integration discovery | Unscored | M51-M72 (22 opportunity, applicability, or governance questions) |

---

## Pixel / CAPI Health (30% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M01 | Meta Pixel installed | Critical | Pixel firing on all pages | Firing on most pages (>90%) | Pixel not firing |
| M02 | Conversions API applicability and status | High | Eligible web, app, offline, or CRM events have a consent-valid server connection where it improves completeness | Planned or partial deployment | A material, measurable event gap exists and no server-side option was evaluated |
| M03 | Event deduplication | Critical | Browser and server copies share a stable event identifier and diagnostics show duplicates are controlled | Identifier is present but diagnostics are inconclusive | The same business event is demonstrably counted more than once |
| M04 | Event Match Quality diagnostics | High | Match diagnostics are monitored and lawful match keys are complete for the event source | Diagnostics identify remediable gaps | Material matching failure is observed and unresolved; no universal EMQ number is a health boundary |
| M05 | Domain verification | High | Business domain verified in Business Manager | N/A | Domain not verified |
| M06 | Aggregated measurement applicability | Medium | Current Events Manager requirements are reviewed for the account's web/app events and geography | Configuration evidence is incomplete | A confirmed required event configuration is missing |
| M07 | Standard events vs custom | High | Using standard events (Purchase, AddToCart, Lead, etc.) | Mix of standard and custom | Custom events replacing standard events |
| M08 | CAPI Gateway | Medium | CAPI Gateway deployed for simplified server-side | Direct CAPI integration active | N/A |
| M09 | iOS attribution window | High | 7-day click / 1-day view configured | 1-day click only | Attribution not configured |
| M10 | Data freshness | Medium | Events firing in real-time (no >1hr lag in Events Manager) | <4hr lag | >4hr lag or intermittent firing |

---

## Creative: Diversity & Fatigue (30% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M25 | Creative format diversity | High | Creative coverage matches eligible placements and distinct audience motivations | Coverage is narrow but evidence is inconclusive | A missing required format blocks intended delivery or testing |
| M26 | Creative concept coverage | High | The account tests enough genuinely distinct concepts for its spend and learning rate | Variants exist but concepts are repetitive | Creative scarcity is confirmed by delivery concentration or exhausted tests |
| M27 | Video aspect ratios | High | 9:16 vertical video present for Reels/Stories | Only 1:1 or 4:5 video | No video assets |
| M28 | Creative fatigue detection | Critical | Same-cohort performance, frequency, reach, and conversion quality show no credible fatigue | Directional decline lacks enough data or a matched cohort | A sustained account-relative decline is confirmed after excluding auction, budget, audience, and tracking changes |
| M29 | Hook rate (video) | High | Video ads: <50% skip rate in first 3 seconds | 50-70% skip rate | >70% skip rate in first 3s |
| M30 | Social proof utilization | Medium | Top organic posts boosted as partnership/Spark ads | Some organic boosting | No organic content leveraged |
| M31 | UGC / social-native content | High | ≥30% of creative assets are UGC or social-native | 10-30% UGC content | <10% UGC (all polished/corporate) |
| M32 | Advantage+ Creative | Medium | Advantage+ enhancements enabled (test vs control) | N/A | Not tested |
| M-CR1 | Creative freshness | High | New creative tested within last 14-21 days (tightened from 30d due to Andromeda acceleration) | New creative 21-45 days ago | No new creative in >45 days |
| M-CR2 | Frequency: Prospecting (ad set) | High | Ad set frequency <3.0 in last 7 days | Frequency 3.0-5.0 | Frequency >5.0 (audience exhausted) |
| M-CR3 | Frequency: Retargeting | Medium | Ad set frequency <8.0 in last 7 days | Frequency 8.0-12.0 | Frequency >12.0 |
| M-CR4 | CTR benchmark | Medium | CTR is compared with a same-objective, placement, format, geography, and date-window cohort | Only a broad benchmark is available | A statistically credible account-relative decline is unexplained |

---

## Account Structure (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M11 | Campaign fragmentation | High | Structure preserves necessary controls without duplicated auctions or starved learning | Possible duplication needs evidence | Confirmed overlap or fragmentation harms delivery, learning, or governance |
| M12 | Campaign- versus ad-set-budget control | High | Budget control matches the experiment or allocation objective and has observed delivery evidence | Choice is undocumented or evidence is incomplete | Allocation behavior conflicts with approved priorities |
| M13 | Learning phase status | Critical | <30% of ad sets in "Learning Limited" | 30-50% Learning Limited | >50% ad sets "Learning Limited" |
| M14 | Learning phase resets | High | No unnecessary edits during learning phase | 1-2 minor resets | Frequent resets from edits during learning |
| M15 | Advantage+ Sales campaign | Medium | Advantage+ Sales (renamed from ASC early 2025) active for e-commerce with catalog. Existing customer budget cap eliminated Feb 2025. Research: 22% higher ROAS, 11.7% CPA improvement | Advantage+ Sales tested but paused | Not tested despite eligible catalog |
| M16 | Ad set consolidation | High | No overlapping ad sets targeting same audience | Minor overlap (<20%) | Significant audience overlap (>30%) |
| M17 | Budget distribution | High | Ad-set delivery is sufficient for the approved test or objective | Thin delivery makes inference provisional | Starved delivery prevents the approved objective while budget is available elsewhere |
| M18 | Campaign objective alignment | High | Objective matches actual business goal | N/A | Objective mismatched (e.g., Traffic for Sales) |
| M33 | Advantage+ Placements | Medium | Advantage+ Placements enabled (unless exclusion needed) | Manual placements (justified) | Manual placements limiting delivery without reason |
| M34 | Placement performance review | Medium | Breakdown reviewed monthly; underperformers excluded | Reviewed quarterly | Never reviewed |
| M35 | Attribution setting | High | Attribution windows verified post-Jan 2026 changes (7-day and 28-day view-through windows REMOVED January 2026). 7-day click / 1-day view configured where available | 1-day click only | Attribution not configured or still expecting removed view-through windows |
| M36 | Bid strategy appropriateness | High | Cost Cap for margin protection; Lowest Cost for volume | N/A | Bid Cap set below historical CPA |
| M37 | Frequency cap monitoring (campaign) | High | Campaign-level prospecting frequency <4.0 (7-day) | Frequency 4.0-6.0 | Frequency >6.0 |
| M38 | Breakdown reporting | Medium | Age, gender, placement, platform reviewed monthly | Reviewed quarterly | Never reviewed |
| M39 | UTM parameters | Medium | UTM parameters on all ad URLs for GA4 attribution | UTMs on some ads | No UTM parameters |
| M40 | A/B testing active | Medium | At least 1 active A/B test (Experiments) | Test planned | No testing infrastructure |
| M-ST1 | Budget adequacy | High | Budget is justified by target economics, conversion lag, expected event volume, and the test design | Data is insufficient to judge | Budget makes the approved target or test statistically infeasible |
| M-ST2 | Budget utilization | Medium | >80% of daily budget being utilized | 60-80% utilization | <60% utilization |

---

## Audience & Targeting (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M19 | Audience overlap | High | Overlap is intentional or experiment-safe and does not create harmful fragmentation | Overlap exists but impact is unknown | Controlled evidence shows overlap harms delivery or test validity |
| M20 | Custom Audience freshness | High | Website Custom Audiences refreshed within 180 days | 180-365 days old | >365 days old or not created |
| M21 | Lookalike source quality | Medium | Lookalike source ≥1,000 users from high-value events | 500-1,000 users | <500 users or low-value source |
| M22 | Advantage+ Audience testing | Medium | Advantage+ Audience tested vs manual | N/A | Not tested |
| M23 | Exclusion audiences | High | Purchasers/converters excluded from prospecting | Partial exclusions | No purchaser exclusions from prospecting |
| M24 | First-party data utilization | High | Customer list uploaded for Custom Audience + Lookalike | List uploaded but not refreshed | No first-party data uploaded |

---

## Andromeda and platform-change discovery (unscored)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M-AN1 | Andromeda creative diversity | Critical | Ads genuinely diverse across creative concepts, messaging motivators, visual styles. Creative Similarity Score <60% across ad set. Different motivators unlock new audiences 89% of the time | Some diversity but similar visual templates or minor copy variations | All ads are minor variations (Andromeda clusters similar ads with Entity IDs; 100 minor variations = no better than 10) |
| M-AT1 | Attribution window post-Jan 2026 | High | Attribution windows verified and aligned with business model after Jan 2026 removal of 7-day/28-day view-through options | Using default settings without review | Attribution settings not configured or still expecting removed windows |
| M-IA1 | Incremental Attribution testing | Medium | Meta Incremental Attribution (launched April 2025) evaluated or active for measuring real causal impact via AI-powered holdout testing | N/A | Not evaluated despite sufficient budget (>$5K/month) |
| M-TH1 | Threads placement evaluation | Low | Threads placement reviewed (GA Jan 2026, 400M+ MAU). Lower CPMs but only ~0.04% of ad spend in Q3 2025. Worth testing for incremental reach | N/A | Not evaluated |

---

## Product and integration discovery (M51-M72, unscored)

These IDs are retained for catalog compatibility and must be re-verified against current
official documentation or in-account evidence. Missing access or non-adoption is
`not_applicable` or an opportunity, never a failed health control. Safety and privacy rows
may create findings only from observed scopes, write behavior, or data transmission.

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| M51 | Meta Ads MCP server inventory | Medium | A connected integration's endpoint, owner, tools, scopes, and rate behavior are inventoried from live evidence | Connection exists but inventory is incomplete | N/A |
| M52 | MCP paused-by-default enforcement | High | All MCP-created campaigns launch PAUSED and pass human review before activation | Manual activation policy exists but not enforced in workflow | MCP campaigns auto-activating without human review |
| M53 | MCP write-action governance | Critical | Read scope is preferred; any write scope is protected by exact preview, approval, audit, verification, and rollback | Write scope exists but the gate is incomplete | Write authority can change account state without an explicit approval gate |
| M54 | March 3 2026 click-through redefinition | Medium | Reporting interpreted under new definition: click-through now counts ONLY link clicks | Aware of change but reports not yet re-baselined | Click-through still read under pre-March-3 definition |
| M55 | Engage-through attribution column | Medium | New engage-through column (likes / shares / saves / expansions / video views) present and used in reporting | Column available but ignored | Engage-through signal not surfaced in reporting |
| M56 | Engaged-view threshold | Low | Engaged-view threshold understood as 5s (dropped from 10s) | N/A | Reporting still assumes the old 10s threshold |
| M57 | Default attribution windows | Medium | Default 7-day click / 1-day engage-through / 1-day view validated against sales cycle | Defaults accepted without validation | Windows misaligned with sales cycle |
| M58 | Pre-March-3-2026 baseline guard | High | YoY comparisons across the March 3 2026 boundary are flagged as non-comparable (analyst consensus, not Meta's stated position) | Boundary noted informally but not flagged in reports | Reporting compares across the boundary with no flag |
| M59 | View-through integration (Northbeam / Triple Whale) | Low | Northbeam + Triple Whale view-through integration evaluated or active | Integration available but not connected | Running with no view-through visibility while a connected tool would expose it |
| M60 | GEM claim provenance | Low | Any GEM claim is dated, vendor-labeled, and excluded from account thresholds | Claim is present but provenance is incomplete | N/A |
| M61 | Lattice claim provenance | Low | Any Lattice claim is dated, vendor-labeled, and excluded from account thresholds | Claim is present but provenance is incomplete | N/A |
| M62 | Andromeda claim provenance | Low | Any retrieval-system claim is dated, vendor-labeled, and separated from observed account evidence | Claim is present but provenance is incomplete | N/A |
| M63 | ARM (Adaptive Ranking Model) readiness | Medium | Broad targeting + campaigns >=30 days so ARM (newest layer; +3% CVR / +5% CTR; removes truncation ceiling for long-history users) has depth signal; returning-customer audiences segmented. See meta-ai-stack.md | Some campaigns short-lived or narrowly targeted, limiting ARM depth | Narrow targeting and short campaigns starving ARM of signal |
| M64 | Incremental Attribution as reporting view | High | Incremental Attribution (Q4 2025 model; +24% incremental conversions vs standard) used as a reporting view | Evaluated but not adopted as a standing view | Not used, causing over-counting / over-spend on last-click tactics |
| M65 | Ad-level placement control | Low | Placement control applied at ad level where useful (was ad-set level) | Still managing placements only at ad-set level | Forcing uniform placements where ad-level control would cut waste |
| M66 | AI-generated Instant Forms | Low | AI-generated Instant Forms from URL/prompt evaluated for lead campaigns | Feature available but not tested on lead campaigns | Hand-building lead forms where AI-generated Instant Forms would speed launch and lift completion |
| M67 | 730-day purchase audience retention governance | High | 730-day purchase audience retention with auto-expansion (was 180) detected, surfaced, and put through explicit review | Detected but review pending | Enabled without governance review |
| M68 | Pixel auto-include detailed info governance | High | New Pixel "auto-include detailed page/product info" setting (often default ON; sends product/page metadata to Meta) detected and reviewed | Detected but review pending | ON without governance review |
| M69 | Advantage+ Creative Image Generation Categories | Low | Advantage+ Creative Image Generation Categories ("Refined product look", "Popular in your niche", "High ROAS") evaluated | Categories available but not tested | Ignoring Advantage+ Creative categories on high-volume ecommerce where they lift ROAS |
| M70 | Automotive market-code migration evidence | High | A current official or in-account notice confirms applicability and the account uses the supported market codes | Migration applies but evidence is incomplete | A confirmed required migration is unresolved; otherwise `not_applicable` |
| M71 | Digital Services Tax pass-through | Low | DST pass-through fees (up to 5%: Austria, France, Italy, Spain, Turkey, UK) accounted for in budget math where applicable | DST-affected markets active but fees not modeled in budget math | Spending in DST markets while treating list budgets as final, understating true cost |
| M72 | CAPI one-click setup + EMQ | High | CAPI one-click setup (Apr 2026) verified enabled and Event Match Quality >= 7 on purchase events | CAPI enabled but EMQ 6.0-6.9 on purchase events | No CAPI, or EMQ < 7 on purchase events |

---

## Context Notes

- **Detailed targeting exclusions removal (2025-2026)**: Meta phased out detailed targeting exclusions starting March 2025, with full removal by January 2026. Advertisers must now use Custom Audience exclusions or Advantage+ Audience instead.
- **Flexible Ads (2024)**: Format launched mid-2024 that automatically optimizes creative elements (headline, image, video) per placement. Evaluate adoption alongside Advantage+ Creative enhancements.
- **Financial Products Special Ad Category (Jan 2025)**: Financial products (loans, insurance, credit cards, investment services) are now enforced as a Special Ad Category with the same targeting restrictions as Housing/Employment/Credit.
- **Andromeda (Oct 2025)**: Meta's AI retrieval engine filters tens of millions of ads down to ~1,000 candidates using 10,000x more complex models. Creative diversity is now the #1 performance lever.
- **Offline Conversions API (May 2025)**: Permanently discontinued. Use CAPI with action_source="physical_store" for offline tracking.
- **Link clicks redefinition (Feb 2025)**: Meta redefined "link clicks" to exclude social engagement clicks. Accounts comparing pre/post Feb 2025 data may see apparent CTR drops. This is a metric change, not a performance decline.
- **Meta Shops checkout (June-August 2025)**: Native checkout phased out, redirects to website.
- **Advantage+ Sales**: Renamed from ASC early 2025. Customer budget cap eliminated Feb 2025.

---

## Quick Wins (Meta)

| Check | Fix | Time |
|-------|-----|------|
| M02: CAPI setup | Deploy via CAPI Gateway (simplified) or direct integration | 15 min (Gateway) |
| M05: Domain verification | Verify domain in Business Manager | 5 min |
| M09: Attribution window | Set to 7-day click / 1-day view in ad set settings | 2 min |
| M23: Exclusion audiences | Create Custom Audience of purchasers, exclude from prospecting | 10 min |
| M25: Format diversity | Add video or carousel to single-image-only ad sets | 15 min |
| M39: UTM parameters | Add UTM template at campaign level | 5 min |
| M35: Attribution setting | Switch from 1-day click to 7-day click / 1-day view | 2 min |

---

## Special Ad Categories Compliance

If running ads in restricted categories, these ADDITIONAL checks apply:

| Category | Requirement | Enforcement |
|----------|-------------|-------------|
| Housing | No ZIP code targeting, age 18-65+ only, no Lookalike | Campaign disapproval |
| Employment | Same as Housing | Campaign disapproval |
| Credit | Same as Housing | Campaign disapproval |
| Financial Products | New Jan 2025: enforced as Special Category | Campaign disapproval |

Must declare Special Ad Category BEFORE campaign creation. See `compliance.md` for full details.
