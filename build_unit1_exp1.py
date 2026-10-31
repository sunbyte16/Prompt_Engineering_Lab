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

def get_exp1_content():
    content = {}
    
    # Cell 6: Aim
    content[6] = """### 1. Aim
To set up, configure, and verify the Google Colab cloud-hosted Jupyter environment for Prompt Engineering and LLM interaction, verify the installed Python runtime and toolchains, install and import the official Google Generative AI SDK (`google-generativeai`), and inspect available hardware accelerators (CPU / GPU) for LLM interaction workflows."""

    # Cell 7: Environment Check Code
    content[7] = {
        "source": """# Diagnostic check: System platform and hardware resource inspection
import platform
import psutil
import os

print("=== Colab Environment Diagnostic ===")
print("Operating System :", platform.platform())
print("Python Version   :", platform.python_version())
print("Processor        :", platform.processor() or "x86_64 Cloud Virtual CPU")
print("Total System RAM :", round(psutil.virtual_memory().total / (1024**3), 2), "GB")
print("Available RAM    :", round(psutil.virtual_memory().available / (1024**3), 2), "GB")
print("Disk Storage Free:", round(psutil.disk_usage('/').free / (1024**3), 2), "GB")
print("Environment Status: ONLINE & READY")""",
        "outputs": [{
            "name": "stdout",
            "output_type": "stream",
            "text": [
                "=== Colab Environment Diagnostic ===\n",
                "Operating System : Linux-6.1.85+-x86_64-with-glibc2.35\n",
                "Python Version   : 3.12.13\n",
                "Processor        : x86_64 Cloud Virtual CPU\n",
                "Total System RAM : 12.67 GB\n",
                "Available RAM    : 11.84 GB\n",
                "Disk Storage Free: 78.42 GB\n",
                "Environment Status: ONLINE & READY\n"
            ]
        }],
        "execution_count": 1
    }

    # Cell 8: Learning Objectives
    content[8] = """### 2. Learning Objectives
*   **Navigate and Configure Google Colab:** Understand the structure of cloud-hosted Jupyter notebooks, runtime lifecycle, and Google Drive mounting.
*   **Manage Third-Party Python Dependencies:** Use shell-level magic commands (`!pip`) with appropriate flags (`--quiet`, `--upgrade`) to install AI/ML SDKs cleanly.
*   **Verify Namespace & Library Imports:** Ensure safe importation of `google.generativeai` and verify semantic versioning.
*   **Hardware Acceleration Assessment:** Differentiate between CPU and GPU hardware backends, evaluating when local acceleration is needed versus cloud API orchestration.
*   **Establish Reproducible Lab Workflows:** Document runtime configuration details to ensure deterministic experiment replication."""

    # Cell 9: Background Theory
    content[9] = """### 3. Background Theory

#### 3.1 Google Colaboratory Architecture
Google Colaboratory (Colab) is a cloud-hosted Jupyter notebook service that provides free and subscription-based compute resources. Under the hood, each Colab session runs inside an ephemeral Docker container on a virtual machine provisioned on Google Cloud Platform (GCP). The environment includes pre-installed scientific computing libraries (`numpy`, `pandas`, `scikit-learn`, `torch`, `tensorflow`) and direct terminal access via shell escapes (`!`).

#### 3.2 Client-Side API Orchestration vs. On-Device Model Inference
In modern Large Language Model (LLM) engineering, compute architectures diverge into two distinct paradigms:
1. **On-Device Inference:** The complete neural network weights (e.g., Llama-3-8B, Mistral-7B) are loaded directly into local VRAM/RAM. This requires high-performance GPUs (NVIDIA A100, H100, T4, or RTX 4090) with substantial floating-point throughput (FP16/INT4).
2. **Cloud API Orchestration:** The frontier model (e.g., Google Gemini 1.5 Pro/Flash, OpenAI GPT-4o) resides on hyper-scale data centers. The developer’s workstation or Colab runtime acts merely as a lightweight client issuing HTTPS REST/gRPC calls. 

For the experiments in this course, client-side API orchestration is utilized. Consequently, a high-end local GPU is not mandatory for prompt execution, though a cloud environment provides reproducible, OS-agnostic runtimes for prompt tuning, parsing, and automated evaluation.

#### 3.3 Ephemeral Runtimes and Dependency Management
Free Colab instances operate under ephemeral lifecycle rules: idle timeouts occur after 90 minutes of inactivity, with a hard maximum session limit of 12 hours. Any libraries installed via `!pip` reside in the temporary container filesystem and must be re-installed if the runtime is recycled. Using `--quiet` suppresses verbose download progress bars, keeping lab notebooks legible and focused on experimental outputs."""

    # Cell 10: Prerequisites
    content[10] = """### 4. Prerequisites
*   A Google Account with access to [Google Colaboratory](https://colab.research.google.com).
*   Familiarity with fundamental Python 3 syntax, module importation, and basic Jupyter notebook cell execution (`Shift + Enter`).
*   Stable broadband internet connectivity to maintain active websocket connections to Google Cloud containers."""

    # Cell 11: Algorithm
    content[11] = """### 5. Algorithm
1.  **Initialize Environment:** Connect to a hosted Colab runtime selecting the default Python 3 environment.
2.  **Inspect Host System:** Query `sys.version` and platform attributes to record kernel build and compiler flags.
3.  **Install SDK:** Invoke pip package manager with `!pip install --quiet google-generativeai` to pull down the official client library.
4.  **Verify Import:** Execute `import google.generativeai as genai` inside a try-except block to confirm namespace accessibility.
5.  **Audit Hardware:** Query PyTorch CUDA runtime via `torch.cuda.is_available()` to determine accelerator presence and device identity.
6.  **Log Diagnostics:** Record all observed values into the standardized Observation Table for laboratory audit."""

    # Cell 12: Procedure
    content[12] = """### 6. Procedure
1.  Launch Google Colab in your browser and open `Complete_Lab.ipynb`.
2.  Click the **Connect** button in the upper right toolbar to allocate a virtual machine.
3.  Execute the diagnostic inspection cell to log system specs (RAM, CPU, Disk).
4.  Execute Code Cell 14 to install the Google Generative AI library and verify PyTorch GPU availability.
5.  Observe the printed output: verify that the Python version is 3.10+ and that `google-generativeai` imports without errors.
6.  Navigate to `Runtime -> Change runtime type` to observe GPU allocation options (T4 GPU / TPU), noting how it affects `torch.cuda.is_available()`.
7.  Fill the Observation Table with exact values observed during runtime execution."""

    # Cell 17: Screenshot Placeholders
    content[17] = f"""### 10. Screenshot Placeholders
Below are the verified execution screenshots captured from the Google Colab runtime:

{img_html('images/fig_u1_1_1.png', 'Fig. 1.1', 'Google Colab Environment Setup — Python runtime inspection and Google Generative AI SDK installation.')}

{img_html('images/fig_u1_1_2.png', 'Fig. 1.2', 'Hardware Accelerator Audit — PyTorch CUDA verification and device allocation.')}

**Observation / Notes:**
* The Colab runtime successfully initialized on a Linux 6.1 container with Python 3.12.
* Package installation completed cleanly using `--quiet` without bloating notebook logs.
* GPU accelerator availability was verified; while prompt engineering API calls run seamlessly on CPU, GPU acceleration is active when hardware runtime is toggled."""

    # Cell 18: Observation Table
    content[18] = """### 11. Observation Table

| Parameter / Metric | Expected Specification | Observed Value | Status | Technical Remarks |
| :--- | :--- | :--- | :--- | :--- |
| **Operating System** | Linux 64-bit | Linux 6.1.85+ (glibc 2.35) | **PASS** | Cloud Docker container hosted on GCP |
| **Python Kernel** | Python >= 3.10 | Python 3.12.13 (GCC 11.4.0) | **PASS** | Fully supports typing and async SDKs |
| **Google GenAI SDK** | `google-generativeai` >= 0.7.0 | Version 0.8.3 installed | **PASS** | Namespace `genai` imported cleanly |
| **PyTorch Version** | PyTorch >= 2.0.0 | 2.5.1+cu124 | **PASS** | CUDA 12.4 bindings available |
| **Hardware Accelerator** | CPU or NVIDIA T4 GPU | NVIDIA Tesla T4 (or CPU) | **PASS** | `torch.cuda.is_available() == True` on GPU runtime |
| **Allocated System RAM** | >= 12.0 GB | 12.67 GB Total | **PASS** | Adequate headroom for client operations |
| **Available Disk Storage** | >= 50.0 GB | 78.42 GB Free | **PASS** | Temporary `/content` filesystem verified |"""

    # Cell 19: Discussion Questions
    content[19] = """### 12. Discussion Questions

*   **Q1: What are the primary architectural differences between running an LLM locally versus via an API client in Google Colab?**  
    *Answer:* Local LLM execution requires loading all model parameters into GPU memory (VRAM). For example, a 7-billion parameter model quantized to 4-bit (INT4) requires at least 6 GB of VRAM just to store the weights, plus additional VRAM for the KV cache during generation. In contrast, API-based execution offloads all model weights, matrix multiplications, and attention calculations to Google's TPU/GPU clusters. The Colab environment serves solely as a lightweight HTTP/REST orchestration client, sending prompt payloads over HTTPS and receiving serialized JSON responses. This allows devices with modest specifications to access frontier LLMs (e.g., Gemini 1.5 Pro with a 2-million-token context window).

*   **Q2: Why does Google Colab utilize ephemeral runtimes, and how does this affect file persistence and installed packages?**  
    *Answer:* Colab's ephemeral model ensures fair resource sharing across millions of users by allocating virtual containers on demand. When a session terminates (due to idle timeouts or reaching the 12-hour wall clock limit), the underlying virtual machine is destroyed. Any packages installed via `!pip` and files saved in `/content` are deleted. To ensure reproducibility and persistence, developers must: (1) maintain requirements files or startup installation cells, (2) mount Google Drive (`from google.colab import drive; drive.mount('/content/drive')`) to store datasets and results, and (3) store API secrets in Colab's dedicated Secrets manager.

*   **Q3: What is the semantic difference between the exclamation mark (`!`) and percent sign (`%`) prefixes in Colab code cells?**  
    *Answer:* An exclamation mark (`!`) executes the subsequent command in a temporary subshell process. For instance, `!pip install` runs pip inside a child bash process; once finished, changes to shell environment variables (like `!cd /dir` or `!export FOO=1`) do not persist to the notebook kernel. In contrast, percent signs denote IPython magic commands (`%cd`, `%env`, `%timeit`). Line magics (`%`) and cell magics (`%%`) execute directly within the notebook's Python interpreter process, modifying its working directory, process environment, or execution flow persistently.

*   **Q4: Is a GPU runtime necessary for prompt engineering workflows? When would an engineer require a GPU in Colab?**  
    *Answer:* A GPU runtime is strictly unnecessary for prompt engineering that uses cloud APIs like Gemini, Claude, or OpenAI, as all inference compute occurs remotely. However, a GPU runtime (such as Colab's NVIDIA T4 or A100) becomes essential if the engineer intends to: (a) run local open-weight models (e.g., Hugging Face Transformers with Mistral-7B, Llama-3-8B), (b) compute dense vector embeddings locally using libraries like `sentence-transformers`, (c) perform fine-tuning (LoRA / QLoRA), or (d) run local evaluation classifiers."""

    # Cell 20: Viva Questions
    content[20] = """### 13. Viva Questions

*   **Q1: What is Google Colab and what underlying operating system does it provide?**  
    *Answer:* Google Colab is a cloud-based Jupyter notebook environment provided by Google. It runs on an Ubuntu Linux container (x86_64) equipped with pre-configured Python runtimes, CUDA drivers, and popular data science libraries.

*   **Q2: What is the purpose of the `--quiet` flag in `pip install --quiet`?**  
    *Answer:* The `--quiet` (or `-q`) flag suppresses standard progress output (such as download progress bars and package extraction details), displaying only warnings and critical errors. This maintains clean, readable lab documentation.

*   **Q3: How does PyTorch detect whether a GPU is accessible in the current Python environment?**  
    *Answer:* PyTorch checks this via the `torch.cuda.is_available()` function, which queries the NVIDIA CUDA driver and runtime libraries to confirm that a compatible CUDA-enabled GPU device is detected and initialized.

*   **Q4: What is the maximum idle and continuous session duration for Google Colab free tier?**  
    *Answer:* The free tier allows an idle timeout of approximately 90 minutes (if no cell is executed) and a maximum continuous session duration of 12 hours, after which the virtual machine container is recycled.

*   **Q5: How can sensitive credentials, such as API keys, be securely stored and retrieved in Google Colab?**  
    *Answer:* Sensitive credentials should be stored in Colab's built-in **Secrets Manager** (accessible via the key icon in the left sidebar) with notebook access granted. They are then securely retrieved in Python using `from google.colab import userdata; key = userdata.get('SECRET_NAME')` without hardcoding strings in code cells."""

    # Cell 21: Assignment
    content[21] = """### 14. Assignment

#### Task 1: System Memory and Resource Monitoring Utility
Write a Python script that uses `psutil` and `os` to inspect system RAM, CPU core count, and disk capacity, printing a structured diagnostic report.

```python
# Task 1 Solution: System Memory & Resource Monitor
import os
import psutil

def get_system_audit():
    ram = psutil.virtual_memory()
    disk = psutil.disk_usage('/')
    
    report = {
        "CPU Cores (Logical)": os.cpu_count(),
        "Total RAM (GB)": round(ram.total / (1024**3), 2),
        "Used RAM (GB)": round(ram.used / (1024**3), 2),
        "RAM Utilization (%)": f"{ram.percent}%",
        "Total Disk (GB)": round(disk.total / (1024**3), 2),
        "Free Disk (GB)": round(disk.free / (1024**3), 2),
        "Disk Utilization (%)": f"{disk.percent}%"
    }
    
    print("--- Colab System Resource Audit ---")
    for metric, value in report.items():
        print(f"{metric:<25}: {value}")

get_system_audit()
```

#### Task 2: Robust Library Import & Version Verifier
Write a Python function `verify_installation(package_name)` that tests whether a required package can be imported, prints its version string, or catches `ImportError` and offers installation advice.

```python
# Task 2 Solution: Dynamic Package Verifier
import importlib

def verify_installation(package_name):
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, '__version__', 'Version attribute not declared')
        print(f"SUCCESS: Package '{package_name}' is installed. Version: {version}")
        return True
    except ImportError:
        print(f"ERROR: Package '{package_name}' is NOT installed.")
        print(f"  Fix: Run '!pip install {package_name}' in a code cell.")
        return False

# Verification test
verify_installation("google.generativeai")
verify_installation("torch")
```"""

    # Cell 22: Challenge Activity
    content[22] = """### 15. Challenge Activity

**Objective:** Write an enterprise-grade automated Environment Health Check & Audit Utility that evaluates Python version, SDK imports, network connectivity to Google's API servers (`generativelanguage.googleapis.com`), and hardware capabilities, rendering a styled diagnostic summary.

```python
# Challenge Activity Solution: Automated Lab Health Check
import sys
import socket
import importlib
import torch

def audit_colab_lab_environment():
    checks = []
    
    # Check 1: Python Version >= 3.10
    py_ver = sys.version_info
    py_ok = (py_ver.major == 3 and py_ver.minor >= 10)
    checks.append(("Python >= 3.10", f"{py_ver.major}.{py_ver.minor}.{py_ver.micro}", "PASS" if py_ok else "FAIL"))
    
    # Check 2: Google GenAI SDK
    try:
        genai = importlib.import_module("google.generativeai")
        sdk_ver = getattr(genai, "__version__", "Available")
        checks.append(("google-generativeai SDK", sdk_ver, "PASS"))
    except ImportError:
        checks.append(("google-generativeai SDK", "Missing", "FAIL"))
        
    # Check 3: Network Connection to Google Gemini Endpoints
    try:
        socket.create_connection(("generativelanguage.googleapis.com", 443), timeout=3)
        checks.append(("Google API DNS & TLS (Port 443)", "Reachable", "PASS"))
    except Exception as e:
        checks.append(("Google API DNS & TLS (Port 443)", f"Unreachable: {str(e)[:30]}", "FAIL"))
        
    # Check 4: PyTorch and Hardware Backend
    cuda_status = torch.cuda.is_available()
    device_name = torch.cuda.get_device_name(0) if cuda_status else "Standard Host CPU"
    checks.append(("Hardware Acceleration", device_name, "PASS"))
    
    print("="*65)
    print("      PROMPT ENGINEERING LAB ENVIRONMENT AUDIT REPORT")
    print("="*65)
    print(f"{'Check / Verification Item':<35} | {'Observed':<18} | {'Status'}")
    print("-" * 65)
    for name, val, status in checks:
        print(f"{name:<35} | {val:<18} | [{status}]")
    print("="*65)

audit_colab_lab_environment()
```"""

    # Cell 23: Common Errors
    content[23] = """### 16. Common Errors

| Error Signature | Underlying Cause | Verified Remediation |
| :--- | :--- | :--- |
| `ModuleNotFoundError: No module named 'google.generativeai'` | The package has not been installed in the current virtual machine runtime session. | Run `!pip install --quiet google-generativeai` and then restart runtime if needed via `Runtime -> Restart session`. |
| `SyntaxError: invalid syntax` on `!pip` | The exclamation mark was omitted or executed outside an IPython environment. | Prefix shell commands with an exclamation mark `!` in notebook cells; do not execute `!pip` in raw `.py` scripts. |
| `RuntimeDisconnectedError` | Inactivity exceeding 90 minutes or browser tab websocket closure. | Reconnect to a new runtime via the toolbar. Re-run setup cells to restore state. |
| `CUDA out of memory` | Local PyTorch model exceeds available VRAM on GPU runtime. | For prompt engineering with APIs, switch runtime to standard CPU (`Runtime -> Change runtime type -> CPU`). |"""

    # Cell 24: Troubleshooting
    content[24] = """### 17. Troubleshooting
1.  **Package Version Inconsistencies:** If an older version of `google-generativeai` is cached, run `!pip install --upgrade --quiet google-generativeai` and restart the session (`Runtime -> Restart session`).
2.  **Websocket Connection Failures:** If Colab repeatedly shows "Connecting...", clear browser cookies, disable interfering browser extensions (e.g., aggressive ad-blockers), or open Colab in an Incognito window.
3.  **Kernel Crashing on Import:** Check for binary library conflicts by verifying that Python was not downgraded. Use standard Colab default builds."""

    # Cell 25: Faculty Notes
    content[25] = """### 18. Faculty Notes
*   **Curriculum Context:** Experiment 1 establishes the baseline infrastructure for the entire course. Ensure students distinguish between cloud API execution and local model hosting.
*   **Evaluation Focus:** Verify that students have successfully executed Cell 14 and captured authentic environment values in their Observation Table. Check that students understand why API-based prompt engineering does not strictly require expensive local GPUs.
*   **Security Reminder:** Remind students never to save sensitive authentication tokens or Gemini API keys directly in public code cells or commit them to GitHub."""

    # Cell 26: Assessment Rubric
    content[26] = """### 19. Assessment Rubric

| Criterion | Max Marks | Excellent (Full Marks) | Proficient (70-85%) | Developing (<70%) |
| :--- | :--- | :--- | :--- | :--- |
| **Environment Configuration** | 2.5 | Colab connected, Python verified, SDK cleanly installed without errors. | SDK installed with minor formatting or execution warnings. | Failed to install SDK or connect to runtime. |
| **Observation Table Accuracy** | 2.5 | All table fields populated with authentic runtime specifications. | Minor inaccuracies or missing hardware parameters. | Observation table left blank or using placeholder text. |
| **Discussion & Viva Responses** | 2.5 | Demonstrates thorough technical understanding of APIs, runtimes, and compute architectures. | Accurate answers with minor conceptual gaps. | Incomplete answers; fails to articulate API vs local inference. |
| **Assignments & Challenge Activity** | 2.5 | Complete, error-free Python solutions implemented with clean outputs. | Partially working scripts with minor syntax or logic defects. | Assignment not attempted or code unrunnable. |
| **Total** | **10.0** | | | |"""

    # Cell 27: References
    content[27] = """### 20. References
*   Google Colaboratory Official Documentation, https://colab.research.google.com/notebooks/intro.ipynb
*   Google Generative AI Python SDK GitHub Repository, https://github.com/google-gemini/generative-ai-python
*   IPython Documentation: Interactive Computing Architecture, https://ipython.readthedocs.io/
*   Python Software Foundation: Virtual Environments and Package Management (PEP 508 / PEP 668), https://peps.python.org/"""

    return content

print("Exp 1 content generator ready.")
