import matplotlib.pyplot as plt
import my_functions as mf
import numpy as np

emissions = np.loadtxt('data\emissions_times_power_law_core.csv',
                 delimiter=",", dtype=float)

binned_emissions = mf.binning(emissions,0.1)
EM = binned_emissions.items()
EM = sorted(EM) 
x, y = zip(*EM)

plt.plot(x,y,'r')
plt.yscale('log')
plt.xscale('log')
plt.ylabel('Int. [counts]')
plt.xlabel('time [ns]')
plt.savefig('graphs\emissions_pl_core.png')