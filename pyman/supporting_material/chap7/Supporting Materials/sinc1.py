def sinc(x):
    y = np.where(x==0.0, 1.0, np.sin(x)/x)
    return y

import numpy as np
import matplotlib.pyplot as plt
import time

x = np.linspace(-10, 10, 65536)
start = time.time()
y = sinc(x)
elapsed = (time.time() - start)
print(elapsed)

plt.plot(x, y)
plt.axhline(color="gray", zorder=-1)
plt.axvline(color="gray", zorder=-1)
plt.show()
