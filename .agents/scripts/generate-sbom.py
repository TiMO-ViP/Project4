#!/usr/bin/env python3
"""
CycloneDX v1.6 SBOM Generator Script
Extracts software component dependency inventory from package.json, Cargo.toml, and pyproject.toml.
Outputs a valid CycloneDX v1.6 JSON file (sbom.cdx.json) in the project root directory.
"""

import datetime
import json
import os
import pathlib
import re
import sys
import uuid

if sys.version_info >= (3, 11):
    import tomllib
else:
    try:
        import tomli as tomllib
    except ImportError:
        tomllib = None


def clean_version(ver_str: str) -> str:
    """Clean version constraint string into a clean version identifier."""
    if not ver_str:
        return "0.0.0"
    cleaned = re.sub(r"^[~^>=<!=v\s]+", "", ver_str.strip())
    cleaned = cleaned.split(",")[0].strip()
    return cleaned if cleaned else "0.0.0"


def parse_package_json(path: pathlib.Path) -> list[dict]:
    """Parse package.json dependencies and devDependencies."""
    components = []
    if not path.exists():
        return components
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except Exception as e:
        print(f"Warning: Failed to parse {path}: {e}", file=sys.stderr)
        return components

    deps = data.get("dependencies", {})
    dev_deps = data.get("devDependencies", {})

    all_deps = {}
    if isinstance(deps, dict):
        all_deps.update(deps)
    if isinstance(dev_deps, dict):
        all_deps.update(dev_deps)

    for name, ver in all_deps.items():
        if not isinstance(ver, str):
            continue
        clean_ver = clean_version(ver)
        if name.startswith("@"):
            parts = name.split("/", 1)
            scope = parts[0][1:]
            pkg_name = parts[1] if len(parts) > 1 else ""
            purl = f"pkg:npm/%40{scope}/{pkg_name}@{clean_ver}"
        else:
            purl = f"pkg:npm/{name}@{clean_ver}"

        components.append({
            "type": "library",
            "bom-ref": purl,
            "name": name,
            "version": clean_ver,
            "purl": purl,
            "scope": "required" if name in deps else "optional"
        })
    return components


def parse_cargo_toml(path: pathlib.Path) -> list[dict]:
    """Parse Cargo.toml dependencies."""
    components = []
    if not path.exists() or tomllib is None:
        return components
    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
    except Exception as e:
        print(f"Warning: Failed to parse {path}: {e}", file=sys.stderr)
        return components

    deps = {}
    for section in ["dependencies", "dev-dependencies", "build-dependencies"]:
        if section in data and isinstance(data[section], dict):
            deps.update(data[section])

    for name, item in deps.items():
        if isinstance(item, str):
            ver = item
        elif isinstance(item, dict) and "version" in item:
            ver = item["version"]
        else:
            ver = "0.0.0"

        clean_ver = clean_version(ver)
        purl = f"pkg:cargo/{name}@{clean_ver}"
        components.append({
            "type": "library",
            "bom-ref": purl,
            "name": name,
            "version": clean_ver,
            "purl": purl
        })
    return components


def parse_pyproject_toml(path: pathlib.Path) -> list[dict]:
    """Parse pyproject.toml dependencies."""
    components = []
    if not path.exists() or tomllib is None:
        return components
    try:
        with open(path, "rb") as f:
            data = tomllib.load(f)
    except Exception as e:
        print(f"Warning: Failed to parse {path}: {e}", file=sys.stderr)
        return components

    raw_deps = []
    project = data.get("project", {})
    if isinstance(project, dict) and "dependencies" in project:
        if isinstance(project["dependencies"], list):
            raw_deps.extend(project["dependencies"])

    dep_groups = data.get("dependency-groups", {})
    if isinstance(dep_groups, dict):
        for group_deps in dep_groups.values():
            if isinstance(group_deps, list):
                raw_deps.extend(group_deps)

    for dep_str in raw_deps:
        if not isinstance(dep_str, str):
            continue
        match = re.match(r"^([a-zA-Z0-9_\-\.]+)(.*)", dep_str.strip())
        if match:
            name = match.group(1)
            ver_spec = match.group(2)
            clean_ver = clean_version(ver_spec)
            purl = f"pkg:pypi/{name.lower()}@{clean_ver}"
            components.append({
                "type": "library",
                "bom-ref": purl,
                "name": name,
                "version": clean_ver,
                "purl": purl
            })
    return components


def generate_sbom():
    # Discover project root relative to script
    script_dir = pathlib.Path(__file__).parent.resolve()
    root_dir = script_dir.parent.parent

    # Collect components from all supported manifests
    components_by_purl = {}

    all_parsed = (
        parse_package_json(root_dir / "package.json")
        + parse_cargo_toml(root_dir / "Cargo.toml")
        + parse_pyproject_toml(root_dir / "pyproject.toml")
    )

    for comp in all_parsed:
        purl = comp["purl"]
        if purl not in components_by_purl:
            components_by_purl[purl] = comp

    sorted_components = sorted(components_by_purl.values(), key=lambda x: x["purl"])

    timestamp = datetime.datetime.now(datetime.timezone.utc).isoformat()

    sbom = {
        "$schema": "http://cyclonedx.org/schema/sbom-1.6.json",
        "bomFormat": "CycloneDX",
        "specVersion": "1.6",
        "serialNumber": f"urn:uuid:{uuid.uuid4()}",
        "version": 1,
        "metadata": {
            "timestamp": timestamp,
            "tools": {
                "components": [
                    {
                        "type": "application",
                        "name": "generate-sbom",
                        "version": "1.0.0"
                    }
                ]
            },
            "component": {
                "type": "application",
                "name": "project4",
                "version": "1.0.0"
            }
        },
        "components": sorted_components
    }

    output_path = root_dir / "sbom.cdx.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(sbom, f, indent=2)

    print(f"Successfully generated CycloneDX v1.6 SBOM at {output_path} with {len(sorted_components)} components.")


if __name__ == "__main__":
    generate_sbom()
