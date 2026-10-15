# PowerPoint MCP Server

A Model Context Protocol (MCP) server that provides comprehensive PowerPoint presentation manipulation capabilities. This server enables AI assistants like Claude to create, modify, and analyze PowerPoint presentations using both basic OpenXML operations and advanced OpenXmlPowerTools features.

## Features

### Core PowerPoint Operations
- **Slide Management**: Get, add, update, and delete slides
- **Content Extraction**: Extract text content from presentations and individual slides
- **Layout Management**: Get available slide layouts and apply them to slides
- **Placeholder Handling**: Add slides with specific placeholder content

### Advanced PowerTools Features
- **Presentation Combining**: Merge multiple PowerPoint files into one
- **Presentation Splitting**: Split presentations into individual slide files
- **Search & Replace**: Advanced regex-based text search and replacement
- **Presentation Metrics**: Extract detailed metadata and statistics

## Installation

### Prerequisites
- .NET 8.0 SDK
- PowerShell (for configuration)

### Build the Server
```bash
git clone <your-repo-url>
cd mcp-powerpoint
dotnet build
```

## Configuration

### Adding to Claude Desktop

1. **Locate your Claude Desktop configuration file**:
   - **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

2. **Add the MCP server configuration**:
   ```json
   {
     "mcpServers": {
       "powerpoint": {
         "command": "/absolute/path/to/mcp-powerpoint/src/bin/Debug/net8.0/PowerPointHelper",
         "args": [],
         "env": {}
       }
     }
   }
   ```

3. **Update the path**: Replace `/absolute/path/to/mcp-powerpoint/src/bin/Debug/net8.0/PowerPointHelper` with the actual absolute path to your built executable.
   - **Windows**: Use `PowerPointHelper.exe`
   - **macOS/Linux**: Use `PowerPointHelper` (no extension)

4. **Restart Claude Desktop** for the changes to take effect.

### Alternative: Development Mode (requires .NET SDK)
For development purposes, you can run directly from source:
```json
{
  "mcpServers": {
    "powerpoint": {
      "command": "dotnet",
      "args": ["run", "--project", "/absolute/path/to/mcp-powerpoint/src"],
      "env": {}
    }
  }
}
```

## Available Tools

### Basic Operations
- `getSlideCount` - Get the number of slides in a presentation
- `getAllSlideContent` - Get content from all slides
- `getSlideContent` - Get content from a specific slide
- `addSlide` - Add a new slide with title and content
- `addSlideWithPlaceholders` - Add a slide using specific layout and placeholder content
- `updateSlide` - Update existing slide content
- `deleteSlide` - Remove a slide from the presentation

### Layout Management
- `getSlideLayouts` - Get all available slide layouts with their placeholders
- `applySlideLayout` - Apply a specific layout to an existing slide

### Advanced PowerTools Operations
- `combinePresentations` - Merge multiple PowerPoint files
- `splitPresentation` - Split a presentation into separate files
- `searchAndReplace` - Regex-based text search and replacement
- `getPresentationMetrics` - Get detailed presentation statistics

## Usage Examples

### Creating a New Slide
```typescript
// Add a basic slide
{
  "tool": "addSlide",
  "arguments": {
    "filePath": "/path/to/presentation.pptx",
    "title": "My New Slide",
    "content": "This is the slide content",
    "position": 1
  }
}
```

### Using Layouts and Placeholders
```typescript
// First, get available layouts
{
  "tool": "getSlideLayouts",
  "arguments": {
    "filePath": "/path/to/presentation.pptx"
  }
}

// Then add a slide with specific placeholders
{
  "tool": "addSlideWithPlaceholders",
  "arguments": {
    "filePath": "/path/to/presentation.pptx",
    "layoutId": "rId2",
    "placeholderContents": {
      "Title": "My Title",
      "Content": "My content here"
    }
  }
}
```

### Advanced Operations
```typescript
// Combine multiple presentations
{
  "tool": "combinePresentations",
  "arguments": {
    "filePaths": ["/path/to/presentation1.pptx", "/path/to/presentation2.pptx"],
    "outputPath": "/path/to/combined.pptx"
  }
}

// Search and replace text
{
  "tool": "searchAndReplace",
  "arguments": {
    "filePath": "/path/to/presentation.pptx",
    "searchPattern": "old text",
    "replacement": "new text",
    "ignoreCase": true
  }
}
```

## Project Structure

```
mcp-powerpoint/
├── src/
│   ├── PowerPointHelper.csproj    # Project file
│   ├── Program.cs                 # MCP server entry point
│   ├── PowerPointTools.cs         # MCP tool definitions
│   ├── SlideOperations.cs         # Core slide operations
│   ├── LayoutOperations.cs        # Layout management
│   ├── TextExtractor.cs           # Text extraction utilities
│   └── PowerToolsOperations.cs    # Advanced PowerTools features
├── CLAUDE.md                      # Claude Code instructions
├── SLIDE_LAYOUTS.md              # Layout documentation
├── .gitignore                    # Git ignore rules
└── README.md                     # This file
```

## Dependencies

- **DocumentFormat.OpenXml** (3.3.0) - Core OpenXML functionality
- **OpenXmlPowerTools** (4.5.3.2) - Advanced PowerPoint operations
- **ModelContextProtocol** (0.2.0-preview.3) - MCP server framework
- **Microsoft.Extensions.Hosting** (9.0.0) - .NET hosting infrastructure

## Troubleshooting

### Common Issues

1. **"Unable to find package OpenXmlPowerTools"**
   - The package installs correctly despite .NET Framework compatibility warnings
   - Build should succeed with warnings about .NET Framework vs .NET 9

2. **File Path Issues**
   - Always use absolute file paths when calling tools
   - Ensure PowerPoint files exist before performing operations

3. **Permission Errors**
   - Ensure the PowerPoint files are not open in another application
   - Check file permissions for read/write access

### Debugging

The server logs to standard error. To see debug output when running from Claude Desktop, check the Claude application logs or run the server manually:

```bash
cd src
dotnet run
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly with various PowerPoint files
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with [OpenXML SDK](https://github.com/OfficeDev/Open-XML-SDK)
- Advanced features powered by [OpenXmlPowerTools](https://github.com/OfficeDev/Open-Xml-PowerTools)
- Uses the [Model Context Protocol](https://modelcontextprotocol.io/) for AI integration