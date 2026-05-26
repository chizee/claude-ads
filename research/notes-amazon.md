# Amazon Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads amazon` deltas (sub-skill itself shipped in v1.7.0)
**Baseline:** v1.7.0 `/ads amazon` (Sponsored Products / Brands / Display, ACOS / TACOS, search-term harvesting — already in)
**Compiled:** May 26, 2026

This file captures the Amazon Ads updates that need to be folded into `/ads amazon` in v1.8.0. Check IDs AMZ-new-1 through AMZ-new-17. The v1.7.0 release already covered the core platform; these are the deltas accumulated since `/ads amazon` first shipped, plus the post-cut deltas from unBoxed 2025 / unBoxed Toronto 2026 / public launches.

---

## unBoxed 2025 (Nashville, November 11–12, 2025) — surface

**Primary source:** [advertising.amazon.com/resources/whats-new](https://advertising.amazon.com/resources/whats-new) (unBoxed 2025 pages)

### AMZ-new-1 — Unified Campaign Manager (UCM)

- Sponsored Ads + Amazon DSP in single platform
- Beta announced November 11, 2025; **live early 2026**
- **15 months daily data + 6 years monthly data** — the largest historical depth any major ad platform now exposes

Audit-relevant: for accounts that previously used separate Sponsored / DSP reporting, surface UCM as the canonical reporting layer. The data depth means new YoY checks become feasible (multi-year seasonality, long-tail ASIN performance decay).

### AMZ-new-2 — Ads Agent

Conversational chat assistant for campaign creation, targeting, AMC (Amazon Marketing Cloud) analytics. Available to anyone with AMC access. Audit-relevant: detect adoption + verify it's not running unattended write actions.

### AMZ-new-3 — Creative Agent

Agentic AI ad creation. Expanded November 11, 2025 to support **Streaming TV and Sponsored TV**. Audit-relevant for CTV campaigns: verify creative agent outputs are reviewed before launch (paused-by-default policy — see `mcp-integration.md`).

### AMZ-new-4 — Full-Funnel Campaigns

New AI campaign type **2026** — single campaign that spans Sponsored Products, Sponsored Brands, display, and streaming TV. Audit-relevant: detect adoption; if user runs Full-Funnel, the channel-level breakouts that worked for single-product campaigns no longer apply.

### AMZ-new-5 — Multi-Touch Attribution (MTA)

Deployed across Campaign Manager early 2026. **Materially different from the previous last-click-only model.** Audit framing: verify MTA is the selected attribution model + verify the user understands previous reports are not like-for-like.

### AMZ-new-6 — Sponsored Products Video in search results

Native video format in Sponsored Products. Audit: detect adoption; flag missing video assets in product catalog for video-eligible categories.

### AMZ-new-7 — Reimagined homepage hero + Top-of-search pre-purchase

New high-visibility placements. Pre-purchase = users who haven't bought yet; high-leverage for cold-prospecting campaigns.

---

## Amazon Ads MCP Server — AMZ-new-8

**Source:** Amazon Ads "What's New" — unBoxed 2025

- **Closed beta:** November 13, 2025
- **Public beta:** February 2, 2026
- **Supports:** Claude, ChatGPT, Gemini, Amazon Q, Bedrock

Full integration details in `mcp-integration.md`. Audit-relevant: verify scope is minimum-necessary (one account, not all-account access), verify read-only first.

---

## Sponsored Brands Collections — AMZ-new-9 — January 28, 2026

**Primary source:** [advertising.amazon.com/resources/whats-new/sponsored-brands-collections](https://advertising.amazon.com/resources/whats-new/sponsored-brands-collections)

### Verbatim from Amazon

> "Amazon is launching Sponsored Brands collections, a new ad format that lets advertisers promote multiple related products in a single ad unit through either automatic (AI-powered) or manual product selection… This format also offers a manual option, allowing advertisers to select up to 10 products to feature in a single ad."

### Spec

- **Replaces** existing Product Collections format starting January 28, 2026
- **Minimum 3 ASINs; maximum 10 ASINs**
- **Auto (AI) + Manual modes**
- **Up to 1,000 ASIN exclusions** in Auto mode
- Removes custom headlines, lifestyle images, branded creative (a notable retreat from advertiser creative control)
- **US only**

### Citation correction (important for benchmarks.md)

The **"+143% click-attributed sales"** figure circulating in coverage belongs to **Sponsored Brands Reserve Share of Voice**, NOT Collections. Amazon's official Reserve Share of Voice page reads:

> "Increased Sponsored Brands top-of-search impression share from 62.7% to 99.3%; Increased click-attributed sales by 143%; Reduced lost top-of-search sales from 10.3% to 0.3%"

The **"2.5× more unique products purchased with AI version vs. manual"** figure is in third-party guides (sentrykit.com) citing unspecified beta tests; **not on Amazon's official launch page**. Flag as not-yet-corroborated by primary source in the notes file.

---

## Sponsored Products Prompts & Sponsored Brands Prompts — GA March 25, 2026 — AMZ-new-10

**Primary source:** [advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts](https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts)

### Verbatim

> "We're excited to announce that Sponsored Products prompts and Sponsored Brands prompts are officially moving from open beta to general availability in the U.S. on March 25, 2026."

> "As we move to general availability in the U.S., we will begin to charge for these ads as part of your CPC bidding and billing parameters."

### Spec

- CPC billing began at GA (March 25, 2026)
- Auto-enrolled for Sponsored Products and Sponsored Brands campaigns
- **Dedicated Prompts report** — Amazon official lists: prompt text, impressions, clicks, orders. Practitioner coverage (Autron) extends the field list to CTR / CPC / spend / sales / ACOS / ROAS / 7-day orders & units.
- Report path: Campaign → Ad Group → Ads → Prompts tab

Audit check: detect Prompts adoption; review prompt-level CTR and ACOS; flag prompts spending without conversions for early kill.

---

## Brand+ and Performance+ — AMZ-new-11 through AMZ-new-13

**Source:** [advertising.amazon.com/resources/whats-new/unboxed-2025-brand-plus-and-performance-plus-enhanced](https://advertising.amazon.com/resources/whats-new/unboxed-2025-brand-plus-and-performance-plus-enhanced)

### Brand+ (prospecting AI)

- **+71% PDP views**
- **+42% brand discovery**
- **+64% purchases** vs. non-Brand+ tactics

### Performance+ (conversion AI)

- **+34% ROAS in-store**
- **+68% CPA improvement off-Amazon**

### Combined (H&R Block case)

- **144% full-funnel CVR lift**
- **35% CPA improvement**

All three figures sourced from Amazon's unBoxed 2025 official page. Use in `benchmarks.md` as Amazon-supplied case study data.

---

## CTV / Prime Video — AMZ-new-14 through AMZ-new-17

| ID | Item |
|---|---|
| AMZ-new-14 | **Prime Video ads** live in 16 countries as of November 2025; 2026 expansion: **Belgium, Denmark, Norway, Turkey** |
| AMZ-new-15 | **Direct Netflix and Spotify integrations** via Amazon DSP |
| AMZ-new-16 | **NBA on Prime Video** — started October 2025; expanded packages from May 2026 |
| AMZ-new-17 | **Complete TV** — cross-publisher streaming TV management across Prime Video + premium publishers with linear TV data integration |

### unBoxed Toronto 2026 (February 25, 2026) — additional disclosures

- Creative Agent expanded to Canada
- Brand+ / Performance+ Canadian availability
- NBA on Prime Video packages starting May 2026

---

## Amazon Q3 2025 advertising revenue

**Source:** Amazon Q3 2025 10-Q SEC filing (filed October 30, 2025); CNBC coverage

> "Advertising services continued to perform strongly, generating $17.7 billion in revenue, up 24 percent compared to Q3 2024."

For benchmarks.md scaling: Amazon ads revenue $17.7B (+24% YoY Q3 2025).

---

## Sources

- Amazon Ads "What's New" — [advertising.amazon.com/resources/whats-new](https://advertising.amazon.com/resources/whats-new)
- Sponsored Brands Collections — [advertising.amazon.com/resources/whats-new/sponsored-brands-collections](https://advertising.amazon.com/resources/whats-new/sponsored-brands-collections)
- SP / SB Prompts GA — [advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts](https://advertising.amazon.com/resources/whats-new/unboxed-2025-sponsored-products-and-sponsored-brands-prompts)
- Brand+ / Performance+ — [advertising.amazon.com/resources/whats-new/unboxed-2025-brand-plus-and-performance-plus-enhanced](https://advertising.amazon.com/resources/whats-new/unboxed-2025-brand-plus-and-performance-plus-enhanced)
- PPC Land, "Amazon's product collections bet: 3-10 ASINs and AI will replace headlines" — [ppc.land/amazons-product-collections-bet-3-10-asins-and-ai-will-replace-headlines/](https://ppc.land/amazons-product-collections-bet-3-10-asins-and-ai-will-replace-headlines/)
- CedCommerce Sponsored Brands Collections overhaul — [cedcommerce.com/blog/amazon-overhauls-sponsored-brands-product-collections-3-asin-minimum-no-custom-creatives-from-jan-28/](https://cedcommerce.com/blog/amazon-overhauls-sponsored-brands-product-collections-3-asin-minimum-no-custom-creatives-from-jan-28/)
- My Amazon Guy Collections explainer — [myamazonguy.com/news/amazon-sponsored-brands-product-collections/](https://myamazonguy.com/news/amazon-sponsored-brands-product-collections/)
- Mansour Norouzi LinkedIn post on Collections Auto vs Manual — [linkedin.com/posts/mansournorouzi_remember-that-sponsored-brands-collections-activity-7437130431625375744-LNJv](https://www.linkedin.com/posts/mansournorouzi_remember-that-sponsored-brands-collections-activity-7437130431625375744-LNJv)
- SentryKit Amazon Headline Search Ads 2026 guide — [sentrykit.com/blog/amazon-headline-search-ads/](https://sentrykit.com/blog/amazon-headline-search-ads/)
- Amazon Q3 2025 10-Q SEC filing (filed October 30, 2025)
