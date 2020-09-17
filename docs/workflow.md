My workflow (which I need to write down someplace)

1. md files are always the cannonical source files
2. Default jupytext config pairing is ipynb,myst:
   https://github.com/eoas-ubc/eoas_tlef/blob/master/docs/support_files/jupyter_notebook_config.py#L45-L50
4. I never commit ipynb files to the repo, if there is more than about 30% python content, I also pair a py:percent file
   by overriding the default jupytext config: https://github.com/eoas-ubc/md2canvas/blob/master/examples/demo_quiz/jupytext.toml
5. I run the jupyter-book pre-commit package checks on every commit: https://github.com/eoas-ubc/md2canvas/blob/master/.pre-commit-config.yaml
6. I use watchdog to monitor the md files for changes and launch jb or sphinx builds, and live-server to refresh the browser
   https://github.com/eoas-ubc/jb_tools and [watchdog.md](./watchdoc.md)
8. I've been using emacs (with elpy) since about 1990, but I'm spending more time in vscode, especially to edit inside containers using the container extension. There's this myst extension: https://marketplace.visualstudio.com/items?itemName=ExecutableBookProject.myst-highlight
   The extra myst markdown syntax doesn't render in notebooks, obviously. It's not too bad for us, but for students we're probably going to have to strip the non-commonmark myst syntax for some of the distributed notebooks
   For the future -- jupyter has completely rewritten their extension package, which should make it possible to swap out their markdown parser for myst in v3.0. See https://discourse.jupyter.org/t/should-jupyter-recommend-a-text-based-representation-of-the-notebook/3273/23 and https://discourse.jupyter.org/t/julia-community-is-creating-a-new-notebook-format/5422/30
9. If I'm not running the apache container to display the html, I push to github.io using https://pypi.org/project/ghp-import/
