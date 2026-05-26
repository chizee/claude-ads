# Google Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads google` addendum
**Baseline:** v1.7.0 `/ads google` AI Max era rewrite (May 17, 2026) + v1.7.1 factual citation polish (May 18, 2026)
**Compiled:** May 26, 2026

This file documents the Google Ads updates that landed AFTER the v1.7.0 cut (May 17, 2026) and need to be folded into `/ads google` in v1.8.0. Check IDs G81–G95.

---

## Google Marketing Live 2026 — May 20, 2026

**Primary source:** [blog.google/products/ads-commerce/google-marketing-live-2026-collection/](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/) (Vidhya Srinivasan, May 20, 2026)

**Timing note:** GML happened 3 days AFTER v1.7.0 shipped and 2 days AFTER v1.7.1 shipped. So the `/ads google` AI Max rewrite captures the April 15 AI Max GA moment but NOT the May 20 layer-on (Ask Advisor, AI Mode ad formats, Demand Gen expansions, bidding/budgeting/measurement disclosures). This is the work for v1.8.0.

### Ask Advisor (G81)

**Status:** Beta, English-only globally
**Replaces:** Ads Advisor, Analytics Advisor, the forthcoming Merchant Center agent

A unified Gemini agent spanning Google Ads + Google Analytics + Google Marketing Platform + Merchant Center. Per Google: "Think of it as your always-on strategic partner, connecting the dots across our products to help you save time and grow your business."

**Audit implication:** Detect adoption. Verify it's not running unattended write actions. If a user has Ask Advisor connected and is also using Google Ads MCP, ensure there's no overlap of write-action governance.

### AI Mode ad formats (G84)

Google I/O May 19, 2026 disclosed AI Mode at 1B MAU and AI Overviews at 2.5B MAU. AI Mode queries average 3× the length of traditional searches. Ad formats now serving inside AI Mode:

- **Conversational Discovery ads** — embedded in AI chat surfaces
- **Highlighted Answers** — sponsored answer placements
- **AI-powered Shopping ads** — Gemini-summarized product carousels
- **Direct Offers expansion** — promotion bundling + native checkout for UCP merchants (G83)
- **Business Agent for Leads** — pilot in education / automotive / real-estate verticals; requires AI Max or Performance Max (G82)

### Bidding/budgeting (G85–G88)

**Source:** Google Ads blog May 7, 2026 disclosures

- **Journey-aware bidding (beta)** — learns from biddable AND non-biddable conversion goals (phone calls, form submissions, newsletter signups)
- **Smart Bidding Exploration** expanded from Search-only to **Performance Max + Shopping**; +27% unique converting users per Google
- **Campaign total budgets** — 66% reduction in manual budget adjustments per Google
- **Demand-led pacing** — Google AI optimizes spend within monthly budget to capture demand peaks

### Measurement (G89–G91)

**Source:** Google Ads blog May 5, 2026 disclosures

- **Meridian integrated into GA360** — open-source MMM brought inside the GA360 reporting interface
- **Meridian GeoX + Meridian Studio + Data Manager Map View** — geo-experiment design and visualization
- **Qualified Future Conversions (QFCs)** — Gemini-powered, predicts up to 6 months ahead
- **Attributed Branded Searches** — new metric tying upper-funnel spend to brand-search lift
- **Data Manager API** — direct connectors to Mailchimp, ActiveCampaign, Klaviyo
- **TransUnion integration** for privacy-safe third-party data

**Cases for benchmarks.md:** Crew Clothing +70% long-term conversions; Doc Martens +16% revenue from first-party data.

### Asset Studio (G92)

- **Gemini Omni (Flash)** integrated — summer 2026 GA; any-input-any-output (text/image/video)
- **1-Click Creative Testing**
- **Veo + Nano Banana** integration
- **Adobe + Canva pull-through**
- **Asset Studio API** (programmatic creative pipeline)

### Demand Gen (G93)

- Multimodal video creation in Asset Studio
- Creator partnership boost in asset picker
- Merchant Center video distribution
- Google Maps inventory
- Checkout links expanded to 9 new markets
- Product feeds expanded to automotive (+33% conversions per Google)
- One-click Demand Gen creation from PMax campaigns
- Campaign Type Attribution to isolate Demand Gen conversions
- Uplift Experiments to measure incremental contribution
- TransUnion + privacy-safe partner integrations

### Ads Advisor 3 agentic safety features (G94)

**Source:** Google Ads blog April 21, 2026

- Real-time policy reviews
- Security monitoring
- Instant certifications

---

## DSA → AI Max forced migration (G95) — September 2026 P0

**Primary source:** Google AI Max for Search GA announcement, April 15, 2026

Verbatim:
> "Starting in September, remaining eligible Search campaigns with legacy settings will automatically upgrade to AI Max, and advertisers will no longer be able to create new campaigns with DSA via Google Ads, Google Ads Editor, or the Google Ads API."

**No opt-out.** DSA users get all three AI Max features enabled by default: search term matching, text customization, and Final URL Expansion.

**Practitioner concern (Digital Applied, NateCue, ALM Corp):** the September timing means the learning period overlaps Black Friday for many e-commerce accounts. This is NOT in Google's official announcement — flag as practitioner analysis.

**Audit check G95:** for any account currently running DSA campaigns, surface this as a P0 hard gate. Recommend pre-migration AI Brief drafting (Messaging Guidelines / Matching Guidelines / Audience Guidelines), text disclaimer setup for regulated industries (FUE compatibility), and brand exclusion list build-out.

---

## AI Max performance claims — contested

**Google-supplied case studies:**
- Lufthansa +24% AI Max ROAS
- IKEA +65% non-branded clicks / +28% incremental ROAS
- AI Max users +15% conversions at similar ROAS

**Independent analysis (April 2026):** JumpFly study + 84% advertiser survey show neutral-to-negative results.

**For benchmarks.md:** flag both. Cite Google's official case studies as "Google-supplied, not independently audited." Cite JumpFly + survey results as the counter.

---

## Universal Commerce Protocol (UCP)

**Primary source:** [blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/](https://blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/) (Sundar Pichai, January 11, 2026)

Already covered in `mcp-integration.md` and cross-referenced in `notes-amazon.md` / `notes-microsoft.md` (both joined UCP later). Key Google-side checks:

- `native_commerce` Merchant Center attribute (the eligibility field)
- `/.well-known/ucp` JSON manifest on the merchant's domain (specification version 2026-04-08)
- RS256/ES256 signing keys for agent-payment-protocol authentication
- Webhook endpoints for order lifecycle events
- Shopping Graph 60B+ listings now searchable from Universal Cart

**Universal Cart began rolling out in the US on May 19, 2026** at Google I/O; expanding to Canada, Australia, UK and into food delivery / travel.

**AP2 (Agent Payments Protocol)** donated to FIDO Alliance April 28, 2026. Compatible with A2A, MCP.

---

## Google Ads MCP — already in /ads google

The `/ads google` rewrite in v1.7.0 already covers `ai_max_setting.enable_ai_max`, AI Brief, FUE, brand exclusions. The Google Ads MCP repository is at <https://github.com/googleads/google-ads-mcp> (open-sourced October 7, 2025). For audit details on the MCP integration, see `mcp-integration.md`.

---

## Sources used in this notes file

- Google Marketing Live 2026 collection — [blog.google/products/ads-commerce/google-marketing-live-2026-collection/](https://blog.google/products/ads-commerce/google-marketing-live-2026-collection/)
- Sundar Pichai NRF 2026 remarks — [blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/](https://blog.google/company-news/inside-google/message-ceo/nrf-2026-remarks/)
- AI Max for Search GA April 15, 2026 — Google Ads blog
- May 5, 2026 measurement disclosures — Google Ads blog
- May 7, 2026 bidding/budgeting disclosures — Google Ads blog
- Ads Advisor 3 — Google Ads blog April 21, 2026
- TechWyse, "Google Retires Dynamic Search Ads, Moves to AI Max" — [techwyse.com/news/platform-updates/google-dynamic-search-ads-retired-ai-max-migration-2026](https://www.techwyse.com/news/platform-updates/google-dynamic-search-ads-retired-ai-max-migration-2026)
- NateCue, "Google Kills DSA for AI Max" — [natecue.com/en/news/google-ai-max-advertising-automation-2026/](https://www.natecue.com/en/news/google-ai-max-advertising-automation-2026/)
- The Keyword recap of GML 2026 — [thekeyword.co/news/google-marketing-live-2026](https://www.thekeyword.co/news/google-marketing-live-2026)
- PPC Land GML 2026 recap — [ppc.land/google-marketing-live-2026-every-announcement-that-actually-matters/](https://ppc.land/google-marketing-live-2026-every-announcement-that-actually-matters/)
- NRF "Google deepens AI investments that impact retail" — [nrf.com/blog/google-deepens-ai-investments-that-impact-retail](https://nrf.com/blog/google-deepens-ai-investments-that-impact-retail)
- Stan Ventures "The Universal Commerce Protocol (UCP) Technical SEO Playbook" — [stanventures.com/news/the-universal-commerce-protocol-ucp-technical-seo-playbook-7339/](https://www.stanventures.com/news/the-universal-commerce-protocol-ucp-technical-seo-playbook-7339/)
- AdwaitX "Google & Walmart Deploy Universal Commerce Protocol at NRF" — [adwaitx.com/google-universal-commerce-protocol-nrf-2026/](https://www.adwaitx.com/google-universal-commerce-protocol-nrf-2026/)
- JumpFly AI Max analysis (April 2026)
