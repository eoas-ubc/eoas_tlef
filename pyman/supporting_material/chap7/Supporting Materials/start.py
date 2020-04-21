import subprocess
import platform

def clear():
    subprocess.Popen( "cls" if platform.system() == 
                      "Windows" else "clear", shell=True)

clear()