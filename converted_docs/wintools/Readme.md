# simple wrappers for jupyter-book and sphinx

These wrappers guarantee that jupyter-book and jupyter-sphinx run with utf8 throughout on
windows.

**Usage**:

## here's a sample environment.yml

```
name: myst
channels:
  - eoas_ubc
  - conda-forge
  - defaults
dependencies:
  - git
  - python=3.7.*
  - jupyter
  - runjb
  - sphinx=2.4.4
  - pydata-sphinx-theme
  - ghp-import
  - pip
  - pip:
    - sphinx_rtd_theme
    - git+https://github.com/executablebooks/jupyter-book
    - git+https://github.com/executablebooks/MyST-NB.git
    - jupyter-cache[cli]
    - git+https://github.com/mwouts/jupytext.git
```
At an anaconda powershell prompt do:

```
conda env create -f environment.yml
conda activate myst
```

then:


## windows

at a powershell prompt:

```
> runmyst .

and

> runjb .
```

## unix

for symmetry, the following will also work in macos or linux

```
> runmyst.sh .

and

> runjb.sh .
```

## Files:

- [runmyst.ps1](binwin/runmyst.ps1)

- [runjb.ps1](binwin/runjb.ps1)

- [runmyst.sh](bin/runmyst.sh)

- [runjb.sh](bin/runjb.sh)


