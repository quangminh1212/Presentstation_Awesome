# ooxml-mcp-server

MCP server for creating, inspecting, editing, and validating **Office Open XML** documents (`.docx`, `.pptx`, `.xlsx`) at the package/part level.

Extracted from [ai-ui](https://github.com/Bajahaw/ai-ui) as a standalone [Model Context Protocol](https://modelcontextprotocol.io/) server.

## Tools

| Tool | Description |
|------|-------------|
| `list_document_parts` | List all internal ZIP parts (path, size, type) |
| `read_document_part` | Read raw XML/content of a part |
| `create_document` | Create a minimal valid docx/pptx/xlsx (optional custom parts) |
| `write_document_part` | Write/replace one or more parts (atomic + validate) |
| `delete_document_part` | Delete a part (only if result still validates) |
| `validate_document` | Validate structure, relationships, content types, XLSX semantics |

All tools take filesystem **paths** (not application-specific file IDs). Writes are validated before saving; invalid packages are rejected and the original file is left unchanged.

## Install

```bash
go install github.com/Bajahaw/ooxml-mcp-server/cmd/ooxml-mcp@latest
```

Or build from source:

```bash
git clone https://github.com/Bajahaw/ooxml-mcp-server.git
cd ooxml-mcp-server
go build -o ooxml-mcp ./cmd/ooxml-mcp
```

## Configure

### Claude Desktop / Cursor / MCP clients

Add to your MCP config (stdio):

```json
{
  "mcpServers": {
    "ooxml": {
      "command": "ooxml-mcp"
    }
  }
}
```

Or with an absolute path:

```json
{
  "mcpServers": {
    "ooxml": {
      "command": "/path/to/ooxml-mcp"
    }
  }
}
```

### ai-ui

In ai-ui settings, add an MCP server pointing at the `ooxml-mcp` binary (or `go run` command) via stdio, or wrap it with an HTTP/SSE bridge if you use remote MCP.

## Validation

Before any write is committed, the package is checked for:

- Valid ZIP archive
- Well-formed XML in every `.xml` / `.rels` part
- `[Content_Types].xml` overrides and default extensions
- Relationship targets exist
- Forward `r:id` / `r:embed` / `r:link` references resolve
- Required content types for known OOXML parts (charts, drawings, worksheets, …)
- XLSX shared string / style index bounds and row ordering

## Example workflow

```
1. create_document  path=./report.docx  format=docx
2. list_document_parts  path=./report.docx
3. read_document_part   path=./report.docx  part_path=word/document.xml
4. write_document_part  path=./report.docx  parts={ "word/document.xml": "<w:document ...>..." }
5. validate_document    path=./report.docx
```

## License

MIT — see [LICENSE](./LICENSE).