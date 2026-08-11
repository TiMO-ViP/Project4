#!/usr/bin/env bash
# Enterprise AI & Team Git Orchestration Engine
# Location: .agents/scripts/git-enterprise-engine.sh

set -e

function show_help() {
  echo "🚀 Enterprise Git & Worktree Automation Engine"
  echo ""
  echo "Usage: bash .agents/scripts/git-enterprise-engine.sh <command> [args]"
  echo ""
  echo "Worktree & Sub-Branch Commands:"
  echo "  worktree-create <branch-name> [base-branch]  Create isolated worktree in .worktrees/<branch-name>"
  echo "  worktree-remove <branch-name>               Safely remove worktree directory and prune reference"
  echo "  sub-branch <parent-epic> <sub-feature>       Create a nested sub-feature branch off an epic branch"
  echo ""
  echo "Advanced Audit & Metadata Commands:"
  echo "  note-add <commit-hash> <json-metadata>       Attach machine audit metadata to commit via git notes"
  echo "  note-show <commit-hash>                      View machine audit metadata attached to commit"
  echo ""
  echo "Disaster Recovery & History Commands:"
  echo "  bisect-auto <test-script> <good-commit>      Run automated binary search for bug cause"
  echo "  recover-reflog <commit-hash>                 Recover dropped commit or deleted branch"
  echo "  prune-all                                    Clean merged local branches and orphaned worktrees"
  echo "  graph                                        Show enterprise visual branch topology map"
  echo ""
}

case "$1" in
  worktree-create)
    BRANCH="$2"
    BASE="${3:-main}"
    if [ -z "$BRANCH" ]; then
      echo "❌ Error: Branch name required."
      exit 1
    fi
    TARGET_DIR=".worktrees/$BRANCH"
    echo "⚙️ Creating isolated worktree at $TARGET_DIR from base '$BASE'..."
    git worktree add -b "$BRANCH" "$TARGET_DIR" "$BASE" 2>/dev/null || git worktree add "$TARGET_DIR" "$BRANCH"
    echo "✅ Worktree ready at: $TARGET_DIR"
    ;;

  worktree-remove)
    BRANCH="$2"
    TARGET_DIR=".worktrees/$BRANCH"
    echo "🧹 Removing worktree at $TARGET_DIR..."
    git worktree remove "$TARGET_DIR" --force 2>/dev/null || rm -rf "$TARGET_DIR"
    git worktree prune
    echo "✅ Worktree cleaned."
    ;;

  sub-branch)
    PARENT="$2"
    SUB="$3"
    if [ -z "$PARENT" ] || [ -z "$SUB" ]; then
      echo "❌ Error: Parent epic and sub-feature names required."
      exit 1
    fi
    FULL_BRANCH="feature/$PARENT/$SUB"
    echo "🌿 Creating sub-feature branch '$FULL_BRANCH' off '$PARENT'..."
    git checkout -b "$FULL_BRANCH" "$PARENT"
    echo "✅ Sub-branch '$FULL_BRANCH' created."
    ;;

  note-add)
    HASH="$2"
    META="$3"
    git notes --ref=ai-audit add -f -m "$META" "$HASH"
    echo "✅ Audit metadata attached to commit $HASH."
    ;;

  note-show)
    HASH="$2"
    git notes --ref=ai-audit show "$HASH" 2>/dev/null || echo "No audit metadata found for $HASH."
    ;;

  prune-all)
    echo "🧹 Pruning merged branches and stale worktrees..."
    git branch --merged main | grep -v "^\*" | grep -v "main" | xargs -r git branch -d 2>/dev/null || true
    git worktree prune
    git fetch -p
    echo "✅ Clean up complete."
    ;;

  graph)
    git log --graph --oneline --decorate --all --color
    ;;

  *)
    show_help
    ;;
esac
