import context
import os
import shutil
from pathlib import Path
import stat

destdir = Path(os.environ['PREFIX']) / 'bin'
if os.name == 'nt':
    scriptfiles=(context.root_dir / 'winbin').glob("*")
else:
    scriptfiles = (context.root_dir / 'bin').glob("*")
for a_file in scriptfiles:
    destfile = destdir / a_file.name
    shutil.copy(a_file,destfile)
    if os.name != 'nt':
        os.chmod(destfile, stat.S_IRWXU | stat.S_IRWXG | stat.S_IRWXO)
    
