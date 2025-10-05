# RAG Website Generator

A Retrieval-Augmented Generation (RAG) application that generates complete, single-file HTML websites from natural language requests. It retrieves relevant UI components, prompts an LLM (Qwen 2.5 Coder) to compose a full page, and guarantees a complete result with a structured fallback generator.

## 🚀 Features

- **Semantic Component Search**: Uses vector embeddings to find relevant UI components
- **FAISS Vector Database**: Fast and efficient similarity search
- **LLM-first Generation**: Uses Qwen 2.5 Coder 3B (Instruct) to compose a cohesive website
- **Structured Fallback**: If LLM output is weak/invalid, a robust template-based generator produces a full site
- **Local Execution**: Runs locally (CPU/GPU); downloads models on first use
- **49 Pre-built Components**: Based on Keep Design components, covering foundations, UI, and dashboard patterns

## 🔧 Installation

### Step 1: Create Project Directory
```bash
mkdir rag-website-generator
cd rag-website-generator
```

### Step 2: Create All Python Files

Create the following files with the code provided in the artifacts:
- `requirements.txt`
- `config.py`
- `scraper.py`
- `embeddings.py`
- `vector_store.py`
- `generator.py`
- `main.py`

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
pip install -U transformers accelerate tiktoken
```

## 📁 Project Structure

```
rag-website-generator/
│
├── data/
│   ├── processed/              # CSV component database
│   └── embeddings/             # FAISS index and metadata
│
├── generated/                  # Generated websites
│
├── config.py                   # Configuration settings
├── scraper.py                  # Component database creation
├── embeddings.py               # Embedding generation
├── vector_store.py             # FAISS operations
├── generator.py                # Website code generation
├── main.py                     # Main application
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🎯 Usage

### First Time Setup

Run the main script. It will automatically set up the knowledge base:

```bash
python main.py
```

This will:
1. Create a component database (CSV file with 49 components)
2. Generate embeddings using sentence-transformers
3. Build a FAISS vector index
4. Download and load the Qwen model on first generation
5. Enter interactive mode

### Generating Websites

Once setup is complete, enter your request:

```
Enter your website request (or 'quit' to exit):
> Create a portfolio website

Enter your website request (or 'quit' to exit):
> Build an ecommerce product page

Enter your website request (or 'quit' to exit):
> Make a landing page for a SaaS product
```

The generated HTML file will be saved in the `generated/` directory as `website.html`.

## 🏗️ Architecture Overview

### 1. Component Database (scraper.py)
- Creates a CSV database with pre-defined UI components
- Each component has: ID, name, category, description, code snippet, use cases
- 15+ components covering common website needs

### 2. Embedding Generation (embeddings.py)
- Uses `sentence-transformers/all-MiniLM-L6-v2` model
- Converts component descriptions into 384-dimensional vectors
- Combines name, category, description, and use cases for rich embeddings

### 3. Vector Storage (vector_store.py)
- Uses FAISS (Facebook AI Similarity Search) for efficient retrieval
- IndexFlatL2: Exact L2 distance search
- Stores embeddings and metadata separately

### 4. Retrieval Process
```
User Query → Embed Query → Search FAISS → Get Top-K Components
```

### 5. Generation (generator.py)
- LLM-first: Prompts Qwen 2.5 Coder 3B with the request + top components
- Output validator: ensures full single-file HTML (doctype, head, Tailwind, header/main/footer)
- Structured fallback: if LLM response is weak/invalid, a template-based generator builds a complete page using retrieved components

### 6. Main Flow (main.py)
```
1. Setup (First Run):
   - Create component CSV
   - Generate embeddings
   - Build FAISS index

2. Query Processing:
   - Load vector database
   - Embed user query
   - Retrieve similar components
   - Generate HTML code
   - Save to file
```

## 🔍 How It Works

### Example Query: "Create a portfolio website"

**Step 1: Query Embedding**
```
Query: "Create a portfolio website"
↓
Embedding Model (MiniLM)
↓
384-dimensional vector
```

**Step 2: Similarity Search**
```
Query Vector → FAISS Index → Top 5 Matches:
1. Image Gallery (Score: 0.87)
2. Hero Section (Score: 0.82)
3. About Section (Score: 0.79)
4. Footer (Score: 0.76)
5. Navigation Bar (Score: 0.75)
```

**Step 3: Code Generation**
```
Retrieved Components
↓
Combine + Add Tailwind CSS
↓
Complete HTML File
```

## 🎨 Available Components (49)

Foundation (6): Colors, Typography, Shadow, Spacing Scale, Icons, Logo

UI (41): Button, Button Group, Avatar, Accordion, Alert, Badge, Charts, Empty, Messaging,
Skeleton, Steps, Breadcrumb, Checkbox, Checkbox Group, Date Picker, Dropdown, File Upload,
Modal, Pagination, Progress Bar, Rating, Slider, Tab Menu, Table, Text Area, Text Input,
Switch Toggle, Tooltip, Play Button, Popover, Search, Carousel, Tree, Toast, Context Menu,
Drawer, Color Picker, Transfer, Light Box, Wysiwyg Editor, Mega Menu

Dashboards (2): Project Management Dashboard, Mail Application Dashboard

## ⚙️ Configuration (config.py)

### Key Settings:

- **EMBEDDING_MODEL**: `sentence-transformers/all-MiniLM-L6-v2`
- **LLM_MODEL**: `Qwen/Qwen2.5-Coder-3B-Instruct` (set to 1.5B if memory-limited)
- **TOP_K_RESULTS**: 5 (number of retrieved components)
- **MAX_TOKENS**: 600–1500 depending on your hardware

### Why These Choices?

**Embedding Model:**
- **all-MiniLM-L6-v2** is chosen because:
  - Small size (80MB) - perfect for local execution
  - Fast inference speed
  - Good balance of quality and performance
  - Well-suited for short text (component descriptions)

**FAISS:**
- Facebook's vector similarity search library
- Highly optimized for speed
- IndexFlatL2 for exact search (small dataset)
- Can scale to millions of vectors

**LLM-First with Guaranteed Output:**
- Primary: Qwen 2.5 Coder 3B generates a cohesive page
- Guaranteed result: Structured fallback builds a complete page when LLM output is invalid/empty

## 🚀 Example Queries

Try these example queries:

```bash
# E-commerce
"Create an ecommerce website"
"Build an online store"
"Make a product showcase page"

# Portfolio
"Create a portfolio website"
"Build a photography portfolio"
"Make a designer portfolio"

# Business
"Create a landing page for SaaS"
"Build a company website"
"Make a business homepage"

# Specific needs
"Create a contact page"
"Build a pricing page"
"Make an about us page"
```

## 📊 Performance (Typical)

- **Setup Time**: ~1–3 minutes on first run (model download)
- **Query Time**: 3–25 seconds (LLM) / <2 seconds (structured fallback)
- **Memory**: ~6–10GB for Qwen 3B; ~4–6GB for Qwen 1.5B
- **Storage**: ~2–6GB (models + data)

## 🔧 Customization

### Adding New Components

Edit `scraper.py` and add to `create_sample_components()`:

```python
{
    'component_id': 'comp_0016',
    'name': 'Your Component Name',
    'category': 'Category',
    'description': 'Detailed description',
    'code_snippet': '<div>HTML code here</div>',
    'use_cases': 'When to use this component'
}
```

Then rebuild the knowledge base:
```bash
# Delete existing index
rm -rf data/embeddings/*

# Run setup again
python main.py
```

### Adjusting Retrieval

In `config.py`, change:
```python
TOP_K_RESULTS = 7  # Retrieve more components
```

## 🐛 Troubleshooting

### Model stalls after "Generating with LLM"
- Ensure you installed: `pip install -U transformers accelerate tiktoken`
- Reduce `MAX_TOKENS` in `config.py` to 400–600
- Try smaller model: `Qwen/Qwen2.5-Coder-1.5B-Instruct`
- If it still fails, the structured fallback will produce a complete page automatically

### FAISS index not found
Delete the data directory and run again:
```bash
rm -rf data/
python main.py
```

### Model download is slow
First run downloads weights. Subsequent runs use cache.

## 📝 Technical Details

### Vector Embeddings
- **Model**: all-MiniLM-L6-v2
- **Dimensions**: 384
- **Similarity Metric**: L2 (Euclidean distance)
- **Normalization**: None (using raw embeddings)

### FAISS Index
- **Type**: IndexFlatL2
- **Search**: Exact nearest neighbor
- **Distance**: L2 distance
- **Quantization**: None (exact vectors)

### Generation Strategy
- **Method**: LLM-first (Qwen) with strict prompt and output validation
- **Fallback**: Structured template generator to guarantee full HTML
- **Output**: Complete Tailwind-based HTML5 page (single file)

## 🎓 Learning Resources

- **FAISS**: https://github.com/facebookresearch/faiss
- **Sentence Transformers**: https://www.sbert.net/
- **RAG**: https://arxiv.org/abs/2005.11401
- **Tailwind CSS**: https://tailwindcss.com/

## 📄 License

This is a demonstration project. Feel free to use and modify for your needs.

---

**Built with ❤️ for simple, functional AI applications**