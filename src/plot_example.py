# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np

# # Data for plotting
# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2 * np.pi * t)

# fig, ax = plt.subplots()
# ax.plot(t, s)

# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()

# fig.savefig("test.png")
# plt.show()

# #
# plt.savefig('books_read.png')

import sys
import typing
import matplotlib.pyplot as plt

# If there's a 1st arg, then store it as first_arg
first_arg: typing.Union[bool, str] = len(sys.argv) > 1 and sys.argv[1]

# Build your graph
plt.plot([0, 1, 2, 3, 4], [0, 3, 5, 9, 11])
plt.xlabel('Months')
plt.ylabel('Books Read')

# Output/display
if first_arg:
    print("Printing plot to file")
    plt.savefig('output.png', bbox_inches='tight')
else:
    print("Opening plot in GUI")
    plt.show()
