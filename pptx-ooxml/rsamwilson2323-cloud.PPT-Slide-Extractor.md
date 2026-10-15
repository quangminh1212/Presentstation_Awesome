# 📊 PPT Slide Extractor

<p align="center">
  <strong>🚀 Convert PowerPoint slides into high-quality PNG images automatically.</strong>
</p>

<p align="center">
  Upload a <code>.ppt</code> or <code>.pptx</code> file and extract every slide as an image with just a few clicks.
</p>

---

## 🌟 About

**PPT Slide Extractor** is a Python-based desktop utility that converts PowerPoint presentations into high-quality PNG images.

Simply upload a PowerPoint presentation through the web interface, and the application automatically:

* 📤 Accepts PPT/PPTX files
* 🔄 Converts presentations into individual slides
* 🖼️ Exports each slide as a high-quality PNG image
* 📁 Creates a separate folder for every presentation
* 💾 Stores extracted slides inside the `data/` directory
* 🔁 Keeps previously extracted presentations
* 🌐 Provides a simple browser-based interface using Streamlit
* 🖥️ Can be launched by double-clicking `run.bat`

---

## ✨ Features

### 📤 Easy PowerPoint Upload

Upload your presentation directly through the Streamlit interface.

Supported formats:

```text
.ppt
.pptx
```

---

### 🖼️ High-Quality Slide Extraction

Each PowerPoint slide is exported as an individual PNG image.

Example:

```text
slide_01.png
slide_02.png
slide_03.png
slide_04.png
```

---

### 📂 Automatic Folder Organization

The application automatically creates a folder using the PowerPoint filename.

For example:

```text
My-Presentation.pptx
```

will create:

```text
data/
└── My-Presentation/
    ├── slide_01.png
    ├── slide_02.png
    ├── slide_03.png
    └── slide_04.png
```

---

### 🔄 Multiple Presentations

You can process multiple PowerPoint files.

Each presentation gets its own folder:

```text
data/
├── AI-Project/
│   ├── slide_01.png
│   ├── slide_02.png
│   └── slide_03.png
│
├── Python-Project/
│   ├── slide_01.png
│   ├── slide_02.png
│   └── slide_03.png
│
└── Smart-Campus/
    ├── slide_01.png
    ├── slide_02.png
    └── slide_03.png
```

Previously extracted presentations are not removed when a new presentation is uploaded.

---

## 🖥️ User Interface

The application provides a simple Streamlit interface:

```text
📊 PPT Slide Extractor

Convert PowerPoint slides into high-quality images automatically

📁 Upload your PowerPoint

        [ Browse files ]

        🚀 Extract All Slides

📂 Previously Extracted PPTs
```

After extraction, the generated slides are also displayed inside the application.

---

## ⚙️ How It Works

The extraction process follows this workflow:

```text
        📤 Upload PPT/PPTX
                │
                ▼
       📄 Read Presentation
                │
                ▼
      🟦 Microsoft PowerPoint
          or LibreOffice
                │
                ▼
       🔄 Convert / Export
                │
                ▼
          🖼️ PNG Slides
                │
                ▼
       📁 Create PPT Folder
                │
                ▼
          💾 Save to data/
```

### Conversion Priority

The application first attempts to use **Microsoft PowerPoint** for direct slide rendering.

If PowerPoint is unavailable or the export fails, it can fall back to **LibreOffice** for PPT/PPTX → PDF conversion, followed by PDF → PNG extraction.

---

## 🛠️ Technology Stack

| Technology              | Purpose                            |
| ----------------------- | ---------------------------------- |
| 🐍 Python 3.9           | Application programming            |
| 🌐 Streamlit            | Web-based user interface           |
| 🖼️ PyMuPDF             | PDF rendering and image extraction |
| 🪟 PyWin32              | Microsoft PowerPoint automation    |
| 📊 Microsoft PowerPoint | Direct slide rendering             |
| 🟠 LibreOffice          | Backup PPT/PPTX conversion         |
| 🖼️ PNG                 | Extracted slide format             |
| 💻 Windows Batch        | One-click application launcher     |

---

## 📋 Requirements

Before running the project, install:

### Python

Recommended:

```text
Python 3.9.x
```

Check your Python version:

```bash
py -3.9 --version
```

---

### Python Packages

Install the required packages:

```bash
py -3.9 -m pip install streamlit PyMuPDF pywin32
```

Or install everything from the project's requirements file:

```bash
py -3.9 -m pip install -r requirements.txt
```

---

## 📊 Microsoft PowerPoint

For the best slide rendering, Microsoft PowerPoint is recommended.

The application can use PowerPoint itself to export slides as PNG images.

This helps preserve:

* Fonts
* Images
* Shapes
* Backgrounds
* Layouts
* Slide dimensions
* Visual formatting

---

## 🟠 LibreOffice

LibreOffice can be used as a fallback conversion method when Microsoft PowerPoint is unavailable.

Install LibreOffice and make sure it is available in one of the standard Windows installation locations.

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/rsamwilson2323-cloud/PPT-Slide-Extractor.git
```

### 2. Open the project folder

```bash
cd PPT-Slide-Extractor
```

### 3. Install dependencies

```bash
py -3.9 -m pip install -r requirements.txt
```

---

## ▶️ Run the Application

### Method 1 — Double Click ⭐

Simply double-click:

```text
run.bat
```

The launcher automatically starts the Streamlit application.

You should see:

```text
==========================================
       PPT SLIDE EXTRACTOR
==========================================

Checking Python 3.9...
Python 3.9.x

Starting application...
```

Then Streamlit provides a local address such as:

```text
http://localhost:8501
```

Open that address in your browser.

---

### Method 2 — Command Line

You can also run the application manually:

```bash
py -3.9 -m streamlit run PPT-Slide-Extractor.py
```

---

## 📁 Project Structure

```text
PPT-Slide-Extractor/
│
├── 📄 PPT-Slide-Extractor.py
│   └── Main Streamlit application
│
├── ▶️ run.bat
│   └── One-click Windows launcher
│
├── 📦 requirements.txt
│   └── Python dependencies
│
├── 📜 LICENSE
│   └── MIT License
│
└── 📂 data/
    └── Extracted presentation folders
```

After using the application:

```text
PPT-Slide-Extractor/
│
├── PPT-Slide-Extractor.py
├── run.bat
├── requirements.txt
├── LICENSE
│
└── data/
    │
    ├── Presentation-1/
    │   ├── slide_01.png
    │   ├── slide_02.png
    │   └── slide_03.png
    │
    └── Presentation-2/
        ├── slide_01.png
        ├── slide_02.png
        └── slide_03.png
```

---

## 🎯 Example

Suppose you upload:

```text
CKEC-Smart-Campus-Resource-and-Energy-Waste-Detector.pptx
```

The application creates:

```text
data/
└── CKEC-Smart-Campus-Resource-and-Energy-Waste-Detector/
    │
    ├── slide_01.png
    ├── slide_02.png
    ├── slide_03.png
    ├── slide_04.png
    └── slide_05.png
```

The slides can then be used for:

* 📱 Social media posts
* 🎨 Thumbnail creation
* 📄 Documentation
* 🖼️ Image editing
* 🌐 Website content
* 📚 Project portfolios
* 📊 Presentation previews

---

## 💡 Use Cases

### 🎓 Students

Quickly convert project presentations into individual images for:

* Project submissions
* Documentation
* Portfolios
* LinkedIn posts
* Project demonstrations

### 💼 Professionals

Useful for:

* Presentation previews
* Documentation
* Reports
* Slide sharing
* Design review

### 🎨 Designers

Extract individual presentation slides for:

* Editing
* Redesigning
* Thumbnail creation
* Visual references

---

## 🔒 Privacy

The application is designed to process presentations locally on your computer.

Uploaded presentation files are processed by the local application and saved to the project's:

```text
data/
```

directory.

No external upload service is required for the core extraction process.

---

## ⚠️ Troubleshooting

### Python 3.9 Not Found

Check:

```bash
py -3.9 --version
```

If Python 3.9 is installed correctly, this should display its version.

---

### Streamlit Does Not Start

Install Streamlit again:

```bash
py -3.9 -m pip install streamlit
```

Then run:

```bash
py -3.9 -m streamlit run PPT-Slide-Extractor.py
```

---

### PowerPoint Export Fails

Make sure Microsoft PowerPoint is installed and can open the presentation normally.

You can also install LibreOffice to provide a fallback conversion method.

---

### No Slides Are Generated

Check that:

* The uploaded file is a valid `.ppt` or `.pptx`
* The presentation can be opened normally
* Microsoft PowerPoint or LibreOffice is installed
* Python dependencies are installed correctly

---

## 🚀 Future Improvements

Planned improvements may include:

* 📦 Download extracted slides as ZIP
* 🖼️ JPG/WebP output support
* 🎚️ Image quality controls
* 📐 Custom image resolution
* 🔢 Custom slide naming
* 🗂️ Drag-and-drop folder processing
* 📊 Batch PPT processing
* 🧹 Automatic duplicate handling
* 👀 Slide preview gallery
* 🌐 LAN access
* 🌓 Dark/Light interface
* 📱 Improved mobile interface

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome!

If you have an idea:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

See the `LICENSE` file for more information.

---

## 👨‍💻 Author

**Sam Wilson**

GitHub:
https://github.com/rsamwilson2323-cloud

---

## ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub.

**Repository:**
https://github.com/rsamwilson2323-cloud/PPT-Slide-Extractor

---

<p align="center">
  📊 <strong>PPT Slide Extractor</strong>
  <br>
  Convert • Extract • Organize
  <br><br>
  Made with ❤️ using Python
</p>
