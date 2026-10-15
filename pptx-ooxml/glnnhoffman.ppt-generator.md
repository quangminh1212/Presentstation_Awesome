# ppt-generator
Code used in a custom GPT to generate pptx files based on a template, with summarization  and execution by ChatGPT

# Using a Custom GPT to Generate PowerPoint Slides via Python

This guide helps you connect a custom GPT that summarizes content into slides **with a Python script that creates a PowerPoint presentation**.

---

## Goal

1. Paste article or source content into GPT, specifying the desired slide count and the target audience.
2. GPT summarizes it into structured JSON slide content.
3. GPT (or you) passes the JSON into a Python script to generate `output.pptx`.

---

## JSON Format Reminder

The GPT should output structured JSON like this:

```json
{
  "slides": [
    {
      "type": "title",
      "title": "Slide Title",
      "subtitle": "Slide Subtitle"
    },
    {
      "type": "content",
      "title": "Slide Title",
      "bullets": [
        "Bullet point 1",
        "Bullet point 2"
      ]
    }
  ]
}
```

---

## GPT Instructions (for GPTs with Code Execution)

The following instruction is then passed to the GPT:

After generating the JSON, save it to a file named `slides.json`, then run the `generator.py` script, available in your knowledge files, that reads this file and generates `output.pptx`.

Example Python snippet to execute:

```python
import json
from generator import build_presentation_from_json

with open("slides.json", "r", encoding="utf-8") as f:
    data = json.load(f)

build_presentation_from_json(data, "my_output_deck.pptx")
```

---

## If You’re Running It Locally

The GPT should:

1. Output the JSON and save it as `slides.json`
2. Run this:

```bash
python generator.py
```

Or include this runnable script:

```python
import json
from generator import build_presentation_from_json

with open("slides.json", "r") as f:
    slide_data = json.load(f)

build_presentation_from_json(slide_data)
```

---

## 🗂️ File Overview

| File | Purpose |
|------|---------|
| `generator.py` | Python script that generates the PowerPoint |
| `slides.json` | Slide content from GPT |
| `output.pptx` | Final PowerPoint presentation |

---

## 🔁 Optional Extensions

- Add `"notes"` field to slides for presenter notes.
- Add `"duration"` or `"layout"` for advanced control.
- Connect to a web form or automation tool.

---


