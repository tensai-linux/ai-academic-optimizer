# Model Configuration Justification

## 1. What is Temperature?

**Temperature** controls the **randomness** of the model's output.

- **Low (0.1–0.3):** Focused, deterministic, consistent
- **High (0.7–1.0):** Creative, varied, sometimes surprising

**Analogy:** "Temperature is like a focus dial. At 0.2, the model always gives the textbook answer. At 0.8, it gives creative but less predictable answers."

**Formula:**
```
P(word_i) = exp(logit_i / T) / Σ exp(logit_j / T)
```
- T → 0: Always picks the most likely word (argmax)
- T → ∞: All words equally likely (uniform)

---

## 2. What is Top-p (Nucleus Sampling)?

**Top-p** controls **how many words** the model considers.

1. Sort all possible next words by probability
2. Add probabilities until reaching threshold `p`
3. Sample ONLY from this "nucleus"

**Example:** `top_p = 0.9` → considers words covering 90% of probability mass.

**Analogy:** "Top-p is like choosing from a shortlist. 0.9 means the model picks from its top candidates covering 90% confidence."

---

## 3. Temperature vs Top-p

| Feature | Temperature | Top-p |
|---------|------------|-------|
| Controls | Distribution shape | Candidate pool size |
| Low value | Deterministic | Restrictive |
| High value | Random | Permissive |

**OpenAI recommends:** Adjust one at a time. We fix `top_p=0.9` and vary `temperature`.

---

## 4. Why Temperature ≈ 0.3 and Top-p ≈ 0.9

### Temperature = 0.3:
- Students need **reliable, consistent** advice
- Study plans require **deterministic formatting**
- Reduces **hallucination risk**
- Not 0.0 — some variation keeps responses natural

### Top-p = 0.9:
- Broad enough for **natural language**
- Excludes bottom 10% noisy words
- Industry standard default

### Why not other values?

| Config | Problem |
|--------|---------|
| Temp=0.0, Top-p=1.0 | Too robotic |
| Temp=0.8, Top-p=0.9 | Too creative for study advice |
| Temp=0.3, Top-p=0.5 | Too restrictive |
| **Temp=0.3, Top-p=0.9** | **✅ Optimal balance** |

---

## 5. Quick Reference

| Parameter | Value | Effect |
|-----------|-------|--------|
| Temperature | 0.3 | Focused, structured output |
| Top-p | 0.9 | Natural vocabulary diversity |
| Max Tokens | 1024 | Detailed responses |
| Model | gpt-3.5-turbo | Cost-effective, fast |

---

## 6. Viva One-Liners

- **"What is temperature?"** → Controls randomness. Low = focused, high = creative.
- **"What is top-p?"** → Limits word choices. 0.9 = top 90% of candidates.
- **"Why 0.3?"** → Students need reliable plans, not creative fiction.
- **"Why not 0?"** → Sounds robotic. 0.3 adds natural variation.
- **"Why 0.9 top-p?"** → Broad enough for natural language, excludes noise.
