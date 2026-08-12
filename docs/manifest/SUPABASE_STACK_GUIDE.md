# Supabase + Drizzle ORM Architecture Guide

> Complete technical handbook for local database development, Drizzle ORM schema migrations, and Supabase Cloud deployment.

---

## 🏛️ Architecture & Data Flow

```text
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                      DEVELOPER WORKSPACE (LOCAL)                        │
 │                                                                         │
 │  TypeScript Schema ──> Drizzle Kit ──> SQL Migrations ──> Local Postgres│
 │  (src/db/schema.ts)    (drizzle.config.ts) (supabase/migrations/) (make db-start)│
 └────────────────────────────────────┬────────────────────────────────────┘
                                      │ make db-push
                                      ▼
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                      SUPABASE CLOUD (PRODUCTION)                        │
 │                                                                         │
 │  Project Ref: awtuyagramircsbjnjzy                                     │
 │  Region: ap-southeast-2 (PostgreSQL 17.6)                              │
 └─────────────────────────────────────────────────────────────────────────┘
```

---

## 💻 Developer Command Reference

| Single-Word Command | Action / Tool Executed | Operational Purpose |
| :--- | :--- | :--- |
| `make db-start` | `npx supabase start` | Starts local PostgreSQL, PostgREST API, Supabase Auth, Storage, and Studio GUI (`http://127.0.0.1:54323`). |
| `npm run db:generate` | `drizzle-kit generate` | Generates a new versioned SQL migration file inside `supabase/migrations/` from `src/db/schema.ts`. |
| `make db-diff` | `npx supabase db diff` | Compares local database schema against remote cloud project schema. |
| `make db-push` / `npm run db:push` | `npx supabase db push` | Pushes local SQL migrations directly to Supabase Cloud production database. |
| `npm run db:studio` | `drizzle-kit studio` | Opens interactive Drizzle Studio database browser in your web browser. |
| `make db-stop` | `npx supabase stop` | Gracefully stops all local Supabase containers. |

#### Proxy Session Refresh (`src/proxy.ts` - Next.js 16+ Convention):
* **Next.js 16+ Structural Standard**: `middleware.ts` has been replaced by `proxy.ts` (`export async function proxy(request: NextRequest)`), which defaults to the Node.js runtime for native cookie and API compatibility.
* **Security Directives**: Always use `supabase.auth.getUser()` in `proxy.ts` to validate session JWT signatures against Supabase server-side. Never rely solely on unverified local cookies.

---

## 🛡️ Security & Environment Best Practices

1. **Local Secrets Protection**: Credentials (`SUPABASE_ACCESS_TOKEN`, `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`) are strictly isolated inside `.env`.
2. **Git Governance**: `.env` is 100% excluded by `.gitignore` and enforced by Gitleaks pre-commit security scanners.
3. **Transaction Pooling**: In production serverless functions, database connections use Supabase Transaction Pooler (Port `6543`) with `{ prepare: false }` to prevent connection exhaustion.
