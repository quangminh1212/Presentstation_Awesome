# MCP-DevTools

A Model Context Protocol (MCP) server implementation for enhanced browser automation and DevTools capabilities using Puppeteer.

## Features

- Full browser automation support via Puppeteer
- Enhanced DevTools Protocol integration
- Docker support for consistent environments
- Non-root user execution for security
- Cross-platform compatibility

## Prerequisites

- Docker
- Cursor IDE

## Setup

1. Build the Docker image:
```bash
docker build -t mcp/puppeteer .
```

2. Configure in Cursor:
   - Open Cursor Settings
   - Navigate to MCP Configuration
   - Add the following command:
```
docker run -i --rm --init -e DOCKER_CONTAINER=true mcp/puppeteer
```

## Configuration

The server is configured to run on port 3000 by default. Environment variables:

- `PUPPETEER_EXECUTABLE_PATH`: Path to Chromium executable
- `DISPLAY`: X11 display for headless mode
- `CHROME_BIN`: Chrome binary path

## Security

- Runs as non-root user in Docker
- Uses Chromium's sandbox
- Implements proper permission handling

## License

MIT License

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request
