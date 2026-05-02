# AI Academic & Cognitive Performance Optimizer

> A domain-specific Generative AI chatbot for student academic optimization.

---

## 🚀 Implementation Guide

### What's Already Done (by the project)

| Component | Status | File |
|-----------|--------|------|
| Streamlit web app | ✅ Complete | `app.py` |
| System prompt (domain-restricted) | ✅ Complete | `prompts.py` |
| Configuration module | ✅ Complete | `config.py` |
| Dependencies list | ✅ Complete | `requirements.txt` |
| System architecture doc | ✅ Complete | `docs/architecture.md` |
| Sample inputs/outputs | ✅ Complete | `docs/sample_io.md` |
| Model config justification | ✅ Complete | `docs/model_config.md` |
| Project report | ✅ Complete | `docs/report.md` |
| Presentation slides | ✅ Complete | `docs/presentation.md` |
| Viva Q&A (15 questions) | ✅ Complete | `docs/viva_prep.md` |

### What You Must Do Manually

| Task | Instructions |
|------|-------------|
| **1. Get OpenAI API Key** | Go to https://platform.openai.com/api-keys → Create new key → Copy it |
| **2. Install Python** | Ensure Python 3.9+ is installed: `python --version` |
| **3. Install dependencies** | Run: `pip install -r requirements.txt` |
| **4. Set your API key** | Copy `.env.example` to `.env` and paste your key (see below) |
| **5. Run the app** | Run: `streamlit run app.py` |
| **6. Test the chatbot** | Try the sample queries from `docs/sample_io.md` |

---

## 📦 Installation (Step by Step)

### Step 1: Open Terminal in Project Folder

```bash
cd ai-academic-optimizer
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `streamlit` — Web UI framework
- `openai` — OpenAI API client
- `python-dotenv` — Environment variable loader

### Step 3: Configure API Key

**Option A — Using .env file (recommended):**
```bash
# Copy the template
copy .env.example .env

# Edit .env and replace the placeholder with your actual key:
# OPENAI_API_KEY=sk-your-actual-key-here
```

**Option B — Enter in app:**
- Just paste your key directly in the sidebar text input when you run the app
- The key is NOT stored anywhere

### Step 4: Run the App

```bash
streamlit run app.py
```

The app opens at `http://localhost:8501` in your browser.

---

## 🎮 How to Use

1. **Enter your API key** in the sidebar (if not in `.env`)
2. **Adjust parameters** — Temperature (default 0.3), Top-p (default 0.9)
3. **Ask a question** — Type in the chat box or click a suggestion button
4. **View structured response** — Goal → Recommendations → Science → Quick Win
5. **Test domain restriction** — Try an off-topic query (e.g., "What's the weather?")
6. **Compare parameters** — Change temperature to 0.8, ask the same question, observe differences

---

## 📁 Project Structure

```
ai-academic-optimizer/
├── app.py                  # Main Streamlit application
├── config.py               # Configuration and constants
├── prompts.py              # System prompt + message builder
├── requirements.txt        # Python dependencies
├── .env.example            # API key template
├── README.md               # This file (implementation guide)
└── docs/
    ├── architecture.md     # System architecture diagram + explanation
    ├── sample_io.md        # 6 sample inputs/outputs + temperature comparison
    ├── model_config.md     # Temperature & Top-p justification
    ├── report.md           # Full project report (10 sections)
    ├── presentation.md     # 9-slide presentation content
    └── viva_prep.md        # 15 viva questions with answers
```

---

## ⚠️ Important Notes

- **API costs:** Each query costs ~$0.001–0.01 depending on model. GPT-3.5-turbo is cheapest.
- **API key safety:** Never commit your `.env` file to git. Add it to `.gitignore`.
- **Internet required:** The app needs internet to call the OpenAI API.
- **Python version:** Requires Python 3.9 or higher.
