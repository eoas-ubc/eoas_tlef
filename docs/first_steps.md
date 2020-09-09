# getting started, September 2020

1) Here's an abstract we just submitted for a conference -- it would be worth following the
   links to get a feeling for the technology stack we're using:

   https://ams.confex.com/ams/101ANNUAL/11python/papers/viewonly.cgi?password=582729&username=384767

2) Installing miniconda

   It would be good to start with a fresh install of https://docs.conda.io/en/latest/miniconda.html

   If you're new to conda, these links are helpful:

   * https://towardsdatascience.com/a-guide-to-conda-environments-bc6180fc533

   * https://conda-forge.org/docs/user/introduction.html
   
   * https://pypi.org/project/conda-lock/

3) Getting started with jupyter-book

   Probably the easiest thing to do is to clone the repository:

   * https://github.com/executablebooks/jupyter-book

   Follow the installation instructions in the docs and the build the documentation like this

     ```
       cd jupyter-book
       jb build docs
     ```

   If you open a browser at `docs/_build/html/index.html`  you should see a copy of:

   https://jupyterbook.org/intro.html

4) for Danil -- to see how we're using docker, clone our python intro, currently running at:

   http://node07.eos.ubc.ca:8080   with a slightly broken jupyterhub at
   http://node07.eos.ubc.ca:8000

   Log in with any username and any password, close the warning message, then open the tree with
   file->open

   The github repository for these containers is at:
   https://github.com/phaustin/Problem-Solving-with-Python-37-Edition/tree/spawner
   note the branch: spawner


5) For Benjamin -- you can see what we've done for notebooks->canvas by clone and building this
   repo:

   https://github.com/maracieco/md2canvas
