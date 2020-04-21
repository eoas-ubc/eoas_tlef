def LineFit(x, y):
    """ Returns slope and y-intercept of linear fit to (x,y) data set"""
    xavg = x.mean()
    slope = (y*(x-xavg)).sum()/(x*(x-xavg)).sum()
    yint = y.mean()-slope*xavg
    return slope, yint

def redchisq(x, y, dy, slope, yint):
    """Returns reduced chi squared for linear fit"""
    chisq = (((y-yint-slope*x)/dy)**2).sum()
    return chisq/float(x.size-2)
    
import numpy as np
import matplotlib.pyplot as plt

# read in data set 2 for falling object from txt file 
t, v, dv = np.loadtxt("VelocityVsTime.txt", skiprows=3, unpack=True)

# Determine fitting parameters
a, v0 = LineFit(t, v)

# ... and the reduced chi^2
rchi2 = redchisq(t, v, dv, a, v0)

# Create points for plotting the fit
dt = 0.05 * (t.max()-t.min())               # add this to span of time in data set
tFit = np.array([t.min()-dt, t.max()+dt])   # only 2 points are needed for a line
vFit0 = v0 + a * tFit                     # create the y-fit data

# Plot fit and data
fig = plt.figure(1)
ax = fig.add_subplot(111)
#ax.plot(tFit, vFit0, "g")    # plot fit
ax.axhline(y=0, color="gray")
ax.plot(t, v, "ro")

# Annotate plot
ax.text(1, 450, "Least squares fit w/o uncertainties")
ax.text(1, 400, "v0 = {0:0.1f} m/s".format(v0))
ax.text(1, 350, "a = {0:0.1f} m/s^2".format(a))
ax.text(1, 300, "redchisq = {0:0.2f}".format(rchi2))

ax.set_xlabel("time (s)")
ax.set_ylabel("velocity (m/s)")

plt.savefig("VelocityVsTimePlot.pdf")

plt.show()
