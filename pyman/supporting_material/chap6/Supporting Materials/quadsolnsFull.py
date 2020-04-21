import numpy as np

a = float(raw_input("What is the coefficients a? "))
b = float(raw_input("What is the coefficients b? "))
c = float(raw_input("What is the coefficients c? "))

d = b*b - 4.*a*c

if d >= 0.0:
    print("Solutions are real")
elif b == 0.0:
    print("Solutions are imaginary")
else:
    print("Solutions are complex")

a, b, c = a+0.j, b+0.j, c+0.j

dd = np.sqrt(b*b-4*a*c)
xp = (-b + dd)/a
xm = (-b - dd)/a

print(xm, xp)
