import numpy as np
import matplotlib.pyplot as plt

# read in spectrum from data file 
f, s, ds = np.loadtxt("Spectrum.txt", skiprows=4, unpack=True)

# Plot data
plt.figure(1)
plt.subplot(111)
plt.errorbar(f, s, yerr=ds, fmt='or', ecolor='black')
plt.xlabel('frequency (THz)')
plt.ylabel('absorption (arb units)')
plt.show()
plt.savefig("Spectrum.pdf")