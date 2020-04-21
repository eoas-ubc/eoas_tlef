import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3)  # makes 50 points by default, which is ok here
y = 3.0*x*x

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')

plt.show()