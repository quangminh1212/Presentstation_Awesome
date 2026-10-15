# Google Slides MCP Server

A Model Context Protocol (MCP) server that provides tools for interacting with Google Slides presentations. This server allows you to create new slides and add rectangles to existing slides.

## Features

- **Create New Slides**: Add blank slides to existing Google Slides presentations
- **Add Rectangles**: Insert rectangles with dimensions that are 20% of the slide size
- **OAuth2 Authentication**: Secure authentication flow with Google APIs
- **Presentation Management**: Get presentation info and list slides

## Installation

1. Clone or download this repository
2. Install dependencies:

```bash
npm install
```

3. Build the TypeScript code:

```bash
npm run build
```

## Google Cloud Console Setup

Before using this MCP server, you need to set up a Google Cloud project and enable the Google Slides API:

### 1. Create a Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select an existing one
3. Enable the Google Slides API:
   - Go to "APIs & Services" > "Library"
   - Search for "Google Slides API"
   - Click on it and press "Enable"

### 2. Create OAuth2 Credentials

1. Go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen first:
   - Choose "External" user type
   - Fill in the required fields (App name, User support email, etc.)
   - Add your email to test users
4. For the OAuth client ID:
   - Choose "Desktop application" as the application type
   - Give it a name (e.g., "Google Slides MCP Server")
5. Download the credentials JSON file

### 3. Configure Environment Variables

1. Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

2. Edit `.env` and add your OAuth2 credentials:

```env
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here
GOOGLE_REDIRECT_URI=http://localhost:3000/oauth2callback
```

## Usage

### Starting the Server

```bash
npm start
```

Or for development with auto-reload:

```bash
npm run dev
```

### Authentication Flow

Before using the Google Slides tools, you need to authenticate:

1. Call the `get_auth_url` tool to get the OAuth2 authorization URL
2. Visit the URL in your browser and grant permissions
3. Copy the authorization code from the redirect URL
4. Call the `authenticate` tool with the authorization code

The authentication tokens will be saved locally and reused for future requests.

### Available Tools

#### 1. `get_auth_url`
Get the OAuth2 authorization URL for Google Slides access.

**Parameters:** None

**Example:**
```json
{
  "name": "get_auth_url",
  "arguments": {}
}
```

#### 2. `authenticate`
Complete OAuth2 authentication with authorization code.

**Parameters:**
- `code` (string, required): Authorization code from OAuth2 flow

**Example:**
```json
{
  "name": "authenticate",
  "arguments": {
    "code": "4/0AX4XfWh..."
  }
}
```

#### 3. `create_slide`
Create a new slide in a Google Slides presentation.

**Parameters:**
- `presentationId` (string, required): The ID of the Google Slides presentation
- `insertionIndex` (number, optional): Position where to insert the slide (defaults to 0)

**Example:**
```json
{
  "name": "create_slide",
  "arguments": {
    "presentationId": "1BxAB07047kHMdtbgoC48KDz3YMgn9_12345678",
    "insertionIndex": 1
  }
}
```

#### 4. `add_rectangle`
Add a rectangle to a slide with 20% of slide dimensions.

**Parameters:**
- `presentationId` (string, required): The ID of the Google Slides presentation
- `slideId` (string, required): The ID of the slide to add the rectangle to
- `x` (number, optional): X position of the rectangle (defaults to center)
- `y` (number, optional): Y position of the rectangle (defaults to center)
- `width` (number, optional): Width of the rectangle (defaults to 20% of slide width)
- `height` (number, optional): Height of the rectangle (defaults to 20% of slide height)

**Example:**
```json
{
  "name": "add_rectangle",
  "arguments": {
    "presentationId": "1BxAB07047kHMdtbgoC48KDz3YMgn9_12345678",
    "slideId": "slide_12345"
  }
}
```

#### 5. `get_presentation_info`
Get information about a Google Slides presentation.

**Parameters:**
- `presentationId` (string, required): The ID of the Google Slides presentation

**Example:**
```json
{
  "name": "get_presentation_info",
  "arguments": {
    "presentationId": "1BxAB07047kHMdtbgoC48KDz3YMgn9_12345678"
  }
}
```

#### 6. `list_slides`
List all slides in a Google Slides presentation.

**Parameters:**
- `presentationId` (string, required): The ID of the Google Slides presentation

**Example:**
```json
{
  "name": "list_slides",
  "arguments": {
    "presentationId": "1BxAB07047kHMdtbgoC48KDz3YMgn9_12345678"
  }
}
```

## Finding Your Presentation ID

The presentation ID can be found in the Google Slides URL:
```
https://docs.google.com/presentation/d/PRESENTATION_ID_HERE/edit
```

For example, in this URL:
```
https://docs.google.com/presentation/d/1BxAB07047kHMdtbgoC48KDz3YMgn9_abcdefgh/edit
```

The presentation ID is: `1BxAB07047kHMdtbgoC48KDz3YMgn9_abcdefgh`

## Common Workflow

1. **First time setup:**
   ```bash
   # Get authorization URL
   {"name": "get_auth_url", "arguments": {}}
   
   # After visiting URL and getting code
   {"name": "authenticate", "arguments": {"code": "your_auth_code"}}
   ```

2. **Create a new slide:**
   ```bash
   {"name": "create_slide", "arguments": {"presentationId": "your_presentation_id"}}
   ```

3. **Add a rectangle to the slide:**
   ```bash
   {"name": "add_rectangle", "arguments": {"presentationId": "your_presentation_id", "slideId": "returned_slide_id"}}
   ```

## Error Handling

The server provides detailed error messages for common issues:
- Authentication required
- Invalid presentation ID
- Invalid slide ID
- Network connectivity issues
- Google API quota limits

## Development

### Project Structure

```
src/
├── index.ts      # Main MCP server entry point
├── auth.ts       # Google OAuth2 authentication
└── slides.ts     # Google Slides API service

dist/             # Compiled JavaScript (after npm run build)
package.json      # Project dependencies and scripts
tsconfig.json     # TypeScript configuration
.env.example      # Environment variables template
```

### Scripts

- `npm run build` - Compile TypeScript to JavaScript
- `npm start` - Run the compiled server
- `npm run dev` - Run with ts-node for development
- `npm run watch` - Watch for changes and recompile

## Troubleshooting

### Authentication Issues

- Ensure your Google Cloud project has the Google Slides API enabled
- Check that your OAuth2 credentials are correct in the `.env` file
- Make sure you're using the correct redirect URI
- Verify that your email is added as a test user if using external OAuth consent

### API Errors

- Check that the presentation ID is correct and accessible
- Ensure you have edit permissions for the Google Slides presentation
- Verify that the slide ID exists when adding rectangles

### Permission Errors

The server requires the following Google API scopes:
- `https://www.googleapis.com/auth/presentations` - For creating and editing slides
- `https://www.googleapis.com/auth/drive.file` - For accessing Google Drive files

## License

MIT
