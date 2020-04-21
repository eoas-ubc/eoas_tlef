import numpy
def makeMatrixs(points, vals, errs):

    npoints = len(points)
    if len(points.shape) == 1:
        nparams = 2
    else:
        nparams = points.shape[1] + 1

    A = numpy.ones( (npoints, nparams)  )
    if nparams == 2:
        for i in xrange(npoints):
            A[i,0] = points[i]
    else:
        A[:,:-1] = points

    b = vals
    if errs is not None:            
        for i in xrange(npoints):
            A[i,:] = A[i,:] / errs[i]
        b = b / errs
    return A, b
