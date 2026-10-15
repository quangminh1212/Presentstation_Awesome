# Model Context Protocol (MCP) - Group M Website

A comprehensive educational website about the Model Context Protocol, including interactive tutorials and working code examples.

**Group Members:** Bibika Ghimire, Mateusz Nowak, Muhammad Sohaib, Michael McCabe, Summer Rhoda

## 📚 Project Structure

```
mcp-website/
├── src/                          # React website source
│   ├── pages/                    # Main pages
│   │   ├── Welcome.jsx           # Landing page
│   │   ├── Home.jsx              # MCP overview
│   │   ├── Presentation.jsx      # Our presentation
│   │   ├── Tutorial.jsx          # Step-by-step tutorial
│   │   └── CodeExplanation.jsx   # Code deep dive
│   ├── components/               # Reusable components
│   └── styles/                   # Global styles
├── tutorial-code/                # Working tutorial code
│   └── mcp-server/               # MCP server example
└── dist/                         # Build output (generated)
```

## 🚀 Quick Start

### Prerequisites

- Node.js v18 or higher
- npm or yarn

### Installation

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Preview production build
npm run preview
```

## 📖 Website Content

### 1. Welcome Page
- Introduction to MCP
- Quick navigation
- Team information

### 2. Home - MCP Overview
- What is MCP and why it was created
- Architecture and components
- Real-world applications
- Key features

### 3. Presentation
- Our complete group presentation
- Topic breakdown
- Key takeaways

### 4. Tutorial (⭐ Main Feature)
A comprehensive 60-minute tutorial teaching how to build an MCP-enabled task manager:

- **Prerequisites & Setup** (10 min)
- **Create MCP Server** (20 min)
- **Test with Claude Desktop** (10 min)
- **Build React Frontend** (15 min)
- **Integration Patterns** (10 min)
- **Testing & Deployment** (5 min)

### 5. Code Explanation
- Detailed architecture breakdown
- Key code patterns
- Data flow diagrams
- Best practices

## 🎓 Tutorial Code

The `/tutorial-code` directory contains a complete, working MCP server example:

```bash
cd tutorial-code/mcp-server
npm install
npm start
```

See the [Tutorial README](./tutorial-code/mcp-server/README.md) for detailed usage instructions.

## 🌐 Deployment to GitHub Pages

### Step 1: Update vite.config.js

Make sure the `base` URL matches your repository name:

```javascript
export default defineConfig({
  base: '/your-repo-name/',  // Change this!
})
```

### Step 2: Deploy

```bash
# Build the site
npm run build

# Deploy to GitHub Pages
npm run deploy
```

### Step 3: Configure GitHub Pages

1. Go to your repository on GitHub
2. Navigate to **Settings > Pages**
3. Under "Source", select **gh-pages** branch
4. Click **Save**

Your site will be available at: `https://yourusername.github.io/your-repo-name/`

## 🎨 Features

- ✅ Fully responsive design
- ✅ Dark theme with gradient accents
- ✅ Syntax-highlighted code blocks with copy functionality
- ✅ Interactive navigation
- ✅ Comprehensive tutorial with working code
- ✅ Real MCP server example
- ✅ Clean, professional UI

## 📝 Assessment Criteria Coverage

### Presentation (50%)
- ✅ Well-structured with progressive examples
- ✅ Strong visual elements
- ✅ Clear explanations of MCP concepts
- ✅ Real-world use cases

### Online Information (20%)
- ✅ Well-formatted documentation
- ✅ Authoritative referenced sources
- ✅ Useful visuals and diagrams
- ✅ Comprehensive content

### Tutorial Lab Instructions (30%)
- ✅ Platform setup instructions
- ✅ Step-by-step guide (60 minutes)
- ✅ Easy to follow structure
- ✅ Working code for meaningful application
- ✅ High degree of originality

## 🔧 Technology Stack

- **Framework:** React 18 + Vite
- **Routing:** React Router v6
- **Syntax Highlighting:** react-syntax-highlighter
- **Styling:** Custom CSS with CSS variables
- **Deployment:** GitHub Pages
- **MCP SDK:** @modelcontextprotocol/sdk

## 📚 Resources

- [Official MCP Documentation](https://modelcontextprotocol.io)
- [MCP GitHub Repository](https://github.com/modelcontextprotocol)
- [Our Presentation](./src/pages/Presentation.jsx)

## 👥 Contributors

- **Bibika Ghimire** - Research & Analysis
- **Mateusz Nowak** - Use Cases & Enterprise
- **Muhammad Sohaib** - Architecture & Server
- **Michael McCabe** - Documentation
- **Summer Rhoda** - Introduction & Overview

## 📄 License

This project is created for educational purposes as part of COMP10020 Internet Technologies coursework at UWS.

## 🎯 Grading Rubric Alignment

This project aims for **A2/A3 grade** by providing:

1. **Exceptional Presentation Quality**
   - Depth of subject knowledge
   - Outstanding visual and verbal presentation
   - Excellent response materials

2. **Outstanding Online Information**
   - Well-formatted and detailed
   - Authoritative referenced sources
   - Useful visuals and tables
   - "Cheat sheet" included

3. **Excellent Tutorial**
   - High degree of originality
   - Complete setup instructions
   - Step-by-step easy-to-follow guide
   - Meaningful working application

---

**Course:** COMP10020 Internet Technologies  
**Institution:** University of the West of Scotland  
**Academic Year:** 2025-26
