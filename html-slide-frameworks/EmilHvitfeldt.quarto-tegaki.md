# quarto-tegaki

![](demo.gif)

A Quarto extension that renders animated handwriting using the [tegaki](https://github.com/KurtGokhan/tegaki) library (bundled version: 0.11.1). Works with both RevealJS presentations and plain HTML documents. All assets are bundled — no internet connection required.

## Installation

```bash
quarto add emilhvitfeldt/quarto-tegaki
```

## Usage

Add the filter to your document's front matter:

```yaml
filters:
  - tegaki
```

Then wrap any text with the `.tegaki` class:

```markdown
[Hello, World!]{.tegaki}
```

### RevealJS fragments

Add `.fragment` to trigger the animation on slide advance:

```markdown
[Hello, World!]{.tegaki .fragment}
```

### Options

All options are optional.

| Attribute  | Description                              | Default                        |
|------------|------------------------------------------|--------------------------------|
| `font`     | Font name (see built-in fonts below)     | Inherited CSS font, or Caveat  |
| `size`     | Font size in `em`                        | `5.15`                         |
| `duration` | Animation duration in seconds            | `0.75`                         |

```markdown
[Hello!]{.tegaki font="Parisienne" size="6" duration="2"}
```

## Built-in fonts

| Name         | Style       |
|--------------|-------------|
| `Caveat`     | Casual      |
| `Italianno`  | Formal      |
| `Tangerine`  | Elegant     |
| `Parisienne` | Decorative  |

### Inherited font

If `font` is not set, the extension checks the element's computed CSS `font-family` against the list of built-in fonts. This lets you set the font via a slide or section class:

```markdown
## My Slide {.parisienne}

[Hello!]{.tegaki .fragment}
```

```scss
// styles.scss
@import url('https://fonts.googleapis.com/css2?family=Parisienne&display=swap');

.parisienne {
  font-family: 'Parisienne', cursive;
}
```

## Adding custom fonts

The tegaki library supports custom fonts generated from TTF files using the interactive generator at [gkurt.com/tegaki](https://gkurt.com/tegaki). To add a custom font:

1. Go to the generator and upload your TTF file to download a zip file.
2. Place the zip file in your project directory.
3. List it in your document's front matter:

```yaml
filters:
  - tegaki
tegaki-fonts:
  - my-font.zip
```

Multiple fonts can be listed. The font name to use in `font=` comes from the zip's `bundle.ts` (e.g. `family: 'My Font'` → `font="My Font"`).

## Format support

- **RevealJS**: animations are triggered by fragments or on slide entry. The extension handles the RevealJS coordinate system so rendering is correct at any window size.
- **HTML**: animations trigger when the element scrolls into the viewport (using `IntersectionObserver` at 50% visibility threshold).
