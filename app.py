"""
AI Academic & Cognitive Performance Optimizer — Streamlit Application
═══════════════════════════════════════════════════════════════════════
A domain-specific Generative AI chatbot that helps students optimize
study planning, focus, sleep, and exam preparation.

Run:  streamlit run app.py
"""

import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

from config import (
    APP_TITLE, APP_SUBTITLE, SIDEBAR_TITLE,
    DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_TOP_P,
    MAX_TOKENS, QUERY_CATEGORIES,
)
from prompts import build_messages

# ── Load environment variables ──────────────────────────────────────
load_dotenv()

# ══════════════════════════════════════════════════════════════════════
#  PAGE CONFIGURATION
# ══════════════════════════════════════════════════════════════════════
st.set_page_config(
    page_title="AcadeMind — Academic Optimizer",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Main header styling */
    .main-header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem 2rem;
        border-radius: 12px;
        margin-bottom: 1.5rem;
        color: white;
    }
    .main-header h1 {
        color: white !important;
        margin: 0 !important;
        font-size: 1.8rem !important;
    }
    .main-header p {
        color: rgba(255,255,255,0.85);
        margin: 0.3rem 0 0 0;
        font-size: 1rem;
    }

    /* Chat message styling */
    .stChatMessage {
        border-radius: 12px !important;
    }

    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #1a1a2e 0%, #16213e 100%);
    }
    [data-testid="stSidebar"] * {
        color: #e0e0e0 !important;
    }
    [data-testid="stSidebar"] .stSlider > div > div > div {
        color: #667eea !important;
    }

    /* Category pills */
    .category-pill {
        display: inline-block;
        padding: 0.3rem 0.8rem;
        margin: 0.2rem;
        border-radius: 20px;
        background: rgba(102, 126, 234, 0.15);
        border: 1px solid rgba(102, 126, 234, 0.3);
        font-size: 0.85rem;
    }

    /* Info boxes */
    .info-box {
        background: rgba(102, 126, 234, 0.08);
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 0 8px 8px 0;
        margin: 0.5rem 0;
    }
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════
#  SIDEBAR — Model Configuration
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown(f"## {SIDEBAR_TITLE}")
    st.markdown("---")

    # API Key input
    api_key = st.text_input(
        "🔑 Groq API Key",
        type="password",
        placeholder="gsk_...",
        help="Paste your Groq API key here. Get one free at console.groq.com (no credit card needed)",
        value=os.getenv("GROQ_API_KEY", ""),
    )

    st.markdown("---")
    st.markdown("### 🎛️ Generation Parameters")

    # Temperature slider
    temperature = st.slider(
        "🌡️ Temperature",
        min_value=0.0,
        max_value=1.0,
        value=DEFAULT_TEMPERATURE,
        step=0.1,
        help=(
            "Controls randomness. Lower = more focused and deterministic. "
            "Higher = more creative and varied. Recommended: 0.3 for study plans."
        ),
    )

    # Top-p slider
    top_p = st.slider(
        "🎯 Top-p (Nucleus Sampling)",
        min_value=0.0,
        max_value=1.0,
        value=DEFAULT_TOP_P,
        step=0.05,
        help=(
            "Controls diversity via nucleus sampling. "
            "0.9 = considers top 90% probability mass. Recommended: 0.9."
        ),
    )

    # Max tokens
    max_tokens = st.slider(
        "📏 Max Response Length",
        min_value=256,
        max_value=2048,
        value=MAX_TOKENS,
        step=128,
        help="Maximum number of tokens in the response.",
    )

    # Model selection
    model = st.selectbox(
        "🤖 Model",
        options=["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "gemma2-9b-it"],
        index=0,
        help="Select the model. llama-3.3-70b-versatile is recommended (powerful and free).",
    )

    st.markdown("---")
    st.markdown("### 📊 Current Settings")
    st.code(
        f"Model:       {model}\n"
        f"Temperature: {temperature}\n"
        f"Top-p:       {top_p}\n"
        f"Max Tokens:  {max_tokens}",
        language="yaml",
    )

    # Parameter explanation toggle
    with st.expander("ℹ️ What do these parameters mean?"):
        st.markdown("""
        **Temperature (0.0 – 1.0)**
        - `0.0–0.3`: Very focused, deterministic → best for study plans
        - `0.4–0.6`: Balanced creativity and structure
        - `0.7–1.0`: More creative, varied → may reduce consistency

        **Top-p (Nucleus Sampling)**
        - `0.9`: Model considers words within the top 90% probability
        - Lower values = more conservative word choices
        - Higher values = broader vocabulary usage

        **Recommended for this app:** `Temperature=0.3, Top-p=0.9`
        """)

    st.markdown("---")
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()


# ══════════════════════════════════════════════════════════════════════
#  MAIN CONTENT
# ══════════════════════════════════════════════════════════════════════

# Header
st.markdown(f"""
<div class="main-header">
    <h1>{APP_TITLE}</h1>
    <p>{APP_SUBTITLE}</p>
</div>
""", unsafe_allow_html=True)

# Category display
cols = st.columns(len(QUERY_CATEGORIES))
for i, cat in enumerate(QUERY_CATEGORIES):
    with cols[i]:
        st.markdown(f'<div class="category-pill">{cat}</div>', unsafe_allow_html=True)

st.markdown("")

# ── Quick Prompt Suggestions ────────────────────────────────────────
if "messages" not in st.session_state or len(st.session_state.messages) == 0:
    st.markdown("### 💡 Try asking me:")
    suggestion_cols = st.columns(2)
    suggestions = [
        "Create a 4-week study plan for my final exams in Math, Physics, and Chemistry",
        "How can I improve my focus during long study sessions?",
        "What is the ideal sleep schedule for a college student to maximize memory retention?",
        "Give me a Pomodoro-based revision strategy for the night before an exam",
    ]
    for i, suggestion in enumerate(suggestions):
        with suggestion_cols[i % 2]:
            if st.button(f"📌 {suggestion}", key=f"sugg_{i}", use_container_width=True):
                st.session_state.pending_suggestion = suggestion
                st.rerun()


# ══════════════════════════════════════════════════════════════════════
#  CHAT LOGIC
# ══════════════════════════════════════════════════════════════════════

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"], avatar="🧑‍🎓" if msg["role"] == "user" else "🧠"):
        st.markdown(msg["content"])


def generate_response(user_input: str) -> str:
    """
    Send user query to OpenAI API and return the response.

    Flow: User Input → build_messages() → OpenAI API → Structured Output
    """
    if not api_key:
        return "⚠️ **Please enter your Groq API key in the sidebar to get started.** Get one free at [console.groq.com](https://console.groq.com)"

    try:
        client = OpenAI(
            api_key=api_key,
            base_url="https://api.groq.com/openai/v1",
        )

        # Build the full message payload (system prompt + history + new query)
        messages = build_messages(
            user_query=user_input,
            chat_history=[
                {"role": m["role"], "content": m["content"]}
                for m in st.session_state.messages
            ],
        )

        # API call with user-configured parameters
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=temperature,
            top_p=top_p,
            max_tokens=max_tokens,
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"❌ **Error:** {str(e)}"


# Handle suggestion click
if "pending_suggestion" in st.session_state:
    user_input = st.session_state.pending_suggestion
    del st.session_state.pending_suggestion

    # Display user message
    with st.chat_message("user", avatar="🧑‍🎓"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate and display response
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Analyzing your query..."):
            response = generate_response(user_input)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})

# Chat input
if user_input := st.chat_input("Ask about study planning, focus, sleep, or exam strategies..."):
    # Display user message
    with st.chat_message("user", avatar="🧑‍🎓"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Generate and display response
    with st.chat_message("assistant", avatar="🧠"):
        with st.spinner("Analyzing your query..."):
            response = generate_response(user_input)
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})


# ══════════════════════════════════════════════════════════════════════
#  FOOTER
# ══════════════════════════════════════════════════════════════════════
st.markdown("---")
st.markdown(
    '<p style="text-align:center; color:#888; font-size:0.85rem;">'
    'AI Academic & Cognitive Performance Optimizer • Built with Streamlit + Groq API • '
    'Domain-restricted to academic optimization only'
    '</p>',
    unsafe_allow_html=True,
)
