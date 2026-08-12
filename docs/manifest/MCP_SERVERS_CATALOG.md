# Model Context Protocol (MCP) Servers Catalog

> Comprehensive guide and operational reference for all Model Context Protocol (MCP) servers configured in Project4 (`.agents/mcp_config.json`).

---

## ⚡ Configured MCP Servers Overview

```text
                                  [.agents/mcp_config.json]
                                              │
 ┌─────────────┬─────────────┬────────────────┼────────────────┬─────────────┬─────────────┐
 ▼             ▼             ▼                ▼                ▼             ▼             ▼
[Supabase]   [SQLite]     [PostgreSQL]     [MongoDB]       [Context7]     [Memory]     [Filesystem/Git]
Remote BaaS  Local Vector DSN Relational   NoSQL Document  Live Docs      FTS Graph    Workspace IO
```

---

## 📋 MCP Servers Reference Matrix

| MCP Server | Server Type / Target | Command / Endpoint | Description & Capabilities |
| :--- | :--- | :--- | :--- |
| **`supabase`** | Remote Managed Endpoint | `https://mcp.supabase.com/mcp?project_ref=awtuyagramircsbjnjzy...` | Official Supabase server. Inspects PostgreSQL schemas, Auth policies, Storage buckets, and Edge Functions. |
| **`context7`** | Live Docs Engine | `npx -y @upstash/context7-mcp` | Up-to-date live documentation search engine for Supabase, Drizzle, React, and TypeScript. |
| **`sqlite`** | Embedded DB | `npx -y @modelcontextprotocol/server-sqlite` | Local SQLite database inspector for `.agents/memory/tier2_vector.db`. |
| **`memory`** | Persistent Memory | `npx -y @modelcontextprotocol/server-memory` | Knowledge graph entity and relation memory engine for cross-session storage. |
| **`fetch`** | Web Fetcher | `npx -y @modelcontextprotocol/server-fetch` | Asynchronous web page scraper and markdown content extractor. |
| **`filesystem`** | Workspace IO | `npx -y @modelcontextprotocol/server-filesystem` | Local file system reader/writer restricted to `/storage/emulated/0/projector/project4`. |
| **`git`** | Version Control | `npx -y @modelcontextprotocol/server-git` | Git repository inspector for commits, diffs, branches, and worktrees. |
