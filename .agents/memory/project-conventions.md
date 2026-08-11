---
type: project
created: 2026-05-25
updated: 2026-08-11
---

# Project Conventions & Git/GitHub Governance

## 🌲 Git Branching Strategy & Lifecycle
- **`main`**: Protected production branch. Always deployable. No direct commits permitted.
- **`develop`**: Integration branch for upcoming releases (if applicable).
- **Feature Branches**: `feature/<short-description>` (e.g., `feature/auth-system`)
- **Bug Fix Branches**: `fix/<short-description>` (e.g., `fix/login-null-pointer`)
- **Chore / Maintenance**: `chore/<short-description>` (e.g., `chore/update-deps`)
- **Documentation**: `docs/<short-description>` (e.g., `docs/api-guide`)

## 📝 Commit Conventions & Detailed Message Protocol
- All commit messages MUST follow **Conventional Commits**: `<type>(<scope>): <summary>`
- Allowed types: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `chore`, `ci`
- **Mandatory Message Structure**:
  1. **Header**: `<type>(<scope>): <summary>` (max 50 chars, present tense, lowercase)
  2. **Body - Why**: Explanation of why the change was necessary and what problem it solves.
  3. **Body - What**: Bullet points of specific code changes made.
  4. **Body - Verification**: Empirical proof/test runner results showing successful validation.

## 🚀 GitHub Remote Management & Merge Protocol
- **Remote Link**: `git remote add origin <github-repo-url>`
- **Initial Push**: `git push -u origin main`
- **Pull Requests (PR)**:
  - All PRs must be opened against `main` (or `develop`).
  - PR titles must follow Conventional Commits.
  - Complete `.github/PULL_REQUEST_TEMPLATE.md` with verification proof.
  - Merge Strategy: **Squash-and-Merge** or **Rebase-and-Merge** to maintain a linear git history.

## 🤖 Supported AI platforms (AG Kit)
- AG Kit **only supports Gemini CLI and Google Antigravity**.
- Do not claim compatibility with Claude Code, Cursor, Copilot, Windsurf, or other assistants unless user explicitly expands scope.
