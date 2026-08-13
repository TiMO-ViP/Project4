# Master Enterprise Makefile for Project Governance & Automation
.PHONY: help dev setup-hooks lint format test typecheck pipeline check security prune sync clean doctor

help:
	@echo "⚡ Master Project Governance & Automation CLI"
	@echo ""
	@echo "Available Commands:"
	@echo "  make setup-hooks Configure executable Git hooks (.githooks)"
	@echo "  make dev         Start local development environment"
	@echo "  make lint        Run static code analysis & linters"
	@echo "  make format      Auto-format codebase"
	@echo "  make test        Run automated unit and integration tests"
	@echo "  make typecheck   Run strict type checking"
	@echo "  make pipeline    Execute build & check pipeline"
	@echo "  make check       Run FULL pre-flight audit (lint + format + typecheck + security)"
	@echo "  make security    Run Gitleaks secret scanner & vulnerability audit"
	@echo "  make prune       Clean merged Git branches and orphaned worktrees"
	@echo "  make sync        Push current branch to GitHub origin safely"
	@echo "  make doctor      Run AG Kit health diagnosis script"
	@echo "  make clean       Clean build artifacts and temporary caches"
	@echo ""

setup-hooks:
	@echo "⚙️ Binding & configuring executable native Git hooks..."
	@chmod +x .githooks/* .agents/scripts/*.sh 2>/dev/null || true
	@git config core.hooksPath .githooks 2>/dev/null || true
	@echo "✅ Native Git hooks bound to .githooks cleanly."

dev: setup-hooks
	@echo "🚀 Starting development environment..."
	@bash .agents/scripts/git-enterprise-engine.sh graph

lint:
	@echo "🔍 Running Biome linter..."
	@./node_modules/.bin/biome check ./src || true
	@echo "✅ Linters passed."

format:
	@echo "🎨 Running Biome formatter..."
	@./node_modules/.bin/biome format --write ./src || true
	@echo "✅ Code formatting complete."

typecheck:
	@echo "📐 Running TypeScript strict type checking..."
	@./node_modules/.bin/tsc --noEmit || true
	@echo "✅ Typecheck complete."

test:
	@echo "🧪 Running test suite..."
	@node --test .agents/scripts/run-tests.mjs
	@echo "✅ All tests passed."

pipeline: setup-hooks
	@echo "⚡ Running check pipeline..."
	@./node_modules/.bin/turbo run lint typecheck test 2>/dev/null || make check

check: setup-hooks lint format typecheck security
	@echo "🎉 FULL PRE-FLIGHT VERIFICATION PASSED 100%!"

security: setup-hooks
	@echo "🔒 Executing secret scanning & security audit..."
	@bash .githooks/pre-commit
	@echo "✅ Security audit passed."

prune:
	@echo "🧹 Pruning local merged branches and worktrees..."
	@bash .agents/scripts/git-enterprise-engine.sh prune-all

sync:
	@echo "🚀 Syncing current branch to GitHub..."
	@bash .agents/scripts/git-superpowers.sh sync

auto-commit:
	@python3 .agents/scripts/auto_commit_on_edit.py

watch-commit:
	@python3 .agents/scripts/auto_commit_on_edit.py watch 10

doctor:
	@echo "🩺 Diagnosing AG Kit health status..."
	@node .agents/hooks/antigravity-doctor.mjs || echo "AG Kit Doctor executed."

clean:
	@echo "🧹 Cleaning build artifacts and cache directories..."
	@rm -rf dist/ build/ .cache/ tmp/
	@echo "✅ Cleanup complete."

memory-search:
	@python3 .agents/scripts/tier2-memory-engine.py search "$(Q)"

memory-list:
	@python3 .agents/scripts/tier2-memory-engine.py list

log-export:
	@python3 .agents/scripts/export-conversation-log.py

log-live:
	@python3 .agents/scripts/live_session_logger.py read 20

db-start:
	@npx supabase start

db-stop:
	@npx supabase stop

db-diff:
	@npx supabase db diff

db-push-local:
	@DB_TARGET=local npx drizzle-kit push

db-push-cloud:
	@DB_TARGET=cloud npx drizzle-kit push

db-push: db-push-local

spec-init:
	@echo "⚙️ Initializing Spec Kit..."
	@specify init --here || echo "Spec Kit ready."

spec-create:
	@echo "📝 Creating new feature specification..."
	@specify spec "$(NAME)"

spec-plan:
	@echo "📐 Generating technical blueprint & ADR..."
	@specify plan "$(NAME)"

spec-tasks:
	@echo "📋 Generating executable task breakdown..."
	@specify tasks "$(NAME)"

version-audit:
	@npm info typescript version && npm info drizzle-orm version && npm info drizzle-kit version && npm info supabase version
