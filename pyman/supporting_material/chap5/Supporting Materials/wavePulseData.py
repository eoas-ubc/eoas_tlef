import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x) * np.exp(-(x/5.0)**2)

xdata = np.linspace(-10., 10., 21)
ydata = f(xdata) * (1.0 + 0.3 * np.random.rand(len(xdata)) )

np.savetxt('wavePulseData.txt', zip(xdata, ydata), fmt='%10.2f')
