def sinc(x):
    y = []              # creates an empty list to store results
    for xx in x:        # loops over all elements in x array
        if xx==0.0:     # adds result of 1.0 to y list if
            y += [1.0]  # xx is zero
        else:           # adds result of sin(xx)/xx to y list if
            y += [np.sin(xx)/xx]  # xx is not zero
    return np.array(y)  # converts y to array and returns array

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

plt.savefig("sinc.pdf")