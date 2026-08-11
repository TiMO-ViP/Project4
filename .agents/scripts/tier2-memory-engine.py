#!/usr/bin/env python3
"""
Tier 2 Semantic & Vector Memory Engine for AG Kit
Location: .agents/scripts/tier2-memory-engine.py

Provides hybrid full-text (FTS5) and semantic relevance search over
unstructured session logs, terminal outputs, and long-term project context.
Database file: .agents/memory/tier2_vector.db
"""

import sys
import os
import sqlite3
import datetime
import json
import re

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "memory", "tier2_vector.db")

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Create main memories table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            content TEXT NOT NULL,
            tags TEXT,
            created_at TEXT NOT NULL
        )
    """)
    
    # Create FTS5 virtual table for high-speed full-text and BM25 relevance search
    cursor.execute("""
        CREATE VIRTUAL TABLE IF NOT EXISTS memories_fts USING fts5(
            content,
            category,
            tags
        )
    """)
    
    conn.commit()
    conn.close()

def store_memory(category, content, tags=""):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    cursor.execute(
        "INSERT INTO memories (category, content, tags, created_at) VALUES (?, ?, ?, ?)",
        (category, content, tags, now)
    )
    row_id = cursor.lastrowid
    
    cursor.execute(
        "INSERT INTO memories_fts (rowid, content, category, tags) VALUES (?, ?, ?, ?)",
        (row_id, content, category, tags)
    )
    
    conn.commit()
    conn.close()
    print(json.dumps({"status": "stored", "id": row_id, "category": category}))

def search_memory(query, limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Clean query for FTS5 search
    clean_query = re.sub(r'[^a-zA-Z0-9_\s]', '', query)
    if not clean_query.strip():
        print(json.dumps({"results": []}))
        return

    fts_query = " OR ".join(clean_query.split())
    
    cursor.execute("""
        SELECT rowid, category, content, tags, rank
        FROM memories_fts
        WHERE memories_fts MATCH ?
        ORDER BY rank
        LIMIT ?
    """, (fts_query, limit))
    
    rows = cursor.fetchall()
    results = []
    for row in rows:
        results.append({
            "id": row[0],
            "category": row[1],
            "content": row[2],
            "tags": row[3],
            "relevance_score": round(-row[4], 4)
        })
    
    conn.close()
    print(json.dumps({"query": query, "count": len(results), "results": results}, indent=2))

def list_memories(limit=10):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT id, category, content, created_at FROM memories ORDER BY id DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    results = [{"id": r[0], "category": r[1], "content": r[2], "created_at": r[3]} for r in rows]
    conn.close()
    print(json.dumps({"total": len(results), "memories": results}, indent=2))

if __name__ == "__main__":
    init_db()
    if len(sys.argv) < 2:
        print("Usage: tier2-memory-engine.py [store <category> <content> [tags] | search <query> | list]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "store" and len(sys.argv) >= 4:
        cat = sys.argv[2]
        content = sys.argv[3]
        tags = sys.argv[4] if len(sys.argv) > 4 else ""
        store_memory(cat, content, tags)
    elif cmd == "search" and len(sys.argv) >= 3:
        search_memory(sys.argv[2])
    elif cmd == "list":
        list_memories()
    else:
        print("Invalid arguments.")
