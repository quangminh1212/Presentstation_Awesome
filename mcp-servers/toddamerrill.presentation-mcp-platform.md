# Presentation MCP Platform

An enterprise-grade Model Context Protocol (MCP) platform that enables Claude to automatically generate professional presentations with infographics from rich text content.

## Features

- 🎯 **Direct Claude Integration**: Works seamlessly with Claude Desktop via MCP
- 📊 **Automatic Infographic Generation**: Converts data and bullet points into visual charts
- 🎨 **Multiple Templates**: Modern and corporate styles with extensible template system
- 🔐 **OAuth2 Authentication**: Secure device flow authentication for enterprise use
- 🚀 **Docker Deployment**: Simple containerized deployment with docker-compose
- 📈 **Scalable Architecture**: Microservices design with Redis caching and PostgreSQL

## Quick Start

### Prerequisites

- Docker (with Compose support)
- Node.js 18+ (for local development)
- Claude Desktop with MCP support

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/presentation-mcp-platform.git
cd presentation-mcp-platform
```

2. Copy the environment template:
```bash
cp .env.example .env
```

3. Update `.env` with your credentials:
```env
DB_USER=mcp_user
DB_PASSWORD=your_secure_password
JWT_SECRET=your_jwt_secret
OAUTH_CLIENT_ID=your-client-id
OAUTH_CLIENT_SECRET=your-client-secret
```

4. Build and start the services:
```bash
docker compose build
docker compose up -d
```

5. The platform will be available at:
   - Gateway: http://localhost:8080
   - Presentation Service: http://localhost:8081
   - Infographic Service: http://localhost:8082

## Claude Desktop Configuration

Add this to your Claude Desktop MCP configuration:

```json
{
  "mcpServers": {
    "presentation-suite": {
      "command": "docker",
      "args": ["run", "-i", "--rm", 
        "-e", "MCP_AUTH_TOKEN=${MCP_AUTH_TOKEN}",
        "your-registry/mcp-client:latest"
      ]
    }
  }
}
```

## Usage

In Claude Desktop, you can now use:

```
Create a presentation about [topic] with modern styling and infographics
```

Claude will:
1. Parse the content into sections
2. Identify data visualization opportunities
3. Generate appropriate infographics
4. Create a professional PowerPoint presentation
5. Return the downloadable file

## Architecture

```
┌─────────────────────┐     ┌─────────────────────┐
│   Claude Desktop    │────▶│    MCP Gateway      │
└─────────────────────┘     └──────────┬──────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
         ┌──────────▼──────────┐  ┌───▼──────────┐  ┌───▼──────────┐
         │ Presentation Server │  │ Infographic  │  │   Storage    │
         │   (PowerPoint)      │  │   Server     │  │   (MinIO)    │
         └─────────────────────┘  └──────────────┘  └──────────────┘
```

## Development

### Local Development Setup

1. Install dependencies for each service:
```bash
cd mcp-gateway && npm install
cd ../mcp-presentation-server && npm install
cd ../mcp-infographic-server && npm install
```

2. Run services in development mode:
```bash
# Terminal 1: Gateway
cd mcp-gateway && npm run dev

# Terminal 2: Presentation Server
cd mcp-presentation-server && npm run dev

# Terminal 3: Infographic Server
cd mcp-infographic-server && npm run dev
```

### Adding New Templates

1. Edit `mcp-presentation-server/src/handlers/generate-slides.js`
2. Add your template configuration to the `templates` object
3. Restart the presentation server

### Adding New Chart Types

1. Edit `mcp-infographic-server/src/generators/chart-generator.js`
2. Add support for new chart types in the `formatData` method
3. Update the chart type enum in the MCP tool definition

## API Documentation

### OAuth2 Device Flow

```bash
# 1. Request device code
POST /oauth/device
{
  "client_id": "your-client-id"
}

# 2. Poll for token
POST /oauth/token
{
  "grant_type": "urn:ietf:params:oauth:grant-type:device_code",
  "device_code": "received-device-code"
}
```

### MCP Tools

**create_presentation**
- `content`: Rich text content from Claude
- `title`: Presentation title
- `template`: Template name (modern/corporate)
- `includeInfographics`: Boolean to enable/disable infographics

## Security

- OAuth2 device flow for secure authentication
- JWT tokens with 24-hour expiration
- Rate limiting per user (100 requests/minute)
- Internal API authentication between services
- Redis-based session management

## Deployment

### Production Deployment

1. Build production images:
```bash
docker compose -f docker-compose.prod.yml build
```

2. Deploy to your container orchestration platform (Kubernetes, ECS, etc.)

3. Configure environment variables for production endpoints

### Scaling Considerations

- Horizontal scaling supported for all services
- Redis cluster for distributed caching
- PostgreSQL read replicas for high availability
- S3-compatible storage for generated assets

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, email support@your-company.com or open an issue in the GitHub repository.
