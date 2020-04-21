# Make simulated data
import numpy as np
import matplotlib.pyplot as plt

npts = 13
A = 1.e8
n = np.logspace(1.1, 2.9, npts)
p = -1.5
m = 0.1 * n**p

m *= A*np.random.normal(loc=1.0, scale=0.1, size=m.size)
n *= np.random.normal(loc=1.0, scale=0.1, size=n.size)
dm = m**0.81



# Write to data file
fileout = open("Mass.txt", "w")
fileout.write("Data for masses\n")
fileout.write("Date: 15-Nov-2013\n")
fileout.write("Data taken by M. D. Gryart and M. S. Groshow\n")
fileout.write(" number   mass    uncertainty\n")
for i in range(m.size):
    fileout.write("{0:5.0f} {1:10.2e} {2:10.1e} \n".format(n[i], m[i], dm[i]))
fileout.close()

# Plot data
fig = plt.figure(1)
ax = fig.add_subplot(111)
ax.errorbar(n, m, yerr=dm, fmt='ro')
ax.set_xscale('log')
ax.set_yscale('log')
ax.set_xlabel('number')
ax.set_ylabel('mass')
plt.show()