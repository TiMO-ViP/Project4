# Memory Index Pointer Directory

## User
- [user] Respond strictly in English on terminal, zero Arabic text → user-preferences.md
- [user] Senior Architect/Engineer style, prefers empirical evidence and CLI automation → user-preferences.md
- [user] No unrequested application code until explicitly commanded → user-preferences.md

## Project
- [project] GitHub repository: https://github.com/TiMO-ViP/Project4.git (main branch) → project-conventions.md
- [project] Single-word CLI Makefile automation (make help, make check, make sync) → project-conventions.md
- [project] Native version-controlled Git hooks active in .githooks/ → project-conventions.md
- [project] Parallel Git worktrees managed via .agents/scripts/git-enterprise-engine.sh → project-conventions.md

## Reference & ADR
- [reference] Secrets in .env or GitHub Secrets; NEVER store secrets in Git branches → tech-decisions.md
- [reference] git rerere enabled for merge conflict memory → tech-decisions.md
- [reference] git notes --ref=ai-audit used for machine commit metadata → tech-decisions.md
- [reference] Biome (JS/TS) and Ruff (Python) default 2026 linter toolchains → tech-decisions.md
- [reference] DevContainer (.devcontainer/) enabled for VS Code / Codespaces → tech-decisions.md
