"""Class for fitting data to y = a + bx"""
import numpy as np

class FitLin:

    def __init__(self, x, y, dy=0.0, errors=True):
        x = np.asarray(x)
        y = np.asarray(y)
        dy = np.asarray(dy)
        if x.size != y.size:
            raise TypeError, "expected x and y to have same length"
        if x.size <= 2:
            raise TypeError, "expected length > 2 for x and y"
        self.x = x
        self.y = y
        self.dy = dy
        if dy.size==1:
            self.s = y.size
            self.sx = x.sum()
            self.sy = y.sum()
            self.sxx = (x*x).sum()
            self.sxy = (x*y).sum()
        else:
            if dy.size != y.size:
                raise TypeError, "expected dy size to be 1 or same as y"
            var = dy*dy
            self.s = (1./var).sum()
            self.sx = (x/var).sum()
            self.sy = (y/var).sum()
            self.sxx = (x*x/var).sum()
            self.sxy = (x*y/var).sum()
        self.norm = self.s*self.sxx - self.sx*self.sx
        self.yint = (self.sxx*self.sy-self.sx*self.sxy)/self.norm
        self.slope = (self.s*self.sxy - self.sx*self.sy)/self.norm
        if errors==True and dy.size==1:
            if dy==0.0:
                self.var = ((self.y - self.yint - self.slope*self.x)**2).sum()/(self.y.size-2.0)
                self.dy = np.array([1.0])
            else:
                self.var = dy*dy
    
    def LinearFit(self):
        return self.yint, self.slope
        
    def DeltaFitParams(self):
        if self.dy.size != 1:
            delta_yint = np.sqrt(self.sxx / self.norm)
            delta_slope = np.sqrt(self.s / self.norm)
        else:
            try:
                delta_yint = np.sqrt(self.var * self.sxx / self.norm)
                delta_slope = np.sqrt(self.var * self.s / self.norm)
            except AttributeError:
                raise AttributeError, "expected errors=True to output parameter uncertainties"
        return delta_yint, delta_slope
    
    def Cov(self):
        if self.dy.size != 1:
            return -self.sx/self.norm
        else:
            return -self.var*self.sx/self.norm
            
    
    def Residuals(self):
        try:
            return self.residuals
        except AttributeError:
            self.residuals = self.y - (self.yint + self.slope*self.x)
            return self.residuals
        
    def RedChiSqr(self):
        try:
            chisq = ((self.residuals/self.dy)**2).sum()
        except AttributeError:
            self.residuals = self.y - (self.yint + self.slope*self.x)
            chisq = ((self.residuals/self.dy)**2).sum()
        return chisq/float(self.x.size-2)

def fitlin(x, y, dy=0.0):
    """
    fitlin(x, y, dy=1.0)
    Use linear least squares method to fit linear function f=a+bx to data
    
    Parameters
    ----------
    x  : one dimensional array of x data with n>2 data points
    y  : one dimensional array of y data with n>2 data points
    dy : one dimensional array of uncertainties (errors) in y data
         or a single positive number if all uncertainties are the same.
         Set equal to 0 if uncertainties not specified
    
    Returns
    -------
    fit : (a,b) tuple of the best fit model parameters a (the y-intercept) 
          and b (the slope) for the input data arrays x, y
    unc : (da,db) tuple of the estimated uncertainties (square root of the 
          variance) of the best fit model parameters a and b.
    redchisq : reduced value of chi-squared goodness of fit parameter
          chisq = sum_i^n [(y_i-(a+bx_i)]^2/dy^2. redchisq = chisq/(n-2) where
          n is the number of data points in x or y.
    cov : covarience of the fitting parameters a and b.
    residuals : ndarray of length n of the differences y-f between y-data and 
          the fitted data f
    
    Raises
    ------
    ArrayDiffError : If input arrays x and y have difference sizes
    ArraySizeError : If input arrays have 2 or fewer elements
    
    Examples
    --------
    Fit a line, "y = a + bx", through some noisy data-points:
    
    >>> x = np.array([0, 1, 2, 3])
    >>> y = np.array([-1, 0.2, 0.9, 2.1])
    >>> dy = np.array([0.18, 0.13, 0.15, 0.17])
    
    Fitting the x and y data without the dy array of uncertainties in y data
    
    >>> fit, dfit, redchisq, cov, residuals = fitlin(x, y)

    >>> print("a = {0:0.2f}\nb = {1:0.2f}".format(fit[0], fit[1]))
    a = -0.95
    b = 1.00
    
    If uncertainties dy are not unspecified, then the uncertainties da and db
    in the fitting paramters a and b are calculated using the standard
    deviation of the residuals as estimates for dy.  See section 8.4 of An
    Introduction to Error Analysis, 2nd Ed. by John R. Taylor (University
    Science Books, 1997). 
    
    >>> print("da = {0:0.2f}\ndb = {1:0.2f}".format(dfit[0], dfit[1]))
    da = 0.13
    db = 0.07
    
    When no estimate of the uncertainties is supplied the value returned
    for redchisq is calculated assuming dy=1.  In that case, np.sqrt(redchisq) 
    gives the standard deviation of residuals, which can be used as an
    estimate of the experimental errors.  In this case, redchisq cannot provide
    an independent estimate of the goodness of the fit.
    
    >>> print("Estimated uncertainties = {0:0.2f}".format(np.sqrt(redchisq)))
    Estimated uncertainties = 0.16
    
    The residuals give the differences between the y-data and the fitted values
    of the y-data
    
    >>> print(residuals)
    array([-0.05  0.15 -0.15  0.05])
    
    --------
    
    Fitting the x and y data _with_ the dy array of uncertainties in y data
    
    >>> fit, dfit, redchisq, cov, residuals = fitlin(x, y, dy)

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
    Fit = FitLin(x, y, dy)
    fit = Fit.LinearFit()
    unc = Fit.DeltaFitParams()
    redchisq = Fit.RedChiSqr()
    cov = Fit.Cov()
    resids = Fit.Residuals()
    return fit, unc, redchisq, cov, resids

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
    fit, dfit, redchisq, cov, residuals = fitlin(x, y)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))

    # Fit linear data set with weighting and print out results
    print("\nFit with weighting (with uncertainty estimates)")
    fit, dfit, redchisq, cov, residuals = fitlin(x, y, dy)
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
    fit, dfit, redchisq, cov, residuals = fitlin(x, y)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))

    # Fit linear data set with weighting and print out results
    print("\nFit with weighting (with uncertainty estimates)")
    fit, dfit, redchisq, cov, residuals = fitlin(x, y, dy)
    print(u"y-intercept = {0:0.1f} \xb1 {1:0.1f}".format(fit[0], dfit[0]))
    print(u"slope = {0:0.1f} \xb1 {1:0.1f}".format(fit[1], dfit[1]))
    print("reduced chi-squared = {0:0.2f}".format(redchisq))
    
    # data set for linear fitting using lists instead of NumPy arrays
    print("\n\nTesting unequally sized data sets")
    x = [2.3, 4.7, 7.1, 9.6, 11.7, 14.1, 16.4, 18.8, 21.1]
    y = [-25., 3., 114., 110., 234., 304., 271., 322., 446., 397.]
    dy = [15., 30., 34., 37., 40., 50., 38., 28., 47., 30.]
    fit, dfit, redchisq, cov, residuals = fitlin(x, y, dy)
    
    # data sets with only 2 elements
    print("\n\nTesting too small data sets")
    x = [2.3, 4.7]
    y = [-25., 3.]
    dy = [15., 30.]
    fit, dfit, redchisq, cov, residuals = fitlin(x, y, dy)
