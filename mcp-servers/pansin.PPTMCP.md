# PPT Writer

A comprehensive PowerPoint presentation generator using MCP (Model Context Protocol) integration with Kiro IDE.

## Overview

PPT Writer is a sophisticated system that enables natural language-driven PowerPoint presentation creation, editing, and management. It integrates with the Office PowerPoint MCP Server to provide seamless presentation generation capabilities within the Kiro development environment.

## Features

### 🎯 Core Functionality

- **Natural Language Processing**: Create presentations using simple English commands
- **Intelligent Content Generation**: Automatically generate slide content based on topics
- **Template Management**: Built-in and custom template support
- **Style Customization**: Professional color schemes and font management
- **Multi-format Export**: PDF, PNG, JPG, and other format support

### 🔧 Advanced Features

- **Real-time Preview**: Live presentation preview with navigation
- **Error Handling**: Comprehensive error recovery and user-friendly messages
- **Backup & Recovery**: Automatic backup with undo/redo functionality
- **Batch Operations**: Process multiple presentations simultaneously
- **Integration Testing**: Comprehensive test suite for reliability

### 🎨 Design & Templates

- **Professional Templates**: 4 built-in professional templates
- **Color Schemes**: 5 predefined color schemes with custom options
- **Smart Layouts**: Automatic layout optimization and element positioning
- **Style Recommendations**: AI-powered style suggestions based on content

## Quick Start

### Prerequisites

- Node.js 18+
- Python 3.12+
- uv package manager
- Kiro IDE

### Installation

1. **Install Dependencies**

   ```bash
   npm install
   ```

2. **Setup MCP Server**

   ```bash
   npm run setup-mcp
   ```

3. **Run Quick Test**

   ```bash
   npm run test:quick
   ```

### Basic Usage

```typescript
import { UserInterface } from './src/ui/UserInterface';
import { PPTCommandInterface } from './src/core/PPTCommandInterface';

// Initialize the system
const pptInterface = new PPTCommandInterface();
const userInterface = new UserInterface(pptInterface);

// Create a session
const session = userInterface.createSession('my-session');

// Create a presentation using natural language
const result = await userInterface.processNaturalLanguageInput(
  'create a presentation about artificial intelligence with 5 slides',
  session.sessionId
);

// Export to PDF
await userInterface.processNaturalLanguageInput(
  'export to PDF as ai-presentation.pdf',
  session.sessionId
);
```

## Configuration

### MCP Configuration

The system uses MCP (Model Context Protocol) to communicate with PowerPoint. Configuration is stored in `.kiro/settings/mcp.json`:

```json
{
  "mcpServers": {
    "office-powerpoint": {
      "command": "/Users/[username]/.local/bin/uvx",
      "args": ["office-powerpoint-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": [
        "create_presentation",
        "add_slide",
        "save_presentation",
        "export_presentation"
      ]
    }
  }
}
```

### Application Configuration

Default settings can be customized in your application:

```typescript
const backupOptions = {
  autoBackup: false,        // Disable auto backup by default
  maxBackups: 50,          // Keep up to 50 backups
  backupInterval: 5,       // Backup every 5 minutes (if enabled)
  compressionEnabled: false
};

const styleOptions = {
  defaultColorScheme: 'professional_blue',
  defaultTemplate: 'modern_business',
  autoSave: true
};
```

## API Reference

### Core Classes

#### PPTCommandInterface

Main interface for PowerPoint operations.

```typescript
// Create presentation
const presentationId = await pptInterface.createPresentation({
  title: 'My Presentation'
});

// Add slide
await pptInterface.addSlide(presentationId, {
  title: 'Slide Title',
  content: 'Slide content',
  layout: 'title_and_content'
});

// Save presentation
await pptInterface.savePresentation(presentationId, 'output.pptx');
```

#### PresentationGenerator

Generate presentations from natural language descriptions.

```typescript
const generator = new PresentationGenerator(pptInterface);
const presentationId = await generator.generatePresentation({
  topic: 'Machine Learning',
  slideCount: 6,
  includeTitle: true,
  includeConclusion: true
});
```

#### StyleManager

Manage presentation styles and themes.

```typescript
const styleManager = new StyleManager(pptInterface);

// Apply color scheme
await styleManager.customizeColors(presentationId, 'professional_blue');

// Set fonts
await styleManager.setFontStyle(presentationId, {
  titleFont: 'Arial',
  bodyFont: 'Calibri',
  titleSize: 32,
  bodySize: 18
});
```

#### FileManager

Handle file operations and management.

```typescript
const fileManager = new FileManager(pptInterface);

// Save with options
await fileManager.savePresentation(presentationId, 'output.pptx', {
  overwrite: true,
  createBackup: true
});

// Load presentation
const loadResult = await fileManager.loadPresentation('input.pptx');
```

## Testing

### Quick Test

```bash
npm run test:quick
```

### Full Test Suite

```bash
npm run test:all
```

### Integration Tests

```bash
npm run test:integration
```

### Individual Component Tests

```bash
# Test specific components
npm run test:presentation-generator
npm run test:style-manager
npm run test:file-manager
```

## Troubleshooting

### Common Issues

1. **MCP Connection Failed**
   - Verify uvx is installed: `uvx --version`
   - Check MCP server status in Kiro
   - Restart MCP server from Kiro settings

2. **PowerPoint Not Found**
   - Ensure PowerPoint is installed
   - Check system PATH includes PowerPoint
   - Verify MCP server permissions

3. **File Permission Errors**
   - Check write permissions in output directory
   - Ensure PowerPoint files are not open in other applications
   - Run with appropriate user permissions

### Debug Mode

Enable debug logging:

```typescript
const pptInterface = new PPTCommandInterface({
  debug: true,
  logLevel: 'verbose'
});
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Run tests: `npm run test:all`
4. Submit a pull request

### Development Setup

```bash
# Install dependencies
npm install

# Setup development environment
npm run setup:dev

# Run in development mode
npm run dev

# Build for production
npm run build
```

## Architecture

### System Components

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Interface   │    │  Core Managers  │    │   MCP Server    │
│                 │    │                 │    │                 │
│ • Natural Lang  │◄──►│ • PPTCommand    │◄──►│ • PowerPoint    │
│ • Session Mgmt  │    │ • Presentation  │    │ • File Ops      │
│ • Command Parse │    │ • Style/Template│    │ • Export        │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         ▼                       ▼                       ▼
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   UI Components │    │  Support Systems│    │   File System   │
│                 │    │                 │    │                 │
│ • Preview       │    │ • Error Handler │    │ • Backups       │
│ • Style Picker  │    │ • Backup Mgr    │    │ • Templates     │
│ • Template UI   │    │ • Retry Logic   │    │ • Exports       │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

### Data Flow

1. **User Input** → Natural language command
2. **Command Parser** → Structured command object
3. **Core Manager** → Business logic execution
4. **MCP Interface** → PowerPoint operations
5. **Result Processing** → User feedback and file output

## License

MIT License - see LICENSE file for details.

## Support

- Documentation: [Link to docs]
- Issues: [GitHub Issues]
- Discussions: [GitHub Discussions]

---

Built with ❤️ for the Kiro IDE ecosystem.
