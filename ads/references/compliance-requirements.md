# Compliance Requirements — Reference

**Status:** rewritten for v1.8.0 (rebaseline against v1.7.1 May 18, 2026)
**Scope:** the regulatory surface area an advertising audit must cover in 2026 — EU AI Act Article 50, US state privacy laws (22 states), Privacy Sandbox post-shutdown reality, iOS 26 impact, Digital Services Act, HIPAA / LegitScript / Special Ad Categories, and global frameworks (PIPL, LGPD, DPDPA, TCF, GPP).

This file is loaded on-demand by the new `audit-regulatory-compliance` agent (split from the original `audit-compliance` agent in v1.8.0).

---

## The five hard regulatory clocks

These are the dates the audit must surface unprompted to anyone running ads with EU exposure or US consumer-facing traffic:

| Clock | Date | Scope | What happens |
|---|---|---|---|
| Meta Comscore migration | June 22, 2026 | US automotive model ads on Meta | Nielsen DMA discontinued; campaigns still using DMA paused until updated to Comscore Markets® |
| Connecticut neural data | July 1, 2026 | All advertisers reaching CT residents | Neural data added to sensitive data; **no volume threshold** for law applicability |
| EU AI Act Article 50 | August 2, 2026 | Any advertiser using AI-generated creative shown to EU users | Transparency obligations live; penalties up to €15M or 3% global turnover |
| Google AI Max forced migration | September 2026 | All Google Ads accounts running DSA | DSA campaigns auto-upgrade to AI Max; no opt-out |
| EU AI Act watermarking (grandfathered) | December 2, 2026 | Generative AI systems placed on market before Aug 2, 2026 | Watermarking compliance required (subject to May 7, 2026 Omnibus formal adoption) |

---

## 1. EU AI Act — Article 50 transparency obligations

**Primary source:** [artificialintelligenceact.eu/article/50/](https://artificialintelligenceact.eu/article/50/)
**Supporting:** European Commission digital-strategy.ec.europa.eu Code of Practice page; Latham & Watkins client alert (May 2026); Jones Day client alert (January 2026)

### Effective date timeline

| Date | Event |
|---|---|
| August 1, 2024 | AI Act entered into force |
| August 2, 2025 | GPAI model provider obligations effective |
| February 2, 2025 | Prohibited practices and AI literacy obligations effective |
| **August 2, 2026** | **Article 50 transparency obligations effective (BASELINE)** |
| May 7, 2026 | Political agreement on AI Act Omnibus — watermarking compliance extended to December 2, 2026 for pre-existing systems |
| Dec 17, 2025 → June 2026 | Draft → final Code of Practice on Transparency of AI-Generated Content (multi-layered watermarking) |
| **December 2, 2026** | **Watermarking grandfathered deadline for systems placed on market before Aug 2, 2026** (subject to formal Omnibus adoption, expected July 2026) |

### What Article 50 actually requires

**For providers** of generative AI systems (model creators):
- Mark outputs as artificially generated in **machine-readable format** (audio, image, video, text)
- Outputs must be **detectable as artificially generated**
- Multi-layered watermarking (per Code of Practice): metadata + imperceptible + logging/fingerprinting; no single technique is sufficient

**For deployers** (marketing teams, brands, agencies USING AI creative):
- Disclose deepfakes when shown to the public
- Disclose AI-generated text on matters of public interest
- **Heightened standard for deepfakes (Article 50(4))**: must be clearly labeled
- Chatbots must disclose at first interaction that the user is talking to AI

**Penalties:** up to **€15M or 3% of global annual turnover, whichever is higher**.

### Audit-check templates

```yaml
- id: C01
  severity: P0
  applies_when: account targets EU/EEA users AND uses AI-generated creative
  check: |
    Identify all ad creative tagged as AI-generated (Adobe Firefly, DALL-E, Midjourney, Gemini Omni, Veo, Nano Banana, banana-claude, Meta Advantage+ Creative).
    Verify each asset:
    1. Preserves the provider's machine-readable watermark (does not strip metadata)
    2. Is disclosed as AI-generated in the ad copy or on the landing page if the EU-facing audience could reasonably be deceived
    3. Meets the heightened deepfake standard if it depicts a real person or real event
  remediation: |
    1. Enable metadata preservation in your creative pipeline
    2. Add "AI-generated" disclosure to ad copy / landing page for EU traffic
    3. For deepfakes: clearly label as AI-generated and obtain rights for the depicted person
    4. Document the watermarking-preservation policy in your brand's compliance file

- id: C02
  severity: P1
  applies_when: account uses AI chatbot ad surfaces (e.g., LinkedIn Wire chat, Microsoft Brand Agents, Meta WhatsApp Business)
  check: Verify the chatbot discloses at first interaction that the user is interacting with AI
  remediation: Add first-interaction disclosure to chatbot opening message
```

---

## 2. US state privacy laws

### The 22-state map (May 2026)

| State | Effective | Notes |
|---|---|---|
| California (CCPA / CPRA) | 2018 / 2023 | Strictest enforcement; **§7025(c)(6) visible-confirmation effective Jan 1, 2026** |
| Virginia (VCDPA) | Jan 1, 2023 | First post-CCPA |
| Colorado (CPA) | July 1, 2023 | GPC required |
| Connecticut (CTDPA) | July 1, 2023 / amendments July 1, 2026 | Neural data July 1, 2026 |
| Utah (UCPA) | Dec 31, 2023 / amendments July 1, 2026 | |
| Texas (TDPSA) | July 1, 2024 | GPC required; $1B+ settlement against major tech co. |
| Oregon (OCPA) | July 1, 2024 | GPC required |
| Montana (MTCDPA) | Oct 1, 2024 | GPC required |
| Iowa (ICDPA) | Jan 1, 2025 | |
| Delaware (DPDPA) | Jan 1, 2025 | GPC required |
| Nebraska (NDPA) | Jan 1, 2025 | GPC required |
| New Hampshire (NHDPA) | Jan 1, 2025 | GPC required |
| New Jersey (NJDPA) | Jan 15, 2025 | GPC required |
| Tennessee (TIPA) | July 1, 2025 | |
| Minnesota (MCDPA) | July 31, 2025 | GPC required |
| Maryland (MODPA) | Oct 1, 2025 / **enforcement against newly collected data April 2026** | **Strictest data minimization in US; bans selling sensitive data regardless of consent; bans targeting under-18s** |
| Indiana (ICDPA) | Jan 1, 2026 | |
| Kentucky (KCDPA) | Jan 1, 2026 | |
| Rhode Island (RIDTPPA) | Jan 1, 2026 | |
| Arkansas | (amendments July 1, 2026) | |
| Oklahoma | Jan 1, 2027 | Signed March 20, 2026 |
| Alabama | May 1, 2027 | Signed April 17, 2026 |

### Global Privacy Control (GPC) — 12 mandatory states

**Effective January 1, 2026, twelve states require honoring GPC** as a valid Universal Opt-Out Mechanism (UOOM) or Opt-Out Preference Signal (OOPS):

**CA, CO, CT, MT, NE, NH, NJ, MN, MD, DE, OR, TX**

California, Colorado, and Connecticut have **explicitly confirmed** that GPC qualifies. Texas requires it under TDPSA. Most other states accept it as one of multiple valid signal types.

**California Opt Me Out Act** (October 2025): all web browsers operating in California must send GPC by **January 1, 2027**.

### CCPA §7025(c)(6) — visible confirmation (NEW for 2026)

**Effective January 1, 2026:**

> "A business must display whether it has processed the consumer's opt-out preference signal as a valid request to opt-out of sale/sharing on its website."

Background processing alone is no longer sufficient. The visible-confirmation requirement means:

- When a CA visitor's browser sends GPC, the website **must** display a visible indicator (footer message, status notification in privacy center, banner) stating "Your Opt-Out Request Has Been Honored" or equivalent
- The display must be triggered by GPC detection, **before any consent banner**, and **regardless of any previous consent**

### Connecticut neural data — July 1, 2026

**Source:** Connecticut SB 1295, signed June 24, 2025 by Gov. Lamont; effective July 1, 2026

> "Neural data means any information that is generated by measuring the activity of an individual's central nervous system."

This addition triggers law applicability with **no volume threshold** for businesses processing neural data — every advertiser handling such data is in scope regardless of how many CT consumers they reach. Other additions to sensitive data: **transgender or nonbinary status, financial account data, government ID numbers**.

### Maryland MODPA — strictest data minimization

**Source:** Maryland Online Data Privacy Act, effective October 1, 2025; enforcement against newly collected data effective April 2026

The "reasonably necessary" standard is the strictest in the US. Key provisions:

- Data collection limited to "reasonably necessary and proportionate" for the disclosed purpose
- **Bans selling sensitive data regardless of consent**
- **Bans targeting under-18s with advertising**
- Heightened consent for sensitive data processing

### Sensitive data — what counts in 2026

Across the 22 states (with overlapping definitions):

- **Precise geolocation** (within 1,750 feet)
- **Health inferences** (not just health records — also inferences derived from purchase or browsing behavior)
- **Neural data** (Connecticut, July 1, 2026)
- Race, ethnicity, religion, sexual orientation, transgender or nonbinary status
- Genetic data, biometric data
- Children's data
- Financial account data, government ID numbers
- Precise immigration or citizenship status

### "Sharing" redefinition

Most state laws have clarified that **transferring consumer data to ad platforms to improve targeting or build lookalike audiences constitutes "sharing"** even when no money changes hands. This means:

- Building Custom Audiences in Meta from US visitor data = "sharing" requiring opt-out compliance
- Building Customer Match audiences in Google = "sharing"
- Lookalike / similar-audiences seeding = "sharing"

### Enforcement track record

| Case | Amount | Date | Reason |
|---|---|---|---|
| Sephora | $1.2M | Aug 2022 | Earliest CCPA enforcement |
| Healthline Media | $1.55M | July 2025 | Failure to honor GPC + misuse of health data |
| Tractor Supply | $1.35M | Sept 2025 | Largest CPPA fine to date (until Disney) |
| Jam City | $1.4M | Nov 2025 | Children's data |
| **Disney** | **$2.75M** | **Feb 2026** | **Largest CCPA AG settlement to date** — §7025(c)(2) cross-account propagation violation |
| **Ford** | **$375,703** | **March 2026** | **CPPA — remedial obligation: audit every tracking technology** |
| Texas (major tech co.) | $1B+ | 2025–2026 | Texas Data Privacy and Security Act |

**Coordinated enforcement sweeps:** California + Colorado + Connecticut AGs announced a joint investigative sweep on September 9, 2025 targeting GPC compliance. Honda was fined for asymmetric cookie controls (opt-in easier than opt-out). Blue Shield of California investigation triggered after misconfigured analytics tools shared health information affecting 4.7M members.

### California Delete Act — DROP platform

**Effective January 1, 2026:** California's Data Removal Request and Opt-out Platform (DROP) is live. Consumers can submit a single deletion request that propagates to all registered data brokers.

**Compounding fines:** $200 per day per unfulfilled deletion request beginning **January 31, 2026**.

### Audit-check templates

```yaml
- id: C09
  severity: P0
  applies_when: account targets users in any of the 12 GPC states
  check: |
    Inspect the user's tag management system (GTM, Tealium, Adobe Launch, etc.).
    Verify that when a request arrives with the Sec-GPC: 1 header:
    1. Targeted advertising pixels (Meta Pixel, TikTok Pixel, LinkedIn Insight Tag, etc.) are suppressed
    2. The suppression happens BEFORE any consent banner is shown
    3. The suppression overrides any previous consent the user may have given
  remediation: |
    Configure GTM with a GPC-detection variable; bind to all targeted-advertising tag firing rules as a negation condition.

- id: C11
  severity: P0
  applies_when: account targets California users AND honors GPC
  check: |
    Verify the website displays a visible confirmation when GPC is detected.
    Acceptable formats: footer message, status notification in privacy center, banner, badge.
    Text must indicate the opt-out has been honored (e.g., "Your Opt-Out Request Has Been Honored").
  remediation: |
    Add a CCPA §7025(c)(6) confirmation indicator. Display when Sec-GPC: 1 is detected.

- id: C13
  severity: P0
  applies_when: account collects or infers data that could be neural data AND targets CT residents
  check: |
    Identify any data flows that could capture neural data (per CT SB 1295 definition: "any information generated by measuring the activity of an individual's central nervous system").
    This includes: BCI products, neurofeedback devices, EEG-based fitness/wellness apps, sleep-tracking with brainwave inference, mental-health apps using neural inputs.
  remediation: |
    If applicable, obtain explicit opt-in for neural data processing; CT applies the law with no volume threshold.

- id: C16
  severity: P0
  applies_when: account targets MD residents AND processes any consumer data
  check: |
    Verify data minimization compliance:
    1. Data collection is reasonably necessary for the disclosed purpose
    2. Sensitive data is NEVER sold (regardless of consent — MD ban)
    3. Under-18 users are NOT targeted with advertising (MD ban)
  remediation: |
    Audit data flows for unnecessary collection; remove any sensitive-data sales; add age-gating for ad targeting.
```

---

## 3. Privacy Sandbox — October 17, 2025 shutdown

**Primary source:** [privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies) (Anthony Chavez, October 17, 2025)

Google retired the following Privacy Sandbox APIs:

- Attribution Reporting API (Chrome + Android)
- IP Protection
- On-Device Personalization
- Private Aggregation (including Shared Storage)
- Protected Audience (Chrome + Android)
- Protected App Signals
- Related Website Sets
- SelectURL
- SDK Runtime
- Topics (Chrome + Android)

**Remaining features:** CHIPS (Cookies Having Independent Partitioned State), FedCM (Federated Credential Management), Private State Tokens.

**Third-party cookies remain in Chrome** via user-choice model — but reliability is declining as Safari, Firefox, and Brave block by default. UK CMA released Google from Sandbox commitments on the same day; CMA testing cited **85% attribution inaccuracy and 30% publisher revenue decline** during sandbox trials.

### Audit implication

The previous `compliance-requirements.md` recommendations to prepare for Privacy Sandbox are **out of date** and must be replaced with:

- **Server-side conversion APIs are now mandatory** (Meta CAPI, Google Enhanced Conversions, TikTok Events API, Snap CAPI, Pinterest CAPI, LinkedIn CAPI, Reddit CAPI)
- **CHIPS-aware tagging** (low priority — limited use cases)
- **FedCM for sign-in flows** (forward-looking)
- **First-party data infrastructure** is the primary investment area

---

## 4. iOS 26 — Apple's privacy expansion (September 15, 2025)

**Source:** WebProNews; WITHIN.co iOS 26 explainer

iOS 26 affects **ALL iOS attribution pipelines**, not just Apple Ads:

### Advanced Fingerprinting Protection (ATFP)

- **Default ON in ALL Safari browsing** (previously only Private Browsing)
- Per WebProNews early testing: up to 90% reduction in fingerprinting effectiveness
- Affects: device-graph-based attribution, probabilistic match modeling, server-side resolution

### Expanded Link Tracking Protection

- Strips **gclid / fbclid / msclkid** in all Safari browsing (was Private + Mail only)
- Click-attribution to platforms is broken for iOS Safari users without server-side fallback
- Server-side conversion APIs become the only reliable signal pathway

### Audit implications

```yaml
- id: C-iOS-1
  severity: P0
  applies_when: account has iOS Safari traffic share > 5%
  check: |
    Verify server-side conversion API is configured for every major platform with iOS traffic.
    Required: Meta CAPI, Google Enhanced Conversions, TikTok Events API.
    Recommended for share > 10%: Snap CAPI, Pinterest CAPI, LinkedIn CAPI, Reddit CAPI.
  remediation: |
    Use the /ads server-side-tracking sub-skill to audit the existing setup.
    Target EMQ ≥ 7 for Meta CAPI.
    Configure event_id deduplication between Pixel + CAPI.
```

---

## 5. Digital Services Act (DSA) — 2026 enforcement

DSA enforcement is accelerating in 2026:

- **Ad transparency reporting** — VLOPs (Very Large Online Platforms) must publish ad libraries with all served ads
- **Targeting prohibitions** — no targeting of minors based on profiling; no targeting based on sensitive categories (sexual orientation, religion, political views)
- **Recommender system transparency** — users must be able to see why ads are shown
- **Enforcement examples 2026**: French authorities' Grok deepfake investigation (Q1 2026)

### Audit check

```yaml
- id: C22
  severity: P1
  applies_when: account targets EU/EEA users
  check: |
    Verify no targeting of:
    1. Minors based on profiling
    2. Sensitive categories (sexual orientation, religion, political views, race, ethnicity)
    3. Health-status inferences without explicit opt-in
    Verify the platform's ad-transparency library (Meta Ad Library, TikTok Ad Library, etc.) is accessible.
  remediation: |
    Audit Custom Audiences and lookalike seeds for sensitive-category proxies (e.g., interest categories that imply religion).
    Remove minor-targeting from any active campaign.
```

---

## 6. HIPAA, LegitScript, Special Ad Categories

These regimes remain in effect through 2026:

- **HIPAA** — Healthline Media $1.5M fine and Blue Shield California investigation indicate continued health-data enforcement; covered entities must ensure ad pixels do not exfiltrate PHI
- **LegitScript** — required for telehealth, pharmacy, and addiction-treatment ads on Google and Meta
- **Special Ad Categories** (Meta) and equivalent on Google — Housing, Credit, Employment, Social Issues / Politics — restricted targeting (no age, gender, ZIP, detailed interests for housing/credit/employment); requires advertiser identity verification and disclosure

### Audit check

```yaml
- id: C24
  severity: P0
  applies_when: industry template is healthcare OR finance OR real_estate
  check: |
    Verify Special Ad Categories declaration is set correctly:
    - Housing: HOUSING category on Meta; restricted targeting
    - Credit/Finance: CREDIT category on Meta; restricted targeting
    - Employment: EMPLOYMENT category on Meta; restricted targeting
    - Politics: SOCIAL_ISSUES_ELECTIONS_OR_POLITICS; advertiser verification + disclaimer required
    Verify LegitScript certification for telehealth/pharmacy/addiction-treatment ads.
  remediation: |
    Re-declare Special Ad Category on affected campaigns.
    Apply for LegitScript certification if missing.
```

---

## 7. Global frameworks

| Framework | Region | Notes |
|---|---|---|
| **GDPR + ePrivacy** | EU/EEA | Continued primacy; consent for non-essential cookies; legitimate interest tightened |
| **PIPL** | China | Cross-border data transfer rules; security assessment for large transfers |
| **LGPD** | Brazil | ANPD enforcement increasing |
| **DPDPA** | India | Phased rollout continuing; consent management |
| **TCF v2.3** | EU | Continues as primary EU consent signaling framework |
| **GPP (Global Privacy Platform)** | Global | IAB Tech Lab framework; adopted in Agent Registry validation |
| **UK GDPR + PECR** | UK | Maintained post-Brexit |
| **Quebec Law 25** | Quebec | Sept 22, 2024 effective; biometric and minor protections |
| **PIPEDA / CPPA reform** | Canada | Bill C-27 stalled but expected revival |

---

## 8. The audit-regulatory-compliance agent — output format

When the new `audit-regulatory-compliance` agent runs, it outputs a structured JSON block with findings indexed by check ID (C01–C29), severity (P0/P1/P2), evidence, risk, and remediation. The orchestrator aggregates these into the Ads Health Score under the new "regulatory exposure" weighting band (see `scoring-system.md` v1.8.0 update).

Example output structure:

```json
{
  "agent": "audit-regulatory-compliance",
  "findings": [
    {
      "id": "C11",
      "severity": "P0",
      "category": "US state privacy",
      "evidence": "GPC signal detected in test session; no visible confirmation displayed",
      "risk": "CCPA §7025(c)(6) violation; Disney $2.75M precedent for §7025 family",
      "remediation": "Add visible confirmation indicator triggered by Sec-GPC: 1 header",
      "applicable_to_account": true
    }
  ],
  "regulatory_clock_warnings": [
    {
      "clock": "EU AI Act Article 50",
      "date": "2026-08-02",
      "days_until": 68,
      "applicable": true,
      "reason": "Account uses AI-generated creative AND targets EU users"
    }
  ]
}
```

---

## Sources

- Article 50 EU AI Act — [artificialintelligenceact.eu/article/50/](https://artificialintelligenceact.eu/article/50/)
- European Commission Code of Practice on Transparency of AI-Generated Content — digital-strategy.ec.europa.eu
- Latham & Watkins, "AI Act Update: EU Resolves to Change Rules and Extend Deadlines," May 2026 — [lw.com](https://www.lw.com/)
- Jones Day, "European Commission Publishes Draft Code of Practice on AI Labelling and Transparency," January 2026 — [jonesday.com](https://www.jonesday.com/)
- IAPP US state privacy law tracker — [iapp.org](https://iapp.org/)
- Multistate state privacy summaries — [multistate.us](https://www.multistate.us/)
- Greenberg Traurig, "Revised and New CCPA Regulations Set to Take Effect on Jan. 1, 2026" — [gtlaw.com](https://www.gtlaw.com/)
- Nelson Mullins, "Show Me That You've Opted Me Out: New CCPA Rules Require Businesses to Prove Compliance," January 2026 — [nelsonmullins.com](https://www.nelsonmullins.com/)
- Hunton, "Connecticut Amends the Connecticut Data Privacy Act" — [hunton.com](https://www.hunton.com/)
- Consenteo, "Global Privacy Control (GPC) in 2026" — [consenteo.com](https://www.consenteo.com/)
- Privacy Sandbox shutdown — [privacysandbox.google.com](https://privacysandbox.google.com/blog/update-on-plans-for-privacy-sandbox-technologies)
- WebProNews, iOS 26 ATFP analysis — [webpronews.com](https://www.webpronews.com/)
- WITHIN, iOS 26 Link Tracking Protection explainer — [within.co/blog/ios-26/](https://www.within.co/blog/ios-26/)

---

## Cross-references

- **MCP write-action governance** — see `mcp-integration.md`
- **Meta automotive Comscore migration** — see `notes-meta.md`
- **Google AI Max forced migration** — see `notes-google.md`
- **iOS 26 server-side tracking requirements** — see `/ads server-side-tracking` SKILL.md
- **EU AI Act AI-creative deployer obligations** — see `/ads creative` SKILL.md
