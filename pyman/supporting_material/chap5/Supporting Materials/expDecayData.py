import numpy as np

def f(x):
    return 1.1+ 3.0*x*np.exp(-(x/10.0)**2)

xdata = np.linspace(1., 43., 13)
yerr = 1.0 + 0.5 * np.sqrt(f(xdata))
ydata = f(xdata) + 2.0 * yerr * (np.random.rand(len(xdata))-0.5)

np.savetxt('expDecayData.txt', zip(xdata, ydata, yerr), fmt='%0.15e')
