# Mini Gamma-like Presentation Generator

A powerful MCP (Model Context Protocol) server that enables AI agents to create professional presentations using Google Slides templates. This system provides Gamma-like functionality for automated presentation generation with template-based design consistency.

## 🚀 Features

### Core Capabilities
- **Template Management**: Registry-based template system for different presentation types
- **Template Cloning**: Automatic template duplication via Google Drive API
- **Layout Extraction**: Analyze template structure for AI content planning
- **Content Injection**: Replace placeholders with generated content
- **Multi-Category Support**: Business, marketing, startup, academic templates

### AI Integration Ready
- **Layout-Aware Content**: AI can understand template structure before generating content
- **Placeholder Mapping**: Structured content injection system
- **Agent-Friendly**: Designed for seamless AI agent integration
- **Batch Operations**: Efficient multi-slide creation and editing

## 📋 Available Templates

### Business Templates
- **Professional Business**: Clean corporate presentations, pitch decks
- **Startup Pitch**: Investor-ready deck with standard startup sections

### Marketing Templates
- **Marketing Campaign**: Vibrant, engaging marketing presentations
- **Product Launch**: Feature-focused presentation layouts

### Academic Templates
- **Minimal Clean**: Academic and technical presentations
- **Research**: Research paper and thesis presentations

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- [uv](https://docs.astral.sh/uv/) - Fast Python package installer
- Google Cloud Project with APIs enabled:
  - Google Slides API
  - Google Drive API
- OAuth2 credentials (client ID, client secret, refresh token)

### Quick Setup with uv

1. **Install uv** (if not already installed):
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

2. **Clone and setup environment**:
```bash
cd /path/to/your/workspace/Google_MCP
./setup.sh
```

This will:
- Create a virtual environment with uv
- Install all required dependencies
- Create a .env template file

3. **Configure Google API credentials**:
Edit the `.env` file created by setup:
```bash
GOOGLE_CLIENT_ID=your_client_id_here
GOOGLE_CLIENT_SECRET=your_client_secret_here  
GOOGLE_REFRESH_TOKEN=your_refresh_token_here
```

4. **Set up templates**:
- Copy your template presentations to Google Drive
- Update `templates.json` with your template file IDs
- Ensure templates have appropriate placeholders ({{TITLE}}, {{CONTENT}}, etc.)

5. **Start the MCP server**:
```bash
./run.sh
```

Server will start on `http://127.0.0.1:8101`

### Development Setup

For development with additional tools (pytest, black, flake8, mypy):
```bash
./setup-dev.sh
```

### Manual Installation (Alternative)

If you prefer manual setup:

```bash
# Create virtual environment
uv venv

# Activate virtual environment  
source .venv/bin/activate

# Install dependencies
uv pip install mcp google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2 python-dotenv uvicorn fastapi pydantic requests aiohttp

# Run server
python google_slides_mcp_sse.py
```

## 🎯 Usage

### MCP Tools Available

#### Template Management
- `get_templates()` - List available templates
- `get_templates(category="business")` - Filter by category
- `extract_layouts(template_name="business")` - Analyze template structure

#### Presentation Creation
- `clone_template(template_name, new_title)` - Clone template
- `create_presentation_from_template(template_name, new_title, content_data)` - Full workflow

#### Standard Slides Operations
- `create_presentation(title)` - Create blank presentation
- `get_presentation(presentationId)` - Get presentation details
- `batch_update_presentation(presentationId, requests)` - Batch updates
- `summarize_presentation(presentationId)` - Extract content

### Example Workflows

#### 1. Business Presentation Creation
```python
# Get business templates
templates = await get_templates(category="business")

# Analyze template structure
layouts = await extract_layouts(template_name="business")

# Create presentation with content
result = await create_presentation_from_template(
    template_name="business",
    new_title="Q4 2024 Business Review",
    content_data={
        "company_name": "TechCorp Industries",
        "presenter": "Sarah Johnson, CEO",
        "title": "Strategic Business Review",
        "content": "Revenue growth of 127% year-over-year..."
    }
)
```

#### 2. Marketing Campaign Deck
```python
# Create marketing presentation
result = await create_presentation_from_template(
    template_name="marketing", 
    new_title="Green Revolution Campaign 2024",
    content_data={
        "brand_name": "EcoLife Products",
        "campaign_title": "Green Revolution 2024", 
        "value_proposition": "Sustainable living made simple",
        "cta": "Join the Green Revolution Today!"
    }
)
```

#### 3. AI Agent Integration
```python
# Agent workflow
async def create_ai_presentation(user_request: str):
    # 1. Analyze request and determine template type
    template_type = analyze_request_type(user_request)
    
    # 2. Get template structure for content planning
    layouts = await extract_layouts(template_name=template_type)
    
    # 3. Generate content using GPT with layout awareness
    content_data = await generate_content_for_template(
        user_request, layouts, template_type
    )
    
    # 4. Create presentation
    return await create_presentation_from_template(
        template_name=template_type,
        new_title=extract_title(user_request),
        content_data=content_data
    )
```

## 🏗️ Template Structure

### Template Registry Format
```json
{
  "template_name": {
    "fileId": "google_drive_file_id",
    "name": "Human Readable Name",
    "description": "Template description", 
    "category": "business|marketing|academic",
    "layouts": {
      "slide_type": "GOOGLE_LAYOUT_TYPE"
    },
    "placeholders": {
      "key": "{{PLACEHOLDER_PATTERN}}"
    }
  }
}
```

### Placeholder System
Templates use placeholder patterns that get replaced with actual content:
- `{{COMPANY_NAME}}` → Company name
- `{{TITLE}}` → Slide title
- `{{CONTENT}}` → Main content
- `{{DATE}}` → Presentation date
- `{{PRESENTER}}` → Presenter name

## 🤖 AI Agent Integration

### Content Planning with Layout Awareness
The `extract_layouts` tool provides structure information that AI agents can use to:
- Understand available slide layouts
- Plan content appropriate for each layout type
- Map generated content to correct placeholders
- Ensure content fits layout constraints

### Example Agent Prompt
```
You are creating a marketing presentation using the "marketing" template.

Available layouts: hero, feature, stats, testimonial, cta
Template placeholders: brand_name, campaign_title, value_proposition, features, testimonial, cta

Generate content that fits these layouts and maps to the placeholders appropriately.
```

## 📊 Template Layout Types

### Standard Google Slides Layouts
- `TITLE_SLIDE` - Title and subtitle
- `TITLE_AND_BODY` - Title with body content
- `TITLE_AND_TWO_COLUMNS` - Title with two-column layout  
- `SECTION_HEADER` - Section divider slide
- `BLANK` - Empty slide

### Custom Template Layouts
Templates can define semantic layout names:
- `hero` - Main presentation slide
- `problem` - Problem statement  
- `solution` - Solution overview
- `features` - Feature highlights
- `testimonial` - Customer testimonials
- `cta` - Call to action

## 🔧 Advanced Features

### Batch Slide Creation
Create multiple slides with different layouts in one operation:
```python
requests = [
    {"createSlide": {"slideLayoutReference": {"predefinedLayout": "TITLE_SLIDE"}}},
    {"createSlide": {"slideLayoutReference": {"predefinedLayout": "TITLE_AND_BODY"}}},
    # Add content to slides
    {"insertText": {"objectId": "slide1_title", "text": "My Title"}},
]

await batch_update_presentation(presentation_id, requests)
```

### Custom Content Injection
Beyond simple placeholder replacement:
- Insert images and shapes
- Apply custom formatting
- Add charts and tables
- Set slide transitions

## 🚦 Error Handling

The system includes comprehensive error handling for:
- Invalid template names
- Missing Google API credentials  
- Drive API permission issues
- Malformed content data
- Template cloning failures

## 🔐 Security & Permissions

### Required Google OAuth Scopes
- `https://www.googleapis.com/auth/presentations` - Slides API access
- `https://www.googleapis.com/auth/drive` - Drive API for template cloning

### Template Access
- Templates must be accessible by the service account/OAuth user
- Cloned presentations inherit the same permissions
- Consider using shared drives for team templates

## 📈 Performance Considerations

- Template registry is loaded once at startup
- Layout extraction is cached per template
- Batch operations are preferred for multiple slides
- Large templates may have slower clone operations

## 🧪 Testing

Run the example usage script:
```bash
python example_usage.py
```

This demonstrates the complete workflow and shows expected output formats.

## 🔄 Future Enhancements

- [ ] Dynamic template creation from existing presentations
- [ ] Template marketplace integration
- [ ] Advanced content generation with layout optimization
- [ ] Multi-language template support
- [ ] Custom theme and branding injection
- [ ] Integration with design systems
- [ ] Real-time collaboration features

## 🤝 Contributing

1. Add new template types to `templates.json`
2. Extend placeholder system for new content types
3. Add new MCP tools for advanced functionality
4. Improve AI agent integration patterns

## 📝 License

This project is designed for educational and development purposes. Ensure you have appropriate Google API quotas and permissions for production use.

---

Ready to build the future of AI-powered presentation creation! 🎨✨
