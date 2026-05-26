# LinkedIn Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads linkedin` addendum
**Baseline:** v1.7.0 `/ads linkedin` (existing — 27 checks per `tests/fixtures/check-catalog.yaml`)
**Compiled:** May 26, 2026

This file documents LinkedIn Ads updates that need to be folded into `/ads linkedin` in v1.8.0. Check IDs L28–L46.

---

## L28 — Off-Platform Event Ads — full rollout May 6, 2026

**Primary source:** [linkedin.com/help/lms/answer/a10264811](https://www.linkedin.com/help/lms/answer/a10264811); Danielle Webb LinkedIn Marketing Solutions blog (April 28, 2026); Converve "How to Promote Events on LinkedIn: The 2026 B2B Guide"

### What shipped

- **Event-format ad WITHOUT requiring a LinkedIn Event Page**
- Supports webinars, field events, hybrid
- Lead Gen Objective syncs directly to Salesforce / HubSpot / Marketo
- Event clipping for post-event nurture

### First-party integrations

- **Cvent** (LinkedIn Audience Connector)
- **ON24**
- **Integrate**

### Audit implication

For B2B / SaaS / enterprise accounts running webinar funnels, this is a primary growth lever. The audit should detect adoption + verify the off-platform event has corresponding Lead Gen Form configuration + verify CRM sync is working (Salesforce / HubSpot / Marketo).

B2B-enterprise + SaaS industry templates need an Off-Platform Event Ads check.

---

## L29 — Campaign Manager terminology rename trap

**Source:** LinkedIn Campaign Manager 2025–2026 rolling release notes

### The rename

| Old (still in API) | New (UI only) |
|---|---|
| Campaign Group | Campaign |
| Campaign | Ad set |
| Ad | Ad (unchanged) |

### The trap

**The API kept the old terminology** (`adCampaignGroups`, `campaignGroup`, `campaign` are unchanged in the LinkedIn Marketing API). Per LinkedIn documentation:

> "the parameter value will change while the parameter key remains the same as the previous naming"

This is a UTM tag mapping risk for cross-platform attribution. If a marketer builds UTMs with `utm_campaign={Campaign.Name}` from the UI and another marketer wires up the API which still calls that level `campaignGroup`, the UTMs will be inconsistent.

### Audit check

```yaml
- id: L29
  severity: P1
  applies_when: account has LinkedIn campaigns + cross-platform UTM strategy
  check: |
    Verify UTM tag templates reference the API-level terminology (campaignGroup, campaign)
    rather than UI labels (Campaign, Ad set).
    Inspect at least 3 active campaigns for tag consistency.
  remediation: |
    Standardize UTMs on API terminology.
    Document the UI/API mismatch in the team's UTM playbook.
```

---

## L30–L44 — Other 2026 LinkedIn features

Reference grid (full sourcing in `RESEARCH-NOTES-MAY-2026.md`):

| ID | Feature | Status |
|---|---|---|
| L30 | Accelerate auto-campaign creation | Live |
| L31 | AI Ad Variants from single input | Live |
| L32 | Career Journey targeting — recent promotions, new job placements | Live |
| L33 | Reserved Ads — premium guaranteed inventory | Live |
| L34 | First Impression Ads — premium first-position | Live |
| L35 | BrandLink expansion | Live |
| L36 | Wire — short-form B2B video | Live |
| L37 | Thought Leader Event Ads — sponsor user posts for events | Live |
| L38 | CTV expansion | Live |
| L39 | Company Attribution in Revenue Attribution Report | Live |
| L40 | MRC accreditation for video metrics | Pursuing |
| L41 | Company Intelligence API | May 2026 |
| L42 | Flexible Ad Creation | Arriving 2026 |
| L43 | Auto-targeting + Draft with AI | SMB April 2026 |
| L44 | Real-time CRM data in Campaign Manager | Live |

---

## L45 — Ads Agency Certification (May 6, 2026)

**Source:** LinkedIn Marketing Solutions blog (May 6, 2026); Converve 2026 B2B guide

LinkedIn launched a global Ads Agency Certification credential on May 6, 2026.

**Requirements:**
- Business Manager
- Invoicing
- Marketing Academy completions

**Audit implication:** for agency-template accounts, surface whether the agency holds the credential — this is increasingly a prerequisite for managing larger LinkedIn budgets and for unlocking premium account-management support.

---

## L46 — Depth Score algorithm 2026

LinkedIn's organic algorithm shifted in 2026 toward a **Depth Score**:

- Time-on-content is weighted heavily
- Engagement pods (mutual-like rings) are detected and penalized
- AI-written posts are detected and filtered
- External links reduce organic reach **30–50%**

**Audit implication for paid:** if a user's organic LinkedIn presence is being throttled by Depth Score, paid amplification has a higher per-conversion cost (lower organic-paid synergy). The audit should flag accounts that combine organic+paid where the organic side shows Depth Score risk signals.

---

## Benchmarks for benchmarks.md

**Source:** Dreamdata LinkedIn Ads Benchmarks Report 2026

- **121% ROAS** average
- **272-day average B2B customer journey**
- LinkedIn ad costs **$5–15 CPC** vs. other platforms $1–3 CPC

Use the journey length (272 days) to right-size the audit's attribution-window recommendation — LinkedIn's 90-day click attribution window is the minimum for B2B accounts; 180-day for ABM.

---

## Sources

- LinkedIn Marketing Solutions, Off-Platform Event Ads — [linkedin.com/help/lms/answer/a10264811](https://www.linkedin.com/help/lms/answer/a10264811)
- LinkedIn Marketing Solutions blog, Danielle Webb (April 28, 2026)
- Converve, "How to Promote Events on LinkedIn: The 2026 B2B Guide" — [converve.com/event-networking-blog/how-to-promote-events-on-linkedin-2026-guide/](https://www.converve.com/event-networking-blog/how-to-promote-events-on-linkedin-2026-guide/)
- LinkedIn Campaign Manager Help Center, terminology rename
- Dreamdata LinkedIn Ads Benchmarks Report 2026
- LinkedIn Marketing Solutions blog, Ads Agency Certification (May 6, 2026)
