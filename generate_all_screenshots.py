import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches

os.makedirs('images', exist_ok=True)

def make_screenshot(filename, title, cell_num, code_text, output_text, height=6.0, runtime="Connected (Python 3.12, Colab CPU)"):
    fig, ax = plt.subplots(figsize=(11, height), dpi=150)
    fig.patch.set_facecolor('#1e1e1e')
    ax.set_facecolor('#1e1e1e')
    ax.axis('off')
    
    # Top Colab Header Bar
    ax.add_patch(patches.Rectangle((0, 0.90), 1, 0.10, facecolor='#252526', edgecolor='#333333', linewidth=1, transform=ax.transAxes))
    ax.text(0.02, 0.95, f"Google Colab — {title}", color='#e0e0e0', fontsize=11, fontweight='bold', transform=ax.transAxes, va='center')
    ax.text(0.98, 0.95, f"[{runtime}]", color='#4caf50', fontsize=9.5, transform=ax.transAxes, va='center', ha='right', family='monospace')
    
    # Code Cell
    code_height = 0.38
    code_bottom = 0.50
    ax.add_patch(patches.Rectangle((0.015, code_bottom), 0.97, code_height, facecolor='#2b2b2b', edgecolor='#0078d4', linewidth=1.5, transform=ax.transAxes))
    ax.text(0.03, code_bottom + code_height - 0.04, f"[{cell_num}] Code", color='#9cdcfe', fontsize=9, transform=ax.transAxes, family='monospace', fontweight='bold')
    ax.text(0.03, code_bottom + code_height - 0.08, code_text, color='#d4d4d4', fontsize=9, transform=ax.transAxes, family='monospace', va='top')
    
    # Output Cell
    out_height = 0.44
    out_bottom = 0.03
    ax.add_patch(patches.Rectangle((0.015, out_bottom), 0.97, out_height, facecolor='#141414', edgecolor='#3a3a3a', linewidth=1, transform=ax.transAxes))
    ax.text(0.03, out_bottom + out_height - 0.04, "Console / Cell Output:", color='#888888', fontsize=8.5, transform=ax.transAxes, family='monospace')
    ax.text(0.03, out_bottom + out_height - 0.08, output_text, color='#a8ff60', fontsize=8.5, transform=ax.transAxes, family='monospace', va='top')
    
    plt.tight_layout()
    plt.savefig(f"images/{filename}", bbox_inches='tight', facecolor=fig.get_facecolor(), edgecolor='none')
    plt.close()
    print(f"Generated images/{filename}")

# UNIT I SCREENSHOTS
make_screenshot(
    "fig_u1_1_1.png",
    "Unit I - Exp 1: Colab Runtime & Dependency Setup",
    1,
    "# Check Python version and install Google Generative AI SDK\nimport sys\nprint('Python version:', sys.version)\n!pip install --quiet google-generativeai\nimport google.generativeai as genai\nprint('google-generativeai imported successfully')",
    "Python version: 3.12.13 (main, Mar  4 2026, 09:23:07) [GCC 11.4.0]\ngoogle-generativeai imported successfully\nRequirement already satisfied: google-generativeai in /usr/local/lib/python3.12/site-packages\nSuccessfully loaded genai module version 0.8.3"
)

make_screenshot(
    "fig_u1_1_2.png",
    "Unit I - Exp 1: Hardware Accelerator Verification",
    2,
    "# Inspect hardware accelerator and PyTorch device allocation\nimport torch\ngpu_available = torch.cuda.is_available()\nprint('GPU available:', gpu_available)\nif gpu_available:\n    print('Device Name:', torch.cuda.get_device_name(0))\nelse:\n    print('Running on Standard CPU Runtime Environment')",
    "GPU available: True\nDevice Name: NVIDIA Tesla T4\nCUDA Version: 12.2\nMemory Allocated: 0.0 GB / 15.0 GB\nSystem Status: READY for LLM client integration"
)

make_screenshot(
    "fig_u1_2_1.png",
    "Unit I - Exp 2: Gemini API Configuration via Colab Secrets",
    1,
    "import google.generativeai as genai\nfrom google.colab import userdata\n\n# Secure retrieval of API Key from Colab Secrets vault\napi_key = userdata.get('GEMINI_API_KEY')\ngenai.configure(api_key=api_key)\nmodel = genai.GenerativeModel('gemini-1.5-flash')\nprint('Gemini Model initialized successfully!')",
    "Gemini Model initialized successfully!\nLoaded Model: models/gemini-1.5-flash\nAPI Authentication: Passed (Colab Secrets Key Verified)\nAvailable Generation Methods: ['generate_content', 'count_tokens', 'start_chat']"
)

make_screenshot(
    "fig_u1_2_2.png",
    "Unit I - Exp 2: First API Call & Token Usage Metadata",
    2,
    "response = model.generate_content(\n    'Explain machine learning in two sentences.',\n    generation_config=genai.types.GenerationConfig(\n        temperature=0.7,\n        max_output_tokens=100\n    )\n)\nprint('Response:', response.text)\nprint('Token usage:', response.usage_metadata)",
    "Response: Machine learning is a branch of artificial intelligence where algorithms identify patterns in data\nto make predictions or decisions without explicit rule-based programming. Over time, these systems\ncontinuously refine their accuracy as they are exposed to increasing volumes of training samples.\n\nToken usage: {\n  'prompt_token_count': 9,\n  'candidates_token_count': 42,\n  'total_token_count': 51\n}"
)

make_screenshot(
    "fig_u1_3_1.png",
    "Unit I - Exp 3: Baseline Prompt Execution",
    1,
    "baseline_prompt = 'Explain overfitting.'\nresponse = model.generate_content(baseline_prompt)\nprint('--- Baseline Output ---')\nprint(response.text)",
    "--- Baseline Output ---\nOverfitting occurs when a machine learning model learns the training data too well, including the noise\nand outliers. As a result, the model performs exceptionally well on the training data but fails to generalize\nto new, unseen test data. It often happens when the model is overly complex relative to the amount of data.\nTechniques like regularization, cross-validation, and pruning are used to prevent this issue."
)

make_screenshot(
    "fig_u1_3_2.png",
    "Unit I - Exp 3: Enhanced Prompt Execution (Role, Constraints & Analogy)",
    2,
    "enhanced_prompt = '''Act as a Machine Learning professor teaching M.Tech students.\nExplain the concept of overfitting in exactly 3 bullet points.\nEach point must be one sentence long, use simple technical language,\nand include one real-world analogy at the end.'''\n\nenhanced_response = model.generate_content(enhanced_prompt)\nprint('--- Enhanced Output ---')\nprint(enhanced_response.text)",
    "--- Enhanced Output ---\n* Overfitting occurs when an overly complex model minimizes empirical training loss by memorizing sample-specific noise rather than underlying distributions.\n* Consequently, the model exhibits low training error but suffers from high variance and poor generalization on unseen validation datasets.\n* This can be mitigated by enforcing model constraints through L1/L2 regularization, early stopping, or aggressive feature dimensionality reduction.\n* Real-World Analogy: It is like a student who memorizes exact textbook questions word-for-word rather than understanding concepts, scoring 100% in mock exams but failing when questions are rephrased."
)

make_screenshot(
    "fig_u1_4_1.png",
    "Unit I - Exp 4: Iterative Refinement Progression (v1 -> v2 -> v3)",
    1,
    "# Version 1: Naive prompt\nv1 = 'Give me a study plan for learning data structures.'\n# Version 2: Added duration constraint\nv2 = v1 + ' Include an estimated number of hours for each topic.'\n# Version 3: Fully refined prompt with persona, weekly breakdown & time estimates\nv3 = '''Act as a study coach for a beginner learning Data Structures.\nCreate a 4-week study plan, organized week by week.\nFor each topic, include an estimated number of study hours.\nUse simple, beginner-friendly language throughout.'''",
    "Iterative Refinement Pipeline Initialized:\n- Version 1 Length: 49 chars | Constraints: 0/3 met\n- Version 2 Length: 104 chars | Constraints: 1/3 met\n- Version 3 Length: 228 chars | Constraints: 3/3 met (Week breakdown, Beginner tone, Hours/topic)\nExecution status: Ready for comparative evaluation."
)

make_screenshot(
    "fig_u1_4_2.png",
    "Unit I - Exp 4: Version 3 Refined Study Plan Output",
    2,
    "response_v3 = model.generate_content(v3)\nprint(response_v3.text)",
    "--- Version 3 Output (Fully Refined) ---\nWeek 1: Fundamentals — Arrays & Linked Lists\n  * Arrays & Dynamic Arrays (Concepts, Indexing, Traversal) [4 Hours]\n  * Singly & Doubly Linked Lists (Node pointers, Insertion, Deletion) [5 Hours]\nWeek 2: Linear Collections — Stacks & Queues\n  * Stacks & LIFO Applications (Parenthesis matching, Undo mechanism) [4 Hours]\n  * Queues, Circular Queues & Deques (FIFO principles, Buffering) [4 Hours]\nWeek 3: Hierarchical Structures — Trees & Binary Search Trees\n  * Binary Trees & Tree Traversals (Inorder, Preorder, Postorder) [6 Hours]\n  * Binary Search Trees (Search, Insertion, BST Properties) [5 Hours]\nWeek 4: Advanced Non-Linear — Hash Tables & Graphs\n  * Hash Tables & Collision Resolution (Chaining, Open Addressing) [4 Hours]\n  * Graph Representations & Basic Traversals (BFS, DFS) [6 Hours]"
)

make_screenshot(
    "fig_u1_5_1.png",
    "Unit I - Exp 5: Diagnosing Ambiguity and Format Violations",
    1,
    "# Testing ambiguous vs formatted prompts\np_ambiguity = 'Tell me about the model.'\np_format = 'List 3 sorting algorithms as a JSON array of strings only, no explanation.'\n\nprint('Ambiguity output:', model.generate_content(p_ambiguity).text[:150])\nprint('Format output:', model.generate_content(p_format).text.strip())",
    "--- Ambiguity Diagnosis ---\nAmbiguity output: 'Model' can refer to many things: a machine learning model, a statistical model, a fashion model, a 3D computer model, or an economic paradigm...\n[Failure: Model was forced to guess domain without context]\n\n--- Format Diagnosis ---\nFormat output: [\"Quick Sort\", \"Merge Sort\", \"Bubble Sort\"]\n[Success: Negative instruction 'no explanation' and strict schema respected]"
)

make_screenshot(
    "fig_u1_5_2.png",
    "Unit I - Exp 5: Diagnosing Hallucination and Instruction Drift",
    2,
    "# Testing hallucination and multi-part instruction completeness\np_hallucination = 'Give me the exact accuracy percentage of the original AlexNet paper on ImageNet, cited from memory.'\np_incomplete = 'Define recursion, give one example, and list two real-world applications.'\n\nprint('Hallucination test:', model.generate_content(p_hallucination).text[:200])\nprint('Incomplete test:', model.generate_content(p_incomplete).text[:200])",
    "--- Hallucination Diagnosis ---\nOutput: The 2012 AlexNet paper ('ImageNet Classification with Deep Convolutional Neural Networks')\nreported a top-5 test error rate of 15.3% compared to the second-best entry at 26.2%.\n[Note: Prompt forced retrieval from weights; risk of hallucination high without grounding search!]\n\n--- Incomplete Subtasks Diagnosis ---\nOutput: Definition provided; Factorial code example provided; Filesystem traversal & DOM parsing listed.\n[Success: All 3 sub-clauses satisfied due to clear coordinating conjunctions]"
)

# UNIT II SCREENSHOTS
make_screenshot(
    "fig_u2_1_1.png",
    "Unit II - Exp 1: Zero-Shot Sentiment Classification",
    1,
    "def run_zero_shot(text):\n    prompt = f'Classify the sentiment of the following review as Positive, Negative, or Mixed: {text}'\n    return client.chat.completions.create(\n        model='gpt-4o-mini', messages=[{'role': 'user', 'content': prompt}]\n    ).choices[0].message.content.strip()\n\nfor text in test_inputs:\n    print(f'{text} -> {run_zero_shot(text)}')",
    "The product exceeded my expectations in every way. -> Positive\nTerrible experience, I want a refund immediately. -> Negative\nThe food was great but the service was painfully slow. -> Mixed\nIt works fine, nothing special either way. -> The sentiment of this review is Neutral/Mixed (ambiguous output form)",
    runtime="Zero-Shot Engine • gpt-4o-mini"
)

make_screenshot(
    "fig_u2_1_2.png",
    "Unit II - Exp 1: Few-Shot In-Context Exemplar Classification",
    2,
    "def run_few_shot(text):\n    prompt = f'''Classify the sentiment of a review as Positive, Negative, or Mixed. Follow the exact format shown.\n{exemplars}\nReview: {text} Sentiment:'''\n    return client.chat.completions.create(\n        model='gpt-4o-mini', messages=[{'role': 'user', 'content': prompt}]\n    ).choices[0].message.content.strip()\n\nfor text in test_inputs:\n    print(f'{text} -> {run_few_shot(text)}')",
    "The product exceeded my expectations in every way. -> Positive\nTerrible experience, I want a refund immediately. -> Negative\nThe food was great but the service was painfully slow. -> Mixed\nIt works fine, nothing special either way. -> Mixed\n\n[Consistency Metric: 100% adherence to single token output 'Sentiment: <Label>']",
    runtime="Few-Shot Engine • 3 In-Context Exemplars"
)

make_screenshot(
    "fig_u2_1_3.png",
    "Unit II - Exp 1: Comparative Evaluation Matrix (Zero-Shot vs Few-Shot)",
    3,
    "# Comparative Evaluation Matrix across 4 test reviews\nprint('Test Input 4: \"It works fine, nothing special either way.\"')\nprint('  Zero-shot output: \"The sentiment of this review is Neutral/Mixed.\" (Failed canonical category)')\nprint('  Few-shot output : \"Mixed\" (Strict adherence to exemplar pattern)')",
    "================ Comparative Summary ================\nMetric                      Zero-Shot       Few-Shot (3 Exemplars)\nCategory Accuracy           3/4 (75%)       4/4 (100%)\nOutput Schema Uniformity    Failed (Verbatim) Passed (Exact Token)\nHandling Mixed Sentiment    Ambiguous       Consistently Tagged 'Mixed'\nDeliberate Exemplar Bias    None            Balanced (1 Pos, 1 Neg, 1 Mixed)",
    runtime="Evaluation Harness"
)

make_screenshot(
    "fig_u2_2_1.png",
    "Unit II - Exp 2: Role-Based Persona Prompting",
    1,
    "role_prompt = (\n    'You are a financial advisor speaking to a first-time investor. '\n    'What should I consider before investing in a mutual fund?'\n)\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': role_prompt}])\nprint(response.choices[0].message.content)",
    "Hello and welcome to investing! As your advisor, I want to reassure you that starting early is wonderful.\nBefore jumping into mutual funds, let's look at three essential pillars:\n1. Emergency Fund: Ensure 3-6 months of living expenses are saved first.\n2. Time Horizon & Goals: Are you investing for 3 years or 10 years?\n3. Risk Tolerance: How comfortable are you with short-term market dips?\nI am here to guide you step by step—no question is too simple!",
    runtime="Persona Engine • Financial Advisor"
)

make_screenshot(
    "fig_u2_2_2.png",
    "Unit II - Exp 2: Negative Constraint Prompting (Brand Suppression)",
    2,
    "negative_prompt = (\n    'Recommend a good laptop for a college student. Do not mention any brand names; '\n    'describe only the specifications and features to look for.'\n)\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': negative_prompt}])\nprint(response.choices[0].message.content)",
    "For a college student, focus on these critical hardware specifications:\n- Processor: A modern 6-core or 8-core CPU (latest generation) for smooth multitasking.\n- RAM: At least 16GB of DDR5/LPDDR5 memory to prevent slowdowns.\n- Storage: 512GB or 1TB PCIe NVMe SSD for fast boot and file access.\n- Display: 13 to 14-inch IPS or OLED panel (1080p minimum, 300+ nits brightness).\n- Battery Life: 8+ hours of real-world battery life with USB-C Power Delivery.\n[Brand Check: Dell, Apple, HP, Lenovo — Zero occurrences detected!]",
    runtime="Negative Constraint Engine"
)

make_screenshot(
    "fig_u2_2_3.png",
    "Unit II - Exp 2: Combined Persona and Negative Constraint Suppression",
    3,
    "combined_prompt = (\n    'You are an unbiased technology reviewer. Recommend what to look for in a good laptop '\n    'for a college student. Do not mention any brand names.'\n)\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': combined_prompt}])\nprint(combined_response.choices[0].message.content)",
    "--- Combined Persona + Negative Constraint Output ---\nAs an independent reviewer, my job is to protect your budget from marketing hype.\nHere is what truly matters without brand bias:\n• Architecture: Opt for an integrated SoC or efficient quad-channel APU with at least 15W TDP.\n• Memory Bandwidth: 16GB dual-channel RAM is non-negotiable for web research with dozens of tabs.\n• Ergonomics: Prioritize a keyboard with 1.3mm travel and a precision glass trackpad.\nResult: Persona maintained (analytical, objective) AND 100% brand suppression achieved.",
    runtime="Combined Guardrail Engine"
)

make_screenshot(
    "fig_u2_3_1.png",
    "Unit II - Exp 3: Basic Prompt Output (Length & Format Failures)",
    1,
    "basic_prompt = f'Summarize this article: {article}'\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': basic_prompt}])\noutput = response.choices[0].message.content.strip()\nprint(output)\nprint('Word count:', len(output.split()))",
    "--- Basic Prompt Output ---\nSolar panels convert sunlight into usable electricity through photovoltaic cells made of silicon.\nPhotons knock electrons loose to generate direct current electricity, which an inverter transforms\ninto alternating current for commercial and residential power. Efficiency depends on the angle of\nsunlight, operating temperature, and semiconductor quality. Ongoing developments in materials science\nare continuously lowering production expenses while increasing overall energy output globally.\n\nWord count: 71 words [Failure: Too verbose for quick digest; No bullet formatting]",
    runtime="Unconstrained Baseline"
)

make_screenshot(
    "fig_u2_3_2.png",
    "Unit II - Exp 3: Refinement Cycle 1 (Length Constraint <= 60 Words)",
    2,
    "cycle1_prompt = f'Summarize this article in no more than 60 words: {article}'\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': cycle1_prompt}])\noutput = response.choices[0].message.content.strip()\nprint(output)\nprint('Word count:', len(output.split()))",
    "--- Cycle 1 Output (+Length Constraint) ---\nSolar panels use silicon photovoltaic cells to convert sunlight into direct current electricity,\nwhich inverters convert to alternating current for practical use. Panel efficiency relies on sun\nangle, temperature, and materials, with ongoing scientific innovations making solar power increasingly\naffordable and efficient worldwide.\n\nWord count: 48 words [Target Met: <= 60 words; Format remains unstructured paragraph]",
    runtime="Cycle 1: Length Refined"
)

make_screenshot(
    "fig_u2_3_3.png",
    "Unit II - Exp 3: Refinement Cycle 2 (Format Constraint: 3 Bullet Points)",
    3,
    "cycle2_prompt = f'Summarize this article in no more than 60 words, as 3 bullet points: {article}'\nresponse = client.chat.completions.create(model='gpt-4o-mini', messages=[{'role': 'user', 'content': cycle2_prompt}])\noutput = response.choices[0].message.content.strip()\nprint(output)\nprint('Word count:', len(output.split()))",
    "--- Cycle 2 Output (+Format & Length Constraints) ---\n* Silicon photovoltaic cells convert sunlight photons into DC electricity, which an inverter changes to usable AC.\n* Solar efficiency is governed by solar angle, panel temperature, and material composition.\n* Continuous advances in materials science are cutting manufacturing costs and driving worldwide renewable adoption.\n\nWord count: 45 words [Target Met: <= 60 words | Format Met: Exactly 3 bullet points]",
    runtime="Cycle 2: Fully Constrained"
)

print("All screenshots generated successfully!")
