import numpy as np
import matplotlib.pyplot as plt

distance = np.array([0.38, 0.64, 0.91, 1.26, 1.41, 1.66, 1.90, 2.18])
force = np.array([1.4, 1.65, 3.0, 3.95, 4.3, 5.20, 6.85, 7.4])
df = np.array([ 0.4, 0.5, 0.4, 0.5, 0.6, 0.5, 0.5, 0.4])
xfit = np.array([0.2, 2.4])
yfit = 3.41 * xfit - 0.182
ylfit = 3.0 * xfit + 0.35
yufit = 3.8 * xfit - 0.7

plt.figure(figsize=(6,4))
plt.plot(xfit, ylfit, 'gray', ls='--')
plt.plot(xfit, yufit, 'gray', ls='--')
plt.plot(xfit, yfit, 'k')
plt.errorbar(distance, force, yerr=df, ls='', 
             marker='d', mfc='yellow', mec='brown', ms=9,
             ecolor='brown')

plt.xlabel('distance (cm)')
plt.ylabel('force (N)')

plt.tight_layout()
plt.savefig("LinearData.eps")
plt.show()
