# to build with windows

cd pyman
conda env remove -n myst
conda env create -f environment.yml
conda activate myst
./update_jupyter_sphinx.ps1
./build_windows.ps1

# to view the result with your default browser

start _build/html/index.html
