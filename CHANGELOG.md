# Changelog

> All notable changes to Project4 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [Unreleased]

### Added
- Native Spec Kit (SDD) lifecycle integration with `develop` and `feature/*` Git branching strategy.
- Government-grade Clean Architecture core directory skeleton (`src/domain`, `src/application`, `src/infrastructure`, `src/features`).
- Documentation manifests (`docs/manifest/SYSTEM_VERSIONS.md`, `MCP_SERVERS_CATALOG.md`, `SUPABASE_STACK_GUIDE.md`).
- Live-audited dependencies: TypeScript v7.0.2 (Go compiler), Drizzle ORM v0.45.2, Drizzle Kit v0.31.10, Next.js v16.3.0 (`proxy.ts` convention).
- Local Supabase CLI v2.113.0 integration and cloud project linking (`Project4` / `awtuyagramircsbjnjzy`).
- Official Supabase Agent Skills (`supabase`, `supabase-postgres-best-practices`).
- 2-Tier persistent memory vault (Markdown Index + SQLite FTS5 BM25 search engine).
- Crash-proof real-time session logger (`.agents/logs/live_session.jsonl`).
