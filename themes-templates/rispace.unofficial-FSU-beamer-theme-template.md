# FSU Beamerposter & Presentation Theme (Unofficial)

An unofficial custom **Beamerposter** and **presentation** theme designed for Florida State University (FSU) — ideal for math, science, and engineering departments. This theme follows the FSU Garnet & Gold color scheme and supports both **poster-style** layouts and standard **slides-style** presentations.  

**Disclaimer:** This is an adaptation of the `CambridgeUS` theme for Beamer posters and presentations.

---

## Features

### Poster Mode   

✅ Elegant header with logo support  
✅ Signature FSU Garnet & Gold color scheme  
✅ Clean serif font inspired by Times New Roman  
✅ Shadowed blocks with rounded corners  
✅ Numbered figures and tables  
✅ 3-column layout support for posters  
✅ Custom footer with optional contact/info bar  

**Preview**  
![Poster Preview](images/sample-poster-preview.png)  

### beamerposter Custom Size Configuration

This document uses the `beamerposter` package with a custom poster size.

**Current Physical Dimensions:**
- **Width**  = 91.44 cm (exactly 36 inches = 3 feet)
- **Height** = 60.94 cm (exactly 24 inches = 2 feet)
- Aspect Ratio ≈ 3:2 (portrait orientation)

This produces a standard **36" × 24"** poster, which is compact and suitable for many conferences.

---

### How to Change to a 4×3 Feet Poster (48" × 36")

To create a standard **4 feet × 3 feet** poster (the most popular academic size):

**Option 1: Landscape (Recommended - 48" wide × 36" high)**  

```latex
\usepackage[size=custom, width=121.92, height=91.44, scale=1.0]{beamerposter}
```  

**Option 2: Portrait (36" wide × 48" high)**   

```latex
\usepackage[size=custom, width=91.44, height=121.92, scale=1.0]{beamerposter}
```  

Note:
1 foot = 30.48 cm
4 ft = 121.92 cm
3 ft = 91.44 cm  

### How to Change the Scale  

If your poster appears too small or too large when printed, adjust the scale parameter:  

- Increase scale → make everything bigger (e.g., scale=1.1 or scale=1.2)
- Decrease scale → make everything smaller (e.g., scale=0.9)

**Example**  
```latex
\usepackage[size=custom, width=121.92, height=91.44, scale=1.1]{beamerposter}
```  

**Tip:** Only change the scale after finalizing your content. It affects font sizes, block widths, and spacing uniformly.  

| Size          | Width (cm) | Height (cm) | Orientation          |
|---------------|------------|-------------|----------------------|
| 36" × 24"     | 91.44      | 60.94       | Current (3:2)        |
| 48" × 36"     | 121.92     | 91.44       | Most Common (4:3)    |
| 60" × 36"     | 152.40     | 91.44       | Wide format          |
| 48" × 48"     | 121.92     | 121.92      | Square               |

### Here is my real poster:

![My Poster](images/gsrw_RafiqIslam.png) 

---

### Presentation Mode    

✅ Modern slide header with clickable dot navigation  
✅ Custom footline with author/title/date/page  
✅ Table of contents with automatic section listing  
✅ Font styling optimized for screen readability  
✅ Optional clickable bullets linked to slides  
✅ Math-ready with `amsmath`, `amssymb`, `newtxmath`  
✅ Easy toggle between poster and presentation styles

**Preview**  
![Presentation Sample](images/fsu_slides_grid_1.jpg)  
![Sample](images/fsu_slides_grid_2.jpg)  

The complete [PDF can be found here](images/presentation_sample.pdf) 

---

## How to Use on Overleaf  

### Option 1: Direct Copy  

1. [Overleaf project link](https://www.overleaf.com/read/ndyfpyvjkdzh#7472ae)

### Option 2: Clone from GitHub to Overleaf
1. Go to [Overleaf](https://overleaf.com)  
2. Click `New Project → Import from GitHub`  
3. Paste the repo URL:  
   ```
   https://github.com/rispace/unofficial-FSU-beamer-theme-template
   ```

## How to use Locally

###  Download ZIP
1. Click the green **Code** button → `Download ZIP`  
2. Upload files to Overleaf or use in local TeX setup  

---

## Files Included

- `beamerthemefsu.sty` – Theme structure and layout  
- `beamercolorthemefsucolor.sty` – FSU color definitions  
- `presentation.tex` – Working presentation example  
- `poster.tex` – Working poster example  
- `logo/` – Official FSU and Math department logos  
- `images/` – Additional graphics for slides/posters  
- `ref.bib` – Sample bibliography file
- `README.md` - Read me file

---

## Author

**Rafiq Islam**  
Ph.D. Candidate in Mathematics  
Florida State University  

Email: `rislam@fsu.edu`  
GitHub: [rispace](https://github.com/rispace)

