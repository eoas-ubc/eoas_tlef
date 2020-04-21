def circle(r, x0=0.0, y0=0.0, n=12):
    theta = np.linspace(0., 2.*np.pi, n, endpoint=False)
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    return x0+x, y0+y

import numpy as np
import matplotlib.pyplot as plt

x0, y0 = 1, -1
x, y = circle(2, x0, y0)
plt.axes().set_aspect('equal')
plt.axhline(y=y0, color='gray', ls='--')
plt.axvline(x=x0, color='gray', ls='--')
plt.axhline(color='black')
plt.axvline(color='black')
plt.plot(x, y, 'ro')
plt.show()