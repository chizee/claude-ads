# Release Requirements

These gates are cumulative. A release candidate is demoted when a load-bearing
source expires, a critical security or privacy finding opens, a declared
capability loses its test evidence, or required remote CI does not pass.

## Product and contract gates

- Buyer, promise, commands, outputs, boundaries, privacy defaults, and mutation
  authority are documented consistently.
- Public schemas have semantic versions and fixtures. Breaking changes require
  a major schema version and migration notes.
- Capability status matches implementation, adapter, fixture, and test evidence.
- Every complete-audit claim reports module completeness and evidence coverage.
- Health, evidence confidence, regulatory exposure, and opportunities remain
  separate outputs.

## Evidence gates

- Every load-bearing platform, API, policy, regulation, benchmark, or creative
  specification claim has a claim ID and at least one dated source ID.
- Official, regulator, standards-body, or primary sources are preferred.
- Practitioner evidence is labeled and cannot alone establish mandatory policy
  or compliance behavior.
- API, policy, feature, and creative-specification sources refresh within 30
  days; regulation receives event-driven review plus a 30-day check near an
  effective date; benchmarks refresh quarterly; foundational methods refresh
  within 12 months.
- Overdue load-bearing sources block release until refreshed or the dependent
  claim and capability are demoted.

## Safety and privacy gates

- Writes are disabled by default and capability-gated by platform.
- Mutation lifecycle tests cover preview, approval, apply, repeated apply,
  verify, failure, audit, and rollback.
- URL, redirect, DNS, browser-subresource, output-path, symlink, archive, and
  parser-differential defenses pass adversarial tests.
- Untrusted content cannot change instructions or mutation authority.
- Secrets and personal data are absent from tracked files, fixtures, reports,
  logs, task packets, archives, and Git history.
- Data classification, redaction, retention, encryption, and deletion behavior
  are documented and tested.

## Evaluation gates

- Schema, scoring, normalization, missing-data, deduplication, routing, and
  report-rendering suites pass.
- Every target platform has sanitized export fixtures and failure cases.
- Routing and safety regressions pass at 100 percent.
- Model evaluations reach at least 90 percent overall with no P0 safety failure
  and no unintended regression against retained v1 behavior.
- A fresh-context verifier confirms completion claims from artifacts and test
  output, not from the implementation conversation.

## Installation and packaging gates

- Install, upgrade, and uninstall are tested on Linux, macOS, and Windows for
  every advertised runtime.
- Installation does not silently mutate global Python or execute unverified
  network content.
- Uninstall removes only ownership-manifest entries and leaves no unowned files.
- A clean checkout reproducibly builds the release archive, release manifest,
  SHA-256 checksums, SBOM, and license notices.
- Archive paths are portable and contain no invalid, absolute, or traversal
  names.

## Merge and release gate

- Required GitHub Actions checks pass on the integration commit. Local success
  does not substitute for unavailable, skipped, or billing-blocked remote CI.
- The integration branch receives independent code, evidence, security,
  privacy, and licensing review.
- No critical blocker remains in the ecosystem disposition ledger.
- Only after all gates pass may the reviewed branch merge and receive a v2 tag.
- Repository visibility remains private; public release requires the separate
  gate in `PUBLISHING_POLICY.md`.
