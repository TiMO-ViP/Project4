#!/usr/bin/env python3
"""
Enterprise Single-File & Rotating Conversation Log Engine for AG Kit
Location: .agents/scripts/export-conversation-log.py

Maintains a SINGLE master continuous Markdown log file (.agents/logs/CURRENT_SESSION.md)
so your workspace never fills up with redundant files.
Also provides direct keyword search over transcript logs.
"""

import os
import sys
import json
import glob
import re
from datetime import datetime

BRAIN_DIR = "/root/.gemini/antigravity-cli/brain"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")
MASTER_LOG_PATH = os.path.join(OUTPUT_DIR, "CURRENT_SESSION.md")

def find_latest_transcript():
    if not os.path.exists(BRAIN_DIR):
        return None
    transcripts = glob.glob(os.path.join(BRAIN_DIR, "*", ".system_generated", "logs", "transcript.jsonl"))
    if not transcripts:
        return None
    transcripts.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return transcripts[0]

def cleanup_old_exports(max_files=3):
    """Auto-prunes old timestamped export files so disk space remains clean."""
    files = glob.glob(os.path.join(OUTPUT_DIR, "conversation_*.md"))
    if len(files) > max_files:
        files.sort(key=lambda x: os.path.getmtime(x))
        for f in files[:-max_files]:
            try:
                os.remove(f)
            except Exception:
                pass

def export_transcript(transcript_path=None, output_path=MASTER_LOG_PATH):
    if not transcript_path:
        transcript_path = find_latest_transcript()
        
    if not transcript_path or not os.path.exists(transcript_path):
        print("Error: No conversation transcript log found.")
        sys.exit(1)
        
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    cleanup_old_exports(max_files=3)
    
    entries = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
                    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 📝 Master Conversation Log (Continuous Session)\n\n")
        f.write(f"- **Last Updated**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"- **Total Conversation Turns**: {len(entries)}\n")
        f.write(f"- **Transcript Source**: `{transcript_path}`\n\n")
        f.write("> 💡 *This single master file updates in-place so your repository never clutters.* \n\n")
        f.write("---\n\n")
        
        for entry in entries:
            step_idx = entry.get("step_index", "?")
            created_at = entry.get("created_at", "N/A")
            step_type = entry.get("type", "UNKNOWN")
            source = entry.get("source", "UNKNOWN")
            content = entry.get("content", "")
            
            f.write(f"### Turn {step_idx} | [{created_at}] ({step_type})\n")
            f.write(f"**Source**: `{source}`\n\n")
            
            if content:
                clean_content = content.replace("<USER_REQUEST>", "").replace("</USER_REQUEST>", "")
                clean_content = re.sub(r'<ADDITIONAL_METADATA>.*?</ADDITIONAL_METADATA>', '', clean_content, flags=re.DOTALL)
                clean_content = re.sub(r'<USER_SETTINGS_CHANGE>.*?</USER_SETTINGS_CHANGE>', '', clean_content, flags=re.DOTALL)
                f.write(f"```text\n{clean_content.strip()}\n```\n\n")
            
            tool_calls = entry.get("tool_calls", [])
            if tool_calls:
                f.write("**Tool Executions**:\n")
                for tc in tool_calls:
                    name = tc.get("name", "tool")
                    args_summary = json.dumps(tc.get("args", {}), indent=2)
                    if len(args_summary) > 500:
                        args_summary = args_summary[:500] + "\n  ... [truncated for readability]"
                    f.write(f"- Tool `{name}`:\n```json\n{args_summary}\n```\n")
            f.write("\n---\n\n")
            
    print(f"✅ Single Master Log updated: {output_path}")

def search_transcript(query):
    transcript_path = find_latest_transcript()
    if not transcript_path or not os.path.exists(transcript_path):
        print("Error: No transcript log found.")
        return
        
    results = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if query.lower() in line.lower():
                try:
                    data = json.loads(line)
                    results.append({
                        "step": data.get("step_index"),
                        "time": data.get("created_at"),
                        "type": data.get("type"),
                        "snippet": data.get("content", "")[:200]
                    })
                except Exception:
                    pass
                    
    print(json.dumps({"query": query, "count": len(results), "matches": results}, indent=2))

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "search" and len(sys.argv) > 2:
        search_transcript(sys.argv[2])
    else:
        export_transcript()
