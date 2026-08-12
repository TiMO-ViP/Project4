# System & Tooling Dependency Manifest

> Exhaustive manifest of all system runtimes, CLI binaries, package managers, ORMs, databases, and dependencies used in Project4.

---

## 🛠️ Runtimes & Core Infrastructure

| Tool / Runtime | Version | Scope & Purpose | Location / Executable |
| :--- | :--- | :--- | :--- |
| **Node.js** | `v24.19.0` | JavaScript / TypeScript Server Runtime | `/usr/bin/node` |
| **Python** | `v3.14.4` | System Automation, Log Processors & Memory Engine | `/usr/bin/python3` |
| **Git** | `v2.53.0` | Distributed Version Control System | `/usr/bin/git` |
| **GitHub CLI (`gh`)** | `v2.46.0` | GitHub Automation & PR Management | `/usr/bin/gh` |
| **pnpm** | `v11.21.0` | High-Performance Package Manager | `/usr/bin/pnpm` |
| **npm** | `v10.9.2` | Node Package Manager | `/usr/bin/npm` |
| **Cargo / Rust** | `v1.97.1` | Systems Programming Runtime & Compiler | `/root/.cargo/bin/cargo` |
| **GCC** | `v15.2.0` | GNU C/C++ Compiler | `/usr/bin/gcc` |
| **Make** | `v4.4.1` | Build Automation Engine | `/usr/bin/make` |
| **Specify CLI (`specify-cli`)** | `v0.16.3.dev0` | GitHub Spec Kit SDD Tooling | `/usr/local/bin/specify-cli` |

---

## 🗄️ Database Engines & ORMs

| Software / Library | Version | Category | Description |
| :--- | :--- | :--- | :--- |
| **Supabase CLI** | `v2.113.0` | BaaS / Local DB | Local PostgreSQL, Auth, Storage, and Studio GUI |
| **Drizzle ORM** | `v0.40.0` | SQL ORM | Ultra-lightweight 100% type-safe SQL ORM for TypeScript |
| **Drizzle Kit** | `v0.30.4` | Schema CLI | Migration generator and local Drizzle Studio GUI |
| **Postgres (`postgres-js`)** | `v3.4.5` | DB Client | Native high-performance PostgreSQL driver |
| **TypeScript** | `v5.7.3` | Type Compiler | Modern TypeScript compiler engine (ES2024 NodeNext target) |
| **SQLite FTS5** | `v3.x` | Vector / Search Engine | Tier 2 hybrid BM25 full-text search memory engine |

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
├── src/                      # TypeScript Application Source Code
│   └── db/                   # Drizzle ORM Schema definitions & DB Client
├── supabase/                 # Local Supabase Scaffolding & SQL Migrations
│   ├── config.toml           # Supabase CLI Project Configuration
│   └── migrations/           # Version-Controlled SQL Migration Files
├── drizzle.config.ts         # Drizzle Kit Configuration File
├── Makefile                  # Developer CLI Commands (make db-start, make verify)
├── package.json              # Node Package Manifest & NPM Scripts
├── pyproject.toml            # Python Ruff & Pytest Manifest
├── Cargo.toml                # Rust Cargo Manifest
└── tsconfig.json             # TypeScript Compiler Configuration
```
