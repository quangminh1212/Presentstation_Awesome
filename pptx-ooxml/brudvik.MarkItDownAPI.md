# MarkItDown API

A C# ASP.NET Core Web API wrapper for Microsoft's [MarkItDown](https://github.com/microsoft/markitdown) Python library. Converts various document formats to Markdown.

## Features

- **Clean Architecture**: Domain, Application, Infrastructure, and API layers
- **CQRS Pattern**: Commands and Queries with MediatR
- **File Conversion**: Upload files (PDF, DOCX, PPTX, XLSX, images, etc.) and get Markdown
- **URL Conversion**: Convert webpages and YouTube videos to Markdown
- **IIS Compatible**: Designed for Windows/IIS deployment
- **Python.NET Integration**: Direct Python integration without subprocess overhead
- **Scalar Documentation**: Interactive API documentation

## Supported Formats

| Category | Extensions |
|----------|-----------|
| Documents | `.pdf`, `.docx`, `.doc`, `.pptx`, `.ppt`, `.xlsx`, `.xls` |
| Text | `.html`, `.htm`, `.csv`, `.json`, `.xml`, `.txt`, `.md` |
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff`, `.webp` |
| Audio | `.mp3`, `.wav`, `.m4a` |
| Other | `.zip`, `.epub`, `.msg`, `.eml` |
| URLs | HTTP/HTTPS webpages, YouTube videos |

## Project Structure

```
MarkItDownAPI/
├── src/
│   ├── MarkItDownAPI.Domain/           # Entities, Value Objects
│   ├── MarkItDownAPI.Application/      # Use Cases, CQRS, Validators
│   ├── MarkItDownAPI.Infrastructure/   # Python Integration
│   └── MarkItDownAPI.Api/              # Controllers, Middleware
├── tests/
│   ├── MarkItDownAPI.UnitTests/
│   └── MarkItDownAPI.IntegrationTests/
├── Install.ps1                         # Installation script
├── start-dev.ps1                       # Development server script
└── CHANGELOG.md
```

## Prerequisites

### Option 1: Automatic Installation (Recommended)

Run the installation script - it will automatically install Python and MarkItDown if needed:

```powershell
.\Install.ps1
```

**Script options:**
```powershell
# Interactive mode (prompts for input)
.\Install.ps1

# Fully automated (for CI/CD)
.\Install.ps1 -NonInteractive

# Specify Python version
.\Install.ps1 -PythonVersion 3.11

# Skip Python installation (if already installed)
.\Install.ps1 -SkipPythonInstall
```

### Option 2: Manual Installation

#### 1. Install Python 3.10+

Download and install Python from [python.org](https://www.python.org/downloads/). Make sure to:
- Install for all users
- Add Python to PATH
- Note the installation path (e.g., `C:\Python312`)

#### 2. Install MarkItDown

```powershell
pip install "markitdown[all]"
```

#### 3. Install ffmpeg (Optional - for audio file conversion)

Download from [ffmpeg.org](https://ffmpeg.org/download.html) or use winget:

```powershell
winget install Gyan.FFmpeg
```

#### 4. Install .NET 8 SDK

Download from [dot.net](https://dotnet.microsoft.com/download).

## Configuration

Edit `src/MarkItDownAPI.Api/appsettings.json`:

```json
{
  "Python": {
    "PythonHome": "C:\\Python312",
    "PythonDll": "python312.dll",
    "EnableLlmDescriptions": false,
    "OpenAIApiKey": "",
    "LlmModel": "gpt-4o",
    "EnablePlugins": false,
    "DocumentIntelligenceEndpoint": ""
  }
}
```

### Configuration Options

| Setting | Description |
|---------|-------------|
| `PythonHome` | Path to Python installation. Leave empty for auto-detection. |
| `PythonDll` | Python DLL filename (e.g., `python312.dll` for Python 3.12) |
| `EnableLlmDescriptions` | Enable AI image descriptions (requires OpenAI API key) |
| `OpenAIApiKey` | OpenAI API key for LLM features |
| `EnablePlugins` | Enable MarkItDown third-party plugins |
| `DocumentIntelligenceEndpoint` | Azure Document Intelligence endpoint (optional) |

## Running Locally

Use the development script:

```powershell
.\start-dev.ps1
```

This will:
1. Validate Python environment
2. Build the solution
3. Start the API in a new console window
4. Open Scalar documentation in your browser

The API will be available at:
- **HTTPS**: https://localhost:5001
- **HTTP**: http://localhost:5000
- **Docs**: https://localhost:5001/scalar/v1

### Development Script Options

```powershell
.\start-dev.ps1                 # Default (builds and opens browser)
.\start-dev.ps1 -NoBuild        # Skip build step
.\start-dev.ps1 -NoBrowser      # Don't open browser
.\start-dev.ps1 -Release        # Build in Release mode
.\start-dev.ps1 -Port 8080      # Use custom port
```

## API Endpoints

### Convert File

```http
POST /api/convert/file
Content-Type: multipart/form-data
```

**cURL example:**
```bash
curl -X POST "https://localhost:5001/api/convert/file" \
  -F "file=@document.pdf"
```

### Convert URL

```http
POST /api/convert/url
Content-Type: application/json

{
  "url": "https://example.com"
}
```

### Get Supported Formats

```http
GET /api/convert/supported-formats
```

### Health Check

```http
GET /api/convert/health
```

## Response Format

```json
{
  "success": true,
  "markdown": "# Document Title\n\nContent...",
  "title": "Document Title",
  "error": null,
  "processingTimeMs": 1234
}
```

## IIS Deployment

### 1. Publish the Application

```powershell
dotnet publish src/MarkItDownAPI.Api -c Release -o ./publish
```

### 2. Configure IIS

1. Install the [ASP.NET Core Hosting Bundle](https://dotnet.microsoft.com/download/dotnet/8.0)
2. Create a new IIS site pointing to the `publish` folder
3. Set the Application Pool to "No Managed Code"
4. Ensure the App Pool identity has access to Python installation

### 3. Configure Environment Variables

Edit `web.config` in the publish folder to set the correct Python paths:

```xml
<environmentVariables>
  <environmentVariable name="PYTHONHOME" value="C:\Python312" />
  <environmentVariable name="PATH" value="C:\Python312;C:\Python312\Scripts;%PATH%" />
</environmentVariables>
```

### 4. Grant Permissions

```powershell
# Grant IIS_IUSRS access to Python directory
icacls "C:\Python312" /grant "IIS_IUSRS:(OI)(CI)RX" /T
```

## Running Tests

```powershell
dotnet test
```

## Known Limitations

### Audio File Transcription

MarkItDown uses Google's free speech recognition API to transcribe audio files (MP3, WAV, etc.) to text. This has several limitations:

- **External API dependency**: Requires internet access to Google's speech recognition service
- **File size/duration limits**: Long audio files may fail or be truncated
- **Rate limits**: Google's free API has usage limits
- **Accuracy**: Depends on audio quality, language, and background noise

If audio transcription fails, you'll receive an error: "Audio transcription failed. MarkItDown uses speech recognition to convert audio files..."

For production use with audio files, consider:
- Using OpenAI Whisper API (configure via `OpenAIApiKey`)
- Pre-processing audio files to shorter segments
- Accepting that some audio files may not convert

### OCR (Image Text Extraction)

Text extraction from images requires Tesseract OCR to be installed separately.

## Troubleshooting

### Python not found
- Verify `PythonHome` in `appsettings.json` points to correct path
- Check that environment variables are set in `web.config`

### MarkItDown module not found
- Run `pip install "markitdown[all]"` in the Python installation
- Ensure pip installed packages are accessible to IIS

### Permission issues
- Grant IIS App Pool identity read/execute permissions on Python folder
- Check `stdout` logs in the `logs` folder

## License

MIT License. See [LICENSE](LICENSE) for details.

MarkItDown itself is © Microsoft Corporation, licensed under MIT.
