# Slidev Builder MCP v2.1 ���️

## **Never Lose Your Presentation Work Again!**

A revolutionary Model Context Protocol (MCP) server for creating professional Slidev presentations with **built-in Git Guardian protection**. Experience automatic backup, smart recovery, and bulletproof data protection.

## ���️ **NEW: Git Guardian Protection System**

### **Automatic Protection Features**
- ✅ **Real-time Auto-Backup**: Every edit automatically saved
- ✅ **Git Integration**: Automatic commits and version history  
- ✅ **Smart Recovery**: AI-powered restoration suggestions
- ✅ **File Monitoring**: Instant detection of changes and deletions
- ✅ **Emergency Restore**: One-click recovery from any backup point
- ✅ **Zero Configuration**: Protection works automatically

### **Protection Philosophy**
```
OLD WAY: Create → Lose Work → Panic → Try to Recover
NEW WAY: Create → Auto-Protect → Continue Confidently
```

## ��� **Core Features**

### **Professional Presentation Creation**
- ��� **Automated Slide Generation**: Create presentations with simple prompts
- ��� **Hatch Brand Integration**: Professional corporate themes and styling  
- ��� **Dynamic Charts**: Auto-generate interactive visualizations
- ���️ **Asset Integration**: Fetch icons and images from multiple APIs
- ⚡ **Interactive Components**: Animations, diagrams, and data visualizations
- ��� **Multi-format Export**: PDF, HTML, PowerPoint, and web applications

### **Advanced Capabilities** 
- ��� **Component Library**: Reusable presentation elements
- ��� **Team Collaboration**: Share and sync presentations
- ��� **Live Preview**: Real-time presentation development
- ��� **AI-Powered**: Smart content suggestions and optimization

## ��� **Installation**

### **Global Installation (Recommended)**
```bash
npm install -g @hatch/slidev-builder-mcp-v2
```

### **MCP Client Configuration**
Add to your MCP client (Claude Desktop, VS Code, etc.):

```json
{
  "mcpServers": {
    "slidev-builder-v2": {
      "command": "npx",
      "args": ["-y", "@hatch/slidev-builder-mcp-v2"]
    }
  }
}
```

## ���️ **Protection in Action**

### **Automatic Protection (No Setup Required)**
```bash
# Every operation is automatically protected:
"Create a presentation about AI strategy"
# → Auto-backup created, presentation built, success committed

"Add a slide with financial projections" 
# → Pre-operation backup, slide created, changes saved

"Apply the Hatch corporate theme"
# → Checkpoint created, theme applied, verified and committed
```

### **Smart Recovery** 
```bash
# If something goes wrong:
"I think I lost some content, can you help?"
# → AI analyzes backups: "Found 3 versions with that content:
#    1. 5 minutes ago (most recent)
#    2. 30 minutes ago (before theme change)  
#    3. 1 hour ago (complete version)"
```

## ��� **Available Tools**

### **Protected Creation Tools**
- `create_deck_protected` - Create presentations with automatic protection
- `create_slide` - Add slides with auto-backup
- `apply_theme` - Apply themes with rollback capability
- `generate_chart` - Create charts with version control

### **Protection Management**
- `backup_presentation` - Manual backup creation
- `restore_presentation` - Emergency recovery from backups
- `backup_status` - Check protection health
- `enable_protection` - Activate protection for existing projects

### **Component Library**
- `create_component` - Build reusable presentation elements
- `list_components` - Browse available components  
- `add_component` - Insert components into slides
- `publish_component` - Share components with team

## ��� **Professional Themes**

- **Hatch Corporate**: Professional business presentations
- **Hatch Executive**: C-level summary formats  
- **Hatch Technical**: Developer and engineering content
- **Hatch Client**: Customer-facing presentations

## ��� **Example Usage**

### **Create Protected Presentation**
```typescript
await mcp.callTool('create_deck_protected', {
  title: 'Q4 Strategic Review',
  template: 'hatch-corporate',
  outputPath: './presentations/q4-review',
  protection: {
    autoBackup: true,     // ✅ Automatic (default)
    gitIntegration: true, // ✅ Automatic (default)  
    fileWatching: true    // ✅ Automatic (default)
  }
});
```

### **Add Interactive Content**
```typescript
await mcp.callTool('create_slide', {
  deckPath: './presentations/q4-review',
  slideType: 'chart',
  content: {
    title: 'Revenue Growth',
    chartType: 'line',
    data: {
      labels: ['Q1', 'Q2', 'Q3', 'Q4'],
      values: [100, 120, 140, 180]
    }
  }
});
// ✅ Auto-protected: backup → create → verify → commit
```

## ��� **Development**

### **Local Setup**
```bash
git clone https://github.com/adolfosalasgomez3011/slidev-builder-mcp.git
cd slidev-builder-mcp
npm install
npm run build
npm link
```

### **Testing Protection**
```bash
# Test backup functionality
npm run protection:backup

# Test restore functionality  
npm run protection:restore

# Check protection status
npm run protection:status
```

## ��� **Why Slidev Builder MCP v2?**

### **For Professionals**
- ✅ **Zero Data Loss**: Never lose presentation work again
- ✅ **Enterprise Quality**: Hatch consulting-grade templates
- ✅ **Rapid Development**: Create presentations 10x faster
- ✅ **Team Ready**: Built for collaboration and sharing

### **For Developers**
- ✅ **MCP Standard**: Future-proof protocol compliance
- ✅ **TypeScript**: Full type safety and IntelliSense
- ✅ **Open Source**: MIT license for customization
- ✅ **Extensible**: Plugin architecture for custom features

## ��� **License**

MIT License - see [LICENSE](LICENSE) file for details.

## ��� **About Hatch**

Built by [Hatch Ltd](https://hatch.com), a leading engineering and consulting firm with 70+ years of expertise in mining, energy, and infrastructure. Our AI-Native Advisory Practice brings cutting-edge technology to traditional industries.

---

**���️ Your presentations are now bulletproof. Create with confidence!**
