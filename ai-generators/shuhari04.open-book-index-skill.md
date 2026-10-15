# 开卷索引 Skill

`open-book-index` is a Codex skill for turning course materials into an open-book exam index.

It accepts course folders, PowerPoint files, PDFs, Word documents, and supported archives, then helps produce:

- a `.docx` open-book index
- a matching `.pdf`
- a dictionary-style concept index sorted by mixed Chinese/English order
- a chapter/section knowledge-point index
- file-first source references such as `lecture.pptx: slide 12` or `chapter.pdf: PDF第8页`

## Contents

- `open-book-index/` - skill source directory
- `dist/open-book-index.skill` - packaged installable skill

## Install

Copy or install `dist/open-book-index.skill` into your Codex skills setup, or use the source folder directly:

```bash
cp -R open-book-index ~/.codex/skills/
```

## Main Workflow

The skill includes helper scripts for deterministic preprocessing and document generation:

```bash
python3 open-book-index/scripts/extract_materials.py \
  --input "/path/to/course-materials" \
  --output-workdir "/path/to/workdir"
```

After reviewing and shaping the extracted knowledge into `concepts.json`:

```bash
python3 open-book-index/scripts/build_index_docx.py \
  --concepts "/path/to/concepts.json" \
  --summary "/path/to/workdir/summary.json" \
  --output-dir "/path/to/output" \
  --basename "open_book_index"
```

## Notes

- LibreOffice/`soffice` is recommended for PPT/PPTX/DOCX conversion and PDF export.
- `pdftotext` is recommended for PDF text extraction with page boundaries.
- OCR requires an OCR tool such as `tesseract`; missing OCR dependencies are reported in `summary.json`.
