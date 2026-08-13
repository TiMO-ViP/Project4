#!/usr/bin/env python3
"""
Enterprise Automated Git Commit & Audit Engine (AG Kit)
Location: .agents/scripts/auto_commit_on_edit.py

Features:
- Automatic stale Git lockfile detection and recovery (.git/*.lock).
- Atomic change categorization (code, docs, config grouped separately).
- FUSE/PRoot storage compatibility (silences ignoredHook warnings).
- Machine audit trail via `git notes --ref=ai-audit`.
- Continuous background polling daemon with zero resource churn.
"""

import os
import sys
import subprocess
import time
import json
from datetime import datetime, timezone

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

def run_cmd(cmd, cwd=PROJECT_ROOT):
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    return result.returncode, result.stdout.strip(), result.stderr.strip()

def cleanup_stale_locks():
    git_dir = os.path.join(PROJECT_ROOT, ".git")
    if not os.path.exists(git_dir):
        return
    for lock in ["index.lock", "config.lock", "HEAD.lock"]:
        lock_path = os.path.join(git_dir, lock)
        if os.path.exists(lock_path):
            try:
                mtime = os.path.getmtime(lock_path)
                if (time.time() - mtime) > 3.0:  # Lock older than 3s
                    os.remove(lock_path)
                    print(f"🧹 Cleaned stale git lock: {lock}")
            except Exception:
                pass

def configure_git_environment():
    cleanup_stale_locks()
    run_cmd("git config advice.ignoredHook false")
    run_cmd("git config core.hooksPath .githooks")

def get_modified_files():
    cleanup_stale_locks()
    code, out, _ = run_cmd("git status --porcelain")
    if code != 0 or not out:
        return []
    
    files = []
    for line in out.splitlines():
        line = line.strip()
        if not line:
            continue
        parts = line.split(maxsplit=1)
        if len(parts) == 2:
            status, path = parts[0], parts[1]
            # Ignore internal superpowers scratch directories
            if path.startswith(".superpowers/") or path.startswith(".cache/"):
                continue
            files.append((status, path))
    return files

def categorize_files(files):
    groups = {
        "code": [],
        "docs": [],
        "config": []
    }
    for status, path in files:
        if path.endswith(".md") or path.startswith("docs/"):
            groups["docs"].append(path)
        elif path.startswith(".github/") or path in ["Makefile", "package.json", "package-lock.json", "turbo.json", ".gitignore", ".npmrc", "pnpm-lock.yaml", "Cargo.toml", "pyproject.toml"]:
            groups["config"].append(path)
        else:
            groups["code"].append(path)
    return groups

def commit_group(group_name, paths):
    if not paths:
        return True

    cleanup_stale_locks()
    # Stage specific files
    for p in paths:
        run_cmd(f'git add "{p}"')

    # Security pre-commit audit
    code, out, err = run_cmd("bash .githooks/pre-commit")
    if code != 0:
        print(f"❌ Security audit blocked commit for {group_name}:\n{err or out}")
        return False

    # Generate Conventional Commit message
    code, msg, _ = run_cmd("bash .agents/scripts/git-auto-commit-msg.sh")
    if code != 0 or not msg:
        if group_name == "docs":
            msg = f"docs(workspace): update documentation ({len(paths)} file(s))"
        elif group_name == "config":
            msg = f"chore(env): update build configuration and dependencies ({len(paths)} file(s))"
        else:
            msg = f"feat(workspace): auto-commit verified code changes ({len(paths)} file(s))"

    safe_msg = msg.replace('"', '\\"')
    commit_res, c_out, c_err = run_cmd(f'git commit -m "{safe_msg}"')
    if commit_res == 0:
        # Get head hash
        _, head_hash, _ = run_cmd("git rev-parse HEAD")
        print(f"✅ Auto-commit [{group_name}] succeeded! ({head_hash[:7]})")
        
        # Attach machine audit metadata via git notes
        audit_meta = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "auto_commit": True,
            "group": group_name,
            "file_count": len(paths),
            "files": paths
        }
        meta_str = json.dumps(audit_meta).replace('"', '\\"')
        run_cmd(f'git notes --ref=ai-audit add -f -m "{meta_str}" {head_hash}')
        return True
    else:
        print(f"⚠️ Auto-commit [{group_name}] skipped or failed: {c_err or c_out}")
        return False

def auto_commit_all():
    configure_git_environment()
    files = get_modified_files()
    if not files:
        print("ℹ️ No uncommitted workspace changes detected.")
        return True

    groups = categorize_files(files)
    success = True
    for group_name in ["code", "docs", "config"]:
        if groups[group_name]:
            res = commit_group(group_name, groups[group_name])
            if not res:
                success = False

    if success:
        # Export conversation logs
        run_cmd("python3 .agents/scripts/live_session_logger.py read 5")
        run_cmd("python3 .agents/scripts/export-conversation-log.py")
    return success

def watch_loop(interval=5):
    configure_git_environment()
    print(f"🚀 Enterprise Auto-Commit Watcher active (polling every {interval}s). Press Ctrl+C to stop.")
    try:
        while True:
            files = get_modified_files()
            if files:
                print(f"\n⚡ Detected {len(files)} modified file(s)! Running atomic auto-commit pipeline...")
                auto_commit_all()
            time.sleep(interval)
    except KeyboardInterrupt:
        print("\n👋 Auto-Commit Watcher stopped.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "watch":
        interval = int(sys.argv[2]) if len(sys.argv) > 2 else 5
        watch_loop(interval)
    else:
        auto_commit_all()
