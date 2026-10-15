# gl-transitions

A Quarto RevealJS extension that adds GPU-accelerated slide transitions using [GL Transitions](https://gl-transitions.com/) — a library of 100+ GLSL fragment shader transitions.

![](transitions.webp)

## Installation

```bash
quarto add emilhvitfeldt/quarto-revealjs-transitions
```

## Usage

Add the extension to your document's YAML front matter and set `transition: none` to disable RevealJS's built-in transitions:

```yaml
---
format:
  revealjs:
    transition: none
revealjs-plugins:
  - gl-transitions
---
```

Then add a `gl-transition` attribute to any slide you want to animate **into**:

```markdown
## My slide {gl-transition="crosswarp"}

Slide content here.
```

The transition plays when navigating **to** that slide. Slides without a `gl-transition` attribute cut instantly.

## Available transitions

You can preview all transitions at [gl-transitions.com/gallery](https://gl-transitions.com/gallery).

| Name | Name | Name | Name |
|------|------|------|------|
| AdvancedMosaic | angular | BlockDissolve | BookFlip |
| Bounce | BowTieHorizontal | BowTieVertical | BowTieWithParameter |
| Box | burn | ButterflyWaveScrawler | cannabisleaf |
| chessboard | circle | CircleCrop | circleopen |
| colorphase | ColourDistance | CrazyParametricFun | crosshatch |
| crosswarp | CrossZoom | cube | DefocusBlur |
| Directional | DirectionalScaled | directionalwarp | directionalwipe |
| displacement | dissolve | DoomScreenTransition | doorway |
| Dreamy | DreamyZoom | EdgeTransition | fade |
| fadecolor | fadegrayscale | FilmBurn | flyeye |
| Fold | fragment | GlitchDisplace | GlitchMemories |
| GridFlip | heart | hexagonalize | HorizontalClose |
| HorizontalOpen | HSVfade | InvertedPageCurl | kaleidoscope |
| LeftRight | LinearBlur | luma | morph |
| Mosaic | Overexposure | perlin | pinwheel |
| pixelize | PolkaDotsCurtain | powerKaleido | PuzzleRight |
| Radial | randomNoisex | randomsquares | Rectangle |
| RectangleCrop | ripple | Rolls | RotateScaleVanish |
| rotateTransition | SimpleFlip | SimpleZoom | SimpleZoomOut |
| Slides | splitSlideInHorizontal | splitSlideInOutHorizontal | splitSlideInOutVertical |
| splitSlideInVertical | splitSlideOutHorizontal | splitSlideOutVertical | squareswire |
| squeeze | StarWipe | StaticFade | StereoViewer |
| swap | Swirl | tangentMotionBlur | TilesWave |
| TopBottom | TVStatic | undulatingBurnOut | VerticalClose |
| VerticalOpen | WaterDrop | wind | windowblinds |
| windowslice | wipeDown | wipeLeft | wipeRight |
| wipeUp | ZoomInCircles | zoomInOut | ZoomLeftWipe |
| ZoomRigthWipe | | | |

Transition names are **case-sensitive**.

## Slide backgrounds

GL Transitions works with all RevealJS background types. Use the standard Quarto background attributes alongside `gl-transition`:

```markdown
## Color background {gl-transition="burn" background-color="#4a90d9"}

## Image background {gl-transition="crosswarp" background-image="photo.jpg"}

## Dark slide {gl-transition="windowslice" background-color="#1a1a2e"}
```

## How it works

When a slide change occurs, the extension:

1. Captures the current slide as a WebGL texture using [html2canvas](https://html2canvas.hertzen.com/)
2. Captures the incoming slide as a second texture
3. Runs the GLSL fragment shader over both textures for 1 second, blending from one to the other
4. Hides the overlay canvas once the animation completes

The WebGL canvas is overlaid on top of the presentation at full opacity during the transition, then hidden, so RevealJS's own slide management is unaffected.
