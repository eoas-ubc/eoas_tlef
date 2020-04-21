import numpy as np
import matplotlib.pyplot as plt

def LineFitWt(x, y, sig):
    """ 
    Returns slope and y-intercept of weighted linear fit to (x,y) data set.
    Inputs: x and y data array and uncertainty array (unc) for y data set.
    Ouputs: slope and y-intercept of best fit to data.
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
t, N, dN = np.loadtxt("betaDecay.txt", skiprows=2, unpack=True)

########## Code to tranform & fit data starts here ##########

# Transform data and parameters to linear form: Y = A + B*X
X = t           # transform t data for fitting (not necessary since X=t)
Y = np.log(N)   # transform N data for fitting
dY = dN/N       # transform uncertainties for fitting

# Fit transformed data X, Y, dY to obtain fitting parameters A & B
# Also returns uncertainties in A and B
B, A, dB, dA = LineFitWt(X, Y, dY)
# Return reduced chi-squared
redchisqr = redchisq(X, Y, dY, B, A)

# Determine fitting parameters for original exponential function
# N = N0 exp(-t/tau) ...
N0 = np.exp(A)
tau = -1.0/B
# ... and their uncertainties
dN0 = N0 * dA
dtau = tau**2 * dB

########## Code to plot transformed data and fit starts here ##########

# Create line corresponding to fit using fitting parameters
# Only two points are needed to specify a straight line
Xext = 0.05*(X.max()-X.min())
Xfit = np.array([X.min()-Xext, X.max()+Xext]) # smallest & largest X points
Yfit = A + B*Xfit                   # generates Y from X data & fitting function

plt.errorbar(X, Y, dY, fmt="bo")
plt.plot(Xfit, Yfit, "r-", zorder=-1)
plt.xlim(0, 100)
plt.ylim(1.5, 7)
plt.title("$\mathrm{Fit\\ to:}\\ \ln N = -t/\\tau + \ln N_0$")
plt.xlabel("t")
plt.ylabel("ln(N)")

plt.text(50, 6.6, "A = ln N0 = {0:0.2f} $\pm$ {1:0.2f}".format(A, dA))
plt.text(50, 6.3, "B = -1/tau = {0:0.4f} $\pm$ {1:0.4f}".format(-B, dB))
plt.text(50, 6.0, "$\chi_r^2$ = {0:0.3f}".format(redchisqr))

plt.text(50, 5.7, "N0 = {0:0.0f} $\pm$ {1:0.0f}".format(N0, dN0))
plt.text(50, 5.4, "tau = {0:0.1f} $\pm$ {1:0.1f} days".format(tau, dtau))

plt.savefig("betaDecay.pdf")
plt.show()