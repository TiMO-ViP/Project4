# 🗄️ Database Architecture & Schema Documentation

> Comprehensive guide for PostgreSQL, Drizzle ORM, Supabase Cloud & Local, Row-Level Security (RLS), and Modular ERP Table Conventions.

---

## 🏛️ Database Topology Overview

```mermaid
erDiagram
    USERS ||--o{ SALES_ORDERS : places
    USERS {
        varchar_64 id PK
        varchar_255 email UK
        text name
        varchar_32 role
        timestamp created_at
        timestamp updated_at
    }
    SALES_ORDERS {
        varchar_64 id PK
        varchar_64 user_id FK
        numeric total_amount
        varchar_32 status
        timestamp created_at
    }
```

---

## ⚙️ Environment Isolation Architecture

To guarantee **Local-First Database Safety**, database connections are strictly isolated:

* **Local Development (Default)**:
  * **Target**: Local Docker / Supabase Postgres container
  * **URL**: `postgresql://postgres:postgres@127.0.0.1:54322/postgres`
  * **Studio GUI**: `http://127.0.0.1:54323` (Supabase Studio)
  * **CLI Target**: `make db-push-local` (`DB_TARGET=local npx drizzle-kit push`)

* **Cloud Production**:
  * **Target**: Supabase Cloud Project `awtuyagramircsbjnjzy` (EU Central 1 Region)
  * **URL**: Configured via `SUPABASE_CLOUD_DATABASE_URL` in `.env`
  * **CLI Target**: `make db-push-cloud` (`DB_TARGET=cloud npx drizzle-kit push`)

---

## 📊 Table Specifications

### 1. `users` Table ([src/db/schema.ts](file:///storage/emulated/0/projector/project4/src/db/schema.ts))

| Column | Type | Constraints | Default | Description |
| :--- | :--- | :--- | :--- | :--- |
| `id` | `varchar(64)` | `PRIMARY KEY` | — | Unique user identifier |
| `email` | `varchar(255)` | `NOT NULL`, `UNIQUE` | — | User email address |
| `name` | `text` | `NOT NULL` | — | Full display name |
| `role` | `varchar(32)` | `NOT NULL` | `'user'` | Access role (`admin`, `user`, `guest`) |
| `created_at` | `timestamp` | `NOT NULL` | `now()` | Record creation timestamp |
| `updated_at` | `timestamp` | `NOT NULL` | `now()` | Record last modification timestamp |

#### B-Tree Index Strategy
* `idx_users_email` ON `users(email)` — Fast lookups for authentication & queries.
* `idx_users_role` ON `users(role)` — Fast filtering by permission tier.

---

## 🔒 Row-Level Security (RLS) Policy Specification

All exposed tables in `public` enforce strict RLS policies ([supabase/migrations/20260812000000_create_users_rls.sql](file:///storage/emulated/0/projector/project4/supabase/migrations/20260812000000_create_users_rls.sql)):

```sql
-- Enable RLS
ALTER TABLE public.users ENABLE ROW LEVEL SECURITY;

-- 1. SELECT Policy (Owner Access)
CREATE POLICY "users_select_own_profile"
ON public.users FOR SELECT TO authenticated
USING ( (select auth.uid())::text = id );

-- 2. INSERT Policy (Owner Insert)
CREATE POLICY "users_insert_own_profile"
ON public.users FOR INSERT TO authenticated
WITH CHECK ( (select auth.uid())::text = id );

-- 3. UPDATE Policy (Owner Update with Hijack Protection)
CREATE POLICY "users_update_own_profile"
ON public.users FOR UPDATE TO authenticated
USING ( (select auth.uid())::text = id )
WITH CHECK ( (select auth.uid())::text = id );
```

---

## 🏬 Modular ERP Table Naming Standard

For future enterprise module extensions, tables follow standard domain prefix conventions:

| Domain Module | Table Prefix | Example Table Names |
| :--- | :--- | :--- |
| **CRM** | `crm_` | `crm_contacts`, `crm_deals`, `crm_leads` |
| **Inventory** | `inv_` | `inv_products`, `inv_stock_levels`, `inv_warehouses` |
| **Accounting** | `acc_` | `acc_invoices`, `acc_ledger_entries`, `acc_taxes` |
| **HR** | `hr_` | `hr_employees`, `hr_departments`, `hr_payrolls` |
| **Supply Chain** | `scm_` | `scm_suppliers`, `scm_purchase_orders` |
| **Sales** | `sales_` | `sales_orders`, `sales_quotations` |
