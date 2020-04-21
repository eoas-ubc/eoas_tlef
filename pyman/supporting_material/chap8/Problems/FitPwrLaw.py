# Routine FitPwrLaw
import numpy as np
import matplotlib.pyplot as plt

def LineFitWt(x, y, sig):
    """ 
    Returns slope and y-intercept of weighted linear fit to
    (x,y) data set.
    Inputs: x and y data array and uncertainty array (unc)
            for y data set.
    Outputs: slope and y-intercept of best fit to data and
             uncertainties of slope & y-intercept.
    """
    sig2 = sig**2
    norm = (1./sig2).sum()
    xhat = (x/sig2).sum() / norm
    yhat = (y/sig2).sum() / norm
    slope = ((x-xhat)*y/sig2).sum()/((x-xhat)*x/sig2).sum()
    yint = yhat - slope*xhat
    sig2_slope = 1./((x-xhat)*x/sig2).sum()
    sig2_yint = sig2_slope * (x*x/sig2).sum() / norm
    return slope, yint, np.sqrt(sig2_slope), np.sqrt(sig2_yint)

def redchisq(x, y, dy, slope, yint):
    chisq = (((y-yint-slope*x)/dy)**2).sum()
    return chisq/float(x.size-2)

# Read data from data file
t, r, dr = np.loadtxt("aggdata.txt", skiprows=4, unpack=True)

########## Code to tranform & fit data starts here ##########

# Transform data and parameters to linear form: Y = A + B*X
X = np.log(t) # transform N data for fitting
Y = np.log(r) # transform t data for fitting
dY = dr/r     # transform uncertainties for fitting

# Fit transformed data X, Y, dY to obtain fitting parameters
# A & B.  Also returns uncertainties dB & dA in A & B
A, B, dA, dB = LineFitWt(X, Y, dY)
# Return reduced chi-squared
redchisqr = redchisq(X, Y, dY, A, B)

# Determine fitting parameters for original exponential function
# N = N0 exp(-Gamma t) ...
p = A
K = np.exp(B)
# ... and their uncertainties
dp = dA
dK = np.exp(B)*dB

###### Code to plot transformed data and fit starts here ######

# Create line corresponding to fit using fitting parameters
# Only two points are needed to specify a straight line
Xext = 0.05*(X.max()-X.min())
Xfit = np.array([X.min()-Xext, X.max()+Xext])
Yfit = A*Xfit + B                   # generates Y from X data & 
                                    # fitting function
plt.errorbar(X, Y, dY, fmt="gs", ms=3)
plt.plot(Xfit, Yfit, "k-", zorder=-1)
plt.title(r"$\mathrm{Fit\ to:}\ \ln\,r = d\, \ln\,t + \ln\,r_0$ or $Y = AX+B$")
plt.xlabel(r'$\ln\,t$', fontsize=16)
plt.ylabel(r'$\ln\,r$', fontsize=16)

plt.text(-2.7, 8.2, u"A = d = {0:0.2f} \xb1 {1:0.2f}".format(A, dA))
plt.text(-2.7, 8.0, u"B = ln r_0 = {0:0.1f} \xb1 {1:0.1f}".format(B, dB))
plt.text(-2.7, 7.8, u"r_0 = {0:0.1e} \xb1 {1:0.1e}".format(K, dK))
plt.text(-2.7, 7.6, "$\chi_r^2$ = {0:0.3f}".format(redchisqr))

plt.show()
plt.savefig("FitSemiLogWtsErrBars.pdf")