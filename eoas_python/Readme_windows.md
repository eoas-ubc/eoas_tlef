# to build with windows

- cd eoas_python
- conda env remove -n ebp
- conda env create -f environment.yml
- conda activate myst
- ./update_jupyter_sphinx.ps1
- ./build_windows.ps1

# to view the result with your default browser

start _build/html/index.html
