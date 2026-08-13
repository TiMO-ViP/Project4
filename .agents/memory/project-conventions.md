# Project Conventions Memory Vault

> Stores project governance rules, directory topology, and Git workflow conventions.

---

## 🌲 Git Branching & Hierarchy Rules
* **`main`**: Protected production trunk. Only stable, production-tested code.
* **`develop`**: Primary integration branch for active development.
* **`feature/<short-slug>`**: Feature development branches created for SDD specs.
* **`fix/<short-slug>`**: Bug fix branches.
* **`chore/<short-slug>`**: Infrastructure, dependency, and documentation updates.

---

## 🏛️ Government-Grade Clean Architecture & Monorepo Topology
* **`src/domain/`**: Pure Business Logic (Entities & Repository Contracts - ZERO dependencies).
* **`src/application/`**: Use Cases & Application Services.
* **`src/infrastructure/`**: Database (Drizzle ORM), Supabase Adapters, & OpenTelemetry Tracing (`src/infrastructure/telemetry/tracer.ts`).
* **`src/features/`**: Domain Feature Modules (UI + Local Logic).
* **`src/app/`**: Next.js 16 App Router Routes & `src/proxy.ts` (Node.js runtime network boundary).

### 📦 2026 Monorepo Package Backbone (`packages/`)
* **`packages/types/`**: Shared domain interfaces, API responses (`ApiResponse<T>`), and Result types (`Result<T, E>`) exposed as `@project4/types`.
* **`packages/config/`**: Central application settings, log levels, and environment stages exposed as `@project4/config`.
* **`packages/utils/`**: Shared functional utilities (`assertNever`, `deepFreeze`, `isNonNullable`) exposed as `@project4/utils`.

---

## 📜 Spec-Driven Development (SDD) Lifecycle
* **Phase 1**: Run `/speckit.specify` on `develop` to generate `.specify/specs/<feature>.md`.
* **Phase 2**: Run `/speckit.plan` to generate technical blueprint & ADRs in `docs/superpowers/plans/`.
* **Phase 3**: Run `/speckit.tasks` to generate executable task list with atomic verification steps.
* **Phase 4**: Create `feature/<feature-slug>` branch and run `/speckit.implement` or `subagent-driven-development` to execute tasks cleanly.
* **Phase 5**: Run `make check` pre-flight verification and open Pull Request (PR) to merge into `develop`.

