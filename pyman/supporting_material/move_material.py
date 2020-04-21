from pathlib import Path

the_dir = Path()
notebooks = list(the_dir.glob("**/*rst"))
print(notebooks)
for a_notebook  in notebooks:
    print(f"removing {a_notebook.name}")
    a_notebook.unlink()
    
