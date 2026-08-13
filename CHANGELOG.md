# Changelog

> All notable changes to Project4 will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0](https://github.com/TiMO-ViP/Project4/compare/project4-v1.0.0...project4-v1.1.0) (2026-08-13)


### Features

* **architecture:** establish government-grade Clean Architecture project skeleton (NIST SSDF & FedRAMP compliant) ([a761cb1](https://github.com/TiMO-ViP/Project4/commit/a761cb15bf5a961db3a7377d2d89a251f10a071c))
* **ci:** add github actions workflow and git superpowers automation script ([b606984](https://github.com/TiMO-ViP/Project4/commit/b6069843ef79d402ea5f32d9576d863d32325e25))
* **config:** provision multi-language stack configuration files (TS, Python, Rust) ([a81f775](https://github.com/TiMO-ViP/Project4/commit/a81f775491dc2c38b71d3e33cdea769a78b8d0bb))
* **develop:** update generate-live-manifest.py (def compute_sha256(file_path):;def count_lines(file_path):;def scan_files(output_file_path):;) ([8cef44d](https://github.com/TiMO-ViP/Project4/commit/8cef44d0e4e165e55aad4b6bc4fe935031b1ff35))
* **develop:** update proxy.ts (const userAgent = req.headers['user-agent'] || '';;) ([9d6acfb](https://github.com/TiMO-ViP/Project4/commit/9d6acfb4546745d1a506260a7e9b6ca746441317))
* **drizzle:** setup Drizzle ORM, PostgreSQL schema, and TypeScript 5 integration for Supabase ([5725219](https://github.com/TiMO-ViP/Project4/commit/57252191ebd7358772ce5e3e5235dd7e0b9d4bc6))
* **env:** add pre-flight environment provisioner for typescript and python ([09fdf24](https://github.com/TiMO-ViP/Project4/commit/09fdf24f483e6d6ce86f78384f870811171622f5))
* **env:** add Turborepo build pipeline configuration and typecheck script ([f5928d4](https://github.com/TiMO-ViP/Project4/commit/f5928d428b184010405985e72903f3cd9030981c))
* **env:** expand multi-language environment provisioner for TypeScript, Python, and Rust ([9b48645](https://github.com/TiMO-ViP/Project4/commit/9b4864548fbcb56e3b919ac508a27b8be611856f))
* **git:** add complete github governance commit templates and branching rules ([e252f03](https://github.com/TiMO-ViP/Project4/commit/e252f0328836337c0b6388a2755e9c58dacb9c89))
* **git:** add enterprise git orchestration engine and worktrees support ([d8364d0](https://github.com/TiMO-ViP/Project4/commit/d8364d0a79e122d5f037000bd7dddf96f161f251))
* **git:** add setup-hooks recipe and expand pre-commit secret patterns ([6c7296d](https://github.com/TiMO-ViP/Project4/commit/6c7296dd6aca9763e544260351f3f86538ad28d8))
* **git:** add version-controlled git hooks for pre-commit secret scanning and auto-commit-msg ([097e291](https://github.com/TiMO-ViP/Project4/commit/097e291f1a599431892fd86ac1d10d822107acb8))
* **governance:** ratify Directive 6 for Always-Latest Package & Tooling Protocol ([60d6234](https://github.com/TiMO-ViP/Project4/commit/60d6234309ca9af98da4b5d52f167cf19a7586c7))
* **infra:** add master Makefile, DevContainer, status board, and mermaid diagrams ([33adf6e](https://github.com/TiMO-ViP/Project4/commit/33adf6e3a93da37d29876a9c103535ce8901546b))
* **logging:** add atomic append-only JSON Lines live logger live_session.jsonl ([3dfdd70](https://github.com/TiMO-ViP/Project4/commit/3dfdd708938928743e7dce4c1e84576640231179))
* **logging:** add automated timestamped conversation transcript exporter script and make log-export CLI command ([82448c2](https://github.com/TiMO-ViP/Project4/commit/82448c23af043b9cec70de3b87f61d1d9310eb73))
* **logging:** automate real-time JSON Lines session logger on session boot and turn ([a581bba](https://github.com/TiMO-ViP/Project4/commit/a581bba9fc17f034fd4c4001f3d52407523c9284))
* **logging:** extract 100% full verbatim copy-and-paste text of user prompts and assistant markdown responses ([dcd1d87](https://github.com/TiMO-ViP/Project4/commit/dcd1d879e749e03d0ee14db60bd3fc1f0018d55f))
* **logging:** refactor conversation logger to use single continuous master log file CURRENT_SESSION.md ([e1db68e](https://github.com/TiMO-ViP/Project4/commit/e1db68ed1a9e04bd8005273b7c98f3d7c8d46c73))
* **mcp:** configure essential free open-source MCP servers (filesystem, git, memory, fetch, context7) ([41d34ae](https://github.com/TiMO-ViP/Project4/commit/41d34aeabec4e3aad30fdf0e45fe3c05141a2be0))
* **mcp:** register enterprise database MCP servers (SQLite, Postgres, Supabase, MongoDB) ([3042a27](https://github.com/TiMO-ViP/Project4/commit/3042a27d82762d58920266dc18ba8f8c7c25a619))
* **memory:** add tier 2 local fts5 hybrid vector memory engine and cli search ([abd3c1f](https://github.com/TiMO-ViP/Project4/commit/abd3c1f31144e9b1ffea90afb88bc1508bcfd771))
* **sdd:** integrate GitHub Spec Kit lifecycle natively with enterprise Git branching strategy ([3082fff](https://github.com/TiMO-ViP/Project4/commit/3082fff11e74c26fa1ed0a6234a26d49d2c2249b))
* **security:** add CycloneDX SBOM generator script and initial inventory ([818bccf](https://github.com/TiMO-ViP/Project4/commit/818bccfc4729d910202a386add7ce1bc8696b806))
* **skills:** install official Supabase and Supabase Postgres Best Practices agent skills ([a3705cb](https://github.com/TiMO-ViP/Project4/commit/a3705cb2fa462b9a10bc3152bd0e948e36535b73))
* **speckit:** install github spec-kit CLI and integrate SDD workflow slash commands ([8a13340](https://github.com/TiMO-ViP/Project4/commit/8a1334008d1f32c1000c997b28eba29f3e41d43f))
* **supabase:** initialize local Supabase CLI config, migrations directory, and Makefile commands ([50453eb](https://github.com/TiMO-ViP/Project4/commit/50453eb411612f528ba0dd12e7e8797bfa7ab3d3))
* **telemetry:** add OpenTelemetry structured logger and context propagation module ([613a0ff](https://github.com/TiMO-ViP/Project4/commit/613a0ffa0f8ddd07e731539ce8c7026172068ac1))
* **user:** implement GetUserProfileUseCase following TDD Red-Green-Refactor cycle ([ce70ff6](https://github.com/TiMO-ViP/Project4/commit/ce70ff66ab168fc3724ea7c4287877889c8bcf68))


### Bug Fixes

* **ci:** add gitleaks.toml allowlist for test fixtures and update workflow config ([5676fcd](https://github.com/TiMO-ViP/Project4/commit/5676fcd8e1f861775ddebe773e0f467e9f910554))
* **ci:** correct editorconfig-checker GitHub action repository reference ([4e85f48](https://github.com/TiMO-ViP/Project4/commit/4e85f4842c38c427dbe9e1104d3f27e7bcaff576))
* **develop:** update 1 file(s) in develop ([eee512f](https://github.com/TiMO-ViP/Project4/commit/eee512f13500d3280f24f119a8aab301d95635a5))
* **develop:** update auto_commit_on_edit.py (def cleanup_stale_locks():;def configure_git_environment():;def get_modified_files():;) ([6033063](https://github.com/TiMO-ViP/Project4/commit/6033063533e3e5bd860996ec9af2e26d48c63ac7))
* **make:** optimize make check execution to run under 1 second without network loops ([4879623](https://github.com/TiMO-ViP/Project4/commit/4879623d5b6f1cad87a5087ab76ed28f664e3fae))
* **review:** address code review feedback for Turborepo and Git hooks ([dfdaa7c](https://github.com/TiMO-ViP/Project4/commit/dfdaa7c99c5e962494f985f20f90f178ebb2add7))

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
