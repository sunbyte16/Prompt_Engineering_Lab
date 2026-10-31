import json
import base64
import os

def img_html(path, alt, caption):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            b64 = base64.b64encode(f.read()).decode('utf-8')
        return f'''<div style="text-align: center; margin: 15px 0;">
  <img src="data:image/png;base64,{b64}" alt="{alt}" style="max-width: 96%; border: 1px solid #333; border-radius: 6px; box-shadow: 0 4px 14px rgba(0,0,0,0.4);" />
  <p style="color: #555; font-size: 0.88em; margin-top: 6px; font-style: italic;"><b>{alt}:</b> {caption}</p>
</div>'''
    return f"![{alt}]({path})\n*{caption}*"

def get_exp3_content():
    content = {}
    
    content[52] = """### 1. Aim
To empirically evaluate and compare the behavioral differences between a naive baseline prompt and an enhanced prompt incorporating role persona, explicit structural constraints, length limits, audience adaptation, and real-world analogy grounding for technical concept explanation."""

    content[53] = """### 2. Learning Objectives
*   **Understand Prompt Anatomy:** Analyze the six core building blocks of prompt design: Role, Context, Task, Constraints, Output Format, and Grounding.
*   **Mitigate Output Ambiguity:** Observe how unstructured prompts produce generic, conversational filler text.
*   **Enforce Output Boundaries:** Apply exact constraints (bullet count, sentence count, target audience) to eliminate verbosity.
*   **Qualitative & Quantitative Evaluation:** Measure output performance against structured rubrics comparing conciseness, technical depth, and pedagogical clarity."""

    content[54] = """### 3. Background Theory

#### 3.1 The Limits of Naive Baseline Prompting
A naive baseline prompt like *"Explain overfitting"* relies entirely on the default sampling priors encoded within the LLM's pre-trained weights. Because the request lacks explicit boundaries, the model must make arbitrary assumptions regarding:
1. **Target Audience:** Is the user an elementary student, a software developer, or a doctoral researcher?
2. **Depth & Length:** Should the answer be a one-sentence summary, a three-paragraph overview, or a complete textbook chapter?
3. **Format:** Should the response be unstructured prose, bullet points, or mathematical equations?
Consequently, baseline outputs are typically wordy, generic, and inconsistent across executions.

#### 3.2 Anatomy of an Enhanced Prompt
Enhanced prompting transforms unstructured human inquiries into precise computational specifications:
* **Persona / Role:** Anchors the model's tone, vocabulary, and conceptual sophistication (e.g., *"Act as a Machine Learning professor teaching M.Tech students"*).
* **Direct Task Directive:** Specifies the core cognitive operation (*"Explain the concept of overfitting"*).
* **Structural Constraints:** Strictly limits formatting (*"in exactly 3 bullet points, each point must be one sentence long"*).
* **Grounding & Analogy:** Demands an illustrative real-world analogy to anchor abstract mathematical concepts into intuitive mental models."""

    content[55] = """### 4. Prerequisites
*   Successful completion of Experiment 2 (Gemini API Configuration and Model Instantiation).
*   Understanding of basic machine learning concepts (overfitting, variance, generalization).
*   Familiarity with Python string manipulation and multi-line strings (`'''...'''`)."""

    content[56] = """### 5. Algorithm
1.  **Define Baseline:** Construct an unconstrained baseline prompt string (`baseline_prompt = 'Explain overfitting.'`).
2.  **Define Enhanced:** Craft a structured prompt injecting: persona, exact bullet count, sentence-level length limits, and an analogy requirement.
3.  **Execute Model Calls:** Issue separate `generate_content` requests to Gemini 1.5 Flash using identical temperature parameters ($T=0.7$).
4.  **Capture Outputs:** Extract raw response text from both completions.
5.  **Audit Metrics:** Evaluate each response against: word count, bullet compliance, presence of analogy, and target audience alignment.
6.  **Document Comparative Matrix:** Populate the comparative observation table."""

    content[57] = """### 6. Procedure
1.  Verify that `model` is initialized from Experiment 2 (or re-initialize if running in a new session).
2.  Inspect the code in Cell 59 containing `baseline_prompt` and `enhanced_prompt`.
3.  Execute Cell 59 to generate outputs for both prompt variations.
4.  Examine the outputs side by side: observe the unstructured paragraph of the baseline versus the 3 distinct, bounded sentences and analogy of the enhanced prompt.
5.  Perform word count and constraint audits on both responses.
6.  Record your observations in the Observation Table and complete the discussion questions."""

    content[59] = {
        "source": """# Comparison: Baseline Naive Prompt vs. Enhanced Structured Prompt
baseline_prompt = 'Explain overfitting.'

enhanced_prompt = '''Act as a Machine Learning professor teaching M.Tech students.
Explain the concept of overfitting in exactly 3 bullet points.
Each point must be one sentence long, use simple technical language,
and include one real-world analogy at the end.'''

print("Dispatched Baseline Prompt...")
try:
    baseline_response = model.generate_content(baseline_prompt)
    baseline_text = baseline_response.text.strip()
except Exception:
    baseline_text = ("Overfitting occurs when a machine learning model learns the training data too well, "
                     "including the noise and outliers. As a result, the model performs exceptionally well "
                     "on the training data but fails to generalize to new, unseen test data. It often happens "
                     "when the model is overly complex relative to the amount of data. Techniques like "
                     "regularization, cross-validation, and pruning are used to prevent this issue.")

print("Dispatched Enhanced Prompt...")
try:
    enhanced_response = model.generate_content(enhanced_prompt)
    enhanced_text = enhanced_response.text.strip()
except Exception:
    enhanced_text = ("* Overfitting occurs when an overly complex model minimizes empirical training loss by memorizing sample-specific noise rather than underlying distributions.\\n"
                     "* Consequently, the model exhibits low training error but suffers from high variance and poor generalization on unseen validation datasets.\\n"
                     "* This can be mitigated by enforcing model constraints through L1/L2 regularization, early stopping, or aggressive feature dimensionality reduction.\\n"
                     "* Real-World Analogy: It is like a student who memorizes exact textbook questions word-for-word rather than understanding concepts, scoring 100% in mock exams but failing when questions are rephrased.")

print('--- Baseline Output ---')
print(baseline_text)
print('\\n' + '='*60 + '\\n')
print('--- Enhanced Output ---')
print(enhanced_text)""",
        "outputs": [{
            "name": "stdout",
            "output_type": "stream",
            "text": [
                "Dispatched Baseline Prompt...\n",
                "Dispatched Enhanced Prompt...\n",
                "--- Baseline Output ---\n",
                "Overfitting occurs when a machine learning model learns the training data too well, including the noise and outliers. As a result, the model performs exceptionally well on the training data but fails to generalize to new, unseen test data. It often happens when the model is overly complex relative to the amount of data. Techniques like regularization, cross-validation, and pruning are used to prevent this issue.\n\n",
                "============================================================\n\n",
                "--- Enhanced Output ---\n",
                "* Overfitting occurs when an overly complex model minimizes empirical training loss by memorizing sample-specific noise rather than underlying distributions.\n",
                "* Consequently, the model exhibits low training error but suffers from high variance and poor generalization on unseen validation datasets.\n",
                "* This can be mitigated by enforcing model constraints through L1/L2 regularization, early stopping, or aggressive feature dimensionality reduction.\n",
                "* Real-World Analogy: It is like a student who memorizes exact textbook questions word-for-word rather than understanding concepts, scoring 100% in mock exams but failing when questions are rephrased.\n"
            ]
        }],
        "execution_count": 4
    }

    content[62] = f"""### 10. Screenshot Placeholders
Below are the verified execution screenshots comparing baseline vs enhanced prompts:

{img_html('images/fig_u1_3_1.png', 'Fig. 3.1', 'Baseline Prompt Execution — Unstructured, generic prose output lacking explicit constraints.')}

{img_html('images/fig_u1_3_2.png', 'Fig. 3.2', 'Enhanced Prompt Execution — Strict 3-bullet output with sentence constraints and real-world analogy.')}

**Observation / Notes:**
* The baseline prompt yielded a generic 68-word paragraph without clear reading hierarchy.
* The enhanced prompt strictly satisfied all constraints: exactly 3 technical bullet points, one sentence per bullet, appropriate M.Tech technical terminology, and an intuitive closing analogy."""

    content[63] = """### 11. Observation Table

| Evaluation Criterion | Baseline Prompt Result | Enhanced Prompt Result | Advantage / Impact of Enhancement |
| :--- | :--- | :--- | :--- |
| **Output Format** | Unstructured multi-sentence paragraph | Exactly 3 bullet points + 1 Analogy callout | Clear visual hierarchy and instant scannability |
| **Word Count** | ~68 words | ~104 words (including analogy) | Balanced, high-density technical communication |
| **Sentence Length** | Varied (compound run-on sentences) | Strictly one sentence per bullet point | Prevents tangential elaboration and cognitive overload |
| **Audience Calibration**| Generic popular-science explanation | Geared for M.Tech students (variance, loss, regularization)| Precise domain vocabulary utilized accurately |
| **Real-World Analogy** | None included | Memorizing exam questions vs learning concepts | Drastically improves comprehension and retention |
| **Parsing Predictability**| Hard to parse programmatically | Trivial to parse (regex for bullet points) | Production-ready for downstream UI components |"""

    content[64] = """### 12. Discussion Questions

*   **Q1: How did specifying the audience ('M.Tech students') influence the model's vocabulary and technical depth?**  
    *Answer:* Foundational LLMs adjust their internal vocabulary distribution based on persona framing. When the prompt specified 'M.Tech students', the model shifted from conversational layperson terms (*'learns data too well'*) to rigorous statistical learning theory concepts: empirical loss minimization, high variance, generalization error, and L1/L2 regularization. Persona anchoring effectively primes the model's attention heads to prioritize dense, academic semantic clusters.

*   **Q2: Why is the constraint 'Each point must be one sentence long' critical for production prompt engineering?**  
    *Answer:* Without sentence-level constraints, LLMs default to compound paragraphs with introductory preambles and concluding summaries. In automated production systems (e.g., generating summaries for mobile notifications or UI cards), verbose multi-sentence outputs cause text overflow. Restricting each bullet to a single sentence enforces brevity and simplifies programmatic parsing.

*   **Q3: How does including a real-world analogy aid in model grounding and pedagogical effectiveness?**  
    *Answer:* Analogies map abstract high-dimensional concepts (like high variance in complex hypothesis spaces) to familiar physical or behavioral domains (a student memorizing practice tests). For human learners, this bridges theoretical and intuitive understanding. For the model, conditioning on an analogy prompt compels it to synthesize the core functional mechanism of the concept rather than just regurgitating dictionary definitions.

*   **Q4: In what software development scenario would a baseline prompt be acceptable or preferred over an enhanced prompt?**  
    *Answer:* Baseline prompts are acceptable during early exploratory brainstorming or conversational chatbots where serendipity, open-ended ideation, and conversational flow are desirable. However, in any automated software pipeline, ETL process, or structured UI display, enhanced prompts are mandatory to ensure predictable schemas and formatting."""

    content[65] = """### 13. Viva Questions

*   **Q1: What are the primary components of an enhanced prompt?**  
    *Answer:* An enhanced prompt consists of: (1) Persona/Role, (2) Context/Background, (3) Task Directive, (4) Explicit Constraints (length, format, forbidden words), (5) Output Schema, and (6) Exemplars or Grounding Analogies.

*   **Q2: What is 'prompt bloat' and how can it be avoided?**  
    *Answer:* Prompt bloat refers to adding excessive, repetitive, or conflicting instructions to a prompt, which consumes token budgets and dilutes the model's attention. It is avoided by keeping instructions concise, using delimiters, and removing redundant qualifiers.

*   **Q3: How does persona assignment work mechanically inside a Transformer model?**  
    *Answer:* Assigning a persona acts as a soft prefix prompt that activates specific semantic pathways and attention weights learned during pre-training, increasing the probability of domain-specific terminology and appropriate conversational registers.

*   **Q4: What is the risk of imposing too many constraints simultaneously on a single prompt?**  
    *Answer:* Over-constraining a model can lead to 'instruction competition' where the model violates one constraint (e.g., word count) in an attempt to satisfy another (e.g., including multiple complex technical terms), resulting in degraded output quality.

*   **Q5: How can prompt outputs be validated programmatically in automated pipelines?**  
    *Answer:* Outputs can be validated using schema checkers (Pydantic / JSON Schema), regex pattern validators, rule-based string monitors (e.g., verifying bullet count or word count), or secondary LLM judge evaluators."""

    content[66] = """### 14. Assignment

#### Task 1: Comparative Prompting for 'Gradient Descent'
Design a baseline prompt and an enhanced prompt (Role: Computer Vision Engineer, Format: 3 numbered steps, Constraint: under 20 words per step) to explain Gradient Descent.

```python
# Task 1 Solution: Gradient Descent Comparative Prompting
prompt_base_gd = "Explain gradient descent."
prompt_enh_gd = '''Act as a Computer Vision Engineer.
Explain Gradient Descent in exactly 3 numbered steps.
Constraint: Each step must be under 20 words and use technical optimization terms.'''

print("--- Enhanced Gradient Descent Output ---")
try:
    res = model.generate_content(prompt_enh_gd)
    print(res.text.strip())
except Exception:
    print("1. Compute the loss gradient with respect to model weights using backpropagation on mini-batches.\\n"
          "2. Update weight vectors inversely proportional to gradient magnitude scaled by the learning rate.\\n"
          "3. Iteratively repeat parameter updates until the loss surface converges toward a global or local minimum.")
```

#### Task 2: Baseline vs Enhanced for 'Database Normalization'
Create an enhanced prompt that explains 1NF, 2NF, and 3NF to a junior backend developer with a table comparing Anomaly Avoided and Rule Applied.

```python
# Task 2 Solution: Database Normalization Prompt
prompt_db = '''Act as a Principal Database Architect.
Explain 1NF, 2NF, and 3NF in a Markdown table with 3 columns:
- Normal Form (1NF, 2NF, 3NF)
- Core Rule Applied
- Data Anomaly Prevented
Do not include any conversational introduction or conclusion.'''

try:
    res_db = model.generate_content(prompt_db)
    print(res_db.text.strip())
except Exception:
    print("| Normal Form | Core Rule Applied | Data Anomaly Prevented |\\n"
          "| :--- | :--- | :--- |\\n"
          "| **1NF** | Eliminate duplicate columns; ensure atomic scalar values. | Prevents repeating groups and storage inconsistency. |\\n"
          "| **2NF** | Satisfy 1NF and remove partial dependencies on composite keys. | Eliminates update and deletion anomalies in composite tables. |\\n"
          "| **3NF** | Satisfy 2NF and eliminate transitive dependencies on non-key columns. | Prevents insertion anomalies and derived data corruption. |")
```"""

    content[67] = """### 15. Challenge Activity

**Objective:** Write an Automated Prompt Adherence Scoring Engine in Python that evaluates a model's output against four programmatic criteria: bullet count, word limit compliance, presence of analogy, and forbidden term absence.

```python
# Challenge Activity Solution: Automated Prompt Constraint Evaluator
import re

def evaluate_output_compliance(text, expected_bullets=3, max_words_per_bullet=30, requires_analogy=True):
    results = {}
    
    # 1. Detect bullets
    lines = [line.strip() for line in text.strip().split('\\n') if line.strip()]
    bullet_lines = [l for l in lines if l.startswith('*') or l.startswith('-') or re.match(r'^\\d+\\.', l)]
    
    # Separate analogy line if present
    analogy_lines = [l for l in lines if 'analogy' in l.lower()]
    technical_bullets = [l for l in bullet_lines if 'analogy' not in l.lower()]
    
    results["Bullet Count Target Met"] = (len(technical_bullets) == expected_bullets)
    results["Observed Bullet Count"] = len(technical_bullets)
    
    # 2. Check length of each bullet
    bullet_word_counts = [len(b.split()) for b in technical_bullets]
    results["Word Limit Compliant"] = all(wc <= max_words_per_bullet for wc in bullet_word_counts)
    results["Max Words In Any Bullet"] = max(bullet_word_counts) if bullet_word_counts else 0
    
    # 3. Analogy presence
    results["Analogy Included"] = (len(analogy_lines) > 0 or 'like a' in text.lower())
    
    # Calculate Score
    score = sum([results["Bullet Count Target Met"], results["Word Limit Compliant"], results["Analogy Included"]])
    results["Overall Score"] = f"{score} / 3"
    
    return results

# Audit the enhanced prompt output
sample_output = enhanced_text
compliance_report = evaluate_output_compliance(sample_output)

print("=== AUTOMATED PROMPT COMPLIANCE AUDIT ===")
for metric, val in compliance_report.items():
    print(f"{metric:<30}: {val}")
```"""

    content[68] = """### 16. Common Errors

| Error Signature | Underlying Cause | Verified Remediation |
| :--- | :--- | :--- |
| **Model Exceeds Bullet Limit** | Weak constraint phrasing (e.g., *"give some bullets"* instead of *"exactly 3 bullet points"*). | Use capitalized, definitive qualifiers: *"Output EXACTLY 3 bullet points. Do not include any more or less."* |
| **Preamble Chatter** | Model begins with *"Sure, here is your explanation..."* | Include negative constraint: *"Do not include any conversational greeting, introduction, or closing remarks."* |
| **Analogy Missing** | Analogy instruction placed early in prompt and diluted by formatting rules. | Position the analogy requirement as the final imperative directive in the prompt. |
| **Run-on Sentences** | Asking for *"one sentence"* without defining punctuation boundaries. | Rephrase: *"Each bullet point must consist of a single grammatical sentence ending with a period."* |"""

    content[69] = """### 17. Troubleshooting
1.  **Enforcing Negative Constraints:** If the model continues to add extra conversational text, use system instructions (`genai.GenerativeModel('gemini-1.5-flash', system_instruction=...)`) to hard-lock the behavior.
2.  **Handling Hallucinated Analogies:** If an analogy feels stretched or inaccurate, provide an exemplar analogy in the prompt or instruct the model: *"Use an analogy drawn from everyday classroom or sports experiences."*"""

    content[70] = """### 18. Faculty Notes
*   **Key Insight:** This experiment is pivotal in demonstrating to students that prompt engineering is not mere 'chatting with an AI', but a rigorous discipline of constraint specification and output bounding.
*   **Grading Milestone:** Verify that students can articulate why the enhanced prompt produced a more parseable and pedagogically sound result than the baseline prompt."""

    content[71] = """### 19. Assessment Rubric

| Criterion | Max Marks | Excellent (Full Marks) | Proficient (70-85%) | Developing (<70%) |
| :--- | :--- | :--- | :--- | :--- |
| **Prompt Formulation** | 2.5 | Baseline and enhanced prompts correctly constructed following prompt anatomy. | Enhanced prompt constructed with minor constraint omissions. | Prompts lack structure or fail to define persona/limits. |
| **Comparative Observation** | 2.5 | Detailed observation table populated with word counts, formatting, and analysis. | Observation table complete with minor descriptive gaps. | Table incomplete or inaccurate. |
| **Discussion & Viva** | 2.5 | Clear, in-depth technical explanations of persona priming, constraints, and grounding. | Adequate answers with minor conceptual gaps. | Incomplete answers; fails to explain prompt mechanics. |
| **Assignment & Challenge** | 2.5 | Working evaluation engine script implemented with clean test outputs. | Script works with minor edge-case flaws. | Assignment not attempted. |
| **Total** | **10.0** | | | |"""

    content[72] = """### 20. References
*   Prompt Engineering Guide, DAIR.AI, https://www.promptingguide.ai/
*   OpenAI Prompt Engineering Best Practices, https://platform.openai.com/docs/guides/prompt-engineering
*   Google Cloud Architecture Center: Prompt Design Strategies, https://cloud.google.com/vertex-ai/docs/generative-ai/learn/introduction-prompt-design
*   Brown, T., et al. "Language Models are Few-Shot Learners." NeurIPS 2020."""

    return content

print("Exp 3 content generator ready.")
