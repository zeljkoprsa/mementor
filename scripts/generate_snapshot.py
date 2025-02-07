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

import re
from datetime import datetime, timedelta
from typing import List, Tuple

def extract_sections(content: str) -> List[Tuple[int, str, str]]:
    """Extract section headers with their levels and content."""
    lines = content.split('\n')
    sections = []
    current_section = None
    current_content = []
    
    for line in lines:
        if line.startswith('#'):
            if current_section:
                sections.append((current_section[0], current_section[1], '\n'.join(current_content)))
            level = len(re.match(r'^#+', line).group())
            title = line.lstrip('#').strip()
            current_section = (level, title)
            current_content = []
        else:
            current_content.append(line)
            
    if current_section:
        sections.append((current_section[0], current_section[1], '\n'.join(current_content)))
    
    return sections

def calculate_readability(text: str) -> float:
    """Calculate Flesch reading ease score."""
    sentences = len(re.split(r'[.!?]+', text))
    words = len(text.split())
    syllables = len(re.findall(r'[aeiou]+', text.lower()))
    
    if sentences == 0 or words == 0:
        return 0.0
    
    # Flesch Reading Ease = 206.835 - 1.015 × (words/sentences) - 84.6 × (syllables/words)
    score = 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    return max(0.0, min(100.0, score))  # Clamp between 0 and 100

def find_links(content: str) -> Tuple[List[str], List[str]]:
    """Find all links and check if they're valid."""
    # Find markdown links [text](url) and bare URLs
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)|<([^>]+)>|(?:https?://[^\s]+)'
    links = re.findall(link_pattern, content)
    
    valid_links = []
    broken_links = []
    
    for link in links:
        # Extract URL from different capture groups
        url = link[1] if link[1] else link[2] if link[2] else link[0]
        
        # Basic validation (could be enhanced with actual HTTP checks)
        if url.startswith(('http://', 'https://', '/', './')):
            valid_links.append(url)
        else:
            broken_links.append(url)
    
    return valid_links, broken_links

def calculate_health_metrics(doc_path: Path) -> HealthMetrics:
    """Calculate comprehensive health metrics for a documentation file."""
    content = doc_path.read_text()
    
    # Basic metrics
    words = len(content.split())
    reading_time = words / 200  # Average reading speed of 200 WPM
    
    # TODO detection
    has_todos = "TODO" in content or "[ ]" in content
    todo_count = content.count("TODO") + content.count("[ ]")
    
    # Link analysis
    linked_files, broken_links = find_links(content)
    
    # Completion metrics
    total_items = content.count("- [")
    completed_items = content.count("- [X]") + content.count("- [✓]")
    completion = (completed_items / total_items * 100) if total_items > 0 else 100
    
    # Section analysis
    sections = extract_sections(content)
    section_count = len(sections)
    section_depth = max(level for level, _, _ in sections) if sections else 0
    total_section_words = sum(len(content.split()) for _, _, content in sections)
    avg_section_length = total_section_words / section_count if section_count > 0 else 0
    
    # Code block detection
    code_blocks = len(re.findall(r'```[^`]*```', content, re.DOTALL))
    
    # Calculate readability
    readability_score = calculate_readability(content)
    
    # Calculate time since last snapshot
    archives_dir = doc_path.parent / "archives"
    last_snapshot_delta = 0.0
    if archives_dir.exists():
        snapshots = list(archives_dir.rglob("*.md"))
        if snapshots:
            latest = max(snapshots, key=lambda p: p.stat().st_mtime)
            last_snapshot_delta = (datetime.now() - datetime.fromtimestamp(latest.stat().st_mtime)).days
    
    return HealthMetrics(
        last_updated=datetime.fromtimestamp(doc_path.stat().st_mtime),
        word_count=words,
        reading_time=reading_time,
        has_todos=has_todos,
        todo_count=todo_count,
        linked_files=linked_files,
        broken_links=broken_links,
        completion_percentage=completion,
        section_count=section_count,
        section_depth=section_depth,
        code_blocks=code_blocks,
        avg_section_length=avg_section_length,
        readability_score=readability_score,
        last_snapshot_delta=last_snapshot_delta
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
