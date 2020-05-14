---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.8'
    jupytext_version: 1.4.2
kernelspec:
  display_name: Python 3
  name: python3
---

# Andrew's Trivial Lab II

+++

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
