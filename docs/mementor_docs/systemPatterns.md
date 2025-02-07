# System Patterns

## Development Patterns

### 1. CLI-First Design
- Command-line interface as primary interaction method
- Intuitive commands following Git-style patterns
- Consistent command structure and naming
```bash
memory-system init            # Basic initialization
memory-system init --config   # With custom config
memory-system snapshot        # Create snapshot
```

### 2. Template-Based Generation
- All documentation files are template-based
- Templates stored in package resources
- Customizable through configuration
```yaml
templates:
  custom_dir: path/to/templates
  overrides:
    activeContext: custom_template.md
```

### 3. Configuration Management
- YAML-based configuration
- Hierarchical settings structure
- Environment variable support
```yaml
project:
  name: string
  docs_dir: string
  snapshot:
    frequency: bi-weekly
    day: monday
    time: "09:00"
```

### 4. Documentation Patterns

#### Three-Tier Memory Structure
1. **Short-Term (Active Context)**
   - Current state tracking
   - Recent changes
   - Active tasks
   - Bi-weekly snapshots

2. **Mid-Term (Knowledge Base)**
   - Technical documentation
   - Implementation details
   - Configuration guides
   - Usage examples

3. **Long-Term (System Patterns)**
   - Architecture decisions
   - Development patterns
   - Best practices
   - Standards

#### Progress Tracking
- Status markers: [✓] [-] [×] [ ] [!]
- Chronological logging
- Task templates
- Monthly summaries

## Code Standards

### Python Standards
- Python 3.8+ compatibility
- Type hints required
- Black code formatting
- Docstring format:
```python
def function_name(param1: str, param2: int) -> bool:
    """Short description.

    Detailed description of the function.

    Args:
        param1: Description of param1
        param2: Description of param2

    Returns:
        Description of return value

    Raises:
        ExceptionType: Description of when this exception occurs
    """
```

### Testing Standards
- Pytest for testing
- 90%+ coverage requirement
- Integration tests required
- Property-based testing where applicable

### Documentation Standards
- Markdown for all documentation
- Clear hierarchy with headers
- Code examples where relevant
- Regular updates required

## Architecture Decisions

### 1. Package Structure
```
memory-system-init/
├── memory_system_init/
│   ├── __init__.py
│   ├── cli.py          # CLI interface
│   ├── core.py         # Core functionality
│   ├── config.py       # Configuration management
│   └── templates/      # Default templates
├── tests/
└── docs/              # Documentation
```

### 2. Dependency Choices
- click: CLI framework
- PyYAML: Configuration
- rich: Terminal formatting
- python-crontab: Automation

### 3. Template Engine
- Simple string templates
- Variable substitution
- Markdown-based
- Custom delimiters

## Best Practices

### 1. Error Handling
- Descriptive error messages
- Graceful degradation
- User-friendly feedback
- Recovery suggestions

### 2. Configuration
- Sensible defaults
- Clear override paths
- Environment awareness
- Validation on load

### 3. Documentation
- Keep activeContext.md updated
- Regular snapshots
- Clear progress tracking
- Pattern documentation

### 4. Testing
- Test-driven development
- Integration testing
- Documentation testing
- Regular coverage checks
