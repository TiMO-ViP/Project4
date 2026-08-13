# 🗄️ Database Migration & Deployment Guide

> **Production Operator Documentation for Project4**

---

## 📌 Overview

This document outlines version-controlled database schema migration procedures using **Supabase CLI** and **Drizzle ORM**, adhering to **NIST SP 800-218 (SSDF)** deployment safety standards.

---

## ⚡ Local Database Workflow

1. **Start Local Supabase Environment**:
   ```bash
   make db-start
   ```
   *Launches local PostgreSQL 17, Auth, Storage, and Studio GUI.*

2. **Generate SQL Migrations from Drizzle Schema**:
   ```bash
   pnpm exec drizzle-kit generate
   ```
   *Generates version-controlled SQL files in `supabase/migrations/`.*

3. **Apply Local Migrations**:
   ```bash
   make db-push-local
   ```

---

## 🚀 Cloud Migration Deployment

1. **Verify Pre-Flight Audit**:
   ```bash
   make check
   ```

2. **Deploy Migrations to Supabase Production**:
   ```bash
   make db-push-cloud
   ```

---

## 🔒 Security & Rollback Protocol

* **Row Level Security (RLS)**: Every new table MUST enable RLS policies (`ALTER TABLE ... ENABLE ROW LEVEL SECURITY;`).
* **Indexes**: Enforce B-tree indexing on foreign key columns (`user_id`, `org_id`).
* **Rollback Plan**: Test database rollbacks in local environment before deploying to cloud production.
