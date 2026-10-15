# Paper-presentation-template

A modern, responsive paper/project presentation website template built with **Next.js (App Router)**, **React**, **Tailwind CSS**, and a set of reusable UI/section components.  
Use it to showcase a research paper, course project, or open-source work with sections like **Title**, **Abstract**, **Method**, **Formulas (LaTeX)**, **Tables**, **Charts**, **Visualizations**, **FAQ**, and **BibTeX**.

## Preview

- Local preview: run the project and open `http://localhost:3000`
- Recommended deployment: Vercel / any Node.js hosting

> Tip: Replace the demo content in `app/page.tsx` to make it your own.

---

## Features

- **Paper-style landing page** layout (clean typography + centered content)
- Modular sections:
  - Title / Authors / Affiliations / Venue / Links
  - Abstract + Keywords
  - Markdown-like rich content (React nodes)
  - LaTeX formulas (KaTeX)
  - Results table (supports LaTeX + bold cells)
  - Charts (Recharts)
  - Image slider comparisons
  - Collapsible FAQ
  - BibTeX copy block
- **Responsive** design for desktop/tablet/mobile
- Utility UI components (shadcn/ui-style) located in `components/ui`
- Dark mode via `next-themes` (if enabled in your layout/provider)

---

## Tech Stack

- **Next.js** (App Router)
- **React**
- **Tailwind CSS**
- **Radix UI** primitives (via UI components)
- **Recharts** for charts
- **KaTeX** for LaTeX rendering

---

## Getting Started

### 1) Install dependencies

This repo uses **pnpm** (recommended).

```bash
pnpm install
````

If you prefer npm/yarn, it may work, but pnpm is the best match for the lockfile.

### 2) Run the development server

```bash
pnpm dev
```

Open `http://localhost:3000` in your browser.

### 3) Build for production

```bash
pnpm build
pnpm start
```

---

## Customize Content

All demo content lives in:

* `app/page.tsx`

Typical items to change:

* Paper/project title, authors, affiliations, venue
* Links (paper/arxiv/code/data/video)
* Abstract + keywords
* Method section content
* Formulas array
* Table headers/rows
* Chart data + series names
* Image slider content
* FAQ items
* BibTeX entry
* Footer name

### Recommended pattern: single config object

To keep things reusable, define a `DEMO`/`siteConfig` object and reference it throughout `page.tsx` (method name, venue, links, etc.). This prevents hardcoding and makes open-sourcing easier.

---

## Project Structure

```text
.
├── app/
│   ├── layout.tsx
│   ├── page.tsx              # Main page (edit this for your content)
│   └── globals.css
├── components/
│   ├── header.tsx
│   ├── theme-provider.tsx
│   ├── sections/             # Paper sections (Title/Abstract/Table/Chart/...)
│   └── ui/                   # UI primitives (buttons, dialog, table, etc.)
├── public/                   # Icons & placeholder images
├── styles/
│   └── globals.css
└── README.md
```

### Sections (`components/sections`)

* `title-section.tsx` – title, author list, affiliations, venue, links
* `abstract-section.tsx` – abstract + keywords
* `markdown-section.tsx` – accepts rich React node content
* `latex-section.tsx` – formula list + descriptions
* `table-section.tsx` – table rendering (supports LaTeX/bold cells)
* `chart-section.tsx` – chart rendering (Recharts)
* `image-slider-section.tsx` – before/after slider style visualizations
* `collapse-section.tsx` – FAQ accordion/collapsible list
* `bibtex-section.tsx` – BibTeX snippet block

---

## Adding Your Own Sections

1. Create a new component in `components/sections/your-section.tsx`
2. Import it in `app/page.tsx`
3. Place it in the layout with dividers as needed

Keep props simple and data-driven so it stays a “template” instead of a single-purpose site.

---

## Deployment

### Vercel (recommended)

* Push to GitHub
* Import into Vercel
* Deploy

No special configuration is required for most cases.

---

## License

This project is licensed under the **MIT License**.
See `LICENSE` for details.

---

## Credits

* Built with Next.js + Tailwind CSS
* UI primitives inspired by the shadcn/ui approach
* LaTeX rendering powered by KaTeX
* Charts powered by Recharts
