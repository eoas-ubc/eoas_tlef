# Chapter 6 Problem: Loops - while
# Calculates return on initial investestment compounded annually, monthly, and
# daily
p = float(raw_input("What is the principal? "))
ratePC = float(raw_input("What is the interest rate in percent? "))
rate = 0.01*ratePC
years = float(raw_input("How many years to invest? (fractional years ok) "))

yearsLeft = int(years)
valueY = p
comp = 1.0+rate
while yearsLeft > 0:
    valueY *= comp
    yearsLeft -= 1

m = 12.0
monthsLeft = int(m*years)
valueM = p
comp = 1.0+rate/m
while monthsLeft > 0:
    valueM *= 1.0+rate/m
    monthsLeft -= 1

d = 365.24
daysLeft = int(d*years)
valueD = p
comp = 1.0+rate/d
while daysLeft > 0:
    valueD *= comp
    daysLeft -= 1

print("\nValue of investment after {0:0.2f} years".format(years))
print("${0:5.2f} (annual)\n${1:5.2f} (monthly)\n${2:5.2f} (daily)"
      .format(valueY, valueM, valueD))