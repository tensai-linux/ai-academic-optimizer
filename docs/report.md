# Project Report: AI Academic & Cognitive Performance Optimizer Chatbot

---

## 1. Introduction

The AI Academic & Cognitive Performance Optimizer is a domain-specific Generative AI chatbot built to help students improve their academic outcomes through scientifically grounded advice. Unlike general-purpose AI assistants, this system is strictly constrained to four domains: study planning, focus optimization, sleep optimization, and exam preparation.

The chatbot leverages OpenAI's GPT models with carefully engineered system prompts and tuned generation parameters to produce structured, actionable, and reproducible advice.

---

## 2. Problem Statement

Students face several challenges that reduce academic performance:

- **Poor study planning:** Lack of structured schedules leads to inefficient cramming
- **Inability to focus:** Digital distractions and dopamine dysregulation reduce deep work capacity
- **Bad sleep habits:** Late-night studying disrupts memory consolidation during sleep
- **Ineffective exam preparation:** Over-reliance on passive re-reading instead of active recall

Existing AI chatbots (ChatGPT, Gemini) provide generic advice without domain restriction, structured output, or scientific grounding. Students need a specialized tool that delivers actionable, evidence-based guidance.

---

## 3. Objectives

1. Build a domain-restricted AI chatbot focused exclusively on academic and cognitive optimization
2. Implement structured output formatting (Goal → Recommendation → Science → Quick Win)
3. Provide real-time model parameter controls (Temperature, Top-p) with visible effects
4. Ground all advice in cognitive science and neuroscience research
5. Deliver a clean, user-friendly web interface using Streamlit

---

## 4. Methodology

### 4.1 Development Approach
- **Architecture:** Modular Python application with separated concerns (config, prompts, app)
- **Frontend:** Streamlit for rapid prototyping with built-in chat UI components
- **Backend:** Python with OpenAI SDK for API integration
- **Prompt Engineering:** Iterative refinement of system prompt for domain restriction and output structure

### 4.2 Key Design Decisions

| Decision | Reasoning |
|----------|-----------|
| Streamlit over Flask/Django | Built-in chat UI, sliders, and session state; zero frontend code needed |
| System prompt enforcement | Domain restriction at the AI level, not just client-side filtering |
| Separated config/prompts modules | Clean architecture, easy to modify without touching main app |
| Session state for history | Multi-turn conversations without database overhead |

---

## 5. System Design

### 5.1 Architecture Overview

```
User Input → Streamlit UI → Prompt Builder → OpenAI API → Structured Response → Chat Display
```

### 5.2 Components

1. **app.py** — Main Streamlit application (UI, chat logic, API calls)
2. **prompts.py** — System prompt and message construction
3. **config.py** — Centralized configuration (defaults, keywords, UI strings)
4. **requirements.txt** — Python dependencies

### 5.3 Data Flow

1. User types a query or clicks a suggestion button
2. `build_messages()` constructs the API payload with system prompt + chat history
3. OpenAI API processes the request with user-configured temperature and top-p
4. Response is rendered as Markdown in the chat interface
5. Both query and response are saved to session state for multi-turn context

---

## 6. API Integration

### 6.1 OpenAI Chat Completions API

```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_query}
    ],
    temperature=0.3,
    top_p=0.9,
    max_tokens=1024
)
```

### 6.2 Key Parameters

| Parameter | Value | Purpose |
|-----------|-------|---------|
| model | gpt-3.5-turbo | Cost-effective, fast responses |
| temperature | 0.3 | Structured, deterministic output |
| top_p | 0.9 | Natural vocabulary diversity |
| max_tokens | 1024 | Sufficient for detailed plans |

### 6.3 Authentication
- API key loaded from `.env` file or entered via sidebar input
- Key is never stored or logged

---

## 7. Prompt Engineering Strategy

### 7.1 System Prompt Design

The system prompt is the most critical component. It enforces:

1. **Domain restriction** — Explicit instruction to reject off-topic queries with a specific rejection message
2. **Output structure** — Mandatory format: 🎯 Goal → 📋 Recommendation → 🔬 Scientific Basis → ⚡ Quick Win
3. **Behavioral rules** — Be specific (exact numbers), structured (numbered lists), scientific (cite research), concise (no filler)
4. **Personalization** — Adapt to user-mentioned schedules, subjects, and habits

### 7.2 Why This Approach Works

- **Domain restriction at AI level** ensures even creative prompt attacks are rejected
- **Structured format** guarantees consistent, evaluator-friendly output
- **Scientific grounding** differentiates this from generic chatbots
- **Quick Win** ensures every response has an immediate actionable takeaway

---

## 8. Model Configuration

### Temperature (0.3)
- Low randomness → consistent, reliable study advice
- Not 0.0 → avoids robotic-sounding responses
- Reduces hallucination risk for factual claims

### Top-p (0.9)
- Considers top 90% of word probability mass
- Broad enough for natural language, excludes noisy outliers
- Industry-standard default value

### Comparison Results
- **Temperature 0.2:** Highly consistent, textbook-style responses
- **Temperature 0.8:** More creative, varied phrasing, occasional novel suggestions
- Both maintain structured format due to strong system prompt

---

## 9. Results & Observations

### 9.1 Domain Restriction
- Successfully rejects off-topic queries (tested with cooking, sports, entertainment questions)
- Rejection message is consistent and redirects user to valid topics

### 9.2 Output Quality
- All responses follow the mandated 4-part structure
- Scientific references are relevant and accurate
- Quick Wins are genuinely actionable

### 9.3 Parameter Effects
- Temperature changes produce measurable differences in creativity and word choice
- Top-p changes affect vocabulary richness
- Low temperature (0.2–0.3) is optimal for study plans and schedules
- Higher temperature (0.5–0.8) works for motivational and brainstorming queries

### 9.4 Multi-Turn Context
- Chat history enables follow-up questions
- System prompt persists across turns, maintaining domain restriction

---

## 10. Conclusion

The AI Academic & Cognitive Performance Optimizer demonstrates a practical application of Generative AI in education. Key achievements:

1. **Domain-specific chatbot** that strictly operates within academic optimization
2. **Structured, scientific output** that goes beyond generic advice
3. **Real-time parameter tuning** allowing demonstration of temperature and top-p effects
4. **Clean, modular architecture** that is easy to understand, explain, and extend

The system proves that prompt engineering and parameter tuning are sufficient to transform a general-purpose LLM into a specialized, reliable domain assistant — without fine-tuning or custom training.

### Future Improvements
- Integration with calendar APIs for automated scheduling
- Student profile system for personalized long-term tracking
- Fine-tuned model on academic coaching datasets
- Mobile-responsive design with PWA support
