import matplotlib.pyplot as plt
import my_functions as mf
import numpy as np

emissions = np.loadtxt('Master_Thesis\data\emissions_times.csv',
                 delimiter=",", dtype=float)

binned_emissions = mf.binning(emissions)
EM = binned_emissions.items()
EM = sorted(EM) 
x, y = zip(*EM)

plt.plot(x,y,'ro')
plt.yscale('log')
plt.savefig('Master_Thesis\graphs\mygraph.png')