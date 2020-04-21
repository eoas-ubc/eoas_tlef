def sinc(x):
    z = np.where(x==0.0, 1.0, np.sin(x)/x)
    return z

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 65536)
y = sinc(x)

plt.plot(x, y)
plt.axhline(color="gray", zorder=-1)
plt.axvline(color="gray", zorder=-1)
plt.show()
