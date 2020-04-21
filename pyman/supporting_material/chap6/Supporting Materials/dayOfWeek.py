import numpy as np

daysInMonth = np.array([31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31])

year = int(raw_input("Which year 1900 or later? "))
month = int(raw_input("Which month (1-12)? "))
day = int(raw_input("Which day (1-{0:0d})? ".format(daysInMonth[month-1])))

days = (year-1900)*365 + daysInMonth[:month-1].sum() + day
for yr in range(1900, year):
    if yr%4 == 0:
        days += 1
        if yr%100 == 0:
            if yr%400 != 0:
                days -= 1
if year%4 == 0:
    if month <= 2:
        days -= 1
        if year%100 == 0:
            if year%400 != 0:
                days += 1

dayOfWeek = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
print(dayOfWeek[days%7])