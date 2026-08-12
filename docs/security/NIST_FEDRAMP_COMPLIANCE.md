# Government-Grade Security & Compliance Specification

> Security governance standards for Project4 aligned with NIST SP 800-218 (Secure Software Development Framework - SSDF) and FedRAMP Moderate/High requirements.

---

## 🛡️ 4 SSDF Security Pillar Execution

### 1. Prepare the Organization (PO)
* **Configuration Management**: Immutable configuration defined in `package.json`, `tsconfig.json`, `biome.json`, and `drizzle.config.ts`.
* **Environment Isolation**: Local secrets (`.env`) are strictly isolated from source code via `.gitignore` and enforced by Gitleaks pre-commit hooks.

### 2. Protect Software (PS)
* **Dependency Provenance**: Automated lockfile verification (`package-lock.json`, `skills-lock.json`).
* **Secret Leak Prevention**: Gitleaks security scanners configured in `.gitleaks.toml` and GitHub Actions CI pipelines.

### 3. Produce Well-Secured Software (PW)
* **Zero-Trust Server Actions**: All Next.js Server Actions verify user authentication (`await supabase.auth.getUser()`) and sanitize inputs via Zod.
* **Database Row-Level Security (RLS)**: 100% of PostgreSQL tables have RLS enabled with indexed `auth.uid() = user_id` B-tree queries.

### 4. Respond to Vulnerabilities (RV)
* **Live Version Audits**: Mandatory `make version-audit` commands and automated dependency audits.
