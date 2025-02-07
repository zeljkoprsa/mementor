#!/usr/bin/env python3
"""
Pre-commit hook for Mementor documentation snapshots.
This script checks if documentation files have changed and generates a new snapshot if needed.
"""
import subprocess
from pathlib import Path
import sys
from typing import List, Set
import re

def get_staged_files() -> Set[str]:
    """Get list of staged files that will be committed."""
    result = subprocess.run(
        ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR'],
        capture_output=True,
        text=True
    )
    return set(result.stdout.splitlines())

def is_doc_file(file_path: str) -> bool:
    """Check if a file is a documentation file that should trigger a snapshot."""
    doc_patterns = [
        r'^docs/.*\.(md|rst|txt)$',  # Documentation files
        r'^README\.md$',             # Root README
        r'^CHANGELOG\.md$',          # Changelog
        r'^CONTRIBUTING\.md$'        # Contributing guide
    ]
    return any(re.match(pattern, file_path) for pattern in doc_patterns)

def has_doc_changes(staged_files: Set[str]) -> bool:
    """Check if any documentation files have been changed."""
    return any(is_doc_file(file) for file in staged_files)

def get_project_root() -> Path:
    """Get the root directory of the git project."""
    result = subprocess.run(
        ['git', 'rev-parse', '--show-toplevel'],
        capture_output=True,
        text=True
    )
    return Path(result.stdout.strip())

def generate_snapshot() -> bool:
    """Generate a new documentation snapshot."""
    try:
        # Add the project root to Python path
        project_root = get_project_root()
        sys.path.insert(0, str(project_root))
        
        # Import and run the snapshot generator
        from scripts.generate_snapshot import create_snapshot
        from pathlib import Path
        
        doc_path = Path("docs/mementor_docs/activeContext.md")
        output_dir = doc_path.parent / "archives" / "2025"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        create_snapshot(doc_path, output_dir)
        
        # Stage the new snapshot
        subprocess.run(['git', 'add', str(output_dir)])
        return True
    except Exception as e:
        print(f"Error generating snapshot: {e}", file=sys.stderr)
        return False

def main() -> int:
    """Main entry point for the pre-commit hook."""
    staged_files = get_staged_files()
    
    if not has_doc_changes(staged_files):
        print("No documentation changes detected, skipping snapshot generation")
        return 0
        
    print("Documentation changes detected, generating snapshot...")
    if generate_snapshot():
        print("Successfully generated and staged documentation snapshot")
        return 0
    else:
        print("Failed to generate documentation snapshot", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
