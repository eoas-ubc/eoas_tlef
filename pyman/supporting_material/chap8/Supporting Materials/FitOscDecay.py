import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec  # for unequal plot boxes
import scipy.optimize

# define function to calculate reduced chi-squared
def RedChiSqr(func, x, y, dy, params):
    resids = y - func(x, *params)
    chisq = ((resids/dy)**2).sum()
    return chisq/float(x.size-params.size)

# define fitting function
def SineGaussDecay(t, A, B, C, tau, omega):
    y = A * (1.0 + B*np.cos(omega*t)) * np.exp(-0.5*t*t/(tau*tau)) + C
    return y

# read in spectrum from data file
t, decay, unc = np.loadtxt("OscData.txt", skiprows=4, unpack=True)

# initial values for fitting parameters (guesses)
A0 = 15.0
B0 = 0.6
C0 = 1.2*A0
tau0 = 16.0
omega0 = 2.0 * (2.0*np.pi/tau0)
#omega0 = 2.34

# fit data using SciPy's Levenberg-Marquart method
nlfit, nlpcov = scipy.optimize.curve_fit(SineGaussDecay, 
             t, decay, p0=[A0, B0, C0, tau0, omega0], sigma=unc)

# calculate reduced chi-squared
rchi = RedChiSqr(SineGaussDecay, t, decay, unc, nlfit)

# create fitting function from fitted parameters
A, B, C, tau, omega = nlfit
t_fit = np.linspace(0.0, 1.02*t[-1], 512)
d_fit = SineGaussDecay(t_fit, A, B, C, tau, omega)

# Create figure window to plot data
fig = plt.figure(1, figsize=(8,8))      # extra length for residuals
gs = gridspec.GridSpec(2, 1, height_ratios=[6, 2])

# Top plot: data and fit
ax1 = fig.add_subplot(gs[0])
ax1.plot(t_fit, d_fit)
ax1.errorbar(t, decay, yerr=unc, fmt='or', ecolor='black', ms=4)
ax1.set_xlabel('time (ms)')
ax1.set_ylabel('decay (arb units)')
ax1.text(0.55, 0.8, 'A = {0:0.1f}\nB = {1:0.3f}\nC = {2:0.1f}'.format(A, B, C), 
        transform = ax1.transAxes)
ax1.text(0.75, 0.8, '$\\tau$ = {0:0.1f}\n$\omega$ = {1:0.3f}\n$\chi^2$ = {2:0.3f}'.format(tau, omega, rchi), 
        transform = ax1.transAxes)
ax1.set_title('$d(t) = A (1+B\,\cos\,\omega t) e^{-t^2/2\\tau^2} + C$')

# Bottom plot: residuals
resids = decay - SineGaussDecay(t, A, B, C, tau, omega)
ax2 = fig.add_subplot(gs[1])
ax2.axhline(color="gray")
ax2.errorbar(t, resids, yerr = unc, ecolor="black", fmt="ro", ms=4)
ax2.set_xlabel('time (ms)')
ax2.set_ylabel('residuals')
ax2.set_ylim(-5, 5)
yticks = (-5, 0, 5)
ax2.set_yticks(yticks)

plt.savefig('FitOscDecay.pdf')

plt.show()

