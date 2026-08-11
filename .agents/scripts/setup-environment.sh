#!/usr/bin/env bash
# Universal Multi-Language Environment Provisioner
# Location: .agents/scripts/setup-environment.sh

set -e

function setup_ts() {
  echo "⚡ Provisioning Modern TypeScript / JS Environment (Biome + Vitest + TS Strict)..."
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

  cat << 'EOF' > biome.json
{
  "$schema": "https://biomejs.dev/schemas/1.8.3/schema.json",
  "organizeImports": { "enabled": true },
  "linter": { "enabled": true, "rules": { "recommended": true } },
  "formatter": { "enabled": true, "indentStyle": "space", "indentWidth": 2, "lineWidth": 100 }
}
EOF
  echo "✅ TypeScript environment configured."
}

function setup_python() {
  echo "⚡ Provisioning Modern Python Environment (uv + Ruff + Pytest)..."
  cat << 'EOF' > pyproject.toml
[project]
name = "project4"
version = "0.1.0"
description = "Enterprise Multi-Language Workspace"
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
  echo "✅ Python environment configured."
}

function setup_rust() {
  echo "⚡ Provisioning Modern Rust Environment (Cargo + Clippy + Rustfmt)..."
  if [ ! -f "Cargo.toml" ]; then
    cat << 'EOF' > Cargo.toml
[package]
name = "project4"
version = "0.1.0"
edition = "2024"

[dependencies]
serde = { version = "1.0", features = ["derive"] }
tokio = { version = "1.0", features = ["full"] }

[dev-dependencies]
EOF
  fi
  echo "✅ Rust Cargo environment configured."
}

case "$1" in
  ts|typescript)
    setup_ts
    ;;
  py|python)
    setup_python
    ;;
  rust)
    setup_rust
    ;;
  all)
    setup_ts
    setup_python
    setup_rust
    ;;
  *)
    echo "Usage: bash .agents/scripts/setup-environment.sh [typescript|python|rust|all]"
    ;;
esac
