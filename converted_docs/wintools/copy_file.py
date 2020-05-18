import context
import os
import shutil
from pathlib import Path
import stat
import pprint

pp=pprint.PrettyPrinter(indent=4)
#pp.pprint(dict(os.environ))

destdir = Path(os.environ['PREFIX']) / 'bin'
destdir.mkdir(exist_ok=True,parents=True)
if os.name == 'nt':
    scriptfiles=(context.root_dir / 'binwin').glob("*")
else:
    scriptfiles = (context.root_dir / 'bin').glob("*")

for a_file in scriptfiles:
    destfile = destdir / a_file.name
    shutil.copy(a_file,destfile)
    print(f"from {str(a_file)}  to {str(destfile)}")
    if os.name != 'nt':
        os.chmod(destfile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    