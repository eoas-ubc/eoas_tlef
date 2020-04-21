import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) * np.exp(-(x/5.0)**2)

def frangeAdd(x, xtend):
    xmin = np.min(x)
    xmax = np.max(x)
    add = xtend*(xmax-xmin)
    xmin -= add
    xmax += add
    return xmin, xmax

npts = 21
noiseAmp = 0.05
xdata = np.linspace(-10., 10., npts) + 0.2*np.random.randn(npts)
xdata = np.sort(xdata)
ydata = f(xdata) * (1.0 + noiseAmp * np.random.randn(npts))

xmin, xmax = frangeAdd(xdata, 0.05)
x = np.linspace(xmin, xmax, 200)

np.savetxt('wavePulseData9.txt', zip(xdata, ydata), fmt='%10.2f')

plt.plot(xdata, ydata, 'or')
plt.plot(x, f(x))
plt.show()
