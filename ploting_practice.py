import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
# plt.style.use('classic')

x = np.linspace(0, 10, 100)

fig, ax = plt.subplots()

ax.plot(x, np.sin(x - 0), c='blue')
ax.plot(x, np.sin(x - 1), c='g')
# ax[2].plot(x, np.sin(x - 2), c='.75')
# ax[3].plot(x, np.sin(x - 3), linestyle='-.')
# ax[4].plot(x, np.sin(x - 4), linestyle=':')
# ax[5].plot(x, np.sin(x - 3.5), ':k')
ax2 = ax.twinx()
#ax.set(xlim=(0, 10), ylim=(-2, 2), xlabel='x', ylabel='sin(x)', title='Sample sin(x)')

plt.show()
