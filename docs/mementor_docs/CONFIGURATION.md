# Mementor Configuration Guide

This guide explains how to configure Mementor for your AI-driven development workflow.

## Table of Contents
1. [Basic Configuration](#basic-configuration)
2. [AI Integration Settings](#ai-integration-settings)
3. [Documentation Health](#documentation-health)
4. [Git Integration](#git-integration)
5. [Advanced Options](#advanced-options)

## Basic Configuration

### Project Configuration
Configure Mementor in your `pyproject.toml`:

```toml
[tool.mementor]
# Project identification
project_name = "your-project"
version = "0.1.0"

# Directory settings
docs_dir = "docs/your-project-docs"
template_dir = "templates"
archive_dir = "archives"

# Documentation structure
default_template = "active_context"
```

### Environment Variables
Set these in your `.env` file:

```bash
# Documentation paths
MEMENTOR_DOCS_ROOT=/path/to/docs
MEMENTOR_TEMPLATES=/path/to/templates

# Git integration
MEMENTOR_GIT_HOOKS=true
MEMENTOR_AUTO_COMMIT=false
```

## AI Integration Settings

### Context Management
Configure how Mementor interacts with AI tools:

```toml
[tool.mementor.ai]
# AI tool integration
ai_tools = ["windsurf", "cursor"]
context_format = "markdown"

# Context preservation
max_context_age = "7d"
min_context_relevance = 0.7

# Memory tiers
active_context_limit = "2w"
progress_history = "1m"
pattern_retention = "1y"
```

### AI Tool-specific Settings
```toml
[tool.mementor.ai.windsurf]
context_injection = true
auto_snapshot = true
memory_format = "three_tier"

[tool.mementor.ai.cursor]
context_sync = true
decision_tracking = true
```

## Documentation Health

### Health Metrics
Configure quality thresholds:

```toml
[tool.mementor.metrics]
# Readability
min_readability_score = 60.0
max_section_depth = 3
optimal_section_length = 250

# Progress tracking
max_todos = 10
max_snapshot_age = "3d"

# Link health
check_external_links = true
validate_internal_refs = true
```

### Alerts and Notifications
```toml
[tool.mementor.alerts]
# Health alerts
notify_on_low_score = true
min_score_threshold = 50

# Update reminders
snapshot_reminder = "1d"
review_reminder = "1w"
```

## Git Integration

### Pre-commit Configuration
In `.pre-commit-config.yaml`:

```yaml
repos:
-   repo: local
    hooks:
    -   id: mementor-snapshot
        name: Generate Documentation Snapshot
        entry: python -m mementor.hooks.pre_commit
        language: python
        pass_filenames: false
        stages: [pre-commit]
        additional_dependencies: ['pystache>=0.6.0']
```

### Git Hook Settings
```toml
[tool.mementor.git]
# Snapshot generation
auto_snapshot = true
snapshot_on_branch = ["main", "develop"]

# Commit messages
snapshot_commit_prefix = "docs"
snapshot_message_template = "docs: update {doc_type} documentation"
```

## Advanced Options

### Template Customization
```toml
[tool.mementor.templates]
# Template settings
custom_templates_dir = "templates/custom"
fallback_template = "default"

# Template variables
company_name = "Your Company"
doc_standards_url = "https://docs.example.com/standards"
```

### Performance Tuning
```toml
[tool.mementor.performance]
# Cache settings
cache_templates = true
cache_snapshots = true
max_cache_size = "100MB"

# Processing
parallel_processing = true
max_workers = 4
```

### Security Settings
```toml
[tool.mementor.security]
# Access control
require_auth = false
allow_external_templates = false

# Content validation
validate_links = true
allow_scripts = false
```

## Example Configurations

### Minimal Setup
```toml
[tool.mementor]
project_name = "my-project"
docs_dir = "docs"

[tool.mementor.ai]
ai_tools = ["windsurf"]

[tool.mementor.metrics]
min_readability_score = 60.0
```

### Full AI Development Setup
```toml
[tool.mementor]
project_name = "ai-project"
docs_dir = "docs/ai-project"
template_dir = "templates"

[tool.mementor.ai]
ai_tools = ["windsurf", "cursor"]
context_injection = true
auto_snapshot = true

[tool.mementor.metrics]
min_readability_score = 70.0
max_section_depth = 3
check_external_links = true

[tool.mementor.git]
auto_snapshot = true
snapshot_on_branch = ["main"]
```

## Best Practices

1. **AI Integration**
   - Enable context injection for seamless AI tool integration
   - Set reasonable context age limits
   - Configure tool-specific settings

2. **Documentation Health**
   - Set realistic quality thresholds
   - Enable automated health checks
   - Configure notifications for quality issues

3. **Git Integration**
   - Use automatic snapshots for main branches
   - Configure meaningful commit messages
   - Enable pre-commit hooks

4. **Performance**
   - Enable caching for better performance
   - Configure parallel processing based on your system
   - Set appropriate cache size limits

## Troubleshooting

### Common Issues

1. **Configuration Not Loading**
   ```bash
   # Verify configuration
   mementor config --verify
   
   # Show current configuration
   mementor config --show
   ```

2. **Git Hook Issues**
   ```bash
   # Reinstall hooks
   mementor hooks --install
   
   # Test hook manually
   mementor hooks --test
   ```

3. **AI Integration Problems**
   ```bash
   # Check AI tool connection
   mementor ai --check
   
   # Verify context injection
   mementor ai --verify-context
   ```
