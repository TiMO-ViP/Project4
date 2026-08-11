#!/usr/bin/env python3
"""
Atomic Real-Time Append-Only Live Session Logger for AG Kit
Location: .agents/scripts/live_session_logger.py

Maintains a crash-proof, append-only JSON Lines (.jsonl) file:
.agents/logs/live_session.jsonl

Features:
- Instant atomic append ('a' mode with os.fsync)
- Zero file rewrites / Zero data loss on sudden crashes or shutdown
- Real-time timestamping (ISO 8601 UTC)
"""

import os
import sys
import json
import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
LIVE_LOG_PATH = os.path.join(LOG_DIR, "live_session.jsonl")

def append_log_entry(role, content, tool_calls=None, metadata=None):
    os.makedirs(LOG_DIR, exist_ok=True)
    
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    
    entry = {
        "timestamp": now,
        "role": role,
        "content": content,
        "tool_calls": tool_calls or [],
        "metadata": metadata or {}
    }
    
    # Atomic line append with immediate physical disk sync (os.fsync)
    with open(LIVE_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())
        
    print(json.dumps({"status": "appended_atomic", "timestamp": now, "role": role}))

def read_live_log(limit=20):
    if not os.path.exists(LIVE_LOG_PATH):
        print(json.dumps({"status": "empty", "entries": []}))
        return
        
    entries = []
    with open(LIVE_LOG_PATH, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
                    
    recent = entries[-limit:] if limit > 0 else entries
    print(json.dumps({"total": len(entries), "shown": len(recent), "entries": recent}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: live_session_logger.py [append <user|assistant> <content> [tool_calls_json] | read [limit]]")
        sys.exit(1)
        
    cmd = sys.argv[1]
    if cmd == "append" and len(sys.argv) >= 4:
        role = sys.argv[2]
        content = sys.argv[3]
        tools = json.loads(sys.argv[4]) if len(sys.argv) > 4 else None
        append_log_entry(role, content, tools)
    elif cmd == "read":
        limit = int(sys.argv[2]) if len(sys.argv) > 2 else 20
        read_live_log(limit)
    else:
        print("Invalid arguments.")
