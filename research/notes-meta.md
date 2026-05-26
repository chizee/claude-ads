# Meta Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads meta` addendum
**Baseline:** v1.7.0 `/ads meta` Andromeda + GEM + Lattice era rewrite (May 17, 2026) + v1.7.1 factual citation polish (May 18, 2026)
**Compiled:** May 26, 2026

This file documents the Meta Ads updates that need to be folded into `/ads meta` in v1.8.0. Check IDs M51–M72. See also: `meta-ai-stack.md` (full Andromeda + GEM + Lattice + ARM reference) and `mcp-integration.md` (Meta MCP write-action governance).

---

## 1. Meta Ads AI Connectors — Official MCP (April 29, 2026) — M51–M53

**Primary source:** [facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors); Search Engine Land coverage (Anu Adegbola); PPC Land "Meta opens its ad system to Claude and ChatGPT with new AI connectors"

### What shipped

- **Endpoint:** `mcp.facebook.com/ads`
- **Companion CLI** for terminal-based agentic workflows
- **29 tools across 5 categories:**
  1. Campaign management (create/read/update/pause/activate campaigns, ad sets, ads)
  2. Product catalog (feed audits, catalog operations)
  3. Accounts and assets (Business Manager / ad account / asset inspection)
  4. Datasets and tracking (Pixel + CAPI health, EMQ, event volume)
  5. Insights and benchmarks (performance trends, anomaly detection, industry benchmarks)
- **OAuth:** Meta Business OAuth — no Developer App, no App Review required
- **Rate limit:** ~200 calls/hour per ad account
- **Clients supported:** Claude, ChatGPT, Perplexity (added May 2026), Codex, Claude Code
- **Default safety:** all MCP-created campaigns launch in PAUSED state

### Audit checks

- **M51** Detect Meta Ads MCP connection
- **M52** Verify paused-by-default safety is honored
- **M53** **CRITICAL: enforce write-action governance** — see SurfaceLabs cautionary tale below; full policy in `mcp-integration.md`

### SurfaceLabs cautionary tale (April 2026)

Cody Schneider's SurfaceLabs lost its Meta Ads account permanently after one week of running autonomous campaigns via an unofficial connector. Trigger pattern Meta's fraud-detection flagged: rapid sequential API calls + frequent budget adjustments + no human-in-the-loop. No appeal. **The lesson encoded in `/ads meta`: semi-automation (AI drafts, human approves) > full autonomy.**

---

## 2. March 3, 2026 attribution rebuild — M54–M59

**Primary source:** [facebook.com/business/news/click-attribution](https://www.facebook.com/business/news/click-attribution) (March 3, 2026); Search Engine Land coverage

### Verbatim from Meta

> "We are shifting conversions that came from a share, save, or other non-link click actions to be included in engaged-view attribution… we are also renaming engaged-view attribution, and going forward, it will be known as engage-through attribution."

> "46% of online purchase conversions with Reels now happen within the first 2 seconds of attention on our video ads… we have updated the definition for an engaged view for a video ad from 10 seconds to 5 seconds."

> "We also are starting to partner with third party analytics providers, such as Northbeam and Triple Whale, to incorporate both clicks and views into their attribution model."

### What changed

- **M54** Click-through now ONLY counts link clicks (websites, apps, lead forms, destinations). Likes, shares, saves, comments, video views, expansions are **no longer click-through**.
- **M55** **Engage-through attribution** is the new column name (was "engaged-view attribution"). Covers all non-link interactions.
- **M56** Engaged-view threshold dropped **10s → 5s**.
- **M57** Default attribution window: 7-day click, 1-day engage-through, 1-day view.
- **M58** **YoY data not comparable** to pre-March-3-2026 baselines. Audit must flag this in any YoY reporting view.
- **M59** Northbeam + Triple Whale view-through integration available.

### Audit framing — "YoY not comparable"

This framing is a **practitioner consensus** (Lucid Media, Marketing Code, Leaf Signal, Media Performance UK) rather than a direct Meta quote — Meta has stated there is no legacy reporting view to compare old vs. new attribution. The position is correct; cite it as analyst interpretation, not Meta's own language.

---

## 3. Meta AI stack Q1 2026 refresh + ARM addition — M60–M64

See `meta-ai-stack.md` for the full reference. Audit-check additions:

- **M60 GEM Q1 2026:** +13% CTR / +16% CVR on tested accounts; "4× more efficient" per Meta
- **M61 Lattice Q1 2026:** +6% landing-page-view ad CVR (new); 20% infrastructure capacity savings; +~3% app-ads conversions (Q3 2025 earnings)
- **M62 Andromeda compute tripled** per Meta January 2026 disclosure
- **M63 ARM (Adaptive Ranking Model)** — newest layer; +3% CVR / +5% CTR early testing; removes truncation ceiling for high-value users with long interaction histories. Eligibility: broad audiences + ≥30-day campaign history.
- **M64 Incremental Attribution Q4 2025 model:** +24% incremental conversions vs. standard attribution per Meta

The v1.7.0 `/ads meta` rewrite already covers Andromeda + GEM + Lattice at concept level + Entity-ID clustering detection + creative-similarity suppression. v1.8.0 adds the ARM layer and the Q1 2026 metric refresh.

---

## 4. May 2026 spotted updates — M65–M69

- **M65** Ad-level placement control (was ad-set level only)
- **M66** AI-generated Instant Forms from URL/prompt
- **M67** **730-day purchase audience retention** (up from 180) with auto-expansion. **Governance flag:** detect, surface to user, recommend explicit review. Privacy concern: longer retention with auto-expansion means audiences expand into older purchasers without explicit operator consent.
- **M68** **New Pixel "auto-include detailed page/product info" setting** — often default ON. Sends product/page metadata (titles, prices, categories) to Meta. **Governance flag:** detect setting state, recommend explicit governance review, especially for healthcare / finance / regulated industries.
- **M69** Advantage+ Creative Image Generation Categories now include: "Refined product look," "Popular in your niche," "High ROAS" — accept/decline based on creative QA needs.

---

## 5. Comscore Markets cutoff — M70 — June 22, 2026 P0

**Primary source:** Meta for Developers blog (Patrick Opoosun, March 13, 2026)

### Verbatim

> "Beginning on June 22, 2026, we will discontinue the use of Nielsen's Designated Market Area (DMA) for automotive model ads. Comscore Markets®, which we introduced in August 2025, will serve as the replacement solution. After this date, campaigns still using Nielsen's DMA for automotive model ads targeting will be paused and require an update to Comscore Markets® to resume delivery."

### Field migration

| Before | After |
|---|---|
| `dma_code` | `comscore_market_codes` |

### Audit gate

For accounts running automotive model ads (Special Ad Category: automotive or product feed includes auto vehicles), this is a hard gate:

```yaml
- id: M70
  severity: P0
  applies_when: account runs automotive model ads with DMA targeting
  check: |
    Inspect campaign targeting payload.
    Detect any active or scheduled campaign using `dma_code`.
    Flag urgency based on days_until_cutoff.
  remediation: |
    Replace `dma_code` with `comscore_market_codes` mapping before June 22, 2026.
    Comscore Markets was introduced in August 2025 — accounts already have access.
    Test in a paused campaign first before bulk migration.
```

**Automotive industry template (v1.8.0) must add this as a P0 check.**

---

## 6. Other Meta May 2026 — M71, M72

- **M71** Digital Services Tax pass-through fees up to 5% in Austria, France, Italy, Spain, Turkey, UK starting mid-2026. Update bid-modeling and ROAS-target benchmarks for EU/UK accounts.
- **M72** CAPI one-click setup launched April 2026. Audit check: verify enabled + Event Match Quality (EMQ) ≥ 7 for purchase events. CAPI Gateway recommended for high-value purchase events.

---

## Sources

- Meta Ads AI Connectors official launch — [facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors)
- Admove, "Meta's MCP and CLI: What Advertisers Need to Know in 2026" — [admove.ai/blog/metas-mcp-and-cli-for-advertisers](https://www.admove.ai/blog/metas-mcp-and-cli-for-advertisers)
- PPC Land, "Meta opens its ad system to Claude and ChatGPT with new AI connectors" — [ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/](https://ppc.land/meta-opens-its-ad-system-to-claude-and-chatgpt-with-new-ai-connectors/)
- Meta "Simplifying Ad Measurement for a Social-First World" (March 3, 2026) — [facebook.com/business/news/click-attribution](https://www.facebook.com/business/news/click-attribution)
- Search Engine Land, "Meta introduces click and engage-through attribution updates" — [searchengineland.com/meta-introduces-click-and-engage-through-attribution-updates-470629](https://searchengineland.com/meta-introduces-click-and-engage-through-attribution-updates-470629)
- Media Performance, "Meta Engage-Through Attribution Explained" — [mediaperformance.co.uk/meta-engage-through-attribution/](https://www.mediaperformance.co.uk/meta-engage-through-attribution/)
- Leaf Signal, "What Meta's March 2026 attribution update means for your reporting & performance" — [leafsignal.com/blog/meta-march-2026-attribution-update](https://www.leafsignal.com/blog/meta-march-2026-attribution-update)
- Meta "2026 — AI Drives Performance" — [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/)
- Social Media Today, "Meta switches to Comscore Markets data for auto ads" — [socialmediatoday.com/news/meta-switches-to-comscore-markets-data-for-auto-ads/814886/](https://www.socialmediatoday.com/news/meta-switches-to-comscore-markets-data-for-auto-ads/814886/)
- Foxwell Digital, "Meta Marketing Summit 2026: Key Takeaways for Advertisers" — [foxwelldigital.com/blog/meta-marketing-summit-2026-what-you-need-to-know](https://www.foxwelldigital.com/blog/meta-marketing-summit-2026-what-you-need-to-know)
- Triple Whale, "It's Not Andromeda: Inside Meta's AI Ad Stack" — [triplewhale.com/blog/meta-ads-ai-system](https://www.triplewhale.com/blog/meta-ads-ai-system)
- SurfaceLabs (Cody Schneider) public post-mortem, April 2026
