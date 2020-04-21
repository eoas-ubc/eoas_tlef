import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 10., 0.04)
ytan = np.tan(theta)

plt.figure()
plt.plot(theta, ytan)

plt.savefig('plotLimits1.pdf')

plt.show()