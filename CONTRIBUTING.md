# Developer Contribution Guide

> Workflow guidelines, branching rules, and code standards for Project4.

---

## 🌲 Git Branching & PR Rules

1. **Main Trunk Protection**:
   Direct pushes to `main` are restricted. All feature work integrates via `develop` first.
2. **Branch Hierarchy**:
   * `main` — Production release trunk.
   * `develop` — Primary integration branch.
   * `feature/<short-name>` — Feature development branches.
   * `fix/<short-name>` — Bug fix branches.
   * `chore/<short-name>` — Tooling, dependency, and documentation updates.
3. **Spec-Driven Development (SDD)**:
   * Step 1: Run `/speckit.specify` on `develop` to generate `.specify/specs/<feature>.md`.
   * Step 2: Run `/speckit.plan` to generate architectural blueprint.
   * Step 3: Run `/speckit.tasks` to generate executable task list.
   * Step 4: Create feature branch (`git checkout -b feature/<feature-slug>`).
   * Step 5: Run `/speckit.implement` to execute tasks and push PR to `develop`.

---

## 📝 Commit Protocol

Commit messages must follow Conventional Commits format:
```text
<type>(<scope>): <short summary>

WHY / MOTIVATION: ...
WHAT / CHANGES MADE: ...
VERIFICATION & EVIDENCE: ...
```

Types: `feat`, `fix`, `docs`, `chore`, `refactor`, `test`, `ci`.
