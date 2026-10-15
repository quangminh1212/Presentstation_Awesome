# 📊 PowerPoint-PPTX-Generator

A powerful Python-based tool for programmatically generating professional PowerPoint presentations. This project leverages the `python-pptx` library to create structured, styled, and data-rich slides with ease.

## 🚀 Features

- **Automated Slide Creation**: Generate multi-slide presentations in seconds.
- **Custom Layouts**: Support for title slides, content slides, and blank layouts with custom positioning.
- **Rich Text Formatting**: Control font sizes, colors, bolding, and alignment programmatically.
- **Table Support**: Create and format complex data tables with alternate row styling and custom headers.
- **Dynamic Content**: Automatically include timestamps and dynamic data in your slides.
- **No MS Office Required**: Generates `.pptx` files completely independent of Microsoft PowerPoint.

## 🛠️ Technologies Used

- **Python 3.x**
- **[python-pptx](https://python-pptx.readthedocs.io/)**: The core engine for PPTX manipulation.
- **Pillow**: For image processing and handling within slides.
- **xlsxwriter**: For advanced data handling (if integrated with Excel).

## 🏁 Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your system.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/sameer9860/PowerPoint-PPTX--Generator.git
   cd PowerPoint-PPTX--Generator
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

Run the main script to generate a demo presentation:

```bash
python preentation1.py
```

This will create a file named `demo_presentation_[TIMESTAMP].pptx` in the project directory, containing 6 feature-rich slides.

## 📁 Project Structure

- `preentation1.py`: The main script containing the logic for PPTX generation.
- `requirements.txt`: List of Python dependencies.
- `demo_presentation_*.pptx`: Generated output files (example included).

## 👤 Author

**Sameer**

- GitHub: [@sameer9860](https://github.com/sameer9860)

---

_Created for automated storytelling and data reporting._
