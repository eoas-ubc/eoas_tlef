# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: true
#     sideBar: true
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: true
#     toc_position: {}
#     toc_section_display: true
#     toc_window_display: true
# ---

# %% [markdown] {"toc": true}
# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#First-Steps" data-toc-modified-id="First-Steps-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>First Steps</a></span><ul class="toc-item"><li><span><a href="#Installing-Python-on-your-computer" data-toc-modified-id="Installing-Python-on-your-computer-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Installing Python on your computer</a></span><ul class="toc-item"><li><span><a href="#Launching-IPython" data-toc-modified-id="Launching-IPython-1.1.1"><span class="toc-item-num">1.1.1&nbsp;&nbsp;</span>Launching IPython</a></span></li><li><span><a href="#Testing-your-installation-of-Python" data-toc-modified-id="Testing-your-installation-of-Python-1.1.2"><span class="toc-item-num">1.1.2&nbsp;&nbsp;</span>Testing your installation of Python</a></span></li></ul></li><li><span><a href="#IPython-Basics" data-toc-modified-id="IPython-Basics-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>IPython Basics</a></span><ul class="toc-item"><li><span><a href="#Magic-Functions" data-toc-modified-id="Magic-Functions-1.2.1"><span class="toc-item-num">1.2.1&nbsp;&nbsp;</span>Magic Functions</a></span></li><li><span><a href="#Navigation-Commands" data-toc-modified-id="Navigation-Commands-1.2.2"><span class="toc-item-num">1.2.2&nbsp;&nbsp;</span>Navigation Commands</a></span></li><li><span><a href="#More-Magic-Commands" data-toc-modified-id="More-Magic-Commands-1.2.3"><span class="toc-item-num">1.2.3&nbsp;&nbsp;</span>More Magic Commands</a></span></li><li><span><a href="#System-shell-commands" data-toc-modified-id="System-shell-commands-1.2.4"><span class="toc-item-num">1.2.4&nbsp;&nbsp;</span>System shell commands</a></span></li><li><span><a href="#Tab-completion" data-toc-modified-id="Tab-completion-1.2.5"><span class="toc-item-num">1.2.5&nbsp;&nbsp;</span>Tab completion</a></span></li><li><span><a href="#Recap-of-commands" data-toc-modified-id="Recap-of-commands-1.2.6"><span class="toc-item-num">1.2.6&nbsp;&nbsp;</span>Recap of commands</a></span></li></ul></li><li><span><a href="#Interactive-Python-as-a-calculator" data-toc-modified-id="Interactive-Python-as-a-calculator-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Interactive Python as a calculator</a></span><ul class="toc-item"><li><span><a href="#Binary-arithmetic-operations-in-Python" data-toc-modified-id="Binary-arithmetic-operations-in-Python-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>Binary arithmetic operations in Python</a></span></li><li><span><a href="#Types-of-numbers" data-toc-modified-id="Types-of-numbers-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Types of numbers</a></span></li></ul></li><li><span><a href="#Python-Modules" data-toc-modified-id="Python-Modules-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Python Modules</a></span></li><li><span><a href="#Python-functions:-a-first-look" data-toc-modified-id="Python-functions:-a-first-look-1.5"><span class="toc-item-num">1.5&nbsp;&nbsp;</span>Python functions: a first look</a></span><ul class="toc-item"><li><span><a href="#Some-NumPy-functions" data-toc-modified-id="Some-NumPy-functions-1.5.1"><span class="toc-item-num">1.5.1&nbsp;&nbsp;</span>Some NumPy functions</a></span></li><li><span><a href="#Keyword-arguments" data-toc-modified-id="Keyword-arguments-1.5.2"><span class="toc-item-num">1.5.2&nbsp;&nbsp;</span>Keyword arguments</a></span></li></ul></li><li><span><a href="#Variables" data-toc-modified-id="Variables-1.6"><span class="toc-item-num">1.6&nbsp;&nbsp;</span>Variables</a></span><ul class="toc-item"><li><span><a href="#Names-and-the-assignment-operator" data-toc-modified-id="Names-and-the-assignment-operator-1.6.1"><span class="toc-item-num">1.6.1&nbsp;&nbsp;</span>Names and the assignment operator</a></span></li><li><span><a href="#Legal-and-recommended-variable-names" data-toc-modified-id="Legal-and-recommended-variable-names-1.6.2"><span class="toc-item-num">1.6.2&nbsp;&nbsp;</span>Legal and recommended variable names</a></span></li><li><span><a href="#Reserved-words-in-Python" data-toc-modified-id="Reserved-words-in-Python-1.6.3"><span class="toc-item-num">1.6.3&nbsp;&nbsp;</span>Reserved words in Python</a></span></li></ul></li><li><span><a href="#Script-files-and-programs" data-toc-modified-id="Script-files-and-programs-1.7"><span class="toc-item-num">1.7&nbsp;&nbsp;</span>Script files and programs</a></span><ul class="toc-item"><li><span><a href="#Scripting-Example-1" data-toc-modified-id="Scripting-Example-1-1.7.1"><span class="toc-item-num">1.7.1&nbsp;&nbsp;</span>Scripting Example 1</a></span></li><li><span><a href="#Scripting-Example-2" data-toc-modified-id="Scripting-Example-2-1.7.2"><span class="toc-item-num">1.7.2&nbsp;&nbsp;</span>Scripting Example 2</a></span></li></ul></li><li><span><a href="#Importing-Modules" data-toc-modified-id="Importing-Modules-1.8"><span class="toc-item-num">1.8&nbsp;&nbsp;</span>Importing Modules</a></span></li><li><span><a href="#Getting-help:-documentation-in-IPython-shell" data-toc-modified-id="Getting-help:-documentation-in-IPython-shell-1.9"><span class="toc-item-num">1.9&nbsp;&nbsp;</span>Getting help: documentation in IPython shell</a></span></li><li><span><a href="#Programming-is-a-detail-oriented-activity" data-toc-modified-id="Programming-is-a-detail-oriented-activity-1.10"><span class="toc-item-num">1.10&nbsp;&nbsp;</span>Programming is a detail-oriented activity</a></span></li><li><span><a href="#Exercises" data-toc-modified-id="Exercises-1.11"><span class="toc-item-num">1.11&nbsp;&nbsp;</span>Exercises</a></span></li></ul></li></ul></div>

# %% [markdown]
# python
#
# First Steps
# ===========
#
# Installing Python on your computer
# ----------------------------------
#
# If you haven't already installed Python on your computer, see `apdx1` ,
# which includes instructions for installing Python on Macs running under
# MacOSX and on PCs running under Windows.
#
# single: miniconda
#
# ### Launching IPython
#
# Once you have installed Python, open a shell and at the prompt type:
#
#     $ cd ~
#     $ mkdir testfold
#     $ cd testfold
#
# which will make a new directory called testfold and change into it.
#
# By typing short commands at the prompt, IPython can be used to perform
# various system tasks, such as running programs and creating and moving
# files around on your computer. This is a different kind of computer
# interface than the icon-based interface (or "graphical user interface"
# GUI) that you usually use to communicate with your computer. While it
# may seem more cumbersome for some tasks, it can be more powerful for
# other tasks, particularly those associated with programming.
#
# Before getting started, we point out that like most modern computer
# languages, Python is *case sensitive*. That is, Python distinguishes
# between upper and lower case letters. Thus, two words spelled the same
# but having different letters capitalized are treated as different names
# in Python. Keep that in mind as we introduce different commands.
#
# ### Testing your installation of Python
#
# Running the Python program below tests your installation of Python to
# verify that the installation was successful. In particular, it tests
# that the NumPy, SciPy, and MatPlotLib libraries that are needed for this
# manual are properly installed. Now that you are in directory testfold,
# start a python session with:
#
#     $jupyter  qtconsole &
#
# The '&' at the end 'backgrounds' the session and gives you back the bash
# prompt so you can type further commands.
#
# Launch atom from the command line with the empty file name
# test\_python.py:
#
#     $ atom test_python.py
#
# Copy these lines into test\_python.py You should input your first and
# last names inside the single quotes on lines 15 and 16, respectively.
# Save this file in atom.
#
# ``` python
# # This code tests that your Python installation worked.
# # It generates a png image file that you should e-mail 
# # to the address shown on the plot
# import scipy 
# import numpy 
# import matplotlib 
# import matplotlib.pyplot as plt 
# import platform 
# import socket
#
# # If you are a student, please fill in your first and last
# # names inside the quotes in the two lines below.  Do not
# # modify anything else in this file
#
# your_first_name = 'First' 
# your_last_name = 'Last'
#
# # If you are an instructor, modify the next 3 lines.
# # You do not need to modify anything else in this file.
#
# classname = 'ATSC 301'
# term = 'Fall_2016'      # must contain no spaces
# email = 'paustin@eos.ubc.ca'
#
# plt.plot([0,1], 'r', [1,0], 'b')
# plt.text( 0.5, 0.8, '{0:s} {1:s}'
#         .format(your_first_name, your_last_name), 
#         horizontalalignment='center',
#         size = 'x-large',
#         bbox=dict(facecolor='purple', alpha=0.4))
# plt.text( 0.5, 0.1,
#     '{1:s}\nscipy {2:s}\nnumpy {3:s}\nmatplotlib {4:s}\non {5:s}\n{6:s}'
#         .format( 
#         classname,
#         term,
#         scipy.__version__, 
#         numpy.__version__, 
#         matplotlib.__version__, 
#         platform.platform(), 
#         socket.gethostname() 
#         ) ,
#     horizontalalignment='center'
#     )
# filename = your_last_name + '_' + your_first_name + '_' + term + '.png'
# plt.title('*** E-mail the saved version of this plot, ***\n' +
#     '"{0:s}" to {1:s}'.format(filename, email), fontsize=12)
# plt.savefig(filename)
# plt.show()
# ```
#
# To run your saved file go to the IPython window and at the prompt type:
#
#     run test_python
#
# which should produce a plot that looks something like this:
#
# ![image](attachment:screenshots/inline_plot.png)
#
# To save this as a png file, type:
#
#     %matplotlib qt4
#
# which switches from inline graphics to graphics that appear in a
# separate window. Type:
#
#     run test_python
#
# again to get a windowed plot
#
# ![image](attachment:screenshots/qt4_window.png)
#
# Clicking on the floppy disk icon should prompt you for a file name to
# save the figure into.
#
# IPython Basics
# --------------
#
# ### Magic Functions
#
# pair: IPython; magic functions
#
# IPython features a number of commands called "magic" commands that let
# you perform various useful tasks. There are two types of magic commands,
# line magic commands that begin with `%`---these are executed on a single
# line---and cell magic commands that begin with `%%`---these are executed
# on several lines. Here we will concern ourselves only with line magic
# commands.
#
# The first thing to know about magic commands is that you can toggle
# (turn on and off) the need to use the `%` prefix for line magic commands
# by typing `%automagic`. By default, the `Automagic` switch is set to
# `ON` so you don't need the `%` prefix. To set `Automagic` to `OFF`,
# simply type `%automagic` at the IPython prompt. Cell magic commands
# always need the `%%` prefix.
#
# In what follows below, we assume that the `Automagic` switch is set to
# `ON` so we omit the `%` sign.
#
# single: IPython; navigation commands
#
# ### Navigation Commands
#
# IPython recognizes several common navigation commands that are used
# under the Unix/Linux operating systems. In the IPython shell, these few
# commands work on Macs, PCs, and Linux machines.
#
# At the IPython prompt, type `cd ~` (*i.e.* "`cd`" -- "space" -- "tilde"
# , where tilde is found near the upper left part of most keyboards). This
# will set your computer to its home (default) directory. Next type `pwd`
# (**p**rint **w**orking **d**irectory) and press RETURN. The console
# should return the name of the current directory of your computer. It
# might look like this on a Mac:
#
# ``` ipython
# In [2]: pwd
# Out[2]: u'/Users/phil'
# ```
#
# or this on a PC:
#
# ``` ipython
# In [3]: pwd
# Out[3]: C:\\Users\\phil
# ```
#
# The responses `Out[2]: u'/Users/phil'` for the Mac and
# `Out[3]: C:\\Users\\phil` for the PC mean the the current directory is
# `phil`, which is a subdirectory of `Users`. Taken together `/Users/phil`
# on a Mac or `C:\\Users\\phil` on a PC is known as the *path* of the
# current directory. The path is just the name of a directory and the
# sequence of subdirectories in which it resides up to the *root*
# directory.
#
# Typing `cd ..` ("`cd`" -- "space" -- two periods) moves the IPython
# shell up one directory in the directory tree, as illustrated by the set
# of commands below.
#
# ``` ipython
# In [4]: cd ..
# /Users
#
# In [5]: pwd
# Out[5]: u'/Users'
# ```
#
# The directory moved up one from `/Users/phil` to `/Users`. Now type `ls`
# (**l**i**s**t) and press `RETURN`. The console should list the names of
# the files and subdirectories in the current directory.
#
# ``` ipython
# In [6]: ls
# Shared/    phil/
# ```
#
# In this case, there are only two directories (indicated by the slash)
# and not files. Type `cd ~` again to return to your home directory and
# then type `pwd` to verify where you are in your directory tree.
# \[Technically, `ls` isn't a magic command, but typing it without the `%`
# sign lists the contents of the current directory, irrespective of
# whether `Automagic` is `ON` or `OFF`.\]
#
# Let's create a directory within your documents directory that you can
# use to store your Python programs. We will call it `PyProgs`. First,
# return to your home directory by typing `cd ~`. To create directory
# `PyProgs`, type `mkdir PyProgs` (**m**a**k**e **dir**ectory). Type `ls`
# to confirm that you have created `PyProgs` and then type `cd PyProgs` to
# switch to that directory.
#
# Now let's say you want to return to the previous subdirectory,
# `Documents` or `My Documents`, which should be one up in the directory
# tree if you have followed along. Type `cd ..` and then type `pwd`. You
# should find that you are back in the previous directory, `Documents` or
# `My Documents`. If you type `ls`, you should see the new directory
# `PyProgs` that you just created.
#
# ### More Magic Commands
#
# single: IPython; magic commands
#
# The most important magic command is `%run` *filename* where *filename*
# is the name of a Python program you have created. We haven't done this
# yet but include it here just for reference. We will come back to this
# later.
#
# Some other useful magic commands include `%hist`, which lists the recent
# commands issued to the IPython terminal, and `%edit`, which opens a new
# empty file in the code editor window. Typing `%edit` *filename*, will
# open the file *filename* if it exists in the current directory, or it
# will create a new file by that name if it does not, and will open it as
# a blank file in the code editor window.
#
# There are a number of other magic commands. You can get a list of them
# by typing `lsmagic`.
#
# ``` ipython
# In [7]: lsmagic
# Available line magics:
# %alias  %alias_magic  %autocall  %automagic  %bookmark  %cd
# %clear  %colors  %config  %connect_info  %debug  %dhist  %dirs
# %doctest_mode  %ed  %edit  %env  %gui  %guiref  %hist  %history
# %install_default_config  %install_ext  %install_profiles
# %killbgscripts  %less  %load  %load_ext  %loadpy  %logoff  %logon
# %logstart %logstate  %logstop  %lsmagic  %macro  %magic  %man
# %more  %notebook  %page  %pastebin  %pdb  %pdef  %pdoc  %pfile
# %pinfo  %pinfo2  %popd  %pprint  %precision  %profile  %prun
# %psearch  %psource  %pushd  %pwd  %pycat  %pylab  %qtconsole
# %quickref  %recall  %rehashx  %reload_ext  %rep  %rerun  %reset
# %reset_selective  %run  %save  %sc  %store  %sx  %system  %tb
# %time  %timeit  %unalias  %unload_ext  %who  %who_ls  %whos
# %xdel  %xmode
#
# Available cell magics:
# %%!  %%bash  %%capture  %%file  %%javascript  %%latex  %%perl
# %%prun  %%pypy %%python  %%python3  %%ruby  %%script  %%sh  %%svg
# %%sx  %%system  %%timeit
#
# Automagic is ON, % prefix IS NOT needed for line magics.
# ```
#
# There are a lot of magic commands, most of which we don't need right
# now. We will introduce them in the text as needed.
#
# ### System shell commands
#
# single: IPython; system shell commands
#
# You can also run system shell commands from the IPython shell by typing
# `!` followed by a system shell command. For Macs running OSX and for
# Linux machines, this means that Unix (or equivalently Linux) commands
# can be issued from the IPython prompt. For PCs, this means that Windows
# (DOS) commands can be issued from the IPython prompt. For example,
# typing `!ls` (**l**i**s**t) and pressing RETURN lists all the files in
# the current directory on a Mac. Typing `!dir` on a PC does essentially
# the same thing (note that system shell commands in Windows are *not*
# case sensitive).
#
# pair: IPython; tab completion
#
# ### Tab completion
#
# IPython also incorporates a number of shortcuts that make using the
# shell more efficient. One of the most useful is **tab completion**.
# Let's assume you have been following along and that your are in the
# directory `Documents` or `My Documents`. To switch to the directory
# `PyProgs`, you could type `cd PyProgs`. Instead of doing that, type
# `cd PyP` and then press the `TAB` key. This will complete the command,
# provided there is no ambiguity in how to finish the command. In the
# present case, that would mean that there was no other subdirectory
# beginning with `PyP`. Tab completion works with any command you type
# into the IPython terminal. Try it out! It will make your life more
# wonderful.
#
# A related shortcut involves the $\uparrow$ key. If you type a command,
# say `cd` and then to press the $\uparrow$ key, IPython will complete the
# `cd` command with the last instance of that command. Thus, when you
# launch IPython, you can use this shortcut to take you to the directory
# you used when you last ran IPython.
#
# You can also simply press the $\uparrow$ key, which will simply recall
# the most recent command. Repeated application of the $\uparrow$ key
# scrolls though the most recent commands in reverse order. The
# $\downarrow$ key can be used to scroll in the other direction.
#
# ### Recap of commands
#
# Let's recap the (magic) commands introduced above:
#
# > `pwd`:  
# > (**p**rint **w**orking **d**irectory) Prints the path of the current
# > directory.
# >
# > `ls`:  
# > (**l**i**s**t) Lists the names of the files and directories located in
# > the current directory.
# >
# > `mkdir` *filename*:  
# > (**m**a**k**e **dir**ectory) Makes a new directory *filename*.
# >
# > `cd` *directoryname*:  
# > (**c**hange **d**irectory) Changes the current directory to
# > *directoryname*. Note: for this to work, *directoryname* must be a
# > subdirectory in the current directory. Typing `cd ~` changes to the
# > home directory of your computer. Typing `cd ..` moves the console one
# > directory up in the directory tree.
# >
# > `clear`:  
# > Clears the IPython screen of previous commands.
# >
# > `run` *filename*:  
# > Runs (executes) a Python script. Described later in the section
# > `chap2:ScriptExmp1`
# >
# > Tab completion:  
# > Provides convenient shortcuts, with or without the arrow keys, for
# > executing commands in the IPython shell.
#
# Interactive Python as a calculator
# ----------------------------------
#
# You can use the IPython shell to perform simple arithmatic calculations.
# For example, to find the product $3\times 15$, you type `3*15` at the
# `In` prompt and press `RETURN`:
#
# ``` ipython
# In [1]: 3*15
# Out[1]: 45
# ```
#
# Python returns the correct product, as expected. You can do more
# complicated calculations:
#
# ``` ipython
# In [2]: 6+21/3
# Out[2]: 13.0
# ```
#
# Let's try some more arithmetic:
#
# ``` ipython
# In [3]: (6+21)/3
# Out[3]: 9.0
# ```
#
# Notice that the effect of the parentheses in `In [3]: (6+21)/3` is to
# cause the addition to be performed first and then the division. Without
# the parentheses, Python will always perform the multiplication and
# division operations *before* performing the addition and subtraction
# operations. The order in which arithmetic operations are performed is
# the same as for most calculators: exponentiation first, then
# multiplication or division, then addition or subtraction, then left to
# right.
#
# ### Binary arithmetic operations in Python
#
# The table below lists the binary arithmatic operations in Python. It has
# all the standard binary operators for arithmetic, plus a few you may not
# have seen before.
#
# > <table style="width:75%;">
# > <colgroup>
# > <col style="width: 25%" />
# > <col style="width: 15%" />
# > <col style="width: 16%" />
# > <col style="width: 18%" />
# > </colgroup>
# > <thead>
# > <tr class="header">
# > <th><strong>Operation</strong></th>
# > <th><strong>Symbol</strong></th>
# > <th><strong>Example</strong></th>
# > <th><strong>Output</strong></th>
# > </tr>
# > </thead>
# > <tbody>
# > <tr class="odd">
# > <td>addition</td>
# > <td><code>+</code></td>
# > <td><code>12+7</code></td>
# > <td><code>19</code></td>
# > </tr>
# > <tr class="even">
# > <td>subtraction</td>
# > <td><code>-</code></td>
# > <td><code>12-7</code></td>
# > <td><code>5</code></td>
# > </tr>
# > <tr class="odd">
# > <td>multiplication</td>
# > <td><code>*</code></td>
# > <td><code>12*7</code></td>
# > <td><code>84</code></td>
# > </tr>
# > <tr class="even">
# > <td>division</td>
# > <td><code>/</code></td>
# > <td><code>12/7</code></td>
# > <td><code>1.714285</code></td>
# > </tr>
# > <tr class="odd">
# > <td>floor division</td>
# > <td><code>//</code></td>
# > <td><code>12//7</code></td>
# > <td><code>1</code></td>
# > </tr>
# > <tr class="even">
# > <td>remainder</td>
# > <td><code>%</code></td>
# > <td><code>12%7</code></td>
# > <td><code>5</code></td>
# > </tr>
# > <tr class="odd">
# > <td>exponentiation</td>
# > <td><code>**</code></td>
# > <td><code>12**7</code></td>
# > <td><code>35831808</code></td>
# > </tr>
# > </tbody>
# > </table>
# >
# *Floor division*, designated by the symbols `//`, means divide and keep
# only the integer part without rounding. *Remainder*, designated by the
# symbols `%`, gives the remainder of after a floor division.
#
# Warning
#
# Integer division is different in Python 2 and 3
#
# integer division; Python 2 and 3 differences
#
# One peculiarity of all versions of Python prior to version 3 is that
# dividing two integers by each other yields the "floor division"
# result---another integer. Therefore `12/7` yields `1` whereas `12./7` or
# `12/7.` or `12./7.` all yield `1.714285`. Starting with version 3 of
# Python, all of the above expressions, including `3/2` yield `1.714285`.
# Unfortunately, we are using version 2.7 of Python so `12/7` yields `1`.
# You can force versions of Python prior to version 3 to divide integers
# like version 3 does by typing
#
# ``` ipython
# from __future__ import division
# ```
#
# at the beginning of an IPython session. You only need to type it once
# and it works for the entire session.
#
# ### Types of numbers
#
# There are four different types of numbers in Python: plain integers,
# long integers, floating point numbers, and complex numbers.
#
# **Plain integers**, or simply **integers**, are 32 bits (binary digits)
# long, which means they extend from $-2^{31}=-2147483648$ to
# $2^{31}-1=2147483647$. One bit is used to store the sign of the integer
# so there are only 31 bits left---hence, the power of 31. In Python, a
# number is automatically treated as an integer if is written without a
# decimal point and it is within the bounds given above. This means that
# `23`, written without a decimal point, is an integer and `23.`, written
# with a decimal point, is a floating point number. If an integer extends
# beyond the bounds of a simple integer, the it becomes a **long
# integer**, and is designated as such by an `L` following the last digit.
# Here are some examples of integer arithmetic:
#
# ``` ipython
# In [4]: 12*3
# Out[4]: 36
#
# In [5]: 4+5*6-(21*8)
# Out[5]: -134
#
# In [6]: 11/5
# Out[6]: 2.2
#
# In [7]: 11//5
# Out[7]: 2
#
# In [8]: 9734828*79372    # product of these two large integers
# Out[8]: 772672768016L    # is a long integer
# ```
#
# For the binary operators `+`, `-`, `*`, and `//`, the output is an
# integer if the inputs are integers. The only exception is if the result
# of the calculation is out of the bounds of Python integers, in which
# case Python automatically converts the result to a long integer. The
# output of the division operator `/` is a floating point as of version 3
# of Python. If an integer output is desired when two integers are
# divided, the floor division operator `//` must be used.
#
# **Floating point** numbers are essentially rational numbers and can have
# a fractional part; integers, by their very nature, have no fractional
# part. In most versions of Python running on PCs or Macs, floating point
# numbers go between approximately $\pm 2 \times 10^{-308}$ and
# $\pm 2 \times 10^{308}$. Here are some examples of floating point
# arithmetic:
#
# ``` ipython
# In [9]: 12.*3.
# Out[9]: 36.0
#
# In [10]: 123.4*(-53.9)/sqrt(5.)
# Out[10]: -2974.5338992050501
#
# In [11]: 11./5.
# Out[11]: 2.2
#
# In [12]: 11.//5.
# Out[12]: 2.0
#
# In [13]: 11.%5.
# Out[13]: 1.0
#
# In [14]: 6.022e23*300.
# Out[14]: 1.8066e+26
# ```
#
# Note that the result of any operation involving only floating point
# numbers as inputs is a real number, even in the cases where the floor
# division `//` or remainder `%` operators are used. The last output also
# illustrates an alternative way of writing floating point numbers as a
# mantissa followed by and `e` or `E` followed by a power of 10: so
# 1.23e-12 is equivalent to $1.23 \times 10^{-12}$.
#
# We also sneaked into our calculations `sqrt`, the square root function.
# We will have more to say about functions in a few pages.
#
# **Complex numbers** are written in Python as a sum of a real and
# imaginary part. For example, the complex number $3-2i$ is represented as
# `3-2j` in Python where `j` represents $\sqrt{-1}$. Here are some
# examples of complex arithmetic:
#
# ``` ipython
# In [15]: (2+3j)*(-4+9j)
# Out[15]: (-35+6j)
#
# In [16]: (2+3j)/(-4+9j)
# Out[16]: (0.1958762886597938-0.3092783505154639j)
#
# In [17]: sqrt(-3)
# Out[17]: nan
#
# In [18]: sqrt(-3+0j)
# Out[18]: 1.7320508075688772j
# ```
#
# Notice that to obtain the expected result or $\sqrt{-3}$, you must write
# the argument of the square root function as a complex number. Otherwise,
# Python returns `nan` (not a number).
#
# If you multiply an integer by a floating point number, the result is a
# floating point number. Similarly, if you multiply a floating point
# number by a complex number, the result is a complex number. Python
# always promotes the result to the most complex of the inputs.
#
# single: Python; module pair: module; NumPy pair: module; SciPy pair:
# module; MatPlotLib
#
# Python Modules
# --------------
#
# The Python computer language consists of a "core" language plus a vast
# collection of supplementary software that is contained in **modules**.
# Many of these modules come with the standard Python distribution and
# provide added functionality for performing computer system tasks. Other
# modules provide more specialized capabilities that not every user may
# want. You can think of these modules as a kind of library from which you
# can borrow according to your needs.
#
# We will need three Python modules that are not part of the core Python
# distribution, but are nevertheless widely used for scientific computing.
# The three modules are
#
# > NumPy  
# > is the standard Python package for scientific computing with Python.
# > It provides the all-important `array` data structure, which is at the
# > very heart of NumPy. In also provides tools for creating and
# > manipulating arrays, including indexing and sorting, as well as basic
# > logical operations and element-by-element arithmetic operations like
# > addition, subtraction, multiplication, division, and exponentiation.
# > It includes the basic mathematical functions of trigonometry,
# > exponentials, and logarithms, as well vast collection of special
# > functions (Bessel functions, *etc.*), statistical functions, and
# > random number generators. It also includes a large number of linear
# > algebra routines that overlap with those in SciPy, although the SciPy
# > routines tend to be more complete. You can find more information about
# > NumPy at <http://docs.scipy.org/doc/numpy/reference/index.html>.
# >
# > SciPy  
# > provides a wide spectrum of mathematical functions and numerical
# > routines for Python. SciPy makes extensive use of NumPy arrays so when
# > you import SciPy, you should always import NumPy too. In addition to
# > providing basic mathematical functions, SciPy provides Python
# > "wrappers" for numerical software written in other languages, like
# > Fortran, C, or C++. A "wrapper" provides a transparent easy-to-use
# > Python interface to standard numerical software, such as routines for
# > doing curve fitting and numerically solving differential equations.
# > SciPy greatly extends the power of Python and saves you the trouble of
# > writing software in Python that someone else has already written and
# > optimized in some other language. You can find more information about
# > SciPy at <http://docs.scipy.org/doc/scipy/reference/>.
# >
# > MatPlotLib  
# > is the standard Python package for making two and three dimensional
# > plots. MatPlotLib makes extensive use of NumPy arrays. You will make
# > all of your plots in Python using this package. You can find more
# > information about MatPlotLib at <http://MatPlotLib.sourceforge.net/>.
#
# We will use these three modules extensively and therefore will provide
# introductions to their capabilities as we develop Python in this manual.
# The links above provide much more extensive information and you will
# certainly want to refer to them from time to time.
#
# These modules, NumPy, MatPlotLib, and SciPy, are built into the IPython
# shell so we can use them freely in that environment. Later, when we
# introduce Python programs (or scripts), we will see that in those cases
# you must explicitly load these modules using the `import` command to
# have access to them.
#
# Finally, we note that you can write your own Python modules. They are a
# convenient way of packaging and storing Python code so that you can
# reuse it. We defer learning about how to write modules until after we
# have learned about Python.
#
# Python functions: a first look
# ------------------------------
#
# A function in Python is similar to a mathematical function. In consists
# of a name and one or more arguments contained inside parentheses, and it
# produces some output. For example, the NumPy function `sin(x)`
# calculates the sine of the number `x` (where `x` is expressed in
# radians). Let's try it out in the IPython shell:
#
# ``` ipython
# In [1]: sin(0.5)
# Out[1]: 0.47942553860420301
# ```
#
# The argument of the function can be a number or any kind of expression
# whose output produces a number. For example, the function `log(x)`
# calculates the natural logarithm of `x`. All of the following
# expressions are legal and produce the expected output:
#
# ``` ipython
# In [2]: log(sin(0.5))
# Out[2]: -0.73516668638531424
#
# In [3]: log(sin(0.5)+1.0)
# Out[3]: 0.39165386283471759
#
# In [4]: log(5.5/1.2)
# Out[4]: 1.5224265354444708
# ```
#
# pair: NumPy; functions
#
# ### Some NumPy functions
#
# pair: NumPy; functions
#
# NumPy includes an extensive library of mathematical functions. In the
# table below, we list some of the most useful ones. A much more complete
# list is available at
# <http://docs.scipy.org/doc/numpy/reference/ufuncs.html#math-operations>.
#
# > <table>
# > <colgroup>
# > <col style="width: 22%" />
# > <col style="width: 77%" />
# > </colgroup>
# > <thead>
# > <tr class="header">
# > <th><strong>Function</strong></th>
# > <th><strong>Description</strong></th>
# > </tr>
# > </thead>
# > <tbody>
# > <tr class="odd">
# > <td><code>sqrt(x)</code></td>
# > <td>Square root of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="even">
# > <td><code>exp(x)</code></td>
# > <td>Exponential of x, <em>i.e.</em> <span class="math inline"><em>e</em><sup><em>x</em></sup></span></td>
# > </tr>
# > <tr class="odd">
# > <td><code>log(x)</code></td>
# > <td>Natural log of x, <em>i.e.</em> <span class="math inline">ln <em>x</em></span></td>
# > </tr>
# > <tr class="even">
# > <td><code>log10(x)</code></td>
# > <td>Base 10 log of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="odd">
# > <td><code>degrees(x)</code></td>
# > <td>Converts <span class="math inline"><em>x</em></span> from radians to degrees</td>
# > </tr>
# > <tr class="even">
# > <td><code>radians(x)</code></td>
# > <td>Converts <span class="math inline"><em>x</em></span> from degrees to radians</td>
# > </tr>
# > <tr class="odd">
# > <td><code>sin(x)</code></td>
# > <td>Sine of <span class="math inline"><em>x</em></span> (<span class="math inline"><em>x</em></span> in radians)</td>
# > </tr>
# > <tr class="even">
# > <td><code>cos(x)</code></td>
# > <td>Cosine <span class="math inline"><em>x</em></span> (<span class="math inline"><em>x</em></span> in radians)</td>
# > </tr>
# > <tr class="odd">
# > <td><code>tan(x)</code></td>
# > <td>Tangent <span class="math inline"><em>x</em></span> (<span class="math inline"><em>x</em></span> in radians)</td>
# > </tr>
# > <tr class="even">
# > <td><code>arcsin(x)</code></td>
# > <td>Arc sine (in radians) of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="odd">
# > <td><code>arccos(x)</code></td>
# > <td>Arc cosine (in radians) of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="even">
# > <td><code>arctan(x)</code></td>
# > <td>Arc tangent (in radians) of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="odd">
# > <td><code>fabs(x)</code></td>
# > <td>Absolute value of <span class="math inline"><em>x</em></span></td>
# > </tr>
# > <tr class="even">
# > <td><code>round(x)</code></td>
# > <td>Rounds a float to nearest integer</td>
# > </tr>
# > <tr class="odd">
# > <td><code>floor(x)</code></td>
# > <td>Rounds a float <em>down</em> to nearest integer</td>
# > </tr>
# > <tr class="even">
# > <td><code>ceil(x)</code></td>
# > <td>Rounds a float <em>up</em> to nearest integer</td>
# > </tr>
# > <tr class="odd">
# > <td><code>sign(x)</code></td>
# > <td>-1 if <span class="math inline"><em>x</em> &lt; 0</span>, +1 if <span class="math inline"><em>x</em> &gt; 0</span>, 0 if <span class="math inline"><em>x</em> = 0</span></td>
# > </tr>
# > </tbody>
# > </table>
# >
# The functions discussed here all have one input and one output. Python
# functions can, in general, have multiple inputs and multiple outputs. We
# will discuss these and other features of functions later when we take up
# functions in the context of user-defined functions.
#
# ### Keyword arguments
#
# In addition to regular arguments, Python functions can have keyword
# arguments (`kwargs`). Keyword arguments are *optional* arguments that
# need not be specified when a function is called. See
# `chap5BasicPlotting` for examples of the use of keyword arguments. For
# the moment, we don't need them so we defer a full discussion of keyword
# arguments until we introduce them in the section on `userDefdFuncs`.
#
# Variables
# ---------
#
# ### Names and the assignment operator
#
# single: variable single: assignment operator
#
# A variable is a name that is used to store data. It can be used to store
# different kinds of data, but here we consider the simplest case where
# the data is a single numerical value. Here are a few examples:
#
# ``` ipython
# In [1]: a = 23
#
# In [2]: p, q = 83.4, sqrt(2)
# ```
#
# The equal sign "`=`" is the *assignment operator*. In the first
# statement, it assigns the value of 23 to the variable `a`. In the second
# statement it assigns a value of 83.4 to `p` and a value of
# 1.4142135623730951 to `q`. To be more precise, the name of a variable,
# such as `a`, is associated with a *memory location* in your computer;
# the assignment variable tells the computer to put a particular piece of
# data, in this case a numerical value, in that memory location. Note that
# Python stores the *numerical value*, not the expression used to generate
# it. Thus, `q` is assigned the 17-digit number 1.4142135623730951
# generated by evaluating the expression `sqrt(2)`, *not* with $\sqrt{2}$.
# (Actually the value of `q` is stored as a binary, base 2, number using
# scientific notation with a mantissa and an exponent.)
#
# Suppose we write
#
# ``` ipython
# In [3]: b = a
# ```
#
# In this case Python associates a new memory location with the name `b`,
# distinct from the one associated with `a`, and sets the value stored at
# that memory location to 23, the value of `a`. The following sequence of
# statements demonstrate that fact. Can you see how? Notice that simply
# typing a variable name and pressing `Return` prints out the value of the
# variable.
#
# ``` ipython
# In [4]: a=23
#
# In [5]: b=a
#
# In [6]: a
# Out[6]: 23
#
# In [7]: b
# Out[7]: 23
#
# In [8]: a=12
#
# In [9]: a
# Out[9]: 12
#
# In [10]: b
# Out[10]: 23
# ```
#
# The assignment variable works from right to left; that is, it assigns
# the value of the number on the right to the variable name on the left.
# Therefore, the statement "`5=a`" makes no sense in Python. The
# assignment operator "`=`" in Python is not equivalent to the equals sign
# "$=$" we are accustomed to in algebra.
#
# The assignment operator can be used to increment or change the value of
# a variable
#
# ``` ipython
# In [11]: b = b+1
#
# In [12]: b
# Out[12]: 24 
# ```
#
# The statement, `b = b+1` makes no sense in algebra, but in Python (and
# most computer languages), it makes perfect sense: it means "add 1 to the
# current value of `b` and assign the result to `b`." This construction
# appears so often in computer programming that there is a special set of
# operators to perform such changes to a variable: `+=`, `-=`, `*=`, and
# `/=`. Here are some examples of how they work:
#
# ``` ipython
# In [13]: c , d = 4, 7.92
#
# In [14]: c += 2
#
# In [15]: c
# Out[15]: 6
#
# In [16]: c *= 3
#
# In [16]: c
# Out[16]: 18
#
# In [17]: d /= -2
#
# In [17]: d
# Out[17]: -3.96
#
# In [18]: d -= 4
#
# In [19]: d
# Out[19]: -7.96
# ```
#
# Verify that you understand how the above operations work.
#
# single: variable names
#
# ### Legal and recommended variable names
#
# Variable names in Python must start with a letter, and can be followed
# by as many alphanumeric characters as you like. Spaces are not allowed
# in variable names. However, the underscore character "`_`" is allowed,
# but no other character that is not a letter or a number is permitted.
#
# Recall that Python is *case sensitive*, so the variable `a` is distinct
# from the variable `A`.
#
# We recommend giving your variables descriptive names as in the following
# calculation:
#
# ``` ipython
# In [20]: distance = 34.
#
# In [21]: time_traveled = 0.59
#
# In [22]: velocity = distance/time_traveled
#
# In [23]: velocity
# Out[23]: 57.6271186440678
# ```
#
# The variable names `distance`, `time_traveled`, and `velocity`
# immediately remind you of what is being calculated here. This is good
# practice. But so is keeping variable names reasonably short, so don't go
# nuts!
#
# single: reserved words
#
# ### Reserved words in Python
#
# There are also some names or words that are reserved by Python for
# special purposes or functions. You must avoid using these names, which
# are provided here for your reference:
#
# > <table style="width:81%;">
# > <colgroup>
# > <col style="width: 18%" />
# > <col style="width: 16%" />
# > <col style="width: 15%" />
# > <col style="width: 15%" />
# > <col style="width: 15%" />
# > </colgroup>
# > <tbody>
# > <tr class="odd">
# > <td><code>and</code></td>
# > <td><code>del</code></td>
# > <td><code>from</code></td>
# > <td><code>not</code></td>
# > <td><code>while</code></td>
# > </tr>
# > <tr class="even">
# > <td><code>as</code></td>
# > <td><code>elif</code></td>
# > <td><code>global</code></td>
# > <td><code>or</code></td>
# > <td><code>with</code></td>
# > </tr>
# > <tr class="odd">
# > <td><code>assert</code></td>
# > <td><code>else</code></td>
# > <td><code>if</code></td>
# > <td><code>pass</code></td>
# > <td><code>yield</code></td>
# > </tr>
# > <tr class="even">
# > <td><code>break</code></td>
# > <td><code>except</code></td>
# > <td><code>import</code></td>
# > <td><code>print</code></td>
# > <td></td>
# > </tr>
# > <tr class="odd">
# > <td><code>class</code></td>
# > <td><code>exec</code></td>
# > <td><code>in</code></td>
# > <td><code>raise</code></td>
# > <td></td>
# > </tr>
# > <tr class="even">
# > <td><code>continue</code></td>
# > <td><code>finally</code></td>
# > <td><code>is</code></td>
# > <td><code>return</code></td>
# > <td></td>
# > </tr>
# > <tr class="odd">
# > <td><code>def</code></td>
# > <td><code>for</code></td>
# > <td><code>lambda</code></td>
# > <td><code>try</code></td>
# > <td></td>
# > </tr>
# > </tbody>
# > </table>
# >
# In addition, you should not use function names, like `sin`, `cos`, and
# `sqrt`, defined in the SciPy, NumPy, or any other library that you are
# using.
#
# single: scripts single: programs
#
# Script files and programs
# -------------------------
#
# Performing calculations in the IPython shell is handy if the
# calculations are short. But calculations quickly become tedious when
# they are more than a few lines long. If you discover you made a mistake
# at some early step, for example, you may have to go back and retype all
# the steps subsequent to the error. The solution to this problem is to
# save your code in a file. Saving code in a file means you can just
# correct the error and rerun the code without having to retype it. Saving
# code can also be useful if you want to reuse it later, perhaps with
# different inputs.
#
# When we save code in a computer file, we call the sequence of commands
# stored in the file a *script* or a *program* or sometimes a *routine*.
# Programs can become quite sophisticated and complex. Here we are only
# going to introduce the simplest features of programming by writing a
# very simple script. Much later, we will introduce some of the more
# advanced features of programming.
#
# single: Anaconda; Code Editor pair: Anaconda; tab completion
#
# To write a script you need a text editor. In principle, any text editor
# will do, but it's more convenient to use an editor that was designed for
# the task. We are going to use the **Code Editor** in the Spyder window
# that appears when you launch Spyder. This editor, like most good
# programming editors, provides syntax highlighting, which color codes key
# words, comments, and other features of the Python syntax according to
# their function, and thus makes it easier to read the code and easier to
# spot programming mistakes. The Canopy code editor also provides syntax
# checking, much like a spell-checker in a word processing program, that
# identifies many coding errors. This can greatly speed the coding
# process. Tab completion also work.
#
# ### Scripting Example 1
#
# Let's work through an example to see how scripting works. Suppose you
# are going on a road trip and you would like to estimate how long the
# drive will take, how much gas you will need, and the cost of the gas.
# It's a simple calculation. As inputs, you will need the distance of the
# trip, your average speed, the cost of gasoline, and the mileage of your
# car.
#
# Writing a script to do these calculations is straightforward. First,
# launch Spyder and open the code editor. Enter the following in the
# editor pane:
#
# ``` python
# # Calculates time, gallons of gas used, and cost of gasoline for
# # a trip
# distance = 400.         # miles
# mpg = 30.               # car mileage
# speed = 60.             # average speed
# costPerGallon = 4.10    # price of gas
#
# time = distance/speed
# gallons = distance/mpg
# cost = gallons*costPerGallon
# ```
#
# The number (or hash) symbol `#` is the "comment" character in Python;
# anything on a line following `#` is ignored when the code is executed.
# Judicious use of comments in your code will make your code much easier
# to understand days, weeks, or months after the time you wrote it. Use
# comments generously.
#
# Python ignores blank spaces or "white space" as it is sometimes called.
# The statement `costPerGallon = 4.10` in the above program could equally
# well be written as `costPerGallon=4.10` without the spaces before and
# after the `=` assignment operator; either way the statement means the
# same thing. Similarly, the white space after `costPerGallon = 4.10` but
# before the comment (hash) symbol is also ignored by Python. The idea is
# that you should use white space to make your program more readable.
#
# Now you are ready to run the code.
#
# ``` ipython
# In [1]: cd ~/Documents/PyProgs/
# ```
#
# To *run* or *execute* a script, simply type `run` *filename*, which in
# this case means type `run myTrip.py`. When you run a script, Python
# simply executes the sequence of commands in the order they appear.
#
# ``` ipython
# In [2]: run myTrip.py
# ```
#
# Once you have run the script, you can see the values of the variables
# calculated in the script simply by typing the name of the variable.
# IPython responds with the value of that variable.
#
# ``` ipython
# In [3]: time
# Out[3]: 6.666666666666667
#
# In [4]: gallons
# Out[4]: 13.333333333333334
#
# In [5]: cost
# Out[5]: 54.666666666666664
# ```
#
# You can change the number of digits IPython displays using the command
# `%precision`:
#
# ``` ipython
# In [6]: %precision 2
# Out[6]: u'%.2f'
#
# In [7]: time
# Out[7]: 6.67
#
# In [8]: gallons
# Out[8]: 13.33
#
# In [9]: cost
# Out[9]: 54.67
# ```
#
# Typing `%precision` returns IPython to its default state;
# `%precision %e` causes IPython to display numbers in exponential format
# (scientific notation).
#
# #### Note about printing
#
# If you want your script to return the value of a variable (that is,
# print the value of the variable to your computer screen), use the
# `print` function. For example, at the end of our script, if we include
# the code
#
# ``` python
# print(time)
# print(gallons)
# print(cost)
# ```
#
# the script will return the values of the variables `time`, `gallons`,
# and `cost` that the script calculated. We will discuss the `print`
# function in much greater detail, as well as other methods for data
# output, in Chapter 4 on `chap4`.
#
# ### Scripting Example 2
#
# Let's try another problem. Suppose you want to find the distance between
# two Cartesian coordinates $(x_1, y_1, z_1)$ and $(x_2, y_2, z_2)$. The
# distance is given by the formula
#
# $$\Delta r = \sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2}$$
#
# Now let's write a script to do this calculation and save it in a file
# called `twoPointDistance.py`.
#
# ``` python
# # Calculates the distance between two 3d Cartesian coordinates
# import numpy as np
#
# x1, y1, z1 = 23.7, -9.2, -7.8
# x2, y2, z2 = -3.5, 4.8, 8.1
#
# dr = np.sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )
# ```
#
# We have introduced extra spaces into some of the expressions to improve
# readability. They are not necessary; where and whether you include them
# is largely a matter of taste.
#
# There are two important differences between the code above and the
# commands we would have written into the IPython console to execute the
# same set of commands. The first is the statement on the second line
#
# ``` python
# ...
# import numpy as np
# ...
# ```
#
# and the second is the "`np.`" in front of the `sqrt` function on the
# last line. If you leave out the `import numpy as np` line and remove the
# `np.` in front of the `sqrt` function, you will get the following error
# message
#
# ``` ipython
# ----> 7 dr = sqrt( (x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2 )
#
# NameError: name 'sqrt' is not defined
# ```
#
# The reason for the error is that the `sqrt` function is not a part of
# core Python. But it is a part of the NumPy module discussed earlier. To
# make the NumPy library available to the script, you need to add the
# statement `import numpy as np`. Then, when you call a NumPy function,
# you need to write the function with the `np.` prefix. Failure to do
# either will result in a error message. Now we can run the script.
#
# ``` ipython
# In [10]: run twoPointDistance.py
#
# In [11]: dr
# Out[11]: 34.48
# ```
#
# The script works as expected.
#
# The reason we do not have to import NumPy when working in the IPython
# shell is that it is done automatically when the IPython shell is
# launched. Similarly, the package MatPlotLib is also automatically loaded
# (imported) when IPython is launched. However, when a script or program
# is executed, it is run on its own outside the IPython shell, even if the
# command to run the script is executed from the IPython shell.
#
# single: line continuation
#
# #### Line continuation
#
# From time to time, a line of code in a script will be unusually long,
# which can make the code difficult to read. In such cases, it is
# advisable to split the code onto several lines. For example, line 7 in
# the preceding script could be written as
#
# ``` ipython
# dr = np.sqrt( (x2-x1)**2 
#             + (y2-y1)**2 
#             + (z2-z1)**2 )
# ```
#
# You can generally continue an expression on another line in Python for
# code that is within a function argument, as it is here where the line is
# split inside the argument of the square root function. Note that the
# sub-expressions written on different lines are lined up. This is done
# solely to improve readability; Python does not require it. Nevertheless,
# as the whole point of splitting a line is to improve readability, it's
# best to line up expressions so as to maximize readability.
#
# You can split any Python line inside of parentheses, brackets, and
# braces, as illustrated above. You can split it other places as well by
# using the backslash (`\`) character. For example, the code
#
# ``` ipython
# a = 1 + 2 \
#   + 3 + 4
# ```
#
# is equivalent to
#
# ``` ipython
# a = 1 + 2 + 3 + 4
# ```
#
# So you can use backslash character (`\`) of explicit line continuation
# when implicit line continuation won't work.
#
# Importing Modules
# -----------------
#
# single: module; importing
#
# We saw in Example 2 in the last section that we needed to import the
# NumPy module in order to use the `sqrt` function. Indeed the NumPy
# library contains many useful functions, some of which are listed in
# section `chap2:NumPyFuncs`. Whenever any NumPy functions are used, the
# NumPy library must be loaded using an `import` statement.
#
# There are a few ways to do this. The one we generally recommend is to
# use the `import as` implementation that we used in Example 2. For the
# main NumPy and MatPlotLib libraries, this is implemented as follows:
#
# ``` python
# import numpy as np
# import maplotlib.pyplot as plt
# ```
#
# These statements import the entire library named in the `import`
# statement and associate a prefix with the imported library: `np` and
# `plt` in the above examples. Functions from within these libraries are
# then called by attaching the appropriate prefix with a period *before*
# the function name. Thus, the functions `sqrt` or `sin` from the NumPy
# library are called using the syntax `np.sqrt` or `np.sin`; the functions
# `plot` or `xlabel` from the `maplotlib.pyplot` would be called using
# `plt.plot` or `plt.xlabel`.
#
# Alternatively, the NumPy and MatPlotLib libraries can be called simply
# by writing
#
# ``` python
# import numpy
# import maplotlib.pyplot
# ```
#
# When loaded this way, the `sqrt` function would be called as
# `numpy.sqrt` and the `plot` function would be called as
# `MatPlotLib.pyplot.plot`. The `import as` syntax allows you to define
# nicknames for `numpy` and `maplotlib.pyplot`. Nearly any nickname can be
# chosen, but the Python community has settled on the nicknames `np` and
# `plt` for `numpy` and `maplotlib.pyplot`, so you are advised to stick
# with those. Using the standard nicknames makes your code more readable.
#
# You can also import a single functions or subset of functions from a
# module without importing the entire module. For example, suppose you
# wanted to import just the natural log function `log` from NumPy. You
# could write
#
# ``` python
# from numpy import log
# ```
#
# To use the `log` function in a script, you would write
#
# ``` python
# a = log(5)
# ```
#
# which would assign the value `1.6094379124341003` to the variable `a`.
# If you wanted to import the three functions, `log`, `sin`, and `cos`,
# you would write
#
# ``` python
# from numpy import log, sin, cos
# ```
#
# and would similarly use them without an "`np.`" prefix. In general, we
# do not recommend using the the `from` *module* `import ...` way of
# importing functions. When reading code, it makes it harder to determine
# from which modules functions are imported, and can lead to clashes
# between similarly named functions from different modules. Nevertheless,
# you will see the form used in programs you encounter on the web and
# elsewhere so it is important to understand the syntax.
#
# Getting help: documentation in IPython shell
# --------------------------------------------
#
# Help is never far away when you are running the IPython shell. To obtain
# information on any valid Python or NumPy function, and many MatPlotLib
# functions, simply type `help(` *function* `)`, as illustrated here
#
# ``` ipython
# In [1]: help(range)
# range([start,] stop[, step]) -> list of integers
#
# Return a list containing an arithmetic progression of integers.
# range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults
# to 0.  When step is given, it specifies the increment (or
# decrement).  For example, range(4) returns [0, 1, 2, 3].  The
# end point is omitted! These are exactly the valid indices for a
# list of 4 elements.
# ```
#
# Often, the information provided can be quite extensive and you might
# find it useful to clear the IPython window with the `clear` command so
# you can easily scroll back to find the beginning of the documentation.
# You may have also noticed that when you type the name of a function plus
# the opening parenthesis, IPython displays a window showing the first
# dozen lines or so of the documentation on that function.
#
# Programming is a detail-oriented activity
# -----------------------------------------
#
# Now that you have a little experience with Python and computer
# programming, it's time for an important reminder: *Programming is a
# detail-oriented activity*. To be good at computer programming, to avoid
# frustration when programming, you must pay attention to details. A
# misplaced or forgotten comma or colon can keep your code from working.
# Note that I did not say it can "keep your code from working *well*"; it
# can keep your code from working at all! Worse still, little errors can
# make your code give erroneous answers, where your code appears to work,
# but in fact does not! So pay attention to the details!
#
# This raises a second point: sometimes your code will run but give the
# wrong answer because of a programming error or because of a more subtle
# error in your algorithm. For this reason, it is important to test your
# code to make sure it is behaving properly. Test it to make sure it gives
# the correct answers for cases where you already know the correct answer
# or where you have some independent means of checking it. Test it in
# limiting cases, that is, for cases that are at the extremes of the sets
# of parameters you will employ. Always test your code; this is a cardinal
# rule of programming.
#
# Exercises
# ---------
#
# 1.  A ball is thrown vertically up in the air from a height $h_0$ above
#     the ground at an initial velocity $v_0$. Its subsequent height $h$
#     and velocity $v$ are given by the equations
#
#     $$\begin{aligned}
#     h &= h_0 + v_0t - \tfrac{1}{2}gt^2 \\
#     v &= v_0 - gt
#     \end{aligned}$$
#
#     where $g = 9.8$ is the acceleration due to gravity in
#     $\mathrm{m/s^2}$. Write a script that finds the height $h$ and
#     velocity $v$ at a time $t$ after the ball is thrown. Start the
#     script by setting $h_0 = 1.2$ (meters) and $v_0 = 5.4$ (m/s) and
#     have your script print out the values of height and velocity (see
#     `printNote`). Then use the script to find the height and velocity
#     after 0.5 seconds. Then modify your script to find them after 2.0
#     seconds.
#
# 2.  Write a script that defines the variables $V_0 = 10$, $a = 2.5$, and
#     $z = 4\tfrac{1}{3}$, and then evaluates the expression
#
#     $$V = V_0 \left( 1 - \frac{z}{\sqrt{a^2+z^2}} \right) \;.$$
#
#     Then find $V$ for $z=8\frac{2}{3}$ and print it out (see
#     `printNote`). Then find $V$ for $z=13$ by changing the value of $z$
#     in your script.
#
# 3.  Write a single Python script that calculates the following
#     expressions:
#
#     > 1.  $\displaystyle a = \frac{2 + e^{2.8}}{\sqrt{13}-2}$
#     > 2.  $\displaystyle b = \frac{1-(1+\ln 2)^{-3.5}}{1+\sqrt{5}}$
#     > 3.  $\displaystyle c = \sin\left( \frac{2-\sqrt{2}}{2+\sqrt{2}} \right)$
#
#     After running your script in the IPython shell, typing `a`, `b`, or
#     `c` at the IPython prompt should yield the value of the expressions
#     in (a), (b), or (c), respectively.
#
# 4.  A quadratic equation with the general form
#
#     $$ax^2+bx+c=0$$
#
#     has two solutions given by the quadratic formula
#
#     $$x = \frac{-b \pm \sqrt{b^2-4ac}}{2a} \;.$$
#
#     1.  Given $a$, $b$, and $c$ as inputs, write a script that gives the
#         numerical values of the two solutions. Write the constants $a$,
#         $b$, and $c$ as floats, and show that your script gives the
#         correct solutions for a few test cases when the solutions are
#         real numbers, that is, when the discriminant $b^2-4ac \ge 0$.
#         Use the `print` function in your script, discussed at the end of
#         Section 2.8.1 `chap2:ScriptExmp1`, to print out your two
#         solutions.
#     2.  Written this way, however, your script gives an error message
#         when the solutions are complex. For example, see what happens
#         when $a=1$, $b=2$, and $c=3$. You can fix this using statements
#         in your script like `a = a+0j` after setting `a` to some float
#         value. Thus, you can make the script work for any set of real
#         inputs for $a$, $b$, and $c$. Again, use the `print` function to
#         print out your two solutions.
