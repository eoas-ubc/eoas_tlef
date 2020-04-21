import numpy as np
import matplotlib.pyplot as plt

# read data from file
time, counts, unc = np.loadtxt('SemilogDemo.txt', unpack=True)

# create theoretical fitting curve
tau = 20.2      # Phosphorus-32 half life = 14 days; tau = t_half/ln(2)
N0 = 8200.       # Initial count rate (per second)
t = np.linspace(0, 180, 128)
N = N0 * np.exp(-t/tau)

# create plot
plt.figure(1, figsize = (10,4) )

plt.subplot(1, 2, 1)
plt.plot(t, N, 'b-', label="theory")
plt.plot(time, counts, 'ro', label="data")
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')

plt.subplot(1, 2, 2)
plt.semilogy(t, N, 'b-', label="theory")
plt.semilogy(time, counts, 'ro', label="data")
plt.xlabel('time (days)')
plt.ylabel('counts per second')
plt.legend(loc='upper right')

plt.tight_layout()

# save plot to file
plt.savefig('semilogDemo.pdf')

# display plot on screen
plt.show()