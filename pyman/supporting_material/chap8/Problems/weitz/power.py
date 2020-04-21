import numpy as np
import matplotlib.pyplot as plt

t = np.array([0.002, 0.003, 0.007, 0.015, 0.035, 0.1, 0.3, 0.7])
r = np.array([115., 130., 202., 335., 510., 890., 1700., 2600.])
dr = np.array([ 10.,  12.,  14.,  18.,  20.,  30.,  40.,  50.])

t *= 60.

head = """Mass of growing aggregate
Date: 19-Nov-2013
Data taken by M. D. Gryart and M. S. Groshow
time (m)   size (nm)    unc (nm)"""

np.savetxt("aggdata.txt", zip(t, r, dr),
           fmt="%6.2f %10.0f %10.0f", header = head,
           comments = "")

fig = plt.figure()
ax = fig.add_subplot(111)
ax.errorbar(t, r, yerr=dr, fmt="sr", ms=3)
ax.set_xscale("log")
ax.set_yscale("log")
ax.set_xlim(0.1, 60)
ax.set_ylim(90, 3000)
plt.show()
