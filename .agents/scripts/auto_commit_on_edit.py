#!/usr/bin/env python3
"""
Automated Git Commit on Edit Engine (AG Kit)
Location: .agents/scripts/auto_commit_on_edit.py

Monitors git workspace status, executes security pre-commit validation,
and automatically creates conventional commits upon code edits.
"""

import os
import sys
import subprocess
import time

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def run_cmd(cmd, cwd=PROJECT_ROOT):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def check_uncommitted_changes():
    code, out, _ = run_cmd("git status --porcelain")
    if code == 0 and out:
        return True, out
    return False, ""

def auto_commit():
    has_changes, changes = check_uncommitted_changes()
    if not has_changes:
        print("ℹ️ No uncommitted changes detected in workspace.")
        return True

    print("🔍 Staging workspace modifications...")
    run_cmd("git add -A")

    print("🔒 Running security pre-commit audit...")
    code, out, err = run_cmd("bash .githooks/pre-commit")
    if code != 0:
        print(f"❌ Security audit blocked commit:\n{err or out}")
        return False

    print("📝 Generating deterministic Conventional Commit...")
    code, msg, _ = run_cmd("bash .agents/scripts/git-auto-commit-msg.sh")
    if code != 0 or not msg:
        msg = "chore(workspace): auto-commit verified changes"

    # Escape quotes for safety
    safe_msg = msg.replace('"', '\\"')
    commit_res, c_out, c_err = run_cmd(f'git commit -m "{safe_msg}"')
    if commit_res == 0:
        print(f"✅ Auto-commit succeeded!\n{c_out}")

        # Also sync live session log
        run_cmd("python3 .agents/scripts/live_session_logger.py read 5")
        run_cmd("python3 .agents/scripts/export-conversation-log.py")
        return True
    else:
        print(f"⚠️ Commit skipped or failed: {c_err or c_out}")
        return False

def watch_loop(interval=10):
    print(f"🚀 Auto-Commit Watcher active (checking every {interval}s). Press Ctrl+C to stop.")
    try:
        while True:
            has_changes, _ = check_uncommitted_changes()
            if has_changes:
                print("\n⚡ Code edits detected! Executing automated commit flow...")
                auto_commit()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n👋 Auto-Commit Watcher stopped.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 10
        watch_loop(interval)
    else:
        auto_commit()
