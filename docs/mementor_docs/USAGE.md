# Using Mementor

This guide explains how to effectively use Mementor in your project for documentation management.

## Table of Contents
1. [Basic Usage](#basic-usage)
2. [Git Integration](#git-integration)
3. [Health Metrics](#health-metrics)
4. [Templates](#templates)
5. [Best Practices](#best-practices)

## Basic Usage

### Initializing a Project

```bash
# Initialize Mementor in your project
mementor init

# Initialize with custom configuration
mementor init --config custom_config.toml

# Initialize in a specific directory
mementor init /path/to/project
```

### Managing Documentation

1. **Active Context** (`activeContext.md`):
   - Record immediate decisions and changes
   - Track current tasks and next steps
   - Document recent technical discussions

2. **Progress Tracking** (`progress.md`):
   - Log completed milestones
   - Track ongoing work
   - Plan upcoming features

3. **System Patterns** (`systemPatterns.md`):
   - Document architectural decisions
   - Record design patterns
   - Track long-term evolution

## Git Integration

### Pre-commit Hook

Mementor automatically generates snapshots when documentation changes:

1. **Installation**:
   ```bash
   pip install pre-commit
   pre-commit install
   ```

2. **Configuration** (`.pre-commit-config.yaml`):
   ```yaml
   repos:
   -   repo: local
       hooks:
       -   id: mementor-snapshot
           name: Generate Documentation Snapshot
           entry: python3 scripts/hooks/pre_commit.py
           language: python
           pass_filenames: false
           stages: [pre-commit]
           additional_dependencies: ['pystache>=0.6.0']
   ```

3. **Usage**:
   - Snapshots are generated automatically on commit
   - Only runs when documentation files change
   - Snapshots are automatically staged

## Health Metrics

Mementor provides comprehensive documentation health metrics:

### Content Metrics
- Word count and reading time
- Readability score (Flesch reading ease)
- Content freshness (time since last update)

### Structure Metrics
- Section count and depth
- Average section length
- Code block count

### Progress Metrics
- Task completion percentage
- Open TODO count
- Snapshot frequency

### Link Health
- Valid link count
- Broken link detection
- Reference validation

## Templates

### Default Templates
Mementor provides several default templates:
- Active context template
- Progress tracking template
- System patterns template
- Snapshot template

### Custom Templates
Create custom templates in your project's `templates` directory:

1. **Template Structure**:
   ```mustache
   {{! templates/custom.mustache }}
   # {{ title }}

   ## Overview
   {{ description }}

   ## Sections
   {{#sections}}
   ### {{ name }}
   {{ content }}
   {{/sections}}
   ```

2. **Metadata Support**:
   ```yaml
   version: 1.0.0
   created_at: 2025-02-07
   dependencies:
     - name: pystache
       version: 0.6.7
   ```

## Best Practices

### Documentation Organization
1. **Keep Active Context Current**:
   - Update after significant decisions
   - Remove outdated information
   - Link to detailed documentation

2. **Regular Snapshots**:
   - Commit documentation changes separately
   - Review snapshot metrics
   - Address health issues promptly

3. **Template Usage**:
   - Use consistent templates
   - Include required metadata
   - Follow section structure

### Health Metrics
1. **Monitor Trends**:
   - Track readability scores
   - Watch completion rates
   - Check link health

2. **Quality Targets**:
   - Maintain readability above 60
   - Keep section depth under 3
   - Resolve broken links quickly

3. **Regular Reviews**:
   - Review metrics weekly
   - Update stale content
   - Clean up TODOs

## Troubleshooting

### Common Issues

1. **Snapshot Generation Fails**:
   ```bash
   # Check git hook installation
   pre-commit install --force
   
   # Verify template syntax
   mementor verify-templates
   ```

2. **Metrics Seem Incorrect**:
   ```bash
   # Regenerate metrics
   mementor analyze docs/your-project-docs
   
   # View detailed metrics
   mementor metrics --verbose
   ```

3. **Template Issues**:
   ```bash
   # Validate templates
   mementor validate-templates
   
   # Reset to defaults
   mementor reset-templates
   ```
