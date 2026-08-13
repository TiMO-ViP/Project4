# Enterprise Development Environment Upgrade Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Upgrade local environment configuration and scripts to conform to 2026 enterprise-grade standards (hermetic reproducibility, pnpm monorepo structure, Turborepo pipeline caching, automated strict typechecking, local database orchestration, and zero-drift pre-flight verification).

**Architecture:** We will enforce Corepack for deterministic pnpm package management, configure Turborepo (`turbo.json`) for cached task graphs across build/test/lint phases, integrate Biome and TypeScript typechecking into `package.json` scripts, expand local Supabase/Drizzle workflow targets in `Makefile`, and establish an automated environment health diagnostic suite.

**Tech Stack:** Node.js v24.19, pnpm v11.21, Turborepo v2.x, Next.js v16.3, Supabase CLI v2.113, Drizzle ORM v0.45, Biome v1.9, Vitest v3.0, TypeScript v7.0.

## Global Constraints

- Strict terminal output in English.
- Always-Latest Package Protocol (`npm info`, `context7`).
- Local-First Database Strategy (`make db-start`, `make db-push`).
- No unrequested application business logic.
- 100% deterministic, testable commands.

---

### Task 1: Lock Corepack & pnpm Package Manager Configuration

**Files:**
- Modify: `package.json:1-12`
- Test: Executing `pnpm --version` in terminal

**Interfaces:**
- Consumes: Existing Node.js & pnpm installation.
- Produces: Locked `packageManager` field enforcing pnpm v11.21.0 via Corepack.

- [ ] **Step 1: Write failing test script in temporary check**

Run: `node -e 'const pkg=require("./package.json"); if (!pkg.packageManager) process.exit(1);'`
Expected: Verify current state or failure if missing exact format.

- [ ] **Step 2: Update package.json with Corepack configuration**

Update `package.json` to explicitly include:
```json
"packageManager": "pnpm@11.21.0",
"engines": {
  "node": ">=24.0.0",
  "pnpm": ">=11.0.0"
}
```

- [ ] **Step 3: Run validation check**

Run: `node -e 'const pkg=require("./package.json"); console.log(pkg.packageManager && pkg.engines.node);'`
Expected: `pnpm@11.21.0` and `>=24.0.0` printed clean.

- [ ] **Step 4: Commit**

```bash
git add package.json
git commit -m "chore(env): lock corepack pnpm and node engine versions"
```

---

### Task 2: Configure Turborepo Pipeline Caching (`turbo.json`)

**Files:**
- Create: `turbo.json`
- Modify: `package.json:8-18`

**Interfaces:**
- Consumes: NPM scripts (`build`, `lint`, `test`, `typecheck`).
- Produces: High-velocity cached pipeline execution for single-repo or monorepo workflows.

- [ ] **Step 1: Create failing validation test for turbo configuration**

Run: `test -f turbo.json`
Expected: FAIL (file does not exist yet)

- [ ] **Step 2: Create `turbo.json`**

Create `turbo.json` with:
```json
{
  "$schema": "https://turbo.build/schema.json",
  "tasks": {
    "build": {
      "dependsOn": ["^build"],
      "outputs": [".next/**", "!-next/cache/**", "dist/**"]
    },
    "lint": {
      "outputs": []
    },
    "typecheck": {
      "outputs": []
    },
    "test": {
      "outputs": []
    },
    "dev": {
      "cache": false,
      "persistent": true
    }
  }
}
```

- [ ] **Step 3: Update `package.json` scripts to wire `typecheck` and `turbo` orchestration**

In `package.json`, add `"typecheck": "tsc --noEmit"` to scripts.

- [ ] **Step 4: Verify test passes**

Run: `test -f turbo.json && node -e 'const pkg=require("./package.json"); if(!pkg.scripts.typecheck) process.exit(1);'`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add turbo.json package.json
git commit -m "feat(env): add Turborepo build pipeline configuration and typecheck script"
```

---

### Task 3: Enhance Master Makefile with Automated Pre-flight & Health Verification

**Files:**
- Modify: `Makefile:1-127`

**Interfaces:**
- Consumes: `pnpm`, `biome`, `tsc`, `vitest`, `gitleaks`, `antigravity-doctor.mjs`.
- Produces: One-word developer commands (`make check`, `make doctor`, `make typecheck`, `make db-start`).

- [ ] **Step 1: Write test for new Makefile targets**

Run: `make -n typecheck`
Expected: Outputs `tsc --noEmit` or equivalent recipe without errors.

- [ ] **Step 2: Update Makefile targets**

Update `Makefile` to align targets with `pnpm` execution:
```makefile
lint:
	@echo "🔍 Running Biome linter..."
	@pnpm run lint

format:
	@echo "🎨 Running Biome formatter..."
	@pnpm run format

typecheck:
	@echo "📐 Running TypeScript strict type checking..."
	@pnpm run typecheck

test:
	@echo "🧪 Running test suite..."
	@pnpm run test
```

- [ ] **Step 3: Run full pre-flight verification via Makefile**

Run: `make check`
Expected: Executing lint, format, typecheck, and security checks cleanly.

- [ ] **Step 4: Commit**

```bash
git add Makefile
git commit -m "chore(env): upgrade Makefile to delegate tasks via pnpm and turbo"
```

---

### Task 4: Verify Environment Readiness & Integration

**Files:**
- Modify: `STATUS.md`

**Interfaces:**
- Consumes: Updated project status and toolchain.
- Produces: Live verified status board.

- [ ] **Step 1: Run complete environment audit**

Run: `make check`
Expected: All verification steps pass cleanly.

- [ ] **Step 2: Update `STATUS.md`**

Mark environment upgrade items as complete in `STATUS.md`.

- [ ] **Step 3: Commit**

```bash
git add STATUS.md
git commit -m "docs(status): update workspace status to reflection upgraded enterprise environment"
```
