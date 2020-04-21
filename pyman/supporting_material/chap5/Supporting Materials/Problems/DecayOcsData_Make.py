import numpy as np
import matplotlib.pyplot as plt

def f(x):
    decay = 10.0
    period = decay
    return (3.0+0.5*np.sin(2.*np.pi*x/period))*x*np.exp(-x/decay)

x = np.linspace(0.0, 45., 128)
xdata = np.linspace(1., 43., 13)
yerr = 0.4 * np.sqrt(f(xdata))
ydata = f(xdata) + 2.0 * yerr * (np.random.rand(len(xdata))-0.5)

info = 'Data for Exercise 5'
info += '\nDate: 16-Aug-2013'
info += '\nData taken by Lauren and John'
info += '\n\n t      d       dy'
np.savetxt('DecayOcsData.txt', zip(xdata, ydata, yerr), fmt='%4.1f %7.2f %6.1f',
           header=info, comments='')

plt.plot(x, f(x))
plt.plot(xdata, ydata, 'ro')
plt.show()
