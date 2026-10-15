# 🎯 Autonomous AI Presentation Creator

An autonomous multi-agent workflow built with **MachinaOS** that researches a topic, generates structured presentation content, and automatically creates a professional **PowerPoint (.pptx)** presentation using **python-pptx**.

---

## 🚀 Features

- 🤖 Multi-Agent Architecture
- 🔍 Automatic Topic Research
- 📝 Intelligent Presentation Outline Generation
- 📄 Professional Slide Content Creation
- 📊 Automatic PowerPoint Generation (.pptx)
- 🎨 Theme & Layout Support
- 🖼️ Image Query Generation for Each Slide
- ⚡ End-to-End Workflow Automation

---

## 🏗️ Workflow

```text
                User
                  │
                  ▼
        Presentation Manager
                  │
      ┌───────────┴───────────┐
      ▼                       ▼
Research Agent          Slide Writer
                  │
                  ▼
          PPT Generator
          (python-pptx)
                  │
                  ▼
          presentation.pptx
```

---

## 🧠 AI Employees

### 📌 Presentation Manager
- Coordinates the complete workflow
- Delegates tasks to specialist agents
- Collects outputs
- Returns the final presentation

### 🔍 Research Agent
- Researches the requested topic
- Identifies key concepts
- Generates a logical presentation outline
- Suggests image search queries

### ✍️ Slide Writer
- Converts the outline into presentation-ready slides
- Writes concise bullet points
- Determines suitable slide layouts
- Generates speaker notes (optional)

### 💻 PPT Generator
- Uses **python-pptx**
- Creates PowerPoint slides
- Applies layouts and formatting
- Inserts titles and bullet points
- Exports the final `.pptx` file

---

## 🛠️ Tech Stack

- MachinaOS
- AI Employees
- Python
- python-pptx
- Web Search
- JSON
- Workflow Automation

---

## 📂 Project Structure

```text
Autonomous-AI-Presentation-Creator/
│
├── workflow/
│   └── workflow.json
│
├── screenshots/
│
├── README.md
│
└── sample_output/
    └── presentation.pptx
```

---

## 📋 Workflow Process

1. User provides a presentation topic.
2. Research Agent gathers relevant information.
3. Research Agent creates a presentation outline.
4. Slide Writer generates concise slide content.
5. PPT Generator creates a PowerPoint presentation using `python-pptx`.
6. Final presentation is exported as `.pptx`.

---

## 📸 Screenshots

### Workflow

<img width="1241" height="725" alt="workflow" src="https://github.com/user-attachments/assets/38bdf7d2-ba1e-47c3-8895-6aaec055a5a4" />

### Generated Presentation

<img width="1891" height="772" alt="sample" src="https://github.com/user-attachments/assets/95675fc9-a475-4f63-a6d0-6dbfe94ab311" />

---

## 🎯 Future Improvements

- Automatic image download and insertion
- Multiple presentation themes
- Charts and graphs
- Smart slide layouts
- Company branding
- Export speaker notes
- PDF export
- Animated slides

---

## 💡 Learning Outcomes

This project demonstrates:

- Multi-Agent Orchestration
- Prompt Engineering
- Workflow Automation
- AI Employee Collaboration
- Structured Data Generation
- Automated Document Generation
- Python Integration
- PowerPoint Automation

---

## 👨‍💻 Author

**Siddharth**

Built during my internship at **Zeenie** using **MachinaOS**.
