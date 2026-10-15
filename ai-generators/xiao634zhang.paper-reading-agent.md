# 🦞 Paper Reading Agent Team

**论文研读Agent团队** - 一个多Agent协作的自动化论文分析与PPT生成系统

## ✨ 功能特性

- 🔍 **论文搜索** - ArXiv API搜索学术论文
- 📥 **PDF下载** - 支持代理、流式下载、自动重试
- 📖 **PDF解析** - 提取文本、章节、图表信息
- 📝 **摘要生成** - 快速摘要和详细摘要
- ⚖️ **批判性分析** - 论文质量评估
- 📊 **PPT生成** - 自动生成学术风格PPT
- 🧠 **记忆系统** - 本地存储研读历史
- 💬 **对话功能** - 与论文内容对话（需要Ollama）

## 🏗️ 架构设计

```
┌─────────────────────────────────────────────────────────────┐
│                    Paper Reading Team                        │
│                     (协调器 Agent)                            │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ Scraper Agent │    │ Parser Agent  │    │ Vector Agent  │
│   论文搜索     │    │   PDF解析     │    │   向量存储     │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│Summarizer Agt │    │ Reviewer Agt  │    │  PPT Agent    │
│   摘要生成     │    │   批判分析     │    │   PPT生成     │
└───────────────┘    └───────────────┘    └───────────────┘
        │                     │                     │
        └─────────────────────┼─────────────────────┘
                              │
                              ▼
                    ┌───────────────┐
                    │ Memory Agent  │
                    │   记忆存储     │
                    └───────────────┘
```

## 🚀 快速开始

### 安装依赖

```bash
pip install -r requirements.txt
```

### 基本使用

```python
from main import PaperReadingTeam

# 创建团队
team = PaperReadingTeam(user_id="your_user_id")

# 研读单篇论文
result = team.read_paper("1505.04597", generate_ppt=True)
print(f"PPT已生成: {result['ppt_path']}")

# 批量研读
results = team.batch_read(["1505.04597", "1606.06650", "1606.04797"])

# 搜索论文
papers = team.search_papers("medical image segmentation", max_results=10)

# 生成综述PPT
survey_ppt = team.batch_processor.generate_survey_ppt(
    papers, results, "医学图像分割综述"
)
```

### 使用代理

```bash
export https_proxy=http://127.0.0.1:7890
export http_proxy=http://127.0.0.1:7890
```

## 📁 项目结构

```
paper-reading-agent/
├── main.py                 # 主入口
├── config.yaml             # 配置文件
├── requirements.txt        # 依赖列表
├── agents/
│   ├── scraper_agent.py    # 论文搜索Agent
│   ├── parser_agent.py     # PDF解析Agent
│   ├── vector_agent.py     # 向量存储Agent
│   ├── summarizer_agent.py # 摘要生成Agent
│   ├── reviewer_agent.py   # 批判分析Agent
│   ├── ppt_agent.py        # PPT生成Agent
│   ├── memory_agent.py     # 记忆存储Agent
│   ├── chat_agent.py       # 对话Agent
│   └── batch_processor.py  # 批量处理器
├── data/
│   ├── pdfs/               # PDF存储
│   ├── memory.json         # 记忆数据
│   └── *.pptx              # 生成的PPT
└── README.md
```

## ⚙️ 配置说明

编辑 `config.yaml`:

```yaml
# 数据存储
data:
  output_dir: ./data
  pdf_dir: pdfs

# ArXiv搜索
scraper:
  max_results: 20
  sort_by: relevance

# PDF解析
parser:
  chunk_size: 1000
  chunk_overlap: 200

# 摘要生成
summarizer:
  use_local: true
  local_model: llama3.2

# PPT生成
ppt:
  template: academic
  style: dark_blue
```

## 🔧 可选功能

### 对话功能（需要Ollama）

```bash
# 安装Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 下载模型
ollama pull llama3.2
```

### 向量检索（需要LangChain）

```bash
pip install langchain langchain-community faiss-cpu
```

## 📊 示例输出

### 单篇论文PPT

```
第1页: 封面
第2页: 目录
第3页: 论文信息
第4页: 摘要
第5页: 核心方法
第6页: 实验结果
第7页: 总结
```

### 综述PPT

```
第1页: 封面
第2页: 目录
第3-N页: 各论文摘要
第N+1页: 总结与展望
```

## 🤝 贡献

欢迎提交Issue和Pull Request！

## 📄 许可证

MIT License

## 🙏 致谢

- [ArXiv API](https://arxiv.org/help/api/) - 论文搜索
- [PyMuPDF](https://pymupdf.readthedocs.io/) - PDF解析
- [python-pptx](https://python-pptx.readthedocs.io/) - PPT生成
- [Ollama](https://ollama.ai/) - 本地LLM推理
