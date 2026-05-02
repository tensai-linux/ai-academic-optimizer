"""
Configuration module for AI Academic & Cognitive Performance Optimizer.
Centralizes all configurable parameters including model settings,
UI defaults, and domain boundaries.
"""

# ── Model Defaults ──────────────────────────────────────────────────
DEFAULT_MODEL = "llama-3.3-70b-versatile" # Free, powerful, fast via Groq
FALLBACK_MODEL = "llama-3.1-8b-instant"   # Lighter alternative
DEFAULT_TEMPERATURE = 0.3                # Low randomness → structured advice
DEFAULT_TOP_P = 0.9                      # Broad but controlled vocabulary
MAX_TOKENS = 1024                        # Enough for detailed plans

# ── Temperature Presets (shown in UI) ───────────────────────────────
TEMPERATURE_PRESETS = {
    "Precise (0.2)": 0.2,
    "Balanced (0.3)": 0.3,
    "Creative (0.5)": 0.5,
    "Explorative (0.8)": 0.8,
}

# ── Domain Keywords (for basic client-side filtering) ───────────────
DOMAIN_KEYWORDS = [
    "study", "exam", "focus", "sleep", "learn", "memory",
    "attention", "revision", "schedule", "plan", "cognitive",
    "dopamine", "concentration", "procrastination", "note",
    "pomodoro", "recall", "retention", "homework", "assignment",
    "grade", "test", "quiz", "semester", "gpa", "academic",
    "brain", "caffeine", "nap", "circadian", "melatonin",
    "motivation", "habit", "routine", "discipline", "distraction",
    "spaced repetition", "active recall", "flashcard",
    "performance", "optimize", "preparation", "strategy",
    "timetable", "deadline", "syllabus", "curriculum",
]

# ── Supported Query Categories ──────────────────────────────────────
QUERY_CATEGORIES = [
    "📚 Study Planning",
    "🧠 Focus & Cognitive Performance",
    "😴 Sleep Optimization",
    "📝 Exam Preparation",
    "🎯 General Academic Optimization",
]

# ── UI Strings ──────────────────────────────────────────────────────
APP_TITLE = "🧠 AI Academic & Cognitive Performance Optimizer"
APP_SUBTITLE = "Your AI-powered study coach — scientifically grounded, personally tailored."
SIDEBAR_TITLE = "⚙️ Model Configuration"
