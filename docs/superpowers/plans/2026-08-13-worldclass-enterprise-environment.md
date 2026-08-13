# World-Class Enterprise Environment Upgrade Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Transform the local workspace into a 2026 world-class enterprise development environment with automated Release-Please versioning, CycloneDX SBOM supply-chain generation, OIDC/DevContainer prebuilding, and zero-trust pre-flight security gates.

**Architecture:** We will implement an automated CycloneDX SBOM generator script, configure Google `release-please` for automated semver releases and CHANGELOG maintenance, update `.devcontainer/devcontainer.json` for 1-click workspace provisioning, and wire all security/verification targets into `Makefile` and GitHub Actions CI/CD pipelines.

**Tech Stack:** Node.js v24.19, pnpm v11.21, Python 3.14, CycloneDX 1.6, Release-Please, DevContainers, Gitleaks, GitHub Actions OIDC.

## Global Constraints

- Strict English terminal output.
- Always-Latest Package Protocol (`npm info`, `context7`).
- Local-First Database Strategy (`make db-start`, `make db-push`).
- No unrequested application business logic.
- 100% testable execution.

---

### Task 1: Add CycloneDX SBOM Generator Script

**Files:**
- Create: `.agents/scripts/generate-sbom.py`
- Test: Executing `python3 .agents/scripts/generate-sbom.py`

**Interfaces:**
- Consumes: `package.json`, `Cargo.toml`, `pyproject.toml`.
- Produces: `sbom.cdx.json` (CycloneDX 1.6 specification format).

- [ ] **Step 1: Write test for SBOM generation**

Run: `python3 .agents/scripts/generate-sbom.py && test -f sbom.cdx.json`
Expected: FAIL (script does not exist yet)

- [ ] **Step 2: Create `.agents/scripts/generate-sbom.py`**

Create `.agents/scripts/generate-sbom.py` with standard CycloneDX schema output.

- [ ] **Step 3: Run SBOM generator and verify schema**

Run: `python3 .agents/scripts/generate-sbom.py && grep -q "cyclonedx" sbom.cdx.json`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add .agents/scripts/generate-sbom.py sbom.cdx.json
git commit -m "feat(security): add CycloneDX SBOM generator script and initial inventory"
```

---

### Task 2: Configure Release-Please for Automated Changelog & SemVer

**Files:**
- Create: `.github/release-please-config.json`
- Create: `.github/.release-please-manifest.json`
- Create: `.github/workflows/release.yml`

**Interfaces:**
- Consumes: Conventional Commits on `main` branch.
- Produces: Automated Release PRs, CHANGELOG updates, and GitHub Release tags.

- [ ] **Step 1: Create failing test for release-please configuration**

Run: `test -f .github/release-please-config.json`
Expected: FAIL (file does not exist yet)

- [ ] **Step 2: Create Release-Please configuration and manifest**

Create `.github/release-please-config.json` and `.github/.release-please-manifest.json`.

- [ ] **Step 3: Create GitHub Actions release workflow `.github/workflows/release.yml`**

Define scoped permissions (`permissions: contents: write, pull-requests: write`).

- [ ] **Step 4: Run JSON schema validation**

Run: `node -e 'require("./.github/release-please-config.json"); require("./.github/.release-please-manifest.json");'`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add .github/release-please-config.json .github/.release-please-manifest.json .github/workflows/release.yml
git commit -m "ci(release): add release-please workflow and semver configuration"
```

---

### Task 3: Upgrade DevContainer for Enterprise 1-Click Provisioning

**Files:**
- Modify: `.devcontainer/devcontainer.json`

**Interfaces:**
- Consumes: Docker & VS Code DevContainer spec.
- Produces: Zero-configuration development environment with pre-installed extensions and hooks.

- [ ] **Step 1: Test existing devcontainer configuration**

Run: `node -e 'require("./.devcontainer/devcontainer.json");'`
Expected: PASS or check fields

- [ ] **Step 2: Enhance `.devcontainer/devcontainer.json`**

Update `.devcontainer/devcontainer.json` to include postCreateCommand: `make setup-hooks`, Biome, TypeScript, and Supabase VS Code extensions.

- [ ] **Step 3: Verify JSON validity**

Run: `node -e 'JSON.parse(require("fs").readFileSync("./.devcontainer/devcontainer.json", "utf-8"));'`
Expected: PASS

- [ ] **Step 4: Commit**

```bash
git add .devcontainer/devcontainer.json
git commit -m "chore(devcontainer): upgrade devcontainer spec with automated hook initialization"
```

---

### Task 4: Integrate SBOM Target & Full Verification Suite in Makefile

**Files:**
- Modify: `Makefile`
- Modify: `STATUS.md`

**Interfaces:**
- Consumes: All verification targets (`sbom`, `security`, `lint`, `format`, `typecheck`, `test`).
- Produces: `make sbom` and unified `make check`.

- [ ] **Step 1: Test `make sbom` recipe**

Run: `make sbom`
Expected: Generates `sbom.cdx.json` cleanly.

- [ ] **Step 2: Update `Makefile` and `STATUS.md`**

Add `sbom` target to `Makefile` and update status board in `STATUS.md`.

- [ ] **Step 3: Run full pre-flight verification**

Run: `make check`
Expected: 100% clean execution.

- [ ] **Step 4: Commit**

```bash
git add Makefile STATUS.md
git commit -m "docs(status): complete world-class enterprise environment upgrade"
```
