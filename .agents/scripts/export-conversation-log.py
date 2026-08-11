#!/usr/bin/env python3
"""
Conversation Log Exporter for AG Kit
Location: .agents/scripts/export-conversation-log.py

Parses system-generated transcript.jsonl logs and exports human-readable,
timestamped conversation records to .agents/logs/conversation_export.md
"""

import os
import sys
import json
import glob
from datetime import datetime

BRAIN_DIR = "/root/.gemini/antigravity-cli/brain"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")

def find_latest_transcript():
    if not os.path.exists(BRAIN_DIR):
        return None
    transcripts = glob.glob(os.path.join(BRAIN_DIR, "*", ".system_generated", "logs", "transcript.jsonl"))
    if not transcripts:
        return None
    # Sort by modification time
    transcripts.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return transcripts[0]

def export_transcript(transcript_path=None, output_path=None):
    if not transcript_path:
        transcript_path = find_latest_transcript()
        
    if not transcript_path or not os.path.exists(transcript_path):
        print("Error: No conversation transcript log found.")
        sys.exit(1)
        
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    if not output_path:
        timestamp_str = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = os.path.join(OUTPUT_DIR, f"conversation_{timestamp_str}.md")
        
    print(f"📖 Reading transcript from: {transcript_path}")
    
    entries = []
    with open(transcript_path, "r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    entries.append(json.loads(line))
                except Exception:
                    pass
                    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("# 📝 Complete Timestamped Conversation Log\n\n")
        f.write(f"- **Export Date**: {datetime.now().strftime('%Y-%m-%d %H:%M:%S UTC')}\n")
        f.write(f"- **Total Steps**: {len(entries)}\n")
        f.write(f"- **Source File**: `{transcript_path}`\n\n")
        f.write("---\n\n")
        
        for entry in entries:
            step_idx = entry.get("step_index", "?")
            created_at = entry.get("created_at", "N/A")
            step_type = entry.get("type", "UNKNOWN")
            source = entry.get("source", "UNKNOWN")
            content = entry.get("content", "")
            
            f.write(f"### Step {step_idx} | [{created_at}] ({step_type})\n")
            f.write(f"**Source**: `{source}`\n\n")
            
            if content:
                # Clean prompt tags if present
                clean_content = content.replace("<USER_REQUEST>", "").replace("</USER_REQUEST>", "")
                f.write(f"```text\n{clean_content.strip()}\n```\n\n")
            
            tool_calls = entry.get("tool_calls", [])
            if tool_calls:
                f.write("**Tool Executions**:\n")
                for tc in tool_calls:
                    name = tc.get("name", "tool")
                    args = json.dumps(tc.get("args", {}), indent=2)
                    f.write(f"- Tool `{name}`:\n```json\n{args}\n```\n")
            f.write("\n---\n\n")
            
    print(f"✅ Conversation log successfully exported to: {output_path}")

if __name__ == "__main__":
    export_transcript()
