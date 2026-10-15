# SII Beamer Theme

An unofficial LaTeX Beamer theme for Shanghai Innovation Institute (SII, 上海创智学院). The theme provides a 16:9 academic presentation style with SII logo assets, a branded title page, section overview pages, reusable color blocks, compact takeaway bars, and TikZ flowchart styles.

This repository is intended for academic talks, seminars, lectures, thesis defenses, and internal research presentations that need a consistent SII visual style.

## Preview

The example deck is available as [`sii-beamer.pdf`](sii-beamer.pdf). Rebuild it locally with XeLaTeX after editing the theme or example source.

## Files

```text
.
├── README.md
├── beamerthemesii.sty      # Beamer theme layout and templates
├── siicolor.sty            # SII color palette
├── sii-beamer.tex          # Clean example presentation source
├── sii-beamer.pdf          # Compiled example presentation preview
└── assets/
    ├── sii-background.png  # Title page background
    ├── SIIlogo.png         # White logo for dark pages
    ├── SIIlogo_blue.png    # Blue logo for light pages
    └── *.svg               # Source logo assets
```

## Requirements

- A TeX distribution such as TeX Live or MacTeX
- XeLaTeX
- `latexmk` is recommended

The example uses `xeCJK`, so XeLaTeX is recommended for Chinese text.

## Quick Start

Compile the example deck:

```bash
latexmk -xelatex sii-beamer.tex
```

If you do not use `latexmk`, compile directly with XeLaTeX:

```bash
xelatex sii-beamer.tex
```

## Minimal Example

```latex
\documentclass{beamer}

\usepackage{xeCJK}
\usetheme{sii}

\titlebackground{assets/sii-background}
\footlinecolor{maincolor}

\title{Presentation Title}
\subtitle{Presentation Subtitle}
\author{Your Name}
\date{\today}

\begin{document}

\maketitle
\overviewpage

\section{Introduction}

\begin{frame}{A Sample Slide}
  Hello, SII.
\end{frame}

\backmatter

\end{document}
```

## Theme Features

- Use `\usetheme{sii}` to load the theme.
- Use `\titlebackground{assets/sii-background}` to set the title page background.
- Use `\course{...}` for a small title-page label such as a course, venue, or talk type.
- Use `\footlinecolor{maincolor}` and `\footlinepayoff{...}` to configure the footer.
- Use `\overviewpage` after `\maketitle` to insert the table-of-contents overview page.
- Each `\section{...}` automatically inserts a section overview page and highlights the current section.
- Use `\backmatter` to add the closing thank-you page.

## Reusable Components

Highlighted blocks:

```latex
\begin{colorblock}{siiaccent}{Key Message}
  Important content goes here.
\end{colorblock}
```

Compact takeaway bar:

```latex
\takeaway{One sentence that summarizes the slide.}
```

Small tags:

```latex
\tagbox{maincolor}{METHOD}
\tagbox{siigreen}{RESULT}
```

Flowchart styles:

```latex
\begin{tikzpicture}
  \node[siiflowbox] (a) {Input};
  \node[siiflowbox,right=1.5cm of a] (b) {Output};
  \draw[siiflowarrow] (a) -- (b);
\end{tikzpicture}
```

Available colors are defined in [`siicolor.sty`](siicolor.sty), including `maincolor`, `siiblue`, `siidarkblue`, `siilightblue`, `siigrey`, `siiaccent`, `siired`, `siiyellow`, and `siigreen`.

## Development

The preview PDF is committed for convenient browsing. LaTeX intermediate files such as `*.aux`, `*.log`, `*.nav`, `*.snm`, `*.toc`, `*.vrb`, and `*.xdv` are ignored by Git.

To clean intermediate LaTeX files while keeping `sii-beamer.pdf`:

```bash
latexmk -c sii-beamer.tex
```

To rebuild the preview PDF:

```bash
latexmk -xelatex sii-beamer.tex
```

## License

The theme source is licensed under the GNU General Public License v3.0 or later (GPL-3.0-or-later), following the license notice in [`beamerthemesii.sty`](beamerthemesii.sty).

Logo and brand assets may be subject to Shanghai Innovation Institute's own visual identity and trademark rules. Shanghai Innovation Institute, SII, 上海创智学院, and related logos are names and marks of Shanghai Innovation Institute. This repository is an unofficial theme package.
