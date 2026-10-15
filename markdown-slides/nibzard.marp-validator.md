# Marp Slide Validator

A simple tool that validates your Marp presentations for readability and formatting.

## What It Does

- Checks slide content length and density
- Validates title lengths and bullet point counts
- Analyzes code blocks and special content
- Provides scoring from 0-100 for each slide
- Gives objective feedback without prescriptive suggestions

## Quick Start

```bash
# Basic validation
python validate_slides.py presentation.md

# With custom config
python validate_slides.py presentation.md --config custom_config.yaml
```

## Understanding Results

Each slide gets a score and status:
- ✅ **70-100**: Good to go
- ❌ **Below 70**: Needs attention

The output shows:
- Overall statistics (total slides, average score)
- Individual slide scores with specific issues
- Content analysis (lengths, bullets, titles)

## Default Rules

- **Titles**: Max 35 chars (main), 50 chars (subtitle)
- **Content**: Max 350 chars (450 for exercise slides)
- **Bullets**: Max 6 per slide, 80 chars each
- **Code**: Max 10 lines (simple), 5 lines (complex)
- **Total lines**: Max 15 per slide

## Configuration

Create `slide_config.yaml` to customize rules:

```yaml
validation_rules:
  title:
    max_length_main: 35
    max_length_sub: 50
  content:
    max_characters: 350
    max_bullets: 6
    max_bullet_length: 80
    exercise_max_characters: 450
    min_characters: 50
  code:
    max_lines_simple: 10
    max_lines_complex: 5
```

## Scoring

Points deducted for issues:
- Missing title: -20
- Content too long: -15
- Title too long: -10
- Too many bullets: -10
- Long bullets: -5
- Code too long: -8
- Content too short: -5

## Troubleshooting

**Fewer slides than expected?** Make sure `---` delimiters are on separate lines.

**False positives?** Adjust the configuration limits to match your needs.

**Performance issues?** Split large presentations into smaller files.

## License

Free to use and adapt for your presentation needs.