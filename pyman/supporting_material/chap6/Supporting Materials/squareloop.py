import numpy as np
a = np.linspace(0, 100, 1e7)
print(a)
for i in range(len(a)):
    a[i] = a[i]*a[i]
print(a)