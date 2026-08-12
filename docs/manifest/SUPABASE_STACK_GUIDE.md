# Supabase + Drizzle ORM + Next.js 16 Architecture Guide

> Complete technical handbook for local database development, Drizzle ORM schema migrations, Next.js 16 `proxy.ts` network boundary, and Supabase Cloud deployment.

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
| `make db-start` | `npx supabase start` | Starts local PostgreSQL 17, PostgREST API, Supabase Auth, Storage, and Studio GUI (`http://127.0.0.1:54323`). |
| `npm run db:generate` | `drizzle-kit generate` | Generates a new versioned SQL migration file inside `supabase/migrations/` from `src/db/schema.ts`. |
| `make db-diff` | `npx supabase db diff` | Compares local database schema against remote cloud project schema. |
| `make db-push` / `npm run db:push` | `npx supabase db push` | Pushes local SQL migrations directly to Supabase Cloud production database. |
| `npm run db:studio` | `drizzle-kit studio` | Opens interactive Drizzle Studio database browser in your web browser. |
| `make db-stop` | `npx supabase stop` | Gracefully stops all local Supabase containers. |

---

## 🌐 Next.js 16+ `proxy.ts` Network Boundary & Cookie Auth

In Next.js 16+, `middleware.ts` has been replaced by **`proxy.ts`** running natively on the **Node.js runtime**:

```typescript
// src/proxy.ts (Next.js 16+ Standard)
import { NextRequest, NextResponse } from 'next/server';
import { updateSession } from '@/lib/supabase/proxy';

export async function proxy(request: NextRequest) {
  // 1. Refresh Supabase JWT session cookies via Node.js runtime
  const response = await updateSession(request);

  // 2. Perform route protection checks
  return response;
}

export const config = {
  matcher: [
    '/((?!_next/static|_next/image|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|webp)$).*)',
  ],
};
```

---

## 🛡️ Security & Environment Best Practices

1. **PostgreSQL 17 Row-Level Security (RLS)**:
   Every table MUST have RLS enabled (`ALTER TABLE table_name ENABLE ROW LEVEL SECURITY;`). Ensure `auth.uid() = user_id` columns are indexed with B-tree indexes for fast execution.
2. **Zero-Trust Server Actions**:
   Server Actions (`"use server"`) are public HTTP endpoints. Always check `await supabase.auth.getUser()` and validate inputs with **Zod** schemas inside every action.
3. **Local Secrets Protection**: Credentials (`SUPABASE_ACCESS_TOKEN`, `SUPABASE_SERVICE_ROLE_KEY`, `DATABASE_URL`) are strictly isolated inside `.env`.
4. **Git Governance**: `.env` is 100% excluded by `.gitignore` and enforced by Gitleaks pre-commit security scanners.
5. **Transaction Pooling**: In production serverless functions, database connections use Supabase Transaction Pooler (Port `6543`) with `{ prepare: false }` to prevent connection exhaustion.
