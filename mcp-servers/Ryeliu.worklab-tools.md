# worklab-tools — MCP Server for Personal Knowledge Management

A [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) server that provides AI-powered tools for knowledge management, including semantic search, audio transcription, image generation, and PPT creation.

Built for use with [Claude Code](https://claude.ai/claude-code) and the [Knowledge](https://github.com/Ryeliu/knowledge) system.

## Tools

| Tool | Description |
|------|-------------|
| `search_knowledge(query, type?, company?, person?)` | Semantic search over knowledge base (ChromaDB + bge-m3) |
| `index_knowledge()` | Full rebuild of vector index from all markdown files |
| `upsert_knowledge()` | Incremental index update (MD5 diff, only re-index changed files) |
| `generate_ppt(topic, context_text?, page_count?)` | Generate PPT: plan outline → slide images → PDF output |
| `generate_image(prompt, filename?)` | Generate image from text description (Gemini) |
| `transcribe_audio(file_path, model_size?)` | Speech-to-text with speaker diarization (Whisper + pyannote) |
| `register_voiceprint(name, file_path)` | Register speaker voiceprint for future identification |

## Setup

```bash
# Clone
git clone https://github.com/Ryeliu/worklab-tools.git
cd worklab-tools

# Install dependencies (requires Python 3.12+, uv recommended)
uv sync

# Configure environment
cp .env.example .env
# Edit .env with your API keys

# Run
uv run mcp run server.py
```

## Environment Variables

Create a `.env` file:

```
GEMINI_API_KEY=your_google_ai_studio_key
HF_TOKEN=your_huggingface_token
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
OPENROUTER_API_KEY=your_openrouter_key
```

| Variable | Required For | Source |
|----------|-------------|--------|
| `GEMINI_API_KEY` | `generate_image` | [Google AI Studio](https://aistudio.google.com/apikey) |
| `HF_TOKEN` | `transcribe_audio`, `register_voiceprint` | [HuggingFace](https://huggingface.co/settings/tokens) |
| `OPENROUTER_API_KEY` | `generate_ppt` | [OpenRouter](https://openrouter.ai/keys) |

## Register with Claude Code

Add to your Claude Code MCP settings:

```json
{
  "mcpServers": {
    "worklab-tools": {
      "command": "uv",
      "args": ["run", "--directory", "/path/to/worklab-tools", "mcp", "run", "server.py"],
      "env": {
        "GEMINI_API_KEY": "...",
        "HF_TOKEN": "...",
        "OPENROUTER_BASE_URL": "https://openrouter.ai/api/v1",
        "OPENROUTER_API_KEY": "..."
      }
    }
  }
}
```

## Dependencies

- **Semantic Search**: `chromadb`, `sentence-transformers` (BAAI/bge-m3, CPU)
- **Transcription**: `openai-whisper` (large-v3), `pyannote.audio` (speaker diarization)
- **PPT Generation**: `openai` SDK (OpenRouter → Gemini), `Pillow`
- **Image Generation**: `httpx` (Gemini API direct)

## License

MIT
