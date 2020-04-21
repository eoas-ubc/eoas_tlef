#!/bin/sh
# This code tests that your Python installation worked.
# It generates a png image file that you should e-mail 
# to the address shown on the plot
import scipy 
import numpy 
import matplotlib 
import matplotlib.pyplot as plt 
import platform 
import socket

# If you are a student, please fill in your first and last
# names inside the quotes in the two lines below.  Do not
# modify anything else in this file

your_first_name = 'Dana' 
your_last_name = 'Smith'

# If you are an instructor, modify the next 3 lines.
# You do not need to modify anything else in this file.

classname = 'Intro Exp Phys I'
term = 'Fall_2012'      # must contain no spaces
email = 'phys-ua71@physics.nyu.edu'

plt.plot([0,1], 'r', [1,0], 'b')
plt.text( 0.5, 0.9, '{0:s} {1:s}\n{2:s}\n{3:s}'
    .format(your_first_name, your_last_name, classname, term), 
    horizontalalignment='center', verticalalignment='top',
    size = 'x-large', bbox=dict(facecolor='purple', alpha=0.4))
plt.text( 0.5, 0.1,
    'scipy {0:s}\nnumpy {1:s}\nmatplotlib {2:s}\non {3:s}\n{4:s}'
        .format(scipy.__version__, numpy.__version__, 
        matplotlib.__version__, platform.platform(), 
        socket.gethostname() ) ,
    horizontalalignment='center', verticalalignment='bottom')
filename = your_last_name + '_' + your_first_name + '_' + \
     term + '.png'
plt.title('{0:s} "{1:s}"\n E-mail this file to "{2:s}"'
    .format('This plot has been saved on your computer as', 
    filename, email), fontsize=12)
plt.savefig(filename)
plt.show()
