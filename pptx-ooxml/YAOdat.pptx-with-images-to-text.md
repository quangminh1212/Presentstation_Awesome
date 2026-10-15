# Document Text Extractor

Extract text from PowerPoint (PPTX) and PDF files including OCR for images. Supports multiple file uploads with combined output.

## Install

```bash
pip install -r requirements.txt
```

**Note:** For OCR functionality, you'll also need to install Tesseract:
- Ubuntu/Debian: `sudo apt-get install tesseract-ocr tesseract-ocr-ara`
- macOS: `brew install tesseract`
- Windows: Download from [GitHub](https://github.com/UB-Mannheim/tesseract/wiki)

## Web Service (Recommended)

Run the Flask web service for easy file upload and download:

```bash
python3 app.py
```

Then open your browser to `http://localhost:5000` or `http://0.0.0.0:5000`

The web interface allows you to:
- Upload multiple PPTX and/or PDF files at once
- Drag-and-drop or use file picker
- Configure OCR languages
- Download combined text file automatically (all files in one output)

To host on the internet, you can deploy to:
- Heroku
- AWS Elastic Beanstalk
- Google Cloud Run
- Digital Ocean App Platform
- Railway
- Fly.io

## Command Line Usage

For command-line use:

**PPTX files:**
```bash
python3 extract_pptx_ocr.py presentation.pptx
python3 extract_pptx_ocr.py presentation.pptx output.txt
python3 extract_pptx_ocr.py presentation.pptx output.txt eng+ara
```

**PDF files:**
```bash
python3 extract_pdf.py document.pdf
python3 extract_pdf.py document.pdf output.txt
```

## Output

Text extracted to output file with:
- **PPTX**: Text boxes, tables, OCR from images, speaker notes
- **PDF**: All text from all pages
- **Multiple files**: Combined output with clear file separators

## Features

- ✅ Support for PPTX and PDF files
- ✅ Upload multiple files at once
- ✅ Combined output for multiple files
- ✅ Extract text from text boxes and tables
- ✅ OCR text from images (PPTX only)
- ✅ Extract speaker notes (PPTX only)
- ✅ Multi-language OCR support
- ✅ Web interface for easy upload/download
- ✅ Stateless operation (no database required)
