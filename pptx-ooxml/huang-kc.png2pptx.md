# png2pptx

You have a slide **image** an AI generated for you. You want the actual
PowerPoint file — the one where you can fix a typo.

png2pptx reconstructs it **1:1**: every line of text becomes a real text box,
every card and divider a real shape, laid out at the coordinates measured from
your image. Only genuine artwork — 3D renders, curved arrows, photos — stays a
bitmap, because that is what it is.

[中文说明见下](#中文)

---

## The problem

Image models (ChatGPT / gpt-image-1, Gemini, …) will happily generate a
beautiful, complete slide. What they hand back is a bitmap. Drop it into
PowerPoint and you get:

- blur the moment you project it or print it,
- no way to fix a typo,
- the wrong aspect ratio — `gpt-image-1` maxes out at 3:2 (`1536×1024`); the
  PowerPoint standard is 16:9.

Commercial converters exist. Their own docs say complex flowcharts and posters
are handled *best-effort* and "may remain as image elements" — which is the
part you actually wanted converted.

## How it works

```
image ──▶ reflow (3:2→16:9) ──▶ upscale ──▶ crop assets ──▶ build .pptx
                                                                 │
                                    pixel-diff report ◀── render ┘
```

Measured against the source image, reconstructed slides land at **12.9–16.2
mean pixel difference** (0–255 scale). Most of the remainder is the typeface
itself differing from whatever the image model drew with.

## Install

```bash
pip install python-pptx pillow numpy
brew install --cask upscayl        # optional, for the upscale step
```

macOS only for the preview/render step — it drives PowerPoint through
AppleScript. Everything else is portable.

```bash
export SLIDE2PPT_UPSCAYL="/Applications/Upscayl.app/Contents/Resources"
export SLIDE2PPT_FONT="/path/to/your.ttc"   # used to measure text width
```

## Use

```bash
python cli.py new  slide.png  mypage    # scaffold a spec + upscale
# …fill in the text you can read in the image…
python cli.py build mypage              # crop → build → render → diff
python diffviz.py slide.png out/mypage.preview.png   # what's still off
```

A *spec* is a small Python module describing one slide: which regions are
artwork, and where each line of text sits. Coordinates and font sizes are
**measured from the image**, not guessed — see below.

Python rather than YAML on purpose: real layouts are full of "six evenly spaced
columns", "divider at the midpoint of two anchors". Config formats end up
growing expressions anyway.

## Three rules that make or break it

**1. Derive font size from measured *width*, never from block height.**

CJK glyphs fill the em box, so block height looks like a safe proxy for font
size. It isn't. Microsoft YaHei runs 8–10% wider than the geometric sans these
image models tend to draw with; get the height right and the width still
overflows. In a 180px-wide card a line needing 195px wraps, and no amount of
size tweaking fixes it — the size was never wrong, the *dimension* was.

```python
unit = ImageFont.truetype(font, 100).getlength(text) / 100.0
size = measured_width_px / unit          # font metrics are linear
```

One page went from *every line in five cards wrapping* to **79 text runs, zero
manual sizes, zero wraps**.

**2. A measurement window must contain only its target.**

Four ways to get this wrong, all of which produce plausible-looking numbers:

| mistake | symptom |
|---|---|
| overlaps a neighbour | measures the adjacent element, sizes come out large |
| touches the container border | inside a white box, the border counts as ink |
| much wider than the text | you measure the window, not the content |
| clips the target | a CJK glyph "40 wide × 24 tall" — it got cut |

Derive window edges from the **midpoint between adjacent anchors**. For short
strings, measure once and hard-code the ink extent. Prefer text as an anchor
over graphics — a coloured circle's detection flickers with tolerance.

**3. Address GUI documents by name.**

The renderer drives PowerPoint. `save active presentation` saves *whatever the
user has in front*, silently and without error. `repeat while (count
presentations) > 0 … close saving no` will close their unsaved work.

Of four ways to reference a presentation, exactly one works:

| AppleScript | result |
|---|---|
| `active presentation` | saves the user's document |
| `first presentation whose name is …` | error −1750 |
| `set t to open POSIX file …` | `open` returns nothing, −2753 |
| `presentation "x.pptx"` | ✅ |

Parallel builds must serialise the render stage — the app is a single instance
and two drivers will fight over focus.

## Modules

| file | role |
|---|---|
| `core.py` | `Deck` builder, `size_for()`, asset cropping, render, side-by-side |
| `genlib.py` | measurement helpers for writing generators: `ink` `rows` `fills` `bounds` |
| `extract.py` | auto-segment a slide into blocks; recurses into filled cards |
| `diffviz.py` | per-pixel diff, regions ranked by total difference |
| `reflow.py` | 3:2 → 16:9 by compressing whitespace bands, not by scaling |
| `cli.py` / `buildall.py` | single page / many pages (build parallel, render serial) |

### On `reflow.py`

To go from `1536×1024` to `1536×864` you must lose 160px. Scaling leaves ~17%
side margins; stretching turns circular icons into ellipses. Instead it finds
rows that are entirely background and squeezes *those*, leaving content pixels
untouched. If a page is too dense to yield enough whitespace it **refuses**
rather than quietly distorting — you get told to re-generate or accept margins.

## Asset modes

- `key` — flat artwork on a near-solid background → alpha-key the background
- `circle` — photographs → circular mask (keying eats faces and pale clothing)
- `raw` — crop with the background → the slide background must match exactly,
  or you get a visible rectangle

## Gotchas worth knowing before you start

- **PowerPoint recompresses images to 220 ppi on save.** Settings → Image Size
  and Quality → *Do not compress images in file*. Otherwise everything above is
  wasted.
- **ChatGPT cannot output 16:9.** Sizes are `1024²`, `1536×1024`, `1024×1536`.
- **Upscaling is not required for keying** — it only affects sharpness when the
  slide is enlarged. 2× is plenty (~230 ppi); 4× costs minutes for no visible
  gain.
- Budget **40–60 minutes per dense page**. Regular grids go fast. The time goes
  into layouts that *look* aligned and aren't — one page had step icons and a
  timeline on two different column systems.

## License

MIT

---

<a name="中文"></a>

# 中文说明

你手上是 AI 给你生成的一张**幻灯片图片**，你想要的是那份真正的 PPT ——
能改错字的那份。

png2pptx 把它**一比一复刻**出来：每一行文字都是真的文本框、每张卡片和分隔线
都是真的形状，位置按你那张图量出来排。只有真正的插画（3D 渲染、曲线箭头、
照片）才留作位图，因为它本来就是。

## 为什么要做

图像模型能生成很漂亮的整页幻灯片，但交付的是位图：投影就糊、错字改不了、
比例还不对（`gpt-image-1` 最宽只有 3:2 的 `1536×1024`，而 PPT 标准是 16:9）。

市面上有转换服务，但它们自己的文档写着复杂流程图和海报只做 best-effort、
"may remain as image elements" —— 而那恰恰是你想转换的部分。

## 三条硬纪律

**一、字号从实测宽度反算，不按块高估。** 中日韩字形占满 em，块高看着像个安全的
代理量，其实不是：微软雅黑比这类模型常画的几何无衬线宽 8–10%，高度对上了宽度
仍然溢出。卡片可用 180px 而需要 195px，怎么调字号都没用 —— **字号没估错，
估错的是维度**。改成宽度反算后，同一页 79 处文字全自动定号、零折行。

**二、量测窗口只许框住目标本身。** 四种越界（重叠邻居 / 撞到框线 / 比文字宽太多 /
把目标切掉）都会给出看起来合理的数字。窗口边界要由**相邻锚点的中点**算出；
短文本先量一次拿到墨迹范围再写死；锚点优先用文字不用图形。

**三、GUI 文档一律按名字引用。** `save active presentation` 存的是用户当前打开的
那份，不报错；`count > 0` 全量关闭会关掉别人未保存的工作。PowerPoint 的四种写法
里只有 `presentation "x.pptx"` 可用。并行构建时渲染必须串行。

## 开始之前值得知道的

- **PowerPoint 保存时默认把图片压回 220ppi** —— 设置 → 图像大小和质量 →
  勾「不压缩文件中的图像」，否则前面全白做
- **超分不是抠图的前置条件**，只影响放大后糊不糊；2 倍够用，4 倍是浪费
- 密集页预算 **40–60 分钟**，时间花在「看起来对齐其实没对齐」的地方
