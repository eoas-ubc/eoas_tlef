import numpy as np
import matplotlib.pyplot as plt

def smiley(r, x0=0., y0=0., smile=True, color="blue"):
    N=360
    theta = np.linspace(0., 2.*np.pi, N+1)
    cx, cy = r*np.cos(theta), r*np.sin(theta)
    x = x0 + cx
    y = y0 + cy
    # Draw face outline
    plt.plot(x,y, color=color)
    # Draw smile
    if smile==True:
        b, e = N*5/8, N*7/8
        plt.plot(x0+0.75*cx[b:e],y0+0.75*cy[b:e], color=color)
    # Draw frown
    else:
        b, e = N/8, 3*N/8
        plt.plot(x0+0.75*cx[b:e],y0+0.75*cy[b:e]-1.15*r, color=color)
    # Draw nose
    plt.plot(x0+0.05*cx, y0+0.05*cy-0.2*r, color=color)
    # Draw eyes
    plt.plot(x0+0.5*r+0.1*cx, y0+0.1*r+0.1*cy, color=color)
    plt.plot(x0-0.5*r+0.1*cx, y0+0.1*r+0.1*cy, color=color)
    if smile==True:
        return "Happy"
    else:
        return "Sad"

state = smiley(2)
print(state)
smiley(1, x0=2.5, y0=2.5, smile=False, color="green")
smiley(1, x0=-2.5, y0=-2.5, color="red")
plt.axes().set_aspect(1)
plt.show()
plt.savefig("smiley.eps")