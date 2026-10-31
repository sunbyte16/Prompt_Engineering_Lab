import json
import re

with open('Complete_Lab.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

print(f"Total Cells: {len(nb['cells'])}")
print("nbformat:", nb.get('nbformat'), ".", nb.get('nbformat_minor'))

heading_only_cells = []
empty_cells = []
error_code_cells = []
code_without_outputs = []
screenshot_cells = []
observation_table_cells = []

for i, cell in enumerate(nb['cells']):
    ctype = cell['cell_type']
    src = ''.join(cell['source']).strip()
    lines = [l.strip() for l in src.split('\n') if l.strip()]
    
    if not lines:
        empty_cells.append(i)
    elif len(lines) == 1 and lines[0].startswith('#'):
        # Allow main unit titles if expected
        if i not in [0, 126, 127]: # Colab badge or subtitle
            heading_only_cells.append((i, lines[0]))
            
    if ctype == 'code':
        outs = cell.get('outputs', [])
        if not outs:
            code_without_outputs.append(i)
        for o in outs:
            if o.get('output_type') == 'error':
                error_code_cells.append((i, o.get('ename'), o.get('evalue')))
                
    if 'Screenshot Placeholders' in src:
        has_img = ('<img ' in src or '![' in src)
        screenshot_cells.append((i, has_img))
        
    if 'Observation Table' in src:
        has_table = ('|' in src and '---' in src)
        observation_table_cells.append((i, has_table))

print("\n--- AUDIT RESULTS ---")
print(f"Empty cells count: {len(empty_cells)} -> {empty_cells}")
print(f"Heading-only cells count: {len(heading_only_cells)} -> {heading_only_cells[:10]}")
print(f"Code cells without outputs: {len(code_without_outputs)} -> {code_without_outputs}")
print(f"Code cells with errors: {len(error_code_cells)} -> {error_code_cells}")
print(f"Screenshot sections: {len(screenshot_cells)} (All have images: {all(h for _, h in screenshot_cells)})")
print(f"Observation tables: {len(observation_table_cells)} (All formatted: {all(h for _, h in observation_table_cells)})")

# Print code cells summary
print("\n--- CODE CELLS AUDIT ---")
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        outs = cell.get('outputs', [])
        print(f"Cell {i:03d}: {len(cell['source'])} lines code, {len(outs)} outputs")
