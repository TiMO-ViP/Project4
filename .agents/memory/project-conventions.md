---
type: project
created: 2026-05-25
updated: 2026-08-11
---

# Project Conventions & Git Governance Memory

## 🌐 Repository & Environment Details
- **GitHub Repository**: `https://github.com/TiMO-ViP/Project4.git` (Default Branch: `main`)
- **System**: Ubuntu 26.04 LTS (`resolute`) on `aarch64` inside PRoot-Distro
- **Runtimes**: Node.js `v24.19.0`, Python `3.14.4`, Git `2.53.0`
- **Toolkit**: AG Kit `2026.7.27`

## 🌲 Git Branching & Worktree Strategy
- **`main`**: Protected production branch. Always deployable. Direct pushes forbidden once linked.
- **Git Worktrees**: Parallel tasks run in `.worktrees/<branch-name>` via `.agents/scripts/git-enterprise-engine.sh`.
- **Branch Taxonomy**: `epic/<domain>`, `feature/<epic>/<task>`, `fix/<issue>`, `chore/<tooling>`.
- **Automated Pruning**: Run `make prune` to clean merged branches and stale worktrees.

## 📝 Commit & Hook Conventions
- **Conventional Commits**: `<type>(<scope>): <summary>` (enforced by `.gitmessage`).
- **Required Body Sections**: WHY / MOTIVATION, WHAT / CHANGES MADE, VERIFICATION & EVIDENCE.
- **Git Hooks Path**: Configured to `.githooks/` via `git config core.hooksPath .githooks`.
  - `.githooks/pre-commit`: Secret scanning security gate (Gitleaks).
  - `.githooks/prepare-commit-msg`: Deterministic auto-commit message generator.

## ⚡ Automation CLI (`Makefile`)
- Single-word commands: `make help`, `make dev`, `make lint`, `make format`, `make test`, `make typecheck`, `make check`, `make security`, `make prune`, `make sync`, `make clean`.
