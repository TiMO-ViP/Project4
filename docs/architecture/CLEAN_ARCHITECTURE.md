# Government-Grade Enterprise Clean Architecture Blueprint

> Structural specification and dependency direction rules for Project4 based on NIST SP 800-218 (SSDF) and FedRAMP enterprise standards.

---

## 🏛️ Layer Topology & Dependency Graph

```text
 [Presentation Layer]          [Next.js 16 App Router (src/app/) + Features (src/features/)]
         │
         ▼
 [Application Layer]           [Use Cases & Services (src/application/)]
         │
         ▼
 [Domain Layer (Core)]         [Entities & Contracts (src/domain/)] (ZERO DEPENDENCIES)
         ▲
         │ (Implements Contracts)
 [Infrastructure Layer]        [Database / Supabase / APIs (src/infrastructure/)]
```

---

## 📁 Directory Responsibilities

| Directory | Layer | Strict Rules & Responsibilities |
| :--- | :--- | :--- |
| **`src/domain/`** | **Core Domain** | **Zero Framework Dependencies**. Contains pure TypeScript Entities (`User`, `Tenant`) and Repository Interfaces (`UserRepository`). |
| **`src/application/`** | **Use Cases** | Implements application workflows (`createUserUseCase.ts`). Depends ONLY on Domain interfaces. |
| **`src/infrastructure/`** | **Adapters** | Implements Domain contracts using concrete tools (**Drizzle ORM**, **Supabase Client**, **Redis**). |
| **`src/features/`** | **Feature Modules** | Self-contained domain UI components and hooks (`src/features/auth/`). |
| **`src/app/`** | **App Router** | Thin routing layer (`page.tsx`, `layout.tsx`, `proxy.ts`). Calls Application Use Cases. |
| **`docs/adr/`** | **Governance** | Architecture Decision Records (ADRs) tracking structural technical decisions. |
| **`tests/`** | **Quality Control** | AAA pattern test suites (`unit/`, `integration/`, `e2e/`). |
| **`deploy/`** | **Ops / IaC** | Container definitions (`Dockerfile`) and CI/CD pipelines. |
