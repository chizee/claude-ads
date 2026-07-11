# LinkedIn Ads Audit Checklist

<!-- Grounded: 2026-07-11 | source IDs: linkedin-marketing-api-official, linkedin-conversion-tracking-official, linkedin-conversions-api-official -->
<!-- Total Checks: 46 | v1.8.0: Off-Platform Event Ads + rename (L28-L46) -->

## Runtime evaluation contract

- Establish B2B objective, ICP, geography, buying cycle, conversion lag, spend, sample size, format, and feature access first. Missing evidence is `unknown`; irrelevant formats or unavailable features are `not_applicable`.
- Numeric audience, budget, CTR, CPC, frequency, form, and attribution bands are practitioner prompts. They affect health only with a comparable account cohort or a current official eligibility rule.
- L28-L46 are unscored discovery. Product adoption, certification, AI features, premium formats, and roadmap awareness are not account health.
- Use current Campaign Manager/API evidence for hierarchy and availability; do not infer either from a dated announcement.

## Official evidence

- `linkedin-marketing-api-official`: [LinkedIn Marketing Developer Platform](https://learn.microsoft.com/en-us/linkedin/marketing/overview)
- `linkedin-conversion-tracking-official`: [Conversion Tracking](https://learn.microsoft.com/en-us/linkedin/marketing/integrations/ads-reporting/conversion-tracking)
- `linkedin-conversions-api-official`: [Conversions API use cases](https://learn.microsoft.com/en-us/linkedin/marketing/conversions/conversions-usecase)

## Quick Reference

| Category | Weight | Check Count |
|----------|--------|-------------|
| Technical Setup | 25% | L01-L02 (2 checks) |
| Audience Quality | 25% | L03-L09 (7 checks) |
| Creative & Formats | 20% | L10-L13 (4 checks) |
| Lead Gen Forms | 15% | L14-L15 (2 checks) |
| Bidding & Budget | 15% | L16-L17 (2 checks) |
| Structure & Performance | N/A | L18-L25 (8 checks, scored across categories) |
| CRM & Compliance | 10% | L-CRM1, L-EU1 (2 checks) |
| Product and format discovery | Unscored | L28-L46 (19 applicability, opportunity, or mapping questions) |

---

## Technical Setup (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L01 | Insight Tag installed | Critical | LinkedIn Insight Tag firing on all pages | Firing on most pages (>90%) | Tag not installed or broken |
| L02 | Conversions API applicability and status | High | Eligible conversions use Insight Tag, Conversions API, CSV, or a justified combination with deduplication | Setup is partial or evidence is incomplete | A material measurement gap exists and no supported source was evaluated |

---

## Audience Quality (25% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L03 | Job title targeting precision | High | Specific job titles matching ICP (not just functions) | Broad function targeting only | No job title targeting |
| L04 | Company size filtering | Medium | Company size matches ICP | Includes all sizes | N/A |
| L05 | Seniority level targeting | High | Seniority appropriate for offer (C-suite for enterprise, Manager for mid-market) | Broad seniority targeting | Mismatched seniority level |
| L06 | Matched Audiences | High | Website retargeting + contact list audiences active | One type active | No matched audiences |
| L07 | ABM company-list applicability | Medium | An authorized, policy-compliant company list represents the approved ICP where ABM is the strategy | Coverage is partial | N/A when ABM is not the approved strategy; otherwise confirmed ICP coverage is missing |
| L08 | Audience expansion setting | Medium | OFF for precise targeting, ON for scale (intentional). **CRITICAL: Always uncheck Audience Expansion for ABM campaigns.** ABM budget distribution can be wildly uneven. One case showed 96% of budget going to just 3 accounts out of 400 targeted (AJ Wilcox, B2Linked) | N/A | Default ON without review |
| L09 | Predictive audiences | Medium | Predictive audiences tested (replaced Lookalike Audiences 2024; 21% CPL reduction). Now accepts company lists and retargeting sources as inputs (March 2025) | N/A | Not tested for eligible campaigns |

---

## Creative & Formats (20% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L10 | Thought Leader Ads applicability | Low | Format fit, authorization, brand risk, and account-relative experiment evidence were evaluated | Experiment is incomplete | N/A; absence is not a health failure |
| L11 | Ad format diversity | High | ≥2 formats tested (single image, video, document, carousel) | 1 format only | N/A |
| L12 | Video ads present | Medium | Video ads tested | N/A | No video tested |
| L13 | Creative refresh cadence | Medium | Creative refreshed every 4-6 weeks | Refreshed every 6-10 weeks | Same creative >10 weeks |

---

## Lead Gen Forms (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L14 | Lead Gen Form friction | High | Every field is required for routing, qualification, consent, or sales follow-up and form quality is measured | Some fields lack a documented purpose | Unnecessary fields create confirmed abandonment or policy risk |
| L15 | Lead Gen Form CRM integration | High | Form synced to CRM in real-time | Synced within 24hrs | Manual CSV download only |

---

## Bidding & Budget (15% weight)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L16 | Bid strategy appropriate | High | Manual CPC or Cost Cap for cost control; start manual, then test automated bidding with established data | N/A | Maximum Delivery left as default without cost analysis (most expensive option) |
| L17 | Budget sufficiency | High | Budget supports the approved auction, conversion economics, and experiment duration | Delivery or sample is inconclusive | Budget makes the approved objective or test infeasible |

---

## Structure & Performance (scored across categories)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L18 | Ad Set objective alignment | High | Objective matches funnel stage | N/A | Objective mismatched to goal |
| L19 | A/B testing active | Medium | Active A/B test on creative or audience | Test planned | No testing |
| L20 | Frequency monitoring | High | Message frequency ≤1 per 30-45 days per user | 1 per 20-30 days | >1 per 20 days (inbox fatigue) |
| L21 | CTR benchmark | Medium | CTR is compared with a same-objective, format, placement, geography, and date-window cohort | Only a broad benchmark is available | A statistically credible account-relative decline is unexplained |
| L22 | CPC benchmark | Medium | CPC is evaluated with conversion quality and a comparable account cohort | Only a broad benchmark is available | Higher cost produces worse qualified economics at adequate sample |
| L23 | Lead quality tracking | High | Lead-to-opportunity rate tracked (not just CPL) | CPL tracked only | No lead quality metrics |
| L24 | Conversion tracking attribution | Medium | 30-day click / 7-day view window configured | Default window without review | Attribution not configured |
| L25 | Demographics report review | Medium | Job title and company breakdown reviewed monthly | Reviewed quarterly | Never reviewed |

---

## CRM & Compliance (v1.5)

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L-CRM1 | CRM integration for revenue attribution | High | Salesforce or HubSpot CRM integration configured (launched June 2025) enabling closed-loop reporting from impression to revenue | CRM available but not integrated with LinkedIn | No CRM integration despite having Salesforce/HubSpot (missing revenue attribution loop) |
| L-EU1 | EU Sponsored Messaging compliance | Medium | No Message Ads or Conversation Ads targeting EU audiences (EU Sponsored Messaging discontinued since January 2022) | N/A | Message/Conversation Ads targeting EU audiences (will not deliver; discontinued) |

---

## Product and format discovery (L28-L46, unscored)

These IDs are retained for catalog compatibility. Re-verify terminology, availability,
geography, and eligibility through current official documentation or account evidence.
Missing access or non-adoption is `not_applicable` or an opportunity, never a health failure.

| ID | Check | Severity | Pass | Warning | Fail |
|----|-------|----------|------|---------|------|
| L28 | Off-Platform Event Ads (full rollout May 6, 2026) | Medium | B2B/SaaS event campaigns evaluated for the event-format ad: no LinkedIn Event Page required; supports webinars/field/hybrid; Lead Gen syncs to Salesforce/HubSpot/Marketo; Cvent/ON24/Integrate integrations | Format known but not evaluated for relevant event campaigns | N/A |
| L29 | Campaign Manager terminology rename trap | High | UTM/tracking templates map correctly: UI renamed "Campaign Group"->"Campaign" and "Campaign"->"Ad set", but the API kept old terms (`adCampaignGroups`, `campaignGroup`, `campaign`) | UI/API mapping not verified after rename | UTM/templates mismap UI vs API hierarchy |
| L30 | Accelerate auto-campaign creation | Low | Accelerate AI auto-campaign creation evaluated | Eligible but auto-campaign creation not evaluated | Ignored despite sufficient conversion history that fits Accelerate |
| L31 | AI Ad Variants | Low | AI Ad Variants (multiple variants from a single input) evaluated | Available but variant generation not evaluated | Ignored despite a clear creative-testing need that AI Ad Variants would serve |
| L32 | Career Journey targeting | Medium | Career Journey targeting (recent promotions / new job placements) evaluated for relevant ABM plays | Eligible ABM plays not evaluated | N/A |
| L33 | Reserved Ads | Low | Reserved Ads (premium guaranteed inventory) evaluated for awareness | Awareness budget present but Reserved Ads not evaluated | Running large brand pushes with no guaranteed premium inventory |
| L34 | First Impression Ads | Low | First Impression Ads (premium first-position) evaluated for awareness | Awareness budget present but First Impression Ads not evaluated | Ignored despite an awareness goal that premium first-position placement would serve |
| L35 | BrandLink expansion | Low | BrandLink expansion evaluated for brand-safe video reach | Eligible but BrandLink not evaluated for video campaigns | Ignored despite running brand video with an awareness goal that fits BrandLink |
| L36 | Wire | Low | Wire (short-form B2B video) evaluated | Available but Wire short-form video not evaluated | Ignored despite clear B2B fit for short-form video reach |
| L37 | Thought Leader Event Ads | Low | Thought Leader Event Ads evaluated | Eligible event/TLA plays present but format not evaluated | Ignored despite running events and TLAs that this format would combine |
| L38 | CTV expansion | Low | CTV expansion evaluated for B2B brand reach | Awareness budget present but CTV expansion not evaluated | Ignored despite a B2B brand-reach goal that CTV inventory would serve |
| L39 | Company Attribution in Revenue Attribution Report | Medium | Company-level attribution reviewed for B2B (accounts for 272-day journey) | Report available but company-level view not reviewed | N/A |
| L40 | MRC accreditation for video metrics | Low | MRC accreditation noted in benchmark caveats (LinkedIn pursuing; video metrics not yet third-party accredited) | Video metrics reported but accreditation caveat not noted | Relevant video budget reported on un-accredited metrics with no caveat flagged |
| L41 | Company Intelligence API | Low | Company Intelligence API (May 2026) evaluated | Available but Company Intelligence API not evaluated | Ignored despite clear ABM/B2B fit for company-level intelligence |
| L42 | Flexible Ad Creation availability | Low | Current official or account evidence confirms access and the feature has an owner-approved experiment rationale | Availability is unknown | N/A when unavailable; non-adoption is an opportunity |
| L43 | SMB Auto-targeting + Draft with AI | Low | SMB Auto-targeting + Draft with AI (Apr 2026) evaluated | Available but SMB Auto-targeting + Draft with AI not evaluated | Ignored despite an SMB account that this lightweight setup path would serve |
| L44 | Real-time CRM data in Campaign Manager | Medium | CRM connected so audiences/exclusions stay fresh via real-time CRM data in Campaign Manager | CRM available but not connected for real-time refresh | N/A |
| L45 | Ads Agency Certification | Low | Certification is evaluated only when it is a documented business objective and current prerequisites are verified | Evaluation is incomplete | N/A; certification is not paid-account health |
| L46 | Organic-signal relevance | Low | Any organic signal used in paid strategy is based on observed first-party performance and policy-compliant behavior | Evidence is incomplete | N/A; unverified algorithm folklore must not affect paid-account health |

---

## Quick Wins (LinkedIn)

| Check | Fix | Time |
|-------|-----|------|
| L01: Insight Tag | Install/verify Insight Tag on all pages | 10 min |
| L10: Thought Leader Ads | Create TLA using employee organic posts | 10 min |
| L14: Lead Gen Form fields | Reduce form to ≤5 fields | 5 min |
| L08: Audience expansion | Review and set intentionally (OFF for precision) | 2 min |
| L20: Message frequency | Set frequency cap to 1 per 30-45 days | 2 min |
| L24: Attribution window | Configure 30-day click / 7-day view | 2 min |

---

## Context Notes

- **October 2025 naming**: Campaign Groups renamed to "Campaigns"; Campaigns renamed to "Ad Sets"
- **CRM integration (June 2025)**: Salesforce/HubSpot closed-loop reporting from impression to revenue
- **TLA expansion (March 2025)**: Non-employee members can now be featured in Thought Leader Ads
- **Predictive Audiences (March 2025)**: Now accept company lists and retargeting sources
- **LinkedIn Audience Network**: Expert consensus (AJ Wilcox, $200M+ spend): turn it OFF. Quality is poor. It's enabled by default
- **Document Ads**: 7.00% engagement rate (14% YoY increase), leading all LinkedIn content formats
- **Conversation Ads**: 50-60% open rates, 2-5% CTR (far exceeds feed benchmarks of 0.3-0.5%)
- **Connected TV Ads (2025)**: LinkedIn extended reach to CTV inventory via partnerships, allowing B2B brand campaigns on streaming platforms.
- **BrandLink (2025)**: Premium video placement alongside trusted publisher content on LinkedIn. Ideal for awareness-stage B2B campaigns.
- **Live Event Ads (2025)**: Sponsored LinkedIn Live events with built-in registration and reminder flows. Effective for webinar-driven lead gen.
- **Accelerate ad sets**: LinkedIn's AI-optimized ad set type delivers 42% lower CPA and 21% lower CPL on average. Recommended for advertisers with sufficient conversion history.

---

## LinkedIn-Specific Context

| Fact | Value |
|------|-------|
| Minimum audience for delivery | 500 members |
| Recommended audience size | 50,000-300,000 |
| Predictive Audiences seed | 300+ members |
| Company list upload limit | 300,000 |
| Lookalike audiences | Discontinued Feb 29, 2024 |
| Lead Gen Form CVR benchmark | 13% (3.25x landing pages) |
| B2B ROAS benchmark | 113% ($1.13 per $1 spent) |
| Accelerate ad sets | 42% lower CPA, 21% lower CPL |
| TLA CPC advantage | $2.29-4.14 vs $13.23 standard |
| Hierarchy naming (Oct 2025) | "Campaigns" (formerly Campaign Groups) → "Ad Sets" (formerly Campaigns) |
