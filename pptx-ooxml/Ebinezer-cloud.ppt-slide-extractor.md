# 📊 PPT Slide Extractor

<p align="center">
  <strong>🚀 Convert PowerPoint presentations into high-quality PNG slide images automatically.</strong>
</p>

<p align="center">
  Upload a <code>.ppt</code> or <code>.pptx</code> presentation and extract individual slides as images with a simple browser-based interface.
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20UI-red?logo=streamlit)
![PowerPoint](https://img.shields.io/badge/Microsoft-PowerPoint-orange?logo=microsoftpowerpoint)
![License](https://img.shields.io/badge/License-MIT-green)

</p>

---

## 🌟 About

**PPT Slide Extractor** is a Python-based utility designed to convert PowerPoint presentations into individual high-quality PNG slide images.

The application provides a simple **Streamlit web interface** where users can upload `.ppt` or `.pptx` files and extract their slides automatically.

Instead of manually taking screenshots of every slide, the application automates the extraction process and organizes the generated images into presentation-specific folders.

### ✨ What it does

* 📤 Accepts `.ppt` and `.pptx` presentations
* 🔄 Processes PowerPoint slides automatically
* 🖼️ Extracts individual slides as PNG images
* 📁 Organizes slides into separate presentation folders
* 💾 Stores extracted images locally
* 🌐 Provides a simple Streamlit web interface
* ▶️ Includes a Windows `run.bat` launcher
* 🖥️ Designed for Windows-based PowerPoint automation

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

Each presentation slide is converted into an individual PNG image.

Example:

```text
slide_01.png
slide_02.png
slide_03.png
slide_04.png
```

---

### 📂 Automatic Organization

Extracted slides can be organized by presentation name.

Example:

```text
data/
└── My-Presentation/
    ├── slide_01.png
    ├── slide_02.png
    ├── slide_03.png
    └── slide_04.png
```

---

### ⚡ Simple Workflow

The application is designed to keep the extraction process simple:

```text
       📤 Upload PPT/PPTX
              │
              ▼
       📄 Read Presentation
              │
              ▼
       🖥️ Process Slides
              │
              ▼
       🔄 Extract / Convert
              │
              ▼
         🖼️ PNG Images
              │
              ▼
       📁 Organize Output
```

---

## 🖥️ User Interface

The application uses Streamlit to provide a simple browser-based interface.

Typical workflow:

```text
📊 PPT Slide Extractor

Upload your PowerPoint presentation

        [ Browse Files ]

        🚀 Extract Slides

              ↓

      🖼️ Extracted Slides
```

After processing, the generated slide images can be accessed from the project's output location.

---

## 🛠️ Technology Stack

| Technology              | Purpose                         |
| ----------------------- | ------------------------------- |
| 🐍 Python 3.9           | Core application                |
| 🌐 Streamlit            | Web-based user interface        |
| 🪟 PyWin32              | Windows / PowerPoint automation |
| 🖼️ PyMuPDF             | PDF/image processing            |
| 📊 Microsoft PowerPoint | Presentation rendering          |
| 🖼️ PNG                 | Extracted slide format          |
| 💻 Windows Batch        | One-click launcher              |

---

## 📋 Requirements

Before running the project, make sure you have:

### Python

Python **3.9.x** is recommended.

Check your Python version:

```bash
py -3.9 --version
```

Expected:

```text
Python 3.9.x
```

---

### Microsoft PowerPoint

Microsoft PowerPoint is recommended for PowerPoint-based slide rendering and automation.

Make sure PowerPoint is installed and can open your `.ppt` / `.pptx` files normally.

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ebinezer-cloud/ppt-slide-extractor.git
```

### 2. Open the Project Folder

```bash
cd ppt-slide-extractor
```

### 3. Install Dependencies

```bash
py -3.9 -m pip install -r requirements.txt
```

If you want to install the main dependencies manually:

```bash
py -3.9 -m pip install streamlit PyMuPDF pywin32
```

---

## 🚀 Run the Application

### Method 1 — One-Click Launch ⭐

Simply double-click:

```text
run.bat
```

The launcher checks for Python 3.9 and starts the Streamlit application.

You should see something similar to:

```text
==========================================
      PPT SLIDE EXTRACTOR
==========================================

Checking Python 3.9...
Python 3.9.x

Starting Streamlit...
```

Streamlit will then provide a local URL such as:

```text
http://localhost:8501
```

Open the address in your browser.

---

### Method 2 — Command Line

You can also start the application manually:

```bash
py -3.9 -m streamlit run PPT-Slide-Extractor.py
```

Then open:

```text
http://localhost:8501
```

---

## 📁 Project Structure

```text
ppt-slide-extractor/
│
├── 📄 PPT-Slide-Extractor.py
│   └── Main Streamlit application
│
├── 📦 requirements.txt
│   └── Python dependencies
│
├── ▶️ run.bat
│   └── Windows one-click launcher
│
├── 📜 LICENSE
│   └── MIT License
│
└── 📂 data/
    └── Extracted slide images
```

---

## 🎯 Example

Suppose you upload:

```text
AI-Smart-Campus.pptx
```

The extracted slides can be organized as:

```text
data/
└── AI-Smart-Campus/
    ├── slide_01.png
    ├── slide_02.png
    ├── slide_03.png
    ├── slide_04.png
    └── slide_05.png
```

Each PNG represents an individual presentation slide.

---

## 💡 Use Cases

### 🎓 Students

Useful for:

* 📚 Project presentations
* 📝 Documentation
* 🎓 Academic submissions
* 📊 Presentation previews
* 💼 Portfolio creation

### 💼 Professionals

Useful for:

* 📄 Documentation
* 📊 Presentation previews
* 🖼️ Slide sharing
* 🎨 Design references
* 📋 Reports

### 🎨 Designers

Extracted slides can be used as:

* 🎨 Design references
* 🖼️ Image editing sources
* 📱 Social media content
* 🧩 Presentation components
* 🖥️ Visual references

---

## 🔒 Privacy

The project is designed to process presentation files locally on the user's computer.

The core extraction workflow does not require uploading presentations to an external cloud service.

Your presentation files remain under your local control.

---

## ⚠️ Troubleshooting

### ❌ `No module named streamlit`

Install Streamlit for Python 3.9:

```bash
py -3.9 -m pip install streamlit
```

Then verify:

```bash
py -3.9 -m streamlit --version
```

---

### ❌ Python 3.9 Not Found

Check:

```bash
py -3.9 --version
```

If Python 3.9 is installed correctly, its version should be displayed.

---

### ❌ `requirements.txt` Not Found

Make sure you are inside the correct project directory:

```bash
cd ppt-slide-extractor
```

Then check:

```bash
dir
```

You should see:

```text
PPT-Slide-Extractor.py
requirements.txt
run.bat
LICENSE
```

---

### ❌ PowerPoint Processing Fails

Make sure:

* Microsoft PowerPoint is installed
* PowerPoint can open the presentation normally
* The uploaded file is a valid `.ppt` or `.pptx`
* `pywin32` is installed correctly

Install it with:

```bash
py -3.9 -m pip install pywin32
```

---

## 🚀 Future Improvements

Planned improvements may include:

* 📦 Download all slides as ZIP
* 🖼️ JPG / WebP output support
* 🎚️ Image quality controls
* 📐 Custom resolution
* 🔢 Custom slide naming
* 🖱️ Drag-and-drop upload
* 📊 Batch presentation processing
* 👀 Slide preview gallery
* 🌓 Dark / Light interface
* 📱 Improved responsive UI
* 🗂️ Advanced output management
* ⚡ Faster slide processing

---

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome.

To contribute:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push the branch
6. Open a Pull Request

---

## 📜 License

This project is licensed under the **MIT License**.

See the [`LICENSE`](LICENSE) file for more information.

---

## 👨‍💻 Author

### Ebinezer

AI & Robotics Enthusiast • Python Developer • Automation & Computer Vision

GitHub:

https://github.com/Ebinezer-cloud

---

## ⭐ Support

If you find **PPT Slide Extractor** useful, consider giving the repository a ⭐ on GitHub.

Your support helps encourage further development and improvements.

### Repository

https://github.com/Ebinezer-cloud/ppt-slide-extractor

---

<p align="center">
  📊 <strong>PPT Slide Extractor</strong>
  <br>
  Convert • Extract • Organize
  <br><br>
  Built with ❤️ using Python & Streamlit
</p>
