# PPTX MCP Server

A Model Context Protocol (MCP) server that enables AI assistants to programmatically generate PowerPoint (`.pptx`) presentations. It acts as an engine that clones slide layouts from a master template, injecting text and images dynamically.

Built with Python and `python-pptx`.

---

## How It Works

This server expects a directory containing:
1. **Master templates (`.pptx`)**: Your corporate template with predefined slide layouts.
2. **Schemas (`.schema.yaml`)**: Companion files for each template that map semantic field names (like `title` or `photo`) to exact shape positions and styling on the slides.

The AI assistant can query the schema to understand the available slide types and then request a full presentation generation.

## Available Tools

* `pptx_get_schema`: Returns the slide types available in a `.pptx` template and the fields each slide type accepts. Call this before generating to know the required structure.
* `pptx_generate`: Generates a `.pptx` presentation from a template and a structured list of slides. Injects text and downloads external image URLs to place them on the slides. Returns the local path of the generated file.

---

## Setup & Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Themetralla3000/pptx-mcp-server.git
   cd pptx-mcp-server
   ```
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```
3. Configure the environment variables (or `.env` file):
   ```bash
   cp .env.example .env
   ```

## Configuration

Set up the paths where templates are stored and where generated files should be saved.

```env
PPTX_TEMPLATES_DIR=/absolute/path/to/templates
PPTX_OUTPUT_DIR=/absolute/path/to/output
```

## Schema Format Example

To use a template named `base.pptx`, create a `base.schema.yaml` file in your templates directory:

```yaml
slide_types:
  title_slide:
    source_index: 0
    fields:
      - name: main_title
        type: text
        shape_index: 0
      - name: subtitle
        type: text
        shape_index: 1

  image_slide:
    source_index: 1
    fields:
      - name: title
        type: text
        shape_index: 0
      - name: photo
        type: image
        shape_index: 1
```

## Usage with Claude Desktop / Cursor

To use this MCP with Claude Desktop or Cursor, configure it to run the Python script within its virtual environment:

```json
{
  "mcpServers": {
    "pptx": {
      "command": "/absolute/path/to/pptx-mcp-server/venv/bin/python",
      "args": ["/absolute/path/to/pptx-mcp-server/server.py"],
      "env": {
        "PPTX_TEMPLATES_DIR": "/absolute/path/to/templates",
        "PPTX_OUTPUT_DIR": "/absolute/path/to/output"
      }
    }
  }
}
```

## License

MIT License

## 🛠️ Adding New Templates

Creating the `.schema.yaml` by hand can be difficult because you need to know the exact internal `shape_index` of every element in your PowerPoint file.

To solve this, a helper script is included:

```bash
python extract_schema.py /path/to/templates/my_new_presentation.pptx
```

This script will read your `.pptx` file and generate a base `my_new_presentation.schema.yaml` right next to it, listing every text box and image placeholder along with their internal IDs and sample text. 

You just need to open the generated YAML and rename the fields to semantic names (e.g. `title`, `company_logo`) and delete the shapes you don't want the AI to be able to modify.
