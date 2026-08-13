---
type: reference
created: 2026-08-11
updated: 2026-08-13
---

# Architectural Decision Records (ADR) Memory

## ADR 1: Secret Isolation & Security Rules
- **Decision**: Never store API tokens, secrets, or keys in ANY Git branch of a public repository.
- **Implementation**: Secrets live locally in `.env` (excluded by `.gitignore`) or in GitHub Actions Encrypted Secrets (`${{ secrets.* }}`). Pre-commit hook blocks secret pushes.

## ADR 2: Git Conflict Memory (`rerere`)
- **Decision**: Enable `git rerere` locally (`git config --local rerere.enabled true`).
- **Implementation**: Recurring merge conflicts are remembered and auto-resolved by Git.

## ADR 3: Machine Audit Notes (`git notes`)
- **Decision**: Use `git notes --ref=ai-audit` to attach structured JSON metadata (agent session ID, test results) directly to commit hashes without changing commit SHAs.

## ADR 4: 2026 Linter & Formatter Selection
- **Decision**: Biome for JS/TS, Ruff for Python.
- **Rationale**: 10-25x faster Rust-based toolchains replacing legacy ESLint + Prettier + Black setups.

## ADR 5: DevContainer & Cloud Environment
- **Decision**: Provide `.devcontainer/devcontainer.json`, `Dockerfile`, and `docker-compose.yml` for 1-click cloud development in VS Code / GitHub Codespaces.

## ADR 6: Strict Zero-Crash TypeScript Compiler Flags (TS 5.7+)
- **Decision**: Enforce `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`, `"noImplicitReturns": true`, `"noUnusedLocals": true`, and `"noUnusedParameters": true` in `tsconfig.json`.
- **Implementation**: Enforced during build and typechecking via `make typecheck`. Prevents runtime undefined access and unused variable pollution.

## ADR 7: OpenTelemetry v1.34 Structured Tracing & Context Propagation
- **Decision**: Implement OpenTelemetry W3C TraceContext standard propagation and structured JSON log correlation module (`src/infrastructure/telemetry/tracer.ts`).
- **Implementation**: Generates W3C header format (`00-<trace_id>-<span_id>-01`), parses incoming contexts, and attaches trace/span correlation metadata to logs across application boundaries.

## ADR 8: CycloneDX 1.6 Supply-Chain Security & SBOM
- **Decision**: Mandate automated CycloneDX 1.6 Software Bill of Materials (SBOM) generation via `make sbom` outputting `sbom.cdx.json`.
- **Implementation**: Executed as part of `make check` pre-flight audit to maintain 100% supply chain transparency and NIST SP 800-218 compliance.

## ADR 9: Monorepo Architecture & `@project4/*` Package Backbone
- **Decision**: Scaffold modular directory structure under `packages/` (`packages/types`, `packages/config`, `packages/utils`) mapped via TypeScript path aliases (`@project4/types`, `@project4/config`, `@project4/utils`).
- **Implementation**: Promotes reusability across microservices/apps, isolating core interfaces, runtime configurations, and functional utilities.

## ADR 10: Cryptographic Live File Manifest (`make manifest`)
- **Decision**: Implement `.agents/scripts/generate-live-manifest.py` to generate timestamped SHA-256 signature matrices for all repository files at `docs/manifest/LIVE_FILE_MANIFEST.md`.
- **Implementation**: Excludes virtual store paths and self-scanned output files to guarantee 100% reproducible diff verification.

## ADR 11: AG Kit Health Diagnosis Contract & Operator Docs (`MIGRATION.md`)
- **Decision**: Enforce 100% `make doctor` diagnostic contract readiness across 6 phases (`discovery`, `mcp`, `hooks`, `orchestration`, `plugin`, `validation`) and mandate production operator documentation ([`MIGRATION.md`](../../MIGRATION.md)).
