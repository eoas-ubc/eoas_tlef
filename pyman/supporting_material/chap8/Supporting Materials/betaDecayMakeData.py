import numpy as np
import numpy.random
import matplotlib.pyplot as plt

def CreateSimulatedData(N0, tau, t):
    N = N0 * np.exp(-t/tau)                   # Decay signal w/o noise
    for i in range(t.size):                   # make a noisy signal
        N[i] = numpy.random.poisson(N[i], 1)  # Poisson statistics for shot noise
    dN = np.sqrt(N)                           # Estimate of uncertainties for raw data
    return N, dN
  
# Create simulated data
npts = 32              # Number of data points
tau = 14.2/np.log(2.)  # Phosphorus-32 half life = 14.29 days; tau = t_half/ln(2)
N0 = 900.             # Initial count rate (per second)
t = np.arange(0., 5.52*tau, 3)
N, dN = CreateSimulatedData(N0, tau, t)

fout = open("betaDecay.txt", "w")
fout.write("Exponential decaying data for betaDecay\n")
fout.write("time (s)   decays   uncertainty\n")
for i in range(npts):
    fout.write("{0:6.2f} {1:9.0f} {2:10.0f}\n".format(t[i], N[i], dN[i]))
fout.close()