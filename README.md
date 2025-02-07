# 📚 Mementor

**Your documentation, always up-to-date and healthy**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why Mementor?

🤔 **Ever wondered why your project documentation...**
- Gets outdated so quickly?
- Lacks important context?
- Is hard to maintain?
- Doesn't reflect the current state?

✨ **Mementor solves these problems by:**
- Automatically capturing documentation changes
- Tracking documentation health
- Integrating with your git workflow
- Providing insights into documentation quality

## 🚀 Quick Start

```bash
# Install Mementor
pip install mementor

# Initialize in your project
mementor init

# Start documenting!
vim docs/your-project/activeContext.md
```

## ✨ Key Features

### 🔄 Living Documentation
- **Active Context Tracking**: Capture decisions and changes as they happen
- **Automatic Snapshots**: Documentation versioned with your code
- **Health Metrics**: Know when docs need attention

### 🎯 Smart Integration
- **Git Hooks**: Automatic snapshots on commit
- **Project-specific Spaces**: Isolated documentation per project
- **Template System**: Consistent documentation structure

### 📊 Health Dashboard
- **Readability Scoring**: Ensure docs are easy to understand
- **Progress Tracking**: Monitor documentation completion
- **Link Validation**: Catch broken references early

## 🎯 Use Cases

### For Developers
```bash
# Record a design decision
vim docs/your-project/activeContext.md
git commit -m "docs: add API authentication decision"
# Mementor automatically:
# ✓ Generates snapshot
# ✓ Calculates health metrics
# ✓ Archives the changes
```

### For Tech Leads
```bash
# Check documentation health
mementor health

# Review recent decisions
mementor history --days 7

# Track documentation progress
mementor metrics --trend
```

### For Teams
```bash
# Set up team standards
mementor init --template team-standard

# Monitor documentation quality
mementor report --weekly

# Review documentation changes
mementor diff HEAD~1
```

## 📈 Benefits

### 🎯 Immediate Impact
- **No More Stale Docs**: Automatic updates and health checks
- **Context Preservation**: Capture decisions as they happen
- **Quality Insights**: Know what needs improvement

### 💪 Long-term Value
- **Knowledge Retention**: Never lose important context
- **Reduced Maintenance**: Automated health monitoring
- **Better Collaboration**: Clear, up-to-date documentation

## 🔗 Next Steps

- 📖 [Detailed Usage Guide](docs/mementor_docs/USAGE.md)
- 🛠️ [Configuration Options](docs/mementor_docs/CONFIGURATION.md)
- 🎨 [Template Gallery](docs/mementor_docs/TEMPLATES.md)

## 💡 Contributing

We love contributions! See our [Contributing Guide](CONTRIBUTING.md) for ways to get started.

## 📄 License

MIT © [2025 Mementor](LICENSE)
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
