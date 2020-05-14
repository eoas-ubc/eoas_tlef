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
    jupytext_version: 1.5.0-dev
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Andrew's Trivial Lab II

+++

 There are dozens of different flavors of shell. One of these is the
    bash shell; if you have a Mac, then you already have a bash shell,
    which you can launch from spotlight by typing ⌘-space (i.e. press
    the "command" key together with the a space, then type the word
    "terminal" into the spotlight search bar).

```{code-cell} ipython3
Δ=5
print(Δ)
```

## Another very easy lab
In addition to linear and quadratic functions, we can also define *cubic* functions:

$$
y = ax^3 + bx^2 + cx + d
$$

```{code-cell} ipython3
# Enter values for the coefficients and x
a = 1
b = 1
c = 1
d = 1

x = 1

y = a*x**3 + b*x**2 + c*x + d
print(f'y = {y}')
```
