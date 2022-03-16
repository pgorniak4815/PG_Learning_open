import matplotlib as plt

import my_functions as mf


binned_emissions = mf.binning(emissions)
EM = binned_emissions.items()
EM = sorted(EM) 
x, y = zip(*EM)

plt.plot(x,y,'ro')
plt.yscale('log')
plt.savefig("graphs\mygraph.png")