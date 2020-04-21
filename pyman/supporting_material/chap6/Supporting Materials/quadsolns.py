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

print("Finished!")