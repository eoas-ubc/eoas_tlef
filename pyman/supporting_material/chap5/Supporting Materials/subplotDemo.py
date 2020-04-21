import numpy as np
import matplotlib.pyplot as plt

theta = np.arange(0.01, 8., 0.04)
y = np.sqrt((8./theta)**2-1.)
ytan = np.tan(theta)
ytan = np.ma.masked_where(np.abs(ytan)>20., ytan)
ycot = 1./np.tan(theta)
ycot = np.ma.masked_where(np.abs(ycot)>20., ycot)

plt.figure(1)

plt.subplot(2, 1, 1)
plt.plot(theta, y)
plt.plot(theta, ytan)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=np.pi/2., color="gray", linestyle='--', zorder=-1)
plt.axvline(x=3.*np.pi/2., color="gray", linestyle='--', zorder=-1)
plt.axvline(x=5.*np.pi/2., color="gray", linestyle='--', zorder=-1)
plt.xlabel("theta")
plt.ylabel("tan(theta)")

plt.subplot(2, 1, 2)
plt.plot(theta, -y)
plt.plot(theta, ycot)
plt.ylim(-8, 8)
plt.axhline(color="gray", zorder=-1)
plt.axvline(x=np.pi, color="gray", linestyle='--', zorder=-1)
plt.axvline(x=2.*np.pi, color="gray", linestyle='--', zorder=-1)
plt.xlabel("theta")
plt.ylabel("cot(theta)")

plt.savefig('subplotDemo.pdf')

plt.show()