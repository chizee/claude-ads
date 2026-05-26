# Automation Tier Classifier — Reference

<!-- Created: 2026-05-26 | v1.8.0 -->
**Scope:** how to classify the *degree* of automation an account has handed to each platform's
AI layer, so the audit can recommend the right level of human oversight. New in v1.8.0 because
2026 platforms expose **module-level** automation control (you can no longer treat a campaign
as simply "automated" or "manual").

This file is loaded on-demand by `/ads audit`, `/ads budget`, `/ads meta`, `/ads tiktok`,
`/ads microsoft`, and `/ads google`.

---

## Why a classifier

Through 2025, "automation" was binary per campaign (e.g., Advantage+ Shopping on/off). In 2026
the major platforms expose automation as independently toggleable modules:

- **TikTok Smart+ One Buying Experience** — targeting, budget, and placements can each be on or
  off independently; the Smart+ label appears per module.
- **Meta Advantage+** — Advantage+ Audience, Placements, Creative, and campaign budget are
  separate switches.
- **Google AI Max for Search** — keywordless matching, Final URL Expansion, and text
  customization are separate controls layered onto a Search campaign.
- **Microsoft AI Max for Search** — query expansion with brand/term guardrails as separate
  controls.
- **LinkedIn Accelerate** — full auto-campaign creation vs manual.

An audit that flags "you're not using automation" or "you've fully automated" misreads the
account. The classifier resolves the actual per-module state.

---

## Tiers

| Tier | Name | Definition | Recommended oversight |
|------|------|------------|----------------------|
| T0 | Manual | No platform AI delegation; manual bids, targeting, placements | Standard |
| T1 | Assisted | One module delegated (e.g., Smart Bidding only) with human structure | Light review |
| T2 | Module-mixed | Some modules automated, others manual (e.g., Smart+ budget auto, targeting manual) | Per-module review; verify the *manual* modules are intentional, not neglected |
| T3 | Platform-managed | Most modules delegated (Advantage+ / Smart+ all-on / AI Max full) with humans setting goals + creative + guardrails | Goal + guardrail review; confirm creative volume + clean signals feed the AI |
| T4 | Agentic | An external agent (MCP) plans/launches/optimizes campaigns | **Mandatory** write-action governance (see `mcp-integration.md` C-MCP-1..6); read-only-first, human approval gate, paused-by-default |

---

## Per-platform module map

| Platform | Modules to classify | Notes |
|----------|--------------------|-------|
| Meta | Advantage+ Audience · Placements · Creative · Campaign Budget · MCP connection | ARM/GEM/Lattice reward T3 with broad targeting + 15-20 creative angles |
| Google | Smart Bidding · AI Max keywordless · Final URL Expansion · text customization · PMax | DSA → AI Max forced migration Sept 2026 pushes accounts toward T3 |
| TikTok | Smart+ targeting · budget · placements (each independent) · GMV Max | Recognize module-level granularity, not all-or-nothing |
| Microsoft | AI Max for Search query expansion · automated bidding · Brand Agents | Guardrails (brand/term exclusions) required at T3 |
| LinkedIn | Accelerate auto-campaign · Auto-targeting · Draft with AI | SMB-focused; verify targeting precision not lost |

---

## Audit usage

1. Determine each account's tier per platform from the module states above.
2. At **T2**, verify every manual module is a deliberate choice (a manual module inside an
   otherwise-automated campaign is often neglect, not strategy).
3. At **T3**, the audit's job shifts from "tune the levers" to "feed the AI well":
   creative volume + diversity, broad targeting, clean conversion signals (Pixel + CAPI,
   EMQ ≥ 7), and correct goal/guardrail configuration.
4. At **T4 (agentic)**, escalate to the `audit-regulatory-compliance` MCP governance checks
   (C-MCP-1..6). A T4 account without a human approval gate is a P0 account-loss risk
   (SurfaceLabs precedent, April 2026).

## Cross-references

- `mcp-integration.md` — write-action governance for T4 (agentic) accounts
- `meta-ai-stack.md` — why T3 Meta accounts must feed the four-layer AI stack with creative diversity
- `scoring-system.md` — regulatory-exposure band picks up T4 governance gaps
