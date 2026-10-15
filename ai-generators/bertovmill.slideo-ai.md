# Slideo

A modern, AI-powered presentation generator that transforms documents into professional slides with real-time collaboration features.

## 🚀 Overview

Slideo is a full-stack application that combines the power of AI with modern web technologies to create stunning presentations. Users can upload documents (PDF, DOCX, TXT, MD), and the system will automatically generate professional slides with customizable themes and layouts.

## ✨ Features

### Core Features
- **AI-Powered Slide Generation**: Transform documents into professional presentations
- **Real-time Collaboration**: WebSocket-based live editing and chat
- **Multi-format Support**: Upload PDF, DOCX, TXT, and Markdown files
- **Theme Customization**: Professional themes with color scheme options and logo-based color extraction
- **Export Options**: Download presentations in multiple formats with **1:1 canvas-to-PPTX fidelity**
- **Professional Templates**: 8+ curated Fabric.js templates for business presentations
- **Responsive Design**: Works seamlessly across all devices

### Technical Features
- **Modern Frontend**: Next.js 14 with TypeScript and Tailwind CSS
- **Real-time Backend**: Python FastAPI with WebSocket support
- **Authentication**: Supabase-powered user management
- **File Processing**: Advanced document parsing and content extraction
- **AI Integration**: LLM-powered content analysis and slide generation
- **Theme Engine**: Advanced color palette extraction from logos and images with file upload and clipboard paste support
- **Canvas-to-PPTX Export**: Direct Fabric.js canvas export for pixel-perfect PowerPoint generation

## 🏗️ Architecture

```
slideflip/
├── app/                    # Next.js frontend application
├── backend/               # Python FastAPI backend
├── components/            # React components
├── hooks/                # Custom React hooks
├── lib/                  # Utility libraries
├── services/             # API services
└── types/                # TypeScript type definitions
```

## 🎨 Professional Templates

Slideo comes with 8+ professionally designed templates built with Fabric.js for pixel-perfect rendering:

### **Business & Professional**
- **Hero Title**: Bold opening slides with layered design and CTA buttons
- **Professional Gradient**: Modern gradient backgrounds with glass morphism effects
- **Three Column KPIs**: Clean metric displays with descriptive text
- **Feature Comparison**: Two-column analysis with checkmarks and action buttons
- **Financial Consultant**: Comprehensive financial analysis for earnings calls and financial reports

### **Modern & Creative**
- **Timeline**: Horizontal project phases with milestone tracking
- **Modern Cards**: Three-column card layout with colored headers
- **Data Visualization**: Charts and metrics for analytics presentations
- **Quote & Testimonial**: Dark-themed inspirational content with attribution

All templates feature:
- **16:9 aspect ratio** for standard presentations
- **Professional color schemes** optimized for business use
- **Fabric.js rendering** for 1:1 PowerPoint export fidelity
- **Responsive design** that works across all devices

## 🛠️ Tech Stack

### Frontend
- **Framework**: Next.js 14 with App Router
- **Language**: TypeScript
- **Styling**: Tailwind CSS + shadcn/ui
- **Authentication**: Supabase Auth
- **Real-time**: WebSocket connections
- **Deployment**: Vercel

### Backend
- **Framework**: FastAPI (Python)
- **WebSocket**: WebSocket support for real-time communication
- **File Processing**: Multiple format support (PDF, DOCX, TXT, MD)
- **AI Integration**: LLM-powered content analysis
- **Database**: File-based storage with structured data
- **Deployment**: Docker-ready

## 🚀 Quick Start

### Prerequisites
- Node.js 18+
- Python 3.11+
- Supabase account
- Git

### 1. Clone the Repository
```bash
git clone <repository-url>
cd slideflip
```

### 2. Frontend Setup
```bash
# Install dependencies
npm install
```

## 🔧 Recent Fixes & Improvements

### Thumbnail Overflow Resolution (Latest)
**Issue**: Thumbnails across the application were experiencing overflow issues due to hardcoded scaling values that didn't account for different content sizes and container dimensions.

**Solution**: Implemented responsive scaling system across all thumbnail components:
- **Dynamic Scale Calculation**: Scale is now calculated based on container width using `Math.max(0.35, Math.min(0.75, containerWidth / 500))`
- **Responsive Width/Height**: Width and height are dynamically calculated as `100 / scale` to prevent overflow
- **Window Resize Handling**: Added resize observers to recalculate scaling when window size changes
- **Smooth Transitions**: Added fade-in effects and opacity transitions for better UX
- **Overflow Protection**: Added `overflow-hidden` and max-width/height constraints

**Files Fixed**:
- `app/presentations/page.tsx` - Main presentations grid
- `app/presentations/[id]/page.tsx` - Individual presentation view
- `app/page.tsx` - Home page presentations and templates
- `app/templates/page.tsx` - Templates grid
- `components/test-response-handler.tsx` - Test component previews

**Benefits**:
- ✅ No more thumbnail overflow issues
- ✅ Consistent scaling across different screen sizes
- ✅ Better responsive behavior
- ✅ Improved user experience with smooth transitions
- ✅ Maintains aspect ratios while preventing content overflow

#### Markdown rendering in Content Planning

The Content Planning step now renders the proposed plan using Markdown and uses a formatted WYSIWYG editor for changes (no raw Markdown or preview pane during editing).

Install the required packages (already listed in `package.json`):

```bash
npm install react-markdown remark-gfm marked turndown
```

No additional configuration is required.

### 3. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials and keys

# Start the backend server
python main.py
```

### 4. Database Setup

#### Supabase Configuration
The application uses Supabase for authentication and data storage. You'll need to:

1. Create a Supabase project at [supabase.com](https://supabase.com)
2. Get your project URL and anon key from the project settings
3. Add them to your `.env.local` file:

```bash
NEXT_PUBLIC_SUPABASE_URL=your_supabase_project_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key
SUPABASE_SERVICE_ROLE_KEY=your_service_role_key
```

#### Recent Database Fixes
If you encounter the error "infinite recursion detected in policy for relation 'workspace_members'" when uploading templates, run the SQL script in `scripts/fix-workspace-members-recursion.sql` in your Supabase SQL editor. This fixes RLS policy issues that can cause template uploads to fail.

#### Database Migrations
Run the following migrations in order in your Supabase SQL editor:
1. `001_create_slide_templates.sql` - Creates the base slide templates table
2. `011_workspace_members_invitations.sql` - Creates workspace collaboration system
3. `014_fix_slide_templates_and_workspace_members.sql` - Fixes RLS recursion issues
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start backend server
python main.py
```

Quick start from project root:

```bash
# one-command start from repo root
npm run backend:start
```

#### PDF and DOCX parsing

The backend now supports server-side text extraction from PDF and DOCX uploads using `pdfminer.six` and `python-docx`.

- Ensure you have the virtual environment activated (`source venv/bin/activate`).
- Dependencies are included in `backend/requirements.txt` and are installed with the step above.
- The WebSocket upload flow automatically extracts text for `.pdf` and `.docx` files via the backend.
- The REST endpoint `POST /api/parse-documents` will mark PDFs/DOCX as “Uploaded for server-side parsing” and rely on the WebSocket pipeline for full extraction.

### 4. Access the Application
- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📖 Documentation

### Frontend Documentation
- [Frontend README](./FRONTEND_README.md) - Complete frontend guide
- [Component Architecture](./FRONTEND_README.md#component-architecture)
- [Authentication Setup](./FRONTEND_README.md#authentication)
- [Real-time Features](./FRONTEND_README.md#real-time-features)

### Backend Documentation
- [Backend README](./backend/README.md) - Complete backend guide
- [API Documentation](./backend/README.md#api-endpoints)
- [WebSocket Communication](./backend/README.md#websocket-communication)
- [File Processing](./backend/README.md#file-processing)

### Additional Documentation
- [Frontend Integration](./backend/docs/FRONTEND_INTEGRATION.md)
- [LLM Integration](./backend/docs/LLM_INTEGRATION_README.md)
- [Content Storage](./backend/docs/CONTENT_STORAGE_README.md)
- [Slide Generation](./backend/docs/SLIDE_GENERATION_README.md)
- [HTML Features](./backend/docs/HTML_FEATURES_README.md)
- [Implementation Summary](./backend/docs/IMPLEMENTATION_SUMMARY.md)
- [pptxgenjs Documentation](./docs/pptxgenjs/README.md) - Complete guide for PowerPoint generation
- [Fabric.js Documentation](./docs/fabricjs/) - Complete guide for canvas-based slide editing and rendering

## 🔧 Configuration

### Environment Variables

All variables are demonstrated in `.env.example` at the repo root. Copy it to `.env` (root) for the frontend and to `backend/.env` for the Python backend.

#### Root `.env` (Next.js / server routes)
```env
# Supabase client (required)
NEXT_PUBLIC_SUPABASE_URL=your_supabase_url
NEXT_PUBLIC_SUPABASE_ANON_KEY=your_supabase_anon_key

# Backend URLs used by the app
# For local development:
NEXT_PUBLIC_BACKEND_URL=http://localhost:8000
NEXT_PUBLIC_BACKEND_WS_URL=ws://localhost:8000

# For production (using deployed Google Cloud Run backend):
# NEXT_PUBLIC_BACKEND_URL=https://slideflip-backend-167734449742.us-central1.run.app
# NEXT_PUBLIC_BACKEND_WS_URL=wss://slideflip-backend-167734449742.us-central1.run.app

# AI keys
OPENAI_API_KEY=your_openai_api_key            # required for AI features
TAVILY_API_KEY=                                # optional, research API for /api/research

# LDAP (optional; enable if using corporate directory)
LDAP_URL=ldap://your-ldap-server:389
LDAP_BASE_DN=dc=yourcompany,dc=com
LDAP_BIND_DN=cn=admin,dc=yourcompany,dc=com
LDAP_BIND_PASSWORD=your-admin-password
LDAP_USER_SEARCH_BASE=ou=users,dc=yourcompany,dc=com
LDAP_USER_SEARCH_FILTER=(uid={username})
LDAP_GROUP_SEARCH_BASE=ou=groups,dc=yourcompany,dc=com
LDAP_GROUP_SEARCH_FILTER=(member={userDn})

# Node scripts (do not expose to browsers)
SUPABASE_SERVICE_ROLE_KEY=
```

### Fallback slide generation

If AI generation is unavailable (for example, `OPENAI_API_KEY` is missing or rate-limited), the Preview step will automatically load a local fallback slide so you can proceed through the flow:

- Fallback endpoint: `GET /api/fallback-slide` reads `templates/imported-02.html` and returns it as `slideHtml`.
- If both AI and the fallback fail, the UI shows a placeholder image (`cat-slide-placeholder`).

You can replace the fallback HTML by editing `templates/imported-02.html`.

### Google OAuth + Supabase

This project uses Supabase Auth with Google as an OAuth provider. Configure it once for production and local development.

1) Google Cloud Console → Credentials → Your Web OAuth client

- Authorized redirect URIs (exactly one for Supabase):
  - `https://wyelvtfmvjturmxhoqfd.supabase.co/auth/v1/callback`
- Authorized JavaScript origins (where your app is served from):
  - `http://localhost:3000` or `http://localhost:3001` (match your local port)
  - Your production origin (for example `https://slideflip.vercel.app`)

Why: Google redirects back to Supabase, not directly to your app. Supabase finishes the OAuth handshake and then redirects the browser to your app using the URL you pass as `redirectTo` in code.

2) Supabase → Authentication → URL configuration

- Site URL: your production site (e.g., `https://slideflip.vercel.app`). For local‑only testing, you can temporarily set this to `http://localhost:3001`.
- Redirect URLs (allowlist): add the origins and callback routes you will use in development and production, for example:
  - `http://localhost:3000`
  - `http://localhost:3000/auth/callback`
  - `http://localhost:3001`
  - `http://localhost:3001/auth/callback`
  - `https://slideflip.vercel.app`
  - `https://slideflip.vercel.app/auth/callback`

3) App behavior (already implemented)

- The app initiates OAuth with `redirectTo: ${window.location.origin}/auth/callback`.
- The route handler at `app/auth/callback/route.ts` exchanges the code for a session and then redirects to `/` (or the `next` param if present).

Troubleshooting

- If logging in on localhost sends you to production, your localhost URL is likely missing from Supabase “Redirect URLs,” so Supabase falls back to the Site URL.
- After changing Google or Supabase settings, wait 1–2 minutes, sign out, and retry. Clearing cookies for localhost and your prod domain can also help.

#### Backend `backend/.env` (FastAPI)
```env
# Host/port and operational flags
HOST=0.0.0.0
PORT=8000
DEBUG=True

# Security
SECRET_KEY=your_secret_key

# Storage and limits
UPLOAD_DIR=uploads
MAX_FILE_SIZE=52428800

# AI key (backend will also read OPENAI_API_KEY if present here)
OPENAI_API_KEY=your_openai_api_key
```

## 🧪 Testing

### Frontend Tests
```bash
npm run test
npm run test:integration
npm run test:e2e
```

### Backend Tests
```bash
cd backend
python -m pytest tests/
```

## 🚀 Deployment

### Frontend (Vercel)
1. Connect your GitHub repository to Vercel
2. Configure environment variables in Vercel dashboard
3. Deploy automatically on push to main branch

#### Note on bundling Node-only modules

The app uses `pptxgenjs` for PPTX export in the browser. Some versions of this library include conditional imports of Node built-ins like `node:fs` and `node:https` inside the ESM bundle, which can cause bundlers to error when creating client chunks. To prevent this, the Next.js config stubs these modules for the browser build via aliases in `next.config.ts`:

```ts
// next.config.ts (excerpt)
webpack: (config, { isServer }) => {
  if (!isServer) {
    config.resolve.alias = {
      ...(config.resolve.alias || {}),
      'node:fs': false,
      'node:https': false,
      fs: false,
      https: false,
      'image-size': false,
      path: false,
      os: false,
      'node:path': false,
    };
    // Optional compatibility fallbacks
    // @ts-ignore
    config.resolve.fallback = { ...(config.resolve.fallback || {}), fs: false, https: false, path: false, os: false };
  }
  return config;
}
```

This ensures successful builds on Vercel while keeping runtime behavior unchanged in the browser.

### Backend Deployment

#### Local Development
```bash
cd backend
source venv/bin/activate
python main.py
```

#### Google Cloud Run (Production)
The backend is deployed to Google Cloud Run at:
**https://slideflip-backend-167734449742.us-central1.run.app**

To deploy updates:
```bash
cd backend
gcloud builds submit --config cloudbuild.yaml .
```

Configuration:
- **Docker**: Uses `backend/Dockerfile` for containerization
- **Cloud Build**: Automated deployment via `backend/cloudbuild.yaml`
- **Environment**: Production variables set via Google Secret Manager
- **Secrets**: OpenAI API key stored securely in Secret Manager
- **Resources**: 2GB memory, 4 CPU, auto-scaling 1-2 instances

#### Docker (Alternative)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## 🔄 Development Workflow

### Recent Updates
- **Documentation**: Added comprehensive pptxgenjs documentation in `docs/pptxgenjs/` covering installation, usage, features, and API reference
- **Scripts**: Added utility scripts in `scripts/` directory for HTML to Markdown conversion
- **Templates**: Added weekly schedule template and YouTube description template
- **Build fix**: added missing `lib/fabric-to-slide.ts` and corrected `lib/index.ts` imports for Next.js bundling on Vercel.
- **Invite acceptance flow**: wrapped `useSearchParams` in a Suspense boundary for `/invite/accept` to satisfy Next.js requirements and ensure production builds succeed.
- **Rebranded visible UI text**: from "SlideFlip" to "Slideo" across pages and templates; PPTX metadata now uses "Slideo" and "Slideo AI".

- Added reusable card style `card-contrast` in `app/globals.css` for high-emphasis cards with thin white borders on dark backgrounds. Apply it via `className="card-contrast"` alongside `variant="glass"` on `Card` components.
 - Updated `card-contrast` to use a hairline `0.5px` border for a more refined outline on high-DPI displays.
 - Added `builder-background` utility (Supabase-like pointillism) with a slightly lighter dark base. Applied to the builder root container in `app/build/page.tsx`.

- Theme step UX: the Template selection and Color Palette sections are now collapsible using shadcn/ui `Accordion`. This makes the page easier to scan while preserving all functionality.
  - New component: `components/ui/accordion.tsx`
  - Updated: `components/builder/theme-step.tsx`

- Templates now support Fabric.js/PptxGenJS JSON in Supabase:
  - Added migration `009_update_slide_templates_for_fabric.sql` to add `slide_json JSONB` to `slide_templates`.
  - API `app/api/examples/list` now prefers `slide_templates` with `slide_json` and falls back to legacy HTML examples.
  - Template cards in `ThemeStep` can preview either HTML or Fabric JSON.
  - Seed examples: `templates/fabric/hero-title-01.json`, `templates/fabric/three-column-kpis-01.json`.
  - Upsert endpoint: `POST /api/templates/upsert-fabric` with body `{ id, name, description?, theme?, aspect_ratio?, tags? }` reads `templates/fabric/{id}.json` and stores it as `slide_json`.

### Seeding Fabric templates

```bash
curl -s -X POST http://localhost:3000/api/templates/upsert-fabric \
  -H 'Content-Type: application/json' \
  -d '{"id":"hero-title-01","name":"Hero Title"}'

curl -s -X POST http://localhost:3000/api/templates/upsert-fabric \
  -H 'Content-Type: application/json' \
  -d '{"id":"three-column-kpis-01","name":"Three Column KPIs"}'

# New: Professional Gradient template
curl -s -X POST http://localhost:3000/api/templates/upsert-fabric \
  -H 'Content-Type: application/json' \
  -d '{"id":"professional-gradient-01","name":"Professional Gradient"}'

# Note: `id` refers to the JSON filename under templates/fabric; the DB row id remains a UUID.
```

Bulk import all Fabric templates found in `templates/fabric` at once:

```bash
curl -s -X POST http://localhost:3000/api/import-fabric-templates
```

### Debugging preview rendering

- Visit `/test-fabric` to load all templates from `/api/examples/list` and preview them.
- The page renders Fabric JSON on a canvas and shows the raw JSON for quick inspection.
 - Sidebar includes "My Templates" entry linking to `/templates`.
 - New page: `/templates` lists templates from `slide_templates` with Fabric and HTML previews.

### Assets
- `public/slideo-waitlist.png` — static image used on the Waitlist page (QR/preview).
- Landing page CTAs updated: all "Get Started" buttons now navigate to `'/auth/login'` so users are prompted to sign in before creating content.
- Landing page bottom CTA alignment: "View Examples" button height now matches "Start Free Trial" for a uniform appearance.
 - Added a new route `'/waitlist'` accessible from the sidebar as "Waitlist QR Code". Users can scan a QR or submit an email to join the waitlist. Emails are stored in Supabase table `waitlist_emails` (see migration `004_create_waitlist_emails.sql`).
 - The waitlist page shows both a dynamic QR that points to the current `/waitlist` URL and a static QR image at `public/slideo-waitlist.png` if you want to reuse a branded code offline.

### Waitlist feature setup

1. Install dependency for QR rendering in the frontend:

```bash
npm install react-qr-code
```

2. Apply Supabase migration to create the table:

```sql
-- supabase/migrations/004_create_waitlist_emails.sql
CREATE TABLE IF NOT EXISTS waitlist_emails (
  id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
  email TEXT NOT NULL,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE UNIQUE INDEX IF NOT EXISTS idx_waitlist_unique_email ON waitlist_emails(email);
```

3. Usage

- Navigate to `Waitlist QR Code` in the sidebar or go to `http://localhost:3000/waitlist`.
- Scan the QR to open the page on mobile or submit an email in the form. Entries appear in the `waitlist_emails` table in Supabase.

### Adding New Features

1. **Frontend Changes**:
   - Create feature branch
   - Add components in `components/`
   - Update types in `types/`
   - Test with `npm run test`

2. **Backend Changes**:
   - Add API endpoints in `main.py`
   - Create services in `src/services/`
   - Add models in `src/models/`
   - Test with pytest

3. **Integration**:
   - Update WebSocket messages
   - Test real-time features
   - Verify API communication

### Code Style
- **Frontend**: ESLint + Prettier
- **Backend**: Black + isort
- **TypeScript**: Strict mode enabled
- **Python**: Type hints required

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow the existing code style
- Add tests for new features
- Update documentation
- Ensure all tests pass
- Test both frontend and backend integration

## 🐛 Troubleshooting

### Common Issues

#### Frontend Issues
- **Authentication Problems**: Check Supabase configuration
- **WebSocket Issues**: Verify backend is running
- **Build Errors**: Clear node_modules and reinstall

#### Backend Issues
- **Import Errors**: Check Python environment
- **File Upload Issues**: Verify upload directory permissions
- **WebSocket Connection**: Check firewall settings

#### Integration Issues
- **CORS Errors**: Verify backend CORS configuration
- **WebSocket Connection**: Check WebSocket URL
- **API Communication**: Verify environment variables

## 📊 Performance

### Frontend Optimization
- Code splitting and lazy loading
- Image optimization with Next.js
- Bundle analysis and optimization
- Caching strategies

### Backend Optimization
- Async file processing
- Connection pooling
- Memory-efficient file handling
- Configurable concurrent processing

## 🔒 Security

### Frontend Security
- Supabase authentication
- Environment variable protection
- Input validation
- XSS prevention

### Backend Security
- File type validation
- File size limits
- Filename sanitization
- Error message sanitization

## 📈 Monitoring

### Frontend Monitoring
- Vercel Analytics
- Error tracking
- Performance monitoring
- User analytics

### Backend Monitoring
- Health check endpoints
- Connection statistics
- Processing metrics
- Error logging

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Next.js](https://nextjs.org/) for the amazing React framework
- [Supabase](https://supabase.com/) for authentication and real-time features
- [Tailwind CSS](https://tailwindcss.com/) for utility-first styling
- [shadcn/ui](https://ui.shadcn.com/) for beautiful components
- [FastAPI](https://fastapi.tiangolo.com/) for the high-performance Python API

## 📞 Support

- **Documentation**: Check the README files in each directory
- **Issues**: Create an issue on GitHub
- **Discussions**: Use GitHub Discussions for questions
- **Email**: Contact the development team

---

**Made with ❤️ by the Slideo Team**
