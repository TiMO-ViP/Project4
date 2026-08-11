# CODEBASE.md — System Architecture & Directory Map

> Architectural overview and file dependency guide for AI assistants and human developers.

---

## 🗺️ System Topology Diagram

```mermaid
graph TD
    User[Developer / AI Agent] --> CLI[Master Makefile / terminal]
    CLI --> GitHooks[.githooks/ pre-commit & prepare-commit-msg]
    GitHooks --> GitEngine[.agents/scripts/git-enterprise-engine.sh]
    GitEngine --> Worktrees[.worktrees/ Isolated Execution]
    GitEngine --> RemoteRepo[GitHub Remote origin/main]
    CLI --> DevContainer[.devcontainer/ Docker Container]
```

---

## 📁 Project Directory Map

```
/storage/emulated/0/projector/project4/
├── AGENTS.md                  ← Master AI agent rules and standards
├── CODEBASE.md                ← System map & architectural index (this file)
├── STATUS.md                  ← Live interactive workspace status board
├── Makefile                   ← Master CLI automation interface (make help, make dev)
├── Dockerfile                 ← Multi-stage production container build
├── docker-compose.yml         ← Container orchestration file
├── .editorconfig              ← Code formatting rules across editors
├── .gitignore                 ← Git exclusion rules
├── .env.example               ← Environment variable template
├── .devcontainer/             ← 1-click VS Code / Codespaces dev container
│   └── devcontainer.json
├── .githooks/                 ← Version-controlled native Git hooks
│   ├── pre-commit             ← Secret scanning security gate
│   └── prepare-commit-msg     ← Deterministic auto-commit generator
└── .agents/                   ← AG Kit Governance & Agentic Suite
    ├── ARCHITECTURE.md        ← AG Kit component catalog
    ├── VERSION                ← AG Kit CalVer version (2026.7.27)
    ├── antigravity.json       ← Runtime configuration contract
    ├── agent/                 ← 20 specialist agent personas
    ├── skills/                ← 50+ modular engineering skills
    ├── scripts/               ← Automation scripts (git-enterprise-engine.sh, setup-environment.sh)
    ├── memory/                ← Cross-session persistent memory vault
    │   ├── MEMORY.md          ← Memory index pointer
    │   ├── user-preferences.md← Persistent user settings & style
    │   ├── project-conventions.md ← Coding conventions & branch rules
    │   └── tech-decisions.md  ← Architectural decision record (ADR)
    ├── rules/                 ← Core protocol & routing rules
    └── workflows/             ← Interactive slash command guides
```

---

## ⚙️ Environment Specifications

- **OS / Host**: Ubuntu 26.04 LTS (`resolute`) on `aarch64` inside PRoot-Distro
- **Runtimes**: Node.js `v24.19.0`, Python `3.14.4`
- **VCS**: Git `2.53.0` (Default branch: `main`)
- **Toolkit**: AG Kit `2026.7.27`

---

## 🔗 File Dependency Matrix

| File / Component | Upstream Dependencies | Downstream Dependents |
| :--- | :--- | :--- |
| `Makefile` | `.githooks/`, `.agents/scripts/` | Developer CLI execution |
| `.githooks/` | `.agents/scripts/git-auto-commit-msg.sh` | Git commit lifecycle |
| `.devcontainer/` | `Dockerfile`, `docker-compose.yml` | Cloud & container development |
| `AGENTS.md` | `.editorconfig`, `.gitignore` | All agent execution pipelines |
