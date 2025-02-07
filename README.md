# Mementor

An intelligent documentation management system that helps maintain living documentation through automated snapshots, health metrics, and git integration.

## Features

### Documentation Management
- **Three-tier Memory System**:
  - Short-term: Active context tracking
  - Mid-term: Knowledge base documentation
  - Long-term: System patterns and archives
- **Project-specific Documentation**:
  - Isolated documentation spaces
  - Custom templates and configurations
  - Automatic directory structure

### Automated Snapshots
- **Git Integration**:
  - Pre-commit hooks for automatic snapshots
  - Documentation change detection
  - Automatic staging of snapshots
- **Comprehensive Health Metrics**:
  - Content quality (readability, length, reading time)
  - Document structure (sections, depth, code blocks)
  - Progress tracking (completion, TODOs, snapshot frequency)
  - Link validation and health checks

### Template System
- **Customizable Templates**:
  - Mustache-based templating
  - Metadata support
  - Version tracking
- **Smart Metadata**:
  - Automatic health metrics
  - Dependency tracking
  - Change detection

## Quick Start

### 1. Installation

```bash
# Install Mementor and its dependencies
pip install mementor

# Install pre-commit for git integration
pip install pre-commit
```

### 2. Project Integration

```bash
# Initialize Mementor in your project
mementor init

# Install git hooks
pre-commit install
```

### 3. Configuration

Create or update your `pyproject.toml`:

```toml
[tool.mementor]
project_name = "your-project"
docs_dir = "docs/your-project-docs"
template_dir = "templates"

[tool.mementor.metrics]
min_readability_score = 60.0
max_section_depth = 3
max_todos = 10
```

### 4. Directory Structure

Mementor creates the following structure:

```
docs/
└── your-project-docs/     # Project-specific documentation
    ├── activeContext.md    # Short-term decisions
    ├── progress.md         # Progress tracking
    ├── structure.md        # Documentation structure
    ├── systemPatterns.md   # System patterns
    └── archives/           # Automated snapshots
        └── YYYY/
            └── snapshot_YYYYMMDD_HHMMSS.md
```
            └── context_snapshot.md
```

## Configuration

Create a `memory-system.yaml` file to customize:

```yaml
project:
  name: "Your Project"
  docs_dir: "docs"
  snapshot_schedule: "bi-weekly"
  templates:
    custom_dir: "path/to/templates"
```

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details
