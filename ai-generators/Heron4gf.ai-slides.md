# Presentation Generator - Optimized Version

An AI-powered presentation generator that creates professional Quarkdown presentations through a structured 4-step pipeline.

## Overview

This system generates presentations by following a systematic approach:
1. **Web Research & Resume**: Gather comprehensive information about the topic
2. **Image Collection**: Find and integrate relevant images with descriptions
3. **Markdown Presentation**: Structure content into a presentation format
4. **Quarkdown Adaptation**: Convert to rich Quarkdown format for compilation

## Project Structure

### Core Files
- `config.yml` - Main configuration file (YAML-based)
- `llm_optimized.py` - Optimized LLM module with 4-step pipeline
- `slides_pipeline_optimized.py` - Main pipeline orchestrator
- `slides_response_optimized.py` - Enhanced response models
- `generate_quarkdown.py` - Quarkdown compilation utilities

### Template Files
- `templates/step1_research.md` - Research step prompt template
- `templates/step2_images.md` - Image collection step prompt template
- `templates/step3_markdown.md` - Markdown formatting step prompt template
- `templates/step4_quarkdown.md` - Quarkdown adaptation step prompt template

### Legacy Files (for backward compatibility)
- `llm.py` - Original LLM implementation
- `slides_pipeline.py` - Original pipeline
- `slides_response.py` - Original response models
- `prompt.md` - Original monolithic prompt

## Configuration

The system is configured via `config.yml`:

```yaml
presentation:
  llm:
    model: "openai:gpt-4.1-nano"
    max_results_per_search: 5
    image_search_limit: 5
  
  steps:
    step1_research:
      name: "Web Research & Resume"
      input: ["user_prompt"]
      output: "research_resume"
      tools: ["duckduckgo_search_tool"]
    # ... other steps
```

## Usage

### Quick Start

```python
from slides_pipeline_optimized import prompt_to_presentation_pipeline

# Generate a presentation
prompt_to_presentation_pipeline("Create a presentation about artificial intelligence")
```

### Advanced Usage

```python
from llm_optimized import PresentationPipeline

# Initialize pipeline with custom config
pipeline = PresentationPipeline("custom_config.yml")

# Generate presentation
document = pipeline.generate_presentation("Your topic here")
```

## Pipeline Steps

### Step 1: Web Research & Resume
- **Input**: User prompt
- **Output**: Structured research resume
- **Tools**: DuckDuckGo search
- **Purpose**: Gather comprehensive information about the topic

### Step 2: Image Collection
- **Input**: User prompt + Research resume
- **Output**: Research resume enhanced with images
- **Tools**: Image search (DuckDuckGo)
- **Purpose**: Find and integrate relevant visual content

### Step 3: Markdown Presentation
- **Input**: User prompt + Research with images
- **Output**: Markdown-formatted presentation
- **Tools**: None (formatting only)
- **Purpose**: Structure content into presentation slides

### Step 4: Quarkdown Adaptation
- **Input**: User prompt + Markdown presentation
- **Output**: Document (Quarkdown format)
- **Tools**: None (conversion only)
- **Purpose**: Convert to rich Quarkdown with advanced features

## Key Features

### Modular Design
- Each step has its own specialized prompt template
- Tools are filtered per step (only relevant tools available)
- Clear input/output definitions for each step

### Configurable
- YAML-based configuration
- Customizable prompts via template files
- Adjustable parameters for each step

### Step Isolation
- Each step receives only the necessary input
- Clear data flow between steps
- Independent execution of each phase

### Enhanced Error Handling
- Structured error reporting
- Step-by-step execution tracking
- Graceful failure handling

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
OPENAI_API_KEY=your_api_key_here
```

3. Configure Quarkdown path in `config.yml` if needed

## Running the System

### Streamlit
```bash
streamlit run streamlit_app.py
```

### Programmatic
```python
from slides_pipeline_optimized import prompt_to_presentation_pipeline

prompt_to_presentation_pipeline("Your presentation topic")
```

## Customization

### Adding New Steps
1. Add step configuration to `config.yml`
2. Create prompt template in `templates/`
3. Update pipeline logic in `llm_optimized.py`

### Modifying Prompts
Edit the corresponding template file in `templates/` directory.

### Changing Tools
Update the `tools` list in the step configuration in `config.yml`.

## Output

The system generates:
- Quarkdown presentation file (`.qmd`)
- Compiled presentation (HTML/PDF via Quarkdown)
- Intermediate outputs for debugging
