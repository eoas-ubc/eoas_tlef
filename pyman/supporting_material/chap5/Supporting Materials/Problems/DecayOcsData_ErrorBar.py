import numpy as np
import matplotlib.pyplot as plt

def f(x):
    decay = 10.0
    period = decay
    return (3.0+0.5*np.sin(2.*np.pi*x/period))*x*np.exp(-x/decay)

# read data from file
xdata, ydata, yerror = np.loadtxt('DecayOcsData.txt', skiprows=5, unpack=True)

# create theoretical fitting curve
x = np.linspace(0, 45, 128)
y = f(x)

# create plot
plt.figure(1, figsize = (7,4.5) )
plt.plot(x, y, 'b-', label="theory")
plt.errorbar(xdata, ydata, fmt='ro', label="data", 
             xerr=0.75, yerr=yerror, ecolor='k')
plt.xlabel('x')
plt.ylabel('transverse displacement')
plt.legend(loc='upper right')

# save plot to file
plt.savefig('DecayOcsData.pdf')

# display plot on screen
plt.show()