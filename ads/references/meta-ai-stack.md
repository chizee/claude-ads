# Meta AI Stack — Reference

**Status:** new for v1.8.0 (post-v1.7.0 `/ads meta` Andromeda+GEM+Lattice rewrite; consolidates with Q1 2026 metrics + adds ARM)
**Scope:** the four-layer AI ad system Meta now runs in production, what each layer does, the Q1 2026 performance metrics, and the audit-check implications for `/ads meta`.

This file is loaded on-demand by `/ads meta` and the `audit-meta` agent.

---

## TL;DR

Meta now operates a four-layer AI ad system:

1. **Andromeda** — retrieval (narrows millions of ads → ~1,000–1,500 candidates per impression)
2. **GEM (Generative Ads Recommendation Model)** — central LLM-style intelligence; trains across all surfaces; transfers knowledge to downstream models via teacher-student distillation
3. **Lattice** — unified ad ranking architecture; replaced ~100 siloed models
4. **ARM (Adaptive Ranking Model)** — newest layer; removes truncation ceiling for high-value users with long interaction histories

All four together drove Meta to Q4 2025 ads revenue of $50.1B (+26% YoY); Advantage+ and adjacent AI tools hit a $60B annualized run-rate by Q3 2025 earnings call (October 29, 2025). Q1 2026 advertising tools doubled in advertiser adoption per Meta's Q1 2026 earnings.

**The single most important audit implication:** creative diversity is no longer a count-based check (≥10 ads). It is a quality-and-sequence-based check (15–20 distinct creative angles, broad-targeting friendly, cross-surface portable, sequence-aware).

---

## Layer 1 — Andromeda (retrieval)

**Source:** [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/); Meta Engineering AI Innovation blog; Foxwell Digital and Triple Whale recap (April 2026)

### What it does

Andromeda is the **first stage** of Meta's ad serving pipeline. Before any ranking decision, Andromeda has to narrow a pool of tens of millions of eligible ads down to a few thousand candidates worth ranking. It is the retrieval engine.

### How it's built

- **Hardware:** Meta Training and Inference Accelerator (MTIA) + NVIDIA Grace Hopper Superchip
- **Model complexity:** 10,000× increase in retrieval model complexity vs. the prior system
- **Compute (Jan 2026):** Andromeda compute capacity **tripled** per Meta's January 2026 disclosure
- **Rollout:** Initial Reels + Feed (2024); full global rollout completed January 9, 2026 (with reported CPM volatility during transition)

### What it reads

- Image pixels, video frames, audio
- Ad copy, landing page, product feed signals
- Behavioral signals from the user (organic + ad engagement history)
- Surface context (Feed, Reels, Stories, etc.)

### What it does NOT do

- Andromeda does **not** generate ad creative. "Andromeda" sometimes gets confused with "creative generation" — it's a retrieval engine, not a creative engine. (Advantage+ Creative is the creative engine.)
- Andromeda does **not** make the final auction decision — that's Lattice + ARM.

### Audit implication

If the account is providing fewer than ~15 genuinely distinct creative angles, Andromeda has less material to retrieve against and the same ads collapse onto the same audiences (the "creative-similarity suppression" pattern that `/ads meta` Entity-ID predictor already detects). **The fix is creative volume + diversity, not bid changes.**

---

## Layer 2 — GEM (Generative Ads Recommendation Model)

**Source:** [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/); Meta Engineering paper published November 10, 2025; Triple Whale, "It's Not Andromeda" (April 2026)

### What it does

GEM is the **central intelligence layer**. It trains across all of Meta's surfaces (Feed, Stories, Reels, Messenger, WhatsApp), all objectives (conversions, reach, engagement, awareness), and on both ad content and organic engagement. Then it distills that learning into smaller production models via knowledge distillation.

**Critical clarification:** "Generative" in GEM does NOT mean it generates ad creative. It means the model GENERATES predictions about the next-best-ad to show a user given their sequence history. GEM produces decision signals, not creative.

### How it's built

- **Architecture:** Teacher-student knowledge distillation. GEM is the teacher; downstream Lattice / Andromeda / vertical models are the students.
- **Training compute (Q4 2025):** GPU cluster size **doubled** in Q4 2025
- **Q1 2026:** "**4× more efficient** at driving ad performance gains" than prior ranking models, per Meta

### Performance milestones

| Period | Surface | Result |
|---|---|---|
| Q3 2025 launch | Meta Reels | +5% conversions |
| Q4 2025 | Facebook | +3.5% ad clicks (sequence-learning architecture) |
| Q1 2026 | Tested accounts | **+13% CTR, +16% CVR** |

### What it does

- Reads ad content + organic engagement signals across all surfaces
- Predicts the next-best-ad in a user's sequence (not just "is this ad relevant" but "is this the right next ad given everything they've seen")
- Transfers learning to downstream models so they don't each have to learn from scratch

### Audit implication

GEM rewards advertisers who provide enough creative diversity for sequence learning to operate. **If you only run one or two creatives, GEM can only place you at one moment in a user's journey.** More distinct angles → more placement moments. The audit check is creative-volume + creative-distinctness, not just count.

---

## Layer 3 — Lattice (ranking architecture)

**Source:** Meta Lattice official Business news post [facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance); about.fb.com January 2026 post

### What it does

Lattice **replaced about 100 siloed models** (each optimized for a single objective or surface) with one unified ranking architecture. The breakthrough: learnings from one surface inform another. Reels performance influences Feed ranking. Click optimization informs conversion optimization. Everything teaches everything.

### Key innovation — Sequence Learning

Lattice doesn't just evaluate single impressions. It evaluates sequences. A user who's seen 3 brand-awareness creatives and is now ready for a conversion creative is treated differently from a cold prospect. This sequence-aware ranking is what unlocked the Q1 2026 conversion lifts.

### Performance milestones

| Period | Metric | Result |
|---|---|---|
| Initial deployment | Ad quality | +12% |
| Initial deployment | Conversions | +6% |
| Q3 2025 earnings | App ads conversions | ~+3% |
| Q1 2026 | Landing-page-view ad CVR | **+6%** |
| Q1 2026 | Infrastructure capacity savings | 20% |

### Audit implication

Cross-surface creative coverage matters. An account running ads on Feed only is leaving cross-surface learning on the table. The audit should check (a) cross-surface placement coverage, (b) creative variants tuned to each surface format (square + vertical + horizontal), and (c) at least one creative per major objective (awareness + conversion).

---

## Layer 4 — ARM (Adaptive Ranking Model) — NEWEST

**Source:** Meta Performance Marketing Summit (San Jose, 2026); Meta Q1 2026 earnings disclosures; Foxwell Digital Meta Marketing Summit 2026 recap

### What it does

ARM is the newest layer in Meta's AI stack. It addresses a specific weakness: previous ranking systems had a **truncation ceiling for users with very long interaction histories**. A user who'd seen hundreds of ads over months had their sequence truncated; ranking decisions for that user were based on a shortened history that lost the high-value signal.

ARM dynamically adjusts ranking strategy based on the depth of a user's interaction history, **removing the truncation ceiling** for high-value users.

### Performance milestones

| Test phase | Metric | Result |
|---|---|---|
| Q1 2026 early testing | CVR | **+3%** |
| Q1 2026 early testing | CTR | **+5%** |

### Audit implication

For accounts with substantial returning-customer audiences (e.g., subscription businesses, repeat-purchase ecommerce), ARM eligibility is genuinely important. The audit should check:

- Is the account using **broad targeting** so ARM has a depth-of-history signal to work with?
- Is the account running campaigns long enough (≥30 days) to build the sequence history ARM operates on?
- Are returning-customer audiences segmented appropriately so ARM can target them differently from cold prospects?

---

## The complete pipeline — putting it together

```
User opens Reels / Feed / Stories
         ↓
[ANDROMEDA] retrieval — narrow 10M+ eligible ads → ~1,000 candidates
         ↓
[GEM] sequence-aware predictions — what's the next-best ad for this user given their history?
         ↓
[LATTICE] unified ranking — cross-surface, cross-objective learning applied
         ↓
[ARM] adaptive ranking — for users with deep history, removes truncation ceiling
         ↓
Auction → impression
         ↓
Outcome signal feeds back to all four models for retraining
```

The key insight for advertisers: every layer **rewards creative diversity, broad targeting, and clean conversion signals.** None of the layers reward old-school tactics like interest stacking, narrow audiences, or single-creative campaigns.

---

## Incremental Attribution Q4 2025 model

**Source:** [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/) — January 2026

Verbatim from Meta:

> "Our incremental attribution feature is gaining real momentum — our latest Q4 model rollout drove a 24% increase in incremental conversions compared to our standard attribution model, and the product reached a multi-billion-dollar annual run-rate just seven months after launch."

The audit should flag accounts not using incremental attribution as a reporting view — they are over-counting conversions and likely over-spending on last-click-heavy tactics.

---

## Operational best practices (for the audit-meta agent and benchmarks.md)

These are the four principles `/ads meta` should optimize toward in 2026, all sourced from Meta's official guidance and the Performance Marketing Summit:

### 1. Creative volume + diversity

- **Target: 15–20 distinct creative angles** in active rotation (not just count of ads — Entity-ID clustering check)
- Per Advantage+ Shopping best practice: 50–150 creative assets per campaign
- Cross-format variants (square, vertical, horizontal) for cross-surface portability
- Distinct angles: UGC, high-production "hype," carousel of benefits, static bold-hook, founder-talking-head, problem/solution narrative

### 2. Simplified structure

- **1–3 core campaigns**, not 10+
- Advantage+ Shopping as primary for ecommerce
- CBO (Campaign Budget Optimization) over ad-set budgets
- Single broad audience per campaign

### 3. Broad targeting

- Move away from interest stacks
- Trust Andromeda + GEM to handle audience matching from creative + behavioral signals
- Exclude only true negatives (existing customers for prospecting, recent converters for cold)

### 4. Clean signal infrastructure

- **Pixel + CAPI together** (not one or the other) — server-side handles the iOS Safari Link Tracking Protection gap
- **Event Match Quality (EMQ) ≥ 7** for purchase events (CAPI Gateway recommended for high-value events)
- Event deduplication via `event_id`
- 7-day learning window minimum, ≥50–75 conversions before structural changes

---

## What this means for the existing `/ads meta` rewrite

The v1.7.0 `/ads meta` rewrite (May 17, 2026) already covers:

- Andromeda awareness
- GEM + Lattice concepts (at v1.7.0 release-note level)
- Entity-ID clustering detection
- Creative-similarity suppression awareness

The v1.8.0 additions in this file are:

- **ARM layer documentation** (was missing — this is the newest layer)
- **Q1 2026 performance metric refresh** (GEM +13% CTR / +16% CVR; Lattice +6% landing-page-view ad CVR; Andromeda compute tripled; ARM +3% CVR / +5% CTR)
- **Sequence-learning audit checks** (creative diversity for GEM's sequence-aware ranking)
- **Cross-surface portability audit checks** (Lattice rewards cross-surface learning)
- **ARM eligibility detection** (broad audiences + long campaign history)
- **Incremental Attribution Q4 2025 model adoption check** (+24% incremental conversions)

---

## Sources

- Meta official "AI Innovation in Meta's Ads Ranking Driving Advertiser Performance" — [facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance](https://www.facebook.com/business/news/ai-innovation-in-metas-ads-ranking-driving-advertiser-performance)
- Meta "2026 — AI Drives Performance" — [about.fb.com/news/2026/01/2026-ai-drives-performance/](https://about.fb.com/news/2026/01/2026-ai-drives-performance/)
- Meta Engineering GEM technical paper — November 10, 2025
- Meta Performance Marketing Summit (San Jose, 2026) recap — Foxwell Digital
- Meta Q1 2026 earnings call (PPC Land coverage) — [ppc.land/meta-q1-2026-56-3b-revenue-as-ai-tools-double-advertiser-adoption/](https://ppc.land/meta-q1-2026-56-3b-revenue-as-ai-tools-double-advertiser-adoption/)
- Triple Whale "It's Not Andromeda: Inside Meta's AI Ad Stack" (April 2026) — [triplewhale.com/blog/meta-ads-ai-system](https://www.triplewhale.com/blog/meta-ads-ai-system)
- ALM Corp "Meta's AI-Driven Advertising Infrastructure" — [almcorp.com/blog/meta-andromeda-gem-ai-advertising-system-guide/](https://almcorp.com/blog/meta-andromeda-gem-ai-advertising-system-guide/)
- WASK "Meta's New AI Ad Infrastructure: GEM, Lattice & Andromeda" — [blog.wask.co/digital-marketing/meta-ai-ad-infrastructure-gem-lattice-andromeda/](https://blog.wask.co/digital-marketing/meta-ai-ad-infrastructure-gem-lattice-andromeda/)
- Logical Position "The 2026 Paid Social Playbook" — [logicalposition.com/blog/the-2026-paid-social-playbook](https://www.logicalposition.com/blog/the-2026-paid-social-playbook)
- GrowthMarketer "Meta Campaign Structure for Scaling in 2026" — [growthmarketer.com/blog/meta-campaign-structure-2026/](https://growthmarketer.com/blog/meta-campaign-structure-2026/)
- DOJO AI "Meta Andromeda Explained" — [dojoai.com/blog/meta-andromeda-explained-performance-marketers-2026](https://www.dojoai.com/blog/meta-andromeda-explained-performance-marketers-2026)
