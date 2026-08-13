# User Preferences Memory Vault

> Stores persistent user communication preferences, execution rules, and workflow directives.

---

## 🗣️ Language & Output Directives
* **Strict Terminal Communication**: Respond strictly in English. No Arabic characters in terminal outputs to prevent encoding and display corruption.

---

## ⚡ Technical & Tooling Preferences

1. **Strict pnpm Execution Protocol**: Always use `pnpm` (`pnpm install`, `pnpm exec`, `pnpm run`, `pnpm info`) as the primary package manager. `npm` usage is strictly forbidden in project commands.
2. **Directive 6 - Always-Latest Package Protocol**: AI agents MUST always query live registry APIs (`pnpm info <pkg> version`, `context7` live docs) before installing, updating, or scaffolding dependencies. Never assume outdated or hardcoded versions.
3. **Latest Framework Documentation & Directive Rules**:
   * **Next.js v16.3.0+**:
     - Network Boundary: Use `proxy.ts` (root/src) with `proxy()` export instead of legacy `middleware.ts`.
     - Caching Strategy: Enable `cacheComponents: true` in `next.config.ts` and use the explicit `use cache` directive with `cacheLife()`.
     - React 19: Utilize built-in React Compiler automatic memoization; consume Server Promises in Client Components via the `use()` hook.
     - Security: Enforce strict Server Actions input validation and cookie auth boundaries.
   * **Supabase CLI v2.114.0+**:
     - Use `@supabase/ssr` for server-side auth cookie handling (`createBrowserClient`, `createServerClient`).
     - Enforce Row Level Security (RLS) policies with B-tree indexes (`auth.uid() = user_id`).
   * **Drizzle ORM v0.45.2+**:
     - Maintain version-controlled SQL migrations under `supabase/migrations/`.
   * **TypeScript v5.7+**:
     - Zero-crash strict flags: `"strict": true`, `"noUncheckedIndexedAccess": true`, `"exactOptionalPropertyTypes": true`.
   * **OpenTelemetry v1.34**:
     - Structured JSON logging with W3C `traceparent` context propagation (`00-<trace_id>-<span_id>-01`).
4. **Local-First Database Strategy**: Develop and test database schemas locally via Supabase CLI (`make db-start`) and Drizzle ORM before deploying SQL migrations to cloud (`make db-push`).
5. **No Unrequested Application Logic**: Never build application business logic or features without explicit user authorization via slash commands (`/speckit.specify`) or direct commands.
6. **Real-Time Verbatim Session Logging**: Automatically stream turn entries to `.agents/logs/live_session.jsonl` with full verbatim text and `os.fsync` disk flushing.
