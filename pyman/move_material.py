from pathlib import Path
import shutil

the_dir = Path().home() / "repos/pyman"
dest_dir = Path().home() / "repos/myst_nb/docs/examples/pyman"
notebooks = list(the_dir.glob("**/*txt"))
print(notebooks)
for a_notebook  in notebooks:
    new_name = dest_dir / a_notebook.name
    print(new_name)
    shutil.copy(a_notebook,new_name)
