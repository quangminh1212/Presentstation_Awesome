# PowerPoint Inconsistency Analyzer

## Overview
This tool analyzes multi-slide PowerPoint presentations (PPTX) and associated slide images to automatically detect factual or logical inconsistencies across slides. It uses Google Gemini 2.5 Flash (via API) for advanced reasoning and natural language analysis.

## Features
- Extracts text from both PPTX files and slide images (JPEG/PNG).
- Uses OCR (Tesseract) for image text extraction.
- Detects:
  - Conflicting numerical data (e.g., mismatched revenue figures)
  - Contradictory textual claims (e.g., "highly competitive" vs "few competitors")
  - Timeline mismatches (e.g., inconsistent dates or forecasts)
- Outputs a clear, structured report referencing slide numbers and the nature of each issue.
- Generalized for any deck and scalable to large presentations.


## Requirements
- Python 3.8+
- Packages:
  - python-pptx
  - pytesseract
  - Pillow
  - requests
- Google Gemini API key (get a free key at https://aistudio.google.com/app/apikey)
- Tesseract OCR installed and in your PATH (https://github.com/tesseract-ocr/tesseract)

## API Key Security
**Do NOT share or commit your Gemini API key to GitHub or any public repository.**

This project loads the API key from an environment variable. Before running the code, set your API key in your environment:

On Windows (Command Prompt):
```
set GEMINI_API_KEY=your_actual_key_here
```
On Windows (PowerShell):
```
$env:GEMINI_API_KEY="your_actual_key_here"
```
On Linux/Mac:
```
export GEMINI_API_KEY=your_actual_key_here
```

The code will read the key using `os.getenv("GEMINI_API_KEY")`. If the key is not set, the script will raise an error.

## Usage
1. Place your PPTX file and a folder of slide images in the same directory. Example structure:

```
AssignmentFolder/
  NoogatAssignment.pptx
  NoogatAssignment/
    Slide1.jpeg
    Slide2.jpeg
    ...
```

2. In a Jupyter notebook, import the code and run:
```python
main(r"C:\path\to\AssignmentFolder")
```

3. The tool will print an inconsistency report to the output.


## Example Output
```
=== Inconsistency Report ===
Slide 2:
  (pptx) Revenue for 2024 is $1,000,000.
  (image) Revenue for 2024 is $1,200,000.
  Issue: Conflicting revenue figures between slide text and image.

Slide 3:
  (pptx) The market is highly competitive.
Slide 4:
  (pptx) There are only a few competitors in this space.
  Issue: Contradictory claims about market competition between slides 3 and 4.

Slide 5:
  (pptx) Forecast: Product launch in Q2 2025.
Slide 6:
  (pptx) Product launch scheduled for Q4 2025.
  Issue: Timeline mismatch for product launch between slides 5 and 6.
```

## Limitations
- OCR accuracy depends on image quality.
- Gemini API may have rate limits or require prompt tuning for best results.
- Only as accurate as the AI model and text extraction.

## Submission
- Include this README, your code, and a requirements.txt in your git repository.
- Document any changes or improvements you make.

## License
For educational use only.
