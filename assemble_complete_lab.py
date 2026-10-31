import json
import shutil
import os

from build_unit1_exp1 import get_exp1_content
from build_unit1_exp2 import get_exp2_content
from build_unit1_exp3 import get_exp3_content
from build_unit1_exp4 import get_exp4_content
from build_unit1_exp5 import get_exp5_content
from build_unit1_appendices import get_appendices_content
from build_unit2_updates import get_unit2_updates

def assemble():
    notebook_path = 'Complete_Lab.ipynb'
    backup_path = 'Complete_Lab_backup.ipynb'
    
    # 1. Backup original notebook
    if not os.path.exists(backup_path):
        shutil.copyfile(notebook_path, backup_path)
        print(f"Created backup at {backup_path}")
        
    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)
        
    total_cells = len(nb['cells'])
    print(f"Loaded {notebook_path} with {total_cells} cells.")
    
    # Gather all updates
    all_updates = {}
    all_updates.update(get_exp1_content())
    all_updates.update(get_exp2_content())
    all_updates.update(get_exp3_content())
    all_updates.update(get_exp4_content())
    all_updates.update(get_exp5_content())
    all_updates.update(get_appendices_content())
    all_updates.update(get_unit2_updates())
    
    # Update Cell 4 (intro banner)
    all_updates[4] = """<div class="alert alert-block alert-info" style="border-left: 5px solid #2196f3; padding: 15px; margin: 20px 0; background-color: #f0f7ff; border-radius: 4px;">
  <h4 style="color: #0d47a1; margin-top: 0;">📘 Unit I: Foundations of Prompt Engineering & LLM Interaction</h4>
  <p style="color: #333; margin-bottom: 0;">
    Welcome to <b>Unit I</b>. This unit establishes the experimental foundation of the course: configuring Google Colab, establishing secure API authentication with Google Gemini 1.5 Flash, exploring baseline vs. enhanced prompting paradigms, implementing systematic iterative refinement cycles, and diagnosing core prompt failure modes.
  </p>
</div>"""

    print(f"Applying updates to {len(all_updates)} cells...")
    
    for idx, new_val in all_updates.items():
        if idx >= total_cells:
            print(f"WARNING: Cell index {idx} out of range ({total_cells})")
            continue
            
        cell = nb['cells'][idx]
        if isinstance(new_val, str):
            # Markdown or text replacement
            cell['source'] = [line + '\n' for line in new_val.split('\n')]
            # Fix trailing newline on last line
            if cell['source']:
                cell['source'][-1] = cell['source'][-1].rstrip('\n')
        elif isinstance(new_val, dict):
            # Code cell with source and outputs
            if 'source' in new_val:
                src_lines = [line + '\n' for line in new_val['source'].split('\n')]
                if src_lines:
                    src_lines[-1] = src_lines[-1].rstrip('\n')
                cell['source'] = src_lines
            if 'outputs' in new_val:
                cell['outputs'] = new_val['outputs']
            if 'execution_count' in new_val:
                cell['execution_count'] = new_val['execution_count']

    # Write out updated notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)
        
    print(f"Successfully wrote updated notebook to {notebook_path}!")

if __name__ == '__main__':
    assemble()
