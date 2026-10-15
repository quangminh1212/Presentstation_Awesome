# HTML to PPTX Converter

This is a command-line tool to convert structured HTML slides into a PowerPoint (.pptx) presentation.

## Installation

It is recommended to use `uv` to install the dependencies.

```bash
uv pip install -r requirements.txt
```

## Usage

```bash
python html2ppt.py -i <input.html> -o <output.pptx>
```

### Example

```bash
python html2ppt.py -i example.html -o presentation.pptx
```

This will convert the `example.html` file into a `presentation.pptx` file.

## Supported HTML Structure

The tool expects a specific HTML structure to correctly identify slides and content. Each slide should be a `<section>` tag within a `div` with the class `slides`.

The following HTML tags are supported:

*   `<h1>`, `<h2>`, `<h3>`, `<h4>`: Slide titles
*   `<p>`: Paragraphs
*   `<ul>`, `<ol>`, `<li>`: Lists
*   `<img>`: Images (both local and remote)
*   `data-background-color`: Slide background color

For more details, please refer to the `example.html` file.
