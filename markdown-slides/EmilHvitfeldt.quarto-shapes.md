# quarto-shapes

CSS shape classes for Quarto — style divs as shapes (circles, hexagons, stars, etc.) that can contain text and other elements. Supports fill, stroke, rotation, and sizing modifier classes. Works across **HTML**, **RevealJS**, and **Typst** (PDF) output.

📖 **[Documentation site](https://emilhvitfeldt.github.io/quarto-shapes/)**

![A grid of shapes: circle, star, hexagon, heart, triangle, diamond, cloud, arrow, pentagon, moon, lightning bolt, and octagon.](examples/grid-shot.png)

## Installation

```bash
quarto add emilhvitfeldt/quarto-shapes
```

## Usage

Add the filter to your document:

```yaml
---
title: My Document
format: html
filters:
  - shapes
---
```

Then use shape classes on divs:

```markdown
::: {.shape-circle fill="blue"}
Hello
:::

::: {.shape-hexagon fill="none" stroke="red" .shape-stroke-lg .shape-lg}
:::
```

## Features

- **Shape classes**: circle, square, triangle, hexagon, and more
- **Fill color**: `fill="<any CSS color>"` for the interior
- **Stroke**: `stroke="<any CSS color>"` for outline color and `.shape-stroke-{sm,md,lg,xl}` for width
- **Rotation classes**: `.shape-rotate-45` through `.shape-rotate-315`
- **Sizing**: `.shape-sm`, `.shape-md`, `.shape-lg`, `.shape-full`, or `size="<any length>"` for a custom size
- **Composable**: mix any combination of modifiers

## Format support

| Format   | Notes |
|----------|-------|
| HTML     | ✅    |
| RevealJS | ✅    |
| Typst    | ✅ SVG embedded as image; size classes map to print lengths (sm 3cm / md 5cm / lg 8cm). |

## License

MIT
