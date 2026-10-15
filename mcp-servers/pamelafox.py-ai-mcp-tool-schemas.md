# MCP tool schema variants

This repo accompanies the talk **"Improving MCP tool schemas to increase agent reliability"**.
[View the slides](https://pamelafox.github.io/py-ai-mcp-tool-schemas/)

It contains:

- A **FastMCP server** that exposes multiple tool schema variants for the same expense-tracking actions
  (e.g., category as `str` vs `Literal` vs `Enum` vs `Annotated[Enum]`).
- **Four agent implementations** (PydanticAI, GitHub Copilot SDK, LangChain, Microsoft Agent Framework)
  that connect to the MCP server over Streamable HTTP.
- An **evaluation harness** that runs 17 test cases across schema variants and generates comparison reports.

## Table of contents

- [Setup](#setup)
- [Run the MCP server](#run-the-mcp-server)
- [Run agents](#run-agents)
- [Run evaluations](#run-evaluations)
- [Tracing with Logfire](#tracing-with-logfire)

## Setup

### Install dependencies

```bash
uv sync
```

### Configure environment variables

Create a `.env` file with:

```env
AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_OPENAI_CHAT_DEPLOYMENT=<your-deployment-name>
```

You also need Azure credentials via `DefaultAzureCredential` (run `az login` for local dev),
or set `AZURE_OPENAI_KEY` for API key auth.

Optional:

- `MCP_SERVER_URL` — defaults to `http://localhost:8000/mcp`
- `LOGFIRE_TOKEN` — enables sending traces to [Logfire](https://logfire.pydantic.dev/)

To use different models, create separate env files (e.g., `.env.gpt4o`, `.env.gpt53codex`)
and pass them with `--env-file`.

## Run the MCP server

```bash
uv run python servers/expenses_mcp.py
```

The server exposes multiple variants of each tool with different schema approaches:

- **Category variants** (`cat_b` through `cat_e`): `Annotated[str]`, `Literal`, `Enum`, `Annotated[Enum]`
- **Date variants** (`date_a` through `date_d`): `str`, `Annotated[str]`, `date`, `Field(pattern=...)`
- **Output variants** (`get_expenses_a` through `get_expenses_c`): `str`, `list[dict]`, `list[Expense]`

## Run agents

Start the MCP server first, then run any agent:

### PydanticAI

```bash
uv run python agents/pydanticai_agent.py
uv run python agents/pydanticai_agent.py --tools add_expense_cat_e --query "Coffee for $5"
uv run python agents/pydanticai_agent.py --reasoning medium --show-tool-calls --show-reasoning
```

### GitHub Copilot SDK

```bash
uv run python agents/copilotsdk_agent.py
uv run python agents/copilotsdk_agent.py --model gpt-5.3-codex --show-tool-calls
```

### LangChain

```bash
uv run python agents/langchain_agent.py
uv run python agents/langchain_agent.py --tools add_expense_cat_c --query "Lunch for $15"
```

### Microsoft Agent Framework

```bash
uv run python agents/agentframework_agent.py
uv run python agents/agentframework_agent.py --tools add_expense_cat_e --reasoning high
```

### Common agent options

| Option | Description |
| -------- | ------------- |
| `--tools` | Tool variant to use (e.g., `add_expense_cat_e`) |
| `--query` | Custom query to send |
| `--model` | Model deployment name |
| `--seed` | Seed for reproducibility (default: 42) |
| `--temperature` | Sampling temperature |
| `--reasoning` | Reasoning effort: none, minimal, low, medium, high, xhigh |
| `--show-tool-calls` | Print extracted tool calls |
| `--show-reasoning` | Print reasoning summary |
| `--env-file` | Path to .env file (PydanticAI only) |

## Run evaluations

The evaluation harness runs a dataset of 17 prompts across schema variants and writes results
to a folder under [evals/runs/](evals/runs/).

```bash
# Run all default variants (category + date)
uv run python evals/runner.py --output evals/runs/my_run

# Category variants only
uv run python evals/runner.py --variants add_expense_cat_b,add_expense_cat_c,add_expense_cat_d,add_expense_cat_e \
  --output evals/runs/my_cat_run

# Date variants only
uv run python evals/runner.py --variants add_expense_date_a,add_expense_date_b,add_expense_date_c,add_expense_date_d \
  --output evals/runs/my_date_run

# With a specific model
uv run python evals/runner.py --env-file .env.gpt4o --seed 42 --temperature 0 \
  --output evals/runs/gpt4o_run

# With reasoning (required for gpt-5 level models)
uv run python evals/runner.py --env-file .env.gpt53codex --reasoning medium \
  --output evals/runs/gpt53codex_run

# Output schema evals (get_expenses variants)
uv run python evals/runner.py --eval-type output --output evals/runs/output_run

# With a different agent framework
uv run python evals/runner.py --agent copilot --deployment gpt-5.3-codex \
  --output evals/runs/copilot_run
```

Each run produces:

- `results.json` — machine-readable results with per-case eval details
- `RESULTS.md` — human-readable summary report

## Tracing with Logfire

Both the MCP server and agents support [Logfire](https://logfire.pydantic.dev/) tracing:

- Set `LOGFIRE_TOKEN` in `.env` to enable
- The agent prints a Logfire trace URL after each run
