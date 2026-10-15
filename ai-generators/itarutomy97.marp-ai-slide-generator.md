# Marp AI Slide Generator

AI-powered slide generator using [Marp](https://marp.app/). Create beautiful presentations from JSON with AI assistance.

## Features

- **JSON-based slide definition**: Define slides in JSON format, generate Markdown automatically
- **30+ built-in templates**: Professional layouts ready to use
- **AI Agent integration**: Works with Claude, GPT, Gemini and other AI agents via AGENTS.md
- **PDF/PPTX export**: Convert to PDF or PowerPoint with a single command
- **Image generation support**: Integrate with AI image generation via nano-banana skill

## Quick Start

```bash
# Install dependencies
npm install

# Generate slides from JSON
node generator/md_build.js projects/sample/slides.json

# Convert to PDF
./generator/pdf_build.sh projects/sample/slides.marp.md

# Convert to PPTX
./generator/pptx_build.sh projects/sample/slides.marp.md
```

## VS Code Setup

To preview slides in VS Code with the custom theme:

### 1. Install Marp for VS Code

Install the [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension.

### 2. Configure Custom Theme

1. Open VS Code Settings (`Cmd+,` or `Ctrl+,`)
2. Search for "Marp: Themes"
3. Click "Add Item" and enter: `./theme/deskrex.css`

Or add to your `.vscode/settings.json`:

```json
{
  "markdown.marp.themes": [
    "./theme/deskrex.css"
  ]
}
```

### 3. Preview Slides

Open any `.marp.md` file and click the preview icon in the top right corner.

![VS Code Marp Preview](assets/screenshots/vscode-marp-preview.png)

## Usage

### 1. Define slides in JSON

```json
{
  "meta": {
    "theme": "deskrex",
    "header": "Presentation Title",
    "footer": "@your-handle"
  },
  "slides": [
    {
      "type": "title-cover",
      "data": {
        "mainTitle": "Main Title",
        "subTitle": "Subtitle"
      }
    },
    {
      "type": "section-divider",
      "data": {
        "title": "Chapter 1",
        "subtitle": "Section Name"
      }
    }
  ]
}
```

### 2. Generate Markdown

```bash
# Basic usage (generates input.marp.md)
node generator/md_build.js <input.json>

# With timestamp
node generator/md_build.js <input.json> --timestamp

# Specify output path
node generator/md_build.js slides.json output/presentation.md
```

### 3. Convert to PDF/PPTX

```bash
# PDF (with image compression)
./generator/pdf_build.sh <input.md>

# PDF (no compression)
./generator/pdf_build.sh --no-compress <input.md>

# PPTX
./generator/pptx_build.sh <input.md>

# Direct Marp CLI
npx @marp-team/marp-cli@latest file.md -o output.html
npx @marp-team/marp-cli@latest file.md --pdf -o output.pdf
npx @marp-team/marp-cli@latest file.md --pptx-editable --allow-local-files
```

## Project Structure

```
.
├── package.json          # Dependencies
├── AGENTS.md             # AI Agent instructions
├── generator/            # JSON→Markdown generation tools
│   ├── md_build.js       # JSON → Markdown converter
│   ├── pdf_build.sh      # Markdown → PDF converter
│   ├── pptx_build.sh     # Markdown → PPTX converter
│   ├── merge-json.js     # Merge split JSON files
│   ├── templates/        # Handlebars templates (.hbs) and previews (.md)
│   └── README.md         # Template documentation
├── assets/               # Images and media files
├── projects/             # Your presentation projects
├── theme/                # Custom CSS theme
│   └── deskrex.css       # Theme with Tailwind CSS + Font Awesome
└── .claude/              # Claude Code skills
    └── skills/
        └── nano-banana/  # AI image generation skill
```

## Available Templates

See `generator/templates/` for 30+ available templates including:

- `title-cover` - Title slide
- `section-divider` - Section divider
- `two-column-text` - Two column layout
- `image-grid` - Image grid
- `timeline` - Timeline visualization
- `comparison-table` - Comparison table
- And many more...

Full list: `generator/README.md`

## Split JSON Management

For large presentations, split JSON files by section:

```
projects/my-presentation/
├── part_00_intro.json          # Merged
├── part_01_main.json           # Merged
├── part_02_conclusion.json     # Merged
└── slides.json                 # Output
```

Merge and build:
```bash
node generator/merge-json.js <project-dir> --build
```

## AI Agent Integration

This project includes `AGENTS.md` with detailed instructions for AI agents (Claude, GPT, Gemini). The AI can:

- Generate slides from natural language descriptions
- Choose appropriate templates automatically
- Create professional presentations with consistent styling

### Using with Claude Code

1. Open the project in Claude Code
2. Ask Claude to create a presentation
3. Claude will use the templates and generate slides

### Image Generation

Use the `nano-banana` skill (`.claude/skills/nano-banana/`) to generate images with Gemini API.

**Required Setup**: To use Nano Banana Pro, you must set the `GOOGLE_API_KEY` environment variable in `~/.claude/settings.json`:

```json
{
  "env": {
    "GOOGLE_API_KEY": "your-google-api-key-here"
  }
}
```

Example usage in slides:

```json
{
  "type": "centered-image",
  "data": {
    "title": "AI Vision",
    "image": {
      "src": "placeholder.png",
      "alt": "[Generate] Futuristic office with AI robots and humans collaborating"
    }
  }
}
```

## Theme Features

The `deskrex` theme includes:

- **Tailwind CSS** - Utility-first styling
- **Font Awesome 6** - Icon support
- **Mermaid diagrams** - Flowcharts, sequence diagrams, etc.

### Icons

```html
<i class="fa-solid fa-rocket fa-2x text-blue-600"></i>
```

### Mermaid

Add to slide header:
```html
<script type="module">
  import mermaid from 'https://cdn.jsdelivr.net/npm/mermaid@10/dist/mermaid.esm.min.mjs';
  mermaid.initialize({ startOnLoad: true });
</script>
```

Use in slides:
```html
<div class="mermaid">
graph TD;
    A[Start] --> B{Decision};
    B -->|Yes| C[Action A];
    B -->|No| D[Action B];
</div>
```

## Important Notes

### CSS Styling

Marp ignores inline `style=""` attributes. Use CSS classes only:

```html
<!-- Wrong -->
<div style="width: 60%;">

<!-- Correct -->
<div class="w-3/5">
```

### Absolute Positioning

In Marp, `<section>` has `position: relative`. Use `absolute` directly:

```html
<!-- Correct -->
<div class="absolute right-0 top-0">
  <img src="image.jpg">
</div>
```

### Size Guidelines

Keep elements small for 16:9 slides:

| Element | Recommended | Too Large |
|---------|-------------|-----------|
| Title font | `text-2xl` | `text-4xl+` |
| Body font | `text-xs` | `text-lg+` |
| Padding | `p-3`~`p-4` | `p-6+` |
| Icons | `w-10 h-10` | `w-16+` |

## Dependencies

- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Handlebars](https://handlebarsjs.com/)
- Optional: Ghostscript (for PDF compression)

## License

MIT

## Links

- [Marp Documentation](https://marpit.marp.app/)
- [Marp CLI](https://github.com/marp-team/marp-cli)
- [Tailwind CSS](https://tailwindcss.com/)
- [Font Awesome](https://fontawesome.com/icons)
- [Mermaid](https://mermaid.js.org/)
