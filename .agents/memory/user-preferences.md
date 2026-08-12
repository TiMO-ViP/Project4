# User Preferences Memory Vault

> Stores persistent user communication preferences, execution rules, and workflow directives.

---

## 🗣️ Language & Output Directives
* **Strict Terminal Communication**: Respond strictly in English. No Arabic characters in terminal outputs to prevent encoding and display corruption.

---

## ⚡ Technical & Tooling Preferences
1. **Directive 6 - Always-Latest Package Protocol**: AI agents MUST always query live registry APIs (`npm info <pkg> version`, `context7` live docs) before installing or scaffolding dependencies.
2. **Local-First Database Strategy**: Develop and test database schemas locally via Supabase CLI (`make db-start`) and Drizzle ORM before deploying SQL migrations to cloud (`make db-push`).
3. **No Unrequested Application Logic**: Never build application business logic or features without explicit user authorization via slash commands (`/speckit.specify`) or direct commands.
4. **Real-Time Verbatim Session Logging**: Automatically stream turn entries to `.agents/logs/live_session.jsonl` with full verbatim text and `os.fsync` disk flushing.
