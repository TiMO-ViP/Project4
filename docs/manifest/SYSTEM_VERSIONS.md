# System & Tooling Dependency Manifest

> Exhaustive, live-audited manifest of all system runtimes, CLI binaries, package managers, ORMs, databases, and dependencies used in Project4.

---

## 🛠️ Runtimes & Core Infrastructure

| Tool / Runtime | Version | Status / Release Date | Key Architecture Notes | Location / Executable |
| :--- | :--- | :--- | :--- | :--- |
| **TypeScript** | `v7.0.2` | 🟢 **STABLE (Jul 2026)** | Native Go compiler (8x-12x faster parallel checking) | Installed in `node_modules` |
| **Next.js** | `v16.3.0` | 🟢 **ACTIVE LTS (Aug 2026)**| React 19, `proxy.ts` network boundary, Turbopack default | Installed in `node_modules` |
| **Node.js** | `v24.19.0` | 🟢 **ACTIVE LTS** | JavaScript / TypeScript Server Runtime | `/usr/bin/node` |
| **Python** | `v3.14.4` | 🟢 **ACTIVE STABLE**| System Automation, Log Processors & Memory Engine | `/usr/bin/python3` |
| **Git** | `v2.53.0` | 🟢 **LATEST STABLE**| Distributed Version Control System | `/usr/bin/git` |
| **GitHub CLI (`gh`)** | `v2.46.0` | 🟢 **LATEST STABLE**| GitHub Automation & PR Management | `/usr/bin/gh` |
| **pnpm** | `v11.21.0` | 🟢 **LATEST STABLE**| High-Performance Package Manager | `/usr/bin/pnpm` |
| **npm** | `v10.9.2` | 🟢 **LATEST STABLE**| Node Package Manager | `/usr/bin/npm` |
| **Cargo / Rust** | `v1.97.1` | 🟢 **LATEST STABLE**| Systems Programming Runtime & Compiler | `/root/.cargo/bin/cargo` |
| **GCC** | `v15.2.0` | 🟢 **LATEST STABLE**| GNU C/C++ Compiler | `/usr/bin/gcc` |
| **Make** | `v4.4.1` | 🟢 **LATEST STABLE**| Build Automation Engine | `/usr/bin/make` |
| **Specify CLI (`specify-cli`)** | `v0.16.3.dev0` | 🟢 **ACTIVE SDD** | GitHub Spec Kit SDD Tooling | `/usr/local/bin/specify-cli` |

---

## 🗄️ Database Engines & ORMs

| Software / Library | Version | Audit Status | Category | Description |
| :--- | :--- | :--- | :--- | :--- |
| **Supabase CLI** | `v2.113.0` | 🟢 **LATEST 2026** | BaaS / Local DB | Local PostgreSQL 17, Auth, Storage, and Studio GUI |
| **Drizzle ORM** | `v0.45.2` | 🟢 **LATEST 2026** | SQL ORM | Ultra-lightweight ~50KB SQL ORM for TypeScript |
| **Drizzle Kit** | `v0.31.10` | 🟢 **LATEST 2026** | Schema CLI | Transparent SQL migration generator & Studio GUI |
| **Postgres (`postgres-js`)** | `v3.4.9` | 🟢 **LATEST 2026** | DB Client | Native high-performance PostgreSQL driver |
| **`@types/node`** | `v26.2.0` | 🟢 **LATEST 2026** | Types Package | Official TypeScript type definitions for Node.js v26+ |
| **SQLite FTS5** | `v3.x` | 🟢 **ACTIVE** | Vector / Search | Tier 2 hybrid BM25 full-text search memory engine |

---

## 📁 Repository Structure Map

```text
/storage/emulated/0/projector/project4
├── .agents/                  # AG Kit Agent Framework, Skills, & Memory
│   ├── mcp_config.json       # MCP Server Registration Manifest
│   ├── memory/               # 2-Tier Persistent Memory Vault (MEMORY.md + tier2_vector.db)
│   ├── scripts/              # Live Session Logger & Memory Engine Scripts
│   └── skills/               # 49 Installed Agent Skills (inc. Supabase & Drizzle)
├── .github/                  # GitHub Actions CI Workflows & PR Templates
├── .specify/                 # GitHub Spec Kit SDD Templates & Project Constitution
├── docs/                     # Documentation Portal
│   └── manifest/             # Dedicated Tooling, Versions, and Architecture Manifests
│       ├── SYSTEM_VERSIONS.md     # Runtimes, compilers, databases, ORMs & directory map
│       ├── MCP_SERVERS_CATALOG.md # 9 Configured Model Context Protocol servers
│       └── SUPABASE_STACK_GUIDE.md# Next.js 16, Supabase Local/Cloud & Drizzle handbook
├── src/                      # TypeScript Application Source Code
│   ├── db/                   # Drizzle ORM Schema definitions & DB Client
│   └── proxy.ts              # Next.js 16+ Node.js Runtime Network Boundary
├── supabase/                 # Local Supabase Scaffolding & SQL Migrations
│   ├── config.toml           # Supabase CLI Project Configuration
│   └── migrations/           # Version-Controlled SQL Migration Files
├── drizzle.config.ts         # Drizzle Kit Configuration File
├── Makefile                  # Developer CLI Commands (make db-start, make version-audit)
├── package.json              # Node Package Manifest & NPM Scripts
├── pyproject.toml            # Python Ruff & Pytest Manifest
├── Cargo.toml                # Rust Cargo Manifest
└── tsconfig.json             # TypeScript Compiler Configuration
```
