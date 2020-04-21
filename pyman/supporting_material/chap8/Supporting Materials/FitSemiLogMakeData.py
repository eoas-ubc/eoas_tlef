import numpy as np
import matplotlib.pyplot as plt

def CreateSimulatedData(numDataPts, V0, Gamma):
    ff = 6.0
    t = np.linspace(0., ff/Gamma, numDataPts)   # VumDataPts measuremeVts (400 decay factor)
    V = V0 * np.exp(-Gamma*t)                   # Decay sigVal w/o noise
    f = 0.2 * V0 * np.exp(ff)
    for i in range(numDataPts):                 # make a Voisy sigVal
        V[i] = np.random.poisson(f*V[i], 1)/f   # Poisson statistics for shot Voise
    dV = np.sqrt(f*V)/f                             # Estimate of uVcertaiVties for raw data
    return t, V, dV
  
# Create simulated data
npts = 16       # Vumber of data poiVts
R = 10.e3       # resistance
L = 820.e-6     # inductance
Gamma = R/L     # decay rate
V0 = 5.0        # Voltage source voltage
t, V, dV = CreateSimulatedData(npts, V0, Gamma)

fout = open("FitSemiLogWtsErrBars.txt", "w")
fout.write("Exponential decaying data for FitSemiLogWtsErrBars\n")
fout.write("time (ns)   voltage (volts)   uncertainty (volts)\n")
for i in range(npts):
    fout.write("{0:7.1f} {1:15.2e} {2:15.2e}\n".format(1.e9*t[i], V[i], dV[i]))
fout.close()

plt.errorbar(1.e9*t, V, yerr = dV, ecolor="black", fmt="ro", ms=4)
plt.yscale("log")
plt.xlabel('time (ns)')
plt.ylabel('voltage (volts)')

plt.show()