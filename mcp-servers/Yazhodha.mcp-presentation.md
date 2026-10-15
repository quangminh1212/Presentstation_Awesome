# Flight MCP Presentation

A modern, interactive presentation about the Flight MCP Server built with React, TypeScript, and Tailwind CSS.

![MCP Presentation](https://img.shields.io/badge/React-18.3.1-blue?logo=react)
![TypeScript](https://img.shields.io/badge/TypeScript-5.6.2-blue?logo=typescript)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.4.17-38B2AC?logo=tailwind-css)
![Vite](https://img.shields.io/badge/Vite-5.4.20-646CFF?logo=vite)

## 🎯 Overview

This presentation provides a deep dive into the Flight MCP Server, covering:

- Business idea and why MCP
- Protocol overview and SDK usage
- .NET implementation and architecture
- API call flow, caching, and errors
- Demo flow for team walkthroughs

## ✨ Features

- **📱 Fully Responsive** - Works seamlessly on mobile, tablet, and desktop
- **👆 Touch Gestures** - Swipe left/right on mobile for navigation
- **⌨️ Keyboard Navigation** - Use arrow keys to navigate slides
- **🎨 Modern Design** - Beautiful gradients, animations, and transitions
- **🚀 Fast Performance** - Built with Vite for lightning-fast development and builds
- **🎭 Custom Animations** - Smooth transitions and engaging visual effects

## 🚀 Getting Started

### Prerequisites

- Node.js (v18 or higher)
- npm or yarn

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Yazhodha/flight-mcp-presentation.git
cd flight-mcp-presentation
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to:
```
http://localhost:5173/flight-mcp-presentation/
```

## 📦 Build & Deploy

### Production Build

```bash
npm run build
```

The built files will be in the `dist/` directory.

### Preview Production Build

```bash
npm run preview
```

### Deploy to GitHub Pages

This project is configured to automatically deploy to GitHub Pages when you push to the `main` branch.

Live demo: https://yazhodha.github.io/flight-mcp-presentation/

## 🎮 Controls

### Keyboard
- `→` or `Space` - Next slide
- `←` - Previous slide
- Click on slide indicators to jump to a specific slide

### Touch Devices
- Swipe left - Next slide
- Swipe right - Previous slide
- Tap on slide indicators to jump to a specific slide

## 📁 Project Structure

```
flight-mcp-presentation/
├── src/
│   ├── Presentation.tsx      # Main presentation component
│   ├── App.tsx               # App entry point
│   ├── index.css             # Custom styles and animations
│   └── main.tsx              # React entry point
├── public/                   # Static assets
├── .github/
│   └── workflows/
│       └── deploy.yml        # GitHub Pages deployment
├── CLAUDE.md                 # Project documentation for Claude Code
├── RESPONSIVE_CHANGES.md     # Mobile responsive design documentation
└── README.md                 # This file
```

## 🎨 Technology Stack

- **React 18.3.1** - UI library
- **TypeScript 5.6.2** - Type safety
- **Vite 5.4.20** - Build tool and dev server
- **Tailwind CSS 3.4.17** - Utility-first CSS framework
- **Lucide React** - Icon library

## 📱 Responsive Design

The presentation is fully optimized for all screen sizes:

### Mobile (< 640px)
- Vertical stacking of content
- Touch-friendly swipe navigation
- Optimized text sizes and spacing
- Hidden desktop-only controls

### Tablet (640px - 1024px)
- Balanced grid layouts (2 columns)
- Responsive typography
- Touch and keyboard navigation

### Desktop (> 1024px)
- Full grid layouts (2-3 columns)
- Large text and icons
- Keyboard navigation with arrow keys
- Hover effects and transitions

## 🎯 Key Slides

1. **Title Slide** - Flight MCP overview
2. **Agenda** - 30 minute deep dive
3. **Business Idea** - Conversational flight search
4. **MCP Primer** - Tools, resources, transport
5. **System Context** - Endpoints and integrations
6. **Architecture** - Clean architecture layers
7. **Tools** - Search, pagination, itinerary details
8. **Search Flow** - Stateless caching
9. **Tool Call Flow** - End-to-end diagram
10. **API Call Flow** - Polling, retry, circuit breaker
11. **Caching** - Providers and pagination
12. **Error Handling** - Degradation strategy
13. **Widget Resource** - UI + CSP metadata
14. **Demo** - Step-by-step scenario
15. **Reliability** - Observability and performance
16. **Wrap Up** - Next steps

## 🛠️ Development

### Adding New Slides

Add new slides to the `slides` array in `src/Presentation.tsx`:

```typescript
{
  content: (
    <div className="space-y-4 md:space-y-6">
      <h2 className="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold font-heading tracking-tight text-gray-800 mb-3 md:mb-6 animate-fade-in-up">
        Your Slide Title
      </h2>
      {/* Your slide content */}
    </div>
  )
}
```

### Custom Animations

Available animation classes (defined in `src/index.css`):
- `animate-fade-in`
- `animate-fade-in-up`
- `animate-slide-in-left`
- `animate-slide-in-right`
- `animate-scale-in`
- `animate-bounce-slow`
- `animate-pulse-slow`
- `animate-float`
- `animation-delay-{100-1000}` (100ms increments)

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👤 Author

**Yashodha Athureliyage**

- GitHub: [@Yazhodha](https://github.com/Yazhodha)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 🙏 Acknowledgments

- [Model Context Protocol](https://modelcontextprotocol.io) by Anthropic
- [Lucide Icons](https://lucide.dev) for beautiful icons
- [Tailwind CSS](https://tailwindcss.com) for styling utilities
- Built with assistance from [Claude Code](https://claude.com/claude-code)

## 📚 Resources

- [MCP Documentation](https://modelcontextprotocol.io)
- [TypeScript SDK](https://www.npmjs.com/package/@modelcontextprotocol/sdk)
- [Python SDK](https://pypi.org/project/mcp/)
- [.NET SDK](https://www.nuget.org/packages/ModelContextProtocol)

---

**Note**: This presentation was created for educational purposes to introduce developers to the Model Context Protocol.
