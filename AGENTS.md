# AGENTS.md — Machine Instructions & Repository Guardrails

> Universal machine-readable guidelines for AI coding agents operating within this workspace.

---

## 🎯 Primary Directives

1. **Deterministic Execution**: Always read [.agents/memory/MEMORY.md](.agents/memory/MEMORY.md) (the Single Master Brain Hub) and [CODEBASE.md](CODEBASE.md) before making structural code edits.
2. **Quality & Clean Code**: Adhere to `@[skills/clean-code]`. No unnecessary abstractions, no dummy fallback code, no swallowing errors.
3. **No Unrequested Project Code**: Do NOT generate application logic or build new components without explicit user authorization.
4. **Strict Security**: Never commit secrets, credentials, API keys, or private certificates. Validate `.gitignore` before every commit.
5. **Automated Real-Time Session Logging**: Automatically log session boot and turn entries to `.agents/logs/live_session.jsonl` via `python3 .agents/scripts/live_session_logger.py` for 100% crash-proof persistence.
6. **Always-Latest Package & Tooling Protocol**: Always query live package registries (`pnpm info`, `context7`) to ensure all installed libraries, tools, and runtimes use the absolute latest stable versions.


---

## 🛠️ Environment & Formatting Rules

- **Package Manager**: Mandatory `pnpm` (`pnpm exec`, `pnpm run`, `pnpm install`, `pnpm info`).
- **Indentation**: 2 spaces for JS/TS/JSON/YAML, 4 spaces for Python, tabs for Makefile (enforced by `.editorconfig`).
- **Line Endings**: LF (`\n`).
- **Encoding**: UTF-8 without BOM.
- **Language Constraint**: Terminal responses MUST be strictly in English unless explicitly asked otherwise.

---

## 🌲 Git Branching & GitHub Protocol

- **Branch Naming**: `feature/short-description`, `fix/short-description`, `chore/short-description`, `docs/short-description`.
- **Protected Trunk**: Direct pushes to `main` are forbidden once remote is connected. Use Pull Requests (PRs).
- **Git Worktrees**: For parallel task execution, use `git worktree add ../<folder> <branch>` to avoid switching context on `main`.

---

## 📝 Commit Message Protocol

- **Format**: `<type>(<scope>): <short-summary>`
- **Template**: Enforced by `.gitmessage`.
- **Commit Body Requirements**:
  1. **Why**: Context and motivation for the change.
  2. **What**: Bullet points of technical modifications.
  3. **Verification**: Command evidence showing tests/lints passed.

---

## 🔄 GitHub Remote Commands Quick-Reference

- **Link Remote**: `git remote add origin <url>`
- **Push Branch**: `git push -u origin <branch-name>`
- **Create PR via GitHub CLI**: `gh pr create --title "type(scope): summary" --body-file .github/PULL_REQUEST_TEMPLATE.md`
- **Merge PR via GitHub CLI**: `gh pr merge --squash --delete-branch`

---

## 📁 Key Workspace Paths

- `.agents/` — AG Kit agent personas, skills, workflows, and memory system.
- `.agents/memory/MEMORY.md` — Single Master Brain Hub & Persistent cross-session index pointer.
- `.github/` — PR templates, issue templates, and CODEOWNERS routing.
- `.gitmessage` — Structured commit template.
- `.gitignore` — Exclusion manifest.
- `.editorconfig` — Code formatting definitions.
