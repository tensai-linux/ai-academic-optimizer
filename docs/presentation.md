# Presentation Slides — AI Academic & Cognitive Performance Optimizer

---

## Slide 1: Title

- **Project Title:** AI Academic & Cognitive Performance Optimizer Chatbot
- **Subtitle:** A Domain-Specific Generative AI System for Student Success
- **Tech Stack:** Python · Streamlit · OpenAI GPT API
- [Student Name] | [Course Name] | [Date]

---

## Slide 2: Problem Statement

- Students struggle with **unstructured study habits** and inefficient learning
- Common issues:
  - No systematic study plan → last-minute cramming
  - Digital distractions → inability to sustain focus
  - Poor sleep hygiene → impaired memory consolidation
  - Passive study methods → low retention rates
- General-purpose AI (ChatGPT) gives **generic, unstructured advice**
- **Gap:** No specialized AI tool for academic performance optimization

---

## Slide 3: Our Solution

- **AcadeMind** — a domain-restricted AI chatbot for academic optimization
- Strictly limited to 4 domains:
  - 📚 Study Planning & Scheduling
  - 🧠 Focus & Cognitive Performance
  - 😴 Sleep Optimization for Learning
  - 📝 Exam Preparation Strategies
- Every response is **structured, actionable, and scientifically grounded**
- Off-topic queries are **automatically rejected**

---

## Slide 4: System Architecture

- **Input:** Student query via chat interface
- **Processing:** System prompt + chat history → message construction
- **API Call:** OpenAI GPT-3.5-turbo with tuned parameters
- **Output:** Structured response (Goal → Recommendations → Science → Quick Win)
- **Architecture:** `app.py` → `prompts.py` → `config.py` → OpenAI API
- Modular design: each component has a single responsibility

---

## Slide 5: Key Features

- ✅ **Domain Restriction** — rejects off-topic queries automatically
- ✅ **Structured Output** — consistent 4-part response format
- ✅ **Parameter Controls** — real-time Temperature & Top-p sliders
- ✅ **Scientific Grounding** — every recommendation cites cognitive science
- ✅ **Multi-Turn Chat** — remembers conversation context
- ✅ **Quick Start Suggestions** — pre-built prompts for new users
- ✅ **Model Selection** — choose between GPT-3.5, GPT-4, GPT-4o

---

## Slide 6: Demo Walkthrough

- **Step 1:** User opens the web app in browser
- **Step 2:** Enters API key in sidebar (one-time setup)
- **Step 3:** Adjusts Temperature (0.3) and Top-p (0.9) via sliders
- **Step 4:** Types query: *"Create a 2-week study plan for my biology exam"*
- **Step 5:** AI returns structured plan with time blocks, break intervals, and spaced repetition
- **Step 6:** User asks follow-up: *"How should I handle the toughest chapter?"*
- **Step 7:** AI uses context from previous turn to give personalized advice
- **Demo:** Off-topic test → *"What's the weather?"* → 🚫 Rejected

---

## Slide 7: Model Parameters

- **Temperature = 0.3**
  - Controls randomness of output
  - Low value → focused, deterministic, consistent
  - Ideal for structured study advice
- **Top-p = 0.9 (Nucleus Sampling)**
  - Controls vocabulary diversity
  - 0.9 = considers top 90% probability mass
  - Excludes noisy, unlikely words
- **Why these values?**
  - Students need reliable advice, not creative fiction
  - Low temperature reduces hallucination risk
  - Top-p 0.9 keeps language natural

---

## Slide 8: Results & Observations

| Test | Result |
|------|--------|
| Study plan query | ✅ Structured 4-part response with time blocks |
| Focus improvement | ✅ Specific techniques with scientific backing |
| Sleep optimization | ✅ Circadian rhythm advice with exact timings |
| Off-topic (cooking) | ✅ Rejected with redirect message |
| Temp 0.2 vs 0.8 | ✅ Visible difference: precision vs creativity |

- System prompt successfully enforces domain restriction
- All outputs follow mandated structure
- Temperature changes produce measurable output differences

---

## Slide 9: Conclusion

- Successfully built a **domain-specific Generative AI chatbot**
- Demonstrates practical **prompt engineering** for domain restriction
- Real-time **parameter tuning** shows temperature/top-p effects
- **Clean architecture:** 3 files, single responsibility, easy to explain
- **Future scope:**
  - Calendar API integration
  - Student profile tracking
  - Fine-tuned model on academic coaching data
- **Key takeaway:** Prompt engineering + parameter tuning can specialize a general LLM without custom training

---

*Each slide should have a clean background. Use a consistent color scheme (purple/indigo gradient). Minimal text — speak the details, don't write them.*
