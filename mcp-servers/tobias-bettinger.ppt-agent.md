# PPT Agent

AI-powered PowerPoint generation system that creates McKinsey-level professional presentations using a multi-agent architecture.

Built with [pydantic_ai](https://ai.pydantic.dev/), [FastMCP](https://gofastmcp.com/), and [python-pptx](https://python-pptx.readthedocs.io/).

## Architecture

```
┌─────────────────────────────────────────────────┐
│              MCP Client                          │
│  (MCP Inspector / FastMCP CLI / Any MCP Client)  │
└────────────────────┬────────────────────────────┘
                     │ Streamable HTTP
┌────────────────────▼────────────────────────────┐
│           FastMCP Server (v3.1)                   │
│                                                   │
│  Tools:                                           │
│  ├─ create_presentation(topic, audience, style)   │
│  └─ list_styles()                                 │
│                                                   │
│  Elicitations (interactive follow-up questions):  │
│  ├─ Target audience                               │
│  ├─ Presentation style                            │
│  └─ Key message / takeaway                        │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────▼────────────────────────────┐
│        Deterministic Workflow Pipeline            │
│                                                   │
│  Step 1: Research Agent (+ Web Search)            │
│       → ResearchResult                            │
│                                                   │
│  Step 2: Outline Agent                            │
│       → PresentationOutline                       │
│                                                   │
│  Step 3: Content Agent                            │
│       → SlideContentList                          │
│                                                   │
│  Step 4: Design Agent                             │
│       → DesignSpec                                │
│                                                   │
│  Step 5: PPTX Builder (deterministic, no LLM)     │
│       → .pptx file                                │
│                                                   │
│  Step 6: Visual QA Loop (vision model)            │
│       → pptxtoimages → evaluate → iterate         │
└─────────────────────────────────────────────────┘
```

### Design Principles

- **Deterministic workflows** — Agents run in a fixed sequence. Each step produces a typed Pydantic model, eliminating ambiguity between pipeline stages.
- **Structured output everywhere** — Every agent returns a `BaseModel`. The PPTX builder works purely on these models with zero LLM calls.
- **Visual QA loop** — Rendered slides are converted to images via `pptxtoimages`, then evaluated by a vision model for iterative quality improvement.
- **Swappable models** — Configure once in `.env`, swap between Claude (testing) and OpenAI (production).

## Project Structure

```
ppt_agent/
├── pyproject.toml                  # Dependencies & entry point
├── .env.example                    # Environment config template
├── templates/
│   └── base.pptx                   # Base template (replaceable)
├── output/                         # Generated presentations
└── src/ppt_agent/
    ├── config.py                   # Model & path configuration
    ├── models.py                   # All Pydantic models (pipeline contracts)
    ├── server.py                   # FastMCP server with elicitations
    ├── orchestrator.py             # Deterministic 5-step workflow engine
    ├── agents/
    │   ├── research.py             # Web search + insight extraction
    │   ├── outline.py              # SCR narrative + action titles
    │   ├── content.py              # Slide content (bullets, charts, tables)
    │   ├── design.py               # Layout selection + color palette
    │   └── visual_qa.py            # Vision-based quality evaluation
    └── builder/
        ├── template.py             # Base template generator
        └── pptx_builder.py         # Deterministic PPTX renderer
```

## Setup

**Prerequisites:** Python 3.12+, [LibreOffice](https://www.libreoffice.org/) (required by `pptxtoimages` for the visual QA loop)

```bash
# Clone
git clone https://github.com/tobias-bettinger/ppt-agent.git
cd ppt-agent

# Create virtual environment
python3.12 -m venv .venv
source .venv/bin/activate

# Install
pip install -e ".[dev]"

# Configure API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY (or OPENAI_API_KEY)
```

## Usage

### Start the MCP Server

```bash
python -m ppt_agent.server
```

The server starts on `http://localhost:8000/mcp` using Streamable HTTP transport.

### Test with MCP Inspector

```bash
# Terminal 1: Start the server
python -m ppt_agent.server

# Terminal 2: Start the inspector
npx @modelcontextprotocol/inspector
```

In the Inspector UI:
1. Set **Transport Type** to `Streamable HTTP`
2. Set **URL** to `http://localhost:8000/mcp`
3. Click **Connect**
4. Call `create_presentation` — the inspector will show elicitation prompts for audience, style, and key message

### Test with FastMCP CLI

```bash
# List available tools
fastmcp list http://localhost:8000/mcp

# List presentation styles
fastmcp call http://localhost:8000/mcp list_styles

# Generate a presentation (CLI supports interactive elicitations)
fastmcp call http://localhost:8000/mcp create_presentation topic="AI in Healthcare"
```

### Connect from a pydantic_ai Agent

```python
from pydantic_ai import Agent
from pydantic_ai.mcp import MCPServerStreamableHTTP

server = MCPServerStreamableHTTP("http://localhost:8000/mcp")
agent = Agent("anthropic:claude-sonnet-4-20250514", toolsets=[server])

async with agent:
    result = await agent.run("Create a presentation about renewable energy trends for investors")
    print(result.output)
```

## Configuration

All configuration is done via environment variables (`.env` file):

| Variable | Default | Description |
|---|---|---|
| `ANTHROPIC_API_KEY` | — | Anthropic API key (for Claude models) |
| `OPENAI_API_KEY` | — | OpenAI API key (for GPT models) |
| `PPT_AGENT_MODEL` | `anthropic:claude-sonnet-4-20250514` | Model for all content agents |
| `PPT_AGENT_VISION_MODEL` | `anthropic:claude-sonnet-4-20250514` | Model for visual QA (must support vision) |
| `PPT_AGENT_MAX_QA_ITERATIONS` | `2` | Max visual QA optimization rounds |

### Switching to OpenAI

```env
PPT_AGENT_MODEL=openai:gpt-4o
PPT_AGENT_VISION_MODEL=openai:gpt-4o
OPENAI_API_KEY=sk-...
```

## Agents

### Research Agent
Uses the built-in `WebSearchTool` to gather current information. Produces structured insights with action-oriented headlines, quantitative data points, and source citations.

### Outline Agent
Creates a narrative structure using the **Situation → Complication → Resolution (SCR)** framework. Every slide title is an action title that states the key message, not just the topic.

### Content Agent
Generates detailed content per slide: concise bullets (max 8 words each), chart data, table data, quotes, and speaker notes. Follows the "so what" principle.

### Design Agent
Selects color palettes, layout variants, and emphasis elements per slide. Default palette: dark navy (`#003366`), medium blue (`#005B96`), teal accent (`#0097A7`).

### Visual QA Agent
Evaluates rendered slide images on a 1–10 scale across visual hierarchy, professional appearance, white space, data visualization clarity, and consistency. Scores below 7 trigger improvement suggestions.

## Slide Types

The builder supports 10 slide types:

| Type | Description |
|---|---|
| `title` | Full-bleed dark title slide |
| `agenda` | Agenda / table of contents |
| `section_divider` | Section break with dark background |
| `content` | Standard slide with action title + bullets |
| `two_column` | Side-by-side comparison layout |
| `chart` | Bar, column, line, pie, or stacked bar chart |
| `table` | Formatted data table with styled header |
| `quote` | Centered quote with attribution |
| `key_takeaway` | Bold headline with supporting points |
| `closing` | Thank you / contact slide |

## Custom Templates

Replace `templates/base.pptx` with your own 16:9 PowerPoint template. The builder uses a blank slide layout and creates all shapes programmatically, so any template with at least one blank layout will work.

To regenerate the default template:

```bash
python -m ppt_agent.builder.template
```

## License

MIT
