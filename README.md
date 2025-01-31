# Mementor

Documentation memory system for AI driven projects.

## Features

- Three-tier memory management:
  - Short-term: Active context tracking
  - Mid-term: Knowledge base documentation
  - Long-term: System patterns
- Automated snapshot creation
- Customizable templates
- Git integration
- CLI interface

## Installation

```bash
pip install memory-system-init
```

## Quick Start

Initialize the memory system in your project:

```bash
# Basic initialization
memory-system init

# With custom configuration
memory-system init --config custom_config.yaml

# In a specific directory
memory-system init /path/to/project
```

## Documentation Structure

The system creates the following structure:

```
docs/
├── activeContext.md    # Short-term memory
├── productContext.md   # Product documentation
├── progress.md        # Progress tracking
├── structure.md       # Documentation structure
├── systemPatterns.md  # Long-term patterns
├── techContext.md     # Technical documentation
└── archives/         # Bi-weekly snapshots
    └── YYYY/
        └── WXX/
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
