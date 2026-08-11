---
type: reference
created: 2026-08-11
updated: 2026-08-11
---

# Architectural Decision Records (ADR) Memory

## ADR 1: Secret Isolation & Security Rules
- **Decision**: Never store API tokens, secrets, or keys in ANY Git branch of a public repository.
- **Implementation**: Secrets live locally in `.env` (excluded by `.gitignore`) or in GitHub Actions Encrypted Secrets (`${{ secrets.* }}`). Pre-commit hook blocks secret pushes.

## ADR 2: Git Conflict Memory (`rerere`)
- **Decision**: Enable `git rerere` locally (`git config --local rerere.enabled true`).
- **Implementation**: Recurring merge conflicts are remembered and auto-resolved by Git.

## ADR 3: Machine Audit Notes (`git notes`)
- **Decision**: Use `git notes --ref=ai-audit` to attach structured JSON metadata (agent session ID, test results) directly to commit hashes without changing commit SHAs.

## ADR 4: 2026 Linter & Formatter Selection
- **Decision**: Biome for JS/TS, Ruff for Python.
- **Rationale**: 10-25x faster Rust-based toolchains replacing legacy ESLint + Prettier + Black setups.

## ADR 5: DevContainer & Cloud Environment
- **Decision**: Provide `.devcontainer/devcontainer.json`, `Dockerfile`, and `docker-compose.yml` for 1-click cloud development in VS Code / GitHub Codespaces.
