# TikTok Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads tiktok` addendum
**Baseline:** v1.7.0 `/ads tiktok` (existing — 28 checks per `tests/fixtures/check-catalog.yaml`)
**Compiled:** May 26, 2026

This file documents TikTok Ads updates that need to be folded into `/ads tiktok` in v1.8.0. Check IDs T29–T46. Timing note: TikTok World 2026 (May 13–15) finished 2 days BEFORE v1.7.0 cut on May 17, so most of these announcements are not yet in the skill.

---

## TikTok World 2026 — May 13–15, 2026

**Primary source:** [newsroom.tiktok.com](https://newsroom.tiktok.com/) TikTok World 2026 announcements; PPC Land, Adweek, AdExchanger coverage

### T29 — TikTok Ads MCP Server (official)

Last of the four majors to ship MCP (after Google Oct 2025, Amazon Nov 2025, Meta April 2026). Third-party AI agents — Claude, ChatGPT — can now plan, launch, and optimize campaigns autonomously. Audit-checks live in `mcp-integration.md`.

### T30 — TikTok Ads Skills

Developer building blocks: campaign creation, performance insights, creative analysis, audience discovery, budget optimization. Bundle pattern similar to Anthropic skills — encapsulated capability that agents can compose.

### T31 — Smart+ One Buying Experience (module-level)

This is the most important Smart+ change for audit logic. **Smart+ automation is now module-level**, not all-or-nothing. The four modules — targeting, bidding/budget, placements, creative — can each be turned on or off independently. The Smart+ label appears on each module in the UI.

**Audit implication:** `/ads tiktok` needs to recognize module-level granularity. A campaign with "Smart+ targeting ON but Smart+ creative OFF" is a different audit case from a fully-Smart+ or fully-manual campaign.

### T32 — Smart+ Music Autofix

Automatic music licensing — replaces unlicensed sounds in user creative with licensed equivalents. Audit: detect adoption; flag if user is uploading custom audio without disabling Music Autofix (overrides may not be intended).

### T33 — Smart+ creative reporting + multi-URL + higher asset group limit

- Creative-level reporting now inside Smart+ (was a major gap pre-2026)
- Multi-URL support per ad group (was single-URL)
- Higher asset group limit (specific number TBD in TikTok's spec)

### T34 — Smart+ for app install / app-event optimization

New objectives for Smart+ — mobile-app advertisers can now go fully Smart+. Audit-relevant for `/ads mobile-app` industry template.

### T35 — TopReach + Creative Sequencing

TopView + TopFeed unified buy with narrative sequencing. Audit-check: detect TopReach campaigns; verify creative sequence is intentional, not a random rotation.

### T36 — Branded Buzz

Large-scale creator collaboration format. Higher production / longer engagement than typical Spark Ads. Audit-relevant for brand-awareness campaigns at scale.

### T37 — Search Hubs

Brand-owned sponsored pages prioritized at top of TikTok search results. Audit-check: detect Search Hubs presence + verify search-intent coverage for the brand's category.

### T38 — Symphony AI updates

- **Dreamina Seedance 2.0** (ByteDance video generation) integrated into Symphony
- **Reference to Video** — prompt-driven moment-specific generation
- Symphony already in v1.7.0 `/ads tiktok`; this is a feature refresh.

### T39 — TikTok GO

Full holiday booking inside TikTok. Partners: Booking.com, Expedia, Viator, GetYourGuide, Tiqets, Trip.com. Audit-relevant for travel-vertical accounts.

### T40 — Mini Series & Mini Games

Long-form serialized content (Mini Series) and gamified ad formats (Mini Games). **Growth Max for Mini Games** is the campaign type for game publishers.

### T41 — Collage Carousel (US Q2 2026)

Hero image + 3 product visuals in a single ad unit. Replaces the older Single Product format for many use cases. **US only at launch.**

### T42 — One Asset Manager

Unified asset management across formats — one place to upload, version, and organize creative. Reduces the asset-management overhead Smart+ would otherwise spread across multiple campaign types.

### T43 — View+ for Pulse Core Max

Premium-reach upgrade for high-CPM brands. Pulse Core Max is the premium-inventory product (contextual brand-safe placements next to top creators).

### T44 — TikTok Market Scope

Competitive intelligence tool — share-of-voice, competitor creative library, category trend tracking.

### T45 — TikTok Real + UK Ad-Free Subscription

- **TikTok Real** — counterfeit / IP protection program for brand owners
- **UK Ad-Free Subscription £3.99/month** — opts users out of advertising data use. Audit implication: UK reach forecasts need to reflect a subscriber opt-out segment.

### T46 — GMV Max expansion

Shop-tab AI optimization (Smart+ for Shop). Expanded to more markets in 2026 — verify the user's market is now in scope.

---

## TikTok USDS divestiture — closed January 22, 2026

**Primary sources:**
- Variety, "TikTok U.S. Joint Venture Deal Set to Close in January With Investors Including Oracle, Silver Lake, Abu Dhabi's MGX" — [variety.com/2025/digital/news/tiktok-us-joint-venture-deal-close-date-oracle-silver-lake-1236612315/](https://variety.com/2025/digital/news/tiktok-us-joint-venture-deal-close-date-oracle-silver-lake-1236612315/)
- Data Center Dynamics, "TikTok US spin-off finalized, led by Oracle, Silver Lake, and MGX" — [datacenterdynamics.com/en/news/tiktok-us-spin-off-finalized-led-by-oracle-silver-lake-and-mgx/](https://www.datacenterdynamics.com/en/news/tiktok-us-spin-off-finalized-led-by-oracle-silver-lake-and-mgx/)

### Structure

| Stakeholder | % |
|---|---|
| Oracle | 15% |
| Silver Lake | 15% |
| MGX (Abu Dhabi) | 15% |
| ByteDance | 19.9% |
| Other US investors | ~30.1% |
| **Non-Chinese ownership** | **80.1%** |

### Operational

- Oracle is "trusted security partner" hosting US data in Oracle US cloud
- Algorithm retrained on US data only
- CEO: Adam Presser
- CSO: Will Farrell

### CEO statement (Shou Zi Chew memo, via Variety)

> "ByteDance and TikTok have signed binding agreements with three managing investors, Oracle Corporation, Silver Lake, and MGX, to form [the joint venture]…"

### Impact on advertisers

**No measurable disruption to advertiser operations.** The audit should note this for any user worried about TikTok exit risk — divestiture closed cleanly, ad APIs and ad accounts continue unchanged.

---

## Revenue benchmarks for benchmarks.md

| Year | Figure | Source |
|---|---|---|
| 2024 | ~$23.6B global ad revenue | Business of Apps |
| 2025 | **~$33.1B** global ad revenue | Business of Apps, January 2026 |
| 2026 | **~$34.8B** (eMarketer projection) | eMarketer December 2025–January 2026 |

**Higher figures circulating in secondary compilations ($43.5B+ from MediaMister, SQ Magazine) are not confirmed by a primary source — flag as practitioner speculation.**

---

## Sources

- TikTok World 2026 newsroom — [newsroom.tiktok.com](https://newsroom.tiktok.com/)
- Variety, TikTok USDS deal — [variety.com/2025/digital/news/tiktok-us-joint-venture-deal-close-date-oracle-silver-lake-1236612315/](https://variety.com/2025/digital/news/tiktok-us-joint-venture-deal-close-date-oracle-silver-lake-1236612315/)
- Data Center Dynamics, TikTok US spin-off — [datacenterdynamics.com/en/news/tiktok-us-spin-off-finalized-led-by-oracle-silver-lake-and-mgx/](https://www.datacenterdynamics.com/en/news/tiktok-us-spin-off-finalized-led-by-oracle-silver-lake-and-mgx/)
- Hypebeast, "TikTok U.S. Joint Venture to Close in January" — [hypebeast.com/2025/12/tiktok-us-joint-venture-to-close-in-january-2026-oracle-silver-lake-mgx-news](https://hypebeast.com/2025/12/tiktok-us-joint-venture-to-close-in-january-2026-oracle-silver-lake-mgx-news)
- AutoFaceless, "TikTok Statistics 2026" — [autofaceless.ai/blog/tiktok-statistics-2026](https://autofaceless.ai/blog/tiktok-statistics-2026)
- Growth Navigate, "TikTok Statistics 2026" — [growthnavigate.com/tiktok-statistics](https://www.growthnavigate.com/tiktok-statistics)
- Business of Apps, TikTok revenue and usage statistics, January 2026
