# System Architecture — AI Academic & Cognitive Performance Optimizer

## 1. High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────────────┐
│                        USER (Web Browser)                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐  │
│  │  Chat Input Box  │  │ Parameter Sliders│  │ Suggestion Btns  │  │
│  │  (Text Query)    │  │ (Temp, Top-p,    │  │ (Pre-built       │  │
│  │                  │  │  Max Tokens)     │  │  queries)        │  │
│  └────────┬─────────┘  └────────┬─────────┘  └────────┬─────────┘  │
│           │                     │                      │            │
│           └─────────────────────┼──────────────────────┘            │
│                                 ▼                                   │
└─────────────────────────────────┬───────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                     STREAMLIT APPLICATION (app.py)                  │
│                                                                     │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    INPUT PROCESSING                          │   │
│  │  1. Receive user query                                      │   │
│  │  2. Load chat history from session state                    │   │
│  │  3. Read parameter values (temperature, top_p, max_tokens)  │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                  PROMPT CONSTRUCTION (prompts.py)            │   │
│  │  1. Load SYSTEM_PROMPT (domain restriction + output format) │   │
│  │  2. Append chat history (multi-turn context)                │   │
│  │  3. Append new user query                                   │   │
│  │  Output: messages = [system, ...history, user]              │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                    API CALL (OpenAI)                         │   │
│  │  client.chat.completions.create(                            │   │
│  │      model       = user_selected_model,                     │   │
│  │      messages     = constructed_messages,                   │   │
│  │      temperature  = slider_value,                           │   │
│  │      top_p        = slider_value,                           │   │
│  │      max_tokens   = slider_value                            │   │
│  │  )                                                          │   │
│  └──────────────────────────┬──────────────────────────────────┘   │
│                              ▼                                      │
│  ┌─────────────────────────────────────────────────────────────┐   │
│  │                   OUTPUT RENDERING                          │   │
│  │  1. Extract response.choices[0].message.content             │   │
│  │  2. Render as Markdown in chat bubble                       │   │
│  │  3. Append to session state (chat history)                  │   │
│  └─────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────┐
│                      OpenAI API (Cloud)                             │
│  ┌──────────────┐  ┌──────────────────┐  ┌───────────────────────┐ │
│  │  GPT-3.5     │  │  System Prompt   │  │  Temperature / Top-p  │ │
│  │  / GPT-4     │  │  Enforcement     │  │  Sampling Control     │ │
│  └──────────────┘  └──────────────────┘  └───────────────────────┘ │
└─────────────────────────────────────────────────────────────────────┘
```

## 2. Component Breakdown

### Component 1: Frontend (Streamlit UI — `app.py`)

| Element | Purpose |
|---------|---------|
| Chat input box | Accepts natural language queries from the student |
| Suggestion buttons | Pre-built prompts for first-time users |
| Sidebar sliders | Adjust Temperature, Top-p, Max Tokens in real time |
| Model selector | Choose between GPT-3.5-turbo, GPT-4, etc. |
| Chat display | Renders conversation history with Markdown formatting |

### Component 2: Prompt Engine (`prompts.py`)

| Function | Purpose |
|----------|---------|
| `SYSTEM_PROMPT` | Master instruction set that constrains the AI to academic domain, enforces structured output format, and grounds advice in cognitive science |
| `build_messages()` | Constructs the full API payload: `[system_prompt, ...chat_history, user_query]` |

### Component 3: Configuration (`config.py`)

| Setting | Default | Purpose |
|---------|---------|---------|
| `DEFAULT_TEMPERATURE` | 0.3 | Low randomness for structured advice |
| `DEFAULT_TOP_P` | 0.9 | Broad but controlled vocabulary |
| `MAX_TOKENS` | 1024 | Sufficient for detailed plans |
| `DOMAIN_KEYWORDS` | 40+ terms | Client-side domain validation |

### Component 4: OpenAI API (External)

The API receives the constructed messages and returns a completion based on the model parameters. Key parameters sent:
- `model`: Which GPT model to use
- `messages`: The full conversation context including system prompt
- `temperature`: Controls output randomness
- `top_p`: Controls vocabulary diversity
- `max_tokens`: Limits response length

## 3. Data Flow (Step-by-Step)

```
Step 1: User types query → "Create a study plan for my physics exam"
Step 2: app.py reads slider values → temperature=0.3, top_p=0.9
Step 3: build_messages() constructs:
        [
          {"role": "system",    "content": SYSTEM_PROMPT},
          ...previous_messages,
          {"role": "user",      "content": "Create a study plan..."}
        ]
Step 4: OpenAI API processes with temperature=0.3, top_p=0.9
Step 5: API returns structured response following system prompt format
Step 6: Response rendered as Markdown in Streamlit chat bubble
Step 7: Both user query and response saved to session state
```

## 4. Why This Architecture?

| Design Decision | Reasoning |
|----------------|-----------|
| **Streamlit frontend** | Rapid prototyping, built-in chat UI, zero JavaScript needed |
| **System prompt enforcement** | Domain restriction happens at the AI level, not just client-side |
| **Session state for history** | Enables multi-turn conversations without a database |
| **Sliders for parameters** | Demonstrates temperature/top-p effects in real-time |
| **Separated config/prompts** | Clean architecture, easy to modify without touching main app |
