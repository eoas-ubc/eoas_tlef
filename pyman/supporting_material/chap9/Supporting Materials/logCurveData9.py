import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d, UnivariateSpline, BarycentricInterpolator

def f(x):
    return np.log(x)

def frangeAdd(x, xtend):
    xmin = np.min(x)
    xmax = np.max(x)
    add = xtend*(xmax-xmin)
    xmin -= add
    xmax += add
    return xmin, xmax

# Create "data" to be fit & save to data file
npts = 7
noiseAmp = 0.03
xdata = np.linspace(0.2, 10., npts) + 0.3*np.random.randn(npts)
xdata = np.sort(xdata)
ydata = f(xdata) * (1.0 + noiseAmp * np.random.randn(npts))
np.savetxt('logCurveData9.txt', zip(xdata, ydata), fmt='%10.2f')

# Create x array spanning data set plus 5%
xmin, xmax = frangeAdd(xdata, 0.05)
x = np.linspace(xmin, xmax, 200)

# Plot data and "fit"
plt.plot(xdata, ydata, 'or', label='data')
plt.plot(x, f(x), 'k-', label='fitting function')

# Create y array from cubic spline
f_cubic = interp1d(xdata, ydata, kind='cubic', bounds_error=False)
plt.plot(x, f_cubic(x), 'k-', label='cubic spline')

# Create y array from univariate spline
f_univar = UnivariateSpline(xdata, ydata, w=None, bbox=[xmin, xmax], k=3)
plt.plot(x, f_univar(x), label='univariate spline')

# Create y array from barycentric interpolation
f_bary = BarycentricInterpolator(xdata, ydata)
plt.plot(x, f_bary.__call__(x), label='barycentric interp')

plt.legend(loc='best')

plt.show()
