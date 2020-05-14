---
jupytext:
  cell_metadata_filter: all
  encoding: '# -*- coding: utf-8 -*-'
  formats: ipynb,md:myst
  notebook_metadata_filter: all,-language_info
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Andrew's Trivial Lab 
### A program for testing git and github

+++

This is some trivial content using markdown, LaTeX, and Python code to solve a simple problem using Python code. Here's an equation. $y$ is a *linear function* of $x$:


$$
    y = mx + b\tag{equation of a line}
$$

$$
y = mx + b
$$(eq:line)

As we see on {eq}`eq:line`

Edit the cell below by entering your values for $m$, $x$ and $b$. The output of the cell will be the value of $y$ corresponding to the values you enter.

### Problem 1:

```{code-cell} ipython3
# Choose values for m, x, and b
m = 1
x = 1
b = 1

y = m * x + b
print(f'{m}*{x} + {b} = {y}')
```

### Problem 2:
Write a cell which solves a *quadratic equation*. 

*HINT: A quadratic equation is of the form $y = ax^2 + bx + c$. $x^2$ is written in Python as "x**2"*

```{code-cell} ipython3
# your code goes here
```

### Conclusion
We can use Jupyter notebooks to solve math problems.
