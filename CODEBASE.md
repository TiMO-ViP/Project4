# CODEBASE.md — System Architecture & Directory Map

> Architectural overview and file dependency guide for AI assistants and human developers.

---

## 🗺️ Project Directory Map

```
/storage/emulated/0/projector/project4/
├── AGENTS.md                  ← Master AI agent rules and standards
├── CODEBASE.md                ← System map & architectural index (this file)
├── .editorconfig              ← Code formatting rules across editors
├── .gitignore                 ← Git exclusion rules
├── .env.example               ← Environment variable template
└── .agents/                   ← AG Kit Governance & Agentic Suite
    ├── ARCHITECTURE.md        ← AG Kit component catalog
    ├── VERSION                ← AG Kit CalVer version (2026.7.27)
    ├── antigravity.json       ← Runtime configuration contract
    ├── agent/                 ← 20 specialist agent personas
    ├── skills/                ← 50+ modular engineering skills
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
| `AGENTS.md` | `.editorconfig`, `.gitignore` | All agent execution pipelines |
| `.agents/antigravity.json` | `.agents/rules/`, `.agents/skills/` | CLI runner & Doctor validation script |
| `.agents/memory/MEMORY.md` | `.agents/memory/*.md` topic files | All session initialization routines |
