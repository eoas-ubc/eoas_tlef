# Calculates time, gallons of gas used, and cost of gasoline for a trip

distance = float(raw_input("Input distance of trip in miles: "))
mpg = 30.               # car mileage
speed = 60.             # average speed
costPerGallon = 4.10    # price of gas

time = distance/speed
gallons = distance/mpg
cost = gallons*costPerGallon

print(time, gallons, cost)
