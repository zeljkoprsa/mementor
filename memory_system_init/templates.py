from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List, Any, Optional
from pathlib import Path

@dataclass
class HealthMetrics:
    """Health metrics for documentation files."""
    last_updated: datetime
    word_count: int
    has_todos: bool
    linked_files: List[str]
    completion_percentage: float

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
            header.append("\nHealth Metrics:")
            metrics = metadata.health_metrics
            header.append(f"- Last Updated: {metrics.last_updated.isoformat()}")
            header.append(f"- Word Count: {metrics.word_count}")
            header.append(f"- Completion: {metrics.completion_percentage}%")
            header.append(f"- TODOs Present: {'Yes' if metrics.has_todos else 'No'}")
            
        if metadata.tags:
            header.append(f"\nTags: {', '.join(metadata.tags)}")
            
        return '\n'.join(header)
