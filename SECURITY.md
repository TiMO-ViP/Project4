# Security Policy

> Vulnerability reporting guidelines and security standards for Project4.

---

## 🛡️ Reporting Vulnerabilities

If you discover a potential security vulnerability within this repository or application, please **DO NOT** create a public GitHub Issue.

Instead, report security concerns directly via private disclosure:
* **Security Contact**: `security@project4.local` / GitHub Private Vulnerability Reporting
* **Response SLA**: Initial triage within 24 hours.

---

## 🔒 Security Standards & Automated Controls

1. **Zero Secret Policy**:
   Plaintext secrets, API keys, private keys (`.pem`), and database passwords MUST NEVER be committed to version control. All local secrets live in `.env` (excluded by `.gitignore`).
2. **Automated Secret Scanning**:
   Pre-commit hook (`.githooks/pre-commit`) and Gitleaks (`.gitleaks.toml`) scan every commit for secret patterns prior to pushing.
3. **Row-Level Security (RLS)**:
   100% of PostgreSQL tables in Supabase must have Row Level Security enabled with indexed policy checks (`auth.uid() = user_id`).
4. **Server Actions Security**:
   All Next.js Server Actions verify user authentication (`await supabase.auth.getUser()`) and sanitize inputs via Zod schemas.
