"""
Visualization of binned emissions data 
"""

import matplotlib.pyplot as plt
import numpy as np

(x, y) = np.loadtxt('data\emissions_binned.csv',
                 delimiter=",", dtype=float)

plt.plot(x,y,'r')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')
plt.savefig('graphs\emissions_merged.png')
