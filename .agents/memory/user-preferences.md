# User Preferences Memory Vault

> Stores persistent user communication preferences, execution rules, and workflow directives.

---

## 🗣️ Language Directives
* **Terminal Communication**: Respond strictly in English. No Arabic characters in terminal outputs to avoid encoding/display corruption.

---

## ⚡ Technical & Tooling Preferences
1. **Always-Latest Versions Directive**: AI agents must always check live registry APIs (`npm info <pkg> version`, `context7`) to use the latest versions of TypeScript, Drizzle ORM, Supabase CLI, and Node packages.
2. **Local-First Database Strategy**: Use Supabase CLI (`supabase start`) and Drizzle ORM locally before deploying migrations to cloud.
3. **No Unrequested Application Code**: Do not generate application features or business logic without explicit user commands.
