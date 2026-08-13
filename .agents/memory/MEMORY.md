# 🧠 AG Kit 2-Tier Persistent Memory Vault

> Master index pointer file for cross-session AI memory in Project4.

---

## 📌 Memory Vault Index Pointer

1. **[User Preferences (`user-preferences.md`)](user-preferences.md)**:
   * English-only terminal output directive.
   * Directive 6: Always-Latest Package Protocol (`npm info`, `context7`).
   * Local-First Database strategy (`make db-start`).
   * No unrequested application business logic.
   * Atomic real-time JSONL session logging (`live_session.jsonl`).

2. **[Project Conventions (`project-conventions.md`)](project-conventions.md)**:
   * Git Branching Hierarchy: `main` (Protected), `develop` (Integration), `feature/*` (SDD specs).
   * Government-Grade Clean Architecture (`src/domain`, `src/application`, `src/infrastructure`, `src/features`, `src/app`).
   * Monorepo `@project4/*` package backbone (`packages/types`, `packages/config`, `packages/utils`).
   * Spec-Driven Development (SDD) 5-Phase Lifecycle & Spec-Kit workflow.

3. **[Technical Decisions & ADRs (`tech-decisions.md`)](tech-decisions.md)**:
   * Audited 2026 Stack: Next.js v16.3.0 (`proxy.ts`), TypeScript v5.7+ strict zero-crash compiler safety flags, Supabase v2.113.0, Drizzle ORM v0.45.2.
   * OpenTelemetry v1.34 structured tracing & context propagation (`src/infrastructure/telemetry/tracer.ts`).
   * CycloneDX 1.6 Supply Chain Security & SBOM (`make sbom`).
   * Monorepo path aliases (`@project4/types`, `@project4/config`, `@project4/utils`).
   * NIST SP 800-218 (SSDF) Security & B-tree indexed RLS policies.

---

## ⚡ Tier 2 Vector Memory Search Command
```bash
make memory-search Q="supabase auth"
```
