import numpy as np

def leapyear(year):
    if year%4 != 0:
        return False
    elif year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    else:
        return True

def leapyearcount(years):
    a = np.where(years%4==0, 1, 0)
    b = np.where(years%100==0, -1, 0)
    c = np.where(years%400==0, 1, 0)
    return np.sum(a+b+c)

def daysBtwnDates(startDate, endDate):
    syear = int(startDate[:4])
    eyear = int(endDate[:4])
    return syear, eyear

for year in [1899, 1900, 1901, 1923, 1924, 1925, 1999, 2000, 2001, 2008, 2009]:
    print("{0:d} is a leap year: {1}".format(year, leapyear(year)))

print(leapyearcount(np.arange(1899,1999)))

out = daysBtwnDates("2012-Sep-21", "2013-Jan-15")
print(out)