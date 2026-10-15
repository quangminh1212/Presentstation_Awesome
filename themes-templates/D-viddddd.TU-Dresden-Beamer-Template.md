# TU-Dresden-Beamer-Template

Clean, lightweight Beamer appearance inspired by TU Dresden’s current corporate design. **This is an unofficial template** provided for personal and academic presentations; it is not affiliated with or endorsed by TU Dresden. The demo presentation shows a white canvas with TU blue accents, a compact footline, and a progress headline. It draws ideas from TU Dresden’s official corporate design manuals and community Beamer themes such as `beamerthemetud` as well as clean blue layouts seen in Tsinghua University slides like [THUBeamer](https://github.com/tl3shi/THUBeamer), while simplifying the setup for quick reuse.

## Highlights
- Original lightweight theme: `template/beamerthemeTUDneo.sty`
- Official 2025 layout: `template/beamerthemeTUDofficial2025.sty` with cover helper and selectable compact or spread footlines
- Outline frame auto-breaks across slides with compact spacing that only expands when subsections exist
- Cover date line configurable via `\completiontime{<text>}` plus centered title/subtitle typography
- Progress indicator in the headline (toggle with `headprogress=false`)
- Automatic logo helper `\TUDCenteredLogo{<basename>}` supporting PDF/PNG/JPG/SVG
- Ships with a XeLaTeX-first toolchain (`latexmk`) and sensible defaults for assets in `assets/`

## Quick start
```bash
# Recommended builds (XeLaTeX + Biber)
latexmk -xelatex example/demo.tex           # Lightweight neo theme demo
latexmk -xelatex example/demo_official.tex         # Compact official footline
latexmk -xelatex example/demo_official_spread.tex  # Spread official footline

# Optional fallback
pdflatex example/demo.tex && pdflatex example/demo.tex
```

Requirements: TeX Live (or MiKTeX) with `latexmk`, `biblatex`, and XeLaTeX enabled. If you want SVG logo support you also need the `svg` package **and** Inkscape on your PATH.

VS Code (LaTeX Workshop) users can just press `Cmd+S` on macOS or `Ctrl+S` on Windows: the extension triggers the bundled `latexmk` workflow automatically.

## Using the theme
```tex
\documentclass{beamer}
\usepackage{graphicx}
\graphicspath{{../assets/}}
\usepackage[headprogress=true]{beamerthemeTUDneo}

\title{Your Talk}
\author{You}
\begin{document}

\begin{frame}[plain]
  \TUDCenteredLogo[0.15\paperwidth]{Logo_TU_Dresden_2025}
  \titlepage
\end{frame}

\end{document}
```

### 2025 official slides template
```tex
\documentclass[aspectratio=169]{beamer}
\usepackage[headprogress=true,footline=compact]{beamerthemeTUDofficial2025}

\title[Short Presentation Title]{Full Presentation Title}
\subtitle{Optional Subtitle}
\author[Presentation Team]{Author One \\ Author Two \\ Author Three}
\TUDSetSpeaker{Author One} % current speaker; used only in the footline

\begin{document}

\completiontime{Finished \today} % optional; defaults to \insertdate
\TUDOfficialTitleFrame % auto cover: TU blue background + logo

\begin{frame}{Agenda}
  \tableofcontents
\end{frame}

\end{document}
```
`beamerthemeTUDofficial2025` mirrors the official corporate PPT (Brillantblau (#00008C) cover, white content canvas, TU footer). Select `footline=compact` for `TUD • short title • current speaker • Slide N` in one group, or `footline=spread` to keep the title and speaker on the left while aligning `Slide N` at the right edge. The optional argument of `\title`, such as `\title[Short Presentation Title]{Full Presentation Title}`, supplies the footer title. Keep the complete list of contributors in `\author{...}` for the cover and PDF metadata, and use `\TUDSetSpeaker{<name>}` only for the person presenting the current slides. This separation prevents a long author list from overflowing the footline. If no speaker is set, the speaker field and its preceding separator are omitted. Use `\completiontime{<text>}` before `\begin{document}` to override the cover’s date line (falls back to `\insertdate` if omitted).

For a presentation split across multiple files, set the speaker inside each file before its frames. This makes the active speaker explicit without changing the shared author list:

```tex
% main.tex
\author{Author One \\ Author Two \\ Author Three}
\input{part-one}
\input{part-two}

% part-one.tex
\TUDSetSpeaker{Author One}
\begin{frame}{First Part}
  % ...
\end{frame}

% part-two.tex
\TUDSetSpeaker{Author Two}
\begin{frame}{Second Part}
  % ...
\end{frame}
```

Place logos and other assets in `assets/`. The default latexmk configuration (`.latexmkrc`) writes each PDF next to its source file and extends `TEXINPUTS`/`XDVIPDFMXINPUTS` so XeLaTeX and the PDF driver can find the shared files. It also adds the root `ref/` directory to `BIBINPUTS`, so `\addbibresource{../ref/refs.bib}` works from inside `example/`.

## Project layout
```
TU-Dresden-Beamer-Template/
├─ assets/                      # Logos, sample graphics
├─ example/
│  ├─ demo.tex                  # Showcases the lightweight theme
│  ├─ demo_official.tex         # Official 2025 theme, compact footline
│  └─ demo_official_spread.tex  # Same official demo, spread footline
├─ template/
│  ├─ beamerthemeTUDneo.sty             # Lightweight theme
│  └─ beamerthemeTUDofficial2025.sty    # Official TU blue template
├─ ref/                         # Example BibLaTeX database
├─ .latexmkrc                   # latexmk configuration (XeLaTeX by default)
├─ Makefile                     # Convenience targets for CI/local builds
└─ README.md
```

## Tips
- The demo uses `latexmk -xelatex` and Biber; rerun the command after editing slides.
- `\TUDCenteredLogo` prefers PDF/PNG/JPG/JPEG assets. If only an SVG exists and the `svg` package is loaded, it will call `\includesvg`; otherwise it emits a warning.
- Want a darker background? Fork the theme and tweak `structure`, `normal text`, and block colors directly in `template/beamerthemeTUDneo.sty`.

## License
LaTeX Project Public License (LPPL) 1.3c or later. See `LICENSE` or <https://www.latex-project.org/lppl/lppl-1-3c/>. Avoid committing trademarked logos you are not licensed to distribute.
