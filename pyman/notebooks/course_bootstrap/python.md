---
jupytext:
  cell_metadata_filter: -all
  formats: ipynb,py:percent
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

# The command line shell and git

  - The default shell on OSX is bash, which is taught in this set of
    lessons: <https://swcarpentry.github.io/shell-novice/> or in this
    [detailed bash reference](https://programminghistorian.org/en/lessons/intro-to-bash)
  - if you are on Windows, powershell is somewhat similar -- here is
    a table listing commands for both shell side by side taken from
    this in-depth [powershell tutorial](https://programminghistorian.org/en/lessons/intro-to-powershell#quick-reference)

## Using the command line

### Powershell and Bash common commands

* To go to your $HOME folder:
  
```
cd ~

or

cd $HOME
```

* To open explorer or finder for the current folder:

```
windows explorer do:

   start .

MacOs finder do:

   open .
   
```
       
* To move up one folder:

```
cd ..
```

* To save typing, remember that hitting the tab key completes filenames

### To configure  powershell on windows

* first start a powershell terminal with admin privileges, then type:

   `set-executionpolicy remotesigned`
   
* then, in your miniconda3 powershel profile, do:

   `Test-Path $profile`
   
  to see whether you have an existing profile.
  
* if you don't have a profile, then do the following (this will overwrite an existing profile, so be aware):

   `New-Item –Path $Profile –Type File –Force`
   
* To add to your profile, open with:

   `start $profile`
   
### To configure bash or zsh on MacOS

* open a terminal then type either

   `open .bash_profile`
   
  or for Catalina
  
    `open .zshenv`
   
  

### Bash and powershell command reference

| Cmdlet | Alias | Bash Equivalent | Description |
| ------- | ------- | ------- | ------- |
| `Get-ChildItem` | `gci` | `ls` | List the directories and files in the current location. | 
| `Set-Location` | `sl` | `cd` | Change to the directory at the given path. Typing `..` rather than a path will move up one directory. |
| `Push-Location` | `pushd` | `pushd` | Changes to the directory. |
| `Pop-Location` | `popd` | `popd` | Changes back to the previous directory after using `pushd` |
| `New-Item` | `ni` | (`touch`) | Creates a new item. Used with no parameter, the item is by default a file. Using `mkdir` is a shortcut for including the parameter `-ItemType dir`. |
| `mkdir` | none | `mkdir` | Creates a new directory. (See `New-Item`.) |
| `Explorer` | `start .` | `open .`) | Open something using File Explorer (the GUI) |
| `Remove-Item` | `rm` | `rm` | Deletes something. Permanently! |
| `Move-Item` | `mv` | `mv` | Moves something. Takes two arguments - first a filename (i.e. its present path), then a path for its new location (including the name it should have there). By not changing the path, it can be used to rename files. |
| `Copy-Item` | `cp` | `cp` | Copies a file to a new location. Takes same arguments as move, but keeps the original file in its location. |
| `Write-Output` | `write` | `echo` | Outputs whatever you type. Use redirection to output to a file. Redirection with `>>` will add to the file, rather than overwriting contents. |
| `Get-Content` | `gc` | `cat` | Gets the contents of a file and prints it to the screen. Adding the parameter `-TotalCount` followed by a number x prints only the first x lines. Adding the parameter `-Tail` followed by a number x prints only the final x lines. |
| `Select-String` | `sls` | (`grep`) | Searches for specific content. |
| `Measure-Object` | `measure` | (`wc`) | Gets statistical information about an object. Use `Get-Content` and pipe the output to `Measure-Object` with the parameters `-line`, `-word`, and `-character` to get word count information. |
| `>` | none | `>` |Redirection. Puts the output of the command to the left of `>` into a file to the right of `>`. |
| `\|` | none | `\|` |Piping. Takes the output of the command to the left and uses it as the input for the command to the right. |
| `Get-Help` | none | `man` | Gets the help file for a cmdlet. Adding the parameter `-online` opens the help page on TechNet. |
| `exit` | none | `exit` | Exits PowerShell |

Remember the keyboard shortcuts of `tab` for auto-completion and the up and down arrows to scroll through recent commands. These shortcuts can save a lot of typing!

## Git

- A good place to go to learn git fundamentals is this lesson
    <https://swcarpentry.github.io/git-novice/>

## Pulling changes from the github repository

When we commit changes to the master branch and push to our github
repository, you'll need to download those changes to keep current. To do
that:

1)  open a shell

2)  cd to the numeric repository

3)  fetch the changes with:
    
        git fetch origin

4)  make sure you aren't going to clobber any of your own files:
    
        git status
    
    you can ignore "untracked files", but pay attention to any files
    labeled "modified". Those will be overwritten when you reset to our
    commit, so copy them to a new name or folder.

5)  Finally, get to our commit with:
    
        git reset --hard origin/master
    
    If that worked, then printing the most recent log entry:
    
        git log -1
    
    should tell you the most recent commit message, and it should agree
    with what you see at our github repository.

# Books and tutorials

  - We will be referring to our version of  David Pine's Introduction to Python:
    http://phaustin.github.io/pyman.  The notebooks for each chapter are included
    in the [numeric_students/pyman](https://github.com/phaustin/numeric_students/tree/downloads/pyman) folder.
  - If you are new to python, I would recommend you also go over the
    following short ebook in detail:
      - Jake Vanderplas' [Whirlwind tour of
        Python](https://github.com/jakevdp/WhirlwindTourOfPython/blob/f40b435dea823ad5f094d48d158cc8b8f282e9d5/Index.ipynb)
        is available both as a set of notebooks which you can clone from
        github or as a free ebook:
        <http://www.oreilly.com/programming/free/a-whirlwind-tour-of-python.csp>
          - to get the notebooks do:
            
            git clone <https://github.com/jakevdp/WhirlwindTourOfPython>
  - We will be referencing chapters from:
      - A Springer ebook from the UBC library: [Numerical
        Python](https://login.ezproxy.library.ubc.ca/login?qurl=https%3a%2f%2flink.springer.com%2fopenurl%3fgenre%3dbook%26isbn%3d978-1-4842-0554-9)
          - with code on github:
            
            git clone
            <https://github.com/jrjohansson/numerical-python-book-code>
  - Two other texts that are available as a set of notebooks you can
    clone with git:
      - <https://github.com/fangohr/introduction-to-python-for-computational-science-and-engineering>
      - <https://github.com/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/Index.ipynb>
  - My favorite O'Reilly book is:
      - [Python for Data
        Analysis](http://shop.oreilly.com/product/0636920023784.do)
  - Some other resources:
      - If you know Matlab, there is [Numpy for Maltab
        users](http://wiki.scipy.org/NumPy_for_Matlab_Users)
      - Here is a [python
        translation](http://nbviewer.jupyter.org/gist/phaustin/1af744215e51562d010b9f6a19c0724c)
        by [Don
        MacMillen](http://blogs.siam.org/from-matlab-guide-to-ipython-notebook/)
        of [Chapter 1 of his matlab
        guide](http://clouds.eos.ubc.ca/~phil/courses/atsc301/downloads_pw/matlab_guide_2nd.pdf)
      - [Python data structure cheat
        sheet](pdfs/Python-data-manipulations.pdf)
      - [Numpy beginners
        guide](http://www.packtpub.com/numpy-mathematical-2e-beginners-guide/book)
      - [Learning
        Ipython](http://www.packtpub.com/learning-ipython-for-interactive-computing-and-data-visualization/book)
      - [The official Python
        tutorial](http://docs.python.org/tut/tut.html)
      - [Numpy
        cookbook](http://www.packtpub.com/numpy-for-python-cookbook/book)
      - A general computing introduction: [How to think like a computer
        scientist](http://www.openbookproject.net/thinkcs/python/english3e)
        with an [interactive
        version](http://interactivepython.org/courselib/static/thinkcspy/index.html)
      - [Think Stats](http://greenteapress.com/wp/think-stats-2e/)
      - [Think Bayes](http://greenteapress.com/wp/think-bayes/)

```{code-cell} ipython3

```
