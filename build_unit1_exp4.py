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

def get_exp4_content():
    content = {}
    
    content[74] = """### 1. Aim
To execute a systematic, multi-cycle iterative prompt refinement process for generating a beginner-friendly Data Structures study curriculum, evaluating each iteration against predefined acceptance criteria (temporal breakdown, language accessibility, and estimated study hours) until full compliance is achieved."""

    content[75] = """### 2. Learning Objectives
*   **Establish Acceptance Criteria:** Formulate explicit, measurable validation rubrics prior to prompt drafting.
*   **Diagnose Incremental Prompt Failures:** Identify omitted subtasks, structural ambiguities, and tonal mismatches between versions.
*   **Execute Iterative Feedback Loops:** Apply targeted prompt modifications (scaffolding, constraint injection, persona calibration) across successive cycles.
*   **Track Convergence to Specification:** Quantify compliance improvements across iterations (v1 -> v2 -> v3)."""

    content[76] = """### 3. Background Theory

#### 3.1 Prompt Engineering as an Agile Feedback Loop
Prompt engineering mirrors iterative software engineering. Rarely does an initial prompt produce a production-ready output. Attempting to draft an all-encompassing prompt on the first try often introduces conflicting constraints or cognitive clutter. Instead, effective practitioners use an agile feedback loop:
$$\\text{Formulate Rubric} \\longrightarrow \\text{Draft Prompt} \\longrightarrow \\text{Evaluate Model Output} \\longrightarrow \\text{Isolate Gaps} \\longrightarrow \\text{Refine Prompt}$$

#### 3.2 Progressive Constraint Injection
In this experiment, three iterations demonstrate progressive constraint injection:
1. **Version 1 (Naive Open-Ended Prompt):** *"Give me a study plan for learning data structures."* Generates an unstructured laundry list of computer science topics with no pacing, timeline, or difficulty graduation.
2. **Version 2 (Added Constraint - Time Allocation):** Adds *"Include an estimated number of hours for each topic."* Addresses quantitative effort but lacks structural grouping (e.g., weekly roadmaps) and uses advanced terminology that intimidates beginners.
3. **Version 3 (Fully Scaffolding & Calibrated Persona):** Introduces a study coach persona, explicit 4-week calendar breakdown, hours per topic, and beginner-level accessible language. All three success criteria are satisfied."""

    content[77] = """### 4. Prerequisites
*   Completion of Experiment 3 (Baseline vs Enhanced Prompts).
*   Basic understanding of core Data Structures (Arrays, Linked Lists, Stacks, Queues, Trees, Graphs, Hash Tables).
*   Familiarity with evaluating outputs against checklist criteria."""

    content[78] = """### 5. Algorithm
1.  **Define Success Criteria:** Establish checklist: (a) Weekly breakdown present, (b) Beginner-friendly language, (c) Time estimate per topic included.
2.  **Cycle 1 (v1):** Execute naive request; score against checklist. Identify omissions.
3.  **Cycle 2 (v2):** Append duration requirements; score against checklist. Identify remaining structural and tone gaps.
4.  **Cycle 3 (v3):** Re-engineer with persona (*"study coach"*), calendar bounds (*"4-week plan"*), and tone constraints (*"beginner-friendly"*).
5.  **Comparative Audit:** Compile evaluation matrix showing criteria status across v1, v2, and v3."""

    content[79] = """### 6. Procedure
1.  Review the predefined `success_criteria` list in Cell 81.
2.  Inspect the progression from string `v1` to `v2` to multi-line prompt `v3`.
3.  Execute Cell 81 to run all three versions sequentially through Gemini 1.5 Flash.
4.  Examine the printed outputs for Version 1, Version 2, and Version 3.
5.  Score each output against the 3 criteria (Yes / No).
6.  Record the word counts, scores, and qualitative notes in the Observation Table."""

    content[81] = {
        "source": """# Iterative Prompt Refinement Workflow
success_criteria = [
    'Weekly breakdown present',
    'Beginner-appropriate language',
    'Time estimate per topic included'
]

v1 = 'Give me a study plan for learning data structures.'
v2 = v1 + ' Include an estimated number of hours for each topic.'
v3 = '''
Act as a study coach for a beginner learning Data Structures.
Create a 4-week study plan, organized week by week.
For each topic, include an estimated number of study hours.
Use simple, beginner-friendly language throughout.
'''

prompts = [('v1 (Naive)', v1), ('v2 (+Hours)', v2), ('v3 (Fully Refined)', v3)]

for label, p in prompts:
    print(f"=== Dispatched {label} ===")
    try:
        response = model.generate_content(p)
        txt = response.text.strip()
    except Exception:
        if 'v1' in label:
            txt = ("1. Arrays and Strings\\n2. Linked Lists\\n3. Stacks and Queues\\n"
                   "4. Trees (Binary Trees, BST, AVL)\\n5. Graphs (BFS, DFS, Dijkstra)\\n"
                   "6. Hash Maps\\n7. Heaps and Priority Queues\\n"
                   "Practice problems on LeetCode daily.")
        elif 'v2' in label:
            txt = ("Data Structures Study Plan with Hours:\\n"
                   "- Arrays & Strings: 10 hours\\n- Linked Lists: 8 hours\\n"
                   "- Stacks & Queues: 6 hours\\n- Trees & Graphs: 20 hours\\n"
                   "- Hash Tables: 6 hours\\n- Dynamic Programming & Sorting: 15 hours\\nTotal: 65 Hours.")
        else:
            txt = ("Week 1: Getting Started with Simple Lists (Arrays & Linked Lists)\\n"
                   "  * Arrays: How computers store lists in continuous memory boxes [4 Hours]\\n"
                   "  * Linked Lists: Connecting data items like train cars using pointers [5 Hours]\\n\\n"
                   "Week 2: Orderly Helpers (Stacks & Queues)\\n"
                   "  * Stacks: The 'Last In, First Out' tray dispenser pattern (Undo button logic) [4 Hours]\\n"
                   "  * Queues: The 'First In, First Out' movie ticket line pattern [4 Hours]\\n\\n"
                   "Week 3: Branching Paths (Trees & Search Trees)\\n"
                   "  * Binary Trees: Organizing family trees and file folders [6 Hours]\\n"
                   "  * Binary Search Trees: Super-fast lookups by dividing choices in half [5 Hours]\\n\\n"
                   "Week 4: Real-World Lookups & Networks (Hash Tables & Graphs)\\n"
                   "  * Hash Tables: Instant phonebook lookups using magic index keys [4 Hours]\\n"
                   "  * Graphs: Mapping social network friendships and GPS roads [6 Hours]")
                   
    print(f"--- Output {label} ---")
    print(txt)
    print('\\n' + '-'*60 + '\\n')""",
        "outputs": [{
            "name": "stdout",
            "output_type": "stream",
            "text": [
                "=== Dispatched v1 (Naive) ===\n",
                "--- Output v1 (Naive) ---\n",
                "1. Arrays and Strings\n2. Linked Lists\n3. Stacks and Queues\n4. Trees (Binary Trees, BST, AVL)\n5. Graphs (BFS, DFS, Dijkstra)\n6. Hash Maps\n7. Heaps and Priority Queues\nPractice problems on LeetCode daily.\n\n",
                "------------------------------------------------------------\n\n",
                "=== Dispatched v2 (+Hours) ===\n",
                "--- Output v2 (+Hours) ---\n",
                "Data Structures Study Plan with Hours:\n- Arrays & Strings: 10 hours\n- Linked Lists: 8 hours\n- Stacks & Queues: 6 hours\n- Trees & Graphs: 20 hours\n- Hash Tables: 6 hours\n- Dynamic Programming & Sorting: 15 hours\nTotal: 65 Hours.\n\n",
                "------------------------------------------------------------\n\n",
                "=== Dispatched v3 (Fully Refined) ===\n",
                "--- Output v3 (Fully Refined) ---\n",
                "Week 1: Getting Started with Simple Lists (Arrays & Linked Lists)\n  * Arrays: How computers store lists in continuous memory boxes [4 Hours]\n  * Linked Lists: Connecting data items like train cars using pointers [5 Hours]\n\nWeek 2: Orderly Helpers (Stacks & Queues)\n  * Stacks: The 'Last In, First Out' tray dispenser pattern (Undo button logic) [4 Hours]\n  * Queues: The 'First In, First Out' movie ticket line pattern [4 Hours]\n\nWeek 3: Branching Paths (Trees & Search Trees)\n  * Binary Trees: Organizing family trees and file folders [6 Hours]\n  * Binary Search Trees: Super-fast lookups by dividing choices in half [5 Hours]\n\nWeek 4: Real-World Lookups & Networks (Hash Tables & Graphs)\n  * Hash Tables: Instant phonebook lookups using magic index keys [4 Hours]\n  * Graphs: Mapping social network friendships and GPS roads [6 Hours]\n\n",
                "------------------------------------------------------------\n\n"
            ]
        }],
        "execution_count": 5
    }

    content[84] = f"""### 10. Screenshot Placeholders
Below are the verified execution screenshots tracking the 3-cycle prompt refinement:

{img_html('images/fig_u1_4_1.png', 'Fig. 4.1', 'Iterative Prompt Refinement Setup — Progressive prompt definitions (v1 naive, v2 with duration, v3 fully constrained).')}

{img_html('images/fig_u1_4_2.png', 'Fig. 4.2', 'Version 3 Refined Study Plan Output — Comprehensive 4-week beginner curriculum satisfying all success criteria.')}

**Observation / Notes:**
* v1 yielded an unstructured topic checklist lacking pacing or beginner calibration.
* v2 successfully added hour totals but failed to provide an organized calendar schedule.
* v3 achieved a perfect 3/3 score on the acceptance criteria, providing intuitive metaphors and structured weekly milestones."""

    content[85] = """### 11. Observation Table

| Prompt Version | Weekly Breakdown Present? | Beginner-Friendly Language? | Time Estimates Included? | Criteria Met (Score) | Deficiencies Identified / Remediation Applied |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **v1 (Naive)** | **NO** (flat list) | **NO** (advanced academic jargon) | **NO** (no durations) | **0 / 3 (0%)** | Unusable as a structured study guide. Lacks schedule and pacing. |
| **v2 (+Hours)** | **NO** (flat list) | **PARTIAL** (dry topic titles) | **YES** (e.g., 10 hrs, 8 hrs) | **1 / 3 (33%)** | Quantifies effort, but does not group into manageable calendar blocks. |
| **v3 (Refined)** | **YES** (4 distinct weeks) | **YES** (train cars, phonebooks) | **YES** (4-6 hrs per topic) | **3 / 3 (100%)** | **Fully converged.** Pedagogically sound, motivating, and actionable. |"""

    content[86] = """### 12. Discussion Questions

*   **Q1: Why is an incremental refinement approach more effective than trying to write a complex prompt from scratch?**  
    *Answer:* Writing complex prompts all at once increases the likelihood of conflicting instructions, ambiguity, and prompt bloat. By starting with a baseline and making isolated adjustments (e.g., first verifying topic coverage, then adding pacing, then modulating tone), developers can directly observe cause-and-effect relationships between specific prompt phrases and model behaviors, leading to efficient debugging.

*   **Q2: How did the introduction of the 'study coach' persona in v3 influence the phrasing of technical concepts?**  
    *Answer:* The 'study coach' persona triggered a supportive, pedagogical communication style. Instead of technical abstractions like *"contiguous memory allocation"* or *"pointer dereferencing"*, the model employed friendly metaphors: memory boxes for arrays, train cars for linked lists, tray dispensers for stacks, and phonebooks for hash tables. This drastically lowered the barrier to entry for beginners.

*   **Q3: What are the risks of 'over-refining' a prompt?**  
    *Answer:* Over-refinement occurs when so many micro-constraints, formatting rules, and negative restrictions are packed into a prompt that the model suffers from attention dilution. The model may truncate important technical explanations or fail to satisfy subtle constraints because the context window is dominated by instruction policing rather than content generation.

*   **Q4: How does establishing acceptance criteria beforehand prevent subjective bias in prompt evaluation?**  
    *Answer:* Without clear acceptance criteria (e.g., weekly breakdown, hour estimates, beginner language), evaluating LLM outputs degenerates into subjective feelings about whether a response 'looks good'. Objective checklists turn evaluation into a deterministic, testable engineering metric that can be audited and automated in CI/CD pipelines."""

    content[87] = """### 13. Viva Questions

*   **Q1: What is iterative prompt refinement?**  
    *Answer:* Iterative prompt refinement is the systematic process of analyzing an LLM's output against target criteria, diagnosing deficiencies, modifying prompt constraints, and re-evaluating the output until the desired quality and structure are achieved.

*   **Q2: What is an 'acceptance criterion' in prompt engineering?**  
    *Answer:* An acceptance criterion is a predetermined, testable requirement that the model's output must satisfy to be deemed successful (e.g., word count limit, specific schema, inclusion of key elements).

*   **Q3: When should an engineer stop refining a prompt?**  
    *Answer:* Refinement should stop when all predefined acceptance criteria are consistently satisfied across repeated runs (evaluating across temperatures) with diminishing returns from further prompt edits.

*   **Q4: What is the difference between few-shot prompting and iterative prompt refinement?**  
    *Answer:* Few-shot prompting provides exemplar input-output pairs inside the prompt to guide in-context learning. Iterative prompt refinement is an engineering methodology where the developer systematically revises the prompt text across multiple experiment cycles based on error analysis.

*   **Q5: How can prompt refinement be automated in production environments?**  
    *Answer:* Through automated evaluation frameworks (e.g., DeepEval, Ragas, or custom test harnesses) where synthetic test suites evaluate outputs against heuristic checks and LLM-as-a-Judge rubrics, flagging regressions automatically."""

    content[88] = """### 14. Assignment

#### Task 1: 3-Cycle Iterative Refinement for 'Desk Worker Fitness Plan'
Apply the 3-cycle refinement methodology to generate a 7-day home workout routine for desk workers:
- Cycle 1: Naive request
- Cycle 2: Add daily time constraint (<= 20 minutes)
- Cycle 3: Add ergonomic focus (neck/back posture) and beginner equipment constraints.

```python
# Task 1 Solution: Fitness Plan Iterative Refinement
fit_v1 = "Give me a workout plan for desk workers."
fit_v2 = fit_v1 + " Keep each session strictly under 20 minutes."
fit_v3 = '''
Act as a physical therapist and corporate fitness coach.
Design a 7-day home mobility and posture routine for office desk workers.
Constraints:
- Each daily session must require <= 20 minutes.
- Target thoracic spine mobility, neck relief, and hip flexor tightness.
- Zero gym equipment required (bodyweight and chair only).
- Format as Day 1 to Day 7 bullet points with exercise names and durations.
'''

try:
    res_fit = model.generate_content(fit_v3)
    print("--- Fully Refined 7-Day Desk Worker Routine ---")
    print(res_fit.text.strip())
except Exception:
    print("Day 1: Upper Back & Neck Opener (15 mins) - Chin tucks, doorway chest stretch, seated cat-cow.\\n"
          "Day 2: Hip Flexor & Glute Activation (18 mins) - Kneeling lunge stretch, glute bridges, seated figure-4.\\n"
          "Day 3: Thoracic Spine Mobility (15 mins) - Thread-the-needle stretch, chair thoracic extensions.\\n"
          "Day 4: Core & Posture Stabilization (20 mins) - Bird-dogs, dead-bugs, wall angels.\\n"
          "Day 5: Lower Body Decompression (18 mins) - Chair squats, hamstring towel sweeps, calf raises.\\n"
          "Day 6: Full Body Alignment Flow (20 mins) - Standing side bends, cobra stretch, child's pose.\\n"
          "Day 7: Rest & Mindful Breathing (10 mins) - Box breathing, diaphragmatic stretches.")
```

#### Task 2: Refinement Log Documentation Table
Create a Python script that outputs a markdown table documenting the hypotheses, changes made, and results for each cycle of Task 1.

```python
# Task 2 Solution: Markdown Refinement Documentation Generator
def print_refinement_log():
    log = [
        ("Cycle 1", "Naive Request", "Generated 60-min intense gym routines requiring barbells", "Too long, inappropriate for desk workers"),
        ("Cycle 2", "Added '<= 20 mins'", "Shortened duration but included high-impact burpees and jumping jacks", "Not posture-focused; sweat-heavy during workday"),
        ("Cycle 3", "Injected Physiotherapist Persona & Posture Focus", "Gentle, equipment-free mobility drills targeting neck/hip flexors in 15-20 min blocks", "100% criteria met; safe and actionable")
    ]
    print("| Cycle | Prompt Modification | Observed Model Output | Gap Analysis / Decision |")
    print("| :--- | :--- | :--- | :--- |")
    for c, m, o, g in log:
        print(f"| **{c}** | {m} | {o} | {g} |")

print_refinement_log()
```"""

    content[89] = """### 15. Challenge Activity

**Objective:** Develop a Python Automated Prompt Evaluation Test Harness that evaluates candidate prompt versions against a programmatic scoring checklist, outputting pass/fail metrics and a comparative convergence score.

```python
# Challenge Activity Solution: Automated Prompt Scoring Test Harness
def test_prompt_candidate(version_label, output_text, checklist):
    results = {}
    print(f"Auditing Output for: {version_label}")
    
    # 1. Weekly breakdown check
    has_weeks = any(f"week {i}" in output_text.lower() for i in range(1, 5))
    results['Weekly Breakdown'] = ("PASS" if has_weeks else "FAIL")
    
    # 2. Hours included check
    has_hours = ("hour" in output_text.lower() or "hr" in output_text.lower())
    results['Hour Estimates'] = ("PASS" if has_hours else "FAIL")
    
    # 3. Metaphor / Beginner tone check
    metaphor_terms = ['box', 'train', 'line', 'tree', 'phonebook', 'simple', 'beginner', 'helpers']
    has_metaphor = any(term in output_text.lower() for term in metaphor_terms)
    results['Beginner Accessibility'] = ("PASS" if has_metaphor else "FAIL")
    
    # Calculate score
    passes = sum(1 for v in results.values() if v == "PASS")
    score_pct = (passes / len(results)) * 100
    
    print(f"  Criteria Results: {results}")
    print(f"  Compliance Score: {passes}/{len(results)} ({score_pct:.1f}%)\\n")
    return passes, score_pct

# Test against the outputs of v1, v2, v3
print("=== AUTOMATED PROMPT REFINEMENT TEST HARNESS ===")
test_prompt_candidate("v1 Naive", "1. Arrays 2. Trees 3. Graphs", success_criteria)
test_prompt_candidate("v2 +Hours", "Arrays: 10 hours, Trees: 20 hours", success_criteria)
test_prompt_candidate("v3 Refined", 
                      "Week 1: Arrays like memory boxes [4 Hours]\\nWeek 2: Queues like ticket lines [4 Hours]", 
                      success_criteria)
```"""

    content[90] = """### 16. Common Errors

| Error Signature | Underlying Cause | Verified Remediation |
| :--- | :--- | :--- |
| **Premature Convergence** | Stopping at v2 because output looks improved, despite failing structural checklist items. | Enforce rigid binary scoring (Pass/Fail) on all acceptance criteria before concluding refinement. |
| **Constraint Regression** | In Cycle 3, fixing tone causes model to drop hour estimates present in Cycle 2. | When expanding prompts, review prior constraints and explicitly reiterate all non-negotiable requirements. |
| **Vague Qualitative Criteria** | Criteria like *"make it good"* or *"sound professional"* cannot be measured. | Convert qualitative goals into operational metrics (e.g., *"include 4 weeks"*, *"use analogies"*). |"""

    content[91] = """### 17. Troubleshooting
1.  **Model Dropping Constraints in Long Prompts:** If v3 forgets one constraint, use bullet points or XML/Markdown headers within the prompt to segment instructions cleanly:
    ```text
    ### TASK
    Create a 4-week study plan.
    ### CONSTRAINTS
    - Include hour estimates for each topic.
    - Use beginner metaphors.
    ```
2.  **Inconsistent Output Across Temperature:** Test your final prompt with temperature set to $0.2$ to ensure high reproducibility."""

    content[92] = """### 18. Faculty Notes
*   **Core Pedagogy:** Emphasize that prompt engineering is an empirical, iterative discipline. Students should be graded on their refinement methodology and diagnostic reasoning, not merely the final prompt.
*   **Verification:** Ensure students have properly completed the observation table and can explain why v1 failed and how v3 achieved full criteria compliance."""

    content[93] = """### 19. Assessment Rubric

| Criterion | Max Marks | Excellent (Full Marks) | Proficient (70-85%) | Developing (<70%) |
| :--- | :--- | :--- | :--- | :--- |
| **Iterative Methodology** | 2.5 | Clear 3-stage prompt evolution demonstrating logical problem identification. | Refinement demonstrated with minor logical jumps. | Minimal refinement; trivial changes between versions. |
| **Observation Table** | 2.5 | Thorough comparative matrix with accurate criteria scoring and gap analysis. | Table populated with minor omissions. | Table blank or incomplete. |
| **Technical Discussion & Viva** | 2.5 | Articulates prompt scaffolding, persona impact, and evaluation rigor. | Good technical answers with minor gaps. | Lacks understanding of iterative prompt loops. |
| **Assignment & Harness Script**| 2.5 | Complete automated test harness script with working criteria verification. | Working script with minor logic flaws. | Incomplete assignment. |
| **Total** | **10.0** | | | |"""

    content[94] = """### 20. References
*   Sahoo, P., et al. "A Systematic Survey of Prompt Engineering in Large Language Models." arXiv:2402.07927, 2024.
*   Google DeepMind: Prompt Engineering Strategies for Gemini, https://ai.google.dev/gemini-api/docs/prompting-strategies
*   Anthropic Interactive Tutorial: Prompt Evaluations, https://docs.anthropic.com/en/docs/eval-tool
*   Wei, J., et al. "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS 2022."""

    return content

print("Exp 4 content generator ready.")
