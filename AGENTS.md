# AGENTS.md — Machine Instructions & Repository Guardrails

> Universal machine-readable guidelines for AI coding agents operating within this workspace.

---

## 🎯 Primary Directives

1. **Deterministic Execution**: Always read `CODEBASE.md` and `.agents/memory/MEMORY.md` before making structural code edits.
2. **Quality & Clean Code**: Adhere to `@[skills/clean-code]`. No unnecessary abstractions, no dummy fallback code, no swallowing errors.
3. **No Unrequested Project Code**: Do NOT generate application logic or build new components without explicit user authorization.
4. **Strict Security**: Never commit secrets, credentials, API keys, or private certificates. Validate `.gitignore` before every commit.

---

## 🛠️ Environment & Formatting Rules

- **Indentation**: 2 spaces for JS/TS/JSON/YAML, 4 spaces for Python, tabs for Makefile (enforced by `.editorconfig`).
- **Line Endings**: LF (`\n`).
- **Encoding**: UTF-8 without BOM.
- **Language Constraint**: Terminal responses MUST be strictly in English unless explicitly asked otherwise.

---

## 🔄 Commit & Git Conventions

- **Branch Naming**: `feature/short-name`, `fix/short-name`, `chore/short-name`.
- **Commit Style**: Conventional Commits (`type(scope): description`).
  - Types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`.
- **Verification**: Always run lint and test suites before making assertions of completion.

---

## 📁 Key Workspace Paths

- `.agents/` — AG Kit agent personas, skills, workflows, and memory system.
- `.agents/memory/MEMORY.md` — Persistent cross-session index pointer.
- `.gitignore` — Exclusion manifest.
- `.editorconfig` — Code formatting definitions.
