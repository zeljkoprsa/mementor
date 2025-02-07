# 📚 Mementor

**Supercharge your AI development with living documentation**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Why Mementor?

🤖 **Using AI-powered development tools like Windsurf or Cursor?**
AI assistants work best with up-to-date context about your project. But maintaining this context is challenging:

- Context gets fragmented across conversations
- Key decisions get lost in chat history
- Project state becomes unclear
- AI responses lack important background

✨ **Mementor is your AI development companion:**
- Maintains living context for AI tools
- Tracks decisions and progress automatically
- Keeps documentation in sync with code
- Ensures AI always has the full picture

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

### 🤖 AI-First Documentation
- **Context Management**: Keep AI tools informed about your project state
- **Decision Tracking**: Record and reference architectural choices
- **Progress Snapshots**: Automatic versioning with your code

### 🧠 Three-Tier Memory System
- **Active Context**: Current state and recent decisions (for AI tools)
- **Progress Tracking**: Sprint goals and milestone tracking
- **System Patterns**: Long-term architectural decisions

### 🎯 Smart Integration
- **AI Tool Support**: Ready for Windsurf, Cursor, and other AI assistants
- **Git Hooks**: Automatic context updates
- **Health Metrics**: Ensure documentation serves AI tools effectively

## 🎯 Use Cases

### AI-Driven Development
```bash
# Update context for AI tools
vim docs/your-project/activeContext.md
git commit -m "docs: add authentication flow context"

# Mementor automatically:
# ✓ Updates AI context
# ✓ Preserves decision history
# ✓ Maintains knowledge continuity
```

### Sprint Planning with AI
```bash
# Track sprint progress
mementor progress

# Update sprint context
vim docs/your-project/progress.md

# Let AI analyze progress
mementor analyze --sprint-current
```

### Team Collaboration
```bash
# Share context with AI tools
mementor context --share

# Review AI-assisted decisions
mementor decisions --recent

# Track architectural evolution
mementor patterns --timeline
```

## 📈 Benefits

### 🤖 AI Development
- **Smarter AI Assistance**: AI tools always have current context
- **Continuous Learning**: AI understands your project's evolution
- **Context Preservation**: Key decisions available for future AI interactions

### 💪 Team Empowerment
- **AI-Ready Documentation**: Structured for both humans and AI
- **Knowledge Continuity**: No context loss between AI sessions
- **Reduced Cognitive Load**: Let AI handle context management

## 🔗 Next Steps

- 📖 [Detailed Usage Guide](docs/mementor_docs/USAGE.md)
- 🛠️ [Configuration Guide](docs/mementor_docs/CONFIGURATION.md)
- 🎨 Template Gallery *(coming soon)*

Want to contribute? Help us build the template gallery!

## 💡 Contributing

We love contributions! See our [Contributing Guide](CONTRIBUTING.md) for ways to get started.

## 📄 License

Mementor is open-source software licensed under the [MIT License](LICENSE). © 2025 Zeljko Prsa

Feel free to use it for both personal and commercial projects!
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
