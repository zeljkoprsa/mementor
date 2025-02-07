from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

@dataclass
class HealthMetrics:
    """Health metrics for documentation files.
    
    Attributes:
        last_updated: Last modification time
        word_count: Total number of words
        reading_time: Estimated reading time in minutes
        has_todos: Whether TODOs are present
        todo_count: Number of open TODOs
        linked_files: List of linked files/documents
        broken_links: List of broken/invalid links
        completion_percentage: Percentage of completed items
        section_count: Number of sections (h1, h2, etc)
        section_depth: Maximum section nesting depth
        code_blocks: Number of code blocks
        avg_section_length: Average words per section
        readability_score: Flesch reading ease score
        last_snapshot_delta: Days since last snapshot
    """
    last_updated: datetime
    word_count: int
    reading_time: float
    has_todos: bool
    todo_count: int
    linked_files: List[str]
    broken_links: List[str]
    completion_percentage: float
    section_count: int
    section_depth: int
    code_blocks: int
    avg_section_length: float
    readability_score: float
    last_snapshot_delta: float = 0.0

@dataclass
class DocumentationMetadata:
    """Metadata for documentation templates and snapshots."""
    version: str
    created_at: datetime
    updated_at: datetime
    dependencies: List[Dict[str, str]]  # List of {name: str, version: str}
    health_metrics: Optional[HealthMetrics] = None
    tags: List[str] = field(default_factory=list)

@dataclass
class DocumentationTemplate:
    """Template for generating documentation with metadata."""
    name: str
    content: str
    metadata: DocumentationMetadata
    sections: List[Dict[str, Any]] = field(default_factory=list)

class TemplateRegistry:
    """Registry for managing documentation templates."""
    def __init__(self):
        self.templates: Dict[str, DocumentationTemplate] = {}
        self.template_dir = Path('templates')

    def register_template(self, template: DocumentationTemplate) -> None:
        """Register a new template or update existing one."""
        self.templates[template.name] = template

    def get_template(self, name: str) -> Optional[DocumentationTemplate]:
        """Retrieve a template by name."""
        return self.templates.get(name)
    
    def create_snapshot(self, template_name: str, context: Dict[str, Any]) -> Optional[str]:
        """Create a snapshot from a template with current context."""
        template = self.get_template(template_name)
        if not template:
            return None
            
        # Update metadata
        template.metadata.updated_at = datetime.now()
        
        # Generate snapshot with metadata header
        snapshot = self._generate_metadata_header(template.metadata)
        snapshot += "\n---\n\n"
        
        # Render template content
        import pystache
        renderer = pystache.Renderer()
        snapshot += renderer.render(template.content, context)
        
        return snapshot
    
    def _generate_metadata_header(self, metadata: DocumentationMetadata) -> str:
        """Generate a metadata header for snapshots."""
        header = ["=== MEMENTOR SNAPSHOT ==="]
        header.append(f"Version: {metadata.version}")
        header.append(f"Created: {metadata.created_at.isoformat()}")
        header.append(f"Updated: {metadata.updated_at.isoformat()}")
        
        if metadata.dependencies:
            header.append("\nDependencies:")
            for dep in metadata.dependencies:
                header.append(f"- {dep['name']} ({dep['version']})")
        
        if metadata.health_metrics:
            metrics = metadata.health_metrics
            
            # Content Metrics
            header.append("\nContent Metrics:")
            header.append(f"- Word Count: {metrics.word_count} words")
            header.append(f"- Reading Time: {metrics.reading_time:.1f} minutes")
            header.append(f"- Readability Score: {metrics.readability_score:.1f}/100.0")
            
            # Structure Metrics
            header.append("\nStructure Metrics:")
            header.append(f"- Sections: {metrics.section_count} (max depth: {metrics.section_depth})")
            header.append(f"- Average Section Length: {metrics.avg_section_length:.1f} words")
            header.append(f"- Code Blocks: {metrics.code_blocks}")
            
            # Progress Metrics
            header.append("\nProgress Metrics:")
            header.append(f"- Completion: {metrics.completion_percentage:.1f}%")
            header.append(f"- Open TODOs: {metrics.todo_count}")
            header.append(f"- Days Since Last Snapshot: {metrics.last_snapshot_delta:.1f}")
            
            # Link Health
            if metrics.linked_files or metrics.broken_links:
                header.append("\nLink Health:")
                if metrics.linked_files:
                    header.append(f"- Valid Links: {len(metrics.linked_files)}")
                if metrics.broken_links:
                    header.append(f"- Broken Links: {len(metrics.broken_links)}")
                    for link in metrics.broken_links:
                        header.append(f"  • {link}")
            
        if metadata.tags:
            header.append(f"\nTags: {', '.join(metadata.tags)}")
            
        return '\n'.join(header)
