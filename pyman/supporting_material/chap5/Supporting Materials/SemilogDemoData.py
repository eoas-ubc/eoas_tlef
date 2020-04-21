# Create simulated exponential decay data
# Radioactive decay
from __future__ import division

import numpy as np
import numpy.random

def CreateSimulatedData(N0, tau):
    tstart = 2.0
    t = np.arange(tstart, 8.7*tau, 7.0)
    N = 10.*N0 * np.exp(-t/tau)                     # Decay signal w/o noise
    for i in range(N.size):                          # make a noisy signal
        N[i] = numpy.random.poisson(N[i], 1)    # Poisson statistics for shot noise
    dN = np.sqrt(N)                             # Estimate of uncertainties for raw data
    return t, N/10., dN/10.
  
# Create simulated data
tau = 20.6      # Phosphorus-32 half life = 14.3 days; tau = t_half/ln(2)
N0 = 8200.      # Initial count rate (per second)
t, N, dN = CreateSimulatedData(N0, tau)

# Save simulated data to text file
np.savetxt("SemilogDemo.txt", zip(t, N, dN), fmt='%10.2e')