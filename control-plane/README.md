# Claude Ads Control Plane

This directory is the public-safe contract layer for Claude Ads v2. It records
what the product is allowed to claim, what it can actually do, which evidence
supports it, how work is coordinated, and what must pass before release.

The design is a clean-room synthesis of source-first research discipline,
capability honesty, progressive disclosure, reversible operations, and
fresh-context verification. It contains no copied private prompts, captured
system text, account exports, credentials, or raw private corpus.

## Contracts

- `PRODUCT_BOUNDARIES.md`: buyer, promise, supported workflows, and explicit
  non-promises.
- `PUBLISHING_POLICY.md`: private/public classification and publication gate.
- `RELEASE_REQUIREMENTS.md`: maturity, testing, security, packaging, and remote
  CI requirements.
- `schemas/`: JSON Schema Draft 2020-12 contracts.
- `manifests/`: current product, evidence, capability, safety, orchestration,
  maturity, and ecosystem-review state.

## Doctrine

1. No source, no current claim.
2. No implementation, fixture, and test, no capability claim.
3. No approval and rollback, no account mutation.
4. No independent verification path, no release.
5. Staleness, security failures, or broken evaluations demote maturity.

Manifests are release inputs, not marketing copy. A planned capability must be
marked `declared` or `disabled`; only verified behavior may be marked
`fixture-verified` or `live-verified`.
