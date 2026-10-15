# MCP Server Setup with JavaScript

This guide walks you through setting up a Model Context Protocol (MCP) server using JavaScript.

## Prerequisites

- Node.js (v16 or higher)
- npm or yarn package manager
- latest VS Code

## Setup Instructions

### 1. Initialize Your Project

```bash
npm init -y
```

### 2. Install Dependencies

```bash
npm install @modelcontextprotocol/sdk zod
```

### 3. Create Project Structure

```bash
mkdir src
# or on Windows: md src

touch src/index.js
# or on Windows: new-item src\index.js
```

### 4. Create Your MCP Server

Add the following code to `src/index.js`:

```js
#!/usr/bin/env node

const { McpServer } = require("@modelcontextprotocol/sdk/server/mcp.js");
const { StdioServerTransport } = require("@modelcontextprotocol/sdk/server/stdio.js");
const { z } = require("zod");

// Create an MCP server
const server = new McpServer({
  name: "demo-server",
  version: "1.0.0"
});

// Add an addition tool
server.registerTool(
  "add",
  {
    title: "Addition Tool",
    description: "Add two numbers",
    inputSchema: { a: z.number(), b: z.number() }
  },
  async ({ a, b }) => ({
    content: [{ type: "text", text: String(a + b) }]
  })
);

// Start receiving messages on stdin and sending messages on stdout
const transport = new StdioServerTransport();
server.connect(transport);
```

## Running Your Server

Run your MCP server with:

```bash
node src/index.js
```

## Project Structure

```
your-project/
├── src/
│   └── index.js          # Main server implementation
├── package.json          # Project configuration
└── README.md            # This file
```

## Next Steps

- Add more tools to your MCP server using `server.registerTool()`
- Implement resources using `server.registerResource()`
- Add error handling and logging
- Test your server with an MCP client

## Additional Resources

- [MCP JavaScript SDK Documentation](https://modelcontextprotocol.io/docs/sdk/javascript)
- [MCP Specification](https://spec.modelcontextprotocol.io/)
- [Example MCP Servers](https://github.com/modelcontextprotocol/servers)

## Troubleshooting

### Common Issues

1. **Permission denied on Linux/macOS**: Make sure your script file is executable: `chmod 755 src/index.js`
2. **Module resolution errors**: Ensure you are using the correct file extensions in your require/import statements
3. **Import errors**: Use `.js` extensions in your require/import statements