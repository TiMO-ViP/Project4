#!/usr/bin/env python3
"""
Live File Manifest & Cryptographic Signature Generator (AG Kit)
Location: .agents/scripts/generate-live-manifest.py

Scans all files and directories in the repository (excluding node_modules, .git, .cache, docs/manifest),
computes line counts, byte sizes, and SHA-256 checksums, and produces a timestamped
master file manifest at `docs/manifest/LIVE_FILE_MANIFEST.md`.
"""

import os
import sys
import hashlib
from datetime import datetime, timezone

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))

EXCLUDE_DIRS = {
    "node_modules",
    ".git",
    ".cache",
    ".next",
    ".turbo",
    "dist",
    "build",
    "tmp",
    ".superpowers",
    "docs/manifest"
}

BINARY_EXTENSIONS = {
    ".db", ".sqlite", ".png", ".jpg", ".jpeg", ".gif", ".ico", ".woff", ".woff2", ".ttf", ".eot", ".zip", ".tar", ".gz"
}

def compute_sha256(file_path):
    h = hashlib.sha256()
    with open(file_path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

def count_lines(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    if ext in BINARY_EXTENSIONS:
        return 0
    try:
        with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
            return sum(1 for _ in f)
    except Exception:
        return 0

def scan_files(output_file_path):
    records = []
    out_dir_abs = os.path.dirname(os.path.abspath(output_file_path))
    
    for root, dirs, files in os.walk(PROJECT_ROOT):
        # Exclude specified directories
        rel_root = os.path.relpath(root, PROJECT_ROOT)
        if rel_root in EXCLUDE_DIRS or any(ex in rel_root.split(os.sep) for ex in EXCLUDE_DIRS):
            continue
            
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        
        for file in files:
            full_path = os.path.join(root, file)
            # Skip the manifest file itself
            if os.path.abspath(full_path) == os.path.abspath(output_file_path):
                continue
                
            rel_path = os.path.relpath(full_path, PROJECT_ROOT)
            rel_link = os.path.relpath(full_path, out_dir_abs)
            
            if file.startswith(".") and file.endswith(".swp"):
                continue
                
            try:
                size_bytes = os.path.getsize(full_path)
                line_count = count_lines(full_path)
                sha = compute_sha256(full_path)
                records.append({
                    "path": rel_path,
                    "link": rel_link,
                    "size_bytes": size_bytes,
                    "lines": line_count,
                    "sha256": sha
                })
            except Exception as e:
                print(f"Skipping {rel_path}: {e}")
                
    records.sort(key=lambda r: r["path"])
    return records

def generate_manifest():
    output_path = os.path.join(PROJECT_ROOT, "docs", "manifest", "LIVE_FILE_MANIFEST.md")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    timestamp = datetime.now(timezone.utc).isoformat()
    records = scan_files(output_path)
    
    lines = [
        "# 📑 LIVE FILE MANIFEST & CRYPTOGRAPHIC SIGNATURE MATRIX",
        "",
        "> **AUTOMATED AUDIT & REPRODUCIBILITY MANIFEST**",
        f"> **Timestamp Signature (UTC)**: `{timestamp}`",
        f"> **Total Tracked Files**: `{len(records)}`",
        "",
        "---",
        "",
        "## 🔍 File Signature Index",
        "",
        "| Relative File Path | Size (Bytes) | Lines | SHA-256 Checksum (First 16 chars) | Full SHA-256 Signature |",
        "| :--- | :--- | :--- | :--- | :--- |"
    ]
    
    for r in records:
        short_sha = r["sha256"][:16]
        lines.append(f'| [`{r["path"]}`]({r["link"]}) | `{r["size_bytes"]}` | `{r["lines"]}` | `{short_sha}` | `{r["sha256"]}` |')
        
    lines.extend([
        "",
        "---",
        "",
        "## 🛠️ Verification & Diff Instructions",
        "",
        "To verify or compare a new manifest against this snapshot:",
        "```bash",
        "# 1. Re-generate live file manifest",
        "python3 .agents/scripts/generate-live-manifest.py",
        "",
        "# 2. Compare diff against previous signature snapshot",
        "git diff docs/manifest/LIVE_FILE_MANIFEST.md",
        "```"
    ])
    
    content = "\n".join(lines) + "\n"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
        
    print(f"✅ Generated Live File Manifest with {len(records)} files at: {output_path}")
    return output_path

if __name__ == "__main__":
    generate_manifest()
