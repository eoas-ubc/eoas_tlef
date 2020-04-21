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
plt.close('all')
your_first_name = 'Dana'
your_last_name = 'Martin'
print('here i am')
# If you are an instructor, modify the next 3 lines.
# You do not need to modify anything else in this file.

classname = 'Intro Phys I'
term = 'Fall_2014'      # must contain no spaces
email = 'hmwkemail@univX.edu'

plt.plot([0,1], 'r', [1,0], 'b')
plt.text( 0.5, 0.8, '{0:s} {1:s}'
        .format(your_first_name, your_last_name),
        horizontalalignment='center',
        size = 'x-large',
        bbox=dict(facecolor='purple', alpha=0.4))
plt.text( 0.5, 0.1,
    '{1:s}\nscipy {2:s}\nnumpy {3:s}\nmatplotlib {4:s}\non {5:s}\n{6:s}'
        .format(
        classname,
        term,
        scipy.__version__,
        numpy.__version__,
        matplotlib.__version__,
        platform.platform(),
        socket.gethostname()
        ) ,
    horizontalalignment='center'
    )
filename = your_last_name + '_' + your_first_name + '_' + term + '.png'
plt.title('*** E-mail the saved version of this plot, ***\n' +
    '"{0:s}" to {1:s}'.format(filename, email), fontsize=12)
plt.savefig(filename)
fig=plt.gcf()
ax=plt.gca()
plt.show()
