---
jupytext:
  cell_metadata_filter: all
  formats: ipynb,myst
  notebook_metadata_filter: all,-language_info,-toc,-latex_envs
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
language_info:
  codemirror_mode:
    name: ipython
    version: 3
  file_extension: .py
  mimetype: text/x-python
  name: python
  nbconvert_exporter: python
  pygments_lexer: ipython3
  version: 3.7.6
---

# Student installs

**If you already have conda or anaconda installed, skip to `Git install` below**



## For MacOS new installs


1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the `Miniconda3 MacOSX 64-bit pkg` file from the menu and run it, agreeing to the licences and accepting all defaults. You should install for "just me"

1. To test your installation, open a fresh terminal window and at the prompt type `which conda`.  You should see something resembling the following output, with your username instead of `phil`:

```
% which conda
/Users/phil/opt/miniconda3/bin/conda
```

## For Windows new installs

1. Download miniconda from  https://docs.conda.io/en/latest/miniconda.html  -- choose the `Miniconda3 Windows 64-bit`. download from the menu and run it, agreeing to the licences and accepting all defaults.

The installer should suggest installing in a path that looks like:

```
C:\Users\phil\Miniconda3
```

2. Once the install completes hit the windows key and start typing `anaconda`.  You should see a shortcut that looks like:

```
Anaconda Powershell Prompt
(Miniconda3)
```

**Note that Windows comes with two different terminals `cmd` (old) and `powershell` (new).  Always select the powershell version of the anaconda terminal**

3. Select the short cut.  If the install was successful you should see something like:

```
(base) (Miniconda3):Users/phil>
```
with your username substituted for phil.

## Git install

Inside your powershell or MacOs terminal, install git using conda:

```
conda install git
```

## Setting up the course repository

In the terminal, change directories to your home directory (called `~` for short) and make a new directory
called `repos` to hold the course notebook repository.  Change into `repos` and clone the course:

```
cd ~
mkdir repos
cd repos
git clone https://github.com/phaustin/numeric_students.git
```

## Creating the course environment

In the terminal, execute the following commands:

```
cd numeric_students/utils
conda env create -f numeric.yml
conda activate numeric
```

## Opening the notebook folder

```
cd ~/repos/numeric_students/numeric_notebooks
jupyter notebook
```
