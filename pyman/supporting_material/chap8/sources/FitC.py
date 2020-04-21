"""Function for fitting data to y = a + bx"""
import numpy as np

def fitlin(x, y, dy=1.0, errors=True, residuals=True):
    """
    fitlin(x, y, dy=1.0, errors=True, residuals=True)
    Use linear least squares method to find optimal values of a and b that fit
    the linear function f=a+bx to x,y data.
    
    Parameters
    ----------
    x : ndarray
        one dimensional array of x data with n>2 data points.
    y : ndarray
        one dimensional array of y data with n>2 data points.
    dy : ndarray or float
        one dimensional array of uncertainties (errors) in y data
        or a single positive number if all uncertainties are the same.
        Setting dy=1 is equivalent to using no weighting.
    errors : bool
        If True, return dfit and cov.
    residuals : bool
        If True, return redchisq and residuals
    
    Returns
    -------
    fit : (a,b) tuple of floats
        The best fit model parameters a (the y-intercept) and b (the slope) for
        the input data arrays x, y
          
    dfit : (da,db) tuple floats
        The estimated uncertainties da and db of the best fit model parameters
        a and b.  These are the square roots of the diagonal elements of the
        covariance matrix.
        [Calculated and returned only if errors==True]
        
    cov : float
        Covarience of the fitting parameters a and b.  This is the off diagonal
        element of the 2x2 symmetric covariance matrix.
        [Calculated and returned only if errors==True]
          
    redchisq : float
        Reduced value of chi-squared goodness of fit parameter 
        chisq = sum_i^n [(y_i-(a+bx_i)]^2/dy^2. redchisq = chisq/(n-2)
        where n is the number of data points in x or y.
        [Calculated and returned only if residuals==True]
        
    residuals : ndarray
        Length n array of the differences y-(a+bx) between y-data and the fitted
        data a+bx.
        [Calculated and returned only if residuals==True]

    Raises
    ------
    TypeError : if x and y have difference lengths
    TypeError : If x and y have 2 or fewer elements
    TypeError : If dy length is not 1 or the same as y
    
    Notes
    _____
    By default, fitlin returns optimal fitting paramenters a and b along with 
    estimates of their uncertainties da and db, the covariance, the reduced
    chi-squared value, and the residuals.  The returned value of reduced
    chi-squared should be near 1 for a good fit, provided valid estimeates of
    the uncertainties dy in the y data are given.  Set dy=1.0 if uncertainties
    are not known, in which case the returned value of reduced chi-squared
    is the variance of the data from the fit, which provides an empirical
    estimate of the experimental uncertainties.
    
    Setting one or both of the input parameters, errors or residuals, to False
    makes the program run faster.
    
    Examples
    --------
    Fit a line, "y = a + bx", through some noisy data-points:
    
    >>> x = np.array([0, 1, 2, 3])
    >>> y = np.array([-1, 0.2, 0.9, 2.1])
    >>> dy = np.array([0.18, 0.13, 0.15, 0.17])
    
    Fitting the x and y data without the dy array of uncertainties in y data
    
    >>> fit, dfit, cov, redchisq, residuals = fitlin(x, y)

    >>> print("a = {0:0.2f}\nb = {1:0.2f}".format(fit[0], fit[1]))
    a = -0.95
    b = 1.00
    
    When uncertainties dy are not unspecified, then the uncertainties da and db
    in the fitting paramters a and b are calculated using the standard
    deviation of the residuals, obtained from chi-squared, as estimates for dy.
    See section 8.4 of An Introduction to Error Analysis, 2nd Ed. by John R.
    Taylor (University Science Books, 1997). 
    
    >>> print("da = {0:0.2f}\ndb = {1:0.2f}".format(dfit[0], dfit[1]))
    da = 0.13
    db = 0.07
    
    When no estimate of the uncertainties is supplied the value returned
    for redchisq is calculated assuming dy=1.0.  In that case, np.sqrt(redchisq) 
    gives the standard deviation of residuals, which can be used as an
    estimate of the experimental errors and the uncertainties da and db in the
    fitting parameters.  In this case, redchisq cannot provide an independent
    estimate of the goodness of the fit.
    
    >>> print("Estimated uncertainties = {0:0.2f}".format(np.sqrt(redchisq)))
    Estimated uncertainties = 0.16
    
    The residuals give the differences between the y-data and the fitted values
    of the y-data
    
    >>> print(residuals)
    array([-0.05  0.15 -0.15  0.05])
    
    --------
    
    Fitting the x and y data using the dy array of uncertainties
    
    >>> fit, dfit, cov, redchisq, residuals = fitlin(x, y, dy)

    >>> print("a = {0:0.2f}\nb = {1:0.2f}".format(fit[0], fit[1]))
    a = -0.91
    b = 0.98
    
    Estimates of the uncertainties in the fitted values of a and b given by da
    and db when the dy array of uncertainties is supplied.
    
    >>> print("da = {0:0.2f}\ndb = {1:0.2f}".format(dfit[0], dfit[1]))
    da = 0.14
    db = 0.08
    
    When the array of uncertainties dy is supplied, redchisq gives the reduced
    value of the goodness-of-fit parameter chi-squared.  A redchisq value near
    1 indicates the fit is believable, provided the dy estimates are valid.
    
    >>> print(redchisq)
    1.20731129496665
    
    The covariance divided by the product of the uncertainties of the fitted
    parameters gives the coefficient of correlation r, a number between -1 and 1
    that tells whether errors in the fitting parameters a and b are likely to
    have the same sign (r>0) or opposite signs (r<0)
    
    >>> print(cov/(dfit[0]*dfit[1]))
    -0.827152541117
    
    The residuals give the differences between the y-data and the fitted values
    of the y-data
    
    >>> print(residuals)
    array([-0.08856653,  0.12781099, -0.1558115 ,  0.06056602])
    
    >>> import matplotlib.pyplot as plt
    >>> plt.errorbar(x, y, yerr=dy, fmt='o', label='data')
    >>> plt.plot(x, fit[0] + fit[1]*x, 'r', label='Fitted line')
    >>> plt.legend(loc="best")
    >>> plt.show()
    """

    x = np.asarray(x)
    y = np.asarray(y)
    dy = np.asarray(dy)
    if x.size != y.size:
        raise TypeError, "Expected x and y to have same length"
    if x.size <= 2:
        raise TypeError, "Expected x and y length > 2"

    if dy.size==1:
        s = y.size
        sx = x.sum()
        sy = y.sum()
        sxx = (x*x).sum()
        sxy = (x*y).sum()
    else:
        if dy.size != y.size:
            raise TypeError, "Expected dy size to be 1 or same as y"
        var = dy*dy
        s = (1./var).sum()
        sx = (x/var).sum()
        sy = (y/var).sum()
        sxx = (x*x/var).sum()
        sxy = (x*y/var).sum()
    norm = s*sxx-sx*sx
    yint = (sxx*sy-sx*sxy)/norm
    slope = (s*sxy-sx*sy)/norm
    returns = [np.array([yint, slope])]

    if errors==True:
        if dy.size != 1:
            delta_yint = np.sqrt(sxx/norm)
            delta_slope = np.sqrt(s/norm)
            cov = -sx/norm
        else:
            redchisq, resids = _resids(x, y, dy, yint, slope)
            delta_yint = np.sqrt(redchisq*sxx/norm)
            delta_slope = np.sqrt(redchisq*s/norm)
            cov = -redchisq*sx/norm
        returns += np.array([delta_yint, delta_slope]), cov

    if residuals==True:
        if dy.size != 1 or errors==False :
            redchisq, resids = _resids(x, y, dy, yint, slope)
        returns += redchisq, resids

    return returns

def _resids(x, y, dy, yint, slope):
        resids = y - (yint + slope*x)
        redchisq = ((resids/dy)**2).sum()/(x.size-2)
        return redchisq, resids

if __name__ == '__main__':
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib.gridspec as gridspec  # for unequal plot boxes

    # data set for linear fitting 
    x = np.array([2.3, 4.7, 7.1, 9.6, 11.7, 14.1, 16.4, 18.8, 21.1, 23.0])
    y = np.array([-25., 3., 114., 110., 234., 304., 271., 322., 446., 397.])
    dy = np.array([15., 30., 34., 37., 40., 50., 38., 28., 47., 30.])

    # Fit linear data set without weighting and print out results
    print("\nFit without weighting (no uncertainty estimates)")
    fit, dfit, cov, redchisq, residuals = fitlin(x, y)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))

    # Fit linear data set with weighting and print out results
    print("\nFit with weighting (with uncertainty estimates)")
    fit, dfit, cov, redchisq, residuals = fitlin(x, y, dy)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))
    
    # Open figure window for plotting data with linear fit
    fig1 = plt.figure(1, figsize=(8,8))
    gs = gridspec.GridSpec(2, 1, height_ratios=[2.5, 6])
    
    # Bottom plot: data and fit
    ax1 = fig1.add_subplot(gs[1])
    
    # Plot data with error bars on top of fit
    ax1.errorbar(x, y, yerr = dy, ecolor="black", fmt="ro", ms=4)
    
    # Plot fit (behind data)
    endt = 0.05 * (x.max()-x.min())
    tFit = np.array([x.min()-endt, x.max()+endt])
    vFit = fit[0] + fit[1]*tFit
    ax1.plot(tFit, vFit, '-b', zorder=-1)
    
    # Print out results of fit on plot
    ax1.text(0.05, 0.9,
        u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]),
        ha='left', va='center', transform = ax1.transAxes)
    ax1.text(0.05, 0.83,
        u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]),
        ha='left', va='center', transform = ax1.transAxes)
    ax1.text(0.05, 0.76,
        "redchisq = {0:0.2f}".format(redchisq),
        ha='left', va='center', transform = ax1.transAxes)
    ax1.text(0.05, 0.69,
        "r = {0:0.2f}".format(cov/(dfit[0]*dfit[1])),
        ha='left', va='center', transform = ax1.transAxes)
    
    # Label axes
    ax1.set_xlabel('time')
    ax1.set_ylabel('velocity')
    
    # Top plot: residuals
    ax2 = fig1.add_subplot(gs[0])
    ax2.axhline(color="gray")
    ax2.errorbar(x, residuals, yerr = dy, ecolor="black", fmt="ro", ms=4)
    ax2.set_ylabel('residuals')
    ax2.set_ylim(-100, 150)
    ax2.set_yticks((-100, 0, 100))
 
    plt.show()
    
    # data set for linear fitting using lists instead of NumPy arrays
    print("\n\nTesting with data lists instead of data arrays")
    x = [2.3, 4.7, 7.1, 9.6, 11.7, 14.1, 16.4, 18.8, 21.1, 23.0]
    y = [-25., 3., 114., 110., 234., 304., 271., 322., 446., 397.]
    dy = [15., 30., 34., 37., 40., 50., 38., 28., 47., 30.]
    
    # Fit linear data set without weighting and print out results
    print("\nFit without weighting (no uncertainty estimates)")
    fit, dfit, cov, redchisq, residuals = fitlin(x, y)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))

    # Fit linear data set with weighting and print out results
    print("\nFit with weighting (with uncertainty estimates)")
    fit, dfit, cov, redchisq, residuals = fitlin(x, y, dy)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))
