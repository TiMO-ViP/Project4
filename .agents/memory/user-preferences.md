# User Preferences Memory Vault

> Stores persistent user communication preferences, execution rules, and workflow directives.

---

## 🗣️ Language & Output Directives
* **Strict Terminal Communication**: Respond strictly in English. No Arabic characters in terminal outputs to prevent encoding and display corruption.

---

## ⚡ Technical & Tooling Preferences
1. **Strict pnpm Execution Protocol**: Always use `pnpm` (`pnpm install`, `pnpm exec`, `pnpm run`, `pnpm info`) as the primary package manager. `npm` usage is strictly forbidden in project commands.
2. **Directive 6 - Always-Latest Package Protocol**: AI agents MUST always query live registry APIs (`pnpm info <pkg> version`, `context7` live docs) before installing or scaffolding dependencies.
3. **Local-First Database Strategy**: Develop and test database schemas locally via Supabase CLI (`make db-start`) and Drizzle ORM before deploying SQL migrations to cloud (`make db-push`).
4. **No Unrequested Application Logic**: Never build application business logic or features without explicit user authorization via slash commands (`/speckit.specify`) or direct commands.
5. **Real-Time Verbatim Session Logging**: Automatically stream turn entries to `.agents/logs/live_session.jsonl` with full verbatim text and `os.fsync` disk flushing.
