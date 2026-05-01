#!/usr/bin/env bash
# =============================================================================
# bootstrap.sh — Template Initialization
#
# Automatically replaces all template placeholders (e.g., {{project_name}})
# with your actual project values.
#
# Usage:
#   ./scripts/bootstrap.sh --project-name my-app --organization my-org
# =============================================================================

set -euo pipefail

if [[ $# -eq 0 ]] || [[ "$1" == "-h" ]] || [[ "$1" == "--help" ]]; then
    echo "Usage: $0 [OPTIONS]"
    echo ""
    echo "Bootstraps the repository by replacing template variables."
    echo ""
    echo "Options:"
    echo "  --project-name NAME    Replacement for {{project_name}}"
    echo "  --project-desc DESC    Replacement for {{project_description}}"
    echo "  --organization ORG     Replacement for {{organization}}"
    echo "  --org-name ORG         Replacement for {{org_name}}"
    echo ""
    echo "Example: $0 --project-name my-app --organization my-org"
    exit 0
fi

PROJECT_NAME=""
PROJECT_DESC=""
ORGANIZATION=""
ORG_NAME=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --project-name)
            if [[ $# -lt 2 ]] || [[ "$2" == -* ]]; then
                echo "[ERROR] Option $1 requires a value."
                echo "Use $0 --help for usage guidance."
                exit 1
            fi
            PROJECT_NAME="$2"
            shift 2
            ;;
        --project-desc)
            if [[ $# -lt 2 ]] || [[ "$2" == -* ]]; then
                echo "[ERROR] Option $1 requires a value."
                echo "Use $0 --help for usage guidance."
                exit 1
            fi
            PROJECT_DESC="$2"
            shift 2
            ;;
        --organization)
            if [[ $# -lt 2 ]] || [[ "$2" == -* ]]; then
                echo "[ERROR] Option $1 requires a value."
                echo "Use $0 --help for usage guidance."
                exit 1
            fi
            ORGANIZATION="$2"
            shift 2
            ;;
        --org-name)
            if [[ $# -lt 2 ]] || [[ "$2" == -* ]]; then
                echo "[ERROR] Option $1 requires a value."
                echo "Use $0 --help for usage guidance."
                exit 1
            fi
            ORG_NAME="$2"
            shift 2
            ;;
        *)
            echo "[ERROR] Unknown option: $1"
            exit 1
            ;;
    esac
done

echo "[INFO] Starting repository bootstrap..."

export PROJECT_NAME
export PROJECT_DESC
export ORGANIZATION
export ORG_NAME

python3 -c "
import os, sys

replacements = {
    '{{project_name}}': os.environ.get('PROJECT_NAME', ''),
    '{{project_description}}': os.environ.get('PROJECT_DESC', ''),
    '{{organization}}': os.environ.get('ORGANIZATION', ''),
    '{{org_name}}': os.environ.get('ORG_NAME', '')
}

# Filter out empty arguments
replacements = {k: v for k, v in replacements.items() if v}

if not replacements:
    print('[INFO] No replacements provided. Use -h for options.')
    sys.exit(0)

ignore_dirs = {'.git', '.venv', 'node_modules', 'site', '__pycache__', 'assets'}
ignore_exts = ('.pyc', '.png', '.svg', '.jpg', '.jpeg', '.gif', '.ico', '.woff', '.woff2', '.ttf', '.eot')

for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ignore_dirs]
    for file in files:
        if file.endswith(ignore_exts) or file == 'bootstrap.sh':
            continue
            
        filepath = os.path.join(root, file)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            continue
            
        new_content = content
        for placeholder, replacement in replacements.items():
            new_content = new_content.replace(placeholder, replacement)
            
        if content != new_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'[INFO] Updated: {filepath}')
"

echo "[INFO] Bootstrap complete! You may now delete this script if desired."
