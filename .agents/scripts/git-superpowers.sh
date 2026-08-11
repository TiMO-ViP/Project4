#!/usr/bin/env bash
# Git Superpowers Helper Script for Workspace Automation
# Location: .agents/scripts/git-superpowers.sh

set -e

function show_help() {
  echo "⚡ Git Superpowers Automation Helper"
  echo ""
  echo "Usage: bash .agents/scripts/git-superpowers.sh <command>"
  echo ""
  echo "Commands:"
  echo "  prune         Delete all local branches already merged into main"
  echo "  log-graph     Show a beautiful visual color topology map of all branches"
  echo "  enable-rerere Turn on auto-resolution memory for recurring merge conflicts"
  echo "  enable-maint  Turn on background Git repository optimization & prefetching"
  echo "  sync          Push current branch to origin with auto-upstream tracking"
  echo ""
}

case "$1" in
  prune)
    echo "🧹 Pruning local merged branches..."
    git branch --merged main | grep -v "^\*" | grep -v "main" | xargs -r git branch -d
    git fetch -p
    echo "✅ Local branches pruned clean."
    ;;
  log-graph)
    git log --graph --oneline --decorate --all --color
    ;;
  enable-rerere)
    git config --local rerere.enabled true
    echo "✅ Git rerere enabled (Merge conflict resolutions will be remembered automatically)."
    ;;
  enable-maint)
    git maintenance start
    echo "✅ Git background maintenance started."
    ;;
  sync)
    BRANCH=$(git branch --show-current)
    echo "🚀 Syncing branch '$BRANCH' to origin..."
    git push -u origin "$BRANCH"
    ;;
  *)
    show_help
    ;;
esac
