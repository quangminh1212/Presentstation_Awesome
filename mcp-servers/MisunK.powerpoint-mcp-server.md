# PowerPoint MCP Server

A Model Context Protocol (MCP) server that provides comprehensive PowerPoint (.pptx) editing capabilities. This server allows you to create, edit, and manipulate PowerPoint presentations programmatically through Claude and other MCP-compatible clients.

## Features

- **Create Presentations**: Start with blank presentations or use existing files as templates
- **Slide Management**: Add, delete, and read slide information
- **Text Editing**: Edit titles, content, and add formatted text boxes
- **Shape Operations**: Add rectangles, ovals, and triangles with optional text
- **Image Support**: Insert images with customizable positioning and sizing
- **Table Operations**: Create tables and edit cell content
- **Text Extraction**: Extract all text content from presentations
- **File Listing**: List all PowerPoint files in the current directory

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup Steps

1. **Clone or download this repository**
   ```bash
   git clone <repository-url>
   cd powerpoint-mcp-server
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   
   On Windows:
   ```bash
   venv\Scripts\activate
   ```
   
   On macOS/Linux:
   ```bash
   source venv/bin/activate
   ```

4. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the MCP Server

The server can be run in two modes:

#### 1. MCP Mode (for use with Claude Desktop or other MCP clients)
```bash
python pptx_mcp_server.py --stdio
```

#### 2. HTTP Mode (for testing)
```bash
python pptx_mcp_server.py
```
This will start an HTTP server on `localhost:8000` for testing purposes.

### Configuring with Claude Desktop

To use this MCP server with Claude Desktop, add the following configuration to your Claude Desktop config file:

**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`
**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`

```json
{
  "mcpServers": {
    "powerpoint-editor": {
      "command": "python",
      "args": ["/path/to/pptx_mcp_server.py", "--stdio"],
      "env": {}
    }
  }
}
```

Replace `/path/to/pptx_mcp_server.py` with the actual path to the server file.

## Available Tools

### Presentation Management
- `create_presentation`: Create a new PowerPoint file
- `read_presentation_info`: Get detailed information about a presentation
- `extract_text`: Extract all text content from a presentation

### Slide Operations
- `add_slide`: Add a new slide with optional title and content
- `delete_slide`: Remove a specific slide from the presentation
- `edit_slide_text`: Edit text in slides (title, content, or specific shapes)

### Content Addition
- `add_text_box`: Add formatted text boxes to slides
- `add_shape`: Add geometric shapes (rectangle, oval, triangle)
- `add_image`: Insert images into slides
- `add_table`: Create tables in slides

### Table Operations
- `update_table_cell`: Edit individual table cells

### File Management
- `list_pptx_files` (resource): List all .pptx files in the current directory

## Example Usage

Once connected to an MCP client like Claude Desktop, you can use natural language commands such as:

- "Create a new presentation called 'quarterly-report.pptx'"
- "Add a title slide with the title 'Q4 Financial Results'"
- "Insert a table with 3 rows and 4 columns on slide 2"
- "Add a text box with the content 'Key Findings' to slide 3"
- "Extract all text from the presentation"

## Error Handling

The server includes comprehensive error handling for:
- File not found scenarios
- Invalid slide numbers or indices
- Missing presentation elements
- File permission issues
- Invalid shape types and parameters

All errors are logged and returned with descriptive messages to help with debugging.

## Supported File Formats

- PowerPoint files (.pptx) - both reading and writing
- Template files (.pptx) - for creating new presentations from existing layouts
- Image files for insertion: PNG, JPEG, GIF, BMP

## Limitations

- Only supports .pptx format (not .ppt legacy format)
- Slide animations and transitions are not supported
- Advanced formatting features like themes and master slides have limited support
- Chart creation is not currently implemented

## Development

### Project Structure

```
powerpoint-mcp-server/
├── pptx_mcp_server.py    # Main server implementation
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── examples/             # Example presentations (optional)
```

### Adding New Features

To add new PowerPoint manipulation features:

1. Add a new `@mcp.tool()` decorated function to `pptx_mcp_server.py`
2. Follow the existing error handling patterns
3. Update the README with the new functionality
4. Test with both MCP and HTTP modes

### Testing

To test the server:

1. Run in HTTP mode: `python pptx_mcp_server.py`
2. Use curl or a REST client to test endpoints
3. Test with Claude Desktop for full MCP integration

## Troubleshooting

### Common Issues

1. **"Module not found" errors**: Ensure all dependencies are installed and virtual environment is activated

2. **File permission errors**: Check that the script has read/write permissions for the target directory

3. **Claude Desktop not connecting**: Verify the config file path and syntax, ensure the Python path is correct

4. **PowerPoint files not opening**: Ensure files are in .pptx format and not corrupted

### Debug Mode

The server logs to stderr by default. To see detailed logs:

```bash
python pptx_mcp_server.py --stdio 2>debug.log
```

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Add tests for new functionality
4. Submit a pull request with clear description

## License

This project is open source. Please check the repository for license details.

## Support

For issues and questions:
- Check the troubleshooting section above
- Review the MCP documentation at https://modelcontextprotocol.io/
- Open an issue in the repository

## Version History

### v1.0.0
- Initial release with core PowerPoint editing functionality
- Support for slides, text, shapes, images, and tables
- MCP server implementation with FastMCP
