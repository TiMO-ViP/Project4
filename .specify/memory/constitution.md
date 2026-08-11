# Project4 Enterprise Constitution

## Core Principles

### I. Spec-Driven Development (SDD) Mandatory
Every non-trivial feature or modification MUST follow the SDD pipeline:
1. Requirements Spec (`/speckit.specify`)
2. Technical Plan (`/speckit.plan`)
3. Task List (`/speckit.tasks`)
4. Implementation (`/speckit.implement`)
No unrequested code generation or raw chat-driven feature building allowed.

### II. Machine Readability & Language Rule
- Terminal responses and code comments MUST be strictly in English (zero Arabic output).
- AG Kit governance (`AGENTS.md`) and memory (`.agents/memory/MEMORY.md`) supersede informal prompts.

### III. Zero Secrets & Strict Security Gate
- NEVER store credentials, passwords, or API keys in Git branches or public files.
- All secrets live in local `.env` (excluded by `.gitignore`) or GitHub Actions Encrypted Secrets.
- Pre-commit hook (`.githooks/pre-commit`) blocks secret leaks automatically.

### IV. Test-Driven & Clean Code Quality
- Clean Code principles (`@[skills/clean-code]`) strictly enforced. No swallowing errors, no dummy fallbacks.
- Automated tests written & passing before marking features as complete.

### V. Git Worktree & Branch Governance
- Main branch (`main`) is protected.
- Parallel tasks executed in isolated Git Worktrees (`.worktrees/`).
- Commit messages follow Conventional Commits (`type(scope): description` + Why, What, Verification).

## Development Workflow & Quality Gates
- **CLI Commands**: Execute `make check` for pre-flight verification, `make sync` for GitHub sync.
- **Spec Drift Guard**: Run `/speckit.checklist` and `/speckit.analyze` to ensure implementation matches original requirements.

## Governance
This Constitution supersedes informal chat requests. Any architectural amendment requires updating `.specify/memory/constitution.md` and committing the change to Git.

**Version**: 1.0.0 | **Ratified**: 2026-08-11 | **Last Amended**: 2026-08-11
