# Apple Ads — Research Notes (May 2026)

**For:** v1.8.0 `/ads apple` addendum
**Baseline:** v1.7.0 `/ads apple` (existing — 35 checks per v1.2.0 launch; AdAttributionKit + GA4 + Consent Mode V2 + MMP health now in `/ads attribution`)
**Compiled:** May 26, 2026

This file documents Apple Ads updates that need to be folded into `/ads apple` in v1.8.0. Check IDs A36–A42. iOS 26 cross-platform implications appear in `compliance-requirements.md` as well.

---

## A36 — Multiple Search Ad Placements — March 3, 2026

**Primary sources:** 9to5Mac (January 22, 2026); Apple Ads documentation (December 18, 2025)

### Rollout

- **March 3, 2026:** UK and Japan first
- **End of March 2026:** global rollout to all 91 Apple Ads markets
- **Up to 2 ads per single search query**
- **Existing campaigns auto-enrolled** — no opt-out, no separate setup
- **iOS 26.2 / iPadOS 26.2+ required** — older OS continues to show single placement
- **65% of App Store downloads happen after a search** (Apple-supplied; high-leverage placement)
- CPT / CPI pricing model unchanged
- Relevance-first auction (Apple's existing auction logic, applied to both positions)

### The reporting gap

**No position-level reporting initially in AdAttributionKit.** Audits cannot measure position 1 vs. position 2 performance, only aggregate.

```yaml
- id: A36
  severity: P1
  applies_when: account uses Apple Search Ads in iOS 26.2+ markets
  check: |
    Verify campaigns are running in markets where multi-placement is live.
    Note that all reporting from March 3, 2026 onward includes both position 1 and 2 impressions blended.
    Any TAP (Today/Search/Product Pages) placement-coverage report must caveat this.
  remediation: |
    Document the caveat in client-facing reporting:
    "Apple Search Ads now shows up to 2 ads per query in supported markets;
    position-level breakdown is not available in AdAttributionKit."
```

---

## A37 — App Store registered with AdAttributionKit (April 10, 2025)

The App Store itself is now registered with AdAttributionKit. This is a precondition for postback / view-through attribution from App Store ad surfaces. Audit check: verify the user's app has AdAttributionKit framework included in the App Store metadata.

---

## A38 — AdAttributionKit feature surface (WWDC 2025 / iOS 18.4+)

**Source:** [developer.apple.com/videos/play/wwdc2025/221/](https://developer.apple.com/videos/play/wwdc2025/221/); DEV Community WWDC 2025 AdAttributionKit explainer; Dataseat Mobile DSP analysis

### Features in production

| Feature | What it does |
|---|---|
| Configurable attribution windows | Per ad network / interaction type / global |
| Configurable cooldowns | Prevent attribution cannibalization between install and re-engagement |
| Country codes in postbacks | Subject to crowd anonymity threshold |
| Overlapping re-engagement conversion windows | Via Conversion Tags |
| Development Postbacks | Settings test tool for QA |
| View-through attribution | April 2025 GA |
| Custom-click ads | Programmatic-friendly format |
| Re-engagement attribution | Existing-user campaign measurement |

### Audit-check refresh

The v1.7.0 `/ads attribution` sub-skill already covers AdAttributionKit. v1.8.0 should refresh the check thresholds and add postback-decoding examples for the country-code field.

---

## A39 — Custom Product Pages (CPP) replacing Creative Sets

- **Up to 35 Custom Product Pages per app**
- Each CPP can be targeted with a distinct creative combination
- Replaces the older Creative Sets format (deprecated)

**Audit check:** verify CPP usage is within the 35-per-app limit; flag accounts using fewer than 5 CPPs for product-page testing (indicates underutilization of the format).

---

## A40 — iOS 26 Advanced Fingerprinting Protection (ATFP) — September 15, 2025

**Source:** WebProNews early-test reporting

### What changed

- **Default ON in ALL Safari browsing** (was Private Browsing only)
- Up to **~90% reduction in fingerprinting effectiveness** per early WebProNews testing

### Cross-platform impact

This affects **all iOS attribution pipelines**, not just Apple Ads:

- Device-graph-based attribution
- Probabilistic match modeling
- Server-side identity resolution

**Server-side conversion APIs become the only reliable signal pathway for iOS Safari conversion measurement.**

---

## A41 — iOS 26 expanded Link Tracking Protection — September 15, 2025

**Source:** WITHIN.co iOS 26 Link Tracking Protection explainer

### What changed

- Strips **gclid / fbclid / msclkid** in **all Safari browsing** (was Private + Mail only)
- Affects every iOS Safari user, not just the privacy-conscious minority

### Audit implication

For accounts with > 5% iOS Safari traffic share, server-side conversion APIs are mandatory:

```yaml
- id: A41
  severity: P0
  applies_when: iOS Safari traffic share > 5%
  check: |
    Verify Meta CAPI configured (event_id dedup, EMQ ≥ 7).
    Verify Google Enhanced Conversions ≥ 50% coverage.
    Verify TikTok Events API configured.
    For share > 10%: also verify Snap CAPI, Pinterest CAPI, LinkedIn CAPI, Reddit CAPI.
  remediation: |
    Use the /ads server-side-tracking sub-skill to audit and remediate.
```

(Already covered in `/ads server-side-tracking` from v1.7.0; this is the cross-reference from `/ads apple`.)

---

## A42 — WWDC 2026 watch list (June 2026)

WWDC 2026 keynote is in June 2026. Likely Apple Ads / AdAttributionKit announcements to monitor:

- **Further AdAttributionKit window / cooldown granularity**
- **Possible SKAN sunset roadmap** (SKAdNetwork has been on the path to deprecation since AdAttributionKit GA)
- **iOS 27** announcement
- **Possible Apple News ad expansion**
- **Apple Intelligence Ads** — speculative; Apple has been quiet on AI-generated ad creative

**Schedule a v1.8.x addendum within 14 days of the keynote** to incorporate any of the above.

---

## Sources

- 9to5Mac, Apple Search Ads multi-placement coverage (January 22, 2026)
- Apple Ads documentation (December 18, 2025)
- WWDC 2025 Session 221 — AdAttributionKit — [developer.apple.com/videos/play/wwdc2025/221/](https://developer.apple.com/videos/play/wwdc2025/221/)
- DEV Community, "WWDC 2025 — AdAttributionKit iOS 18.4" — [dev.to/arshtechpro/wwdc-2025-adattributionkit-ios-184-essential-features-for-modern-app-attribution-2h5c](https://dev.to/arshtechpro/wwdc-2025-adattributionkit-ios-184-essential-features-for-modern-app-attribution-2h5c)
- Dataseat Mobile DSP, "What Apple's WWDC25 Updates Mean for iOS Growth Marketers" — [dataseat.com/blog/wwdc25-adkit-updates](https://dataseat.com/blog/wwdc25-adkit-updates)
- SplitMetrics, "Apple SKAdNetwork 2025: What It Is and How It Works" — [splitmetrics.com/blog/apple-skadnetwork-guide/](https://splitmetrics.com/blog/apple-skadnetwork-guide/)
- WebProNews, "Apple Enhances Safari Privacy with Default Fingerprinting Protection in iOS 26" — [webpronews.com/apple-enhances-safari-privacy-with-default-fingerprinting-protection-in-ios-26/](https://www.webpronews.com/apple-enhances-safari-privacy-with-default-fingerprinting-protection-in-ios-26/)
- WITHIN, "iOS 26 Link Tracking Protection Explained" — [within.co/blog/ios-26/](https://www.within.co/blog/ios-26/)
