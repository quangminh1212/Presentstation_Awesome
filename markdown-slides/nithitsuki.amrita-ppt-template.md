# Slides for Amrita University

Create simple static slides with Typst for Amrita University presentations.

This package allows the creation of slides using standard Typst headings. It is designed to be lightweight and easy to use.

## Multiple Title Slide themes!

<p style="display:flex; gap:12px; align-items:center;">
<img src="./assets/title-min.png" style="width:320px;">
<img src="./assets/title.png" style="width:320px;">
</p>

## Dense & Non-Dense Modes!
<p style="display:flex; gap:12px; align-items:center;">
<img src="./assets/dense.png" style="width:320px;">
<img src="./assets/not-dense.png" style="width:320px;">
</p>

> **Note:** This package is slightly inspired by, and based on [Slydst](https://github.com/glambrechts/slydst).


## temporary Installation

If you prefer not to install the package or need to use the template in the online Typst editor, simply [download](./amrita-ppt.typ) the single `amrita-ppt.typ` file from the repository and place it next to your main `.typ` file. Then import it directly using:

```typst
#import "amrita-ppt.typ": *
```


## Permenant Installation

To install this package locally, clone the repository into your local Typst package directory.

**Linux:**
```bash
git clone https://github.com/nithitsuki/amrita-ppt-template.git "${XDG_DATA_HOME:-$HOME/.local/share}/typst/packages/local/amrita-ppt/0.2.0"
```

**macOS:**
```bash
git clone https://github.com/nithitsuki/amrita-ppt-template.git  ~/Library/Application\ Support/typst/packages/local/amrita-ppt/0.2.0
```

**Windows (powershell):**
```powershell
git clone https://github.com/nithitsuki/amrita-ppt-template.git "$env:APPDATA/typst/packages/local/amrita-ppt/0.2.0"
```

and then you can start using it with: 

```bash
typst init "@local/amrita-ppt:0.2.0"
```

## Usage

Notes on common options

- `title-theme`: choose between `"default"` (large title with top/bottom bars) and `"minimal"` (compact title layout).
- `dense-mode`: when `true`, header and footer show tighter spacing and can display the page/event compactly.
- `authors`: accepts a single string, an array of strings, or an array of maps with keys like `name`, `email`, and `affiliation`. Examples:

```typst
// simple
authors: ("Ada Lovelace",)

// detailed
authors: ((name: "Ada Lovelace", email: "ada@example.com", affiliation: "Dept A"),
          (name: "Alan Turing", email: "alan@example.com", affiliation: "Dept B"),)
```

- `affiliations`: an array of affiliation strings. If authors include `affiliation` values, they are matched to these entries and rendered as superscripts.
- `team-logo` (optional): pass an image block or `image("path", width: ...)` to show a team/institution logo on title slides.

You can use framed environments for highlighted content:

```typst
#definition(title: "Term")[
  A short definition.
]

#theorem(title: "Important")[
  Statement of the theorem.
]
```
