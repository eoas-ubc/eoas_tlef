import numpy as np
import matplotlib.pyplot as plt

def bessel_sph(x, n):
    j0 = np.where(x==0., 1., np.sin(x)/x)
    if n==0:
        return j0
    else:
        j1 = np.where(x==0., 0., (j0-np.cos(x))/x)
        if n==1:
            return j0, j1
        else:
            j2 = np.where(x==0., 0., 3.*j1/x - j0)
            return j0, j1, j2

x = np.linspace(0.0, 20, 256)
y0, y1, y2 = bessel_sph(x, 2)
plt.plot(x, y0, label='j0(x)')
plt.plot(x, y1, label='j1(x)')
plt.plot(x, y2, label='j2(x)')
plt.legend()
plt.xlabel('x')
plt.axhline(color="gray", zorder=-1)
plt.show()
plt.savefig("besselSph.eps")