    import time

    npts = 1000
    a, b = 2.*np.random.rand(2)-1.
    x = np.random.rand(npts)
    y = a + b*x
    dy = (y.mean()/10.)*np.random.randn(npts)
    
    start = time.clock()
    fitnew = fitlin(x, y, dy, errors=False, residuals=False)
    tnew = time.clock() - start

    start = time.clock()
    A = np.vstack([x/dy, 1./dy]).T
    fitold = np.linalg.lstsq(A, y/dy)[0]
    told = time.clock() - start

    print("New fit = {0:7.4f} {1:7.4f} {2:10.7f}".format(fitnew[0], fitnew[1], tnew))
    print("Old fit = {0:7.4f} {1:7.4f} {2:10.7f}".format(fitold[1], fitold[0], told))

