#!/usr/bin/env python3
"""
Full Verbatim Conversation Logger for AG Kit
Location: .agents/scripts/live_session_logger.py

Extracts 100% full verbatim copy-and-paste text of all user inputs
and assistant Markdown responses directly from system transcript logs.
"""

import os
import sys
import json
import glob
import re

BRAIN_DIR = "/root/.gemini/antigravity-cli/brain"
LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
LIVE_LOG_PATH = os.path.join(LOG_DIR, "live_session.jsonl")

def find_latest_transcript_full():
    if not os.path.exists(BRAIN_DIR):
        return None
    transcripts = glob.glob(os.path.join(BRAIN_DIR, "*", ".system_generated", "logs", "transcript_full.jsonl"))
    if not transcripts:
        return None
    transcripts.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return transcripts[0]

def sync_full_conversation_logs():
    """Syncs 100% full verbatim text to live_session.jsonl."""
    transcript_path = find_latest_transcript_full()
    if not transcript_path or not os.path.exists(transcript_path):
        return
        
    os.makedirs(LOG_DIR, exist_ok=True)
    
    full_turns = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    data = json.loads(line)
                    ttype = data.get("type")
                    content = data.get("content", "")
                    
                    if content and ttype in ("USER_INPUT", "PLANNER_RESPONSE"):
                        # Clean system prompt wrapper tags if present
                        clean_content = re.sub(r'<USER_REQUEST>\s*', '', content)
                        clean_content = re.sub(r'\s*</USER_REQUEST>', '', clean_content)
                        clean_content = re.sub(r'<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>', '', clean_content, flags=re.DOTALL)
                        clean_content = re.sub(r'<USER_SETTINGS_CHANGE>.*?</USER_SETTINGS_CHANGE>', '', clean_content, flags=re.DOTALL)
                        clean_content = clean_content.strip()
                        
                        if clean_content and not clean_content.startswith("Created At:"):
                            role = "user" if ttype == "USER_INPUT" else "assistant"
                            full_turns.append({
                                "step": data.get("step_index"),
                                "timestamp": data.get("created_at"),
                                "role": role,
                                "verbatim_text": clean_content
                            })
                except Exception:
                    pass
                    
    with open(LIVE_LOG_PATH, "w", encoding="utf-8") as f:
        for turn in full_turns:
            f.write(json.dumps(turn, ensure_ascii=False) + "\n")
            
    return full_turns

def read_full_log(limit=4):
    turns = sync_full_conversation_logs() or []
    recent = turns[-limit:] if limit > 0 else turns
    print(json.dumps({"total_text_turns": len(turns), "shown": len(recent), "turns": recent}, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    limit = int(sys.argv[2]) if len(sys.argv) > 2 else 4
    read_full_log(limit)
