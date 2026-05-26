# Microsoft Advertising — Research Notes (May 2026)

**For:** v1.8.0 `/ads microsoft` addendum
**Baseline:** v1.7.0 `/ads microsoft` (existing — 24 checks per `tests/fixtures/check-catalog.yaml`)
**Compiled:** May 26, 2026

This file documents Microsoft Advertising updates that need to be folded into `/ads microsoft` in v1.8.0. Check IDs MS25–MS41.

---

## MS25 — Microsoft AI Max for Search (pilot opened May 2026)

**Primary source:** [about.ads.microsoft.com](https://about.ads.microsoft.com/); Microsoft Advertising Activate 2026 (May 19, 2026); TechWyse "Microsoft Advertising Launches AI Max & Agentic Web Tools"

### What it is

**Distinct from Google's AI Max.** Microsoft's version is more conversational-surface focused — expands query matching across **Copilot Search, Copilot Answers, and Bing**.

### Guardrails

- Brand inclusions / exclusions
- Term exclusions
- Messaging constraints

### Reporting

- Search term + asset reporting at launch
- No position-level reporting initially (similar caveat to Apple Ads multi-placement)

### Performance signals (Microsoft-supplied)

- Early adopters: +5% CTR
- PMax users see +8% incremental conversions when AI Max enabled

### Audit framing

```yaml
- id: MS25
  severity: P1
  applies_when: account in pilot eligibility (US/UK English-speaking retail to start)
  check: |
    Detect AI Max for Search pilot enrollment.
    Verify brand inclusions/exclusions list is populated (not empty).
    Verify term exclusion list covers known irrelevant queries.
    Verify messaging constraints align with brand voice.
  remediation: |
    Pre-pilot prep: build inclusion/exclusion lists from search-term report data.
    Define messaging constraints before enabling.
```

---

## MS26 — Offer Highlights

**Source:** Microsoft Advertising blog April 22, 2026

Product details (free shipping, in-store pickup, price match) appear inside Copilot conversations as structured ad surfaces. **Best Buy is the launch partner.** English-speaking retail.

**Audit check:** detect adoption + verify feed has the requisite fields (`shipping_speed`, `availability_pickup`, etc.).

---

## MS27 — Audience Generation (US + Canada closed pilot)

Plain-language description → targeting (demographics, locations, in-market signals). Audit-relevant for new-campaign launches — verify the user is in pilot eligibility and that the generated audience is bounded by GPC-state opt-out (CA, MD, etc.).

---

## MS28 — Performance Max transparency (April 2026)

Final URL reporting now available. Audit check: verify the user is pulling Final URL spend / impressions / clicks / ROAS data; if PMax is dark, AI Max won't be informative either.

---

## MS29 — Clarity AI Visibility

New diagnostic: how the brand appears in AI interfaces (citations, presence in Copilot answers, etc.). Sits alongside Microsoft Clarity (the heatmap product).

**Audit-relevant:** for SaaS / agency / publisher accounts where AI-Overview / Copilot citation visibility is a goal, this is the platform-native measurement.

---

## MS30 — Brand Agents

Embed on Shopify / WooCommerce. Live April 22, 2026. The commerce-surface equivalent of an AI sales-assistant.

**Audit:** detect Brand Agent installation; verify it's connected to the user's product catalog; verify it respects Special Ad Category constraints.

---

## MS31 — Universal Commerce Protocol (UCP) support in Merchant Center

**Live April 22, 2026 (US).** Microsoft adopted UCP for Copilot Checkout. Shopify Catalog real-time sync — top Shopify merchants saw nearly 90% growth in impression share in Copilot.

See `notes-google.md` for full UCP context (originated at NRF 2026 January 11; Microsoft joined later as a co-implementer).

---

## MS32 — Copilot Checkout

500,000+ US merchants. Target Circle loyalty linking is the launch partner.

Audit-relevant for retail accounts: verify Copilot Checkout eligibility + loyalty program integration.

---

## MS33 — Rewarded Portals

In-game ad format with opt-in engagement and brand lift. Microsoft's gaming network surface. Audit-relevant for entertainment / gaming verticals.

---

## MS34 — Import Center

Consolidated import workflow — Google Ads, Facebook Ads, file uploads now go through a single interface. Replaces the older Google Import + Facebook Import separate tools.

---

## MS35 — Automated bidding updates + custom columns

Refresh in the standard reporting interface. Audit: verify the user has migrated to the new custom-columns API; old "named columns" calls are deprecated.

---

## MS36 — Performance Shift Root Cause Analysis (Copilot diagnostic)

When campaign performance shifts unexpectedly, Copilot now provides an auto-generated root-cause analysis (bid changes, audience drift, creative fatigue, etc.).

**Audit check:** verify the user reviews these diagnostics weekly; flag accounts where Copilot has flagged 3+ shifts in 30 days without remediation.

---

## MS37 — Conversion Tracking Diagnostics

Native diagnostic tool for UET tag / conversion goal health. Audit: verify regular use, flag any "conversion not received in 7 days" warnings.

---

## MS38 — Data-Driven Attribution

Adoption gate: verify DDA model is selected, not Last Click. Microsoft's DDA has been GA for a while but adoption remains uneven.

---

## MS39 — Conversion API (CAPI) server-to-server

UET CAPI for server-side conversion measurement. **Increasingly important** post-iOS 26 (see `compliance-requirements.md` C-iOS-1).

**Audit check:** for accounts with iOS Safari traffic share > 5%, verify Microsoft CAPI is configured.

---

## MS40 — Ad Studio Brand Kit

Brand asset library inside Ad Studio (Microsoft's creative tool). Audit: verify Brand Kit is populated; missing logo / colors / fonts leads to inconsistent generated creative.

---

## MS41 — SOAP API deprecation

**Migration warning.** Microsoft is deprecating SOAP API in favor of REST. Any third-party tool the user is using that talks to Microsoft Advertising via SOAP needs to migrate.

**Audit check:** detect SOAP-based integrations (especially older bid management platforms); flag for REST migration.

---

## Sources

- Microsoft Advertising blog, "What's new" — [about.ads.microsoft.com](https://about.ads.microsoft.com/)
- Microsoft Advertising Activate 2026 May 19, 2026
- TechWyse, "Microsoft Advertising Launches AI Max & Agentic Web Tools" — [techwyse.com/news/ai-search/microsoft-advertising-ai-max-offer-highlights-ucp-agentic-web](https://www.techwyse.com/news/ai-search/microsoft-advertising-ai-max-offer-highlights-ucp-agentic-web)
- ALM Corp Microsoft Advertising Activate 2026 recap
- PPC News Feed Activate 2026 partner coverage
