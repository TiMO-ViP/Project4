#!/usr/bin/env bash
# Pre-Flight Environment Configurator (2026 Engineering Standards)
# Location: .agents/scripts/setup-environment.sh

set -e

function setup_ts() {
  echo "⚡ Provisioning Modern TypeScript / JS Environment (Biome + Vitest + TS Strict)..."
  
  # Create tsconfig.json
  cat << 'EOF' > tsconfig.json
{
  "compilerOptions": {
    "target": "ES2024",
    "module": "NodeNext",
    "moduleResolution": "NodeNext",
    "esModuleInterop": true,
    "strict": true,
    "noUncheckedIndexedAccess": true,
    "exactOptionalPropertyTypes": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "outDir": "./dist"
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "**/*.spec.ts", "**/*.test.ts"]
}
EOF

  # Create biome.json
  cat << 'EOF' > biome.json
{
  "$schema": "https://biomejs.dev/schemas/1.8.3/schema.json",
  "organizeImports": {
    "enabled": true
  },
  "linter": {
    "enabled": true,
    "rules": {
      "recommended": true
    }
  },
  "formatter": {
    "enabled": true,
    "indentStyle": "space",
    "indentWidth": 2,
    "lineWidth": 100
  }
}
EOF

  echo "✅ TypeScript environment configuration generated."
}

function setup_python() {
  echo "⚡ Provisioning Modern Python Environment (uv + Ruff + Pytest)..."
  
  # Create pyproject.toml
  cat << 'EOF' > pyproject.toml
[project]
name = "project4"
version = "0.1.0"
description = "Enterprise Project Workspace"
readme = "README.md"
requires-python = ">=3.12"
dependencies = []

[dependency-groups]
dev = [
    "pytest>=8.0.0",
    "ruff>=0.5.0",
]

[tool.ruff]
line-length = 100
target-version = "py312"

[tool.ruff.lint]
select = ["E4", "E7", "E9", "F", "B", "I", "UP"]

[tool.ruff.format]
docstring-code-format = true

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = ["-ra", "-q"]
EOF

  echo "✅ Python pyproject.toml configuration generated."
}

case "$1" in
  ts|typescript)
    setup_ts
    ;;
  py|python)
    setup_python
    ;;
  all)
    setup_ts
    setup_python
    ;;
  *)
    echo "Usage: bash .agents/scripts/setup-environment.sh [typescript|python|all]"
    ;;
esac
