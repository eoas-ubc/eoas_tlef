import numpy as np

dataPt, time, height, error = np.loadtxt("MyData.txt",
        skiprows=5 , unpack=True)

np.savetxt('MyDataOut.txt',
        zip(dataPt, time, height, error), fmt="%12.1f")

info = 'Data for falling mass experiment'
info += '\nDate: 16-Aug-2013'
info += '\nData taken by Lauren and John'
info += '\n\n   data point    time (sec) height (mm)  '
info += 'uncertainty (mm)'

np.savetxt('MyDataOutHeader.txt',
        zip(dataPt, time, height, error), header=info, fmt="%12.1f")


np.savetxt('MyDataOut.csv',
        zip(dataPt, time, height, error), fmt="%0.1f", 
        delimiter=",")
