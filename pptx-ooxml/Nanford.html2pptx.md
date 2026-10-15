# HTML to PowerPoint Converter

## Project Overview

This Python script converts HTML files into PowerPoint presentations (.pptx).
It aims to render the visual design of specified HTML content areas as slide backgrounds and extract text content, preserving basic styles and layout within editable text boxes in the PowerPoint presentation.

The core functionalities include:
- Generating a background image from a specified HTML element or the entire viewport using Playwright.
- Hiding text elements during background image generation to create a clean visual backdrop.
- Parsing text content and its styling (font, size, color, weight, alignment) from the HTML using BeautifulSoup.
- Calculating the position and dimensions of text elements.
- Assembling a PowerPoint presentation with the generated background image and overlaying extracted text in editable text boxes.

## Features

- Converts local HTML files to PPTX slides.
- Allows specifying a CSS selector to define the main content area for conversion.
- Extracts text content, basic styling (font family, size, color, weight, style, text alignment, line height), and positioning.
- Sets slide dimensions to a 16:9 aspect ratio (1920x1080 pixels equivalent).

## Prerequisites

- Python 3.8 or higher.
- `pip` (Python package installer).
- A modern web browser compatible with Playwright (Chromium is used by default and will be downloaded by Playwright if not found).

## Setup Instructions

1.  **Clone the repository or download the project files.**

2.  **Navigate to the project directory:**
    ```bash
    cd path/to/html2pptx
    ```

3.  **Create a Python virtual environment (recommended):**
    ```bash
    python -m venv .venv
    ```

4.  **Activate the virtual environment:**
    *   On Windows (PowerShell):
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```
    *   On macOS/Linux:
        ```bash
        source .venv/bin/activate
        ```

5.  **Install the required Python libraries:**
    Make sure you have a `requirements.txt` file in the project root. If not, create one with the following content:
    ```plaintext
    playwright
    python-pptx
    beautifulsoup4
    ```
    Then run:
    ```bash
    pip install -r requirements.txt
    ```
    Playwright will download the necessary browser binaries during its first run if they are not already present.

## Usage

The main script for conversion is `src/main.py`.

**Command-Line Arguments:**

*   `html_file_path`: (Required) Path to the input HTML file.
*   `-o`, `--output`: (Optional) Path for the output PPTX file. Defaults to `<input_file_name>.pptx` in the `output_pptx` directory relative to the project root.
*   `-s`, `--selector`: (Optional) CSS selector for the main HTML element to be converted. If not provided, the entire visible viewport (1920x1080) of the HTML page will be captured as the background, and text will be extracted from the entire document.

**Running the script:**

Ensure your virtual environment is activated.

**Examples:**

1.  **Convert an HTML file using the entire viewport and default output path:**
    ```bash
    python src/main.py "path/to/your/input.html"
    ```
    *(Output will be `output_pptx/input.pptx`)*

2.  **Convert an HTML file, specifying a CSS selector for the main content and a custom output path:**
    ```bash
    python src/main.py "path/to/your/input.html" -s ".main-content-area" -o "my_presentation.pptx"
    ```

3.  **Convert an HTML file using a specific content area (e.g., `.aspect-ratio-box` which often contains the slide-like content) and output to a specific folder:**
    ```bash
    python src/main.py "input_html/1.html" -s ".aspect-ratio-box" -o "output_pptx/1_converted.pptx"
    ```

**Important Notes:**

*   **CSS Selector:** Using an accurate CSS selector (`-s` option) is crucial for complex HTML pages to isolate the desired content area for conversion. This helps in generating a clean background image and relevant text extraction.
*   **File Paths:** It's generally recommended to use absolute paths for input and output files, or ensure relative paths are correctly structured based on your current working directory when running the script.
*   **HTML Structure:** The quality of the conversion heavily depends on the structure and styling of the input HTML. Well-structured HTML with clear text elements and CSS will yield better results.
*   **Font Availability:** For accurate text styling in the PPTX, ensure that the fonts used in the HTML are also available on the system where the PowerPoint presentation is being viewed.

## Project Structure (Simplified)

```
html2pptx/
├── .venv/                     # Python virtual environment
├── input_html/                # Example input HTML files
│   └── 1.html
├── output_pptx/               # Default output directory for PPTX and generated images
├── src/
│   ├── __init__.py
│   ├── main.py                # Main control script
│   ├── image_generator.py     # Module for background image generation
│   ├── html_parser.py         # Module for HTML parsing and text extraction
│   ├── pptx_builder.py        # Module for building the PPTX presentation
│   └── constants.py           # (If you have one for shared constants)
├── README.md                  # This file
└── requirements.txt           # Python dependencies
```

## Troubleshooting

*   **`ImportError` or `ModuleNotFoundError`**: Ensure your virtual environment is activated and all dependencies from `requirements.txt` are installed.
*   **Playwright browser download issues**: If Playwright fails to download browser binaries, you might be behind a proxy or have network restrictions. Try running `playwright install` manually in the activated virtual environment.
*   **Incorrect background image/text extraction**: 
    *   Verify your CSS selector (`-s` argument) is correct and accurately points to the desired content block in the HTML.
    *   Check the `text_elements_selectors` list in `src/image_generator.py` and `TARGET_TEXT_SELECTORS` in `src/html_parser.py` to ensure they cover the types of text elements you want to process.
*   **PowerShell Execution Policy (Windows)**: If you cannot activate the virtual environment with `.\.venv\Scripts\Activate.ps1` due to an execution policy error, you might need to temporarily change the policy. Run PowerShell as Administrator and execute:
    ```powershell
    Set-ExecutionPolicy RemoteSigned -Scope Process
    ```
    Then try activating again. Remember to set it back to a more restrictive policy if needed.

## Future Enhancements (Ideas)

- Support for SVG elements.
- More advanced style preservation (e.g., complex text formatting, list styles).
- Handling of more HTML element types (e.g., tables, images within content).
- Option for multi-page HTML to multi-slide PPTX conversion.
- GUI interface. 