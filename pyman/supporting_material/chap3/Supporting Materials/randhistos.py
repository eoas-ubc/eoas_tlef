import numpy as np
import matplotlib.pyplot as plt

n=10000
normal = np.random.randn(n)
uniform = np.random.rand(n)

plt.figure(figsize=(8,5))
plt.hist(uniform, 10, normed=1, facecolor='blue', alpha=0.5)
plt.hist(normal, 50, normed=1, facecolor='green', alpha=0.5)
plt.xlabel('x')
plt.ylabel('P(x)')

plt.show()

plt.savefig('randhistos.pdf')