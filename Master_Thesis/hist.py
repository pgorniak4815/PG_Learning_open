
import matplotlib.pyplot as plt
import numpy as np
import math

def FD_bins_n(x):
    """returns the number of histogram bins for x dataset according to the Freedman-Diacons rule"""
    median = np.median(x)

    Q1 = x[x<median]
    Q3 = x[x>median]

    q1 = np.median(Q1)
    q3 = np.median(Q3)

    iqr = q3 - q1

    #histogram bins width according Freedmen Diacons rule
    bin_width = 2 * iqr * (len(x) ** (-1/3))

    #calculating number of bins with rounding
    bins = round((x.max() - x.min()) / bin_width)

    return bins


def Rice_bins_n(x):
    """returns the number of histogram bins for x dataset according to the Riece rule"""
    n = len(x)
    bins = math.ceil(2*n**(1/3))

    return bins


#random dataset generation 
np.random.seed(2134)
x = np.random.normal(size=1000)

b1 = FD_bins_n(x)
b2 = Rice_bins_n(x)

#building a histogram from prepared data
plt.hist(x, bins=b1)

plt.ylabel("Counts")
plt.xlabel("Values")
plt.title("Histogram");

plt.show()