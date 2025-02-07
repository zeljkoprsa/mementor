#!/usr/bin/env python3
from datetime import datetime
from pathlib import Path
import sys
sys.path.append('.')  # Add current directory to path

from memory_system_init.templates import (
    DocumentationTemplate,
    DocumentationMetadata,
    HealthMetrics,
    TemplateRegistry
)

def calculate_health_metrics(doc_path: Path) -> HealthMetrics:
    """Calculate health metrics for a documentation file."""
    content = doc_path.read_text()
    words = len(content.split())
    has_todos = "TODO" in content or "[ ]" in content
    linked_files = []  # TODO: Implement link detection
    
    # Simple completion metric based on TODO count
    total_items = content.count("- [")
    completed_items = content.count("- [X]") + content.count("- [✓]")
    completion = (completed_items / total_items * 100) if total_items > 0 else 100
    
    return HealthMetrics(
        last_updated=datetime.fromtimestamp(doc_path.stat().st_mtime),
        word_count=words,
        has_todos=has_todos,
        linked_files=linked_files,
        completion_percentage=completion
    )

def create_snapshot(doc_path: Path, output_dir: Path) -> None:
    """Create a snapshot of the current documentation state."""
    registry = TemplateRegistry()
    
    # Create metadata
    metadata = DocumentationMetadata(
        version="0.1.0",
        created_at=datetime.now(),
        updated_at=datetime.now(),
        dependencies=[
            {"name": "pystache", "version": "0.6.7"},
            {"name": "python", "version": "3.10"}
        ],
        health_metrics=calculate_health_metrics(doc_path),
        tags=["documentation", "snapshot"]
    )
    
    # Create template
    template = DocumentationTemplate(
        name="snapshot",
        content=Path("templates/snapshot.mustache").read_text(),
        metadata=metadata
    )
    
    # Register template
    registry.register_template(template)
    
    # Generate snapshot
    context = {
        "title": "Documentation Snapshot",
        "description": "Current state of project documentation",
        "changes": [
            "Updated template system",
            "Added metadata support",
            "Implemented snapshot generation"
        ],
        "state_items": [
            {
                "category": "Implementation",
                "items": [
                    {"description": "Template system", "completed": True},
                    {"description": "Metadata support", "completed": True},
                    {"description": "Snapshot generation", "completed": False}
                ]
            }
        ],
        "dependencies": metadata.dependencies,
        "next_actions": [
            "Implement automated snapshot scheduling",
            "Add more comprehensive health metrics",
            "Create snapshot comparison tools"
        ]
    }
    
    snapshot = registry.create_snapshot("snapshot", context)
    if snapshot:
        # Create output directory if it doesn't exist
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_path = output_dir / f"snapshot_{timestamp}.md"
        output_path.write_text(snapshot)
        print(f"Created snapshot: {output_path}")
    else:
        print("Failed to create snapshot")

if __name__ == "__main__":
    # Get the project docs directory from the input file path
    doc_path = Path("docs/mementor_docs/activeContext.md")
    project_docs_dir = doc_path.parent
    
    # Create archives within the project's documentation directory
    output_dir = project_docs_dir / "archives" / datetime.now().strftime("%Y")
    output_dir.mkdir(parents=True, exist_ok=True)
    create_snapshot(doc_path, output_dir)
