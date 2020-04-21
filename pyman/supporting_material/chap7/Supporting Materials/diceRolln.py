import numpy as np
import matplotlib.pyplot as plt

def dice(n):
    sum = 0
    for i in range(n):
        sum += np.random.random_integers(6)
    return sum
    
n = int(raw_input("How many dice do you want to roll & sum: "))

rolls = []
for i in range(100000):
    rolls.append(dice(n))
rolls = np.array(rolls)

plt.hist(rolls, 5*n+1)
plt.xlabel("sum of {0:d} dice".format(n))
plt.xlim(n, 6*n)
plt.show()
plt.savefig("diceRoll{0:s}.eps".format(str(n)))
