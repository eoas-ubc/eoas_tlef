import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-15, 15, 200)  # makes 50 points by default, which is ok here
y = np.cos(x)/(1.+0.2*x*x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()