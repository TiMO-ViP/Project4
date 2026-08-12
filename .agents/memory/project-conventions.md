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

## 🏛️ Government-Grade Clean Architecture Topology
* **`src/domain/`**: Pure Business Logic (Entities & Repository Contracts - ZERO dependencies).
* **`src/application/`**: Use Cases & Application Services.
* **`src/infrastructure/`**: Database (Drizzle ORM) & Supabase Adapters.
* **`src/features/`**: Domain Feature Modules (UI + Local Logic).
* **`src/app/`**: Next.js 16 App Router Routes & `src/proxy.ts` (Node.js runtime network boundary).

---

## 📜 Spec-Driven Development (SDD) Lifecycle
* **Phase 1**: Run `/speckit.specify` on `develop` to generate `.specify/specs/<feature>.md`.
* **Phase 2**: Run `/speckit.plan` to generate technical blueprint & ADR.
* **Phase 3**: Run `/speckit.tasks` to generate executable task list.
* **Phase 4**: Create `feature/<feature-slug>` branch and run `/speckit.implement`.
* **Phase 5**: Open Pull Request (PR) to merge into `develop`.
