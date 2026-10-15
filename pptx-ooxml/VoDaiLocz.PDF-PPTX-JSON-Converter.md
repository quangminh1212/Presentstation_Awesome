# 🔄 PDF-to-JSON Converter

Một tool toàn diện để chuyển đổi file PDF thành format JSON có cấu trúc mà AI có thể hiểu được. Tool này trích xuất text, hình ảnh, tables và sử dụng AI vision để phân tích visual content.

## ✨ Tính năng chính

- **📝 Trích xuất text**: Lấy toàn bộ text từ PDF với thông tin vị trí, font và định dạng
- **🖼️ Trích xuất hình ảnh**: Lấy tất cả hình ảnh, sơ đồ, biểu đồ từ PDF với metadata chi tiết
- **🤖 AI Vision Analysis**: Sử dụng OpenAI GPT-4V để phân tích và mô tả visual content
- **📊 Table extraction**: Trích xuất và cấu trúc hóa tables từ PDF
- **🔗 Relationship analysis**: Phân tích mối quan hệ giữa các elements trong document
- **📋 JSON Output**: Tạo cấu trúc JSON toàn diện bảo toàn semantic meaning
- **✅ Validation**: Kiểm tra tính hợp lệ của JSON output
- **🧪 Comprehensive Testing**: 69 unit tests và integration tests

## 🚀 Quick Start

### Cài đặt

```bash
# Clone repository
git clone <repository-url>
cd pdf_converter

# Cài đặt dependencies
pip install -r requirements.txt

# Tạo test PDFs
python tests/create_test_pdf.py

# Chạy demo
python demo.py
```

### Sử dụng cơ bản

```bash
# Chuyển đổi PDF thành JSON (không AI analysis)
python -m src.cli.main input.pdf --output output.json --no-ai-analysis

# Chuyển đổi với AI analysis (cần OpenAI API key)
python -m src.cli.main input.pdf --openai-api-key YOUR_API_KEY

# Verbose mode để xem chi tiết
python -m src.cli.main input.pdf --verbose

# Validate PDF trước khi convert
python -m src.cli.main input.pdf --validate-only
```

## 📁 Cấu trúc JSON Output

Tool tạo ra JSON với cấu trúc như sau:

```json
{
  "document_metadata": {
    "title": "Document title",
    "author": "Author name",
    "total_pages": 5,
    "creation_date": "...",
    "pdf_version": "1.4"
  },
  "pages": [
    {
      "page_number": 0,
      "dimensions": {"width": 595, "height": 842},
      "element_counts": {
        "text_blocks": 10,
        "images": 2,
        "tables": 1
      }
    }
  ],
  "elements": [
    {
      "element_id": "text_p0_0001",
      "element_type": "paragraph",
      "page_number": 0,
      "bbox": [100, 100, 200, 120],
      "content": {
        "text": "Sample text content",
        "font_name": "Arial",
        "font_size": 12
      },
      "metadata": {
        "word_count": 3,
        "is_heading": false
      }
    },
    {
      "element_id": "image_p0_0002",
      "element_type": "image",
      "page_number": 0,
      "bbox": [200, 200, 300, 300],
      "content": {
        "image_id": "img_p0_1_abc123",
        "width": 100,
        "height": 100,
        "ai_description": "A flowchart showing process steps",
        "ai_image_type": "diagram",
        "ai_text_content": "Start -> Process -> End",
        "base64_data": "iVBORw0KGgoAAAANSUhEUgAA..."
      },
      "metadata": {
        "ai_confidence": 0.95,
        "ai_model": "gpt-4-vision-preview"
      }
    }
  ],
  "relationships": [
    {
      "relationship_type": "heading_to_content",
      "from_element": "text_p0_0001",
      "to_element": "text_p0_0002",
      "description": "heading1 introduces content"
    }
  ],
  "ai_analysis_summary": {
    "total_analyses": 5,
    "average_confidence": 0.87,
    "image_types_distribution": {
      "diagram": 3,
      "chart": 2
    }
  },
  "extraction_metadata": {
    "extraction_timestamp": "2024-01-01T12:00:00",
    "total_elements": 25,
    "total_pages": 5,
    "total_images": 5
  }
}
```

## 🛠️ Cấu trúc dự án

```
pdf_converter/
├── src/
│   ├── pdf_extractor/          # Text và image extraction
│   ├── ai_vision/              # AI vision analysis
│   ├── json_builder/           # JSON structure building
│   └── cli/                    # Command line interface
├── tests/
│   ├── test_pdf_extractor/     # Unit tests cho PDF extraction
│   ├── test_ai_vision/         # Unit tests cho AI vision
│   ├── test_json_builder/      # Unit tests cho JSON builder
│   └── test_integration/       # End-to-end integration tests
├── output/                     # Generated JSON files
├── demo.py                     # Demo script
├── requirements.txt            # Dependencies
└── README.md                   # Documentation
```

## 🧪 Testing

Tool có 69 comprehensive tests:

```bash
# Chạy tất cả tests
python -m pytest tests/ -v

# Chạy với coverage
python -m pytest tests/ -v --cov=src

# Chạy integration tests
python -m pytest tests/test_integration/ -v

# Chạy specific test module
python -m pytest tests/test_pdf_extractor/ -v
```

## 🔧 Configuration

### Environment Variables

- `OPENAI_API_KEY`: OpenAI API key cho AI vision analysis

### Command Line Options

```bash
python -m src.cli.main --help
```

Options:
- `--output, -o`: Output JSON file path
- `--openai-api-key`: OpenAI API key
- `--no-ai-analysis`: Skip AI image analysis
- `--verbose, -v`: Enable verbose logging
- `--validate-only`: Only validate PDF without conversion

## 🚀 Advanced Usage

### Programmatic Usage

```python
from src.cli.main import PDFConverter

# Initialize converter
converter = PDFConverter(openai_api_key="your-key")

# Convert PDF
success = converter.convert_pdf_to_json(
    pdf_path="input.pdf",
    output_path="output.json",
    analyze_images=True
)

if success:
    print("Conversion successful!")
```

### Custom AI Analysis

```python
from src.ai_vision.vision_analyzer import VisionAnalyzer

analyzer = VisionAnalyzer(api_key="your-key")
result = analyzer.analyze_image(image_data, image_id)
print(result.description)
```

## 📊 Performance

- **Text extraction**: ~1-2 seconds per page
- **Image extraction**: ~0.5 seconds per image
- **AI analysis**: ~2-5 seconds per image (depends on API)
- **JSON building**: ~0.1 seconds per document

## 🤝 Contributing

1. Fork the repository
2. Create feature branch: `git checkout -b feature-name`
3. Make changes and add tests
4. Run tests: `python -m pytest tests/`
5. Submit pull request

## 📝 License

MIT License - see LICENSE file for details.

## 🆘 Troubleshooting

### Common Issues

1. **"Failed to open PDF"**: Ensure PDF file is not corrupted and not password-protected
2. **"No AI client available"**: Set OPENAI_API_KEY environment variable
3. **"Import errors"**: Install all dependencies with `pip install -r requirements.txt`

### Debug Mode

```bash
python -m src.cli.main input.pdf --verbose
```

## 📞 Support

- Create an issue on GitHub
- Check existing issues for solutions
- Run demo script: `python demo.py`
