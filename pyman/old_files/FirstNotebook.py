# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all,-language_info,-toc,-latex_envs
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Demo of IPython Notebook

# %% [markdown]
# ## David Pine

# %%
2+3

# %%
import numpy as np
import matplotlib.pyplot as plt

# %%
np.sin(np.pi/6)

# %%
plt.plot([1,2,3,2,3,4,3,4,5])

# %%

# %%
# Calculates time, gallons of gas used, and cost of gasoline for
# a trip

distance = float(input("Input distance of trip in miles: "))
mpg = 30.               # car mileage
speed = 60.             # average speed
costPerGallon = 4.10    # price of gas

time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print("\nDuration of trip = {0:0.1f} hours".format(time))
print("Gasoline used = {0:0.1f} gallons (@ {1:0.0f} mpg)"
      .format(gallons, mpg))
print("Cost of gasoline = ${0:0.2f} (@ ${1:0.2f}/gallon)"
      .format(cost, costPerGallon))

# %% [markdown]
# The total distance $x$ traveled during a trip can be
# obtained by integrating the velocity $v(t)$ over the
# duration $T$ of the trip:
# \begin{align}
#     x = \int_0^T v(t)\, dt
# \end{align}

# %%
# !cat LiamSelinaData.txt

# %%
