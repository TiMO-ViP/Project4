# Project4 Enterprise Spec Constitution

## Core Principles

### I. Spec-Driven Development (SDD) Lifecycle
Every non-trivial feature or structural change MUST begin with a specification phase before code is written:
- **Phase 1 (Specification)**: Define requirements in `.specify/specs/<feature-slug>.md`.
- **Phase 2 (Technical Blueprint & ADR)**: Define architecture, data model, and API contracts in `.specify/plans/<feature-slug>.md`.
- **Phase 3 (Task Breakdown)**: Generate executable, atomic tasks in `.specify/tasks/<feature-slug>.md`.
- **Phase 4 (Implementation & Auto-Commit)**: Execute tasks on a dedicated `feature/<feature-slug>` branch and auto-commit verified changes.

### II. Clean Architecture & Domain Isolation
- Business domain entities (`src/domain/`) MUST remain pure TypeScript with ZERO external framework dependencies.
- Use Cases (`src/application/`) orchestrate domain entities and repository contracts.
- Database access and external SDKs MUST be encapsulated in infrastructure adapters (`src/infrastructure/`).

### III. Automated Verification & Quality Gates
- Code edits MUST NOT be claimed complete without empirical command evidence (`make test`, `make check`).
- Pre-commit secret scanning (`.githooks/pre-commit`) blocks unencrypted credentials or private keys from entering Git history.

### IV. Local-First Database & Environment Safety
- Database schema changes MUST be tested against local Supabase Postgres (`DB_TARGET=local`) before applying to cloud production (`DB_TARGET=cloud`).

## Governance
This Constitution supersedes informal practices. Amendments require documentation and updating this file.

**Version**: 1.0.0 | **Ratified**: 2026-08-12 | **Last Amended**: 2026-08-12
