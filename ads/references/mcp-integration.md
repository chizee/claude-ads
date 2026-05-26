# MCP Integration — Reference

**Status:** rewritten for v1.8.0 (rebaseline against v1.7.1 May 18, 2026)
**Scope:** documents every official Model Context Protocol (MCP) server now exposed by major ad platforms, the relevant third-party and aggregator connectors, the write-action governance policy claude-ads enforces, and the SurfaceLabs cautionary tale.

This file replaces the prior `mcp-integration.md`. It is loaded on-demand by the `/ads` orchestrator and by the `/ads server-side-tracking` and `/ads attribution` sub-skills.

---

## Why this matters now

Between October 2025 and May 2026, every major ad platform shipped an official MCP server:

| Platform | Status | Date | Endpoint / source |
|---|---|---|---|
| Google Ads | Open-sourced | October 7, 2025 | <https://github.com/googleads/google-ads-mcp> |
| Amazon Ads | Closed beta → public beta | Nov 13, 2025 → Feb 2, 2026 | [advertising.amazon.com/resources/whats-new](https://advertising.amazon.com/resources/whats-new) |
| Meta Ads | Open beta global | April 29, 2026 | `mcp.facebook.com/ads` per [facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors) |
| Microsoft Advertising | Activate 2026 | April 22, 2026 (Brand Agents); May 19, 2026 (Activate) | [about.ads.microsoft.com](https://about.ads.microsoft.com/) |
| TikTok Ads | Announced at TikTok World | May 13–15, 2026 | [newsroom.tiktok.com](https://newsroom.tiktok.com/) |

In parallel, the IAB Tech Lab named its umbrella framework **AAMP (Agentic Advertising Management Protocols)** on February 26, 2026 and launched the **Agent Registry** in early March 2026 (10 active MCP entries by March 11, 2026: Amazon Ads MCP, Burt Intelligence (EU + US), HyperMindZ Campaign Orchestrator, Mixpeek, Optable, IAB Tech Lab Agent Registry MCP, Dstillery, PubMatic, Equativ). Source: [iabtechlab.com/introducing-the-iab-tech-lab-agent-registry/](https://iabtechlab.com/introducing-the-iab-tech-lab-agent-registry/).

This means: a 2026 audit must verify (a) which platform MCPs are connected to the user's account, (b) which scopes those connections hold, (c) whether the user has a write-action governance policy in place, and (d) whether the third-party MCP servers in use are validated against GPP + TCF ID via the IAB Agent Registry.

---

## Platform MCP servers — by platform

### Google Ads MCP

**Repository:** <https://github.com/googleads/google-ads-mcp>
**Status:** Open-sourced October 7, 2025; first-party Google project; widely adopted via direct setup or aggregators

**Capabilities (typical):**
- Read access to campaigns, ad groups, ads, keywords, audiences, conversions, GAQL queries
- Asset management
- Reporting and analytics queries via GAQL
- Limited write actions depending on installed version

**Audit checks the orchestrator should perform:**
- Detect whether the user has Google Ads MCP installed (look for the `google-ads-mcp` server configuration in the Claude Code MCP settings)
- Verify the MCP is using OAuth, not refresh tokens shared by the user
- Verify the MCP is scoped to the minimum-necessary Google Ads accounts (not "all accounts")

### Amazon Ads MCP Server

**Source:** Amazon Ads "What's New" — unBoxed 2025 (Nov 11–13, 2025); public beta February 2, 2026
**Status:** Public beta February 2, 2026; supports Claude, ChatGPT, Gemini, Amazon Q, Bedrock

**Capabilities:**
- Sponsored Products / Sponsored Brands / Sponsored Display campaign management
- DSP via Unified Campaign Manager (15 months daily + 6 years monthly data)
- Brand+ / Performance+ AI campaign management
- Creative Agent for ad creation
- AMC (Amazon Marketing Cloud) analytics through Ads Agent

**Audit checks:**
- Verify the MCP is scoped to the correct Amazon Ads account
- Verify the user understands that Creative Agent expansion to Streaming TV / Sponsored TV (announced Nov 11, 2025) is also write-capable

### Meta Ads MCP — Meta Ads AI Connectors (Official)

**Source:** [facebook.com/business/news/meta-ads-ai-connectors](https://www.facebook.com/business/news/meta-ads-ai-connectors); Search Engine Land coverage (Anu Adegbola)
**Endpoint:** `mcp.facebook.com/ads`
**Status:** Open beta global, launched **April 29, 2026**

**Capabilities — 29 tools across 5 categories:**

1. **Campaign management** — create / read / update / pause / activate campaigns, ad sets, ads
2. **Product catalog** — feed audits, catalog operations
3. **Accounts and assets** — Business Manager / ad account / asset inspection
4. **Datasets and tracking** — Pixel + CAPI health, EMQ scoring, event volume statistics
5. **Insights and benchmarks** — performance trends, anomaly detection, industry benchmarks

**Authentication:** Meta Business OAuth — **no Developer App, no App Review required**. Rate limit ~200 calls/hour per ad account. Supports Claude, ChatGPT, Perplexity (added May 2026), Codex, Claude Code.

**Default safety:** all MCP-created campaigns launch in **PAUSED** state. Nothing goes live without manual review in Ads Manager.

**Audit checks:**
- Detect Meta Ads MCP connection
- Verify it is using `ads_read` scope as the default; flag `ads_management` (write) scope as requiring explicit governance review
- Verify paused-by-default is honored — any campaign created via MCP should pass through human review before activation
- Verify the ad account has not been subject to fraud-detection patterns (rapid API call rate, frequent budget adjustments) that triggered the SurfaceLabs ban

### Microsoft Advertising — Brand Agents + AI Max

**Source:** [about.ads.microsoft.com](https://about.ads.microsoft.com/) (April 22, 2026); Activate 2026 (May 19, 2026)
**Status:** Brand Agents live April 22, 2026; AI Max for Search pilot May 2026

**Capabilities:**
- Brand Agents embed on Shopify / WooCommerce (commerce surface)
- Audience Generation (plain-language → targeting, US + Canada closed pilot)
- Performance Max transparency (Final URL reporting, April 2026)
- Clarity AI Visibility (how brands appear in AI interfaces)
- AI Max for Search expands query matching across Copilot Search / Answers / Bing with brand inclusions/exclusions, term exclusions, messaging constraints

**Audit checks:**
- Detect Brand Agents adoption
- Verify Audience Generation pilot eligibility for US/Canada accounts
- Verify Performance Max transparency reporting is being read (April 2026 Final URL reporting)

### TikTok Ads MCP Server

**Source:** [newsroom.tiktok.com](https://newsroom.tiktok.com/) TikTok World 2026 (May 13, 2026); Adweek + AdExchanger coverage
**Status:** Announced May 13, 2026 at TikTok World; last of the four majors to ship MCP

**Capabilities:**
- Campaign creation, launch, optimization via natural language
- TikTok Ads Skills — developer building blocks for campaign creation, performance insights, creative analysis, audience discovery, budget optimization
- Smart+ module-level automation control via MCP

**Audit checks:**
- Detect TikTok Ads MCP connection
- Verify Smart+ module-level granularity is being respected (targeting / budget / placements can be on or off independently)

---

## Aggregator and third-party connectors

The official platform MCPs are not the only ones in production. Aggregators provide cross-platform agentic ad management:

- **Adspirer** — Amazon (Sponsored Products / Brands / Display), Walmart Connect (coming), Meta, Google
- **Pipeboard** — multi-platform reporting and campaign control
- **AdAmigo.ai** — Meta Ads management with read/write distinction
- **GrowthSpree** — LinkedIn Ads
- **Adzviser** — LinkedIn + Microsoft

**Validation:** the IAB Tech Lab Agent Registry validates third-party MCP / A2A entries against GPP & TCF ID. Audits should prefer Agent-Registry-validated connectors over unvalidated ones.

---

## Write-action governance policy

**This is the most important section of this file.** Every claude-ads audit that detects an MCP connection MUST evaluate the user's write-action governance against this policy.

### Required defaults

1. **Start with read-only scope.** First MCP connection should use the read-only scope variant (`ads_read` for Meta, `read-only` for Google, etc.). Reporting and analysis flows do not need write access.
2. **Human approval gate for writes.** Write actions (`ads_management` for Meta, write-enabled OAuth for Google, etc.) should not be granted until the user has implemented a manual approval gate (e.g., a Slack-bot review step, a human-in-the-loop confirmation in the AI assistant flow, or a dedicated review queue).
3. **Paused-by-default for created campaigns.** Honor the Meta Ads MCP default: any campaign created via MCP launches in PAUSED state. Activate only after manual review.
4. **Rate-limit compliance.** Stay well below the Meta ~200 calls/hour limit. Aggressive rapid API calls are a fraud-detection trigger.
5. **No autonomous budget loops.** Budget changes above a configurable threshold (default: 25% of ad-set lifetime spend or $500/day, whichever is lower) require explicit human approval.
6. **Audit-log retention ≥ 90 days.** Every MCP-initiated action should be logged with timestamp, action type, before/after state, requesting agent, and user identity.

### The SurfaceLabs cautionary tale (April 2026)

**Source:** SurfaceLabs (Cody Schneider) public post-mortem, April 2026; AdAmigo.ai blog coverage

A developer running Claude Code in an autonomous campaign-management loop **lost his Meta Ads account permanently after one week**, including years of accumulated Pixel data and Custom Audiences. The trigger pattern Meta's fraud-detection flagged:

- Rapid sequential API calls
- Frequent budget adjustments (multiple per hour)
- No human-in-the-loop confirmation on changes
- Use of an unofficial Meta connector (not the now-official April 29, 2026 release)

**There was no appeal.** The account ban was permanent.

**The lesson encoded in claude-ads:** full automation for ad spend is not worth the account risk. Semi-automation (AI drafts, human approves) gets you 80% of the efficiency with 0% of the ban risk.

### Audit-finding template

When the `/ads` audit detects MCP write access without these governance defaults, surface the finding using this template:

```
SEVERITY: P0 (potential account-loss risk)
CATEGORY: MCP governance
FINDING: <platform> MCP write access detected without human approval gate.
EVIDENCE: <e.g., ads_management scope on Meta Ads connection without documented approval workflow>
RISK: Account ban precedent (SurfaceLabs, April 2026) on aggressive autonomous API behavior.
REMEDIATION:
  1. Downgrade scope to read-only until governance is in place
  2. Implement human approval gate (Slack bot, review queue, or interactive confirmation)
  3. Configure rate-limiting to stay below 200 calls/hour per ad account
  4. Set budget-change approval threshold (default 25% or $500/day)
  5. Enable audit-log retention with ≥90 day retention
```

---

## The four-major comparison table

For sales / community / README use:

| Platform | MCP launch | Tools | Scopes | Default safety | Notes |
|---|---|---|---|---|---|
| Google Ads | Oct 7, 2025 | varies by build | OAuth, read + write | depends on integration | first-party open-source |
| Amazon Ads | Nov 13, 2025 closed → Feb 2, 2026 public | full suite | OAuth | DSP + Sponsored Ads unified | supports Claude/ChatGPT/Gemini/Q/Bedrock |
| Meta Ads | April 29, 2026 | **29 across 5 categories** | `ads_read`, `ads_management` | **paused-by-default**, ~200 calls/hour | first official; SurfaceLabs precedent |
| TikTok Ads | May 13, 2026 | TBD (announced) | TBD | TBD | last of the four majors to ship |
| Microsoft (Brand Agents) | April 22, 2026 | commerce + Audience Generation | OAuth | depends on integration | Copilot Search / Answers / Bing |

---

## IAB Tech Lab AAMP framework

**Source:** [iabtechlab.com](https://iabtechlab.com/) — February 26, 2026 announcement by CEO Anthony Katsur

AAMP (Agentic Advertising Management Protocols) is the umbrella framework. Three pillars:

1. **Execution layer** — what the agent does (campaign creation, optimization, reporting). Built on existing IAB standards: OpenRTB, AdCOM, OpenDirect, VAST.
2. **Protocols layer** — how agents communicate. MCP for tool-use, A2A for agent-to-agent.
3. **Agent Registry** — discoverability and validation. Launched March 1, 2026; 10 active MCP entries by March 11, 2026. Each entry validated against GPP & TCF ID.

**Audit relevance:** prefer Agent-Registry-validated MCPs over unvalidated ones; flag any unvalidated third-party MCP server in the user's stack.

---

## What's coming (watch list)

- **Anthropic / OpenAI agent runtimes** — possible successor protocols to MCP; monitor for v1.8.x successor-protocol section
- **More IAB Agent Registry entries** — count is increasing; re-verify at every ship
- **A2A (Agent-to-Agent) protocol adoption** — currently 0 entries in IAB Registry; first adopters will define convention
- **WWDC 2026 (June 2026)** — possible Apple MCP-equivalent for Apple Ads
- **Reddit Ads MCP** — not yet announced as of May 26, 2026; Reddit has shipped Dual Attribution beta (May 20, 2026) but no MCP yet
- **Snap Ads MCP** — not yet announced
- **Pinterest Ads MCP** — not yet announced (Pinterest is in the post-tvScientific-acquisition integration phase)

---

## Cross-references

- **Write-action governance audit checks:** see the `audit-regulatory-compliance` agent, checks C-MCP-1 through C-MCP-6
- **Per-platform MCP details:** see platform-specific SKILL.md files (`ads-google`, `ads-meta`, `ads-tiktok`, `ads-microsoft`, `ads-amazon`)
- **Regulatory implications of agentic ad management:** see `compliance-requirements.md` — particularly the EU AI Act Article 50 obligations for AI-generated outputs (deployer obligations apply when an agent generates ad creative)
