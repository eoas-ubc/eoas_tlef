# Solution to Exercise on zip
from numpy import array

a = array([1, 3, 5, 7])
b = array([8, 7, 5, 4])
c = array([0, 9,-6,-8])
d = zip(a,b,c)

print('\nd = {}'.format(d))     # d is a list of 4 3-element tuples

e = array(d)                    # e is an 3 x 4 NumPy array

print('\ne =\n{}'.format(e))

print('\ne[3,2] = {}'.format(e[3,2]))   # e[3,2] = -8

print('\nd[3][2] = {}'.format(e[3,2]))   # d[3][2] = -8