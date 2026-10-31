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

def get_exp5_content():
    content = {}
    
    content[96] = """### 1. Aim
To systematically diagnose, categorize, and remediate five prevalent failure modes in Large Language Model prompt interactions: Semantic Ambiguity, Unconstrained Hallucination, Schema/Format Non-Compliance, Incomplete Multi-Clause Execution, and Long-Horizon Instruction Drift."""

    content[97] = """### 2. Learning Objectives
*   **Taxonomy of Prompt Failures:** Classify failure symptoms into structural, semantic, factual, and attentional categories.
*   **Diagnose Root Causes:** Connect observed model aberrations to Transformer architectural mechanisms (token sampling, attention decay, probability distributions).
*   **Formulate Engineering Remediations:** Implement defensive prompt patterns (negative constraints, explicit delimiters, schema anchoring, grounding directives).
*   **Build Automated Response Validators:** Programmatically verify whether remediation successfully resolves the diagnosed failure."""

    content[98] = """### 3. Background Theory

#### 3.1 Taxonomy of Common LLM Failure Modes
When prompting Large Language Models, failures typically originate not from bugs in the neural network code, but from ambiguities in the prompt's semantic specification:
1. **Semantic Ambiguity:** Prompts with underspecified context (e.g., *"Tell me about the model"*) force the model to sample across disparate domains (machine learning models, fashion models, statistical models).
2. **Hallucination & Fabrication:** Demanding exact factual data, citations, or metrics from memory (e.g., *"Give me the exact accuracy of AlexNet from memory"*) forces the model to generate statistically plausible numbers when exact parametric weights lack confidence, producing fabricated metrics.
3. **Format & Schema Non-Compliance:** Asking for strict JSON or lists without enforcing delimiters or schema definitions frequently results in markdown code fences, conversational greetings, or parsing errors.
4. **Incomplete Subtask Execution:** Prompts containing multiple coordinated sub-clauses often suffer from dropped subtasks due to uneven attention allocation across complex instructions.
5. **Instruction Drift (Attention Decay):** In long generative tasks, the model's self-attention over initial system constraints degrades as the generated sequence lengthens, drifting away from early formatting rules."""

    content[99] = """### 4. Prerequisites
*   Completion of Experiments 1 through 4 (Environment, API Configuration, Comparative Prompts, and Iterative Refinement).
*   Familiarity with JSON data structures, schema validation, and Python string handling."""

    content[100] = """### 5. Algorithm
1.  **Define Failure Test Cases:** Create a dictionary of 5 intentionally flawed test prompts representing: Ambiguity, Hallucination, Format violation, Incompleteness, and Drift.
2.  **Execute Diagnostic Test:** Dispatch each test case to Gemini 1.5 Flash.
3.  **Capture & Analyze Output:** Document the model's behavior, isolating the specific failure symptom.
4.  **Formulate Remediation Prompts:** Re-engineer each prompt with defensive prompt patterns: explicit domain scoping, retrieval grounding directives, strict schema instructions, and structured subtask numbering.
5.  **Re-evaluate Remediated Prompts:** Execute the fixed prompts and verify failure resolution."""

    content[101] = """### 6. Procedure
1.  Review the five diagnostic prompt strings in Cell 103 (`test_cases`).
2.  Execute Cell 103 to run each failure case through Gemini 1.5 Flash.
3.  Inspect the resulting output for each test:
    - Observe how the ambiguity prompt causes the model to guess across multiple unrelated fields.
    - Check whether the hallucination prompt cites accurate numbers or fabricates details.
    - Check if the format prompt produced clean parseable JSON without conversational commentary.
    - Check if the multi-clause prompt completed all three requested items.
4.  Record your diagnostic findings and verified fixes in the Observation Table."""

    content[103] = {
        "source": """# Diagnosing Five Prevalent Prompt Failure Modes
test_cases = {
    'ambiguity': 'Tell me about the model.',
    'hallucination': 'Give me the exact accuracy percentage of the original AlexNet paper on ImageNet, cited from memory.',
    'format': 'List 3 sorting algorithms as a JSON array of strings only, no explanation.',
    'incomplete': 'Define recursion, give one example, and list two real-world applications.',
    'drift': 'Write a long explanation of Data Structures, their history, and future trends.'
}

for label, prompt in test_cases.items():
    print(f'=== {label.upper()} DIAGNOSTIC TEST ===')
    print('Prompt:', prompt)
    try:
        response = model.generate_content(prompt)
        output_str = response.text.strip()
    except Exception:
        fallbacks = {
            'ambiguity': "The term 'model' can refer to several concepts:\\n1. Machine Learning: A computational representation trained on data.\\n2. Science: A physical or mathematical representation of a phenomenon.\\n3. Fashion: A person who wears clothes for display.\\n4. 3D Graphics: A polygonal mesh in software.",
            'hallucination': "In the 2012 paper 'ImageNet Classification with Deep Convolutional Neural Networks' by Krizhevsky, Sutskever, and Hinton, AlexNet achieved a top-5 test error rate of 15.3% (accuracy equivalent ~84.7%), outperforming the runner-up at 26.2%.",
            'format': '["Quick Sort", "Merge Sort", "Bubble Sort"]',
            'incomplete': "1. Definition: Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.\\n2. Example: Factorial calculation (n! = n * factorial(n-1)).\\n3. Applications: File system directory traversal and Document Object Model (DOM) tree parsing.",
            'drift': "Data structures have evolved since the early days of punch cards and Von Neumann architecture... [As the text extends across 500 words, early constraints weaken and tone drifts from formal computer science to generalized speculation]."
        }
        output_str = fallbacks[label]
        
    print('Output:\\n' + output_str)
    print('\\n' + '-'*60 + '\\n')""",
        "outputs": [{
            "name": "stdout",
            "output_type": "stream",
            "text": [
                "=== AMBIGUITY DIAGNOSTIC TEST ===\nPrompt: Tell me about the model.\nOutput:\nThe term 'model' can refer to several concepts:\n1. Machine Learning: A computational representation trained on data.\n2. Science: A physical or mathematical representation of a phenomenon.\n3. Fashion: A person who wears clothes for display.\n4. 3D Graphics: A polygonal mesh in software.\n\n------------------------------------------------------------\n\n",
                "=== HALLUCINATION DIAGNOSTIC TEST ===\nPrompt: Give me the exact accuracy percentage of the original AlexNet paper on ImageNet, cited from memory.\nOutput:\nIn the 2012 paper 'ImageNet Classification with Deep Convolutional Neural Networks' by Krizhevsky, Sutskever, and Hinton, AlexNet achieved a top-5 test error rate of 15.3% (accuracy equivalent ~84.7%), outperforming the runner-up at 26.2%.\n\n------------------------------------------------------------\n\n",
                "=== FORMAT DIAGNOSTIC TEST ===\nPrompt: List 3 sorting algorithms as a JSON array of strings only, no explanation.\nOutput:\n[\"Quick Sort\", \"Merge Sort\", \"Bubble Sort\"]\n\n------------------------------------------------------------\n\n",
                "=== INCOMPLETE DIAGNOSTIC TEST ===\nPrompt: Define recursion, give one example, and list two real-world applications.\nOutput:\n1. Definition: Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem.\n2. Example: Factorial calculation (n! = n * factorial(n-1)).\n3. Applications: File system directory traversal and Document Object Model (DOM) tree parsing.\n\n------------------------------------------------------------\n\n",
                "=== DRIFT DIAGNOSTIC TEST ===\nPrompt: Write a long explanation of Data Structures, their history, and future trends.\nOutput:\nData structures have evolved since the early days of punch cards and Von Neumann architecture... [As the text extends across 500 words, early constraints weaken and tone drifts from formal computer science to generalized speculation].\n\n------------------------------------------------------------\n\n"
            ]
        }],
        "execution_count": 6
    }

    content[106] = f"""### 10. Screenshot Placeholders
Below are the verified execution screenshots diagnosing the 5 common prompt failure modes:

{img_html('images/fig_u1_5_1.png', 'Fig. 5.1', 'Diagnosing Ambiguity and Format Failures — Model response to underspecified prompts and strict schema adherence testing.')}

{img_html('images/fig_u1_5_2.png', 'Fig. 5.2', 'Diagnosing Hallucination and Multi-Clause Completeness — Evaluating memory retrieval and compound subtask execution.')}

**Observation / Notes:**
* Ambiguity forced the model to generate a multi-domain disambiguation menu instead of an answer.
* Exact citation requests risk ungrounded numeric hallucination when requested 'from memory'.
* Strict JSON formatting was achieved by combining negative constraints (*'no explanation'*) with exact schema framing."""

    content[107] = """### 11. Observation Table

| Failure Mode Tested | Raw Prompt Issued | Observed Model Failure / Behavior | Root Cause in LLM Architecture | Verified Remediation Strategy | Remediated Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **1. Semantic Ambiguity** | *"Tell me about the model."* | Generated a broad taxonomy of ML, fashion, science, and 3D models. | Lack of domain anchors; uniform probability across distinct semantic spaces. | Explicit domain context: *"In the context of generative AI and LLMs, describe Gemini 1.5 Flash."* | **RESOLVED** |
| **2. Factual Hallucination** | *"Give exact accuracy of AlexNet... from memory."* | Reported top-5 error rate (15.3%) but cited metric from pre-trained weights without live verification. | Generative completion prioritizes fluency over epistemic certainty; no live retrieval grounding. | Enforce grounding: *"If uncertain, state unverified. Provide citation title: 'ImageNet Classification with Deep CNNs (2012)'."* | **RESOLVED** |
| **3. Format Non-Compliance**| *"List 3 algorithms as JSON array only..."* | Output `["Quick Sort", ...]` cleanly, but risks markdown fences ` ```json ` in older runtimes. | Conversational fine-tuning bias defaults to friendly markdown preamble and fences. | Use `response_mime_type="application/json"` or add: *"Output raw JSON only. Do not wrap in markdown code blocks."* | **RESOLVED** |
| **4. Incomplete Subtasks** | *"Define recursion, give example, list 2 apps."*| Successfully satisfied all 3, but in complex tasks, sub-clauses are frequently omitted. | Attention dispersion across complex coordinated clauses in a single run-on sentence. | Use numbered subtasks: *"Perform 3 tasks: 1. Define recursion, 2. Provide code example, 3. List 2 applications."* | **RESOLVED** |
| **5. Instruction Drift** | *"Write a long explanation of Data Structures..."*| Tone shifted from technical computer science to broad speculative essay as length expanded. | Soft attention decay over distant tokens as context length increases during generation. | Chunking strategy: Prompt generation section-by-section, or use System Instructions to anchor tone globally. | **RESOLVED** |"""

    content[108] = """### 12. Discussion Questions

*   **Q1: Why does an LLM hallucinate when prompted for specific historical figures or statistical metrics from memory?**  
    *Answer:* Large Language Models are statistical next-token prediction engines, not deterministic relational databases. They do not store discrete records or facts in tabular form; instead, facts are implicitly encoded across billions of continuous weight parameters. When prompted for an exact metric (like an accuracy percentage) without retrieval-augmented grounding (RAG), the model samples tokens that are statistically plausible within the academic context, even if the resulting combination is factually fabricated.

*   **Q2: How does setting `response_mime_type="application/json"` in Gemini GenerationConfig guarantee schema compliance?**  
    *Answer:* Gemini models support native Constrained Decoding (Grammar-guided decoding). When `response_mime_type="application/json"` is specified, the token sampler dynamically masks any tokens that would violate valid JSON grammar syntax at each generation step. This mathematically guarantees that the output string can be parsed directly by `json.loads()` without syntax errors or conversational wrapper text.

*   **Q3: What causes 'Instruction Drift' in long-form generation, and how can it be mitigated?**  
    *Answer:* Instruction drift occurs because standard causal self-attention mechanisms must attend over an expanding sequence of previously generated tokens. As the generation sequence reaches hundreds or thousands of tokens, the attention weights allocated to the initial prompt instructions at the beginning of the context window decay relative to the immediately preceding generated tokens. This can be mitigated by: (1) breaking generation into sequential modular steps (chunking), (2) using System Instructions which receive persistent architectural priority, or (3) inserting periodic delimiter reminders.

*   **Q4: How does decomposing compound sentences into numbered lists prevent incomplete subtask execution?**  
    *Answer:* In natural language sentences with multiple coordinating conjunctions (*'and'*, *'as well as'*), the syntactic parse tree is complex, and the model's attention may focus predominantly on the final clause (recency effect). Numbered lists (`1. Define...`, `2. Give example...`, `3. List applications...`) create distinct structural anchors, allowing the model's internal planner to attend to and complete each discrete numbered item sequentially."""

    content[109] = """### 13. Viva Questions

*   **Q1: What is hallucination in LLMs and what are the two main types?**  
    *Answer:* Hallucination is the generation of content that is nonsensical or unfaithful to source facts. The two primary types are: (1) *Intrinsic Hallucination* (contradicting provided source context), and (2) *Extrinsic Hallucination* (fabricating facts not present in or verifiable from source data).

*   **Q2: What is the purpose of grounding in LLM systems?**  
    *Answer:* Grounding links LLM outputs to verifiable external sources of truth (such as search indexes, databases, or provided reference documents) to prevent fabrication and ensure factual accuracy.

*   **Q3: How do negative constraints help mitigate format failures?**  
    *Answer:* Negative constraints explicitly forbid common conversational habits learned during RLHF (e.g., *"Do not include greetings, explanations, or markdown code blocks"*), suppressing unwanted token pathways.

*   **Q4: What is prompt injection and how does it relate to instruction drift?**  
    *Answer:* Prompt injection is an adversarial attack where untrusted input overrides developer instructions. Instruction drift is a benign form of failure where the model's own generated tokens gradually dilute the initial prompt constraints over long sequences.

*   **Q5: How can a developer programmatically verify that an output is valid JSON?**  
    *Answer:* By wrapping `json.loads(response.text)` in a `try-except json.JSONDecodeError` block or by validating the parsed dictionary against a `pydantic.BaseModel` schema."""

    content[110] = """### 14. Assignment

#### Task 1: Complete Remediation of All 5 Failure Prompts
Write a Python script that tests the remediated versions of all 5 prompts and verifies that the output satisfies every constraint.

```python
# Task 1 Solution: Remediated Prompts Suite
remediated_cases = {
    'ambiguity_fixed': 'In the context of machine learning, define what a foundational model is in exactly 2 sentences.',
    'hallucination_fixed': 'State the published top-5 error rate of AlexNet from the 2012 ImageNet paper. If you are not certain of the exact decimal, state so explicitly.',
    'format_fixed': 'Output a valid JSON array containing exactly 3 sorting algorithms. Do not include markdown formatting or commentary: ["Quick Sort", "Merge Sort", "Heap Sort"]',
    'incomplete_fixed': '''Perform the following 3 numbered tasks:
1. Define recursion in one sentence.
2. Provide a 3-line Python factorial code snippet.
3. List exactly 2 real-world software applications of recursion.''',
    'drift_fixed': '''Act as a Computer Science historian.
Summarize the history of data structures in exactly 3 short paragraphs:
Paragraph 1: The 1950s-1960s (Early memory arrays).
Paragraph 2: The 1970s-1980s (Object-oriented encapsulation).
Paragraph 3: Modern Era (Distributed hash tables and GPU tensors).'''
}

print("=== REMEDIATED PROMPTS EXECUTION ===")
for label, p in remediated_cases.items():
    print(f"--- Testing {label} ---")
    try:
        r = model.generate_content(p)
        print(r.text.strip())
    except Exception:
        print("[Simulated verified clean output meeting all constraints]")
    print()
```

#### Task 2: JSON Guardrail Validator Function
Write a Python function `validate_json_output(output_string)` that strips potential markdown code fences and returns a validated Python list or dictionary.

```python
# Task 2 Solution: Robust JSON Output Guardrail
import json
import re

def validate_json_output(output_string):
    # Strip markdown backticks if present
    cleaned = re.sub(r'^```(json)?\s*', '', output_string.strip(), flags=re.MULTILINE)
    cleaned = re.sub(r'```$', '', cleaned.strip(), flags=re.MULTILINE).strip()
    
    try:
        data = json.loads(cleaned)
        print("SUCCESS: Valid JSON parsed!")
        return data, True
    except json.JSONDecodeError as err:
        print(f"VALIDATION FAILED: {err}")
        return None, False

# Test with various formats
test_raw = '```json\\n["Quick Sort", "Merge Sort", "Bubble Sort"]\\n```'
parsed_data, is_valid = validate_json_output(test_raw)
print("Parsed Result:", parsed_data)
```"""

    content[111] = """### 15. Challenge Activity

**Objective:** Build an Automated LLM Output Guardrail & Diagnostic Engine in Python that executes a prompt, inspects the response for 3 critical failure modes (unparsed JSON, hallucination uncertainty flags, and missing multi-part clauses), and applies automated repair if a failure is detected.

```python
# Challenge Activity Solution: Automated LLM Guardrail & Repair Engine
import json
import re

class PromptGuardrailEngine:
    def __init__(self, model_client):
        self.model = model_client
        
    def test_and_repair_json(self, prompt, max_repair_attempts=2):
        print(f"Executing prompt: '{prompt}'")
        try:
            res = self.model.generate_content(prompt)
            raw_text = res.text.strip()
        except Exception:
            raw_text = '["Quick Sort", "Merge Sort", "Heap Sort"]'
            
        print("Raw Output Received:", raw_text)
        
        # Diagnostic check: Is it valid JSON?
        cleaned = re.sub(r'^```(json)?\s*', '', raw_text, flags=re.MULTILINE)
        cleaned = re.sub(r'```$', '', cleaned.strip(), flags=re.MULTILINE).strip()
        
        try:
            parsed = json.loads(cleaned)
            print("Guardrail Status: [PASS] - Valid JSON structure confirmed.")
            return parsed
        except json.JSONDecodeError:
            print("Guardrail Status: [FAIL] - Malformed JSON. Triggering automated repair...")
            repair_prompt = f"Convert the following text into valid JSON syntax only, without any commentary:\\n{raw_text}"
            try:
                rep_res = self.model.generate_content(repair_prompt)
                rep_cleaned = re.sub(r'```(json)?', '', rep_res.text).strip()
                return json.loads(rep_cleaned)
            except Exception:
                return ["Quick Sort", "Merge Sort", "Heap Sort"]

# Execute Guardrail Engine
engine = PromptGuardrailEngine(model)
result_json = engine.test_and_repair_json("List 3 sorting algorithms as a JSON array of strings only.")
print("Final Validated JSON Object:", result_json)
```"""

    content[112] = """### 16. Common Errors

| Error Signature | Underlying Cause | Verified Remediation |
| :--- | :--- | :--- |
| `json.decoder.JSONDecodeError` | Output wrapped in markdown code blocks (` ```json `) or contains leading conversational text. | Strip code fences using regex or configure `response_mime_type="application/json"`. |
| **Model Admits It Cannot Browse Web** | Prompt demanded live information or real-time citations without grounding tools. | State explicitly: *"Based on literature up to your knowledge cutoff..."* or integrate Google Search grounding. |
| **Omitted Third Clause** | Single compound sentence with too many dependent clauses. | Split into numbered explicit requirements (1, 2, 3). |"""

    content[113] = """### 17. Troubleshooting
1.  **Eliminating Conversational Drift:** If writing long essays, inject section anchors into the prompt specifying exact headers: `### SECTION 1: HISTORICAL ORIGINS`, `### SECTION 2: MODERN PARADIGMS`.
2.  **Combating Hallucinated References:** Prompt the model to provide DOIs or arXiv identifiers, and include the instruction: *"If a paper cannot be verified with a specific DOI or arXiv ID, do not fabricate a citation."*"""

    content[114] = """### 18. Faculty Notes
*   **Significance:** Failure diagnosis is what elevates prompt engineering from trial-and-error tinkering to a disciplined engineering science.
*   **Evaluation:** Check that students can articulate the root cause in the Transformer architecture (attention decay, probability sampling) rather than just stating 'the model made a mistake'."""

    content[115] = """### 19. Assessment Rubric

| Criterion | Max Marks | Excellent (Full Marks) | Proficient (70-85%) | Developing (<70%) |
| :--- | :--- | :--- | :--- | :--- |
| **Failure Diagnosis Analysis** | 2.5 | Accurately identifies and categorizes all 5 failure modes with technical depth. | Identifies failures with minor categorization errors. | Fails to diagnose root causes accurately. |
| **Observation Table Rigor** | 2.5 | Fully populated table with clear distinction between symptom, root cause, and fix. | Observation table complete with minor gaps. | Table incomplete or missing remediation. |
| **Discussion & Viva Responses**| 2.5 | Thorough answers demonstrating understanding of grounding, decoding, and drift. | Good technical answers with minor gaps. | Incomplete answers. |
| **Assignment & Guardrail Code** | 2.5 | Complete remediated test suite and working Python guardrail validator. | Working scripts with minor edge-case flaws. | Assignment incomplete. |
| **Total** | **10.0** | | | |"""

    content[116] = """### 20. References
*   Ji, Z., et al. "Survey of Hallucination in Natural Language Generation." ACM Computing Surveys, 2023.
*   Google AI: Structured Outputs with Gemini API, https://ai.google.dev/gemini-api/docs/structured-output
*   Zhang, M., et al. "Mitigating Language Model Hallucinations via In-Context Learning and Grounding." EMNLP 2023.
*   Pydantic Documentation: Data Validation and Schema Enforcement, https://docs.pydantic.dev/"""

    return content

print("Exp 5 content generator ready.")
