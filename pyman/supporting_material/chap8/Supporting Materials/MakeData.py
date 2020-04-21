# Make simulated data
import numpy as np
import matplotlib.pyplot as plt

npts = 45
f = np.linspace(0.4, 23.5, npts)

a = 58.7
b = -3.8
c = 0.078
P = 83.2
fp = 11.1
fw = 1.9

NoiseAmp = 0.0
NoiseWidth = 4.3

noise = np.random.normal(loc=NoiseAmp, scale=NoiseWidth, size=f.size)

spectrum = a + b*f + c*f*f + P*np.exp(-0.5*((f-fp)/fw)**2) + noise

unc = np.random.normal(loc=NoiseWidth, scale=0.2*NoiseWidth, size=f.size)

# Write to data file
fileout = open("Spectrum.txt", "w")
fileout.write("Data for absorption spectrum\n")
fileout.write("Date: 21-Nov-2011\n")
fileout.write("Data taken by Saitor and Chang\n")
fileout.write("frequency (THz) counts uncertainty\n")
for i in range(f.size):
    fileout.write("{0:5.2f} \t\t {1:5.0f} \t\t {2:2.1f} \n".format(f[i], spectrum[i], unc[i]))
fileout.close()

# Plot data
plt.figure(1)
plt.subplot(111)
plt.plot(f, spectrum, 'or')
plt.show()