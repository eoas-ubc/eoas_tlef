# Make simulated data
import numpy as np
import matplotlib.pyplot as plt

def SineGaussDecay(t, A, B, C, tau, omega):
    y = A * (1.0 + B*np.cos(omega*t)) * np.exp(-0.5*t*t/(tau*tau)) + C
    return y

A = 15.0
B = 0.6
C = 1.2*A
tau = 16.0
omega = 2.0 * (2.0*np.pi/tau) 

npts = 32
t = np.linspace(0.2, 2.4*tau, npts)

NoiseAmp = 0.0
NoiseWidth = A/18.

noise = np.random.normal(loc=NoiseAmp, scale=NoiseWidth, size=t.size)

decay = SineGaussDecay(t, A, B, C, tau, omega) + noise

unc = np.random.normal(loc=NoiseWidth, scale=0.2*NoiseWidth, size=t.size)

# Write to data file
fileout = open("OscData.txt", "w")
fileout.write("Data for absorption spectrum\n")
fileout.write("Date: 21-Nov-2012\n")
fileout.write("Data taken by P. Dubson and M. Sparks\n")
fileout.write("time (ms)  signal  uncertainty\n")
for i in range(t.size):
    fileout.write("{0:5.1f} {1:9.1f} {2:9.1f} \n".format(t[i], decay[i], unc[i]))
fileout.close()

# Plot data
plt.errorbar(t, decay, yerr = unc, ecolor="black", fmt="ro")
plt.xlabel('time (ms)')
plt.ylabel('decay (arb units)')

plt.savefig('DataOscDecay.pdf')
plt.show()