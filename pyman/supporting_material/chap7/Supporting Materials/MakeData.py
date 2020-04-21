# Make simulated data
import numpy as np

npts = 10
time = np.linspace(0.1, 2.6, npts) + 0.01 * np.random.randn(npts)

v0 = 5.
a = -9.8
noise = 1.2
vel = v0 + a * time + noise * np.random.randn(npts)
dv = np.random.normal(loc=noise, scale=0.2*noise, size=npts)

fout = open("VelocityVsTime.txt", "w")
fout.write("Velocity vs time data\n")
fout.write("for a falling mass\n")
fout.write("time (s)   velocity (m/s)   uncertainty (m/s)\n")
for i in range(npts):
    fout.write("{0:5.2f} {1:15.2f} {2:15.2f}\n".format(time[i], vel[i], dv[i]))
fout.close()