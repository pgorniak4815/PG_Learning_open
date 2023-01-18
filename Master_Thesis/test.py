"""
Test of binning methods
"""
import matplotlib.pyplot as plt
import numpy as np

x = np.loadtxt('data\emissions.csv',
                 delimiter=",", dtype=float)

bin_size = 10

number_of_bins = round((x.max()-x.min())/bin_size) + 1

bins_edges = np.linspace(x.min(), x.max(), number_of_bins)

print(bins_edges)
print(len(bins_edges))

binned, edges = np.histogram(x, bins_edges)

print(binned)

plt.hist(binned, bins = bins_edges)
plt.xscale, kwargs)
plt.show()
