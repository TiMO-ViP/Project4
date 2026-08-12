# Technical Decisions & Architectural Records (ADRs)

> Architectural Decision Records (ADRs) and audited software stack versions.

---

## 🛠️ Audited Ecosystem Stack (2026)

| Layer / Library | Audited Version | Key Decision Rationale |
| :--- | :--- | :--- |
| **Next.js** | `v16.3.0` | App Router, React 19, `src/proxy.ts` (Node.js runtime network boundary), Turbopack Rust bundler. |
| **TypeScript** | `v7.0.2` | Native Go compiler delivering 8x-12x parallel type-checking speedups (ES2024 NodeNext). |
| **Supabase** | `v2.113.0` (CLI) | Local-first Postgres 17, cookie JWT auth (`@supabase/ssr`), and RLS policies (`auth.uid() = user_id`). Cloud project linked (`Project4` / `awtuyagramircsbjnjzy`). |
| **Drizzle ORM** | `v0.45.2` | Ultra-lightweight ~50KB SQL-first ORM layer with transparent versioned SQL migrations (`supabase/migrations/`). |
| **Postgres Driver** | `v3.4.9` | Native `postgres-js` driver configured with `{ prepare: false }` for PgBouncer transaction pooling. |

---

## 🛡️ Security & Compliance Standards
* **NIST SP 800-218 (SSDF)** & **FedRAMP Moderate/High**: Automated secret scanning (`.gitleaks.toml`), zero plaintext credentials in source code, and zero-trust Server Actions.
* **Row-Level Security (RLS)**: B-tree indexing on `user_id` columns to eliminate full-table scans during RLS policy execution.
