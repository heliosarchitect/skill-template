---
name: skill-name
description: Brief one-line description of what this skill does
homepage: https://github.com/yourusername/your-skill
emoji: 🛠️
metadata:
  clawdbot:
    requires:
      env:
        - REQUIRED_API_KEY
      bins:
        - jq
        - curl
---

# Skill Name

Brief description of what this skill does and why it's useful.

## What It Does

- Feature 1
- Feature 2
- Feature 3

## Requirements

- **Environment variables:**
  - `REQUIRED_API_KEY` - Description of what this key does
  
- **System binaries:**
  - `jq` - JSON processor
  - `curl` - HTTP client

## Installation

### Manual Installation

```bash
# Clone to your skills directory
cd ~/.openclaw/workspace/skills/
git clone https://github.com/yourusername/your-skill.git skill-name
```

### Via ClawHub (after publishing)

```bash
openclaw skill install skill-name
```

## Configuration

Set required environment variables in your OpenClaw config or shell:

```bash
export REQUIRED_API_KEY=your_key_here
```

Or add to `~/.openclaw/openclaw.json`:

```json
{
  "env": {
    "REQUIRED_API_KEY": "your_key_here"
  }
}
```

## Usage

### Basic Usage

```bash
./scripts/main_script.sh arg1 arg2
```

### From OpenClaw

The skill is automatically available when loaded. OpenClaw will detect and offer it based on context.

### Examples

See `examples/` directory for common use cases.

## Files

- `SKILL.md` - This file (skill documentation + frontmatter)
- `scripts/` - Executable scripts and tools
- `references/` - Documentation, guides, links
- `assets/` - Images, data files, templates
- `examples/` - Example usage and sample outputs

## Development

### Testing

```bash
# Run tests
./scripts/test.sh
```

### Contributing

1. Fork the repo
2. Create a feature branch
3. Make your changes
4. Submit a PR

## Troubleshooting

### Common Issues

**Problem:** Script fails with "command not found"
- **Solution:** Install required system binaries (see Requirements)

**Problem:** API authentication fails
- **Solution:** Check that `REQUIRED_API_KEY` is set correctly

## License

MIT License - see LICENSE file

## Author

[Your Name](https://github.com/yourusername)

## Links

- GitHub: https://github.com/yourusername/your-skill
- Documentation: (link to docs if separate)
- Issues: https://github.com/yourusername/your-skill/issues
