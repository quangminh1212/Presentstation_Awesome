# PPTX Generator MCP Server

**Model Context Protocol (MCP) server for generating professional PowerPoint presentations from Markdown.**

Transform your lesson plans and documentation into beautiful PPTX presentations with support for:
- ✅ **Inline code** with monospace formatting
- ✅ **Code blocks** with syntax highlighting background
- ✅ **Tables** with styled headers
- ✅ **Bold text** and mixed formatting
- ✅ **Bullet lists** with proper indentation
- ✅ **Mixed content** slides (bullets + code + tables)
- ✅ **Custom branding** (logos, colors, instructor info)

---

## 📋 Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
  - [Method 1: Quick Install (Recommended)](#method-1-quick-install-recommended)
  - [Method 2: Manual Install](#method-2-manual-install)
- [Configuration](#configuration)
  - [Claude Desktop Setup](#claude-desktop-setup)
  - [Customization](#customization)
- [Usage](#usage)
  - [In Claude Desktop](#in-claude-desktop)
  - [Markdown Format](#markdown-format)
- [Examples](#examples)
- [Troubleshooting](#troubleshooting)
- [Updating](#updating)
- [Uninstalling](#uninstalling)

---

## 🔧 Requirements

- **Node.js** 18.0 or higher ([Download](https://nodejs.org/))
- **Claude Desktop** ([Download](https://claude.ai/download))
- **macOS, Linux, or Windows**

Check your Node.js version:
```bash
node -v
```

---

## 📦 Installation

### Method 1: Quick Install (Recommended)

**1. Clone the repository:**
```bash
cd ~/Documents  # or any directory you prefer
git clone https://github.com/dmytro-ustynov/pptx-generator-mcp.git
cd pptx-generator-mcp
```

**2. Run the installation script:**
```bash
./install.sh
```

The script will:
- Install all dependencies
- Install the command globally
- Show you the Claude Desktop configuration

**3. Configure Claude Desktop:**

The installer will show you what to add. Copy the configuration to:
- **macOS/Linux:** `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "pptx-generator": {
      "command": "pptx-generator-mcp"
    }
  }
}
```

**4. Restart Claude Desktop**

✅ Done! The `pptx-generator` tools are now available in Claude.

---

### Method 2: Manual Install

**1. Clone and install dependencies:**
```bash
# Change dmytro-ustynov to your username if you want to use your fork
git clone https://github.com/dmytro-ustynov/pptx-generator-mcp.git 
cd pptx-generator-mcp
npm install
```

**2. Install globally:**
```bash
npm install -g .
```

Or with sudo if needed:
```bash
sudo npm install -g .
```

**3. Verify installation:**
```bash
which pptx-generator-mcp
# Should show: /usr/local/bin/pptx-generator-mcp (or similar)
```

**4. Configure Claude Desktop** (same as Method 1, step 3)

---

## ⚙️ Configuration

### Claude Desktop Setup

After installation, configure Claude Desktop to use the MCP server.

**macOS/Linux:**
```bash
# Open the config file
code ~/Library/Application\ Support/Claude/claude_desktop_config.json
# or
nano ~/Library/Application\ Support/Claude/claude_desktop_config.json
```

**Windows:**
```powershell
notepad %APPDATA%\Claude\claude_desktop_config.json
```

**Add this configuration:**
```json
{
  "mcpServers": {
    "pptx-generator": {
      "command": "pptx-generator-mcp"
    }
  }
}
```

**If you have other MCP servers:**
```json
{
  "mcpServers": {
    "pptx-generator": {
      "command": "pptx-generator-mcp"
    },
    "other-server": {
      "command": "other-server-command"
    }
  }
}
```

**Restart Claude Desktop** for changes to take effect.

---

### Customization

Customize colors, fonts, and branding by editing `config.json` in the installation directory.

**Find your installation:**
```bash
npm list -g pptx-generator-mcp
# Shows: /usr/local/lib/node_modules/pptx-generator-mcp
```

**Edit config:**
```bash
cd $(npm root -g)/pptx-generator-mcp
nano config.json
```

**Configuration options:**

#### Instructor Information
```json
{
  "instructor": {
    "rank": "майор",
    "name": "Дмитро УСТИНОВ",
    "position": "викладач"
  }
}
```

#### Institution Details
```json
{
  "institution": {
    "name": [
      "Військовий інститут",
      "телекомунікацій та інформатизації",
      "імені Героїв Крут"
    ],
    "department": "кафедри Комп'ютерних наук та інтелектуальних технологій"
  }
}
```

#### Colors
Colors are adjusted according to the official Armed Forces of Ukraine [brandbook](https://warbooks.com.ua/contents/brendbuk-zsu-kerivnitstvo-iz-vikoristannya-grafichnogo-stilyu-u-vizualniy-komunikatsii.pdf?srsltid=AfmBOoqJlDFC6vqXpO5LluAIv1D3PE9M42JNLUSyexejGHWkl5rz9hNi), and the logo is Armed Forces of Ukraine emblem.

```json
{
  "colors": {
    "step": "#6A653A",        // Dividers and table headers
    "titleText": "#003366",   // Slide titles
    "bodyText": "#333333"     // Regular text
  }
}
```

#### Fonts
```json
{
  "fonts": {
    "title": "Raleway",
    "body": "Open Sans",
    "code": "JetBrains Mono"  // For inline code and code blocks
  }
}
```

#### Font Sizes
```json
{
  "sizes": {
    "slideTitle": 28,
    "body": 18,
    "code": 14
  }
}
```

**After editing config.json:**
- No need to restart Claude Desktop
- Changes apply to next generated presentation

---

## 🎯 Usage

### In Claude Desktop

Once installed and configured, you can use these tools in Claude:

**1. Generate a presentation:**
```
Create a presentation about Docker basics with 5 slides
```

Claude will use the `pptx-generator:generate_presentation` tool automatically.

**2. Get a template:**
```
Show me the markdown template for presentations
```

Uses `pptx-generator:get_template` tool.

**3. View configuration:**
```
What are the current presentation settings?
```

Uses `pptx-generator:get_config` tool.

**4. Update instructor:**
```
Change the instructor to "капітан Іван ПЕТРЕНКО"
```

Uses `pptx-generator:update_instructor` tool.

---

### Markdown Format

Presentations are created from Markdown with special syntax:

#### Frontmatter (Required)

```yaml
---
discipline: Веб-розробка
type: practical
module: "3: Docker та контейнеризація"
lesson: "3.1: Основи Docker"
---
```

**Types:**
- `practical` - Практичне заняття
- `lecture` - Лекційне заняття
- `group` - Групове заняття

#### Slide Types

**Plan Slide:**
```markdown
## [plan] План заняття

- Topic 1
- Topic 2
- Topic 3
```

**Divider Slide:**
```markdown
## [divider] 🔹 ЧАСТИНА 1. Introduction
```

**Content Slide:**
```markdown
## [content] Slide Title

Regular text with **bold** and `inline code`.

Bullet points:
- First point with **bold**
- Second point with `code`
- Third point with **bold** and `code` mixed

Code block:
```bash
docker ps
docker images
```

Table:
| Column 1 | Column 2 |
|----------|----------|
| `value1` | Description 1 |
| `value2` | Description 2 |
```

#### Formatting

- **Bold text:** `**text**`
- **Inline code:** `` `code` ``
- **Code blocks:** Triple backticks with optional language
- **Tables:** Standard Markdown table syntax
- **Bullets:** `-` or `*` with optional indentation

---

## 📚 Examples

### Simple Presentation

```markdown
---
discipline: Programming Basics
type: lecture
module: "1: Introduction"
lesson: "1.1: Hello World"
---

## [plan] План заняття

- What is programming
- First program
- Variables and types

## [divider] 🔹 Getting Started

## [content] What is Programming?

**Programming** is giving instructions to computers.

Key concepts:
- Variables store data
- Functions perform actions
- Loops repeat tasks

Example:
```python
print("Hello, World!")
```
```

### Advanced Features

```markdown
## [content] Docker Commands

Common commands:

| Command | Description |
|---------|-------------|
| `docker ps` | List running containers |
| `docker images` | List images |
| `docker run` | Run a container |

Example usage:
```bash
docker run -d -p 80:80 nginx
```

The `-d` flag runs in **detached mode**.
```

---

## 🐛 Troubleshooting

### Command not found: pptx-generator-mcp

**Solution 1:** Check if installed globally
```bash
npm list -g pptx-generator-mcp
```

**Solution 2:** Add npm global bin to PATH
```bash
# Find npm global bin path
npm config get prefix

# Add to PATH (add to ~/.bashrc or ~/.zshrc)
export PATH=$(npm config get prefix)/bin:$PATH
```

**Solution 3:** Reinstall
```bash
cd /path/to/pptx-generator-mcp
npm install -g .
```

---

### Tools not showing in Claude

1. **Check Claude Desktop config:**
   ```bash
   cat ~/Library/Application\ Support/Claude/claude_desktop_config.json
   ```

2. **Verify JSON syntax** (use [JSONLint](https://jsonlint.com/))

3. **Restart Claude Desktop completely:**
   - Quit Claude Desktop (Cmd+Q on macOS)
   - Reopen Claude Desktop

4. **Check MCP server logs** (if available in Claude Desktop)

---

### Permission denied when installing

**Solution:** Use sudo
```bash
sudo npm install -g .
```

Or install without sudo by configuring npm:
```bash
mkdir ~/.npm-global
npm config set prefix '~/.npm-global'
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc
source ~/.bashrc
```

---

### Fonts not displaying correctly

**Issue:** Custom fonts like JetBrains Mono not showing

**Solution:** Install the font on your system:
1. Download [JetBrains Mono](https://www.jetbrains.com/lp/mono/)
2. Install the font
3. Restart PowerPoint/Keynote

---

## 🔄 Updating

To update to the latest version:

```bash
# Navigate to repository
cd /path/to/pptx-generator-mcp

# Pull latest changes
git pull

# Reinstall
npm install
npm install -g .
```

**No need to restart Claude Desktop** - changes take effect immediately for new presentations.

---

## 🗑️ Uninstalling

```bash
# Uninstall global command
npm uninstall -g pptx-generator-mcp

# Remove repository
rm -rf /path/to/pptx-generator-mcp

# Remove from Claude Desktop config
# Edit: ~/Library/Application Support/Claude/claude_desktop_config.json
# Remove the "pptx-generator" section
```

---

## 📖 Additional Resources

- **MCP Documentation:** https://modelcontextprotocol.io/
- **Claude Desktop:** https://claude.ai/download
- **Markdown Guide:** https://www.markdownguide.org/

---

## 📝 License

MIT License - See LICENSE file for details

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 💬 Support

For issues or questions:
- Open an issue on GitHub
- Check the [Troubleshooting](#troubleshooting) section

---

**Made with ❤️ for VITI education**
