<p align="center">
  <h1 align="center">🧪 MARP</h1>
  <p align="center"><strong>Multi-Agent Research Platform</strong></p>
  <p align="center">
    A collaborative AI framework for accelerating scientific discovery through<br/>
    multi-agent orchestration, autonomous tool construction, and intelligent code generation.
  </p>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#architecture">Architecture</a> •
  <a href="#quick-start">Quick Start</a> •
  <a href="#usage">Usage</a> •
  <a href="#project-structure">Project Structure</a> •
  <a href="#license">License</a>
</p>

---

## Overview

**MARP** (Multi-Agent Research Platform) is a modular, extensible AI system designed to assist researchers — particularly in materials science, chemistry, and biology — through an end-to-end collaborative workflow. It pairs a **Project Coordinator Agent** with a **Domain Expert Agent** (e.g., a materials scientist) that engage in structured multi-round dialogue to formulate research plans, autonomously build and test computational tools, generate production-grade executable code, and iteratively refine results.

Unlike single-agent coding assistants, MARP implements a *full research lifecycle*: from hypothesis discussion and plan validation, through automated tool construction and testing, to code execution, result analysis, and experimental design.

## Features

### 🤖 Multi-Agent Collaboration
- **Assistant Agent** — Acts as project coordinator: manages workflow phases, generates code, orchestrates tool chains, and drives the research pipeline forward.
- **Materials Science Expert Agent** — Provides scientific judgment: evaluates computation plans, interprets results, and decides when to proceed to experimental validation.
- **Hierarchical Executor (META + EXEC)** — A two-tier agent system for complex code execution tasks: a META-planner decomposes problems, while an EXEC-agent carries out individual steps using MCP tool servers.

### 🔧 Autonomous Tool Construction
- **On-the-fly Tool Generation** — Analyzes the research plan against existing tool inventories and automatically generates missing tools as production-grade Python modules.
- **Automated Testing & Enhancement** — Each generated tool undergoes automated testing with structured test reports. Tools not reaching production quality are iteratively enhanced (up to 3 rounds) until all quality gates pass.
- **Tool Description Management** — Auto-generates JSONL-based tool descriptions via LLM analysis of source code, enabling dynamic tool discovery and registration.

### 💻 Intelligent Code Generation & Execution
- **Plan-to-Code Pipeline** — Converts finalized research plans into complete, executable Python scripts with proper tool imports, process logging, and structured output.
- **Smart Execution with Auto-Debug** — Executes code in a sandboxed environment with automatic error detection and iterative repair.
- **Import Whitelist Security** — Sandboxed code execution with configurable import whitelists to prevent unauthorized module usage.

### 📚 Extensible Domain Toolkits
- **Materials Science** — DFT calculations (via ORB models), structure optimization, adsorption stability analysis, Materials Project API integration, MOF/COF tools.
- **Chemistry** — RDKit-based cheminformatics (3 modules), ML chemistry tools, reaction prediction (RXN4Chemistry), NCBI integration.
- **Biology** — Protein analysis tools, sequence analysis, biological common utilities.
- **General** — Data processing, statistical analysis, common scientific computing utilities.

### 🔍 Literature Research Engine
- **Multi-Publisher Crawlers** — Automated literature retrieval from Elsevier (ScienceDirect), Nature/Springer, and Wiley publishers.
- **Keyword-based Search** — YAML-configurable keyword prompts for targeted literature discovery.
- **Document Processing Pipeline** — Structured extraction and processing of academic papers.

### 🌐 MCP Tool Server Ecosystem
A suite of [Model Context Protocol](https://modelcontextprotocol.io/) (MCP) servers providing the Executor agent with runtime capabilities:

| Server | Capabilities |
|--------|-------------|
| `code_agent` | Sandboxed code execution, workspace file management, terminal commands |
| `search_tool` | Privacy-respecting web search via SearxNG |
| `documents_tool` | Document parsing (DOCX, PPTX, PDF via Chunkr) |
| `excel_tool` | Excel/CSV data processing |
| `image_tool` | Image analysis and processing |
| `video_tool` | Video download, keyframe extraction, multimodal Q&A |
| `math_tool` | Mathematical computation |
| `ai_crawl` | AI-powered web crawling (Crawl4AI) |

### 🔌 Multi-Provider LLM Support
Seamlessly switch between LLM backends with a unified API client:
- **Qwen** (Alibaba DashScope) — Default provider
- **DeepSeek** — Chat and code-specialized models
- **Kimi** (Moonshot) — Long-context reasoning
- **Azure OpenAI** — Enterprise deployment
- **OpenAI** — GPT-4o and beyond

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         MARP Platform                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────────┐     Dialogue      ┌────────────────────┐  │
│  │  Assistant Agent  │◄────────────────►│  Scientist Agent   │  │
│  │  (Coordinator)    │   Multi-round     │  (Domain Expert)   │  │
│  └────────┬─────────┘   Discussion       └────────────────────┘  │
│           │                                                      │
│     ┌─────┴──────────────────────────────────────┐              │
│     │             Workflow Engine                  │              │
│     │  Planning → Tool Build → Code Gen → Review  │              │
│     └─────┬──────────┬──────────┬────────────────┘              │
│           │          │          │                                │
│  ┌────────▼──┐ ┌─────▼────┐ ┌──▼──────────────┐               │
│  │   Tool    │ │  Code    │ │   Hierarchical   │               │
│  │  Builder  │ │Generator │ │ Executor (META/  │               │
│  │          │ │          │ │    EXEC Agents)  │               │
│  └────┬─────┘ └──────────┘ └────────┬─────────┘               │
│       │                              │                          │
│  ┌────▼──────────────────────────────▼──────────┐              │
│  │              MCP Tool Servers                  │              │
│  │  code_agent │ search │ docs │ excel │ video   │              │
│  └───────────────────────────────────────────────┘              │
│                                                                 │
│  ┌──────────────────────────────────────────────┐              │
│  │           Domain Tool Libraries               │              │
│  │  Materials │ Chemistry │ Biology │ General    │              │
│  └──────────────────────────────────────────────┘              │
│                                                                 │
│  ┌──────────────────────────────────────────────┐              │
│  │         Literature Research Engine            │              │
│  │  Elsevier │ Nature │ Wiley  │ Processors     │              │
│  └──────────────────────────────────────────────┘              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### Workflow Phases

MARP's collaborative workflow consists of **8 phases**:

1. **Project Initialization** — Set research goal and configure workspace.
2. **Planning & Discussion** — 3–10 rounds of structured dialogue between the Assistant and Scientist agents to formulate a technically sound plan.
3. **Final Plan Generation** — Synthesize all discussion into a detailed, executable plan document.
4. **Tool Construction & Testing** — Analyze the plan, generate missing tools, run automated tests, and iteratively enhance until production-ready.
5. **Code Generation & Execution** — Generate executable Python scripts based on the plan and available tools, then execute with auto-debug.
6. **Result Review & Decision** — Scientist agent evaluates results and decides: proceed to experiment, refine approach, or continue computation.
7. **Experimental Design** *(optional)* — Multi-round discussion on experimental preparation and characterization plans.
8. **Final Report** — Generate a comprehensive research report summarizing all findings.

## Quick Start

### Prerequisites

- Python ≥ 3.11
- [uv](https://docs.astral.sh/uv/) (recommended) or pip

### Installation

```bash
# Clone the repository
git clone https://github.com/your-org/marp.git
cd marp

# Install with uv (recommended)
uv sync

# Or install with pip
pip install -e .
pip install -r requirements.txt
```

### Configuration

1. Copy the environment template:
```bash
cp .env.example .env
```

2. Edit `.env` and fill in your API keys:
```env
# Required: At least one LLM provider
OPENAI_API_KEY=your_openai_key
DEEPSEEK_API_KEY=your_deepseek_key
QWEN_API_KEY=your_qwen_key

# Optional services
JINA_API_KEY=your_jina_key          # For web fetching
ASSEMBLYAI_API_KEY=your_key         # For audio transcription
CHUNKR_API_KEY=your_key             # For document parsing
GEMINI_API_KEY=your_key             # For multimodal tasks
```

## Usage

### CLI Interface

```bash
# Run a collaborative research workflow
marp run --goal "Design high-capacity lithium battery cathode materials" \
         --api-key YOUR_API_KEY

# Run with custom settings
marp run --goal "Screen bifunctional OER/ORR catalysts" \
         --log-dir ./my_sessions \
         --max-rounds 8

# List available tools
marp tools

# Run system tests
marp test --api-key YOUR_API_KEY
```

### Python API

```python
from marp import EnhancedAssistantAgent

# Initialize the assistant agent
agent = EnhancedAssistantAgent(
    api_key="your_api_key",
    workspace="./my_workspace",
    provider="qwen",                          # or 'deepseek', 'kimi', 'azure'
    mature_tools_paths=[
        "func_tools/Materials",
        "func_tools/Modelling"
    ]
)

# Run the full collaborative workflow
result = agent.run_collaborative_workflow(
    initial_prompt="Design SAC catalysts with optimal OER/ORR bifunctional activity"
)

# Access results
print(f"Status: {result['status']}")
print(f"Workspace: {result['workspace']}")
print(f"Summary: {result['summary']}")
```

### Using Individual Components

```python
from marp.api_client import APIClient
from marp.code_gen_executor import CodeGenerator
from marp.tool_builder import ToolBuilder

# Initialize API client
client = APIClient(api_key="your_key", provider="qwen")

# Generate tools from descriptions
builder = ToolBuilder(api_key="your_key", provider="qwen")
tool_prompts = builder.generate_tool_prompts(
    plan="Your research plan...",
    project_goal="Your goal...",
    available_tools_description="Existing tools..."
)
tool_files = builder.tool_construction(tool_prompts)

# Generate executable code
generator = CodeGenerator(provider="qwen", api_key="your_key")
result = generator.generate_code_by_your_tools(
    task_name="analysis_pipeline",
    plan="Detailed plan...",
    tools_description="Tool descriptions...",
    tool_paths=["/path/to/tool1.py", "/path/to/tool2.py"],
    workspace="./workspace"
)
```

## Project Structure

```
marp/
├── marp/                          # Core framework
│   ├── __init__.py                # Package entry, version, exports
│   ├── assistant_agent.py         # Project Coordinator Agent (main orchestrator)
│   ├── materials_scientist_agent.py  # Domain Expert Agent
│   ├── api_client.py              # Unified multi-provider LLM client
│   ├── code_gen_executor.py       # Code generation engine
│   ├── code_execuagent.py         # Hierarchical executor (META/EXEC agents)
│   ├── tool_builder.py            # Autonomous tool construction & testing
│   ├── tool_manager.py            # Tool description management
│   ├── tool_descriptions.py       # Tool description formatting
│   ├── logger.py                  # Logging & dialogue compression
│   ├── file_manager.py            # Session data persistence
│   └── cli.py                     # Command-line interface
│
├── func_tools/                    # Domain tool libraries
│   ├── agent_tools.py             # DFT, ML, prediction & analysis tools
│   ├── BASE/                      # Base scientific tool collections
│   │   ├── Biology/               # Protein analysis, sequence tools
│   │   ├── Chemical/              # RDKit, ML chemistry, reaction prediction
│   │   ├── General/               # Common utilities
│   │   ├── Material/              # Materials Project, MOF, adsorption tools
│   │   └── utils/                 # Shared utilities
│   ├── Materials/                 # Materials science tool descriptions
│   ├── Modelling/                 # Modelling tool descriptions
│   └── literaturer_tool/          # Literature research engine
│       ├── crawler/
│       │   └── crawlers/          # Publisher-specific crawlers
│       │       ├── elsevier.py    # Elsevier/ScienceDirect
│       │       ├── nature.py      # Nature/Springer
│       │       └── wiley.py       # Wiley Online Library
│       └── processors/           # Document processing pipeline
│
├── server/                        # MCP tool servers
│   ├── code_agent.py              # Sandboxed code execution server
│   ├── search_tool.py             # SearxNG web search server
│   ├── documents_tool.py          # Document parsing server
│   ├── excel_tool.py              # Excel/CSV processing server
│   ├── image_tool.py              # Image analysis server
│   ├── video_tool.py              # Video processing server
│   ├── math_tool.py               # Math computation server
│   ├── ai_crawl.py                # AI-powered web crawling server
│   ├── jina_fetch_tool.py         # Jina web fetching
│   ├── serp_search.py             # SERP search integration
│   └── interpreters/              # Code execution interpreters
│       └── interpreters.py        # Docker, Jupyter, Subprocess, E2B
│
├── pyproject.toml                 # Project metadata & dependencies
├── requirements.txt               # Pip requirements
├── .env.example                   # Environment variable template
├── LICENSE                        # MIT License
└── README.md                      # This file
```

## Workspace Output Structure

Each workflow session generates an organized workspace:

```
workspace/
├── logs/                          # Dialogue logs and activity records
│   ├── assistant_activity.log     # Full activity log
│   ├── scientist_*.log            # Scientist agent decisions
│   └── final_plan_*.md            # Generated research plan
├── tools/                         # Auto-generated tool code
│   ├── tool_name.py               # Generated tool modules
│   ├── test_report_*.md           # Tool test reports
│   └── test_summary_report.md     # Overall test summary
└── *.py, *.json                   # Execution scripts and results
```

## Key Dependencies

| Package | Purpose |
|---------|---------|
| `openai` | LLM API client (OpenAI-compatible) |
| `fastmcp` | Model Context Protocol servers |
| `pandas` / `numpy` | Data processing and analysis |
| `scikit-learn` / `xgboost` | Machine learning models |
| `matplotlib` / `seaborn` | Data visualization |
| `crawl4ai` | AI-powered web crawling |
| `tiktoken` | Token counting for context management |
| `tenacity` | Retry logic for API calls |
| `loguru` / `colorlog` | Structured logging |
| `yt-dlp` / `opencv-python` | Video processing |
| `chunkr-ai` | Document parsing |

## Contributing

Contributions are welcome! Please follow these guidelines:

1. **Fork** the repository and create your feature branch.
2. **Follow** PEP 8 style conventions.
3. **Include** type hints and docstrings for all public APIs.
4. **Write** tests for new tools following the existing test pattern.
5. **Submit** a pull request with a clear description of changes.

### Adding New Domain Tools

1. Create a new Python module in the appropriate `func_tools/BASE/` subdirectory.
2. Follow the standard tool function signature returning `Dict[str, Any]` with fields: `result`, `process_log`, `saved_files`, `status`, `error`.
3. Include a `tool_name_dict.py` for tool name mapping.
4. Run `ToolManager.descriptions_update()` to auto-generate JSONL descriptions.

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---
