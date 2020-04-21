import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 4.*np.pi, 129)
y = np.sin(x)

plt.plot(x, y)

plt.show()

plt.savefig("sinePlotDenserXY.png")