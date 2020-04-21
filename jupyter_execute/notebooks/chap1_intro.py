<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Introduction" data-toc-modified-id="Introduction-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introduction</a></span><ul class="toc-item"><li><span><a href="#Introduction-to-Python-and-its-use-in-science" data-toc-modified-id="Introduction-to-Python-and-its-use-in-science-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>Introduction to Python and its use in science</a></span></li></ul></li></ul></div>

Introduction
============

latex

Introduction to Python and its use in science
---------------------------------------------

This manual is meant to serve as an introduction to the Python
programming language and its use for scientific computing. It's ok if
you have never programmed a computer before. This manual will teach you
how to do it from the ground up.

The Python programming language is useful for all kinds of scientific
and engineering tasks. You can use it to analyze and plot data. You can
also use it to numerically solve science and engineering problems that
are difficult or even impossible to solve analytically.

While we want to marshall Python's powers to address scientific
problems, you should know that Python is a general purpose computer
language that is widely used to address all kinds of computing tasks,
from web applications to processing financial data on Wall Street and
various scripting tasks for computer system management. Over the past
decade it has been increasingly used by scientists and engineers for
numerical computations, graphics, and as a "wrapper" for numerical
software originally written in other languages, like Fortran and C.

Python is similar to Matlab and IDL, two other computer languages that
are frequently used in science and engineering applications. Like Matlab
and IDL, Python is an *interpreted* language, meaning you can run your
code without having to go through an extra step of compiling, as
required for the C and Fortran programming languages. It is also a
*dynamically typed* language, meaning you don't have to declare
variables and set aside memory before using them. Don't worry if you
don't know exactly what these terms mean. Their primary significance for
you is that you can write Python code, test, and use it quickly with a
minimum of fuss.

One advantage of Python over similar languages like Matlab and IDL is
that it is free. It can be downloaded from the web and is available on
all the standard computer platforms, including Windows, MacOS, and
Linux. This also means that you can use Python without being tethered to
the internet, as required for commercial software that is tied to a
remote license server.

Another advantage is Python's clean and simple syntax, including its
implementation of *object oriented* programming (which we do not
emphasize in this introduction).

An important disadvantage is that Python programs can be slower than
compiled languages like C. For large scale simulations and other
demanding applications, there can be a considerable speed penalty in
using Python. In these cases, C, C++, or Fortran is recommended,
although intelligent use of Python's array processing tools contained in
the NumPy module can greatly speed up Python code. Another disadvantage
is that compared to Matlab and IDL, Python is less well documented. This
stems from the fact that it is public *open source* software and thus is
dependent on volunteers from the community of developers and users for
documentation. The documentation is freely available on the web but is
scattered among a number of different sites and can be terse. This
manual will acquaint you with the most commonly-used web sites. Search
engines like Google can help you find others.

You are not assumed to have had any previous programming experience.
However, the purpose of this manual isn't to teach you the principles of
computer programming; it's to provide a practical guide to getting
started with Python for scientific computing. Perhaps once you see some
of the powerful tasks that you can accomplish with Python, you will be
inspired to study computational science and engineering, as well as
computer programming, in greater depth.