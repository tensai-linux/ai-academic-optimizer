# Viva Preparation — 15 Questions & Answers

---

## Q1: What is the purpose of your project?

**Answer:** Our project is a domain-specific AI chatbot that helps students optimize their academic performance. It provides scientifically grounded advice on study planning, focus improvement, sleep optimization, and exam preparation. Unlike general-purpose AI, it's restricted to only these domains and produces structured, actionable outputs.

---

## Q2: Why did you restrict the chatbot to a specific domain?

**Answer:** Domain restriction serves two purposes. First, it improves output quality — the system prompt forces the model to stay within its area of expertise, producing more relevant and accurate advice. Second, it demonstrates prompt engineering skill — showing that we can control a general-purpose LLM's behavior through instructions alone, without fine-tuning.

---

## Q3: How does the domain restriction work technically?

**Answer:** The domain restriction is enforced through the **system prompt**. The system prompt explicitly lists the allowed domains (study planning, focus, sleep, exam prep) and includes a specific rejection message for off-topic queries. Since the system prompt is processed before every user query, the model follows these instructions consistently. The system prompt says: if the query is outside these domains, respond with a specific rejection message and redirect the user.

---

## Q4: What API are you using and how does it work?

**Answer:** We use the **OpenAI Chat Completions API**. It accepts a list of messages with roles (system, user, assistant) and returns a generated completion. The system message sets the AI's behavior, user messages contain queries, and assistant messages contain previous responses. We send this entire conversation context with each request, enabling multi-turn conversations.

**Code:**
```python
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[system_prompt, ...history, user_query],
    temperature=0.3,
    top_p=0.9
)
```

---

## Q5: What is Temperature and why did you choose 0.3?

**Answer:** Temperature controls randomness in the model's output. It scales the probability distribution before sampling — low temperature makes high-probability words more likely (deterministic), high temperature flattens the distribution (more random). We chose 0.3 because students need **reliable, structured advice**. Study plans should be consistent, not creative. But we didn't use 0.0 because that sounds too robotic — 0.3 adds enough variation for natural language.

---

## Q6: What is Top-p and why did you choose 0.9?

**Answer:** Top-p (nucleus sampling) limits the model's word choices to a subset that covers `p` proportion of the total probability mass. With top-p = 0.9, the model only considers words in the top 90% of probability, excluding rare, unlikely words. We chose 0.9 because it's broad enough for natural, fluent language but filters out noisy outliers. It's also the industry-standard default recommended by OpenAI.

---

## Q7: What happens when Temperature is 0.2 vs 0.8?

**Answer:** At **Temperature 0.2**, the output is highly deterministic — you get the same structured, textbook-style response every time. The language is clinical and precise. At **Temperature 0.8**, the model produces more varied responses — different word choices, creative suggestions (like "strategic procrastination"), and more conversational tone. The structure remains the same because our system prompt enforces it, but the creativity within that structure increases significantly.

---

## Q8: Explain your system prompt design.

**Answer:** Our system prompt has four sections:

1. **Role & Boundaries** — Defines the AI as "AcadeMind" and lists exactly which domains are allowed. Includes a specific rejection message for off-topic queries.
2. **Output Structure** — Mandates a 4-part format: 🎯 Goal → 📋 Recommendation → 🔬 Scientific Basis → ⚡ Quick Win.
3. **Behavioral Rules** — Be specific (exact numbers, not vague), be structured (numbered lists), be scientific (cite research), be concise.
4. **Tone** — Professional yet approachable, like an academic coach.

This is the most critical component — it transforms a general-purpose LLM into a specialized tool.

---

## Q9: Why did you choose Streamlit over Flask or React?

**Answer:** Streamlit was chosen for three reasons: (1) It has **built-in chat UI components** (`st.chat_input`, `st.chat_message`) that handle conversation display without custom HTML. (2) It has **native slider widgets** perfect for demonstrating temperature and top-p controls. (3) It provides **session state** for maintaining chat history without a database. For a prototype/demo, Streamlit lets us build a production-quality UI in a single Python file.

---

## Q10: How do you maintain conversation context?

**Answer:** We use Streamlit's `st.session_state` to store chat history as a list of dictionaries with `role` and `content` keys. Before each API call, we prepend the system prompt, append all previous messages, then add the new user query. This way, the model has full context of the conversation, enabling follow-up questions and personalized responses.

---

## Q11: What is the role of the system prompt vs the user prompt?

**Answer:** The **system prompt** sets the AI's behavior, personality, and constraints. It's like giving instructions to an employee before they start working. The **user prompt** is the actual query. The system prompt is sent with every request but is invisible to the user. It controls WHAT the AI can talk about and HOW it formats responses. The user prompt controls what specific topic to address.

---

## Q12: Can the domain restriction be bypassed?

**Answer:** In theory, advanced prompt injection attacks could attempt to override the system prompt. However, our implementation has two safeguards: (1) The system prompt explicitly lists rejection criteria, and (2) we use low temperature (0.3), which makes the model more likely to follow instructions deterministically. In practice, simple off-topic queries are reliably rejected. For a production system, we would add additional server-side keyword filtering.

---

## Q13: What are the limitations of your system?

**Answer:** Four main limitations: (1) **API dependency** — requires internet and a valid OpenAI API key. (2) **No persistent storage** — chat history is lost when the page refreshes. (3) **Cost** — each query costs API tokens. (4) **No personalization memory** — the system doesn't remember individual student profiles across sessions. These could be addressed with a database backend and user authentication in a production version.

---

## Q14: How is your chatbot different from just using ChatGPT?

**Answer:** Three key differences: (1) **Domain restriction** — ChatGPT answers anything; ours only answers academic optimization questions. (2) **Structured output** — ChatGPT gives freeform text; ours always follows Goal → Recommendation → Science → Quick Win format. (3) **Scientific grounding** — our system prompt forces every recommendation to cite cognitive science principles. This makes our output more reliable, consistent, and academically useful.

---

## Q15: What would you improve if you had more time?

**Answer:** Five improvements: (1) **Persistent user profiles** — remember study habits and track progress over time. (2) **Calendar integration** — auto-generate Google Calendar events from study plans. (3) **RAG (Retrieval-Augmented Generation)** — connect to a knowledge base of cognitive science papers for more accurate citations. (4) **Analytics dashboard** — visualize study patterns and chatbot usage. (5) **Fine-tuning** — train a custom model on academic coaching conversations for even better domain performance.
