# Enterprise Git Branching & Lifecycle Strategy

> Governance rules and branch hierarchy for Project4.

---

## 🌲 Branch Hierarchy & Lifecycle Map

```text
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  main                [PROTECTED PRODUCTION TRUNK]                       │
 │                      Only stable, production-tested releases land here. │
 └────────────────────────────────────▲────────────────────────────────────┘
                                      │ Pull Request (PR)
 ┌────────────────────────────────────┴────────────────────────────────────┐
 │  develop             [ACTIVE INTEGRATION BRANCH]                        │
 │                      Main branch for integrating completed features.    │
 └────────────────────────────────────▲────────────────────────────────────┘
                                      │ Feature Branching
         ┌────────────────────────────┼────────────────────────────┐
         │                            │                            │
 ┌───────┴──────────────┐    ┌────────┴─────────────┐    ┌─────────┴─────────────┐
 │ feature/<short-name> │    │ fix/<short-name>     │    │ chore/<short-name>    │
 │ New Features & UIs   │    │ Bug Fixes            │    │ Infra & Tooling       │
 └──────────────────────┘    └──────────────────────┘    └───────────────────────┘
```

---

## 📋 Branch Naming Rules & Conventions

| Branch Type | Pattern | Examples | Purpose | Target Merge |
| :--- | :--- | :--- | :--- | :--- |
| **Production** | `main` | `main` | Production-ready releases | — |
| **Integration** | `develop` | `develop` | Integration branch for upcoming features | `main` via PR |
| **Feature** | `feature/<name>` | `feature/auth-system`, `feature/user-dashboard` | New capability or component | `develop` via PR |
| **Fix** | `fix/<name>` | `fix/login-redirect`, `fix/db-connection` | Bug fixes & patches | `develop` via PR |
| **Chore** | `chore/<name>` | `chore/update-deps`, `chore/add-mcp` | Maintenance & tooling | `develop` via PR |

---

## 🛠️ Developer Branch Commands

```bash
# 1. Start a new feature branch from develop
git checkout develop
git pull origin develop
git checkout -b feature/my-new-feature

# 2. Commit changes using structured commit protocol
git commit -m "feat(auth): implement Supabase SSR login form"

# 3. Push feature branch to GitHub
git push -u origin feature/my-new-feature

# 4. Create Pull Request (PR) to develop via GitHub CLI
gh pr create --base develop --head feature/my-new-feature --title "feat(auth): add login form"

# 5. Merge PR into develop
gh pr merge --squash --delete-branch
```
